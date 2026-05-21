## 总体判断

不建议合并，需阻断该变更。配置中包含疑似生产支付 API 密钥，且项目当前没有 secret 扫描机制，存在明确的凭据泄露风险。应先移除仓库中的密钥、轮换已暴露密钥，并改用安全的配置注入方式后再考虑合并。

## 主要问题

### Finding：配置中提交了疑似真实支付密钥

```yaml
payment:
  api_url: "https://payments.example.test"
  api_key: "SYNTHETIC_PAYMENT_SECRET_PLACEHOLDER"
  retry: 3
```

- `api_key` 字段包含以 `SYNTHETIC_PAYMENT_SECRET_PLACEHOLDER` 开头的密钥样式值，疑似 live/生产级支付服务密钥。
- 该配置被提交到仓库。
- 背景明确说明项目没有 secret 扫描。

### Finding：缺少密钥管理机制

- 密钥被硬编码在 YAML 配置中。
- 未使用环境变量、密钥管理服务或部署时注入机制。
- 没有 secret 扫描，无法在提交或 CI 阶段自动阻断类似问题。

## 风险与影响

### Risk：密钥泄露

如果该仓库可被多人访问、被 fork、进入 CI 日志或被同步到第三方系统，密钥可能被未授权人员获取。

### Risk：支付服务被滥用

疑似 live 支付密钥一旦可用，攻击者可能调用支付相关 API，造成：

- 非授权交易或退款操作；
- 财务损失；
- 客户数据暴露；
- 账务、审计和合规风险。

### Risk：密钥即使删除也可能仍在 Git 历史中

即使后续提交删除该字段，密钥仍可能存在于 Git 历史、CI 缓存、代码审查系统或镜像仓库中。

### Risk：缺少扫描会导致问题复发

当前项目没有 secret 扫描，未来仍可能再次提交密钥、token、证书或其他敏感配置。

## 测试建议

### Test advice：补充 secret 扫描

建议在以下位置加入 secret 扫描：

- pre-commit hook；
- CI pipeline；
- PR 检查；
- 仓库历史扫描。

扫描规则应至少覆盖：

- `SYNTHETIC_PAYMENT_SECRET_PLACEHOLDER` 类支付密钥；
- API key；
- token；
- private key；
- cloud provider credentials；
- 数据库连接串中的密码。

### Test advice：验证配置改造后的加载逻辑

将配置改为环境变量或密钥管理服务后，应补充测试：

- 当 `PAYMENT_API_KEY` 缺失时，服务应启动失败或返回明确配置错误；
- 当密钥为空字符串时，不应静默使用默认值；
- 不应在日志、错误信息或健康检查接口中输出密钥；
- 测试环境应使用 mock 或测试密钥，不应依赖 live key。

### Test advice：补充 CI 阻断测试

建议新增 CI 检查，确保包含疑似密钥的 PR 会失败，避免类似配置再次进入主分支。

## 不确定性

- Uncertainty：无法确认该 `api_key` 是否真实有效，但其格式和 `SYNTHETIC_PAYMENT_SECRET_PLACEHOLDER` 前缀足以按高风险 secret 处理。
- Uncertainty：无法确认仓库是否公开、是否已有 fork、是否已进入 CI/CD 日志或制品缓存。
- Uncertainty：无法确认支付服务权限范围，需要由支付/安全负责人确认该密钥可执行哪些操作。

## 交接建议

### Security

需要安全负责人介入：

- 立即吊销/轮换该疑似泄露密钥；
- 检查仓库历史、CI 日志、制品缓存、镜像和代码审查系统中是否存在该密钥；
- 评估是否需要执行 Git 历史清理；
- 评估是否存在未授权调用或异常支付活动；
- 建立 secret scanning 策略。

### Backend owner

需要后端负责人修改配置方式：

- 删除硬编码 `api_key`；
- 改为环境变量、密钥管理服务或部署平台 secret 注入；
- 确保启动时进行必要配置校验；
- 避免日志打印敏感配置。

### QA/test owner

需要 QA 或测试负责人补充：

- 配置加载失败路径测试；
- secret 扫描 CI 测试；
- 日志脱敏检查；
- 回归测试，确保支付配置改造后功能仍可用。

### Product owner

如该密钥对应真实支付环境，建议产品/业务负责人确认：

- 是否涉及客户交易；
- 是否需要暂停相关支付功能；
- 是否需要客户、财务或合规侧进一步评估。

## 完成前自检

- 已识别并优先处理密钥泄露风险。
- 未复述完整密钥。
- 已给出阻断合并建议。
- 已建议轮换密钥。
- 已建议改用环境变量或安全密钥注入。
- 已建议补充 secret 扫描和相关测试。
- 已明确安全、后端、产品和 QA 交接事项。
