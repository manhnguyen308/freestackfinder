# FreeStackFinder — Claude Code Rules

## Mission
Build freestackfinder.com into a high-quality, useful, monetizable Hugo site by making steady, production-ready progress every day.

## Project skill

For all task-specific workflows — daily content publishing, feature work, GSC-led refresh, AdSense workflow, affiliate safety, image generation, validation checklist, tracker updates, commit/deploy rules — use:

**`docs/SKILL.md`**

For general agent operating discipline — session scope, plan-first, targeted reads, repeated-failure rule, diff/commit discipline, optional advanced tools — use:

**`docs/AGENT-WORKFLOW.md`** (works for Claude, Codex, or any coding agent)

For every task that writes, rewrites, reviews, or publishes reader-visible website copy, use:

**`website-content-humanizer.md`**

@website-content-humanizer.md

Treat it as the governing editorial standard for articles, hubs, homepage copy, trust pages, headings, metadata, calls to action, navigation labels, empty states, and shared template text. Run its full publication gate before delivery. Its accuracy, anti-fabrication, sitewide-audit, and no-dash rules are mandatory.

## When to read what

| Task | Read |
|------|------|
| Every fresh session | This file + `docs/AGENT-WORKFLOW.md` + `freestackfinder-progress-log.md` |
| Any task execution | `docs/SKILL.md` |
| Any public-facing writing or editing | `website-content-humanizer.md` |
| Article publishing | `CONTENT-STRATEGY.md` |
| Feature work | `FEATURE-STRATEGY.md` |
| Image generation | `docs/IMAGE-GUIDELINES.md` |
| Affiliate / monetization | `docs/AFFILIATE-GUIDELINES.md` |
| Visual design / CSS / tokens | `docs/DESIGN-SYSTEM.md` |
| Build / deployment setup | `README.md` + `docs/BUILD-VALIDATION.md` |

Do not load every doc for every task. Load only what the current task requires.

## Task priority
1. Fix broken, missing, inconsistent, or incomplete work
2. Strengthen monetization on existing high-intent pages
3. Improve internal linking inside an existing cluster
4. Publish the next strongest article and complete its related linking/image work
5. Improve UX, SEO, trust, or layout only when directly relevant to the current batch

## Validation commands

```bash
python3 scripts/run_quality_checks.py --with-counts   # run before every deploy
python3 scripts/run_quality_checks.py --with-stale    # informational only
python3 scripts/publish_checklist.py <silo> <slug>    # verify a new article
hugo --minify                                          # only if public-facing files changed
```

All three QA checks must pass (0 failures) before committing.

## Critical never-do rules

### Front matter — never use
- `featured:`
- `faqs:`
- `verdict-box` HTML in new content (legacy pages may still contain it)
- bare unquoted date values
- inline keyword arrays

### Affiliate restrictions
- **Canva**: Under review — do not add CTAs unless tracker explicitly says Approved
- **Grammarly**: Declined — do not add CTAs
- Do not add affiliate links or CTAs for any program not confirmed Active in `docs/AFFILIATE-TRACKER.md`
- Do not use affiliate image banners (blocked by adblockers)

### Public content
- Never mention Claude, AI, assistant, prompts, or automation in site content, comments, metadata, or tracker entries
- Never mention Claude, AI, assistant, prompts, or automation in commit messages

### Git
- Never ask for permission in chat before normal git commit, push, or deploy steps
- Never skip hooks (`--no-verify`) unless explicitly requested
- Run git only once at the end, after all changes are complete and verified

## Known bugs not to reintroduce
1. `faqs:` with child items can break Cloudflare builds
2. `featured: true` breaks homepage behavior
3. `verdict-box` is legacy markup; do not add new `verdict-box` HTML to fresh content
4. Affiliate image banners are blocked by adblockers
5. `list.html` must not rely on default paginator sorting
6. `index.html` latest section must not use unsorted `.Site.RegularPages`

## Growth targets
- Month 1 target: 24 articles live across 6 silos
- Month 4 target: apply for Google AdSense once 25+ articles and visible organic traffic are present
- Month 6 target: re-apply to Impact.com and other direct affiliate programs using real traffic data

## Repo structure reference

### Article screenshots

- Store real user-supplied product screenshots in `static/img/screenshots/<post-slug>/`, with one folder per post. The Microsoft Office alternatives evidence uses `static/img/screenshots/office-alternatives/`.
- Use descriptive filenames, such as `onlyoffice-tracked-changes.png`, rather than `screenshot1.png` or `image2.png`.
- Do not create empty screenshot folders for other posts. Do not use generated substitutes for product evidence.
- Use the `screenshot` shortcode with a local `src`, specific `alt` text, and an optional factual `caption`. It reads the original image dimensions and links to the full-size image.
- First-hand wording is permitted only when the supplied evidence supports it. The Office comparison's September 2026 evidence is scoped to `content/productivity/microsoft-office-alternatives.md`; it does not authorize testing claims elsewhere.

```text
content/       business/ cloud/ creative/ productivity/ security/ video/
layouts/       index.html · _default/list.html · _default/single.html
               partials/schema.html · head.html · nav.html · footer.html
               partials/article-card.html
static/        css/style.css · img/
scripts/       images/ · run_quality_checks.py · validate_front_matter.py
               check_internal_links.py · check_feature_images.py
               report_article_counts.py · report_stale_content.py
               publish_checklist.py
```
