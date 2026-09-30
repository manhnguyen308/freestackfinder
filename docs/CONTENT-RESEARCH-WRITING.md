# Content research and writing

The research and drafting loop for FreeStackFinder articles: brief, research, outline, opening, section-by-section drafting with review, full draft review, then the publication gate. It sits between "pick the article" and "validate and commit" in `docs/SKILL.md` section 4.

This file adds process. It does not replace any of these, and when they disagree with anything here, they win:

- Article structure and front matter: `docs/SKILL.md` section 6 and `archetypes/default.md`
- Editorial standard, anti-fabrication, sitewide sameness, publication gate: `website-content-humanizer.md`
- Star ratings: `docs/RATINGS.md`
- Volatile facts and evergreen wording: `docs/FRESHNESS-CHECKS.md`
- First-hand evidence and screenshots: "Article screenshots" in `CLAUDE.md`
- Affiliate status: `docs/AFFILIATE-TRACKER.md`

## 1. When to use it

| Task | Stages to run |
|---|---|
| New article or net-new cluster | All of them |
| GSC-led refresh of a title, description, opening, or section | Brief, research for the claims touched, opening (section 6), review of the changed sections, gate |
| Freshness rotation that changes a price or limit | Research and the notes file, then review of the sentences that carry the figure |
| Screenshot or first-hand evidence integration | Brief, then research with the screenshots as the primary source, review, gate |

Skip it for layout, CSS, script, and typo work.

## 2. The loop

| Stage | Output | Where it lives |
|---|---|---|
| Brief | The deciding fact, reader question, silo neighbors, what must not change | Top of the research notes |
| Research | One row per claim, with source and date read | `docs/research/<slug>.md` |
| Outline | The six structure slots filled, plus research gaps | Research notes, below the claims table |
| Opening | Two or three candidate openings and descriptions, one kept | Working notes only; the kept version goes into the article |
| Draft | The article, one section at a time, reviewed after each | `content/<silo>/<slug>.md` |
| Full draft review | Findings list, fixed before the gate | Working notes |
| Gate and validation | Humanizer gate, QA scripts, build | Progress log entry |

Work one section at a time. Draft a section, review it (section 7), fix it, then move on. Reviewing only the finished article lets an early mistake, such as a figure the research did not confirm, spread into the table, the paid section, and the rating.

## 3. Write the brief first

Answer these from the repo before drafting. Ask the user one specific question only when the page's job or the evidence behind a claim is genuinely unclear, such as whether screenshots exist for a sentence that implies use. Otherwise proceed.

| Question | Where the answer comes from |
|---|---|
| What single fact drives the recommendation? | Research. It becomes the opening and usually the ranking logic. |
| Who is reading, and what did they search? | The slug's intent; for refreshes, the queries in `docs/GSC-NOTES.md` |
| What must they be able to decide after reading? | Which free plan fits their job, and when paying beats the workaround |
| What format and length? | Fixed by `docs/SKILL.md` section 6. Length follows the number of tools and limits, not a word target. |
| What voice? | Calm editorial prose. Read the two most recently updated articles in the same silo as the voice sample before writing. |
| What already exists? | Earlier progress-log entries for the slug, an existing research notes file, supplied screenshots |
| What sits next to it? | The descriptions and first paragraphs of every other article in the silo |
| What must not change? (refresh only) | Rankings, recommendations, links, slug, date, affiliate placements, and any first-hand wording already backed by evidence |
| Which tools have affiliate programs? | `docs/AFFILIATE-TRACKER.md`. Status never changes a ranking or a rating. |

## 4. Research

### Source order

1. The vendor's pricing or plan page. Where prices vary by country, read the US view (for example Canva's `?countryCode=us`) and note the currency.
2. The vendor's help center, support articles, release notes, or dated blog posts.
3. Screenshots supplied by the user in `static/img/screenshots/<slug>/`. These are the only basis for first-hand wording, and only for the tools they show.
4. Third-party references, such as Wikipedia or a named news report, for background facts only. Never for a current price or limit.

Do not cite other "best free" roundups, search-result snippets or summary boxes, affiliate landing pages, or cached copies. A figure seen only in one of those goes into research gaps until the vendor's own page confirms it.

### Verification rules

- Open the page and read the figure there. Record the wording of the limit, the region or currency, and the date read.
- When the vendor's own pages disagree, cite the narrower figure or state both. When the vendor disagrees with a third party, the vendor wins.
- Give every tool at least one limit or weakness as well as what the free plan includes. A tool with only strengths in the notes is not researched yet.
- If a source cannot be reached or is unclear, drop the exact figure and use the evergreen wording in `docs/FRESHNESS-CHECKS.md`. Never guess a number to fill the gap.
- Mark each claim Confirmed, Narrowed, Dropped, or Needs evidence. Only Confirmed and Narrowed claims go into the article.
- A month cited in the text, such as "September 2026 prices", sets the earliest allowed `lastmod` (bulk update rule, `docs/SKILL.md` section 6).

### Research notes file

Create `docs/research/<slug>.md` for the article being written or refreshed, and only for that article. The folder is internal and not built by Hugo, but the tracker rule still applies: no mention of assistants, prompts, or automation. Keep URLs clean, with no tracking parameters.

```markdown
# Research notes: <slug>

Brief
- Deciding fact:
- Reader's question:
- Silo neighbors read:
- Must not change (refresh only):

| Tool | Claim as it will read | Source | Read on | Status |
|---|---|---|---|---|
| Box | Free individual plan lists 10GB and a 250MB upload cap | https://www.box.com/pricing/individual | 2026-09-30 | Confirmed |

Outline
(section 5)

Research gaps
- [ ] ...
```

The freshness rotation rechecks each row and updates "Read on". Star ratings in `docs/RATINGS.md` should rest on limits that appear in this table.

## 5. Outline inside the fixed structure

Fill the six slots from `docs/SKILL.md` section 6 in order. Do not add, drop, or reorder slots.

```markdown
Opening: <deciding fact> then the picks
Why people look: <the limit readers hit first>
Tools, in ranked order:
  1. <Tool>: <what separates it on this page> | free plan | where it stops | who it suits | rating | sources confirmed?
  2. ...
Comparison table columns:
When to pay: <the point where paying costs less than the workaround>
Closing decision rule: <a rule or boundary the opening does not state>
Internal links: <2 to 5 targets, and the 1 or 2 older articles that will link back>
```

Check the outline before drafting:

- Line of thought: each slot depends on the one before. If the tool sections could be shuffled without changing the argument, the deciding fact is not doing its job.
- Ranking: the order follows from the deciding fact, and the outline says why the first pick beats the second.
- Evidence: every tool line has a Confirmed or Narrowed row in the claims table, or it goes to research gaps.
- Headings: write the real, page-specific headings here, in sentence case, not placeholders.
- Tool openers: decide now which angle each tool section opens with (its limit, file model, audience, or tradeoff) so no two open the same way and none opens with a definition by reflex.
- Links: each internal link sits in a sentence that makes a claim. The "For ..., see our" and "If you ..., see our" formulas are retired sitewide.

## 6. Opening, description, and title

Draft two or three candidate openings, each in a different permitted shape:

- The limit that sends people looking
- The split between tool types
- The change that made the old default wrong
- The number that decides it

Test each candidate:

- Is the first sentence a Confirmed fact from the notes?
- Does it change the reader's decision, not only catch their interest?
- Does it pass the portability test, so it fails if another category's noun is swapped in?
- Does it differ in opening word and shape from the openings of every other article in the silo?
- Is it free of the imperative verdict ("Choose X for..."), a page announcement, rhetorical questions, and anecdotes?

Keep the one that passes most cleanly and discard the rest. Run the same exercise for the description (150 to 160 characters, read beside the silo's other descriptions, then `validate_front_matter.py`). On a refresh, change a live title only when the task calls for it, such as a GSC-led refresh. Titles are sentence case, with a colon only when the second phrase adds information.

## 7. Section review, after each section

Review each section as soon as it is drafted, in Detect mode from the humanizer: name the pattern, quote the line, give the fix in a few words. Then fix it before moving on.

| Check | What to look for |
|---|---|
| Evidence | Every number, limit, and price matches a Confirmed or Narrowed row. Vendor claims use "lists", "says", or "states" and link the source on the claim itself, not on "here". |
| Clarity | Tangled clauses, buried verbs, jargon the reader cannot follow without a definition |
| Flow | The section builds on the one before; no mini-summary at the end |
| Sameness | The opener differs from the other tool sections on this page and from the same tool's section on sibling pages |
| Tradeoff | The section says where the free plan stops and who should skip it |
| Rating | The `rating` score fits the limits this section states; the row in `docs/RATINGS.md` matches |
| Voice | Matches the silo voice sample; strong existing prose on a refresh is left alone |

For a line edit, write the original, the suggested version, and one line on why. Close the review with the question the humanizer asks of every recommendation: what would make this one wrong? If the section cannot answer it, the tradeoff is missing.

## 8. Full draft review

Read the whole article once as the reader, top to bottom, before the gate:

- Argument: opening fact, then tools in an order it explains, then a table that maps exact figures, then when to pay, then a decision rule the opening did not state.
- Evidence: compare the draft against the claims table twice, once for figures that drifted and once for claims with no row.
- Sitewide: the description, first sentence, tool openers, and closing each differ from their silo neighbors.
- Readability: most paragraphs run 2 to 4 sentences, with some variation; no run of same-shape sentences.
- Links: 2 to 5 internal links, real external sources, and the back-links added to older articles.

Then run the humanizer's final publication gate and the validation in `docs/SKILL.md` section 9. The progress-log entry names the research notes file and lists any claims that were narrowed or dropped.

## 9. What this workflow does not borrow

The general research-writing method this file adapts also recommends techniques that break site rules. Do not use them:

- Anecdote or personal-story hooks, invented people, or first-person experience without supplied evidence
- Rhetorical-question or curiosity hooks
- Statistics or expert quotes without a named, opened source, and "[needs source]" markers in public copy
- "Studies show" or "experts say" attribution
- Numbered, footnote, or academic reference lists in the article body. Sources are inline links on the claim.
- Versioned draft files in `content/`. Git keeps the history, and the notes file keeps the research.
- Emojis, dashes as punctuation, and celebratory sign-offs
