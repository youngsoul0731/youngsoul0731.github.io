// Navigation enhancements. All homepage content remains available without JavaScript.
const menu = document.querySelector('.menu-toggle');
const navLinks = document.querySelector('#nav-links');

if (menu && navLinks) {
  document.documentElement.classList.add('js');
  const closeMenu = () => menu.setAttribute('aria-expanded', 'false');
  menu.addEventListener('click', () => {
    menu.setAttribute('aria-expanded', String(menu.getAttribute('aria-expanded') !== 'true'));
  });
  navLinks.addEventListener('click', (event) => {
    if (event.target.closest('a')) closeMenu();
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && menu.getAttribute('aria-expanded') === 'true') {
      closeMenu();
      menu.focus();
    }
  });
}

// Hero background starts below the fixed nav; keep --nav-h in sync with the real nav height (collapsed state only).
const nav = document.querySelector('nav');
function updateNavHeight() {
  if (!nav || (menu && menu.getAttribute('aria-expanded') === 'true')) return;
  document.documentElement.style.setProperty('--nav-h', `${nav.offsetHeight}px`);
}
window.addEventListener('resize', updateNavHeight);
window.addEventListener('load', updateNavHeight);
updateNavHeight();

const links = [...document.querySelectorAll('#nav-links a')];
const sections = links.map(link => document.querySelector(link.getAttribute('href')));
const progress = document.querySelector('.scroll-progress');
let scheduled = false;

function updateNavigation() {
  const scrollRange = document.documentElement.scrollHeight - window.innerHeight;
  if (progress) progress.style.transform = `scaleX(${scrollRange > 0 ? Math.min(1, Math.max(0, window.scrollY / scrollRange)) : 0})`;
  let active = null;
  sections.forEach((section, index) => {
    if (section && section.getBoundingClientRect().top <= 150) active = links[index];
  });
  if (scrollRange > 0 && window.scrollY >= scrollRange - 2) active = links[links.length - 1];
  links.forEach(link => {
    link.classList.toggle('active', link === active);
    if (link === active) link.setAttribute('aria-current', 'location');
    else link.removeAttribute('aria-current');
  });
  scheduled = false;
}

function scheduleUpdate() {
  if (!scheduled) {
    scheduled = true;
    window.requestAnimationFrame(updateNavigation);
  }
}
window.addEventListener('scroll', scheduleUpdate, { passive: true });
window.addEventListener('resize', scheduleUpdate);
window.addEventListener('load', scheduleUpdate);
updateNavigation();
