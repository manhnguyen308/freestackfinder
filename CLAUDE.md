# FreeStackFinder — Claude Code Rules

## Mission
Build freestackfinder.com into a high-quality, useful, monetizable Hugo site by making one production-ready improvement per run.

## Daily workflow
1. Read `freestackfinder-progress-log.md`
2. Use it as the primary source of current project state
3. Choose the best next day activity
4. Inspect only the files needed for that day activity
5. Implement the change directly in the repo
6. Update `freestackfinder-progress-log.md`

## Definition of "next day activity"
A next day activity is a focused bundle of related work for that day, not necessarily a single task.

A valid day activity may include:
- creating and publishing one new article
- generating its feature image or image script
- adding related internal links between the new article and existing relevant articles
- improving affiliate placement on directly related pages
- making small, relevant UX/SEO/content enhancements tied to that work
- updating the progress tracker
- committing and deploying after verification

Keep the day activity cohesive. Do not mix unrelated work from different parts of the site unless it is part of the same publishing or improvement batch.

## Execution rules
- A daily run may contain multiple related tasks, but they must belong to one focused day activity
- Prefer meaningful progress over artificial one-task limits
- Do not perform a broad repo audit unless the tracker is clearly outdated or inconsistent
- Do not scan unrelated directories
- Do not reread the same file unless necessary
- Trust actual repo files over the tracker if they conflict, then correct the tracker
- Keep changes production-ready and cohesive
- Preserve existing working behavior
- Keep output concise and focused on actual edits

## Weekly publishing schedule
Use this schedule as the default operating rhythm unless the tracker indicates a higher-priority issue.

- Monday: Research and outline 2 articles
- Tuesday–Wednesday: Write and publish article 1
- Thursday–Friday: Write and publish article 2
- Friday: Add internal links from new articles to older related articles
- Sunday: Check Search Console and note new impressions, CTR movement, and keyword ideas

## Monthly maintenance
Spend around 30 minutes on:
- reviewing the top 5 articles for outdated pricing, limits, or features
- updating the `lastmod` date on any changed article
- checking affiliate redirects or affiliate links still work
- reviewing Search Console for pages ranking in positions 8–20 as quick-win candidates

## Growth targets
- Month 1 target: 24 articles live across 6 silos
- Month 4 target: apply for Google AdSense once 25+ articles and visible organic traffic are present
- Month 6 target: re-apply to Impact.com and other direct affiliate programs using real traffic data

## Long-term operating principle
Consistency matters more than occasional bursts.
Prefer steady publishing and incremental improvements every week over large but inconsistent pushes.

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

For completed valid changes:
- stage the relevant changed files
- create a clean production-style commit message
- push to the configured remote branch
- use the repo’s normal deployment flow after push

Never:
- ask for permission before normal git commit/push/deploy steps
- mention Claude, AI, assistant, prompts, or automation in commit messages
- mention Claude, AI, assistant, prompts, or automation in site content, comments, metadata, or tracker entries unless explicitly requested

## Commit and deploy rule
After completing and verifying a valid change, commit and deploy it by default without asking for confirmation.

Requirements:
- Do not ask for permission to run `git add`, `git commit`, `git push`, or the normal repo deployment flow
- Proceed automatically with staging, commit, push, and deploy once the task is complete and verified
- Only stop before commit or deploy if blocked by an actual error, missing credentials, missing permissions, failing checks, or an unavailable remote
- If blocked, clearly report what failed and at which step

Commit message rules:
- Write clean, professional commit messages only about the actual code or content change
- Do not mention Claude, Claude Code, AI, assistant, model, prompt, automation, or tool usage in commit messages
- Do not mention that the change was generated automatically
- Do not include conversational phrasing such as "as requested", "per prompt", or "from Claude"
- Keep commit messages concise, task-based, and production-appropriate

Content rules:
- Do not insert Claude, AI, assistant, model, or prompt references anywhere in site content, source files, comments, tracker entries, metadata, or generated assets unless I explicitly ask for it
- Do not include authorship notes such as "generated by Claude" or "created by AI"
- All outputs must read as normal production website content and normal repo maintenance work

Default git flow:
1. Stage relevant changed files
2. Create a clean commit message
3. Push to the configured remote branch
4. Let normal deployment run from git push, or run the standard deploy command if this repo requires it

If commit or deploy is blocked:
- Report the exact command that failed
- Report the exact reason
- Stop only at the blocking step

## Output format for daily runs
Return only:
- Current task
- Files inspected
- Files changed
- What changed
- Tracker update summary
- Deploy commands
