---
theme: none
title: Amazon 评论洞察实战课
info: |
  从竞品评论到产品决策
  Amazon Review Insight · 60 分钟 · 实战工作坊
highlighter: shiki
lineNumbers: false
drawings:
  persist: false
transition: slide
mdc: true
---

<script setup>
const TOOL_URL = import.meta.env.VITE_TOOL_URL || 'http://182.92.240.206:8080/'

function openToolPage() {
  window.location.assign(TOOL_URL)
}
</script>

---
layout: cinema
variant: ink
eyebrow: Amazon Review Insight · Workshop
index: 00 / 40
---

# Amazon 评论<br/>洞察实战

<p class="cinema__sub">从竞品评论到产品、Listing和风险决策</p>

---
layout: editorial
module: 课程培训与工具
page: 01 / 40
---

<h1 class="editorial__headline">你能学到什么，<br/>学不到什么。</h1>

<div class="editorial__grid">
  <div class="editorial__column">
    <div class="editorial__card editorial__card--good" v-click>
      <h3>能学到</h3>
      <p>Amazon 评论分析的方法：怎么从评论里读出人物、场景、优势、痛点和优先级。</p>
    </div>
    <div class="editorial__card editorial__card--good" v-click>
      <h3>能学到</h3>
      <p>获取和分析评论的工具用法：上传、清洗、分析、读报告、回看证据。</p>
    </div>
    <div class="editorial__card editorial__card--good" v-click>
      <h3>能学到</h3>
      <p>AI 时代做洞察的基本经验：样本意识、证据链、抽样偏差、上下文窗口和幻觉风险。</p>
    </div>
    <div class="editorial__card" v-click>
      <h3>这是一条线</h3>
      <p>先学方法，再看工具，再回到报告和决策。</p>
    </div>
  </div>
  <div class="editorial__column">
    <div class="editorial__card" v-click>
      <h3>学不到</h3>
      <p>分析工具的设计细节：prompt 怎么写、schema 怎么定、chunk 怎么切、如何归并标签、如何做评估和审计。</p>
    </div>
    <div class="editorial__card" v-click>
      <h3>学不到</h3>
      <p>后端和工程实现：队列、存储、报告生成、API、部署和 harness 的内部架构。</p>
    </div>
    <p class="editorial__lede" v-click style="font-size:14px; color:var(--mist);">先学方法，再学判断。我们先把边界说清楚，后面再讨论。</p>
  </div>
</div>

---
layout: lottie-stage
variant: paper
eyebrow: The hook
index: 02 / 39
name: 01-hook-star-climb
caption: 同样 1000 条评论，有人只看到评分，有人看到可以让评分上升的具体动作。
---

---
layout: lottie-stage
variant: paper
eyebrow: The hook
index: 02 / 40
name: 01-hook-star-climb
caption: 同样 1000 条评论，有人只看到评分，有人看到可以让评分上升的具体动作。
---

---
layout: cinema
variant: paper
eyebrow: Opening question
index: 03 / 40
---

# 如果要进入<br/>一个新品类

<p class="cinema__sub">你会看关注哪些内容？</p>

<div style="position:absolute; bottom:58px; left:56px; right:56px; display:flex; justify-content:center; gap:14px; flex-wrap:wrap;">
  <span v-click class="chip">市场</span>
  <span v-click class="chip">价格带</span>
  <span v-click class="chip">广告关键词</span>
  <span v-click class="chip">新品表现</span>
  <span v-click class="chip">竞品评论</span>
</div>

---
layout: poll
poll: first-signal
eyebrow: Warm-up
variant: paper
index: 04 / 40
---

看一个 Amazon 竞品时，<br/>你最先想知道<span style="color: var(--cyan-deep);">哪件事</span>？

---
layout: cinema-quote
variant: ink
eyebrow: Core shift
index: 05 / 39
---

评论不是用来证明产品好不好。

评论是用来发现：<strong style="font-style:normal; color:var(--cyan);">用户为什么买、为什么吐槽、为什么复购。</strong>

---
layout: editorial
module: Core path
page: 06 / 39
---

<h1 class="editorial__headline">今天只解决<br/>一个问题。</h1>

<p class="editorial__lede">如何把一堆 Amazon评论，变成老板能听懂、团队能执行的商业决策 or 分析报告。</p>

<div class="editorial__grid">
  <div class="editorial__column">
    <div class="review-snippet" v-click>
      <p class="review-snippet__text">"The lid opened inside my bag twice."</p>
      <div class="review-snippet__meta">
        <span class="chip">3★</span>
        <span class="chip">travel use</span>
        <span class="chip chip--bad">leak risk</span>
      </div>
    </div>
  </div>
  <div class="editorial__column">
    <div class="reasoning-ladder">
      <div class="reasoning-step" v-click>
        <div class="reasoning-step__label">Signal</div>
        <p>不是泛泛的“质量差”，而是移动场景下的闭合失败。</p>
      </div>
      <div class="reasoning-step" v-click>
        <div class="reasoning-step__label">Insight</div>
        <p>用户把它当 travel-safe 产品使用，但实际体验破坏了这个预期。</p>
      </div>
      <div class="reasoning-step" v-click>
        <div class="reasoning-step__label">Decision</div>
        <p>验证卡扣/磁吸结构，同时调整 Listing 中的便携承诺。</p>
      </div>
    </div>
  </div>
</div>

---
layout: cinema
variant: cyan
eyebrow: Framework
index: 07 / 40
---

# Review → Signal<br/>Insight → Decision

<p class="cinema__sub">评论原文 → 可量化信号 → 业务洞察 → 行动决策</p>

---
layout: lottie-stage
variant: paper
eyebrow: From surface to action
index: 08 / 39
name: 02-ci-three-layers
caption: 不停在表层评价，而是往下拆到场景、动机、障碍和可执行动作。
---

---
layout: editorial
module: Module 01 · What reviews can answer
page: 09 / 40
---

<h1 class="editorial__headline">Amazon 评论<br/>能回答什么？</h1>

<div class="editorial__grid">
  <div class="editorial__column">
    <div class="review-snippet">
<p class="review-snippet__text">"Bought this for <strong style="color: red;">my dad</strong>. Easy to use, but the <strong style="color: red;">instructions were confusing</strong> at first."</p>
      <div class="review-snippet__meta">
        <span class="chip">gift buyer</span>
        <span class="chip">first-time setup</span>
      </div>
    </div>
    <div class="signal-strip" v-click>
      <span class="signal-pill"><strong>People</strong> gift buyer</span>
      <span class="signal-pill"><strong>Context</strong> first use</span>
      <span class="signal-pill"><strong>Love</strong> easy to use</span>
      <span class="signal-pill"><strong>Hate</strong> instructions</span>
    </div>
  </div>
  <div class="editorial__column">
    <div class="reasoning-ladder">
      <div class="reasoning-step" v-click>
        <div class="reasoning-step__label">Question</div>
        <p>谁在买？为什么买？哪个环节卡住？</p>
      </div>
      <div class="reasoning-step" v-click>
        <div class="reasoning-step__label">Answer</div>
        <p>礼品购买者认可易用性，但首次设置说明影响体验。</p>
      </div>
      <div class="reasoning-step" v-click>
        <div class="reasoning-step__label">Action</div>
        <p>优化说明书、首屏 FAQ、开箱引导，而不是重写全部卖点。</p>
      </div>
    </div>
  </div>
</div>

---
layout: editorial
module: Module 01 · What reviews cannot answer
page: 10 / 40
---

<h1 class="editorial__headline">Amazon 评论中<br/>不能回答什么？</h1>

<div class="editorial__grid">
  <div class="editorial__column">
    <div class="review-snippet">
      <p class="review-snippet__text">"I returned it because it was not what I expected."</p>
      <div class="review-snippet__meta">
        <span class="chip chip--bad">missing context</span>
        <span class="chip chip--bad">unclear expectation</span>
      </div>
    </div>
    <div class="signal-strip" v-click>
      <span class="signal-pill"><strong>不能回答</strong> 市场的需求多大</span>
      <span class="signal-pill"><strong>不能回答</strong> 生活状态与环境</span>
      <span class="signal-pill"><strong>不能回答</strong> 年龄与人生阶段</span>
      <span class="signal-pill"><strong>不能回答</strong> 没写评论的人怎么想</span>
    </div>
  </div>
  <div class="editorial__column">
    <div class="reasoning-ladder">
      <div class="reasoning-step" v-click>
        <div class="reasoning-step__label">Bias</div>
        <p>评论样本偏向强情绪用户，沉默的大多数不会自动出现。</p>
      </div>
      <div class="reasoning-step" v-click>
        <div class="reasoning-step__label">Boundary</div>
        <p>评论能一定程度反映解释体验问题，但不能单独证明市场规模、价格弹性或购买路径。</p>
      </div>
      <div class="reasoning-step" v-click>
        <div class="reasoning-step__label">Use</div>
        <p>把评论当作“假设生成器”，再用销量、关键词、广告、访谈和测试去验证。</p>
      </div>
    </div>
  </div>
</div>

---
layout: editorial
module: Module 01 · Output map
page: 11 / 40
---

<h1 class="editorial__headline">工具报告<br/>对应这些问题。</h1>

<div class="editorial__grid">
  <div class="editorial__column">
    <div class="editorial__card" v-click>
      <span class="num">01</span>
      <h3>Personas</h3>
      <p>谁在买、什么场景使用、哪个人群最值得服务。</p>
    </div>
    <div class="editorial__card" v-click>
      <span class="num">02</span>
      <h3>Advantages</h3>
      <p>哪些卖点已经被用户验证，不只是我们自己想说。</p>
    </div>
  </div>
  <div class="editorial__column">
    <div class="editorial__card" v-click>
      <span class="num">03</span>
      <h3>Pain Points</h3>
      <p>哪些摩擦正在造成差评、退货、犹豫和低转化。</p>
    </div>
    <div class="editorial__card editorial__card--good" v-click>
      <span class="num">04</span>
      <h3>Top Priorities</h3>
      <p>把洞察转成产品、营销、风险控制的前三个动作。</p>
    </div>
  </div>
</div>

---
layout: cinema
variant: ink
eyebrow: Module 02
index: 12 / 40
---

# 先判断<br/>数据能不能信

<p class="cinema__sub">评论分析的第一个坑：样本错了，洞察再漂亮也没用。</p>

---
layout: lottie-stage
variant: paper
eyebrow: Review data scale
index: 13 / 39
name: 03-gold-mine-scale
caption: 评论数量越大，越需要抽样、清洗、分层，而不是直接把全部内容塞给 AI。
---

---
layout: lottie-stage
variant: paper
eyebrow: Review data scale
index: 13 / 40
name: 03-gold-mine-scale
caption: 评论数量越大，越需要抽样、清洗、分层，而不是直接把全部内容塞给 AI。
---

---
layout: editorial
module: Module 02 · Data quality
page: 14 / 39
---

<h1 class="editorial__headline">不要只问：<br/>评分高不高。</h1>

<div class="compare-grid">
  <div class="compare-card compare-card--bad" v-click>
    <h3>5★ · 低信息</h3>
    <p>"Great product. Works well."</p>
    <div class="review-snippet__meta">
      <span class="chip chip--bad">结论少</span>
      <span class="chip chip--bad">无场景</span>
    </div>
  </div>
  <div class="compare-card compare-card--good" v-click>
    <h3>3★ · 高信息</h3>
    <p>"Easy to install, but the screw holes did not align with my cabinet."</p>
    <div class="review-snippet__meta">
      <span class="chip">场景</span>
      <span class="chip">部件</span>
      <span class="chip">原因</span>
    </div>
  </div>
</div>

<div class="evidence-bar" style="margin-top:18px;">
  <div class="evidence-item" v-click><strong>Verified</strong><span>优先保留，但不是绝对真相</span></div>
  <div class="evidence-item" v-click><strong>Helpful</strong><span>代表其他买家觉得这条有用</span></div>
  <div class="evidence-item" v-click><strong>Date</strong><span>判断问题是历史还是近期爆发</span></div>
</div>

---
layout: editorial
module: Module 02 · Input schema
page: 15 / 39
---

<h1 class="editorial__headline">工具需要的<br/>不是玄学。</h1>

<div class="editorial__grid">
  <div class="editorial__column">
    <p class="editorial__lede">`amazon-review-insight` 接受一份 Amazon 评论 CSV 或 Excel。</p>
    <div class="editorial__card" v-click>
      <span class="chip">Required columns</span>
      <p style="margin-top:12px;"><code>Content</code> · <code>Rating</code> · <code>Date</code> · <code>Helpful</code> · <code>Verified Purchase</code></p>
    </div>
  </div>
  <div class="editorial__column">
    <div class="editorial__card editorial__card--good" v-click>
      <h3>清洗动作</h3>
      <p>去重、剔除空内容、校验评分、规范日期、生成稳定 <code>review_id</code>，再进入分析。</p>
    </div>
    <p v-click class="editorial__lede" style="font-size:14px; color:var(--mist);">SellerSprite 星级均衡抽样要特别标注：评分分布不能当作自然评分分布。</p>
  </div>
</div>

---
layout: cinema-quote
variant: paper
eyebrow: Principle
index: 16 / 39
---

样本不是“有就行”，
而是决定你看到的是信号还是噪声。

<div style="margin-top:24px; display:flex; justify-content:center; gap:12px; flex-wrap:wrap;">
  <span class="chip">抽样偏差</span>
  <span class="chip">样本量</span>
  <span class="chip">代表性</span>
  <span class="chip">置信度</span>
</div>

<p style="margin-top:24px; max-width:760px; margin-left:auto; margin-right:auto; font-size:18px; line-height:1.65; color:var(--ink-soft); text-align:left;">
  少量评论可以用来找线索，但不能直接代表整体。
  如果样本偏向高星、近期、verified，或者只抽到某一类用户，
  你看到的就会是被放大过的结果，而不是市场本身。
</p>

<p style="margin-top:16px; max-width:760px; margin-left:auto; margin-right:auto; font-size:18px; line-height:1.65; color:var(--ink-soft); text-align:left;">
  统计上最先要问的不是“结论是什么”，而是“这个样本能不能撑得住这个结论”。
  n 太小时，1 到 2 条极端评论就足以把比例、频次和优先级带偏。
</p>

---
layout: cinema
variant: ink
eyebrow: Module 03
index: 17 / 39
---

# 工具到底在做什么？

<p class="cinema__sub">Personas · Advantages · Pain Points → Top Priorities</p>

---
layout: lottie-stage
variant: paper
eyebrow: Tool extraction map
index: 18 / 39
name: 04-four-use-cases
caption: 不是把评论“总结一下”，而是把每条评论拆成可追溯、可聚合、可行动的结构化发现。
---

---
layout: editorial
module: Module 03 · Tool output model
page: 19 / 39
---

<h1 class="editorial__headline">先看工具<br/>最终要交什么。</h1>

<div class="editorial__grid">
  <div class="editorial__column">
    <div class="editorial__card" v-click>
      <span class="chip">Input</span>
      <p style="margin-top:12px;"><code>Content</code> · <code>Rating</code> · <code>Date</code> · <code>Helpful</code> · <code>Verified Purchase</code></p>
    </div>
    <div class="editorial__card" v-click>
      <span class="chip">Pipeline</span>
      <p style="margin-top:12px;">清洗 → 150 条/块 → LLM 抽取 → 近义归并 → 报告生成。</p>
    </div>
  </div>
  <div class="editorial__column">
    <div class="signal-strip">
      <span class="signal-pill" v-click><strong>Personas</strong> 谁在买、什么场景用</span>
      <span class="signal-pill" v-click><strong>Advantages</strong> 哪些卖点被真实验证</span>
      <span class="signal-pill" v-click><strong>Pain Points</strong> 哪些摩擦影响体验和转化</span>
      <span class="signal-pill" v-click><strong>Top 3</strong> 产品、营销、风险动作</span>
    </div>
    <div class="editorial__card editorial__card--good" v-click style="margin-top:12px;">
      <p>交付一份有准确数据、可靠分析和行动策略的报告</p>
    </div>
  </div>
</div>

---
layout: editorial
module: Module 03 · Evidence-backed extraction
page: 20 / 39
---

<h1 class="editorial__headline">每个结论<br/>都要能回查。</h1>

<div class="editorial__grid">
  <div class="editorial__column">
    <div class="review-snippet">
      <p class="review-snippet__text">"Easy to swallow, but I wish the dosage instructions were clearer."</p>
      <div class="review-snippet__meta">
        <span class="chip">review_id: 128</span>
        <span class="chip">4★</span>
        <span class="chip">verified</span>
      </div>
    </div>
    <div class="editorial__card" v-click>
      <span class="chip">不要输出</span>
      <p style="margin-top:12px;">"用户觉得说明不好。"</p>
    </div>
  </div>
  <div class="editorial__column">
    <div class="editorial__card editorial__card--good" v-click>
      <span class="chip">工具应输出</span>
      <p style="margin-top:12px;"><strong>Usage Guidance Gap</strong>：部分用户认可易吞咽，但剂量/用法说明不够清楚；证据来自 review_id 和短 quote。</p>
    </div>
    <p class="editorial__lede" v-click style="font-size:14px; color:var(--mist);">你的工具有一个硬规则：报告里的 quote 必须能匹配同一个 <code>review_id</code> 的原始评论。</p>
  </div>
</div>

layout: editorial
module: Module 03 · From extraction to insight
page: 21 / 39
---

<h1 class="editorial__headline">抽取结果<br/>还不是洞察。</h1>

<div class="reasoning-ladder">
  <div class="reasoning-step" v-click>
    <div class="reasoning-step__label">Weak</div>
    <p>很多用户说产品质量不好。</p>
  </div>
  <div class="reasoning-step" v-click>
    <div class="reasoning-step__label">Better</div>
    <p>低星评论集中提到 "lid does not close" 和 "magnet weak"。</p>
  </div>
  <div class="reasoning-step" v-click>
    <div class="reasoning-step__label">Insight</div>
    <p>差评不是否定整体产品，而是集中在闭合体验；优先修复磁吸和开合手感，可能比重做音质更有效。</p>
  </div>
</div>

---
layout: editorial
module: Module 03 · Insight test
page: 22 / 39
---

<h1 class="editorial__headline">洞察必须<br/>过五关。</h1>

<div class="editorial__grid">
  <div class="editorial__column">
    <ul class="editorial__list">
      <li v-click><span class="marker">1</span><span class="body"><strong>有证据</strong><span>能回到 <code>review_id</code> 和原文片段</span></span></li>
      <li v-click><span class="marker">2</span><span class="body"><strong>有频次</strong><span>知道覆盖率或支持评论数</span></span></li>
      <li v-click><span class="marker">3</span><span class="body"><strong>有对象</strong><span>知道是哪类用户在表达</span></span></li>
    </ul>
  </div>
  <div class="editorial__column">
    <ul class="editorial__list">
      <li v-click><span class="marker">4</span><span class="body"><strong>有场景</strong><span>知道问题在什么时候发生</span></span></li>
      <li v-click><span class="marker">5</span><span class="body"><strong>有动作</strong><span>能落到产品、Listing、广告或客服</span></span></li>
    </ul>
    <div class="editorial__card editorial__card--good" v-click>
      <p>不能行动的结论，只能叫观察。</p>
    </div>
  </div>
</div>

---
layout: editorial
module: Module 03 · Decision matrix
page: 23 / 39
---

<h1 class="editorial__headline">优先级不是<br/>看声音最大。</h1>

<div class="decision-matrix">
  <div class="matrix-cell matrix-cell--focus" v-click>
    <h3>高频 × 易修</h3>
    <p>马上改：说明书、包装提示、Listing 误导。</p>
  </div>
  <div class="matrix-cell" v-click>
    <h3>高频 × 难修</h3>
    <p>进路线图：结构、配方、核心性能。</p>
  </div>
  <div class="matrix-cell matrix-cell--risk" v-click>
    <h3>低频 × 高风险</h3>
    <p>必须处理：安全、过敏、合规、误用。</p>
  </div>
  <div class="matrix-cell matrix-cell--focus" v-click>
    <h3>高意图场景</h3>
    <p>转成广告角度、A+ 页面和人群投放。</p>
  </div>
</div>

---
layout: cinema
variant: ink
eyebrow: Module 04
index: 24 / 39
---

# AI 如何<br/>帮你读评论？

<p class="cinema__sub">从人工读、关键词规则，到 LLM 和 harness。</p>

---
layout: lottie-stage
variant: paper
eyebrow: Method shift
index: 25 / 39
name: 05-four-step-pipeline
caption: 评论分析的方法，不是一下子从人工跳到 AI，而是一步一步把不稳定的经验变成可复现流程。
---

---
layout: editorial
module: Module 04 · Pre-AI reading
page: 26 / 39
---

<h1 class="editorial__headline">最早，<br/>靠人工读评论。</h1>

<div class="editorial__grid">
  <div class="editorial__column">
    <ul class="editorial__list">
      <li v-click><span class="marker">1</span><span class="body"><strong>人工浏览</strong><span>读标题、星级、正文，手工记印象。</span></span></li>
      <li v-click><span class="marker">2</span><span class="body"><strong>人工编码</strong><span>复制到表格，给评论贴标签，再人工汇总频次。</span></span></li>
      <li v-click><span class="marker">3</span><span class="body"><strong>问题</strong><span>慢、贵、主观，而且很难稳定复现。</span></span></li>
    </ul>
  </div>
  <div class="editorial__column">
    <div class="editorial__card editorial__card--good" v-click>
      <h3>经验</h3>
      <p>人工最适合做的是定义问题、看少量样本、建立 scheme，再把规则交给后续流程。</p>
    </div>
    <p class="editorial__lede" v-click style="font-size:14px; color:var(--mist);">这一步的价值在“判断”和“方法论”，不是在“规模”。</p>
  </div>
</div>

---
layout: editorial
module: Module 04 · Regex and keywords
page: 27 / 39
---

<h1 class="editorial__headline">后来，<br/>靠正则表达式匹配。</h1>

<div class="editorial__grid">
  <div class="editorial__column">
    <div class="editorial__card" v-click>
      <span class="chip">Can catch</span>
      <p style="margin-top:12px;">`broken` `leak` `refund` `too small` `not fit` `easy to use`</p>
    </div>
    <div class="editorial__card editorial__card--good" v-click>
      <span class="chip">Why it helps</span>
      <p style="margin-top:12px;">便宜、快、可批量跑，适合做初筛和高频词聚合。</p>
    </div>
  </div>
  <div class="editorial__column">
    <div class="editorial__card" v-click>
      <span class="chip chip--bad">Misses</span>
      <p style="margin-top:12px;">"not bad at all"、"works for me"、"great for travel but not for kids" 这种上下文和否定关系，规则常常读错。</p>
    </div>
    <p class="editorial__lede" v-click style="font-size:14px; color:var(--mist);">经验：规则适合找“明显的词”，不适合判断“词在这里是什么意思”。</p>
  </div>
</div>

---
layout: cinema
variant: ink
eyebrow: Module 04
index: 28 / 39
---

# 再后来，<br/>把文件交给 LLM。

<p class="cinema__sub">LLM 让我们不只看关键词，而是看句子、语气、场景和因果。</p>

---
layout: editorial
module: Module 04 · Discussion
page: 29 / 39
---

<h1 class="editorial__headline">日常中<br/>你们平时怎么用 LLM。</h1>

<div class="editorial__grid">
  <div class="editorial__column">
    <div class="editorial__card editorial__card--good" v-click>
      <h3>可以交流的场景</h3>
      <p>润色论文、改摘要、生成文案、整理访谈纪要、翻译材料、提炼会议要点。</p>
    </div>
    <div class="editorial__card" v-click>
      <h3>可以交流的方法</h3>
      <p>你怎么给 LLM 限定角色、限定输入、要求引用证据、检查输出是否可靠。</p>
    </div>
  </div>
  <div class="editorial__column">
    <div class="editorial__card editorial__card--good" v-click>
      <h3>我们想讨论的</h3>
      <p>哪些任务适合交给 LLM，哪些任务你仍然会保留人工判断。</p>
    </div>
    <p class="editorial__lede" v-click style="font-size:14px; color:var(--mist);">把你最常用的一个文本工作场景带进来，我们一起拆一拆。</p>
    <button
      type="button"
      @click.stop.prevent="openToolPage"
      style="display:inline-flex; align-items:center; justify-content:center; margin-top:12px; padding:12px 18px; border:0; border-radius:999px; background:var(--cyan); color:#fff; text-decoration:none; font-weight:700; cursor:pointer; position:relative; z-index:5;"
    >
      打开工具页面
    </button>
  </div>
</div>

---
layout: editorial
module: Module 04 · LLM reading
page: 30 / 39
---

<h1 class="editorial__headline">LLM 读评论，<br/>强在语境，不强在自控。</h1>

<div class="editorial__grid">
  <div class="editorial__column">
    <div class="editorial__card" v-click>
      <span class="chip">What it does well</span>
      <p style="margin-top:12px;">能识别否定、转折、语气、隐含场景和多句因果，把“意思”读出来。</p>
    </div>
    <div class="editorial__card editorial__card--good" v-click>
      <span class="chip">Typical win</span>
      <p style="margin-top:12px;">把“not bad for travel” 读成场景优势，而不是单纯正面评论。</p>
    </div>
  </div>
  <div class="editorial__column">
    <div class="editorial__card" v-click>
      <span class="chip chip--bad">What can go wrong</span>
      <p style="margin-top:12px;">批量扔进去时，模型会受上下文窗口限制，读不完就开始抽样、压缩和“补完”语义。</p>
    </div>
    <div class="editorial__card" v-click>
      <span class="chip chip--bad">Common failure</span>
      <p style="margin-top:12px;">抽样偏差、概率输出和幻觉会让报告看起来完整，但不一定真实。</p>
    </div>
    <p class="editorial__lede" v-click style="font-size:14px; color:var(--mist);">经验：LLM 适合读语义，不适合替你承担方法论责任。</p>
  </div>
</div>

---
layout: editorial
module: Module 04 · Harness
page: 31 / 40
---

<h1 class="editorial__headline">现在，<br/>要用 harness 管住 AI。</h1>

<div class="editorial__grid">
  <div class="editorial__column">
    <ul class="editorial__list">
      <li v-click><span class="marker">1</span><span class="body"><strong>定义输入</strong><span>只喂需要的字段，先清洗再分析。</span></span></li>
      <li v-click><span class="marker">2</span><span class="body"><strong>固定输出</strong><span>persona / advantage / pain_point，返回 strict JSON。</span></span></li>
      <li v-click><span class="marker">3</span><span class="body"><strong>加证据</strong><span>每条结论都要带 review_id 和短 quote。</span></span></li>
      <li v-click><span class="marker">4</span><span class="body"><strong>切分上下文</strong><span>按 chunk 分块，控制每次输入的评论量。</span></span></li>
    </ul>
  </div>
  <div class="editorial__column">
    <ul class="editorial__list">
      <li v-click><span class="marker">5</span><span class="body"><strong>做归并</strong><span>合并近义主题，避免模型制造碎片化标签。</span></span></li>
      <li v-click><span class="marker">6</span><span class="body"><strong>设评估</strong><span>检查覆盖率、重复率、幻觉和可追溯性。</span></span></li>
      <li v-click><span class="marker">7</span><span class="body"><strong>留审计</strong><span>输出 cleaned XLSX、JSON、HTML report。</span></span></li>
    </ul>
  </div>
</div>

<p class="editorial__lede" style="margin-top:16px; font-size:14px; color:var(--mist);">
  harness 的作用不是让模型“更会说”，而是让它在受限上下文里仍然尽量少偷懒、少幻觉、少漏证据。
</p>

---
layout: cinema
variant: cyan
eyebrow: Module 05
index: 32 / 39
---

# 报告怎么读？

<p class="cinema__sub">不要从漂亮图表开始，要从业务问题开始。</p>

---
layout: editorial
module: Module 05 · Read the report
page: 33 / 39
---

<h1 class="editorial__headline">第一眼，<br/>先看方法说明。</h1>

<div class="editorial__grid">
  <div class="editorial__column">
    <div class="evidence-bar" style="grid-template-columns:1fr;">
      <div class="evidence-item" v-click><strong>Source</strong><span>文件来自哪里？自然全量评论，还是第三方抽样导出？</span></div>
      <div class="evidence-item" v-click><strong>Sample</strong><span>分析了多少条？清洗掉了多少？是否只看 verified？</span></div>
      <div class="evidence-item" v-click><strong>Time</strong><span>问题是近期爆发，还是历史遗留？</span></div>
    </div>
  </div>
  <div class="editorial__column">
    <div class="editorial__card editorial__card--good" v-click>
      <h3>Warning</h3>
      <p>如果是星级均衡抽样，评分分布只能看样本结构，不能当作真实市场表现。</p>
    </div>
    <p class="editorial__lede" v-click style="font-size:14px; color:var(--mist);">方法说明是报告可信度的一部分。</p>
  </div>
</div>

---
layout: editorial
module: Module 05 · Persona
page: 34 / 39
---

<h1 class="editorial__headline">Personas：<br/>谁最值得服务？</h1>

<div class="editorial__grid">
  <div class="editorial__column">
    <p class="editorial__lede">不要把 persona 做成人口统计标签。Amazon 评论里更有价值的是使用场景和购买动机。</p>
    <div class="editorial__card" v-click>
      <span class="chip">差</span>
      <p style="margin-top:12px;">女性用户、年轻用户、中产用户。</p>
    </div>
  </div>
  <div class="editorial__column">
    <div class="editorial__card editorial__card--good" v-click>
      <span class="chip">好</span>
      <p style="margin-top:12px;">frequent travelers、parents buying for children、first-time users、maintenance-seeking users。</p>
    </div>
    <p v-click class="editorial__lede" style="font-size:14px; color:var(--mist);">除非评论者明确自述，不要推断年龄、性别、健康状况等敏感属性。</p>
  </div>
</div>

---
layout: editorial
module: Module 05 · Advantages
page: 35 / 39
---

<h1 class="editorial__headline">Advantages：<br/>哪些卖点被验证？</h1>

<div class="editorial__grid">
  <div class="editorial__column">
    <div class="editorial__card" v-click>
      <h3>Listing 卖点</h3>
      <p>品牌想说什么。</p>
    </div>
    <div class="editorial__card" v-click>
      <h3>Review 优势</h3>
      <p>用户真的感知到了什么。</p>
    </div>
  </div>
  <div class="editorial__column">
    <div class="editorial__card editorial__card--good" v-click>
      <h3>决策方式</h3>
      <p>把高覆盖优势放进首图、标题、五点、A+ 和广告素材；把低感知优势降级。</p>
    </div>
  </div>
</div>

---
layout: editorial
module: Module 05 · Pain points
page: 36 / 39
---

<h1 class="editorial__headline">Pain Points：<br/>差评背后是什么？</h1>

<div class="editorial__grid">
  <div class="editorial__column">
    <ul class="editorial__list">
      <li v-click><span class="marker">1</span><span class="body"><strong>体验缺陷</strong><span>产品真的不好用</span></span></li>
      <li v-click><span class="marker">2</span><span class="body"><strong>预期落差</strong><span>Listing 让用户误会</span></span></li>
      <li v-click><span class="marker">3</span><span class="body"><strong>使用门槛</strong><span>说明、安装、剂量、兼容性不清楚</span></span></li>
    </ul>
  </div>
  <div class="editorial__column">
    <div class="editorial__card editorial__card--good" v-click>
      <h3>先分类，再行动</h3>
      <p>体验缺陷改产品；预期落差改页面；使用门槛改说明和客服触达。</p>
    </div>
  </div>
</div>

---
layout: lottie-stage
variant: paper
eyebrow: Case pattern
index: 37 / 39
name: 07-case-magnet-fix
caption: 很多评分问题不是“大质量问题”，而是一个高频摩擦点被反复放大。
---

---
layout: editorial
module: Module 05 · Top priorities
page: 38 / 40
---

<h1 class="editorial__headline">Top Priorities：<br/>报告最后看这里。</h1>

<div class="editorial__grid">
  <div class="editorial__column">
    <p class="editorial__lede">工具会输出前三个建议，但讲师要提醒：这不是命令，是候选动作。</p>
    <div class="editorial__card" v-click>
      <h3>Product</h3>
      <p>结构、材质、配方、配件、包装、说明书。</p>
    </div>
  </div>
  <div class="editorial__column">
    <div class="editorial__card" v-click>
      <h3>Marketing</h3>
      <p>标题、五点、A+、广告角度、人群场景。</p>
    </div>
    <div class="editorial__card editorial__card--good" v-click>
      <h3>Risk</h3>
      <p>误用提醒、合规表达、售后预案、FAQ。</p>
    </div>
  </div>
</div>

---
layout: cinema-quote
variant: ink
eyebrow: Human judgment
index: 39 / 40
---

工具负责把评论读快。

但把数据变成决策的，永远是<strong style="font-style:normal; color:var(--cyan);">人的判断力</strong>。

---
layout: cinema
variant: ink
eyebrow: Thanks
index: 40 / 40
---

# Q&A

<p class="cinema__sub" style="margin-top: 56px;">
  <span style="opacity: 0.55;">提问，是思考最好的证明。</span>
</p>
