## 总体判断

**高风险** — 存在 SQL 注入漏洞，且缺乏测试覆盖。当前代码不可直接用于生产环境。

---

## 主要问题

| 类别 | 问题 | 证据 |
|:---|:---|:---|
| **安全** | SQL 注入（SQLi） | `customer_id` 直接字符串拼接到查询中，未参数化 |
| **正确性** | 查询结果可能包含未预期列 | `SELECT *` 返回所有列，若表结构变更会影响下游 |
| **可靠性** | 无错误处理 | `db.execute()` 可能因连接问题、语法错误等抛出异常 |
| **隐私** | 可能返回敏感数据 | `SELECT *` 可能包含不应暴露的内部字段（如 `created_by_admin_id`, `internal_flag` 等） |

---

## 风险与影响

- **Finding**: `customer_id` 通过 HTTP query 参数传入，直接字符串拼接进 SQL 查询
- **Risk**: 攻击者可构造 `customer_id=1 OR 1=1` 或 `customer_id=1; DROP TABLE notes;--` 等 payload，导致数据泄露、篡改或删除
- **Risk**: 即使当前为"内部 CRM"，内部人员或 compromised 账户仍可利用此漏洞
- **Risk**: `SELECT *` 若包含敏感列，违反最小权限原则，可能泄露内部操作信息

---

## 测试建议

| 测试类型 | 具体检查 |
|:---|:---|
| **安全测试** | 使用 `customer_id="1' OR '1'='1"` 验证是否被注入 |
| **安全测试** | 使用 `customer_id="1; DROP TABLE notes;--"` 验证参数化防御 |
| **正确性测试** | 验证查询仅返回预期列，而非 `SELECT *` |
| **边界测试** | `customer_id` 为空字符串、非数字、超长字符串、Unicode |
| **错误处理** | 数据库连接断开、表不存在时的行为 |
| **权限测试** | 验证 A 用户无法通过篡改 `customer_id` 查看 B 用户备注 |

---

## 不确定性

- **Uncertainty**: `db` 的具体类型（`sqlite3.Connection`? SQLAlchemy? 其他？）— 影响参数化语法
- **Uncertainty**: `notes` 表实际列结构，无法判断 `SELECT *` 具体泄露风险
- **Uncertainty**: 当前是否已有 WAF、ORM 层或其他 SQLi 缓解措施
- **Uncertainty**: `customer_id` 是否在其他层有预校验（如仅允许数字）

---

## 交接建议

| 风险领域 | 交接对象 | 原因 |
|:---|:---|:---|
| **安全** | Security 团队 | SQL 注入属于严重安全漏洞，需安全评审修复方案 |
| **后端** | Backend Owner | 参数化查询改造、错误处理加固、列白名单设计 |
| **产品** | Product Owner | 确认 `notes` 表中哪些列对 CRM 用户可见，定义数据访问边界 |
| **QA** | QA/Test Owner | 补充 SQLi 回归测试、权限隔离测试、异常路径测试 |

---

## 完成前自检

- [x] 发现 SQL 注入漏洞，直接由代码字符串拼接支持
- [x] 未重复任何 secrets 或敏感标识
- [x] 未假设外部缓解措施存在
- [x] 未提供具体代码修改（仅建议参数化查询方向）
- [x] 安全、后端、QA 交接对象已明确
