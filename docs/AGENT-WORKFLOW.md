# Agent Workflow

Operating discipline for any coding agent (Claude, Codex, or other) working in this repo. Task-specific workflows live in `docs/SKILL.md`. This file covers *how* to work, not *what* to build.

---

## 1. Purpose

Keep agent runs scoped, verifiable, and token-efficient. Every change must be production-ready and traceable to a single intended task.

## 2. Session discipline

- One task type per session. Do not mix article publishing, feature work, and refactors in the same run.
- Start a fresh context for unrelated work. Do not extend a stale session into a new task type.
- Do not perform broad audits unless explicitly requested.
- If an instruction conflicts with `CLAUDE.md`, stop and flag it; do not silently override.
- State assumptions briefly when they affect the outcome.

## 3. Plan before edit

Plan first when a task touches **3+ files**, unfamiliar layouts/scripts, or build/deploy config. A plan is a short ordered list (files, change, why) — not a separate document.

For a single-file edit, no plan is needed.

Plan Mode (Claude) and equivalent planning features in other agents are optional aids; the rule is the discipline, not the tool.

## 4. Context and token management

- Use targeted file reads (known paths or sed line ranges) over full reads.
- Use `grep -RIn` only for exact terms inside a specific folder, always capped (`| head -20`).
- Do not scan `content/` articles broadly. Do not read `docs/ARCHIVE/` unless an old decision is required.
- Do not reread the same file in one session unless it has changed.
- Do not print large command outputs.

Allowed examples:
```bash
sed -n '1,220p' docs/SKILL.md
find content -maxdepth 2 -name "*.md"
grep -RIn "exact-term" content/business --include="*.md" | head -20
```

## 5. Verification before claiming completion

Never claim a task is done without running the relevant repo checks. At minimum:

```bash
python3 scripts/run_quality_checks.py --with-counts
```

Run `hugo --minify` only when public-facing files (`content/`, `layouts/`, `static/`, `assets/`, `config.toml`) changed. For new articles, also run:

```bash
python3 scripts/publish_checklist.py <silo> <slug>
```

Full checklist: `docs/BUILD-VALIDATION.md`.

## 6. Repeated-failure rule

After **two failed attempts** at the same correction (build error, test failure, validation error), stop. Do not loop a third fix.

Instead, write a 3–5 line diagnosis:
- what was attempted
- what the actual error says
- the most likely root cause
- the next concrete step (or a request for clarification)

Looping more than twice burns context and rarely converges.

## 7. Diff and commit

Before commit:
1. Inspect `git diff` (and `git status`) to confirm only intended files changed.
2. Run `git diff --check` for whitespace damage.
3. Run validation (Section 5).

Commit rules:
- Run git **once at the end**, after all edits and validation.
- Commit message describes only the actual repo change. Short, production-style.
- Never use `--no-verify` unless explicitly requested.
- Never mention agents, AI, automation, prompts, or assistants in commit messages.

## 8. Tracker and handoff

Every task ends with a `freestackfinder-progress-log.md` entry. See `docs/SKILL.md` §10 for the day-labeling rule and entry format.

If an article publishes, update `CONTENT-STRATEGY.md`. If a feature ships, update `FEATURE-STRATEGY.md`. Otherwise leave roadmap files alone.

## 9. Optional advanced tools

These are aids, not requirements. Core repo rules above must work without them.

- **Plan Mode / planning UIs** (Claude, Codex) — useful for §3 multi-file work.
- **Skills** (Claude) — `docs/SKILL.md` is the project skill; no other skills required.
- **Subagents / parallel agents** — useful only when a task has independent research branches.
- **Hooks** — not required; `.claude/` is gitignored.
- **MCP servers** — not used by this repo.
- **Worktrees** — useful for risky refactors; not needed for content/feature work.

If an agent does not support a feature above, ignore that bullet — none of the core workflow depends on it.

## 10. Quick rule summary

1. One task type per session.
2. Plan before editing 3+ files.
3. Targeted reads, capped greps.
4. Validate before claiming done.
5. Stop after two failed fixes; diagnose.
6. Inspect diff before commit.
7. Update progress log at end of every task.
8. Fresh context for unrelated work.
