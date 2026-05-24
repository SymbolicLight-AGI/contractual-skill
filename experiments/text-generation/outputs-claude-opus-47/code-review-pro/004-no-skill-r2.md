# 配置评审结论：**不建议合并**

## 严重问题：硬编码生产密钥泄露

`api_key` 字段包含以 `FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY` 开头的生产密钥（疑似 Stripe 风格的 live secret key）。一旦该配置被提交到仓库，密钥即视为**已泄露**，无论后续是否回滚提交。

风险等级：**高危 / 阻断级**

---

## 必须执行的处置动作

### 1. 阻断本次合并
- 在 PR 上标记 `block / changes requested`，禁止 squash 或 merge。
- 不要通过 force-push / amend 来"掩盖"提交——历史中仍可被恢复。

### 2. 立即轮换密钥（最高优先级）
- 登录支付服务商控制台，**吊销当前 live key**，签发新密钥。
- 检查该密钥近期调用日志，确认是否存在未授权调用。
- 即便 PR 尚未合并，只要曾推送到远端分支，就应视为已外泄。

### 3. 从 Git 历史中清除
- 仅删除文件不够，需使用 `git filter-repo`（或 BFG）重写历史，并强制推送。
- 通知所有协作者重新 clone / rebase。
- 注意：GitHub/GitLab 等平台的 fork、缓存、PR 快照可能仍保留，需联系平台支持彻底清除（不确定性：取决于所用平台与镜像策略）。

### 4. 改用环境变量 / Secret 管理
建议改造为：

```yaml
payment:
  api_url: "https://payments.example.test"
  api_key: ${PAYMENT_API_KEY}   # 从环境变量注入
  retry: 3
```

落地方式（按部署形态选择其一）：
- 本地开发：`.env` 文件 + `.gitignore` 排除，提供 `.env.example` 占位。
- CI/CD：使用 GitHub Actions Secrets / GitLab CI Variables。
- 生产：Vault、AWS Secrets Manager、KMS 等托管方案。

### 5. 补充防御措施
- **接入 secret 扫描**：启用 `gitleaks` / `trufflehog` / GitHub Secret Scanning，作为 pre-commit hook 与 CI 必过检查。
- **pre-commit 钩子**：本地阻断含密钥模式（`FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY`、`AWS_ACCESS_KEY_ID_PATTERN`、`PRIVATE_KEY_BLOCK_PATTERN` 等）的提交。
- **新增单元/集成测试**：
  - 配置加载逻辑应在缺少 `PAYMENT_API_KEY` 时显式失败，而非使用默认值或空串。
  - 验证生产环境配置中不存在以 `FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY` 开头的字面量（可加一条 lint/test 断言）。
- **文档**：在 `CONTRIBUTING.md` 中明确密钥处理规范与泄露应急流程。

---

## 其他次要建议（非阻断）

- `retry: 3` 建议补充重试间隔与退避策略说明，避免对支付接口产生雪崩重试。
- `api_url` 当前是 `.test` 域名，请确认这是占位还是真实环境配置——若与生产 live key 同时出现，存在环境配置错配风险。

---

## 不确定性标注
- 密钥真实归属服务商需根据上下文确认，`FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY` 仅为常见前缀约定。
- 平台侧历史清除的彻底性依赖具体托管方政策。
