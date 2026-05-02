# FreeStackFinder — Claude Code Rules

## Mission
Build freestackfinder.com into a high-quality, useful, monetizable Hugo site by making steady, production-ready progress every day.

## Project skill

For all operational guidance — daily content workflow, feature workflow, weekly/monthly review, GSC-led refresh, affiliate safety, image generation, validation checklist, commit/deploy rules, and output format — use:

**`docs/SKILL.md`**

## When to read what

| Task | Read |
|------|------|
| Every run | This file + `freestackfinder-progress-log.md` |
| Article publishing | `CONTENT-STRATEGY.md` |
| Feature work | `FEATURE-STRATEGY.md` |
| Image generation | `docs/IMAGE-GUIDELINES.md` |
| Affiliate / monetization | `docs/AFFILIATE-GUIDELINES.md` |
| Build / deployment setup | `README.md` |

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
