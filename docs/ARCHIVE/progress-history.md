# FreeStackFinder — Progress History Archive

This file contains detailed log entries from Days 15–46. Moved from `freestackfinder-progress-log.md` to reduce token load in daily runs. Current entries remain in the main log.

---

### Day 46j — footer trust CTA cleanup
- Converted footer trust links from plain underlined `<p>` with "·" separators to a `<div role="list">` flex row of pill-style links
- Removed `text-decoration: underline` and raw default styling
- New style: `display: flex; flex-wrap: wrap; gap: 8px` row; each link uses `border-radius: 20px`, 1px `rgba(255,255,255,0.15)` border, `4px 12px` padding, `12px` font, `#94A3B8` base color → white on hover with border brightening
- Added `:focus-visible` outline using `var(--primary)` for keyboard accessibility
- Links wrap cleanly on mobile via `flex-wrap`; no horizontal overflow
- All three destination links preserved: `/about/`, `/disclaimer/`, `/contact/`
- Hugo build passed — 308 pages, no errors

---

### Day 46i — reusable tool verdict badges on selected comparison articles
- Shortcode `layouts/shortcodes/verdict.html` and CSS section 33 (`.verdict-badge`) were already in place from a prior partial run; this pass completed the rollout
- Badge style: small all-caps pill using `--primary-dark` text on `--primary-bg` tint with a subtle border — editorial, not promotional
- Applied badges to 4 evergreen comparison pages:
  - `content/business/free-accounting-software.md` — 5 badges: Best overall · Best for Zoho users · Best open source · Best offline option · Best for sole proprietors
  - `content/security/free-vpn.md` — 3 badges: Best overall · Best for variety · Most transparent (Hotspot Shield excluded — not a recommended tool)
  - `content/productivity/microsoft-office-alternatives.md` — 3 badges: Best overall · Best for offline use · Best .docx compatibility (WPS excluded — not a primary recommendation)
  - `content/creative/canva-alternatives.md` — 5 badges: Best overall · Best for image editing · Best for AI drafts · Best browser fallback · Best for mobile
- Badges placed immediately after the tool heading `###` line, before the first paragraph, matching accounting article convention
- All labels match actual article verdicts — no overclaiming, no unsupported superlatives
- Hugo build passed — 308 pages, no errors; badge text verified in rendered HTML for all 4 pages

---

### Day 46h — surface freshness consistently on homepage and category/article cards
- Audited all Hugo-rendered discovery surfaces: homepage Featured comparisons, homepage Latest comparisons, category/list pages, and "More from this category" on article pages — all use `article-card.html` or inline list-item markup that already emitted "Updated {date}" text when `lastmod != date`
- Gap identified: the "Updated" text was visually indistinguishable from a plain publish date — both rendered in `--text-light` (#94A3B8 muted gray)
- Added `class="updated"` to `<time>` elements in `layouts/partials/article-card.html` and the Latest section in `layouts/index.html` when `lastmod != date`; plain-date `<time>` elements get no class, keeping markup clean
- Added CSS section 32 to `static/css/style.css`: `.card-meta time.updated, .article-list-item time.updated { color: var(--primary); font-weight: 600; }` — the site's teal primary (#0F766E) makes updated dates clearly scannable vs muted plain dates without looking like links
- Coverage: all 4 card/list surfaces now render fresh "Updated Apr 24, 2026" text in teal with heavier weight; cards for newly published articles with no lastmod change show plain muted date — no duplicate or conflicting date display
- Search results (JS-rendered) intentionally left unchanged at this time
- Hugo build passed — 308 pages, no errors

---

### Day 46g — curated related-guides logic on article pages
- Added `layouts/partials/related-guides.html` — a slug-keyed curated map that returns the strongest editorial next-reads per article; cluster-first with deliberate adjacent-cluster jumps where they genuinely help
- Falls back to Hugo's built-in `.Site.RegularPages.Related` when a slug is not yet mapped
- Replaced the sidebar block in `layouts/_default/single.html`: heading is now "Read next", list comes from the curated partial with limit=5
- Replaced the bottom "More free software guides" section: now titled "More from {category}" and pulls same-section articles by date, excluding the current page and the five items already shown in the sidebar
- Curated mappings cover all 33 current articles across the 6 silos
- Hugo build passed — 308 pages, no errors

---

### Day 46f — reusable comparison-table component for key comparison articles
- Added `layouts/shortcodes/comparison-table.html` — YAML-driven Hugo shortcode that accepts a `columns` list (key + label) and `rows` list
- Architecture: shortcode + inline YAML via `transform.Unmarshal`, so the structured summary lives inside the article markdown
- First-column cells render as `<th scope="row">`, remaining cells as `<td>` with `data-label` attributes for mobile card-style stacking
- Added CSS section 31 to `static/css/style.css`: compact editorial table on desktop; under 720px the thead hides and each row becomes a card
- Applied to 4 strong evergreen pages:
  - `content/business/free-accounting-software.md`
  - `content/creative/canva-alternatives.md`
  - `content/productivity/microsoft-office-alternatives.md`
  - `content/security/free-vpn.md`
- Hugo build passed — 308 pages, no errors

---

### Day 46e — curated homepage featured collections
- Added a curated collections block to `layouts/index.html` between Featured comparisons and the Trust banner — three use-case cards
- Collections added:
  - "The freelance business stack" — free-accounting-software, free-invoicing-software, free-crm-software, free-project-management-software, free-time-tracking-software
  - "Replace Microsoft Office" — microsoft-office-alternatives, free-spreadsheet-alternatives, free-note-taking-apps, free-calendar-app, grammarly-alternatives
  - "Privacy and safety basics" — free-password-managers, free-vpn, free-antivirus-software, best-free-2fa-apps, free-email-service
- Added CSS section 30 to `static/css/style.css`: 3-column collection-card grid on desktop, collapses to 2-up under 960px and 1-up under 640px
- Hugo build passed — 308 pages, no errors

---

### Day 46d — targeted Productivity and Business cluster link pass
- Added Productivity links from `slack-alternatives` to `microsoft-office-alternatives` and from `free-note-taking-apps` to `microsoft-office-alternatives`
- Added Business links from `quickbooks-alternatives` to `free-crm-software`, from `free-invoicing-software` to `free-spreadsheet-alternatives`, from `free-time-tracking-software` to `free-crm-software`, and from `free-spreadsheet-alternatives` to `free-time-tracking-software`
- Replaced one loose off-cluster recommendation on `quickbooks-alternatives` with a more relevant Business-cluster path
- Hugo build passed — 308 pages, no errors

---

### Day 46c — targeted CTR and internal-link review pass
- Updated title/meta positioning on 6 articles: microsoft-office-alternatives, notion-alternatives, grammarly-alternatives, free-project-management-software, free-crm-software, free-invoicing-software
- Strengthened internal links inside the Productivity cluster and Business cluster
- Hugo build passed — 308 pages, no errors

---

### Day 46b — reusable review/methodology trust block on article pages
- Added `layouts/partials/review-block.html` — compact 3-column editorial block: Last reviewed date, How we evaluate, What "free" means here
- Gating: renders only when `not .Params.noindex`, `ne .Type "page"`, and `.Params.categories` is set
- Added CSS section 29 to `static/css/style.css`: 3-column grid on desktop, stacks to 1 column under 740px
- Hugo build passed — 308 pages, no errors

---

### Day 46a — free-accounting-software article
- Created `content/business/free-accounting-software.md` — 5 tools: Wave, Zoho Books, Akaunting, Manager, GnuCash; date `"2026-04-24"`; weight 76
- Created `scripts/images/generate_free_accounting_software.py` — Business silo, emerald accent `#10b981`
- Generated `static/img/free-accounting-software.webp` (31 KB, 1200×630)
- Added internal links from `quickbooks-alternatives` and `free-invoicing-software` to new article
- Hugo build passed — 308 pages, no errors
- Site now has 33 articles total; Business silo has 7

---

### Day 45d — Wave 2 archive quality and freshness refresh
- Audited remaining high-visibility comparison pages across Business, Creative, Cloud, and Video
- Rewrote free-crm-software, photoshop-alternatives, canva-alternatives, free-cloud-storage-comparison, free-backup-software, free-video-editing-software, and premiere-pro-alternatives
- Improved internal linking between related clusters
- Hugo build passed — 305 pages, 11 paginator pages, no errors

---

### Day 45c — Wave 1 trust and content remediation pass
- Homepage trust fixes in `layouts/index.html`: removed overstated claim, renamed "Most popular" to "Featured comparisons", added trust links
- Structural trust fixes in templates: list.html, single.html, article-card.html, footer.html
- Legal/trust page cleanup: about.md, disclaimer.md, privacy-policy.md, terms.md, contact.md
- Utility-page SEO cleanup: no article-style metadata or schema on noindex pages
- Section page quality improvements: all 6 section `_index.md` files improved
- Focused article remediation: quickbooks-alternatives, free-invoicing-software, free-project-management-software, free-password-managers, free-vpn
- Hugo build passed — 305 pages, no errors

---

### Day 45b — header layout rework and search UI polish
- Restructured `layouts/partials/nav.html`: logo → primary nav → actions group (search icon + mobile toggle) on the far right
- Polished search page styling in CSS section 28
- Hugo build passed — 305 pages, no errors

---

### Day 45a — site search and category filtering
- Architecture: Hugo JSON output format → `/index.json` static search index + vanilla JS search, no external libraries
- Added `JSON` to `[outputs] home` in `config.toml`
- Created `layouts/index.json` — excludes noindex pages
- Created `content/search.md` — dedicated search page, noindex
- Created `layouts/_default/search.html` — search page layout with 7 filter buttons
- Created `static/js/search.js` — vanilla JS: fetches `/index.json`, filters by query and category, highlights matches, debounced input (150ms), reads `?q=` URL param
- Added search icon link to nav
- Added CSS section 28: search page styles
- Hugo build passed — 305 pages, no errors

---

### Day 44a — full-site quality and trust audit pass
- Audited all 32 published articles across 6 silos, all 6 section index pages, and trust/legal pages
- Fixed: Removed internal dev note from `content/business/free-crm-software.md`
- Fixed: Updated stale "Last updated: January 2025" dates in about.md and disclaimer.md → April 2026
- Fixed: Corrected affiliate programs list in disclaimer.md
- Improved: Strengthened `content/video/_index.md`
- Hugo build passed — 303 pages, no errors

---

### Day 43e — homepage trust badge copy fix
- Replaced `✓ No affiliate bias` with `✓ Clear tradeoffs` in the hero badge row
- Hugo build passed — 303 pages, no errors

### Day 43d — fix header nav: replace About with Cloud
- In `config.toml` `[menu]` block: replaced `About /about/ weight=6` with `Cloud /cloud/ weight=6`
- Hugo build passed — 303 pages, no errors

### Day 43c — back-to-top button
- Added `<button id="back-to-top">` with inline chevron SVG to `layouts/_default/baseof.html`
- Added CSS section 27: fixed bottom-right 44×44 circle, fade-in after 400px scroll, accessible
- Added JS to `static/js/main.js`
- Hugo build passed — 303 pages, no errors

### Day 43b — noindex utility/legal pages
- Set `noindex: true` and `sitemap: { disable: true }` on all 5 utility pages: about, contact, disclaimer, terms, privacy-policy
- Hugo build passed — 303 pages, no errors

### Day 43a — free-spreadsheet-alternatives article
- Created `content/business/free-spreadsheet-alternatives.md` — 5 tools: Google Sheets, LibreOffice Calc, Zoho Sheet, ONLYOFFICE, Airtable; date `"2026-04-23"`; weight 78
- Created `scripts/images/generate_free_spreadsheet_alternatives.py` — Business silo, emerald accent
- Generated `static/img/free-spreadsheet-alternatives.webp` (32 KB, 1200×630)
- Hugo build passed — 303 pages, no errors
- Site now has 32 articles total; Business silo has 6

---

### Day 41a — free-calendar-app article
- Created `content/productivity/free-calendar-app.md` — 5 tools: Google Calendar, Notion Calendar, Apple Calendar, Proton Calendar, Zoho Calendar; date `"2026-04-22"`; weight 74
- Created `scripts/images/generate_free_calendar_app.py` — Productivity silo, indigo accent `#6366f1`
- Generated `static/img/free-calendar-app.webp` (27 KB, 1200×630)
- Hugo build passed — 296 pages, no errors
- Site now has 31 articles total; Productivity silo has 8

---

### Day 40a — free-chatgpt-alternatives article
- Created `content/productivity/free-chatgpt-alternatives.md` — 5 tools: Claude, Microsoft Copilot, Google Gemini, Perplexity AI, Meta AI; date `"2026-04-21"`; weight 76
- Created `scripts/images/generate_free_chatgpt_alternatives.py` — Productivity silo, indigo accent `#6366f1`
- Generated `static/img/free-chatgpt-alternatives.webp` (29 KB, 1200×630)
- Hugo build passed — 287 pages, no errors
- Site now has 30 articles total; Productivity silo has 7

---

### Day 39b — Amazon Associates activation
- Activated Amazon Associates US tag `freestackfi20-20` on 3 hardware-adjacent pages:
  - `best-free-2fa-apps.md` — hardware security keys (YubiKey search)
  - `free-backup-software.md` — portable SSDs
  - `free-screen-recording-software.md` — USB microphones
- Hugo build passed — 278 pages, no errors

### Day 39a — free-ai-writing-tools article
- Created `content/productivity/free-ai-writing-tools.md` — 5 tools: Claude, ChatGPT free, Microsoft Copilot, Rytr, Copy.ai; date `"2026-04-20"`; weight 78
- Site now has 29 articles total; Productivity silo has 6

---

### Day 38a — CLAUDE.md day-labeling rule
- Added day-labeling rule to `CLAUDE.md`: multiple runs on the same SGT calendar day use letter suffixes

### Day 37 — branding cleanup
- Updated public-facing brand name from `FreeStackFinder` to `Free Stack Finder` across config, layouts, schema, and all static content pages
- Logo visual in nav and footer kept as compact `FreeStack<span>Finder</span>` form
- `author: "FreeStackFinder Team"` kept as compact byline

### Day 36 — free-font-websites article
- Created `content/creative/free-font-websites.md` — 5 tools: Google Fonts, Font Squirrel, DaFont, Fontsource, 1001 Fonts; date `"2026-04-17"`
- Site now has 28 articles total; Creative silo has 6

### Days 35b–35e — review, hotfixes, and cleanup
- Day 35b: Guarded broken links in layouts; removed invalid SearchAction schema; corrected factual drift in figma-alternatives, free-backup-software, free-cloud-storage-comparison
- Day 35c: Replaced broken Formspree with direct email; moved AdSense publisher ID to config.toml; renamed quickbook→quickbooks slug
- Day 35d: Git ignore cleanup
- Day 35e: Workflow cadence update to CLAUDE.md

### Day 35 — figma-alternatives article
- Created `content/creative/figma-alternatives.md` — 5 tools: Penpot, Lunacy, Plasmic, Quant UX, Figma Starter; date `"2026-04-17"`
- Site now has 27 articles total; Creative silo has 5

### Day 34 — GSC snapshot
- GSC: 2,220 impressions, 5 clicks, avg position 54.4, CTR 0.2% (vs prior 1,420 / 4 / 51.8 / 0.3%)
- Impressions up 56%; CTR still weak; avg position slightly deeper

### Day 33 — CLAUDE.md cleanup
- Fixed article date rule; added Coding and change discipline section

### Day 32 — free-time-tracking-software article
- Created `content/business/free-time-tracking-software.md` — 5 tools: Clockify, Toggl Track, RescueTime Lite, TimeCamp, Harvest; date `"2026-04-16"`
- Site now has 26 articles total; Business silo has 5

### Day 31 — duplicate date fix
- Fixed duplicate publish dates across all 25 articles; 7 articles had dates moved forward; photoshop-alternatives dates quoted
- Final date range: 2025-01-15 through 2026-04-15

### Day 30 — JPEG → WebP conversion
- Converted all 25 article feature images from JPEG to WebP using Python + Pillow (quality 82, method 4)
- Total savings: ~807 KB (1882 KB → 1074 KB, ~43% reduction)
- Deleted all .jpg files from `static/img/`; updated all 25 article front matter `image` paths to `.webp`

### Day 29 — image optimization
- Deleted 1.7 MB unreferenced PNG (`best-free-canva-alternatives-2026-featured-image.png`)
- Re-compressed all 26 JPEGs from quality 92 → 82 using Python + Pillow; saved ~802 KB

### Day 28 — performance improvements
- Fixed `canva-alternatives.md` image path (was referencing 1.7 MB PNG)
- Added `defer` to `/js/main.js` reference in baseof.html
- Added AdSense `preconnect` and `dns-prefetch` in head.html
- Added `width`/`height`/`decoding="async"` to featured image; added `aspect-ratio` CSS to prevent CLS

### Day 27 — image helpers module
- Created `scripts/images/image_helpers.py` — shared module with font loader, text truncation, word-wrap, rounded-rect, circle, draw_chrome, draw_featured_card, draw_grid, draw_bar, and output-path helper
- Rewrote/updated: `generate_free_note_taking_apps.py`, `generate_free_invoicing_software.py`, `generate_free_stock_photos.py`
- Created `scripts/images/generate_free_crm_software.py`

### Day 26 — CONTENT-STRATEGY.md
- Created `CONTENT-STRATEGY.md` in repo root — 50-article content plan, 30-day SEO action plan, realism check, income timeline, growth milestones

### Day 25 — script organization
- Moved all 3 generator scripts from repo root into `scripts/images/`; updated output paths

### Days 15–24 — early articles and affiliate setup
- Days 17–21: Homepage/category sorting fixes; AdSense script added to head.html; NordVPN CTAs added to security pages
- Days 22–23: NordVPN and NordPass CTAs added to free-vpn, free-password-managers
- Day 24: free-note-taking-apps published (25 articles total; all 6 silos at 4 articles each)
- Day 24b: Hotfix for missing feature images (free-invoicing-software, free-stock-photos)
- Day 15: Updated titles on Slack and Office pages based on GSC queries
