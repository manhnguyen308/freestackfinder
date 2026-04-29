# FreeStackFinder — Project State

**Site:** freestackfinder.com
**Last updated:** 2026-04-29 (Day 52c)
**Current day:** 52c

## Current state

- Total articles: 40
- Silos: Productivity 9/9 ✓ · Business 13/13 ✓ · Creative 6/8 · Security 4/6 · Cloud 4/7 · Video 4/7
- AdSense: script live (`ca-pub-5934721249825043`); formal approval pending
- GSC (2026-04-28): 4,640 impressions · 13 clicks · avg position 51.7 · CTR 0.3% over the last 3 months
- Next content: Creative or Cloud silo — see CONTENT-STRATEGY.md for next unpublished article
- Next feature: see `FEATURE-STRATEGY.md` Phases 5–9; next non-content candidate is a stale-content checker

---

### Day 52c — GSC refresh verification pass

- Verified all 8 GSC target pages from Day 52a (Microsoft Office, Dropbox, Slack, Grammarly, Illustrator, free backup software, QuickBooks, free project management) have improvements in place; all carry `lastmod: "2026-04-28"`
- Same 2026-04-28 GSC snapshot confirmed recorded in `docs/GSC-NOTES.md`; no new data requiring action
- Fixed stale article count in `docs/BUILD-VALIDATION.md`: 39 → 40
- No new content published; article count remains 40; Canva and Grammarly remain under review / needs approval
- Validation: git diff --check clean · QA runner 3 passed · 0 failed · Hugo build 388 pages · 0 errors

---

### Day 52b — repository hygiene cleanup

- Removed tracked Python bytecode from version control and added general Python cache ignore rules
- No article files or public output changed; article count remains 40
- Validation: git status reviewed, diff check clean, QA runner passed with counts

---

### Day 52a — GSC-led CTR refresh for high-impression pages

- Reviewed last-3-month GSC snapshot: 13 clicks, 4.64K impressions, 0.3% CTR, average position 51.7
- Priority pages inspected: Microsoft Office alternatives, Dropbox alternatives, Grammarly alternatives, Slack alternatives, Illustrator alternatives, free backup software, QuickBooks alternatives, free project management software
- Refreshed query-aligned SEO titles/descriptions on 8 target pages where useful; kept URLs, slugs, aliases, and routing unchanged
- Light first-screen wording updates made on Microsoft Office, Dropbox, and Slack pages to better match Office replacement, Dropbox replacement, and Slack replacement search intent
- Fixed weak public snippet wording on `free-backup-software`; removed unsupported "tested" wording from the Illustrator title and Microsoft Office intro
- Existing hub, related-guide, and contextual links already cover target pages; no mass backlinking added
- No new article published; article count remains 40; Business silo remains 13/13
- No affiliate links added; no Canva or Grammarly CTAs added; Canva and Grammarly remain under review / needs approval
- `docs/GSC-NOTES.md` updated with snapshot, priority pages, query themes, actions, and follow-up items
- Validation: git diff check, quality runner, Hugo build, article count, internal links, and generated-output checks completed

---

### Day 51a — publish free-hr-software

- Published `content/business/free-hr-software.md`: "Best Free HR Software in 2026 — Simple People Ops Without the Price Tag"
- Covers: Zoho People (free up to 5 employees), OrangeHRM Community Edition (self-hosted, no user cap), Homebase (scheduling/time tracking, 1 location free), Bitrix24 (HR features in free workspace), Google Sheets (DIY fallback)
- Clearly distinguishes HRIS tools, scheduling/time tracking, and spreadsheet-based options; payroll and compliance caveats throughout
- Created `scripts/images/generate_free_hr_software.py` and generated `static/img/free-hr-software.webp` (27 KB, 1200×630, Business accent #10b981)
- Internal links from new article: free-project-management-software, free-time-tracking-software, free-crm-software, free-spreadsheet-alternatives, free-invoicing-software, free-accounting-software
- Backlinks added: free-time-tracking-software verdict section → free-hr-software; free-project-management-software verdict section → free-hr-software
- `CONTENT-STRATEGY.md` updated: free-hr-software marked ✓ Published
- Article count: 39 → 40 · Business silo: 12/13 → 13/13 ✓
- Canva and Grammarly remain under review / needs approval
- Build: PASSED · 388 pages · 0 errors · 0 warnings · front matter valid · image resolves · internal links resolve · QA runner 3 passed · 0 failed

---

### Day 50c — Hugo 0.160.1 migration

- Hugo Extended 0.160.1 confirmed as system version; build already passes cleanly
- No template, config, shortcode, or content changes required — zero deprecation warnings
- `README.md` updated: `HUGO_VERSION` env var and version check comment changed from `0.128.0` → `0.160.1`
- `docs/BUILD-VALIDATION.md` created: records required Hugo version, QA script usage, and deployment checklist
- Validation: `hugo --minify` clean (373 pages, 0 errors, 0 warnings); QA runner 3 passed · 0 failed; article count confirmed at 39; Canva/Grammarly remain under review
- Cloudflare Pages: update `HUGO_VERSION` env var in dashboard to `0.160.1`

---

### Day 50b — review pass after recent site updates

- Reviewed recent Business/Productivity content, Start Here, category hub top-picks, search/index changes, related guides, affiliate docs, roadmap docs, and QA scripts
- Issues found: stale feature roadmap counts after `free-web-analytics`, affiliate tracker missing `free-web-analytics`, unsupported public "tested" wording, and missing curated related-guide coverage for the new analytics article
- Fixes made: updated public trust wording to "compare/evaluate" language, added `free-web-analytics` to curated related guides and affiliate tracker, refreshed `FEATURE-STRATEGY.md` counts/next recommendation, and corrected current tracker next-content/feature notes
- Validation: git diff --check clean; QA runner clean with known warnings only; Hugo build passed; article count confirmed at 39 total and Business 12/13
- Follow-up: publish `free-hr-software` on the next content day; keep Canva/Grammarly deferred until approval is confirmed; update NordPass only if an approved tracked URL is available

---

### Day 50a — publish free-web-analytics

- Published `content/business/free-web-analytics.md`: "Best Free Web Analytics Tools in 2026"
- Covers: Google Analytics 4, Google Search Console, Microsoft Clarity, Umami (self-hosted), Matomo On-Premise
- Clearly distinguishes traffic analytics, search performance tools, privacy-friendly analytics, and self-hosted options
- Includes comparison table, tool-by-tool breakdown, decision guide (when free is enough vs. when to pay), and product analytics vs. website analytics note
- Created `scripts/images/generate_free_web_analytics.py` and generated `static/img/free-web-analytics.webp` (32 KB, 1200×630, Business accent #10b981)
- Internal links added to free-website-builders, free-project-management-software, free-crm-software
- `CONTENT-STRATEGY.md` updated: free-web-analytics marked ✓ Published
- Article count: 38 → 39 · Business silo: 11/13 → 12/13
- Canva and Grammarly remain under review / needs approval
- Build: PASSED · front matter valid · image resolves · internal links resolve

---

### Day 49f — article count by silo report script

- Created `scripts/report_article_counts.py`: scans content silo folders, excludes `_index.md` and utility/root pages, respects `draft: true`, prints count/target/remaining table; Python standard library only
- Script output confirmed: Business 11/13 · Cloud 4/7 · Creative 6/8 · Productivity 9/9 ✓ · Security 4/6 · Video 4/7 · Total 38 — matches tracker
- Updated `scripts/run_quality_checks.py`: added `--with-counts` flag that runs the report after QA checks (informational only; count mismatches do not affect exit code)
- `FEATURE-STRATEGY.md` updated: Phase 9 article count item marked done (Day 49f); archive row added; Suggested Next Feature updated to `free-web-analytics`
- No article published; article count unchanged at 38
- No public page, template, CSS, JS, image, or article body changed
- Canva and Grammarly remain under review / needs approval

---

### Day 49e — validation runner script

- Created `scripts/run_quality_checks.py`: runs all three QA scripts in sequence (front matter, internal links, feature images)
- Supports `--with-build` flag (runs `hugo --minify` after QA) and `--quiet` flag (suppresses verbose child output, shows last 4 lines)
- Uses Python standard library only; locates repo root from script path; returns non-zero exit if any checker fails
- Runner executed: 3 passed · 0 failed · 18 description-length warnings (known, no action required) · 3 image orphans (known, no action required)
- `FEATURE-STRATEGY.md` updated: Phase 9 runner item marked done (Day 49e); archive row added; Suggested Next Feature updated
- No article published; article count unchanged at 38
- No public page, template, CSS, JS, image, or article body changed
- No affiliate CTAs added; Canva and Grammarly remain under review / needs approval

---

### Day 49d — feature roadmap reorganization

- `FEATURE-STRATEGY.md` fully reorganized after completion of all Phase 1–4 features
- All 26 completed features moved from mixed inline entries into a clean "Completed Feature Archive" table with day, category, and one-line note
- Old Phase 1–4 active sections (all done) replaced with 5 new future phases: Phase 5 (content expansion), Phase 6 (GSC-led refresh), Phase 7 (monetization readiness), Phase 8 (E-E-A-T strengthening), Phase 9 (maintenance automation)
- Current Feature Baseline updated: 38 articles, Business 11/13, Canva/Grammarly under review noted, validators listed
- Suggested Next Feature updated: primary recommendation is `free-web-analytics`; no Canva/Grammarly CTA suggestion
- "What Not To Build Yet" updated to include sticky ToC and affiliate CTA shortcode
- "How To Choose The Next Feature" updated to reference new phase numbers
- No article published; article count unchanged at 38
- No public page, template, CSS, JS, image, or article body changed
- No affiliate CTAs added; Canva and Grammarly remain under review
- Validation: git diff --check clean · front matter 0 errors PASSED · internal links 0 broken PASSED · feature images 0 errors PASSED

---

### Day 49c — GSC search performance notes template

- Created `docs/GSC-NOTES.md`: lightweight internal file for tracking Google Search Console observations
- Contains: snapshot history table (date, clicks, impressions, CTR, avg position, notes); page opportunity table (page, query/theme, impressions, clicks, CTR, avg position, issue, next action, priority); action rules for CTR issues, position 8–20 pages, newly published pages, and already-improving pages; monthly review checklist
- Baseline snapshot from 2026-04-15 added: 5 clicks · 2,220 impressions · 0.2% CTR · avg position 54.4
- Update cadence: weekly light check · monthly deeper review · after major content batches
- No new article published; article count unchanged at 38
- No public page, template, CSS, JS, image, or article body changed
- No affiliate CTAs added; Canva and Grammarly remain deferred (not available for placement)
- `FEATURE-STRATEGY.md` updated: Phase 4.4 marked complete (Day 49c); row added to Completed Feature Systems; Suggested Next Feature updated
- Front matter: 0 errors · 18 warnings · PASSED
- Internal links: 0 broken · PASSED
- Feature images: 0 errors · 3 orphans · PASSED

---

### Day 49b — affiliate tracker Canva/Grammarly cleanup

- Canva and Grammarly CTA placement confirmed not currently available; all related tracker rows downgraded from High/Medium priority to Deferred
- Updated `docs/AFFILIATE-TRACKER.md`: header active-programs list corrected; 7 Canva/Grammarly rows set to Deferred; next-action queue cleaned (items 1 and 2 removed)
- Updated `docs/AFFILIATE-GUIDELINES.md`: Canva and Grammarly changed from Active to Deferred with placement note
- Updated `FEATURE-STRATEGY.md`: removed Canva/Grammarly CTA suggestion from Suggested Next Feature; replaced with NordPass tracked URL follow-up
- No public article published; article count unchanged at 38
- No public page, template, CSS, JS, or image changed
- No affiliate CTAs added

---

### Day 49a — affiliate tracker verification pass

- Reviewed `docs/AFFILIATE-TRACKER.md` against `docs/AFFILIATE-GUIDELINES.md`
- Resolved all 15 "Needs verification" rows by checking actual article files
- Confirmed 8 articles have live CTAs: `free-password-managers` (NordPass), `free-vpn` (NordVPN), `free-antivirus-software` (NordVPN), `best-free-2fa-apps` (NordVPN + Amazon), `free-backup-software` (Amazon), `free-screen-recording-software` (Amazon), `dropbox-alternatives` (NordVPN), `free-email-service` (NordVPN)
- Confirmed 7 articles have no CTA yet: `canva-alternatives`, `grammarly-alternatives`, `free-stock-photos`, `free-ai-writing-tools`, `photoshop-alternatives`, `illustrator-alternatives`, `microsoft-office-alternatives`
- Flagged: NordPass link in `free-password-managers` uses direct nordpass.com URL rather than a tracked affiliate URL — noted for future update if tracked URL is available
- Removed duplicate `best-free-2fa-apps` Amazon row (was double-listed); merged into single row
- Added `free-website-builders` (Day 48n) to tracker as Deferred — no active program fit
- Updated next-action queue; Zoho rows remain on hold pending CJ approval
- No public article published; article count unchanged at 38
- No public page, template, CSS, JS, or image changed
- No affiliate CTAs added in this run
- `FEATURE-STRATEGY.md` updated: affiliate verification pass marked complete (Day 49a); Suggested Next Feature updated

---

### Day 48o — feature image inventory checker script

- Created `scripts/check_feature_images.py`: cross-checks `image:` fields in all 38 silo articles against files in `static/img/`; flags missing files as errors; reports unreferenced files in `static/img/` as possible orphans (warnings only); checks for non-WebP extensions
- Run: `python3 scripts/check_feature_images.py` — exits 1 on missing images, 0 on clean or warnings-only
- First run: 38 articles checked · 38 images verified · 0 errors · 3 possible orphans (`default-article.jpg`, `nordpass-banner.png`, `nordvpn-banner.png`) — PASSED with warnings
- Orphans left in place; banner PNGs are not used per affiliate guidelines (no image banners), placeholder JPG may be safe to remove later
- No new article published; article count unchanged at 38
- No public page, template, CSS, JS, or image changed
- `FEATURE-STRATEGY.md` updated: Phase 4.3 marked complete (Day 48o); row added to Completed Feature Systems; Suggested Next Feature updated

---

### Day 48n — publish free-website-builders article

- Published `content/business/free-website-builders.md`: Business silo, article 11/13
- Covers 5 tools: Wix (featured — most features on free plan), Google Sites (best zero-cost), WordPress.com (best for blogging), Carrd (best one-pager), Canva Websites (best for Canva users)
- Includes comparison table shortcode and 5 verdict badges
- 4 internal links: `/business/free-crm-software/`, `/business/free-invoicing-software/`, `/business/free-social-media-scheduling/`, `/productivity/microsoft-office-alternatives/`, `/cloud/free-cloud-storage-comparison/`
- Feature image generated: `static/img/free-website-builders.webp` (32 KB, 1200×630 WebP)
- Image script: `scripts/images/generate_free_website_builders.py`
- Related-guides mapping updated for `free-website-builders` and `free-social-media-scheduling`
- `CONTENT-STRATEGY.md` updated: `free-website-builders` marked ✓ Published
- Front matter validator: 0 errors · 19 warnings (1 new description-length warning) · PASSED
- Internal link checker: 0 broken links · PASSED
- Hugo build: 360 pages, no errors

---

### Day 48m — internal link checker script

- Created `scripts/check_internal_links.py`: scans all `.md` files under `content/` for internal Markdown links (`[text](/path/)`); builds a route map from front matter slugs and file paths; skips external, mailto, tel, and anchor-only links; strips fragments before matching; normalizes trailing slashes
- Run: `python3 scripts/check_internal_links.py` — exits 1 on broken links, 0 if clean
- First run: 44 files · 53 known routes · 0 broken links — PASSED
- No broken links to fix; no article edits required
- No new article published; article count unchanged at 37
- No public page, template, CSS, JS, or image changed
- `FEATURE-STRATEGY.md` updated: Phase 4.2 marked complete (Day 48m); row added to Completed Feature Systems; Suggested Next Feature updated

---

### Day 48l — front matter validator script

- Created `scripts/validate_front_matter.py`: scans all 37 silo articles for 9 categories of front matter issues — missing required fields, banned keys (`featured`, `faqs`), future dates, bare unquoted dates, image path format, image file existence in `static/img/`, empty/overlong descriptions, duplicate slugs, accidental `noindex` on silo articles
- Run: `python3 scripts/validate_front_matter.py` — exits 1 on errors, 0 on warnings-only or clean
- First run result: 2 errors (missing `slug` on `photoshop-alternatives` and `microsoft-office-alternatives`) — both fixed; 18 description-length warnings remain as informational backlog (not blocking)
- Final run: 0 errors · 18 warnings · PASSED with warnings
- No new article published; article count unchanged at 37
- No public page, template, CSS, JS, or image changed
- `FEATURE-STRATEGY.md` updated: Phase 4.1 marked complete (Day 48l); row added to Completed Feature Systems; Suggested Next Feature updated

---

### Day 48k — internal affiliate opportunity tracker

- Created `docs/AFFILIATE-TRACKER.md`: internal ops file listing all 37 articles with affiliate program candidate, CTA placed status, verification status, priority, and notes
- High-priority verification queue covers 8 articles (NordVPN, NordPass, Canva, Grammarly, Amazon); Amazon Day 39b placements flagged for link/tag confirmation
- Zoho and Impact.com rows marked "Needs approval" / "Deferred" — no placements added
- No public article published; article count unchanged at 37
- No public page, template, CSS, JS, or image changed
- No affiliate CTA added in this run
- `FEATURE-STRATEGY.md` updated: Phase 3.1 marked complete (Day 48k); row added to Completed Feature Systems; Suggested Next Feature updated to content publishing or verification pass

---

### Day 48j — category hub top-picks upgrade
- Added "Where to start" box to all 6 silo hub pages: Productivity, Business, Creative, Security, Cloud, Video
- Each box shows 4 curated links with a one-line decision guide explaining who each article is for
- Links use existing published articles only; no invented or broken links
- Template unchanged — content renders via existing `category-intro` div in `layouts/_default/list.html`
- CSS: added `.hub-top-picks` and related rules to `static/css/style.css` (no new layout system)
- No new article published; article count unchanged at 37
- Hugo build passed — 347 pages, no errors
- `FEATURE-STRATEGY.md` updated: Phase 2.3 marked complete (Day 48j); next suggestion updated to content publishing

---

### Day 48i — add Start Here guided entry page
- Created `content/start-here.md`: indexable static page at `/start-here/`
- Six reader-path cards covering all silos: freelancer/solo → Business; replacing Office → Productivity; safer accounts → Security; creative tools → Creative; storage/backup → Cloud; video/media → Video
- Each card contains 4 curated links to existing high-value articles (24 internal links total)
- Footer note links to `/search/` and all 6 silo category pages
- "Start Here" nav link added to `config.toml` (weight 0, appears first)
- Two CSS rules added to `static/css/style.css` (`.start-here-paths`, `.start-here-footer`) for grid spacing; no new layout or shortcode required
- No new article published; article count unchanged at 37
- Hugo build passed — 347 pages, no errors
- `FEATURE-STRATEGY.md` updated: Phase 2.2 marked complete (Day 48i); Phase 2.3 category hub upgrade set as next suggested feature

---

### Day 48h — documentation restructure
- Split `CLAUDE.md` image rules into `docs/IMAGE-GUIDELINES.md`
- Split affiliate/monetization rules into `docs/AFFILIATE-GUIDELINES.md`
- Moved Days 15–46 detailed history to `docs/ARCHIVE/progress-history.md`
- Added "When to read what" routing table to `CLAUDE.md`
- Condensed progress log from 926 lines to ~250 lines; stale "Current snapshot" and "Current priorities" sections removed
- No article content, templates, layouts, CSS, JS, or images changed
- Manual checks: all referenced doc paths valid; CLAUDE.md still contains all safety-critical rules; progress log current state reflects 37 articles

---

### Day 48g — upgrade search result cards
- Search result cards now display: category pill (existing), title link (existing), description excerpt (existing), and a freshness date line
- Freshness line shows "Updated [date]" in primary green when `lastmod ≠ date`; "Published [date]" in muted text when equal
- `layouts/index.json` updated to include `date` and `lastmod` fields (ISO format) in the search index JSON
- `static/js/search.js` updated: added `formatDate()` helper and date label generation in the render function
- `static/css/style.css` updated: added `.search-result-date` and `.search-result-date--updated` rules
- Category filtering and query highlighting remain unchanged
- No new article published; article count unchanged at 37
- `FEATURE-STRATEGY.md` updated: search card upgrade marked complete (Day 48g); next suggested feature updated to Start Here page (Phase 2.2)

---

### Day 48f — expand verdict badges to comparison pages
- Rolled out `verdict.html` shortcode to all 7 remaining high-intent comparison pages
- Pages updated: free-password-managers, free-project-management-software, free-crm-software, free-invoicing-software, free-cloud-storage-comparison, free-video-editing-software, photoshop-alternatives
- 3 defensible per-tool labels per page; all labels match the existing article verdict and tool ordering
- No article body content rewritten; badge insertions only
- No new article published; article count unchanged at 37
- `FEATURE-STRATEGY.md` updated: verdict badge rollout marked complete (Day 48f)

---

### Day 48e — normalize recent article publish dates
- Spread the four Day 48 articles across four consecutive calendar days to avoid multiple same-day publications
- Dates assigned: free-pdf-editor-alternatives → 2026-04-22, free-resume-builders → 2026-04-23, free-social-media-scheduling → 2026-04-24, free-visio-alternatives → 2026-04-25
- No article body content changed; front matter `date` and `lastmod` updated only
- Total published articles unchanged: 37

---

### Day 48d — publish free-visio-alternatives
- Published new Business article: Best Free Microsoft Visio Alternatives in 2026
- Article covers draw.io, Lucidchart Free, Miro Free, and Whimsical Free; honest notes on LibreOffice Draw, Cacoo, and Microsoft Visio Viewer
- Comparison table shortcode at top; verdict badge shortcode on draw.io
- Feature image generated: `static/img/free-visio-alternatives.webp` (30 KB)
- Image script created: `scripts/images/generate_free_visio_alternatives.py`
- Related-guides map updated; internal link added to `free-project-management-software`
- `CONTENT-STRATEGY.md` updated: `free-visio-alternatives` marked Published
- Total published articles: 37 (Business now at 10/13)

---

### Day 48c — publish free-social-media-scheduling
- Published first Later-queue Business article: Best Free Social Media Scheduling Tools in 2026
- Article covers Buffer, Metricool, Later, and Meta Business Suite
- Comparison table shortcode at top; verdict badge shortcode on two tools
- Feature image generated: `static/img/free-social-media-scheduling.webp` (35 KB)
- Related-guides map updated; internal link added to `free-crm-software`
- `CONTENT-STRATEGY.md` updated: `free-social-media-scheduling` marked Published
- Total published articles: 36 (Business now at 9/13)

---

### Day 48b — publish free-resume-builders
- Published new Business article: Best Free Resume Builders in 2026
- Article covers Canva, Google Docs, Indeed Resume Builder, Resume.com; honest notes on Zety, Novoresume, Kickresume
- Comparison table shortcode at top; verdict badge shortcode on two tools
- Feature image generated: `static/img/free-resume-builders.webp` (29 KB)
- Related-guides map updated; internal link added to `grammarly-alternatives`
- `CONTENT-STRATEGY.md` updated: `free-resume-builders` marked Published
- Total published articles: 35 (Business now at 8/13)

---

### Day 48a — publish free-pdf-editor-alternatives
- Published new Productivity article: Best Free PDF Editor Alternatives in 2026
- Article covers PDFgear, PDF24 Tools, Sejda, LibreOffice Draw, and Xodo
- Comparison table shortcode at top; verdict badge shortcode on four tools
- Feature image generated: `static/img/free-pdf-editor-alternatives.webp` (29 KB)
- Image script created: `scripts/images/generate_free_pdf_editor_alternatives.py`
- Related-guides map updated; internal links added to `microsoft-office-alternatives` and `free-note-taking-apps`
- `CONTENT-STRATEGY.md` updated: `free-pdf-editor-alternatives` marked Published
- Total published articles: 34 (Productivity now at 9 — silo target reached)

---

### Day 47d — continued weekly code and AdSense-readiness review
- Fixed: Article JSON-LD string values with embedded quote characters
- Fixed: Removed synthetic FAQPage schema from all article pages (was rendering on all 33 articles without matching visible FAQ sections)
- Fixed: Softened `free-vpn` framing from blanket claims to more precise language about ads, data collection, and trial-like limits
- Files changed: `layouts/partials/schema.html`, `content/security/free-vpn.md`
- Hugo build passed — 308 pages, 9 paginator pages, no errors

---

### Day 47c — weekly audit and review pass
- Found and fixed 4 pages that had both the reusable comparison table shortcode AND an older markdown "Quick comparison table": `microsoft-office-alternatives`, `canva-alternatives`, `free-accounting-software`, `free-vpn`
- Updated `lastmod` to `"2026-04-25"` on the 4 corrected articles
- Hugo build passed — 308 pages, 9 paginator pages, no errors

---

### Day 47b — expand comparison tables to seven high-intent articles
- Deployed comparison-table shortcode to 7 articles (total now 11):
  - `free-crm-software`, `free-invoicing-software`, `free-project-management-software`, `free-cloud-storage-comparison`, `free-video-editing-software`, `photoshop-alternatives`, `free-password-managers`
- Each table moved to immediately after the Quick verdict section
- `FEATURE-STRATEGY.md` Phase 1.1 marked complete
- Hugo build: not available locally; build verifies on Cloudflare Pages

---

### Day 47a — feature strategy file
- Created `FEATURE-STRATEGY.md` in repo root
- Documents all completed feature systems, 4 roadmap phases, feature principles, deferred/not-yet list, and maintenance notes
- No site-rendered files changed

---

## Days 40–46 milestone summary

| Day | What shipped |
|-----|-------------|
| 46a | Published `free-accounting-software` (33 articles, Business 7/13) |
| 46b | Added review/methodology trust block to all article pages |
| 46c | CTR + internal-link review; updated 6 article title/descriptions |
| 46d | Productivity + Business cluster link pass |
| 46e | Curated homepage collections (freelance stack, Office alternatives, privacy basics) |
| 46f | Reusable `comparison-table` shortcode; deployed on 4 articles |
| 46g | Curated related-guides logic; covers all 33 articles |
| 46h | Freshness display on article/homepage cards (Updated in teal) |
| 46i | Verdict badge shortcode; deployed on 4 comparison pages |
| 46j | Footer trust CTA cleanup — pill-row flex layout |
| 45a | Site search + category filtering (JSON index, vanilla JS, /search/) |
| 45b | Header layout rework, search UI polish |
| 45c | Wave 1 trust remediation — 10+ articles, legal pages, schema cleanup |
| 45d | Wave 2 quality refresh — 7 older articles (crm, photoshop, canva, cloud storage, backup, video, premiere-pro) |
| 44a | Full-site quality audit; fixed CRM dev note, stale dates in legal pages, disclaimer program list |
| 43a–e | back-to-top button; noindex utility pages; free-spreadsheet-alternatives published; nav fix (Cloud replaces About); homepage trust badge copy fix |
| 41a | Published `free-calendar-app` (31 articles, Productivity 8/9) |
| 40a | Published `free-chatgpt-alternatives` (30 articles, Productivity 7/9) |

Detailed entries for Days 15–46 are in `docs/ARCHIVE/progress-history.md`.

---

## Affiliate focus

| Program | Priority pages |
|---------|---------------|
| NordVPN | `free-vpn`, `free-antivirus-software`, `dropbox-alternatives`, `free-email-service`, `best-free-2fa-apps` |
| NordPass | `free-password-managers` |
| Canva | `canva-alternatives`, `free-stock-photos` |
| Grammarly | `grammarly-alternatives`, `free-ai-writing-tools` |
| Amazon US (`freestackfi20-20`) | `best-free-2fa-apps` (security keys), `free-backup-software` (SSDs), `free-screen-recording-software` (USB mics) |
| Zoho (pending via CJ) | `free-crm-software`, `free-email-service`, `free-invoicing-software` |

See `docs/AFFILIATE-GUIDELINES.md` for placement rules.

---

## Pending actions

- Zoho affiliate via CJ Affiliate — still pending; apply when Zoho content is established
- AdSense formal approval pending (`ca-pub-5934721249825043` script is live)
- Impact.com reapplication deferred until traffic data is sufficient
- Reddit post #3 drafted for `r/entrepreneur`

---

## Cluster internal link reference

Full inventory in `CONTENT-STRATEGY.md`. Quick cluster reference:

- **Productivity:** slack-alternatives · microsoft-office-alternatives · grammarly-alternatives · notion-alternatives · free-note-taking-apps · free-ai-writing-tools · free-chatgpt-alternatives · free-calendar-app · free-pdf-editor-alternatives
- **Creative:** canva-alternatives · photoshop-alternatives · illustrator-alternatives · free-stock-photos · figma-alternatives · free-font-websites
- **Business:** quickbooks-alternatives · free-crm-software · free-project-management-software · free-invoicing-software · free-time-tracking-software · free-spreadsheet-alternatives · free-accounting-software · free-resume-builders · free-social-media-scheduling · free-visio-alternatives
- **Security:** free-password-managers · free-antivirus-software · free-vpn · best-free-2fa-apps
- **Cloud:** free-cloud-storage-comparison · dropbox-alternatives · free-email-service · free-backup-software
- **Video:** free-video-editing-software · zoom-alternatives · premiere-pro-alternatives · free-screen-recording-software
