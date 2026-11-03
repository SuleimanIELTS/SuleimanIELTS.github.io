# 🎯 SuleimanIELTS (Public Frontend)

> **Canlı Veb Sayt**: [https://suleimanielts.github.io](https://suleimanielts.github.io)  
> **Data Repozitoriyası (Şəxsi / Private)**: [https://github.com/SuleimanIELTS/SuleimanIELTS](https://github.com/SuleimanIELTS/SuleimanIELTS)

**Suleiman IELTS** — Cambridge IELTS Academic sınaq testlərini (xüsusilə **Cambridge 15–21**) və **Engnovate** platformasını qarışıqlıq olmadan, təmiz ("distraction-free") və yüksək məhsuldarlıqla işləmək üçün hazırlanmış vizual tədris platformasıdır.

---

## ✨ Əsas Üstünlüklər və İmkanlar

1. **⚡ Engnovate Companion (Yanaşı İşləmə Rejimi)**:
   - Sağ yuxarıdakı **"Companion Mode"** düyməsi ilə səhifə yığcam yan panel (sidecar) rejiminə keçir.
   - Engnovate pəncərəsi ilə yanaşı yerləşdirilərək rahat işləməyə imkan verir.
   - Engnovate-dəki testlərə tək kliklə keçid təmin edilir.

2. **⏱️ Speaking Part 2 Timerləri və Audio Yazıcı**:
   - **1 Dəqiqəlik Hazırlıq Timeri** və **2 Dəqiqəlik Danışıq Timeri**.
   - Vaxt bitdikdə avtomatik xəbərdarlıq səsi (Web Audio API Chime).
   - Real imtahan mühiti üçün daxili **Audio Recorder** (danışığınızı birbaşa brauzerdə səsyazma edib dərhal dinləyə və ya `.webm` formatında yükləyə bilərsiniz).
   - Hazırlıq vaxtı qeydlər götürmək üçün avtomatik yadda saxlayan **Scratchpad**.

3. **🇦🇿 Band 8.5 Model Cavablar və Azərbaycan Dilində İzahlar**:
   - Cambridge 21 Academic Speaking Test 3 və digər testlərin bütün suallarına (Part 1, 2, 3) C1/C2 səviyyəli akademik cavablar.
   - Hər bir sual üçün tək kliklə açılan **Azərbaycanca Tərcümə** akordionu.
   - Əsas lüğət tərkibinin interaktiv fişkaları (çiplər).

4. **💎 Lexical Resource Vault (C1 / C2)**:
   - İmtahanda yüksək bal gətirən kollokasiyalar və idiomlar.
   - Canlı axtarış və kateqoriya filtri.
   - Hər bir ifadə üçün Azərbaycan dilində dəqiq məna və real imtahan nümunə cümlələri.

5. **✍️ Academic Writing Blueprints**:
   - Task 1 və Task 2 üçün struktur şablonları və bağlayıcı ifadələr (cohesive devices).

6. **🌙 Dark / Light Rejim**:
   - Apple minimalist dizayn sistemi ilə göz yormayan qaranlıq və aydınlıq rejimləri.

---

## 🌐 Axtarış Motoru Optimizasiyası və URL Sxemi (Senior SEO Architecture)

Platformanın bütün URL və alt-keçidləri (paths) Google, Bing, Yandex və digər qlobal axtarış sistemlərində ən yüksək reytinq (Top 1 Rank) üçün **Senior / Architect səviyyəsində** optimallaşdırılmışdır:

| URL / Path | Modul Təyinatı | JSON-LD Schema Növü | İndekslənmə Prioriteti |
| :--- | :--- | :--- | :---: |
| `https://suleimanielts.github.io/` | Əsas İdarəetmə Portalı & Dashboard | `WebSite`, `EducationalOrganization` | `1.0` (Daily) |
| `https://suleimanielts.github.io/speaking/` | Speaking Suite, Timerlər & Səs Yazıcı | `WebApplication`, `BreadcrumbList`, `FAQPage` | `0.95` (Weekly) |
| `https://suleimanielts.github.io/tests/` | Cambridge IELTS (15–21) Kataloqu | `ItemList`, `BreadcrumbList` | `0.95` (Weekly) |
| `https://suleimanielts.github.io/vault/` | C1/C2 Lexical Vault (Kollokasiyalar) | `DefinedTermSet`, `BreadcrumbList` | `0.95` (Weekly) |
| `https://suleimanielts.github.io/writing/` | Writing Blueprints (Task 1 & 2) | `Course`, `BreadcrumbList` | `0.95` (Weekly) |
| `https://suleimanielts.github.io/stories/` | 500 Söz 25 Hekayədə (Bilingual Reader) | `LearningResource`, `BreadcrumbList` | `0.95` (Weekly) |
| `https://suleimanielts.github.io/dashboard/` | Gündəlik Hazırlıq Planı & Bələdçi | `WebPage`, `BreadcrumbList` | `0.90` (Daily) |
| `https://suleimanielts.github.io/about/` | Rəhbərlik, Missiya & Private Data Access | `AboutPage`, `EducationalOrganization` | `0.85` (Monthly) |

### 🛠️ SEO Texniki İmkanları:
- **XML Sitemap**: `https://suleimanielts.github.io/sitemap.xml` (bütün keçidlər və şəkil uzantıları daxildir).
- **Robots Directives**: `https://suleimanielts.github.io/robots.txt` (Googlebot, Bingbot, Yandex, Applebot üçün açıq indeksləmə).
- **Strukturlaşdırılmış Verilənlər (JSON-LD)**: Schema.org standartlı `EducationalOrganization`, `Person`, `Course`, `WebApplication`, `BreadcrumbList`, `FAQPage`.
- **Pre-rendered HTML & Noscript Fallback**: JavaScript işləməyən axtarış botları üçün tam mətn və suallar DOM-da mövcuddur.
- **PWA & Manifest**: `manifest.json`, 192x192 və 512x512 maskable ikonlar, `theme-color: #dc2626`.
- **Metadata**: Canonical URL-lər, `hreflang` (`az`, `en`, `x-default`), Open Graph (`og:*`), Twitter Cards (`summary_large_image`), GEO teqləri.

---

## 🔒 Arxitektura və Məxfi Məlumat Girişi (Private Data Access)

> [!IMPORTANT]
> **🔒 Məxfi Məlumat Bazası (Private Data Notice):**  
> Bu layihənin mərkəzi data anbarı, 400+ xam IELTS sənədi, fərdi tələbə esseləri, Cambridge sınaqları və 62 səhifəlik Obsidian LLM Wiki bilik bazası saxlanılan **`SuleimanIELTS`** repozitoriyası **tamamilə məxfidir (Private)**.  
> 
> Giriş (access) əldə etmək istəyirsinizsə, elektron poçt vasitəsilə müraciət edə bilərsiniz:  
> 📧 **[suleyman.hacizade1@gmail.com](mailto:suleyman.hacizade1@gmail.com?subject=Access%20Request%20-%20SuleimanIELTS%20Private%20Data)**

- **Frontend (Bu repo - Public)**: Yalnız statik HTML5, CSS3 və təmiz ES6 JavaScript. Heç bir kənar ağır asılılıq və ya izləyici yoxdur.
- **Data Repozitoriyası (`SuleimanIELTS` - Private)**: Bütün testlər, şəxsi qeydlər, tədris planları və lüğət bazası `SuleimanIELTS` şəxsi repozitoriyasında saxlanılır və avtomatlaşdırılmış şəkildə yoxlanılaraq bura sinxronlaşdırılır. Giriş üçün müraciət: `suleyman.hacizade1@gmail.com`.

---

## 🚀 Engnovate-də Keş Və Limit Problemi Olmadan İstifadə

Engnovate-də tapşırıqları edərkən limit və ya upgrade xəbərdarlıqlarının qarşısını almaq və hesabları səliqəli dəyişmək üçün:
- **Chrome Incognito (Cmd+Shift+N)** rejimində işləyin; hər dəfə pəncərəni bağladıqda bütün sessiya çərəzləri və keş dərhal silinir.
- Bu platformadan testin suallarına, vaxtına və model cavablarına baxıb, Engnovate-də sadəcə audio göndərişini həyata keçirin.
