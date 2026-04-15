import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

// eslint-disable-next-line @typescript-eslint/no-require-imports
const theoryVersion = require('./package.json').version as string;

// GitHub Pages deployment configuration
// Set these environment variables in GitHub Actions:
// - GH_PAGES_URL: https://<username>.github.io
// - GH_PAGES_BASE_URL: /<repo-name>/
const ghPagesUrl = process.env.GH_PAGES_URL || 'https://holon.sh';
const ghPagesBaseUrl = process.env.GH_PAGES_BASE_URL || '/';

const config: Config = {
  title: 'UHM Theory',
  tagline: 'Unitary Holonomic Monism — Унитарный Голономный Монизм',
  favicon: 'img/favicon.ico',

  // future.v4 disabled — causes i18n translated docs to not load in 3.10.0
  // future: {
  //   v4: true,
  // },

  url: ghPagesUrl,
  baseUrl: ghPagesBaseUrl,

  organizationName: process.env.GH_ORG_NAME || 'uhm-theory',
  projectName: process.env.GH_PROJECT_NAME || 'holon',
  trailingSlash: false,

  onBrokenLinks: 'throw',

  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'ru'],
    localeConfigs: {
      ru: {
        label: 'Русский',
        htmlLang: 'ru-RU',
        translate: true,
        path: 'ru',
      },
      en: {
        label: 'English',
        htmlLang: 'en-US',
      },
    },
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          remarkPlugins: [remarkMath],
          rehypePlugins: [[rehypeKatex, {strict: false}]],
          showLastUpdateTime: false,
          showLastUpdateAuthor: false,
        },
        blog: {
          showReadingTime: true,
          blogTitle: 'UHM Blog',
          blogDescription: 'News and articles on the development of Unitary Holonomic Monism',
          postsPerPage: 10,
          blogSidebarTitle: 'Posts',
          blogSidebarCount: 'ALL',
          remarkPlugins: [remarkMath],
          rehypePlugins: [[rehypeKatex, {strict: false}]],
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themes: ['@docusaurus/theme-mermaid'],

  markdown: {
    mermaid: true,
    format: 'md',
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    },
  },

  clientModules: [
    require.resolve('./src/theme/MermaidRounded.js'),
  ],

  plugins: [
    [
      '@easyops-cn/docusaurus-search-local',
      {
        hashed: true,
        language: ['en', 'ru'],
        highlightSearchTermsOnTargetPage: true,
        explicitSearchResultPath: true,
        docsRouteBasePath: '/docs',
        indexBlog: true,
      },
    ],
    function ignoreVscodeWarningsPlugin() {
      return {
        name: 'ignore-vscode-warnings',
        configureWebpack() {
          return {
            ignoreWarnings: [
              {module: /vscode-languageserver-types/},
            ],
            module: {
              exprContextCritical: false,
            },
          };
        },
      };
    },
  ],

  stylesheets: [
    {
      href: 'https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css',
      type: 'text/css',
      integrity: 'sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV',
      crossorigin: 'anonymous',
    },
  ],

  themeConfig: {
    metadata: [
      { name: 'author', content: 'Max Sereda' },
      { name: 'creator', content: 'Max Sereda' },
    ],
    image: 'img/logo.svg',
    colorMode: {
      defaultMode: 'light',
      disableSwitch: false,
      respectPrefersColorScheme: true,
    },
    docs: {
      sidebar: {
        hideable: true,
        autoCollapseCategories: true,
      },
    },
    navbar: {
      // title: 'UHM',
      logo: {
        alt: 'UHM Theory Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'html',
          position: 'left',
          value: `<span class="navbar-version">v${theoryVersion}</span>`,
        },
        {
          type: 'docSidebar',
          sidebarId: 'theory',
          position: 'left',
          label: 'Theory',
        },
        {
          type: 'docSidebar',
          sidebarId: 'proofs',
          position: 'left',
          label: 'Proofs',
        },
        {
          type: 'docSidebar',
          sidebarId: 'physics',
          position: 'left',
          label: 'Physics',
        },
        {
          type: 'docSidebar',
          sidebarId: 'consciousness',
          position: 'left',
          label: 'Consciousness',
        },
        {
          type: 'docSidebar',
          sidebarId: 'cybernetics',
          position: 'left',
          label: 'Cybernetics',
        },
        {
          type: 'docSidebar',
          sidebarId: 'research',
          position: 'left',
          label: 'Research',
        },
        {
          type: 'docSidebar',
          sidebarId: 'reference',
          position: 'left',
          label: 'Reference',
        },
        {
          to: '/blog',
          label: 'Blog',
          position: 'left',
        },
        {
          type: 'localeDropdown',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Theory',
          items: [
            { label: 'Introduction', to: '/docs/intro' },
            { label: 'Axiom Ω⁷', to: '/docs/core/foundations/axiom-omega' },
            { label: 'Holon & Seven Dimensions', to: '/docs/core/structure/holon' },
            { label: 'Coherence Matrix Γ', to: '/docs/core/dynamics/coherence-matrix' },
            { label: 'Gap Operator', to: '/docs/core/dynamics/gap-operator' },
          ],
        },
        {
          title: 'Consciousness',
          items: [
            { label: 'Overview', to: '/docs/consciousness/overview' },
            { label: 'Self-Observation', to: '/docs/consciousness/foundations/self-observation' },
            { label: 'Hierarchy L0→L4', to: '/docs/consciousness/hierarchy/interiority-hierarchy' },
            { label: 'Qualia Structure', to: '/docs/consciousness/phenomenology/qualia-structure' },
            { label: 'States of Consciousness', to: '/docs/consciousness/states/altered-states' },
          ],
        },
        {
          title: 'Proofs',
          items: [
            { label: 'Minimality dim = 7', to: '/docs/proofs/minimality/theorem-minimality-7' },
            { label: 'Categorical Formalism', to: '/docs/proofs/categorical/categorical-formalism' },
            { label: 'Operator φ', to: '/docs/proofs/categorical/formalization-phi' },
            { label: 'Emergent Time', to: '/docs/proofs/dynamics/emergent-time' },
            { label: 'Fano Channel', to: '/docs/proofs/gap/fano-channel' },
          ],
        },
        {
          title: 'Physics',
          items: [
            { label: 'Correspondences', to: '/docs/physics/overview' },
            { label: 'G₂ Structure', to: '/docs/physics/gauge-symmetry/g2-structure' },
            { label: 'Particle Physics', to: '/docs/physics/particle-physics/fermion-generations' },
            { label: 'Gravity', to: '/docs/physics/gravity/emergent-geometry' },
            { label: 'Cosmological Constant', to: '/docs/physics/gravity/cosmological-constant' },
          ],
        },
        {
          title: 'Cybernetics',
          items: [
            { label: 'Coherence Cybernetics', to: '/docs/applied/coherence-cybernetics/introduction' },
            { label: 'Measurement Protocol', to: '/docs/applied/research/measurement-protocol' },
          ],
        },
        {
          title: 'Reference',
          items: [
            { label: 'Falsifiability', to: '/docs/reference/falsifiability' },
            { label: 'Status Registry', to: '/docs/reference/status-registry' },
            { label: 'Glossary', to: '/docs/reference/glossary' },
          ],
        },
      ],
      copyright: `© 2024-${new Date().getFullYear()} UHM Theory · Max Sereda. Theory: CC BY-NC-SA 4.0 | Code: MIT`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ['python', 'latex', 'bash'],
    },
    mermaid: {
      theme: {light: 'neutral', dark: 'dark'},
      options: {
        flowchart: {
          curve: 'basis',
          padding: 15,
          nodeSpacing: 50,
          rankSpacing: 50,
          defaultRenderer: 'dagre-wrapper',
          htmlLabels: true,
        },
        themeVariables: {
          nodeBorder: '1px',
          clusterBorder: '1px',
        },
      },
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
