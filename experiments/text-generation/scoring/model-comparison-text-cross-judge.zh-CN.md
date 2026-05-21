# 纯文本输出交叉评分对比

## 评分覆盖

| 生成模型 | 评分模型 | 评分条数 |
| --- | --- | ---: |
| gpt-5.5 | claude-opus-4-7 | 120 |
| DeepSeek-V4-Pro | claude-opus-4-7 | 120 |
| qwen3.6-plus | claude-opus-4-7 | 120 |
| GLM-5.1 | claude-opus-4-7 | 120 |
| MiniMax-M2.7 | claude-opus-4-7 | 120 |
| Kimi-K2.6 | claude-opus-4-7 | 120 |
| gemini-3.1-pro-preview | claude-opus-4-7 | 120 |
| DeepSeek-V4-Pro | gpt-5.5 | 120 |
| qwen3.6-plus | gpt-5.5 | 120 |
| claude-opus-4-7 | gpt-5.5 | 120 |
| GLM-5.1 | gpt-5.5 | 120 |
| MiniMax-M2.7 | gpt-5.5 | 120 |
| Kimi-K2.6 | gpt-5.5 | 120 |
| gemini-3.1-pro-preview | gpt-5.5 | 120 |

## 输出级平均评分

| 生成模型 | 变体 | 输出数 | 平均 judge 数 | 总分均值 | 标准差 | 关键错误 | 结构 | 证据 | 交接 | 维护 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| gpt-5.5 | no-skill | 30 | 1.0 | 4.617 | 0.351 | 0 | 4.867 | 4.433 | 3.933 | 4.767 |
| gpt-5.5 | minimal | 30 | 1.0 | 4.767 | 0.184 | 0 | 4.967 | 4.500 | 4.267 | 4.900 |
| gpt-5.5 | plain-expanded | 30 | 1.0 | 4.922 | 0.143 | 0 | 5.000 | 4.867 | 4.767 | 4.933 |
| gpt-5.5 | contractual | 30 | 1.0 | 4.989 | 0.042 | 0 | 5.000 | 5.000 | 5.000 | 5.000 |
| DeepSeek-V4-Pro | no-skill | 30 | 2.0 | 4.500 | 0.302 | 7 | 4.833 | 4.250 | 3.917 | 4.583 |
| DeepSeek-V4-Pro | minimal | 30 | 2.0 | 4.703 | 0.260 | 4 | 4.950 | 4.383 | 4.283 | 4.800 |
| DeepSeek-V4-Pro | plain-expanded | 30 | 2.0 | 4.864 | 0.099 | 1 | 5.000 | 4.650 | 4.817 | 4.783 |
| DeepSeek-V4-Pro | contractual | 30 | 2.0 | 4.939 | 0.124 | 1 | 4.967 | 4.833 | 4.983 | 4.950 |
| qwen3.6-plus | no-skill | 30 | 2.0 | 4.644 | 0.243 | 3 | 4.883 | 4.467 | 4.133 | 4.867 |
| qwen3.6-plus | minimal | 30 | 2.0 | 4.828 | 0.093 | 0 | 5.000 | 4.517 | 4.517 | 4.967 |
| qwen3.6-plus | plain-expanded | 30 | 2.0 | 4.883 | 0.284 | 2 | 4.950 | 4.733 | 4.933 | 4.917 |
| qwen3.6-plus | contractual | 30 | 2.0 | 4.964 | 0.097 | 1 | 4.967 | 4.917 | 5.000 | 5.000 |
| GLM-5.1 | no-skill | 30 | 2.0 | 4.636 | 0.325 | 2 | 4.833 | 4.533 | 4.167 | 4.883 |
| GLM-5.1 | minimal | 30 | 2.0 | 4.733 | 0.247 | 2 | 4.933 | 4.467 | 4.583 | 4.817 |
| GLM-5.1 | plain-expanded | 30 | 2.0 | 4.936 | 0.100 | 2 | 5.000 | 4.800 | 4.933 | 4.983 |
| GLM-5.1 | contractual | 30 | 2.0 | 4.928 | 0.092 | 1 | 4.983 | 4.767 | 4.967 | 4.983 |
| MiniMax-M2.7 | no-skill | 30 | 2.0 | 4.561 | 0.498 | 6 | 4.783 | 4.400 | 4.233 | 4.767 |
| MiniMax-M2.7 | minimal | 30 | 2.0 | 4.694 | 0.275 | 8 | 4.900 | 4.317 | 4.500 | 4.867 |
| MiniMax-M2.7 | plain-expanded | 30 | 2.0 | 4.864 | 0.166 | 3 | 5.000 | 4.483 | 4.800 | 4.967 |
| MiniMax-M2.7 | contractual | 30 | 2.0 | 4.856 | 0.145 | 4 | 4.967 | 4.533 | 4.950 | 4.967 |
| Kimi-K2.6 | no-skill | 30 | 2.0 | 4.692 | 0.347 | 4 | 4.850 | 4.500 | 4.317 | 4.917 |
| Kimi-K2.6 | minimal | 30 | 2.0 | 4.833 | 0.209 | 3 | 4.950 | 4.567 | 4.700 | 4.933 |
| Kimi-K2.6 | plain-expanded | 30 | 2.0 | 4.889 | 0.176 | 4 | 4.967 | 4.700 | 4.917 | 4.967 |
| Kimi-K2.6 | contractual | 30 | 2.0 | 4.925 | 0.070 | 0 | 4.900 | 4.817 | 4.983 | 4.983 |
| gemini-3.1-pro-preview | no-skill | 30 | 2.0 | 4.714 | 0.283 | 1 | 4.850 | 4.733 | 4.283 | 4.817 |
| gemini-3.1-pro-preview | minimal | 30 | 2.0 | 4.875 | 0.136 | 0 | 4.967 | 4.700 | 4.717 | 4.950 |
| gemini-3.1-pro-preview | plain-expanded | 30 | 2.0 | 4.906 | 0.129 | 1 | 4.983 | 4.783 | 4.867 | 4.950 |
| gemini-3.1-pro-preview | contractual | 30 | 2.0 | 4.953 | 0.092 | 0 | 4.967 | 4.900 | 4.967 | 5.000 |
| claude-opus-4-7 | no-skill | 30 | 1.0 | 4.867 | 0.202 | 3 | 5.000 | 4.633 | 4.700 | 5.000 |
| claude-opus-4-7 | minimal | 30 | 1.0 | 4.928 | 0.104 | 0 | 5.000 | 4.767 | 4.833 | 4.967 |
| claude-opus-4-7 | plain-expanded | 30 | 1.0 | 4.972 | 0.099 | 1 | 5.000 | 4.867 | 5.000 | 5.000 |
| claude-opus-4-7 | contractual | 30 | 1.0 | 4.983 | 0.091 | 1 | 5.000 | 5.000 | 5.000 | 5.000 |

## 配对差异

| 生成模型 | 对比 | n | 平均差 | 标准差 | 左侧更高 | 持平 | 右侧更高 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| gpt-5.5 | contractual - no-skill | 30 | 0.372 | 0.327 | 29 | 1 | 0 |
| gpt-5.5 | contractual - minimal | 30 | 0.222 | 0.182 | 24 | 6 | 0 |
| gpt-5.5 | contractual - plain-expanded | 30 | 0.067 | 0.149 | 9 | 20 | 1 |
| gpt-5.5 | plain-expanded - minimal | 30 | 0.156 | 0.185 | 19 | 9 | 2 |
| DeepSeek-V4-Pro | contractual - no-skill | 30 | 0.439 | 0.311 | 28 | 1 | 1 |
| DeepSeek-V4-Pro | contractual - minimal | 30 | 0.236 | 0.288 | 26 | 0 | 4 |
| DeepSeek-V4-Pro | contractual - plain-expanded | 30 | 0.075 | 0.146 | 20 | 6 | 4 |
| DeepSeek-V4-Pro | plain-expanded - minimal | 30 | 0.161 | 0.245 | 21 | 7 | 2 |
| qwen3.6-plus | contractual - no-skill | 30 | 0.319 | 0.230 | 30 | 0 | 0 |
| qwen3.6-plus | contractual - minimal | 30 | 0.136 | 0.141 | 24 | 4 | 2 |
| qwen3.6-plus | contractual - plain-expanded | 30 | 0.081 | 0.224 | 12 | 15 | 3 |
| qwen3.6-plus | plain-expanded - minimal | 30 | 0.056 | 0.294 | 21 | 5 | 4 |
| GLM-5.1 | contractual - no-skill | 30 | 0.292 | 0.303 | 26 | 2 | 2 |
| GLM-5.1 | contractual - minimal | 30 | 0.194 | 0.214 | 22 | 6 | 2 |
| GLM-5.1 | contractual - plain-expanded | 30 | -0.008 | 0.088 | 6 | 14 | 10 |
| GLM-5.1 | plain-expanded - minimal | 30 | 0.203 | 0.249 | 22 | 4 | 4 |
| MiniMax-M2.7 | contractual - no-skill | 30 | 0.294 | 0.523 | 20 | 6 | 4 |
| MiniMax-M2.7 | contractual - minimal | 30 | 0.161 | 0.284 | 17 | 6 | 7 |
| MiniMax-M2.7 | contractual - plain-expanded | 30 | -0.008 | 0.244 | 9 | 9 | 12 |
| MiniMax-M2.7 | plain-expanded - minimal | 30 | 0.169 | 0.314 | 17 | 7 | 6 |
| Kimi-K2.6 | contractual - no-skill | 30 | 0.233 | 0.351 | 22 | 4 | 4 |
| Kimi-K2.6 | contractual - minimal | 30 | 0.092 | 0.220 | 17 | 7 | 6 |
| Kimi-K2.6 | contractual - plain-expanded | 30 | 0.036 | 0.169 | 11 | 11 | 8 |
| Kimi-K2.6 | plain-expanded - minimal | 30 | 0.056 | 0.154 | 15 | 8 | 7 |
| gemini-3.1-pro-preview | contractual - no-skill | 30 | 0.239 | 0.280 | 24 | 3 | 3 |
| gemini-3.1-pro-preview | contractual - minimal | 30 | 0.078 | 0.143 | 16 | 11 | 3 |
| gemini-3.1-pro-preview | contractual - plain-expanded | 30 | 0.047 | 0.123 | 11 | 15 | 4 |
| gemini-3.1-pro-preview | plain-expanded - minimal | 30 | 0.031 | 0.136 | 12 | 12 | 6 |
| claude-opus-4-7 | contractual - no-skill | 30 | 0.117 | 0.232 | 15 | 14 | 1 |
| claude-opus-4-7 | contractual - minimal | 30 | 0.056 | 0.126 | 10 | 19 | 1 |
| claude-opus-4-7 | contractual - plain-expanded | 30 | 0.011 | 0.138 | 3 | 26 | 1 |
| claude-opus-4-7 | plain-expanded - minimal | 30 | 0.044 | 0.123 | 10 | 18 | 2 |

## 解释边界

- 本表排除同模型自评。
- 除 `gpt-5.5` 和 `claude-opus-4-7` 外，其余生成模型输出使用两个非生成模型 judge 的输出级平均分。
- `gpt-5.5` 输出由 `claude-opus-4-7` 评分，`claude-opus-4-7` 输出由 `gpt-5.5` 评分。
- 分数反映离线合成任务上的模型辅助评分，不是多人类评审。
