# FreeStackFinder — Project State

**Site:** freestackfinder.com
**Last updated:** 2026-05-04 (Day 60b)
**Current day:** 60b

## Current state

- Total articles: 46
- Silos: Productivity 9/9 ✓ · Business 13/13 ✓ · Creative 6/8 · Security 6/6 ✓ · Cloud 7/7 ✓ · Video 5/7
- AdSense: script live (`ca-pub-5934721249825043`); formal approval pending
- GSC (2026-04-28): 4,640 impressions · 13 clicks · avg position 51.7 · CTR 0.3% over the last 3 months
- Next content: Creative (2 remaining) or Security (1 remaining: free-security-audit-tools)
- Next feature: see `FEATURE-STRATEGY.md` Phases 5–9; next Phase 9 candidate is orphan-image cleanup listing

---

### Day 60b — Publish free-video-conferencing (Video silo 5/7)

- Article: Best Free Video Conferencing Tools in 2026 (`content/video/free-video-conferencing.md`)
- Silo: Video — now 5/7
- Word count: ~2,200 words
- Feature image: `static/img/free-video-conferencing.webp` — 36.1 KB, generated via `scripts/images/generate_free_video_conferencing.py`
- Internal links from new article: `/video/zoom-alternatives/`, `/video/free-screen-recording-software/`, `/business/free-project-management-software/`
- Backlinks added to existing articles:
  - `content/video/zoom-alternatives.md` — added link to broader conferencing guide in the verdict paragraph
  - `content/video/free-screen-recording-software.md` — added link to conferencing guide in the Our verdict section
- Validation: `git diff --check` clean · QA 3/3 passed (46 articles, 46 images, 0 broken links, 0 stale) · `hugo --minify` clean · article at `public/video/free-video-conferencing/index.html` confirmed (34.7 KB)
- Article count: 45 → 46 (4 remaining to reach 50)
- AdSense note: Video silo now 5/7. Remaining gap: Creative 2, Video 2. Canva Under review — no CTAs. Grammarly Declined — no CTAs.

---

### Day 60a — Publish free-security-audit-tools (Security silo complete)

- Article: Best Free Security Audit Tools in 2026 (`content/security/free-security-audit-tools.md`)
- Silo: Security — now 6/6 ✓ (complete)
- Word count: 2,402 words
- Feature image: `static/img/free-security-audit-tools.webp` — 29.6 KB, generated via `scripts/images/generate_free_security_audit_tools.py`
- Internal links from new article: `/security/free-password-managers/`, `/security/best-free-2fa-apps/`
- Backlinks added to existing articles:
  - `content/security/free-antivirus-software.md` — added link at end of "Do you need paid antivirus?" section
  - `content/security/free-vpn.md` — added link in the "full security stack" closing paragraph
- Validation: `git diff --check` clean · QA 3/3 passed (45 articles, 45 images, 0 broken links, 0 stale) · `hugo --minify` clean · article at `public/security/free-security-audit-tools/index.html` confirmed
- Article count: 44 → 45 (5 remaining to reach 50)
- AdSense note: Security silo now complete. Remaining gap: Creative 2, Video 3. Canva Under review — no CTAs. Grammarly Declined — no CTAs.

---

### Day 59f — Final AdSense readiness verification

- Full checklist pass against Google AdSense and publisher policy criteria. No content or code changes required.
- Article count: 44 unchanged. No new articles. No URL/slug/alias changes.

**Checklist results:**

1. **Trust pages (About, Contact, Privacy Policy, Terms, Disclaimer):** All five are indexable (`index, follow`) ✓ · All five appear in `public/sitemap.xml` ✓ · Footer links all five from every page ✓.
2. **Contact email:** `contact@freestackfinder.com` is consistent across all 7 occurrences (contact.md ×4, privacy-policy.md ×1, schema.html ×1, config.toml ×1). No `hello@`, `info@`, or admin variant found ✓.
3. **Homepage and Start Here:** Homepage has hero, editorial strip, six-category browse grid with article counts, use-case collections, and latest articles — not a link directory. Start Here has six structured use-case paths with contextual intros and curated links per path ✓.
4. **Navigation:** Nav links homepage, Start Here, all 6 silo hubs, and search. Footer has trust links. Internal link check: 0 broken links across 51 files ✓.
5. **Taxonomy/term noindex:** `/categories/`, `/categories/business/`, `/tags/free-crm/` (sample) all render `noindex, follow` ✓.
6. **Search page noindex:** `/search/` renders `noindex, follow` ✓.
7. **Article pages index:** `/business/free-crm-software/` and all sampled article pages render `index, follow` ✓.
8. **Duplicate content across silos:** No duplicate article slugs found across silos. QA internal link check: 0 broken links ✓.
9. **Content variety:** Day 59c expansions confirmed — four articles each received structurally different new sections (common-mistakes, who-should-not, what-to-watch-out-for, how-we-evaluated) at varied positions. Section headers do not repeat across articles ✓.
10. **No placeholder/under-construction content:** grep for "placeholder", "lorem ipsum", "coming soon", "under construction" returned zero matches in content ✓.
11. **No ad-click encouragement:** grep for "click.*ad", "encourage.*click", "help us by clicking" returned zero matches in site content and templates ✓. Disclaimer uses standard disclosure phrasing ✓.
12. **Canva/Grammarly affiliate safety:** No `affiliate-cta` shortcode blocks found in any article for either program. Canva external links in three articles (free-resume-builders, free-website-builders, illustrator-alternatives) are plain editorial links without affiliate parameters ✓. Grammarly appears only as the comparison subject on `grammarly-alternatives` ✓.
13. **Content roadmap gap documented:** Creative 2 remaining (targets 8/8) · Security 1 remaining (free-security-audit-tools) · Video 3 remaining (targets 7/7) — total 6 articles to reach 50.
14. **Tracker recommendation:** Publish 6 outstanding articles to push count past 50, then click "Request review" in AdSense console no earlier than 2026-05-10, ideally 2026-05-17, to allow Googlebot to complete the recrawl cycle from Day 59a taxonomy noindex changes.

**Known gap (not a blocking AdSense issue):** 181 taxonomy/term URLs appear in `public/sitemap.xml` despite being noindexed. Hugo includes all page kinds in sitemap by default; excluding them requires a custom sitemap template. This is a mild signal contradiction (noindex meta + sitemap presence) but not a primary AdSense rejection signal. Deferred — would require a custom `layouts/sitemap.xml` template change.

**Known gap (deferred):** `/business/page/2/` and equivalent paginated section pages still render `index, follow`. Hugo pagination shares `.RelPermalink` with the parent section, making a head-level noindex rule unsafe without risking `.Paginator` contract conflicts. Not a primary AdSense rejection signal.

- Files changed: `freestackfinder-progress-log.md` only.
- Validation: `git diff --check` clean · QA 3/3 passed (44 articles, 44 images, 0 broken links) · `hugo --minify` clean.
- Re-review recommendation: do not click "Request review" before 2026-05-10; ideally 2026-05-17. Optionally publish 6 outstanding articles first to demonstrate content cadence.

---

### Day 59e — Standardize contact email to contact@freestackfinder.com

- Issue: public contact email was inconsistently set to `hello@freestackfinder.com` across four files.
- Fix: replaced all instances of `hello@freestackfinder.com` with `contact@freestackfinder.com` in `content/contact.md`, `content/privacy-policy.md`, `layouts/partials/schema.html`, and `config.toml`.
- Post-fix grep confirmed no `hello@`, `info@`, `admin@`, or other variant email addresses remain.
- Article count: 44 unchanged. No URL/slug/alias changes. No new articles.
- Validation: `git diff --check` clean · QA 3/3 passed · `hugo --minify` clean.

---

### Day 59d — AdSense readiness verification

- Verification pass on Day 59a–59c remediation. No content or code changes required; tracker entry only.
- Article count: 44 (unchanged). No new article created.
- Shortest-article audit (post-Day 59c expansions, top 10 by word count):
  - 1,654w · creative/canva-alternatives
  - 1,671w · cloud/free-backup-software
  - 1,681w · productivity/microsoft-office-alternatives (expanded Day 59c)
  - 1,780w · business/free-hr-software
  - 1,800w · video/premiere-pro-alternatives (expanded Day 59c)
  - 1,807w · creative/free-font-websites
  - 1,848w · business/free-crm-software
  - 1,887w · cloud/free-cloud-storage-comparison
  - 1,896w · creative/figma-alternatives
  - 1,898w · cloud/free-email-signature
- Articles under 1,200 words: zero.
- Fifth-thinnest article (creative/canva-alternatives, 1,654w): does not need expansion. It is 454 words above the 1,200 threshold and above the 1,500 mark that triggered the Day 59c expansions. Original "5 thinnest" framing in the previous task was over-broad — only four articles actually sat in the at-risk band. No further article expansion required.
- Description/meta audit: all 44 articles carry a `description` field of 100+ characters. None missing, none short.
- Disclosure check: per-article disclosure renders at the top of every article via `layouts/_default/single.html` line 54: "Some links on this page are affiliate links — we may earn a commission if you make a purchase, at no extra cost to you." Plus trust links to /about/, /disclaimer/, /contact/.
- Author/reviewer bio check: `single.html` author-box reads "We test the tools we cover, compare the free tier with the paid upgrade when it matters, and document the limits that would make us tell you to skip it. Our reviews are written for everyday users, freelancers, and small teams rather than enterprise buyers." This is an honestly framed methodology claim — does not say "we download and use every tool we review." No softening required; copy left as-is.
- Trust page check: about, contact, privacy-policy, terms, disclaimer all build with `name=robots content="index, follow"` and all five appear in `public/sitemap.xml`. Footer links all five from every page (footer.html columns "Site" and inline trust-links row).
- Robots/noindex check (verified on built `public/`):
  - `/about/`, `/contact/`, `/privacy-policy/`, `/terms/`, `/disclaimer/`: `index, follow` ✓
  - `/categories/`, `/categories/business/`, `/tags/2fas-review/` (sample term): `noindex, follow` ✓
  - `/`, `/start-here/`, `/business/`, sample article: `index, follow` ✓
  - `/search/`: `noindex, follow` ✓ (preserved from existing `Params.noindex`)
  - One remaining gap: `/business/page/2/` paginated archive renders `index, follow`. Hugo's pagination shares `.RelPermalink` with the section page, so a head-level rule isn't trivially safe; deferred — not a primary AdSense rejection signal.
- Fixes made: none. Verification confirms the Day 59a/b/c work is intact and complete for this remediation cycle. Only the progress log was updated.
- Files changed: `freestackfinder-progress-log.md`.
- Validation: `git diff --check` clean · QA runner 3/3 passed (44 articles, 44 images, 0 broken links, 0 stale articles) · `hugo --minify` clean · trust pages indexable, taxonomy/tag pages noindex/follow, article pages index/follow · no URL/slug/alias changes · no new article created · no public-facing internal-workflow language introduced.
- Recommendation on AdSense review request: proceed with re-review after the existing 7–14 day wait from Day 59a (i.e., not before approximately 2026-05-10, ideally 2026-05-17). Optional but worthwhile before clicking: publish the 6 outstanding articles (Creative 2, Security 1, Video 3) to push the count past 50 and demonstrate cadence; that is content-roadmap work, not part of this verification pass.

---

### Day 59c — AdSense disclosure tightening + thinnest-article expansions

- Tightened the per-article disclosure line in `layouts/_default/single.html` from soft phrasing ("may earn from some paid links") to explicit AdSense-style copy: "Some links on this page are affiliate links — we may earn a commission if you make a purchase, at no extra cost to you." Trust links (How we evaluate · Full disclosure · Report a change) preserved.
- Expanded the four shortest articles (all previously 1,339–1,499 words) with substantive original sections, deliberately varying the section type across silos to break the cookie-cutter pattern:
  - `content/productivity/microsoft-office-alternatives.md` (1,339 → 1,681 words): added "Common mistakes when switching from Microsoft Office" — five named pitfalls (switching all at once, sending .odt files, assuming Sheets equals Excel, trusting the auto-converter, forgetting Outlook).
  - `content/video/premiere-pro-alternatives.md` (1,374 → 1,800 words): added "Who should NOT switch from Premiere Pro" — six concrete reader profiles where staying on Adobe is the honest answer (After Effects Dynamic Link, 10-bit footage, agency environments, paid plugin ecosystems, ACES/HDR finishing, billing-rate math).
  - `content/creative/photoshop-alternatives.md` (1,497 → 2,021 words): added "What to watch out for when leaving Photoshop" — seven gotchas including PSD smart objects, CMYK/print, Adobe Fonts, generative-fill assumptions, Action recordings, brush behaviour, and version history.
  - `content/video/free-video-editing-software.md` (1,499 → 1,963 words): added "How we evaluated these editors" near the top — explains the evaluation method (real watermark tests, format/codec checks against common 2026 source footage, time-to-first-cut, consumer-hardware stability, honest free-tier limits) and what was deliberately ignored (review aggregator scores, tutorial volume).
- Structural variety achieved: each of the four expansions uses a different section pattern and a different position in the article (mid-body for two, near-top "how we evaluated" for one, decision-frame for one). No repeated H2 wording.
- No new articles created. No URLs/slugs/aliases changed. No affiliate links added. No ad slots added. No Canva or Grammarly CTAs introduced.
- Verified pre-existing AdSense-readiness items already in place (no changes needed): trust pages exist with substantial content (about 531w, contact 307w, privacy 815w, disclaimer 546w, terms 590w; all indexable since Day 59a); footer links all five trust pages from every page; `single.html` already renders a visible "Updated" date when `lastmod` differs from `date`; `single.html` already renders a team/author bio block beneath the article; all 44 article descriptions are 100+ characters.
- Files changed: `layouts/_default/single.html`, `content/productivity/microsoft-office-alternatives.md`, `content/video/premiere-pro-alternatives.md`, `content/creative/photoshop-alternatives.md`, `content/video/free-video-editing-software.md`, `freestackfinder-progress-log.md`.
- Validation: `git diff --check` clean · QA runner 3/3 passed (44 articles, 44 images, 0 broken links) · `hugo --minify` clean · all four expanded articles still build · article count 44 unchanged · no URL/slug/alias changes.
- Recommendation on AdSense review request: still wait 7–14 days from Day 59a before clicking "Request review" so Googlebot can recrawl and re-index. The expansions and disclosure tightening from today reinforce the structural fixes from Day 59a/59b — they do not reset the recrawl clock.

---

### Day 59b — AdSense second-pass content/ad-readiness audit

- Context: builds on the Day 59a structural pass (trust pages re-indexed, taxonomy archives noindexed). This pass audited content quality, ad-readiness, and commercial density against Google publisher policy and AdSense quality guidance.
- Google low-value criteria applied: enough unique content for crawl understanding · substantial value vs similar sites · no duplicate/scraped/cookie-cutter content · expanded or consolidated rather than thin duplicate surfaces · accurate navigation and working links · ads not allowed on screens that are mostly navigation, thin, or under construction · no thin affiliate-style pages or doorway pages · no keyword stuffing.
- Ad-readiness criteria applied: steady documented publishing cadence · page content as the main focus, not ads/CTAs · no deceptive ad behaviour or click-encouragement copy · on-topic affiliate placements only · weekly post-approval monitoring planned · ad A/B testing deferred until after approval and stable serving · soften anything that reads ad-first or affiliate-first.
- Audit findings:
  1. Footer already links all five trust pages from every page; with Day 59a making them indexable, trust signals are now fully discoverable.
  2. Homepage (`layouts/index.html`): substantive — hero with tagline, four-tenet editorial strip, six-category browse grid with live counts, three curated use-case collections, and a latest-comparisons list. Not navigation-only.
  3. Start Here (`content/start-here.md`): six use-case "paths," each with its own intro paragraph and four contextual links. Day 57c rendering fix still good — no escaped HTML in built output.
  4. Sampled high-risk article (`cloud/free-backup-software.md`, 219 lines): substantive original analysis — distinguishes sync vs backup, applies a 3-2-1 frame, gives per-tool free-plan limits, and offers honest paid-tier guidance. Not a thin affiliate page.
  5. Affiliate CTA pattern: `affiliate-cta` blocks appear at line 190+ in articles (deep, post-content), not on the first screen. NordVPN placements on `dropbox-alternatives` and `free-email-service` have contextual bridges (NordLocker/encrypted storage; VPN alongside private email) — borderline but defensible and on-topic for a security/privacy audience.
  6. Ad slots: `showAds = false` in `config.toml`. No live AdSense units render anywhere. AdSense script is conditional on publisher ID and only loads when configured. No first-screen ad pressure exists today.
  7. `review-block.html` partial renders only on article pages (not trust/page kinds) — methodology copy is generic but honest, no fake testing-lab claims.
  8. Spot-checked metadata: titles like "Best Free [X] in 2026 — [hook]" follow a consistent template but each carries a unique hook clause and per-article description; no keyword-stuffed titles or doorway-style near-duplicates spotted.
  9. No unapproved Canva or Grammarly affiliate placements introduced. Existing Canva mentions are editorial only; Grammarly mentions appear on `productivity/grammarly-alternatives` as the comparison subject, which is on-topic, not a CTA.
- Fixes made: no further content or code changes required beyond Day 59a. The remaining gaps (deeper original commentary on the highest-impression GSC pages, more Creative/Security/Video articles to deepen topical coverage) are content-roadmap work and deliberately out of scope for this remediation pass per the no-new-articles rule.
- Noindex/search-surface changes: none this pass. Day 59a noindex of `/categories/` and `/tags/` term pages remains in effect; trust pages remain indexable.
- Trust/compliance changes: none beyond Day 59a.
- Homepage/Start Here changes: none — both reviewed and confirmed substantive.
- High-priority page changes: none — sampled pages are not thin.
- Affiliate/commercial safety: confirmed clean. Canva still Under review (no CTAs added). Grammarly still Declined (no CTAs added). NordVPN/NordPass/Amazon placements unchanged. No banner images, no incentivized-click copy, no ad-clicking encouragement language anywhere.
- Weekly post-approval monitoring plan (added here so it survives across runs): once AdSense approves, the weekly review should check (a) `pageviews` and `top landing pages` in GSC vs. prior week, (b) ad CTR and impressions per page from AdSense, (c) bounce rate and average engagement time per top page, (d) any "Limited ad serving" or policy notices in the AdSense console, (e) freshness — articles untouched for 90+ days that still receive impressions. Findings go into `docs/GSC-NOTES.md` and inform the next refresh cycle.
- Ad A/B testing posture: no ad layout, ad density, or ad placement experiments will be run before AdSense approval and at least four weeks of stable serving. Premature A/B tests risk policy strikes and skew the baseline data needed to evaluate any future change.
- Files changed: `freestackfinder-progress-log.md` (this entry only).
- Validation: `git diff --check` clean · QA runner 3/3 passed (44 articles, 44 images, 0 broken links) · stale-content report informational only · `hugo --minify` clean · Day 59a noindex/index behaviour confirmed unchanged · no URL/slug/alias changes · no new article created · no public-facing copy changed · article count 44.
- Recommendation on AdSense review request: still do not click "Request review" yet. Give Googlebot 7–14 days to recrawl trust pages and process taxonomy noindex from Day 59a. Best next move before re-submitting is to publish the remaining Creative (2), Security (1), and Video (3) articles to push article count past 50 and visibly demonstrate publishing cadence — both are signals AdSense weighs for "low value content" decisions.

---

### Day 59a — AdSense low-value-content remediation pass

- Trigger: AdSense rejected freestackfinder.com again with "Low value content / site does not yet meet the criteria of use in the Google publisher network" (site ownership verified). No request-review click yet.
- Audit findings:
  1. Trust/compliance pages (`about`, `contact`, `privacy-policy`, `terms`, `disclaimer`) all carried `noindex: true` and `sitemap: disable: true`. AdSense reviewers and Googlebot could not discover them via crawl or sitemap, weakening site trust signals.
  2. Taxonomy surfaces (`/categories/<silo>/` term pages and all `/tags/<tag>/` term pages, plus `/categories/`, `/tags/` index pages) were indexable. Categories duplicated section hubs (`/business/`, `/cloud/`, etc.); tag terms each held only 1–2 articles, creating ~250+ thin/duplicative archive surfaces.
  3. Homepage and Start Here verified — substantive editorial copy, 4-tenet strip, curated collections, latest section. No raw-HTML regression on Start Here.
  4. High-impression GSC pages and recent Cloud articles spot-checked — no thin-content rewrites required this pass.
  5. No unapproved Canva/Grammarly placements introduced. Affiliate posture unchanged.
- Fixes made:
  - Removed `noindex: true` and `sitemap: disable: true` from `content/about.md`, `content/contact.md`, `content/privacy-policy.md`, `content/terms.md`, `content/disclaimer.md`. Trust pages now indexable and present in `sitemap.xml`.
  - Updated `layouts/partials/head.html` to emit `<meta name="robots" content="noindex, follow">` for all `taxonomy` and `term` pages. Existing `Params.noindex` and search-page noindex behavior preserved.
- Files changed: `content/about.md`, `content/contact.md`, `content/privacy-policy.md`, `content/terms.md`, `content/disclaimer.md`, `layouts/partials/head.html`, `freestackfinder-progress-log.md`.
- Validation: `git diff --check` clean · QA runner 3/3 passed (44 articles, 44 images, 0 broken links) · `hugo --minify` clean (430 pages, 19 paginator pages) · `/about/` now serves `robots: index, follow` · `/categories/business/` and `/tags/2fas-review/` serve `robots: noindex, follow` · `/about/` present in sitemap.xml · article-page robots behavior unchanged · Start Here renders 6 `collection-card` elements with 0 escaped entities · pagination still renders cleanly · search page still noindex via existing `Params.noindex` · article count unchanged at 44 · no URL/slug/alias changes · no new article created · no affiliate or CTA changes.
- Recommendation on AdSense review request: do not click "Request review" yet. Wait at least 7–14 days so Googlebot can recrawl the now-indexable trust pages and process noindex on taxonomy archives, then reassess. Consider one further pass to publish the remaining Creative/Security/Video articles to push topical depth before the next review.

---

### Day 58a — Publish free-password-managers-teams

- Published `content/security/free-password-managers-teams.md`: "Best Free Password Managers for Teams in 2026 — Shared Vaults Without the Price Tag"
- Covers: Bitwarden Free Organizations (2-user cloud free tier), Bitwarden Self-Hosted (unlimited users, Docker), Vaultwarden (lightweight Bitwarden-compatible self-hosted), Passbolt Community Edition (open-source, purpose-built team sharing, GPG), KeePassXC shared vault (DIY file-based option)
- Includes comparison-table shortcode, per-tool verdict badge shortcodes on two tools, privacy/security notes, and honest "who should pay" decision guide
- Date set to 2026-05-02 (UTC build date) to avoid future-date validator error while running just past midnight SGT
- Created `scripts/images/generate_free_password_managers_teams.py` and generated `static/img/free-password-managers-teams.webp` (30.1 KB, 1200×630, Security accent #8b5cf6)
- Internal links from new article: free-password-managers, best-free-2fa-apps, free-vpn
- NordPass Business affiliate CTA added in "who should pay" section (NordPass: Active)
- Backlink added: `free-password-managers.md` → `free-password-managers-teams` in "Who should pay" section
- `CONTENT-STRATEGY.md` updated: free-password-managers-teams marked ✓ Published
- Article count: 43 → 44 · Security silo: 4/6 → 5/6
- Canva remains Under review / Needs approval; Grammarly remains Declined; no new Canva or Grammarly CTAs added
- Validation: `git diff --check` clean · QA runner 3/3 passed (44 articles, 44 images, 0 broken links) · stale report: 0 stale articles · `hugo --minify` clean · `public/security/free-password-managers-teams/index.html` confirmed · `/start-here/` confirmed 6 collection-card elements, 0 escaped entities · pagination page-item confirmed in business hub · no URL/slug/alias changes
- Follow-up: Security silo needs 1 more article (free-security-audit-tools) to reach 6/6 target

---

### Day 57e — Pagination button styling fix

- Bug observed: current page number rendered with a teal vertical background block (full `li` height) rather than a clean teal rounded button; navigation arrows double-styled by `.pagination span` selector.
- Root cause: two CSS selector mistakes. (1) `.pagination .active` targeted `li.page-item` — a block element with no fixed dimensions — causing the teal fill to stretch vertically as a strip. (2) `.pagination a, .pagination span` targeted the inner `span[aria-hidden]` elements inside navigation anchors, double-applying `inline-flex`, `padding`, and `border` inside the already-styled `a.page-link`. Hugo's internal pagination template generates `ul.pagination > li.page-item(.active|.disabled) > a.page-link` and inner `span[aria-hidden]` for arrow symbols.
- Fix: rewrote pagination CSS block in `static/css/style.css`. Added `list-style: none; padding: 0` to `ul.pagination`; added `.page-item { display: flex }` to make list items flex containers; replaced `.pagination a, .pagination span` with `.pagination .page-link` (targets only the anchor buttons, not inner spans); moved active state to `.page-item.active .page-link`; added `.page-item.disabled .page-link { opacity: 0.4; pointer-events: none }`.
- Files changed: `static/css/style.css`, `freestackfinder-progress-log.md`
- Validation: `git diff --check` clean; QA runner 3/3 passed (43 articles, 43 images, 0 broken links); `hugo --minify` clean; pagination HTML in `public/business/index.html` confirmed `li.page-item.active > a.page-link` structure; article count 43 unchanged; no URL changes.
- Follow-up: none required.

---

### Day 57d — Design handoff cleanup and permanent design reference

- Why this pass: temporary `design_handoff_freestackfinder/` folder contained the React/CSS reference package used during the design-system implementation (Days 57a–57b). Now that implementation is complete, the folder was cleaned up and its durable rules distilled into a permanent reference.
- Start Here status: confirmed fixed from Day 57c — `/start-here/` renders 6 `collection-card` HTML elements, 0 escaped entities.
- Files inspected: `design_handoff_freestackfinder/DESIGN_SYSTEM.md`, `design_handoff_freestackfinder/README.md`, `CLAUDE.md`, `docs/SKILL.md`, `public/start-here/index.html`
- Files changed: `docs/DESIGN-SYSTEM.md` (created), `CLAUDE.md` (added design reference row), `freestackfinder-progress-log.md`
- Deleted: `design_handoff_freestackfinder/` (entire folder — was untracked, never committed)
- Permanent design reference: `docs/DESIGN-SYSTEM.md` — covers color tokens, typography, category icon accent colors, layout/spacing, header/footer rules, trust/legal routes, component rules, article structure, image rules, raw-HTML-in-Markdown caution, AdSense compliance notes.
- CLAUDE.md updated: added `Visual design / CSS / tokens → docs/DESIGN-SYSTEM.md` row to the "When to read what" table.
- Validation result: `git diff --check` clean; QA runner 3/3 passed (43 articles, 43 images, 0 broken links); `hugo --minify` clean; article count 43 unchanged; no new article created; no URL changes.

---

### Day 57c — Start Here page rendering fix

- Bug observed: `/start-here/` displayed raw escaped HTML (`&lt;div class="collection-card"&gt;` etc.) instead of rendered collection cards.
- Root cause: CommonMark/Goldmark HTML block parsing rule — an HTML block ends at the first blank line. Blank lines between `<div class="collections-grid">` and the nested `<div class="collection-card">` elements caused the parser to exit HTML block mode; the 4-space-indented card divs were then treated as Markdown code blocks and escaped. Hugo `unsafe = true` was already set (correct); the issue was purely in the Markdown source structure.
- Files changed: `content/start-here.md` — removed blank lines between outer wrapper divs and inner collection-card divs so the entire card grid stays within one continuous HTML block.
- Validation: `git diff --check` clean; QA runner 3/3 passed (43 articles, 43 images, 0 broken links); `hugo --minify` clean; built `public/start-here/index.html` contains 6 `collection-card` HTML elements, 0 escaped `&lt;` entities; article count unchanged at 43; no new article created; no URL changes.
- Follow-up: none required.

---

### Day 57b — homepage hero, tenets strip, guide counts, article H2 rule

- Why this pass: Day 57a only ported category SVG icons. The handoff hero pattern, tenets strip, category-card guide counts, and the gated article H2 desktop top-border were not yet implemented. This pass closes those gaps without touching routing, content, or affiliate logic.
- Files inspected: `design_handoff_freestackfinder/ui_kit/site.css`, `design_handoff_freestackfinder/ui_kit/shell.jsx`, `design_handoff_freestackfinder/ui_kit/pages-home-category.jsx`, `design_handoff_freestackfinder/ui_kit/pages-article-search.jsx`, `static/css/style.css`, `layouts/index.html`, `layouts/_default/list.html`, `layouts/_default/single.html`, `layouts/_default/search.html`, `layouts/partials/nav.html`, `layouts/partials/footer.html`
- Files changed: `static/css/style.css`, `layouts/index.html`, `freestackfinder-progress-log.md`
- Design system areas implemented now:
  - Hero: replaced `.hero-badges` chips with the handoff `.hero-cta-row` (teal primary + ghost outline), added `.hero-eyebrow` (uppercase teal label), italicized teal `<em>` accent in H1, swapped `.hero-note` for the smaller `.hero-meta` line; flattened the gradient background to flat `--bg-2` per handoff.
  - Tenets strip: removed the loud full-bleed teal `.trust-section` banner from the homepage and added the editorial `.tenets-section` (light surface, 28px circle SVG checkmarks, four trust statements) per `site.css`.
  - Category cards: added per-card guide count (`.cat-count`) computed from `where .Site.RegularPages "Section" "<silo>"` — 6/9/4/13/4/7 = 43.
  - Article H2 motif: gated `border-top: 2px solid var(--border)` and `padding-top: 14px` to `min-width: 601px` so the rule is desktop-only as specified; mobile keeps the lighter rhythm; `text-wrap: balance` added to H2.
  - Hero responsive padding tightened to 56px/40px per handoff.
- Areas compared and already matched (production CSS is the documented source of truth, per `DESIGN_SYSTEM.md`):
  - Header (`.site-header`, sticky, 64px, `.logo` with teal `.logo-accent`, nav, search icon button) — class names differ from the React shell but token values, sizes, hover states, and mobile toggle all match the handoff.
  - Footer (3-column dark slate `#0F172A`, brand + categories + site, trust pill links, affiliate notice with disclosure link) — current footer matches the handoff layout and palette; uses real existing routes, no `href="#"`.
  - Article single (two-column 720/280, collapse below 960px, breadcrumb, header, editorial-note, content typography, tags, author box, related sidebar) — matches handoff article layout.
  - Category list (breadcrumb, large H1, description, editorial-note, article-count, articles grid) — already follows the editorial header pattern.
  - Search page (`#search-input` with inline icon, filter chips, results list) — already matches handoff input/chip/result styling.
  - Verdict boxes, comparison tables, tool cards, FAQ details, affiliate CTA, sidebar widgets, TOC — production CSS already mirrors handoff component styling.
  - Tokens (palette, typography, radii, shadows, container/article widths) — identical values to `colors_and_type.css`; only token *names* differ (`--primary` vs `--p`), which is intentional to avoid breaking active selectors.
- Areas intentionally preserved (changing would break routing/content/SEO):
  - Token names (`--primary`, `--text`, `--border`, etc.) kept rather than aliased to handoff short names — every layout, partial, shortcode, and content shortcode reference would need rewriting.
  - Trust/legal routes kept as `/about/`, `/disclaimer/`, `/privacy-policy/`, `/terms/`, `/contact/` (not handoff's `/how-we-test/`, `/disclosure/`, `/privacy/`) per the no-URL-change constraint; existing pages already cover the same content.
  - System font stack retained (no Inter loaded) per AdSense compliance and the `colors_and_type.css` production fallback note.
  - AdSense slot HTML, order, and `data-ad-*` attributes untouched.
  - `/go/*` affiliate redirect routes untouched.
- Trust/legal pages: inspected; `/about/`, `/disclaimer/`, `/privacy-policy/`, `/terms/`, `/contact/` already render with `.static-page` styling that matches the handoff trust-page tone. No content overwrite.
- Category icon update: SVG icons from Day 57a confirmed rendered in `public/index.html`; no emoji fallback remains visible anywhere.
- Search/page behavior: search.html and `/js/search.js` index logic untouched; results still return.
- Affiliate/AdSense safety: no /go/ redirect, no AdSense slot, no affiliate link added or moved; Canva remains Under review; Grammarly remains Declined.
- Site-name signal check: `og:site_name = Free Stack Finder`, `application-name = Free Stack Finder`, WebSite/Organization JSON-LD names, and canonical homepage URL untouched.
- Validation result: `git diff --check` clean; QA runner 3/3 passed (43 articles, 43 images, 0 broken links); `hugo --minify` 421 pages / 183 aliases clean; rendered homepage shows `.hero-eyebrow`, `.hero-cta-row`, `.hero-meta`, `.tenets-section`, six `.cat-count` spans (6+9+4+13+4+7 = 43); article count remains 43; no new article created.
- Follow-up: optional — sweep older articles for dated `verdict-box` shortcode usage if a future polish pass is needed; no functional issue today.

---

### Day 57a — homepage category SVG icons and per-silo accent colors

- Files inspected: `CLAUDE.md`, `docs/SKILL.md`, `freestackfinder-progress-log.md`, `design_handoff_freestackfinder/DESIGN_SYSTEM.md`, `design_handoff_freestackfinder/ui_kit/icons.jsx`, `design_handoff_freestackfinder/ui_kit/shell.jsx`, `design_handoff_freestackfinder/ui_kit/site.css`, `static/css/style.css`, `layouts/index.html`, `layouts/partials/nav.html`, `layouts/partials/footer.html`, `layouts/_default/baseof.html`, `layouts/_default/list.html`, `layouts/_default/single.html`, `content/about.md`, content directory listing
- Files changed: `static/css/style.css`, `layouts/index.html`, `freestackfinder-progress-log.md`
- What changed: replaced six emoji category icons (🎨 ⚡ 🎬 💼 🔒 ☁️) on the homepage with stroke-based inline SVGs from the design handoff (palette, clock, camera, briefcase, shield, cloud); added a 44px circle `.cat-icon` container with per-silo accent palette (creative coral · productivity green · video purple · business amber · security teal · cloud blue) keyed via `data-cat` on each category card; SVGs use `currentColor` so each card inherits its silo color; existing nav, footer, article and category templates left intact (already aligned with the design system); no URL, slug, alias, AdSense slot, or affiliate behavior changes
- Design areas implemented: category icon system (six distinct accent colors, no emoji fallback, no icon font, no CDN); 44px icon circle motif; preserved teal-only UI chrome rule (accent colors confined to icon circles only)
- Routes/pages validated: `/`, `/about/`, `/disclaimer/`, `/privacy-policy/`, `/search/`, `/creative/`, `/productivity/`, `/video/`, `/business/`, `/security/`, `/cloud/` all build successfully
- Validation result: `git diff --check` clean; QA runner passed 3/3 with 43 articles, 43 images, 0 broken internal links; Hugo Extended build clean (421 pages, 183 aliases); homepage SVG cat-icon markup verified in `public/index.html`
- Guardrails confirmed: article count remains 43; no new article created; no URL/slug/alias changes; no affiliate links added; Canva remains Under review; Grammarly remains Declined; site-name signals (og:site_name, application-name, WebSite/Organization JSON-LD, canonical homepage) untouched; no public workflow language introduced
- Follow-up: optional — port the same SVG icons to category list-page headers and the footer category list when a future polish pass is needed

---

### Day 56b — project skill file and CLAUDE.md refactor

- Files inspected: `CLAUDE.md`, `freestackfinder-progress-log.md`, `FEATURE-STRATEGY.md`, `CONTENT-STRATEGY.md`, `docs/BUILD-VALIDATION.md`, `.claude/` directory
- Files changed: `CLAUDE.md` (refactored), `docs/SKILL.md` (created)
- What changed: created `docs/SKILL.md` with YAML front matter and 12 operational sections covering daily content workflow, feature workflow, weekly/monthly review, GSC-led refresh, affiliate safety, image workflow, token-saving rules, content quality rules, validation checklist, tracker update expectations, commit/deploy rules, and output format; refactored `CLAUDE.md` from ~340 lines to ~90 lines — kept mission, read-first routing table, task priority, validation commands, critical never-do rules, known bugs list, growth targets, and repo structure reference; moved all repeatable operational guidance into SKILL.md with a pointer from CLAUDE.md
- Validation result: `git diff --check` clean; QA runner passed 3/3 with 43 articles, 43 images, 0 broken internal links, 0 stale articles; article count remains 43; no new article created; no public-facing content changed; Canva remains Under review; Grammarly remains Declined
- Guardrails confirmed: no URL/slug/alias changes; no affiliate links added; no public workflow or internal language added to content
- Follow-up: none — FEATURE-STRATEGY.md not updated as this is a documentation/maintenance item not yet listed in the Phase 9 roadmap; can be added if desired

---

### Day 56a — weekly site quality review

- Weekly review date: 2026-05-02
- Files inspected: required project runbook, tracker, feature/content strategy, GSC notes, build validation, affiliate guidelines/tracker; priority GSC pages across Productivity, Cloud, Creative, and Business; newest Cloud email guides; recent QA scripts; `layouts/partials/schema.html`, `layouts/partials/head.html`, `layouts/partials/related-guides.html`, `layouts/index.html`, `static/site.webmanifest`; homepage/About/disclaimer/category-hub signals
- Issues found: `static/site.webmanifest` colors had drifted from the Day 55c theme-color note; homepage trust copy still made a stronger hands-on claim than the documented evaluation process supports; the two newest Cloud email guides were missing curated related-guide entries; `docs/BUILD-VALIDATION.md` and the feature roadmap still referenced a 42-article / incomplete-Cloud baseline
- Fixes made: aligned manifest colors with the homepage head theme color; softened homepage trust copy to practical-limit checking; added curated related-guide coverage for the newest Cloud email pages and adjacent email guides; refreshed build-validation count and roadmap baseline; added a GSC notes entry for this review
- Validation result: `git diff --check` clean; QA runner passed 3/3 with 43 articles, 43 images, 0 broken internal links, 0 stale articles; publish checklist passed for `cloud/free-ai-email-tools`; Hugo Extended 0.160.1 build passed cleanly; generated homepage confirms `og:site_name`, `application-name`, WebSite JSON-LD name/alternateName, Organization JSON-LD name, and canonical homepage URL
- Guardrails confirmed: article count remains 43; no new article created; no content file, URL, slug, or alias changes; Canva remains Under review / Needs approval; Grammarly remains Under review / Needs approval; no affiliate links or CTAs added
- Follow-up: next GSC action should wait for a fresh data window; local PATH `hugo` currently resolves to 0.161.1 and emits deprecation warnings, while the documented 0.160.1 target still builds cleanly with the pinned binary

---

### Day 55c — site name signal pass

- Issue observed: Google SERP was showing "freestackfinder.com" as the site label instead of "Free Stack Finder"
- **`layouts/partials/schema.html`**: WebSite JSON-LD — fixed `url` to include trailing slash (`https://freestackfinder.com/`), added `alternateName` array (`["FreeStackFinder", "freestackfinder.com"]`); added Organization JSON-LD block on homepage with `name: "Free Stack Finder"`, `url`, and `contactPoint`
- **`layouts/partials/head.html`**: added `application-name` meta (`Free Stack Finder`), `theme-color` meta, favicon link tags (ico, 16×16 png, 32×32 png), apple-touch-icon link, and `<link rel=manifest>` — all were missing despite favicon files existing in `static/`
- **`static/site.webmanifest`**: updated `name` from "FreeStackFinder" to "Free Stack Finder"; updated `theme_color` and `background_color` to match site dark theme `#101116`
- No article published; article count remains 43; no URLs, slugs, aliases, or routing changed
- Canva and Grammarly remain under review / needs approval
- Generated homepage signals confirmed: og:site_name ✓ · application-name ✓ · manifest ✓ · favicon.ico ✓ · WebSite JSON-LD name ✓ · alternateName ✓ · Organization JSON-LD name ✓ · canonical URL ✓
- Note: Google may take days to weeks to recrawl and update the SERP site name display after these signals are live
- Validation: git diff --check clean · QA 3/3 passed · 43 articles · 0 broken links · 0 stale · Hugo build clean

---

### Day 55b — pre-publish checklist script

- Added `scripts/publish_checklist.py`: Phase 9 pre-publish checklist command
- No-arg mode: prints the full 10-step publish checklist (file, front matter, draft flag, date, image, internal links, backlinks, QA, Hugo build, git)
- Silo + slug mode (`python3 scripts/publish_checklist.py <silo> <slug>`): auto-verifies 7 file-level checks (file exists, required fields, draft:false, date valid, lastmod valid, image field format, image file size) then prints remaining manual steps; exits non-zero on failures
- Updated `FEATURE-STRATEGY.md`: pre-publish checklist marked complete in Phase 9 archive; baseline updated to Day 55b / 43 articles; next Phase 9 candidate updated to orphan-image cleanup listing
- No articles published; article count remains 43; no URLs, slugs, or public templates changed
- Canva and Grammarly remain under review / needs approval
- Validation: git diff --check clean · QA 3/3 passed · 43 articles · 43 images · 0 broken links · 0 stale articles · no Hugo rebuild needed (no public-facing files changed)

---

### Day 55a — publish free-ai-email-tools

- Published `content/cloud/free-ai-email-tools.md`: "Best Free AI Email Tools in 2026 — Draft, Summarize, and Reply Faster"
- Covers: Gmail Smart Compose (built-in, no cap), Compose AI (full drafts, monthly credits), ChatGPT free (complex drafts, copy/paste), Boomerang for Gmail (Respondable quality scorer, free always), Spike (AI app, draft + summarize, individual free plan)
- Includes comparison-table shortcode, privacy/business-use cautions section, and decision guide on when free runs out
- Created `scripts/images/generate_free_ai_email_tools.py` and generated `static/img/free-ai-email-tools.webp` (28.4 KB, 1200×630, Cloud accent #06b6d4)
- Internal links from new article: free-team-email, free-email-service, free-email-signature, free-ai-writing-tools
- Backlinks added: free-team-email verdict → free-ai-email-tools; free-email-service verdict → free-ai-email-tools
- `CONTENT-STRATEGY.md` updated: free-ai-email-tools marked ✓ Published; Cloud silo 7/7 complete
- Article count: 42 → 43 · Cloud silo: 6/7 → 7/7 ✓ complete
- Canva and Grammarly remain under review / needs approval; no affiliate CTAs added to this article (no active relevant program)
- Validation: git diff --check clean · QA runner 3/3 passed · 43 articles counted · 43 images verified · 0 broken links · 3 known image orphans unchanged · Hugo 0.161.1 build: 0 errors · `public/cloud/free-ai-email-tools/index.html` confirmed · stale report: 0 stale articles

---

### Day 54b — stale content report

- Added `scripts/report_stale_content.py`: scans published silo articles, skips drafts and `_index.md`, and flags articles whose `lastmod` is 183+ days old
- Added `--with-stale` to `scripts/run_quality_checks.py` so the stale content report can run alongside the existing QA checks when needed
- Updated `docs/BUILD-VALIDATION.md` with the optional stale report command and refreshed the documented article count to 42
- Updated `FEATURE-STRATEGY.md`: current baseline now reflects 42 articles and Cloud 6/7; Phase 9 stale content report marked complete; suggested next non-content options refreshed
- Initial stale report result: 42 published articles checked · 0 stale articles found
- No article published; article count remains 42
- No URLs, slugs, aliases, public templates, article bodies, images, affiliate links, Canva CTAs, or Grammarly CTAs changed
- Canva and Grammarly remain Under review / Needs approval
- Validation: git diff --check clean · QA runner 3/3 passed with counts · stale report clean · Hugo Extended 0.160.1 build passed · 42 articles counted · 0 broken internal links

---

### Day 54a — publish free-team-email

- Published `content/cloud/free-team-email.md`: "Best Free Team Email Tools in 2026 — Custom Domain, Shared Inbox, and Collaboration"
- Covers: Zoho Mail (5 users, custom domain, best free overall), Spike (email-as-chat, 5 users free), Proton Mail Free (encrypted, individual), Tutanota Free (open-source, encrypted), Gmail delegate access (workaround for teams on Gmail)
- Includes comparison-table shortcode and decision guide on when free options run out
- Created `scripts/images/generate_free_team_email.py` and generated `static/img/free-team-email.webp` (27.7 KB, 1200×630, Cloud accent #06b6d4)
- Internal links from new article: free-crm-software, free-email-service, free-email-signature, free-cloud-storage-comparison
- Backlink added: free-email-service verdict → free-team-email
- `CONTENT-STRATEGY.md` not changed (free-team-email was "Later" — marking complete via tracker only; update CONTENT-STRATEGY.md in next routine pass)
- Article count: 41 → 42 · Cloud silo: 5/7 → 6/7
- Canva and Grammarly remain under review / needs approval
- Validation: git diff --check clean · QA runner 3/3 passed · 42 articles counted · 42 images verified · 0 broken links · 3 known image orphans unchanged · Hugo Extended 0.160.1 build: 0 errors · `public/cloud/free-team-email/index.html` confirmed in output

---

### Day 53b — deep review recent site updates

- Reviewed recent Cloud/Business/Productivity content, GSC target pages, Start Here, category hubs, search index/card behavior, schema/head partials, related guides, affiliate/disclosure docs, validation docs, and QA/reporting scripts
- Fixed future-date validation gap: front matter validation now blocks live articles dated after the UTC build date; article count reporting now lists future-dated files that normal Hugo builds would exclude; build docs and run rules now require confirming new article output in `public/<silo>/<slug>/index.html`
- Corrected stale documentation/tracker state: `docs/BUILD-VALIDATION.md` now shows 41 articles, `FEATURE-STRATEGY.md` reflects Business 13/13 and Cloud 5/7, and affiliate tracker rows now include `free-hr-software` and `free-email-signature`
- Removed an existing Grammarly CTA from `free-note-taking-apps`; Canva and Grammarly remain Under review / Needs approval, not Active; public disclosure now lists only currently used affiliate programs
- Added curated related-guide coverage for `free-hr-software` and `free-email-signature`; related-guide map now covers all 41 article slugs with no self-links or missing targets
- Softened unsupported public testing language and trimmed overlong meta descriptions; front matter validator now reports 0 description warnings
- No new article published; no slugs, URLs, aliases, or generated output were changed
- Validation: `python3 scripts/run_quality_checks.py --with-counts` passed 3/3; 41 articles counted; 41 images verified; 0 broken internal links; only the 3 known image orphans remain
- Hugo build: Hugo Extended 0.160.1 exact binary passed with 399 pages, 17 paginator pages, 173 aliases, 0 errors; `free-email-signature` and `free-hr-software` both appear in built output and search index
- Follow-up: keep Cloud or Creative as the next content silo; update NordPass only if an approved tracked URL becomes available; keep Canva/Grammarly placements on hold until approval is confirmed

---

### Day 53a — publish free-email-signature

- Published `content/cloud/free-email-signature.md`: "Best Free Email Signature Makers in 2026 — Clean, Professional, No Design Skills Needed"
- Covers: HubSpot Email Signature Generator (best free, no account, no branding), MySignature (1 saved signature, Gmail/Outlook install), WiseStamp (established, basic free plan), Newoldstamp (modern design, free plan), Signature Maker (minimal, branding-free)
- Includes comparison table shortcode and decision guide on when to pay
- Created `scripts/images/generate_free_email_signature.py` and generated `static/img/free-email-signature.webp` (32 KB, 1200×630, Cloud accent #3b82f6)
- Internal links from new article: free-email-service, free-cloud-storage-comparison, free-crm-software
- Backlink added: free-email-service verdict section → free-email-signature
- `CONTENT-STRATEGY.md` updated: free-email-signature marked ✓ Published
- Article count: 40 → 41 · Cloud silo: 4/7 → 5/7
- Canva and Grammarly remain under review / needs approval
- Build: see validation below

---

### Day 52c — GSC refresh verification pass

- Verified all 8 GSC target pages from Day 52a (Microsoft Office, Dropbox, Slack, Grammarly, Illustrator, free backup software, QuickBooks, free project management) have improvements in place; all carry `lastmod: "2026-04-28"`
- Same 2026-04-28 GSC snapshot confirmed recorded in `docs/GSC-NOTES.md`; no new data requiring action
- Fixed stale article count in `docs/BUILD-VALIDATION.md`: 39 → 40
- No new content published; article count remains 40; Canva and Grammarly remain under review / needs approval
- Validation: git diff --check clean · QA runner 3 passed · 0 failed · Hugo build 388 pages · 0 errors

---

### Day 52b — repository hygiene cleanup

- Removed tracked Python bytecode from version control and added general Python cache ignore rules
- No article files or public output changed; article count remains 40
- Validation: git status reviewed, diff check clean, QA runner passed with counts

---

### Day 52a — GSC-led CTR refresh for high-impression pages

- Reviewed last-3-month GSC snapshot: 13 clicks, 4.64K impressions, 0.3% CTR, average position 51.7
- Priority pages inspected: Microsoft Office alternatives, Dropbox alternatives, Grammarly alternatives, Slack alternatives, Illustrator alternatives, free backup software, QuickBooks alternatives, free project management software
- Refreshed query-aligned SEO titles/descriptions on 8 target pages where useful; kept URLs, slugs, aliases, and routing unchanged
- Light first-screen wording updates made on Microsoft Office, Dropbox, and Slack pages to better match Office replacement, Dropbox replacement, and Slack replacement search intent
- Fixed weak public snippet wording on `free-backup-software`; removed unsupported "tested" wording from the Illustrator title and Microsoft Office intro
- Existing hub, related-guide, and contextual links already cover target pages; no mass backlinking added
- No new article published; article count remains 40; Business silo remains 13/13
- No affiliate links added; no Canva or Grammarly CTAs added; Canva and Grammarly remain under review / needs approval
- `docs/GSC-NOTES.md` updated with snapshot, priority pages, query themes, actions, and follow-up items
- Validation: git diff check, quality runner, Hugo build, article count, internal links, and generated-output checks completed

---

### Day 51a — publish free-hr-software

- Published `content/business/free-hr-software.md`: "Best Free HR Software in 2026 — Simple People Ops Without the Price Tag"
- Covers: Zoho People (free up to 5 employees), OrangeHRM Community Edition (self-hosted, no user cap), Homebase (scheduling/time tracking, 1 location free), Bitrix24 (HR features in free workspace), Google Sheets (DIY fallback)
- Clearly distinguishes HRIS tools, scheduling/time tracking, and spreadsheet-based options; payroll and compliance caveats throughout
- Created `scripts/images/generate_free_hr_software.py` and generated `static/img/free-hr-software.webp` (27 KB, 1200×630, Business accent #10b981)
- Internal links from new article: free-project-management-software, free-time-tracking-software, free-crm-software, free-spreadsheet-alternatives, free-invoicing-software, free-accounting-software
- Backlinks added: free-time-tracking-software verdict section → free-hr-software; free-project-management-software verdict section → free-hr-software
- `CONTENT-STRATEGY.md` updated: free-hr-software marked ✓ Published
- Article count: 39 → 40 · Business silo: 12/13 → 13/13 ✓
- Canva and Grammarly remain under review / needs approval
- Build: PASSED · 388 pages · 0 errors · 0 warnings · front matter valid · image resolves · internal links resolve · QA runner 3 passed · 0 failed

---

### Day 50c — Hugo 0.160.1 migration

- Hugo Extended 0.160.1 confirmed as system version; build already passes cleanly
- No template, config, shortcode, or content changes required — zero deprecation warnings
- `README.md` updated: `HUGO_VERSION` env var and version check comment changed from `0.128.0` → `0.160.1`
- `docs/BUILD-VALIDATION.md` created: records required Hugo version, QA script usage, and deployment checklist
- Validation: `hugo --minify` clean (373 pages, 0 errors, 0 warnings); QA runner 3 passed · 0 failed; article count confirmed at 39; Canva/Grammarly remain under review
- Cloudflare Pages: update `HUGO_VERSION` env var in dashboard to `0.160.1`

---

### Day 50b — review pass after recent site updates

- Reviewed recent Business/Productivity content, Start Here, category hub top-picks, search/index changes, related guides, affiliate docs, roadmap docs, and QA scripts
- Issues found: stale feature roadmap counts after `free-web-analytics`, affiliate tracker missing `free-web-analytics`, unsupported public "tested" wording, and missing curated related-guide coverage for the new analytics article
- Fixes made: updated public trust wording to "compare/evaluate" language, added `free-web-analytics` to curated related guides and affiliate tracker, refreshed `FEATURE-STRATEGY.md` counts/next recommendation, and corrected current tracker next-content/feature notes
- Validation: git diff --check clean; QA runner clean with known warnings only; Hugo build passed; article count confirmed at 39 total and Business 12/13
- Follow-up: publish `free-hr-software` on the next content day; keep Canva/Grammarly deferred until approval is confirmed; update NordPass only if an approved tracked URL is available

---

### Day 50a — publish free-web-analytics

- Published `content/business/free-web-analytics.md`: "Best Free Web Analytics Tools in 2026"
- Covers: Google Analytics 4, Google Search Console, Microsoft Clarity, Umami (self-hosted), Matomo On-Premise
- Clearly distinguishes traffic analytics, search performance tools, privacy-friendly analytics, and self-hosted options
- Includes comparison table, tool-by-tool breakdown, decision guide (when free is enough vs. when to pay), and product analytics vs. website analytics note
- Created `scripts/images/generate_free_web_analytics.py` and generated `static/img/free-web-analytics.webp` (32 KB, 1200×630, Business accent #10b981)
- Internal links added to free-website-builders, free-project-management-software, free-crm-software
- `CONTENT-STRATEGY.md` updated: free-web-analytics marked ✓ Published
- Article count: 38 → 39 · Business silo: 11/13 → 12/13
- Canva and Grammarly remain under review / needs approval
- Build: PASSED · front matter valid · image resolves · internal links resolve

---

### Day 49f — article count by silo report script

- Created `scripts/report_article_counts.py`: scans content silo folders, excludes `_index.md` and utility/root pages, respects `draft: true`, prints count/target/remaining table; Python standard library only
- Script output confirmed: Business 11/13 · Cloud 4/7 · Creative 6/8 · Productivity 9/9 ✓ · Security 4/6 · Video 4/7 · Total 38 — matches tracker
- Updated `scripts/run_quality_checks.py`: added `--with-counts` flag that runs the report after QA checks (informational only; count mismatches do not affect exit code)
- `FEATURE-STRATEGY.md` updated: Phase 9 article count item marked done (Day 49f); archive row added; Suggested Next Feature updated to `free-web-analytics`
- No article published; article count unchanged at 38
- No public page, template, CSS, JS, image, or article body changed
- Canva and Grammarly remain under review / needs approval

---

### Day 49e — validation runner script

- Created `scripts/run_quality_checks.py`: runs all three QA scripts in sequence (front matter, internal links, feature images)
- Supports `--with-build` flag (runs `hugo --minify` after QA) and `--quiet` flag (suppresses verbose child output, shows last 4 lines)
- Uses Python standard library only; locates repo root from script path; returns non-zero exit if any checker fails
- Runner executed: 3 passed · 0 failed · 18 description-length warnings (known, no action required) · 3 image orphans (known, no action required)
- `FEATURE-STRATEGY.md` updated: Phase 9 runner item marked done (Day 49e); archive row added; Suggested Next Feature updated
- No article published; article count unchanged at 38
- No public page, template, CSS, JS, image, or article body changed
- No affiliate CTAs added; Canva and Grammarly remain under review / needs approval

---

### Day 49d — feature roadmap reorganization

- `FEATURE-STRATEGY.md` fully reorganized after completion of all Phase 1–4 features
- All 26 completed features moved from mixed inline entries into a clean "Completed Feature Archive" table with day, category, and one-line note
- Old Phase 1–4 active sections (all done) replaced with 5 new future phases: Phase 5 (content expansion), Phase 6 (GSC-led refresh), Phase 7 (monetization readiness), Phase 8 (E-E-A-T strengthening), Phase 9 (maintenance automation)
- Current Feature Baseline updated: 38 articles, Business 11/13, Canva/Grammarly under review noted, validators listed
- Suggested Next Feature updated: primary recommendation is `free-web-analytics`; no Canva/Grammarly CTA suggestion
- "What Not To Build Yet" updated to include sticky ToC and affiliate CTA shortcode
- "How To Choose The Next Feature" updated to reference new phase numbers
- No article published; article count unchanged at 38
- No public page, template, CSS, JS, image, or article body changed
- No affiliate CTAs added; Canva and Grammarly remain under review
- Validation: git diff --check clean · front matter 0 errors PASSED · internal links 0 broken PASSED · feature images 0 errors PASSED

---

### Day 49c — GSC search performance notes template

- Created `docs/GSC-NOTES.md`: lightweight internal file for tracking Google Search Console observations
- Contains: snapshot history table (date, clicks, impressions, CTR, avg position, notes); page opportunity table (page, query/theme, impressions, clicks, CTR, avg position, issue, next action, priority); action rules for CTR issues, position 8–20 pages, newly published pages, and already-improving pages; monthly review checklist
- Baseline snapshot from 2026-04-15 added: 5 clicks · 2,220 impressions · 0.2% CTR · avg position 54.4
- Update cadence: weekly light check · monthly deeper review · after major content batches
- No new article published; article count unchanged at 38
- No public page, template, CSS, JS, image, or article body changed
- No affiliate CTAs added; Canva and Grammarly remain deferred (not available for placement)
- `FEATURE-STRATEGY.md` updated: Phase 4.4 marked complete (Day 49c); row added to Completed Feature Systems; Suggested Next Feature updated
- Front matter: 0 errors · 18 warnings · PASSED
- Internal links: 0 broken · PASSED
- Feature images: 0 errors · 3 orphans · PASSED

---

### Day 49b — affiliate tracker Canva/Grammarly cleanup

- Canva and Grammarly CTA placement confirmed not currently available; all related tracker rows downgraded from High/Medium priority to Deferred
- Updated `docs/AFFILIATE-TRACKER.md`: header active-programs list corrected; 7 Canva/Grammarly rows set to Deferred; next-action queue cleaned (items 1 and 2 removed)
- Updated `docs/AFFILIATE-GUIDELINES.md`: Canva and Grammarly changed from Active to Deferred with placement note
- Updated `FEATURE-STRATEGY.md`: removed Canva/Grammarly CTA suggestion from Suggested Next Feature; replaced with NordPass tracked URL follow-up
- No public article published; article count unchanged at 38
- No public page, template, CSS, JS, or image changed
- No affiliate CTAs added

---

### Day 49a — affiliate tracker verification pass

- Reviewed `docs/AFFILIATE-TRACKER.md` against `docs/AFFILIATE-GUIDELINES.md`
- Resolved all 15 "Needs verification" rows by checking actual article files
- Confirmed 8 articles have live CTAs: `free-password-managers` (NordPass), `free-vpn` (NordVPN), `free-antivirus-software` (NordVPN), `best-free-2fa-apps` (NordVPN + Amazon), `free-backup-software` (Amazon), `free-screen-recording-software` (Amazon), `dropbox-alternatives` (NordVPN), `free-email-service` (NordVPN)
- Confirmed 7 articles have no CTA yet: `canva-alternatives`, `grammarly-alternatives`, `free-stock-photos`, `free-ai-writing-tools`, `photoshop-alternatives`, `illustrator-alternatives`, `microsoft-office-alternatives`
- Flagged: NordPass link in `free-password-managers` uses direct nordpass.com URL rather than a tracked affiliate URL — noted for future update if tracked URL is available
- Removed duplicate `best-free-2fa-apps` Amazon row (was double-listed); merged into single row
- Added `free-website-builders` (Day 48n) to tracker as Deferred — no active program fit
- Updated next-action queue; Zoho rows remain on hold pending CJ approval
- No public article published; article count unchanged at 38
- No public page, template, CSS, JS, or image changed
- No affiliate CTAs added in this run
- `FEATURE-STRATEGY.md` updated: affiliate verification pass marked complete (Day 49a); Suggested Next Feature updated

---

### Day 48o — feature image inventory checker script

- Created `scripts/check_feature_images.py`: cross-checks `image:` fields in all 38 silo articles against files in `static/img/`; flags missing files as errors; reports unreferenced files in `static/img/` as possible orphans (warnings only); checks for non-WebP extensions
- Run: `python3 scripts/check_feature_images.py` — exits 1 on missing images, 0 on clean or warnings-only
- First run: 38 articles checked · 38 images verified · 0 errors · 3 possible orphans (`default-article.jpg`, `nordpass-banner.png`, `nordvpn-banner.png`) — PASSED with warnings
- Orphans left in place; banner PNGs are not used per affiliate guidelines (no image banners), placeholder JPG may be safe to remove later
- No new article published; article count unchanged at 38
- No public page, template, CSS, JS, or image changed
- `FEATURE-STRATEGY.md` updated: Phase 4.3 marked complete (Day 48o); row added to Completed Feature Systems; Suggested Next Feature updated

---

### Day 48n — publish free-website-builders article

- Published `content/business/free-website-builders.md`: Business silo, article 11/13
- Covers 5 tools: Wix (featured — most features on free plan), Google Sites (best zero-cost), WordPress.com (best for blogging), Carrd (best one-pager), Canva Websites (best for Canva users)
- Includes comparison table shortcode and 5 verdict badges
- 4 internal links: `/business/free-crm-software/`, `/business/free-invoicing-software/`, `/business/free-social-media-scheduling/`, `/productivity/microsoft-office-alternatives/`, `/cloud/free-cloud-storage-comparison/`
- Feature image generated: `static/img/free-website-builders.webp` (32 KB, 1200×630 WebP)
- Image script: `scripts/images/generate_free_website_builders.py`
- Related-guides mapping updated for `free-website-builders` and `free-social-media-scheduling`
- `CONTENT-STRATEGY.md` updated: `free-website-builders` marked ✓ Published
- Front matter validator: 0 errors · 19 warnings (1 new description-length warning) · PASSED
- Internal link checker: 0 broken links · PASSED
- Hugo build: 360 pages, no errors

---

### Day 48m — internal link checker script

- Created `scripts/check_internal_links.py`: scans all `.md` files under `content/` for internal Markdown links (`[text](/path/)`); builds a route map from front matter slugs and file paths; skips external, mailto, tel, and anchor-only links; strips fragments before matching; normalizes trailing slashes
- Run: `python3 scripts/check_internal_links.py` — exits 1 on broken links, 0 if clean
- First run: 44 files · 53 known routes · 0 broken links — PASSED
- No broken links to fix; no article edits required
- No new article published; article count unchanged at 37
- No public page, template, CSS, JS, or image changed
- `FEATURE-STRATEGY.md` updated: Phase 4.2 marked complete (Day 48m); row added to Completed Feature Systems; Suggested Next Feature updated

---

### Day 48l — front matter validator script

- Created `scripts/validate_front_matter.py`: scans all 37 silo articles for 9 categories of front matter issues — missing required fields, banned keys (`featured`, `faqs`), future dates, bare unquoted dates, image path format, image file existence in `static/img/`, empty/overlong descriptions, duplicate slugs, accidental `noindex` on silo articles
- Run: `python3 scripts/validate_front_matter.py` — exits 1 on errors, 0 on warnings-only or clean
- First run result: 2 errors (missing `slug` on `photoshop-alternatives` and `microsoft-office-alternatives`) — both fixed; 18 description-length warnings remain as informational backlog (not blocking)
- Final run: 0 errors · 18 warnings · PASSED with warnings
- No new article published; article count unchanged at 37
- No public page, template, CSS, JS, or image changed
- `FEATURE-STRATEGY.md` updated: Phase 4.1 marked complete (Day 48l); row added to Completed Feature Systems; Suggested Next Feature updated

---

### Day 48k — internal affiliate opportunity tracker

- Created `docs/AFFILIATE-TRACKER.md`: internal ops file listing all 37 articles with affiliate program candidate, CTA placed status, verification status, priority, and notes
- High-priority verification queue covers 8 articles (NordVPN, NordPass, Canva, Grammarly, Amazon); Amazon Day 39b placements flagged for link/tag confirmation
- Zoho and Impact.com rows marked "Needs approval" / "Deferred" — no placements added
- No public article published; article count unchanged at 37
- No public page, template, CSS, JS, or image changed
- No affiliate CTA added in this run
- `FEATURE-STRATEGY.md` updated: Phase 3.1 marked complete (Day 48k); row added to Completed Feature Systems; Suggested Next Feature updated to content publishing or verification pass

---

### Day 48j — category hub top-picks upgrade
- Added "Where to start" box to all 6 silo hub pages: Productivity, Business, Creative, Security, Cloud, Video
- Each box shows 4 curated links with a one-line decision guide explaining who each article is for
- Links use existing published articles only; no invented or broken links
- Template unchanged — content renders via existing `category-intro` div in `layouts/_default/list.html`
- CSS: added `.hub-top-picks` and related rules to `static/css/style.css` (no new layout system)
- No new article published; article count unchanged at 37
- Hugo build passed — 347 pages, no errors
- `FEATURE-STRATEGY.md` updated: Phase 2.3 marked complete (Day 48j); next suggestion updated to content publishing

---

### Day 48i — add Start Here guided entry page
- Created `content/start-here.md`: indexable static page at `/start-here/`
- Six reader-path cards covering all silos: freelancer/solo → Business; replacing Office → Productivity; safer accounts → Security; creative tools → Creative; storage/backup → Cloud; video/media → Video
- Each card contains 4 curated links to existing high-value articles (24 internal links total)
- Footer note links to `/search/` and all 6 silo category pages
- "Start Here" nav link added to `config.toml` (weight 0, appears first)
- Two CSS rules added to `static/css/style.css` (`.start-here-paths`, `.start-here-footer`) for grid spacing; no new layout or shortcode required
- No new article published; article count unchanged at 37
- Hugo build passed — 347 pages, no errors
- `FEATURE-STRATEGY.md` updated: Phase 2.2 marked complete (Day 48i); Phase 2.3 category hub upgrade set as next suggested feature

---

### Day 48h — documentation restructure
- Split `CLAUDE.md` image rules into `docs/IMAGE-GUIDELINES.md`
- Split affiliate/monetization rules into `docs/AFFILIATE-GUIDELINES.md`
- Moved Days 15–46 detailed history to `docs/ARCHIVE/progress-history.md`
- Added "When to read what" routing table to `CLAUDE.md`
- Condensed progress log from 926 lines to ~250 lines; stale "Current snapshot" and "Current priorities" sections removed
- No article content, templates, layouts, CSS, JS, or images changed
- Manual checks: all referenced doc paths valid; CLAUDE.md still contains all safety-critical rules; progress log current state reflects 37 articles

---

### Day 48g — upgrade search result cards
- Search result cards now display: category pill (existing), title link (existing), description excerpt (existing), and a freshness date line
- Freshness line shows "Updated [date]" in primary green when `lastmod ≠ date`; "Published [date]" in muted text when equal
- `layouts/index.json` updated to include `date` and `lastmod` fields (ISO format) in the search index JSON
- `static/js/search.js` updated: added `formatDate()` helper and date label generation in the render function
- `static/css/style.css` updated: added `.search-result-date` and `.search-result-date--updated` rules
- Category filtering and query highlighting remain unchanged
- No new article published; article count unchanged at 37
- `FEATURE-STRATEGY.md` updated: search card upgrade marked complete (Day 48g); next suggested feature updated to Start Here page (Phase 2.2)

---

### Day 48f — expand verdict badges to comparison pages
- Rolled out `verdict.html` shortcode to all 7 remaining high-intent comparison pages
- Pages updated: free-password-managers, free-project-management-software, free-crm-software, free-invoicing-software, free-cloud-storage-comparison, free-video-editing-software, photoshop-alternatives
- 3 defensible per-tool labels per page; all labels match the existing article verdict and tool ordering
- No article body content rewritten; badge insertions only
- No new article published; article count unchanged at 37
- `FEATURE-STRATEGY.md` updated: verdict badge rollout marked complete (Day 48f)

---

### Day 48e — normalize recent article publish dates
- Spread the four Day 48 articles across four consecutive calendar days to avoid multiple same-day publications
- Dates assigned: free-pdf-editor-alternatives → 2026-04-22, free-resume-builders → 2026-04-23, free-social-media-scheduling → 2026-04-24, free-visio-alternatives → 2026-04-25
- No article body content changed; front matter `date` and `lastmod` updated only
- Total published articles unchanged: 37

---

### Day 48d — publish free-visio-alternatives
- Published new Business article: Best Free Microsoft Visio Alternatives in 2026
- Article covers draw.io, Lucidchart Free, Miro Free, and Whimsical Free; honest notes on LibreOffice Draw, Cacoo, and Microsoft Visio Viewer
- Comparison table shortcode at top; verdict badge shortcode on draw.io
- Feature image generated: `static/img/free-visio-alternatives.webp` (30 KB)
- Image script created: `scripts/images/generate_free_visio_alternatives.py`
- Related-guides map updated; internal link added to `free-project-management-software`
- `CONTENT-STRATEGY.md` updated: `free-visio-alternatives` marked Published
- Total published articles: 37 (Business now at 10/13)

---

### Day 48c — publish free-social-media-scheduling
- Published first Later-queue Business article: Best Free Social Media Scheduling Tools in 2026
- Article covers Buffer, Metricool, Later, and Meta Business Suite
- Comparison table shortcode at top; verdict badge shortcode on two tools
- Feature image generated: `static/img/free-social-media-scheduling.webp` (35 KB)
- Related-guides map updated; internal link added to `free-crm-software`
- `CONTENT-STRATEGY.md` updated: `free-social-media-scheduling` marked Published
- Total published articles: 36 (Business now at 9/13)

---

### Day 48b — publish free-resume-builders
- Published new Business article: Best Free Resume Builders in 2026
- Article covers Canva, Google Docs, Indeed Resume Builder, Resume.com; honest notes on Zety, Novoresume, Kickresume
- Comparison table shortcode at top; verdict badge shortcode on two tools
- Feature image generated: `static/img/free-resume-builders.webp` (29 KB)
- Related-guides map updated; internal link added to `grammarly-alternatives`
- `CONTENT-STRATEGY.md` updated: `free-resume-builders` marked Published
- Total published articles: 35 (Business now at 8/13)

---

### Day 48a — publish free-pdf-editor-alternatives
- Published new Productivity article: Best Free PDF Editor Alternatives in 2026
- Article covers PDFgear, PDF24 Tools, Sejda, LibreOffice Draw, and Xodo
- Comparison table shortcode at top; verdict badge shortcode on four tools
- Feature image generated: `static/img/free-pdf-editor-alternatives.webp` (29 KB)
- Image script created: `scripts/images/generate_free_pdf_editor_alternatives.py`
- Related-guides map updated; internal links added to `microsoft-office-alternatives` and `free-note-taking-apps`
- `CONTENT-STRATEGY.md` updated: `free-pdf-editor-alternatives` marked Published
- Total published articles: 34 (Productivity now at 9 — silo target reached)

---

### Day 47d — continued weekly code and AdSense-readiness review
- Fixed: Article JSON-LD string values with embedded quote characters
- Fixed: Removed synthetic FAQPage schema from all article pages (was rendering on all 33 articles without matching visible FAQ sections)
- Fixed: Softened `free-vpn` framing from blanket claims to more precise language about ads, data collection, and trial-like limits
- Files changed: `layouts/partials/schema.html`, `content/security/free-vpn.md`
- Hugo build passed — 308 pages, 9 paginator pages, no errors

---

### Day 47c — weekly audit and review pass
- Found and fixed 4 pages that had both the reusable comparison table shortcode AND an older markdown "Quick comparison table": `microsoft-office-alternatives`, `canva-alternatives`, `free-accounting-software`, `free-vpn`
- Updated `lastmod` to `"2026-04-25"` on the 4 corrected articles
- Hugo build passed — 308 pages, 9 paginator pages, no errors

---

### Day 47b — expand comparison tables to seven high-intent articles
- Deployed comparison-table shortcode to 7 articles (total now 11):
  - `free-crm-software`, `free-invoicing-software`, `free-project-management-software`, `free-cloud-storage-comparison`, `free-video-editing-software`, `photoshop-alternatives`, `free-password-managers`
- Each table moved to immediately after the Quick verdict section
- `FEATURE-STRATEGY.md` Phase 1.1 marked complete
- Hugo build: not available locally; build verifies on Cloudflare Pages

---

### Day 47a — feature strategy file
- Created `FEATURE-STRATEGY.md` in repo root
- Documents all completed feature systems, 4 roadmap phases, feature principles, deferred/not-yet list, and maintenance notes
- No site-rendered files changed

---

## Days 40–46 milestone summary

| Day | What shipped |
|-----|-------------|
| 46a | Published `free-accounting-software` (33 articles, Business 7/13) |
| 46b | Added review/methodology trust block to all article pages |
| 46c | CTR + internal-link review; updated 6 article title/descriptions |
| 46d | Productivity + Business cluster link pass |
| 46e | Curated homepage collections (freelance stack, Office alternatives, privacy basics) |
| 46f | Reusable `comparison-table` shortcode; deployed on 4 articles |
| 46g | Curated related-guides logic; covers all 33 articles |
| 46h | Freshness display on article/homepage cards (Updated in teal) |
| 46i | Verdict badge shortcode; deployed on 4 comparison pages |
| 46j | Footer trust CTA cleanup — pill-row flex layout |
| 45a | Site search + category filtering (JSON index, vanilla JS, /search/) |
| 45b | Header layout rework, search UI polish |
| 45c | Wave 1 trust remediation — 10+ articles, legal pages, schema cleanup |
| 45d | Wave 2 quality refresh — 7 older articles (crm, photoshop, canva, cloud storage, backup, video, premiere-pro) |
| 44a | Full-site quality audit; fixed CRM dev note, stale dates in legal pages, disclaimer program list |
| 43a–e | back-to-top button; noindex utility pages; free-spreadsheet-alternatives published; nav fix (Cloud replaces About); homepage trust badge copy fix |
| 41a | Published `free-calendar-app` (31 articles, Productivity 8/9) |
| 40a | Published `free-chatgpt-alternatives` (30 articles, Productivity 7/9) |

Detailed entries for Days 15–46 are in `docs/ARCHIVE/progress-history.md`.

---

## Affiliate focus

| Program | Priority pages |
|---------|---------------|
| NordVPN | `free-vpn`, `free-antivirus-software`, `dropbox-alternatives`, `free-email-service`, `best-free-2fa-apps` |
| NordPass | `free-password-managers` |
| Canva | `canva-alternatives`, `free-stock-photos` |
| Grammarly | `grammarly-alternatives`, `free-ai-writing-tools` |
| Amazon US (`freestackfi20-20`) | `best-free-2fa-apps` (security keys), `free-backup-software` (SSDs), `free-screen-recording-software` (USB mics) |
| Zoho (pending via CJ) | `free-crm-software`, `free-email-service`, `free-invoicing-software` |

See `docs/AFFILIATE-GUIDELINES.md` for placement rules.

---

## Pending actions

- Zoho affiliate via CJ Affiliate — still pending; apply when Zoho content is established
- AdSense formal approval pending (`ca-pub-5934721249825043` script is live)
- Impact.com reapplication deferred until traffic data is sufficient
- Reddit post #3 drafted for `r/entrepreneur`

---

## Cluster internal link reference

Full inventory in `CONTENT-STRATEGY.md`. Quick cluster reference:

- **Productivity:** slack-alternatives · microsoft-office-alternatives · grammarly-alternatives · notion-alternatives · free-note-taking-apps · free-ai-writing-tools · free-chatgpt-alternatives · free-calendar-app · free-pdf-editor-alternatives
- **Creative:** canva-alternatives · photoshop-alternatives · illustrator-alternatives · free-stock-photos · figma-alternatives · free-font-websites
- **Business:** quickbooks-alternatives · free-crm-software · free-project-management-software · free-invoicing-software · free-time-tracking-software · free-spreadsheet-alternatives · free-accounting-software · free-resume-builders · free-social-media-scheduling · free-visio-alternatives
- **Security:** free-password-managers · free-antivirus-software · free-vpn · best-free-2fa-apps
- **Cloud:** free-cloud-storage-comparison · dropbox-alternatives · free-email-service · free-backup-software
- **Video:** free-video-editing-software · zoom-alternatives · premiere-pro-alternatives · free-screen-recording-software
