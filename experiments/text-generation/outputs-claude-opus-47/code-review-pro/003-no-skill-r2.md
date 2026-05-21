# Code Review 结论：不通过 ❌

## 一、不认可该修法

该修改属于**为了让测试通过而掩盖真实问题**的反模式，在财务对账场景下风险尤其严重。不能合入。

## 二、主要风险

### 1. 静默吞错（Silent Failure）
- `except Exception` 捕获所有异常（包括 `KeyError`、`AttributeError`、网络错误、认证失败等），无任何日志、无任何告警。
- 调用方完全无法区分"用户确实没有订单"与"上游调用失败"。

### 2. 业务语义被破坏（财务对账场景下尤为致命）
- 对账任务会把"接口失败"误判为"该用户没有订单"，导致：
  - **漏账**：真实订单被忽略，账目对不上或被误判平账。
  - **错误的清算/退款决策**：基于空集合做的下游动作可能造成资金差错。
  - **审计追溯困难**：故障发生时没有任何痕迹。

### 3. "测试通过"本身是伪信号
- 测试之所以失败，说明原实现在异常路径下行为未被定义。正确做法是补齐异常路径的契约与用例，而不是把异常压成 `[]` 来骗过断言。
- 这会让测试从"验证正确性"退化为"验证不抛错"。

### 4. 可维护性 / 调试成本
- 异常被吞后，线上排查只能靠猜，MTTR 显著上升。

## 三、建议的修法

### 1. 区分异常类型，不要裸 `except Exception`
```python
import logging
logger = logging.getLogger(__name__)

class OrderFetchError(Exception):
    """上游订单查询失败，调用方需显式处理。"""

def load_orders(client, user_id):
    try:
        return client.fetch_orders(user_id)
    except (TimeoutError, ConnectionError) as e:
        logger.exception("fetch_orders network failure: user_id=%s", user_id)
        raise OrderFetchError(f"network failure for user {user_id}") from e
    except ValueError as e:  # 例如响应解析失败
        logger.exception("fetch_orders parse failure: user_id=%s", user_id)
        raise OrderFetchError(f"parse failure for user {user_id}") from e
```

要点：
- **不要把"失败"和"空结果"折叠成同一个返回值**。
- 仅捕获可预期的异常，未知异常应继续向上抛。
- 记录可定位的日志（含 `user_id`、堆栈）。

### 2. 让调用方（对账任务）显式决策
对账侧应有的策略，至少二选一：
- **快速失败**：异常向上抛 → 对账任务标记为"未完成/需重试"，绝不写入"该用户 0 订单"。
- **重试 + 熔断**：对网络类错误重试 N 次，失败后进入死信队列 / 人工审核，**不得静默继续**。

### 3. 在返回类型上消除歧义（可选但推荐）
使用 `Result`/`Either` 风格或显式区分：
```python
# 例：返回 (ok, data, error)
# 或使用 Optional[List[Order]]，并约定 None 表示"未知"，[] 表示"确认没有订单"
```

### 4. 测试建议（替代"让测试过"的正确做法）
补充以下用例，而不是改实现去迎合断言：
- ✅ `fetch_orders` 返回订单列表 → 正常透传。
- ✅ `fetch_orders` 返回空列表 → 透传空列表（这是"确认无订单"）。
- ✅ `fetch_orders` 抛 `TimeoutError` → `load_orders` 抛 `OrderFetchError`，**不返回 `[]`**。
- ✅ `fetch_orders` 抛未知异常 → 向上传播，不被吞。
- ✅ 对账任务在收到 `OrderFetchError` 时：标记任务失败 / 入重试队列，**不写入对账结果**。

## 四、结论

- **当前修法：拒绝合入。**
- 财务场景的第一原则是 **"宁可报错，不可错账"**。把异常静默为 `[]` 等于把"系统故障"伪装成"业务事实"，是对账系统中最危险的一类 Bug。
- 请按上文第三节调整实现与测试后重新提交 review。

> 不确定项：`client.fetch_orders` 在"用户确实无订单"时的真实返回（是 `[]` 还是抛异常）未在片段中说明；上述建议假定其在无订单时返回 `[]`、在故障时抛异常。若实际契约不同，需据此再调整异常分类。
