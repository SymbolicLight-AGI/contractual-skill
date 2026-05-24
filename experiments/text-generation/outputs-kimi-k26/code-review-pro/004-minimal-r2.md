## 审查结果：阻断合并

### 严重风险：密钥泄露

| 项目 | 详情 |
|:---|:---|
| **位置** | `payment.api_key` |
| **类型** | 硬编码生产环境密钥（`FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY` 前缀表明 Stripe 生产密钥） |
| **影响** | 密钥已暴露于代码仓库历史，即使删除仍可被追溯 |

### 即时措施

1. **阻断合并** — 当前 PR 不可合并
2. **密钥轮换** — 立即在支付服务商处吊销并重新生成 `FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY*` 密钥
3. **历史清理** — 评估是否需要轮换仓库或执行 `git filter-repo` 清理（注：公开仓库历史极难彻底清除）

### 配置修正建议

```yaml
payment:
  api_url: "https://payments.example.test"
  api_key: ${PAYMENT_API_KEY}  # 从环境变量读取
  retry: 3
```

### 工程防护建议

| 层级 | 措施 |
|:---|:---|
| **CI 强制** | 引入 `truffleHog` / `git-secrets` / `gitleaks` 扫描，配置为 pre-commit 与 CI 双卡点 |
| **代码规范** | 将 `.env*.local`、`*secret*` 加入 `.gitignore` 模板；禁止 `FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY`、`SYNTHETIC_PAYMENT_TEST_SECRET_PLACEHOLDER` 等模式出现在提交中 |
| **密钥管理** | 生产密钥托管于 Vault / AWS Secrets Manager / Azure Key Vault，应用启动时注入 |
| **测试补充** | 添加配置加载单元测试，断言 `api_key` 符合环境变量引用格式或从 Vault 获取；添加扫描工具空跑测试，确保规则集生效 |

### 不确定性

- 仓库是否为公开仓库未知（影响泄露面评估）
- 密钥是否已被推送至远程仓库未知（影响紧急程度）
