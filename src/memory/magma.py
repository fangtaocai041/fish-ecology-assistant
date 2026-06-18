"""
memory/magma.py — 四维正交图谱记忆 (MAGMA + NetworkX)

核心: 将每个记忆项在四个正交关系图上表示:
  语义图 (Semantic)   — 内容相似性
  时序图 (Temporal)   — 时间关联
  因果图 (Causal)     — 因果关系链
  实体图 (Entity)     — 实体间关系

双重后端:
  - Dict (内置) — 零依赖, 轻量快速
  - NetworkX (可选) — 高级图算法: PageRank/社区发现/最短路径/中心性

语义编码器:
  - CharacterNgramEncoder (内置) — 中文汉字 n-gram
  - HuggingFaceEncoder (可选) — sentence-transformers

移植自: MAGMA (arXiv 2601.03236 | FredJiang0324/MAGMA)
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Set, Tuple
from datetime import datetime
import hashlib
import math
import time
import uuid


# ═══════════════════════════════════════════════════════════════
# 语义编码器
# ═══════════════════════════════════════════════════════════════

def _char_ngrams(text: str, n: int = 2) -> Set[str]:
    clean = ''.join(c for c in text if c.isalpha() or c.isdigit())
    return {clean[i:i+n] for i in range(len(clean) - n + 1)}


def _jaccard(a: Set, b: Set) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / max(len(a | b), 1)


class CharacterNgramEncoder:
    """字符 n-gram 语义编码器 (零依赖)。"""
    def __init__(self, n: int = 2):
        self.n = n
        self.name = "char_ngram"

    def encode(self, text: str) -> Set[str]:
        return _char_ngrams(text, self.n)

    def similarity(self, a: str, b: str) -> float:
        ngrams_a = self.encode(a)
        ngrams_b = self.encode(b)
        bigram_sim = _jaccard(ngrams_a, ngrams_b)
        tri_a = _char_ngrams(a, 3)
        tri_b = _char_ngrams(b, 3)
        trigram_sim = _jaccard(tri_a, tri_b)
        return bigram_sim * 0.6 + trigram_sim * 0.4


class HuggingFaceEncoder:
    """sentence-transformers 编码器 (可选)。"""
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.name = f"huggingface/{model_name}"
        self._model = None
        self._model_name = model_name

    def _lazy_load(self):
        if self._model is not None:
            return
        try:
            from sentence_transformers import SentenceTransformer
            self._model = SentenceTransformer(self._model_name)
        except ImportError:
            raise ImportError("pip install sentence-transformers")

    def similarity(self, a: str, b: str) -> float:
        self._lazy_load()
        emb_a = self._model.encode(a)
        emb_b = self._model.encode(b)
        dot = sum(x * y for x, y in zip(emb_a, emb_b))
        norm_a = math.sqrt(sum(x * x for x in emb_a))
        norm_b = math.sqrt(sum(x * x for x in emb_b))
        return dot / max(norm_a * norm_b, 1e-8)


def create_encoder(backend: str = "char_ngram", **kwargs) -> Any:
    if backend == "huggingface":
        return HuggingFaceEncoder(**kwargs)
    return CharacterNgramEncoder(**kwargs)


# ═══════════════════════════════════════════════════════════════
# 图数据结构
# ═══════════════════════════════════════════════════════════════

class RelationType:
    TEMPORAL = "temporal"
    SEMANTIC = "semantic"
    CAUSAL = "causal"
    ENTITY = "entity"


@dataclass
class MemoryNode:
    node_id: str = ""
    content: str = ""
    summary: str = ""
    entities: List[str] = field(default_factory=list)
    timestamp: float = 0.0
    importance: float = 0.5
    access_count: int = 0
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        if not self.node_id:
            self.node_id = uuid.uuid4().hex[:12]
        if not self.timestamp:
            self.timestamp = time.time()
        if not self.summary:
            self.summary = self.content[:80]

    @property
    def age_hours(self) -> float:
        return (time.time() - self.timestamp) / 3600


@dataclass
class Relation:
    source_id: str
    target_id: str
    rel_type: str
    weight: float = 1.0
    label: str = ""


# ═══════════════════════════════════════════════════════════════
# NetworkX 图后端 (增强版)
# ═══════════════════════════════════════════════════════════════

class NetworkXGraphDB:
    """NetworkX 图数据库后端。

    提供 Dict 后端无法实现的高级图分析:
      - PageRank: 节点重要性排名
      - 社区发现: 自动识别物种/文献群组
      - 最短路径: 概念间最短关联路径
      - 中心性: 关键节点识别

    对渔业资源研究的意义:
      - 物种关联网络: 同一栖息地的物种自动聚类
      - 文献引用网络: PageRank 识别核心文献
      - 生态网络: 捕食/竞争/共生关系建模

    用法:
        db = NetworkXGraphDB()
        db.add_node("鳤", {"type": "species"})
        db.add_edge("鳤", "长江", "habitat", 0.9)
        db.page_rank()  # 计算节点重要性
    """

    def __init__(self):
        try:
            import networkx as nx
            self.nx = nx
        except ImportError:
            raise ImportError("networkx not installed. Run: pip install networkx")
        self._g = nx.MultiDiGraph()
        self._rel_types: Dict[str, str] = {}  # {(u,v,key): rel_type}

    @property
    def node_count(self) -> int:
        return self._g.number_of_nodes()

    @property
    def edge_count(self) -> int:
        return self._g.number_of_edges()

    def add_node(self, node_id: str, **attrs):
        self._g.add_node(node_id, **attrs)

    def add_edge(self, u: str, v: str, rel_type: str = "", weight: float = 1.0,
                 label: str = ""):
        key = self._g.add_edge(u, v, weight=weight, label=label)
        self._rel_types[(u, v, key)] = rel_type

    def has_node(self, node_id: str) -> bool:
        return self._g.has_node(node_id)

    def get_edges(self, node_id: str) -> List[Tuple[str, str, float, str]]:
        """获取节点的所有邻接边。"""
        result = []
        for u, v, data in self._g.edges(node_id, data=True):
            result.append((u, v, data.get("weight", 1.0), data.get("label", "")))
        return result

    # ── 高级图分析 (核心价值) ──

    def page_rank(self, top_k: int = 10) -> List[Tuple[str, float]]:
        """PageRank 节点重要性排名。

        在文献网络中: 高 PageRank = 核心文献
        在物种网络中: 高 PageRank = 关键物种
        """
        if self.node_count == 0:
            return []
        try:
            pr = self.nx.pagerank(self._g, weight="weight")
            return sorted(pr.items(), key=lambda x: -x[1])[:top_k]
        except self.nx.PowerIterationFailedConvergence:
            return []

    def community_detection(self) -> List[Set[str]]:
        """社区发现 — 自动识别节点群组。

        在物种-栖息地网络中:
          同一社区 = 共享栖息地或食性关联的物种群
        """
        if self.node_count < 2:
            return [set(self._g.nodes)]
        try:
            from networkx.algorithms.community import greedy_modularity_communities
            return [set(c) for c in greedy_modularity_communities(self._g.to_undirected())]
        except Exception:
            return [set(self._g.nodes)]

    def shortest_path(self, source: str, target: str) -> Optional[List[str]]:
        """最短路径 — 概念间最短关联路径。

        例如: "鳤" → "长江" → "珍稀鱼类" → "保护等级"
        """
        try:
            return self.nx.shortest_path(self._g.to_undirected(), source=source, target=target)
        except (self.nx.NetworkXNoPath, self.nx.NodeNotFound):
            return None

    def centrality(self, top_k: int = 10) -> List[Tuple[str, float]]:
        """介数中心性 — 桥梁节点识别。

        高介数 = 连接不同知识社区的桥梁节点。
        """
        if self.node_count < 2:
            return []
        try:
            cb = self.nx.betweenness_centrality(self._g.to_undirected(), weight="weight")
            return sorted(cb.items(), key=lambda x: -x[1])[:top_k]
        except Exception:
            return []

    def density(self) -> float:
        """图密度 — 网络连接紧密程度。"""
        try:
            return self.nx.density(self._g)
        except Exception:
            return 0.0

    def subgraph(self, nodes: Set[str]) -> "NetworkXGraphDB":
        """提取子图。"""
        sub = NetworkXGraphDB()
        sub._g = self._g.subgraph(nodes).copy()
        return sub

    def to_dict_edges(self) -> Dict[str, List[dict]]:
        """导出边数据为 Dict 格式 (与 MagmaMemory._graphs 兼容)。"""
        edges: Dict[str, List[dict]] = {}
        for u, v, k, data in self._g.edges(data=True, keys=True):
            rt = self._rel_types.get((u, v, k), "semantic")
            edges.setdefault(rt, []).append({
                "source": u, "target": v,
                "weight": data.get("weight", 1.0),
                "label": data.get("label", ""),
            })
        return edges

    def report(self) -> dict:
        """图分析报告。"""
        return {
            "nodes": self.node_count,
            "edges": self.edge_count,
            "density": round(self.density(), 4),
            "page_rank_top": self.page_rank(5),
            "communities": len(self.community_detection()),
            "centrality_top": self.centrality(5),
        }


# ═══════════════════════════════════════════════════════════════
# 四维图谱记忆 (主类)
# ═══════════════════════════════════════════════════════════════

class MagmaMemory:
    """四维正交图谱记忆 — 支持 Dict/NetworkX 双后端。

    Dict 后端: 零依赖, 默认, 轻量
    NetworkX 后端: 启用 nx_backend=True, 获得 PageRank/社区发现/最短路径

    用法:
        # 零依赖模式
        mem = MagmaMemory()

        # NetworkX 增强模式
        mem = MagmaMemory(nx_backend=True)
        mem.page_rank()     # 节点重要性
        mem.communities()   # 自动社区发现
        mem.shortest_path("鳤", "保护等级")  # 概念路径
    """

    def __init__(self, encoder_backend: str = "char_ngram",
                 nx_backend: bool = False, **encoder_kwargs):
        self.name = "magma"
        self._nodes: Dict[str, MemoryNode] = {}
        self._graphs: Dict[str, Dict[str, List[Relation]]] = {
            RelationType.TEMPORAL: {},
            RelationType.SEMANTIC: {},
            RelationType.CAUSAL: {},
            RelationType.ENTITY: {},
        }
        self._encoder = create_encoder(encoder_backend, **encoder_kwargs)
        self._encoder_name = encoder_backend
        self._nx = NetworkXGraphDB() if nx_backend else None

    # ── 写入 ──

    def add(self, content: str, entities: Optional[List[str]] = None,
            importance: float = 0.5, metadata: Optional[Dict] = None) -> MemoryNode:
        node = MemoryNode(
            content=content,
            entities=entities or self._extract_entities(content),
            importance=importance,
            metadata=metadata or {},
        )
        self._nodes[node.node_id] = node
        if self._nx:
            self._nx.add_node(node.node_id, content=content[:50], entities=entities or [])

        for existing in self._nodes.values():
            if existing.node_id == node.node_id:
                continue
            semantic_score = self._calc_semantic(node, existing)
            if semantic_score > 0.25:
                self._relate(node.node_id, existing.node_id,
                            RelationType.SEMANTIC, semantic_score)
            entity_overlap = set(node.entities) & set(existing.entities)
            if entity_overlap:
                union_size = len(set(node.entities) | set(existing.entities))
                self._relate(node.node_id, existing.node_id,
                            RelationType.ENTITY,
                            len(entity_overlap) / max(union_size, 1))
            time_diff = abs(node.timestamp - existing.timestamp)
            if time_diff < 3600:
                tw = 1.0 - (time_diff / 3600)
                self._relate(node.node_id, existing.node_id,
                            RelationType.TEMPORAL, tw, "concurrent" if time_diff < 300 else "precedes")
        return node

    def relate(self, source_id: str, target_id: str, rel_type: str = RelationType.CAUSAL,
               weight: float = 1.0, label: str = ""):
        self._relate(source_id, target_id, rel_type, weight, label)

    def _relate(self, source_id: str, target_id: str, rel_type: str, weight: float, label: str = ""):
        if source_id not in self._nodes or target_id not in self._nodes:
            return
        rel = Relation(source_id, target_id, rel_type, weight, label)
        self._graphs[rel_type].setdefault(source_id, []).append(rel)
        if self._nx:
            self._nx.add_edge(source_id, target_id, rel_type, weight, label)

    # ── 检索 ──

    def search(self, query: str, top_k: int = 10) -> List[MemoryNode]:
        if not self._nodes:
            return []
        query_entities = self._extract_entities(query)
        scored: Dict[str, float] = {}
        for nid, node in self._nodes.items():
            score = 0.0
            if query_entities and node.entities:
                overlap = len(set(query_entities) & set(node.entities))
                score += overlap * 0.3
            semantic = self._encoder.similarity(query, node.content)
            score += semantic * 0.3
            q_lower = query.lower()
            if q_lower in node.content.lower():
                score += 0.2
            score *= node.importance
            if score > 0:
                scored[nid] = score

        if not scored:
            return []

        top_anchors = sorted(scored, key=scored.get, reverse=True)[:3]
        visited: Set[str] = set()
        results: Dict[str, float] = {}
        for anchor_id in top_anchors:
            self._traverse(anchor_id, visited, results, 0, 2)

        sorted_ids = sorted(results, key=results.get, reverse=True)[:top_k]
        return [self._nodes[nid] for nid in sorted_ids if nid in self._nodes]

    def _traverse(self, node_id: str, visited: Set[str],
                  results: Dict[str, float], depth: int, max_depth: int):
        if depth > max_depth or node_id in visited:
            return
        visited.add(node_id)
        decay = 0.7 ** depth
        results[node_id] = results.get(node_id, 0) + decay
        for rel_type in (RelationType.TEMPORAL, RelationType.SEMANTIC,
                         RelationType.CAUSAL, RelationType.ENTITY):
            relations = self._graphs[rel_type].get(node_id, [])
            for rel in relations:
                next_id = rel.target_id
                if next_id not in visited:
                    results[next_id] = results.get(next_id, 0) + decay * rel.weight
                    self._traverse(next_id, visited, results, depth + 1, max_depth)

    # ── NetworkX 高级分析 ──

    @property
    def nx(self) -> Optional[NetworkXGraphDB]:
        return self._nx

    def page_rank(self, top_k: int = 10) -> List[Tuple[str, float]]:
        """PageRank 节点重要性排名。需要 nx_backend=True。"""
        if not self._nx:
            return []
        return self._nx.page_rank(top_k)

    def communities(self) -> List[Set[str]]:
        """社区发现。需要 nx_backend=True。"""
        if not self._nx:
            return []
        comms = self._nx.community_detection()
        # 将 node_id 映射为内容摘要
        named = []
        for c in comms:
            names = set()
            for nid in c:
                if nid in self._nodes:
                    names.add(self._nodes[nid].summary[:30])
                else:
                    names.add(nid[:8])
            named.append(names)
        return named

    def shortest_path(self, source_query: str, target_query: str) -> Optional[List[str]]:
        """最短概念路径。需要 nx_backend=True。

        例: mem.shortest_path("鳤", "保护等级")
          → ["鳤", "珍稀鱼类", "保护等级"]
        """
        if not self._nx:
            return None
        src_id = self._find_node_id(source_query)
        tgt_id = self._find_node_id(target_query)
        if not src_id or not tgt_id:
            return None
        path = self._nx.shortest_path(src_id, tgt_id)
        if path is None:
            return None
        return [self._nodes.get(nid, MemoryNode()).summary for nid in path]

    def centrality(self, top_k: int = 10) -> List[Tuple[str, float]]:
        """介数中心性。需要 nx_backend=True。"""
        if not self._nx:
            return []
        return self._nx.centrality(top_k)

    def graph_report(self) -> dict:
        """完整图分析报告。"""
        if not self._nx:
            return {"status": "NetworkX not enabled (use nx_backend=True)"}
        return self._nx.report()

    def _find_node_id(self, query: str) -> Optional[str]:
        q = query.lower()
        for nid, node in self._nodes.items():
            if q in node.content.lower() or q in node.summary.lower():
                return nid
        return None

    # ── 辅助 ──

    def _extract_entities(self, text: str) -> List[str]:
        words = text.split()
        entities = []
        for w in words:
            clean = w.strip("，。！？、""''（）()《》【】[]·,").strip()
            if len(clean) >= 2:
                if clean[0].isupper() or any(c.isalpha() for c in clean):
                    entities.append(clean)
        return entities

    def _calc_semantic(self, a: MemoryNode, b: MemoryNode) -> float:
        return self._encoder.similarity(a.content, b.content)

    # ── 统计 ──

    @property
    def node_count(self) -> int:
        return len(self._nodes)

    @property
    def edge_count(self) -> int:
        return sum(len(edges) for g in self._graphs.values() for edges in g.values())

    def stats(self) -> dict:
        s = {
            "nodes": self.node_count,
            "edges": self.edge_count,
            "encoder": self._encoder_name,
            "nx_enabled": self._nx is not None,
            "graphs": {rt: sum(len(es) for es in g.values())
                      for rt, g in self._graphs.items()},
        }
        if self._nx:
            s["nx_analysis"] = {
                "density": self._nx.density(),
                "communities": len(self._nx.community_detection()),
            }
        return s

    def report(self) -> dict:
        return {"status": "ok", "stats": self.stats()}
