import os

pages = [
    'custom-suits.html', 'ready-to-wear-suits.html',
    'about-us.html', 'handmade-shoes.html', 'tuxedos.html',
    'wedding-dresses.html', 'gallery.html', 'appointment-form.html'
]

OLD_NAV_LEFT = '''      <div class="nav-left">
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
      </div>'''

NEW_NAV_LEFT = '''      <div class="nav-left">
        <button class="nav-trigger" data-panel="mega-men" aria-expanded="false" aria-controls="mega-men">
          Men <span class="nav-chevron" aria-hidden="true">&#9662;</span>
        </button>
        <button class="nav-trigger" data-panel="mega-women" aria-expanded="false" aria-controls="mega-women">
          Women <span class="nav-chevron" aria-hidden="true">&#9662;</span>
        </button>
      </div>'''

MEGA_PANELS = '''
    <!-- Men Mega Panel -->
    <div class="mega-panel" id="mega-men" aria-hidden="true">
      <button class="mega-close" aria-label="Close men\'s menu">&#215;</button>
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

    <!-- Women Mega Panel -->
    <div class="mega-panel" id="mega-women" aria-hidden="true">
      <button class="mega-close" aria-label="Close women\'s menu">&#215;</button>
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

    <div class="mobile-menu" aria-hidden="true">'''

OLD_MOBILE_COMMENT = '    <div class="mobile-menu" aria-hidden="true">'

OLD_MOBILE_WOMEN = '''      <div class="has-dropdown">
        <a href="#">Women</a>
        <ul class="dropdown-menu">
          <li><a href="wedding-dresses.html">Wedding Dresses</a></li>
        </ul>
      </div>'''

NEW_MOBILE_WOMEN = '''      <div class="has-dropdown">
        <a href="#">Women</a>
        <ul class="dropdown-menu">
          <li><a href="wedding-dresses.html">Wedding Dresses</a></li>
          <li><a href="#">Bridal Alterations</a></li>
          <li><a href="#">Bridal Accessories</a></li>
          <li><a href="#">Mother of the Bride</a></li>
          <li><a href="#">Ready to Wear Suits</a></li>
        </ul>
      </div>'''

for page in pages:
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()

    assert OLD_NAV_LEFT in content, f"nav-left pattern not found in {page}"
    assert OLD_MOBILE_COMMENT in content, f"mobile comment not found in {page}"
    assert OLD_MOBILE_WOMEN in content, f"mobile women pattern not found in {page}"

    content = content.replace(OLD_NAV_LEFT, NEW_NAV_LEFT)
    content = content.replace(OLD_MOBILE_COMMENT, MEGA_PANELS)
    content = content.replace(OLD_MOBILE_WOMEN, NEW_MOBILE_WOMEN)

    with open(page, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"OK {page}")

print("Done.")
