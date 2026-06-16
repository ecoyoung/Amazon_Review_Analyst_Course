# Amazon Review Analyst Course

60 分钟的内部培训课件：**基于 Amazon 评论分析的消费者洞察**。

- 主课件：[slides.md](./slides.md) — 56 张幻灯片，8 个模块
- 讲师指引：[teacher-notes.md](./teacher-notes.md) — 逐模块节奏、互动节点、应急预案
- 10 个 Lottie 动画：[public/animations/](./public/animations/) — 关键视觉时刻
- 动画源工程：[lottie-source/](./lottie-source/) — diffusionstudio/lottie player，用于二次编辑

## 技术栈

- [Slidev](https://sli.dev) — Markdown 驱动的幻灯片框架
- [vue3-lottie](https://github.com/megasanjay/vue3-lottie) — Vue 3 Lottie 播放组件
- [diffusionstudio/lottie](https://github.com/diffusionstudio/lottie) — Lottie 动画的本地播放器和编辑器
- [amazon-review-insight](https://github.com/ecoyoung/Amazon_Review_Analyst) — 模块 6 嵌入的实时演示工具

## 端口分配

为了避免冲突，三个服务分别使用不同端口：

| 服务 | 端口 | 用途 |
|------|------|------|
| Slidev 课件 | `4000` | 主课件演示 |
| Lottie 源工程 | `3030` | 编辑/验证动画 |
| Amazon Review Insight 工具 | `8080` | M6 iframe 嵌入 |

## 本地开发

需要三个终端（首次运行）：

```bash
# Terminal 1 — 启动 amazon-review-insight 工具（M6 iframe 依赖）
cd ../amazon-review-insight   # 或你克隆 demo tool 的位置
docker compose up

# Terminal 2 — 启动课件
npm install
npm run dev
# → http://localhost:4000

# Terminal 3（仅编辑动画时需要）— Lottie 源工程
cd lottie-source
npm install
npm run dev
# → http://localhost:3030
```

## 课件演示（培训当天）

只需要 Terminal 1 + Terminal 2：

```bash
# 启动 demo 工具
cd amazon-review-insight && docker compose up

# 启动课件
cd Amazon_Review_Analyst_Course && npm run dev
```

打开 http://localhost:4000 开始演示。讲师按 `→` / `←` 切换幻灯片。

## 编辑/新增动画

每个动画是 `public/animations/NN-<slug>.json` 一个独立的 Lottie JSON。修改流程：

1. 在 [lottie-source/public/projects/](./lottie-source/public/projects/) 找到对应的 project（如 `hook/`）
2. 编辑 `scene-1/lottie.json`
3. 浏览器打开 http://localhost:3030/hook/scene-1 验证
4. 用 `?frame=N` 参数 scrub 到具体帧：`http://localhost:3030/hook/scene-1?frame=60`
5. 验证 OK 后，复制到 `public/animations/`：
   ```bash
   cp lottie-source/public/projects/hook/scene-1/lottie.json \
      public/animations/01-hook-star-climb.json
   ```
6. 课件热更新，立即可见

新增动画请遵循 [text-to-lottie skill 规则](https://github.com/diffusionstudio/lottie/blob/main/skills/text-to-lottie/SKILL.md)，特别是：
- 每个 Lottie 必须暴露至少一个 `bgColor` 槽位
- 文件夹结构必须 `public/projects/<slug>/scene-N/lottie.json`

## 10 个动画清单

| # | 文件 | 模块 | 视觉概念 |
|---|------|------|---------|
| 01 | `01-hook-star-climb.json` | M0 | 评分 4.2★ → 4.7★，一颗金星点亮 |
| 02 | `02-ci-three-layers.json` | M1 | 表层 → 中层 → 深层 三层洋葱 |
| 03 | `03-gold-mine-scale.json` | M2 | 评论数 1 → 100 → 1000 → 10000，"金矿"印章 |
| 04 | `04-four-use-cases.json` | M3 | 2×2 应用场景象限，逐格揭示 |
| 05 | `05-four-step-pipeline.json` | M4 | 四步流水线：定 → 收 → 提 → 出 |
| 06 | `06-observation-to-insight.json` | M4 | 观察打红 X，洞察打绿 ✓ |
| 07 | `07-case-magnet-fix.json` | M5 | 耳机盒盖合上，差评率 12% → 3% |
| 08 | `08-tool-assembly-line.json` | M6 | 清洗 → LLM 分析 → 报告，文件流转 |
| 09 | `09-demo-intro-badge.json` | M6 | LIVE DEMO 标识脉冲 |
| 10 | `10-closing-loop.json` | M7 | 50 万预算 → 读竞品评论，闭环 |

## 导出讲义

```bash
# 导出 PDF（动画定格在第一帧）
npm run export

# 输出 slides.pdf
```

## 部署为静态网站

```bash
npm run build
# 输出 dist/，可直接部署到任意静态托管
```

注意：iframe 嵌入的 demo 工具需要单独部署，课件构建产物只包含幻灯片本身。

## 项目结构

```
Amazon_Review_Analyst_Course/
├── slides.md                       主课件
├── teacher-notes.md                讲师指引
├── setup/main.ts                   全局注册 Vue3Lottie
├── components/
│   ├── LottieFrame.vue             带标题的 Lottie 容器
│   └── LiveDemo.vue                带加载态的 iframe 包装
├── public/
│   ├── animations/                 10 个最终交付的 Lottie JSON
│   └── logos/                      品牌资源
└── lottie-source/                  动画源工程（diffusionstudio/lottie）
    └── public/projects/<slug>/     每个动画一个 project
```

## 鸣谢

- 课件大纲：基于 `CI课程大纲_Amazon评论消费者洞察.md`
- Lottie 编辑器：[diffusionstudio/lottie](https://github.com/diffusionstudio/lottie)
- 演示工具：[Amazon Review Insight](https://github.com/ecoyoung/Amazon_Review_Analyst)
