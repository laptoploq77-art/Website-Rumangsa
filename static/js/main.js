// --- Mobile nav toggle ---
const navToggle = document.getElementById('navToggle');
const navLinks = document.getElementById('navLinks');
if (navToggle) {
  navToggle.addEventListener('click', () => navLinks.classList.toggle('open'));
}

// --- Scroll reveal ---
const revealEls = document.querySelectorAll('.reveal');
const io = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('in');
      io.unobserve(e.target);
    }
  });
}, { threshold: 0.12 });
revealEls.forEach(el => io.observe(el));

// --- Background audio toggle ---
const audio = document.getElementById('bgAudio');
const soundBtn = document.getElementById('soundToggle');
let playing = false;

function setIcon() {
  soundBtn.innerHTML = playing ? '&#9835;' : '&#9835;';
  soundBtn.classList.toggle('muted', !playing);
  soundBtn.title = playing ? 'Matikan musik latar' : 'Nyalakan musik latar';
}

if (soundBtn && audio) {
  soundBtn.addEventListener('click', () => {
    if (playing) {
      audio.pause();
      playing = false;
    } else {
      audio.volume = 0.35;
      audio.play().catch(() => {});
      playing = true;
    }
    setIcon();
  });
  setIcon();
}

// --- Highlight target saat dituju via anchor dari Daftar Menu ---
// Mendukung #foto-... di halaman Foto Menu, dan #desc-... di halaman Deskripsi Menu.
function highlightTargetAnchor() {
  const hash = location.hash;
  if (!hash.startsWith('#foto-') && !hash.startsWith('#desc-')) return;

  const target = document.querySelector(hash);
  if (!target) return;
  if (!target.classList.contains('photo-menu-card') && !target.classList.contains('desc-item')) return;

  // Pastikan kartu/parent kategori sudah terlihat (skip animasi reveal fade)
  target.classList.add('in');
  const parentReveal = target.closest('.reveal');
  if (parentReveal) parentReveal.classList.add('in');

  setTimeout(() => {
    target.scrollIntoView({ behavior: 'smooth', block: 'center' });
    target.classList.add('highlight');
    setTimeout(() => target.classList.remove('highlight'), 3600);
  }, 60);
}

window.addEventListener('DOMContentLoaded', highlightTargetAnchor);
window.addEventListener('hashchange', highlightTargetAnchor);
