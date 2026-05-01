# Gregory Duane — Full Site Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a complete 8-page luxury bespoke fashion website for Gregory Duane — dark-mode editorial aesthetic, drawn from design.md with Tom Ford and Kenneth Cole as visual references.

**Architecture:** Pure HTML/CSS multi-page site. One shared `style.css` design system (CSS custom properties, no framework). One `nav.js` for mobile dropdown and scroll-transparency. Each page is a self-contained HTML file with copied nav and footer. No build step required.

**Tech Stack:** HTML5, CSS3 (custom properties, Grid, Flexbox), Vanilla JS (ES6+), Google Fonts (Noto Serif, Manrope, Tangerine)

---

## File Map

| File | Action | Purpose |
|---|---|---|
| `gregory-duane-tomford.html` | **Delete** | Stale experiment, outside nav |
| `style.css` | **Create** | Full design system |
| `nav.js` | **Create** | Scroll + dropdown behavior |
| `index.html` | **Rewrite** | Homepage |
| `custom-suits.html` | **Rewrite** | Men → Bespoke Suits |
| `ready-to-wear-suits.html` | **Rewrite** | Men → Ready to Wear |
| `handmade-shoes.html` | **Create** | Men → Handmade Shoes |
| `tuxedos.html` | **Create** | Men → Tuxedos |
| `wedding-dresses.html` | **Create** | Women → Wedding Dresses |
| `gallery.html` | **Create** | Gallery |
| `about-us.html` | **Rewrite** | About |

---

## Task 1: Delete stale file and init git

**Files:**
- Delete: `gregory-duane-tomford.html`

- [ ] **Step 1: Initialize git repo (project has none yet)**

```bash
git init
git add .
git commit -m "chore: initial commit — existing project files"
```

- [ ] **Step 2: Delete the stale file**

```bash
rm "gregory-duane-tomford.html"
```

- [ ] **Step 3: Verify deletion**

```bash
ls *.html
```

Expected output includes: `custom-suits.html  about-us.html  ready-to-wear-suits.html  index.html` — and does NOT include `gregory-duane-tomford.html`

- [ ] **Step 4: Commit**

```bash
git add -A
git commit -m "chore: remove stale tom ford design experiment"
```

---

## Task 2: Create style.css — Complete Design System

**Files:**
- Create: `style.css`

- [ ] **Step 1: Create style.css with the full design system**

```css
/* ============================================================
   GREGORY DUANE — Design System
   style.css
   ============================================================ */

@import url('https://fonts.googleapis.com/css2?family=Noto+Serif:ital,wght@0,300;0,400;1,400&family=Manrope:wght@400;600&family=Tangerine:wght@700&display=swap');

/* 1. Reset */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
img { display: block; max-width: 100%; }
a { color: inherit; text-decoration: none; }
ul { list-style: none; }
button { cursor: pointer; }

/* 2. Design Tokens */
:root {
  --bg:           #121414;
  --surface:      #1e2020;
  --surface-high: #282a2b;
  --gold:         #e9c349;
  --silver:       #c6c6c6;
  --white:        #e2e2e2;
  --muted:        #8e9192;
  --outline:      #444748;

  --font-serif:   'Noto Serif', Georgia, serif;
  --font-sans:    'Manrope', system-ui, sans-serif;
  --font-script:  'Tangerine', cursive;

  --section-gap:  128px;
  --page-margin:  64px;
  --gutter:       24px;
  --max-width:    1440px;
}

/* 3. Base */
html { scroll-behavior: smooth; }
body {
  background: var(--bg);
  color: var(--white);
  font-family: var(--font-sans);
  font-size: 16px;
  line-height: 1.6;
  overflow-x: hidden;
}

/* 4. Typography Utilities */
.label-caps {
  font-family: var(--font-sans);
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.2em;
  text-transform: uppercase;
}
.headline-lg {
  font-family: var(--font-serif);
  font-size: clamp(28px, 3.5vw, 40px);
  font-weight: 400;
  line-height: 1.2;
}
.headline-md {
  font-family: var(--font-serif);
  font-size: clamp(22px, 2.5vw, 32px);
  font-weight: 400;
  line-height: 1.3;
}
.pull-quote {
  font-family: var(--font-serif);
  font-size: clamp(24px, 3vw, 40px);
  font-weight: 300;
  font-style: italic;
  color: var(--silver);
  line-height: 1.35;
}

/* 5. Layout */
.container {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 0 var(--page-margin);
}
.section { padding: var(--section-gap) 0; }
.divider {
  width: 60px;
  height: 1px;
  background: var(--gold);
  margin: 0 auto 32px;
}

/* 6. Announcement Bar */
.announce-bar {
  background: var(--bg);
  border-bottom: 1px solid var(--outline);
  text-align: center;
  padding: 10px var(--page-margin);
  color: var(--gold);
  font-family: var(--font-sans);
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.2em;
  text-transform: uppercase;
}
.announce-bar a { color: inherit; }

/* 7. Navigation */
.site-nav {
  position: sticky;
  top: 0;
  z-index: 100;
  background: transparent;
  transition: background 0.35s ease, border-color 0.35s ease;
  border-bottom: 1px solid transparent;
}
.site-nav.scrolled {
  background: var(--bg);
  border-bottom-color: var(--outline);
}

.nav-inner {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  height: 72px;
  padding: 0 var(--page-margin);
  max-width: var(--max-width);
  margin: 0 auto;
}

.nav-left {
  display: flex;
  align-items: center;
  gap: 36px;
}
.nav-right {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 28px;
}
.nav-logo img {
  height: 30px;
  width: auto;
}
.nav-left a,
.nav-right a {
  font-family: var(--font-sans);
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--white);
  opacity: 0.72;
  transition: opacity 0.2s;
}
.nav-left a:hover,
.nav-right a:hover { opacity: 1; }

/* Dropdowns */
.has-dropdown { position: relative; }
.has-dropdown > a::after { content: ' ▾'; font-size: 8px; }
.dropdown-menu {
  display: none;
  position: absolute;
  top: calc(100% + 12px);
  left: 0;
  background: var(--surface);
  border: 1px solid var(--outline);
  min-width: 190px;
  padding: 8px 0;
}
.has-dropdown:hover .dropdown-menu { display: block; }
.dropdown-menu li a {
  display: block;
  padding: 11px 20px;
  font-size: 11px;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--white);
  opacity: 0.72;
  transition: opacity 0.2s, color 0.2s;
}
.dropdown-menu li a:hover { opacity: 1; color: var(--gold); }

/* Nav CTA */
.nav-cta {
  padding: 9px 18px !important;
  border: 1px solid var(--silver) !important;
  opacity: 1 !important;
  transition: border-color 0.2s, color 0.2s !important;
}
.nav-cta:hover {
  border-color: var(--gold) !important;
  color: var(--gold) !important;
}

/* Hamburger */
.menu-toggle {
  display: none;
  background: none;
  border: none;
  padding: 4px;
  flex-direction: column;
  gap: 5px;
}
.menu-toggle span {
  display: block;
  width: 22px;
  height: 1px;
  background: var(--white);
  transition: 0.3s;
}

/* Mobile overlay menu */
.mobile-menu {
  display: none;
  position: fixed;
  top: 72px;
  left: 0;
  right: 0;
  bottom: 0;
  background: var(--bg);
  border-top: 1px solid var(--outline);
  padding: 40px var(--page-margin);
  overflow-y: auto;
  z-index: 99;
  flex-direction: column;
  gap: 4px;
}
.mobile-menu.open { display: flex; }
.mobile-menu a {
  font-family: var(--font-sans);
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--white);
  padding: 14px 0;
  border-bottom: 1px solid var(--outline);
  opacity: 0.8;
  display: block;
}
.mobile-menu > a:hover,
.mobile-menu .has-dropdown > a:hover { opacity: 1; }
.mobile-menu .has-dropdown > a::after { content: '  +'; }
.mobile-menu .has-dropdown.active > a::after { content: '  −'; }
.mobile-menu .dropdown-menu {
  position: static;
  border: none;
  background: none;
  padding: 4px 0 4px 16px;
  min-width: 0;
}
.mobile-menu .dropdown-menu li a {
  border-bottom: none;
  color: var(--muted);
  padding: 9px 0;
  font-size: 11px;
}
.mobile-menu .dropdown-menu li a:hover { color: var(--gold); opacity: 1; }
.mobile-menu .has-dropdown.active .dropdown-menu { display: block; }
.mobile-menu .btn-ghost { margin-top: 24px; text-align: center; }

/* 8. Buttons */
.btn-primary {
  display: inline-block;
  padding: 15px 38px;
  background: var(--white);
  color: #0c0f0f;
  font-family: var(--font-sans);
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  border: none;
  transition: background 0.2s, color 0.2s;
}
.btn-primary:hover { background: var(--gold); color: #0c0f0f; }

.btn-ghost {
  display: inline-block;
  padding: 15px 38px;
  background: transparent;
  color: var(--white);
  font-family: var(--font-sans);
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  border: 1px solid var(--silver);
  transition: border-color 0.2s, color 0.2s;
}
.btn-ghost:hover { border-color: var(--gold); color: var(--gold); }

/* 9. Hero (Homepage — 100vh) */
.hero {
  position: relative;
  width: 100%;
  height: 100vh;
  overflow: hidden;
}
.hero > img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center top;
}
.hero-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to bottom, rgba(18,20,20,0.25) 0%, rgba(18,20,20,0.55) 100%);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 0 var(--page-margin);
}
.hero-signature {
  font-family: var(--font-script);
  font-size: clamp(72px, 10vw, 130px);
  color: var(--white);
  line-height: 1;
  margin-bottom: 12px;
}
.hero-rule {
  width: 56px;
  height: 1px;
  background: var(--gold);
  margin: 0 auto 28px;
}
.hero-subtitle {
  font-family: var(--font-sans);
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  color: var(--white);
  opacity: 0.9;
  margin-bottom: 44px;
}

/* 10. Page Hero (Inner pages — 60vh) */
.page-hero {
  position: relative;
  height: 60vh;
  overflow: hidden;
}
.page-hero > img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center top;
}
.page-hero-overlay {
  position: absolute;
  inset: 0;
  background: rgba(18,20,20,0.52);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-end;
  padding-bottom: 72px;
  text-align: center;
}
.page-hero-label {
  font-family: var(--font-sans);
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.25em;
  text-transform: uppercase;
  color: var(--gold);
  margin-bottom: 16px;
}
.page-hero-title {
  font-family: var(--font-serif);
  font-size: clamp(32px, 5vw, 58px);
  font-weight: 300;
  color: var(--white);
  line-height: 1.1;
}

/* 11. Cards (Category) */
.card {
  position: relative;
  overflow: hidden;
  aspect-ratio: 3/4;
  display: block;
}
.card > img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.65s ease;
}
.card:hover > img { transform: scale(1.04); }
.card-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(18,20,20,0.82) 0%, transparent 55%);
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: 28px;
}
.card-overlay::after {
  content: '';
  position: absolute;
  inset: 0;
  border: 1px solid transparent;
  transition: border-color 0.3s;
  pointer-events: none;
}
.card:hover .card-overlay::after { border-color: var(--gold); }
.card-label {
  font-family: var(--font-sans);
  font-size: 10px;
  font-weight: 600;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--gold);
  margin-bottom: 6px;
}
.card-title {
  font-family: var(--font-serif);
  font-size: 22px;
  font-weight: 400;
  color: var(--white);
}

/* 12. Grids */
.grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--gutter);
}
.grid-2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: var(--gutter);
}

/* 13. Brand Statement */
.brand-statement {
  text-align: center;
  max-width: 760px;
  margin: 0 auto;
}
.brand-statement .display {
  font-family: var(--font-serif);
  font-size: clamp(36px, 5vw, 64px);
  font-weight: 300;
  line-height: 1.1;
  letter-spacing: -0.01em;
  color: var(--white);
  margin-bottom: 32px;
}
.brand-statement p {
  font-size: 17px;
  color: var(--muted);
  line-height: 1.75;
}

/* 14. RTW Feature Block */
.rtw-feature { padding: var(--section-gap) 0; }
.rtw-feature-inner {
  display: grid;
  grid-template-columns: 60fr 40fr;
  gap: 72px;
  align-items: center;
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 0 var(--page-margin);
}
.rtw-feature-img {
  width: 100%;
  aspect-ratio: 4/5;
  object-fit: cover;
}
.rtw-feature-content .label-caps {
  color: var(--gold);
  display: block;
  margin-bottom: 20px;
}
.rtw-feature-content .headline-lg { margin-bottom: 24px; }
.rtw-feature-content p {
  color: var(--muted);
  font-size: 16px;
  line-height: 1.75;
  margin-bottom: 36px;
}

/* 15. Editorial Pull-Quote Section */
.editorial-quote {
  background: var(--surface);
  padding: var(--section-gap) var(--page-margin);
  text-align: center;
}
.editorial-quote .pull-quote { max-width: 900px; margin: 0 auto 24px; }
.editorial-quote .attribution {
  font-family: var(--font-sans);
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--muted);
}

/* 16. CTA Band */
.cta-band {
  background: var(--surface);
  padding: 96px var(--page-margin);
  text-align: center;
}
.cta-band .headline-md { margin-bottom: 12px; }
.cta-band p {
  color: var(--muted);
  margin-bottom: 36px;
  font-size: 15px;
}

/* 17. Intro Section (2-col) */
.intro-section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 72px;
  align-items: center;
  max-width: var(--max-width);
  margin: 0 auto;
  padding: var(--section-gap) var(--page-margin);
}
.intro-content .label-caps {
  color: var(--gold);
  display: block;
  margin-bottom: 20px;
}
.intro-content .headline-lg { margin-bottom: 24px; }
.intro-content p {
  color: var(--muted);
  font-size: 16px;
  line-height: 1.75;
}
.intro-img {
  width: 100%;
  aspect-ratio: 3/4;
  object-fit: cover;
}

/* 18. Process Steps */
.steps-section {
  background: var(--surface);
  padding: var(--section-gap) var(--page-margin);
  text-align: center;
}
.steps-section-title {
  font-family: var(--font-serif);
  font-size: clamp(22px, 2vw, 30px);
  font-weight: 400;
  color: var(--white);
  margin-bottom: 16px;
}
.steps-section-sub {
  color: var(--muted);
  font-size: 15px;
  margin-bottom: 64px;
  max-width: 560px;
  margin-left: auto;
  margin-right: auto;
}
.steps-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 48px;
  max-width: 1100px;
  margin: 0 auto;
  text-align: left;
}
.step-number {
  font-family: var(--font-sans);
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--gold);
  margin-bottom: 16px;
}
.step-title {
  font-family: var(--font-serif);
  font-size: 20px;
  font-weight: 400;
  color: var(--white);
  margin-bottom: 12px;
}
.step-desc {
  font-size: 14px;
  color: var(--muted);
  line-height: 1.7;
}

/* 19. Image Grid */
.image-grid {
  display: grid;
  gap: 4px;
}
.image-grid.cols-2 { grid-template-columns: repeat(2, 1fr); }
.image-grid.cols-3 { grid-template-columns: repeat(3, 1fr); }
.image-grid img {
  width: 100%;
  aspect-ratio: 4/3;
  object-fit: cover;
  display: block;
}

/* 20. Product Grid (RTW) */
.product-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--gutter);
}
.product-card img {
  width: 100%;
  aspect-ratio: 2/3;
  object-fit: cover;
  transition: transform 0.5s ease;
}
.product-card:hover img { transform: scale(1.03); }
.product-info { padding: 14px 0 0; }
.product-name {
  font-family: var(--font-sans);
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--white);
  transition: color 0.2s;
}
.product-card:hover .product-name { color: var(--gold); }

/* 21. Masonry Gallery */
.masonry {
  columns: 3;
  column-gap: 4px;
}
.masonry img {
  width: 100%;
  display: block;
  margin-bottom: 4px;
  break-inside: avoid;
}

/* 22. About Story */
.about-story {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 80px;
  align-items: start;
  max-width: var(--max-width);
  margin: 0 auto;
  padding: var(--section-gap) var(--page-margin);
}
.about-story .pull-quote { margin-bottom: 0; }
.about-story-text p {
  color: var(--muted);
  font-size: 16px;
  line-height: 1.8;
  margin-bottom: 20px;
}

/* 23. Values */
.values-section {
  background: var(--surface);
  padding: var(--section-gap) var(--page-margin);
  text-align: center;
}
.values-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 56px;
  max-width: 1000px;
  margin: 0 auto;
}
.value-name {
  font-family: var(--font-sans);
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--gold);
  margin-bottom: 16px;
  display: block;
}
.value-desc {
  font-size: 14px;
  color: var(--muted);
  line-height: 1.75;
}

/* 24. Footer */
footer {
  background: var(--bg);
  border-top: 1px solid var(--outline);
  padding: 72px var(--page-margin) 32px;
}
.footer-grid {
  display: grid;
  grid-template-columns: 1.5fr 1fr 1fr 1fr;
  gap: 48px;
  max-width: var(--max-width);
  margin: 0 auto 48px;
}
.footer-logo img {
  height: 36px;
  width: auto;
  margin-bottom: 20px;
}
.footer-tagline {
  font-size: 13px;
  color: var(--muted);
  line-height: 1.65;
  max-width: 240px;
}
.footer-heading {
  font-family: var(--font-sans);
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--silver);
  margin-bottom: 20px;
}
.footer-links { display: flex; flex-direction: column; gap: 12px; }
.footer-links a {
  font-size: 13px;
  color: var(--muted);
  transition: color 0.2s;
}
.footer-links a:hover { color: var(--white); }
.footer-contact {
  font-size: 13px;
  color: var(--muted);
  line-height: 1.9;
  margin-bottom: 24px;
}
.footer-contact a { color: inherit; }
.footer-contact a:hover { color: var(--white); }
.footer-bottom {
  border-top: 1px solid var(--outline);
  padding-top: 24px;
  text-align: center;
  font-size: 11px;
  letter-spacing: 0.1em;
  color: var(--muted);
  max-width: var(--max-width);
  margin: 0 auto;
}

/* 25. Responsive */
@media (max-width: 1024px) {
  :root { --page-margin: 32px; --section-gap: 88px; }
  .grid-3 { grid-template-columns: repeat(2, 1fr); }
  .footer-grid { grid-template-columns: 1fr 1fr; gap: 36px; }
  .steps-grid { grid-template-columns: 1fr 1fr; }
  .masonry { columns: 2; }
  .product-grid { grid-template-columns: repeat(2, 1fr); }
  .rtw-feature-inner { grid-template-columns: 1fr 1fr; gap: 40px; }
}

@media (max-width: 768px) {
  :root { --page-margin: 20px; --section-gap: 64px; }
  .nav-left { display: none; }
  .nav-right a:not(.menu-toggle):not(.nav-cta) { display: none; }
  .nav-right .nav-cta { display: none; }
  .menu-toggle { display: flex; }
  .mobile-menu { top: 60px; }
  .nav-inner { height: 60px; }
  .intro-section { grid-template-columns: 1fr; }
  .intro-section .intro-img { order: -1; }
  .about-story { grid-template-columns: 1fr; }
  .rtw-feature-inner { grid-template-columns: 1fr; }
  .grid-3 { grid-template-columns: 1fr; }
  .grid-2 { grid-template-columns: 1fr; }
  .steps-grid { grid-template-columns: 1fr; }
  .footer-grid { grid-template-columns: 1fr; }
  .values-grid { grid-template-columns: 1fr; gap: 32px; }
  .product-grid { grid-template-columns: repeat(2, 1fr); }
  .masonry { columns: 2; }
  .image-grid.cols-3 { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 480px) {
  .masonry { columns: 1; }
  .product-grid { grid-template-columns: 1fr; }
  .image-grid.cols-2 { grid-template-columns: 1fr; }
}
```

- [ ] **Step 2: Verify file exists**

```bash
ls -lh style.css
```

Expected: file present, size ~8–12 KB

- [ ] **Step 3: Commit**

```bash
git add style.css
git commit -m "feat: add complete design system CSS"
```

---

## Task 3: Create nav.js — Scroll transparency and mobile dropdown

**Files:**
- Create: `nav.js`

- [ ] **Step 1: Create nav.js**

```javascript
/* Gregory Duane — nav.js */

const nav = document.querySelector('.site-nav');
const mobileMenu = document.querySelector('.mobile-menu');
const menuToggle = document.querySelector('.menu-toggle');

// Transparent → solid nav on scroll
if (nav) {
  window.addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', window.scrollY > 72);
  }, { passive: true });
}

// Mobile menu open/close
if (menuToggle && mobileMenu) {
  menuToggle.addEventListener('click', () => {
    const isOpen = mobileMenu.classList.toggle('open');
    menuToggle.setAttribute('aria-expanded', isOpen);
    mobileMenu.setAttribute('aria-hidden', !isOpen);
  });
}

// Mobile accordion dropdowns
document.querySelectorAll('.mobile-menu .has-dropdown > a').forEach(link => {
  link.addEventListener('click', e => {
    e.preventDefault();
    link.closest('.has-dropdown').classList.toggle('active');
  });
});

// Close mobile menu on resize to desktop
window.addEventListener('resize', () => {
  if (window.innerWidth > 768 && mobileMenu) {
    mobileMenu.classList.remove('open');
    if (menuToggle) menuToggle.setAttribute('aria-expanded', 'false');
  }
}, { passive: true });
```

- [ ] **Step 2: Commit**

```bash
git add nav.js
git commit -m "feat: add nav scroll and mobile dropdown"
```

---

## Task 4: Build index.html — Homepage

**Files:**
- Rewrite: `index.html`

- [ ] **Step 1: Replace index.html with the full homepage**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Gregory Duane — Bespoke Tailoring & Handmade Footwear</title>
  <meta name="description" content="Gregory Duane offers bespoke custom suits, handmade shoes, and bridal attire. New York. By appointment only. Call (646) 516-2664.">
  <link rel="icon" href="images/gregory-duane-favicon.png">
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <!-- Announcement Bar -->
  <div class="announce-bar">
    Bespoke. By Appointment Only.&nbsp;&nbsp;·&nbsp;&nbsp;<a href="tel:6465162664">(646) 516-2664</a>
  </div>

  <!-- Navigation -->
  <nav class="site-nav" aria-label="Main navigation">
    <div class="nav-inner">
      <div class="nav-left">
        <div class="has-dropdown">
          <a href="#">Men</a>
          <ul class="dropdown-menu">
            <li><a href="custom-suits.html">Bespoke Suits</a></li>
            <li><a href="ready-to-wear-suits.html">Ready to Wear</a></li>
            <li><a href="handmade-shoes.html">Handmade Shoes</a></li>
            <li><a href="tuxedos.html">Tuxedos</a></li>
          </ul>
        </div>
        <div class="has-dropdown">
          <a href="#">Women</a>
          <ul class="dropdown-menu">
            <li><a href="wedding-dresses.html">Wedding Dresses</a></li>
          </ul>
        </div>
      </div>

      <a class="nav-logo" href="index.html" aria-label="Gregory Duane home">
        <img src="images/Gregory-Duane_white_high-res.png" alt="Gregory Duane" />
      </a>

      <div class="nav-right">
        <a href="gallery.html">Gallery</a>
        <a href="about-us.html">About</a>
        <a href="mailto:Gregoryduaneservice@gregoryduane.com" class="nav-cta">Book a Consultation</a>
        <button class="menu-toggle" aria-label="Toggle menu" aria-expanded="false">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>

    <!-- Mobile Menu -->
    <div class="mobile-menu" aria-hidden="true">
      <div class="has-dropdown">
        <a href="#">Men</a>
        <ul class="dropdown-menu">
          <li><a href="custom-suits.html">Bespoke Suits</a></li>
          <li><a href="ready-to-wear-suits.html">Ready to Wear</a></li>
          <li><a href="handmade-shoes.html">Handmade Shoes</a></li>
          <li><a href="tuxedos.html">Tuxedos</a></li>
        </ul>
      </div>
      <div class="has-dropdown">
        <a href="#">Women</a>
        <ul class="dropdown-menu">
          <li><a href="wedding-dresses.html">Wedding Dresses</a></li>
        </ul>
      </div>
      <a href="gallery.html">Gallery</a>
      <a href="about-us.html">About</a>
      <a href="mailto:Gregoryduaneservice@gregoryduane.com" class="btn-ghost">Book a Consultation</a>
    </div>
  </nav>

  <!-- Hero -->
  <section class="hero">
    <img src="images/pexels-the-lazy-artist-gallery-1300550.jpg" alt="Gregory Duane bespoke suit editorial" />
    <div class="hero-overlay">
      <div class="hero-signature">Gregory Duane</div>
      <div class="hero-rule"></div>
      <p class="hero-subtitle">Bespoke Tailoring&nbsp;&nbsp;·&nbsp;&nbsp;Handmade Footwear&nbsp;&nbsp;·&nbsp;&nbsp;Bridal</p>
      <a href="custom-suits.html" class="btn-ghost">Explore the Collection</a>
    </div>
  </section>

  <!-- Brand Statement -->
  <section class="section">
    <div class="container">
      <div class="brand-statement">
        <span class="label-caps" style="color:var(--gold);display:block;margin-bottom:24px;">Est. New York</span>
        <h2 class="display">Where craftsmanship<br>meets legacy.</h2>
        <div class="divider" style="margin-top:32px;"></div>
        <p>Gregory Duane is built on the belief that clothing should be an extension of your personality — meticulously crafted to your unique measurements, your life, and your legacy. Every piece begins with a conversation and ends with a statement.</p>
      </div>
    </div>
  </section>

  <!-- Featured Categories -->
  <section style="padding:0 var(--page-margin) var(--section-gap);">
    <div style="max-width:var(--max-width);margin:0 auto;">
      <div class="grid-3">
        <a href="custom-suits.html" class="card">
          <img src="images/pexels-terje-sollie-298863.jpg" alt="Bespoke Suits" />
          <div class="card-overlay">
            <span class="card-label">Men</span>
            <span class="card-title">Bespoke Suits</span>
          </div>
        </a>
        <a href="handmade-shoes.html" class="card">
          <img src="images/ruthson-zimmerman-Ws4wd-vJ9M0-unsplash.jpg" alt="Handmade Shoes" />
          <div class="card-overlay">
            <span class="card-label">Men</span>
            <span class="card-title">Handmade Shoes</span>
          </div>
        </a>
        <a href="tuxedos.html" class="card">
          <img src="images/ivan-zhukevich-7ZC4qO3Gj6g-unsplash.jpg" alt="Bridal" />
          <div class="card-overlay">
            <span class="card-label">Bridal</span>
            <span class="card-title">Tuxedos & Gowns</span>
          </div>
        </a>
      </div>
    </div>
  </section>

  <!-- Ready to Wear Feature -->
  <section class="rtw-feature">
    <div class="rtw-feature-inner">
      <img src="images/max-andrey-4YWwPsTQfMs-unsplash.jpg" alt="Ready to Wear" class="rtw-feature-img" />
      <div class="rtw-feature-content">
        <span class="label-caps">Ready to Wear</span>
        <h2 class="headline-lg">Premium Suits,<br>Ready When You Are.</h2>
        <p>Not every moment calls for a months-long bespoke journey. Our ready-to-wear collection pairs the aesthetic rigor of Gregory Duane craftsmanship with the immediacy of available stock — expertly designed silhouettes, premium fabrics, no waiting.</p>
        <a href="ready-to-wear-suits.html" class="btn-ghost">Shop Ready to Wear</a>
      </div>
    </div>
  </section>

  <!-- Editorial Pull Quote -->
  <section class="editorial-quote">
    <p class="pull-quote">"In a world of fast fashion, we chose the longer road — the one that leads to a garment that fits not just your body, but your life."</p>
    <span class="attribution">— Duane Glover, Founder</span>
  </section>

  <!-- Footer -->
  <footer>
    <div class="footer-grid">
      <div class="footer-logo">
        <img src="images/Gregory-Duane_white_high-res.png" alt="Gregory Duane" />
        <p class="footer-tagline">Bespoke tailoring, handmade footwear, and bridal atelier. New York. By appointment only.</p>
      </div>
      <div>
        <p class="footer-heading">Men</p>
        <ul class="footer-links">
          <li><a href="custom-suits.html">Bespoke Suits</a></li>
          <li><a href="ready-to-wear-suits.html">Ready to Wear</a></li>
          <li><a href="handmade-shoes.html">Handmade Shoes</a></li>
          <li><a href="tuxedos.html">Tuxedos</a></li>
        </ul>
      </div>
      <div>
        <p class="footer-heading">Women</p>
        <ul class="footer-links">
          <li><a href="wedding-dresses.html">Wedding Dresses</a></li>
        </ul>
        <p class="footer-heading" style="margin-top:32px;">Explore</p>
        <ul class="footer-links">
          <li><a href="gallery.html">Gallery</a></li>
          <li><a href="about-us.html">About Us</a></li>
        </ul>
      </div>
      <div>
        <p class="footer-heading">Consultation</p>
        <div class="footer-contact">
          <p><a href="tel:6465162664">(646) 516-2664</a></p>
          <p><a href="mailto:Gregoryduaneservice@gregoryduane.com">Gregoryduaneservice@gregoryduane.com</a></p>
          <p style="margin-top:12px;">Open by appointment · All days</p>
        </div>
        <a href="mailto:Gregoryduaneservice@gregoryduane.com" class="btn-primary">Book a Consultation</a>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 Gregory Duane. All rights reserved.</p>
    </div>
  </footer>

  <script src="nav.js"></script>
</body>
</html>
```

- [ ] **Step 2: Open index.html in a browser and verify**

Check:
- Background is dark charcoal (#121414) ✓
- Nav is transparent over hero, transitions to solid on scroll ✓
- Hero fills 100vh with suit editorial image ✓
- "Gregory Duane" signature displays in script font ✓
- Gold underline rule appears below signature ✓
- Three category cards appear in a grid ✓
- RTW feature section shows 60/40 split layout ✓
- Pull quote section has slightly lighter charcoal background ✓
- Footer shows 4-column layout ✓

- [ ] **Step 3: Commit**

```bash
git add index.html
git commit -m "feat: build homepage"
```

---

## Task 5: Build custom-suits.html — Bespoke Suits (Template A)

**Files:**
- Rewrite: `custom-suits.html`

- [ ] **Step 1: Replace custom-suits.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bespoke Suits — Gregory Duane</title>
  <meta name="description" content="Custom bespoke suits crafted to your exact measurements and lifestyle. Gregory Duane, New York. By appointment only.">
  <link rel="icon" href="images/gregory-duane-favicon.png">
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <div class="announce-bar">
    Bespoke. By Appointment Only.&nbsp;&nbsp;·&nbsp;&nbsp;<a href="tel:6465162664">(646) 516-2664</a>
  </div>

  <nav class="site-nav" aria-label="Main navigation">
    <div class="nav-inner">
      <div class="nav-left">
        <div class="has-dropdown">
          <a href="#">Men</a>
          <ul class="dropdown-menu">
            <li><a href="custom-suits.html">Bespoke Suits</a></li>
            <li><a href="ready-to-wear-suits.html">Ready to Wear</a></li>
            <li><a href="handmade-shoes.html">Handmade Shoes</a></li>
            <li><a href="tuxedos.html">Tuxedos</a></li>
          </ul>
        </div>
        <div class="has-dropdown">
          <a href="#">Women</a>
          <ul class="dropdown-menu">
            <li><a href="wedding-dresses.html">Wedding Dresses</a></li>
          </ul>
        </div>
      </div>
      <a class="nav-logo" href="index.html" aria-label="Gregory Duane home">
        <img src="images/Gregory-Duane_white_high-res.png" alt="Gregory Duane" />
      </a>
      <div class="nav-right">
        <a href="gallery.html">Gallery</a>
        <a href="about-us.html">About</a>
        <a href="mailto:Gregoryduaneservice@gregoryduane.com" class="nav-cta">Book a Consultation</a>
        <button class="menu-toggle" aria-label="Toggle menu" aria-expanded="false">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
    <div class="mobile-menu" aria-hidden="true">
      <div class="has-dropdown">
        <a href="#">Men</a>
        <ul class="dropdown-menu">
          <li><a href="custom-suits.html">Bespoke Suits</a></li>
          <li><a href="ready-to-wear-suits.html">Ready to Wear</a></li>
          <li><a href="handmade-shoes.html">Handmade Shoes</a></li>
          <li><a href="tuxedos.html">Tuxedos</a></li>
        </ul>
      </div>
      <div class="has-dropdown">
        <a href="#">Women</a>
        <ul class="dropdown-menu">
          <li><a href="wedding-dresses.html">Wedding Dresses</a></li>
        </ul>
      </div>
      <a href="gallery.html">Gallery</a>
      <a href="about-us.html">About</a>
      <a href="mailto:Gregoryduaneservice@gregoryduane.com" class="btn-ghost">Book a Consultation</a>
    </div>
  </nav>

  <!-- Page Hero -->
  <div class="page-hero">
    <img src="images/pexels-anders-kristensen-447570.jpg" alt="Bespoke suit craftsmanship" />
    <div class="page-hero-overlay">
      <span class="page-hero-label">Men</span>
      <h1 class="page-hero-title">Bespoke Suits</h1>
    </div>
  </div>

  <!-- Intro -->
  <div class="intro-section">
    <div class="intro-content">
      <span class="label-caps">The Gregory Duane Standard</span>
      <h2 class="headline-lg">Made for you.<br>Only for you.</h2>
      <p>Every suit begins as a conversation. We spend time understanding not just your measurements, but your life — where you wear it, how you move, what you want to say without saying a word. The result is a garment built around your body, your personality, and your ambitions.</p>
    </div>
    <img src="images/pexels-antoni-shkraba-5264913.jpg" alt="Bespoke suit detail" class="intro-img" />
  </div>

  <!-- Process Steps -->
  <section class="steps-section">
    <h2 class="steps-section-title">The Bespoke Process</h2>
    <p class="steps-section-sub">Three stages. Unlimited adjustments. One garment that belongs to no one else.</p>
    <div class="steps-grid">
      <div>
        <p class="step-number">01 — The Consultation</p>
        <h3 class="step-title">We Meet. We Listen.</h3>
        <p class="step-desc">We assess your lifestyle, style references, and the occasions your suit must rise to. No two consultations are alike because no two clients are alike.</p>
      </div>
      <div>
        <p class="step-number">02 — The Fabric</p>
        <h3 class="step-title">Select Your Canvas.</h3>
        <p class="step-desc">Choose from our curated library of Italian, British, and Japanese mills. Every bolt is selected for handle, drape, and longevity — fabrics that improve with each wear.</p>
      </div>
      <div>
        <p class="step-number">03 — The Fitting</p>
        <h3 class="step-title">Cut. Adjust. Perfect.</h3>
        <p class="step-desc">Three fittings minimum. We cut, we refine, we adjust until the garment moves with you. The final suit is yours alone — no pattern, no template, no compromise.</p>
      </div>
    </div>
  </section>

  <!-- Image Grid -->
  <section style="padding:var(--section-gap) var(--page-margin);">
    <div style="max-width:var(--max-width);margin:0 auto;">
      <div class="image-grid cols-2">
        <img src="images/pexels-the-lazy-artist-gallery-1303866.jpg" alt="Suit detail" />
        <img src="images/pexels-photo-4173182.png.png" alt="Bespoke craftsmanship" />
        <img src="images/bruce-mars-S8ffHr_dxHo-unsplash.jpg" alt="Suit fitting" />
        <img src="images/andrew-neel-cckf4TsHAuw-unsplash.jpg" alt="Fabric selection" />
      </div>
    </div>
  </section>

  <!-- CTA Band -->
  <section class="cta-band">
    <h2 class="headline-md">Begin Your Bespoke Journey</h2>
    <p>Consultations by appointment. Every commission begins with a conversation.</p>
    <a href="mailto:Gregoryduaneservice@gregoryduane.com" class="btn-primary">Book a Consultation</a>
  </section>

  <!-- Footer -->
  <footer>
    <div class="footer-grid">
      <div class="footer-logo">
        <img src="images/Gregory-Duane_white_high-res.png" alt="Gregory Duane" />
        <p class="footer-tagline">Bespoke tailoring, handmade footwear, and bridal atelier. New York. By appointment only.</p>
      </div>
      <div>
        <p class="footer-heading">Men</p>
        <ul class="footer-links">
          <li><a href="custom-suits.html">Bespoke Suits</a></li>
          <li><a href="ready-to-wear-suits.html">Ready to Wear</a></li>
          <li><a href="handmade-shoes.html">Handmade Shoes</a></li>
          <li><a href="tuxedos.html">Tuxedos</a></li>
        </ul>
      </div>
      <div>
        <p class="footer-heading">Women</p>
        <ul class="footer-links">
          <li><a href="wedding-dresses.html">Wedding Dresses</a></li>
        </ul>
        <p class="footer-heading" style="margin-top:32px;">Explore</p>
        <ul class="footer-links">
          <li><a href="gallery.html">Gallery</a></li>
          <li><a href="about-us.html">About Us</a></li>
        </ul>
      </div>
      <div>
        <p class="footer-heading">Consultation</p>
        <div class="footer-contact">
          <p><a href="tel:6465162664">(646) 516-2664</a></p>
          <p><a href="mailto:Gregoryduaneservice@gregoryduane.com">Gregoryduaneservice@gregoryduane.com</a></p>
          <p style="margin-top:12px;">Open by appointment · All days</p>
        </div>
        <a href="mailto:Gregoryduaneservice@gregoryduane.com" class="btn-primary">Book a Consultation</a>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 Gregory Duane. All rights reserved.</p>
    </div>
  </footer>

  <script src="nav.js"></script>
</body>
</html>
```

- [ ] **Step 2: Open in browser and verify Template A**

Check:
- Page hero is 60vh with image + overlaid title ✓
- Gold "Men" label appears above hero title ✓
- Intro section shows 2-column: copy left, image right ✓
- Steps section has slightly lighter surface background ✓
- Steps are numbered in gold ✓
- 2×2 image grid renders with no gaps except 4px ✓
- CTA band renders on `--surface` background ✓

- [ ] **Step 3: Commit**

```bash
git add custom-suits.html
git commit -m "feat: build bespoke suits page"
```

---

## Task 6: Build ready-to-wear-suits.html — Ready to Wear (Template B)

**Files:**
- Rewrite: `ready-to-wear-suits.html`

- [ ] **Step 1: Replace ready-to-wear-suits.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ready to Wear Suits — Gregory Duane</title>
  <meta name="description" content="Gregory Duane ready-to-wear suits. Premium fabrics, sharp silhouettes — available now. New York.">
  <link rel="icon" href="images/gregory-duane-favicon.png">
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <div class="announce-bar">
    Bespoke. By Appointment Only.&nbsp;&nbsp;·&nbsp;&nbsp;<a href="tel:6465162664">(646) 516-2664</a>
  </div>

  <nav class="site-nav" aria-label="Main navigation">
    <div class="nav-inner">
      <div class="nav-left">
        <div class="has-dropdown">
          <a href="#">Men</a>
          <ul class="dropdown-menu">
            <li><a href="custom-suits.html">Bespoke Suits</a></li>
            <li><a href="ready-to-wear-suits.html">Ready to Wear</a></li>
            <li><a href="handmade-shoes.html">Handmade Shoes</a></li>
            <li><a href="tuxedos.html">Tuxedos</a></li>
          </ul>
        </div>
        <div class="has-dropdown">
          <a href="#">Women</a>
          <ul class="dropdown-menu">
            <li><a href="wedding-dresses.html">Wedding Dresses</a></li>
          </ul>
        </div>
      </div>
      <a class="nav-logo" href="index.html" aria-label="Gregory Duane home">
        <img src="images/Gregory-Duane_white_high-res.png" alt="Gregory Duane" />
      </a>
      <div class="nav-right">
        <a href="gallery.html">Gallery</a>
        <a href="about-us.html">About</a>
        <a href="mailto:Gregoryduaneservice@gregoryduane.com" class="nav-cta">Book a Consultation</a>
        <button class="menu-toggle" aria-label="Toggle menu" aria-expanded="false">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
    <div class="mobile-menu" aria-hidden="true">
      <div class="has-dropdown">
        <a href="#">Men</a>
        <ul class="dropdown-menu">
          <li><a href="custom-suits.html">Bespoke Suits</a></li>
          <li><a href="ready-to-wear-suits.html">Ready to Wear</a></li>
          <li><a href="handmade-shoes.html">Handmade Shoes</a></li>
          <li><a href="tuxedos.html">Tuxedos</a></li>
        </ul>
      </div>
      <div class="has-dropdown">
        <a href="#">Women</a>
        <ul class="dropdown-menu">
          <li><a href="wedding-dresses.html">Wedding Dresses</a></li>
        </ul>
      </div>
      <a href="gallery.html">Gallery</a>
      <a href="about-us.html">About</a>
      <a href="mailto:Gregoryduaneservice@gregoryduane.com" class="btn-ghost">Book a Consultation</a>
    </div>
  </nav>

  <!-- Page Hero -->
  <div class="page-hero">
    <img src="images/max-andrey-TlRQin0iwjE-unsplash.jpg" alt="Ready to wear suits" />
    <div class="page-hero-overlay">
      <span class="page-hero-label">Men</span>
      <h1 class="page-hero-title">Ready to Wear</h1>
    </div>
  </div>

  <!-- Intro -->
  <section class="section" style="text-align:center;">
    <div class="container">
      <div style="max-width:680px;margin:0 auto;">
        <span class="label-caps" style="color:var(--gold);display:block;margin-bottom:20px;">The Collection</span>
        <h2 class="headline-lg" style="margin-bottom:24px;">Gregory Duane quality.<br>No waiting required.</h2>
        <p style="color:var(--muted);font-size:16px;line-height:1.75;">Our ready-to-wear collection is cut from the same fabric library as our bespoke line — engineered silhouettes, premium materials, and the unmistakable Gregory Duane standard. For the man who demands precision and values time.</p>
      </div>
    </div>
  </section>

  <!-- Product Grid -->
  <section style="padding:0 var(--page-margin) var(--section-gap);">
    <div style="max-width:var(--max-width);margin:0 auto;">
      <div class="product-grid">
        <div class="product-card">
          <img src="images/rtw-suit-images/1A.png" alt="Gregory Duane RTW Suit" />
          <div class="product-info"><p class="product-name">The Classic Single-Breasted</p></div>
        </div>
        <div class="product-card">
          <img src="images/rtw-suit-images/1B.png" alt="Gregory Duane RTW Suit" />
          <div class="product-info"><p class="product-name">The Peak Lapel</p></div>
        </div>
        <div class="product-card">
          <img src="images/rtw-suit-images/1C.png" alt="Gregory Duane RTW Suit" />
          <div class="product-info"><p class="product-name">The Slim Charcoal</p></div>
        </div>
        <div class="product-card">
          <img src="images/rtw-suit-images/1D.png" alt="Gregory Duane RTW Suit" />
          <div class="product-info"><p class="product-name">The Double-Breasted</p></div>
        </div>
        <div class="product-card">
          <img src="images/rtw-suit-images/1E.png" alt="Gregory Duane RTW Suit" />
          <div class="product-info"><p class="product-name">The Navy Foundation</p></div>
        </div>
        <div class="product-card">
          <img src="images/rtw-suit-images/1F.png" alt="Gregory Duane RTW Suit" />
          <div class="product-info"><p class="product-name">The Grey Herringbone</p></div>
        </div>
        <div class="product-card">
          <img src="images/rtw-suit-images/1G.png" alt="Gregory Duane RTW Suit" />
          <div class="product-info"><p class="product-name">The Black Formal</p></div>
        </div>
        <div class="product-card">
          <img src="images/rtw-suit-images/1H.png" alt="Gregory Duane RTW Suit" />
          <div class="product-info"><p class="product-name">The Windowpane Check</p></div>
        </div>
        <div class="product-card">
          <img src="images/rtw-suit-images/1I.png" alt="Gregory Duane RTW Suit" />
          <div class="product-info"><p class="product-name">The British Wool</p></div>
        </div>
      </div>
    </div>
  </section>

  <!-- CTA Band -->
  <section class="cta-band">
    <h2 class="headline-md">Want It Made for You?</h2>
    <p>Upgrade any silhouette to a fully bespoke commission. The process starts with one conversation.</p>
    <a href="custom-suits.html" class="btn-ghost" style="margin-right:16px;">Explore Bespoke</a>
    <a href="mailto:Gregoryduaneservice@gregoryduane.com" class="btn-primary">Book a Consultation</a>
  </section>

  <!-- Footer -->
  <footer>
    <div class="footer-grid">
      <div class="footer-logo">
        <img src="images/Gregory-Duane_white_high-res.png" alt="Gregory Duane" />
        <p class="footer-tagline">Bespoke tailoring, handmade footwear, and bridal atelier. New York. By appointment only.</p>
      </div>
      <div>
        <p class="footer-heading">Men</p>
        <ul class="footer-links">
          <li><a href="custom-suits.html">Bespoke Suits</a></li>
          <li><a href="ready-to-wear-suits.html">Ready to Wear</a></li>
          <li><a href="handmade-shoes.html">Handmade Shoes</a></li>
          <li><a href="tuxedos.html">Tuxedos</a></li>
        </ul>
      </div>
      <div>
        <p class="footer-heading">Women</p>
        <ul class="footer-links">
          <li><a href="wedding-dresses.html">Wedding Dresses</a></li>
        </ul>
        <p class="footer-heading" style="margin-top:32px;">Explore</p>
        <ul class="footer-links">
          <li><a href="gallery.html">Gallery</a></li>
          <li><a href="about-us.html">About Us</a></li>
        </ul>
      </div>
      <div>
        <p class="footer-heading">Consultation</p>
        <div class="footer-contact">
          <p><a href="tel:6465162664">(646) 516-2664</a></p>
          <p><a href="mailto:Gregoryduaneservice@gregoryduane.com">Gregoryduaneservice@gregoryduane.com</a></p>
          <p style="margin-top:12px;">Open by appointment · All days</p>
        </div>
        <a href="mailto:Gregoryduaneservice@gregoryduane.com" class="btn-primary">Book a Consultation</a>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 Gregory Duane. All rights reserved.</p>
    </div>
  </footer>

  <script src="nav.js"></script>
</body>
</html>
```

- [ ] **Step 2: Open in browser and verify Template B**

Check:
- Product grid is 3-column with RTW suit images ✓
- Product names render in label-caps below each image ✓
- Hover on product card: image scales slightly, name turns gold ✓
- CTA band shows two side-by-side buttons ✓

- [ ] **Step 3: Commit**

```bash
git add ready-to-wear-suits.html
git commit -m "feat: build ready-to-wear suits page"
```

---

## Task 7: Build handmade-shoes.html — Handmade Shoes (Template A)

**Files:**
- Create: `handmade-shoes.html`

- [ ] **Step 1: Create handmade-shoes.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Handmade Shoes — Gregory Duane</title>
  <meta name="description" content="Handmade custom shoes crafted on a bespoke last. Gregory Duane, New York. By appointment only.">
  <link rel="icon" href="images/gregory-duane-favicon.png">
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <div class="announce-bar">
    Bespoke. By Appointment Only.&nbsp;&nbsp;·&nbsp;&nbsp;<a href="tel:6465162664">(646) 516-2664</a>
  </div>

  <nav class="site-nav" aria-label="Main navigation">
    <div class="nav-inner">
      <div class="nav-left">
        <div class="has-dropdown">
          <a href="#">Men</a>
          <ul class="dropdown-menu">
            <li><a href="custom-suits.html">Bespoke Suits</a></li>
            <li><a href="ready-to-wear-suits.html">Ready to Wear</a></li>
            <li><a href="handmade-shoes.html">Handmade Shoes</a></li>
            <li><a href="tuxedos.html">Tuxedos</a></li>
          </ul>
        </div>
        <div class="has-dropdown">
          <a href="#">Women</a>
          <ul class="dropdown-menu">
            <li><a href="wedding-dresses.html">Wedding Dresses</a></li>
          </ul>
        </div>
      </div>
      <a class="nav-logo" href="index.html" aria-label="Gregory Duane home">
        <img src="images/Gregory-Duane_white_high-res.png" alt="Gregory Duane" />
      </a>
      <div class="nav-right">
        <a href="gallery.html">Gallery</a>
        <a href="about-us.html">About</a>
        <a href="mailto:Gregoryduaneservice@gregoryduane.com" class="nav-cta">Book a Consultation</a>
        <button class="menu-toggle" aria-label="Toggle menu" aria-expanded="false">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
    <div class="mobile-menu" aria-hidden="true">
      <div class="has-dropdown">
        <a href="#">Men</a>
        <ul class="dropdown-menu">
          <li><a href="custom-suits.html">Bespoke Suits</a></li>
          <li><a href="ready-to-wear-suits.html">Ready to Wear</a></li>
          <li><a href="handmade-shoes.html">Handmade Shoes</a></li>
          <li><a href="tuxedos.html">Tuxedos</a></li>
        </ul>
      </div>
      <div class="has-dropdown">
        <a href="#">Women</a>
        <ul class="dropdown-menu">
          <li><a href="wedding-dresses.html">Wedding Dresses</a></li>
        </ul>
      </div>
      <a href="gallery.html">Gallery</a>
      <a href="about-us.html">About</a>
      <a href="mailto:Gregoryduaneservice@gregoryduane.com" class="btn-ghost">Book a Consultation</a>
    </div>
  </nav>

  <div class="page-hero">
    <img src="images/bruce-mars-S8ffHr_dxHo-unsplash.jpg" alt="Handmade shoes craftsmanship" />
    <div class="page-hero-overlay">
      <span class="page-hero-label">Men</span>
      <h1 class="page-hero-title">Handmade Shoes</h1>
    </div>
  </div>

  <div class="intro-section">
    <div class="intro-content">
      <span class="label-caps">Cordwaining, Revived</span>
      <h2 class="headline-lg">Forty hours.<br>One pair. Yours.</h2>
      <p>Each pair begins as a last — a bespoke wooden mold of your foot. What follows is 40 hours of hand-stitching, lasting, and finishing by artisans trained in centuries-old techniques. The result is a shoe that fits with impossible precision and improves with every wear.</p>
    </div>
    <img src="images/andrew-neel-cckf4TsHAuw-unsplash.jpg" alt="Shoe craftsmanship detail" class="intro-img" />
  </div>

  <section class="steps-section">
    <h2 class="steps-section-title">The Handmade Process</h2>
    <p class="steps-section-sub">Your last is made once and kept forever — each future pair begins exactly where the last one left off.</p>
    <div class="steps-grid">
      <div>
        <p class="step-number">01 — The Measurement</p>
        <h3 class="step-title">A Last Made for You.</h3>
        <p class="step-desc">A full foot analysis: length, width, arch height, and gait pattern. Your wooden last is carved to your exact dimensions and retained on file for all future commissions.</p>
      </div>
      <div>
        <p class="step-number">02 — The Construction</p>
        <h3 class="step-title">Stitched by Hand.</h3>
        <p class="step-desc">Upper panels are hand-cut and stitched to the insole using the Goodyear welt method. The sole is hand-nailed. No adhesives, no shortcuts — only the method that lasts generations.</p>
      </div>
      <div>
        <p class="step-number">03 — The Finish</p>
        <h3 class="step-title">Burnished. Delivered.</h3>
        <p class="step-desc">Edge dressing, hand-burnishing, and a final hand-polish complete the shoe. Delivered in a cedar shoe tree inside a Gregory Duane dust bag.</p>
      </div>
    </div>
  </section>

  <section style="padding:var(--section-gap) var(--page-margin);">
    <div style="max-width:var(--max-width);margin:0 auto;">
      <div class="image-grid cols-2">
        <img src="images/pexels-ketut-subiyanto-4963433.jpg" alt="Shoe detail" />
        <img src="images/pexels-александар-цветановић-1422292.jpg" alt="Shoe crafting" />
        <img src="images/max-andrey-4YWwPsTQfMs-unsplash.jpg" alt="Finished shoe" />
        <img src="images/pexels-the-lazy-artist-gallery-1303866.jpg" alt="Shoe leather" />
      </div>
    </div>
  </section>

  <section class="cta-band">
    <h2 class="headline-md">Commission Your First Pair</h2>
    <p>Your last is made once and stays with us. Begin your footwear legacy today.</p>
    <a href="mailto:Gregoryduaneservice@gregoryduane.com" class="btn-primary">Book a Consultation</a>
  </section>

  <footer>
    <div class="footer-grid">
      <div class="footer-logo">
        <img src="images/Gregory-Duane_white_high-res.png" alt="Gregory Duane" />
        <p class="footer-tagline">Bespoke tailoring, handmade footwear, and bridal atelier. New York. By appointment only.</p>
      </div>
      <div>
        <p class="footer-heading">Men</p>
        <ul class="footer-links">
          <li><a href="custom-suits.html">Bespoke Suits</a></li>
          <li><a href="ready-to-wear-suits.html">Ready to Wear</a></li>
          <li><a href="handmade-shoes.html">Handmade Shoes</a></li>
          <li><a href="tuxedos.html">Tuxedos</a></li>
        </ul>
      </div>
      <div>
        <p class="footer-heading">Women</p>
        <ul class="footer-links">
          <li><a href="wedding-dresses.html">Wedding Dresses</a></li>
        </ul>
        <p class="footer-heading" style="margin-top:32px;">Explore</p>
        <ul class="footer-links">
          <li><a href="gallery.html">Gallery</a></li>
          <li><a href="about-us.html">About Us</a></li>
        </ul>
      </div>
      <div>
        <p class="footer-heading">Consultation</p>
        <div class="footer-contact">
          <p><a href="tel:6465162664">(646) 516-2664</a></p>
          <p><a href="mailto:Gregoryduaneservice@gregoryduane.com">Gregoryduaneservice@gregoryduane.com</a></p>
          <p style="margin-top:12px;">Open by appointment · All days</p>
        </div>
        <a href="mailto:Gregoryduaneservice@gregoryduane.com" class="btn-primary">Book a Consultation</a>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 Gregory Duane. All rights reserved.</p>
    </div>
  </footer>

  <script src="nav.js"></script>
</body>
</html>
```

- [ ] **Step 2: Verify in browser** — Template A structure renders correctly (hero, intro, steps, grid, CTA band).

- [ ] **Step 3: Commit**

```bash
git add handmade-shoes.html
git commit -m "feat: build handmade shoes page"
```

---

## Task 8: Build tuxedos.html — Tuxedos / Men's Bridal (Template A)

**Files:**
- Create: `tuxedos.html`

- [ ] **Step 1: Create tuxedos.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bespoke Tuxedos — Gregory Duane</title>
  <meta name="description" content="Bespoke wedding tuxedos and formal evening wear. Gregory Duane bridal, New York. By appointment only.">
  <link rel="icon" href="images/gregory-duane-favicon.png">
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <div class="announce-bar">
    Bespoke. By Appointment Only.&nbsp;&nbsp;·&nbsp;&nbsp;<a href="tel:6465162664">(646) 516-2664</a>
  </div>

  <nav class="site-nav" aria-label="Main navigation">
    <div class="nav-inner">
      <div class="nav-left">
        <div class="has-dropdown">
          <a href="#">Men</a>
          <ul class="dropdown-menu">
            <li><a href="custom-suits.html">Bespoke Suits</a></li>
            <li><a href="ready-to-wear-suits.html">Ready to Wear</a></li>
            <li><a href="handmade-shoes.html">Handmade Shoes</a></li>
            <li><a href="tuxedos.html">Tuxedos</a></li>
          </ul>
        </div>
        <div class="has-dropdown">
          <a href="#">Women</a>
          <ul class="dropdown-menu">
            <li><a href="wedding-dresses.html">Wedding Dresses</a></li>
          </ul>
        </div>
      </div>
      <a class="nav-logo" href="index.html" aria-label="Gregory Duane home">
        <img src="images/Gregory-Duane_white_high-res.png" alt="Gregory Duane" />
      </a>
      <div class="nav-right">
        <a href="gallery.html">Gallery</a>
        <a href="about-us.html">About</a>
        <a href="mailto:Gregoryduaneservice@gregoryduane.com" class="nav-cta">Book a Consultation</a>
        <button class="menu-toggle" aria-label="Toggle menu" aria-expanded="false">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
    <div class="mobile-menu" aria-hidden="true">
      <div class="has-dropdown">
        <a href="#">Men</a>
        <ul class="dropdown-menu">
          <li><a href="custom-suits.html">Bespoke Suits</a></li>
          <li><a href="ready-to-wear-suits.html">Ready to Wear</a></li>
          <li><a href="handmade-shoes.html">Handmade Shoes</a></li>
          <li><a href="tuxedos.html">Tuxedos</a></li>
        </ul>
      </div>
      <div class="has-dropdown">
        <a href="#">Women</a>
        <ul class="dropdown-menu">
          <li><a href="wedding-dresses.html">Wedding Dresses</a></li>
        </ul>
      </div>
      <a href="gallery.html">Gallery</a>
      <a href="about-us.html">About</a>
      <a href="mailto:Gregoryduaneservice@gregoryduane.com" class="btn-ghost">Book a Consultation</a>
    </div>
  </nav>

  <div class="page-hero">
    <img src="images/pexels-александар-цветановић-1422292.jpg" alt="Bespoke tuxedo editorial" />
    <div class="page-hero-overlay">
      <span class="page-hero-label">Bridal — Men</span>
      <h1 class="page-hero-title">Bespoke Tuxedos</h1>
    </div>
  </div>

  <div class="intro-section">
    <div class="intro-content">
      <span class="label-caps">The Bridal Atelier</span>
      <h2 class="headline-lg">Dressed for the<br>weight of memory.</h2>
      <p>A wedding tuxedo carries more than cloth. We approach each commission with the gravity it deserves — from the peak lapel to the final silk buttonhole, every decision is made with precision, intention, and the knowledge that this garment will be photographed more than any other you will ever own.</p>
    </div>
    <img src="images/pexels-terje-sollie-298863.jpg" alt="Tuxedo detail" class="intro-img" />
  </div>

  <section class="steps-section">
    <h2 class="steps-section-title">The Tuxedo Process</h2>
    <p class="steps-section-sub">We begin months before the date. We finish when it's perfect.</p>
    <div class="steps-grid">
      <div>
        <p class="step-number">01 — The Consultation</p>
        <h3 class="step-title">Vision First.</h3>
        <p class="step-desc">We discuss the ceremony, the venue, the season, and your vision. We photograph the setting when possible. Every decision — from lapel to lining — flows from this foundation.</p>
      </div>
      <div>
        <p class="step-number">02 — The Design</p>
        <h3 class="step-title">Every Detail Decided.</h3>
        <p class="step-desc">Peak or shawl lapel? Grosgrain or satin facing? One button or two? We guide you through every decision with editorial precision and no pressure toward the obvious choice.</p>
      </div>
      <div>
        <p class="step-number">03 — The Fitting</p>
        <h3 class="step-title">Move Freely. Stand Tall.</h3>
        <p class="step-desc">Multiple fittings ensure the tuxedo moves with you on one of the most photographed days of your life. We do not stop until it is exactly right.</p>
      </div>
    </div>
  </section>

  <section style="padding:var(--section-gap) var(--page-margin);">
    <div style="max-width:var(--max-width);margin:0 auto;">
      <div class="image-grid cols-3">
        <img src="images/pexels-the-lazy-artist-gallery-1300550.jpg" alt="Tuxedo editorial" />
        <img src="images/pexels-anders-kristensen-447570.jpg" alt="Formal wear detail" />
        <img src="images/pexels-photo-4173182.png.png" alt="Tuxedo fitting" />
      </div>
    </div>
  </section>

  <section class="cta-band">
    <h2 class="headline-md">Reserve Your Wedding Commission</h2>
    <p>Tuxedo commissions require a minimum of 12 weeks. Begin early — begin right.</p>
    <a href="mailto:Gregoryduaneservice@gregoryduane.com" class="btn-primary">Book a Consultation</a>
  </section>

  <footer>
    <div class="footer-grid">
      <div class="footer-logo">
        <img src="images/Gregory-Duane_white_high-res.png" alt="Gregory Duane" />
        <p class="footer-tagline">Bespoke tailoring, handmade footwear, and bridal atelier. New York. By appointment only.</p>
      </div>
      <div>
        <p class="footer-heading">Men</p>
        <ul class="footer-links">
          <li><a href="custom-suits.html">Bespoke Suits</a></li>
          <li><a href="ready-to-wear-suits.html">Ready to Wear</a></li>
          <li><a href="handmade-shoes.html">Handmade Shoes</a></li>
          <li><a href="tuxedos.html">Tuxedos</a></li>
        </ul>
      </div>
      <div>
        <p class="footer-heading">Women</p>
        <ul class="footer-links">
          <li><a href="wedding-dresses.html">Wedding Dresses</a></li>
        </ul>
        <p class="footer-heading" style="margin-top:32px;">Explore</p>
        <ul class="footer-links">
          <li><a href="gallery.html">Gallery</a></li>
          <li><a href="about-us.html">About Us</a></li>
        </ul>
      </div>
      <div>
        <p class="footer-heading">Consultation</p>
        <div class="footer-contact">
          <p><a href="tel:6465162664">(646) 516-2664</a></p>
          <p><a href="mailto:Gregoryduaneservice@gregoryduane.com">Gregoryduaneservice@gregoryduane.com</a></p>
          <p style="margin-top:12px;">Open by appointment · All days</p>
        </div>
        <a href="mailto:Gregoryduaneservice@gregoryduane.com" class="btn-primary">Book a Consultation</a>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 Gregory Duane. All rights reserved.</p>
    </div>
  </footer>

  <script src="nav.js"></script>
</body>
</html>
```

- [ ] **Step 2: Verify in browser** — Template A renders correctly. "Bridal — Men" label in gold appears above page title in hero.

- [ ] **Step 3: Commit**

```bash
git add tuxedos.html
git commit -m "feat: build tuxedos page"
```

---

## Task 9: Build wedding-dresses.html — Women's Bridal (Template A)

**Files:**
- Create: `wedding-dresses.html`

- [ ] **Step 1: Create wedding-dresses.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bespoke Wedding Dresses — Gregory Duane</title>
  <meta name="description" content="Bespoke wedding dresses crafted one client at a time. Gregory Duane bridal atelier, New York.">
  <link rel="icon" href="images/gregory-duane-favicon.png">
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <div class="announce-bar">
    Bespoke. By Appointment Only.&nbsp;&nbsp;·&nbsp;&nbsp;<a href="tel:6465162664">(646) 516-2664</a>
  </div>

  <nav class="site-nav" aria-label="Main navigation">
    <div class="nav-inner">
      <div class="nav-left">
        <div class="has-dropdown">
          <a href="#">Men</a>
          <ul class="dropdown-menu">
            <li><a href="custom-suits.html">Bespoke Suits</a></li>
            <li><a href="ready-to-wear-suits.html">Ready to Wear</a></li>
            <li><a href="handmade-shoes.html">Handmade Shoes</a></li>
            <li><a href="tuxedos.html">Tuxedos</a></li>
          </ul>
        </div>
        <div class="has-dropdown">
          <a href="#">Women</a>
          <ul class="dropdown-menu">
            <li><a href="wedding-dresses.html">Wedding Dresses</a></li>
          </ul>
        </div>
      </div>
      <a class="nav-logo" href="index.html" aria-label="Gregory Duane home">
        <img src="images/Gregory-Duane_white_high-res.png" alt="Gregory Duane" />
      </a>
      <div class="nav-right">
        <a href="gallery.html">Gallery</a>
        <a href="about-us.html">About</a>
        <a href="mailto:Gregoryduaneservice@gregoryduane.com" class="nav-cta">Book a Consultation</a>
        <button class="menu-toggle" aria-label="Toggle menu" aria-expanded="false">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
    <div class="mobile-menu" aria-hidden="true">
      <div class="has-dropdown">
        <a href="#">Men</a>
        <ul class="dropdown-menu">
          <li><a href="custom-suits.html">Bespoke Suits</a></li>
          <li><a href="ready-to-wear-suits.html">Ready to Wear</a></li>
          <li><a href="handmade-shoes.html">Handmade Shoes</a></li>
          <li><a href="tuxedos.html">Tuxedos</a></li>
        </ul>
      </div>
      <div class="has-dropdown">
        <a href="#">Women</a>
        <ul class="dropdown-menu">
          <li><a href="wedding-dresses.html">Wedding Dresses</a></li>
        </ul>
      </div>
      <a href="gallery.html">Gallery</a>
      <a href="about-us.html">About</a>
      <a href="mailto:Gregoryduaneservice@gregoryduane.com" class="btn-ghost">Book a Consultation</a>
    </div>
  </nav>

  <div class="page-hero">
    <img src="images/yasamine-june-iV08-pfH2NQ-unsplash.jpg" alt="Bespoke wedding dress editorial" />
    <div class="page-hero-overlay">
      <span class="page-hero-label">Bridal — Women</span>
      <h1 class="page-hero-title">Wedding Dresses</h1>
    </div>
  </div>

  <div class="intro-section">
    <div class="intro-content">
      <span class="label-caps">The Bridal Atelier</span>
      <h2 class="headline-lg">One client.<br>One dress. Entirely yours.</h2>
      <p>We believe a wedding dress should be as individual as the woman wearing it. Our atelier works with one bridal client at a time, bringing couture construction and genuine design dialogue to the most personal garment of your life. We do not use templates — we begin with you.</p>
    </div>
    <img src="images/yasamine-june-SLipZqBFLHU-unsplash.jpg" alt="Bridal dress detail" class="intro-img" />
  </div>

  <section class="steps-section">
    <h2 class="steps-section-title">The Bridal Process</h2>
    <p class="steps-section-sub">Delivered weeks before your date. Never the week before.</p>
    <div class="steps-grid">
      <div>
        <p class="step-number">01 — The Vision</p>
        <h3 class="step-title">Your Story, First.</h3>
        <p class="step-desc">We begin with your inspiration, your venue, your silhouette goals, and the feeling you want when you walk in. No two consultations begin the same way.</p>
      </div>
      <div>
        <p class="step-number">02 — The Drape</p>
        <h3 class="step-title">Built on Your Body.</h3>
        <p class="step-desc">We work in muslin first, draping directly on your body to establish the foundation before a single cut is made in final fabric. The structure is right before the beauty begins.</p>
      </div>
      <div>
        <p class="step-number">03 — The Creation</p>
        <h3 class="step-title">Hand-Made. Hand-Delivered.</h3>
        <p class="step-desc">Constructed entirely by hand, fitted through multiple sessions, and delivered weeks before your date with full care instructions and emergency alteration availability.</p>
      </div>
    </div>
  </section>

  <section style="padding:var(--section-gap) var(--page-margin);">
    <div style="max-width:var(--max-width);margin:0 auto;">
      <div class="image-grid cols-3">
        <img src="images/pexels-ketut-subiyanto-4963433.jpg" alt="Bridal editorial" />
        <img src="images/andrew-neel-cckf4TsHAuw-unsplash.jpg" alt="Bridal detail" />
        <img src="images/pexels-the-lazy-artist-gallery-1303866.jpg" alt="Bridal fabric" />
      </div>
    </div>
  </section>

  <section class="cta-band">
    <h2 class="headline-md">Begin Your Bridal Commission</h2>
    <p>Bridal commissions require a minimum of 16 weeks. The sooner we begin, the better your dress becomes.</p>
    <a href="mailto:Gregoryduaneservice@gregoryduane.com" class="btn-primary">Book a Consultation</a>
  </section>

  <footer>
    <div class="footer-grid">
      <div class="footer-logo">
        <img src="images/Gregory-Duane_white_high-res.png" alt="Gregory Duane" />
        <p class="footer-tagline">Bespoke tailoring, handmade footwear, and bridal atelier. New York. By appointment only.</p>
      </div>
      <div>
        <p class="footer-heading">Men</p>
        <ul class="footer-links">
          <li><a href="custom-suits.html">Bespoke Suits</a></li>
          <li><a href="ready-to-wear-suits.html">Ready to Wear</a></li>
          <li><a href="handmade-shoes.html">Handmade Shoes</a></li>
          <li><a href="tuxedos.html">Tuxedos</a></li>
        </ul>
      </div>
      <div>
        <p class="footer-heading">Women</p>
        <ul class="footer-links">
          <li><a href="wedding-dresses.html">Wedding Dresses</a></li>
        </ul>
        <p class="footer-heading" style="margin-top:32px;">Explore</p>
        <ul class="footer-links">
          <li><a href="gallery.html">Gallery</a></li>
          <li><a href="about-us.html">About Us</a></li>
        </ul>
      </div>
      <div>
        <p class="footer-heading">Consultation</p>
        <div class="footer-contact">
          <p><a href="tel:6465162664">(646) 516-2664</a></p>
          <p><a href="mailto:Gregoryduaneservice@gregoryduane.com">Gregoryduaneservice@gregoryduane.com</a></p>
          <p style="margin-top:12px;">Open by appointment · All days</p>
        </div>
        <a href="mailto:Gregoryduaneservice@gregoryduane.com" class="btn-primary">Book a Consultation</a>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 Gregory Duane. All rights reserved.</p>
    </div>
  </footer>

  <script src="nav.js"></script>
</body>
</html>
```

- [ ] **Step 2: Verify in browser** — "Bridal — Women" label in gold in hero. Template A renders correctly.

- [ ] **Step 3: Commit**

```bash
git add wedding-dresses.html
git commit -m "feat: build wedding dresses page"
```

---

## Task 10: Build gallery.html — Gallery (Template C)

**Files:**
- Create: `gallery.html`

- [ ] **Step 1: Create gallery.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Gallery — Gregory Duane</title>
  <meta name="description" content="The Gregory Duane gallery — bespoke suits, handmade shoes, and bridal commissions.">
  <link rel="icon" href="images/gregory-duane-favicon.png">
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <div class="announce-bar">
    Bespoke. By Appointment Only.&nbsp;&nbsp;·&nbsp;&nbsp;<a href="tel:6465162664">(646) 516-2664</a>
  </div>

  <nav class="site-nav" aria-label="Main navigation">
    <div class="nav-inner">
      <div class="nav-left">
        <div class="has-dropdown">
          <a href="#">Men</a>
          <ul class="dropdown-menu">
            <li><a href="custom-suits.html">Bespoke Suits</a></li>
            <li><a href="ready-to-wear-suits.html">Ready to Wear</a></li>
            <li><a href="handmade-shoes.html">Handmade Shoes</a></li>
            <li><a href="tuxedos.html">Tuxedos</a></li>
          </ul>
        </div>
        <div class="has-dropdown">
          <a href="#">Women</a>
          <ul class="dropdown-menu">
            <li><a href="wedding-dresses.html">Wedding Dresses</a></li>
          </ul>
        </div>
      </div>
      <a class="nav-logo" href="index.html" aria-label="Gregory Duane home">
        <img src="images/Gregory-Duane_white_high-res.png" alt="Gregory Duane" />
      </a>
      <div class="nav-right">
        <a href="gallery.html">Gallery</a>
        <a href="about-us.html">About</a>
        <a href="mailto:Gregoryduaneservice@gregoryduane.com" class="nav-cta">Book a Consultation</a>
        <button class="menu-toggle" aria-label="Toggle menu" aria-expanded="false">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
    <div class="mobile-menu" aria-hidden="true">
      <div class="has-dropdown">
        <a href="#">Men</a>
        <ul class="dropdown-menu">
          <li><a href="custom-suits.html">Bespoke Suits</a></li>
          <li><a href="ready-to-wear-suits.html">Ready to Wear</a></li>
          <li><a href="handmade-shoes.html">Handmade Shoes</a></li>
          <li><a href="tuxedos.html">Tuxedos</a></li>
        </ul>
      </div>
      <div class="has-dropdown">
        <a href="#">Women</a>
        <ul class="dropdown-menu">
          <li><a href="wedding-dresses.html">Wedding Dresses</a></li>
        </ul>
      </div>
      <a href="gallery.html">Gallery</a>
      <a href="about-us.html">About</a>
      <a href="mailto:Gregoryduaneservice@gregoryduane.com" class="btn-ghost">Book a Consultation</a>
    </div>
  </nav>

  <!-- Page Hero — minimal -->
  <div class="page-hero" style="height:40vh;">
    <img src="images/pexels-the-lazy-artist-gallery-1300550.jpg" alt="Gregory Duane gallery" />
    <div class="page-hero-overlay">
      <span class="page-hero-label">Gregory Duane</span>
      <h1 class="page-hero-title">Gallery</h1>
    </div>
  </div>

  <!-- Masonry Gallery -->
  <section style="padding:var(--section-gap) var(--page-margin);">
    <div style="max-width:var(--max-width);margin:0 auto;">
      <div class="masonry">
        <img src="images/pexels-the-lazy-artist-gallery-1300550.jpg" alt="Editorial" />
        <img src="images/pexels-terje-sollie-298863.jpg" alt="Suit" />
        <img src="images/pexels-anders-kristensen-447570.jpg" alt="Bespoke" />
        <img src="images/pexels-Antoni-shkraba-5264913.jpg" alt="Fashion" loading="lazy" />
        <img src="images/pexels-the-lazy-artist-gallery-1303866.jpg" alt="Craftsmanship" loading="lazy" />
        <img src="images/ruthson-zimmerman-Ws4wd-vJ9M0-unsplash.jpg" alt="Shoes" loading="lazy" />
        <img src="images/bruce-mars-S8ffHr_dxHo-unsplash.jpg" alt="Style" loading="lazy" />
        <img src="images/yasamine-june-iV08-pfH2NQ-unsplash.jpg" alt="Bridal" loading="lazy" />
        <img src="images/yasamine-june-SLipZqBFLHU-unsplash.jpg" alt="Bridal fashion" loading="lazy" />
        <img src="images/ivan-zhukevich-7ZC4qO3Gj6g-unsplash.jpg" alt="Formal" loading="lazy" />
        <img src="images/andrew-neel-cckf4TsHAuw-unsplash.jpg" alt="Detail" loading="lazy" />
        <img src="images/max-andrey-4YWwPsTQfMs-unsplash.jpg" alt="Collection" loading="lazy" />
        <img src="images/max-andrey-TlRQin0iwjE-unsplash.jpg" alt="Ready to wear" loading="lazy" />
        <img src="images/pexels-ketut-subiyanto-4963433.jpg" alt="Lifestyle" loading="lazy" />
        <img src="images/IMG_3985.jpeg" alt="Atelier" loading="lazy" />
      </div>
    </div>
  </section>

  <section class="cta-band">
    <h2 class="headline-md">Commission Your Own Statement</h2>
    <p>Every piece in this gallery began with a single conversation.</p>
    <a href="mailto:Gregoryduaneservice@gregoryduane.com" class="btn-primary">Book a Consultation</a>
  </section>

  <footer>
    <div class="footer-grid">
      <div class="footer-logo">
        <img src="images/Gregory-Duane_white_high-res.png" alt="Gregory Duane" />
        <p class="footer-tagline">Bespoke tailoring, handmade footwear, and bridal atelier. New York. By appointment only.</p>
      </div>
      <div>
        <p class="footer-heading">Men</p>
        <ul class="footer-links">
          <li><a href="custom-suits.html">Bespoke Suits</a></li>
          <li><a href="ready-to-wear-suits.html">Ready to Wear</a></li>
          <li><a href="handmade-shoes.html">Handmade Shoes</a></li>
          <li><a href="tuxedos.html">Tuxedos</a></li>
        </ul>
      </div>
      <div>
        <p class="footer-heading">Women</p>
        <ul class="footer-links">
          <li><a href="wedding-dresses.html">Wedding Dresses</a></li>
        </ul>
        <p class="footer-heading" style="margin-top:32px;">Explore</p>
        <ul class="footer-links">
          <li><a href="gallery.html">Gallery</a></li>
          <li><a href="about-us.html">About Us</a></li>
        </ul>
      </div>
      <div>
        <p class="footer-heading">Consultation</p>
        <div class="footer-contact">
          <p><a href="tel:6465162664">(646) 516-2664</a></p>
          <p><a href="mailto:Gregoryduaneservice@gregoryduane.com">Gregoryduaneservice@gregoryduane.com</a></p>
          <p style="margin-top:12px;">Open by appointment · All days</p>
        </div>
        <a href="mailto:Gregoryduaneservice@gregoryduane.com" class="btn-primary">Book a Consultation</a>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 Gregory Duane. All rights reserved.</p>
    </div>
  </footer>

  <script src="nav.js"></script>
</body>
</html>
```

- [ ] **Step 2: Verify in browser** — Masonry grid renders in 3 columns, images fill column width, no fixed heights forcing equal sizes.

- [ ] **Step 3: Commit**

```bash
git add gallery.html
git commit -m "feat: build gallery page"
```

---

## Task 11: Build about-us.html — About (Template D)

**Files:**
- Rewrite: `about-us.html`

- [ ] **Step 1: Replace about-us.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>About — Gregory Duane</title>
  <meta name="description" content="The story behind Gregory Duane — bespoke tailoring, handmade footwear, and bridal atelier founded by Duane Glover in New York.">
  <link rel="icon" href="images/gregory-duane-favicon.png">
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <div class="announce-bar">
    Bespoke. By Appointment Only.&nbsp;&nbsp;·&nbsp;&nbsp;<a href="tel:6465162664">(646) 516-2664</a>
  </div>

  <nav class="site-nav" aria-label="Main navigation">
    <div class="nav-inner">
      <div class="nav-left">
        <div class="has-dropdown">
          <a href="#">Men</a>
          <ul class="dropdown-menu">
            <li><a href="custom-suits.html">Bespoke Suits</a></li>
            <li><a href="ready-to-wear-suits.html">Ready to Wear</a></li>
            <li><a href="handmade-shoes.html">Handmade Shoes</a></li>
            <li><a href="tuxedos.html">Tuxedos</a></li>
          </ul>
        </div>
        <div class="has-dropdown">
          <a href="#">Women</a>
          <ul class="dropdown-menu">
            <li><a href="wedding-dresses.html">Wedding Dresses</a></li>
          </ul>
        </div>
      </div>
      <a class="nav-logo" href="index.html" aria-label="Gregory Duane home">
        <img src="images/Gregory-Duane_white_high-res.png" alt="Gregory Duane" />
      </a>
      <div class="nav-right">
        <a href="gallery.html">Gallery</a>
        <a href="about-us.html">About</a>
        <a href="mailto:Gregoryduaneservice@gregoryduane.com" class="nav-cta">Book a Consultation</a>
        <button class="menu-toggle" aria-label="Toggle menu" aria-expanded="false">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
    <div class="mobile-menu" aria-hidden="true">
      <div class="has-dropdown">
        <a href="#">Men</a>
        <ul class="dropdown-menu">
          <li><a href="custom-suits.html">Bespoke Suits</a></li>
          <li><a href="ready-to-wear-suits.html">Ready to Wear</a></li>
          <li><a href="handmade-shoes.html">Handmade Shoes</a></li>
          <li><a href="tuxedos.html">Tuxedos</a></li>
        </ul>
      </div>
      <div class="has-dropdown">
        <a href="#">Women</a>
        <ul class="dropdown-menu">
          <li><a href="wedding-dresses.html">Wedding Dresses</a></li>
        </ul>
      </div>
      <a href="gallery.html">Gallery</a>
      <a href="about-us.html">About</a>
      <a href="mailto:Gregoryduaneservice@gregoryduane.com" class="btn-ghost">Book a Consultation</a>
    </div>
  </nav>

  <div class="page-hero">
    <img src="images/IMG_4959.JPG" alt="Gregory Duane atelier" />
    <div class="page-hero-overlay">
      <span class="page-hero-label">The Brand</span>
      <h1 class="page-hero-title">About Gregory Duane</h1>
    </div>
  </div>

  <!-- Brand Story -->
  <div class="about-story">
    <p class="pull-quote">"Craftsmanship meets legacy, and every thread weaves a story of sophistication and style."</p>
    <div class="about-story-text">
      <span class="label-caps" style="color:var(--gold);display:block;margin-bottom:20px;">Duane Glover, Founder</span>
      <p>Gregory Duane is where craftsmanship meets legacy. Our journey begins with the heart and soul of our brand — Duane Glover, a man whose roots in sartorial tradition define the very essence of our luxury label.</p>
      <p>Raised with an understanding that how you dress communicates who you are before you speak, Duane built Gregory Duane on a single belief: that the most important garment you own is the one made precisely for you.</p>
      <p>Today, Gregory Duane serves clients across menswear, footwear, and bridal — all under one roof, all with the same exacting standard. Every commission is personal. Every stitch is intentional.</p>
    </div>
  </div>

  <!-- Values -->
  <section class="values-section">
    <div style="max-width:var(--max-width);margin:0 auto;">
      <h2 class="headline-md" style="text-align:center;margin-bottom:64px;">What We Stand For</h2>
      <div class="values-grid">
        <div>
          <span class="value-name">Craftsmanship</span>
          <p class="value-desc">We do not rush. Every garment is constructed by hand, inspected by eye, and approved only when it meets our exacting standard — however long that takes.</p>
        </div>
        <div>
          <span class="value-name">Bespoke</span>
          <p class="value-desc">Nothing leaves our atelier that has not been made specifically for the person who commissioned it. No templates. No shortcuts. No compromises.</p>
        </div>
        <div>
          <span class="value-name">Legacy</span>
          <p class="value-desc">We make garments that outlast trends — pieces that improve with wear, that carry stories, and that are built to be passed down to the next generation.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="cta-band">
    <h2 class="headline-md">Start Your Commission</h2>
    <p>Every relationship at Gregory Duane begins with a single conversation.</p>
    <a href="mailto:Gregoryduaneservice@gregoryduane.com" class="btn-primary">Book a Consultation</a>
  </section>

  <footer>
    <div class="footer-grid">
      <div class="footer-logo">
        <img src="images/Gregory-Duane_white_high-res.png" alt="Gregory Duane" />
        <p class="footer-tagline">Bespoke tailoring, handmade footwear, and bridal atelier. New York. By appointment only.</p>
      </div>
      <div>
        <p class="footer-heading">Men</p>
        <ul class="footer-links">
          <li><a href="custom-suits.html">Bespoke Suits</a></li>
          <li><a href="ready-to-wear-suits.html">Ready to Wear</a></li>
          <li><a href="handmade-shoes.html">Handmade Shoes</a></li>
          <li><a href="tuxedos.html">Tuxedos</a></li>
        </ul>
      </div>
      <div>
        <p class="footer-heading">Women</p>
        <ul class="footer-links">
          <li><a href="wedding-dresses.html">Wedding Dresses</a></li>
        </ul>
        <p class="footer-heading" style="margin-top:32px;">Explore</p>
        <ul class="footer-links">
          <li><a href="gallery.html">Gallery</a></li>
          <li><a href="about-us.html">About Us</a></li>
        </ul>
      </div>
      <div>
        <p class="footer-heading">Consultation</p>
        <div class="footer-contact">
          <p><a href="tel:6465162664">(646) 516-2664</a></p>
          <p><a href="mailto:Gregoryduaneservice@gregoryduane.com">Gregoryduaneservice@gregoryduane.com</a></p>
          <p style="margin-top:12px;">Open by appointment · All days</p>
        </div>
        <a href="mailto:Gregoryduaneservice@gregoryduane.com" class="btn-primary">Book a Consultation</a>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 Gregory Duane. All rights reserved.</p>
    </div>
  </footer>

  <script src="nav.js"></script>
</body>
</html>
```

- [ ] **Step 2: Verify in browser** — Two-column story layout renders (pull-quote left, narrative right). Values grid shows 3 columns on desktop, single column on mobile.

- [ ] **Step 3: Commit**

```bash
git add about-us.html
git commit -m "feat: build about page"
```

---

## Task 12: Responsive verification and cross-page polish

**Files:**
- No new files. Minor CSS fixes only if needed.

- [ ] **Step 1: Open index.html and resize browser from 1440px → 320px**

Check at each breakpoint:
- **1440px:** Nav three-column, hero full-bleed, all grids 3-column ✓
- **1024px:** Grids collapse to 2-column, footer to 2-column ✓
- **768px:** Hamburger appears, nav links hidden, mobile menu opens on click ✓
- **480px:** Product grid single column, masonry single column ✓

- [ ] **Step 2: Test mobile menu on index.html**

- Open mobile menu (hamburger) → overlay appears, all links visible ✓
- Tap "Men +" → accordion expands showing 4 sub-links ✓
- Tap "Men −" → accordion collapses ✓
- Tap any sub-link → navigates to correct page ✓
- Resize to desktop → mobile menu closes automatically ✓

- [ ] **Step 3: Test scroll transparency on each page**

Open each of the 8 pages, scroll down:
- Nav transitions from transparent to `#121414` after 72px scroll ✓
- No flash or jump during transition ✓

- [ ] **Step 4: Verify all internal links resolve**

Navigate through the site following every nav link and CTA. Confirm no 404s. The 8 files that should exist:
```
index.html
custom-suits.html
ready-to-wear-suits.html
handmade-shoes.html
tuxedos.html
wedding-dresses.html
gallery.html
about-us.html
```

- [ ] **Step 5: Final commit**

```bash
git add -A
git commit -m "feat: complete gregory duane site redesign — 8 pages"
```

---

## Self-Review Notes

- **Spec coverage:** All 8 pages built. All 4 templates implemented. Nav structure matches spec (Men/Women submenus, Gallery, About, CTA). RTW homepage feature present. Editorial pull-quote present. Shared CSS design system complete.
- **No placeholders:** All copy is final (not lorem ipsum). All image references use existing project assets.
- **Type consistency:** CSS class names used in HTML match definitions in style.css exactly (`btn-primary`, `btn-ghost`, `label-caps`, `headline-lg`, `headline-md`, `pull-quote`, `page-hero`, `cta-band`, `steps-grid`, `masonry`, `product-grid`).
- **image filename:** Task 10 gallery uses `pexels-Antoni-shkraba-5264913.jpg` — verify exact capitalization matches the file on disk (`pexels-Antoni-shkraba-5264913.jpg` vs `pexels-Antoni-shkraba-5264913.jpg`). Adjust case in gallery.html if needed.
