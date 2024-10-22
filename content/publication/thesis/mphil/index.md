---
title: 'Energy-Based Diffusion Neural Sampler for Boltzmann Densities'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - admin

author_notes:
  - 'University of Cambridge'

date: ''
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2024-10-22'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['MPhil Thesis']

# Publication name and optional abbreviated publication name.
# publication: In *Hugo Blox Builder Conference*
publication_short: MPhil Thesis, University of Cambridge

abstract: Efficiency and sample quality are essential when drawing statistically independent samples from a Boltzmann-type distribution, which is desired in a wide range of scientific problems, such as generating equilibrium samples of many-body systems. Statistical methods like Monte Carlo and MCMC, or actual numerical methods like Molecular Dynamics, are promis- ing but computationally expensive, emerging a trend that leverages the data compression capacity of neural networks for efficient sampling. In this thesis, we propose ENERGY-BASED DENOISING ENERGY MATCHING (EnDEM) and BOOTSTRAP ENDEM (BEnDEM). The former one, EnDEM, is inspired by the current state-of-the-art Boltzmann neural sampler, DEM, by targeting a less noisy stochastic energy estimator which allows many potentials to further improve performance. While the latter one, BEnDEM, is built on top of EnDEM which improves its learning target by bootstrapping from the learned energy. Both EnDEM and BEnDEM are trained in a bi-level iterated scheme as iDEM, which includes a simulation-free inner loop training an energy-based diffusion sampler and an outer-loop that simulates the learned diffusion sampler to generate more informative samples to further improve the sampler, resulting in scalability to high dimensions. We evaluate EnDEM and BEnDEM on a suit of tasks ranging from synthetic energy functions to invariant n-body particle systems, demonstrating their stronger capacity compared with DEM. We also provide multiple possible ways for further improvement built on top of our models, demonstrating their potential to solve higher dimensional and more complex tasks in the future.
# Summary. An optional shortened abstract.
summary: A neural sampler for Boltzmann distribution, leveraging energy-based diffusion.

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

url_pdf: mphil_thesis/MPhil_Thesis.pdf
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