# Clean URL Restructure Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restructure all site pages from root-level `.html` files into subdirectories (`page/index.html`) so every page is served at a clean `/page/` URL on GitHub Pages.

**Architecture:** Move 8 content pages into named subdirectories as `index.html`; `index.html` stays in root with links updated only. Asset and link paths differ by depth: `index.html` (root) uses bare-relative paths (`tuxedos/`), while subdirectory pages use `../` parent-relative paths (`../style.css`, `../tuxedos/`). Root-relative paths (`/style.css`) are intentionally avoided — the GitHub Pages preview site is at `calvinadaniel.github.io/gregory-duane/` (a project page, not root), so `/style.css` would resolve to the wrong base path.

**Tech Stack:** Static HTML/CSS, GitHub Pages, PowerShell (Windows), Playwright MCP for verification

**Working directory for all commands:** `G:\coding\Claude POC Projects\gregory-duane`

---

## File Map

| Modified | Responsibility |
|---|---|
| `index.html` | Update internal links in-place (assets already correct) |
| `custom-suits/index.html` | Moved from `custom-suits.html`, assets + links → `../` |
| `ready-to-wear-suits/index.html` | Moved from `ready-to-wear-suits.html`, assets + links → `../` |
| `handmade-shoes/index.html` | Moved from `handmade-shoes.html`, assets + links → `../` |
| `tuxedos/index.html` | Moved from `tuxedos.html`, assets + links → `../` |
| `wedding-dresses/index.html` | Moved from `wedding-dresses.html`, assets + links → `../` |
| `gallery/index.html` | Moved from `gallery.html`, assets + links → `../` |
| `about-us/index.html` | Moved from `about-us.html`, assets + links → `../` |
| `appointment-form/index.html` | Moved from `appointment-form.html`, assets + links → `../` |

---

## Replacement Reference

### For index.html (root — assets are already correct, links only)

| Before | After |
|---|---|
| `href="index.html"` | `href="./"` |
| `href="custom-suits.html"` | `href="custom-suits/"` |
| `href="ready-to-wear-suits.html"` | `href="ready-to-wear-suits/"` |
| `href="handmade-shoes.html"` | `href="handmade-shoes/"` |
| `href="tuxedos.html"` | `href="tuxedos/"` |
| `href="wedding-dresses.html"` | `href="wedding-dresses/"` |
| `href="gallery.html"` | `href="gallery/"` |
| `href="about-us.html"` | `href="about-us/"` |
| `href="appointment-form.html"` | `href="appointment-form/"` |

### For all subdirectory pages (assets + links both need `../`)

**Assets:**

| Before | After |
|---|---|
| `href="style.css"` | `href="../style.css"` |
| `src="nav.js"` | `src="../nav.js"` |
| `src="images/` | `src="../images/` |
| `href="images/` | `href="../images/` |

**Links:**

| Before | After |
|---|---|
| `href="index.html"` | `href="../"` |
| `href="custom-suits.html"` | `href="../custom-suits/"` |
| `href="ready-to-wear-suits.html"` | `href="../ready-to-wear-suits/"` |
| `href="handmade-shoes.html"` | `href="../handmade-shoes/"` |
| `href="tuxedos.html"` | `href="../tuxedos/"` |
| `href="wedding-dresses.html"` | `href="../wedding-dresses/"` |
| `href="gallery.html"` | `href="../gallery/"` |
| `href="about-us.html"` | `href="../about-us/"` |
| `href="appointment-form.html"` | `href="../appointment-form/"` |

---

## Task 1: Update index.html in-place

**Files:**
- Modify: `index.html`

- [ ] **Step 1: Apply link replacements (assets are already correct — no asset changes needed)**

```powershell
$file = "G:\coding\Claude POC Projects\gregory-duane\index.html"
(Get-Content $file -Raw) `
  -replace 'href="index\.html"', 'href="./"' `
  -replace 'href="custom-suits\.html"', 'href="custom-suits/"' `
  -replace 'href="ready-to-wear-suits\.html"', 'href="ready-to-wear-suits/"' `
  -replace 'href="handmade-shoes\.html"', 'href="handmade-shoes/"' `
  -replace 'href="tuxedos\.html"', 'href="tuxedos/"' `
  -replace 'href="wedding-dresses\.html"', 'href="wedding-dresses/"' `
  -replace 'href="gallery\.html"', 'href="gallery/"' `
  -replace 'href="about-us\.html"', 'href="about-us/"' `
  -replace 'href="appointment-form\.html"', 'href="appointment-form/"' `
  | Set-Content $file -Encoding UTF8
```

- [ ] **Step 2: Verify no .html hrefs remain**

```powershell
Select-String -Path "G:\coding\Claude POC Projects\gregory-duane\index.html" -Pattern 'href="[^"]*\.html"'
```

Expected: no output (zero matches)

- [ ] **Step 3: Commit**

```powershell
cd "G:\coding\Claude POC Projects\gregory-duane"
git add index.html
git commit -m "refactor: convert index.html internal links to clean URLs"
```

---

## Task 2: Move custom-suits.html → custom-suits/index.html

**Files:**
- Create: `custom-suits/index.html`
- Delete: `custom-suits.html`

- [ ] **Step 1: Create subdirectory and copy file**

```powershell
New-Item -ItemType Directory -Force "G:\coding\Claude POC Projects\gregory-duane\custom-suits"
Copy-Item "G:\coding\Claude POC Projects\gregory-duane\custom-suits.html" `
          "G:\coding\Claude POC Projects\gregory-duane\custom-suits\index.html"
```

- [ ] **Step 2: Apply asset and link replacements**

```powershell
$file = "G:\coding\Claude POC Projects\gregory-duane\custom-suits\index.html"
(Get-Content $file -Raw) `
  -replace 'href="style\.css"', 'href="../style.css"' `
  -replace 'src="nav\.js"', 'src="../nav.js"' `
  -replace 'src="images/', 'src="../images/' `
  -replace 'href="images/', 'href="../images/' `
  -replace 'href="index\.html"', 'href="../"' `
  -replace 'href="custom-suits\.html"', 'href="../custom-suits/"' `
  -replace 'href="ready-to-wear-suits\.html"', 'href="../ready-to-wear-suits/"' `
  -replace 'href="handmade-shoes\.html"', 'href="../handmade-shoes/"' `
  -replace 'href="tuxedos\.html"', 'href="../tuxedos/"' `
  -replace 'href="wedding-dresses\.html"', 'href="../wedding-dresses/"' `
  -replace 'href="gallery\.html"', 'href="../gallery/"' `
  -replace 'href="about-us\.html"', 'href="../about-us/"' `
  -replace 'href="appointment-form\.html"', 'href="../appointment-form/"' `
  | Set-Content $file -Encoding UTF8
```

- [ ] **Step 3: Verify no .html hrefs remain**

```powershell
Select-String -Path "G:\coding\Claude POC Projects\gregory-duane\custom-suits\index.html" -Pattern 'href="[^"]*\.html"'
```

Expected: no output

- [ ] **Step 4: Delete original file and commit**

```powershell
cd "G:\coding\Claude POC Projects\gregory-duane"
git add custom-suits/index.html
git rm custom-suits.html
git commit -m "refactor: move custom-suits.html to custom-suits/index.html"
```

---

## Task 3: Move ready-to-wear-suits.html → ready-to-wear-suits/index.html

**Files:**
- Create: `ready-to-wear-suits/index.html`
- Delete: `ready-to-wear-suits.html`

- [ ] **Step 1: Create subdirectory and copy file**

```powershell
New-Item -ItemType Directory -Force "G:\coding\Claude POC Projects\gregory-duane\ready-to-wear-suits"
Copy-Item "G:\coding\Claude POC Projects\gregory-duane\ready-to-wear-suits.html" `
          "G:\coding\Claude POC Projects\gregory-duane\ready-to-wear-suits\index.html"
```

- [ ] **Step 2: Apply asset and link replacements**

```powershell
$file = "G:\coding\Claude POC Projects\gregory-duane\ready-to-wear-suits\index.html"
(Get-Content $file -Raw) `
  -replace 'href="style\.css"', 'href="../style.css"' `
  -replace 'src="nav\.js"', 'src="../nav.js"' `
  -replace 'src="images/', 'src="../images/' `
  -replace 'href="images/', 'href="../images/' `
  -replace 'href="index\.html"', 'href="../"' `
  -replace 'href="custom-suits\.html"', 'href="../custom-suits/"' `
  -replace 'href="ready-to-wear-suits\.html"', 'href="../ready-to-wear-suits/"' `
  -replace 'href="handmade-shoes\.html"', 'href="../handmade-shoes/"' `
  -replace 'href="tuxedos\.html"', 'href="../tuxedos/"' `
  -replace 'href="wedding-dresses\.html"', 'href="../wedding-dresses/"' `
  -replace 'href="gallery\.html"', 'href="../gallery/"' `
  -replace 'href="about-us\.html"', 'href="../about-us/"' `
  -replace 'href="appointment-form\.html"', 'href="../appointment-form/"' `
  | Set-Content $file -Encoding UTF8
```

- [ ] **Step 3: Verify no .html hrefs remain**

```powershell
Select-String -Path "G:\coding\Claude POC Projects\gregory-duane\ready-to-wear-suits\index.html" -Pattern 'href="[^"]*\.html"'
```

Expected: no output

- [ ] **Step 4: Delete original file and commit**

```powershell
cd "G:\coding\Claude POC Projects\gregory-duane"
git add ready-to-wear-suits/index.html
git rm ready-to-wear-suits.html
git commit -m "refactor: move ready-to-wear-suits.html to ready-to-wear-suits/index.html"
```

---

## Task 4: Move handmade-shoes.html → handmade-shoes/index.html

**Files:**
- Create: `handmade-shoes/index.html`
- Delete: `handmade-shoes.html`

- [ ] **Step 1: Create subdirectory and copy file**

```powershell
New-Item -ItemType Directory -Force "G:\coding\Claude POC Projects\gregory-duane\handmade-shoes"
Copy-Item "G:\coding\Claude POC Projects\gregory-duane\handmade-shoes.html" `
          "G:\coding\Claude POC Projects\gregory-duane\handmade-shoes\index.html"
```

- [ ] **Step 2: Apply asset and link replacements**

```powershell
$file = "G:\coding\Claude POC Projects\gregory-duane\handmade-shoes\index.html"
(Get-Content $file -Raw) `
  -replace 'href="style\.css"', 'href="../style.css"' `
  -replace 'src="nav\.js"', 'src="../nav.js"' `
  -replace 'src="images/', 'src="../images/' `
  -replace 'href="images/', 'href="../images/' `
  -replace 'href="index\.html"', 'href="../"' `
  -replace 'href="custom-suits\.html"', 'href="../custom-suits/"' `
  -replace 'href="ready-to-wear-suits\.html"', 'href="../ready-to-wear-suits/"' `
  -replace 'href="handmade-shoes\.html"', 'href="../handmade-shoes/"' `
  -replace 'href="tuxedos\.html"', 'href="../tuxedos/"' `
  -replace 'href="wedding-dresses\.html"', 'href="../wedding-dresses/"' `
  -replace 'href="gallery\.html"', 'href="../gallery/"' `
  -replace 'href="about-us\.html"', 'href="../about-us/"' `
  -replace 'href="appointment-form\.html"', 'href="../appointment-form/"' `
  | Set-Content $file -Encoding UTF8
```

- [ ] **Step 3: Verify no .html hrefs remain**

```powershell
Select-String -Path "G:\coding\Claude POC Projects\gregory-duane\handmade-shoes\index.html" -Pattern 'href="[^"]*\.html"'
```

Expected: no output

- [ ] **Step 4: Delete original file and commit**

```powershell
cd "G:\coding\Claude POC Projects\gregory-duane"
git add handmade-shoes/index.html
git rm handmade-shoes.html
git commit -m "refactor: move handmade-shoes.html to handmade-shoes/index.html"
```

---

## Task 5: Move tuxedos.html → tuxedos/index.html

**Files:**
- Create: `tuxedos/index.html`
- Delete: `tuxedos.html`

- [ ] **Step 1: Create subdirectory and copy file**

```powershell
New-Item -ItemType Directory -Force "G:\coding\Claude POC Projects\gregory-duane\tuxedos"
Copy-Item "G:\coding\Claude POC Projects\gregory-duane\tuxedos.html" `
          "G:\coding\Claude POC Projects\gregory-duane\tuxedos\index.html"
```

- [ ] **Step 2: Apply asset and link replacements**

```powershell
$file = "G:\coding\Claude POC Projects\gregory-duane\tuxedos\index.html"
(Get-Content $file -Raw) `
  -replace 'href="style\.css"', 'href="../style.css"' `
  -replace 'src="nav\.js"', 'src="../nav.js"' `
  -replace 'src="images/', 'src="../images/' `
  -replace 'href="images/', 'href="../images/' `
  -replace 'href="index\.html"', 'href="../"' `
  -replace 'href="custom-suits\.html"', 'href="../custom-suits/"' `
  -replace 'href="ready-to-wear-suits\.html"', 'href="../ready-to-wear-suits/"' `
  -replace 'href="handmade-shoes\.html"', 'href="../handmade-shoes/"' `
  -replace 'href="tuxedos\.html"', 'href="../tuxedos/"' `
  -replace 'href="wedding-dresses\.html"', 'href="../wedding-dresses/"' `
  -replace 'href="gallery\.html"', 'href="../gallery/"' `
  -replace 'href="about-us\.html"', 'href="../about-us/"' `
  -replace 'href="appointment-form\.html"', 'href="../appointment-form/"' `
  | Set-Content $file -Encoding UTF8
```

- [ ] **Step 3: Verify no .html hrefs remain**

```powershell
Select-String -Path "G:\coding\Claude POC Projects\gregory-duane\tuxedos\index.html" -Pattern 'href="[^"]*\.html"'
```

Expected: no output

- [ ] **Step 4: Delete original file and commit**

```powershell
cd "G:\coding\Claude POC Projects\gregory-duane"
git add tuxedos/index.html
git rm tuxedos.html
git commit -m "refactor: move tuxedos.html to tuxedos/index.html"
```

---

## Task 6: Move wedding-dresses.html → wedding-dresses/index.html

**Files:**
- Create: `wedding-dresses/index.html`
- Delete: `wedding-dresses.html`

- [ ] **Step 1: Create subdirectory and copy file**

```powershell
New-Item -ItemType Directory -Force "G:\coding\Claude POC Projects\gregory-duane\wedding-dresses"
Copy-Item "G:\coding\Claude POC Projects\gregory-duane\wedding-dresses.html" `
          "G:\coding\Claude POC Projects\gregory-duane\wedding-dresses\index.html"
```

- [ ] **Step 2: Apply asset and link replacements**

```powershell
$file = "G:\coding\Claude POC Projects\gregory-duane\wedding-dresses\index.html"
(Get-Content $file -Raw) `
  -replace 'href="style\.css"', 'href="../style.css"' `
  -replace 'src="nav\.js"', 'src="../nav.js"' `
  -replace 'src="images/', 'src="../images/' `
  -replace 'href="images/', 'href="../images/' `
  -replace 'href="index\.html"', 'href="../"' `
  -replace 'href="custom-suits\.html"', 'href="../custom-suits/"' `
  -replace 'href="ready-to-wear-suits\.html"', 'href="../ready-to-wear-suits/"' `
  -replace 'href="handmade-shoes\.html"', 'href="../handmade-shoes/"' `
  -replace 'href="tuxedos\.html"', 'href="../tuxedos/"' `
  -replace 'href="wedding-dresses\.html"', 'href="../wedding-dresses/"' `
  -replace 'href="gallery\.html"', 'href="../gallery/"' `
  -replace 'href="about-us\.html"', 'href="../about-us/"' `
  -replace 'href="appointment-form\.html"', 'href="../appointment-form/"' `
  | Set-Content $file -Encoding UTF8
```

- [ ] **Step 3: Verify no .html hrefs remain**

```powershell
Select-String -Path "G:\coding\Claude POC Projects\gregory-duane\wedding-dresses\index.html" -Pattern 'href="[^"]*\.html"'
```

Expected: no output

- [ ] **Step 4: Delete original file and commit**

```powershell
cd "G:\coding\Claude POC Projects\gregory-duane"
git add wedding-dresses/index.html
git rm wedding-dresses.html
git commit -m "refactor: move wedding-dresses.html to wedding-dresses/index.html"
```

---

## Task 7: Move gallery.html → gallery/index.html

**Files:**
- Create: `gallery/index.html`
- Delete: `gallery.html`

- [ ] **Step 1: Create subdirectory and copy file**

```powershell
New-Item -ItemType Directory -Force "G:\coding\Claude POC Projects\gregory-duane\gallery"
Copy-Item "G:\coding\Claude POC Projects\gregory-duane\gallery.html" `
          "G:\coding\Claude POC Projects\gregory-duane\gallery\index.html"
```

- [ ] **Step 2: Apply asset and link replacements**

```powershell
$file = "G:\coding\Claude POC Projects\gregory-duane\gallery\index.html"
(Get-Content $file -Raw) `
  -replace 'href="style\.css"', 'href="../style.css"' `
  -replace 'src="nav\.js"', 'src="../nav.js"' `
  -replace 'src="images/', 'src="../images/' `
  -replace 'href="images/', 'href="../images/' `
  -replace 'href="index\.html"', 'href="../"' `
  -replace 'href="custom-suits\.html"', 'href="../custom-suits/"' `
  -replace 'href="ready-to-wear-suits\.html"', 'href="../ready-to-wear-suits/"' `
  -replace 'href="handmade-shoes\.html"', 'href="../handmade-shoes/"' `
  -replace 'href="tuxedos\.html"', 'href="../tuxedos/"' `
  -replace 'href="wedding-dresses\.html"', 'href="../wedding-dresses/"' `
  -replace 'href="gallery\.html"', 'href="../gallery/"' `
  -replace 'href="about-us\.html"', 'href="../about-us/"' `
  -replace 'href="appointment-form\.html"', 'href="../appointment-form/"' `
  | Set-Content $file -Encoding UTF8
```

- [ ] **Step 3: Verify no .html hrefs remain**

```powershell
Select-String -Path "G:\coding\Claude POC Projects\gregory-duane\gallery\index.html" -Pattern 'href="[^"]*\.html"'
```

Expected: no output

- [ ] **Step 4: Delete original file and commit**

```powershell
cd "G:\coding\Claude POC Projects\gregory-duane"
git add gallery/index.html
git rm gallery.html
git commit -m "refactor: move gallery.html to gallery/index.html"
```

---

## Task 8: Move about-us.html → about-us/index.html

**Files:**
- Create: `about-us/index.html`
- Delete: `about-us.html`

- [ ] **Step 1: Create subdirectory and copy file**

```powershell
New-Item -ItemType Directory -Force "G:\coding\Claude POC Projects\gregory-duane\about-us"
Copy-Item "G:\coding\Claude POC Projects\gregory-duane\about-us.html" `
          "G:\coding\Claude POC Projects\gregory-duane\about-us\index.html"
```

- [ ] **Step 2: Apply asset and link replacements**

```powershell
$file = "G:\coding\Claude POC Projects\gregory-duane\about-us\index.html"
(Get-Content $file -Raw) `
  -replace 'href="style\.css"', 'href="../style.css"' `
  -replace 'src="nav\.js"', 'src="../nav.js"' `
  -replace 'src="images/', 'src="../images/' `
  -replace 'href="images/', 'href="../images/' `
  -replace 'href="index\.html"', 'href="../"' `
  -replace 'href="custom-suits\.html"', 'href="../custom-suits/"' `
  -replace 'href="ready-to-wear-suits\.html"', 'href="../ready-to-wear-suits/"' `
  -replace 'href="handmade-shoes\.html"', 'href="../handmade-shoes/"' `
  -replace 'href="tuxedos\.html"', 'href="../tuxedos/"' `
  -replace 'href="wedding-dresses\.html"', 'href="../wedding-dresses/"' `
  -replace 'href="gallery\.html"', 'href="../gallery/"' `
  -replace 'href="about-us\.html"', 'href="../about-us/"' `
  -replace 'href="appointment-form\.html"', 'href="../appointment-form/"' `
  | Set-Content $file -Encoding UTF8
```

- [ ] **Step 3: Verify no .html hrefs remain**

```powershell
Select-String -Path "G:\coding\Claude POC Projects\gregory-duane\about-us\index.html" -Pattern 'href="[^"]*\.html"'
```

Expected: no output

- [ ] **Step 4: Delete original file and commit**

```powershell
cd "G:\coding\Claude POC Projects\gregory-duane"
git add about-us/index.html
git rm about-us.html
git commit -m "refactor: move about-us.html to about-us/index.html"
```

---

## Task 9: Move appointment-form.html → appointment-form/index.html

**Files:**
- Create: `appointment-form/index.html`
- Delete: `appointment-form.html`

- [ ] **Step 1: Create subdirectory and copy file**

```powershell
New-Item -ItemType Directory -Force "G:\coding\Claude POC Projects\gregory-duane\appointment-form"
Copy-Item "G:\coding\Claude POC Projects\gregory-duane\appointment-form.html" `
          "G:\coding\Claude POC Projects\gregory-duane\appointment-form\index.html"
```

- [ ] **Step 2: Apply asset and link replacements**

```powershell
$file = "G:\coding\Claude POC Projects\gregory-duane\appointment-form\index.html"
(Get-Content $file -Raw) `
  -replace 'href="style\.css"', 'href="../style.css"' `
  -replace 'src="nav\.js"', 'src="../nav.js"' `
  -replace 'src="images/', 'src="../images/' `
  -replace 'href="images/', 'href="../images/' `
  -replace 'href="index\.html"', 'href="../"' `
  -replace 'href="custom-suits\.html"', 'href="../custom-suits/"' `
  -replace 'href="ready-to-wear-suits\.html"', 'href="../ready-to-wear-suits/"' `
  -replace 'href="handmade-shoes\.html"', 'href="../handmade-shoes/"' `
  -replace 'href="tuxedos\.html"', 'href="../tuxedos/"' `
  -replace 'href="wedding-dresses\.html"', 'href="../wedding-dresses/"' `
  -replace 'href="gallery\.html"', 'href="../gallery/"' `
  -replace 'href="about-us\.html"', 'href="../about-us/"' `
  -replace 'href="appointment-form\.html"', 'href="../appointment-form/"' `
  | Set-Content $file -Encoding UTF8
```

- [ ] **Step 3: Verify no .html hrefs remain**

```powershell
Select-String -Path "G:\coding\Claude POC Projects\gregory-duane\appointment-form\index.html" -Pattern 'href="[^"]*\.html"'
```

Expected: no output

- [ ] **Step 4: Delete original file and commit**

```powershell
cd "G:\coding\Claude POC Projects\gregory-duane"
git add appointment-form/index.html
git rm appointment-form.html
git commit -m "refactor: move appointment-form.html to appointment-form/index.html"
```

---

## Task 10: Verify all pages locally with Playwright

- [ ] **Step 1: Start local server (if not already running)**

```powershell
Start-Process powershell -ArgumentList '-NoProfile -Command "cd ''G:\coding\Claude POC Projects\gregory-duane''; python -m http.server 8090"' -WindowStyle Hidden
Start-Sleep 2
```

- [ ] **Step 2: Visit and screenshot each clean URL**

Use Playwright MCP (`browser_navigate` then `browser_take_screenshot`) for each URL. Confirm the page renders with correct styles, hero image, and navigation links.

| URL | Expected page title |
|---|---|
| `http://localhost:8090/` | Gregory Duane (home) |
| `http://localhost:8090/custom-suits/` | Bespoke Suits |
| `http://localhost:8090/ready-to-wear-suits/` | Ready to Wear |
| `http://localhost:8090/handmade-shoes/` | Handmade Shoes |
| `http://localhost:8090/tuxedos/` | Bespoke Tuxedos |
| `http://localhost:8090/wedding-dresses/` | Wedding Dresses |
| `http://localhost:8090/gallery/` | Gallery |
| `http://localhost:8090/about-us/` | About Us |
| `http://localhost:8090/appointment-form/` | Book a Consultation |

For each page check: CSS is loaded (page is styled), hero image is visible, nav links are present.

- [ ] **Step 3: Confirm no stale .html files remain in root**

```powershell
Get-ChildItem "G:\coding\Claude POC Projects\gregory-duane\*.html" | Select-Object Name
```

Expected — only these two files remain:
```
index.html
email-notification-template.html
```

---

## Task 11: Push to GitHub

- [ ] **Step 1: Confirm clean working tree**

```powershell
cd "G:\coding\Claude POC Projects\gregory-duane"
git status
```

Expected: `nothing to commit, working tree clean`

- [ ] **Step 2: Push**

```powershell
git push
```

GitHub Actions will trigger a Pages deployment. Pages will be live at clean URLs (e.g. `https://calvinadaniel.github.io/gregory-duane/tuxedos/`) within ~60 seconds.
