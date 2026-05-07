# Appointment Form Page Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add an `appointment-form.html` page matching the Gregory Duane design system, update the nav CTA across all 8 pages, and produce a branded HTML email template for Squarespace notification settings.

**Architecture:** Three deliverables — (1) CSS additions to `style.css` for form field and hero-subtitle styles, (2) a new `appointment-form.html` inner page with a 60vh hero and a 2-col form grid, (3) a standalone `email-notification-template.html` built with table-based inline styles for email client compatibility. No form backend is wired locally; Squarespace handles submission in production.

**Tech Stack:** Plain HTML/CSS, no frameworks, no dependencies.

---

## File Map

| Action | File | What changes |
|--------|------|--------------|
| Modify | `style.css` | Add section 26: form field styles + `.page-hero-subtitle` |
| Create | `appointment-form.html` | New inner page |
| Create | `email-notification-template.html` | Standalone HTML email template |
| Modify ×8 | `index.html`, `custom-suits.html`, `ready-to-wear-suits.html`, `about-us.html`, `handmade-shoes.html`, `tuxedos.html`, `wedding-dresses.html`, `gallery.html` | Nav CTA href: `mailto:` → `appointment-form.html` |

---

## Task 1: Update nav CTA across all 8 pages

Each page has two Book-a-Consultation links to update:
- `.nav-right`: `class="nav-cta"` — currently `mailto:Gregoryduaneservice@gregoryduane.com`
- `.mobile-menu`: `class="btn-ghost"` — currently same `mailto:` href

**Files:** All 8 `*.html` files

- [ ] **Step 1: Confirm current state**

```bash
cd "G:/coding/Claude POC Projects/gregory-duane"
grep -c 'mailto:Gregoryduaneservice@gregoryduane.com' *.html
```

Expected: each of the 8 pages shows `2` (one for nav-right, one for mobile menu). `appointment-form.html` does not exist yet so won't appear.

- [ ] **Step 2: Replace nav-right CTA href**

```bash
sed -i 's|href="mailto:Gregoryduaneservice@gregoryduane.com" class="nav-cta"|href="appointment-form.html" class="nav-cta"|g' index.html custom-suits.html ready-to-wear-suits.html about-us.html handmade-shoes.html tuxedos.html wedding-dresses.html gallery.html
```

- [ ] **Step 3: Replace mobile menu CTA href**

```bash
sed -i 's|href="mailto:Gregoryduaneservice@gregoryduane.com" class="btn-ghost"|href="appointment-form.html" class="btn-ghost"|g' index.html custom-suits.html ready-to-wear-suits.html about-us.html handmade-shoes.html tuxedos.html wedding-dresses.html gallery.html
```

- [ ] **Step 4: Verify no nav mailto: links remain**

```bash
grep -n 'nav-cta\|btn-ghost' index.html about-us.html gallery.html
```

Expected output — every matching line should show `appointment-form.html`, not `mailto:`:
```
index.html:46:        <a href="appointment-form.html" class="nav-cta">Book a Consultation</a>
index.html:76:      <a href="appointment-form.html" class="btn-ghost">Book a Consultation</a>
about-us.html:46:        <a href="appointment-form.html" class="nav-cta">Book a Consultation</a>
about-us.html:76:      <a href="appointment-form.html" class="btn-ghost">Book a Consultation</a>
...
```

- [ ] **Step 5: Verify footer mailto: links are untouched**

```bash
grep -n 'btn-primary\|footer-contact' index.html | head -10
```

Expected: the footer `btn-primary` and `footer-contact` mailto links are unchanged.

- [ ] **Step 6: Commit**

```bash
git add index.html custom-suits.html ready-to-wear-suits.html about-us.html handmade-shoes.html tuxedos.html wedding-dresses.html gallery.html
git commit -m "feat: update nav CTA to link to appointment-form.html"
```

---

## Task 2: Add form CSS to style.css

`style.css` currently ends at line 793. Append a new section 26 with form field styles and a `.page-hero-subtitle` rule (needed by Task 3).

**Files:**
- Modify: `style.css` (append after line 793)

- [ ] **Step 1: Append form CSS**

Open `style.css` and add the following block at the very end (after the last `@media` block):

```css

/* 26. Appointment Form */
.page-hero-subtitle {
  font-family: var(--font-sans);
  font-size: 13px;
  letter-spacing: 0.12em;
  color: var(--silver);
  margin-top: 16px;
}
.form-section {
  padding: var(--section-gap) var(--page-margin);
}
.form-container {
  max-width: 680px;
  margin: 0 auto;
}
.form-eyebrow {
  font-family: var(--font-sans);
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.25em;
  text-transform: uppercase;
  color: var(--gold);
  text-align: center;
  margin-bottom: 48px;
}
.form-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0 32px;
}
.form-field {
  margin-bottom: 28px;
}
.form-field.full {
  grid-column: 1 / -1;
}
.form-label {
  display: block;
  font-family: var(--font-sans);
  font-size: 10px;
  font-weight: 600;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--muted);
  margin-bottom: 8px;
}
.form-input,
.form-select,
.form-textarea {
  width: 100%;
  background: var(--surface);
  border: 1px solid var(--outline);
  border-radius: 2px;
  color: var(--white);
  font-family: var(--font-serif);
  font-size: 15px;
  padding: 13px 16px;
  transition: border-color 0.2s;
  appearance: none;
  -webkit-appearance: none;
}
.form-input::placeholder,
.form-textarea::placeholder { color: var(--muted); }
.form-input:focus,
.form-select:focus,
.form-textarea:focus {
  outline: none;
  border-color: var(--gold);
}
.form-select {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='10' height='6' viewBox='0 0 10 6'%3E%3Cpath d='M0 0l5 6 5-6z' fill='%238e9192'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 16px center;
  padding-right: 40px;
  cursor: pointer;
}
.form-select option { background: var(--bg); }
.form-textarea {
  min-height: 130px;
  resize: vertical;
  line-height: 1.6;
}
.form-submit {
  display: flex;
  justify-content: flex-end;
  margin-top: 8px;
}
@media (max-width: 768px) {
  .form-grid { grid-template-columns: 1fr; }
  .form-field.full { grid-column: 1; }
}
```

- [ ] **Step 2: Verify line count increased**

```bash
wc -l style.css
```

Expected: ~870 lines (was 793).

- [ ] **Step 3: Commit**

```bash
git add style.css
git commit -m "feat: add form field and page-hero-subtitle CSS to design system"
```

---

## Task 3: Create appointment-form.html

**Files:**
- Create: `appointment-form.html`

- [ ] **Step 1: Create the file**

Create `appointment-form.html` with this exact content:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Book a Consultation — Gregory Duane</title>
  <meta name="description" content="Reserve a private consultation at the Gregory Duane atelier. Bespoke suits, handmade footwear, and bridal by appointment only. New York City.">
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
        <a href="appointment-form.html" class="nav-cta">Book a Consultation</a>
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
      <a href="appointment-form.html" class="btn-ghost">Book a Consultation</a>
    </div>
  </nav>

  <div class="page-hero">
    <img src="images/IMG_4959.JPG" alt="Gregory Duane atelier" />
    <div class="page-hero-overlay">
      <span class="page-hero-label">Atelier Appointment</span>
      <h1 class="page-hero-title">Book a Consultation</h1>
      <p class="page-hero-subtitle">Private fittings by appointment&nbsp;&nbsp;·&nbsp;&nbsp;New York City</p>
    </div>
  </div>

  <section class="form-section">
    <div class="form-container">
      <p class="form-eyebrow">Reserve Your Visit</p>
      <form action="#" method="post" novalidate>
        <div class="form-grid">

          <div class="form-field">
            <label class="form-label" for="first-name">First Name</label>
            <input class="form-input" type="text" id="first-name" name="first_name"
              placeholder="First name" autocomplete="given-name" required>
          </div>

          <div class="form-field">
            <label class="form-label" for="last-name">Last Name</label>
            <input class="form-input" type="text" id="last-name" name="last_name"
              placeholder="Last name" autocomplete="family-name" required>
          </div>

          <div class="form-field">
            <label class="form-label" for="email">Email Address</label>
            <input class="form-input" type="email" id="email" name="email"
              placeholder="your@email.com" autocomplete="email" required>
          </div>

          <div class="form-field">
            <label class="form-label" for="phone">Phone</label>
            <input class="form-input" type="tel" id="phone" name="phone"
              placeholder="(000) 000-0000" autocomplete="tel">
          </div>

          <div class="form-field full">
            <label class="form-label" for="service">Service</label>
            <select class="form-select" id="service" name="service" required>
              <option value="" disabled selected>Select a service</option>
              <option value="bespoke-suits">Bespoke Suits</option>
              <option value="ready-to-wear">Ready to Wear Suits</option>
              <option value="handmade-shoes">Handmade Shoes</option>
              <option value="tuxedos">Tuxedos</option>
              <option value="wedding-dresses">Wedding Dresses</option>
            </select>
          </div>

          <div class="form-field full">
            <label class="form-label" for="message">Tell us about your vision</label>
            <textarea class="form-textarea" id="message" name="message"
              placeholder="Share details about your occasion, style preferences, timeline, or any questions you have."></textarea>
          </div>

        </div>
        <div class="form-submit">
          <button type="submit" class="btn-primary">Request Appointment</button>
        </div>
      </form>
    </div>
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
        <a href="appointment-form.html" class="btn-primary">Book a Consultation</a>
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

- [ ] **Step 2: Open in browser and verify**

Navigate to `http://localhost:8080/appointment-form.html`

Check:
- 60vh page hero loads with `IMG_4959.JPG` background, dark overlay, gold eyebrow, H1, and subtitle
- Form section shows "Reserve Your Visit" eyebrow in gold caps
- First Name / Last Name appear side-by-side
- Email / Phone appear side-by-side
- Service dropdown is full-width, opens with correct 5 options
- Message textarea is full-width, ~5 rows tall
- "Request Appointment" button is right-aligned, white fill
- Scrolling past 110px turns the nav solid
- Mobile menu works at < 768px width (use browser DevTools to test)
- Footer matches all other pages

- [ ] **Step 3: Verify nav link from homepage**

Navigate to `http://localhost:8080/index.html`, click "Book a Consultation" in the nav. Confirm it loads `appointment-form.html`.

- [ ] **Step 4: Commit**

```bash
git add appointment-form.html
git commit -m "feat: add appointment-form.html — 60vh hero + form grid"
```

---

## Task 4: Create email-notification-template.html

Standalone HTML email built with table-based layout and 100% inline styles for email client compatibility. No external CSS, no web fonts. Placeholders use `{{Field Name}}` syntax — replace with Squarespace's actual merge tags when configuring the notification.

**Files:**
- Create: `email-notification-template.html`

- [ ] **Step 1: Create the file**

Create `email-notification-template.html` with this exact content:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Gregory Duane — New Consultation Request</title>
</head>
<body style="margin:0;padding:0;background:#f0ebe3;font-family:Arial,Helvetica,sans-serif;">

  <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#f0ebe3;">
    <tr>
      <td align="center" style="padding:32px 16px;">
        <table width="600" cellpadding="0" cellspacing="0" border="0" style="max-width:600px;width:100%;">

          <!-- Header -->
          <tr>
            <td style="background:#121414;padding:28px 40px 20px;border-bottom:3px solid #e9c349;text-align:center;">
              <p style="margin:0;font-family:Arial,Helvetica,sans-serif;font-size:18px;font-weight:700;letter-spacing:4px;color:#e9c349;text-transform:uppercase;">GREGORY DUANE</p>
              <p style="margin:6px 0 0;font-size:10px;letter-spacing:2px;text-transform:uppercase;color:#8e9192;font-family:Arial,Helvetica,sans-serif;">New Consultation Request</p>
            </td>
          </tr>

          <!-- Subject Banner -->
          <tr>
            <td style="background:#f0ebe3;padding:14px 40px;border-bottom:1px solid #ddd8ce;">
              <p style="margin:0;font-size:10px;letter-spacing:2px;text-transform:uppercase;font-weight:700;color:#1a1a1a;font-family:Arial,Helvetica,sans-serif;">&#128203;&nbsp; New Appointment Inquiry</p>
            </td>
          </tr>

          <!-- Body -->
          <tr>
            <td style="background:#faf8f4;padding:32px 40px;">

              <!-- Full Name -->
              <table width="100%" cellpadding="0" cellspacing="0" border="0">
                <tr>
                  <td style="border-bottom:1px solid #e8e3db;padding-bottom:20px;margin-bottom:20px;">
                    <p style="margin:0 0 5px;font-size:10px;letter-spacing:2px;text-transform:uppercase;color:#e9c349;font-family:Arial,Helvetica,sans-serif;font-weight:700;">Full Name</p>
                    <p style="margin:0;font-size:15px;color:#2a2a2a;font-family:Georgia,'Times New Roman',serif;line-height:1.5;">{{First Name}} {{Last Name}}</p>
                  </td>
                </tr>
              </table>

              <div style="height:20px;"></div>

              <!-- Email -->
              <table width="100%" cellpadding="0" cellspacing="0" border="0">
                <tr>
                  <td style="border-bottom:1px solid #e8e3db;padding-bottom:20px;">
                    <p style="margin:0 0 5px;font-size:10px;letter-spacing:2px;text-transform:uppercase;color:#e9c349;font-family:Arial,Helvetica,sans-serif;font-weight:700;">Email Address</p>
                    <p style="margin:0;font-size:15px;color:#2a2a2a;font-family:Georgia,'Times New Roman',serif;line-height:1.5;">{{Email}}</p>
                  </td>
                </tr>
              </table>

              <div style="height:20px;"></div>

              <!-- Phone -->
              <table width="100%" cellpadding="0" cellspacing="0" border="0">
                <tr>
                  <td style="border-bottom:1px solid #e8e3db;padding-bottom:20px;">
                    <p style="margin:0 0 5px;font-size:10px;letter-spacing:2px;text-transform:uppercase;color:#e9c349;font-family:Arial,Helvetica,sans-serif;font-weight:700;">Phone</p>
                    <p style="margin:0;font-size:15px;color:#2a2a2a;font-family:Georgia,'Times New Roman',serif;line-height:1.5;">{{Phone}}</p>
                  </td>
                </tr>
              </table>

              <div style="height:20px;"></div>

              <!-- Service -->
              <table width="100%" cellpadding="0" cellspacing="0" border="0">
                <tr>
                  <td style="border-bottom:1px solid #e8e3db;padding-bottom:20px;">
                    <p style="margin:0 0 5px;font-size:10px;letter-spacing:2px;text-transform:uppercase;color:#e9c349;font-family:Arial,Helvetica,sans-serif;font-weight:700;">Requested Service</p>
                    <p style="margin:0;font-size:15px;color:#2a2a2a;font-family:Georgia,'Times New Roman',serif;line-height:1.5;">{{Service}}</p>
                  </td>
                </tr>
              </table>

              <div style="height:20px;"></div>

              <!-- Message -->
              <table width="100%" cellpadding="0" cellspacing="0" border="0">
                <tr>
                  <td>
                    <p style="margin:0 0 5px;font-size:10px;letter-spacing:2px;text-transform:uppercase;color:#e9c349;font-family:Arial,Helvetica,sans-serif;font-weight:700;">Message</p>
                    <p style="margin:0;font-size:15px;color:#2a2a2a;font-family:Georgia,'Times New Roman',serif;line-height:1.6;font-style:italic;">{{Message}}</p>
                  </td>
                </tr>
              </table>

            </td>
          </tr>

          <!-- Footer -->
          <tr>
            <td style="background:#121414;padding:16px 40px;text-align:center;">
              <p style="margin:0;font-size:10px;letter-spacing:1.5px;text-transform:uppercase;color:#8e9192;font-family:Arial,Helvetica,sans-serif;">Gregory Duane &nbsp;·&nbsp; New York City &nbsp;·&nbsp; gregoryduane.com</p>
            </td>
          </tr>

        </table>
      </td>
    </tr>
  </table>

</body>
</html>
```

- [ ] **Step 2: Preview in browser**

Open `http://localhost:8080/email-notification-template.html`

Verify:
- Dark header with "GREGORY DUANE" in gold, "New Consultation Request" subtitle in muted grey
- 3px gold bottom border on header
- Off-white banner with "New Appointment Inquiry"
- Cream body with 5 labeled field blocks (Full Name, Email Address, Phone, Requested Service, Message)
- Gold uppercase labels, Georgia serif values
- Message value displays in italic
- Dark footer with muted text
- Overall email width appears correct at ~600px

- [ ] **Step 3: Note on Squarespace integration**

When configuring the Squarespace form notification email, replace the `{{Field Name}}` placeholders with Squarespace's actual field merge tags. In Squarespace's Form Block settings, field names correspond to the label you gave each field. The notification email body accepts full HTML — paste the entire contents of this file there.

- [ ] **Step 4: Commit**

```bash
git add email-notification-template.html
git commit -m "feat: add branded HTML email notification template for Squarespace"
```

---

## Self-Review Checklist

**Spec coverage:**
- [x] `appointment-form.html` with 60vh hero — Task 3
- [x] Form fields: First Name, Last Name, Email, Phone, Service dropdown, Message — Task 3
- [x] Service options: Bespoke Suits, Ready to Wear Suits, Handmade Shoes, Tuxedos, Wedding Dresses — Task 3
- [x] `email-notification-template.html` with cream body, dark header/footer, gold labels — Task 4
- [x] Nav CTA updated across all 8 pages — Task 1
- [x] Both nav-right and mobile-menu CTAs updated — Task 1 Steps 2–3
- [x] Form `action="#"` (no live submission locally) — Task 3 Step 1
- [x] Footer CTA on appointment-form.html links to appointment-form.html — Task 3 Step 1

**Type consistency:** No shared types — plain HTML/CSS, no naming conflicts across tasks.

**Placeholder scan:** Email template uses `{{First Name}} {{Last Name}}` etc. — these are intentional Squarespace merge tag placeholders, documented in Task 4 Step 3.
