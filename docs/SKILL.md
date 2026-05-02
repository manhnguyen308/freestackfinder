---
name: free-stack-finder
description: Use this skill when working on the Free Stack Finder Hugo repo, including daily content publishing, feature implementation, weekly reviews, GSC/SEO fixes, affiliate safety checks, image workflow, and validation. Covers operational rules for all task types.
---

# Free Stack Finder — Project Skill

## 1. Purpose

Operational guide for agents working in the Free Stack Finder Hugo repo. Covers daily content publishing, feature work, weekly/monthly reviews, GSC-led refreshes, affiliate checks, image generation, build validation, and commit/deploy steps.

## 2. When to use this skill

Use when the task is one of:
- Publishing or improving an article
- Implementing a site feature or QA script
- Running a weekly or GSC-led review
- Checking or updating affiliate placement
- Generating a feature image
- Running build validation or fixing a broken check
- Updating the progress tracker or roadmap

Do not use for unrelated Hugo or Python projects.

## 3. Repo operating rules

### Think before acting
- State assumptions explicitly when they affect the outcome
- If a task has more than one reasonable interpretation, pick the one that best fits publishing/monetization goals and note the choice briefly
- If an instruction conflicts with CLAUDE.md, stop and flag it — do not silently override
- Prefer the simplest change that satisfies the request

### Surgical changes
- Touch only what the task requires
- Do not reformat, refactor, or "improve" adjacent code, front matter, or prose unrelated to the task
- Match existing style, structure, and naming
- If a change makes an import, variable, or asset unused, remove it; do not delete pre-existing unused code unless the task asks for it
- Every changed line must trace back to the current day activity

### Simplicity first
- Write the minimum code, markup, or content needed to meet the goal
- No speculative abstractions or configuration for a single use case
- No error handling for cases that cannot occur in a static Hugo + Cloudflare setup
- If the result feels overengineered, rewrite it shorter before committing

### Execution discipline
- A daily run may contain multiple related tasks, but they must belong to one focused day activity
- Do not take on weekly reviews or monthly audits unless explicitly requested
- Do not perform a broad repo audit unless the tracker is clearly outdated
- Do not scan unrelated directories
- Do not reread the same file unless necessary
- Do not ask what to do next unless blocked by a real conflict or missing file
- Trust actual repo files over the tracker if they conflict; then correct the tracker
- Keep changes production-ready and cohesive
- Keep output concise and focused on actual edits

## 4. Task routing

### Daily content publishing
1. Read CLAUDE.md + `freestackfinder-progress-log.md`
2. Read `CONTENT-STRATEGY.md` for the current article queue
3. Choose the next unpublished "Early" priority article
4. Inspect only files needed: target silo dir, related articles for internal links, `docs/AFFILIATE-GUIDELINES.md` if adding CTA
5. Write the article in the correct silo under `content/<silo>/`
6. Write or run the feature image script; save to `static/img/`
7. Add 2–5 internal links in the new article; update 1–2 older related articles to link back
8. Run `python3 scripts/run_quality_checks.py --with-counts`
9. Run `python3 scripts/publish_checklist.py <silo> <slug>` to auto-verify
10. Confirm article appears in `public/<silo>/<slug>/index.html` after `hugo --minify`
11. Update tracker + commit + push

Day-labeling: new SGT calendar day (12:00 AM Asia/Singapore) = new day number. Multiple runs same SGT day = letter suffixes (Day 37a, 37b, 37c…).

### Same-day feature work
1. Read `FEATURE-STRATEGY.md` for the current phase and next candidate
2. Inspect only the layout, script, or config files the feature touches
3. Build the feature; run `python3 scripts/run_quality_checks.py --with-counts` after
4. Run `hugo --minify` if any public-facing layout or template changed
5. Update `FEATURE-STRATEGY.md` — move the item to Completed Feature Archive with day label
6. Update tracker + commit + push

### Weekly review
- Only run when explicitly requested
- Scope: top 5 high-impression GSC pages, internal link gaps, affiliate placement accuracy, tracker accuracy
- Do not change content dates unless correcting a real error
- Run full validation checklist before committing

### GSC-led refresh
1. Read `docs/GSC-NOTES.md` for the current opportunity table
2. Identify pages in positions 8–20 with CTR below expectation
3. Update title, description, intro, or comparison table for relevance
4. Update `lastmod` on changed articles (do not change `date`)
5. Run validation + commit

### Affiliate/monetization checks
- Before adding any CTA, confirm the program status in `docs/AFFILIATE-TRACKER.md`
- **Canva**: Under review / Needs approval — do not add CTAs unless tracker explicitly says Approved
- **Grammarly**: Declined — do not add CTAs
- **NordVPN**: Active — CTA allowed on approved pages
- **NordPass**: Active — CTA allowed on approved pages
- **Amazon US (`freestackfi20-20`)**: Active — allowed on hardware-adjacent pages only
- **Zoho via CJ**: Pending — do not add CTAs until confirmed Active
- Use adblocker-safe text CTA blocks only (see CLAUDE.md for HTML structure)
- Do not use affiliate image banners
- Prefer monetization on high-intent pages first
- Keep affiliate placement useful and natural, not spammy

### Image work
- Tool: Python + Pillow
- Python path (Windows): `/c/Users/vboxuser/AppData/Local/Programs/Python/Python312/python.exe`
- Output: 1200×630 WebP, below 200 KB, saved to `static/img/`
- Scripts in `scripts/images/`
- Never install placeholders without attempting image generation first
- Full rules: `docs/IMAGE-GUIDELINES.md`

### Validation/build fixes
- Run `python3 scripts/run_quality_checks.py --with-counts` — all 3 checks must pass
- Run `python3 scripts/run_quality_checks.py --with-stale` for informational stale report
- Run `hugo --minify` only if public-facing files changed
- Known non-blocking warnings: 3 image orphans (`default-article.jpg`, `nordpass-banner.png`, `nordvpn-banner.png`)
- Full checklist: see Section 9 below

## 5. Token-saving rules

- Do not use broad grep/search to understand the whole site
- Prefer targeted file reads, tracker notes, directory listings, and known file paths
- Use grep only for exact terms inside a specific folder
- Always cap grep output with `head -20`
- Do not print large command outputs
- Do not scan all content files unless the task truly requires it
- Do not use repeated grep searches with similar keywords
- Do not use `cat` on large Markdown files
- Do not read unrelated folders

Allowed examples:
```bash
find content -maxdepth 3 -name "*.md"
find content -name "*.md" -size +25k
grep -RIn "exact-term" content/business --include="*.md" | head -20
```

## 6. Content quality rules

### Hugo front matter
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

Never use: `featured:` · `faqs:` · bare unquoted date values · inline keyword arrays

### Article date rule
- Use today's actual date for `date` and `lastmod` on new articles
- Never use future dates on live published articles
- Duplicate dates are allowed when multiple articles publish the same day
- Do not inflate dates to keep them unique
- Do not change existing article dates unless correcting a real error

### Article structure
1. Quick verdict
2. Why this matters / why people are switching
3. The best free tools in 2026
4. Quick comparison table
5. Decision guide / when to pay
6. Our verdict

For each tool section include: what it is · free plan includes · what the free plan is missing · who it's best for · why it stands out · tool link

### Internal linking
- Add 2–5 relevant internal links per article
- Use descriptive anchors; never "click here"
- Prefer contextual cluster links
- When publishing a new article, update older related articles where it strengthens the cluster

### Sorting rules
- Homepage "Featured comparisons": sort by `weight` descending
- Homepage "Latest comparisons": sort by `date` descending
- Category pages: sort by `date` descending

## 7. Affiliate safety rules

| Program | Status | Rule |
|---------|--------|------|
| NordVPN | Active | CTAs allowed on approved pages |
| NordPass | Active | CTAs allowed on approved pages |
| Canva | Under review | No CTAs until tracker says Approved |
| Grammarly | Declined | No CTAs |
| Amazon US | Active | Hardware-adjacent pages only; tag `freestackfi20-20` |
| Zoho via CJ | Pending | No CTAs until confirmed Active |

CTA HTML structure (text-only, adblocker-safe):
```html
<div class="affiliate-cta">
  <div class="affiliate-cta-content">
    <p class="affiliate-cta-title">Title here</p>
    <p class="affiliate-cta-desc">Description here.</p>
    <a href="AFFILIATE_URL" class="affiliate-cta-btn" rel="sponsored noopener" target="_blank">CTA text →</a>
  </div>
</div>
```

## 8. Image workflow rules

1. Confirm a script doesn't already exist in `scripts/images/` for this article
2. Write or reuse a Pillow script: 1200×630, dark background, tool name + tagline, logo if available
3. Export as WebP below 200 KB; save to `static/img/<slug>.webp`
4. Set `image: "/img/<slug>.webp"` in front matter
5. Run `python3 scripts/check_feature_images.py` to confirm no broken image reference
6. Full rules: `docs/IMAGE-GUIDELINES.md`

## 9. Validation checklist

Before marking any deployment complete:

1. `git diff --check` clean
2. `python3 scripts/run_quality_checks.py --with-counts` — 3 passed · 0 failed
3. `hugo --minify` — no errors, no deprecation warnings (run only if public-facing files changed)
4. Article count matches tracker (currently 43)
5. Search index JSON builds (`public/index.json` present)
6. Start Here page builds (`public/start-here/`)
7. Category hub pages build (one per silo)
8. `comparison-table` and `verdict` shortcodes render without error
9. Schema/JSON-LD partial produces no build warnings
10. Any newly published article appears in `public/<silo>/<slug>/index.html`
11. No new article created unintentionally
12. No URL/slug/alias changes
13. Canva status: Under review — no CTAs added
14. Grammarly status: Declined — no CTAs added

Non-blocking: 3 known image orphans (`default-article.jpg`, `nordpass-banner.png`, `nordvpn-banner.png`).

## 10. Tracker and roadmap updates

After every day activity, update `freestackfinder-progress-log.md`:
- Add a new `### Day NNx — <short title>` entry at the top of the log body
- Record: date, files inspected, files changed, what changed, validation result, guardrails confirmed, follow-up items
- Update the "Current state" block (article count, silo progress, next content/feature)
- Update `FEATURE-STRATEGY.md` when a feature ships (move to Completed Feature Archive with day label)
- Update `CONTENT-STRATEGY.md` when an article publishes (mark ✓ Published)

Day-labeling rule:
- New SGT calendar day (12:00 AM Asia/Singapore) → new day number (e.g., Day 57a)
- Multiple runs same SGT day → letter suffixes (57a, 57b, 57c…)

## 11. Commit and deploy rules

### Git flow
Run once at the end, after all changes are complete and verified. Batch git steps into a single command where possible.

```bash
git add <specific files>
git commit -m "Short production-style message"
git push
```

### Commit message rules
- Describe only the actual repo change
- Short, production-style
- No filler words: "placeholder", "temp", "misc", "update stuff"
- No mention of Claude, AI, assistant, prompt, automation, or generation
- No conversational phrases like "as requested" or "for user"

Good examples:
- `Publish free-ai-email-tools and add image`
- `Add pre-publish checklist script`
- `Strengthen site name signals in schema and head partials`

### Never
- Ask for permission in chat before git commit, push, or deploy
- Mention Claude, AI, assistant, prompts, or automation in commit messages, site content, metadata, or tracker entries
- Use `--no-verify` or skip hooks unless explicitly requested

## 12. Final response format

Return only:

```
Current activity:
Files inspected:
Files changed:
What changed:
Tracker update summary:
Commit message:
Deploy status:
Any blocking error:
```

For feature work, add:
```
Roadmap update:
Validation result:
```
