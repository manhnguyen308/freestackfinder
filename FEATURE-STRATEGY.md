# FreeStackFinder — Feature Strategy

## Purpose

This file documents the site's feature roadmap so future UX, trust, discovery, monetization, and content-operations work is planned, prioritized, and not repeated. It distinguishes what is already built from what is recommended next and what should be deferred.

Read this before starting any feature work. Update it when a feature ships or when priorities shift.

---

## Current Feature Baseline

The site is a Hugo static site hosted on Cloudflare Pages. All features must be compatible with a static build — no server-side logic, no database, no user accounts. JavaScript is used sparingly for interactivity.

Current content: 33 published articles across 6 silos (Productivity, Creative, Business, Security, Cloud, Video).

Current goal: grow useful content clusters, improve internal linking, strengthen monetization, and prepare for AdSense approval and eventual affiliate expansion.

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

## Completed Feature Systems

The following systems are implemented and should not be re-proposed as pending work.

| Feature | Implemented | Notes |
|---------|-------------|-------|
| Site search with category filtering | Day 45a | Vanilla JS, `/index.json` Hugo output, 7 filter buttons (All + 6 silos) |
| Header/search UI polish | Day 45b | Logo · nav · search icon right-aligned; polished search page styling |
| Back-to-top button | Day 43c | Fixed bottom-right, fade-in after 400px scroll, accessible |
| Utility/legal noindex handling | Day 43b | `noindex: true` + sitemap disable on all 5 utility pages |
| Review/methodology trust block | Day 46b | 3-column block: last reviewed date · how we evaluate · what "free" means; renders on all article pages only |
| Homepage curated collections | Day 46e | 3 use-case clusters manually curated: freelance stack, replace Office, privacy basics |
| Comparison table shortcode | Day 46f | YAML-driven Hugo shortcode; mobile card stacking; deployed on 4 articles |
| Curated related-guides logic | Day 46g | Slug-keyed curated map in `related-guides.html`; falls back to Hugo `.Related`; covers all 33 articles |
| Freshness display on cards | Day 46h | `class="updated"` on `<time>` elements when `lastmod != date`; teal highlight distinguishes updated from published dates |
| Verdict badge shortcode | Day 46i | Small all-caps pill via `verdict.html` shortcode; deployed on 4 comparison pages |
| Verdict badge rollout — extended | Day 48f | Badges deployed on 7 additional high-intent pages: free-password-managers, free-project-management-software, free-crm-software, free-invoicing-software, free-cloud-storage-comparison, free-video-editing-software, photoshop-alternatives; 3 defensible labels per page |
| Search result card upgrade | Day 48g | Search index now includes `date` and `lastmod`; result cards show category pill, description, and freshness line ("Updated" in primary color when lastmod ≠ date, "Published" in muted when equal); vanilla JS only, no new dependencies |
| Start Here guided entry page | Day 48i | `/start-here/` routes readers into 6 silo clusters via collection cards; "Start Here" nav link added; indexable Hugo content page using existing collection CSS |
| Category hub top-picks upgrade | Day 48j | All 6 silo `_index.md` pages now show a "Where to start" box with 4 curated links each; `.hub-top-picks` CSS added; no template changes |
| Internal affiliate opportunity tracker | Day 48k | `docs/AFFILIATE-TRACKER.md` lists all 37 articles with program candidate, CTA placed status, verification status, priority, and notes; no public pages or CTAs added |
| Front matter validator script | Day 48l | `scripts/validate_front_matter.py` scans all silo articles for 9 categories of front matter issues; exits non-zero on errors; first run found and fixed 2 missing slug fields |
| Internal link checker script | Day 48m | `scripts/check_internal_links.py` builds a route map from all content files and validates all internal Markdown links; first run: 0 broken links across 44 files |
| Feature image inventory checker | Day 48o | `scripts/check_feature_images.py` cross-checks article image: fields against static/img/; reports missing images as errors and unreferenced files as warnings; first run: 38/38 verified, 3 known orphans |
| Footer trust CTA cleanup | Day 46j | Pill-row flex layout for About · Disclaimer · Contact; accessible focus states |
| AdSense integration | Day 21 | Live `ca-pub-5934721249825043` in `head.html`; formal approval pending |
| Amazon Associates placement | Day 39b | US tag `freestackfi20-20` on 3 hardware-adjacent pages |
| Article schema and noindex metadata | Day 45c | Article-style schema suppressed on utility/noindex pages |
| JSON-LD structured data | Early work | Present on all article pages via `layouts/partials/schema.html` |
| Feature image system | Day 30 onward | Python + Pillow, 1200×630 WebP, `scripts/images/` folder |
| Homepage featured/latest sorting | Days 17, 46e | Weight-sorted featured, date-sorted latest, curated collections |

---

## Recommended Feature Roadmap

Work through phases in order. Within a phase, pick the item with the clearest benefit and lowest complexity first.

---

## Phase 1 — Extend Existing Article UX Systems

These items extend components already built. They require no new architecture, only rollout to additional articles.

**1.1 Expand comparison tables to more high-intent articles** ✓ Done Day 47b

The `comparison-table` shortcode is now deployed on 11 articles. All 7 recommended target pages received tables on Day 47b: `free-crm-software`, `free-invoicing-software`, `free-project-management-software`, `free-cloud-storage-comparison`, `free-video-editing-software`, `photoshop-alternatives`, `free-password-managers`. Tables sit immediately after the Quick verdict section on each page.

**1.2 Expand verdict badges to more comparison pages** ✓ Done Day 48f

The `verdict.html` shortcode is now deployed on 11 articles. All 7 recommended target pages received badges on Day 48f: `free-password-managers`, `free-project-management-software`, `free-crm-software`, `free-invoicing-software`, `free-cloud-storage-comparison`, `free-video-editing-software`, `photoshop-alternatives`. Each page has 3 defensible per-tool labels matching the article's existing verdicts.

**1.3 Add sticky article table of contents for long guides**

Long articles (6+ tool sections) would benefit from a sticky ToC in the sidebar. Implementation: parse `##` or `###` headings in Hugo using `findRE` on `.Content`; render as a fixed-position sidebar list on desktop; hide on mobile. No external dependencies needed.

Defer until at least one article clearly needs it — likely worth building when article length regularly exceeds 2,500 words.

---

## Phase 2 — Improve Discovery and Retention

**2.1 Upgrade search result cards with category, summary, and freshness** ✓ Done Day 48g

Search index updated to include `date` and `lastmod` fields. Result cards now show: category pill (existing), title link (existing), description excerpt (existing), and a freshness line — "Updated [date]" in primary color when `lastmod ≠ date`, "Published [date]" in muted text otherwise. Changes to `layouts/index.json`, `static/js/search.js`, and `static/css/style.css` only.

**2.2 Add a Start Here / guided entry page** ✓ Done Day 48i

`/start-here/` page live. Routes readers by use case across all 6 silos: freelancer/solo → Business cluster; replacing Office → Productivity cluster; safer accounts → Security cluster; creative/design → Creative cluster; storage/backup → Cloud cluster; video/media → Video cluster. Six collection cards with 4 curated links each. "Start Here" nav link added at weight 0. Implemented as a standard indexable Hugo content page using existing `.collection-card` CSS — no new layout or shortcode required.

**2.3 Improve category hub pages with top picks and starter paths** ✓ Done Day 48j

All six silo `_index.md` files updated. Each hub now shows a "Where to start" box with 4 curated links and a one-line decision guide per link. No list template changes — content renders via existing `category-intro` div. Two CSS rules added for `.hub-top-picks` styling. Article lists and pagination unchanged.

---

## Phase 3 — Monetization and Trust Operations

**3.1 Create an internal affiliate opportunity tracker** ✓ Done Day 48k

`docs/AFFILIATE-TRACKER.md` created. Lists all 37 articles with: program candidate, CTA placed status, verification status, priority, and notes. Deferred rows clearly marked "Not suitable" or "Deferred". Safety rules and pending program actions included. No public pages or CTAs added.

**3.2 Create a reusable affiliate CTA shortcode**

If CTA blocks become hard to maintain across many articles (copy changes, URL updates), a Hugo shortcode like `{{< affiliate-cta program="nordvpn" >}}` could manage CTA content from a central data file. Build only when duplication is genuinely painful — currently 3–4 CTA variants across 33 articles is manageable inline.

**3.3 Improve the "Report outdated info" flow**

The footer currently links to `/contact/` which uses a direct email fallback. When a real form backend is available (e.g. Netlify Forms, Formspree with a live account), replace the email fallback with a prefilled form that passes the current page URL via query string. Defer until backend is available.

---

## Phase 4 — Content Operations and QA Tooling

**4.1 Article front matter validator script** ✓ Done Day 48l

`scripts/validate_front_matter.py` created. Checks all articles under `content/<silo>/`: missing required fields, banned keys (`featured`, `faqs`), future dates, bare unquoted dates, image path format, image file existence, empty/overlong descriptions, duplicate slugs, and accidental `noindex` on silo articles. Run with `python3 scripts/validate_front_matter.py`. On first run: fixed 2 articles missing `slug` field; 18 description-length warnings remain as informational backlog.

**4.2 Internal link checker script** ✓ Done Day 48m

`scripts/check_internal_links.py` created. Builds a route map from all content files (slug overrides respected, section indexes included). Scans all `.md` files under `content/` for `[text](/path/)` links; skips external, mailto, tel, and anchor-only links. Strips fragments before matching; normalizes trailing slash. Run with `python3 scripts/check_internal_links.py`. First run: 44 files · 53 known routes · 0 broken links — PASSED.

**4.3 Feature image inventory checker script** ✓ Done Day 48o

`scripts/check_feature_images.py` created. Scans all silo articles for `image:` field; checks each referenced file exists in `static/img/`; flags non-WebP extensions as warnings; reports files in `static/img/` not referenced by any article as possible orphans (warnings, not errors). Run with `python3 scripts/check_feature_images.py`. First run: 38 articles checked · 38 images verified · 0 errors · 3 possible orphans (`default-article.jpg`, `nordpass-banner.png`, `nordvpn-banner.png`) — PASSED with warnings. Orphans left in place pending confirmation.

**4.4 GSC notes template**

A lightweight Markdown table or section inside `freestackfinder-progress-log.md` for tracking GSC snapshots (date, impressions, clicks, avg position, CTR, notable query/page movements). Currently snapshots are logged inline in daily entries, which makes trend comparison difficult. Build when GSC data starts influencing content decisions regularly (likely month 4–6).

---

## What Not To Build Yet

Do not build these until traffic, income, or operational complexity clearly demands them.

- **User accounts or saved lists** — requires backend and authentication; not justified for current traffic
- **User ratings or reviews** — community features require moderation and a user base; not yet relevant
- **Dynamic database-backed tool directory** — a filterable live database of tools is a different product class from an editorial comparison site; premature for current scale
- **Heavy JavaScript search framework** (Algolia, Fuse.js, Lunr) — current vanilla JS search handles 33 articles comfortably; only revisit if article count exceeds 150+ and search quality degrades
- **Newsletter backend** — an email list is valuable but requires a publishing plan and consistent send cadence; don't build the infrastructure without the content plan
- **Complex affiliate dashboards** — tracker notes and a flat markdown table are sufficient at current affiliate scale
- **Comparison app with dynamic filters** — users filtering by price tier, storage limit, seat count, etc. is a SaaS product feature; editorial comparison tables serve the same intent without the complexity
- **Pagination redesign** — current paginator behavior is correct; do not rebuild unless a specific bug or usability issue emerges
- **Dark/light mode toggle** — the site already uses a dark-by-default design; a toggle adds complexity without clear reader benefit at current traffic

---

## How To Choose The Next Feature

Use this decision order:

1. Is there a completed-system rollout that a high-intent article is missing? (Phase 1 items — do these first.)
2. Is there a discovery or retention gap hurting bounce rate or repeat visits on pages that already have traffic? (Phase 2.)
3. Is there a monetization gap on a page with real impressions where a CTA, badge, or affiliate link is missing? (Phase 3.)
4. Is there a recurring QA or operations pain that a script would eliminate? (Phase 4.)
5. If none of the above, continue publishing new articles — content compounds faster than features at current stage.

Do not build a feature just because it seems like a good idea in isolation. Every feature that is not a content article is a debt against the publishing schedule.

---

## Suggested Next Feature

**Publish the next Business silo article (content, not feature work)**

Phase 2, Phase 3.1, Phase 4.1, Phase 4.2, and Phase 4.3 are now complete. The full QA tooling suite is in place. The site has 38 articles; the Business silo is at 11/13 with two Later-priority articles remaining: `free-web-analytics` and `free-hr-software`.

Why to do this next:
- All Phase 1, 2, and planned Phase 4 QA tools are complete.
- Content compounds faster than features at current traffic levels.
- The next strongest article is `free-web-analytics` — relevant to all site operators, high search volume, fits the site's comparison format.

If feature work is preferred over content, the next candidate:
- **Phase 3: Affiliate verification pass** — use `docs/AFFILIATE-TRACKER.md` to confirm which High-priority articles already have CTAs placed, then add any missing ones (NordVPN, NordPass, Canva, Grammarly priority pages).

---

## Maintenance Notes

- Update the **Completed Feature Systems** table when any new feature ships.
- Update the **Suggested Next Feature** section after completing the current recommendation.
- If a feature from the roadmap is deferred or dropped, move it to **What Not To Build Yet** with a reason.
- This file is for feature planning only — article publishing decisions live in `CONTENT-STRATEGY.md` and `freestackfinder-progress-log.md`.
- Major UX or infrastructure review work belongs to Codex, not daily Claude runs. Daily runs should focus on rollouts of existing components and small scoped features only.
