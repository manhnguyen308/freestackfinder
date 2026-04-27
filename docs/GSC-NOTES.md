# FreeStackFinder — Search Performance Notes

Internal operations file. Not a public page. Do not reference this in site content or commit messages.

**Update cadence:** light check weekly · deeper review monthly · after each major content batch

---

## Snapshot history

| Date | Clicks | Impressions | CTR | Avg position | Notes |
|------|--------|-------------|-----|--------------|-------|
| 2026-04-15 | 5 | 2,220 | 0.2% | 54.4 | Baseline — site indexed but early-stage; no query dominance yet |

---

## Page opportunity table

Track pages worth acting on. Only record pages with meaningful impression counts or clear issues.

| Page | Query / theme | Impressions | Clicks | CTR | Avg pos | Issue | Next action | Priority |
|------|--------------|-------------|--------|-----|---------|-------|-------------|---------|
| — | — | — | — | — | — | First GSC data pull pending | Check after month 2 | — |

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
