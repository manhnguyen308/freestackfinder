# FreeStackFinder — Project State

**Site:** freestackfinder.com  
**Last updated:** 2026-04-14  
**Current day:** 27  

---

## Read this first
This is the primary daily state file.

Rules for daily runs:
- Use this file as the main source of current project truth
- Do not perform a broad repo audit unless this file is clearly outdated or inconsistent with the task
- Choose exactly one meaningful task per run
- Inspect only the files needed for that task
- If repo files conflict with this tracker, trust the files and then correct this tracker

---

## Current snapshot
- Stack: Hugo 0.128.0 + GitHub + Cloudflare Pages
- Total published articles: 25
- Silo balance: Productivity 5, all others 4
- Main monetization active: Amazon Associates, NordVPN, NordPass, Canva, Grammarly
- Pending affiliate priority: Zoho via CJ Affiliate
- GSC baseline to recheck: 1,420 impressions, 4 clicks, average position 51.8, CTR 0.3%
- Current site goal: grow useful content clusters, improve internal linking, strengthen monetization, and prepare for AdSense

---

## Current priorities
1. Apply Zoho affiliate via CJ Affiliate — Zoho referenced on crm, email, and invoicing pages
2. Recheck GSC after Day 15 title updates on Slack and Microsoft Office articles
3. Post Reddit #3 for `r/entrepreneur`
4. Publish next article from the Early queue (see content pipeline below)
5. Continue growing clusters to 50 articles — see `CONTENT-STRATEGY.md`

### Content pipeline — next articles to publish (Priority: Early)
Publish in this order unless a higher-priority fix exists:

- `free-time-tracking-software` — Business silo
- `figma-alternatives` — Creative silo
- `free-font-websites` — Creative silo
- `free-ai-writing-tools` — Productivity silo
- `free-chatgpt-alternatives` — Productivity silo
- `free-calendar-app` — Productivity silo
- `free-spreadsheet-alternatives` — Business silo
- `free-accounting-software` — Business silo
- `free-pdf-editor-alternatives` — Productivity silo
- `free-resume-builders` — Business silo

Full 50-article plan with silo targets and Later-queue articles is in `CONTENT-STRATEGY.md`.

---

## Current content state

### Silo counts
- Productivity: 4
- Creative: 4
- Cloud: 4
- Business: 4
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

---

## Recent completed work

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
- one target file or one feature
- up to 3 related files if needed
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

### Creative
- `canva-alternatives.md`
- `photoshop-alternatives.md`
- `illustrator-alternatives.md`
- `free-stock-photos.md`

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

- Creative cluster:
  - `canva-alternatives`
  - `photoshop-alternatives`
  - `illustrator-alternatives`
  - `free-stock-photos`

- Business cluster:
  - `quickbooks-alternatives`
  - `free-crm-software`
  - `free-project-management-software`
  - `free-invoicing-software`

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
