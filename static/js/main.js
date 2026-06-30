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
