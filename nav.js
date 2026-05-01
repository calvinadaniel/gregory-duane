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
