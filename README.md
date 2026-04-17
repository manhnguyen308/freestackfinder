# FreeStackFinder — Setup & Deployment Guide

## Stack Summary
- **Generator:** Hugo (static site)
- **Hosting:** Cloudflare Pages (free)
- **Repo:** GitHub (free)
- **Domain:** Namecheap (~$12/year)
- **Total monthly cost: $0**

`CLAUDE.md` is the authoritative file for daily operating rules, front matter constraints, and publishing workflow. Keep `README.md` for setup and deployment only.

---

## Prerequisites

Install Hugo (Extended version required for SCSS if you add it later):
```bash
# macOS (Homebrew)
brew install hugo

# Windows (Chocolatey)
choco install hugo-extended

# Linux
sudo apt install hugo
# Or download from https://github.com/gohugoio/hugo/releases
```

Verify installation:
```bash
hugo version
# Should show: hugo v0.128.0+ ...
```

---

## Local Development

### Step 1 — Clone or set up the project

```bash
# If starting fresh:
mkdir freestackfinder && cd freestackfinder
git init

# If cloning:
git clone https://github.com/YOURUSERNAME/freestackfinder.git
cd freestackfinder
```

### Step 2 — Run local server

```bash
hugo server -D
# -D flag includes draft articles
# Visit http://localhost:1313
```

Live reload is automatic — save a file and the browser refreshes.

### Step 3 — Build for production

```bash
hugo --minify
# Output goes to /public/ folder
```

---

## Deployment — Cloudflare Pages

### One-time setup:

1. **Push project to GitHub:**
   ```bash
   git add .
   git commit -m "Initial site setup"
   git remote add origin https://github.com/YOURUSERNAME/freestackfinder.git
   git push -u origin main
   ```

2. **Connect to Cloudflare Pages:**
   - Log in to https://dash.cloudflare.com
   - Go to Workers & Pages → Create application → Pages
   - Connect GitHub → Select your `freestackfinder` repository
   - Build settings:
     - **Framework preset:** Hugo
     - **Build command:** `hugo --minify`
     - **Build output directory:** `public`
     - **Environment variable:** `HUGO_VERSION` = `0.128.0`
   - Click Save and Deploy

3. **Add custom domain:**
   - In Cloudflare Pages → Custom domains → Add custom domain
   - Enter `freestackfinder.com` (or your domain)
   - Update nameservers at Namecheap to Cloudflare's nameservers
   - SSL/HTTPS is automatic via Cloudflare

### Auto-deploy after setup:
Every `git push` to the `main` branch triggers an automatic rebuild and deployment. Takes about 30–60 seconds.

---

## Adding Content

### New article:
```bash
hugo new creative/your-article-slug.md
```

This creates a file from the archetype template in `/archetypes/default.md`.

### Front matter fields explained:

```yaml
---
title: "Article Title Here"           # H1 and page title
description: "Meta description..."     # 150-160 chars. Appears in Google search results.
date: "2026-04-17"                     # Publication date, quoted YYYY-MM-DD
lastmod: "2026-04-17"                  # Last update date, quoted YYYY-MM-DD
draft: false                           # false = live, true = hidden
weight: 50                             # Homepage "Most popular" uses weight, not featured
slug: "your-article-slug"
categories: ["Creative"]               # One of: Creative, Productivity, Video, Business, Security, Cloud
tags:
  - "photoshop"
  - "free tools"
keywords:
  - "free photoshop alt"
  - "best free creative software"
image: "/img/your-image.webp"          # Featured image (1200x630px recommended)
author: "FreeStackFinder Team"
---
```

Do not add `featured:`, `faqs:`, or new `verdict-box` HTML. Follow `CLAUDE.md` for the current authoring rules.

### Publishing an article:
1. Write it in Markdown with `draft: true`
2. Preview locally with `hugo server -D`
3. Change `draft: false` when ready
4. `git add . && git commit -m "Add article: your title" && git push`
5. Cloudflare auto-deploys in ~45 seconds

---

## Google AdSense Setup (Month 4+)

1. Apply at https://adsense.google.com
2. Once approved, get your Publisher ID (format: `ca-pub-XXXXXXXXXX`)
3. Open `config.toml` and update:
   ```toml
   adsensePublisherId = "ca-pub-XXXXXXXXXX"
   ```
4. The shared AdSense script in `layouts/partials/head.html` reads `adsensePublisherId` automatically
5. Keep `showAds = false` until you have replaced the placeholder slot IDs in `layouts/_default/single.html`
6. Once the slot IDs are real, set `showAds = true`
7. Push and deploy

Ad slots in the template:
- `TOP_ARTICLE_SLOT_ID` — top of article, before content
- `SIDEBAR_SLOT_ID` — sidebar rectangle ad

Add a third mid-article slot by inserting the ins tag after your 3rd H2 in the article template if desired.

---

## Affiliate Link Management

For clean affiliate URLs, use Hugo's redirect system:

Create `/static/_redirects` (Cloudflare Pages format):
```
/go/canva-pro      https://www.canva.com/your-affiliate-link    302
/go/grammarly      https://www.grammarly.com/your-link          302
/go/nordvpn        https://nordvpn.com/your-link                302
```

Then in articles, link like this:
```markdown
[Try Canva Pro →](/go/canva-pro)
```

Benefits:
- Clean URLs in articles
- Easy to update if affiliate links change (update one file, not every article)
- Looks professional to readers

---

## Image Optimization

Before adding any image:
1. Resize to max 1200px wide for featured images (1200x630px for OG images)
2. Compress at https://squoosh.app — target under 100KB for article images
3. Save as WebP for best compression (Hugo serves them as-is)
4. Name files descriptively: `photoshop-alternatives-2025.webp`
5. Place in `/static/img/`

---

## Google Search Console Setup

1. Go to https://search.google.com/search-console
2. Add property → URL prefix → Enter `https://freestackfinder.com`
3. Verify via HTML tag (add to head.html) OR DNS record (add via Cloudflare)
4. Once verified, go to Sitemaps → Add `/sitemap.xml`
5. Check Coverage tab weekly in Month 1–3 to confirm pages are indexed

---

## Monthly Maintenance Checklist

Run this checklist once per month:

- [ ] Check Google Search Console for crawl errors
- [ ] Look at Search Console Performance for new keyword opportunities
- [ ] Review top 5 articles — are any facts, prices, or features outdated?
- [ ] Update `lastmod` date on any articles you've changed
- [ ] Verify affiliate links in your top 10 articles still work and go to the right place
- [ ] Check analytics for any surprising traffic patterns
- [ ] Plan content for the next month (2 articles/week target)

---

## Folder Structure Reference

```
freestackfinder/
├── archetypes/
│   └── default.md              # Template for new articles
├── content/
│   ├── _index.md               # Homepage content
│   ├── about.md
│   ├── contact.md
│   ├── privacy-policy.md
│   ├── disclaimer.md
│   ├── terms.md
│   ├── creative/
│   │   ├── _index.md           # Category hub page
│   │   └── photoshop-alternatives.md
│   ├── productivity/
│   │   ├── _index.md
│   │   └── microsoft-office-alternatives.md
│   ├── video/
│   ├── business/
│   ├── security/
│   └── cloud/
├── layouts/
│   ├── _default/
│   │   ├── baseof.html         # Base template all pages inherit
│   │   ├── single.html         # Article page
│   │   └── list.html           # Category page
│   ├── partials/
│   │   ├── head.html           # <head> with SEO meta + schema
│   │   ├── nav.html            # Header navigation
│   │   ├── footer.html         # Footer
│   │   ├── article-card.html   # Reusable card component
│   │   └── schema.html         # JSON-LD structured data
│   ├── index.html              # Homepage template
│   └── page/
│       └── single.html         # Static pages (About, Privacy, etc.)
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   └── img/                    # Put all images here
├── config.toml                 # Site configuration
└── README.md
```

---

## Estimated Timeline

| Milestone | Timeline |
|-----------|----------|
| Site live on Cloudflare | Day 1–2 |
| First 8 articles published | End of Week 2 |
| 24 articles published | End of Month 1 |
| Google index coverage | Month 1–2 |
| First organic search traffic | Month 2–3 |
| AdSense application | Month 4 |
| First AdSense income | Month 4–5 |
| First affiliate commission | Month 2–4 |
| 1,000 monthly visitors | Month 4–6 |
| 5,000 monthly visitors | Month 8–12 |
| $200+/month income | Month 8–14 |
