import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

// KaTeX macros and the table-of-contents repair live in `plugins/`: the built-in
// contents builder reduces a formula in a heading to its bare TeX, and the repair
// rebuilds that entry from the heading itself, with the SAME macros as the page.
// eslint-disable-next-line @typescript-eslint/no-require-imports
const {katexMacros} = require('./plugins/katex-macros') as {
  katexMacros: Record<string, string>;
};
// eslint-disable-next-line @typescript-eslint/no-require-imports
const remarkTocKatex = require('./plugins/remark-toc-katex');

// eslint-disable-next-line @typescript-eslint/no-require-imports
const theoryVersion = require('./package.json').version as string;

// GitHub Pages deployment configuration
// Set these environment variables in GitHub Actions:
// - GH_PAGES_URL: https://<username>.github.io
// - GH_PAGES_BASE_URL: /<repo-name>/
const ghPagesUrl = process.env.GH_PAGES_URL || 'https://holon.sh';
const ghPagesBaseUrl = process.env.GH_PAGES_BASE_URL || '/';

// Large bilingual MDX caches can exhaust the shared validation disk.
// Persistent storage is opt-in; compiler acceleration remains enabled.
const persistentCache = process.env.DOCUSAURUS_PERSISTENT_CACHE === '1'
  && !process.env.CI && !process.env.DOCUSAURUS_DISABLE_WEBPACK_CACHE;

const config: Config = {
  title: 'UHM',
  tagline: 'Unitary Holonomic Monism — Унитарный Голономный Монизм',
  favicon: 'img/favicon.ico',

  // future.v4 stays OFF — it breaks i18n translated-doc loading in 3.10.x.
  // But experimental_faster is INDEPENDENT of v4 and gives the big build speedup:
  // Rspack (instead of Webpack) + SWC (instead of Babel/Terser) + Lightning CSS +
  // MDX cross-compiler cache (shared across the en/ru locales). ssgWorkerThreads is
  // the only sub-flag that requires v4, so it stays off.
  future: {
    faster: {
      rspackBundler: true,
      rspackPersistentCache: persistentCache,
      swcJsLoader: true,
      swcJsMinimizer: true,
      swcHtmlMinimizer: true,
      lightningCssMinimizer: true,
      mdxCrossCompilerCache: true,
      ssgWorkerThreads: false,
    },
  },

  url: ghPagesUrl,
  baseUrl: ghPagesBaseUrl,

  organizationName: process.env.GH_ORG_NAME || 'uhm-theory',
  projectName: process.env.GH_PROJECT_NAME || 'holon',
  trailingSlash: false,

  onBrokenLinks: 'throw',
  // Проверка якорей была молча выключена: сборка рапортовала ноль
  // предупреждений при доказанно битой ссылке реестра
  // (learning-bounds#t-111-стабильность — такого якоря в документе нет).
  // Выставлено явно 2026-07-28.
  onBrokenAnchors: 'warn',

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
          remarkPlugins: [remarkMath, remarkTocKatex],
          rehypePlugins: [[rehypeKatex, {strict: false, macros: katexMacros}]],
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
          remarkPlugins: [remarkMath, remarkTocKatex],
          rehypePlugins: [[rehypeKatex, {strict: false, macros: katexMacros}]],
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
    // 'detect': .md stays CommonMark (corpus-safe), .mdx gets true MDX (needed for
    // pages that import React components, e.g. core/dynamics/coherence-matrix.mdx).
    format: 'detect',
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    },
  },

  // Relative paths: require.resolve() bakes the absolute build-machine path
  // into the site metadata inside the shipped JS bundle, leaking the local
  // directory layout. Docusaurus resolves these relative to the site dir.
  clientModules: [
    './src/theme/MermaidRounded.js',
    './src/theme/TocMath.js',
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
    // Match the Webpack fallback to the Rspack storage policy. Rspack's
    // persistent store is controlled by the faster flag above, not this plugin.
    function boundWebpackCachePlugin() {
      return {
        name: 'bound-webpack-cache',
        configureWebpack() {
          if (!persistentCache) {
            return {
              mergeStrategy: {cache: 'replace' as const},
              cache: false,
            };
          }
          return {
            mergeStrategy: {cache: 'replace' as const},
            cache: {
              type: 'filesystem' as const,
              compression: 'gzip' as const,
              maxAge: 7 * 24 * 60 * 60 * 1000,
            },
          };
        },
      };
    },
  ],

  // KaTeX CSS — локально: рендерит установленный katex (0.16.28), а CDN-ссылка была
  // прибита SRI-хешем к 0.16.9. Код и стили KaTeX поставляются парой; расхождение версий
  // даёт тихие расхождения вёрстки, невидимые проверке разбора формул.
  stylesheets: [
    {
      href: '/katex/katex.min.css',
      type: 'text/css',
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
        alt: 'UHM Logo',
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
        {
          title: 'Related',
          items: [
            { label: 'Verum language', href: 'https://verum-lang.org/' },
          ],
        },
      ],
      copyright: `© 2024-${new Date().getFullYear()} UHM · Max Sereda. Theory: CC BY-NC-SA 4.0 | Code: MIT`,
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
