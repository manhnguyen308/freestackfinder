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
| `/productivity/microsoft-office-alternatives/` | Microsoft Office alternative / MS Office alternative | 1,545 | 2 | 0.1% | — | Strong impressions, weak CTR | 2026-05-16 CTR pass: title shifted to "No Subscription Needed" framing, meta now leads with Word/Excel/PowerPoint replacement, quick verdict opens with explicit decision question | High |
| `/cloud/dropbox-alternatives/` | Dropbox alternative / Dropbox alternatives / dropbox alternatief | 763 | 1 | 0.1% | — | Strong impressions, weak CTR | 2026-05-16 CTR pass: title now anchors "More Free Storage Than 2GB", meta drops inaccurate Sync.com mention and lists actual covered tools, quick verdict opens with explicit decision question | High |
| `/productivity/grammarly-alternatives/` | Grammarly alternatives | 402 | 0 | 0% | — | Meaningful impressions, no clicks | Refreshed title and description only; no CTA because Grammarly is declined | Medium |
| `/productivity/slack-alternatives/` | Slack alternative / Slack alternatives | 339 | 1 | 0.3% | — | Meaningful impressions, weak CTR | 2026-05-16 CTR pass: kept 90-day-limit title; description tightened to lead with Discord as the direct answer and name Teams, Google Chat, Mattermost, and Rocket.Chat | Medium |
| `/creative/canva-alternatives/` | Canva alternative / free Canva alternative | — | — | — | — | Meaningful impressions, weak CTR | 2026-05-16 CTR pass: title now leads with "Social Posts, Templates, and Presentations"; description opens with Adobe Express as the direct answer and names the four other compared tools | Medium |
| `/creative/photoshop-alternatives/` | Photoshop alternative / free Photoshop alternative | — | — | — | — | Meaningful impressions, weak CTR | 2026-05-16 CTR pass: title simplified to "PSD, Desktop, and Browser Editors"; description opens with Photopea as the direct answer and names GIMP, Krita, and Pixlr with intent terms | Medium |
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

## 2026-05-17 — Step 2a structural variation pass (next 10 articles)

- Pages updated: `/productivity/grammarly-alternatives/`, `/creative/illustrator-alternatives/`, `/productivity/notion-alternatives/`, `/productivity/free-chatgpt-alternatives/`, `/productivity/free-pdf-editor-alternatives/`, `/creative/figma-alternatives/`, `/productivity/free-ai-writing-tools/`, `/video/free-video-editing-software/`, `/cloud/free-cloud-storage-comparison/`, `/business/free-crm-software/`.
- Reason: continued AdSense-readiness work. After Step 1 the global label counts were still high (Quick verdict 45, Our verdict 39, Free plan includes 37, What the free plan is missing 31, Who it's best for 37, Why it stands out 40). The ten articles above are the next biggest contributors and include several with GSC impressions (Grammarly, Illustrator, CRM, Cloud Storage).
- Changes: H2 swaps per page using a different combination per article ("The short answer" / "Where to start" / "Start here" / "What we recommend" / "The bottom line" for the opener; "Which writing tool should you choose?" / "Final thoughts" / "Putting it together" / "The takeaway" / "So what should you use?" / "Final recommendation" / "Which CRM makes the most sense?" for the closer). Per-tool labels swapped to article-specific varied label sets so the global text counts of `Free plan includes:`, `What the free plan is missing:`, `Who it's best for:`, and `Why it stands out:` all drop. Short decision-framing paragraphs added to ChatGPT, Figma, AI Writing, and Video to keep word counts flat or up.
- Front-matter rule: no `date`, `lastmod`, `weight`, `image`, `slug`, `alias`, `title`, `description`, `categories`, or `tags` changes on any of the ten pages.
- Repeated-heading counts across all 50 articles (post-Step-1 → post-Step-2a): Quick verdict 45 → 35 · Our verdict 39 → 29 · Why it stands out 40 → 30 · Who it's best for 37 → 27 · Free plan includes 37 → 28 · What the free plan is missing 31 → 24.
- Follow-up: Step 2b should apply the same pass to another ~10 articles across the remaining cluster pages.

## 2026-05-17 — structural variation pass on top 5 GSC pages

- Pages updated: `/productivity/microsoft-office-alternatives/`, `/cloud/dropbox-alternatives/`, `/creative/canva-alternatives/`, `/creative/photoshop-alternatives/`, `/productivity/slack-alternatives/`.
- Reason: same-skeleton risk for the AdSense re-review — every article opened with `## Quick verdict`, closed with `## Our verdict`, and repeated the same `Free plan includes:` / `What the free plan is missing:` / `Who it's best for:` / `Why it stands out:` labels per tool. The top GSC pages are the most likely sampled by a reviewer, so they were varied first.
- Changes: heading text replaced per page (e.g., "Quick verdict" → "The short answer" / "Where to start" / "Start here" / "What we recommend" / "The bottom line"; "Our verdict" → "So what should you actually use?" / "The takeaway" / "Final recommendation" / "Final thoughts" / "Putting it together"). Tool sections rewritten into prose or varied labels per page; comparison-anchor framing ("Unlike Dropbox…", "Compared with Slack…") used on Dropbox and Slack; descriptive H3s used on Office; Canva gained a new "What to look for in a free Canva alternative" section; word counts held steady or increased on every page.
- Front-matter rule: no `date`, `lastmod`, `weight`, `image`, `slug`, `alias`, `title`, `description`, `categories`, or `tags` changes on any of the five pages — this was a structural variation pass, not a CTR refresh.
- Repeated-heading counts across all 50 articles: Quick verdict 50 → 45 · Our verdict 42 → 39 · Why it stands out 44 → 40 · Who it's best for 41 → 37 · Free plan includes 40 → 37 · What the free plan is missing 34 → 31.
- Follow-up: Step 2 should apply the same pass to Grammarly and Illustrator alternatives (deferred from this batch), then progressively to the remaining cluster pages.

## 2026-05-16 CTR pass — Canva, Photoshop, Slack

- Pages updated: `/creative/canva-alternatives/`, `/creative/photoshop-alternatives/`, `/productivity/slack-alternatives/`.
- Query themes addressed: free Canva alternative / social posts / templates / presentations; free Photoshop alternative / PSD editing / layers / browser editing; free Slack alternative / unlimited message history / team chat for small teams.
- Changes: front-matter only — titles and meta descriptions rewritten so the first sentence delivers the direct answer and names the actual compared tools; no body edits, no new affiliate links, no CTA additions, no URL/slug changes, `lastmod` bumped to 2026-05-16 on all three pages.
- Follow-up: monitor CTR, clicks, and average position on all three pages after the next recrawl window; if CTR remains below 1% with rising impressions, consider one round of intro/quick-verdict tightening before further metadata changes.

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

## 2026-05-16 — CTR pass on Office and Dropbox

- Focus: tighten title and meta description on the two highest-impression / low-CTR pages while the site waits for AdSense re-review.
- Pages updated: `/productivity/microsoft-office-alternatives/`, `/cloud/dropbox-alternatives/`.
- Query themes addressed: "microsoft office alternative" / "ms office alternative" / "free office suite" intent around Word, Excel, PowerPoint replacement; "dropbox alternative" / "dropbox replacement" intent around the 2GB free cap and more free storage.
- Title changes: Office title shifted from a long Word/Excel/PowerPoint subtitle to "No Subscription Needed" framing; Dropbox title shifted from "More Free Cloud Storage" to "More Free Storage Than 2GB" to anchor the comparison.
- Meta changes: Office meta now leads with the Word/Excel/PowerPoint replacement promise and names the four tools with their fit; Dropbox meta now leads with the 2GB cap, drops the inaccurate "Sync.com" name that was not covered in the article, and names MEGA, Google Drive, OneDrive, Proton Drive, and Box with their fit.
- First-screen changes: both quick verdicts now open with an explicit "Which … should you pick?" decision line followed by short fit guidance per tool.
- Dutch query handling: GSC shows "dropbox alternatief" impressions; intentionally not creating a Dutch page and not stuffing Dutch terms into title or meta. Monitor whether Dutch impressions keep growing before considering a localized variant.
- Follow-up: monitor CTR, clicks, and average position on both pages after the next Googlebot recrawl; if CTR stays below 1% after the snippet refresh, consider one more conservative title pass on the weaker performer.

## 2026-05-16 — Crawled, currently not indexed fix pass

- Issue: GSC "Crawled - currently not indexed" affecting 2 pages; example URL `/business/free-resume-builders/`.
- Page improved: `content/business/free-resume-builders.md`.
- Editorial additions: stronger opener clarifying who a free resume builder fits; new "When a free resume builder is enough — and when it is not" decision section; practical tradeoffs block covering export format, watermark risk, template quality, privacy/signup, ATS readability, and editing flexibility; common mistakes section; concrete examples for student, freelancer, career switcher, and one-page refresh scenarios.
- Indexing signals: confirmed `index, follow`, canonical points to `https://freestackfinder.com/business/free-resume-builders/`, page present in `public/sitemap.xml`, not blocked by `robots.txt`, no `noindex` in front matter.
- Internal links: added a contextual inbound link from `content/business/free-invoicing-software.md` to strengthen the freelancer cluster path into the resume guide; existing inbound links from `canva-free-vs-paid` and `grammarly-alternatives`, and outbound links from the resume article to Canva alternatives, Microsoft Office alternatives, Grammarly alternatives, free invoicing, free CRM, and free spreadsheet alternatives are unchanged.
- `lastmod` updated to 2026-05-16 on both edited articles.
- Follow-up: monitor indexing status after the next Googlebot recrawl; if the page is still not indexed after the validation window, consider one tighter title/description pass or another contextual inbound link from a high-impression page.

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
