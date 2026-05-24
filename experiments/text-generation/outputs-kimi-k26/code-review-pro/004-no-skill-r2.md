## Review Result: 阻断合并

### 风险识别
- **硬编码密钥泄露**：`api_key` 为生产环境密钥（`FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY` 前缀），存在高严重度泄露风险
- **无 secret 扫描**：仓库缺乏自动化检测机制，无法预防同类问题复发

### 处理建议

| 优先级 | 事项 | 操作 |
|:---|:---|:---|
| P0 | 阻断合并 | 立即拒绝该 PR，禁止含密钥的提交进入主分支 |
| P0 | 密钥轮换 | 作废当前 `FAKE_PAYMENT_TOKEN_FOR_SYNTHETIC_TEST_ONLY` 密钥，重新生成并替换 |
| P1 | 改用环境变量 | 移除 YAML 中的 `api_key` 字段，改为从 `PAYMENT_API_KEY` 等环境变量读取 |
| P1 | 补充扫描机制 | 引入 secret scanning 工具（如 GitHub Secret Scanning、truffleHog、gitleaks）并配置 pre-commit 钩子 |
| P2 | 补充测试 | 添加配置加载单元测试，验证环境变量缺失时抛出明确错误；增加 secret 扫描到 CI 流水线 |
