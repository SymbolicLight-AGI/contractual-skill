## Review: payment 配置

### 发现项

| 严重级别 | 发现 |
|---------|------|
| **阻断 (Block)** | **密钥硬编码**: `api_key` 以明文形式存储在 YAML 配置中，包含疑似生产环境密钥 (`SYNTHETIC_PAYMENT_SECRET_PLACEHOLDER` 前缀) |
| **高** | **无 Secret 扫描**: 项目缺少自动化检测机制，此类泄露无法被及时发现 |
| **中** | **无环境隔离**: 配置未区分环境，测试/生产密钥可能混用 |

### 影响

- **安全**: 生产密钥一旦入仓，即成为永久泄露风险（即使后续删除，Git 历史仍可恢复）
- **合规**: 违反密钥管理最小权限原则，可能导致审计失败
- **业务**: 支付密钥泄露可导致资金损失、数据篡改或监管处罚

### 建议操作

| 优先级 | 行动 | 负责人 |
|-------|------|--------|
| **立即** | **阻断合并** — 该 PR 不可合并 | 提交者 / 安全团队 |
| **立即** | **轮换密钥** — 在支付平台作废 `SYNTHETIC_PAYMENT_SECRET_PLACEHOLDER` 并生成新密钥 | 安全 / 运维 |
| **高** | **改用环境变量** — 移除硬编码，改为 `${PAYMENT_API_KEY}` 或集成 Secret 管理器（如 AWS Secrets Manager、Vault） | 后端开发 |
| **高** | **补充 Secret 扫描** — 引入 `git-secrets`、`truffleHog` 或 GitHub Advanced Security | DevOps / 安全 |
| **中** | **审计历史** — 检查该密钥是否已存在于其他分支或公开镜像 | 安全团队 |

### 测试/扫描建议

- 在 CI 中添加 pre-commit 钩子，拦截 `SYNTHETIC_PAYMENT_SECRET_PLACEHOLDER`、`SYNTHETIC_PAYMENT_TEST_SECRET_PLACEHOLDER` 等模式
- 添加配置加载测试，验证密钥从环境变量读取且不存在回退默认值

### 不确定性

- 该密钥是否已用于生产环境未知（`SYNTHETIC_PAYMENT_SECRET_PLACEHOLDER` 前缀提示可能为生产密钥，但需确认）
- 密钥当前是否已被泄露到外部未知（需审计 Git 历史及任何构建产物）

---

**结论**: **阻断合并**。在密钥轮换完成、硬编码移除、扫描工具配置完毕前，不应允许该变更进入主分支。
