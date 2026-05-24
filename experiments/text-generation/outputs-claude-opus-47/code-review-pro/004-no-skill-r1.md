# 配置审查结论：**不建议合并**（Block）

## 关键风险

**严重：硬编码生产密钥泄露**

`api_key` 字段以明文形式提交了一个 `FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY` 前缀的生产环境密钥（已识别，不在此复述）。一旦该 commit 进入仓库历史，即使后续删除，密钥仍可通过 git history、fork、缓存等途径被读取，必须视为**已泄露**。

附加风险：
- `api_url` 指向疑似生产域名（`payments.example.test`），与 `FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY` 前缀一致，影响面为线上。
- 项目无 secret 扫描，类似问题大概率不是孤例。

---

## 处置建议（按优先级）

### 1. 立即阻断本次合并
- 在 PR 上标记 `Request Changes` / `Block`，禁止 squash & merge。
- 不要仅靠"再提一个 commit 删掉"了事——历史仍可追溯。

### 2. 立即轮换密钥（最高优先级，先于代码修复）
- 登录支付服务商后台**吊销当前 `FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY` 密钥**。
- 生成新密钥，仅注入到运行环境，不再进入版本库。
- 检查支付方提供的调用日志，确认泄露窗口期内有无异常调用。
- 若该密钥已被推送到远端公共/共享仓库，按"已泄露"处置，不要假设没人看到。

### 3. 清理仓库历史（可选但推荐）
- 使用 `git filter-repo` 或 BFG Repo-Cleaner 从历史中移除该值。
- 强推后通知所有协作者重新 clone。
- 注意：即便清理，也**不能替代轮换密钥**。

### 4. 改用环境变量 / Secret 管理
配置文件示例改写：

```yaml
payment:
  api_url: ${PAYMENT_API_URL}
  api_key: ${PAYMENT_API_KEY}   # 从环境/Secret Manager 注入
  retry: 3
```

推荐方案（任选其一，依现有基建而定）：
- 环境变量 + `.env`（`.env` 加入 `.gitignore`，仓库内仅保留 `.env.example`）。
- 集中式 Secret 管理：Vault、AWS Secrets Manager、GCP Secret Manager、K8s Secret + KMS 等。
- CI/CD 中以加密变量注入，禁止在日志打印。

并在代码加载侧做：
- 启动时校验必需 secret 是否存在，缺失则 fail-fast。
- 禁止把 `api_key` 写入日志、错误堆栈、监控上报。

### 5. 补充防回归措施

**扫描类（必须）：**
- 在 CI 接入 secret 扫描：`gitleaks`、`trufflehog`、或 GitHub Advanced Security 的 secret scanning + push protection。
- 加 pre-commit hook（如 `pre-commit` + `detect-secrets`），在开发者本地拦截。
- 对历史全量扫一次，排查其他遗漏密钥。

**测试与流程类：**
- 加单元/集成测试：当 `PAYMENT_API_KEY` 未设置时，加载逻辑应抛出明确错误而非使用默认值。
- 加测试：确认配置加载后 `api_key` 不出现在日志输出中（可对 logger 做断言）。
- 在 `CONTRIBUTING.md` / PR 模板中加入"是否包含密钥/凭据"检查项。
- Code Owner 规则：涉及 `payment*.yaml` 等敏感路径的改动强制 review。

---

## 不确定项
- 该密钥是否已经被推送到远端、远端是否为公共仓库——**未知**，建议按最坏情况（已泄露）处理。
- `payments.example.test` 是否为真实生产域名（`.test` 是保留 TLD，可能是脱敏占位），但 `FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY` 前缀已足以判定按生产密钥处置。
- 项目使用的具体语言/框架与 Secret 基建未提供，上述方案需结合实际选型落地。
