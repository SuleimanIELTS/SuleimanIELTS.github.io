# SuleimanIELTS (Public Frontend)

> **Canlı Veb Sayt**: [https://suleimanielts.github.io](https://suleimanielts.github.io)  
> **Data Repozitoriyası (Şəxsi / Private)**: [https://github.com/SuleimanIELTS/SuleimanIELTS](https://github.com/SuleimanIELTS/SuleimanIELTS)

**Suleiman IELTS** — Cambridge IELTS Academic sınaq testlərini (xüsusilə **Cambridge 15–21**) və **Engnovate** platformasını qarışıqlıq olmadan, təmiz və yüksək məhsuldarlıqla işləmək üçün hazırlanmış vizual tədris platformasıdır.

---

## Əsas Üstünlüklər və İmkanlar

1. **Engnovate Companion (Yanaşı İşləmə Rejimi)**:
   - Sağ yuxarıdakı **"Companion Mode"** düyməsi ilə səhifə yığcam yan panel rejiminə keçir.
   - Engnovate pəncərəsi ilə yanaşı yerləşdirilərək rahat işləməyə imkan verir.
   - Engnovate-dəki testlərə tək kliklə keçid təmin edilir.

2. **Speaking Part 2 Taymerləri və Audio Yazıcı**:
   - 1 dəqiqəlik hazırlıq və 2 dəqiqəlik danışıq taymerləri.
   - Vaxt bitdikdə avtomatik xəbərdarlıq səsi (Web Audio API Chime).
   - Real imtahan mühiti üçün daxili Audio Recorder (danışığınızı birbaşa brauzerdə səsyazma edib dərhal dinləyə və ya `.webm` formatında yükləyə bilərsiniz).
   - Hazırlıq vaxtı qeydlər götürmək üçün avtomatik yadda saxlayan Scratchpad.

3. **Band 8.5 Model Cavablar və Azərbaycan Dilində İzahlar**:
   - Cambridge 21 Academic Speaking Test 3 və digər testlərin bütün suallarına (Part 1, 2, 3) C1/C2 səviyyəli akademik cavablar.
   - Hər bir sual üçün tək kliklə açılan Azərbaycan dilində tərcümə paneli.
   - Əsas lüğət tərkibinin interaktiv fişkaları (çiplər).

4. **Lexical Resource Vault (C1 / C2)**:
   - İmtahanda yüksək bal gətirən kollokasiyalar və idiomlar.
   - Canlı axtarış və kateqoriya filtri.
   - Hər bir ifadə üçün Azərbaycan dilində dəqiq məna və real imtahan nümunə cümlələri.

5. **Academic Writing Blueprints**:
   - Task 1 və Task 2 üçün struktur şablonları və bağlayıcı ifadələr (cohesive devices).

6. **Qaranlıq və Aydınlıq Rejimi (Dark / Light Mode)**:
   - Minimalist dizayn sistemi ilə göz yormayan qaranlıq və aydınlıq rejimləri.

---

## Axtarış Motoru Optimizasiyası və URL Sxemi (SEO Architecture)

Platformanın bütün URL və alt-keçidləri Google, Bing, Yandex və digər qlobal axtarış sistemlərində ən yüksək reytinq üçün hərtərəfli şəkildə optimallaşdırılmışdır:

| URL / Path | Modul Təyinatı | JSON-LD Schema Növü | İndekslənmə Prioriteti |
| :--- | :--- | :--- | :---: |
| `https://suleimanielts.github.io/` | Əsas İdarəetmə Portalı & Dashboard | `WebSite`, `EducationalOrganization` | `1.0` (Daily) |
| `https://suleimanielts.github.io/speaking/` | Speaking Suite, Taymerlər & Səs Yazıcı | `WebApplication`, `BreadcrumbList`, `FAQPage` | `0.95` (Weekly) |
| `https://suleimanielts.github.io/tests/` | Cambridge IELTS (15–21) Kataloqu | `ItemList`, `BreadcrumbList` | `0.95` (Weekly) |
| `https://suleimanielts.github.io/vault/` | C1/C2 Lexical Vault (Kollokasiyalar) | `DefinedTermSet`, `BreadcrumbList` | `0.95` (Weekly) |
| `https://suleimanielts.github.io/writing/` | Writing Blueprints (Task 1 & 2) | `Course`, `BreadcrumbList` | `0.95` (Weekly) |
| `https://suleimanielts.github.io/stories/` | 500 Söz 25 Hekayədə (Bilingual Reader) | `LearningResource`, `BreadcrumbList` | `0.95` (Weekly) |
| `https://suleimanielts.github.io/dashboard/` | Gündəlik Hazırlıq Planı & Bələdçi | `WebPage`, `BreadcrumbList` | `0.90` (Daily) |
| `https://suleimanielts.github.io/about/` | Rəhbərlik, Missiya & Məxfi Data Girişi | `AboutPage`, `EducationalOrganization` | `0.85` (Monthly) |

### SEO Texniki İmkanları:
- **XML Sitemap**: `https://suleimanielts.github.io/sitemap.xml` (bütün keçidlər və şəkil uzantıları daxildir).
- **Robots Directives**: `https://suleimanielts.github.io/robots.txt` (Googlebot, Bingbot, Yandex, Applebot üçün açıq indeksləmə).
- **Strukturlaşdırılmış Verilənlər (JSON-LD)**: Schema.org standartlı `EducationalOrganization`, `Person`, `Course`, `WebApplication`, `BreadcrumbList`, `FAQPage`.
- **Pre-rendered HTML & Noscript Fallback**: JavaScript işləməyən axtarış botları üçün tam mətn və suallar DOM-da mövcuddur.
- **PWA & Manifest**: `manifest.json`, standart maskable ikonlar və tətbiq rəngi.
- **Metadata**: Kanonik (canonical) keçidlər, `hreflang` (`az`, `en`, `x-default`), Open Graph (`og:*`), Twitter Cards (`summary_large_image`), GEO teqləri.

---

## Arxitektura və Məxfi Məlumat Girişi (Private Data Access)

### Məxfi Məlumat Bazası (Private Data Notice)

Bu layihənin mərkəzi data anbarı, 400+ xam IELTS sənədi, fərdi tələbə esseləri, Cambridge sınaqları və 62 səhifəlik Obsidian bilik bazası saxlanılan **`SuleimanIELTS`** repozitoriyası **tamamilə məxfidir (Private)**.  

Giriş (access) əldə etmək istəyirsinizsə, elektron poçt vasitəsilə müraciət edə bilərsiniz:  
Elektron poçt: **[suleyman.hacizade1@gmail.com](mailto:suleyman.hacizade1@gmail.com?subject=Access%20Request%20-%20SuleimanIELTS%20Private%20Data)**

- **Frontend (Bu repo - Public)**: Yalnız statik HTML5, CSS3 və təmiz ES6 JavaScript. Heç bir kənar asılılıq və ya izləyici yoxdur.
- **Data Repozitoriyası (`SuleimanIELTS` - Private)**: Bütün testlər, şəxsi qeydlər, tədris planları və lüğət bazası `SuleimanIELTS` şəxsi repozitoriyasında saxlanılır və avtomatlaşdırılmış şəkildə yoxlanılaraq bura sinxronlaşdırılır. Giriş üçün müraciət: `suleyman.hacizade1@gmail.com`.

---

## Engnovate-də Keş və Limit Problemi Olmadan İstifadə

Engnovate-də tapşırıqları edərkən limit və ya upgrade xəbərdarlıqlarının qarşısını almaq və hesabları səliqəli dəyişmək üçün:
- Chrome Incognito rejimində işləyin; hər dəfə pəncərəni bağladıqda bütün sessiya çərəzləri və keş təmizlənir.
- Bu platformadan testin suallarına, vaxtına və model cavablarına baxıb, Engnovate-də sadəcə audio göndərişini həyata keçirin.
