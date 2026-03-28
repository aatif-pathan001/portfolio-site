"""
Components — HTML Builder
=========================
Each function returns an HTML string for a portfolio section.
Design: Charcoal/Black + Electric Green (#39FF14),
        Bold uppercase Barlow Condensed headings,
        High-contrast white body copy.
"""

from data.portfolio_data import PERSONAL, STATS, TECH_STACK, EXPERIENCE, PROJECTS

# ── SVG icon library ───────────────────────────────────────────────────────────
I = {
    "github":   '<svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>',
    "ext":      '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>',
    "mail":     '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="M22 7l-10 7L2 7"/></svg>',
    "linkedin": '<svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>',
    "blog":     '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M11 4H4a2 2 0 00-2 2v14a2 2 0 002 2h14a2 2 0 002-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 013 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>',
    "location": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>',
    "download": '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>',
    "arrow":    '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>',
    "phone":    '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 9.81 19.79 19.79 0 01.01 1.19 2 2 0 012 0h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L6.91 7.91a16 16 0 006.18 6.18l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 14.92z"/></svg>',
}


# ── NAV ────────────────────────────────────────────────────────────────────────
def render_nav() -> str:
    nav_items = [
        ("About",    "#hero"),
        ("Journey",  "#journey"),
        ("Stack",    "#stack"),
        ("Projects", "#projects"),
        ("Contact",  "#contact"),
    ]
    items = "".join(
        f'<li><a href="{href}">{label}</a></li>' for label, href in nav_items
    )
    return f"""
<nav class="nav" id="main-nav">
  <a class="nav-brand" href="#hero">AK<span class="accent">.</span>ML</a>
  <ul class="nav-links" id="nav-menu">
    {items}
    <li><a href="{PERSONAL['blog']}" class="nav-hire" target="_blank" rel="noopener">Hire Me</a></li>
  </ul>
  <div class="nav-hamburger" id="hamburger">
    <span></span><span></span><span></span>
  </div>
</nav>"""


# ── HERO ───────────────────────────────────────────────────────────────────────
def render_hero() -> str:
    stats = "".join(f"""
    <div class="h-stat">
      <span class="h-stat-val">{s['value']}</span>
      <span class="h-stat-lbl">{s['label']}</span>
    </div>""" for s in STATS)

    return f"""
<section id="hero">
  <div class="hero-status">
    <span class="status-dot"></span>
    {PERSONAL['status']}
  </div>

  <div class="hero-label">{PERSONAL['name']}</div>

  <div class="hero-h1">Building the</div>
  <div class="hero-h1">Intelligence</div>
  <div class="hero-h1-ghost">of Tomorrow.</div>

  <p class="hero-desc">
    <strong>ML Engineer @ TCS</strong> · Electrical Engineering foundations,
    deep AI/ML specialisation.<br>
    Expert in <strong>PyTorch</strong>, <strong>YOLO</strong>, <strong>BERT</strong>,
    <strong>LangChain</strong> and production <strong>MLOps</strong> on GCP.
  </p>

  <div class="hero-ctas">
    <a href="#projects" class="btn btn-green">
      {I['arrow']}&nbsp; View Projects
    </a>
    <a href="{PERSONAL['resume_url']}" download class="btn btn-ghost">
      {I['download']}&nbsp; Resume
    </a>
  </div>

  <div class="hero-stats">{stats}</div>
</section>"""


# ── JOURNEY ────────────────────────────────────────────────────────────────────
def render_journey() -> str:
    badge_map = {
        "current":   ("live",  "● Live"),
        "past":      ("past",  "Past"),
        "education": ("edu",   "Education"),
    }

    items_html = ""
    for idx, exp in enumerate(EXPERIENCE):
        badge_cls, badge_label = badge_map.get(exp["status"], ("past", "Past"))
        side = "left" if idx % 2 == 0 else "right"
        is_current = "current" if exp["status"] == "current" else ""
        highlights = "".join(f"<li>{h}</li>" for h in exp["highlights"])

        items_html += f"""
    <div class="tl-item {side} {is_current}">
      <div class="tl-node"></div>
      <div class="tl-content">
        <div class="tl-period">{exp['period']}</div>
        <span class="tl-badge {badge_cls}">{badge_label}</span>
        <div class="tl-role">{exp['role']}</div>
        <div class="tl-company">{exp['company']} · {exp['location']}</div>
        <ul class="tl-list">{highlights}</ul>
      </div>
    </div>
    {'<div class="tl-spine"></div>' if idx == 0 else ''}"""

    return f"""
<section id="journey">
  <div class="section-wrap">
    <div class="reveal">
      <div class="eyebrow">Career Roadmap</div>
      <h2 class="section-title">The Journey</h2>
      <p class="section-sub">From Electrical Engineering to production AI/ML systems at scale.</p>
    </div>
    <div class="timeline-two-col">
      {items_html}
    </div>
  </div>
</section>"""


# ── TECH STACK ─────────────────────────────────────────────────────────────────
def render_stack() -> str:
    cats = ""
    for name, techs in TECH_STACK.items():
        tags = "".join(f'<span class="stack-tag">{t}</span>' for t in techs)
        cats += f"""
    <div class="stack-cat">
      <div class="stack-cat-name">{name}</div>
      <div class="stack-tags">{tags}</div>
    </div>"""

    return f"""
<section id="stack">
  <div class="section-wrap">
    <div class="reveal">
      <div class="eyebrow">Tools of the Trade</div>
      <h2 class="section-title">Tech Stack</h2>
      <p class="section-sub">Every layer from raw data to deployed model.</p>
    </div>
    <div class="stack-grid">{cats}</div>
  </div>
</section>"""


# ── PROJECTS ───────────────────────────────────────────────────────────────────
def render_projects() -> str:
    categories = sorted(set(p["category"] for p in PROJECTS))

    filter_html = '<button class="filt-btn active" data-filter="all">All</button>'
    filter_html += "".join(
        f'<button class="filt-btn" data-filter="{c}">{c}</button>'
        for c in categories
    )

    cards = ""
    for p in PROJECTS:
        tags    = "".join(f'<span class="proj-tag">{t}</span>' for t in p["tags"])
        metrics = "".join(f'<span class="proj-metric">{m}</span>' for m in p["metrics"])
        star    = '<span class="proj-star">Featured</span>' if p["featured"] else ""
        cls     = "proj-card featured" if p["featured"] else "proj-card"
        cards += f"""
    <div class="{cls}" data-category="{p['category']}">
      <div class="proj-head">
        <span class="proj-cat">{p['category']}</span>
        {star}
      </div>
      <div class="proj-title">{p['title']}</div>
      <p class="proj-desc">{p['description']}</p>
      <div class="proj-metrics">{metrics}</div>
      <div class="proj-tags">{tags}</div>
      <div class="proj-actions">
        <a href="{p['github']}" class="proj-btn" target="_blank">
          {I['github']} GitHub
        </a>
        <a href="{p['demo']}" class="proj-btn" target="_blank">
          {I['ext']} Demo
        </a>
      </div>
    </div>"""

    return f"""
<section id="projects">
  <div class="section-wrap">
    <div class="reveal">
      <div class="eyebrow">Portfolio</div>
      <h2 class="section-title">Projects</h2>
      <p class="section-sub">10 production ML systems — each with real benchmarks and deployed infrastructure.</p>
    </div>
    <div class="filter-row">{filter_html}</div>
    <div class="projects-grid">{cards}</div>
  </div>
</section>"""


# ── CONTACT ────────────────────────────────────────────────────────────────────
def render_contact() -> str:
    rows = [
        (I["mail"],     PERSONAL["email"],              f'mailto:{PERSONAL["email"]}'),
        (I["linkedin"], "linkedin.com/in/aatif-khan-pathan", PERSONAL["linkedin"]),
        (I["github"],   "github.com/aatifkhan",          PERSONAL["github"]),
        (I["blog"],     "Blog & Articles",               PERSONAL["blog"]),
        (I["location"], PERSONAL["location"],            "#"),
    ]

    rows_html = "".join(f"""
    <a href="{url}" class="c-row" target="_blank" rel="noopener">
      <span class="c-icon">{icon}</span>
      <span class="c-text">{label}</span>
    </a>""" for icon, label, url in rows)

    return f"""
<section id="contact">
  <div class="section-wrap">
    <div class="reveal">
      <div class="eyebrow">Get In Touch</div>
      <h2 class="section-title">Let's Build<br><span class="g">Something</span><br>Intelligent.</h2>
    </div>
    <div class="contact-grid">

      <div class="reveal">
        <h3>Open to<br><span class="g">Senior ML / AI</span><br>Opportunities.</h3>
        <p>Looking for ML Engineering roles, research collaborations, and freelance model-building engagements. I read every message.</p>
        <div class="contact-rows">{rows_html}</div>
      </div>

      <div class="reveal">
        <form class="contact-form" id="contact-form" novalidate>
          <div class="form-group">
            <label class="form-label" for="f-name">Name</label>
            <input class="form-input" type="text" id="f-name" name="name" placeholder="Your name" required>
          </div>
          <div class="form-group">
            <label class="form-label" for="f-email">Email</label>
            <input class="form-input" type="email" id="f-email" name="email" placeholder="your@email.com" required>
          </div>
          <div class="form-group">
            <label class="form-label" for="f-subj">Subject</label>
            <input class="form-input" type="text" id="f-subj" name="subject" placeholder="What's this about?">
          </div>
          <div class="form-group">
            <label class="form-label" for="f-msg">Message</label>
            <textarea class="form-textarea" id="f-msg" name="message"
              placeholder="Tell me about the role or project…" required></textarea>
          </div>
          <button type="submit" class="btn btn-green form-submit">
            {I['arrow']}&nbsp; Send Message
          </button>
          <div class="form-message" id="form-message"></div>
        </form>
      </div>

    </div>
  </div>
</section>"""


# ── FOOTER ─────────────────────────────────────────────────────────────────────
def render_footer() -> str:
    return f"""
<footer>
  <div class="footer-copy">
    © 2025 <span class="g">{PERSONAL['name']}</span> · Built with Python &amp; Flask
  </div>
  <div class="footer-links">
    <a href="{PERSONAL['github']}"   target="_blank">GitHub</a>
    <a href="{PERSONAL['linkedin']}" target="_blank">LinkedIn</a>
    <a href="{PERSONAL['blog']}"     target="_blank">Blog</a>
    <a href="{PERSONAL['resume_url']}" download>Resume</a>
  </div>
</footer>"""


# ── FULL PAGE ──────────────────────────────────────────────────────────────────
def render_page() -> str:
    """Assemble and return the complete single-page HTML."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description"
    content="{PERSONAL['name']} — {PERSONAL['title']}. {PERSONAL['summary'][:155]}">
  <meta name="author" content="{PERSONAL['name']}">
  <meta property="og:title"       content="{PERSONAL['name']} | ML Engineer Portfolio">
  <meta property="og:description" content="{PERSONAL['tagline']}">
  <meta property="og:type"        content="website">
  <title>{PERSONAL['name']} · ML Engineer</title>
  <link rel="stylesheet" href="/static/css/style.css">
  <!-- Favicon: lightning bolt emoji -->
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>⚡</text></svg>">
</head>
<body>

<!-- ── Background ────────────────────────── -->
<canvas id="particle-canvas"></canvas>
<div class="vignette"></div>

<div class="page-wrapper">

  {render_nav()}

  <main>
    {render_hero()}
    <hr class="h-rule">
    {render_journey()}
    <hr class="h-rule">
    {render_stack()}
    <hr class="h-rule">
    {render_projects()}
    <hr class="h-rule">
    {render_contact()}
  </main>

  {render_footer()}

</div><!-- /page-wrapper -->

<script src="/static/js/main.js" defer></script>
</body>
</html>"""
