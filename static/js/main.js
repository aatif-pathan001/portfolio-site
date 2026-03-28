/**
 * Portfolio JS — Aatif Khan Pathan
 * Electric Green Particle Star-Field · Nav · Reveal · Filter · Form · CountUp
 */

'use strict';

// ═══════════════════════════════════════════════════════════════
// 1. PARTICLE ENGINE  ·  Star-field + neural network nodes
//    Colour identity: pure white micro-stars + green network nodes
// ═══════════════════════════════════════════════════════════════
class ParticleEngine {
  constructor(id) {
    this.canvas = document.getElementById(id);
    if (!this.canvas) return;
    this.ctx = this.canvas.getContext('2d');
    this.W = 0; this.H = 0;
    this.particles = [];
    this.mouse = { x: -9999, y: -9999 };
    this.raf = null;

    // Tuning
    this.cfg = {
      total:       160,
      starFrac:    0.78,      // proportion of tiny white stars vs green nodes
      nodeColor:   '57,255,20',
      starColor:   '255,255,255',
      connectDist: 100,
      mouseRepel:  140,
      baseSpeed:   0.22,
      lineAlpha:   0.13,
    };

    this._resize();
    this._init();
    this._bindEvents();
    this._loop();
  }

  _bindEvents() {
    window.addEventListener('resize', () => { this._resize(); this._init(); });
    window.addEventListener('mousemove', e => { this.mouse.x = e.clientX; this.mouse.y = e.clientY; });
    window.addEventListener('mouseleave', () => { this.mouse.x = -9999; this.mouse.y = -9999; });
  }

  _resize() {
    this.W = this.canvas.width  = window.innerWidth;
    this.H = this.canvas.height = window.innerHeight;
  }

  _init() {
    const { total, starFrac, baseSpeed } = this.cfg;
    this.particles = Array.from({ length: total }, () => {
      const isStar = Math.random() < starFrac;
      return {
        x:     Math.random() * this.W,
        y:     Math.random() * this.H,
        vx:    (Math.random() - 0.5) * baseSpeed,
        vy:    (Math.random() - 0.5) * baseSpeed,
        r:     isStar ? Math.random() * 0.9 + 0.2 : Math.random() * 1.6 + 0.6,
        alpha: Math.random() * 0.5 + 0.15,
        phase: Math.random() * Math.PI * 2,
        speed: Math.random() * 0.025 + 0.008,
        isStar,
      };
    });
  }

  _loop() {
    this._draw();
    this.raf = requestAnimationFrame(() => this._loop());
  }

  _draw() {
    const { ctx, W, H, particles, mouse, cfg } = this;
    ctx.clearRect(0, 0, W, H);

    const nodes = [];

    for (const p of particles) {
      // Move
      p.x += p.vx;  p.y += p.vy;
      p.phase += p.speed;

      // Wrap
      if (p.x < 0) p.x = W;  else if (p.x > W) p.x = 0;
      if (p.y < 0) p.y = H;  else if (p.y > H) p.y = 0;

      // Mouse repulsion for nodes
      if (!p.isStar) {
        const dx = p.x - mouse.x, dy = p.y - mouse.y;
        const d  = Math.hypot(dx, dy);
        if (d < cfg.mouseRepel && d > 0) {
          const f = ((cfg.mouseRepel - d) / cfg.mouseRepel) * 0.045;
          p.vx += (dx / d) * f;
          p.vy += (dy / d) * f;
          // Speed cap
          const spd = Math.hypot(p.vx, p.vy);
          if (spd > 2.5) { p.vx *= 2.5 / spd; p.vy *= 2.5 / spd; }
        }
        // Gentle friction
        p.vx *= 0.975;  p.vy *= 0.975;
        nodes.push(p);
      }

      // Twinkle
      const tw = 0.55 + 0.45 * Math.sin(p.phase);
      const a  = p.alpha * tw;
      const col = p.isStar ? cfg.starColor : cfg.nodeColor;

      // Draw particle
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(${col},${a})`;
      ctx.fill();

      // Soft glow for nodes
      if (!p.isStar) {
        const g = ctx.createRadialGradient(p.x, p.y, 0, p.x, p.y, p.r * 5);
        g.addColorStop(0, `rgba(${col},${a * 0.4})`);
        g.addColorStop(1, `rgba(${col},0)`);
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.r * 5, 0, Math.PI * 2);
        ctx.fillStyle = g;
        ctx.fill();
      }
    }

    // Connect nearby nodes
    for (let i = 0; i < nodes.length; i++) {
      for (let j = i + 1; j < nodes.length; j++) {
        const dx = nodes[i].x - nodes[j].x;
        const dy = nodes[i].y - nodes[j].y;
        const d  = Math.hypot(dx, dy);
        if (d < cfg.connectDist) {
          const a = cfg.lineAlpha * (1 - d / cfg.connectDist);
          ctx.beginPath();
          ctx.moveTo(nodes[i].x, nodes[i].y);
          ctx.lineTo(nodes[j].x, nodes[j].y);
          ctx.strokeStyle = `rgba(${cfg.nodeColor},${a})`;
          ctx.lineWidth   = 0.6;
          ctx.stroke();
        }
      }
    }
  }
}

// ═══════════════════════════════════════════════════════════════
// 2. NAVIGATION
// ═══════════════════════════════════════════════════════════════
class Nav {
  constructor() {
    this.el     = document.querySelector('.nav');
    this.burger = document.querySelector('.nav-hamburger');
    this.menu   = document.querySelector('.nav-links');
    if (!this.el) return;
    window.addEventListener('scroll', () => this._scroll(), { passive: true });
    this.burger?.addEventListener('click', () => this.menu.classList.toggle('open'));
    this.menu?.querySelectorAll('a').forEach(a =>
      a.addEventListener('click', () => this.menu.classList.remove('open')));
    this._scroll();
  }
  _scroll() {
    this.el.classList.toggle('scrolled', window.scrollY > 50);
  }
}

// ═══════════════════════════════════════════════════════════════
// 3. SCROLL REVEAL
// ═══════════════════════════════════════════════════════════════
class Revealer {
  constructor() {
    const io = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (!e.isIntersecting) return;
        const delay = +(e.target.dataset.delay || 0);
        setTimeout(() => e.target.classList.add('visible'), delay);
        io.unobserve(e.target);
      });
    }, { threshold: 0.10, rootMargin: '0px 0px -40px 0px' });

    document.querySelectorAll('.reveal').forEach(el => io.observe(el));

    document.querySelectorAll('.tl-item').forEach((el, i) => {
      el.dataset.delay = i * 140;
      io.observe(el);
    });

    document.querySelectorAll('.stack-cat').forEach((el, i) => {
      el.dataset.delay = i * 70;
      io.observe(el);
    });

    document.querySelectorAll('.proj-card').forEach((el, i) => {
      el.dataset.delay = i * 55;
      io.observe(el);
    });
  }
}

// ═══════════════════════════════════════════════════════════════
// 4. PROJECT FILTER
// ═══════════════════════════════════════════════════════════════
class Filter {
  constructor() {
    this.btns  = document.querySelectorAll('.filt-btn');
    this.cards = document.querySelectorAll('.proj-card');
    this.btns.forEach(b => b.addEventListener('click', () => {
      this.btns.forEach(x => x.classList.remove('active'));
      b.classList.add('active');
      const cat = b.dataset.filter;
      this.cards.forEach((c, i) => {
        const show = cat === 'all' || c.dataset.category === cat;
        if (show) {
          c.style.display = '';
          setTimeout(() => { c.style.opacity = '1'; c.style.transform = 'translateY(0)'; }, i * 38);
        } else {
          c.style.opacity = '0';
          c.style.transform = 'translateY(18px)';
          setTimeout(() => { c.style.display = 'none'; }, 280);
        }
      });
    }));
  }
}

// ═══════════════════════════════════════════════════════════════
// 5. STAT COUNT-UP
// ═══════════════════════════════════════════════════════════════
class CountUp {
  constructor() {
    const io = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (!e.isIntersecting) return;
        this._run(e.target);
        io.unobserve(e.target);
      });
    }, { threshold: 0.6 });
    document.querySelectorAll('.h-stat-val').forEach(el => io.observe(el));
  }

  _run(el) {
    const raw   = el.textContent.trim();
    const match = raw.match(/[\d.]+/);
    if (!match) return;
    const target = parseFloat(match[0]);
    const suffix = raw.slice(match.index + match[0].length);
    const prefix = raw.slice(0, match.index);
    const decimals = match[0].includes('.') ? match[0].split('.')[1].length : 0;
    const dur  = 1600;
    const t0   = performance.now();

    const tick = (now) => {
      const prog  = Math.min((now - t0) / dur, 1);
      const eased = 1 - Math.pow(1 - prog, 3);
      el.textContent = prefix + (target * eased).toFixed(decimals) + suffix;
      if (prog < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  }
}

// ═══════════════════════════════════════════════════════════════
// 6. CONTACT FORM
// ═══════════════════════════════════════════════════════════════
class ContactForm {
  constructor() {
    this.form = document.getElementById('contact-form');
    this.msg  = document.getElementById('form-message');
    this.form?.addEventListener('submit', e => this._submit(e));
  }

  async _submit(e) {
    e.preventDefault();
    const btn = this.form.querySelector('.form-submit');
    const orig = btn.textContent;
    btn.textContent = 'Sending…';
    btn.disabled = true;

    const body = {
      name:    this.form.querySelector('[name="name"]').value.trim(),
      email:   this.form.querySelector('[name="email"]').value.trim(),
      subject: this.form.querySelector('[name="subject"]').value.trim(),
      message: this.form.querySelector('[name="message"]').value.trim(),
    };

    try {
      const res  = await fetch('/api/contact', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body),
      });
      const json = await res.json();
      this._flash(res.ok ? json.message : (json.detail || 'Something went wrong.'), res.ok ? 'success' : 'error');
      if (res.ok) this.form.reset();
    } catch {
      this._flash('Network error — please email me directly.', 'error');
    } finally {
      btn.textContent = orig;
      btn.disabled = false;
    }
  }

  _flash(text, type) {
    this.msg.textContent = text;
    this.msg.className = `form-message ${type}`;
    setTimeout(() => { this.msg.className = 'form-message'; }, 6000);
  }
}

// ═══════════════════════════════════════════════════════════════
// 7. INIT
// ═══════════════════════════════════════════════════════════════
document.addEventListener('DOMContentLoaded', () => {
  new ParticleEngine('particle-canvas');
  new Nav();
  new Revealer();
  new Filter();
  new CountUp();
  new ContactForm();
});
