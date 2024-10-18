---
title: 'BNEM: A Boltzmann Sampler Based on Bootstrapped Noised Energy Matching'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - admin
  - Bo Qiang
  - José Miguel Hernández-Lobato

author_notes:
  - 'Equal contribution'
  - 'Equal contribution'
  - 'University of Cambridge'

date: 'Sun, 15 Sep 2024 16:41:30 UTC'
doi: 'https://doi.org/10.48550/arXiv.2409.09787'

# Schedule page publish date (NOT publication's date).
publishDate: '2024-09-17'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['preprint']

# Publication name and optional abbreviated publication name.
# publication: In *Hugo Blox Builder Conference*
publication_short: In *arxiv*; accepted by NeurIPS ML4Phy workshop

abstract: Developing an efficient sampler capable of generating independent and identically distributed (IID) samples from a Boltzmann distribution is a crucial challenge in scientific research, e.g. molecular dynamics. In this work, we intend to learn neural samplers given energy functions instead of data sampled from the Boltzmann distribution. By learning the energies of the noised data, we propose a diffusion-based sampler, NOISED ENERGY MATCHING, which theoretically has lower variance and more complexity compared to related works. Furthermore, a novel bootstrapping technique is applied to NEM to balance between bias and variance. We evaluate NEM and BNEM on a 2-dimensional 40 Gaussian Mixture Model (GMM) and a 4-particle double-welling potential (DW-4). The experimental results demonstrate that BNEM can achieve state-of-the-art performance while being more robust.

# Summary. An optional shortened abstract.
summary: A neural sampler for Boltzmann distribution, leveraging energy-based diffusion, denoising energy matching and bootstrap energy estimation.

tags:
  - Probabilistic Machine Learning
  - Neural Sampler
  - Generative Model
  - AI for small molecules

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'https://arxiv.org/pdf/2409.09787'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  # caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/pLCdAaMFLTE)'
  focal_point: ''
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
# projects:
#   - example

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
# slides: example
---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

{{% callout note %}}
Create your slides in Markdown - click the _Slides_ button to check out the example.
{{% /callout %}}

Add the publication's **full text** or **supplementary notes** here. You can use rich formatting such as including [code, math, and images](https://docs.hugoblox.com/content/writing-markdown-latex/).