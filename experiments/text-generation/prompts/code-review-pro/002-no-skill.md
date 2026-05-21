# Experiment Prompt

## Fixed Instruction

请根据任务内容完成。不要使用未提供的外部资料。若信息不足，请明确标注不确定性。最终只输出任务结果，不解释实验设置。

## Task

# Task code-review-pro-002

## 用户请求

这个报错是不是数据库坏了？请直接给结论。

## 合成材料

```text
Traceback:
  File "service.py", line 42, in handle
    return parse_payload(request.body)["items"][0]
IndexError: list index out of range
```

缺失信息：

- 没有请求样例。
- 没有 `parse_payload` 实现。
- 没有数据库调用栈。
- 没有复现步骤。

## 期望输出

不要武断判断数据库损坏。说明已有证据、可能原因、需要补充的信息和建议排查步骤。
