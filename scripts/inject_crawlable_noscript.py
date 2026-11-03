#!/usr/bin/env python3
import json
import html

BASE_PATH = "/Users/macbookairm2/Documents/GitHub/suleimanielts.github.io"

with open(f"{BASE_PATH}/data/cambridge_tests.json", "r", encoding="utf-8") as f:
    cam = json.load(f)

with open(f"{BASE_PATH}/data/stories_500_words.json", "r", encoding="utf-8") as f:
    st = json.load(f)

with open(f"{BASE_PATH}/data/vocabulary_vault.json", "r", encoding="utf-8") as f:
    vo = json.load(f)

with open(f"{BASE_PATH}/data/writing_templates.json", "r", encoding="utf-8") as f:
    wr = json.load(f)

# Build noscript blocks
tests_li = "".join([f"<li><strong>{html.escape(t['title'])}</strong> ({t.get('module')} - {t.get('book')}) &mdash; <a href='{t.get('engnovate_url')}'>Engnovate Keçidi</a></li>" for t in cam.get("tests", [])])

stories_li = "".join([f"<li><strong>Hekayə #{idx+1}: {html.escape(s['title_en'])} ({html.escape(s['title_az'])})</strong> &mdash; 20 hədəf söz</li>" for idx, s in enumerate(st.get("stories", []))])

vocab_blocks = ""
for cat in vo.get("categories", []):
    phrases = ", ".join([f"{html.escape(item['phrase'])} ({html.escape(item['meaning_az'])})" for item in cat.get("items", [])[:8]])
    vocab_blocks += f"<p><strong>{html.escape(cat['category_title'])}:</strong> {phrases} və s.</p>"

noscript_content = f"""
  <!-- Crawlable Noscript Fallback for Search Engines & Non-JS Clients -->
  <noscript>
    <section class="app-container" style="background: var(--bg-surface); padding: 2.5rem; border-radius: 14px; margin-top: 2rem; border: 1px solid var(--border-medium);">
      <h2 style="font-size: 1.5rem; color: var(--text-primary); margin-bottom: 0.5rem;">Suleiman IELTS — Bütün Akademik Resurslar və Test Kataloqu</h2>
      <p style="color: var(--text-secondary); margin-bottom: 1.5rem;">Bu bölmə axtarış sistemlərinin (Google, Bing, Yandex) və JavaScript dəstəkləməyən brauzerlərin bütün platforma resurslarını tam indeksləməsi üçün nəzərdə tutulmuşdur.</p>

      <div style="margin-bottom: 1.5rem;">
        <h3 style="font-size: 1.2rem; color: #2563eb;">📚 Cambridge IELTS Academic Sınaq Testləri (15–21)</h3>
        <ul style="padding-left: 1.25rem; line-height: 1.8;">
          {tests_li}
        </ul>
      </div>

      <div style="margin-bottom: 1.5rem;">
        <h3 style="font-size: 1.2rem; color: #10b981;">💎 C1/C2 Lexical Vault — Əsas Kollokasiyalar və İdiomlar</h3>
        {vocab_blocks}
      </div>

      <div style="margin-bottom: 1.5rem;">
        <h3 style="font-size: 1.2rem; color: #8b5cf6;">📖 500 İngilis Sözü 25 Hekayədə (Bilingual Reader)</h3>
        <ol style="padding-left: 1.25rem; line-height: 1.8;">
          {stories_li}
        </ol>
      </div>

      <div>
        <h3 style="font-size: 1.2rem; color: #ef4444;">🔒 Məxfi Mərkəzi Anbar Girişi (Private Access)</h3>
        <p>Bütün xam sənədlər, fərdi esselər və 62 səhifəlik Obsidian LLM Wiki bilik bazasına giriş əldə etmək üçün elektron poçt ünvanına müraciət edin: <a href="mailto:suleyman.hacizade1@gmail.com?subject=Access%20Request%20-%20SuleimanIELTS%20Private%20Data">suleyman.hacizade1@gmail.com</a></p>
      </div>
    </section>
  </noscript>
"""

with open(f"{BASE_PATH}/index.html", "r", encoding="utf-8") as f:
    content = f.read()

target = "  </main>"
if "<noscript>" not in content:
    content = content.replace(target, target + "\n" + noscript_content)
    with open(f"{BASE_PATH}/index.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("Injected noscript fallback into index.html successfully.")
else:
    print("Noscript already present.")
