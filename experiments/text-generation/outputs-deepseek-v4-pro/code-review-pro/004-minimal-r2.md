**Code Review Findings**

**1. 密钥硬编码泄露（Critical）**

- **位置**：`payment.api_key` 字段
- **问题**：代码中直接写入了明文生产密钥（以 `SYNTHETIC_PAYMENT_SECRET_PLACEHOLDER` 开头的 Stripe 实时密钥）。该配置文件已被提交至代码仓库，意味着密钥已暴露给所有有仓库访问权限的人，且可能永久留存于 Git 历史中。
- **风险**：攻击者可利用泄露的密钥直接操作生产支付系统，造成资金损失、数据泄露或服务滥用。项目缺少密钥扫描，进一步放大了风险。

**阻断合并 & 处置建议**

1. **立即阻断合并**：此配置绝不允许合并至任何分支。
2. **密钥紧急轮换**：立即登录 Stripe 管理后台（或其他支付平台）吊销当前 `SYNTHETIC_PAYMENT_SECRET_PLACEHOLDER` 密钥，并生成新密钥。仓库中已暴露的旧密钥必须视为已被攻陷，不可继续使用。
3. **移除硬编码并使用环境变量**：
   - 将 `api_key` 替换为环境变量引用，例如 `api_key: ${PAYMENT_API_KEY}`（需确保应用支持变量展开）或改为从运行时环境变量读取。
   - 在部署环境中通过安全的密钥管理服务（如 Vault、AWS Secrets Manager）注入该变量，严禁将实际值写入配置文件。
4. **补充安全扫描**：在 CI/CD 流水线中集成密钥扫描工具（truffleHog、git-secrets、detect-secrets 等），并添加 pre-commit hooks，防止未来再次提交硬编码密钥。
5. **补充测试**：为配置加载逻辑编写单元测试，验证在缺少 `PAYMENT_API_KEY` 环境变量时应用能清晰报错，且不会回退至任何默认值或占位符。同时增加一个集成测试，确认正确加载的密钥能成功通过支付服务的认证健康检查。

**其他观察（Informational）**

- `api_url` 使用 `payments.example.test` 域名，如为测试环境，请确保对应密钥为非生产密钥（`SYNTHETIC_PAYMENT_TEST_SECRET_PLACEHOLDER`），并尽快将测试与生产配置分离，避免混淆。
