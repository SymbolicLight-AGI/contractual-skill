## Review: payment 配置

### 发现项与严重级别

| 发现 | 严重级别 |
|------|---------|
| 生产环境密钥硬编码于仓库 | **阻断** |
| 密钥格式可识别（`FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY` 前缀） | **高** |
| 无 secret 扫描机制 | **中** |

---

### 影响分析

- **密钥暴露范围**：已提交至仓库，历史记录永久留存，任何有仓库访问权限的人员均可获取
- **业务风险**：支付 API 密钥泄露可导致资金损失、交易篡改、退款欺诈
- **合规风险**：支付卡行业数据安全标准（PCI-DSS）要求密钥保护

---

### 阻断合并

**建议立即阻断该 PR/合并请求**，原因：
- 生产密钥 `FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY*` 已存在于提交历史中
- 仅删除文件无法从历史中移除密钥

---

### 修复建议

| 优先级 | 措施 | 负责人 |
|--------|------|--------|
| P0 | **轮换密钥**：立即在支付服务商处吊销并重新生成 `FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY*` 密钥 | Security / Backend |
| P0 | **清理历史**：使用 `git-filter-repo` 或 BFG 从 Git 历史中彻底移除该密钥 | Backend |
| P1 | **改用环境变量**：`api_key` 改为 `${PAYMENT_API_KEY}` 或引用 secret 管理系统 | Backend |
| P1 | **启用 secret 扫描**：配置 GitHub Advanced Security / GitLab Secret Detection / pre-commit `detect-secrets` | Security / DevOps |

---

### 测试与扫描建议

- 添加 CI 流水线步骤：阻止含 `FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY`、`SYNTHETIC_PAYMENT_TEST_SECRET_PLACEHOLDER` 等模式的提交
- 集成 secret 扫描工具（如 TruffleHog、GitLeaks）至 pre-commit hook
- 验证配置加载单元测试：确保缺失环境变量时应用明确失败（而非使用默认值）

---

### 不确定性

- 该密钥是否已被其他服务/人员获取：**未知**
- 支付服务商是否支持审计密钥使用记录：**需 Security 确认**

---

### 所需交接

- **Security 团队**：密钥轮换、泄露影响评估、合规审查
- **Backend 团队**：配置重构、历史清理、环境变量改造
- **DevOps 团队**：CI 扫描规则部署
