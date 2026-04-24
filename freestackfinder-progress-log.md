# FreeStackFinder — Project State

**Site:** freestackfinder.com  
**Last updated:** 2026-04-24  
**Current day:** 46f  

---

### Day 46f — reusable comparison-table component for key comparison articles
- Added `layouts/shortcodes/comparison-table.html` — YAML-driven Hugo shortcode that accepts a `columns` list (key + label) and `rows` list, so authors can reuse the same component across silos with different field sets without template edits
- Architecture chosen: shortcode + inline YAML via `transform.Unmarshal`, so the structured summary lives inside the article markdown where authors already edit content, rather than in front matter or a separate data file
- First-column cells render as `<th scope="row">`, remaining cells as `<td>` with `data-label` attributes for mobile card-style stacking; wrapper uses `role="region"` with an accessible label
- Added CSS section 31 to `static/css/style.css`: compact editorial table on desktop (uppercase micro-label header, muted body text, bordered `--bg-2` wrapper matching review-block/collection-card style); under 720px the thead hides and each row becomes a card with `data-label` prefixes, keeping the summary scannable on mobile without horizontal scroll
- Applied to 4 strong evergreen pages where a top-of-article summary clearly helps comparison scanning:
  - `content/business/free-accounting-software.md` — columns: Tool, Best for, Free plan, Main limitation
  - `content/creative/canva-alternatives.md` — columns: Tool, Best for, Free plan, Main limitation
  - `content/productivity/microsoft-office-alternatives.md` — columns: Tool, Best for, Free plan, Main limitation
  - `content/security/free-vpn.md` — columns: Tool, Best for, Free plan, Main limitation
- Kept tables to one row per tool covered in the article and deliberately durable free-plan wording (no brittle GB/seat numbers in the summary) so the row text ages well alongside the article body
- Not applied site-wide — rolled out only to these four high-intent evergreen guides for this run
- Hugo build passed — 308 pages, no errors; verified rendered `.compare-table-wrap` markup in `public/business/free-accounting-software/index.html`

---

### Day 46e — curated homepage featured collections
- Added a curated collections block to `layouts/index.html` between Featured comparisons and the Trust banner — three use-case cards that complement (not duplicate) the silo-driven Featured and chronological Latest sections
- Implementation uses an inline `slice`/`dict` structure with explicit page paths resolved via `.Site.GetPage`, so the curation is manual and editable in one place without new data files
- Collections added (each card: short heading + intro line + 5 linked guides, with a small silo tag per link):
  - "The freelance business stack" — `free-accounting-software`, `free-invoicing-software`, `free-crm-software`, `free-project-management-software`, `free-time-tracking-software`
  - "Replace Microsoft Office" — `microsoft-office-alternatives`, `free-spreadsheet-alternatives`, `free-note-taking-apps`, `free-calendar-app`, `grammarly-alternatives`
  - "Privacy and safety basics" — `free-password-managers`, `free-vpn`, `free-antivirus-software`, `best-free-2fa-apps`, `free-email-service`
- Added CSS section 30 to `static/css/style.css`: 3-column collection-card grid on desktop, collapses to 2-up under 960px and 1-up under 640px; uses existing `--bg-2`, `--border`, `--radius-lg`, `--primary`, `--text`, `--text-muted`, `--text-light` tokens so the block matches the site's editorial design language without a new visual style
- Creative was intentionally left out — Canva, Photoshop, and Illustrator already carry the creative entry points via the Featured comparisons block, and a forced Creative collection would feel like filler against the current inventory
- QA: 3 cards render on the homepage, 15 linked titles resolve via `Site.GetPage`, silo tags show next to each link; Featured, Trust, and Latest sections unchanged
- Hugo build passed — 308 pages, no errors

---

### Day 46b — reusable review/methodology trust block on article pages
- Added `layouts/partials/review-block.html` — compact 3-column editorial block showing Last reviewed date, How we evaluate, and What "free" means here; uses existing `.Lastmod` (the same freshness source already surfaced elsewhere) so the date source remains consistent with article meta and cards
- Gating: renders only when `not .Params.noindex`, `ne .Type "page"`, and `.Params.categories` is set — excludes `about`, `contact`, `disclaimer`, `privacy-policy`, `terms`, and `search`
- Wired into `layouts/_default/single.html` between the featured image and the article body, so it sits near the top of the content without competing with the article header meta and existing editorial-note
- Added CSS section 29 to `static/css/style.css`: 3-column grid on desktop, stacks to 1 column under 740px; uses existing `--bg-2`, `--border`, `--radius`, `--text`, `--text-muted`, `--text-light` tokens so the block matches the site's editorial design language
- Final wording:
  - Last reviewed: `{{ .Lastmod }}` formatted "January 2, 2006"
  - How we evaluate: "Practical usefulness, real free-plan value, the limits that matter, and fit by use case."
  - What "free" means here: "Some tools are fully free or open source. Others have limited free plans that are still genuinely useful."
- QA: confirmed block present on `business/free-accounting-software/` and `security/free-vpn/`, absent from `about/`, `privacy-policy/`, `contact/`; existing `article-editorial-note`, featured image, and author box untouched
- Hugo build passed — 308 pages, no errors

---

### Day 46a — free-accounting-software article
- Created `content/business/free-accounting-software.md` — 5 tools: Wave, Zoho Books, Akaunting, Manager, GnuCash; date `"2026-04-24"`; weight 76
- Article distinguishes accounting software from invoicing tools and spreadsheets, adds a decision guide, and keeps free-plan wording deliberately durable around Zoho Books' revenue cap, Wave's plan structure, Akaunting's cloud tier, and Manager's free desktop edition — each entry points readers to the vendor's current pricing page rather than quoting volatile thresholds
- Created `scripts/images/generate_free_accounting_software.py` — Business silo, emerald accent `#10b981`; left panel mocks a Wave dashboard (KPI cards + P&L ledger rows + net-profit band), right panel features Wave plus a 4-card grid (Zoho Books, Akaunting, Manager, GnuCash)
- Generated `static/img/free-accounting-software.webp` (31 KB, 1200×630)
- Added internal link from `quickbooks-alternatives` → `free-accounting-software` (Our verdict section, broader accounting comparison)
- Added internal link from `free-invoicing-software` → `free-accounting-software` (Our verdict section, full-accounting pairing)
- Existing internal link from `free-spreadsheet-alternatives` → `free-accounting-software` (previously added on Day 43a) now resolves
- Article cross-links back to `free-invoicing-software`, `free-spreadsheet-alternatives`, `quickbooks-alternatives`, `free-crm-software`, and `free-time-tracking-software`
- Updated `lastmod` on `quickbooks-alternatives` and `free-invoicing-software` to `"2026-04-24"`
- Updated `CONTENT-STRATEGY.md`: `free-accounting-software` marked as ✓ Published
- Hugo build passed — 308 pages, no errors
- Site now has 33 articles total; Business silo has 7

---

### Day 45d - Wave 2 archive quality and freshness refresh
- Audited the remaining untouched evergreen archive and prioritized seven older, high-visibility comparison pages across Business, Creative, Cloud, and Video
- Rewrote free-crm-software, photoshop-alternatives, canva-alternatives, free-cloud-storage-comparison, free-backup-software, free-video-editing-software, and premiere-pro-alternatives to improve intros, verdict quality, tradeoff clarity, and free-plan caveats
- Tightened risky wording around CRM seat limits, cloud storage quotas, backup expectations, and free video editor limits so the guides rely on more durable plan language instead of brittle free-plan promises
- Improved internal linking between related clusters including Canva/Photoshop, Premiere/video editing/screen recording, CRM/invoicing/project management, and cloud storage/backup/Dropbox alternatives
- Verified volatile product details against official vendor pages before refreshing current-plan wording for HubSpot, Zoho CRM, Freshsales, Bitrix24, Adobe Express, Canva, Microsoft Designer, Pixlr, MEGA, Google Drive, Box, OneDrive, iCloud, Proton Drive, Dropbox, Backblaze, Blackmagic Design, and CapCut
- Hugo validation build passed after the refresh - 305 pages, 11 paginator pages, no errors

---
### Day 45c â€” Wave 1 trust and content remediation pass
- Audited and strengthened the homepage, section/category pages, footer trust links, legal pages, and a focused set of high-visibility business and security articles
- Homepage trust fixes in `layouts/index.html`: removed the overstated "hundreds of free tools" claim, renamed the weight-driven homepage module from `Most popular comparisons` to `Featured comparisons`, added direct trust links in the hero, and expanded the trust strip to include transparent monetization and update policy language
- Structural trust fixes in templates:
  - `layouts/_default/list.html` now creates the date-sorted paginator before using it, preserving category sort behavior while adding a shared editorial note linking to About, Disclaimer, and Contact
  - `layouts/_default/single.html` now adds a concise editorial/disclosure note under article meta and softens the author box language to match the actual review process more closely
  - `layouts/partials/article-card.html` and homepage latest list now surface `Updated ...` dates when `lastmod` is newer than `date`
  - `layouts/partials/footer.html` now includes trust links (`How we test`, `Affiliate disclosure`, `Report outdated info`) and clearer utility-page labels
- Legal/trust page cleanup:
  - `content/about.md` adds a corrections/updates policy section and sharper editorial positioning
  - `content/disclaimer.md` removes vague affiliate-program wording and fixes the misleading "external-link icon means affiliate" implication
  - `content/privacy-policy.md` was rewritten to match the actual site setup: direct email contact, no current newsletter, AdSense/infrastructure cookies, and no public Google Analytics script
  - `content/terms.md` and `content/contact.md` were updated with April 2026 freshness and clearer, more intentional wording
- Utility-page SEO cleanup:
  - `layouts/partials/head.html` and `layouts/partials/schema.html` no longer emit article-style metadata or schema on `type: page` / `noindex` utility pages, removing bogus `article:published_time` and FAQ markup from legal pages
- Section page quality improvements:
  - `content/_index.md` and all 6 section `_index.md` files now describe methodology, common free-plan traps, and decision-critical limits more clearly
- Focused article remediation:
  - Business: `quickbooks-alternatives`, `free-invoicing-software`, and `free-project-management-software` now use more restrained free-plan wording, better decision guidance, and stronger internal links
  - Security: `free-password-managers` and `free-vpn` now use tighter, more durable verdict language; password manager links now connect into the rest of the security cluster
  - Stale NordVPN CTA pattern fixed across `free-vpn`, `free-antivirus-software`, `dropbox-alternatives`, and `free-email-service`: removed volatile monthly pricing copy and standardized to the verified current 10-device allowance
  - `notion-alternatives` description softened from an overly absolute "completely free forever" claim
- Hugo validation build passed after the pass and after the utility-page metadata cleanup â€” 305 pages, no errors

---

### Day 45b — header layout rework and search UI polish
- Restructured `layouts/partials/nav.html`: logo → primary nav → actions group (search icon + mobile toggle) on the far right; nav items now sit inline next to the logo
- Updated `.header-inner` in `static/css/style.css`: removed `justify-content: space-between`, added `.header-actions` with `margin-left: auto` to anchor search to the far right; increased header gap to 28px for breathing room
- Polished search page styling in CSS section 28: larger H1, narrower container (760px), bigger input (15px padding, subtle shadow, hover state, `appearance: none` to kill UA chrome and webkit search decorations), chip-style filter buttons with focus-visible ring, active-state shadow, and refined mobile sizing
- Nav unchanged in content: Cloud present, About not in primary nav (as expected)
- Hugo build passed — 305 pages, no errors

---

### Day 45a — site search and category filtering
- Architecture: Hugo JSON output format → `/index.json` static search index (32 entries) + vanilla JS search, no external libraries
- Added `JSON` to `[outputs] home` in `config.toml` → Hugo generates `/index.json` at build time
- Created `layouts/index.json` — builds search index from all published pages, excludes pages with `noindex: true` (legal/utility pages)
- Created `content/search.md` — dedicated search page, `noindex: true`, `sitemap: disable: true`
- Created `layouts/_default/search.html` — search page layout: search input, 7 filter buttons (All + 6 silos), results container
- Created `static/js/search.js` — vanilla JS: fetches `/index.json` on page load, filters by query (title + description substring match) and category, highlights matches, debounced input (150ms), reads `?q=` URL param on load
- Added search icon link (`/search/`) to `layouts/partials/nav.html` — visible on all pages, desktop and mobile
- Added `{{ block "scripts" . }}{{ end }}` to `layouts/_default/baseof.html` — allows page-specific scripts before `</body>`; `search.js` loads only on the search page
- Added CSS section 28 to `static/css/style.css`: `.nav-search-btn`, `.search-page`, `.search-bar`, `.search-filters`, `.filter-btn`, `.search-results-list`, `.search-result-item`, `.sr-only`, `mark` highlight, mobile overrides
- QA: 32 entries in index, all 6 categories, no utility/legal pages included; `noindex` on search page confirmed; search icon on all pages; `search.js` only on `/search/`; regular article pages unaffected
- Hugo build passed — 305 pages, no errors

---

### Day 46d — targeted Productivity and Business cluster link pass
- Reviewed only the listed Productivity and Business cluster pages for adjacent-guide gaps, with no new article and no title or description churn
- Added Productivity links from `slack-alternatives` to `microsoft-office-alternatives` and from `free-note-taking-apps` to `microsoft-office-alternatives`
- Added Business links from `quickbooks-alternatives` to `free-crm-software`, from `free-invoicing-software` to `free-spreadsheet-alternatives`, from `free-time-tracking-software` to `free-crm-software`, and from `free-spreadsheet-alternatives` to `free-time-tracking-software`
- Replaced one loose off-cluster recommendation on `quickbooks-alternatives` with a more relevant Business-cluster path into client pipeline software
- Updated `lastmod` on changed pages where the date was not already current
- Hugo build passed — 308 pages, no errors

---

### Day 46c — targeted CTR and internal-link review pass
- Reviewed the priority Productivity and Business pages for search-facing title/description strength and cluster-link gaps, using the tracker priorities and published cluster structure as the selection basis
- Updated title/meta positioning where the old version was less direct or less search-intent aligned:
  - `microsoft-office-alternatives`: broadened from singular "Alternative" to "Alternatives" and surfaced docs, sheets, and slides intent
  - `notion-alternatives`: moved the exact "Notion alternatives" phrase forward and clarified notes, wikis, and offline options
  - `grammarly-alternatives`: moved the exact "Grammarly alternatives" phrase forward and clarified grammar, style, and clarity intent
  - `free-project-management-software`: surfaced Trello, Asana, ClickUp, and broader small-team intent
  - `free-crm-software`: kept the no-credit-card hook while making the description more concrete around HubSpot, Zoho CRM, Freshsales, and Bitrix24
  - `free-invoicing-software`: tightened the description around freelancer/small-business search intent and named the key tools
- Strengthened internal links inside the Productivity cluster from `microsoft-office-alternatives` to `free-note-taking-apps` and `free-calendar-app`
- Strengthened internal links inside the Business cluster:
  - `free-project-management-software` now points naturally to `free-crm-software`
  - `free-crm-software` now points to `free-accounting-software`, `free-project-management-software`, and `free-time-tracking-software` in addition to existing QuickBooks and invoicing links
- Light QA confirmed the touched metadata and added links are present and no broad rewrite was introduced
- Hugo build passed — 308 pages, no errors

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
- Total published articles: 33
- Silo balance: Productivity 8, Creative 6, Business 7, Cloud 4, Security 4, Video 4
- Main monetization active: NordVPN, NordPass, Canva, Grammarly, Amazon Associates (US tag: freestackfi20-20 — now in use on 3 pages)
- Pending affiliate priority: Zoho via CJ Affiliate
- GSC latest (2026-04-15): 2,220 impressions, 5 clicks, average position 54.4, CTR 0.2%
- GSC prior baseline: 1,420 impressions, 4 clicks, average position 51.8, CTR 0.3%
- GSC read: impressions improving (+56%), clicks still low (+1), CTR weak (0.2%), avg position slipped slightly — visibility growing but ranking depth and click appeal still need work
- Current site goal: grow useful content clusters, improve internal linking, strengthen monetization, and prepare for AdSense

---

## Current priorities
1. Continue publishing from the Early queue — next up: `free-pdf-editor-alternatives` (Productivity silo)
2. Targeted CTR improvement on pages already earning impressions — pull GSC query/page report and rework titles + meta descriptions on pages with impressions but near-zero CTR
3. Strengthen internal linking inside the two strongest clusters (Productivity, Business)
4. Apply Zoho affiliate via CJ Affiliate — Zoho referenced on crm, email, and invoicing pages
5. Post Reddit #3 for `r/entrepreneur`
6. Continue growing clusters to 50 articles — see `CONTENT-STRATEGY.md`

### Content pipeline — next articles to publish (Priority: Early)
Publish in this order unless a higher-priority fix exists:

- `free-pdf-editor-alternatives` — Productivity silo
- `free-resume-builders` — Business silo

Full 50-article plan with silo targets and Later-queue articles is in `CONTENT-STRATEGY.md`.

---

## Current content state

### Silo counts
- Productivity: 8
- Creative: 6
- Cloud: 4
- Business: 7
- Security: 4
- Video: 4

### Homepage featured comparisons
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

### Day 44a — full-site quality and trust audit pass
- Audited all 32 published articles across 6 silos, all 6 section index pages, and trust/legal pages
- **Fixed:** Removed internal dev note from `content/business/free-crm-software.md` ("— affiliate program available via CJ Affiliate once traffic grows") — this was visible in published content, a trust and editorial quality issue
- **Fixed:** Updated stale "Last updated: January 2025" date in `content/about.md` → April 2026
- **Fixed:** Updated stale "Last updated: January 2025" date in `content/disclaimer.md` → April 2026
- **Fixed:** Corrected affiliate programs list in `content/disclaimer.md` — removed Impact.com and ShareASale (not active), replaced with accurate list: Amazon Associates, NordVPN, NordPass, Canva, Grammarly affiliate programs
- **Improved:** Strengthened `content/video/_index.md` from 1 sentence to 2 sentences with testing methodology note
- Audit confirmed: all main articles are solid, specific, honest, and appropriately structured — no thin, generic, or misleading content found beyond the issues above
- Hugo build passed — 303 pages, no errors

### Day 43e — homepage trust badge copy fix
- In `layouts/index.html`: replaced `✓ No affiliate bias` with `✓ Clear tradeoffs` in the hero badge row
- Reason: the original phrasing was inaccurate — the site does use affiliate links; "No affiliate bias" is an unverifiable absolute claim
- Final row: `Actually tested · Honest limitations · Clear tradeoffs`
- Hugo build passed — 303 pages, no errors

### Day 43d — fix header nav: replace About with Cloud
- In `config.toml` `[menu]` block: replaced `About /about/ weight=6` with `Cloud /cloud/ weight=6`
- Nav now shows: Creative · Productivity · Video · Business · Security · Cloud
- About remains in footer nav (hardcoded in `footer.html`) — unaffected
- Hugo build passed — 303 pages, no errors

### Day 43c — back-to-top button
- Added `<button id="back-to-top">` with inline chevron SVG to `layouts/_default/baseof.html` — renders site-wide
- Added CSS (section 27) to `static/css/style.css`: fixed bottom-right 44×44 circle using `--primary` color, hidden by default (`opacity: 0; visibility: hidden; transform: translateY(8px)`), `.visible` class fades/slides it in
- Added JS to `static/js/main.js`: scroll listener shows button after 400px scroll; click scrolls to top with `behavior: smooth`; scroll listener uses `{ passive: true }`
- Accessibility: `aria-label="Back to top"`, keyboard focusable, `:focus-visible` outline using `--primary`, icon uses `aria-hidden`
- Mobile: bottom/right reduced to 16px on screens < 640px; hidden in print styles
- Hugo build passed — 303 pages, no errors

### Day 43b — noindex utility/legal pages
- Set `noindex: true` and `sitemap: { disable: true }` in front matter of all 5 utility pages: `about.md`, `contact.md`, `disclaimer.md`, `terms.md`, `privacy-policy.md`
- Head partial already wired `{{ if .Params.noindex }}` → `noindex, follow` — no layout changes needed
- QA confirmed: all 5 pages render `<meta name="robots" content="noindex, follow" />`
- QA confirmed: sitemap.xml contains zero references to these 5 pages
- QA confirmed: content pages (e.g. `free-spreadsheet-alternatives`) still render `index, follow`
- Hugo build passed — 303 pages, no errors

### Day 43a — free-spreadsheet-alternatives article
- Created `content/business/free-spreadsheet-alternatives.md` — 5 tools: Google Sheets, LibreOffice Calc, Zoho Sheet, ONLYOFFICE, Airtable; date `"2026-04-23"`; weight 78
- Created `scripts/images/generate_free_spreadsheet_alternatives.py` — Business silo, emerald accent `#10b981`
- Generated `static/img/free-spreadsheet-alternatives.webp` (32 KB, 1200×630)
- Added internal link from `microsoft-office-alternatives` → `free-spreadsheet-alternatives` (Our recommendation)
- Added internal link from `quickbooks-alternatives` → `free-spreadsheet-alternatives` (Our verdict)
- Article links back to `free-project-management-software`, `free-crm-software`, `free-invoicing-software`, `free-accounting-software`, and `microsoft-office-alternatives`
- Updated `lastmod` on `microsoft-office-alternatives` and `quickbooks-alternatives` to `"2026-04-23"`
- Updated `CONTENT-STRATEGY.md`: `free-spreadsheet-alternatives` marked as ✓ Published
- Hugo build passed — 303 pages, no errors
- Site now has 32 articles total; Business silo has 6

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
- `free-spreadsheet-alternatives.md`
- `free-accounting-software.md`

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
  - `free-spreadsheet-alternatives`
  - `free-accounting-software`

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
