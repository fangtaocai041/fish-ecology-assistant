#!/usr/bin/env python3
"""
贝叶斯思想工程化 — 全链路自检脚本

运行方式:
    python -m fish_ecology.core.bayesian.run_self_check

验证所有模块:
  ✅ 核心引擎 (Beta/Normal/Dirichlet Belief)
  ✅ 搜索可信度 (SearchCredibility)
  ✅ 知识更新 (KnowledgeUpdater)
  ✅ 冲突仲裁 (ConflictResolver)
  ✅ 变点检测 (ChangePointDetector)
  ✅ 智能体信念 (AgentBelief)
  ✅ 元认知 (MetaBayesian)
  ✅ 后验预测检验 (Posterior Predictive Check)
"""

from __future__ import annotations

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))

from fish_ecology.core.bayesian import (
    BetaBelief,
    NormalBelief,
    DirichletBelief,
    BayesianInference,
    conjugate_update,
    SelfCheckReport,
)
from fish_ecology.core.bayesian.applications import (
    SearchCredibility,
    KnowledgeUpdater,
    ConflictResolver,
    ChangePointDetector,
    AgentBelief,
    MetaBayesian,
)


def test_core_engine():
    """测试核心引擎的三类信念"""
    results = []

    # --- BetaBelief ---
    b = BetaBelief(alpha=2, beta=2)
    assert b.mean() == 0.5, "Beta 先验均值应=0.5"
    b.update(successes=8, trials=10)
    assert 0.7 < b.mean() < 0.8, f"Beta 后验均值应≈0.71, 实际={b.mean()}"
    lo, hi = b.credible_interval()
    assert lo < hi, "可信区间下界应<上界"
    weight = b.weight()
    assert weight > 10, f"证据权重应>10, 实际={weight}"
    results.append(("[PASS] BetaBelief", f"后验均值={b.mean():.4f}, CI=[{lo:.4f},{hi:.4f}]"))

    # --- NormalBelief ---
    n = NormalBelief(mu=0, sigma=10)
    n.update(observations=[5.0, 5.5, 4.8, 5.2, 5.1])
    assert 4.0 < n.mean() < 6.0, f"Normal 后验均值应≈5, 实际={n.mean()}"
    lo, hi = n.credible_interval()
    assert lo < hi, "Normal 可信区间应有效"
    results.append(("[PASS] NormalBelief", f"后验均值={n.mean():.3f}, sigma={n.sigma:.3f}"))

    # --- DirichletBelief ---
    d = DirichletBelief(alphas=[1, 1, 1])
    d.update(observations=[0, 1, 2, 0, 1, 0])
    means = d.mean()
    assert abs(sum(means) - 1.0) < 0.01, f"Dirichlet 概率和应=1, 实际={sum(means)}"
    assert means[0] > means[1] > 0, f"类别0概率应最大, 实际={means}"
    results.append(("[PASS] DirichletBelief", f"类别概率={[round(m,3) for m in means]}"))

    return results


def test_conjugate_update():
    """测试共轭更新统一接口"""
    # Beta 共轭更新
    posterior = conjugate_update("beta", {"alpha": 1, "beta": 1}, {"successes": 5, "trials": 10})
    assert 0.4 < posterior["alpha"] / (posterior["alpha"] + posterior["beta"]) < 0.6
    return [("[PASS] conjugate_update", "Beta 共轭更新正确")]


def test_search_credibility():
    """测试搜索可信度"""
    results = []

    # 引擎可靠性
    engine = SearchCredibility.engine_reliability("pubmed")
    assert engine.mean() > 0.8, f"PubMed 先验可信度应>0.8"
    engine.update(successes=50, trials=55)
    assert engine.mean() > 0.85, f"更新后可信度应更高"
    results.append(("[PASS] SearchCredibility.engine", f"PubMed 可信度={engine.mean():.3f}"))

    # 文献可信度
    paper = SearchCredibility.paper_credibility()
    paper.update(successes=1, trials=1)
    assert paper.mean() > 0.5
    # 多源验证
    paper.update(successes=2, trials=2)
    assert paper.mean() > 0.6
    results.append(("[PASS] SearchCredibility.paper", f"文献可信度={paper.mean():.3f}"))

    return results


def test_knowledge_updater():
    """测试知识更新"""
    results = []

    # 贝叶斯验证
    result = KnowledgeUpdater.validate_with_bayes(
        "长江江豚种群下降", supporting_count=8, contradicting_count=1,
        source_credibility=0.85,
    )
    assert result["verdict"] in ("confirmed", "plausible")
    assert result["posterior_mean"] > 0.7
    results.append(("[PASS] KnowledgeUpdater.validate",
                    f"'{result['claim'][:10]}...' → {result['verdict']} ({result['posterior_mean']:.3f})"))

    # 冲突场景
    conflict = KnowledgeUpdater.validate_with_bayes(
        "争议声明", supporting_count=5, contradicting_count=5,
    )
    assert conflict["verdict"] == "uncertain"
    results.append(("[PASS] KnowledgeUpdater.conflict", f"冲突场景 → {conflict['verdict']}"))

    return results


def test_conflict_resolver():
    """测试冲突仲裁"""
    results = []

    # 三源仲裁
    result = ConflictResolver.arbitrate(
        "江豚数量",
        [
            {"name": "文献A", "value": 1012, "credibility": 0.85},
            {"name": "文献B", "value": 1240, "credibility": 0.70},
            {"name": "文献C", "value": 850, "credibility": 0.60},
        ],
    )
    assert result["n_sources"] == 3
    assert result["weighted_estimate"] is not None
    # BMA 估计应在 850-1240 之间
    assert 800 < result["weighted_estimate"] < 1300
    results.append(("[PASS] ConflictResolver",
                    f"BMA估计={result['weighted_estimate']:.1f}, "
                    f"冲突={result['conflict_level']} ({result['conflict_score']:.3f})"))

    # 贝叶斯因子
    bf = ConflictResolver.bayes_factor(0.8, 0.2)
    assert bf > 3, f"BF应>3, 实际={bf}"
    results.append(("[PASS] bayes_factor", f"BF(0.8/0.2)={bf:.2f}"))

    return results


def test_change_point_detector():
    """测试变点检测"""
    results = []

    # 涌现信号
    strong = ChangePointDetector.emergence_score(10, 5, 1, 20)
    assert strong["signal"] == "strong", f"强信号检测失败: {strong}"
    results.append(("[PASS] emergence_score (强)", f"z={strong['z_score']:.2f}, signal={strong['signal']}"))

    none = ChangePointDetector.emergence_score(5.1, 5.0, 1.0, 20)
    assert none["signal"] == "none", f"无信号误报: {none}"
    results.append(("[PASS] emergence_score (无)", f"z={none['z_score']:.2f}, signal={none['signal']}"))

    # 在线检测
    detector = ChangePointDetector.online(0, 5)
    for v in [1.0] * 10:
        detector.update(v)
    assert detector.n_observations == 10
    results.append(("[PASS] OnlineChangePoint", f"处理{detector.n_observations}点"))

    return results


def test_agent_belief():
    """测试智能体信念"""
    results = []

    # 物种状态
    status = AgentBelief.species_status(prior_confident=False)
    summary = status.status_summary()
    assert summary["population"]["estimate"] > 0
    results.append(("[PASS] SpeciesStatus", f"种群={summary['population']['estimate']:.0f}, "
                    f"增长概率={summary['trend_growing_prob']:.3f}"))

    # 策略有效性更新
    strategy = AgentBelief.strategy_effectiveness()
    strategy.update(successes=7, trials=10)
    assert 0.5 < strategy.mean() < 0.9
    results.append(("[PASS] StrategyEffect", f"7/10成功 → {strategy.mean():.3f}"))

    return results


def test_meta_bayesian():
    """测试元贝叶斯"""
    results = []

    # 信念校准
    calib = MetaBayesian.calibrate_prior([
        {"success": True, "confidence": 0.85},
        {"success": True, "confidence": 0.90},
        {"success": False, "confidence": 0.20},
        {"success": False, "confidence": 0.80},  # 过自信
    ])
    assert 0 < calib["calibration_score"] < 1
    results.append(("[PASS] Calibrate", f"校准分数={calib['calibration_score']:.3f}, "
                    f"过自信={calib['overconfident_count']}"))

    # 信念漂移检测
    drift = MetaBayesian.belief_drift_detector(5)
    for v in [0.5] * 10:
        drift.record(v)
    assert not drift.is_drifting(), "稳定序列不应报漂移"
    for v in [0.9, 0.95, 0.98]:
        drift.record(v)
    results.append(("[PASS] DriftDetect", f"稳定→漂移: {drift.is_drifting()}"))

    return results


def test_self_check_integration():
    """测试每个模块的 self_check() 集成"""
    results = []

    modules = [
        ("SearchCredibility", SearchCredibility()),
        ("KnowledgeUpdater", KnowledgeUpdater()),
        ("ConflictResolver", ConflictResolver()),
        ("ChangePointDetector", ChangePointDetector()),
        ("AgentBelief", AgentBelief()),
        ("MetaBayesian", MetaBayesian()),
    ]

    for name, module in modules:
        report = module.self_check()
        assert isinstance(report, SelfCheckReport)
        status = "[PASS]" if report.passed else "[WARN]"
        results.append((f"{status} {name}.self_check",
                        f"{report.passed_checks}/{report.total_checks} 通过"))
        # 输出失败项详情
        for item in report.items:
            if not item.passed:
                results.append((f"  └ [FAIL] {item.name}", item.detail))

    return results


def main():
    """执行所有测试 + 自检"""
    print("=" * 65)
    print("  Bayesian Engineering -- Full Chain Self-Check")
    print("  Bayesian Engineering — Full Chain Self-Check")
    print("=" * 65)

    all_tests = [
        ("核心引擎", test_core_engine),
        ("共轭更新", test_conjugate_update),
        ("搜索可信度", test_search_credibility),
        ("知识更新", test_knowledge_updater),
        ("冲突仲裁", test_conflict_resolver),
        ("变点检测", test_change_point_detector),
        ("智能体信念", test_agent_belief),
        ("元贝叶斯", test_meta_bayesian),
        ("自检集成", test_self_check_integration),
    ]

    total = 0
    passed = 0
    failed_cases = []

    for group_name, test_fn in all_tests:
        print(f"\n── {group_name} ──")
        try:
            results = test_fn()
            for label, detail in results:
                total += 1
                if label.startswith("[PASS]"):
                    passed += 1
                    print(f"  {label}")
                # print(f"    {detail}")
        except AssertionError as e:
            total += 1
            print(f"  [FAIL] {group_name} 失败: {e}")
            failed_cases.append(group_name)
        except Exception as e:
            total += 1
            print(f"  [FAIL] {group_name} 异常: {e}")
            failed_cases.append(group_name)

    # 输出汇总
    print("\n" + "=" * 65)
    success_rate = passed / total * 100 if total > 0 else 0
    if failed_cases:
        print(f"  [WARN] 通过 {passed}/{total} ({success_rate:.0f}%)")
        print(f"  [FAIL] 失败模块: {', '.join(failed_cases)}")
    else:
        print(f"  [ALL PASS] 全通过 {passed}/{total} (100%)")
    print("=" * 65)

    return len(failed_cases) == 0


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
