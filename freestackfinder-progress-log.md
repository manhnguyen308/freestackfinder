# FreeStackFinder — Project State

**Site:** freestackfinder.com  
**Last updated:** 2026-04-22  
**Current day:** 41  


---

## Read this first
This is the primary daily state file.

Rules for daily runs:
- Use this file as the main source of current project truth
- Do not perform a broad repo audit unless this file is clearly outdated or inconsistent with the task
- Choose one focused day activity per run — may include multiple related tasks that belong together
- Inspect only the files needed for that activity
- Keep daily runs focused on content creation or improvement, build verification, light QA, and tracker updates
- Weekly review cleanup and monthly audits belong to Codex unless explicitly requested
- If repo files conflict with this tracker, trust the files and then correct this tracker

---

## Current snapshot
- Stack: Hugo 0.128.0 + GitHub + Cloudflare Pages
- Total published articles: 31
- Silo balance: Productivity 8, Creative 6, Business 5, Cloud 4, Security 4, Video 4
- Main monetization active: NordVPN, NordPass, Canva, Grammarly, Amazon Associates (US tag: freestackfi20-20 — now in use on 3 pages)
- Pending affiliate priority: Zoho via CJ Affiliate
- GSC latest (2026-04-15): 2,220 impressions, 5 clicks, average position 54.4, CTR 0.2%
- GSC prior baseline: 1,420 impressions, 4 clicks, average position 51.8, CTR 0.3%
- GSC read: impressions improving (+56%), clicks still low (+1), CTR weak (0.2%), avg position slipped slightly — visibility growing but ranking depth and click appeal still need work
- Current site goal: grow useful content clusters, improve internal linking, strengthen monetization, and prepare for AdSense

---

## Current priorities
1. Continue publishing from the Early queue — next up: `free-spreadsheet-alternatives` (Business silo)
2. Targeted CTR improvement on pages already earning impressions — pull GSC query/page report and rework titles + meta descriptions on pages with impressions but near-zero CTR
3. Strengthen internal linking inside the two strongest clusters (Productivity, Business)
4. Apply Zoho affiliate via CJ Affiliate — Zoho referenced on crm, email, and invoicing pages
5. Post Reddit #3 for `r/entrepreneur`
6. Continue growing clusters to 50 articles — see `CONTENT-STRATEGY.md`

### Content pipeline — next articles to publish (Priority: Early)
Publish in this order unless a higher-priority fix exists:

- `free-spreadsheet-alternatives` — Business silo
- `free-accounting-software` — Business silo
- `free-pdf-editor-alternatives` — Productivity silo
- `free-resume-builders` — Business silo

Full 50-article plan with silo targets and Later-queue articles is in `CONTENT-STRATEGY.md`.

---

## Current content state

### Silo counts
- Productivity: 8
- Creative: 6
- Cloud: 4
- Business: 5
- Security: 4
- Video: 4

### Homepage most popular
- `slack-alternatives` — 95
- `microsoft-office-alternatives` — 90
- `canva-alternatives` — 85
- `best-free-2fa-apps` — 76
- `free-invoicing-software` — 74
- `free-project-management-software` — 72

---

## Open issues / things to verify
- Recheck GSC to see whether Day 15 title changes improved CTR on Slack and Office pages
- Confirm Zoho references can be monetized after CJ approval
- AdSense can be applied for based on article volume, but trust and UX should still be reviewed before submission
- Internal linking should keep growing cluster-by-cluster, not randomly
- Keep checking for mismatches between tracker and actual repo state
- Contact page now uses direct email fallback until a real form backend is configured

---

## Recent completed work

### Day 41a — free-calendar-app article
- Created `content/productivity/free-calendar-app.md` — 5 tools: Google Calendar, Notion Calendar, Apple Calendar, Proton Calendar, Zoho Calendar; date `"2026-04-22"`; weight 74
- Created `scripts/images/generate_free_calendar_app.py` — Productivity silo, indigo accent `#6366f1`
- Generated `static/img/free-calendar-app.webp` (27 KB, 1200×630)
- Added internal link from `free-note-taking-apps` → `free-calendar-app` (Our verdict)
- Added internal link from `notion-alternatives` → `free-calendar-app` (Our verdict)
- Added internal link from `slack-alternatives` → `free-calendar-app` (Our verdict)
- Article links back to `free-note-taking-apps` (twice), `notion-alternatives`, `free-chatgpt-alternatives`, and `slack-alternatives`
- Updated `lastmod` on `free-note-taking-apps`, `notion-alternatives`, and `slack-alternatives` to `"2026-04-22"`
- Updated `CONTENT-STRATEGY.md`: `free-calendar-app` marked as ✓ Published
- Hugo build passed — 296 pages, no errors
- Site now has 31 articles total; Productivity silo has 8

### Day 40a — free-chatgpt-alternatives article
- Created `content/productivity/free-chatgpt-alternatives.md` — 5 tools: Claude, Microsoft Copilot, Google Gemini, Perplexity AI, Meta AI; date `"2026-04-21"`; weight 76
- Created `scripts/images/generate_free_chatgpt_alternatives.py` — Productivity silo, indigo accent `#6366f1`
- Generated `static/img/free-chatgpt-alternatives.webp` (29 KB, 1200×630)
- Added internal link from `free-ai-writing-tools` → `free-chatgpt-alternatives` (Our verdict)
- Added internal link from `grammarly-alternatives` → `free-chatgpt-alternatives` (Our verdict)
- Article links back to `free-ai-writing-tools` (twice), `grammarly-alternatives`, and `free-note-taking-apps`
- Updated `lastmod` on `free-ai-writing-tools` and `grammarly-alternatives` to `"2026-04-21"`
- Updated `CONTENT-STRATEGY.md`: `free-chatgpt-alternatives` marked as ✓ Published
- Hugo build passed — 287 pages, no errors or warnings
- Site now has 30 articles total; Productivity silo has 7

### Day 39b — Amazon Associates activation
- Audited repo: Amazon Associates was listed as "active" but had zero affiliate links in any article
- Added Amazon hardware security key CTA to `content/security/best-free-2fa-apps.md` (Our verdict section) — links to Amazon search for YubiKey with tag `freestackfi20-20`
- Added Amazon portable SSD CTA to `content/cloud/free-backup-software.md` (Our verdict section) — links to Amazon search for portable SSDs, tied to 3-2-1 backup strategy explanation
- Added Amazon USB microphone CTA to `content/video/free-screen-recording-software.md` (Our verdict section) — links to Amazon search for USB microphones, tied to audio quality explanation
- Updated `lastmod` on all three articles to `"2026-04-20"`
- Hugo build passed — 278 pages, no errors
- Amazon US tag `freestackfi20-20` now active on 3 pages; SG tag `freestackfi20-22` reserved for future SG-specific content
- Placements chosen for hardware fit: security keys (Security), external drives (Cloud/backup), USB mics (Video)

### Day 39a — free-ai-writing-tools article
- Created `content/productivity/free-ai-writing-tools.md` — 5 tools: Claude, ChatGPT free, Microsoft Copilot, Rytr, Copy.ai; date `"2026-04-20"`; weight 78
- Created `scripts/images/generate_free_ai_writing_tools.py` — Productivity silo, indigo accent `#6366f1`
- Generated `static/img/free-ai-writing-tools.webp` (30 KB, 1200×630)
- Added internal link from `grammarly-alternatives` → `free-ai-writing-tools` (Our verdict)
- Added internal link from `free-note-taking-apps` → `free-ai-writing-tools` (Our verdict)
- Added internal link from `notion-alternatives` → `free-ai-writing-tools` (Our verdict)
- Article links back to `grammarly-alternatives` (twice) and `free-note-taking-apps`
- Updated `lastmod` on `grammarly-alternatives`, `free-note-taking-apps`, `notion-alternatives` to `"2026-04-20"`
- Updated `CONTENT-STRATEGY.md`: `free-ai-writing-tools` marked as ✓ Published
- Hugo build passed — 278 pages, article visible on homepage latest and Productivity category
- No future dates found — all existing articles have dates ≤ 2026-04-18
- Site now has 29 articles total; Productivity silo has 6

### Day 38a — CLAUDE.md day-labeling rule
- Added day-labeling rule to `CLAUDE.md`: multiple runs on the same SGT calendar day use letter suffixes (Day 37a, 37b, etc.); new day number starts at 12:00 AM Asia/Singapore time
- Rule applies to tracker logging only — does not affect article publish dates

### Day 37 — branding cleanup
- Updated public-facing brand name from `FreeStackFinder` to `Free Stack Finder` across config, layouts, schema, and all static content pages
- `config.toml` title changed to `Free Stack Finder` — propagates to all `{{ .Site.Title }}` uses (page titles, OG tags, Twitter tags, RSS feed, aria-labels)
- Footer copyright line updated to `Free Stack Finder`
- `layouts/partials/schema.html`: all three JSON-LD `"name"` values updated to `Free Stack Finder`
- `layouts/index.html`: trust section aria-label updated
- `content/_index.md`, `about.md`, `disclaimer.md`, `terms.md`, `privacy-policy.md`, `contact.md`: all prose references updated
- Logo visual in nav and footer kept as compact `FreeStack<span>Finder</span>` form
- `author: "FreeStackFinder Team"` kept as compact byline across article front matter
- Domain, paths, repo, and technical identifiers unchanged

### Day 36
- Created `content/creative/free-font-websites.md` — 5 tools: Google Fonts, Font Squirrel, DaFont, Fontsource, 1001 Fonts; date `"2026-04-17"`
- Created `scripts/images/generate_free_font_websites.py` — Creative silo, orange accent
- Generated `static/img/free-font-websites.webp` (30 KB, 1200×630)
- Added internal link from `canva-alternatives` → `free-font-websites` (Our verdict)
- Added internal link from `figma-alternatives` → `free-font-websites` (Our verdict)
- Added internal link from `illustrator-alternatives` → `free-font-websites` (Our verdict)
- Article links back to `free-stock-photos`, `canva-alternatives`, `illustrator-alternatives`, and `figma-alternatives`
- Updated `CONTENT-STRATEGY.md`: `free-font-websites` marked as ✓ Published
- Site now has 28 articles total; Creative silo has 6

### Day 35e - workflow cadence update
- Clarified the repo workflow so daily runs stay focused on content work, build checks, light QA, and tracker updates, while weekly and monthly review passes belong to Codex

### Day 35d - git ignore cleanup
- Added the local settings folder to git ignore rules and removed it from version tracking without deleting the local copy

### Day 35c - unresolved cleanup pass
- Replaced the broken Formspree placeholder in `content/contact.md` with direct email links to `hello@freestackfinder.com`
- Updated `CLAUDE.md` wording around `verdict-box` so the rules match the actual repo state: legacy styles still exist, but new content should not add more
- Aligned `README.md` with `CLAUDE.md`:
  - removed outdated `featured:` and `faqs:` guidance
  - fixed the clone command typo
  - updated Hugo version guidance to 0.128.0
  - clarified that homepage popularity uses `weight`
  - clarified that the shared AdSense script is config-driven and `showAds` only controls in-article slots
- Renamed `content/business/quickbook-alternatives.md` to `content/business/quickbooks-alternatives.md` to match the public slug and tracker naming without changing the live URL
- Updated `lastmod` on the QuickBooks article to `"2026-04-17"`
- Moved the AdSense publisher ID into `config.toml` as the source of truth and updated `layouts/partials/head.html` to read the shared script from config
- Validation:
  - `hugo version` passed
  - `hugo --minify --cleanDestinationDir --destination .validation/public` passed
  - targeted `rg` sanity checks found no remaining `YOUR_FORM_ID`, `git.git`, `/business/quickbook-alternatives/`, `SearchAction`, `/all/`, or `/free-stack-guide/` strings in the generated validation output

### Day 35b — review hotfixes
- Reviewed repo instructions and tracker before changing implementation
- Guarded homepage `See all` links in `layouts/index.html` so `/all/` is not rendered unless that page exists
- Guarded the sidebar `free-stack-guide` CTA in `layouts/_default/single.html` so the link is not rendered unless that page exists
- Removed invalid homepage `SearchAction` schema from `layouts/partials/schema.html` because the site has no search feature
- Removed the missing publisher logo reference from `layouts/partials/schema.html`
- Corrected factual drift in published content:
  - `content/creative/figma-alternatives.md` — Adobe/Figma merger language corrected
  - `content/cloud/free-backup-software.md` — Google Photos storage claim corrected
  - `content/cloud/free-cloud-storage-comparison.md` — Google Docs/Sheets/Slides storage claim corrected
- Fixed internal link in `content/business/free-invoicing-software.md` to `/business/quickbooks-alternatives/`
- Updated `lastmod` on the edited article files to `"2026-04-17"`

### Day 35
- Created `content/creative/figma-alternatives.md` — 5 tools: Penpot, Lunacy, Plasmic, Quant UX, Figma Starter; date `"2026-04-17"`
- Created `scripts/images/generate_figma_alternatives.py` — Creative silo, orange accent
- Generated `static/img/figma-alternatives.webp` (27 KB, 1200×630)
- Added internal link from `canva-alternatives` → `figma-alternatives` (Our verdict)
- Added internal link from `illustrator-alternatives` → `figma-alternatives` (Our verdict)
- Added internal link from `free-stock-photos` → `figma-alternatives` (Our verdict)
- Added internal link from `photoshop-alternatives` → `figma-alternatives` (final recommendation)
- Article links back to `free-stock-photos`, `canva-alternatives`, and `illustrator-alternatives`
- Updated `CONTENT-STRATEGY.md`: `figma-alternatives` marked as ✓ Published
- Site now has 27 articles total; Creative silo has 5

### Day 34
- Logged new GSC snapshot: 2,220 impressions, 5 clicks, avg position 54.4, CTR 0.2% (vs prior baseline 1,420 / 4 / 51.8 / 0.3%)
- Read: impressions growing steadily (+56%), clicks still very low, CTR weak, avg position drifted slightly deeper — visibility is compounding but ranking depth and title/meta click appeal still need work
- Reordered priorities around continued publishing, targeted CTR work on impression-earning pages, and tightening internal linking in Productivity + Business clusters
- Next content action: publish `figma-alternatives` (Creative silo, next in Early queue)

### Day 33
- Cleaned up `CLAUDE.md` operating rules
- Fixed article date rule: live articles must not use future dates, duplicate dates are allowed on the same publish day, no more inflating dates forward for uniqueness
- Added a concise `Coding and change discipline` section adapted from external best-practice rules — covers think-before-acting, surgical changes, simplicity, and verify-before-claiming-done
- Preserved all existing FreeStackFinder-specific rules (feature image WebP, Python/Pillow, `scripts/images/`, commit/deploy, no AI mentions)
- Verified no duplicate or conflicting sections remain in `CLAUDE.md`

### Day 32
- Updated tracker "Read this first" and "Default daily scope" to align with CLAUDE.md focused day activity model
- Created `content/business/free-time-tracking-software.md` — 5 tools: Clockify, Toggl Track, RescueTime Lite, TimeCamp, Harvest; date `"2026-04-16"`
- Created `scripts/images/generate_free_time_tracking_software.py` — Business silo, emerald accent
- Generated `static/img/free-time-tracking-software.webp` (29 KB, 1200×630)
- Added internal link from `free-invoicing-software` → `free-time-tracking-software` (Our verdict)
- Added internal link from `free-project-management-software` → `free-time-tracking-software` (Our verdict)
- Article links back to `free-invoicing-software` and `free-project-management-software`
- Site now has 26 articles total; Business silo has 5

### Day 31
- Fixed duplicate publish dates across all 25 articles — each article now has a unique `date`
- 7 articles had dates moved forward; 1 article (photoshop-alternatives) had unquoted dates corrected to quoted strings
- `lastmod` updated to match the new `date` for all 7 changed articles
- No titles, slugs, content, weights, or images changed
- Final date range: 2025-01-15 (photoshop) through 2026-04-15 (free-stock-photos), all unique

Date changes:
- `canva-alternatives`: `"2026-03-16"` → `"2026-03-19"`
- `grammarly-alternatives`: `"2026-03-16"` → `"2026-03-20"`
- `zoom-alternatives`: `"2026-03-18"` → `"2026-03-21"`
- `dropbox-alternatives`: `"2026-04-02"` → `"2026-04-08"`
- `free-antivirus-software`: `"2026-04-02"` → `"2026-04-09"`
- `free-screen-recording-software`: `"2026-04-10"` → `"2026-04-11"`
- `free-stock-photos`: `"2026-04-13"` → `"2026-04-15"`
- `photoshop-alternatives`: unquoted `2025-01-15` → quoted `"2025-01-15"` (value unchanged)

### Day 30
- Converted all 25 article feature images from JPEG to WebP using Python + Pillow (quality 82, method 4)
- Total WebP savings: ~807 KB vs Day 29 compressed JPEGs (1882 KB → 1074 KB total, ~43% reduction)
- Deleted all 25 article `.jpg` files from `static/img/` — only `.webp` feature images remain
- Updated all 25 article front matter `image` paths from `.jpg` → `.webp`
- Updated all 4 generator scripts in `scripts/images/` to output `.webp` instead of JPEG; regenerated their 4 images
- CLAUDE.md `Feature image rules` and `Feature image SEO rules` sections were already present with correct WebP/SEO rules — no changes needed
- `default-article.jpg` (fallback) and `nordpass-banner.png`/`nordvpn-banner.png` (unreferenced) left untouched

### Day 29
- Deleted `static/img/best-free-canva-alternatives-2026-featured-image.png` — 1.7 MB unreferenced PNG removed from repo; article already updated to use `canva-alternatives.jpg` in Day 28
- Re-compressed all 26 JPEGs in `static/img/` from quality 92 → quality 82 using Python + Pillow; total JPEG savings ~802 KB
- Combined first-party image payload reduction: ~2.5 MB (PNG deletion + JPEG compression)
- Day 28 changes (defer on main.js, preconnect for AdSense, featured image dimensions, aspect-ratio CSS) are confirmed deployed; mobile PageSpeed test at 11:39:59 on Apr 14 was a pre-deployment cache hit
- Remaining CLS 0.270 on homepage is from AdSense auto-ads injecting content — third-party, not fixable from code without removing ads

### Day 28
- Fixed `canva-alternatives.md` image path: was referencing 1.7 MB PNG; now uses 244 KB `canva-alternatives.jpg`
- Added `defer` to `/js/main.js` reference in `layouts/_default/baseof.html` — removes render-blocking JS flag in Lighthouse
- Added `<link rel="preconnect">` and `<link rel="dns-prefetch">` for `pagead2.googlesyndication.com` in `layouts/partials/head.html` — reduces AdSense connection latency
- Added `width="1200" height="630" decoding="async"` to featured image `<img>` in `layouts/_default/single.html` — browser can reserve correct layout space before image loads
- Added `aspect-ratio: 1200 / 630` and `object-fit: cover` to `.article-featured-image` in `static/css/style.css` — prevents CLS on all article pages from image load
- Homepage CLS 0.78 on `body.is-home` is from AdSense auto-ads injecting content — third-party issue, not fixable from code without removing ads; documented as expected

### Day 27
- Created `scripts/images/image_helpers.py` — shared module with font loader, text truncation, word-wrap, rounded-rect, circle, draw_chrome, draw_featured_card, draw_grid, draw_bar, and output-path helper
- Rewrote `scripts/images/generate_free_note_taking_apps.py` — completely rebuilt to match standard template: macOS chrome, sidebar note list, main editor area with wrapped content, proper font fallbacks via helpers
- Updated `scripts/images/generate_free_invoicing_software.py` — migrated to helpers; added truncation on all variable-length strings; fixed item description overflow in line-item rows; improved button/badge positioning
- Updated `scripts/images/generate_free_stock_photos.py` — migrated to helpers; fixed badge overflow; added truncation on photo labels and stats text
- Created `scripts/images/generate_free_crm_software.py` — new script; Business silo; left panel shows contacts table with pipeline bar and stage pills; featured card: HubSpot; grid: Zoho CRM, Freshsales, Bitrix24, Notion CRM
- Regenerated all 4 images into `static/img/`: free-note-taking-apps.jpg, free-invoicing-software.jpg, free-stock-photos.jpg, free-crm-software.jpg — all 1200×630 JPEG
- All front matter image paths verified to match generated filenames
- Remaining image scripts: none — 21 other article images in static/img/ have no generator scripts and appear as static files from prior work; future articles should use the helpers module

### Day 26
- Created `CONTENT-STRATEGY.md` in repo root — captures 50-article content plan, 30-day SEO action plan, realism check and income timeline, permanent weekly workflow, monthly maintenance checklist, and growth milestones
- Updated tracker priorities to align with the 50-article content strategy and content pipeline order
- No article published; no site content changed

### Day 25
- Moved all 3 feature-image generator scripts from repo root into `scripts/images/`
  - `generate_free_invoicing_software.py`
  - `generate_free_stock_photos.py`
  - `generate_free_note_taking_apps.py`
- Updated `os.path.dirname(__file__)` output paths in all three to use `../..` so `static/img/` still resolves correctly from the new location
- Deleted old root-level copies
- Updated script path references in this tracker (Day 24b and Day 24 entries)
- `CLAUDE.md` repo structure already listed `scripts/images/` — no change needed there

### Day 24b — hotfix
- Fixed missing feature image for `free-invoicing-software` — copied `free-crm-software.jpg` as same-silo (Business, #10b981) placeholder; `scripts/images/generate_free_invoicing_software.py` exists and is ready to run when Python+Pillow available
- Fixed missing feature image for `free-stock-photos` (same Day 19 root cause) — copied `canva-alternatives.jpg` as same-silo (Creative) placeholder; run `scripts/images/generate_free_stock_photos.py` when Python available

### Day 24
- Created `content/productivity/free-note-taking-apps.md` — covers Google Keep, Apple Notes, Standard Notes, Simplenote, Notion free (5 tools)
- Added Grammarly affiliate CTA (using grammarly.com — no tracking URL confirmed yet)
- Added internal link from `notion-alternatives.md` → `free-note-taking-apps` (in Our verdict section)
- Added internal link from `grammarly-alternatives.md` → `free-note-taking-apps` (in Our verdict section)
- Article cross-links back to `notion-alternatives` and `grammarly-alternatives`
- Feature image: placeholder from notion-alternatives.jpg — run `scripts/images/generate_free_note_taking_apps.py` when Python is available
- Site now has 25 articles total; Productivity silo has 5

### Day 23
- Replaced `<!-- NORDVPN_AFFILIATE -->` placeholder comment in `content/security/free-password-managers.md` with live affiliate CTA block
- CTA placed in the "A note on NordPass" section — targets NordVPN users already on the page
- Note: NordPass affiliate URL not yet confirmed as tracking link — using `https://nordpass.com` until specific affiliate URL is available

### Day 22
- Replaced NordVPN placeholder comment in `content/security/free-vpn.md` with live affiliate CTA block
- CTA placed in "When to pay for a VPN" section — highest-intent placement for upgrade conversion
- Affiliate link: go.nordvpn.net (same as antivirus, email, and 2FA pages)

### Day 21
- Added Google AdSense script (ca-pub-5934721249825043) to `layouts/partials/head.html`
- Replaced the commented-out placeholder block with the live script — loads site-wide on every page

### Day 20
- Added NordVPN affiliate CTA to `best-free-2fa-apps.md` (before Our verdict — VPN + 2FA security pairing)

### Day 19
- Created `content/business/free-invoicing-software.md` because it was referenced in the log but missing from disk
- Created `content/creative/free-stock-photos.md`
- Added internal links in 6 existing articles:
  - `quickbooks-alternatives` → `free-invoicing-software`
  - `free-crm-software` → `free-invoicing-software`
  - `free-project-management-software` → `free-invoicing-software`
  - `canva-alternatives` → `free-stock-photos`
  - `photoshop-alternatives` → `free-stock-photos`
  - `illustrator-alternatives` → `free-stock-photos`
- Added image generator scripts for both new articles
- Site now has 24 articles total
- All 6 silos now have 4 articles each

### Day 18
- Added NordVPN CTA to `free-email-service.md`

### Day 17
- Fixed category page sorting in `layouts/_default/list.html`
- Fixed latest section sorting in `layouts/index.html`

### Day 15
- Updated titles on Slack and Microsoft Office pages based on GSC queries

---

## Next-task decision rules
When choosing the next task:
1. Fix broken, missing, or inconsistent work first
2. Then strengthen monetization on strong intent pages
3. Then improve internal linking inside one silo
4. Then add one new article only if no higher-value task exists
5. Avoid broad audits unless something appears inconsistent

---

## Default daily scope
A normal daily run should touch only:
- this tracker
- the files needed for the day activity (article, image script, internal links)
- up to 5 related files if the activity spans an article + linking batch
- one image script if creating an article

Do not scan unrelated silos, layouts, or directories unless necessary.

---

## Inventory reference

### Productivity
- `grammarly-alternatives.md`
- `microsoft-office-alternatives.md`
- `notion-alternatives.md`
- `slack-alternatives.md`
- `free-note-taking-apps.md`
- `free-ai-writing-tools.md`
- `free-chatgpt-alternatives.md`
- `free-calendar-app.md`

### Creative
- `canva-alternatives.md`
- `photoshop-alternatives.md`
- `illustrator-alternatives.md`
- `free-stock-photos.md`
- `figma-alternatives.md`
- `free-font-websites.md`

### Cloud
- `free-cloud-storage-comparison.md`
- `dropbox-alternatives.md`
- `free-email-service.md`
- `free-backup-software.md`

### Business
- `quickbooks-alternatives.md`
- `free-crm-software.md`
- `free-project-management-software.md`
- `free-invoicing-software.md`
- `free-time-tracking-software.md`

### Security
- `free-password-managers.md`
- `free-antivirus-software.md`
- `free-vpn.md`
- `best-free-2fa-apps.md`

### Video
- `free-video-editing-software.md`
- `zoom-alternatives.md`
- `premiere-pro-alternatives.md`
- `free-screen-recording-software.md`

---

## Internal link highlights
Keep these clusters growing naturally:

- Productivity cluster:
  - `microsoft-office-alternatives`
  - `grammarly-alternatives`
  - `notion-alternatives`
  - `slack-alternatives`
  - `free-note-taking-apps`
  - `free-ai-writing-tools`
  - `free-chatgpt-alternatives`
  - `free-calendar-app`

- Creative cluster:
  - `canva-alternatives`
  - `photoshop-alternatives`
  - `illustrator-alternatives`
  - `free-stock-photos`
  - `figma-alternatives`
  - `free-font-websites`

- Business cluster:
  - `quickbooks-alternatives`
  - `free-crm-software`
  - `free-project-management-software`
  - `free-invoicing-software`
  - `free-time-tracking-software`

- Security cluster:
  - `free-password-managers`
  - `free-antivirus-software`
  - `free-vpn`
  - `best-free-2fa-apps`

- Cloud cluster:
  - `free-cloud-storage-comparison`
  - `dropbox-alternatives`
  - `free-email-service`
  - `free-backup-software`

- Video cluster:
  - `free-video-editing-software`
  - `zoom-alternatives`
  - `premiere-pro-alternatives`
  - `free-screen-recording-software`

---

## Affiliate focus
Current high-value affiliate opportunities:
- Zoho: `free-crm-software`, `free-email-service`, `free-invoicing-software`
- NordVPN: `free-vpn`, `free-antivirus-software`, `dropbox-alternatives`, `free-email-service`, `best-free-2fa-apps`
- NordPass: `free-password-managers`
- Amazon Associates US (`freestackfi20-20`): `best-free-2fa-apps` (hardware security keys), `free-backup-software` (portable SSDs), `free-screen-recording-software` (USB microphones)
- Amazon Associates SG (`freestackfi20-22`): reserved for future SG-specific hardware content

---

## Pending actions
- Reddit post #3 is drafted for `r/entrepreneur`
- Zoho affiliate application still pending
- AdSense script is live (ca-pub-5934721249825043) — formal application/review still pending Google approval
- Impact.com reapply only after traffic grows further

---

## Notes for future runs
- Prefer strengthening an existing cluster before opening too many new topic branches
- Prefer high-intent pages with monetization potential
- Avoid random site-wide edits unless there is a clear inconsistency or bug
- Keep tracker concise and correct after every run
