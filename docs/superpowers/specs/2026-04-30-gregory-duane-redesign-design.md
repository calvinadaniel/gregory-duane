# Gregory Duane — Full Site Redesign Spec
**Date:** 2026-04-30  
**Approach:** Pure HTML/CSS multi-page (Approach 1)  
**Status:** Approved

---

## 1. Project Context

Ground-up rebuild of gregoryduane.com. The existing Squarespace site is replaced with a static HTML build. The client offers three product verticals: bespoke custom menswear suits, handmade custom shoes, and a newly added bridal market (tuxedos for men, wedding dresses for women). The bridal line is design-forward, high-end, and bespoke — not off-the-rack.

Visual direction: design.md color/type system + editorial signals from Tom Ford Fashion (full-bleed hero, mega-menu, cinematic category pages) and Kenneth Cole (modular grids, purpose-driven copy).

---

## 2. Architecture

### Pages (8 total)

| File | Nav Location | Status |
|---|---|---|
| `index.html` | Homepage | Rebuild |
| `custom-suits.html` | Men → Bespoke Suits | Rebuild |
| `ready-to-wear-suits.html` | Men → Ready to Wear | Rebuild |
| `handmade-shoes.html` | Men → Handmade Shoes | New |
| `tuxedos.html` | Men → Tuxedos | New |
| `wedding-dresses.html` | Women → Wedding Dresses | New |
| `gallery.html` | Gallery | New |
| `about-us.html` | About | Rebuild |

### Deleted Files
- `gregory-duane-tomford.html` — prior design experiment, outside nav workflow

### Shared Assets
- `style.css` — full design system via CSS custom properties (single file)
- `nav.js` — dropdown toggle only, no framework dependency
- Pexels images in `/images/` distributed across pages
- RTW suit images in `/images/rtw-suit-images/` used on Ready to Wear and Bespoke pages

---

## 3. Navigation Structure

```
[Announcement Bar]
Men ▾ · Women ▾  |  GREGORY DUANE (logo)  |  Gallery · About · [Book a Consultation]

Men submenu:
  - Bespoke Suits        → custom-suits.html
  - Ready to Wear        → ready-to-wear-suits.html
  - Handmade Shoes       → handmade-shoes.html
  - Tuxedos              → tuxedos.html

Women submenu:
  - Wedding Dresses      → wedding-dresses.html
```

Nav behavior: sticky, three-column grid layout. Background transparent over hero, transitions to solid `#121414` on scroll. Dropdowns appear on hover (desktop) / tap (mobile). Logo uses `Gregory-Duane_white_high-res.png`.

---

## 4. Design System

### Color Tokens (CSS custom properties)
```css
--bg:       #121414;   /* page canvas, darkspace */
--surface:  #1e2020;   /* raised cards / containers */
--gold:     #e9c349;   /* primary CTA, hover, heritage accents */
--silver:   #c6c6c6;   /* dividers, ghost borders, secondary metadata */
--white:    #e2e2e2;   /* primary text, primary button fill */
--muted:    #8e9192;   /* captions, secondary labels */
```

### Typography
| Role | Family | Size | Weight | Transform |
|---|---|---|---|---|
| Display | Noto Serif | 64px | 300 | — |
| Headline LG | Noto Serif | 40px | 400 | — |
| Headline MD | Noto Serif | 32px | 400 | — |
| Body LG | Manrope | 18px | 400 | — |
| Body MD | Manrope | 16px | 400 | — |
| Label-caps | Manrope | 12px | 600 | uppercase, 0.2em spacing |
| Accent only | Tangerine | — | — | Never on functional UI |

### Shape Language
`border-radius: 0` on all elements. No exceptions.

### Spacing
- Section gap: 128px
- Page margin: 64px
- Gutter: 24px
- Max-width: 1440px

### Components

**Primary Button:** white fill (`--white`), black text, no radius. Hover: gold fill (`--gold`), black text.

**Ghost Button:** 1px solid `--silver` border, transparent fill, uppercase label-caps text. Hover: border becomes `--gold`, text becomes `--gold`.

**Input Fields:** underline only (border-bottom), no box. Focus: `--silver` → `--gold` transition.

**Cards:** borderless, full imagery fill, gradient scrim (transparent → rgba(0,0,0,0.6)) for text. Text overlaid bottom-left in label-caps.

**Nav:** centered three-column, sticky. Label-caps links. Transparent → solid `#121414` on scroll.

**Elevation:** tonal layers only (no box-shadow). Raised surfaces use `--surface` (#1e2020) against `--bg` (#121414). Ghost outlines use 1px `--silver` borders.

---

## 5. Homepage Layout

1. **Announcement bar** — full-width, `--bg` fill, `--gold` text, label-caps: *"Bespoke. By Appointment Only. · (646) 516-2664"*
2. **Navigation** — sticky three-column (`Men ▾ · Women ▾` | logo | `Gallery · About · CTA`), transparent → solid on scroll
3. **Hero** — 100vh full-bleed editorial image. GD initials (Tangerine) centered with gold underline rule. Label-caps subtitle: *"Bespoke Tailoring. Handmade Footwear. Bridal."* Ghost CTA: *"Explore the Collection"*
4. **Brand statement** — centered, 128px padding. Large Noto Serif pull-quote: *"Where craftsmanship meets legacy."* Manrope body paragraph below.
5. **Featured categories** — 3-column full-bleed image grid: Bespoke Suits · Handmade Shoes · Bridal. Label-caps overlay bottom-left. Gold border reveal on hover.
6. **Ready to Wear feature** — asymmetric 2-column: image 60% left, copy + ghost CTA 40% right.
7. **Editorial pull-quote** — full-width, `--bg`, large Noto Serif italic in `--silver`, centered.
8. **Footer** — 4-column: logo + tagline | Men links | Women + Gallery + About | CTA + contact

---

## 6. Inner Page Templates

### Template A — Bespoke Suits, Handmade Shoes, Tuxedos, Wedding Dresses
1. **Page hero** — 60vh full-bleed image. Category label-caps above, page title Noto Serif centered.
2. **Intro** — 2-column: editorial copy left, portrait/detail image right.
3. **Process steps** — 3-column. Step number in `--gold`, Noto Serif heading, Manrope description.
4. **Image grid** — 2×2 or 3×2 borderless grid from `/images/`.
5. **CTA band** — full-width `--surface`, centered Noto Serif headline + primary white button *"Book a Consultation"*

### Template B — Ready to Wear
1. Page hero (same)
2. Intro copy — single column, centered, wider measure
3. **Product grid** — 3-column cards, RTW suit images, label-caps item names, gold hover state
4. CTA band (same)

### Template C — Gallery
1. Page hero — minimal, title only
2. **Masonry grid** — 3 columns, mixed editorial images, no captions
3. CTA band (same)

### Template D — About
1. Page hero with founder image
2. Brand story — 2-column: large Noto Serif pull-quote left, Manrope narrative paragraphs right
3. Values — 3-column label-caps layout
4. CTA band (same)

---

## 7. Imagery

- **Bridal pages (Tuxedos, Wedding Dresses):** Royalty-free Pexels placeholder images until client provides photography.
- **All other pages:** Existing assets in `/images/` (Pexels editorials, RTW suit images, IMG_3985.jpeg for About).
- **Hero images:** Full-bleed, `object-fit: cover`, `object-position: center top`.
- **Cards:** Fill container, no fixed height — aspect ratio maintained via padding-bottom trick or `aspect-ratio: 3/4`.

---

## 8. Contact & CTA

- Phone: (646) 516-2664
- Email: Gregoryduaneservice@gregoryduane.com
- CTA label: *"Book a Consultation"* (primary) or *"Schedule an Appointment"* (secondary)
- No inline booking form in this build — CTA links to `mailto:` or `tel:` for now.

---

## 9. Out of Scope

- Squarespace CMS integration
- E-commerce / shopping cart
- Blog
- Support / Shipping & Returns page
- Booking widget integration
