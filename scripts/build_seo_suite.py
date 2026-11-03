#!/usr/bin/env python3
"""
Suleiman IELTS SEO Suite Generator
Architect-grade Search Engine Optimization across all URLs, paths, and HTML documents.
"""

import os
import json
import html

BASE_DIR = "/Users/macbookairm2/Documents/GitHub/suleimanielts.github.io"
DATA_DIR = os.path.join(BASE_DIR, "data")

with open(os.path.join(DATA_DIR, "cambridge_tests.json"), "r", encoding="utf-8") as f:
    cambridge_data = json.load(f)

with open(os.path.join(DATA_DIR, "stories_500_words.json"), "r", encoding="utf-8") as f:
    stories_data = json.load(f)

with open(os.path.join(DATA_DIR, "vocabulary_vault.json"), "r", encoding="utf-8") as f:
    vocab_data = json.load(f)

with open(os.path.join(DATA_DIR, "writing_templates.json"), "r", encoding="utf-8") as f:
    writing_data = json.load(f)

with open(os.path.join(DATA_DIR, "study_plan.json"), "r", encoding="utf-8") as f:
    study_plan_data = json.load(f)

# Common Header HTML
def get_header_html(active_route=""):
    routes = [
        ("/", "Dashboard", "view-dashboard", active_route == "dashboard"),
        ("/speaking/", "Speaking Suite", "view-speaking", active_route == "speaking"),
        ("/tests/", "Cambridge Tests", "view-tests", active_route == "tests"),
        ("/vault/", "Lexical Vault C1/C2", "view-vault", active_route == "vault"),
        ("/writing/", "Writing Blueprints", "view-writing", active_route == "writing"),
        ("/stories/", "500 Söz (25 Hekayə)", "view-stories", active_route == "stories"),
        ("/about/", "Haqqımızda & Access", "view-about", active_route == "about")
    ]
    
    nav_links = ""
    for url, label, tab_id, is_active in routes:
        active_cls = " active" if is_active else ""
        nav_links += f'<a href="{url}" class="tab-btn{active_cls}" style="text-decoration: none; display: inline-flex; align-items: center; gap: 0.4rem;"><span>{label}</span></a>\n'

    return f"""  <!-- Top Sticky Glass Header -->
  <header class="site-header">
    <div class="app-container">
      <div class="header-inner">
        <a href="/" class="brand-wrapper" style="text-decoration: none; color: inherit;">
          <img src="/assets/ielts_logo_avatar_square.png" alt="Suleiman IELTS Logo" style="width: 38px; height: 38px; border-radius: 8px; object-fit: contain; background: #ffffff; padding: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.2);" />
          <div>
            <h1 class="brand-title">Suleiman IELTS</h1>
            <span class="brand-subtitle">Distraction-Free Academic Study Platform</span>
          </div>
        </a>

        <div class="header-actions">
          <span class="target-badge">🎯 Band 8.0+ Target</span>

          <a href="mailto:suleyman.hacizade1@gmail.com?subject=Access%20Request%20-%20SuleimanIELTS%20Private%20Data" class="action-btn" title="Məxfi Baza Giriş Müraciəti (Private Data Access Request)" style="text-decoration: none; display: inline-flex; align-items: center; gap: 0.35rem; font-size: 0.82rem; font-weight: 600; background: rgba(220, 38, 38, 0.1); border: 1px solid rgba(220, 38, 38, 0.35); color: #ef4444;">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
              <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
            </svg>
            <span>🔒 Access Request</span>
          </a>

          <a href="/" class="action-btn" title="Ana Portal &amp; Tam İnteraktiv Rejim" style="text-decoration: none;">
            <span>🚀 Full App</span>
          </a>
        </div>
      </div>

      <!-- Navigation Bar -->
      <nav class="nav-tabs" style="overflow-x: auto; white-space: nowrap;">
{nav_links}      </nav>
    </div>
  </header>"""

# Common Footer HTML
def get_footer_html():
    return """  <!-- Clean Production Footer -->
  <footer style="margin-top: 4rem; border-top: 1px solid var(--border-medium); padding: 2.5rem 0; background: var(--bg-surface);">
    <div class="app-container">
      <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1.5rem; margin-bottom: 1.5rem;">
        <div>
          <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
            <img src="/assets/ielts_logo_avatar_square.png" alt="Suleiman IELTS" style="width: 28px; height: 28px; border-radius: 6px; background: #fff; padding: 1px;" />
            <strong style="font-size: 1.1rem; color: var(--text-primary);">Suleiman IELTS</strong>
          </div>
          <p style="color: var(--text-secondary); font-size: 0.88rem; max-width: 580px; margin: 0;">
            Minimalist, distraction-free IELTS Academic companion for Engnovate &amp; Cambridge IELTS (15–21). 
            Engineered for high-performing candidates targeting Band 8.0, 8.5, and 9.0.
          </p>
        </div>
        <div style="display: flex; flex-direction: column; gap: 0.5rem; text-align: right;">
          <a href="/speaking/" style="color: var(--text-secondary); text-decoration: none; font-size: 0.88rem;">🎙️ Speaking Practice Suite</a>
          <a href="/tests/" style="color: var(--text-secondary); text-decoration: none; font-size: 0.88rem;">📚 Cambridge Tests Directory</a>
          <a href="/vault/" style="color: var(--text-secondary); text-decoration: none; font-size: 0.88rem;">💎 C1/C2 Lexical Vault</a>
          <a href="/writing/" style="color: var(--text-secondary); text-decoration: none; font-size: 0.88rem;">✍️ Writing Blueprints</a>
          <a href="/stories/" style="color: var(--text-secondary); text-decoration: none; font-size: 0.88rem;">📖 500 Söz (25 Hekayə)</a>
          <a href="/about/" style="color: var(--text-secondary); text-decoration: none; font-size: 0.88rem;">ℹ️ Haqqımızda &amp; Access</a>
        </div>
      </div>

      <div style="border-top: 1px solid var(--border-light); padding-top: 1.25rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; font-size: 0.82rem; color: var(--text-muted);">
        <div>
          🔒 <strong>Məxfi Məlumat Bazası (Private Data):</strong> Bütün xam sənədlər və 62-səhifəlik Obsidian LLM Wiki bazası məxfidir. Giriş üçün: <a href="mailto:suleyman.hacizade1@gmail.com?subject=Access%20Request%20-%20SuleimanIELTS%20Private%20Data" style="color: #ef4444; font-weight: 600;">suleyman.hacizade1@gmail.com</a>
        </div>
        <div>
          <span>Qurucu: <strong>Süleyman Hacızadə (Suleiman Hajizadeh)</strong></span> • 
          <a href="https://github.com/SuleimanIELTS" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: underline;">GitHub Organization</a>
        </div>
      </div>
    </div>
  </footer>"""

# Common HTML Shell
def build_html_page(title, description, canonical_url, keywords, active_route, body_content, json_ld_graph, og_image="/assets/ielts_logo_badge_square.png"):
    return f"""<!DOCTYPE html>
<html lang="az" data-theme="dark" prefix="og: http://ogp.me/ns#">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  
  <!-- Primary SEO Meta Tags -->
  <title>{title}</title>
  <meta name="title" content="{title}" />
  <meta name="description" content="{description}" />
  <meta name="keywords" content="{keywords}" />
  <meta name="author" content="Suleiman Hajizadeh" />
  <link rel="canonical" href="{canonical_url}" />

  <!-- Crawling & Search Engine Directives -->
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1" />
  <meta name="googlebot" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1" />
  <meta name="bingbot" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1" />
  <meta name="yandex" content="index, follow" />
  <meta name="baiduspider" content="index, follow" />
  <meta name="duckduckbot" content="index, follow" />

  <!-- Alternate Language Tags -->
  <link rel="alternate" hreflang="az" href="{canonical_url}" />
  <link rel="alternate" hreflang="en" href="{canonical_url}" />
  <link rel="alternate" hreflang="x-default" href="{canonical_url}" />

  <!-- Geographic & Locale Metadata -->
  <meta name="geo.region" content="AZ" />
  <meta name="geo.placename" content="Baku" />
  <meta name="geo.position" content="40.4093;49.8671" />
  <meta name="ICBM" content="40.4093, 49.8671" />
  <meta name="language" content="Azerbaijani, English" />

  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="Suleiman IELTS" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:url" content="{canonical_url}" />
  <meta property="og:image" content="https://suleimanielts.github.io{og_image}" />
  <meta property="og:image:secure_url" content="https://suleimanielts.github.io{og_image}" />
  <meta property="og:image:width" content="1000" />
  <meta property="og:image:height" content="1000" />
  <meta property="og:image:alt" content="Suleiman IELTS Emblem" />
  <meta property="og:locale" content="az_AZ" />
  <meta property="og:locale:alternate" content="en_US" />

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:site" content="@SuleimanHajizadeh" />
  <meta name="twitter:creator" content="@SuleimanHajizadeh" />
  <meta name="twitter:title" content="{title}" />
  <meta name="twitter:description" content="{description}" />
  <meta name="twitter:image" content="https://suleimanielts.github.io{og_image}" />

  <!-- Icons & Web App Manifest -->
  <link rel="icon" type="image/png" sizes="64x64" href="/favicon.png" />
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" />
  <link rel="manifest" href="/manifest.json" />
  <meta name="theme-color" content="#dc2626" />
  <meta name="apple-mobile-web-app-capable" content="yes" />
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
  <meta name="apple-mobile-web-app-title" content="SuleimanIELTS" />

  <!-- Stylesheet -->
  <link rel="stylesheet" href="/css/style.css" />

  <!-- JSON-LD Structured Data Schema -->
  <script type="application/ld+json">
{json.dumps(json_ld_graph, indent=2, ensure_ascii=False)}
  </script>
</head>
<body>
{get_header_html(active_route)}

  <main class="app-container" style="padding-top: 2rem; padding-bottom: 2rem;">
{body_content}
  </main>

{get_footer_html()}

  <!-- Theme and interactive handler -->
  <script>
    const savedTheme = localStorage.getItem("suleiman_ielts_theme") || "dark";
    document.documentElement.setAttribute("data-theme", savedTheme);
  </script>
</body>
</html>"""

# Generate 1. Speaking Suite (/speaking/)
def generate_speaking_page():
    os.makedirs(os.path.join(BASE_DIR, "speaking"), exist_ok=True)
    
    # Extract questions from Cambridge 21 speaking test 3
    test = next((t for t in cambridge_data.get("tests", []) if t["id"] == "cambridge-21-speaking-3"), None)
    
    p1_html = ""
    if test:
        for q in test["parts"]["part_1"]["questions"]:
            vocab_badges = "".join([f'<span class="badge" style="background: rgba(37,99,235,0.12); color: #3b82f6; border: 1px solid rgba(37,99,235,0.3); font-size: 0.78rem; padding: 0.2rem 0.5rem; border-radius: 4px; margin-right: 0.4rem; display: inline-block; margin-bottom: 0.3rem;"><strong>{html.escape(v["word"])}</strong>: {html.escape(v["translation"])}</span>' for v in q.get("key_vocab", [])])
            p1_html += f"""
        <div class="card" style="margin-bottom: 1.5rem; padding: 1.5rem; background: var(--bg-surface); border: 1px solid var(--border-medium); border-radius: 12px;">
          <h3 style="font-size: 1.05rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.75rem;">Q{q["number"]}. {html.escape(q["question"])}</h3>
          <div style="background: var(--bg-subtle); padding: 1rem; border-left: 4px solid #10b981; border-radius: 4px; margin-bottom: 0.75rem;">
            <div style="font-size: 0.78rem; font-weight: 700; color: #10b981; text-transform: uppercase; margin-bottom: 0.25rem;">Band 8.5 Model Answer</div>
            <p style="margin: 0; line-height: 1.6; font-size: 0.95rem; color: var(--text-primary);">{html.escape(q["model_answer_band_8"])}</p>
          </div>
          <div style="background: var(--bg-subtle); padding: 0.85rem; border-left: 4px solid #3b82f6; border-radius: 4px; margin-bottom: 0.75rem;">
            <div style="font-size: 0.78rem; font-weight: 700; color: #3b82f6; text-transform: uppercase; margin-bottom: 0.25rem;">Azərbaycan dilində Tərcümə</div>
            <p style="margin: 0; line-height: 1.5; font-size: 0.9rem; color: var(--text-secondary);">{html.escape(q["translation_az"])}</p>
          </div>
          <div style="margin-top: 0.5rem;">
            <span style="font-size: 0.8rem; font-weight: 600; color: var(--text-muted); display: block; margin-bottom: 0.35rem;">Açar Sözlər &amp; Kollokasiyalar:</span>
            {vocab_badges}
          </div>
        </div>"""

    body = f"""    <!-- Breadcrumb navigation -->
    <nav aria-label="Breadcrumb" style="margin-bottom: 1.5rem; font-size: 0.85rem; color: var(--text-muted);">
      <a href="/" style="color: inherit; text-decoration: none;">Ana Səhifə</a> &rsaquo; 
      <span style="color: var(--text-primary); font-weight: 600;">Speaking Practice Suite</span>
    </nav>

    <div class="hero-banner" style="background: linear-gradient(135deg, rgba(220, 38, 38, 0.15), rgba(37, 99, 235, 0.15)); border: 1px solid var(--border-medium); border-radius: 16px; padding: 2rem; margin-bottom: 2rem;">
      <span class="module-badge" style="background: #dc2626; color: #fff; padding: 0.25rem 0.65rem; border-radius: 6px; font-size: 0.8rem; font-weight: 700; display: inline-block; margin-bottom: 0.75rem;">IELTS Academic Speaking Suite</span>
      <h1 style="font-size: 1.85rem; font-weight: 800; margin-bottom: 0.75rem;">IELTS Speaking Practice Suite &amp; In-Browser Simulator</h1>
      <p style="color: var(--text-secondary); font-size: 1rem; max-width: 780px; line-height: 1.6; margin-bottom: 1.25rem;">
        Cambridge 15–21 imtahan sualları, 1 dəqiqəlik hazırlıq və 2 dəqiqəlik danışıq taymerləri, brauzerdaxili səs yazıcı (audio recorder) və Band 8.5+ model cavablar ilə real imtahan təcrübəsi toplayın.
      </p>
      <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
        <a href="/#view-speaking" class="btn-primary" style="padding: 0.65rem 1.25rem; text-decoration: none; border-radius: 8px;">🎙️ İnteraktiv Taymer &amp; Recorder ilə İşlə</a>
        <a href="https://engnovate.com/ielts-speaking-tests/cambridge-ielts-21-academic-speaking-test-3/" target="_blank" rel="noopener noreferrer" class="action-btn" style="padding: 0.65rem 1.25rem; text-decoration: none; border-radius: 8px;">Engnovate-də Aç ↗</a>
      </div>
    </div>

    <!-- Active Test Section: Cambridge 21 Speaking Test 3 -->
    <section style="margin-bottom: 3rem;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 0.5rem;">
        <div>
          <h2 style="font-size: 1.4rem; font-weight: 800; margin: 0;">Cambridge 21 Academic Speaking Test 3 — Part 1 (Money &amp; Spending)</h2>
          <p style="color: var(--text-secondary); font-size: 0.9rem; margin: 0.25rem 0 0 0;">Akademik suallar, C1/C2 səviyyəli nümunə cavablar və Azərbaycan dilində izahlar</p>
        </div>
        <span class="status-badge status-ready" style="background: rgba(16,185,129,0.1); color: #10b981; border: 1px solid rgba(16,185,129,0.3); padding: 0.35rem 0.75rem; border-radius: 6px; font-weight: 600; font-size: 0.85rem;">Full Model Answers</span>
      </div>

      <div class="questions-list">
{p1_html}
      </div>
    </section>

    <!-- Part 2 & Part 3 Outlines -->
    <section class="grid-2" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.5rem; margin-bottom: 2.5rem;">
      <div class="card" style="padding: 1.5rem; background: var(--bg-surface); border: 1px solid var(--border-medium); border-radius: 12px;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1rem;">
          <h3 style="font-size: 1.15rem; font-weight: 700; margin: 0;">Part 2: Cue Card (Gardens &amp; Parks)</h3>
          <span style="font-size: 0.8rem; background: var(--bg-subtle); padding: 0.25rem 0.5rem; border-radius: 4px;">1m Prep / 2m Speech</span>
        </div>
        <div style="background: var(--bg-subtle); padding: 1rem; border-radius: 8px; margin-bottom: 1rem; font-size: 0.92rem; line-height: 1.6;">
          <strong>Describe a public park or garden that you enjoy visiting.</strong><br/>
          You should say:
          <ul style="margin: 0.5rem 0 0 1.25rem; padding: 0;">
            <li>Where it is located and how often you go there</li>
            <li>What you usually do when you are there</li>
            <li>Who you go there with</li>
            <li>And explain why you like or dislike this park/garden</li>
          </ul>
        </div>
        <p style="font-size: 0.88rem; color: var(--text-secondary); line-height: 1.5;">
          Band 8.5 cavabında <em>"oasis of tranquility", "lush verdant foliage", "respite from urban hustle"</em> kimi C1/C2 ifadələrdən istifadə olunmuşdur.
        </p>
        <a href="/#view-speaking" class="action-btn" style="display: inline-block; padding: 0.5rem 1rem; text-decoration: none; border-radius: 6px; font-size: 0.85rem; font-weight: 600; margin-top: 0.5rem;">Taymer və Recorder ilə Məşq Et &rarr;</a>
      </div>

      <div class="card" style="padding: 1.5rem; background: var(--bg-surface); border: 1px solid var(--border-medium); border-radius: 12px;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1rem;">
          <h3 style="font-size: 1.15rem; font-weight: 700; margin: 0;">Part 3: In-Depth Discussion</h3>
          <span style="font-size: 0.8rem; background: var(--bg-subtle); padding: 0.25rem 0.5rem; border-radius: 4px;">4–5 dəqiqə</span>
        </div>
        <p style="font-size: 0.92rem; color: var(--text-secondary); line-height: 1.6; margin-bottom: 1rem;">
          Şəhərsalma, ictimai yaşıllıq zonalarının mental sağlamlığa təsiri və dövlət büdcəsinin parklara ayrılması üzrə analitik suallar və C2 leksik strukturlar.
        </p>
        <div style="background: var(--bg-subtle); padding: 0.75rem 1rem; border-radius: 8px; font-size: 0.85rem; margin-bottom: 1rem;">
          <strong>Açar Mövzular:</strong> Urban infrastructure, ecological conservation, psychological well-being, community cohesion.
        </div>
        <a href="/#view-speaking" class="action-btn" style="display: inline-block; padding: 0.5rem 1rem; text-decoration: none; border-radius: 6px; font-size: 0.85rem; font-weight: 600;">Part 3 Model Cavablarını Aç &rarr;</a>
      </div>
    </section>"""

    json_ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebApplication",
                "@id": "https://suleimanielts.github.io/speaking/#app",
                "name": "Suleiman IELTS Speaking Suite & Simulator",
                "applicationCategory": "EducationalApplication",
                "operatingSystem": "All modern web browsers",
                "browserRequirements": "HTML5, Web Audio API, MediaRecorder API",
                "url": "https://suleimanielts.github.io/speaking/",
                "description": "In-browser IELTS Academic Speaking simulator featuring 1-minute prep timer, 2-minute speech timer, audio recorder, and Cambridge 21 Speaking Test 3 Band 8.5 model answers.",
                "offers": {
                    "@type": "Offer",
                    "price": "0",
                    "priceCurrency": "USD"
                }
            },
            {
                "@type": "BreadcrumbList",
                "@id": "https://suleimanielts.github.io/speaking/#breadcrumbs",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "Ana Səhifə",
                        "item": "https://suleimanielts.github.io/"
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": "Speaking Practice Suite",
                        "item": "https://suleimanielts.github.io/speaking/"
                    }
                ]
            },
            {
                "@type": "FAQPage",
                "@id": "https://suleimanielts.github.io/speaking/#faq",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": "IELTS Speaking Part 2 imtahanında hazırlıq üçün nə qədər vaxt verilir?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "IELTS Speaking Part 2 mərhələsində namizədə kart üzrə qeydlər götürmək üçün düz 1 dəqiqə (60 saniyə) hazırlıq vaxtı verilir. Bundan sonra namizəd 1-2 dəqiqə fasiləsiz danışmalıdır."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "Suleiman IELTS platformasında səs yazısı necə qeydə alınır?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "Platforma brauzerin yerli MediaRecorder API-sindən istifadə edir. Mikrofon icazəsi verildikdən sonra danışığınız heç bir xarici serverə göndərilmədən birbaşa cihazınızda qeydə alınır və dərhal təkrar dinlənə bilir."
                        }
                    }
                ]
            }
        ]
    }

    full_html = build_html_page(
        title="IELTS Speaking Practice Suite & Simulator — Band 8.5+ Model Answers | Suleiman IELTS",
        description="Master IELTS Academic Speaking with Cambridge 15–21 practice tests, 1m prep / 2m speech timers, in-browser audio recorder, and Band 8.5+ model answers with Azerbaijani translations.",
        canonical_url="https://suleimanielts.github.io/speaking/",
        keywords="IELTS Speaking, IELTS Speaking Part 1, IELTS Speaking Part 2 Cue Card, IELTS Speaking Part 3, Cambridge 21 Speaking Test 3, IELTS Speaking Simulator, Audio Recorder, Band 8.5 Model Answers, Engnovate IELTS, Suleiman IELTS",
        active_route="speaking",
        body_content=body,
        json_ld_graph=json_ld
    )

    with open(os.path.join(BASE_DIR, "speaking", "index.html"), "w", encoding="utf-8") as f:
        f.write(full_html)
    print("Created /speaking/index.html")

# Generate 2. Cambridge Tests Directory (/tests/)
def generate_tests_page():
    os.makedirs(os.path.join(BASE_DIR, "tests"), exist_ok=True)

    tests_cards_html = ""
    for t in cambridge_data.get("tests", []):
        engnovate_link = t.get("engnovate_url", "#")
        tests_cards_html += f"""
        <div class="card" style="padding: 1.5rem; background: var(--bg-surface); border: 1px solid var(--border-medium); border-radius: 12px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
              <span style="font-size: 0.8rem; font-weight: 700; background: rgba(37, 99, 235, 0.12); color: #2563eb; padding: 0.2rem 0.5rem; border-radius: 4px;">{html.escape(t.get("book", "Cambridge"))}</span>
              <span style="font-size: 0.75rem; color: var(--text-muted);">{html.escape(t.get("module", "Academic"))}</span>
            </div>
            <h3 style="font-size: 1.1rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.5rem;">{html.escape(t.get("title", ""))}</h3>
            <p style="font-size: 0.88rem; color: var(--text-secondary); line-height: 1.5; margin-bottom: 1rem;">
              Çətinlik dərəcəsi: <strong>{html.escape(t.get("difficulty", "Academic Standard"))}</strong>. Status: <strong>{html.escape(t.get("status", "Active"))}</strong>.
            </p>
          </div>
          <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
            <a href="{engnovate_link}" target="_blank" rel="noopener noreferrer" class="btn-primary" style="flex: 1; text-align: center; font-size: 0.85rem; padding: 0.5rem 0.75rem; text-decoration: none; border-radius: 6px;">Engnovate-də İşlə ↗</a>
            <a href="/#view-tests" class="action-btn" style="font-size: 0.85rem; padding: 0.5rem 0.75rem; text-decoration: none; border-radius: 6px;">Portalda Aç</a>
          </div>
        </div>"""

    body = f"""    <!-- Breadcrumb -->
    <nav aria-label="Breadcrumb" style="margin-bottom: 1.5rem; font-size: 0.85rem; color: var(--text-muted);">
      <a href="/" style="color: inherit; text-decoration: none;">Ana Səhifə</a> &rsaquo; 
      <span style="color: var(--text-primary); font-weight: 600;">Cambridge Tests Directory</span>
    </nav>

    <div class="hero-banner" style="background: linear-gradient(135deg, rgba(37, 99, 235, 0.15), rgba(16, 185, 129, 0.15)); border: 1px solid var(--border-medium); border-radius: 16px; padding: 2rem; margin-bottom: 2rem;">
      <span class="module-badge" style="background: #2563eb; color: #fff; padding: 0.25rem 0.65rem; border-radius: 6px; font-size: 0.8rem; font-weight: 700; display: inline-block; margin-bottom: 0.75rem;">Cambridge Academic Series (15–21)</span>
      <h1 style="font-size: 1.85rem; font-weight: 800; margin-bottom: 0.75rem;">Cambridge IELTS Academic Practice Tests Directory</h1>
      <p style="color: var(--text-secondary); font-size: 1rem; max-width: 780px; line-height: 1.6; margin-bottom: 1.25rem;">
        Cambridge University Press tərəfindən nəşr olunmuş ən son rəsmi IELTS Academic imtahan testləri (Cambridge 15, 16, 17, 18, 19, 20 və 21). Listening, Reading, Writing və Speaking modulları üzrə birbaşa keçidlər.
      </p>
      <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
        <a href="/#view-tests" class="btn-primary" style="padding: 0.65rem 1.25rem; text-decoration: none; border-radius: 8px;">📚 Bütün Testləri İnteraktiv Filtirlə</a>
        <a href="https://engnovate.com" target="_blank" rel="noopener noreferrer" class="action-btn" style="padding: 0.65rem 1.25rem; text-decoration: none; border-radius: 8px;">Engnovate Ana Səhifə ↗</a>
      </div>
    </div>

    <section>
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 0.5rem;">
        <div>
          <h2 style="font-size: 1.35rem; font-weight: 800; margin: 0;">Sınaq Testləri Kolleksiyası</h2>
          <p style="color: var(--text-secondary); font-size: 0.88rem; margin: 0.25rem 0 0 0;">Band 8.0–9.0 hədəfli akademik sınaqlar və Engnovate bələdçisi</p>
        </div>
        <span style="font-size: 0.85rem; color: var(--text-muted);">Cəmi: <strong>{len(cambridge_data.get("tests", []))} sınaq vahidi</strong></span>
      </div>

      <div class="grid-3" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 1.5rem;">
{tests_cards_html}
      </div>
    </section>"""

    item_list = []
    for idx, t in enumerate(cambridge_data.get("tests", []), 1):
        item_list.append({
            "@type": "ListItem",
            "position": idx,
            "name": t.get("title", ""),
            "url": t.get("engnovate_url", f"https://suleimanielts.github.io/tests/#{t.get('id')}")
        })

    json_ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "ItemList",
                "@id": "https://suleimanielts.github.io/tests/#list",
                "name": "Cambridge IELTS Academic Practice Tests 15–21 Directory",
                "description": "Comprehensive catalogue of Cambridge Academic IELTS Practice Tests 15 through 21 with direct interactive links.",
                "numberOfItems": len(item_list),
                "itemListElement": item_list
            },
            {
                "@type": "BreadcrumbList",
                "@id": "https://suleimanielts.github.io/tests/#breadcrumbs",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "Ana Səhifə",
                        "item": "https://suleimanielts.github.io/"
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": "Cambridge Tests Directory",
                        "item": "https://suleimanielts.github.io/tests/"
                    }
                ]
            }
        ]
    }

    full_html = build_html_page(
        title="Cambridge IELTS Academic Practice Tests (15–21) Directory | Suleiman IELTS",
        description="Complete catalogue of Cambridge IELTS Academic Practice Tests 15 to 21 with direct Engnovate links, listening tracks, reading passages, writing tasks, and speaking cue cards.",
        canonical_url="https://suleimanielts.github.io/tests/",
        keywords="Cambridge IELTS, Cambridge IELTS 15, Cambridge IELTS 16, Cambridge IELTS 17, Cambridge IELTS 18, Cambridge IELTS 19, Cambridge IELTS 20, Cambridge IELTS 21, Academic Practice Tests, Engnovate Tests, Suleiman IELTS",
        active_route="tests",
        body_content=body,
        json_ld_graph=json_ld
    )

    with open(os.path.join(BASE_DIR, "tests", "index.html"), "w", encoding="utf-8") as f:
        f.write(full_html)
    print("Created /tests/index.html")

# Generate 3. Lexical Vault (/vault/)
def generate_vault_page():
    os.makedirs(os.path.join(BASE_DIR, "vault"), exist_ok=True)

    categories_html = ""
    for cat in vocab_data.get("categories", []):
        cat_title = cat.get("category_title", "Category")
        cat_desc = cat.get("description", "")
        
        items_html = ""
        for item in cat.get("items", []):
            items_html += f"""
          <tr style="border-bottom: 1px solid var(--border-light);">
            <td style="padding: 0.85rem 1rem; font-weight: 700; color: var(--text-primary);">{html.escape(item.get("phrase", ""))}</td>
            <td style="padding: 0.85rem 1rem; color: #10b981; font-weight: 600;">{html.escape(item.get("meaning_az", ""))}</td>
            <td style="padding: 0.85rem 1rem; color: var(--text-secondary); font-style: italic; font-size: 0.9rem;">"{html.escape(item.get("example", ""))}"</td>
          </tr>"""

        categories_html += f"""
      <div class="card" style="margin-bottom: 2rem; padding: 1.5rem; background: var(--bg-surface); border: 1px solid var(--border-medium); border-radius: 12px;">
        <div style="margin-bottom: 1rem;">
          <h3 style="font-size: 1.25rem; font-weight: 800; color: var(--text-primary); margin: 0 0 0.25rem 0;">{html.escape(cat_title)}</h3>
          <p style="color: var(--text-secondary); font-size: 0.88rem; margin: 0;">{html.escape(cat_desc)}</p>
        </div>
        <div style="overflow-x: auto;">
          <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.92rem;">
            <thead>
              <tr style="background: var(--bg-subtle); border-bottom: 2px solid var(--border-medium);">
                <th style="padding: 0.75rem 1rem; font-weight: 700;">İfadə / Kollokasiya</th>
                <th style="padding: 0.75rem 1rem; font-weight: 700;">Azərbaycanca İzah</th>
                <th style="padding: 0.75rem 1rem; font-weight: 700;">Akademik Cümlə Nümunəsi</th>
              </tr>
            </thead>
            <tbody>
{items_html}
            </tbody>
          </table>
        </div>
      </div>"""

    body = f"""    <!-- Breadcrumb -->
    <nav aria-label="Breadcrumb" style="margin-bottom: 1.5rem; font-size: 0.85rem; color: var(--text-muted);">
      <a href="/" style="color: inherit; text-decoration: none;">Ana Səhifə</a> &rsaquo; 
      <span style="color: var(--text-primary); font-weight: 600;">Lexical Resource Vault (C1 / C2)</span>
    </nav>

    <div class="hero-banner" style="background: linear-gradient(135deg, rgba(245, 158, 11, 0.15), rgba(139, 92, 246, 0.15)); border: 1px solid var(--border-medium); border-radius: 16px; padding: 2rem; margin-bottom: 2rem;">
      <span class="module-badge" style="background: #f59e0b; color: #fff; padding: 0.25rem 0.65rem; border-radius: 6px; font-size: 0.8rem; font-weight: 700; display: inline-block; margin-bottom: 0.75rem;">Band 8.0–9.0 Lexical Resource</span>
      <h1 style="font-size: 1.85rem; font-weight: 800; margin-bottom: 0.75rem;">IELTS C1/C2 Lexical Resource Vault</h1>
      <p style="color: var(--text-secondary); font-size: 1rem; max-width: 780px; line-height: 1.6; margin-bottom: 1.25rem;">
        İmtahanlarda yüksək bal (Band 8.0, 8.5 və 9.0) qazanmaq üçün vacib C1 və C2 səviyyəli kollokasiyalar, idiomatik birləşmələr, mövzu lüğəti və onların Azərbaycan dilində dəqiq mənaları.
      </p>
      <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
        <a href="/#view-vault" class="btn-primary" style="padding: 0.65rem 1.25rem; text-decoration: none; border-radius: 8px;">🔍 İnteraktiv Canlı Axtarış Rejimi</a>
        <a href="/stories/" class="action-btn" style="padding: 0.65rem 1.25rem; text-decoration: none; border-radius: 8px;">📖 500 Söz 25 Hekayədə</a>
      </div>
    </div>

    <section>
{categories_html}
    </section>"""

    json_ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "DefinedTermSet",
                "@id": "https://suleimanielts.github.io/vault/#vault",
                "name": "IELTS Academic C1/C2 Lexical Resource Vault",
                "description": "Curated collection of advanced academic collocations, idioms, and high-band lexical items for IELTS Academic candidates.",
                "inLanguage": ["en", "az"]
            },
            {
                "@type": "BreadcrumbList",
                "@id": "https://suleimanielts.github.io/vault/#breadcrumbs",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "Ana Səhifə",
                        "item": "https://suleimanielts.github.io/"
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": "Lexical Vault C1/C2",
                        "item": "https://suleimanielts.github.io/vault/"
                    }
                ]
            }
        ]
    }

    full_html = build_html_page(
        title="IELTS C1/C2 Lexical Resource Vault — Band 8.0–9.0 Collocations & Idioms | Suleiman IELTS",
        description="High-scoring C1 and C2 vocabulary for IELTS Academic: advanced collocations, idiomatic expressions, topic-specific vocabulary, and Azerbaijani contextual translations.",
        canonical_url="https://suleimanielts.github.io/vault/",
        keywords="IELTS Vocabulary, C1 Vocabulary, C2 Vocabulary, IELTS Collocations, IELTS Idioms, Lexical Resource Band 9, Academic Word List, Suleiman IELTS Vault",
        active_route="vault",
        body_content=body,
        json_ld_graph=json_ld
    )

    with open(os.path.join(BASE_DIR, "vault", "index.html"), "w", encoding="utf-8") as f:
        f.write(full_html)
    print("Created /vault/index.html")

# Generate 4. Writing Blueprints (/writing/)
def generate_writing_page():
    os.makedirs(os.path.join(BASE_DIR, "writing"), exist_ok=True)

    t1_html = ""
    for b in writing_data.get("task1_blueprints", []):
        t1_html += f"""
        <div class="card" style="padding: 1.5rem; background: var(--bg-surface); border: 1px solid var(--border-medium); border-radius: 12px; margin-bottom: 1.5rem;">
          <h3 style="font-size: 1.15rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.75rem;">{html.escape(b.get("type", "Task 1"))}</h3>
          
          <div style="margin-bottom: 0.75rem;">
            <div style="font-size: 0.78rem; font-weight: 700; color: #2563eb; text-transform: uppercase; margin-bottom: 0.25rem;">Giriş Paraqrafı (Introduction Formula)</div>
            <div style="background: var(--bg-subtle); padding: 0.85rem; border-left: 3px solid #2563eb; font-size: 0.9rem; font-family: var(--font-mono); line-height: 1.5;">{html.escape(b.get("introduction_template", ""))}</div>
          </div>

          <div style="margin-bottom: 0.75rem;">
            <div style="font-size: 0.78rem; font-weight: 700; color: #10b981; text-transform: uppercase; margin-bottom: 0.25rem;">Ümumi Baxış (Overview Formula — Band 8.5)</div>
            <div style="background: var(--bg-subtle); padding: 0.85rem; border-left: 3px solid #10b981; font-size: 0.9rem; font-family: var(--font-mono); line-height: 1.5;">{html.escape(b.get("overview_template", ""))}</div>
          </div>
        </div>"""

    t2_html = ""
    for b in writing_data.get("task2_blueprints", []):
        t2_html += f"""
        <div class="card" style="padding: 1.5rem; background: var(--bg-surface); border: 1px solid var(--border-medium); border-radius: 12px; margin-bottom: 1.5rem;">
          <h3 style="font-size: 1.15rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.75rem;">{html.escape(b.get("type", "Task 2"))}</h3>
          
          <div style="margin-bottom: 0.75rem;">
            <div style="font-size: 0.78rem; font-weight: 700; color: #8b5cf6; text-transform: uppercase; margin-bottom: 0.25rem;">Giriş &amp; Tezisi İfadə Etmə (Thesis Statement)</div>
            <div style="background: var(--bg-subtle); padding: 0.85rem; border-left: 3px solid #8b5cf6; font-size: 0.9rem; font-family: var(--font-mono); line-height: 1.5;">{html.escape(b.get("introduction_thesis", ""))}</div>
          </div>

          <div style="margin-bottom: 0.75rem;">
            <div style="font-size: 0.78rem; font-weight: 700; color: #f59e0b; text-transform: uppercase; margin-bottom: 0.25rem;">Əsas Mətn (Body Paragraph PEEL Strukturu)</div>
            <div style="background: var(--bg-subtle); padding: 0.85rem; border-left: 3px solid #f59e0b; font-size: 0.9rem; font-family: var(--font-mono); line-height: 1.5;">{html.escape(b.get("body_paragraph_structure", ""))}</div>
          </div>

          <div>
            <div style="font-size: 0.78rem; font-weight: 700; color: #ec4899; text-transform: uppercase; margin-bottom: 0.25rem;">Nəticə (Concluding Remarks)</div>
            <div style="background: var(--bg-subtle); padding: 0.85rem; border-left: 3px solid #ec4899; font-size: 0.9rem; font-family: var(--font-mono); line-height: 1.5;">{html.escape(b.get("conclusion_template", ""))}</div>
          </div>
        </div>"""

    body = f"""    <!-- Breadcrumb -->
    <nav aria-label="Breadcrumb" style="margin-bottom: 1.5rem; font-size: 0.85rem; color: var(--text-muted);">
      <a href="/" style="color: inherit; text-decoration: none;">Ana Səhifə</a> &rsaquo; 
      <span style="color: var(--text-primary); font-weight: 600;">Academic Writing Blueprints</span>
    </nav>

    <div class="hero-banner" style="background: linear-gradient(135deg, rgba(139, 92, 246, 0.15), rgba(236, 72, 153, 0.15)); border: 1px solid var(--border-medium); border-radius: 16px; padding: 2rem; margin-bottom: 2rem;">
      <span class="module-badge" style="background: #8b5cf6; color: #fff; padding: 0.25rem 0.65rem; border-radius: 6px; font-size: 0.8rem; font-weight: 700; display: inline-block; margin-bottom: 0.75rem;">Band 8.5 Academic Writing Mastery</span>
      <h1 style="font-size: 1.85rem; font-weight: 800; margin-bottom: 0.75rem;">IELTS Academic Writing Blueprints &amp; Cohesive Devices</h1>
      <p style="color: var(--text-secondary); font-size: 1rem; max-width: 780px; line-height: 1.6; margin-bottom: 1.25rem;">
        Task 1 və Task 2 üçün xüsusi hazırlanmış Band 8.5 şablonları, paraqraf strukturları (PEEL metodu), bağlayıcı ifadələr və yüksək ballı akademik cümlə qəlibləri.
      </p>
      <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
        <a href="/#view-writing" class="btn-primary" style="padding: 0.65rem 1.25rem; text-decoration: none; border-radius: 8px;">✍️ İnteraktiv Şablonları Göstər</a>
        <a href="/vault/" class="action-btn" style="padding: 0.65rem 1.25rem; text-decoration: none; border-radius: 8px;">💎 C1/C2 Lüğət Bazasını Aç</a>
      </div>
    </div>

    <!-- Task 1 Section -->
    <section style="margin-bottom: 3rem;">
      <h2 style="font-size: 1.35rem; font-weight: 800; margin-bottom: 0.5rem;">Academic Writing Task 1 Blueprints (Qrafiklər, Cədvəllər &amp; Proseslər)</h2>
      <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 1.25rem;">Xətti qrafik, sütunlu diaqram və xəritələr üçün Overview formulaları</p>
      {t1_html}
    </section>

    <!-- Task 2 Section -->
    <section>
      <h2 style="font-size: 1.35rem; font-weight: 800; margin-bottom: 0.5rem;">Academic Writing Task 2 Blueprints (Mühakimə &amp; Diskussiya Esseləri)</h2>
      <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 1.25rem;">Agree/Disagree, Discuss Both Views və Problem-Solution formatları üçün struktur</p>
      {t2_html}
    </section>"""

    json_ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Course",
                "@id": "https://suleimanielts.github.io/writing/#course",
                "name": "IELTS Academic Writing Mastery: Task 1 and Task 2",
                "description": "Comprehensive frameworks, cohesive devices, and band 8.5 structures for IELTS Academic Writing Task 1 reports and Task 2 essays.",
                "provider": {
                    "@type": "EducationalOrganization",
                    "name": "Suleiman IELTS",
                    "url": "https://suleimanielts.github.io/"
                }
            },
            {
                "@type": "BreadcrumbList",
                "@id": "https://suleimanielts.github.io/writing/#breadcrumbs",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "Ana Səhifə",
                        "item": "https://suleimanielts.github.io/"
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": "Writing Blueprints",
                        "item": "https://suleimanielts.github.io/writing/"
                    }
                ]
            }
        ]
    }

    full_html = build_html_page(
        title="IELTS Academic Writing Blueprints — Task 1 & Task 2 Band 8.5+ Templates | Suleiman IELTS",
        description="Proven paragraph structures, cohesive devices, overview formulas, and high-band templates for IELTS Academic Writing Task 1 and Task 2 essays.",
        canonical_url="https://suleimanielts.github.io/writing/",
        keywords="IELTS Writing, IELTS Writing Task 1, IELTS Writing Task 2, Academic Writing Blueprints, Band 8.5 Writing Template, Band 9 Essay Structure, Cohesive Devices, Suleiman IELTS Writing",
        active_route="writing",
        body_content=body,
        json_ld_graph=json_ld
    )

    with open(os.path.join(BASE_DIR, "writing", "index.html"), "w", encoding="utf-8") as f:
        f.write(full_html)
    print("Created /writing/index.html")

# Generate 5. 500 Words in 25 Stories (/stories/)
def generate_stories_page():
    os.makedirs(os.path.join(BASE_DIR, "stories"), exist_ok=True)

    stories = stories_data.get("stories", [])
    
    stories_list_html = ""
    for idx, s in enumerate(stories, 1):
        words_count = len(s.get("vocabulary", []))
        stories_list_html += f"""
        <div class="card" style="padding: 1.25rem; background: var(--bg-surface); border: 1px solid var(--border-medium); border-radius: 10px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <span style="font-size: 0.75rem; font-weight: 700; color: #dc2626; background: rgba(220, 38, 38, 0.1); padding: 0.2rem 0.5rem; border-radius: 4px;">Hekayə #{idx}</span>
            <span style="font-size: 0.75rem; color: var(--text-muted);">{words_count} Hədəf Söz</span>
          </div>
          <h3 style="font-size: 1.05rem; font-weight: 700; margin: 0 0 0.25rem 0; color: var(--text-primary);">{html.escape(s.get("title_en", ""))}</h3>
          <p style="font-size: 0.85rem; color: var(--text-secondary); margin: 0 0 0.75rem 0;">{html.escape(s.get("title_az", ""))}</p>
          <a href="/#view-stories" class="action-btn" style="display: inline-block; font-size: 0.8rem; padding: 0.35rem 0.75rem; text-decoration: none; border-radius: 6px;">İnteraktiv Oxu &rarr;</a>
        </div>"""

    # First story preview
    first_story = stories[0] if stories else {}
    story_preview_html = ""
    if first_story:
        vocab_table_rows = ""
        for v in first_story.get("vocabulary", [])[:10]:
            vocab_table_rows += f"""
            <tr style="border-bottom: 1px solid var(--border-light);">
              <td style="padding: 0.6rem 0.75rem; font-weight: 700;">{html.escape(v.get("word", ""))}</td>
              <td style="padding: 0.6rem 0.75rem; color: #10b981; font-weight: 600;">{html.escape(v.get("translation", ""))}</td>
              <td style="padding: 0.6rem 0.75rem; color: var(--text-secondary); font-size: 0.85rem;">{html.escape(v.get("example_en", ""))}</td>
            </tr>"""

        story_preview_html = f"""
      <div class="card" style="padding: 1.75rem; background: var(--bg-surface); border: 1px solid var(--border-medium); border-radius: 12px; margin-bottom: 2.5rem;">
        <span class="module-badge" style="background: rgba(16,185,129,0.1); color: #10b981; border: 1px solid rgba(16,185,129,0.3); padding: 0.2rem 0.5rem; border-radius: 4px; font-size: 0.78rem; font-weight: 700; display: inline-block; margin-bottom: 0.5rem;">Nümunə Oxu: Hekayə #1</span>
        <h2 style="font-size: 1.4rem; font-weight: 800; margin-bottom: 0.25rem;">{html.escape(first_story.get("title_en", ""))} ({html.escape(first_story.get("title_az", ""))})</h2>
        <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 1.25rem;">İngilis dilində mətn və paralel Azərbaycan dilində qarşılığı:</p>

        <div class="grid-2" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.25rem; margin-bottom: 1.5rem;">
          <div style="background: var(--bg-subtle); padding: 1.25rem; border-radius: 8px; border-left: 3px solid #2563eb;">
            <div style="font-size: 0.8rem; font-weight: 700; color: #2563eb; text-transform: uppercase; margin-bottom: 0.5rem;">🇬🇧 English Text</div>
            <div style="line-height: 1.7; font-size: 0.95rem; color: var(--text-primary);">{html.escape(first_story.get("text_en", ""))[:650]}...</div>
          </div>
          <div style="background: var(--bg-subtle); padding: 1.25rem; border-radius: 8px; border-left: 3px solid #10b981;">
            <div style="font-size: 0.8rem; font-weight: 700; color: #10b981; text-transform: uppercase; margin-bottom: 0.5rem;">🇦🇿 Azərbaycan Dilində Tərcümə</div>
            <div style="line-height: 1.7; font-size: 0.95rem; color: var(--text-secondary);">{html.escape(first_story.get("text_az", ""))[:650]}...</div>
          </div>
        </div>

        <h3 style="font-size: 1.1rem; font-weight: 700; margin-bottom: 0.75rem;">Hekayənin Əsas Hədəf Sözləri (20 sözdən ilk 10-u):</h3>
        <div style="overflow-x: auto;">
          <table style="width: 100%; border-collapse: collapse; font-size: 0.88rem; text-align: left;">
            <thead>
              <tr style="background: var(--bg-subtle); border-bottom: 2px solid var(--border-medium);">
                <th style="padding: 0.6rem 0.75rem;">Söz</th>
                <th style="padding: 0.6rem 0.75rem;">Tərcümə</th>
                <th style="padding: 0.6rem 0.75rem;">Mətndaxili Nümunə</th>
              </tr>
            </thead>
            <tbody>
              {vocab_table_rows}
            </tbody>
          </table>
        </div>
      </div>"""

    body = f"""    <!-- Breadcrumb -->
    <nav aria-label="Breadcrumb" style="margin-bottom: 1.5rem; font-size: 0.85rem; color: var(--text-muted);">
      <a href="/" style="color: inherit; text-decoration: none;">Ana Səhifə</a> &rsaquo; 
      <span style="color: var(--text-primary); font-weight: 600;">500 Söz 25 Hekayədə</span>
    </nav>

    <div class="hero-banner" style="background: linear-gradient(135deg, rgba(220, 38, 38, 0.15), rgba(245, 158, 11, 0.15)); border: 1px solid var(--border-medium); border-radius: 16px; padding: 2rem; margin-bottom: 2rem;">
      <span class="module-badge" style="background: #dc2626; color: #fff; padding: 0.25rem 0.65rem; border-radius: 6px; font-size: 0.8rem; font-weight: 700; display: inline-block; margin-bottom: 0.75rem;">Bilingual Vocabulary Reader</span>
      <h1 style="font-size: 1.85rem; font-weight: 800; margin-bottom: 0.75rem;">500 İngilis Sözü 25 Hekayədə Rahat Öyrən</h1>
      <p style="color: var(--text-secondary); font-size: 1rem; max-width: 780px; line-height: 1.6; margin-bottom: 1.25rem;">
        Hər hekayədə 20 hədəf söz olmaqla cəmi 500 ən vacib ingilis sözünü kontekstdə öyrənin. Paralel Azərbaycan dilində tərcümə və "Mənaları Gizlət" test rejimi ilə biliyinizi yoxlayın.
      </p>
      <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
        <a href="/#view-stories" class="btn-primary" style="padding: 0.65rem 1.25rem; text-decoration: none; border-radius: 8px;">📖 İnteraktiv Oxucu &amp; Test Rejimini Aç</a>
        <a href="/vault/" class="action-btn" style="padding: 0.65rem 1.25rem; text-decoration: none; border-radius: 8px;">💎 C1/C2 Vault-a Keç</a>
      </div>
    </div>

    <!-- Story Preview Section -->
    {story_preview_html}

    <!-- All 25 Stories Grid -->
    <section>
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 0.5rem;">
        <div>
          <h2 style="font-size: 1.35rem; font-weight: 800; margin: 0;">Bütün 25 Hekayənin Siyahısı</h2>
          <p style="color: var(--text-secondary); font-size: 0.88rem; margin: 0.25rem 0 0 0;">Cəmi 500 akademik və gündəlik ingilis dili lüğəti</p>
        </div>
        <span style="font-size: 0.85rem; color: var(--text-muted);">25 Hekayə • 500 Söz</span>
      </div>

      <div class="grid-3" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 1.25rem;">
{stories_list_html}
      </div>
    </section>"""

    json_ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "LearningResource",
                "@id": "https://suleimanielts.github.io/stories/#curriculum",
                "name": "500 English Words in 25 Stories (Bilingual Reader Curriculum)",
                "description": "Comprehensive bilingual English-Azerbaijani reading curriculum teaching 500 core vocabulary words across 25 thematic stories.",
                "educationalLevel": "Intermediate to Advanced (B1 to C1)",
                "inLanguage": ["en", "az"],
                "author": {
                    "@type": "Person",
                    "name": "Suleiman Hajizadeh",
                    "url": "https://github.com/SuleimanHajizadeh"
                }
            },
            {
                "@type": "BreadcrumbList",
                "@id": "https://suleimanielts.github.io/stories/#breadcrumbs",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "Ana Səhifə",
                        "item": "https://suleimanielts.github.io/"
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": "500 Söz 25 Hekayədə",
                        "item": "https://suleimanielts.github.io/stories/"
                    }
                ]
            }
        ]
    }

    full_html = build_html_page(
        title="500 English Words in 25 Stories (Bilingual Reader) | Suleiman IELTS",
        description="Learn 500 essential academic English words through 25 captivating bilingual stories with parallel Azerbaijani translations and interactive vocabulary test mode.",
        canonical_url="https://suleimanielts.github.io/stories/",
        keywords="500 English Words, 500 soz 25 hekaye, bilingual English Azerbaijani, IELTS vocabulary through stories, learn english vocabulary, Suleiman IELTS Stories",
        active_route="stories",
        body_content=body,
        json_ld_graph=json_ld
    )

    with open(os.path.join(BASE_DIR, "stories", "index.html"), "w", encoding="utf-8") as f:
        f.write(full_html)
    print("Created /stories/index.html")

# Generate 6. Dashboard (/dashboard/)
def generate_dashboard_page():
    os.makedirs(os.path.join(BASE_DIR, "dashboard"), exist_ok=True)

    routine_items = study_plan_data.get("daily_routine", [])
    routine_html = ""
    for r in routine_items:
        routine_html += f"""
        <li style="padding: 0.75rem 0; border-bottom: 1px solid var(--border-light); display: flex; justify-content: space-between; align-items: center;">
          <div>
            <strong style="color: var(--text-primary);">{html.escape(r.get("activity", ""))}</strong>
            <p style="margin: 0.2rem 0 0 0; font-size: 0.85rem; color: var(--text-secondary);">{html.escape(r.get("notes", ""))}</p>
          </div>
          <span style="font-size: 0.8rem; font-weight: 700; background: var(--bg-subtle); padding: 0.25rem 0.6rem; border-radius: 4px;">{html.escape(r.get("time_estimate", ""))}</span>
        </li>"""

    body = f"""    <!-- Breadcrumb -->
    <nav aria-label="Breadcrumb" style="margin-bottom: 1.5rem; font-size: 0.85rem; color: var(--text-muted);">
      <a href="/" style="color: inherit; text-decoration: none;">Ana Səhifə</a> &rsaquo; 
      <span style="color: var(--text-primary); font-weight: 600;">Daily Study Plan &amp; Dashboard</span>
    </nav>

    <div class="hero-banner" style="background: linear-gradient(135deg, rgba(37, 99, 235, 0.15), rgba(220, 38, 38, 0.15)); border: 1px solid var(--border-medium); border-radius: 16px; padding: 2rem; margin-bottom: 2rem;">
      <span class="module-badge" style="background: #2563eb; color: #fff; padding: 0.25rem 0.65rem; border-radius: 6px; font-size: 0.8rem; font-weight: 700; display: inline-block; margin-bottom: 0.75rem;">Study Dashboard &amp; Companion</span>
      <h1 style="font-size: 1.85rem; font-weight: 800; margin-bottom: 0.75rem;">İmtahan Hazırlığı &amp; Engnovate Bələdçisi</h1>
      <p style="color: var(--text-secondary); font-size: 1rem; max-width: 780px; line-height: 1.6; margin-bottom: 1.25rem;">
        Qarışıqlıq olmadan, təmiz və fokuslanmış mühitdə Cambridge 15–21 Academic testlərini işləyin, model cavabları və C1/C2 lüğət bazasını paralel mənimsəyin.
      </p>
      <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
        <a href="/#view-dashboard" class="btn-primary" style="padding: 0.65rem 1.25rem; text-decoration: none; border-radius: 8px;">🚀 İnteraktiv İdarəetmə Paneli</a>
        <a href="mailto:suleyman.hacizade1@gmail.com?subject=Access%20Request%20-%20SuleimanIELTS%20Private%20Data" class="action-btn" style="padding: 0.65rem 1.25rem; text-decoration: none; border-radius: 8px;">🔒 Məxfi Bazaya Giriş İstə</a>
      </div>
    </div>

    <div class="grid-2" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.5rem; margin-bottom: 2.5rem;">
      <div class="card" style="padding: 1.5rem; background: var(--bg-surface); border: 1px solid var(--border-medium); border-radius: 12px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
          <h2 style="font-size: 1.2rem; font-weight: 700; margin: 0;">📅 Gündəlik Hazırlıq Planı</h2>
          <span style="font-size: 0.78rem; font-weight: 700; background: rgba(16, 185, 129, 0.1); color: #10b981; padding: 0.2rem 0.5rem; border-radius: 4px;">Fokus Rejimi</span>
        </div>
        <ul style="list-style: none; padding: 0; margin: 0;">
{routine_html}
        </ul>
      </div>

      <div class="card" style="padding: 1.5rem; background: var(--bg-surface); border: 1px solid var(--border-medium); border-radius: 12px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
          <h2 style="font-size: 1.2rem; font-weight: 700; margin: 0;">💡 Engnovate-də Rahat İşləmək Qaydası</h2>
          <span style="font-size: 0.78rem; font-weight: 700; background: rgba(37, 99, 235, 0.1); color: #2563eb; padding: 0.2rem 0.5rem; border-radius: 4px;">Tövsiyə</span>
        </div>
        <ul style="padding-left: 1.25rem; font-size: 0.9rem; color: var(--text-secondary); display: flex; flex-direction: column; gap: 0.75rem; margin: 0;">
          <li><strong>Qarışıqlıq yoxdur:</strong> Engnovate-dəki reklam və ya abunə tələbləri olmadan sualları buradan oxuyun və timerlə hazırlaşın.</li>
          <li><strong>Hesab Dəyişmə &amp; Keşlənmə:</strong> Saytda hesab dəyişəndə və ya limit bitəndə <em>Chrome Incognito (Gizli Pəncərə - Cmd+Shift+N)</em> rejimindən istifadə edin; heç bir keş ilişib qalmayacaq.</li>
          <li><strong>Companion Mode:</strong> Yuxarı sağdakı "Companion Mode" düyməsinə basaraq bu səhifəni sağ tərəfdə dar pəncərə kimi yerləşdirin və Engnovate ilə yanaşı işləyin.</li>
          <li><strong>Band 8.5 Model Cavablar:</strong> Hər bir sual üçün akademik cavab və Azərbaycan dilində tərcümə hazırdır.</li>
        </ul>
      </div>
    </div>"""

    json_ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebPage",
                "@id": "https://suleimanielts.github.io/dashboard/#webpage",
                "name": "IELTS Academic Daily Study Plan & Engnovate Companion Dashboard",
                "description": "Structured daily IELTS Academic preparation routine, milestone tracking, and Engnovate companion operational guide.",
                "url": "https://suleimanielts.github.io/dashboard/"
            },
            {
                "@type": "BreadcrumbList",
                "@id": "https://suleimanielts.github.io/dashboard/#breadcrumbs",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "Ana Səhifə",
                        "item": "https://suleimanielts.github.io/"
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": "Dashboard",
                        "item": "https://suleimanielts.github.io/dashboard/"
                    }
                ]
            }
        ]
    }

    full_html = build_html_page(
        title="IELTS Academic Daily Study Plan & Engnovate Companion Dashboard | Suleiman IELTS",
        description="Structured daily IELTS preparation dashboard: focused routine, target Band 8.0+, Cambridge test tracking, and Engnovate companion workflow guidelines.",
        canonical_url="https://suleimanielts.github.io/dashboard/",
        keywords="IELTS Study Plan, Daily Preparation Routine, IELTS Band 8.0, Engnovate Companion, Cambridge IELTS Tracker, Suleiman IELTS Dashboard",
        active_route="dashboard",
        body_content=body,
        json_ld_graph=json_ld
    )

    with open(os.path.join(BASE_DIR, "dashboard", "index.html"), "w", encoding="utf-8") as f:
        f.write(full_html)
    print("Created /dashboard/index.html")

# Generate 7. About & Access Page (/about/)
def generate_about_page():
    os.makedirs(os.path.join(BASE_DIR, "about"), exist_ok=True)

    body = f"""    <!-- Breadcrumb -->
    <nav aria-label="Breadcrumb" style="margin-bottom: 1.5rem; font-size: 0.85rem; color: var(--text-muted);">
      <a href="/" style="color: inherit; text-decoration: none;">Ana Səhifə</a> &rsaquo; 
      <span style="color: var(--text-primary); font-weight: 600;">Haqqımızda &amp; Giriş İcazəsi (About &amp; Access)</span>
    </nav>

    <div class="hero-banner" style="background: linear-gradient(135deg, rgba(220, 38, 38, 0.15), rgba(15, 23, 42, 0.25)); border: 1px solid var(--border-medium); border-radius: 16px; padding: 2.5rem; margin-bottom: 2rem;">
      <span class="module-badge" style="background: #dc2626; color: #fff; padding: 0.25rem 0.65rem; border-radius: 6px; font-size: 0.8rem; font-weight: 700; display: inline-block; margin-bottom: 0.75rem;">Platform Mission &amp; Governance</span>
      <h1 style="font-size: 2rem; font-weight: 800; margin-bottom: 0.75rem;">Suleiman IELTS — Platforma Haqqında və Giriş İcazəsi</h1>
      <p style="color: var(--text-secondary); font-size: 1.05rem; max-width: 820px; line-height: 1.6; margin-bottom: 1.5rem;">
        Suleiman IELTS — Cambridge Academic imtahanlarına (15–21) və Engnovate tədris sisteminə fokuslanmış, diqqəti yayındırmayan minimalist akademik hazırlıq mühitidir.
      </p>
    </div>

    <!-- Private Data Notice & Protocol -->
    <section class="card" style="padding: 2rem; background: var(--bg-surface); border: 1px solid var(--border-medium); border-radius: 14px; margin-bottom: 2rem;">
      <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 1rem;">
        <span style="font-size: 1.75rem;">🔒</span>
        <h2 style="font-size: 1.35rem; font-weight: 800; margin: 0; color: #ef4444;">Məxfi Məlumat Bazası və Giriş İcazəsi (Private Data Access Protocol)</h2>
      </div>
      <p style="line-height: 1.7; color: var(--text-primary); margin-bottom: 1rem;">
        Suleiman IELTS təşkilatının əsas tədqiqat və sənəd bazası (<strong>SuleimanIELTS</strong> mərkəzi anbarı) <strong>tamamilə məxfidir (Private)</strong>. Bu bazaya 400-dən artıq xam IELTS materialı, fərdi sınaq imtahanı nəticələri, Cambridge 15–21 rəsmi PDF/audio materialları və 62 səhifəlik xüsusi Obsidian LLM Wiki bilik anbarı daxildir.
      </p>
      <div style="background: var(--bg-subtle); padding: 1.25rem; border-radius: 10px; border-left: 4px solid #ef4444; margin-bottom: 1.5rem;">
        <strong style="color: var(--text-primary); display: block; margin-bottom: 0.5rem;">Məxfi Bazaya Giriş (Access) Qaydası:</strong>
        <p style="margin: 0; font-size: 0.95rem; color: var(--text-secondary); line-height: 1.6;">
          Akademik araşdırma, tədris və ya elmi əməkdaşlıq məqsədilə xam bazaya və ya Obsidian LLM Wiki sisteminə giriş icazəsi almaq istəyən şəxslər elektron poçt ünvanına rəsmi müraciət göndərə bilərlər. Müraciətiniz nəzərdən keçirildikdən sonra fərdi icazə tokeni və ya repozitoriya girişi təqdim olunur.
        </p>
      </div>

      <div style="display: flex; align-items: center; gap: 1rem; flex-wrap: wrap;">
        <a href="mailto:suleyman.hacizade1@gmail.com?subject=Access%20Request%20-%20SuleimanIELTS%20Private%20Data" class="btn-primary" style="padding: 0.75rem 1.5rem; text-decoration: none; border-radius: 8px; font-weight: 700; background: #dc2626; color: #fff;">
          ✉️ suleyman.hacizade1@gmail.com Ünvanına Müraciət Göndər
        </a>
      </div>
    </section>

    <!-- Leadership & Founder -->
    <section class="card" style="padding: 2rem; background: var(--bg-surface); border: 1px solid var(--border-medium); border-radius: 14px; margin-bottom: 2rem;">
      <h2 style="font-size: 1.35rem; font-weight: 800; margin-bottom: 1rem;">Qurucu və Rəhbərlik (Leadership)</h2>
      <div style="display: flex; gap: 1.5rem; align-items: flex-start; flex-wrap: wrap;">
        <img src="/assets/ielts_logo_avatar_square.png" alt="Suleiman Hajizadeh" style="width: 80px; height: 80px; border-radius: 12px; background: #fff; padding: 4px; box-shadow: var(--shadow-md);" />
        <div style="flex: 1; min-width: 260px;">
          <h3 style="font-size: 1.2rem; font-weight: 800; margin: 0 0 0.25rem 0;">Süleyman Hacızadə (Suleiman Hajizadeh)</h3>
          <span style="color: var(--text-muted); font-size: 0.9rem; display: block; margin-bottom: 0.75rem;">Bioinformatician, Computational Biologist &amp; Academic Lead</span>
          <p style="color: var(--text-secondary); font-size: 0.92rem; line-height: 1.6; margin-bottom: 1rem;">
            Azərbaycan Respublikası Elm və Təhsil Nazirliyinin Molekulyar Biologiya və Biotexnologiyalar İnstitutunun (IMBB) tədqiqatçısı, hesablama biologiyası və struktur biofizika sahəsində açıq elm təşəbbüslərinin rəhbəri. IELTS Academic Band 8.0–9.0 hazırlıq sisteminin və Engnovate distraktorsuz təhsil interfeysinin qurucusu.
          </p>
          <div style="display: flex; gap: 0.75rem; flex-wrap: wrap; font-size: 0.85rem;">
            <a href="https://github.com/SuleimanHajizadeh" target="_blank" rel="noopener noreferrer" style="color: #3b82f6; text-decoration: none; font-weight: 600;">GitHub Profil (@SuleimanHajizadeh) &rarr;</a>
            <a href="https://github.com/SuleimanIELTS" target="_blank" rel="noopener noreferrer" style="color: #3b82f6; text-decoration: none; font-weight: 600;">SuleimanIELTS Təşkilatı &rarr;</a>
          </div>
        </div>
      </div>
    </section>"""

    json_ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "AboutPage",
                "@id": "https://suleimanielts.github.io/about/#page",
                "name": "About Suleiman IELTS & Private Data Access Protocol",
                "url": "https://suleimanielts.github.io/about/",
                "description": "Information about Suleiman IELTS, founder Suleiman Hajizadeh, academic mission, and official protocol for requesting access to the private repository and LLM Wiki vault.",
                "mainEntity": {
                    "@type": "EducationalOrganization",
                    "name": "Suleiman IELTS",
                    "founder": {
                        "@type": "Person",
                        "name": "Suleiman Hajizadeh",
                        "email": "suleyman.hacizade1@gmail.com",
                        "url": "https://github.com/SuleimanHajizadeh"
                    }
                }
            },
            {
                "@type": "BreadcrumbList",
                "@id": "https://suleimanielts.github.io/about/#breadcrumbs",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "Ana Səhifə",
                        "item": "https://suleimanielts.github.io/"
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": "Haqqımızda & Access",
                        "item": "https://suleimanielts.github.io/about/"
                    }
                ]
            }
        ]
    }

    full_html = build_html_page(
        title="About Suleiman IELTS — Leadership, Mission & Private Data Access Protocol",
        description="Learn about the Suleiman IELTS platform, founder Suleiman Hajizadeh, open web companion architecture, and protocol for requesting access to the private 400+ document vault.",
        canonical_url="https://suleimanielts.github.io/about/",
        keywords="About Suleiman IELTS, Suleiman Hajizadeh, Süleyman Hacızadə, Private IELTS Data, Access Request, Cambridge IELTS Archive, Engnovate Companion",
        active_route="about",
        body_content=body,
        json_ld_graph=json_ld
    )

    with open(os.path.join(BASE_DIR, "about", "index.html"), "w", encoding="utf-8") as f:
        f.write(full_html)
    print("Created /about/index.html")

def main():
    generate_speaking_page()
    generate_tests_page()
    generate_vault_page()
    generate_writing_page()
    generate_stories_page()
    generate_dashboard_page()
    generate_about_page()
    print("All sub-path SEO pages generated successfully!")

if __name__ == "__main__":
    main()
