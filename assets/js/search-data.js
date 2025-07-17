// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about",
    title: "about",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-publications",
          title: "publications",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications/";
          },
        },{id: "nav-cv",
          title: "cv",
          description: "👋 Here&#39;s my CV!",
          section: "Navigation",
          handler: () => {
            window.location.href = "/cv/";
          },
        },{id: "dropdown-blogs",
              title: "blogs",
              description: "",
              section: "Dropdown",
              handler: () => {
                window.location.href = "/blog/";
              },
            },{id: "dropdown-repositories",
              title: "repositories",
              description: "",
              section: "Dropdown",
              handler: () => {
                window.location.href = "";
              },
            },{id: "post-introduction-to-variational-inference",
      
        title: "Introduction to Variational Inference",
      
      description: "Notes for bounds in Variational Inference",
      section: "Posts",
      handler: () => {
        
          window.location.href = "/blog/2024/intro-2-vi/";
        
      },
    },{id: "post-probabilistic-machine-learning-basics",
      
        title: "Probabilistic Machine Learning Basics",
      
      description: "Notes for probabilistic ML foundations",
      section: "Posts",
      handler: () => {
        
          window.location.href = "/blog/2024/pml-notes/";
        
      },
    },{id: "post-the-family-of-denoising-diffusion-probabilistic-models",
      
        title: "The-Family of Denoising Diffusion Probabilistic Models",
      
      description: "An introduction to DDPM and its variants (i.e. DDIM and IDDPM), with toy implementations on CIFAR-10.",
      section: "Posts",
      handler: () => {
        
          window.location.href = "/blog/2024/family-of-ddpm/";
        
      },
    },{id: "news-i-completed-beng-in-data-science-hitsz",
          title: 'I completed BEng in Data Science @ HITsz 🎓.',
          description: "",
          section: "News",},{id: "news-i-completed-mphil-in-machine-learning-and-machine-intelligence-cambridge",
          title: 'I completed MPhil in Machine Learning and Machine Intelligence @ Cambridge 🎓.',
          description: "",
          section: "News",},{id: "news-i-started-a-new-position-as-research-assistant-in-machine-learning-cambridge",
          title: 'I started a new position as Research Assistant in Machine Learning @ Cambridge....',
          description: "",
          section: "News",},{id: "news-i-gave-an-oral-presentation-for-bnem-in-workshop-on-ml4molecules-ellis-2024",
          title: 'I gave an oral presentation for BNEM in Workshop on ML4Molecules @ ELLIS...',
          description: "",
          section: "News",},{id: "news-one-paper-is-accepted-by-icml-2025",
          title: 'One paper is accepted by ICML 2025 🎉',
          description: "",
          section: "News",},{id: "projects-project-2",
          title: 'project 2',
          description: "a project with a background image and giscus comments",
          section: "Projects",handler: () => {
              window.location.href = "/projects/2_project/";
            },},{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%72%6F%33%35%32@%63%61%6D.%61%63.%75%6B", "_blank");
        },
      },{
        id: 'social-github',
        title: 'GitHub',
        section: 'Socials',
        handler: () => {
          window.open("https://github.com/tonyauyeung", "_blank");
        },
      },{
        id: 'social-instagram',
        title: 'Instagram',
        section: 'Socials',
        handler: () => {
          window.open("https://instagram.com/tony.seoihong.auyeung", "_blank");
        },
      },{
        id: 'social-linkedin',
        title: 'LinkedIn',
        section: 'Socials',
        handler: () => {
          window.open("https://www.linkedin.com/in/tony-ruikang-ouyang-225845235", "_blank");
        },
      },{
        id: 'social-orcid',
        title: 'ORCID',
        section: 'Socials',
        handler: () => {
          window.open("https://orcid.org/0009-0004-1862-330X", "_blank");
        },
      },{
        id: 'social-rss',
        title: 'RSS Feed',
        section: 'Socials',
        handler: () => {
          window.open("/feed.xml", "_blank");
        },
      },{
        id: 'social-scholar',
        title: 'Google Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://scholar.google.com/citations?user=8G4PuYoAAAAJ", "_blank");
        },
      },{
        id: 'social-x',
        title: 'X',
        section: 'Socials',
        handler: () => {
          window.open("https://twitter.com/TonyRKOuYang", "_blank");
        },
      },{
        id: 'social-custom_social',
        title: 'Custom_social',
        section: 'Socials',
        handler: () => {
          window.open("https://www.tonyauyeung.com/", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
