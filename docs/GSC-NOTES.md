# FreeStackFinder — Search Performance Notes

Internal operations file. Not a public page. Do not reference this in site content or commit messages.

**Update cadence:** light check weekly · deeper review monthly · after each major content batch

---

## Snapshot history

| Date | Clicks | Impressions | CTR | Avg position | Notes |
|------|--------|-------------|-----|--------------|-------|
| 2026-04-28 | 13 | 4,640 | 0.3% | 51.7 | Last 3 months — impressions concentrated on Office, Dropbox, Grammarly, Photoshop, Canva, Slack, Illustrator, backup, QuickBooks, and project management pages |
| 2026-04-15 | 5 | 2,220 | 0.2% | 54.4 | Baseline — site indexed but early-stage; no query dominance yet |

---

## Page opportunity table

Track pages worth acting on. Only record pages with meaningful impression counts or clear issues.

| Page | Query / theme | Impressions | Clicks | CTR | Avg pos | Issue | Next action | Priority |
|------|--------------|-------------|--------|-----|---------|-------|-------------|---------|
| `/productivity/microsoft-office-alternatives/` | Microsoft Office alternative / MS Office alternative | 1,545 | 2 | 0.1% | — | Strong impressions, weak CTR | Refreshed title, description, and first-screen wording around Word/Excel/PowerPoint replacement intent | High |
| `/cloud/dropbox-alternatives/` | Dropbox alternative / Dropbox alternatives | 763 | 1 | 0.1% | — | Strong impressions, weak CTR | Refreshed title, description, and quick verdict around more free cloud storage | High |
| `/productivity/grammarly-alternatives/` | Grammarly alternatives | 402 | 0 | 0% | — | Meaningful impressions, no clicks | Refreshed title and description only; no CTA while program remains under review | Medium |
| `/productivity/slack-alternatives/` | Slack alternative / Slack alternatives | 339 | 1 | 0.3% | — | Meaningful impressions, weak CTR | Refreshed title, description, and quick verdict around the 90-day history limit | Medium |
| `/creative/illustrator-alternatives/` | Illustrator alternatives | 249 | 0 | 0% | — | Meaningful impressions, no clicks | Refreshed title and description; removed unsupported "tested" wording | Medium |
| `/cloud/free-backup-software/` | Free backup software | 143 | 0 | 0% | — | Description was not search-snippet friendly | Rewrote description to explain backup use case and tools | Medium |
| `/business/quickbooks-alternatives/` | QuickBooks alternatives | 141 | 0 | 0% | — | Meaningful impressions, no clicks | Refreshed title and description around freelancer accounting intent | Medium |
| `/business/free-project-management-software/` | Free project management software | 94 | 0 | 0% | — | Below 100 impressions but in priority set | Tightened description only; existing hub and related links are sufficient | Low |

## 2026-04-28 review notes

- Overall snapshot: 13 clicks, 4.64K impressions, 0.3% CTR, average position 51.7 over the last 3 months.
- Query themes: Microsoft Office replacement, Dropbox replacement, Slack replacement, Grammarly alternatives, Illustrator alternatives, free backup software, QuickBooks alternatives, and free project management tools.
- Actions taken: refreshed query-aligned titles/descriptions and a few first-screen verdict lines on priority pages; no new articles, URL changes, slug changes, affiliate links, or Canva/Grammarly CTAs.
- Internal links: existing hub, related-guide, and contextual links already cover the priority pages; no mass backlinking added.
- Follow-up: monitor the same pages after the next GSC data window; consider another small title/meta pass only if impressions rise and CTR remains below 1%.

## 2026-05-02 weekly review notes

- No fresh GSC export was available in the repo, so the 2026-04-28 snapshot remains the current baseline.
- Rechecked the eight priority pages from the snapshot for title, description, first-screen clarity, and query fit; the prior CTR-focused updates still look aligned and did not need another title or description change.
- Discovery follow-up: the two newest Cloud email guides were added to the curated related-guides map so email-service and email-workflow readers can move between the relevant Cloud pages more easily.
- Site-name follow-up: manifest colors were aligned with the homepage head theme color after the recent site-name signal pass.
- Follow-up: monitor the same high-impression pages after the next GSC data window before making another snippet change.

---

## Action rules

- **CTR issue** — consider title or meta description refresh only if the page has 100+ impressions and CTR is below 1%; do not rewrite titles on new pages
- **Position 8–20** — consider adding internal links from related pages and strengthening the intro; avoid full rewrites
- **Newly published (< 4 weeks)** — do not edit; let Google settle the ranking signal
- **Already improving** — if impressions or position are trending better week-over-week, leave the page alone
- **Do not chase every query** — focus on pages already getting impressions, not zero-data guesses
- **One change at a time** — make one small trackable edit per session so you can attribute any movement

---

## What to record each session

Paste a short snapshot from GSC (Property → Performance → Last 28 days):

- Date of check
- Total clicks / impressions / CTR / avg position
- Top 3 pages by impressions (query and position)
- Any page that jumped into positions 8–20 since last check
- Any page with high impressions but CTR below 1%
- Any clear internal linking gap spotted while reviewing

Do not paste raw GSC exports or large data tables. Record only actionable observations.

---

## Monthly deeper review checklist

Run once per month (belongs to Codex, not daily Claude runs, unless explicitly assigned):

- [ ] Review top 5 articles for outdated pricing, limits, or features
- [ ] Update `lastmod` on any changed article
- [ ] Check affiliate links and redirects still work
- [ ] Identify pages in positions 8–20 as quick-win candidates
- [ ] Check if any new query theme warrants a new article
