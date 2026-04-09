# FreeStackFinder — Build Progress Log

**Site:** freestackfinder.com  
**Stack:** Hugo + GitHub + Cloudflare Pages  
**Started:** Week 1 (Day 1)  
**Log updated:** Day 14

---

## Site overview

| Item | Detail |
|------|--------|
| Stack | Hugo (static site generator), GitHub, Cloudflare Pages |
| Monetisation | Amazon Associates (US: freestackfi20-20, SG: freestackfi20-22), NordVPN direct, Canva direct, Grammarly direct, Zoho (CJ Affiliate — pending traffic threshold) |
| Affiliate status | NordVPN activated · NordPass activated · HubSpot requires established company (deferred) · Impact.com denied (reapply at traffic threshold) |
| GSC data (Day 11) | 1,420 impressions · 4 clicks · Avg position 51.8 · CTR 0.3% |
| Top GSC queries | slack alternatives (71 imp) · ms office alternative variants (127 imp combined) · canva pro free (2 clicks) |

---

## Content silo targets

| Silo | Target articles | Status |
|------|----------------|--------|
| Productivity | 4+ | ✅ Done (4) |
| Creative | 3+ | ✅ Done (3) |
| Video | 3+ | ✅ Done (3) |
| Business | 3+ | ✅ Done (3) |
| Security | 3+ | ✅ Done (3) |
| Cloud | 3+ | ✅ Done (3 after Day 14) |

---

## All published articles

### Productivity silo (4 articles)

| # | File | Title | Date | Weight |
|---|------|-------|------|--------|
| 1 | grammarly-alternatives.md | Best Free Alternatives to Grammarly in 2026 | 2026-03-16 | 55 |
| 2 | microsoft-office-alternatives.md | Best Free MS Office Alternatives in 2026 | 2026-04-03 | 90 |
| 3 | slack-alternatives.md | Best Free Alternatives to Slack in 2026 | 2026-04-03 | 95 |
| 4 | notion-alternatives.md | Best Free Alternatives to Notion in 2026 | 2026-03-26 | 70 |

### Creative silo (3 articles)

| # | File | Title | Date | Weight |
|---|------|-------|------|--------|
| 5 | canva-alternatives.md | Best Free Alternatives to Canva in 2026 | 2026-03-16 | 85 |
| 6 | photoshop-alternatives.md | Best Free Alternatives to Adobe Photoshop in 2026 | 2026-04-04 | 60 |
| 7 | illustrator-alternatives.md | Best Free Alternatives to Adobe Illustrator in 2026 | 2026-04-03 | 40 |

### Cloud silo (3 articles)

| # | File | Title | Date | Weight |
|---|------|-------|------|--------|
| 8 | free-cloud-storage-comparison.md | Best Free Cloud Storage in 2026 | 2026-03-16 | 75 |
| 9 | dropbox-alternatives.md | Best Free Dropbox Alternatives in 2026 | 2026-04-02 | 35 |
| 10 | free-email-service.md | Best Free Email Service in 2026 | 2026-04-06 | 68 |

### Business silo (3 articles)

| # | File | Title | Date | Weight |
|---|------|-------|------|--------|
| 11 | quickbooks-alternatives.md | Best Free Alternatives to QuickBooks in 2026 | 2026-03-18 | 50 |
| 12 | free-crm-software.md | Best Free CRM Software in 2026 | 2026-04-02 | 37 |
| 13 | free-project-management-software.md | Best Free Project Management Software in 2026 | 2026-04-05 | 72 |

### Security silo (3 articles)

| # | File | Title | Date | Weight |
|---|------|-------|------|--------|
| 14 | free-password-managers.md | Best Free Password Managers in 2026 | 2026-03-27 | 80 |
| 15 | free-antivirus-software.md | Best Free Antivirus Software in 2026 | 2026-04-02 | 38 |
| 16 | free-vpn.md | Best Free VPN in 2026 | 2026-04-04 | 36 |

### Video silo (3 articles)

| # | File | Title | Date | Weight |
|---|------|-------|------|--------|
| 17 | free-video-editing-software.md | Best Free Video Editing Software in 2026 | 2026-03-17 | 65 |
| 18 | zoom-alternatives.md | Best Free Alternatives to Zoom in 2026 | 2026-03-18 | 58 |
| 19 | premiere-pro-alternatives.md | Best Free Alternatives to Adobe Premiere Pro in 2026 | 2026-03-25 | 52 |

---

## Homepage "Most popular" ranking (weight-based)

The homepage shows the 6 highest-weight articles in the "Most popular comparisons" section. Update weights in front matter as GSC data improves.

| Rank | Article | Weight | Basis |
|------|---------|--------|-------|
| 1 | slack-alternatives | 95 | 71 GSC impressions |
| 2 | microsoft-office-alternatives | 90 | 127 impressions (combined variants) |
| 3 | canva-alternatives | 85 | Only article generating clicks |
| 4 | free-password-managers | 80 | High search intent + affiliate |
| 5 | free-cloud-storage-comparison | 75 | Strong evergreen keyword |
| 6 | free-project-management-software | 72 | High volume keyword, Business silo |

**To update:** change `weight:` in the article's front matter. Higher number = more popular. Redeploy after changes.

---

## Technical fixes applied

### Front matter corruption (Days 10–12)
- **Problem:** Articles `photoshop-alternatives.md` and `microsoft-office-alternatives.md` had unsupported `featured: true` and `faqs:` YAML blocks causing Cloudflare build failures.
- **Fix:** Removed `featured`, `faqs`, and `verdict-box` HTML divs. Rewrote both articles with clean front matter.
- **Prevention:** New articles never use `featured`, `faqs`, or `verdict-box`. Front matter template confirmed from `free-cloud-storage-comparison.md`.

### Homepage featured articles (Day 12)
- **Problem:** `index.html` used `where .Site.RegularPages "Params.featured" true` which only showed 2 articles with `featured: true`.
- **Fix:** Replaced with `(.ByParam "weight").Reverse` — shows top 6 articles by weight value. Added `weight:` field to all 17 articles.

### NordVPN affiliate banner (Day 13)
- **Problem:** Image banners using affiliate URLs (`aff_id`, `offer_id`, `aff_c` parameters) are blocked by uBlock Origin and AdBlock Plus via EasyList. No fix possible without changing the affiliate URL structure.
- **Fix:** Replaced all `<div class="affiliate-banner"><img>` blocks with `<div class="affiliate-cta">` text CTAs. Added `.affiliate-cta` CSS to `static/css/style.css`.

### Internal link injection (Days 10–11)
Added contextual internal links to 4 existing articles:
- `microsoft-office-alternatives.md` → notion-alternatives
- `grammarly-alternatives.md` → notion-alternatives  
- `slack-alternatives.md` → notion-alternatives (after Mattermost section)
- `free-cloud-storage-comparison.md` → free-password-managers (after Proton Drive section)

---

## Internal link map

Full cross-link network as of Day 14. Each entry is a link that exists in the source article pointing to the destination.

| From | To | Anchor context |
|------|----|---------------|
| microsoft-office-alternatives | slack-alternatives | team messaging section |
| microsoft-office-alternatives | grammarly-alternatives | writing tools mention |
| microsoft-office-alternatives | notion-alternatives | notes + research section |
| grammarly-alternatives | microsoft-office-alternatives | switching from Word section |
| grammarly-alternatives | notion-alternatives | writing projects + notes |
| slack-alternatives | notion-alternatives | after Mattermost — team wikis |
| notion-alternatives | free-password-managers | workspace security |
| notion-alternatives | free-cloud-storage-comparison | file sync mention |
| notion-alternatives | free-crm-software | CRM bridge (once live) |
| free-cloud-storage-comparison | free-password-managers | after Proton Drive section |
| free-password-managers | free-cloud-storage-comparison | vault backup section |
| free-password-managers | notion-alternatives | secure notes mention |
| free-antivirus-software | free-password-managers | security upgrade section |
| free-antivirus-software | free-cloud-storage-comparison | securing cloud files |
| free-vpn | free-password-managers | full security toolkit |
| free-vpn | free-antivirus-software | security toolkit |
| free-crm-software | quickbooks-alternatives | accounting mention |
| free-crm-software | free-password-managers | client data security |
| dropbox-alternatives | free-cloud-storage-comparison | full comparison |
| dropbox-alternatives | free-password-managers | account security |
| illustrator-alternatives | canva-alternatives | template tools mention |
| photoshop-alternatives | illustrator-alternatives | vector work mention |
| photoshop-alternatives | canva-alternatives | template-based design |
| free-project-management-software | quickbooks-alternatives | accounting alongside PM |
| free-project-management-software | notion-alternatives | tasks + docs combined |
| free-email-service | free-cloud-storage-comparison | file storage alongside email |
| free-email-service | free-password-managers | privacy ecosystem |
| free-email-service | free-crm-software | Zoho ecosystem cross-link |

---

## Affiliate link inventory

| Program | Articles using it | Link / Status |
|---------|------------------|---------------|
| NordVPN | free-vpn, free-antivirus-software, dropbox-alternatives | https://go.nordvpn.net/aff_c?offer_id=15&aff_id=144937&url_id=902 · Active |
| NordPass | free-password-managers | https://go.nordpass.io/aff_c?offer_id=488&aff_id=144937&url_id=9356 · Active |
| Canva | canva-alternatives | Direct affiliate program · Active |
| Grammarly | grammarly-alternatives | Direct affiliate program · Active |
| Amazon Associates | Multiple | US: freestackfi20-20 · SG: freestackfi20-22 |
| HubSpot | free-crm-software | Requires established company — deferred |
| Zoho | free-crm-software, free-email-service | CJ Affiliate — apply at ~5k monthly visitors |
| Impact.com | — | Denied — reapply at traffic threshold |

---

## Reddit posts published

| # | Post | Subreddit | Date |
|---|------|-----------|------|
| 1 | Cloud storage comparison (Bitwarden angle) | r/DataHoarder | Week 1 |
| 2 | Password managers — LastPass alternative angle | r/privacy | Day 10 |

**Planned next posts:**
- Post 3: Free project management — r/entrepreneur or r/startups
- Post 4: Free VPN honest comparison — r/privacy or r/netsec

---

## GSC monitoring checklist

Check GSC every 7 days. For each review:

1. Go to Search Results → Last 28 days → Sort by Impressions descending
2. Screenshot top 10 queries
3. For any article at position 11–30: update H2 headings to match exact query phrasing
4. For any article with impressions but 0 clicks at position 30+: add 200–300 words to weakest section
5. Update `weight:` in front matter for any article gaining traction (redeploy homepage)

**Targets for next GSC review:**
- Slack alternatives: should be moving from ~50 toward page 2 (position 11–20)
- MS Office alternatives: 127 combined impressions — consolidate with title optimisation
- Canva alternatives: already getting clicks — check exact query variants and optimise H2s

---

## Pending actions

| Priority | Action | Notes |
|----------|--------|-------|
| High | Third Reddit post | r/entrepreneur — project management angle |
| High | Reapply Impact.com | Once monthly visitors exceed 1,000 |
| High | Apply Zoho affiliate (CJ Affiliate) | Open program, no traffic threshold |
| Medium | NordVPN links — update in free-email-service.md | Add once article is live |
| Medium | AdSense application | Apply once 20+ articles live and 2–3 months of traffic data |
| Medium | Internal link audit | Every new article needs 2–3 outbound + 1–2 inbound links |
| Low | Cloud silo Article 17 | free-backup-software or free-file-sharing next sprint |
| Low | Productivity Article 5 | free-email or free-calendar next sprint (email now in Cloud) |

---

## Hugo front matter template (confirmed working)

```yaml
---
title: "Best Free [Tool] Alternatives in 2026 — Tested and Compared"
description: "One-sentence hook with the surprising answer. 150–160 chars."
date: "2026-MM-DD"
lastmod: "2026-MM-DD"
draft: false
weight: [number]
slug: "url-slug"
categories: ["Silo Name"]
tags: ["primary tag", "secondary tag", "tertiary tag"]
keywords:
  - "primary keyword"
  - "secondary keyword"
  - "tertiary keyword"
image: "/img/filename.jpg"
author: "FreeStackFinder Team"
---
```

**Rules:**
- Date as quoted string `"2026-03-16"` not bare `2026-03-16`
- Keywords as multiline list with indented dashes
- No `featured:` field — use `weight:` instead
- No `faqs:` block — causes YAML parse failure
- No `verdict-box` HTML divs — Hugo renders as raw HTML, not styled
- Image path always `/img/filename.jpg` (served from `static/img/`)

---

## Deploy commands reference

```bash
# Standard deploy after content changes
git add . && git commit -m "Description of changes" && git push

# Add new article + image
cp article-name.md content/silo/
cp article-image.jpg static/img/
git add . && git commit -m "Add Article N: title" && git push

# Update homepage template
cp index.html layouts/index.html
git add . && git commit -m "Update homepage" && git push

# Update CSS
cp style.css static/css/style.css
git add . && git commit -m "Update styles" && git push
```

---

## File structure reference

```
freestackfinder/
├── content/
│   ├── business/          ← free-crm-software.md, free-project-management-software.md, quickbooks-alternatives.md
│   ├── cloud/             ← dropbox-alternatives.md, free-cloud-storage-comparison.md, free-email-service.md
│   ├── creative/          ← canva-alternatives.md, illustrator-alternatives.md, photoshop-alternatives.md
│   ├── productivity/      ← grammarly-alternatives.md, microsoft-office-alternatives.md, notion-alternatives.md, slack-alternatives.md
│   ├── security/          ← free-antivirus-software.md, free-password-managers.md, free-vpn.md
│   └── video/             ← free-video-editing-software.md, premiere-pro-alternatives.md, zoom-alternatives.md
├── layouts/
│   ├── index.html         ← homepage (weight-based popular articles)
│   ├── partials/          ← article-card.html, footer.html, head.html, nav.html
│   └── _default/          ← baseof.html, list.html, single.html
└── static/
    ├── css/style.css      ← all site styles including .affiliate-cta
    └── img/               ← all feature images (1200×630px JPEG)
```
