# Code Review: `get_customer_notes`

## 总体判断
**不可合并。** 存在高危 SQL 注入漏洞，且无任何测试覆盖。需在合并前修复并补齐测试。

---

## 主要发现

### 1. 【Critical / Security】SQL 注入漏洞
```python
query = f"SELECT * FROM notes WHERE customer_id = {customer_id}"
```
- `customer_id` 来自 HTTP query 参数，直接通过 f-string 拼接进 SQL，属于典型的 SQL 注入。
- **影响**：攻击者可构造 `customer_id=1 OR 1=1` 读取全部备注（客户隐私泄露）；若底层驱动支持多语句，可进一步执行 `DROP TABLE`、`UPDATE`、读取 `information_schema` 等，造成数据泄露或数据损坏。
- **风险等级**：高（生产环境直接可利用，CRM 含个人/业务敏感信息）。
- **修复方向**（不在本次实现）：使用参数化查询（`db.execute("SELECT ... WHERE customer_id = ?", (customer_id,))`），并在入口层做类型校验（强制 int）。

### 2. 【High / Security & Correctness】缺少授权校验
- 函数仅按 `customer_id` 查询，未见调用方对“当前登录用户是否有权访问该 customer”的校验描述。
- **影响**：可能造成 IDOR（越权访问任意客户备注）。
- **不确定性**：调用方是否已在上层做 ACL 校验未提供，需确认。若没有，应在该层或服务层补齐。

### 3. 【Medium / Correctness】`SELECT *` 不稳定
- 使用 `SELECT *` 后 `dict(row)` 直接返回，schema 变化（新增敏感字段如 `internal_flag`、`pii`）会自动暴露给 API 响应。
- **影响**：数据过度暴露、接口契约不稳定。
- **建议**：显式列出所需列，并在序列化层做白名单。

### 4. 【Medium / Correctness】无输入校验与错误处理
- 未校验 `customer_id` 是否为有效整数、是否存在；DB 异常未处理。
- 空结果与“非法 ID”无法区分（都返回 `[]`），调用方难以正确响应 404 / 400。
- **影响**：错误语义模糊，下游可能误判。

### 5. 【Low / Performance & Maintainability】
- 未做分页 / `LIMIT`。若单客户备注量大，会一次性加载全部行并构建 dict，存在内存与延迟风险。
- 无排序保证（如 `ORDER BY created_at DESC`），返回顺序依赖数据库实现。
- 缺少 docstring、类型注解。

### 6. 【Low / Observability】
- 无日志（如查询耗时、异常）。生产排障困难。注意：日志不要打印完整 `customer_id` 之外的潜在敏感参数。

---

## 测试建议（当前完全缺失）

**安全测试**
- SQL 注入用例：`customer_id="1 OR 1=1"`、`"1; DROP TABLE notes--"`、Unicode/编码绕过；断言抛出校验错误或返回空，且不会执行注入语义。
- 越权用例：用户 A 请求用户 B 的 `customer_id`，断言被拒绝（需与上层一起测）。

**正确性测试**
- 正常路径：存在多条备注，返回顺序与字段符合契约。
- 边界：`customer_id` 不存在 → 返回 `[]` 或 404（取决于约定）。
- 非法输入：负数、非数字、超长字符串、`None` → 明确的错误响应。
- Schema 变更回归：固定返回字段集合的快照测试。

**性能 / 鲁棒性**
- 大量备注（如 10k 行）下的延迟与内存。
- DB 异常 / 连接断开 → 抛出可被上层捕获的错误，不静默返回成功状。

---

## 风险影响小结
- **数据泄露**：高（SQL 注入 + 潜在 IDOR + `SELECT *`）。
- **数据完整性**：中高（注入可能写/删）。
- **可维护性**：中（schema 漂移、无测试、无日志）。

---

## 不确定性
- 不清楚 `db.execute` 底层是否为某 ORM/驱动，是否支持参数化语法（`?` vs `%s` vs `:name`）。
- 上层（路由 / 中间件）是否已做认证、授权、类型校验未知。
- `notes` 表的列定义未提供，无法判断哪些字段属于敏感信息。

---

## 建议的 Handoff
- **Security**：确认 SQL 注入修复方案、IDOR/ACL 设计审查、敏感字段分级。
- **Backend Owner**：实现参数化查询、输入校验、分页、显式字段、错误语义。
- **QA / Testing**：补齐上述安全与正确性测试套件，并加入回归。
- **Product**：确认接口返回字段契约（哪些备注字段允许暴露给前端）。
