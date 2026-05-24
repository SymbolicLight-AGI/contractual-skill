## Review 结论

**阻断合并。** 存在密钥泄露风险。

---

## 问题

| 项 | 说明 |
|:---|:---|
| **风险类型** | 硬编码 API 密钥（`FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY` 前缀表明为生产环境密钥） |
| **影响** | 密钥已暴露于代码仓库历史，即使后续删除仍可被追溯 |
| **当前防护缺失** | 无 secret 扫描机制 |

---

## 建议措施

### 立即执行
- **撤销该密钥**：在支付平台侧立即轮换/吊销 `FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY` 对应密钥
- **审查日志**：检查该密钥是否已被调用，排查未授权访问

### 修复方案
- **改用环境变量注入**：`PAYMENT_API_KEY` 由运行时环境或 secret 管理服务（如 AWS Secrets Manager、HashiCorp Vault）提供
- **配置分离**：区分环境配置，禁止将生产凭证纳入版本控制

### 防护补强
- **引入 secret 扫描**：配置 pre-commit 钩子（如 `git-secrets`、`truffleHog`）及 CI 流水线扫描
- **添加测试**：验证应用启动时能从环境正确读取密钥，缺失时优雅失败

---

## 代码修正方向

```yaml
payment:
  api_url: "https://payments.example.test"
  api_key: ${PAYMENT_API_KEY}  # 从环境变量读取
  retry: 3
```
