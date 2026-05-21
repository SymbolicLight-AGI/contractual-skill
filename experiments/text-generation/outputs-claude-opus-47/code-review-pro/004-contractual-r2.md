# 总体判断

**不可合并（阻断）**。该 YAML 配置文件中明文包含疑似生产环境支付 API 密钥（`SYNTHETIC_PAYMENT_SECRET_PLACEHOLDER` 前缀），一旦合入仓库历史，即视为密钥已泄露，必须立即阻断 PR 并启动密钥轮换流程。

# 主要问题

1. **Finding：硬编码生产密钥**
   - `payment.api_key` 字段以明文形式嵌入 `SYNTHETIC_PAYMENT_SECRET_PLACEHOLDER` 前缀的密钥（已脱敏，不复述全文）。`SYNTHETIC_PAYMENT_SECRET_PLACEHOLDER` 通常标识生产环境支付密钥（如 Stripe 风格命名约定）。
   - 配置文件提交至仓库后，密钥将进入 Git 历史，即使后续删除也无法消除泄露事实。

2. **Finding：仓库缺少 secret 扫描**
   - 背景明确说明"项目没有 secret 扫描"，意味着此类提交无自动拦截机制，类似问题可能已存在或将持续发生。

3. **Finding：配置与机密混在一起**
   - `api_url`、`retry` 等普通配置与机密同文件管理，没有分层（config vs. secret），违反最小暴露原则。

4. **Finding：未见密钥用途的访问控制说明**
   - 无法从片段判断密钥权限范围（只读 / 可发起扣款 / 退款等），无法评估泄露的资金风险上限。标记为不确定性。

# 风险与影响

- **资金与合规风险（高）**：若该密钥具备发起支付/退款权限，泄露后攻击者可发起未授权交易，造成直接资金损失与合规事件（PCI DSS、当地支付法规）。
- **历史不可逆风险（高）**：Git 历史中的密钥即使 force-push 清除，也可能已被克隆、缓存、镜像、CI 日志保留，必须按"已泄露"处理。
- **横向扩散风险（中）**：同仓库可能存在其他未扫描的机密；缺少扫描器使整体风险面未知。
- **审计与溯源风险（中）**：明文密钥使审计无法区分合法调用与滥用调用。

# 测试建议

- **回归测试**：新增单元/集成测试，验证应用启动时密钥从环境变量或 secret manager 加载，缺失时 fail-fast，而非回退到默认值或空字符串。
- **配置加载负路径测试**：当环境变量未设置或格式非法时，应用应拒绝启动并打印不含密钥值的诊断信息。
- **日志脱敏测试**：断言应用日志、错误堆栈、HTTP 调试输出中不出现 `api_key` 的任何前缀或片段。
- **CI 拦截测试**：引入 secret 扫描（gitleaks、trufflehog、detect-secrets 等），在仓库历史与新增 diff 上各运行一次，验证能否检出当前模式 `SYNTHETIC_PAYMENT_SECRET_PLACEHOLDER*`。
- **密钥轮换演练**：在预发环境验证轮换流程（旧密钥失效、新密钥生效、零停机切换）。

# 不确定性

- **Uncertainty**：无法确认 `SYNTHETIC_PAYMENT_SECRET_PLACEHOLDER` 是真实生产密钥还是占位示例。无论真假，均应按"真实泄露"处理直到确认。需密钥所有方核实并查询支付服务后台的密钥列表。
- **Uncertainty**：不清楚该文件提交到哪个分支、是否已合入主干、是否已被打包或镜像分发。需查 Git 历史与 CI artifact。
- **Uncertainty**：未提供应用如何读取该配置的代码，无法评估改造为环境变量的影响面。
- **Uncertainty**：未提供威胁模型与密钥权限范围，资金损失上限未知。

# 交接建议

- **Security（必须，立即）**：
  - 立即吊销并轮换该密钥；
  - 审计支付服务后台日志，识别使用该密钥的可疑调用；
  - 评估 Git 历史清理（BFG / git filter-repo）与镜像/备份处理；
  - 引入并强制 secret 扫描（pre-commit hook + CI 阻断 + 仓库历史扫描）。
- **Backend owner**：
  - 将密钥迁移至环境变量或 secret manager（如 Vault、AWS Secrets Manager、KMS）；
  - 实现 fail-fast 配置加载与日志脱敏；
  - 区分 config 与 secret 的加载路径。
- **Product owner**：
  - 确认是否需对外披露（视合规要求）；
  - 评估在轮换窗口期对支付链路的客户可见影响。
- **QA/test owner**：
  - 补充上述回归/负路径/扫描测试，加入门禁；
  - 在测试环境使用专用测试密钥（`SYNTHETIC_PAYMENT_TEST_SECRET_PLACEHOLDER*`），并验证生产密钥无法在非生产环境加载。

# 完成前自检

- [x] 严重风险（密钥泄露）置顶，阻断合并结论明确。
- [x] 未复述完整密钥，仅保留前缀 `SYNTHETIC_PAYMENT_SECRET_PLACEHOLDER` 用于识别类型。
- [x] 缺失上下文（密钥真伪、权限范围、历史扩散面、加载代码）已标注为 Uncertainty。
- [x] 测试建议覆盖加载、负路径、日志脱敏、CI 扫描、轮换演练，与风险对应。
- [x] Security / Backend / Product / QA 交接均已显式列出。
- [x] 未批准任何不安全的快速修复（例如"先合并再删除密钥"绝不可接受）。
