# Code Review: payment 配置合并请求

## 总体判断

**阻断合并（Block merge）。** 该 YAML 文件包含一个看起来是生产环境的明文 API 密钥（`FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY…` 前缀，疑似真实付款服务凭证），不得合入仓库。

---

## 主要发现

### 1. 严重 — 生产密钥明文提交（Secret leakage）
- **位置**：`payment.api_key`
- **证据**：值以 `FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY` 开头（典型的"live/生产"密钥命名约定），长度与常见付款服务密钥一致。不在此复述完整值。
- **影响**：
  - 一旦合入主分支，密钥将进入 Git 历史，即使后续删除文件，历史提交、fork、CI 缓存、镜像中仍然可被检索。
  - 项目没有 secret 扫描，意味着此前可能已有类似泄露未被发现。
  - 攻击者可直接调用付款 API，造成资金损失、欺诈交易、数据泄露与合规问题（PCI-DSS 等）。
- **严重级别**：Critical / Blocker。

### 2. 中 — 配置与机密混在同一文件
- `api_url`、`retry` 等非敏感配置与机密放在一起，鼓励了"顺手把 key 写进去"的反模式。
- 缺少环境分层（dev/staging/prod 同一份配置容易导致 live key 被用于测试）。

### 3. 中 — 缺少 secret 管理与扫描基础设施
- 仓库无 secret scanning，无 pre-commit 钩子，无 CI 阻断策略。
- 没有看到 `.gitignore`/`.gitattributes` 对机密文件的隔离规则（基于所给上下文）。

### 4. 低 — `retry: 3` 缺少上下文
- 未说明重试是否带退避、是否对非幂等的付款请求安全。付款类请求重试若无幂等键可能导致重复扣款。**此项为提示，不阻断合并**，需后端确认。

---

## 风险影响汇总

| 风险 | 可能后果 |
|---|---|
| 生产密钥泄露 | 资金损失、欺诈、合规违规、客户数据风险 |
| 无扫描机制 | 历史与未来泄露均无法及时发现 |
| 付款重试策略不明 | 潜在重复扣款 |

---

## 必需的修复行动（合并前）

1. **立刻轮换该密钥**：联系付款服务方作废当前 `FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY…`，签发新密钥。视作已泄露处理，不要假设"还没人看到"。
2. **从 Git 历史中清除**：使用 `git filter-repo` 或 BFG 重写历史；强制推送；通知所有协作者重新克隆。注意：即便清理，仍须按第 1 步轮换，因为无法保证未被抓取。
3. **改用环境变量 / Secret Manager**：
   ```yaml
   payment:
     api_url: "https://payments.example.test"
     api_key: "${PAYMENT_API_KEY}"   # 由运行时注入
     retry: 3
   ```
   生产侧使用 Vault / AWS Secrets Manager / KMS 等托管方案。
4. **分离环境配置**：`config.dev.yaml` / `config.prod.yaml`，且 prod 文件只在部署管线中渲染，不入库。
5. **添加 `.gitignore` 与示例文件**：提交 `config.example.yaml`（占位值），真实配置文件忽略。

---

## 测试与扫描建议

- **CI 加 secret 扫描**：例如 `gitleaks`、`trufflehog`、GitHub Advanced Security Secret Scanning。对 PR 强制阻断。
- **pre-commit 钩子**：`detect-secrets` 或 `gitleaks protect`，在本地即拦截。
- **回归测试**：
  - 启动时若 `PAYMENT_API_KEY` 缺失应明确失败（fail fast），添加单元测试覆盖。
  - 配置加载层添加测试：禁止任何 `FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY`/`SYNTHETIC_PAYMENT_TEST_SECRET_PLACEHOLDER` 字面量出现在仓库内（可作为 lint 规则）。
- **付款重试**：补充集成测试，验证幂等键存在且重试不会重复扣款。

---

## 不确定项

- 无法从片段确认这是否为真实有效的生产密钥（也可能是占位/示例），但 `FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY` 前缀与"没有 secret 扫描"的背景使得**必须按真实泄露处理**。
- 不清楚该文件是否已经在历史中存在多久、是否已被外部抓取。需要查询 Git 历史与仓库可见性（public/private、fork 情况）。
- 未提供 `retry` 的调用代码，无法判断是否幂等。

---

## 需要的 Handoff

- **Security / Platform**：密钥轮换、历史清理、引入 secret 扫描与 Vault。
- **Backend**：付款客户端改造为从环境变量/Secret Manager 读取；确认重试幂等性。
- **DevOps / CI**：接入 gitleaks 等扫描并将其设为合并阻断检查。
- **合规 / 事件响应**：评估是否触发安全事件上报流程（取决于密钥是否真实生效）。

---

**结论：不通过（Request changes）。** 在完成密钥轮换、历史清理、改用环境变量、并接入 secret 扫描之前，不得合并此 PR。
