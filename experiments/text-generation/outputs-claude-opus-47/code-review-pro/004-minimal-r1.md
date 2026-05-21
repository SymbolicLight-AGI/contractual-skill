# 代码审查结果：payment 配置

## 结论：**不可合并（Block）**

---

## 严重问题（Critical）

### 1. 生产密钥硬编码并提交至仓库
- `api_key` 字段包含一个以 `SYNTHETIC_PAYMENT_SECRET_PLACEHOLDER` 开头的明文生产密钥（已在此省略具体值，避免二次泄露）。
- 仓库未启用 secret 扫描，密钥可能已被 clone/fork/CI 日志/历史记录扩散。
- 即便后续删除该行，Git 历史中仍可检索到，必须视为**已泄露**。

---

## 必须执行的处置步骤（按顺序）

1. **阻断本次合并**：在 PR 上标记 changes requested，禁止 squash/merge。
2. **立即轮换密钥**：
   - 在支付服务商后台 revoke 当前 `SYNTHETIC_PAYMENT_SECRET_PLACEHOLDER…` 密钥。
   - 生成新密钥，仅注入运行时环境，不入库。
3. **清理 Git 历史**：
   - 使用 `git filter-repo` 或 BFG Repo-Cleaner 重写包含该密钥的提交。
   - 强制推送并通知所有协作者重新 clone。
   - 注：历史清理**不能替代**密钥轮换，仅作为补充。
4. **改用环境变量 / Secret 管理**：
   ```yaml
   payment:
     api_url: "https://payments.example.test"
     api_key: "${PAYMENT_API_KEY}"   # 从环境/Secret Manager 注入
     retry: 3
   ```
   推荐通过 Vault / AWS Secrets Manager / GCP Secret Manager / K8s Secret 等托管。
5. **加入 `.gitignore` 与示例文件**：
   - 提交 `config.example.yaml`（占位值），真实配置文件入 ignore。

---

## 次要建议（Maintainability / Robustness）

- `retry: 3` 缺少语义：是次数还是上限？建议改为 `max_retries` 并补充 `retry_backoff_ms`、`timeout_ms`。
- `api_url` 看起来是 `.test` 域名（保留 TLD），与字段名 `SYNTHETIC_PAYMENT_SECRET_PLACEHOLDER` 暗示的生产环境不一致——需澄清环境归属，避免 prod 密钥配 test endpoint 或反之。
- 缺少 schema 校验（如启动时校验 `api_key` 非空、URL 合法、retry 为正整数）。

> 不确定性：未提供加载该配置的代码与部署方式，无法判断密钥是否已进入运行时日志、CI 缓存或镜像层。建议一并排查。

---

## 测试与扫描补充建议

1. **接入 secret 扫描**（CI 阻断 + pre-commit）：
   - `gitleaks` / `trufflehog` / GitHub Advanced Security secret scanning。
   - 在 pre-commit hook 中执行，PR 流水线中再次执行作为门禁。
2. **历史全量扫描**：对整个仓库历史跑一次 `gitleaks detect --log-opts="--all"`，定位其他潜在泄露。
3. **配置加载单元测试**：
   - 当 `api_key` 为空 / 未注入时应快速失败（fail-fast）。
   - 当 `api_key` 仍为明文 `SYNTHETIC_PAYMENT_SECRET_PLACEHOLDER*` 字面量时，测试应报错（防回归）。
4. **集成测试**：使用 mock 或沙箱密钥，禁止在测试中引用生产密钥。
5. **审计与告警**：在支付商后台开启密钥使用审计，关注轮换前后异常调用。

---

## 风险优先级摘要

| 级别 | 项目 |
|------|------|
| Critical | 生产密钥泄露、无 secret 扫描 |
| High | Git 历史污染、环境与密钥前缀不匹配 |
| Medium | 缺少 schema 校验、retry 语义不清 |
| Low | 缺少示例配置文件与文档 |
