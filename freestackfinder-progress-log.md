# FreeStackFinder — Build Progress Log

**Site:** freestackfinder.com  
**Stack:** Hugo 0.128.0 + GitHub + Cloudflare Pages  
**Started:** Week 1 (Day 1)  
**Log updated:** Day 18

---

## Site overview

| Item | Detail |
|------|--------|
| Stack | Hugo 0.128.0, GitHub, Cloudflare Pages |
| Monetisation | Amazon Associates (US: freestackfi20-20 · SG: freestackfi20-22), NordVPN direct, NordPass direct, Canva direct, Grammarly direct |
| Affiliate status | NordVPN ✅ · NordPass ✅ · HubSpot ❌ deferred · Impact.com ❌ denied · Zoho via CJ Affiliate ⏳ apply now |
| GSC data (Day 11) | 1,420 impressions · 4 clicks · Avg position 51.8 · CTR 0.3% |
| Top GSC queries | slack alternatives (71 imp) · ms office variants (127 imp combined) · canva pro free (2 clicks) |
| Total articles | 22 (after Day 18) |
| Reddit posts | 2 published · 1 drafted (r/entrepreneur) |

---

## Content silo status

| Silo | Articles | Status |
|------|----------|--------|
| Productivity | 4 | ✅ |
| Creative | 3 | ✅ |
| Video | 4 | ✅ |
| Business | 4 | ✅ |
| Security | 4 | ✅ +1 2FA (Day 18) |
| Cloud | 4 | ✅ |

---

## All published articles (22 total)

### Productivity (4)
| # | File | Title | Date | Weight |
|---|------|-------|------|--------|
| 1 | grammarly-alternatives.md | Best Free Alternatives to Grammarly in 2026 | 2026-03-16 | 55 |
| 2 | microsoft-office-alternatives.md | Best Free Microsoft Office Alternative in 2026 | 2026-04-07 | 90 |
| 3 | slack-alternatives.md | Best Free Slack Alternatives in 2026 | 2026-04-07 | 95 |
| 4 | notion-alternatives.md | Best Free Alternatives to Notion in 2026 | 2026-03-26 | 70 |

### Creative (3)
| # | File | Title | Date | Weight |
|---|------|-------|------|--------|
| 5 | canva-alternatives.md | Best Free Alternatives to Canva in 2026 | 2026-03-16 | 85 |
| 6 | photoshop-alternatives.md | Best Free Alternatives to Photoshop in 2026 | 2026-04-04 | 60 |
| 7 | illustrator-alternatives.md | Best Free Alternatives to Illustrator in 2026 | 2026-04-03 | 40 |

### Cloud (4)
| # | File | Title | Date | Weight |
|---|------|-------|------|--------|
| 8 | free-cloud-storage-comparison.md | Best Free Cloud Storage in 2026 | 2026-03-16 | 75 |
| 9 | dropbox-alternatives.md | Best Free Dropbox Alternatives in 2026 | 2026-04-02 | 35 |
| 10 | free-email-service.md | Best Free Email Service in 2026 | 2026-04-06 | 68 |
| 11 | free-backup-software.md | Best Free Backup Software in 2026 | 2026-04-08 | 58 |

### Business (4)
| # | File | Title | Date | Weight |
|---|------|-------|------|--------|
| 12 | quickbooks-alternatives.md | Best Free QuickBooks Alternatives in 2026 | 2026-03-18 | 50 |
| 13 | free-crm-software.md | Best Free CRM Software in 2026 | 2026-04-02 | 37 |
| 14 | free-project-management-software.md | Best Free Project Management Software in 2026 | 2026-04-05 | 72 |
| 15 | free-invoicing-software.md | Best Free Invoicing Software in 2026 | 2026-04-09 | 74 |

### Security (4)
| # | File | Title | Date | Weight |
|---|------|-------|------|--------|
| 16 | free-password-managers.md | Best Free Password Managers in 2026 | 2026-03-27 | 80 |
| 17 | free-antivirus-software.md | Best Free Antivirus Software in 2026 | 2026-04-02 | 38 |
| 18 | free-vpn.md | Best Free VPN in 2026 | 2026-04-04 | 36 |
| 19 | best-free-2fa-apps.md | Best Free 2FA Authenticator Apps in 2026 | 2026-04-10 | 76 |

### Video (4)
| # | File | Title | Date | Weight |
|---|------|-------|------|--------|
| 20 | free-video-editing-software.md | Best Free Video Editing Software in 2026 | 2026-03-17 | 65 |
| 21 | zoom-alternatives.md | Best Free Alternatives to Zoom in 2026 | 2026-03-18 | 58 |
| 22 | premiere-pro-alternatives.md | Best Free Alternatives to Premiere Pro in 2026 | 2026-03-25 | 52 |
| 23 | free-screen-recording-software.md | Best Free Screen Recording Software in 2026 | 2026-04-07 | 62 |

---

## Homepage "Most popular" (top 6 by weight)

| Rank | Article | Weight | Basis |
|------|---------|--------|-------|
| 1 | slack-alternatives | 95 | GSC: highest single-keyword impressions |
| 2 | microsoft-office-alternatives | 90 | GSC: 127 combined impressions |
| 3 | canva-alternatives | 85 | Only article generating actual clicks |
| 4 | best-free-2fa-apps | 76 | New — high search intent |
| 5 | free-invoicing-software | 74 | High intent, affiliate potential |
| 6 | free-project-management-software | 72 | High volume keyword |

---

## Technical changes log

| Day | Change | Detail |
|-----|--------|--------|
| 10 | Internal links | Added cross-links to 4 articles (notion + password-managers) |
| 11 | GSC data | 1,420 impressions, 4 clicks. Article 13: illustrator-alternatives |
| 12 | Bug: featured field | `index.html` used `featured:true` — only 2 articles shown. Fixed with `(.ByParam "weight").Reverse` |
| 12 | Bug: YAML faqs block | Dangling `faqs:` children caused Cloudflare build fail on photoshop + ms-office articles |
| 12 | Affiliate | NordVPN + NordPass links added |
| 13 | Bug: affiliate banners | Image banners blocked by adblockers. Replaced with `.affiliate-cta` text CTAs |
| 13 | CSS | Added `.affiliate-cta` styles to `static/css/style.css` |
| 14 | Schema | Added `layouts/partials/schema.html` — Article + Breadcrumb + FAQ + WebSite |
| 15 | GSC titles | slack-alternatives + ms-office titles updated to match GSC query variants |
| 17 | Bug: category sort | `list.html` used `.Paginator` (default sort = weight). Fixed with `.RegularPages.ByDate.Reverse` |
| 17 | Bug: latest sort | `index.html` latest section sorted by weight. Fixed with `$latestArticles.ByDate.Reverse` |
| 18 | NordVPN CTA | Added to free-email-service.md (before Our verdict) |

---

## Internal link map (Day 18)

| From | To |
|------|----|
| microsoft-office-alternatives | slack-alternatives, grammarly-alternatives, notion-alternatives |
| grammarly-alternatives | microsoft-office-alternatives, notion-alternatives |
| slack-alternatives | notion-alternatives |
| notion-alternatives | free-password-managers, free-cloud-storage-comparison, free-crm-software |
| free-cloud-storage-comparison | free-password-managers, free-email-service, free-backup-software |
| free-password-managers | free-cloud-storage-comparison, notion-alternatives, best-free-2fa-apps |
| free-antivirus-software | free-password-managers, free-cloud-storage-comparison |
| free-vpn | free-password-managers, free-antivirus-software, best-free-2fa-apps |
| best-free-2fa-apps | free-password-managers, free-vpn |
| free-crm-software | quickbooks-alternatives, free-password-managers, free-email-service, free-invoicing-software |
| dropbox-alternatives | free-cloud-storage-comparison, free-password-managers, free-backup-software |
| illustrator-alternatives | canva-alternatives |
| photoshop-alternatives | illustrator-alternatives, canva-alternatives |
| free-project-management-software | quickbooks-alternatives, notion-alternatives, free-invoicing-software |
| free-email-service | free-cloud-storage-comparison, free-password-managers, free-crm-software |
| free-video-editing-software | free-screen-recording-software |
| zoom-alternatives | free-screen-recording-software |
| free-screen-recording-software | free-video-editing-software |
| free-backup-software | free-cloud-storage-comparison |
| quickbooks-alternatives | free-invoicing-software |
| free-invoicing-software | quickbooks-alternatives, free-crm-software |

---

## Affiliate link inventory

| Program | Status | Articles | Link |
|---------|--------|----------|------|
| NordVPN | ✅ Active | free-vpn, free-antivirus-software, dropbox-alternatives, free-email-service | https://go.nordvpn.net/aff_c?offer_id=15&aff_id=144937&url_id=902 |
| NordPass | ✅ Active | free-password-managers | https://go.nordpass.io/aff_c?offer_id=488&aff_id=144937&url_id=9356 |
| Canva | ✅ Active | canva-alternatives | Direct |
| Grammarly | ✅ Active | grammarly-alternatives | Direct |
| Amazon Associates | ✅ Active | Multiple | US: freestackfi20-20 · SG: freestackfi20-22 |
| HubSpot | ❌ Deferred | — | Requires established company |
| Zoho | ⏳ Apply now | free-crm-software, free-email-service, free-invoicing-software | CJ Affiliate — open program |
| Impact.com | ❌ Denied | — | Reapply at 1,000+ monthly visitors |

---

## Pending actions

| Priority | Action | Notes |
|----------|--------|-------|
| 🔴 High | Post Reddit #3 | Draft ready — r/entrepreneur, Tue–Thu 8–10am EST |
| 🔴 High | Apply Zoho affiliate | CJ Affiliate — open program, 3 articles reference Zoho |
| 🔴 High | GSC check | Did Day 15 title changes improve CTR on slack + office? |
| 🟡 Medium | AdSense application | 22 articles live — apply now |
| 🟡 Medium | Reapply Impact.com | At 1,000+ monthly visitors |
| 🟢 Low | Productivity Article 5 | free-note-taking-apps or free-calendar-app |
| 🟢 Low | Business Article 5 | free-time-tracking-software — pairs with invoicing |
| 🟢 Low | Creative Article 4 | free-font-websites or free-stock-photos |

---

## Front matter template (Hugo 0.128 — confirmed working)

```yaml
---
title: "Best Free [Tool] in 2026 — [Hook]"
description: "150–160 chars. Lead with the surprising answer."
date: "2026-MM-DD"
lastmod: "2026-MM-DD"
draft: false
weight: [number]
slug: "url-slug"
categories: ["Silo Name"]
tags:
  - "tag one"
  - "tag two"
keywords:
  - "keyword phrase one"
  - "keyword phrase two"
image: "/img/filename.jpg"
author: "FreeStackFinder Team"
---
```

**Never use:** `featured:` · `faqs:` · `verdict-box` HTML · bare (unquoted) date values

---

## Deploy commands

```bash
# New article
cp article.md content/silo/  &&  cp image.jpg static/img/

# Template changes
cp index.html layouts/index.html
cp list.html layouts/_default/list.html
cp schema.html layouts/partials/schema.html
cp style.css static/css/style.css

git add . && git commit -m "Description" && git push
```

---

## File structure

```
content/
  business/   free-crm, free-invoicing, free-project-mgmt, quickbooks
  cloud/      dropbox, free-backup, free-cloud-storage, free-email
  creative/   canva, illustrator, photoshop
  productivity/ grammarly, ms-office, notion, slack
  security/   free-antivirus, free-password-managers, free-vpn, best-free-2fa-apps
  video/      free-screen-recording, free-video-editing, premiere-pro, zoom

layouts/
  index.html              Most Popular (weight↓) + Latest (date↓)
  _default/list.html      category pages — date↓
  _default/single.html    article pages
  partials/schema.html    Article + Breadcrumb + FAQ + WebSite schema

static/
  css/style.css           includes .affiliate-cta
  img/                    all feature images 1200×630px JPEG
```
