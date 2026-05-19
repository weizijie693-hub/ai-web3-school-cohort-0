# CLI Concept Explainer — AI x Web3 学习工具

一个 CLI 交互式概念学习工具，帮助学习 AI × Web3 的 11 个核心概念。

## 用法

```bash
# 列出所有概念
python cli_concept_explainer.py list

# 查询某个概念（精确或模糊匹配）
python cli_concept_explainer.py explain agent
python cli_concept_explainer.py explain blockchain

# 随机展示一个概念
python cli_concept_explainer.py random

# 互动小测验（5 题）
python cli_concept_explainer.py quiz
```

## 概念库（11 个）

| 关键词 | 概念 |
|--------|------|
| `agent` | 智能体 / Agent |
| `blockchain` | 区块链网络 |
| `context-window` | 上下文窗口 |
| `hitl` | Human-in-the-Loop |
| `l2` | 二层网络 |
| `llm` | 大型语言模型 |
| `pos` | 权益证明 |
| `prompt` | 提示 |
| `rollup` | Rollup |
| `smart-contract` | 智能合约 |
| `tool-use` | 工具使用 |

每个概念包含三段式结构：一句话解释、具体例子、常见误解。

## AI 辅助说明

| 部分 | AI 辅助 | 手动验证 |
|------|---------|---------|
| **概念内容的编写** | AI 生成初稿，参考 Handbook 和模型知识 | 人工逐条审校，修正不准确表述，添加"常见误解"中的真实案例 |
| **三段式结构设计** | AI 建议的格式（一句话/例子/误解） | 人工确认结构合适，决定最终模板 |
| **CLI 工具代码** | AI 生成基础框架 | 人工调试编码兼容性（修复 Windows GBK 编码问题）、调整交互流程 |
| **quiz 题目逻辑** | AI 设计基础逻辑 | 人工添加容错、干扰项合理性和分数统计 |
| **概念库内容** | AI 生成初稿 | 人工核对了 Handbook 和官方文档的一致性，确保概念准确 |

## 注意事项

- 运行环境需要 Python 3.6+
- 建议在支持 UTF-8 的终端下运行（VS Code 终端、Windows Terminal、macOS Terminal）
- 概念内容来自 AI × Web3 School Handbook 与 AI 生成，经过人工审校
