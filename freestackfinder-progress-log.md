# FreeStackFinder — Project State

**Site:** freestackfinder.com  
**Last updated:** 2026-04-13  
**Current day:** 21  

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
- Total published articles: 24
- Silo balance: 4 articles in each of 6 silos
- Main monetization active: Amazon Associates, NordVPN, NordPass, Canva, Grammarly
- Pending affiliate priority: Zoho via CJ Affiliate
- GSC baseline to recheck: 1,420 impressions, 4 clicks, average position 51.8, CTR 0.3%
- Current site goal: grow useful content clusters, improve internal linking, strengthen monetization, and prepare for AdSense

---

## Current priorities
1. Post Reddit #3
2. Apply Zoho affiliate via CJ Affiliate
3. Recheck GSC after Day 15 title updates on Slack and Microsoft Office articles
4. Apply for AdSense
5. Expand the next best article cluster

### Next article candidates
- Productivity: `free-note-taking-apps` or `free-calendar-app`
- Business: `free-time-tracking-software`
- Creative: `free-font-websites`

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
