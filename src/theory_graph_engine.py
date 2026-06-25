#!/usr/bin/env python3
"""
MAGMA 四维理论图谱引擎 — 可执行底层
=========================================
f项目核心模块。加载 theory_tree_graph.json → NetworkX 图
提供: 专家路由 · 转座检测 · 适应度评分 · 拓扑矩阵 · 反事实推演

用法:
    from theory_graph_engine import TheoryGraph
    tg = TheoryGraph()
    tg.route("禁渔后鱼类多样性如何变化")  # → [IDH, 替代稳态, 同质化]
    tg.transposon_detect("IDH", "grassland")  # → 草地放牧理论
    tg.fitness_score("IDH")  # → 0.87
    tg.counterfactual("如果1990年开始禁渔...")
"""

import json
import math
import os
from pathlib import Path
from collections import defaultdict

# ── 图加载 ──────────────────────────────

class TheoryGraph:
    """四维理论图谱: X域-Y时间-Z深度-W涌现"""

    def __init__(self, graph_path=None):
        if graph_path is None:
            base = Path(__file__).resolve().parent.parent
            candidates = [
                base / "config" / "knowledge_base" / "ecological_theories" / "_topology" / "theory_tree_graph.json",
                base / "config" / "knowledge_base" / "ecological_theories" / "_拓扑结构" / "理论树图数据.json",
                Path("config/knowledge_base/ecological_theories/_topology/theory_tree_graph.json"),
                Path("config/knowledge_base/ecological_theories/_拓扑结构/理论树图数据.json"),
            ]
            graph_path = None
            for p in candidates:
                if p.exists():
                    graph_path = p
                    break
            if graph_path is None:
                raise FileNotFoundError(
                    "理论图谱数据文件未找到。请确认 config/knowledge_base/ecological_theories/"
                    "_拓扑结构/理论树图数据.json 或 _topology/theory_tree_graph.json 存在"
                )
        
        # 加载 JSON (支持注释行)
        with open(graph_path, 'r', encoding='utf-8') as f:
            raw = f.read()
        # 去掉 // 和 # 注释行
        import re
        raw = re.sub(r'^\s*//.*$', '', raw, flags=re.MULTILINE)
        raw = re.sub(r'^\s*#.*$', '', raw, flags=re.MULTILINE)
        self.data = json.loads(raw)
        
        self.nodes = {n['id']: n for n in self.data['nodes']}
        self.edges = self.data['edges']
        self.emergence_zones = self.data.get('emergence_zones', [])
        
        # 构建邻接表 (edges 是 [{'source':..,'target':..}] 格式)
        self.adj = defaultdict(set)
        for e in self.edges:
            s, t = e['source'], e['target']
            self.adj[s].add(t)
            self.adj[t].add(s)
        
        # 维度定义
        self.domains = self.data['dimension_definitions']['domain']
        self.layers = self.data['dimension_definitions']['layer']
        
        # ── 12 拓扑矩阵 ──
        self._build_topology_matrix()
        
        # ── 6 专家路由权重 ──
        self._init_experts()
        
        # ── 适应度评分缓存 ──
        self._fitness_cache = {}

    # ── 拓扑矩阵 (15×15) ──────────────────

    def _build_topology_matrix(self):
        """构建域间连接矩阵"""
        domain_ids = list(self.domains.keys())
        n = len(domain_ids)
        self.domain_index = {d: i for i, d in enumerate(domain_ids)}
        self.topology_matrix = [[0]*n for _ in range(n)]
        
        for e in self.edges:
            s, t = e['source'], e['target']
            if s not in self.nodes or t not in self.nodes: continue
            sd, td = self.nodes[s]['domain'], self.nodes[t]['domain']
            if sd in self.domain_index and td in self.domain_index:
                si, ti = self.domain_index[sd], self.domain_index[td]
                self.topology_matrix[si][ti] += 1
                self.topology_matrix[ti][si] += 1

    def topology_heatmap(self):
        """返回域间连接热力数据"""
        domain_ids = list(self.domains.keys())
        result = []
        for i, d1 in enumerate(domain_ids):
            for j, d2 in enumerate(domain_ids):
                if i < j and self.topology_matrix[i][j] > 0:
                    result.append({
                        'source': self.domains[d1]['label'],
                        'target': self.domains[d2]['label'],
                        'weight': self.topology_matrix[i][j]
                    })
        return sorted(result, key=lambda x: -x['weight'])

    def find_neighbors(self, domain_id):
        """邻居发现: 哪个域和该域连接最密"""
        if domain_id not in self.domain_index: return []
        idx = self.domain_index[domain_id]
        row = self.topology_matrix[idx]
        neighbors = []
        for i, w in enumerate(row):
            if i != idx and w > 0:
                domain_ids = list(self.domains.keys())
                neighbors.append((self.domains[domain_ids[i]]['label'], w))
        return sorted(neighbors, key=lambda x: -x[1])

    # ── 6 专家路由 ────────────────────────

    def _init_experts(self):
        """初始化 6 个领域专家，每个有理论关键词"""
        self.experts = {
            'disturbance': {
                'label': '干扰生态学',
                'theories': ['THEORY-IDH', 'THEORY-SUCCESSION', 'THEORY-ALTERNATIVE', 'THEORY-LEGACY'],
                'keywords': ['干扰', 'disturbance', '恢复', 'recovery', '演替', '禁渔',
                           '禁捕', 'fishing ban', '多样性', 'diversity', '群落', 'community']
            },
            'invasion': {
                'label': '入侵生物学',
                'theories': ['THEORY-HOMOG', 'THEORY-INVASION', 'THEORY-DILUTION'],
                'keywords': ['外来', 'exotic', '入侵', 'invasion', '同质化', 'homogenization',
                           '非土著', 'non-native', '扩散', 'spread']
            },
            'evolution': {
                'label': '进化生态学',
                'theories': ['FISHEVO', 'ECOEVO', 'EVOLUTION', 'RK', 'CONSGEN'],
                'keywords': ['进化', 'evolution', '选择', 'selection', '体型', 'body size',
                           '遗传', 'genetic', '基因', 'gene', '适应', 'adaptation']
            },
            'functional': {
                'label': '功能生态学',
                'theories': ['FUNCDIV', 'BEF', 'STOICH', 'KEYSTONE'],
                'keywords': ['功能', 'functional', '性状', 'trait', 'BEF', '多样性',
                           'ecosystem function', '生态系统功能', '营养', 'trophic']
            },
            'conservation': {
                'label': '保护生物学',
                'theories': ['CONSGEN', 'PVA', 'METAPOP', 'REWILDING', 'ALLEE', 'MPA'],
                'keywords': ['保护', 'conservation', '濒危', 'endangered', '灭绝', 'extinction',
                           '江豚', 'porpoise', '鲸类', 'cetacean', '保护区', 'protected']
            },
            'freshwater': {
                'label': '淡水生态学',
                'theories': ['RCC', 'FPC', 'ENVFLOW', 'METACOMM', 'WETLAND', 'DAMREM'],
                'keywords': ['河流', 'river', '流域', 'watershed', '洪水', 'flood',
                           '连通', 'connectivity', '长江', 'Yangtze', '大坝', 'dam']
            }
        }

    def route(self, question):
        """MoE 知识路由: 问题 → 激活 Top-2 专家 → 推荐理论"""
        ql = question.lower()
        scores = {}
        for exp_id, exp in self.experts.items():
            score = sum(1 for kw in exp['keywords'] if kw.lower() in ql)
            scores[exp_id] = score
        
        ranked = sorted(scores.items(), key=lambda x: -x[1])
        active = [(eid, s) for eid, s in ranked[:2] if s > 0]
        
        if not active:
            # 无关键词命中 → 返回所有理论
            active = [(eid, 0) for eid in list(self.experts.keys())[:2]]
        
        result = {'question': question, 'activated_experts': [], 'recommended_theories': []}
        for exp_id, score in active:
            exp = self.experts[exp_id]
            result['activated_experts'].append({
                'id': exp_id,
                'label': exp['label'],
                'score': score,
                'theories': [{'id': tid, 'name': self.nodes.get(tid,{}).get('label',tid)} for tid in exp['theories'] if tid in self.nodes]
            })
            result['recommended_theories'].extend(exp['theories'])
        
        return result

    # ── 亲缘传播 ──────────────────────────

    def kinship_propagate(self, theory_id, depth=2, decay=0.5):
        """从理论节点出发，沿边传播激活权重"""
        tid = self._resolve_id(theory_id)
        activated = {tid: 1.0}
        current = {tid}
        
        for d in range(depth):
            next_wave = set()
            weight = decay ** (d + 1)
            for tid in current:
                for neighbor in self.adj.get(tid, set()):
                    if neighbor not in activated:
                        activated[neighbor] = weight
                        next_wave.add(neighbor)
                    else:
                        activated[neighbor] = max(activated[neighbor], weight)
            current = next_wave
        
        return sorted(
            [{'id': tid, 'name': self.nodes.get(tid,{}).get('label',tid), 'weight': w}
             for tid, w in activated.items()],
            key=lambda x: -x['weight']
        )

    # ── 概念转座检测 ──────────────────────

    def transposon_detect(self, source_theory_id, target_domain=None, threshold=0.3):
        """检测某个理论能否'转座'到另一个域"""
        sid = self._resolve_id(source_theory_id)
        if sid not in self.nodes:
            return []
        
        source = self.nodes[sid]
        source_terms = self._extract_terms(source)
        
        candidates = []
        for tid, node in self.nodes.items():
            if tid == sid: continue
            if target_domain and node['domain'] != target_domain: continue
            if node['domain'] == source['domain']: continue  # 同域不转座
            
            target_terms = self._extract_terms(node)
            similarity = self._jaccard(source_terms, target_terms)
            
            if similarity > threshold:
                candidates.append({
                    'id': tid,
                    'name': node['label'],
                    'domain': self.domains.get(node['domain'], {}).get('label', node['domain']),
                    'similarity': round(similarity, 3),
                    'shared_terms': list(source_terms & target_terms)[:5]
                })
        
        return sorted(candidates, key=lambda x: -x['similarity'])

    def _resolve_id(self, short_id):
        """智能解析节点ID: 自动加 THEORY-/DATA- 前缀"""
        if short_id in self.nodes:
            return short_id
        for prefix in ['THEORY-', 'DATA-', 'MATH-']:
            if prefix + short_id in self.nodes:
                return prefix + short_id
        return short_id  # 返回原始值，后续会报 KeyError

    def _extract_terms(self, node):
        """从理论节点提取特征词"""
        text = f"{node['label']} {node.get('founder','')} {node.get('key_paper','')}"
        terms = set()
        for word in text.lower().replace('-',' ').replace('·',' ').split():
            word = word.strip('()[]{}:,.')
            if len(word) > 2:
                terms.add(word)
        return terms

    def _jaccard(self, set_a, set_b):
        if not set_a or not set_b: return 0
        return len(set_a & set_b) / len(set_a | set_b)

    # ── 理论适应度评分 ────────────────────

    def fitness_score(self, theory_id):
        """计算理论节点的适应度"""
        tid = self._resolve_id(theory_id)
        if tid in self._fitness_cache:
            return self._fitness_cache[tid]
        
        if tid not in self.nodes:
            return 0.0
        
        node = self.nodes[tid]
        degree = len(self.adj.get(tid, set()))
        max_degree = max(len(self.adj.get(nid, set())) for nid in self.nodes) or 1
        
        in_degree = sum(1 for e in self.edges if e['target'] == tid)
        
        own_domain = node['domain']
        cross_domain_edges = sum(
            1 for nid in self.adj.get(tid, set())
            if self.nodes.get(nid, {}).get('domain') != own_domain
        )
        
        year = int(node.get('year', 2000))
        age = 2026 - year
        time_factor = 1.0 / (1.0 + math.log(1 + age)) if age > 0 else 1.0
        
        liukai_connected = 'DATA-LIUKAI' in self.adj.get(tid, set())
        
        score = (
            0.25 * (in_degree / max(1, max_degree)) +
            0.25 * (cross_domain_edges / max(1, degree)) +
            0.20 * (degree / max_degree) +
            0.15 * time_factor +
            0.15 * (1.0 if liukai_connected else 0.0)
        )
        
        self._fitness_cache[tid] = round(score, 3)
        return round(score, 3)

    def prune_candidates(self, threshold=0.2):
        """返回适应度低于阈值的理论 (修剪候选)"""
        low = []
        for tid in self.nodes:
            if tid == 'LIUKAI': continue
            score = self.fitness_score(tid)
            if score < threshold:
                low.append({'id': tid, 'name': self.nodes.get(tid,{}).get('label',tid), 'fitness': score})
        return sorted(low, key=lambda x: x['fitness'])

    def top_theories(self, n=10):
        """返回适应度最高的N个理论"""
        scored = [(tid, self.fitness_score(tid)) for tid in self.nodes if tid != 'LIUKAI']
        return sorted(scored, key=lambda x: -x[1])[:n]

    # ── D₃ 反事实推演 ────────────────────

    def counterfactual(self, question):
        """基于图结构的反事实推演
        
        原理: 识别问题涉及的理论，找到与之有'挑战'或'替代'关系的理论，
              构建"如果X→那么Y"的反事实。
        """
        ql = question.lower()
        matched_theories = []
        for tid, node in self.nodes.items():
            if any(kw in ql for kw in node.get('n','').lower().split()):
                matched_theories.append(tid)
        
        counterfactuals = []
        for tid in matched_theories:
            # 找挑战者 (替代稳态 挑战 IDH)
            challengers = []
            for e in self.edges:
                if e['source'] == tid or e['target'] == tid:
                    other = e['target'] if e['source'] == tid else e['source']
                    # 简化: 与matched theory有边连接的理论
                    if other not in matched_theories:
                        challengers.append(other)
            
            for ch in challengers[:3]:
                counterfactuals.append({
                    'if_theory': self.nodes.get(tid,{}).get('label',tid),
                    'alternative': self.nodes[ch]['label'],
                    'question': f"如果{self.nodes[ch]['label']}比{self.nodes.get(tid,{}).get('label',tid)}更准确地描述了长江禁渔，系统会如何不同？",
                    'prediction': f"{self.nodes[ch]['label']}的预测: {self._get_prediction(ch)}"
                })
        
        return counterfactuals[:5]

    def _get_prediction(self, theory_id):
        predictions = {
            'IDH': '多样性先升后趋于平台',
            'ALTERNATIVE': '系统可能锁定在替代稳态,无法回到原始状态',
            'HOMOG': '外来物种比例持续上升',
            'FISHEVO': '大型个体比例缓慢恢复,需要数代',
            'FUNCDIV': '功能多样性恢复滞后于分类多样性',
            'RCC': '不同河段恢复速度不同 (纵向梯度)',
            'NEUTRAL': '任何恢复模式都可以用随机过程解释',
            'LEGACY': '40年捕捞的遗留效应在6年禁渔后仍显著',
        }
        return predictions.get(theory_id, '未知')

    # ── 涌现密度计算 ──────────────────────

    def emergence_density(self, theory_id):
        """计算节点的涌现密度 (D1→D2→D3 指标)"""
        tid = self._resolve_id(theory_id)
        if tid not in self.nodes: return {'density':0,'stage':'unknown'}
        degree = len(self.adj.get(tid, set()))
        max_degree = max(len(self.adj.get(nid, set())) for nid in self.nodes) or 1
        cross_domain = sum(
            1 for nid in self.adj.get(tid, set())
            if self.nodes.get(nid, {}).get('domain') != self.nodes.get(tid, {}).get('domain')
        )
        layer = self.nodes[tid].get('layer', 'middle')
        layer_weight = {'math': 1.0, 'meta': 0.9, 'grand': 0.8, 'middle': 0.5, 'data': 0.3}.get(layer, 0.5)
        
        density = 0.4 * (degree / max_degree) + 0.3 * (cross_domain / max(1, degree)) + 0.3 * layer_weight
        stage = 'D1 (数据)' if density < 0.3 else 'D2 (模式)' if density < 0.6 else 'D3 (理论涌现)'
        
        return {'density': round(density, 3), 'stage': stage, 'degree': degree, 'cross_domain_edges': cross_domain}

    # ── 全景报告 ──────────────────────────

    def full_report(self, question=None):
        """生成全景分析报告"""
        report = {
            'graph_stats': {
                'total_nodes': len(self.nodes),
                'total_edges': len(self.edges),
                'domains': len(self.domains),
                'emergence_zones': len(self.emergence_zones)
            },
            'topology_heatmap': self.topology_heatmap()[:10],
            'top_theories': [{'id': tid, 'name': self.nodes.get(tid,{}).get('label',tid), 'fitness': sc}
                           for tid, sc in self.top_theories(10)],
            'liukai_emergence': self.emergence_density('LIUKAI')
        }
        
        if question:
            report['routing'] = self.route(question)
            report['counterfactuals'] = self.counterfactual(question)
        
        return report


# ── CLI 入口 ──────────────────────────────

if __name__ == '__main__':
    import sys
    tg = TheoryGraph()
    
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        arg = sys.argv[2] if len(sys.argv) > 2 else None
        
        if cmd == 'route' and arg:
            result = tg.route(arg)
            print(json.dumps(result, ensure_ascii=False, indent=2))
        
        elif cmd == 'fitness' and arg:
            print(f"{arg}: {tg.fitness_score(arg)}")
        
        elif cmd == 'transposon' and arg:
            target = sys.argv[3] if len(sys.argv) > 3 else None
            result = tg.transposon_detect(arg, target)
            for r in result:
                print(f"  {r['similarity']} | {r['name']} ({r['domain']}) | {r['shared_terms']}")
        
        elif cmd == 'kinship' and arg:
            result = tg.kinship_propagate(arg)
            for r in result[:10]:
                print(f"  {r['weight']:.2f} | {r['name']}")
        
        elif cmd == 'counterfactual' and arg:
            result = tg.counterfactual(arg)
            for r in result:
                print(f"  {r['question']}")
        
        elif cmd == 'report':
            report = tg.full_report(arg)
            print(json.dumps(report, ensure_ascii=False, indent=2))
        
        elif cmd == 'emergence' and arg:
            result = tg.emergence_density(arg)
            print(f"{arg}: {result}")
        
        elif cmd == 'matrix':
            result = tg.topology_heatmap()
            for r in result[:15]:
                print(f"  {r['source']} ↔ {r['target']}: {r['weight']}")
        
        else:
            print(f"理论图谱引擎 v4.0 | {tg.data['metadata']['total_nodes']}节点·{tg.data['metadata']['total_edges']}边")
            print("命令: route <问题> | fitness <理论ID> | transposon <源ID> [目标域] | kinship <ID>")
            print("      counterfactual <问题> | emergence <ID> | matrix | report [问题]")
    else:
        print(f"理论图谱引擎 v4.0 | {tg.data['metadata']['total_nodes']}节点·{tg.data['metadata']['total_edges']}边")
        print("用法: python theory_graph_engine.py <命令> <参数>")
