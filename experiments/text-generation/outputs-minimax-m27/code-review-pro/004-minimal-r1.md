## 代码审查结果

### 🔴 严重风险

**密钥泄露 (P0 - 阻断合并)**

- `api_key` 字段包含有效密钥（Stripe live 密钥 `SYNTHETIC_PAYMENT_SECRET_PLACEHOLDER****`），已明文硬编码并提交至仓库
- 即使后续删除该配置，密钥仍存于 Git 历史中
- 项目无 secret 扫描机制，无法预防此类泄露

### 建议措施

1. **阻断合并** — 此配置不应合并，需立即回滚
2. **轮换密钥** — 在 Stripe Dashboard 中撤销当前密钥，生成新密钥
3. **改用环境变量** — 将 `api_key` 替换为 `${PAYMENT_API_KEY}`，运行时从环境变量注入
4. **补充测试/扫描** — 引入 secret 扫描工具（如 TruffleHog、Gitleaks、GitGuardian）至 CI 流程
