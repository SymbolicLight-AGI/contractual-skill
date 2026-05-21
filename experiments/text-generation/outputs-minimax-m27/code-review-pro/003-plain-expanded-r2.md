# Code Review: `load_orders` 异常吞没

## Overall Judgment

**不认可此修法。**

该代码在财务对账场景中引入严重静默失败风险，违反了安全修复原则。

---

## Main Findings

### 🔴 高风险：静默吞没所有异常

```python
except Exception:
    return []
```

- 捕获范围过宽，包括网络超时、`AuthError`、`RateLimitError`、`DataError` 等所有异常
- 无日志、无告警、无上下文，错误完全不可追踪
- 后续对账流程无法区分「真实无订单」与「请求失败」

### 🔴 高风险：业务结果错误

财务对账依赖准确数据。上游故障时返回 `[]` 会导致：

- 对账任务误判为「无订单」而非「请求异常」
- 资金差异无法定位根因
- 可能触发错误的资金补偿或结算

### 🟡 中风险：测试掩耳盗铃

测试通过的原因是数据被静默替换，而非业务逻辑正确。掩盖了真实异常，使测试失去保护作用。

---

## Impact

| 影响维度 | 级别 |
|---|---|
| 数据完整性 | 高 — 财务记录可能缺失 |
| 运营可见性 | 高 — 故障被隐藏 |
| 调试能力 | 高 — 无错误上下文 |
| 合规审计 | 高 — 对账结果不可信 |

---

## Recommended Fix

```python
import logging

logger = logging.getLogger(__name__)

def load_orders(client, user_id):
    try:
        return client.fetch_orders(user_id)
    except Exception as e:
        logger.error(
            "Failed to fetch orders",
            extra={"user_id": user_id, "error": type(e).__name__, "detail": str(e)}
        )
        raise  # 或返回特定错误类型，由调用方决策
```

如需隔离错误：

```python
class OrderFetchError(Exception):
    """上游订单接口不可用"""
    pass

def load_orders(client, user_id):
    try:
        return client.fetch_orders(user_id)
    except Exception as e:
        logger.error(f"Order fetch failed for user {user_id}: {e}")
        raise OrderFetchError(f"Unable to fetch orders for user {user_id}") from e
```

---

## Test Advice

1. 单元测试：模拟 `client.fetch_orders` 抛出 `TimeoutError`/`AuthError`，验证异常向上传播
2. 集成测试：验证日志或告警被触发
3. 禁止：不要写「返回空数组」的测试来掩盖异常路径
4. 对账任务侧：调用方应区分「无订单」与「接口异常」，分别处理

---

## Uncertainty

- 不确定 `client.fetch_orders` 的异常类型，无法建议捕获粒度
- 不确定调用方是否已有重试/降级逻辑

---

## Follow-up Owners

| Owner | 关注点 |
|---|---|
| 后端团队 | 实现 `OrderFetchError` 并定义异常分类 |
| 财务系统 | 对账任务需区分「空结果」与「异常结果」 |
| 测试团队 | 确保异常路径被覆盖，不使用空数组 mock 绕过 |
