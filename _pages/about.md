---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}
<span class='anchor' id='about-me'></span>

# 🚀 About Me 
I am first-year PhD student @ [SJTU](https://en.sjtu.edu.cn/), supervised by [Siheng Chen](https://siheng-chen.github.io/).  My general research interest lies in LLM agent applications. Currently, I focus on integrating LLM agents into embodied agent development. If you are interested in me and seek for cooperation, feel free to email me at [youngsoul0731@gmail.com](mailto:youngsoul0731@gmail.com/). 


# 🔥 News

- *2026.01*: &nbsp;🎉🎉 The paper entitled "InfoMosaic-Bench: Evaluating Multi-Source Information Seeking in Tool-Augmented Agents" has been accepted by ICLR 2026.

- *2025.10*: &nbsp;🎉🎉 The paper entitled "FLORA: GNNs as Predictors of Agentic Workflow Performances" has been accepted by LoG 2025: The Fourth Learning on Graphs Conference.

- *2024.07*: &nbsp;🎉🎉 The paper entitled "ERASE: Error-Resilient Representation Learning on Graphs for Label Noise Tolerance" has been accepted by CIKM '24: 33rd International Conference on Information and Knowledge Management. I serve as a **co-first author**.

# 📝 Publications 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2026</div><img src='images/infomosaic-bench.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[InfoMosaic-Bench: Evaluating Multi-Source Information Seeking in Tool-Augmented Agents](https://arxiv.org/abs/2510.02271)

Yaxin Du, **Yuanshuo Zhang**, Xiyuan Yang, Yifan Zhou, Cheng Wang, Gongyi Zou, Xianghe Pang, Wenhao Wang, Menglan Chen, Shuo Tang, Zhiyu Li, Feiyu Xiong, Siheng Chen

[<i class="fab fa-fw fa-github" aria-hidden="true"></i> **Code**](https://github.com/DorothyDUUU/Info-Mosaic) &nbsp; [<i class="fa fa-solid fa-file-pdf" aria-hidden="true"></i> **PDF**](https://arxiv.org/abs/2510.02271)
- Role: co-author.
- We introduce InfoMosaic-Bench to evaluate multi-source information seeking for tool-augmented agents.
- Accepted by ICLR 2026.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">LoG 2025</div><img src='images/flora.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[FLORA: GNNs as Predictors of Agentic Workflow Performances](https://arxiv.org/abs/2503.11301)

Yuanshuo Zhang, Yuchen Hou, Bohan Tang, Shuo Chen, Muhan Zhang, Xiaowen Dong, Siheng Chen

[<i class="fab fa-fw fa-github" aria-hidden="true"></i> **Code**](https://github.com/youngsoul0731/FLORA-Bench) &nbsp; [<i class="fa fa-solid fa-file-pdf" aria-hidden="true"></i> **PDF**](https://arxiv.org/pdf/2503.11301)
- Role: first author.
- We propose FLORA to use GNNs as predictors of agentic workflow performance, reducing repeated LLM invocations during evaluation.
- Accepted by LoG 2025.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CIKM 2024</div><img src='images/erase.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[ERASE: Error-Resilient Representation Learning on Graphs for Label Noise Tolerance](https://dl.acm.org/doi/10.1145/3627673.3679552)

[Ling-Hao Chen](https://lhchen.top/)<sup>*</sup>, **Yuanshuo Zhang**<sup>*</sup>, et al.

[<i class="fa fa-solid fa-cube" aria-hidden="true"></i> **Project**](hhttps://eraseai.github.io/ERASE-page/) &nbsp; [<i class="fab fa-fw fa-github" aria-hidden="true"></i> **Code**](https://github.com/eraseai/erase) &nbsp; [<i class="fa fa-solid fa-video" aria-hidden="true"></i> **Video**](https://www.youtube.com/watch?v=w5HwGb8bElA)
- Role: co-first author.
- We introduce an error-resilient mechanism for graph representation learning under label noise.
- Accepted by CIKM 2024.
</div>
</div>

<span class='anchor' id='-preprints'></span>

# 📝 Preprints


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Technical Report</div><img src='images/embocoach-bench.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[EmboCoach-Bench: Benchmarking AI Agents on Developing Embodied Robots](https://arxiv.org/abs/2601.21570)

Zixing Lei<sup>*</sup>, Genjia Liu<sup>*</sup>, **Yuanshuo Zhang**<sup>*</sup>, Qipeng Liu, Chuan Wen, Shanghang Zhang, Wenzhao Lian, Siheng Chen

[<i class="fa fa-solid fa-file-pdf" aria-hidden="true"></i> **PDF**](https://arxiv.org/pdf/2601.21570)
- Role: core contributor.
- We benchmark AI agents on embodied robot development tasks, highlighting end-to-end tool use and iteration.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Technical Report</div><img src='images/agentif-oneday.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[AgentIF-OneDay: A Task-level Instruction-Following Benchmark for General AI Agents in Daily Scenarios](https://arxiv.org/abs/2601.20613)

[<i class="fab fa-fw fa-github" aria-hidden="true"></i> **Code**](https://github.com/xbench-ai/AgentIF-OneDay) &nbsp; [<i class="fa fa-solid fa-file-pdf" aria-hidden="true"></i> **PDF**](https://arxiv.org/pdf/2601.20613)
- Role: contributor.
- We provide a task-level instruction-following benchmark for daily scenarios to evaluate general AI agents.
</div>
</div>

<!-- <div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='images/flora.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[GNNs as Predictors of Agentic Workflow Performances](https://arxiv.org/abs/2503.11301)

Yuanshuo Zhang, Yuchen Hou, Bohan Tang, Shuo Chen, Muhan Zhang, Xiaowen Dong, Siheng Chen

[<i class="fab fa-fw fa-github" aria-hidden="true"></i> **Code**](https://github.com/youngsoul0731/FLORA-Bench) &nbsp; [<i class="fa fa-solid fa-file-pdf" aria-hidden="true"></i> **PDF**](https://arxiv.org/pdf/2503.11301)
- We propose FLORA to use GNNs as predictors of agentic workflow performance thus avoiding repeated LLM invocations for evaluation. 
</div>
</div> -->
<!-- # 🎖 Honors and Awards
- *2021.10* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.09* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  -->

# 📖 Educations
- *2021.09 - 2025.06*, School of Electronic Engineering, Xidian University. 

<!-- # 💬 Invited Talks
- *2021.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.03*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  \| [\[video\]](https://github.com/) -->

# 💻 Internships
- *2024.08 - 2025.07*, [BIGAI](https://www.bigai.ai/), Beijing, China.

<!-- # 👍 Friends
- [Ling-Hao Chen](https://lhchen.top/), Ph.D. student at [Tsinghua University](https://www.tsinghua.edu.cn/), focussing on Character Animation, Digital Generation, Embodied Intelligence, and Machine Learning (**mentored me in graph representation learning**). 
- [Xijun Wang](https://kopper-xdu.github.io/), undergraduate student at [Xidian University](https://www.xidian.edu.cn/), focussing on Computer Vison and Generative Models.
- [Zhiyang Liang](https://zhiyangliang.github.io/), undergraduate student at [Xidian University](https://www.xidian.edu.cn/), focussing on 3D Vision. -->
<!-- <br><br><br><br><br><br><br><br> -->
&nbsp;

<!-- <script type="text/javascript" id="clustrmaps" src="//cdn.clustrmaps.com/map_v2.js?cl=ffffff&w=a&t=n&d=Dv2XJvfFsJgeunE6i3OYfBPY7jcGv2zSILN4rwgNYH8&co=2d78ad&cmo=3acc3a&cmn=ff5353&ct=ffffff"></script> -->
<!-- <div id="clustrmaps-widget-container" style="width: 40%; margin: 0 auto;">
    <script type="text/javascript" id="clustrmaps" src="//cdn.clustrmaps.com/map_v2.js?cl=ffffff&w=a&t=n&d=Dv2XJvfFsJgeunE6i3OYfBPY7jcGv2zSILN4rwgNYH8&co=2d78ad&cmo=3acc3a&cmn=ff5353&ct=ffffff"></script>
</div> -->
<!-- <body> -->
<!-- <div id="clustrmaps-widget-container" style="width: 40%"> -->
<script type='text/javascript' id='clustrmaps' src='//cdn.clustrmaps.com/map_v2.js?cl=ffffff&w=400&t=tt&d=Dv2XJvfFsJgeunE6i3OYfBPY7jcGv2zSILN4rwgNYH8&co=2d78ad&ct=ffffff&cmo=3acc3a&cmn=ff5353'></script>

<!-- </div> -->
<!-- </body> -->
<!-- 
<head> 
    <script defer src="https://use.fontawesome.com/releases/v6.0.13/js/all.js"></script> 
    <script defer src="https://use.fontawesome.com/releases/v6.0.13/js/v4-shims.js"></script> 
</head> 
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v6.0.13/css/all.css"> -->
