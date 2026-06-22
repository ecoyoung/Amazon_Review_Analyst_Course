# Teacher Notes · Amazon 评论洞察实战课

> 全程 60 分钟。课程定位从“消费者洞察概念课”改为“Amazon 评论分析实战工作坊”。讲师重点不是解释 CI，而是训练学员把评论证据转成产品、Listing、广告和风险动作。

## 总览

| 模块 | 时长 | 核心交付 | 学员应该带走的一句话 |
|------|-----:|---------|--------------------|
| M0 开场 | 5 min | 评论分析的真正目的 | 评论不是评分，是购买动机和阻碍的证据库 |
| M1 评论能回答什么 | 7 min | 6 类业务问题 | 先问业务问题，再读评论 |
| M2 数据可信度 | 8 min | 样本和字段意识 | 样本错了，洞察再漂亮也没用 |
| M3 五类信号 | 8 min | People / Context / Love / Hate / Risk | 不要只看正负面，要拆到场景和属性 |
| M4 什么是洞察 | 10 min | 洞察五关 | 能改变决策的判断才叫洞察 |
| M5 工具实战 | 12 min | 跑 amazon-review-insight | 工具加速阅读，不替代判断 |
| M6 报告解读 | 7 min | 读 personas / advantages / pain points / priorities | 报告最后要变成动作 |
| M7 收尾 SOP | 3 min | 7 步 SOP | 先读竞品评论，但要读出证据、结构和行动 |

---

## 课前准备

1. 启动课件：

```bash
npm run dev
```

2. 启动工具：

```bash
cd amazon-review-insight
docker compose up --build
```

3. 确认这些地址可用：

- 课件：http://localhost:4000
- 工具：http://localhost:8080
- 后端健康检查：http://localhost:8000/api/health

4. 准备一份评论文件，字段至少包含：

- `Content`
- `Rating`
- `Date`
- `Helpful`
- `Verified Purchase`

5. 如果现场网络或 LLM provider 不稳定，提前准备一个已经跑好的 HTML 报告，路径可从 `amazon-review-insight/runs/` 找。

6. 左下角有一个小计时器：

- 显示本次打开课件后的 elapsed time
- 目标时长是 60 分钟
- 点击计时器里的 `↺` 可以重置
- 按键盘 `T` 也可以重置
- 如果课前提前打开了课件，正式开始前点一次 `↺` 或按一次 `T`

---

## 无图片版本的讲法

这版课件故意不依赖图片。讲师要把注意力放在“评论原话如何被翻译成业务动作”上。

每遇到评论原话页，按四步讲：

1. 先只读原话，不解释。
2. 问学员：“这句话里有哪些信号？”
3. 再揭示 People / Context / Love / Hate / Risk。
4. 最后追问：“如果这是你负责的产品，明天会改什么？”

讲师不要把列表逐条念完。优先用这句话推进：

> 这不是一句抱怨。它至少包含一个场景、一个摩擦点、一个预期落差和一个可执行动作。

如果学员回答泛泛，例如“质量不好”，继续追问：

- 哪个部件不好？
- 发生在什么使用场景？
- 是产品缺陷，还是 Listing 预期误导？
- 这个问题该由产品、运营、广告还是客服处理？

---

## M0 开场：为什么读评论经常没有洞察

**目标**：打掉“评论分析就是看评分和差评截图”的习惯。

讲法：

1. 开场直接问：“如果要进入一个新品类，你第一步会看什么？”
2. 让学员先说销量、价格、广告、差评等答案。
3. 翻到核心观点：评论不是用来证明产品好不好，而是发现用户为什么买、为什么骂、为什么复购。

强调：

> 同样 1000 条评论，有人只看到“质量不好”，有人能看到“磁吸弱、安装难、尺寸误导、味道残留、说明书不清楚”。

不要在这里讲太多方法，先制造落差。

---

## M1 评论能回答什么

**目标**：把评论分析和业务问题绑定。

重点讲 6 个问题：

1. 谁在买
2. 为什么买
3. 喜欢什么
4. 讨厌什么
5. 怎么表达
6. 哪里有机会

讲师提示：

- “用户怎么表达”很重要，因为这会直接影响 Listing、广告词和 A+ 页面。
- 不要把评论分析讲成“情绪分析”。整体正负面没有太多业务价值，拆到场景和属性才有价值。

连接工具：

- `personas` 回答谁在买
- `advantages` 回答喜欢什么
- `pain_points` 回答讨厌什么
- `market_semantics` 回答用户语言和语义
- `strategies.top_priorities` 回答下一步做什么

---

## M2 数据可信度：先判断样本能不能信

**目标**：让学员知道工具结果依赖输入质量。

重点讲：

- 星级是入口，不是结论
- 五星评论可能信息密度很低
- 三星和四星经常更有价值，因为用户既认可产品，也指出具体问题
- Verified Purchase 优先，但不是绝对真相
- Helpful votes 是信号，代表其他买家认为这条评论有用
- 日期用于判断问题是历史问题还是近期问题
- SellerSprite 等导出可能是星级均衡抽样，不能直接当自然评分分布

讲师话术：

> 如果样本是偏的，AI 只会更快地帮你总结偏见。

工具连接：

`amazon-review-insight` 会做字段校验、去重、剔除空内容、规范评分和日期、生成稳定 `review_id`。这一步不是技术细节，而是报告可信度的一部分。

---

## M3 五类信号：People / Context / Love / Hate / Risk

**目标**：给学员一个读评论时可执行的标注框架。

五类信号：

- People：谁在买
- Context：什么场景使用
- Love：喜欢什么
- Hate：讨厌什么
- Risk：风险在哪里

互动建议：

现场给一条评论，让学员判断里面有没有这五类信号。例如：

> Bought this for travel. It is compact and easy to pack, but the lid opened inside my bag twice.

引导答案：

- People：travel user
- Context：放在包里旅行使用
- Love：compact / easy to pack
- Hate：lid opened
- Risk：漏出、污染、退货、差评

强调：

> 一条好评论不只是“正面”或“负面”，它通常同时包含场景、评价、原因和后果。

---

## M4 什么才算洞察

**目标**：训练学员区分 observation 和 insight。

核心定义：

> 洞察不是一句总结，而是一个能改变决策的判断。

对比示例：

- Observation：很多用户说质量不好。
- Better observation：低星评论集中提到 “lid does not close” 和 “magnet weak”。
- Insight：差评不是否定整体产品，而是集中在闭合体验；优先修复磁吸和开合手感，可能比重做音质更有效。

洞察五关：

1. 有证据：能回到 `review_id`
2. 有频次：知道覆盖率或评论数
3. 有对象：知道哪类用户表达
4. 有场景：知道什么时候发生
5. 有动作：能落到产品、Listing、广告、客服或风险控制

讲师提示：

- 学员容易把“总结”当洞察，要反复问：“所以我们要做什么？”
- 如果一句话无法推动任何动作，它通常不是洞察。

---

## M5 工具实战：amazon-review-insight

**目标**：让学员看到工具如何把评论转成结构化报告。

演示步骤：

1. 打开 http://localhost:8080
2. 上传评论 CSV 或 Excel
3. 观察进度条，尤其是 chunk 级进度
4. 等待报告生成
5. 打开 HTML 报告
6. 下载或查看输出文件

讲解重点：

- 工具先清洗，再分析，不是直接把原始表格丢给模型
- 每 150 条评论为一个 chunk，避免长文本丢失
- LLM 负责抽取 personas / advantages / pain points
- 后处理会合并近义主题并计算覆盖率
- 报告里的 quote 必须能回到原始 `review_id`

不要过度讲代码。学员只需要理解：

> 工具不是 magic box，它是一条有证据约束的分析流水线。

---

## M6 报告怎么读

**目标**：训练报告阅读顺序。

推荐顺序：

1. 先看方法说明和样本来源
2. 再看 KPI，但不要停在平均评分
3. 看 personas：谁最值得服务
4. 看 advantages：哪些卖点已被验证
5. 看 pain points：哪些摩擦影响评分和转化
6. 看 top priorities：哪些动作最值得先做

Personas 讲法：

- 不要做“女性用户、年轻用户”这种没有证据的人口统计猜测
- 更好的标签是场景和需求：frequent travelers、gift buyers、first-time users、maintenance-seeking users
- 不要推断敏感属性，除非评论者明确自述

Advantages 讲法：

- Listing 卖点是品牌想说什么
- Review 优势是用户真的感知到了什么
- 高覆盖优势应该进入首图、五点、A+ 和广告素材

Pain Points 讲法：

先分类：

- 体验缺陷：改产品
- 预期落差：改 Listing
- 使用门槛：改说明书、FAQ、客服触达
- 风险信号：改合规表达、警示和售后预案

Top Priorities 讲法：

工具输出的是候选动作，不是最终命令。讲师要引导学员结合成本、风险、供应链周期、品牌定位来排序。

---

## M7 收尾：7 步 SOP

最后让学员带走一套流程：

1. 选 3-5 个头部或高相似竞品
2. 导出评论，保留必要字段
3. 清洗样本并标注抽样风险
4. 跑 `amazon-review-insight`
5. 核对证据，尤其是 quote 和 `review_id`
6. 输出产品、Listing、广告、客服、风险动作
7. 每月复盘新评论，看问题是否改善

收尾话术：

> 从今天开始，选品会、改款会、Listing 优化会，不要再只说“我感觉”。先问：评论证据显示什么？

---

## 应急预案

| 状况 | 处理 |
|------|------|
| iframe 加载不出 | 直接打开 http://localhost:8080，或切到已生成 HTML 报告 |
| Docker 未启动 | 跳过现场上传，用 `amazon-review-insight/runs/` 里的历史报告演示 |
| LLM provider 失败 | 解释工具有 provider fallback，但现场可用离线报告继续讲 |
| 学员问“评论能不能预测销量” | 回答：评论主要是回溯信号，不能单独预测销量，但能解释购买阻碍和机会 |
| 学员问“能不能直接让 AI 给结论” | 回答：可以让 AI 做初稿，但必须用 review_id、覆盖率和业务动作校验 |
| 时间不够 | 砍 M1 的部分案例，保留 M2、M4、M5、M6 |
| 时间富余 | 让学员现场选择一个品类，用报告模板写一条洞察 brief |

---

## 参考资料

- Amazon About Amazon: AI-generated review highlights
- Amazon Seller Central: Voice of the Customer
- Aspect-Based Sentiment Analysis in e-commerce review research
- Amazon Customer Reviews policy and fake-review risk discussions

讲师不需要逐条展开这些来源，只需要知道课程背后的方法依据：

- 电商评论分析应该拆到 aspect/topic 级别
- AI 总结已经成为电商评论阅读的一种常见方式
- 评论真实性、抽样偏差和证据追溯必须纳入分析流程
