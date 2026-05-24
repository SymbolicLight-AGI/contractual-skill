## Review 结论：不建议合并 / 必须阻断

### Findings

#### 高危：疑似生产支付 API 密钥被提交到仓库

配置中包含 `payment.api_key`，值形态类似真实 live secret key，例如以 `FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY` 开头。由于该配置已提交到仓库，且项目没有 secret 扫描，这存在明确的密钥泄露风险。

不要合并当前变更。

### Impact

如果该密钥是真实有效的生产支付密钥，可能导致：

- 未授权调用支付服务 API
- 资金、订单、退款等敏感操作被滥用
- 支付数据或客户相关信息泄露
- 后续即使删除该行，密钥仍可能存在于 Git 历史中
- 缺少 secret 扫描会导致类似问题持续发生且难以及时发现

### 必须修改

1. **立即从配置文件中移除明文密钥**
   - 不应把 `api_key` 写入仓库中的 YAML。
   - 改为从环境变量或密钥管理系统读取，例如：
     - `PAYMENT_API_KEY`
     - CI/CD Secret
     - 云厂商 Secret Manager / Vault 等

2. **立即轮换该支付 API 密钥**
   - 假设该密钥已经泄露。
   - 在支付平台吊销当前密钥，生成新密钥。
   - 确认旧密钥不可再使用。

3. **清理仓库历史**
   - 如果该密钥已进入 Git 历史，需要评估是否清理历史记录。
   - 即使清理历史，也不能替代密钥轮换。

4. **补充 secret 扫描**
   - 在本地 pre-commit、CI pipeline、PR 检查中加入 secret scanning。
   - 扫描规则应覆盖常见支付密钥格式、`FAKE_PAYMENT_TOKEN_PREFIX_FOR_SYNTHETIC_TEST_ONLY` / `SYNTHETIC_PAYMENT_TEST_SECRET_PREFIX` 等模式。
   - PR 中一旦发现疑似密钥，应直接失败。

### 测试 / 验证建议

- 增加配置加载测试，确认 `payment.api_key` 来自环境变量或 secret manager，而不是仓库文件。
- 增加 CI 检查：
  - 仓库中不得出现明文 `api_key`、`secret`、`token` 等敏感配置。
  - 对新增 YAML / JSON / env 示例文件执行 secret 扫描。
- 增加启动时校验：
  - 缺少 `PAYMENT_API_KEY` 时服务应启动失败或进入明确错误状态。
  - 不应使用空字符串、占位符或默认密钥继续运行。

### 不确定性

- 无法仅凭片段确认该密钥是否真实有效。
- 但由于其格式像 live 支付密钥，且已提交到仓库，应按已泄露处理。

### Follow-up Owners

- **Security**：确认泄露范围、推动密钥轮换、添加 secret scanning。
- **Backend / Platform**：改造配置加载方式，改用环境变量或密钥管理系统。
- **Testing / CI**：补充 secret 扫描和配置加载相关测试。

### 合并建议

当前变更应阻断合并。完成密钥移除、密钥轮换、配置改造、secret 扫描补充后，再重新提交 review。
