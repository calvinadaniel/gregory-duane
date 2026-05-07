# Appointment Form Page — Design Spec
**Date:** 2026-05-07  
**Project:** Gregory Duane  
**Status:** Approved

---

## Overview

Add a new `appointment-form.html` page to the local Gregory Duane site matching the existing design system. Update the "Book a Consultation" nav CTA across all 8 pages to link to this new local page instead of the current `mailto:` link. Deliver a companion `email-notification-template.html` file containing the branded HTML email template for copy-paste into Squarespace's form notification settings.

This page will eventually live inside Squarespace. The local build is a pixel-perfect design prototype — form submission is not wired up locally (Squarespace handles it in production).

---

## Deliverables

1. **`appointment-form.html`** — new inner page following the existing site structure
2. **`email-notification-template.html`** — standalone branded HTML email template
3. **Nav CTA update** — change `.nav-cta` link from `mailto:Gregoryduaneservice@gregoryduane.com` to `appointment-form.html` in all 8 existing HTML pages

---

## Page: `appointment-form.html`

### Structure

Follows the same document structure as all other inner pages: `<link rel="stylesheet" href="style.css">`, nav markup, page body, 4-column footer, `<script src="nav.js">`.

### Sections (top to bottom)

**1. Announcement bar**  
Identical to all other pages.

**2. Sticky nav**  
Identical markup to all other pages. The `.nav-cta` on this page links to `#` (self) or omits the href — no circular redirect needed.

**3. Page hero (60vh)**  
- Class: `.page-hero` (existing design system class)
- Eyebrow: `ATELIER APPOINTMENT`
- H1: `Book a Consultation`
- Subtitle: `Private fittings by appointment — New York City`
- Background: `images/IMG_4959.JPG` (same atelier photo used in `about-us.html`) with the standard dark overlay treatment

**4. Form section**  
- Centered container, `max-width: 680px`, horizontally centered with auto margins
- Section heading above form: `Reserve Your Visit` (`.section-label` or equivalent caps treatment)
- Form fields:

| Row | Fields | Width |
|-----|--------|-------|
| 1 | First Name, Last Name | 2-col grid |
| 2 | Email Address, Phone | 2-col grid |
| 3 | Service (dropdown) | Full width |
| 4 | Message (textarea, ~5 rows) | Full width |

- **Service dropdown options:** Bespoke Suits, Ready to Wear Suits, Handmade Shoes, Tuxedos, Wedding Dresses
- **Submit button:** `.btn-primary` (gold fill), label "Request Appointment", right-aligned
- **Form action:** `action="#"` — no live submission locally; Squarespace handles production submission

**Field styling** follows the dark form field pattern established in `style.css`:
- Background: `var(--surface)` (`#1e2020`)
- Border: `1px solid var(--outline)` (`#444748`)
- Text color: `var(--white)`
- Label: uppercase Manrope, `var(--muted)`, letter-spacing
- Focus state: border color transitions to `var(--gold)`

**5. 4-column footer**  
Identical markup to all other pages.

---

## Nav Update: All 8 Pages

Change the `.nav-cta` anchor in the nav and mobile menu of every existing HTML page:

**From:**
```html
<a href="mailto:Gregoryduaneservice@gregoryduane.com" class="nav-cta">Book a Consultation</a>
```

**To:**
```html
<a href="appointment-form.html" class="nav-cta">Book a Consultation</a>
```

Pages to update: `index.html`, `custom-suits.html`, `ready-to-wear-suits.html`, `about-us.html`, `handmade-shoes.html`, `tuxedos.html`, `wedding-dresses.html`, `gallery.html`

Note: The nav CTA appears twice in each page's markup (once in `.nav-right`, once inside `.mobile-menu`). Both instances must be updated.

---

## Email Template: `email-notification-template.html`

Standalone HTML file for copy-paste into Squarespace's form notification email body.

### Layout (top to bottom)

**Header**
- Background: `#121414` (dark)
- Bottom border: `3px solid #e9c349` (gold)
- Content: "GREGORY DUANE" in `#e9c349`, `letter-spacing: 3px`, Manrope bold
- Subline: "New Consultation Request" in `#8e9192`, uppercase, small

**Subject banner**
- Background: `#f0ebe3` (warm off-white)
- Bottom border: `1px solid #ddd8ce`
- Text: "NEW APPOINTMENT INQUIRY" — uppercase Manrope, `#1a1a1a`, `letter-spacing: 2px`

**Body**
- Background: `#faf8f4` (cream)
- Each form field displayed as a labeled block:
  - Label: uppercase, `#e9c349`, `letter-spacing: 2px`, Manrope, `font-size: 11px`
  - Value: `#2a2a2a`, Georgia serif, `font-size: 14px`, `line-height: 1.6`
  - Separator: `1px solid #e8e3db` between fields
- Fields shown: Full Name, Email Address, Phone, Requested Service, Message
- Message value displayed in italic

**Footer**
- Background: `#121414` (dark)
- Text: `Gregory Duane · New York City · gregoryduane.com` — `#8e9192`, uppercase, small

### Squarespace Compatibility Notes
- Use inline styles only (no `<style>` blocks — many email clients strip them)
- No web fonts — fall back to Georgia (serif) and Arial/Helvetica (sans)
- Table-based layout for Outlook compatibility
- `#e9c349` gold renders correctly in Outlook without transparency

---

## Design System Tokens Used

| Token | Value | Usage |
|-------|-------|-------|
| `--bg` | `#121414` | Page background |
| `--surface` | `#1e2020` | Form field backgrounds |
| `--gold` | `#e9c349` | Labels, CTA button, borders |
| `--white` | `#e2e2e2` | Body text |
| `--muted` | `#8e9192` | Field placeholder text, subtitles |
| `--outline` | `#444748` | Field borders, dividers |
| Noto Serif | — | Hero heading, body copy |
| Manrope | — | Labels, caps, UI text |

---

## Out of Scope

- Live form submission wiring (Squarespace handles in production)
- Confirmation/thank-you page
- Backend or server-side logic
- Changes to Squarespace itself
