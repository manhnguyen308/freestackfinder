# Writing-pattern audit, 2026-09-25

Detect-mode audit of every reader-visible surface, run against `website-content-humanizer.md` (including the patterns merged from blader/humanizer on this date) and the public-content rules in `CLAUDE.md`. Findings name the pattern, quote the line, and give the fix in a few words. Nothing was rewritten. No score is given, and no finding says whether a machine wrote anything.

Status: the strong tells and medium findings 1 to 13 were fixed in Day 86b (see `freestackfinder-progress-log.md`). Weak tells were left in place unless they sat beside a stronger one. Line numbers below refer to the copy as audited, before those fixes.

## Scope and method

- Surfaces: 64 content files (50 articles, 6 hubs, homepage, Start Here, search, about, contact, disclaimer, privacy, terms), 19 templates in `layouts/`, `config.toml`, and the UI strings in `static/js/`.
- A pattern scan produced 159 candidates. Each was reviewed by hand, and false positives are listed at the end. Sitewide measurements covered sentence openers, label phrases reused across articles, repeated sentences between pages, and internal-link sentences. Trust pages and template copy were read in full.
- Strength follows the "Signal strength" section of the humanizer: strong tells justify an edit on one occurrence, medium tells matter when they recur, and weak tells are reported only as a cluster.

## Result at a glance

| Tier | Findings | Notes |
|---|---|---|
| Site rules | 0 | No dashes, curly quotes, chatbot residue, placeholders, citation tokens, unsupported first-hand claims, or self-reference to how copy is produced |
| Strong | 5 lines | One "not X, it is Y", one page announcement, one staged pivot, two one-line closers |
| Medium | 13 groups | Mostly structural and sitewide: link-sentence formula, label reuse, sibling pages sharing bullets, label-fragment lists, boilerplate positioning |
| Weak | 5 lines | Intensifiers and a figurative "quietly", reported as a cluster only |

## Strong tells

| Pattern | Location | Quote | Fix |
|---|---|---|---|
| Not X but Y | `content/cloud/free-ai-email-tools.md:104` | "Boomerang's free value is not full drafting; it is quality feedback:" | State what the free plan does: it scores a draft. |
| Page announcement (staged run-up) | `content/business/free-accounting-software.md:77` | "This guide focuses specifically on tools that maintain a proper ledger." | Cut; the section already shows it. |
| Staged pivot | `content/cloud/free-team-email.md:30` | "...are easy to find. Team email is different." | Merge into one sentence that states the difference. |
| One-line closer | `content/creative/freecad-alternatives.md:260` | "Mixing tools is normal in CAD work." | Cut; the sentence before already makes the point. |
| One-line closer (borderline) | `content/security/free-security-audit-tools.md:145` | "Interpreting scan output correctly still requires judgment." | Cut or replace with the next step. |

## Medium tells

### 1. Internal-link sentences follow one formula (sitewide)

Across the 50 articles, 67 link sentences open "For ..., see our [X] guide", 26 open "If you ..., see our...", and 8 open "See our...". Eleven articles end with four or more link sentences in a row, for example `content/productivity/grammarly-alternatives.md:163`, `content/business/free-project-management-software.md` (closing), and `content/video/free-video-editing-software.md:197`.

Fix: keep one or two links per closing, each inside a sentence that makes a claim, and vary how they are introduced.

### 2. Sibling pages share bullet lists nearly word for word

Pages that cover the same tools repeat the same bullets and sentences. Counts are sentences sharing a run of five or more content words.

| Pages | Shared | Example |
|---|---|---|
| `video/free-video-conferencing.md` and `video/zoom-alternatives.md` | 10 | "Group calls up to 60 minutes with up to 100 participants" |
| `video/free-video-editing-software.md` and `video/premiere-pro-alternatives.md` | 9 | "8-bit formats up to 60fps at Ultra HD 3840 x 2160" |
| `productivity/free-ai-writing-tools.md` and `productivity/free-chatgpt-alternatives.md` | 8 | "file upload, data analysis, image, voice" limits |
| `productivity/free-note-taking-apps.md` and `productivity/notion-alternatives.md` | 8 | platform and Notion free-plan bullets |
| `business/free-accounting-software.md` and `business/quickbooks-alternatives.md` | 6 | Wave and Zoho Books plan details |
| Four Cloud pages (Dropbox, backup, cloud storage, email) | 3 to 4 each | "Accounts created since March 9, 2026 start with 5GB and unlock the other 10GB after phone-number verification." |
| `creative/canva-alternatives.md:118` and `creative/photoshop-alternatives.md:152` | 1 | "Ads and upgrade prompts are part of the free experience" |

Fix: keep the full detail on the page where the tool is the main subject, and give the sibling page a shorter line with a different fact and a link.

### 3. Label phrases reused across articles

The humanizer allows labels before bullet lists but not one exact label reused across several articles.

| Label | Articles |
|---|---|
| "The practical limit:" | project management, screen recording, time tracking, website builders, Grammarly |
| "Where it falls short:" | PDF editors, video conferencing, FreeCAD, Grammarly |
| "Where you may outgrow it:" | project management, time tracking, website builders |
| "Included free:" | video conferencing, video editing, FreeCAD |
| Pairs used twice | "What you can do for free:", "Where the free plan stops:", "What you get without paying:", "What it covers:", "What it does not do:", "The main catch:", "Where it stops:", "Where the free tier stops:" |

Fix: give each section a label that names its own content, or drop the label where the bullets speak for themselves.

### 4. One label pair repeated inside a page

- `content/business/free-website-builders.md:81` onward: "What you can [build / publish / launch] for free:" five times and "The practical limit:" three times.
- `content/video/free-screen-recording-software.md:41` onward: "What you can [record / capture / share] for free:" three times and "The practical limit:" twice.

Fix: vary the labels per section, as the other tool guides now do.

### 5. Label-fragment lists

Lists where each item opens with a verbless fragment and a period, then explains it. Found in about ten articles, mostly in "Common mistakes" sections.

| Location | Example |
|---|---|
| `content/video/free-video-conferencing.md:34` | "Time limits on group calls. A 40 to 60-minute cap..." |
| `content/creative/canva-alternatives.md:68` | "Export formats you'll use. PNG, JPG, PDF, and GIF are table stakes." |
| `content/creative/canva-free-vs-paid.md:87` | "One-off personal projects. Birthday invitations..." |
| `content/creative/freecad-alternatives.md:69` | "No offline mode at all. If your internet is slow..." |
| `content/creative/photoshop-alternatives.md:167` | "CMYK and print-ready output. Photoshop has decades..." |
| `content/productivity/microsoft-office-alternatives.md:211` | "Switching everything at once. Keep the existing suite..." |
| `content/productivity/slack-alternatives.md:114` | "Migrating channels but not habits. Decide which channels..." |
| `content/video/free-video-editing-mac.md:144` | "Ignoring hardware requirements. DaVinci Resolve asks more..." |
| `content/video/free-video-editing-software.md:59` | "Watermarks and conditional export rules. A clean export..." |
| `content/business/free-resume-builders.md:210` | "Export format. A real PDF export is non-negotiable." |

Fix: turn each item into a full sentence with a subject, or a plain bullet with no label.

### 6. Formulaic sections repeated across articles

- "Common mistakes when switching from..." appears in 9 articles.
- A "When [the paid plan] is worth it" section, in slightly different wording, appears in about 24 articles.

Fix: keep them where the content is substantive, vary the heading to name the page's actual deciding point, and fold short mistake lists into the tool sections they belong to.

### 7. Runs of identical sentence openings

| Location | Run |
|---|---|
| `content/creative/canva-alternatives.md:61` | Four sentences in a row open "If you..." |
| `content/security/free-vpn.md:115` | Three sentences in a row open "If the problem is..." |
| `content/productivity/free-note-taking-apps.md:36` | Three "If you..." or "If notes..." sentences, each ending in an instruction |
| `content/business/free-accounting-software.md:77` | Two sentences open "If what you need is..." |
| `content/productivity/grammarly-alternatives.md:163` | Three link sentences open "If you are..." |
| `content/video/free-video-editing-software.md:197` | Three link paragraphs open "If you..." |

Fix: merge the conditions into one sentence or a short table, or change the subject of each sentence.

### 8. Figurative "gate" as a density signal

"Gate", "gated", or "gates" in the sense of "requires payment" appears 11 times on 6 pages: `canva-alternatives.md:51, 55, 69`, `free-pdf-editor-alternatives.md:84, 88`, `free-project-management-software.md:57` (a heading), `free-visio-alternatives.md:197, 200`, `photoshop-alternatives.md:153, 171`, and `free-time-tracking-software.md:36`.

Fix: say "requires a paid plan" or "is paid-only".

### 9. Unsupported praise

| Location | Quote | Fix |
|---|---|---|
| `content/creative/photoshop-alternatives.md:42` and `:126` | "Excellent brush engine" | Name what the brush engine does, or cut. |
| `content/video/free-open-source-video-editors.md:140` | "Blender's video editor is excellent within Blender workflows." | "suits Blender workflows" |
| `content/cloud/free-email-service.md:125` | "may still be excellent for daily mail" | "may still suit daily mail" |
| `content/business/free-accounting-software.md:86` | "can keep excellent books" | "can keep accurate books" |
| `content/productivity/microsoft-office-alternatives.md:140` | "Less intuitive for new users..." | State the difference, such as the menu layout. |
| `content/video/free-open-source-video-editors.md:79` | "Kdenlive or OpenShot will be more intuitive" | State the difference, such as fewer controls. |
| `content/productivity/microsoft-office-alternatives.md:175` | "Less well-known so community resources are smaller" | "Its community is smaller than LibreOffice's." |

### 10. Colon reveal

- `content/creative/canva-free-vs-paid.md:80`: "The main difference has been consistent for years: free covers the canvas..." Fix: state the difference as a plain sentence.

### 11. Positioning boilerplate repeated across templates

The same promise about limits, missing features, and upgrade points appears in seven places: `layouts/partials/footer.html:9`, `layouts/partials/review-block.html:10`, `layouts/_default/list.html:26`, the author box fallback in `layouts/_default/single.html:95`, `content/about.md:23`, the homepage tenets in `layouts/index.html`, and `config.toml:10`. A reader on an article page sees three versions of it.

Fix: state it fully once, on the about page, and give each template a shorter line that says something different.

### 12. Formula openers in site metadata

| Location | Quote | Pattern |
|---|---|---|
| `config.toml:10` | "Find the best free alternatives to paid software. We compare free-plan limits, practical tradeoffs, and when..." | Imperative opener, "the best", criteria triad |
| `content/_index.md:3` | "Find practical free software alternatives with clear free-plan tradeoffs..." | Imperative opener |
| `content/search.md:3` | "Search Free Stack Finder guides by software category, tool name, or use case..." | Imperative opener and criteria list |
| `content/about.md:3` | "Learn why Free Stack Finder exists, how we evaluate..., and how our guides help..." | Imperative opener and triad |

Fix: lead each with a fact about what the page offers.

### 13. Trust-page redundancy and wording

| Location | Quote | Pattern | Fix |
|---|---|---|---|
| `content/disclaimer.md:27` to `:33`, `:54` | "Affiliate relationships do not determine our recommendations." (bold), then three more independence statements | Redundant restatement, decorative bold | State independence once, with the mechanism. |
| `content/about.md:23` | "the limits readers usually discover too late" | Unsupported generalization | "the limits that decide whether a plan works" |
| `content/about.md:25` | "When a free tool is a good alternative, we explain why. When it is too limited, too narrow, or missing something critical, we say that too." | Parallel openings and a forced triad | One sentence without the triad. |
| `content/about.md:51` | "You can read our full affiliate disclaimer here." | "Here" as link text | Link the words "affiliate disclaimer". |

## Weak tells (cluster only)

- `content/creative/canva-free-vs-paid.md:154`: "The upgrade only really matters when..." (intensifier)
- `content/creative/photoshop-alternatives.md:53`: "the functions the work actually uses" (intensifier)
- `content/creative/photoshop-alternatives.md:177`: "Creative Cloud quietly versions your files." (figurative "quietly")
- `content/business/free-website-builders.md` (Carrd section): "No credit card required." (subjectless fragment)

None of these needs action unless it sits beside a stronger tell.

## Inactive template copy (not currently visible)

- `layouts/_default/single.html:138` to `:145`: the "Free stack for freelancers" sidebar card only renders if a `/free-stack-guide` page exists. None does, so readers never see it. If the page is ever added, "No email required." is a subjectless fragment.
- `layouts/_default/single.html:167`: the "More from this silo" fallback heading uses internal jargon, but every article has a category, so it never renders.

## False positives excluded

| Scanner hit | Count | Why excluded |
|---|---|---|
| Self-reference to AI, prompts, or automation | 8 | All are links to the site's AI-tool guides, or "promptly" in the privacy policy |
| First-hand wording outside evidence pages | 4 | Editorial-process statements ("when we materially revise a page"), not testing claims |
| Title Case headings | 4 | Proper nouns (Free Stack Finder, Google Sheets, product lists) |
| Vague connection | 14 | Literal relationships ("tied to a phone number", "associated with their Apple account") |
| Watch-list words | 25 of 37 | Literal uses: "Dynamic Link", PDF "highlight" annotations, "unlock" storage, "optimized media" |
| Placeholder | 2 | The word used literally in article text |
| Repeated sentence openers | 34 | Product names repeated as subjects, which the humanizer prefers to synonym cycling, and bullet lists |
| Consecutive openings | 19 of 29 | Deliberate contrasts ("For a low-traffic project... For a business...") and bullets |
| `content/contact.md` | 1 | Inline CSS, not copy |

## Suggested order of work

1. Fix the five strong tells.
2. Rewrite the internal-link closings (finding 1) and de-duplicate sibling pages (finding 2). These are the largest sources of sameness a reader clicking between pages will notice.
3. Replace reused labels and label-fragment lists (findings 3 to 5).
4. Tidy the metadata, templates, and trust pages (findings 11 to 13).
5. Leave weak tells unless they sit beside a stronger one.
