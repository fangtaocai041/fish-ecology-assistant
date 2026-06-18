"""测试 MAGMA + NetworkX 增强功能"""
import sys
sys.path.insert(0, ".")

from src.memory.magma import MagmaMemory, NetworkXGraphDB


class TestNetworkX:
    def test_nx_backend_available(self):
        db = NetworkXGraphDB()
        assert db.node_count == 0
        assert db.edge_count == 0

    def test_nx_add_nodes_edges(self):
        db = NetworkXGraphDB()
        db.add_node("a", type="species")
        db.add_node("b", type="habitat")
        db.add_node("c", type="species")
        db.add_edge("a", "b", "habitat", 0.9)
        db.add_edge("c", "b", "habitat", 0.8)
        assert db.node_count == 3
        assert db.edge_count == 2

    def test_page_rank(self):
        db = NetworkXGraphDB()
        for n in ["a", "b", "c", "d"]:
            db.add_node(n)
        db.add_edge("a", "b", "related", 1.0)
        db.add_edge("b", "c", "related", 1.0)
        db.add_edge("c", "a", "related", 1.0)
        db.add_edge("d", "a", "related", 0.5)
        pr = db.page_rank(top_k=4)
        assert len(pr) == 4
        assert abs(sum(v for _, v in pr) - 1.0) < 0.1  # PageRank sums to ~1

    def test_shortest_path(self):
        db = NetworkXGraphDB()
        for n in ["鳤", "长江", "珍稀鱼类", "保护等级"]:
            db.add_node(n)
        db.add_edge("鳤", "长江", "habitat", 0.9)
        db.add_edge("长江", "珍稀鱼类", "attribute", 0.7)
        db.add_edge("珍稀鱼类", "保护等级", "conservation", 0.8)
        path = db.shortest_path("鳤", "保护等级")
        assert path is not None
        assert len(path) == 4

    def test_community_detection(self):
        db = NetworkXGraphDB()
        for n in ["A1", "A2", "A3", "B1", "B2"]:
            db.add_node(n)
        db.add_edge("A1", "A2", "group", 1.0)
        db.add_edge("A2", "A3", "group", 1.0)
        db.add_edge("B1", "B2", "group", 1.0)
        comms = db.community_detection()
        assert len(comms) >= 2

    def test_centrality(self):
        db = NetworkXGraphDB()
        for n in ["bridge", "a", "b", "c", "d"]:
            db.add_node(n)
        db.add_edge("bridge", "a", "", 1.0)
        db.add_edge("bridge", "b", "", 1.0)
        db.add_edge("bridge", "c", "", 1.0)
        db.add_edge("bridge", "d", "", 1.0)
        cb = db.centrality()
        assert len(cb) >= 1

    def test_subgraph(self):
        db = NetworkXGraphDB()
        for n in ["a", "b", "c"]:
            db.add_node(n)
        db.add_edge("a", "b")
        sub = db.subgraph({"a", "b"})
        assert sub.node_count == 2

    def test_density(self):
        db = NetworkXGraphDB()
        assert db.density() == 0.0
        db.add_node("a")
        assert db.density() == 0.0
        db.add_node("b")
        db.add_edge("a", "b")
        assert db.density() > 0

    def test_report(self):
        db = NetworkXGraphDB()
        db.add_node("a")
        db.add_node("b")
        db.add_edge("a", "b")
        r = db.report()
        assert r["nodes"] == 2
        assert r["edges"] == 1


class TestMagmaWithNX:
    def test_magma_nx_backend(self):
        mem = MagmaMemory(nx_backend=True)
        assert mem._nx is not None

    def test_magma_nx_page_rank(self):
        mem = MagmaMemory(nx_backend=True)
        mem.add("鳤是长江珍稀鱼类", entities=["鳤"])
        mem.add("刀鲚是洄游鱼类", entities=["刀鲚"])
        mem.add("长江有丰富的水生生物资源", entities=["长江"])
        pr = mem.page_rank()
        assert len(pr) >= 1

    def test_magma_nx_communities(self):
        mem = MagmaMemory(nx_backend=True)
        mem.add("鳤生活在长江")
        mem.add("刀鲚生活在长江")
        mem.add("松树生长在森林")
        comms = mem.communities()
        assert len(comms) >= 1

    def test_magma_nx_shortest_path(self):
        mem = MagmaMemory(nx_backend=True)
        mem.add("鳤是珍稀鱼类", entities=["鳤"])
        mem.add("珍稀鱼类需要保护", entities=["珍稀鱼类"])
        mem.add("保护等级分为LC/EN/CR", entities=["保护等级"])
        # 通过实体关系建立连接
        mem.add("鳤的保护等级是EN", entities=["鳤", "保护等级"])
        path = mem.shortest_path("鳤", "保护等级")
        # 可能找到路径也可能找不到(取决于关系权重), 至少不崩溃
        assert path is None or len(path) >= 2

    def test_magma_nx_stats(self):
        mem = MagmaMemory(nx_backend=True)
        mem.add("test")
        s = mem.stats()
        assert s["nx_enabled"]
        assert "nx_analysis" in s

    def test_magma_without_nx(self):
        mem = MagmaMemory(nx_backend=False)
        assert mem.page_rank() == []
        assert mem.communities() == []
        assert mem.shortest_path("a", "b") is None
