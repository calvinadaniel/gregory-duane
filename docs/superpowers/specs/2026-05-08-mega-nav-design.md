# Mega Panel Navigation — Design Spec
**Date:** 2026-05-08
**Project:** Gregory Duane
**Status:** Approved

---

## Overview

Replace the current CSS hover-only dropdown navigation with a click-triggered mega panel system. The existing `.has-dropdown:hover` pattern has a 12px dead zone (`top: calc(100% + 12px)`) that collapses the dropdown before users can click links. The new system uses full-width panels that open on click and close explicitly — eliminating all dead-zone issues.

---

## Files Affected

| File | Change |
|------|--------|
| `style.css` | Remove `.has-dropdown` / `.dropdown-menu` desktop rules; add mega panel CSS |
| `nav.js` | Replace hover dropdown logic with click-toggle mega panel logic |
| All 9 HTML pages | Replace `.nav-left` dropdown markup; add two `.mega-panel` blocks inside `.site-nav`; update mobile Women accordion items |

**9 HTML pages:** `index.html`, `custom-suits.html`, `ready-to-wear-suits.html`, `about-us.html`, `handmade-shoes.html`, `tuxedos.html`, `wedding-dresses.html`, `gallery.html`, `appointment-form.html`

---

## Nav HTML Structure (all 9 pages)

### nav-left replacement

**Remove** (current):
```html
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
```

**Add** (new):
```html
<div class="nav-left">
  <button class="nav-trigger" data-panel="mega-men" aria-expanded="false" aria-controls="mega-men">
    Men <span class="nav-chevron" aria-hidden="true">&#9662;</span>
  </button>
  <button class="nav-trigger" data-panel="mega-women" aria-expanded="false" aria-controls="mega-women">
    Women <span class="nav-chevron" aria-hidden="true">&#9662;</span>
  </button>
</div>
```

### Mega panels (added after `.nav-inner`, still inside `<nav class="site-nav">`)

```html
<!-- Men mega panel -->
<div class="mega-panel" id="mega-men" aria-hidden="true">
  <button class="mega-close" aria-label="Close men's menu">&#215;</button>
  <div class="mega-inner">
    <div class="mega-grid-men">
      <div class="mega-col">
        <div class="mega-col-label">Bespoke</div>
        <a class="mega-link" href="custom-suits.html">Bespoke Suits</a>
        <p class="mega-sub">Made to your exact measurements</p>
      </div>
      <div class="mega-col">
        <div class="mega-col-label">Ready to Wear</div>
        <a class="mega-link" href="ready-to-wear-suits.html">RTW Suits</a>
        <p class="mega-sub">Premium silhouettes, in stock</p>
      </div>
      <div class="mega-col">
        <div class="mega-col-label">Footwear</div>
        <a class="mega-link" href="handmade-shoes.html">Handmade Shoes</a>
        <p class="mega-sub">Handcrafted leather</p>
      </div>
      <div class="mega-col">
        <div class="mega-col-label">Formal</div>
        <a class="mega-link" href="tuxedos.html">Tuxedos</a>
        <p class="mega-sub">Black tie &amp; bridal</p>
      </div>
    </div>
  </div>
</div>

<!-- Women mega panel -->
<div class="mega-panel" id="mega-women" aria-hidden="true">
  <button class="mega-close" aria-label="Close women's menu">&#215;</button>
  <div class="mega-inner">
    <div class="mega-grid-women">
      <div class="mega-col">
        <div class="mega-col-label">Bridal</div>
        <a class="mega-link" href="wedding-dresses.html">Wedding Dresses</a>
        <a class="mega-link" href="#">Bridal Alterations</a>
        <a class="mega-link" href="#">Bridal Accessories</a>
        <a class="mega-link" href="#">Mother of the Bride</a>
      </div>
      <div class="mega-col">
        <div class="mega-col-label">Fashion</div>
        <a class="mega-link" href="#">Ready to Wear Suits</a>
      </div>
    </div>
  </div>
</div>
```

> **Note:** Bridal Alterations, Bridal Accessories, Mother of the Bride, and Women's Ready to Wear Suits do not have dedicated pages yet — their `href` is `#` until those pages are built.

### Mobile menu Women accordion update (all 9 pages)

**Remove** (current Women section in `.mobile-menu`):
```html
<div class="has-dropdown">
  <a href="#">Women</a>
  <ul class="dropdown-menu">
    <li><a href="wedding-dresses.html">Wedding Dresses</a></li>
  </ul>
</div>
```

**Replace with:**
```html
<div class="has-dropdown">
  <a href="#">Women</a>
  <ul class="dropdown-menu">
    <li><a href="wedding-dresses.html">Wedding Dresses</a></li>
    <li><a href="#">Bridal Alterations</a></li>
    <li><a href="#">Bridal Accessories</a></li>
    <li><a href="#">Mother of the Bride</a></li>
    <li><a href="#">Ready to Wear Suits</a></li>
  </ul>
</div>
```

---

## CSS Changes — `style.css`

### Remove (desktop dropdown rules — approximately lines 159–182)

```css
/* DELETE these rules: */
.has-dropdown { position: relative; }
.has-dropdown > a::after { content: ' \25be'; font-size: 8px; }
.dropdown-menu { ... }
.has-dropdown:hover .dropdown-menu { display: block; }
.dropdown-menu li a { ... }
.dropdown-menu li a:hover { ... }
```

> Keep all `.mobile-menu .has-dropdown` rules (lines ~242–260) — mobile accordions are unchanged.

### Add (new mega panel rules — append to section 8 or as new section)

```css
/* Nav trigger buttons */
.nav-trigger {
  background: none;
  border: none;
  color: var(--white);
  font-family: var(--font-sans);
  font-size: 11px;
  font-weight: 400;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 5px;
  opacity: 0.8;
  padding: 0;
  transition: opacity 0.2s, color 0.2s;
}
.nav-trigger:hover { opacity: 1; }
.nav-trigger.active { color: var(--gold); opacity: 1; }
.nav-chevron {
  font-size: 7px;
  display: inline-block;
  transition: transform 0.2s;
  color: var(--muted);
}
.nav-trigger.active .nav-chevron {
  transform: rotate(180deg);
  color: var(--gold);
}

/* Mega panel */
.mega-panel {
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  background: var(--surface);
  border-top: 2px solid var(--gold);
  border-bottom: 1px solid var(--outline);
  z-index: 99;
}
.mega-panel.open { display: block; }
.mega-inner {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 32px var(--page-margin) 28px;
}
.mega-grid-men {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 0;
}
.mega-grid-women {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0;
  max-width: 480px;
}
.mega-col {
  padding-right: 32px;
  border-right: 1px solid var(--outline);
  margin-right: 32px;
}
.mega-col:last-child {
  border-right: none;
  margin-right: 0;
  padding-right: 0;
}
.mega-col-label {
  font-family: var(--font-sans);
  font-size: 8px;
  font-weight: 600;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  color: var(--gold);
  margin-bottom: 14px;
}
.mega-link {
  display: block;
  font-family: var(--font-sans);
  font-size: 11px;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--white);
  opacity: 0.72;
  padding: 5px 0;
  transition: opacity 0.15s, color 0.15s;
}
.mega-link:hover { opacity: 1; color: var(--gold); }
.mega-sub {
  font-family: var(--font-serif);
  font-size: 11px;
  color: var(--muted);
  font-style: italic;
  margin-top: 4px;
  line-height: 1.5;
}
.mega-close {
  position: absolute;
  top: 14px;
  right: 24px;
  background: none;
  border: none;
  color: var(--muted);
  font-size: 20px;
  cursor: pointer;
  line-height: 1;
  padding: 0;
  transition: color 0.15s;
}
.mega-close:hover { color: var(--white); }
```

---

## nav.js Changes

### What stays unchanged
All four existing behaviors in `nav.js` are kept as-is:
- Scroll handler (`.scrolled` class toggle)
- Mobile menu open/close toggle
- Mobile accordion (`.mobile-menu .has-dropdown > a` click handler)
- Resize handler (collapses mobile menu at 768px)

**What to add** (new mega panel logic):

```js
// Mega panel open/close
const triggers = document.querySelectorAll('.nav-trigger');
const megaPanels = document.querySelectorAll('.mega-panel');

function closeMegaPanels() {
  megaPanels.forEach(p => {
    p.classList.remove('open');
    p.setAttribute('aria-hidden', 'true');
  });
  triggers.forEach(t => {
    t.classList.remove('active');
    t.setAttribute('aria-expanded', 'false');
  });
}

triggers.forEach(trigger => {
  trigger.addEventListener('click', () => {
    const panelId = trigger.dataset.panel;
    const panel = document.getElementById(panelId);
    const isOpen = panel.classList.contains('open');
    closeMegaPanels();
    if (!isOpen) {
      panel.classList.add('open');
      panel.setAttribute('aria-hidden', 'false');
      trigger.classList.add('active');
      trigger.setAttribute('aria-expanded', 'true');
    }
  });
});

document.querySelectorAll('.mega-close').forEach(btn => {
  btn.addEventListener('click', closeMegaPanels);
});

document.addEventListener('click', e => {
  if (!e.target.closest('.site-nav')) closeMegaPanels();
});

document.addEventListener('keydown', e => {
  if (e.key === 'Escape') closeMegaPanels();
});
```

---

## Interaction Summary

| Action | Result |
|--------|--------|
| Click "Men" (closed) | Opens Men panel, trigger turns gold, chevron rotates |
| Click "Men" (open) | Closes Men panel |
| Click "Women" while Men is open | Closes Men, opens Women |
| Click × | Closes current panel |
| Click outside `.site-nav` | Closes any open panel |
| Press Escape | Closes any open panel |
| Mobile hamburger | Unchanged — existing mobile menu with accordion |

---

## Out of Scope

- New pages for Bridal Alterations, Bridal Accessories, Mother of the Bride, Women's RTW Suits
- Any changes to page content, footer, or announcement bar
- Animations/transitions on panel open (can be added later)
