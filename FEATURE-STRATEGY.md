# FreeStackFinder — Feature Strategy

## Purpose

This file documents the site's feature roadmap so future UX, trust, discovery, monetization, and content-operations work is planned, prioritized, and not repeated. It distinguishes what is already built from what is recommended next and what should be deferred.

Read this before starting any feature work. Update it when a feature ships or when priorities shift.

---

## Current Feature Baseline

The site is a Hugo static site hosted on Cloudflare Pages. All features must be compatible with a static build — no server-side logic, no database, no user accounts. JavaScript is used sparingly for interactivity.

**Current state (Day 49d):**
- 38 published articles across 6 silos (Productivity, Creative, Business, Security, Cloud, Video)
- Business silo: 11/13 — two articles remaining (`free-web-analytics`, `free-hr-software`)
- All Phase 1–4 features complete; full QA tooling suite in place
- Validators available: `scripts/validate_front_matter.py`, `scripts/check_internal_links.py`, `scripts/check_feature_images.py`
- Canva and Grammarly affiliate programs: Under review — do not mark Active or add CTAs
- NordPass: direct link in place; tracked URL follow-up pending if approved URL becomes available
- AdSense: script live (`ca-pub-5934721249825043`); formal approval pending

**Current goal:** grow useful content clusters to 50 articles, improve GSC-led page quality, and strengthen monetization only where programs are approved.

---

## Feature Principles

- Prefer extending existing systems over adding new ones.
- Keep Hugo static-site simplicity — no server-side rendering, no heavy dependencies.
- Avoid heavy JavaScript frameworks. Vanilla JS is the ceiling for new interactivity.
- Keep features editorial and trustworthy, not SaaS-app-like.
- Build only when it helps readers choose tools faster or helps site operations.
- Do not add features that create maintenance burden before traffic justifies them.
- One new system at a time. Finish and verify before opening the next.

---

## Completed Feature Archive

All items listed here are implemented. Do not re-propose as pending work.

| Feature | Day | Category | Notes |
|---------|-----|----------|-------|
| JSON-LD structured data | Early | SEO | Present on all article pages via `layouts/partials/schema.html` |
| Feature image system | Day 30+ | UX | Python + Pillow, 1200×630 WebP, `scripts/images/` folder |
| Homepage featured/latest sorting | Days 17, 46e | UX | Weight-sorted featured, date-sorted latest, curated collections |
| AdSense integration | Day 21 | Monetization | Live `ca-pub-5934721249825043` in `head.html`; formal approval pending |
| Amazon Associates placement | Day 39b | Monetization | US tag `freestackfi20-20` on 3 hardware-adjacent pages |
| Back-to-top button | Day 43b | UX | Fixed bottom-right, fade-in after 400px scroll, accessible |
| Utility/legal noindex handling | Day 43c | SEO | `noindex: true` + sitemap disable on all 5 utility pages |
| Site search with category filtering | Day 45a | Discovery | Vanilla JS, `/index.json` Hugo output, 7 filter buttons (All + 6 silos) |
| Header/search UI polish | Day 45b | UX | Logo · nav · search icon right-aligned; polished search page styling |
| Article schema and noindex metadata | Day 45c | SEO | Article-style schema suppressed on utility/noindex pages |
| Review/methodology trust block | Day 46b | Trust | 3-column block: last reviewed date · how we evaluate · what "free" means |
| Homepage curated collections | Day 46e | Discovery | 3 use-case clusters: freelance stack, replace Office, privacy basics |
| Comparison table shortcode | Day 46f | UX | YAML-driven Hugo shortcode; mobile card stacking; deployed on 11 articles |
| Curated related-guides logic | Day 46g | Discovery | Slug-keyed curated map in `related-guides.html`; falls back to Hugo `.Related` |
| Freshness display on cards | Day 46h | Trust | `class="updated"` teal highlight when `lastmod ≠ date` |
| Verdict badge shortcode | Day 46i | UX | Small all-caps pill via `verdict.html`; deployed on 11 articles |
| Footer trust CTA cleanup | Day 46j | UX | Pill-row flex layout for About · Disclaimer · Contact |
| Comparison table rollout | Day 47b | UX | Tables deployed on 7 additional high-intent pages |
| Verdict badge rollout — extended | Day 48f | UX | Badges deployed on 7 additional high-intent pages |
| Search result card upgrade | Day 48g | Discovery | Search index includes `date`/`lastmod`; cards show freshness line |
| Start Here guided entry page | Day 48i | Discovery | `/start-here/` routes readers into 6 silo clusters via use-case cards |
| Category hub top-picks upgrade | Day 48j | Discovery | All 6 silo `_index.md` pages show "Where to start" box with 4 curated links |
| Internal affiliate opportunity tracker | Day 48k | Monetization | `docs/AFFILIATE-TRACKER.md` — all articles tracked; no public CTAs added |
| Front matter validator script | Day 48l | QA | `scripts/validate_front_matter.py` — 9 issue categories; exits non-zero on errors |
| Internal link checker script | Day 48m | QA | `scripts/check_internal_links.py` — route map + broken link detection |
| Feature image inventory checker | Day 48o | QA | `scripts/check_feature_images.py` — cross-checks `image:` fields vs `static/img/` |
| Affiliate tracker verification pass | Day 49a | Monetization | All 15 rows resolved; 8 confirmed placed; 7 confirmed not placed |
| GSC search performance notes template | Day 49c | Documentation | `docs/GSC-NOTES.md` — snapshot table, opportunity table, action rules |
| Validation runner script | Day 49e | QA | `scripts/run_quality_checks.py` — runs all 3 QA scripts in sequence; `--with-build` and `--quiet` flags |
| Article count by silo report | Day 49f | QA | `scripts/report_article_counts.py` — count by silo, target comparison, draft exclusion; `--with-counts` flag added to runner |

---

## Recommended Feature Roadmap

Work through phases in order. Within a phase, pick the item with the clearest benefit and lowest complexity first.

---

## Phase 5 — Content Expansion and Cluster Completion

**Purpose:** Finish the remaining core content clusters and grow toward 50 useful articles without sacrificing quality.

**Possible work:**
- Complete Business silo from 11/13 to 13/13: publish `free-web-analytics` then `free-hr-software`
- Continue Later queue — one article per publishing day only
- Strengthen internal links from new articles to existing hubs on publish day
- Run validators (`validate_front_matter.py`, `check_internal_links.py`, `check_feature_images.py`) before every publish
- Avoid same-day article batches
- Add `free-website-builders` to related-guides map if not already linked

**Do not do in this phase:** start new Phase 6–9 work before Business silo is at 13/13.

---

## Phase 6 — GSC-Led Refresh and CTR Improvements

**Purpose:** Use Search Console observations to improve pages that already have impressions, not pages that are guessed to need help.

**Possible work:**
- Record GSC snapshots in `docs/GSC-NOTES.md` after each check
- Update titles and meta descriptions for pages with 100+ impressions but CTR below 1%
- Add internal links to pages ranking in positions 8–20
- Avoid rewriting newly published pages within 4 weeks of publish
- Do not chase every query — focus on pages already gaining traction
- Make one small trackable change per session

**Trigger:** begin when any page has 100+ monthly impressions. Do not run GSC refresh sessions on zero-data pages.

---

## Phase 7 — Monetization Readiness and Safe Affiliate Rollout

**Purpose:** Improve monetization only where programs are approved and placements are contextually relevant.

**Possible work:**
- Update NordPass link in `free-password-managers` only if an approved tracked URL is confirmed available
- Resume Canva and Grammarly placement only after program approval is confirmed — both are currently Under review
- Apply for Zoho via CJ once Zoho content cluster is established
- Reapply to Impact.com when traffic data is sufficient (month 4–6 target)
- Add approved CTAs only where contextually useful — one per article maximum unless clearly editorial
- Verify all affiliate links before placement; update `docs/AFFILIATE-TRACKER.md` after every change
- Avoid aggressive monetization before AdSense formal approval

**Do not do in this phase:** add Canva or Grammarly CTAs until approval is confirmed in writing.

---

## Phase 8 — Content Quality and E-E-A-T Strengthening

**Purpose:** Reduce low-value-content risk by making important pages more useful, original, and trustworthy — without inflating word count or adding filler.

**Possible work:**
- Improve thin sections on high-intent pages (Security, Business clusters)
- Add better decision guidance where articles are too list-like
- Strengthen "what free really includes" explanations for each tool
- Improve experience-based notes without making false testing claims
- Add concise FAQs only if the repo's shortcode/markup supports them safely and the content is genuinely useful
- Refresh outdated tool-plan language on articles older than 6 months

**Trigger:** begin after month 2–3 traffic data shows which pages need strengthening. Do not refresh pages with no impressions yet.

---

## Phase 9 — Lightweight Maintenance Automation

**Purpose:** Keep the static site healthy with small scripts and checklists, not heavy systems.

**Possible work:**
- ~~Add a single validation runner script (`scripts/run_quality_checks.py`)~~ **Done — Day 49e** (`scripts/run_quality_checks.py`; `--with-build`, `--quiet` flags)
- ~~Add a small article-count-by-silo report output to the runner~~ **Done — Day 49f** (`scripts/report_article_counts.py`; `--with-counts` flag in runner)
- Add a lightweight stale-content checker based on `lastmod` — flag articles not updated in 6+ months
- Add orphan-image cleanup workflow: list candidates but do not delete automatically
- Add optional pre-publish checklist command that prints the 5-step publish checklist from CLAUDE.md
- Keep all scripts dependency-light (Python standard library where possible); no CI unless clearly justified

**Do not do in this phase:** add external services, webhooks, APIs, or scheduled cloud jobs.

---

## What Not To Build Yet

Do not build these until traffic, income, or operational complexity clearly demands them.

- **User accounts or saved lists** — requires backend and authentication; not justified at current traffic
- **User ratings or reviews** — community features require moderation and a user base; not yet relevant
- **Dynamic database-backed tool directory** — a filterable live database is a different product class from an editorial comparison site; premature for current scale
- **Heavy JavaScript search framework** (Algolia, Fuse.js, Lunr) — current vanilla JS search handles 38 articles comfortably; revisit only if article count exceeds 150+
- **Newsletter backend** — valuable but requires a publishing plan and consistent send cadence; build infrastructure only after the content plan is confirmed
- **Complex affiliate dashboards** — a flat Markdown tracker is sufficient at current affiliate scale
- **Comparison app with dynamic filters** — editorial comparison tables serve the same reader intent without the complexity
- **Pagination redesign** — current paginator behavior is correct; do not rebuild unless a specific bug emerges
- **Dark/light mode toggle** — the site already uses a dark-by-default design; a toggle adds complexity without clear reader benefit at current traffic
- **Sticky article table of contents** — defer until articles regularly exceed 2,500 words and reader need is clear
- **Affiliate CTA shortcode** — 3–4 inline CTA variants across 38 articles is manageable; build only if duplication becomes genuinely painful

---

## How To Choose The Next Feature

Use this decision order:

1. Is the next content cluster article ready to publish? Do that first — content compounds faster than features.
2. Is there a GSC observation that clearly points to a page improvement? (Phase 6.)
3. Is there an approved affiliate program with an unplaced contextually relevant CTA? (Phase 7.)
4. Is there a page with meaningful traffic that is thin or outdated? (Phase 8.)
5. Is there a recurring QA or operations pain that a small script would eliminate? (Phase 9.)

Do not build a feature just because it seems like a good idea in isolation. Every feature that is not a content article is a debt against the publishing schedule.

---

## Suggested Next Feature

**Next publishing day: publish `free-web-analytics` (Business silo — 2 remaining to 13/13)**

Same-day option if no article: add lightweight stale-content checker (Phase 9) flagging articles with `lastmod` older than 6 months.

All Phase 1–4 features are complete. The full QA and ops tooling suite is in place. The site has 38 articles; the Business silo is at 11/13. Priority article is `free-web-analytics` — relevant to all site operators, high search volume, strong comparison format fit.

**Same day / non-content work:**
- Use `docs/GSC-NOTES.md` only if there is new GSC data worth recording
- Use `docs/AFFILIATE-TRACKER.md` only if an approved affiliate link has changed
- Do not add Canva or Grammarly CTAs until program approval is confirmed
- Do not build sticky article ToC unless article length and reader need clearly justify it
- Phase 9 validation runner is complete (`scripts/run_quality_checks.py`); next Phase 9 candidate is article-count-by-silo report or stale-content checker

---

## Maintenance Notes

- Update the **Completed Feature Archive** table when any new feature ships.
- Update the **Suggested Next Feature** section after completing the current recommendation.
- If a Phase 5–9 item is deferred or dropped, move it to **What Not To Build Yet** with a reason.
- This file is for feature planning only — article publishing decisions live in `CONTENT-STRATEGY.md` and `freestackfinder-progress-log.md`.
- Major UX or infrastructure review work belongs to Codex, not daily Claude runs.
