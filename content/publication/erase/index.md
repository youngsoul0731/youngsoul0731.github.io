---
title: 'ERASE: Error-Resilient Representation Learning on Graphs for Label Noise Tolerance'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
- Ling-Hao Chen
- admin

# Author notes (optional)
author_notes:
  - 'Equal contribution'
  - 'Equal contribution'

date: "2023-12-13T00:00:00Z"
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2023-12-13T00:00:00Z'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: In *33rd ACM International Conference on Information and Knowledge Management*
publication_short: In *CIKM-2024*

abstract: Deep learning has achieved remarkable success in graph-related tasks, yet this accomplishment heavily relies on large-scale high-quality annotated datasets. However, acquiring such datasets can be cost-prohibitive, leading to the practical use of labels obtained from economically efficient sources such as web searches and user tags. Unfortunately, these labels often come with noise, compromising the generalization performance of deep networks. To tackle this challenge and enhance the robustness of deep learning models against label noise in graph-based tasks, we propose a method called ERASE (Error-Resilient representation learning on graphs for lAbel noiSe tolerancE). The core idea of ERASE is to learn representations with error tolerance by maximizing coding rate reduction. To the best of our knowledge, it is the first time that the error-resilient mechanism is introduced into graph representation learning against label noise. Particularly, we also propose a decoupled label propagation method to estimate coding rate reduction. Before training, noisy labels are pre-corrected through structural denoising. During training, ERASE combines prototype pseudo-labels with propagated denoised labels and updates representations with error resilience, which significantly improves the generalization performance in node classification. The proposed method allows us to more effectively withstand errors caused by mislabeled nodes, thereby strengthening the robustness of deep networks in handling noisy graph data. Extensive experimental results show that our method can outperform multiple baselines with clear margins in broad noise levels and enjoy great scalabilityCodes are released at (https://github.com/eraseai/erase).

# Summary. An optional shortened abstract.
summary: Trustworthy Machine Leanring on Graphs, Semi-supervised Learning. 

tags:
  - Graph Representation Learning

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org


url_pdf: https://arxiv.org/abs/2312.08852
url_code: 'https://github.com/eraseai/erase'
url_project: 'https://eraseai.github.io/ERASE-page/'
# url_slides: ''
# url_source: '#'
url_video: 'https://www.youtube.com/watch?v=w5HwGb8bElA'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'ERASE'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects:
  - erase

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---

