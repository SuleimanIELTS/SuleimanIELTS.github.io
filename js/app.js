// SuleimanIELTS Main Application Logic

document.addEventListener("DOMContentLoaded", () => {
  initTheme();
  initSidecarMode();
  initTabs();
  loadData();
  initTimers();
  initScratchpad();
});

let appData = {
  tests: [],
  vocab: [],
  writing: {},
  studyPlan: {}
};

// Theme Toggle
function initTheme() {
  const savedTheme = localStorage.getItem("suleiman_ielts_theme") || "dark";
  document.documentElement.setAttribute("data-theme", savedTheme);

  const themeBtn = document.getElementById("theme-toggle-btn");
  if (themeBtn) {
    updateThemeIcon(themeBtn, savedTheme);
    themeBtn.addEventListener("click", () => {
      const current = document.documentElement.getAttribute("data-theme");
      const next = current === "dark" ? "light" : "dark";
      document.documentElement.setAttribute("data-theme", next);
      localStorage.setItem("suleiman_ielts_theme", next);
      updateThemeIcon(themeBtn, next);
    });
  }
}

function updateThemeIcon(btn, theme) {
  if (theme === "dark") {
    btn.innerHTML = `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>`;
    btn.title = "Switch to Light Mode";
  } else {
    btn.innerHTML = `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>`;
    btn.title = "Switch to Dark Mode";
  }
}

// Sidecar (Engnovate Companion) Mode
function initSidecarMode() {
  const sidecarBtn = document.getElementById("sidecar-toggle-btn");
  const isSidecar = localStorage.getItem("suleiman_ielts_sidecar") === "true";
  if (isSidecar) {
    document.body.classList.add("sidecar-mode");
  }

  if (sidecarBtn) {
    sidecarBtn.addEventListener("click", () => {
      document.body.classList.toggle("sidecar-mode");
      const active = document.body.classList.contains("sidecar-mode");
      localStorage.setItem("suleiman_ielts_sidecar", active);
      sidecarBtn.classList.toggle("btn-active", active);
    });
  }
}

// Tab Switching
function initTabs() {
  const tabButtons = document.querySelectorAll(".tab-btn");
  const viewSections = document.querySelectorAll(".view-section");

  tabButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      const targetId = btn.getAttribute("data-tab");

      tabButtons.forEach((b) => b.classList.remove("active"));
      viewSections.forEach((sec) => sec.classList.remove("active"));

      btn.classList.add("active");
      const targetSection = document.getElementById(targetId);
      if (targetSection) {
        targetSection.classList.add("active");
      }
    });
  });

  // Speaking Part Switcher
  const spkPartBtns = document.querySelectorAll(".spk-part-btn");
  spkPartBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      spkPartBtns.forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");

      const partNum = btn.getAttribute("data-spk-part");
      document.querySelectorAll(".speaking-part-view").forEach((view) => {
        view.style.display = view.id === `spk-part-${partNum}` ? "block" : "none";
      });
    });
  });
}

// Fetch and Load JSON Data
async function loadData() {
  try {
    const [testsRes, vocabRes, writingRes, planRes] = await Promise.all([
      fetch("data/cambridge_tests.json"),
      fetch("data/vocabulary_vault.json"),
      fetch("data/writing_templates.json"),
      fetch("data/study_plan.json")
    ]);

    appData.tests = (await testsRes.json()).tests || [];
    appData.vocab = (await vocabRes.json()).categories || [];
    appData.writing = await writingRes.json();
    appData.studyPlan = await planRes.json();

    renderDashboard();
    renderSpeakingSuite();
    renderTestsDirectory();
    renderVocabularyVault();
    renderWritingBlueprints();
  } catch (err) {
    console.error("Failed to load local JSON feeds:", err);
  }
}

// 1. Dashboard View
function renderDashboard() {
  const statsContainer = document.getElementById("dashboard-stats");
  if (!statsContainer) return;

  const total = appData.tests.length;
  const inProgress = appData.tests.filter((t) => t.status === "In Progress").length;
  const completed = appData.tests.filter((t) => t.status === "Completed").length;
  const latestResult = appData.studyPlan.latest_diagnostic_result;

  statsContainer.innerHTML = `
    <div class="card">
      <div class="card-header">
        <span class="card-title">🎯 Hədəf Bal</span>
        <span class="target-badge">${appData.studyPlan.target_band_score || 8.0}</span>
      </div>
      <p style="font-size: 0.85rem; color: var(--text-secondary);">
        Speaking <strong>${appData.studyPlan.component_targets?.speaking || 8.5}</strong> • 
        Listening <strong>${appData.studyPlan.component_targets?.listening || 8.5}</strong> • 
        Reading <strong>${appData.studyPlan.component_targets?.reading || 8.5}</strong>
      </p>
    </div>
    <div class="card">
      <div class="card-header">
        <span class="card-title">📚 Sınaq Testləri</span>
        <span class="status-badge status-in-progress">${completed} tamamlanıb</span>
      </div>
      <p style="font-size: 0.85rem; color: var(--text-secondary);">
        Son işlənən: <strong>Cambridge 19 Listening Test 4</strong>
      </p>
    </div>
    <div class="card">
      <div class="card-header">
        <span class="card-title">⚡ Engnovate Companion</span>
        <span class="status-badge status-ready">Aktiv</span>
      </div>
      <p style="font-size: 0.85rem; color: var(--text-secondary);">
        Keş və limit maneəsi olmadan birbaşa sınaqlara keçid
      </p>
    </div>
    ${latestResult ? `
    <div class="card" style="grid-column: 1 / -1; border-left: 4px solid var(--accent-amber); background: linear-gradient(135deg, var(--bg-surface), var(--bg-subtle));">
      <div class="card-header">
        <span class="card-title">📊 Son İmtahan Nəticəsi (Desktop Arxivindən Əlavə Olundu)</span>
        <span class="target-badge" style="background: rgba(245, 158, 11, 0.15); color: var(--accent-amber); border-color: rgba(245, 158, 11, 0.3);">Toplanan Nəticə: Band ${latestResult.score}</span>
      </div>
      <p style="font-size: 0.95rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.25rem;">
        ${latestResult.test_title}
      </p>
      <p style="font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 0.6rem;">
        Doğru cavablar: <strong>${latestResult.correct_count} / ${latestResult.total_count}</strong> • İmtahan müddəti: <strong>${latestResult.time_spent}</strong> • Tarix: <strong>${latestResult.date}</strong>
      </p>
      <div style="font-size: 0.8rem; color: var(--text-secondary); background: var(--bg-surface); padding: 0.6rem 0.85rem; border-radius: var(--radius-sm); border: 1px solid var(--border-light);">
        <strong>💡 Diaqnostik Təhlil & Band 8.5 Yol Xəritəsi:</strong> ${latestResult.gap_analysis}
      </div>
    </div>
    ` : ''}
  `;

  // Study Routine Checklist
  const routineList = document.getElementById("daily-routine-list");
  if (routineList && appData.studyPlan.daily_routine) {
    routineList.innerHTML = appData.studyPlan.daily_routine.map((item, idx) => `
      <div style="display: flex; align-items: flex-start; gap: 0.75rem; padding: 0.75rem 0; border-bottom: 1px solid var(--border-light);">
        <input type="checkbox" id="routine-${idx}" style="margin-top: 0.3rem;" />
        <div>
          <label for="routine-${idx}" style="font-weight: 700; font-size: 0.9rem; cursor: pointer;">${item.time_block}: ${item.activity}</label>
          <div style="font-size: 0.8rem; color: var(--text-muted);">${item.goal}</div>
        </div>
      </div>
    `).join("");
  }
}

// 2. Speaking Practice Suite (Part 1, 2, 3)
function renderSpeakingSuite() {
  const c21Test = appData.tests.find((t) => t.id === "cambridge-21-speaking-3");
  if (!c21Test) return;

  // Part 1 Questions
  const p1Container = document.getElementById("spk-part-1-content");
  if (p1Container && c21Test.parts.part_1) {
    p1Container.innerHTML = c21Test.parts.part_1.questions.map((q) => `
      <div class="qa-card">
        <div class="qa-question-title">
          <span class="qa-pill">Q${q.number}</span>
          <span>${q.question}</span>
        </div>
        <div class="model-box">
          <div class="model-header">
            <span class="model-tag">Band 8.5 Model Answer</span>
            <button class="translation-toggle-btn" onclick="toggleTranslation('t-p1-${q.id}')">
              🇦🇿 Azərbaycanca Tərcümə
            </button>
          </div>
          <p class="model-speech">${q.model_answer_band_8}</p>
          <div id="t-p1-${q.id}" class="translation-box">${q.translation_az}</div>
          <div class="chip-row">
            ${(q.key_vocab || []).map((v) => `
              <span class="vocab-chip">
                <span>${v.word}</span>
                <span class="vocab-chip-az">(${v.translation})</span>
              </span>
            `).join("")}
          </div>
        </div>
      </div>
    `).join("");
  }

  // Part 2 Cue Card
  const p2Container = document.getElementById("spk-part-2-content");
  if (p2Container && c21Test.parts.part_2) {
    const cue = c21Test.parts.part_2.cue_card;
    p2Container.innerHTML = `
      <div class="cue-card-container">
        <div class="cue-card-header">${cue.title}</div>
        <p style="font-weight: 600; font-size: 0.9rem; color: var(--text-secondary);">You should say:</p>
        <ul class="cue-bullets">
          ${cue.bullet_points.map((bp) => `<li>${bp}</li>`).join("")}
        </ul>

        <div style="margin-top: 1.25rem;">
          <label style="font-size: 0.8rem; font-weight: 700; text-transform: uppercase; color: var(--text-muted); display: block; margin-bottom: 0.4rem;">
            📝 1-Minute Preparation Scratchpad:
          </label>
          <textarea id="cue-scratchpad" class="scratchpad" placeholder="Jot down keywords, collocations, and talking points during your 1-minute prep..."></textarea>
        </div>
      </div>

      <div class="qa-card">
        <div class="model-header">
          <span class="model-tag">Band 8.5 Full Model Speech (1.5 - 2 mins)</span>
          <button class="translation-toggle-btn" onclick="toggleTranslation('t-cue-speech')">
            🇦🇿 Azərbaycanca Tərcümə
          </button>
        </div>
        <p class="model-speech" style="font-size: 0.95rem; line-height: 1.7;">${cue.model_speech_band_8}</p>
        <div id="t-cue-speech" class="translation-box">${cue.translation_az}</div>
        <div class="chip-row">
          ${(cue.key_vocab || []).map((v) => `
            <span class="vocab-chip">
              <span>${v.word}</span>
              <span class="vocab-chip-az">(${v.translation})</span>
            </span>
          `).join("")}
        </div>
      </div>
    `;
    initScratchpad();
  }

  // Part 3 Questions
  const p3Container = document.getElementById("spk-part-3-content");
  if (p3Container && c21Test.parts.part_3) {
    p3Container.innerHTML = c21Test.parts.part_3.questions.map((q) => `
      <div class="qa-card">
        <div class="qa-question-title">
          <span class="qa-pill">Part 3 • Q${q.number}</span>
          <span>${q.question}</span>
        </div>
        <div class="model-box">
          <div class="model-header">
            <span class="model-tag">Analytical Band 8.5 Answer</span>
            <button class="translation-toggle-btn" onclick="toggleTranslation('t-p3-${q.number}')">
              🇦🇿 Azərbaycanca Tərcümə
            </button>
          </div>
          <p class="model-speech">${q.model_answer_band_8}</p>
          <div id="t-p3-${q.number}" class="translation-box">${q.translation_az}</div>
        </div>
      </div>
    `).join("");
  }
}

// Translation Accordion Helper
window.toggleTranslation = function(id) {
  const el = document.getElementById(id);
  if (el) {
    el.classList.toggle("visible");
  }
};

// 3. Cambridge Tests Directory View
function renderTestsDirectory() {
  const grid = document.getElementById("tests-grid");
  if (!grid) return;

  grid.innerHTML = appData.tests.map((t) => {
    const hasScore = t.score !== undefined;
    const scoreBadge = hasScore ? `<span class="target-badge" style="background: rgba(245, 158, 11, 0.15); color: var(--accent-amber); border-color: rgba(245, 158, 11, 0.3); font-size: 0.7rem; padding: 0.15rem 0.45rem;">Band ${t.score} (${t.correct_answers}/${t.total_questions})</span>` : '';
    const hasReview = t.parts && (t.parts.part_1?.key_mistakes || t.parts.part_4?.key_mistakes);
    const reviewId = `review-${t.id}`;

    return `
    <div class="test-card">
      <div>
        <div class="test-badge-row">
          <span class="module-badge">${t.module}</span>
          <div style="display: flex; gap: 0.35rem; align-items: center;">
            ${scoreBadge}
            <span class="status-badge ${getStatusClass(t.status)}">${t.status}</span>
          </div>
        </div>
        <div class="test-title">${t.title}</div>
        <div class="test-topic-desc">
          ${t.attempt_date ? `📅 <strong>Tarix:</strong> ${t.attempt_date} • ⏱️ ${t.time_spent}<br>` : ''}
          ${t.parts?.part_1?.topic || t.parts?.part_2?.topic || t.difficulty}
        </div>
      </div>

      ${hasReview ? `
        <div id="${reviewId}" class="translation-box" style="margin-top: 0.65rem; font-size: 0.8rem; font-style: normal; line-height: 1.5; border-left: 3px solid var(--accent-rose);">
          <strong style="color: var(--accent-rose); display: block; margin-bottom: 0.35rem;">⚠️ Əsas Səhvlər və Düzgün İzahlar:</strong>
          <ul style="padding-left: 1.1rem; display: flex; flex-direction: column; gap: 0.35rem;">
            ${(t.parts.part_1?.key_mistakes || []).slice(0, 3).map(m => `<li><strong>Q${m.q}:</strong> Yazılan: <code style="color:var(--accent-rose); font-weight:700;">${m.user}</code> &rarr; Doğru: <code style="color:var(--accent-green); font-weight:700;">${m.correct}</code> <br><span style="color:var(--text-muted); font-size:0.75rem;">(${m.note})</span></li>`).join('')}
            ${(t.parts.part_4?.key_mistakes || []).slice(0, 3).map(m => `<li><strong>Q${m.q}:</strong> Yazılan: <code style="color:var(--accent-rose); font-weight:700;">${m.user}</code> &rarr; Doğru: <code style="color:var(--accent-green); font-weight:700;">${m.correct}</code> <br><span style="color:var(--text-muted); font-size:0.75rem;">(${m.note})</span></li>`).join('')}
          </ul>
        </div>
      ` : ''}

      <div class="test-actions">
        <a href="${t.engnovate_url}" target="_blank" rel="noopener noreferrer" class="btn-primary" style="font-size: 0.8rem; padding: 0.45rem 0.85rem;">
          <span>Open on Engnovate</span>
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
            <polyline points="15 3 21 3 21 9"></polyline>
            <line x1="10" y1="14" x2="21" y2="3"></line>
          </svg>
        </a>
        ${hasReview ? `
          <button class="btn-secondary" style="font-size: 0.8rem; padding: 0.45rem 0.75rem;" onclick="toggleTranslation('${reviewId}')">
            🔍 Səhvləri Aç / Bağla
          </button>
        ` : `
          <button class="btn-secondary" style="font-size: 0.8rem; padding: 0.45rem 0.75rem;" onclick="markTestDone('${t.id}')">
            ${t.status === 'Completed' ? 'Yenidən İşlə' : 'Tamamlandı'}
          </button>
        `}
      </div>
    </div>
  `}).join("");
}

function getStatusClass(status) {
  if (status === "In Progress") return "status-in-progress";
  if (status === "Completed") return "status-completed";
  return "status-ready";
}

window.markTestDone = function(testId) {
  const t = appData.tests.find((item) => item.id === testId);
  if (t) {
    t.status = t.status === "Completed" ? "In Progress" : "Completed";
    renderTestsDirectory();
    renderDashboard();
  }
};

// 4. Vocabulary Vault View
function renderVocabularyVault(filterCategory = "all", searchQuery = "") {
  const container = document.getElementById("vault-list");
  if (!container) return;

  let html = "";
  appData.vocab.forEach((cat) => {
    if (filterCategory !== "all" && cat.category_id !== filterCategory) return;

    const filteredItems = cat.items.filter((it) => {
      if (!searchQuery) return true;
      const q = searchQuery.toLowerCase();
      return it.phrase.toLowerCase().includes(q) || 
             it.meaning_az.toLowerCase().includes(q) || 
             it.example.toLowerCase().includes(q);
    });

    if (filteredItems.length === 0) return;

    html += `
      <div style="margin-bottom: 2rem;">
        <h3 style="font-size: 1.15rem; font-weight: 700; margin-bottom: 0.5rem; display: flex; align-items: center; gap: 0.5rem;">
          <span>${cat.category_title}</span>
        </h3>
        <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1rem;">${cat.description}</p>
        <div class="grid-2">
          ${filteredItems.map((item) => `
            <div class="vocab-card">
              <div class="vocab-card-header">
                <span class="vocab-phrase">${item.phrase}</span>
                <span class="cefr-tag">${item.cefr}</span>
              </div>
              <div class="vocab-meaning">${item.meaning_az}</div>
              <div class="vocab-example">"${item.example}"</div>
            </div>
          `).join("")}
        </div>
      </div>
    `;
  });

  container.innerHTML = html || `<p style="color: var(--text-muted); text-align: center; padding: 2rem;">No matching vocabulary found.</p>`;
}

// 5. Writing Blueprints View
function renderWritingBlueprints() {
  const container = document.getElementById("writing-blueprints-container");
  if (!container || !appData.writing.task1_blueprints) return;

  container.innerHTML = `
    <div style="margin-bottom: 2rem;">
      <h3 style="font-size: 1.2rem; font-weight: 800; margin-bottom: 1rem;">📊 Task 1 Academic Blueprints</h3>
      <div class="grid-2">
        ${appData.writing.task1_blueprints.map((b) => `
          <div class="card">
            <div class="card-title">${b.type}</div>
            <div style="margin: 0.75rem 0;">
              <strong style="font-size: 0.8rem; color: var(--primary);">Introduction Template:</strong>
              <p style="font-size: 0.85rem; font-style: italic; margin-top: 0.2rem;">${b.introduction_template}</p>
            </div>
            <div style="margin: 0.75rem 0;">
              <strong style="font-size: 0.8rem; color: var(--accent-green);">Overview Template:</strong>
              <p style="font-size: 0.85rem; font-style: italic; margin-top: 0.2rem;">${b.overview_template}</p>
            </div>
            <p style="font-size: 0.8rem; color: var(--text-muted);">${b.body_paragraph_tips}</p>
          </div>
        `).join("")}
      </div>
    </div>

    <div>
      <h3 style="font-size: 1.2rem; font-weight: 800; margin-bottom: 1rem;">✍️ Task 2 Academic Essay Structures</h3>
      <div class="grid-2">
        ${appData.writing.task2_blueprints.map((t2) => `
          <div class="card">
            <div class="card-title">${t2.type}</div>
            <ol style="margin-top: 0.75rem; padding-left: 1.2rem; display: flex; flex-direction: column; gap: 0.4rem; font-size: 0.85rem;">
              ${t2.structure.map((s) => `<li>${s}</li>`).join("")}
            </ol>
          </div>
        `).join("")}
      </div>
    </div>
  `;
}

// Timers & Scratchpad Initialization
function initTimers() {
  window.prepTimer = new SpeakingTimer("prep-timer-display", 60, () => {
    alert("⏰ 1 minute preparation time is up! Start speaking now.");
  });

  window.speechTimer = new SpeakingTimer("speech-timer-display", 120, () => {
    alert("⏰ 2 minutes speaking time completed!");
  });

  window.audioRec = new AudioRecorder("record-btn", "audio-preview-container", "rec-elapsed-timer");

  // Timer Buttons
  document.getElementById("btn-prep-start")?.addEventListener("click", () => window.prepTimer.start());
  document.getElementById("btn-prep-pause")?.addEventListener("click", () => window.prepTimer.pause());
  document.getElementById("btn-prep-reset")?.addEventListener("click", () => window.prepTimer.reset());

  document.getElementById("btn-speech-start")?.addEventListener("click", () => window.speechTimer.start());
  document.getElementById("btn-speech-pause")?.addEventListener("click", () => window.speechTimer.pause());
  document.getElementById("btn-speech-reset")?.addEventListener("click", () => window.speechTimer.reset());

  // Search & Filter listeners
  const searchInput = document.getElementById("vocab-search");
  const filterSelect = document.getElementById("vocab-category-filter");

  if (searchInput && filterSelect) {
    const handleFilter = () => {
      renderVocabularyVault(filterSelect.value, searchInput.value);
    };
    searchInput.addEventListener("input", handleFilter);
    filterSelect.addEventListener("change", handleFilter);
  }
}

function initScratchpad() {
  const pad = document.getElementById("cue-scratchpad");
  if (pad) {
    pad.value = localStorage.getItem("suleiman_ielts_scratchpad") || "";
    pad.addEventListener("input", () => {
      localStorage.setItem("suleiman_ielts_scratchpad", pad.value);
    });
  }
}
