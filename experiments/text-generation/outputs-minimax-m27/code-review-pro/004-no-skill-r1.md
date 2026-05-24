## 安全审查结果

### 风险识别

**高风险：硬编码 API 密钥**

- `api_key` 字段包含明文密钥（`FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY`）
- 密钥直接写入配置文件，缺乏加密或保护
- 若代码库无 secret 扫描，密钥将直接暴露于版本历史

### 建议

1. **阻断合并**：暂缓合并，要求修复后重新提交
2. **轮换密钥**：立即在支付平台生成新密钥并替换
3. **改用环境变量**：将 `api_key` 改为 `${PAYMENT_API_KEY}` 或类似引用，从环境变量读取
4. **补充测试/扫描**：在 CI/CD 中集成 `git-secrets`、`trufflehog` 或 `Gitleaks`，防止敏感信息提交
