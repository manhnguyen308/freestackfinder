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

## 2026-05-05 high-impression quality pass

- Focus: E-E-A-T and human-value improvement on the top 5 high-impression pages ahead of AdSense re-review.
- Pages improved: `/productivity/microsoft-office-alternatives/`, `/cloud/dropbox-alternatives/`, `/productivity/grammarly-alternatives/`, `/productivity/slack-alternatives/`, `/creative/illustrator-alternatives/`.
- Type of editorial additions: decision logic, practical tradeoffs, common mistakes, "who should skip" notes, and use-case guidance — all written in terms not copyable from a product page, without fake testing claims or affiliate CTAs.
- Specific signals added:
  - Office: OnlyOffice tracked-change compatibility note; WPS "who should skip" guidance.
  - Dropbox: MEGA monthly transfer quota practical limit; Google Drive shared-storage trap; common cloud storage mistakes section.
  - Grammarly: LanguageTool character-limit practical note; "which tool for which writing task" combination guide.
  - Slack: Discord work-team setup guidance; common transition mistakes section.
  - Illustrator: Client .ai file compatibility decision point; Inkscape vs Gravit practical comparison; expanded "Making the switch" section.
- Validation: git diff --check clean · QA 3/3 passed (46 articles, 0 broken links, 0 front matter errors) · hugo --minify clean · all 5 pages confirmed index, follow · lastmod updated to 2026-05-05 on all 5 articles.
- Article count: 46 unchanged. No new articles. No URL/slug changes. No affiliate CTAs added.
- Follow-up: monitor CTR and avg position on these 5 pages after next Googlebot recrawl cycle; if CTR remains below 1% at next GSC window, consider a title/description pass on the lowest performers.

## 2026-05-05 production polish follow-up

- Focus: fix high-impression quality issues found after the earlier content pass, especially raw `verdict-box` markup and metadata drift.
- Pages updated: `/productivity/microsoft-office-alternatives/`, `/creative/photoshop-alternatives/`, `/creative/canva-alternatives/`, `/productivity/slack-alternatives/`, `/cloud/dropbox-alternatives/`, `/productivity/grammarly-alternatives/`, `/creative/illustrator-alternatives/`.
- Issues fixed: removed legacy raw `verdict-box` HTML from Office and Photoshop articles; corrected Photoshop source date to match its 2026 title and `lastmod`; rewrote Canva's meta description as reader-facing copy; added Slack homepage weight for Most Popular eligibility.
- Quality improvements: reduced repeated section-label patterns and added practical decision logic around compatibility, free-plan limits, small-team workflow fit, and export/collaboration friction.
- Follow-up: monitor CTR, clicks, and impressions on these pages after the next recrawl. If the snippets update but CTR remains below 1%, consider one small title or description adjustment on the lowest-performing page rather than another broad rewrite.

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
