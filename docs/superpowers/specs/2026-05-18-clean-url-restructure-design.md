# Clean URL Restructure — Design Spec
**Date:** 2026-05-18  
**Project:** gregory-duane  
**Status:** Approved

## Goal

Replace `.html` extension URLs (e.g. `/tuxedos.html`) with clean directory-style URLs (e.g. `/tuxedos/`) across the entire site, hosted on GitHub Pages.

## Approach

Move each content page into its own subdirectory as `index.html`. GitHub Pages natively serves `<dir>/index.html` at `/<dir>/`. No server configuration required.

## File Moves

| From (root) | To | Live URL |
|---|---|---|
| `index.html` | `index.html` (stays) | `/` |
| `custom-suits.html` | `custom-suits/index.html` | `/custom-suits/` |
| `ready-to-wear-suits.html` | `ready-to-wear-suits/index.html` | `/ready-to-wear-suits/` |
| `handmade-shoes.html` | `handmade-shoes/index.html` | `/handmade-shoes/` |
| `tuxedos.html` | `tuxedos/index.html` | `/tuxedos/` |
| `wedding-dresses.html` | `wedding-dresses/index.html` | `/wedding-dresses/` |
| `gallery.html` | `gallery/index.html` | `/gallery/` |
| `about-us.html` | `about-us/index.html` | `/about-us/` |
| `appointment-form.html` | `appointment-form/index.html` | `/appointment-form/` |

## Changes Required in Every HTML File

### 1. Asset paths — convert to root-relative

All moved pages sit one directory level deeper than root, so relative asset paths break. Convert every asset reference to root-relative in all 9 files (including `index.html`):

| Before | After |
|---|---|
| `href="style.css"` | `href="/style.css"` |
| `src="nav.js"` | `src="/nav.js"` |
| `src="images/foo.jpg"` | `src="/images/foo.jpg"` |
| `href="images/gregory-duane-favicon.png"` | `href="/images/gregory-duane-favicon.png"` |

### 2. Internal links — convert to root-relative

| Before | After |
|---|---|
| `href="index.html"` | `href="/"` |
| `href="tuxedos.html"` | `href="/tuxedos/"` |
| `href="custom-suits.html"` | `href="/custom-suits/"` |
| `href="ready-to-wear-suits.html"` | `href="/ready-to-wear-suits/"` |
| `href="handmade-shoes.html"` | `href="/handmade-shoes/"` |
| `href="wedding-dresses.html"` | `href="/wedding-dresses/"` |
| `href="gallery.html"` | `href="/gallery/"` |
| `href="about-us.html"` | `href="/about-us/"` |
| `href="appointment-form.html"` | `href="/appointment-form/"` |

## What Does NOT Change

- `email-notification-template.html` — not a navigable page, left in root untouched
- `style.css`, `nav.js`, `images/` — remain in root
- `.github/workflows/deploy.yml` — uploads entire repo as-is, no changes needed
- All external links (Squarespace CDN product images, `tel:` links, etc.)

## Verification

After implementation, use Playwright to visit each clean URL and confirm:
- Page renders correctly (no broken CSS, JS, or images)
- Navigation links resolve correctly
- Hero images load

## Out of Scope

- 301 redirects from old `.html` URLs (GitHub Pages does not support server-side redirects for static files)
- Any changes to `style.css` or `nav.js`
