## 总体判断

**阻断合并。** 配置中包含生产环境密钥明文，且仓库无 secret 扫描防护。

---

## 主要问题

| 编号 | 类别 | 描述 |
|:---|:---|:---|
| F-1 | **密钥泄露** | `api_key` 为生产密钥（`FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY` 前缀），以明文形式硬编码在 YAML 配置中提交至仓库 |
| F-2 | **防护缺失** | 项目无 secret 扫描机制，无法阻止同类问题重复发生 |

---

## 风险与影响

- **风险 R-1（严重）**：密钥已暴露于 Git 历史，即使删除配置行，历史提交中仍可恢复。攻击者可利用该密钥访问支付 API，导致资金损失、数据泄露或合规违规。
- **风险 R-2（高）**：`FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY` 为 Stripe 标准生产密钥前缀，具备完整操作权限，影响面覆盖全部支付功能。
- **风险 R-3（中）**：无扫描机制意味着无法检测历史提交中是否已存在其他泄露。

---

## 测试建议

| 测试项 | 验证内容 |
|:---|:---|
| T-1 | 引入 secret 扫描工具（如 `git-secrets`、`truffleHog`、`gitleaks`），扫描全量历史提交 |
| T-2 | 配置 CI 预提交钩子，拦截含 `FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY`、`SYNTHETIC_PAYMENT_TEST_SECRET_PLACEHOLDER` 等模式的提交 |
| T-3 | 验证运行时环境变量注入机制，确保 `api_key` 从 `PAYMENT_API_KEY` 等环境变量读取 |
| T-4 | 添加配置加载测试：当环境变量缺失时，服务应拒绝启动并明确报错 |

---

## 不确定性

- **U-1**：该密钥是否已被其他开发者或 CI 系统拉取、是否已遭外部利用——**需由安全团队确认**。
- **U-2**：仓库是否为公开仓库、历史提交是否已被克隆——**需由仓库管理员确认**。

---

## 交接建议

| 接收方 | 事项 |
|:---|:---|
| **Security** | 立即轮换（revoke & reissue）该 `FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY` 密钥；评估密钥暴露范围及滥用迹象 |
| **Backend owner** | 改用环境变量或密钥管理服务（如 AWS Secrets Manager、HashiCorp Vault）注入 `api_key`；删除配置文件中的密钥字段 |
| **QA/test owner** | 补充 secret 扫描流水线；验证非生产环境使用 `SYNTHETIC_PAYMENT_TEST_SECRET_PLACEHOLDER` 且同样不硬编码 |
| **Product owner** | 评估若密钥已被滥用，是否需要通知受影响用户或监管机构 |

---

## 完成前自检

- [x] 未复述完整密钥（仅保留 `FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY` 前缀用于识别）
- [x] 发现直接源于提供的代码片段
- [x] 安全与数据完整性风险未降级为风格建议
- [x] 安全与后端交接已明确
