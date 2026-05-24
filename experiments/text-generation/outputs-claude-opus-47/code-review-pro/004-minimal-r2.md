# Code Review: payment 配置

**结论：阻断合并（Block）。** 该 YAML 中包含疑似生产环境密钥，存在严重安全风险。

---

## 严重问题（Critical）

### 1. 硬编码生产密钥泄露
- `api_key` 字段包含以 `FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY` 前缀开头的明文密钥（已截断，不复述）。该前缀通常表示生产环境的实时密钥。
- 一旦合并进仓库（即便后续删除），将永久保留在 Git 历史中；项目未启用 secret 扫描，泄露可能不会被及时发现。
- 假设：未确认该密钥是否真实有效，但**按"已泄露"处理是必须的默认立场**。

### 2. 缺少 secret 扫描机制
- 项目说明中明确"没有 secret 扫描"，导致此类问题缺乏自动化兜底。

---

## 必须执行的处置步骤（按顺序）

1. **立即阻断该 PR 合并**，不要 squash 或 force-push 掩盖历史。
2. **立刻轮换（rotate）该密钥**：在支付服务后台吊销当前密钥并签发新密钥。轮换优先于清理 Git 历史——只要密钥仍有效，泄露窗口就持续存在。
3. **从配置文件移除明文密钥**，改用：
   - 环境变量（如 `PAYMENT_API_KEY`），通过 `${PAYMENT_API_KEY}` 占位符或代码侧加载；
   - 或使用密钥管理服务（Vault / AWS Secrets Manager / GCP Secret Manager / K8s Secret 等）。
4. **清理 Git 历史**（在轮换之后，作为防御纵深）：使用 `git filter-repo` 或 BFG 移除该提交中的密钥；如已推送到远程，需协调团队 force-push 并通知所有克隆者。
5. **审计访问日志**：检查该密钥在泄露窗口内是否产生异常调用。

---

## 配套改进建议（Should Fix）

### Secret 管理
- 仓库中添加 `.env.example`（仅含 key 名，不含值）作为约定。
- `.gitignore` 中确保 `.env`、本地凭据文件被忽略。
- 在 CI 中接入 secret 扫描工具：例如 `gitleaks`、`trufflehog`、GitHub Advanced Security secret scanning，或 pre-commit hook（`detect-secrets`）。
- 增加 PR 检查：阻断包含 `FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY`、`AWS_ACCESS_KEY_ID_PATTERN`、`PRIVATE_KEY_BLOCK_START_PATTERN` 等常见模式的提交。

### 配置健壮性
- `retry: 3` 缺少配套字段：建议补充 `timeout`、`backoff`（指数退避）、`max_backoff`，避免重试风暴打到支付方。
- `api_url` 使用 `.test` TLD，疑似占位/测试地址，但 `api_key` 是 `FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY` 前缀——**环境不一致**，需澄清这是测试配置误用了生产密钥，还是 URL 写错。这是另一个独立风险点。

### 测试与验证
- 添加单元测试：验证配置加载时若 `PAYMENT_API_KEY` 未设置应**显式失败**（fail fast），而非使用空串或默认值静默继续。
- 添加测试：确保日志/错误输出中**不打印 api_key**（脱敏测试）。
- 添加配置 schema 校验（如 JSON Schema / pydantic / cue），强制 `api_url` 与密钥前缀的环境一致性（live ↔ prod URL，test ↔ test URL）。
- CI 中加入回归用例：grep 仓库是否再次出现 `FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY` / `SYNTHETIC_PAYMENT_TEST_SECRET_PLACEHOLDER` 明文。

---

## 不确定性声明

- 未提供该配置文件被哪些服务读取、是否已部署、密钥是否已在生产使用 → 无法评估实际影响面，**建议按最坏情况处置**。
- 未提供仓库可见性（public / private） → 若为 public，影响等级再上调，需立即对外披露与监控滥用。
- 未提供该密钥是否曾出现在更早提交 → 需 `git log -p -S 'FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY'` 全历史排查。
