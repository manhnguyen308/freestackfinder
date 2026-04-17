# FreeStackFinder — Claude Code Rules

## Mission
Build freestackfinder.com into a high-quality, useful, monetizable Hugo site by making steady, production-ready progress every day.

## Daily workflow
1. Read `CLAUDE.md`
2. Read `freestackfinder-progress-log.md` or `TRACKER.md` if present
3. Use the tracker as the primary source of current project state
4. Choose one focused content creation or content improvement day activity
5. Inspect only the files needed for that day activity
6. Implement the changes directly in the repo
7. Run a build to verify the current batch
8. Do light QA on the touched work only
9. Update `freestackfinder-progress-log.md` or `TRACKER.md` if present
10. Commit and deploy after verifying the changes

## Article date rule
For new article publishing:
- Use today's actual date for `date` and `lastmod`
- Live published articles must not use future dates
- Duplicate dates are allowed when multiple articles publish on the same day
- Do not inflate article dates into the future just to keep dates unique
- Keep `date` and `lastmod` as quoted strings in `YYYY-MM-DD` format
- Do not change existing article dates unless correcting a real error (wrong format, accidental future date, etc.)

## Definition of "next day activity"
A next day activity is a focused bundle of related work for that day, not necessarily a single task.

A valid day activity may include:
- creating and publishing one new article
- generating its feature image or image script
- adding related internal links between the new article and existing relevant articles
- improving affiliate placement on directly related pages
- making small, relevant UX, SEO, or content enhancements tied to that work
- updating the progress tracker
- committing and deploying after verification

Keep the day activity cohesive. Do not mix unrelated work from different parts of the site unless they are clearly part of the same publishing or improvement batch.

## Execution rules
- A daily run may contain multiple related tasks, but they must belong to one focused day activity
- Daily Claude Code runs focus on content creation or improvement, build verification, light QA, and tracker updates
- Do not take on Codex-style weekly reviews or monthly audits unless explicitly requested
- Prefer meaningful progress over artificial one-task limits
- Do not perform a broad repo audit unless the tracker is clearly outdated or inconsistent
- Do not scan unrelated directories
- Do not reread the same file unless necessary
- Do not ask what to do next unless blocked by a real conflict or missing file
- Trust actual repo files over the tracker if they conflict, then correct the tracker
- Keep changes production-ready and cohesive
- Preserve existing working behavior
- Keep output concise and focused on actual edits

## Coding and change discipline
Apply these defaults to every edit, whether content, layout, or scripts.

### Think before acting
- State assumptions explicitly when they affect the outcome
- If a task has more than one reasonable interpretation, pick the one that best fits the site's publishing/monetization goals and note the choice briefly
- If an instruction conflicts with an existing rule in this file, stop and flag the conflict instead of silently overriding
- Prefer the simplest change that satisfies the request

### Surgical changes
- Touch only what the task requires
- Do not reformat, refactor, or "improve" adjacent code, front matter, or prose that is unrelated to the task
- Match existing style, structure, and naming even if a different style would be preferable
- If your change makes an import, variable, or asset unused, remove it; do not delete pre-existing unused code or files unless the task asks for it
- Every changed line should trace back to the current day activity

### Simplicity first
- Write the minimum code, markup, or content needed to meet the goal
- No speculative flexibility, abstractions, or configuration for a single use case
- No error handling for cases that cannot occur in this static Hugo + Cloudflare setup
- If the result feels overengineered, rewrite it shorter before committing

### Verify before claiming done
For each day activity, define a short success check and confirm it before committing:
- New article: file exists in the correct silo, front matter valid, feature image resolves, internal links resolve, Hugo build (if run) passes
- Layout or CSS change: affected page type renders correctly and no known bug list item is reintroduced
- Script change: script runs to completion and produces the expected asset

Do not mark work complete based on intent — confirm the actual file, image, or page state.

## Task priority
Choose the next day activity in this order:
1. Fix broken, missing, inconsistent, or incomplete work
2. Strengthen monetization on existing high-intent pages
3. Improve internal linking inside an existing cluster
4. Publish the next strongest article and complete its related linking/image work
5. Improve UX, SEO, trust, or layout only when directly relevant to the current batch

## Weekly publishing schedule
Use this as the default publishing cadence for daily content work. Weekly review passes belong to Codex unless explicitly requested.

- Monday: Research and outline 2 articles
- Tuesday–Wednesday: Write and publish article 1
- Thursday–Friday: Write and publish article 2
- Friday: Add internal links from new articles to older related articles
- Sunday: Check Search Console and note new impressions, CTR movement, and keyword ideas

## Monthly maintenance
This is not part of a normal daily Claude run. Monthly audit work belongs to Codex unless explicitly requested.

If you are explicitly assigned monthly maintenance, spend around 30 minutes on:
- reviewing the top 5 articles for outdated pricing, limits, or features
- updating the `lastmod` date on any changed article
- checking affiliate links and redirects still work
- reviewing Search Console for pages ranking in positions 8–20 as quick-win candidates

## Growth targets
- Month 1 target: 24 articles live across 6 silos
- Month 4 target: apply for Google AdSense once 25+ articles and visible organic traffic are present
- Month 6 target: re-apply to Impact.com and other direct affiliate programs using real traffic data

## Long-term operating principle
Consistency matters more than occasional bursts.
Prefer steady publishing and incremental improvements every week over large but inconsistent pushes.

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
image: "/img/filename.webp"
author: "FreeStackFinder Team"
---
```

## Never use
- `featured:`
- `faqs:`
- `verdict-box` HTML in new content (legacy pages may still contain it)
- bare unquoted date values
- inline keyword arrays

## Content rules
Use the site’s comparison-article structure:

1. Quick verdict
2. Why this matters / why people are switching
3. The best free tools in 2026
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
- Add 2–5 relevant internal links where useful
- Use descriptive anchors
- Never use “click here”
- Prefer contextual cluster links over random cross-site links
- When publishing a new article, update older related articles when it meaningfully strengthens the cluster

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
3. `verdict-box` is legacy markup with existing styles; do not add new `verdict-box` HTML to fresh content
4. Affiliate image banners are blocked by adblockers
5. `list.html` must not rely on default paginator sorting
6. `index.html` latest section must not use unsorted `.Site.RegularPages`

## Environment and dependency rule
Before skipping any generator, build, or asset task due to a missing local dependency, first check whether the dependency can be installed in the current repo environment.

For required tools such as Python or Pillow:
- detect whether the tool is already available
- if not available, try to install it using the safest normal method for the current environment
- if Python is missing, install Python first if the environment allows it
- if Pillow is missing, install Pillow after Python is available
- after installation, continue the intended task instead of falling back to placeholders

Only use placeholders, temporary stand-ins, or deferred asset generation if:
- installation is blocked by permissions
- installation is blocked by network or package manager restrictions
- installation fails with a real error
- the environment does not allow the install

If blocked:
- clearly report the exact failed install step
- report the exact reason
- then use the best temporary fallback only if necessary


## Python executable paths
When Python is needed for image generation or automation, use the full path below — the `python` and `python3` shell commands resolve to Microsoft Store stubs on this machine and do not work:

```text
/c/Users/vboxuser/AppData/Local/Programs/Python/Python312/python.exe
```

For feature image generation:
- first try `python scripts/images/...`
- if that fails with exit 49 (Microsoft Store stub), use the full path above
- only report Python as unavailable after the full path also fails

## Missing-tool behavior
When a needed tool is missing:
1. Check whether it is already installed
2. Attempt installation if the environment allows it
3. Continue the task after installation
4. Only stop if installation fails or is blocked
5. Never default to placeholders without first attempting installation when installation is feasible

## Feature image rules
- Generate with Python + Pillow
- If Python or Pillow is missing, attempt installation first before falling back
- Size: 1200x630
- Format: WebP
- Use optimized WebP output for all newly generated feature images
- Save generated images to `static/img/`
- Use `.webp` filenames for generated feature images
- Do not generate PNG feature images unless transparency is truly required
- Avoid large JPEG/PNG feature images for article cards and homepage cards
- Target feature image file size below 200 KB where practical without visible quality loss
- Create and store image generator scripts inside a dedicated folder: `scripts/images/`
- Do not create image generator scripts in the repo root
- When fixing existing scripts, move them into `scripts/images/` and update any related references if needed
- Ensure the article front matter `image` path matches the actual generated `.webp` file
- Verify the feature image renders on the article card and the live article page after the fix

## Feature image SEO rules
- All generated feature images must be SEO-optimized
- Use descriptive, lowercase, hyphenated filenames
- Filename should match the article slug where practical
- Prefer filenames like `free-time-tracking-software.webp`, not generic names like `image1.webp`
- Article front matter `image` must point to the optimized WebP file
- Image alt text should be derived from the article title or a clear descriptive phrase
- Do not keyword-stuff filenames or alt text
- Keep filenames short, readable, and relevant
- Use 1200x630 dimensions for social sharing
- Use optimized WebP format for performance
- Target file size below 200 KB where practical without visible quality loss

## Feature image execution rule
For article feature images:
- do not leave placeholder images just because Python is missing without first attempting installation
- if Python is not installed, attempt to install Python
- if Pillow is not installed, attempt to install Pillow
- then run the generator script and produce the real image
- verify the generated image exists in `static/img/`
- verify the article front matter image path matches the generated file

## Blocking-error rule
Do not report "Python not installed" as a final blocker unless you have already attempted installation and the installation failed or was blocked by the environment.

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

scripts/
- images/
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
- ask for permission in chat before normal git commit, push, or deploy steps
- mention Claude, AI, assistant, prompts, or automation in commit messages
- mention Claude, AI, assistant, prompts, or automation in site content, comments, metadata, or tracker entries unless explicitly requested

## Git execution behavior
When git access is available, run the normal git flow automatically after verifying a valid change:
- `git add`
- `git commit`
- `git push`

Do not ask for confirmation in chat before these steps.

If the environment shows a command approval prompt, assume that prompt is external and proceed with the prepared command. Do not ask again in chat.

## Commit message rules
Commit messages must:
- describe only the actual repo change
- be short and production-style
- avoid filler words like "placeholder", "temp", "misc", or "update stuff"
- avoid mentioning Claude, AI, assistant, prompt, automation, or generation
- avoid conversational phrases like "as requested" or "for user"

Preferred commit style examples:
- `Replace NordPass CTA on free-password-managers page`
- `Add AdSense script to shared head partial`
- `Create free-time-tracking-software article and update links`

## Shell command behavior
Minimize shell approval prompts by batching related git steps into a single final command when possible.
Do not run git commands incrementally during the task.
Run git only once at the end after all changes are complete and verified.

## Output format for daily runs
Return only:
- Current day activity
- Files inspected
- Files changed
- What changed
- Tracker update summary
- Commit message
- Deploy status
- Any blocking error
