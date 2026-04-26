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

**2.1 Upgrade search result cards with category, summary, and freshness**

Current search results show title and a plain text excerpt. Improved cards would show: article title, silo/category tag, description excerpt, and lastmod date. This requires updating `static/js/search.js` and search result CSS only — no Hugo output changes.

**2.2 Add a Start Here / guided entry page**

A `/start-here/` page that routes readers by use case: "I'm a freelancer" → Business cluster; "I'm replacing Microsoft Office" → Productivity cluster; "I want better security" → Security cluster. Static Hugo content page with curated links. Low-effort, high-value for first-time visitors from SEO.

Build after site reaches 40+ articles so there is enough content to surface meaningful paths.

**2.3 Improve category hub pages with top picks and starter paths**

Each silo `_index.md` currently has a short description. Upgrading these pages to show top 3 recommended articles and a decision-entry line ("If you just need X, start with Y") would improve category-level engagement. Requires edits to `layouts/_default/list.html` and the `_index.md` files — no new shortcodes.

---

## Phase 3 — Monetization and Trust Operations

**3.1 Create an internal affiliate opportunity tracker**

A simple table inside `freestackfinder-progress-log.md` or a dedicated `AFFILIATE-TRACKER.md` listing: each article, which affiliate program applies, whether a CTA is placed, and whether the link is verified. Currently this state lives in scattered tracker notes. Consolidating it helps identify monetization gaps without a full audit.

**3.2 Create a reusable affiliate CTA shortcode**

If CTA blocks become hard to maintain across many articles (copy changes, URL updates), a Hugo shortcode like `{{< affiliate-cta program="nordvpn" >}}` could manage CTA content from a central data file. Build only when duplication is genuinely painful — currently 3–4 CTA variants across 33 articles is manageable inline.

**3.3 Improve the "Report outdated info" flow**

The footer currently links to `/contact/` which uses a direct email fallback. When a real form backend is available (e.g. Netlify Forms, Formspree with a live account), replace the email fallback with a prefilled form that passes the current page URL via query string. Defer until backend is available.

---

## Phase 4 — Content Operations and QA Tooling

**4.1 Article front matter validator script**

A Python script that reads all article markdown files, parses front matter, and flags: missing required fields (title, description, date, slug, image, categories), future dates, bare unquoted dates, `featured:` or `faqs:` keys, `image` paths not matching a file in `static/img/`. Run manually before major publishing batches.

**4.2 Internal link checker script**

A Python script that scans all article markdown for `[text](/path/)` style links and confirms each internal target resolves to a published article. Flags broken or missing internal links. Run after publishing a batch of new articles or before a major link audit.

**4.3 Feature image inventory checker script**

A Python script that compares the `image:` field in every article's front matter against actual files in `static/img/`. Reports: articles missing a feature image on disk, images in `static/img/` not referenced by any article (orphaned files). Run after publishing batches or before a storage cleanup.

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

**Upgrade search result cards with category, summary, and freshness**

Current search results show title and a plain text excerpt. Improved cards would show: article title, silo/category tag, description excerpt, and lastmod date. This requires updating `static/js/search.js` and search result CSS only — no Hugo output changes needed.

Why to do this next:
- Phase 1 rollout items (comparison tables, verdict badges) are now complete.
- Search is already live and functional — this is an incremental improvement to an existing system.
- Adding category tags and freshness dates to search results helps readers evaluate results faster, reducing bounce from search.
- Low complexity: JavaScript and CSS changes only, no new Hugo partials or shortcodes required.
- Consistent with Phase 2 goal: improve discovery and retention on pages that already have traffic.

---

## Maintenance Notes

- Update the **Completed Feature Systems** table when any new feature ships.
- Update the **Suggested Next Feature** section after completing the current recommendation.
- If a feature from the roadmap is deferred or dropped, move it to **What Not To Build Yet** with a reason.
- This file is for feature planning only — article publishing decisions live in `CONTENT-STRATEGY.md` and `freestackfinder-progress-log.md`.
- Major UX or infrastructure review work belongs to Codex, not daily Claude runs. Daily runs should focus on rollouts of existing components and small scoped features only.
