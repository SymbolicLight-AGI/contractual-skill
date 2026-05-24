# 密钥泄露风险审查结果

## 风险识别
配置中硬编码了生产环境支付服务的 API 密钥（`api_key` 字段，以 `FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY` 开头），存在真实密钥意外提交到仓库的风险。该密钥未脱敏，且项目未启用 secret 扫描，无法自动拦截泄露。

## 阻断建议
- 立即阻断该合并请求（hold merge），禁止将有明文密钥的配置合入主线。
- 将当前提交标记为敏感，避免被进一步分发。

## 密钥轮换
- 联系支付服务管理方，于服务端吊销泄露的 `FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY` 密钥。
- 生成新密钥，确保旧密钥完全失效，避免已被暴露的凭据被恶意使用。

## 配置修改方案
- 移除硬编码的 `api_key` 值，改用占位符或直接删除该字段。
- 在部署环境中通过环境变量注入密钥，例如 `PAYMENT_API_KEY`，配置改为：  
  ```yaml
  payment:
    api_url: "https://payments.example.test"
    api_key: ${PAYMENT_API_KEY}
    retry: 3
  ```
- 确认环境变量在运行时正确加载且不会被打印到日志。

## 补充措施
- 在 CI/CD 流程中集成 secrets 扫描工具（如 git-secrets、truffleHog、Gitleaks）并设为必须通过的门禁。
- 增加测试用例验证：配置加载时未使用明文密钥，配置缺少环境变量时能给出明确错误。
- 审查仓库历史，确认该密钥是否已出现在其他分支或标签中；若有则一并清理并强制轮换。
- 更新项目文档，明确禁止提交任何形式的真实凭证。
