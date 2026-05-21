结论：不建议合并，需阻断该变更。

## 发现的问题

### 严重级别：高 / 阻断

配置中提交了疑似生产支付 API 密钥：

```yaml
api_key: "SYNTHETIC_PAYMENT_SECRET_PLACEHOLDER********"
```

这是敏感凭据泄露风险。由于该配置已被提交到仓库，且项目没有 secret 扫描，存在以下风险：

- 密钥可能已被仓库访问者、CI 日志、缓存、镜像或分支历史获取。
- 如果是 live/production key，可能导致支付接口被未授权调用。
- 即使后续删除该配置，密钥仍可能存在于 Git 历史中。

## 合并建议

当前变更应阻断合并，直到完成以下处理：

1. 立即从配置文件中移除明文密钥。
2. 将密钥改为通过环境变量或安全的 secret manager 注入，例如：

```yaml
payment:
  api_url: "https://payments.example.test"
  api_key: "${PAYMENT_API_KEY}"
  retry: 3
```

3. 轮换当前已暴露的支付 API 密钥。
   - 不应继续使用该密钥。
   - 需要在支付平台侧吊销旧密钥并生成新密钥。
4. 检查 Git 历史、CI 日志、构建产物、容器镜像等位置是否已经包含该密钥。
5. 为仓库补充 secret 扫描机制，例如：
   - pre-commit secret scan
   - CI secret scan
   - 阻断包含 `SYNTHETIC_PAYMENT_SECRET_PLACEHOLDER`、API key、token 等模式的提交
6. 补充配置加载相关测试：
   - 缺少 `PAYMENT_API_KEY` 时应明确失败，而不是使用空值或默认弱配置。
   - 测试生产环境配置不得包含明文 secret。
   - 测试配置模板只包含占位符，不包含真实凭据。

## 其他建议

- 如果 `https://payments.example.test` 是测试域名，需要确认该配置是否误用了 live key。
- 建议提供 `config.example.yaml` 或文档说明所需环境变量，但不要包含真实密钥。
- 不建议通过简单删除当前行来“修复”，因为已提交过的密钥仍应视为泄露并执行轮换。
