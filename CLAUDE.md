# FreeStackFinder — Claude Code Rules

## Mission
Build freestackfinder.com into a high-quality, useful, monetizable Hugo site by making one production-ready improvement per run.

## Daily workflow
1. Read `freestackfinder-progress-log.md`
2. Use it as the primary source of current project state
3. Choose exactly one highest-value next task
4. Inspect only the files needed for that task
5. Implement the change directly in the repo
6. Update `freestackfinder-progress-log.md`

## Execution rules
- Complete exactly one meaningful task per run
- Do not perform a broad repo audit unless the tracker is clearly outdated or inconsistent
- Do not scan unrelated directories
- Do not reread the same file unless necessary
- Do not ask what to do next unless blocked by a real conflict or missing file
- Trust actual repo files over the tracker if they conflict, then correct the tracker
- Keep changes production-ready and cohesive
- Preserve existing working behavior
- Keep output concise and focused on actual edits

## Task priority
Choose the next task in this order:
1. Fix broken, missing, inconsistent, or incomplete work
2. Strengthen monetization on existing high-intent pages
3. Improve internal linking inside an existing cluster
4. Add one new article only if no higher-priority fix exists
5. Improve UX, SEO, trust, or layout only when directly relevant to the current task

## Hugo front matter rules
Always use this structure:

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

## Never use
- `featured:`
- `faqs:`
- `verdict-box` HTML
- bare unquoted date values
- inline keyword arrays

## Content rules
Use the site’s comparison-article structure:

1. Quick verdict
2. Why this matters / why people are switching
3. Best free tools in 2026
4. Quick comparison table
5. Decision guide / when to pay
6. Our verdict

For each main tool section, include:
- What it is
- Free plan includes
- What the free plan is missing
- Who it’s best for
- Why it stands out
- Tool link

## Internal linking rules
- Add 2–3 relevant internal links where useful
- Use descriptive anchors
- Never use “click here”
- Prefer contextual cluster links over random cross-site links

## Monetization rules
Use adblocker-safe text CTA blocks only:

```html
<div class="affiliate-cta">
  <div class="affiliate-cta-content">
    <p class="affiliate-cta-title">Title here</p>
    <p class="affiliate-cta-desc">Description here.</p>
    <a href="AFFILIATE_URL" class="affiliate-cta-btn" rel="sponsored noopener" target="_blank">CTA text →</a>
  </div>
</div>
```

- Do not use affiliate image banners
- Prefer monetization on high-intent pages first
- Keep affiliate placement useful and natural, not spammy

## Active affiliate programs
- NordVPN: active
- NordPass: active
- Canva: active
- Grammarly: active
- Amazon Associates US: `freestackfi20-20`
- Amazon Associates SG: `freestackfi20-22`
- Zoho via CJ: pending / apply
- HubSpot: deferred
- Impact.com: reapply later

## Homepage and list sorting rules
- Homepage “Most popular”: sort by `weight` descending
- Homepage “Latest comparisons”: sort by `date` descending
- Category pages: sort by `date` descending

## Known bugs not to reintroduce
1. `faqs:` with child items can break Cloudflare builds
2. `featured: true` breaks homepage behavior
3. `verdict-box` class is not defined
4. Affiliate image banners are blocked by adblockers
5. `list.html` must not rely on default paginator sorting
6. `index.html` latest section must not use unsorted `.Site.RegularPages`

## Feature image rules
- Generate with Python + Pillow
- Size: 1200x630
- Format: JPEG
- Save to `static/img/`

### Style
- Background: `#101116`
- Left panel: dark mock UI
- Right panel: featured card + 2x2 comparison cards
- Bottom bar: solid accent color, title in bold white
- Cards use circle helper with tool initials

### Accent colors by silo
- Security: `#8b5cf6`
- Business: `#10b981`
- Cloud: `#3b82f6` or `#06b6d4`
- Creative: `#f97316`
- Video: `#ef4444`
- Productivity: `#6366f1`

## Repo structure reference
```text
content/
- business/
- cloud/
- creative/
- productivity/
- security/
- video/

layouts/
- index.html
- _default/list.html
- _default/single.html
- partials/schema.html
- partials/article-card.html
- partials/head.html
- partials/nav.html
- partials/footer.html

static/
- css/style.css
- img/
```

## Deploy conventions
For new content:
- copy article into the correct `content/` silo
- copy image into `static/img/`
- `git add . && git commit -m "Message" && git push`

## Output format for daily runs
Return only:
- Current task
- Files inspected
- Files changed
- What changed
- Tracker update summary
- Deploy commands
