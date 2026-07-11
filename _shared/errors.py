"""
统一错误处理 — 借鉴 LangGraph 5 级错误分类

Usage:
    from _shared.errors import safe_call, AdapterError

    safe_call(lambda: some_network_op(), error_type="transient", max_retries=3)
"""

import time
from typing import Callable


class AdapterError(Exception):
    """统一适配器异常"""

    def __init__(self, msg: str, error_type: str = "fatal", retry_after_ms: int = 0):
        super().__init__(msg)
        self.error_type = error_type
        self.retry_after_ms = retry_after_ms


# 5 级错误策略
ERROR_STRATEGIES = {
    "transient": {"max_retries": 3, "backoff_ms": 1000},    # 网络超时
    "llm_recover": {"max_retries": 2, "backoff_ms": 500},   # LLM 调用失败
    "retryable": {"max_retries": 5, "backoff_ms": 2000},     # 限流/速率限制
    "human_fix": {"max_retries": 0, "backoff_ms": 0},        # 等人工
    "fatal": {"max_retries": 0, "backoff_ms": 0},            # 穿透上报
}


def safe_call(
    fn: Callable,
    error_type: str = "transient",
    max_retries: int | None = None,
    on_error: Callable | None = None,
) -> any:
    """安全调用，自动重试瞬态错误"""
    strategy = ERROR_STRATEGIES.get(error_type, ERROR_STRATEGIES["fatal"])
    retries = max_retries if max_retries is not None else strategy["max_retries"]
    backoff = strategy["backoff_ms"]

    last_error = None
    for i in range(retries + 1):
        try:
            return fn()
        except Exception as e:
            last_error = e
            if i < retries and error_type in ("transient", "llm_recover", "retryable"):
                time.sleep(backoff / 1000 * (2**i))  # 指数退避
                if on_error:
                    on_error(i + 1, e)
            else:
                raise AdapterError(str(e), error_type=error_type) from e

    raise AdapterError(str(last_error), error_type="fatal") from last_error
