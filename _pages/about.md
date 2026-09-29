---
layout: about
title: about
permalink: /
subtitle:

selected_papers: false
custom_publications: false
custom_education: false
custom_service: false
social: false

announcements:
  enabled: false

latest_posts:
  enabled: false
---

<style>
  .post-header {
    display: none;
  }
</style>

<div class="home-hero">
  <div class="home-portrait">
    <img src="{{ '/assets/img/xiaoying_liao.png' | relative_url }}" alt="Xiaoying Liao">
  </div>

  <div class="home-intro">
    <h1 class="home-title">Hello, I'm Xiaoying Liao.</h1>

    <div class="typing-intro" aria-label="I am an AI for Science researcher">
      <span aria-hidden="true">I am <span id="typed-text"></span><span class="typing-cursor">|</span></span>
    </div>

    <p>
      I am a Research Assistant in the <a href="https://www.devo-evo.com/people/xiaoying/">Qiu Lab</a> at
      <a href="https://www.stanford.edu/">Stanford University</a>, working at the intersection of <strong>AI and biology</strong>. My research
      focuses on single-cell and spatial genomics, computational modeling of development and disease, and AI-driven biological discovery.
    </p>

    <p>
      I have a background in both experimental and computational research. I earned my Master of Science in Engineering in Biomedical Engineering from
      <a href="https://www.jhu.edu/">Johns Hopkins University</a> and my Bachelor of Science (Honours) in Statistics from the
      <a href="https://www.sydney.edu.au/">University of Sydney</a>.
    </p>

    <div class="phd-callout">
      <div class="phd-title">I am actively seeking Ph.D. opportunities for Fall 2027.</div>
      <div class="phd-description">
        I am interested in developing AI methods for understanding biological systems and enabling scientific discovery. Please feel free to reach out!
      </div>
    </div>

    <div class="homepage-links">
      <a href="https://scholar.google.com/citations?user=UdXzuvkAAAAJ&amp;hl=zh-CN" target="_blank" rel="noopener noreferrer">
        <i class="ai ai-google-scholar" aria-hidden="true"></i> Scholar
      </a>
      <a href="https://github.com/Cristal0412" target="_blank" rel="noopener noreferrer">
        <i class="fa-brands fa-github" aria-hidden="true"></i> GitHub
      </a>
      <a href="https://www.linkedin.com/in/cristal-liao-64b4721b9/zh-cn?trk=people-guest_people_search-card" target="_blank" rel="noopener noreferrer">
        <i class="fa-brands fa-linkedin" aria-hidden="true"></i> LinkedIn
      </a>
      <a href="{{ '/assets/pdf/Xiaoying_Liao_CV.pdf' | relative_url }}" target="_blank" rel="noopener noreferrer">
        <i class="fa-solid fa-file-lines" aria-hidden="true"></i> CV
      </a>
      <a href="mailto:xliao@stanford.edu"> <i class="fa-solid fa-envelope" aria-hidden="true"></i> Email </a>
    </div>

  </div>
</div>

## Research Experience {#research-experience}

{% include research_experience.liquid %}

## Education {#education}

{% include custom_education.liquid %}

## Selected Publications {#selected-publications}

{% include selected_papers.liquid %}

[See all publications](/publications/)

## Teaching {#teaching}

#### Teaching Assistant · Cell & Tissue Engineering Lab, Johns Hopkins University | 2025–Present

Mentored students in cell culture, gene delivery, metabolic glycoengineering, tissue modeling, and scientific reporting.

#### Teaching Assistant · University of Sydney | 2023

Led tutorials in probability, statistical inference, R programming, data analytics, and introductory machine learning.

## Skills {#skills}

- **Programming and analysis:** Python, R, SQL, MATLAB, Stata, SAS, SPSS, Tableau, GraphPad Prism, FIJI/ImageJ.
- **Computational biology:** single-cell and spatial transcriptomics, statistical modeling, machine learning, bioinformatics.
- **Experimental biology:** cell and tissue culture, immunostaining, confocal and two-photon imaging, PCR/qRT-PCR, Western blot, genotyping, DNA/RNA extraction, mouse procedures.

## Honors & Awards {#honors-awards}

- Dalyell Scholar, University of Sydney (2022).
- Vice Chancellor’s Global Mobility Scholarship, University of Sydney (2020).
- Second Prize, China National High School Biology Olympiad (2018).

[Download the full CV (PDF)](/assets/pdf/Xiaoying_Liao_CV.pdf)

<script>
  document.addEventListener("DOMContentLoaded", function () {
    const phrases = [
      "an AI for Science researcher",
      "a biologist",
      "a dancer",
      "a life enthusiast",
      "an explorer of life"
    ];
    const typedText = document.getElementById("typed-text");
    if (!typedText) return;

    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      typedText.textContent = phrases[0];
      return;
    }

    let phraseIndex = 0;
    let charIndex = 0;
    let deleting = false;

    function type() {
      const phrase = phrases[phraseIndex];
      if (deleting) {
        charIndex--;
        typedText.textContent = phrase.slice(0, charIndex);
        if (charIndex === 0) {
          deleting = false;
          phraseIndex = (phraseIndex + 1) % phrases.length;
          setTimeout(type, 300);
          return;
        }
        setTimeout(type, 38);
      } else {
        charIndex++;
        typedText.textContent = phrase.slice(0, charIndex);
        if (charIndex === phrase.length) {
          deleting = true;
          setTimeout(type, 1400);
          return;
        }
        setTimeout(type, 70);
      }
    }

    type();
  });
</script>
