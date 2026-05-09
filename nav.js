/* Gregory Duane — nav.js */

const nav = document.querySelector('.site-nav');
const mobileMenu = document.querySelector('.mobile-menu');
const menuToggle = document.querySelector('.menu-toggle');

// Transparent → solid nav on scroll
if (nav) {
  window.addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', window.scrollY > 110);
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
