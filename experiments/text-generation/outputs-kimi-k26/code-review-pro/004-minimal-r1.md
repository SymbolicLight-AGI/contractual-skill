## 审查结果：阻断合并

### 🔴 严重 - 密钥泄露

**发现：** `api_key` 明文存储生产环境密钥 `FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY`（末尾 `f` 已截断，不还原完整值）。

**风险：**
- 生产环境密钥已暴露于代码仓库历史，即使后续删除仍可被提取
- 无 secret 扫描机制，无法防止类似泄露重复发生

---

### 建议措施

| 优先级 | 行动 | 说明 |
|:---|:---|:---|
| **立即** | **阻断合并** | 当前 PR/MR 不得合并 |
| **立即** | **轮换密钥** | 在支付平台作废 `FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY` 并生成新密钥 |
| **高** | **改用环境变量** | 移除 `api_key` 字段，改为运行时从 `PAYMENT_API_KEY` 读取 |
| **高** | **补充 secret 扫描** | 部署 pre-commit 钩子（如 `git-secrets`、`truffleHog`）及 CI 扫描 |
| **中** | **密钥注入审计** | 确认该密钥是否已泄露至其他分支/镜像/日志 |

---

### 配置修正方向

```yaml
payment:
  api_url: "https://payments.example.test"
  api_key: "${PAYMENT_API_KEY}"  # 或完全移除，由应用层从环境变量读取
  retry: 3
```

**不确定性：** 未提供运行时密钥注入机制的具体实现，需根据项目技术栈补充（如 Kubernetes Secret、Vault 等）。
