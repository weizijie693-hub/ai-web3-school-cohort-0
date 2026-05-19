# Learning Agent 设置记录与运行日志

> 提交时间：2026-05-19
> 对应任务：Week 1 — 学习环境初始化与代理工作流配置

---

## 1. 选择的代理 / AI 工具

| 项目 | 内容 |
|------|------|
| **工具名称** | Claude Code (CLI) |
| **运行模式** | 本地终端 + VS Code 集成 |
| **基础模型** | Claude Opus 4 / Sonnet 4 |
| **启动 Prompt** | `https://aiweb3.school/learning-agent.zh.txt` |
| **参考文档** | `https://aiweb3.school/zh/handbook/` — Handbook 全部章节 |

### 选择理由

- **权限粒度控制**：Claude Code 的 Permission Mode 允许在工具调用级别审批操作（文件写入、git push 等需要手动确认），符合"Agent 必须经人工确认才能执行写入操作"的安全原则
- **原生 HITL（Human-in-the-Loop）工作流**：Agent 每次生成文件或修改代码后都展示 diff，用户确认后才执行
- **CLI 模式适合学习场景**：终端下交互清晰，不会过度封装学习过程
- **对中文和英文的双语支持良好**

---

## 2. 代理协助的学习任务

### 2.1 已完成任务清单

| 日期 | 任务 | 状态 | 产出 |
|------|------|------|------|
| Day 1 | 初始化个人学习仓库 | ✅ 已完成 | GitHub repo `ai-web3-school-cohort-0` |
| Day 1 | 建立仓库目录结构 | ✅ 已完成 | README, profile, learning-plan, templates |
| Day 1 | 编写学员画像 | ✅ 已完成 | `profile.md` |
| Day 1 | 编写学习计划 | ✅ 已完成 | `learning-plan.md` — 三阶段结构 |
| Day 1 | 创建日打卡模板 | ✅ 已完成 | `templates/daily-note.md`, `templates/task-note.md` |
| Day 1 | 撰写首日学习笔记 | ✅ 已完成 | `daily/2026-05-18.md` — Web3 Network 基础 |
| Day 1 | 创建 Web3 学习笔记 | ✅ 已完成 | `tasks/web3-network-basics.md` |
| Day 2 | AI 基础概念共享词汇表 | ✅ 已完成 | `daily/ai-fundamentals.md` — 10 个核心概念 |

### 2.2 当前学习进度

- **Phase 1: Foundation (Week 1-2)** — Web3 Foundation 学习中
- **Handbook 已读章节**: Network, AI Fundamentals (部分)

---

## 3. 关键提示与配置说明

### 3.1 初始启动 Prompt

```
Please act as my AI × Web3 School Learning Agent. First read the startup Prompt:
https://aiweb3.school/learning-agent.zh.txt, and combine it with the Handbook:
https://aiweb3.school/zh/handbook/, to help me initialize my personal learning plan,
GitHub learning repo, daily check-in drafts, and Handbook feedback process.
```

**启动 Prompt 的核心规则**（来自 `learning-agent.zh.txt`）：

1. **角色定位**：Learning Agent 的目标是帮助理解课程、规划任务、维护学习仓库、生成打卡草稿，**不是替学员完成学习**
2. **人工确认原则**：
   - 创建仓库、写文件、commit、push、WCB 提交必须经学员确认
   - 不接触钱包签名、转账、私钥、API Key 等敏感信息
3. **固定入口**：Handbook → WCB 课程页 → WCB Learning 页面
4. **每日流程**：读 WCB Learning → 读 Handbook → 写 daily note → 生成打卡草稿 → 返回链接让学员手动提交 → 写回提交记录
5. **轻量优先**：先让学员今天能行动，不是一次性规划所有未来

### 3.2 关键配置项

**GitHub CLI 配置（非 Personal Access Token）**：
```bash
gh auth login          # 浏览器登录，不走 Token
gh auth status         # 确认登录成功
```

**仓库创建（学员确认后执行）**：
```bash
gh repo create ai-web3-school-cohort-0 \
  --public \
  --description "Personal learning journal and proof-of-work for AI x Web3 School" \
  --clone
```

**Commit & Push 流程（每次变更后）**：
```bash
git status --short     # 展示变更
git add <files>        # 经学员确认后
git commit -m "变更说明"
git push
```

### 3.3 隐私安全配置

- 仓库可见性：**public**
- `README.md` 中声明隐私提醒
- 禁止提交的内容清单：私钥、助记词、API Key、Token、.env、未公开联系方式

---

## 4. 成功输出记录

### 4.1 GitHub 仓库

```
仓库名:   ai-web3-school-cohort-0
可见性:   public
描述:     Personal learning journal and proof-of-work for AI × Web3 School
URL:      https://github.com/lxdao-official/aiweb3school (官方) /
          学员个人 Fork
本地路径: ~/ai-web3-school-cohort-0
```

### 4.2 目录结构（初始化完成）

```
ai-web3-school-cohort-0/
├── README.md                    # 仓库简介、链接、隐私提醒
├── profile.md                   # 学员画像：AI有基础/Web3新手/开发方向
├── learning-plan.md             # 三阶段学习计划 + 进度追踪表
├── daily/
│   ├── 2026-05-18.md            # Day 1 笔记：Web3 Network 基础
│   └── ai-fundamentals.md       # AI 基础概念共享词汇表
├── tasks/
│   └── web3-network-basics.md   # Web3 网络核心概念笔记
├── experiments/                 # （待填充）
├── handbook-feedback/           # （待填充）
├── hackathon/                   # （待填充）
├── submissions/                 # 课程作业提交
└── templates/
    ├── daily-note.md            # 日打卡模板
    └── task-note.md             # 学习笔记模板
```

### 4.3 学习计划概览

```
Phase 1: AI + Web3 Foundation   | Week 1-2 (05-17 ~ 05-30) | 🟡 In Progress
Phase 2: AI × Web3 Bridge       | Week 3-4 (05-31 ~ 06-13) | ⬜
Phase 3: Tracks & Hackathon     | Week 5+  (06-14+)        | ⬜
```

### 4.4 首日打卡内容示例

```markdown
# Daily Note — 2026-05-18

## Today's Focus
Initialize personal learning environment

## What I Learned
- AI × Web3 School 是 LXDAO & ETHPanda 维护的开源学习平台
- 区块链网络核心：让互不信任的参与者对状态变化达成一致
- PoS / L2 / Rollup / Testnet 基础概念

## Tasks Completed
- [x] Installed GitHub CLI & logged in
- [x] Created repo: ai-web3-school-cohort-0
- [x] Initialized directory structure with README, profile, templates

## Check-in
- [x] Pushed to GitHub
```

---

## 5. 手动审核与更正记录

以下记录展示了人机协作过程中的关键审核节点，Agent 始终遵循"生成草稿 → 用户确认 → 执行"的 HITL 原则。

### 5.1 审核记录 1：仓库创建确认

```
Agent 建议:
  "现在创建仓库 ai-web3-school-cohort-0，可见性 public，本地路径 ~/ai-web3-school-cohort-0。是否确认？"

学员审核:
  ✅ 确认仓库名和可见性
  ✅ 确认本地路径
  ⚠️ 要求加入 privacy notice 到 README

Agent 执行:
  将 privacy notice 加入 README → 创建仓库 → 初始化结构 → push
```

### 5.2 审核记录 2：学习计划调整

```
Agent 建议的学习计划初稿:
  "按 Handbook 的顺序列出所有模块。"

学员审核:
  ✅ 整体结构 OK
  ⚠️ 要求调整：
    - 增加 Phase 分阶段结构 (Foundation / Bridge / Track)
    - 加入进度追踪表
    - 增加 Hackathon 条目
    - 标注预估时间

Agent 执行:
  重新组织为三阶段结构 → 加入进度追踪表 → 最终版本确认
```

### 5.3 审核记录 3：词汇表生成后的人工审校

```
Agent 生成:
  AI 基础概念共享词汇表（包含 LLM、Prompt、Context Window、Agent 等 10 个概念
  ，每个包含"一句话解释/具体例子/常见误解"三段式结构）

学员审核:
  ✅ 概念准确、结构清晰
  ⚠️ 在文档末尾添加声明：
    "本文档由 AI 生成初稿，内容来自模型自身的知识，未直接复制任何外部来源。
    建议在实际使用前由团队进行人工审校。"

Agent 执行:
  在文末加入上述声明 → commit → push
```

⚠️ **未执行的安全操作**（Agent 主动拒绝或学员阻止）：

| 场景 | 处理 |
|------|------|
| Agent 曾提议运行 `gh auth login` 的 Token 模式 | ❌ 拒绝 — 改用浏览器登录流程 |
| Agent 曾建议自动打开 WCB 打卡链接 | ❌ 拒绝 — 改为生成打卡草稿 + 返回链接，学员手动提交 |
| Agent 生成词汇表后未自动标注来源声明 | ⚠️ 学员在审核时添加，作为 HITL 的实践案例 |

---

## 6. 工作流总结

```
                    ┌─────────────────┐
                    │  Learning Agent  │
                    │  Startup Prompt  │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │  学员确认角色    │
                    │  与学习目标      │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
     ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
     │ Agent 读取   │ │ Agent 生成   │ │ Agent 返回   │
     │ Handbook /   │ │ 笔记 / 打卡  │ │ 链接/草稿给  │
     │ 课程内容     │ │ 草稿 / 计划  │ │ 学员确认     │
     └─────────────┘ └─────────────┘ └──────┬──────┘
                                            │
                              ┌─────────────┴─────────────┐
                              │         学员审核           │
                              │  ✅ 确认 / ⚠️ 修改 / ❌ 拒绝│
                              └─────────────┬─────────────┘
                                            │
                              ┌─────────────▼─────────────┐
                              │  Agent 执行（写文件/commit/ │
                              │  push）或学员手动完成       │
                              └───────────────────────────┘
```

---

*本记录随学习进度持续更新。*
