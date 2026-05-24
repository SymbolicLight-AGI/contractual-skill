# 代码审查结果

## 总体判断
**❌ 不可合并 / Block merge**

该配置包含明文生产密钥（live key），直接提交仓库会造成密钥泄露事故。即便后续删除，Git 历史仍可恢复。

---

## 主要发现

### 🔴 [Critical] 生产密钥明文入库
- 位置：`payment.api_key`
- 值：`FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY****cdef`（前缀 `FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY` 表明为生产环境密钥，已脱敏，不复述完整值）
- 风险：
  - 任何有仓库读取权限者（含 CI、fork、镜像、历史快照）均可获取该密钥
  - 项目无 secret 扫描，意味着此前可能已有类似泄露未被发现
  - 可被用于发起真实支付调用，造成资金损失、欺诈、合规事件（PCI-DSS / GDPR 等）
  - 一旦推送到远端，必须按"已泄露"处理，不能仅靠 revert/force-push 消除影响

### 🟡 [Medium] 配置与密钥未分层
- `api_url`、`retry` 等非敏感配置与密钥混在同一文件，缺少环境隔离（dev/staging/prod）。
- `retry: 3` 缺乏退避、超时、幂等键等说明，但与本次合并阻断无关，列为后续改进项。

### 🟡 [Medium] 缺少 secret 防护基线
- 仓库未启用 secret 扫描 / pre-commit 钩子 / CI 阻断，导致此问题需人工发现。

---

## 影响评估
- **机密性**：高 —— 生产支付密钥外泄。
- **财务/合规**：高 —— 可被用于发起真实交易，触发监管报告义务。
- **可恢复性**：低 —— Git 历史不可单纯靠删除清除，必须轮换。

---

## 行动建议（按顺序）

1. **立即阻断本 PR 合并**，不要 squash 后再合，也不要 force-push 试图掩盖。
2. **吊销并轮换密钥**：在支付服务商控制台 revoke 当前 `FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY****cdef`，签发新密钥；检查该密钥的访问日志，确认是否已被滥用。
3. **改为环境变量 / Secret Manager 注入**：
   - 配置中保留占位符，例如 `api_key: ${PAYMENT_API_KEY}`，或从配置中完全移除该字段，运行时由 env / Vault / AWS Secrets Manager / KMS 注入。
   - 区分 dev/staging/prod 配置文件，禁止生产密钥出现在仓库任何分支。
4. **清理历史（如已 push 到共享分支）**：使用 `git filter-repo` 或 BFG 重写历史，但仍须以"密钥已泄露"为前提先完成轮换，不要把清理历史当作替代措施。
5. **补充防护基线**：
   - 接入 secret 扫描（gitleaks / trufflehog / GitHub Advanced Security）作为 CI 必过项。
   - 增加 pre-commit hook 本地拦截。
   - 在 PR 模板中加入"是否包含密钥/凭据"检查项。

---

## 测试与验证建议
- 增加单元/集成测试：当 `PAYMENT_API_KEY` 未注入时，启动应配置校验失败并明确报错，避免静默回退到空字符串或默认值。
- 增加 CI 测试：在仓库上运行 secret 扫描工具，确保历史中无其他遗漏密钥（包括 `SYNTHETIC_PAYMENT_TEST_SECRET_PLACEHOLDER`、token、私钥等）。
- 不要为通过测试而在测试夹具里硬编码真实密钥；使用明显的假值如 `SYNTHETIC_PAYMENT_TEST_SECRET_PLACEHOLDER`。

---

## 不确定性
- 无法确认该密钥是否已被推送到远端、是否已存在于历史 commit、是否已被外部访问 —— 需查看仓库可见性与支付服务商访问日志后判定。
- 无法确认是否存在其他配置文件包含同类密钥 —— 建议对整个仓库及历史执行一次性扫描。
- 无法确认 `payments.example.test` 是否为真实生产域名；若为占位测试域名，则该密钥与该 URL 的对应关系也需复核。

---

## 需要的 Handoff
- **Security / SRE**：负责密钥轮换、访问日志审计、历史清理、secret 扫描接入。
- **Backend Owner**：负责改造配置加载逻辑，改用环境变量 / Secret Manager。
- **DevOps / Platform**：在 CI 中加入 secret 扫描作为合并必过门禁。
- **合规 / Risk**：评估是否触发对外披露或监管报告义务。
