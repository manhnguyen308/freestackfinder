# FreeStackFinder — Claude Code Rules

## Mission
Build freestackfinder.com into a high-quality, useful, monetizable Hugo site by making steady, production-ready progress every day. You are not a passive assistant, you are an active creative associator, act like one.

## Project skill

For all task-specific workflows — daily content publishing, feature work, GSC-led refresh, AdSense workflow, affiliate safety, image generation, validation checklist, tracker updates, commit/deploy rules — use:

**`docs/SKILL.md`**

For general agent operating discipline — session scope, plan-first, targeted reads, repeated-failure rule, diff/commit discipline, optional advanced tools — use:

**`docs/AGENT-WORKFLOW.md`** (works for Claude, Codex, or any coding agent)

For every task that writes, rewrites, reviews, or publishes reader-visible website copy, use:

**`website-content-humanizer.md`**

@website-content-humanizer.md

Treat it as the governing editorial standard for articles, hubs, homepage copy, trust pages, headings, metadata, calls to action, navigation labels, empty states, and shared template text. Run its full publication gate before delivery. Its accuracy, anti-fabrication, sitewide-audit, and no-dash rules are mandatory.

**rtk install**

For token-saving with filters and compresses command outputs before they reach your LLM context. Single Rust binary, 100+ supported commands, <10ms overhead. Check if it's installed first, if not, install from https://github.com/rtk-ai/rtk. Restart the session if you need it to run. Always using this for token saving. Run 'rtk init' in the same project folder so claude.md or agents.md are updated.

## When to read what

| Task | Read |
|------|------|
| Every fresh session | This file + `docs/AGENT-WORKFLOW.md` + `freestackfinder-progress-log.md` |
| Any task execution | `docs/SKILL.md` |
| Any public-facing writing or editing | `website-content-humanizer.md` |
| Article publishing | `CONTENT-STRATEGY.md` |
| Feature work | `FEATURE-STRATEGY.md` |
| Image generation | `docs/IMAGE-GUIDELINES.md` |
| Affiliate / monetization | `docs/AFFILIATE-GUIDELINES.md` |
| Visual design / CSS / tokens | `docs/DESIGN-SYSTEM.md` |
| Build / deployment setup | `README.md` + `docs/BUILD-VALIDATION.md` |

Do not load every doc for every task. Load only what the current task requires.

## Task priority
1. Fix broken, missing, inconsistent, or incomplete work
2. Strengthen monetization on existing high-intent pages
3. Improve internal linking inside an existing cluster
4. Publish the next strongest article and complete its related linking/image work
5. Improve UX, SEO, trust, or layout only when directly relevant to the current batch

## Validation commands

```bash
python3 scripts/run_quality_checks.py --with-counts   # run before every deploy
python3 scripts/run_quality_checks.py --with-stale    # informational only
python3 scripts/publish_checklist.py <silo> <slug>    # verify a new article
hugo --minify                                          # only if public-facing files changed
```

All three QA checks must pass (0 failures) before committing.

## Critical never-do rules

### Front matter — never use
- `featured:`
- `faqs:`
- `verdict-box` HTML in new content (legacy pages may still contain it)
- bare unquoted date values
- inline keyword arrays

### Affiliate restrictions
- **Canva**: Under review — do not add CTAs unless tracker explicitly says Approved
- **Grammarly**: Declined — do not add CTAs
- Do not add affiliate links or CTAs for any program not confirmed Active in `docs/AFFILIATE-TRACKER.md`
- Do not use affiliate image banners (blocked by adblockers)

### Public content
- Never mention Claude, AI, assistant, prompts, or automation in site content, comments, metadata, or tracker entries
- Never mention Claude, AI, assistant, prompts, or automation in commit messages

### Git
- Never ask for permission in chat before normal git commit, push, or deploy steps
- Never skip hooks (`--no-verify`) unless explicitly requested
- Run git only once at the end, after all changes are complete and verified

## Known bugs not to reintroduce
1. `faqs:` with child items can break Cloudflare builds
2. `featured: true` breaks homepage behavior
3. `verdict-box` is legacy markup; do not add new `verdict-box` HTML to fresh content
4. Affiliate image banners are blocked by adblockers
5. `list.html` must not rely on default paginator sorting
6. `index.html` latest section must not use unsorted `.Site.RegularPages`

## Growth targets
- Month 1 target: 24 articles live across 6 silos
- Month 4 target: apply for Google AdSense once 25+ articles and visible organic traffic are present
- Month 6 target: re-apply to Impact.com and other direct affiliate programs using real traffic data

## Repo structure reference

### Article screenshots

- Store real user-supplied product screenshots in `static/img/screenshots/<post-slug>/`, with one folder per post. The Microsoft Office alternatives evidence uses `static/img/screenshots/office-alternatives/`.
- Use descriptive filenames, such as `onlyoffice-tracked-changes.png`, rather than `screenshot1.png` or `image2.png`.
- Do not create empty screenshot folders for other posts. Do not use generated substitutes for product evidence.
- Use the `screenshot` shortcode with a local `src`, specific `alt` text, and an optional factual `caption`. It reads the original image dimensions and links to the full-size image.
- First-hand wording is permitted only when the supplied evidence supports it. The Office comparison's September 2026 evidence is scoped to `content/productivity/microsoft-office-alternatives.md`; it does not authorize testing claims elsewhere.

```text
content/       business/ cloud/ creative/ productivity/ security/ video/
layouts/       index.html · _default/list.html · _default/single.html
               partials/schema.html · head.html · nav.html · footer.html
               partials/article-card.html
static/        css/style.css · img/
scripts/       images/ · run_quality_checks.py · validate_front_matter.py
               check_internal_links.py · check_feature_images.py
               report_article_counts.py · report_stale_content.py
               publish_checklist.py
```

<!-- rtk-instructions v2 -->
# RTK (Rust Token Killer) - Token-Optimized Commands

## Golden Rule

**Always prefix commands with `rtk`**. If RTK has a dedicated filter, it uses it. If not, it passes through unchanged. This means RTK is always safe to use.

**Important**: Even in command chains with `&&`, use `rtk`:
```bash
# ❌ Wrong
git add . && git commit -m "msg" && git push

# ✅ Correct
rtk git add . && rtk git commit -m "msg" && rtk git push
```

## RTK Commands by Workflow

### Build & Compile (80-90% savings)
```bash
rtk cargo build         # Cargo build output
rtk cargo check         # Cargo check output
rtk cargo clippy        # Clippy warnings grouped by file (80%)
rtk tsc                 # TypeScript errors grouped by file/code (83%)
rtk lint                # ESLint/Biome violations grouped (84%)
rtk prettier --check    # Files needing format only (70%)
rtk next build          # Next.js build with route metrics (87%)
```

### Test (60-99% savings)
```bash
rtk cargo test          # Cargo test failures only (90%)
rtk go test             # Go test failures only (90%)
rtk jest                # Jest failures only (99.5%)
rtk vitest              # Vitest failures only (99.5%)
rtk playwright test     # Playwright failures only (94%)
rtk pytest              # Python test failures only (90%)
rtk rake test           # Ruby test failures only (90%)
rtk rspec               # RSpec test failures only (60%)
rtk test <cmd>          # Generic test wrapper - failures only
```

### Git (59-80% savings)
```bash
rtk git status          # Compact status
rtk git log             # Compact log (works with all git flags)
rtk git diff            # Compact diff (80%)
rtk git show            # Compact show (80%)
rtk git add             # Ultra-compact confirmations (59%)
rtk git commit          # Ultra-compact confirmations (59%)
rtk git push            # Ultra-compact confirmations
rtk git pull            # Ultra-compact confirmations
rtk git branch          # Compact branch list
rtk git fetch           # Compact fetch
rtk git stash           # Compact stash
rtk git worktree        # Compact worktree
```

Note: Git passthrough works for ALL subcommands, even those not explicitly listed.

### GitHub (26-87% savings)
```bash
rtk gh pr view <num>    # Compact PR view (87%)
rtk gh pr checks        # Compact PR checks (79%)
rtk gh run list         # Compact workflow runs (82%)
rtk gh issue list       # Compact issue list (80%)
rtk gh api              # Compact API responses (26%)
```

### JavaScript/TypeScript Tooling (70-90% savings)
```bash
rtk pnpm list           # Compact dependency tree (70%)
rtk pnpm outdated       # Compact outdated packages (80%)
rtk pnpm install        # Compact install output (90%)
rtk npm run <script>    # Compact npm script output
rtk npx <cmd>           # Compact npx command output
rtk prisma              # Prisma without ASCII art (88%)
rtk uv run <cmd>        # Compact uv project command output
```

### Files & Search (60-75% savings)
```bash
rtk ls <path>           # Tree format, compact (65%)
rtk read <file>         # Code reading with filtering (60%)
rtk grep <pattern>      # Search grouped by file (75%). Format flags (-c, -l, -L, -o, -Z) run raw.
rtk find <pattern>      # Find grouped by directory (70%)
```

### Analysis & Debug (70-90% savings)
```bash
rtk err <cmd>           # Filter errors only from any command
rtk log <file>          # Deduplicated logs with counts
rtk json <file>         # JSON structure without values
rtk deps                # Dependency overview
rtk env                 # Environment variables compact
rtk summary <cmd>       # Smart summary of command output
rtk diff                # Ultra-compact diffs
```

### Infrastructure (85% savings)
```bash
rtk docker ps           # Compact container list
rtk docker images       # Compact image list
rtk docker logs <c>     # Deduplicated logs
rtk kubectl get         # Compact resource list
rtk kubectl logs        # Deduplicated pod logs
```

### Network (65-70% savings)
```bash
rtk curl <url>          # Compact HTTP responses (70%)
rtk wget <url>          # Compact download output (65%)
```

### Meta Commands
```bash
rtk gain                # View token savings statistics
rtk gain --history      # View command history with savings
rtk discover            # Analyze Claude Code sessions for missed RTK usage
rtk proxy <cmd>         # Run command without filtering (for debugging)
rtk init                # Add RTK instructions to CLAUDE.md
rtk init --global       # Add RTK to ~/.claude/CLAUDE.md
```

## Token Savings Overview

| Category | Commands | Typical Savings |
|----------|----------|-----------------|
| Tests | vitest, playwright, cargo test | 90-99% |
| Build | next, tsc, lint, prettier | 70-87% |
| Git | status, log, diff, add, commit | 59-80% |
| GitHub | gh pr, gh run, gh issue | 26-87% |
| Package Managers | pnpm, npm, npx | 70-90% |
| Files | ls, read, grep, find | 60-75% |
| Infrastructure | docker, kubectl | 85% |
| Network | curl, wget | 65-70% |

Overall average: **60-90% token reduction** on common development operations.
<!-- /rtk-instructions -->