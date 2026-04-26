# FreeStackFinder — Project State

**Site:** freestackfinder.com
**Last updated:** 2026-04-26
**Current day:** 48k

## Current state

- Total articles: 37
- Silos: Productivity 9/9 ✓ · Creative 6/8 · Business 10/13 · Security 4/6 · Cloud 4/7 · Video 4/7
- AdSense: script live (`ca-pub-5934721249825043`); formal approval pending
- GSC (2026-04-15): 2,220 impressions · 5 clicks · avg position 54.4 · CTR 0.2%
- Next content: Business silo — `free-website-builders`, `free-web-analytics`, or `free-hr-software`
- Next feature: Phase 2 complete; see `FEATURE-STRATEGY.md` for Phase 3/4 options

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
