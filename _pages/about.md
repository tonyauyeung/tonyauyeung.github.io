---
layout: about
title: about
permalink: /
subtitle: PhD in <a href='https://cbl.eng.cam.ac.uk/people/'>MLG@Cambridge</a>

profile:
  align: left
  image: prof_pic.jpg
  image_dark: profile-dark.jpg
  image_circular: true # crops the image to make it circular
  more_info: >
    <p>📮: <a href="mailto:ro352@cam.ac.uk">ro352@cam.ac.uk</a></p>

selected_papers: true # includes a list of papers marked as "selected={true}"
# Academic services below sync to the CV page (/cv/) and PDF (bin/build-resume.sh).
academic_service:
  enabled: true
  items:
    - role: journal reviewer
      details: TMLR (2026)
    - role: conference reviewer
      details: ICLR (2025–2026), ICML (2026), NeurIPS (2025–2026)
      items:
        - award: silver reviewer🥈 @ ICML (2026)
    - role: workshop reviewer
      details: >-
        [DELTA@ICLR](https://delta-workshop.github.io/DeLTa2026/) (2025–2026),
        [FPI@NeurIPS](https://fpineurips.framer.website/) (2025),
        [SPIGM@NeurIPS](https://spigmworkshopv3.github.io/) (2025),
        [DynaFront@NeurIPS](https://sites.google.com/view/dynafrontneurips25) (2025),
        [SPIGM@ICML](https://spigmworkshop2026.github.io/) (2026),
        [FoGen@ICML](https://fdgm-workshop.github.io/FDGM_ICML2026/) (2026),
        [NonAR-LM@COLT](https://pengzhangzhi.github.io/NonAR-LM/#top) (2026)
    - role: organizer
      details: "[MolSS reading group](https://molss-reading-group.github.io/MolSS/) (Lead organizer)"
social: true # includes social icons at the bottom of the page

announcements:
  enabled: true # includes a list of news items
  scrollable: true # adds a vertical scroll bar if there are more than 3 news items
  limit: 5 # leave blank to include all the news in the `_news` folder

# latest_posts:
#   enabled: true
#   scrollable: true # adds a vertical scroll bar if there are more than 3 new posts items
#   limit: 3 # leave blank to include all the blog posts
---

<div id="bio-denoise" class="bio-denoise" markdown="1">
Hi there 👋. I'm Tony RuiKang OuYang (歐陽瑞康 in Chinese; SeoiHong AuYeung pronounced in Cantonese). I'm an first-year PhD in Machine Learning 🤖 at the [Machine Learning Group](https://mlg.eng.cam.ac.uk/about.html), University of Cambridge, supervised by [Prof. José Miguel Hernández-Lobato](https://jmhl.org) and fully funded by the _EPSRA DLA_ scholarship.

I completed [MPhil in Machine Learning and Machine Intelligence](https://www.mlmi.eng.cam.ac.uk) from the University of Cambridge, where I graduated with distinction and worked with [Prof. José Miguel Hernández-Lobato](https://jmhl.org) on energy-based neural sampler for sampling from Boltzmann distribution. Prior to that, I finished my BEng in Data Science in [Harbin Institute of Technology, Shenzhen (HITsz)](http://en.hitsz.edu.cn) and spent a wonderful year visiting in the [University of Oxford](https://www.spc.ox.ac.uk/study-here/visiting-students) studying Mathematics and Statistics (fully-funded by HITsz).

I lead the [MolSS Reading Group](https://molss-reading-group.github.io/MolSS/), which invites top researchers to share their works on <u>machine learning for molecular sciences</u>. Save our [website](https://molss-reading-group.github.io/MolSS/) and join our [Slack-channel](https://join.slack.com/t/molss/shared_invite/zt-35u93vepd-H83ftzwBbPCYY31jHcnM8A) to stay tuned 🚀

I play football (midfield) ⚽️

I am always open to discussion and collaboration, feel free to reach out!

<style>
  #bio-denoise {
    font-variant-ligatures: none;
    line-height: 1.45;
    min-height: 6em;
  }
</style>

<script>
  (function() {
    const container = document.getElementById('bio-denoise');
    if (!container) {
      return;
    }

    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      return;
    }

    let animationTimer = null;
    const originalTextNodes = [];
    const originalTexts = [];

    const maskChar = '-';

    function collectTextNodes(node, textNodes = []) {
      node.childNodes.forEach((child) => {
        if (child.nodeType === Node.TEXT_NODE) {
          textNodes.push(child);
        } else if (child.nodeType === Node.ELEMENT_NODE) {
          if (child.tagName === 'SCRIPT' || child.tagName === 'STYLE') {
            return;
          }
          collectTextNodes(child, textNodes);
        }
      });
      return textNodes;
    }

    function restoreOriginalText() {
      for (let index = 0; index < originalTextNodes.length; index += 1) {
        originalTextNodes[index].textContent = originalTexts[index];
      }
    }

    function initializeOriginalTextNodes() {
      if (originalTextNodes.length > 0) {
        return;
      }
      const textNodes = collectTextNodes(container);
      for (let index = 0; index < textNodes.length; index += 1) {
        originalTextNodes.push(textNodes[index]);
        originalTexts.push(textNodes[index].textContent || '');
      }
    }

    function maskToken(value) {
      return Array.from(value || '').map(() => maskChar).join('');
    }

    function shuffle(list) {
      for (let i = list.length - 1; i > 0; i -= 1) {
        const j = Math.floor(Math.random() * (i + 1));
        [list[i], list[j]] = [list[j], list[i]];
      }
      return list;
    }

    function syncNode(idx, textNodes, tokenStates) {
      textNodes[idx].textContent = tokenStates[idx].join('');
    }

    function initializeMaskedDiffusion(textNodes, tokenStates, schedule, finalStates) {
      const tokenSchedule = [];
      for (let nodeIndex = 0; nodeIndex < textNodes.length; nodeIndex += 1) {
        const finalText = finalStates[nodeIndex];
        const parts = finalText.split(/(\s+)/);
        const maskedParts = new Array(parts.length);

        for (let partIndex = 0; partIndex < parts.length; partIndex += 1) {
          const part = parts[partIndex];
          if (!part) {
            maskedParts[partIndex] = '';
            continue;
          }
          if (/^\s+$/.test(part)) {
            maskedParts[partIndex] = part;
          } else {
            maskedParts[partIndex] = maskToken(part);
            tokenSchedule.push({
              nodeIndex,
              partIndex,
              text: part
            });
          }
        }

        tokenStates.push(maskedParts);
      }

      shuffle(tokenSchedule);
      for (let i = 0; i < tokenSchedule.length; i += 1) {
        schedule.push(tokenSchedule[i]);
      }

      for (let nodeIndex = 0; nodeIndex < textNodes.length; nodeIndex += 1) {
        syncNode(nodeIndex, textNodes, tokenStates);
      }

      return tokenSchedule.length;
    }

    function sampleStepCount(remaining) {
      const raw = Math.max(1, Math.floor(Math.random() * 8));
      return Math.min(raw, remaining);
    }

    function revealOneBatch(pointer, revealCount, schedule, tokenStates, pending) {
      if (pointer >= schedule.length) {
        return false;
      }
      const cappedCount = Math.min(revealCount, schedule.length - pointer);
      for (let i = 0; i < cappedCount; i += 1) {
        const slot = schedule[pointer + i];
        tokenStates[slot.nodeIndex][slot.partIndex] = slot.text;
        pending.set(slot.nodeIndex, true);
      }
      return true;
    }

    function flush(textNodes, tokenStates, pending) {
      for (const nodeIndex of pending.keys()) {
        syncNode(nodeIndex, textNodes, tokenStates);
        pending.delete(nodeIndex);
      }
    }

    function rerenderDenoiseAnimation() {
      initializeOriginalTextNodes();
      restoreOriginalText();
      if (animationTimer !== null) {
        window.clearInterval(animationTimer);
      }

      const textNodes = originalTextNodes.slice();
      const finalStates = originalTexts.slice();
      const tokenStates = [];
      const schedule = [];
      const pending = new Map();

      const totalTokens = initializeMaskedDiffusion(textNodes, tokenStates, schedule, finalStates);
      let pointer = 0;
      const intervalMs = 35;

      animationTimer = window.setInterval(() => {
        const canReveal = pointer < totalTokens;
        if (!canReveal) {
          window.clearInterval(animationTimer);
          finalStates.forEach((value, index) => {
            textNodes[index].textContent = value;
          });
          animationTimer = null;
          return;
        }

        const revealCount = sampleStepCount(totalTokens - pointer);
        revealOneBatch(pointer, revealCount, schedule, tokenStates, pending);
        pointer += revealCount;
        flush(textNodes, tokenStates, pending);

        if (pointer >= totalTokens) {
          window.clearInterval(animationTimer);
          finalStates.forEach((value, index) => {
            textNodes[index].textContent = value;
          });
          animationTimer = null;
        }
      }, intervalMs);
    }

    rerenderDenoiseAnimation();
    document.removeEventListener('theme:changed', rerenderDenoiseAnimation);
    document.addEventListener('theme:changed', rerenderDenoiseAnimation);
  })();
</script>

<div style="clear: both;"></div>
</div>

<details class="about-research-box mt-3 about-research-box-gap-narrow" markdown="0">
  <summary class="about-research-box-title">news</summary>
  <ul>
    <li><strong>2026-07-13:</strong> I'm interning at <a href="https://anewbt.com">AnewLabs</a>, an aidd startup spinned-off from Seed@ByteDance recently. Working on equilibrium sampling model for proteins.</li>
  </ul>
</details>

<details class="about-research-box mt-3 about-research-box-gap-narrow" markdown="0">
  <summary class="about-research-box-title">research interests</summary>
  <ul>
    <li><strong>Probabilistic methods:</strong> (few-steps) generative models, EBMs, sampling methods</li>
    <li><strong>AI for science:</strong> computational biochemistry, Boltzmann Generators, free energy estimations</li>
  </ul>
</details>
<!-- 
My current research interests include <u>generative models</u>, <u>energy-based models</u>, <u>sampling methods</u>, and their interactions and also their applications to <u>molecular sciences</u> 🧬. Generally, I'm interested in <u>probabilistic machine learning</u> and <u>AI4Science</u>, especially developing powerful, efficient, and scalable methods that can be applied to physics ⚛️ and biochemistry 🧪. -->
