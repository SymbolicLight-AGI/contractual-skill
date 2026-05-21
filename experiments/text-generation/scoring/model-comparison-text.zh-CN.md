# 纯文本输出多模型对比

## 独立评分汇总

| 生成模型 | 变体 | n | 总分均值 | 标准差 | 关键错误 | 结构 | 证据 | 交接 | 维护 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| gpt-5.5 | no-skill | 30 | 4.617 | 0.351 | 0 | 4.867 | 4.433 | 3.933 | 4.767 |
| gpt-5.5 | minimal | 30 | 4.767 | 0.184 | 0 | 4.967 | 4.500 | 4.267 | 4.900 |
| gpt-5.5 | plain-expanded | 30 | 4.922 | 0.143 | 0 | 5.000 | 4.867 | 4.767 | 4.933 |
| gpt-5.5 | contractual | 30 | 4.989 | 0.042 | 0 | 5.000 | 5.000 | 5.000 | 5.000 |
| DeepSeek-V4-Pro | no-skill | 30 | 4.428 | 0.363 | 0 | 4.800 | 4.267 | 3.733 | 4.367 |
| DeepSeek-V4-Pro | minimal | 30 | 4.622 | 0.287 | 0 | 4.900 | 4.333 | 3.967 | 4.667 |
| DeepSeek-V4-Pro | plain-expanded | 30 | 4.833 | 0.158 | 0 | 5.000 | 4.767 | 4.667 | 4.633 |
| DeepSeek-V4-Pro | contractual | 30 | 4.972 | 0.088 | 0 | 5.000 | 4.967 | 4.967 | 4.933 |
| qwen3.6-plus | no-skill | 30 | 4.544 | 0.369 | 0 | 4.800 | 4.333 | 3.867 | 4.733 |
| qwen3.6-plus | minimal | 30 | 4.778 | 0.119 | 0 | 5.000 | 4.467 | 4.300 | 4.933 |
| qwen3.6-plus | plain-expanded | 30 | 4.922 | 0.174 | 0 | 4.967 | 4.833 | 4.900 | 4.900 |
| qwen3.6-plus | contractual | 30 | 4.994 | 0.030 | 0 | 5.000 | 5.000 | 5.000 | 5.000 |
| GLM-5.1 | no-skill | 30 | 4.778 | 0.397 | 0 | 4.867 | 4.800 | 4.400 | 4.867 |
| GLM-5.1 | minimal | 30 | 4.767 | 0.329 | 0 | 4.900 | 4.667 | 4.567 | 4.733 |
| GLM-5.1 | plain-expanded | 30 | 4.978 | 0.085 | 0 | 5.000 | 4.967 | 4.967 | 4.967 |
| GLM-5.1 | contractual | 30 | 5.000 | 0.000 | 0 | 5.000 | 5.000 | 5.000 | 5.000 |
| MiniMax-M2.7 | no-skill | 30 | 4.689 | 0.592 | 1 | 4.800 | 4.700 | 4.467 | 4.767 |
| MiniMax-M2.7 | minimal | 30 | 4.822 | 0.374 | 0 | 4.833 | 4.800 | 4.667 | 4.833 |
| MiniMax-M2.7 | plain-expanded | 30 | 4.939 | 0.198 | 0 | 5.000 | 4.833 | 4.900 | 4.933 |
| MiniMax-M2.7 | contractual | 30 | 4.961 | 0.084 | 0 | 5.000 | 4.833 | 5.000 | 5.000 |
| Kimi-K2.6 | no-skill | 30 | 4.794 | 0.428 | 0 | 4.833 | 4.767 | 4.567 | 4.867 |
| Kimi-K2.6 | minimal | 30 | 4.944 | 0.141 | 0 | 4.933 | 4.933 | 4.867 | 4.933 |
| Kimi-K2.6 | plain-expanded | 30 | 4.956 | 0.157 | 0 | 4.967 | 4.900 | 4.933 | 4.967 |
| Kimi-K2.6 | contractual | 30 | 5.000 | 0.000 | 0 | 5.000 | 5.000 | 5.000 | 5.000 |
| gemini-3.1-pro-preview | no-skill | 30 | 4.783 | 0.374 | 0 | 4.867 | 4.867 | 4.433 | 4.800 |
| gemini-3.1-pro-preview | minimal | 30 | 4.911 | 0.209 | 0 | 4.967 | 4.833 | 4.833 | 4.900 |
| gemini-3.1-pro-preview | plain-expanded | 30 | 4.933 | 0.173 | 0 | 4.967 | 4.867 | 4.933 | 4.900 |
| gemini-3.1-pro-preview | contractual | 30 | 4.989 | 0.061 | 0 | 5.000 | 4.967 | 5.000 | 5.000 |

## 配对差异

| 生成模型 | 对比 | n | 平均差 | 标准差 | 左侧更高 | 持平 | 右侧更高 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| gpt-5.5 | contractual - no-skill | 30 | 0.372 | 0.327 | 29 | 1 | 0 |
| gpt-5.5 | contractual - minimal | 30 | 0.222 | 0.182 | 24 | 6 | 0 |
| gpt-5.5 | contractual - plain-expanded | 30 | 0.067 | 0.149 | 9 | 20 | 1 |
| gpt-5.5 | plain-expanded - minimal | 30 | 0.156 | 0.185 | 19 | 9 | 2 |
| DeepSeek-V4-Pro | contractual - no-skill | 30 | 0.544 | 0.384 | 29 | 1 | 0 |
| DeepSeek-V4-Pro | contractual - minimal | 30 | 0.350 | 0.311 | 27 | 2 | 1 |
| DeepSeek-V4-Pro | contractual - plain-expanded | 30 | 0.139 | 0.186 | 19 | 8 | 3 |
| DeepSeek-V4-Pro | plain-expanded - minimal | 30 | 0.211 | 0.255 | 20 | 8 | 2 |
| qwen3.6-plus | contractual - no-skill | 30 | 0.450 | 0.359 | 30 | 0 | 0 |
| qwen3.6-plus | contractual - minimal | 30 | 0.217 | 0.125 | 28 | 2 | 0 |
| qwen3.6-plus | contractual - plain-expanded | 30 | 0.072 | 0.173 | 7 | 23 | 0 |
| qwen3.6-plus | plain-expanded - minimal | 30 | 0.144 | 0.226 | 22 | 5 | 3 |
| GLM-5.1 | contractual - no-skill | 30 | 0.222 | 0.397 | 11 | 19 | 0 |
| GLM-5.1 | contractual - minimal | 30 | 0.233 | 0.329 | 13 | 17 | 0 |
| GLM-5.1 | contractual - plain-expanded | 30 | 0.022 | 0.085 | 2 | 28 | 0 |
| GLM-5.1 | plain-expanded - minimal | 30 | 0.211 | 0.355 | 13 | 15 | 2 |
| MiniMax-M2.7 | contractual - no-skill | 30 | 0.272 | 0.575 | 10 | 17 | 3 |
| MiniMax-M2.7 | contractual - minimal | 30 | 0.139 | 0.366 | 8 | 17 | 5 |
| MiniMax-M2.7 | contractual - plain-expanded | 30 | 0.022 | 0.222 | 3 | 22 | 5 |
| MiniMax-M2.7 | plain-expanded - minimal | 30 | 0.117 | 0.449 | 8 | 18 | 4 |
| Kimi-K2.6 | contractual - no-skill | 30 | 0.206 | 0.428 | 7 | 23 | 0 |
| Kimi-K2.6 | contractual - minimal | 30 | 0.056 | 0.141 | 5 | 25 | 0 |
| Kimi-K2.6 | contractual - plain-expanded | 30 | 0.044 | 0.157 | 4 | 26 | 0 |
| Kimi-K2.6 | plain-expanded - minimal | 30 | 0.011 | 0.185 | 4 | 23 | 3 |
| gemini-3.1-pro-preview | contractual - no-skill | 30 | 0.206 | 0.376 | 9 | 21 | 0 |
| gemini-3.1-pro-preview | contractual - minimal | 30 | 0.078 | 0.222 | 6 | 23 | 1 |
| gemini-3.1-pro-preview | contractual - plain-expanded | 30 | 0.056 | 0.154 | 5 | 25 | 0 |
| gemini-3.1-pro-preview | plain-expanded - minimal | 30 | 0.022 | 0.226 | 6 | 21 | 3 |

## 解释边界

- 本表使用 `claude-opus-4-7` 作为独立评分模型。
- 分数反映离线合成任务上的独立模型评分，不是多人类评审。
- 高分不等于可上线，仍需结合工具调用实验和人工复核。
