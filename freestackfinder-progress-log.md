# FreeStackFinder — Build Progress Log

**Site:** freestackfinder.com  
**Stack:** Hugo + GitHub + Cloudflare Pages  
**Started:** Week 1 (Day 1)  
**Log updated:** Day 16

---

## Site overview

| Item | Detail |
|------|--------|
| Stack | Hugo (static site generator), GitHub, Cloudflare Pages |
| Monetisation | Amazon Associates (US: freestackfi20-20, SG: freestackfi20-22), NordVPN direct, NordPass direct, Canva direct, Grammarly direct |
| Affiliate status | NordVPN ✅ Active · NordPass ✅ Active · HubSpot ❌ requires established company (deferred) · Impact.com ❌ denied (reapply at traffic threshold) · Zoho via CJ Affiliate (apply at ~5k monthly visitors) |
| GSC data (Day 11) | 1,420 impressions · 4 clicks · Avg position 51.8 · CTR 0.3% |
| Top GSC queries | slack alternatives (71 imp) · ms office alternative variants (127 imp combined) · canva pro free (2 clicks) |
| Total articles | 20 (after Day 16) |
| Reddit posts | 2 published · 1 drafted (Day 15) |

---

## Content silo status

| Silo | Articles | Target | Status |
|------|----------|--------|--------|
| Productivity | 4 | 4+ | ✅ |
| Creative | 3 | 3+ | ✅ |
| Video | 4 | 3+ | ✅ +1 |
| Business | 3 | 3+ | ✅ |
| Security | 3 | 3+ | ✅ |
| Cloud | 4 | 3+ | ✅ +1 |

---

## All published articles (20 total)

### Productivity silo (4 articles)

| # | File | Title | Date | Weight |
|---|------|-------|------|--------|
| 1 | grammarly-alternatives.md | Best Free Alternatives to Grammarly in 2026 | 2026-03-16 | 55 |
| 2 | microsoft-office-alternatives.md | Best Free Microsoft Office Alternative in 2026 | 2026-04-07 | 90 |
| 3 | slack-alternatives.md | Best Free Slack Alternatives in 2026 | 2026-04-07 | 95 |
| 4 | notion-alternatives.md | Best Free Alternatives to Notion in 2026 | 2026-03-26 | 70 |

### Creative silo (3 articles)

| # | File | Title | Date | Weight |
|---|------|-------|------|--------|
| 5 | canva-alternatives.md | Best Free Alternatives to Canva in 2026 | 2026-03-16 | 85 |
| 6 | photoshop-alternatives.md | Best Free Alternatives to Adobe Photoshop in 2026 | 2026-04-04 | 60 |
| 7 | illustrator-alternatives.md | Best Free Alternatives to Adobe Illustrator in 2026 | 2026-04-03 | 40 |

### Cloud silo (4 articles)

| # | File | Title | Date | Weight |
|---|------|-------|------|--------|
| 8 | free-cloud-storage-comparison.md | Best Free Cloud Storage in 2026 | 2026-03-16 | 75 |
| 9 | dropbox-alternatives.md | Best Free Dropbox Alternatives in 2026 | 2026-04-02 | 35 |
| 10 | free-email-service.md | Best Free Email Service in 2026 | 2026-04-06 | 68 |
| 11 | free-backup-software.md | Best Free Backup Software in 2026 | 2026-04-08 | 58 |

### Business silo (3 articles)

| # | File | Title | Date | Weight |
|---|------|-------|------|--------|
| 12 | quickbooks-alternatives.md | Best Free Alternatives to QuickBooks in 2026 | 2026-03-18 | 50 |
| 13 | free-crm-software.md | Best Free CRM Software in 2026 | 2026-04-02 | 37 |
| 14 | free-project-management-software.md | Best Free Project Management Software in 2026 | 2026-04-05 | 72 |

### Security silo (3 articles)

| # | File | Title | Date | Weight |
|---|------|-------|------|--------|
| 15 | free-password-managers.md | Best Free Password Managers in 2026 | 2026-03-27 | 80 |
| 16 | free-antivirus-software.md | Best Free Antivirus Software in 2026 | 2026-04-02 | 38 |
| 17 | free-vpn.md | Best Free VPN in 2026 | 2026-04-04 | 36 |

### Video silo (4 articles)

| # | File | Title | Date | Weight |
|---|------|-------|------|--------|
| 18 | free-video-editing-software.md | Best Free Video Editing Software in 2026 | 2026-03-17 | 65 |
| 19 | zoom-alternatives.md | Best Free Alternatives to Zoom in 2026 | 2026-03-18 | 58 |
| 20 | premiere-pro-alternatives.md | Best Free Alternatives to Adobe Premiere Pro in 2026 | 2026-03-25 | 52 |
| 21 | free-screen-recording-software.md | Best Free Screen Recording Software in 2026 | 2026-04-07 | 62 |

---

## Homepage "Most popular" ranking (weight-based)

The homepage `index.html` shows the top 6 articles by `weight` value. Update weights in front matter as GSC data changes.

| Rank | Article | Weight | Basis |
|------|---------|--------|-------|
| 1 | slack-alternatives | 95 | 71 GSC impressions — highest single keyword |
| 2 | microsoft-office-alternatives | 90 | 127 impressions combined variants |
| 3 | canva-alternatives | 85 | Only article generating actual clicks |
| 4 | free-password-managers | 80 | High intent keyword + affiliate value |
| 5 | free-cloud-storage-comparison | 75 | Strong evergreen keyword |
| 6 | free-project-management-software | 72 | High-volume Business silo anchor |

**To update:** change `weight:` in the article front matter and redeploy. No code changes needed.

---

## Technical changes log

### Day 10 — Front matter and internal links
- Added internal links to 4 existing articles pointing to notion-alternatives and free-password-managers
- Published Articles 10 (notion-alternatives), 11 (free-password-managers), 12a (free-antivirus), 12b (free-crm), 12c (dropbox-alternatives)

### Day 11 — GSC analysis + Article 13
- First GSC data: 1,420 impressions, 4 clicks
- Published Article 13: illustrator-alternatives (Creative silo)
- Task widget redesigned to match screenshot-style format with expandable steps

### Day 12 — Homepage fix + weight system + affiliate setup
- **Bug fixed:** `index.html` was using `featured: true` which only matched 2 articles. Replaced with `(.ByParam "weight").Reverse` — shows top 6 articles by weight
- **Bug fixed:** `photoshop-alternatives.md` and `microsoft-office-alternatives.md` had `faqs:` YAML block with dangling child items after key removal → caused Cloudflare build failure. Fixed by stripping entire block including children
- Added `weight:` field to all 17 articles
- Published Article 14: free-vpn (Security silo)
- NordVPN affiliate link added: `https://go.nordvpn.net/aff_c?offer_id=15&aff_id=144937&url_id=902`
- NordPass affiliate link added: `https://go.nordpass.io/aff_c?offer_id=488&aff_id=144937&url_id=9356`

### Day 13 — Affiliate banner → text CTA fix + Article 15
- **Issue:** Image banners using affiliate URL parameters (`aff_id`, `offer_id`, `aff_c`) blocked by uBlock Origin / AdBlock Plus via EasyList. No fix possible without changing affiliate URL structure
- **Fix:** Replaced all `<div class="affiliate-banner"><img>` with `<div class="affiliate-cta">` text CTAs
- Added `.affiliate-cta` CSS to `static/css/style.css` — teal left-bordered card, green button, mobile-responsive
- Published Article 15: free-project-management-software (Business silo)
- HubSpot affiliate replaced with Zoho (open program, no traffic threshold via CJ Affiliate)

### Day 14 — Free email + progress log v1
- Published Article 16: free-email-service (Cloud silo — now at 3)
- Added cross-links: free-cloud-storage-comparison → free-email-service, free-crm-software → free-email-service
- Created freestackfinder-progress-log.md (this file, v1)

### Day 15 — GSC title optimisations + schema + Article 17
- **GSC fix:** `slack-alternatives.md` title changed from "Best Free Alternatives to Slack" to "Best Free Slack Alternatives" — matches dominant query variant. Description updated to lead with the key hook (90-day history limit)
- **GSC fix:** `microsoft-office-alternatives.md` title changed from "(2025)" to "(2026)", description updated to match "ms office alternative" query. Keywords expanded to include all GSC variant queries
- Added schema partial `layouts/partials/schema.html` — Article schema, BreadcrumbList (rich breadcrumbs), FAQ schema (auto-generated from description), WebSite schema with SearchAction on homepage
- Published Article 17: free-screen-recording-software (Video silo — now at 4)
- Drafted Reddit post #3 for r/entrepreneur (project management angle)

### Day 16 — Cross-links + Article 18 + progress log v2
- Published Article 18: free-backup-software (Cloud silo — now at 4)
- Added cross-links: free-video-editing-software → free-screen-recording-software, zoom-alternatives → free-screen-recording-software
- Added cross-links: free-cloud-storage-comparison → free-backup-software, dropbox-alternatives → free-backup-software
- Updated progress log (this document) to v2

---

## Internal link map (complete as of Day 16)

| From | To | Context |
|------|----|---------|
| microsoft-office-alternatives | slack-alternatives | team messaging section |
| microsoft-office-alternatives | grammarly-alternatives | writing tools mention |
| microsoft-office-alternatives | notion-alternatives | notes + research alongside Docs |
| grammarly-alternatives | microsoft-office-alternatives | switching from Word |
| grammarly-alternatives | notion-alternatives | writing projects + notes |
| slack-alternatives | notion-alternatives | after Mattermost — team wikis |
| notion-alternatives | free-password-managers | workspace account security |
| notion-alternatives | free-cloud-storage-comparison | file sync mention |
| notion-alternatives | free-crm-software | CRM bridge |
| free-cloud-storage-comparison | free-password-managers | after Proton Drive section |
| free-cloud-storage-comparison | free-email-service | privacy ecosystem |
| free-cloud-storage-comparison | free-backup-software | Our verdict section |
| free-password-managers | free-cloud-storage-comparison | vault backup section |
| free-password-managers | notion-alternatives | secure notes mention |
| free-antivirus-software | free-password-managers | security toolkit |
| free-antivirus-software | free-cloud-storage-comparison | securing cloud files |
| free-vpn | free-password-managers | full security toolkit |
| free-vpn | free-antivirus-software | security toolkit |
| free-crm-software | quickbooks-alternatives | accounting mention |
| free-crm-software | free-password-managers | client data security |
| free-crm-software | free-email-service | Zoho ecosystem cross-link |
| dropbox-alternatives | free-cloud-storage-comparison | full comparison link |
| dropbox-alternatives | free-password-managers | account security |
| dropbox-alternatives | free-backup-software | Our verdict section |
| illustrator-alternatives | canva-alternatives | template tools mention |
| photoshop-alternatives | illustrator-alternatives | vector work mention |
| photoshop-alternatives | canva-alternatives | template-based design |
| free-project-management-software | quickbooks-alternatives | accounting alongside PM |
| free-project-management-software | notion-alternatives | tasks + docs combined |
| free-email-service | free-cloud-storage-comparison | file storage alongside email |
| free-email-service | free-password-managers | privacy ecosystem |
| free-email-service | free-crm-software | Zoho ecosystem |
| free-video-editing-software | free-screen-recording-software | Our verdict — OBS + DaVinci workflow |
| zoom-alternatives | free-screen-recording-software | Our verdict — async recording |
| free-screen-recording-software | free-video-editing-software | editing captured footage |
| free-backup-software | free-cloud-storage-comparison | cloud storage as backup destination |

---

## Affiliate link inventory

| Program | Active? | Articles | Link |
|---------|---------|----------|------|
| NordVPN | ✅ | free-vpn, free-antivirus-software, dropbox-alternatives | https://go.nordvpn.net/aff_c?offer_id=15&aff_id=144937&url_id=902 |
| NordPass | ✅ | free-password-managers | https://go.nordpass.io/aff_c?offer_id=488&aff_id=144937&url_id=9356 |
| Canva | ✅ | canva-alternatives | Direct affiliate program |
| Grammarly | ✅ | grammarly-alternatives | Direct affiliate program |
| Amazon Associates | ✅ | Multiple | US: freestackfi20-20 · SG: freestackfi20-22 |
| HubSpot | ❌ deferred | — | Requires established company |
| Zoho | ⏳ pending | free-crm-software, free-email-service | CJ Affiliate — apply at ~5k monthly visitors |
| Impact.com | ❌ denied | — | Reapply at traffic threshold |

---

## Reddit posts

| # | Title angle | Subreddit | Status |
|---|-------------|-----------|--------|
| 1 | Cloud storage / Bitwarden hook | r/DataHoarder | ✅ Published Week 1 |
| 2 | Password managers — LastPass breach angle | r/privacy | ✅ Published Day 10 |
| 3 | Project management — Basecamp → Trello switch | r/entrepreneur | 📝 Drafted Day 15 |

---

## Pending actions

| Priority | Action | Notes |
|----------|--------|-------|
| High | Post Reddit #3 | Draft ready — r/entrepreneur, Tue–Thu 8–10am EST |
| High | GSC check | Week 4 — check if slack/office title changes improved CTR |
| High | Apply Zoho affiliate (CJ Affiliate) | Open program, apply now |
| Medium | AdSense application | Apply once 20+ articles live and 2+ months traffic data — threshold reached on articles |
| Medium | Reapply Impact.com | Once monthly visitors exceed 1,000 |
| Medium | Add NordVPN CTA to free-email-service.md | Natural fit — add after Proton Mail section |
| Low | Productivity Article 5 | free-calendar-app or free-note-taking-app |
| Low | Security Article 4 | free-2fa-authenticator-app — high intent keyword |
| Low | Business Article 4 | free-invoicing-software — direct affiliate potential (Wave, FreshBooks) |

---

## Hugo front matter template (confirmed working)

```yaml
---
title: "Best Free [Tool] in 2026 — [Hook/angle]"
description: "Lead with the surprising answer. 150–160 characters."
date: "2026-MM-DD"
lastmod: "2026-MM-DD"
draft: false
weight: [number — higher = more popular on homepage]
slug: "url-slug-here"
categories: ["Silo Name"]
tags:
  - "primary tag"
  - "secondary tag"
  - "tertiary tag"
keywords:
  - "primary keyword phrase"
  - "secondary keyword phrase"
  - "tertiary keyword phrase"
image: "/img/filename.jpg"
author: "FreeStackFinder Team"
---
```

**Rules — do not break these:**
- Date as quoted string `"2026-03-16"` — bare `2026-03-16` causes date parsing issues on some Hugo versions
- No `featured:` field — replaced by `weight:` 
- No `faqs:` block — causes YAML parse failure (Cloudflare build error)
- No `verdict-box` HTML divs — theme does not define this class, renders unstyled
- Image path always `/img/filename.jpg` (served from `static/img/`)
- Keywords as multiline list with `  - ` indented dashes (not inline array)

---

## Deploy commands reference

```bash
# Standard deploy after any changes
git add . && git commit -m "Description" && git push

# New article
cp article.md content/silo-name/
cp image.jpg static/img/
git add . && git commit -m "Add Article N: title" && git push

# Update homepage template
cp index.html layouts/index.html

# Update CSS
cp style.css static/css/style.css

# Update schema
cp schema.html layouts/partials/schema.html
```

---

## File structure reference

```
freestackfinder/
├── content/
│   ├── business/
│   │   ├── free-crm-software.md
│   │   ├── free-project-management-software.md
│   │   └── quickbooks-alternatives.md
│   ├── cloud/
│   │   ├── dropbox-alternatives.md
│   │   ├── free-backup-software.md
│   │   ├── free-cloud-storage-comparison.md
│   │   └── free-email-service.md
│   ├── creative/
│   │   ├── canva-alternatives.md
│   │   ├── illustrator-alternatives.md
│   │   └── photoshop-alternatives.md
│   ├── productivity/
│   │   ├── grammarly-alternatives.md
│   │   ├── microsoft-office-alternatives.md
│   │   ├── notion-alternatives.md
│   │   └── slack-alternatives.md
│   ├── security/
│   │   ├── free-antivirus-software.md
│   │   ├── free-password-managers.md
│   │   └── free-vpn.md
│   └── video/
│       ├── free-screen-recording-software.md
│       ├── free-video-editing-software.md
│       ├── premiere-pro-alternatives.md
│       └── zoom-alternatives.md
├── layouts/
│   ├── index.html          — homepage (weight-based popular articles)
│   ├── partials/
│   │   ├── article-card.html
│   │   ├── footer.html
│   │   ├── head.html
│   │   ├── nav.html
│   │   └── schema.html     — Article + BreadcrumbList + FAQ + WebSite schema
│   └── _default/
│       ├── baseof.html
│       ├── list.html
│       └── single.html
└── static/
    ├── css/
    │   └── style.css       — includes .affiliate-cta styles (Day 13)
    └── img/
        └── [all feature images — 1200×630px JPEG]
```
