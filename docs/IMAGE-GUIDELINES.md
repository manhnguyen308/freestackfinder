# FreeStackFinder — Feature Image Guidelines

Read this file when generating or fixing feature images.

---

## Tool requirements

- Generate with Python + Pillow
- Python full path (shell stubs resolve to Microsoft Store on this machine and do not work):
  ```
  /c/Users/vboxuser/AppData/Local/Programs/Python/Python312/python.exe
  ```
- Try `python scripts/images/...` first; if it exits 49 (Store stub), use the full path above
- Only report Python unavailable after the full path also fails

## Installation rule

When Python or Pillow is missing:
1. Check if already installed
2. Attempt install using the safest method available for the environment
3. Continue the task after install — do not fall back to placeholders without attempting first
4. Only stop if install fails or is blocked by permissions/network

## Image specs

- Size: 1200×630
- Format: WebP (optimized output, not PNG unless transparency is truly required)
- Target file size: below 200 KB where practical without visible quality loss
- Save to: `static/img/`

## Filename rules

- Descriptive, lowercase, hyphenated (e.g. `free-time-tracking-software.webp`)
- Match article slug where practical
- Do not use generic names like `image1.webp`

## SEO rules

- Filename must match article slug where practical
- Alt text derived from article title or a clear descriptive phrase
- Do not keyword-stuff filenames or alt text
- Article front matter `image` must point to the generated `.webp` file

## Script rules

- Store all generator scripts in `scripts/images/`
- Do not create image generator scripts in the repo root
- When fixing an existing script in the wrong location, move it into `scripts/images/` and update any related references

## Verification checklist

Before marking image work done:
- [ ] File exists in `static/img/`
- [ ] Article front matter `image` path matches the generated file exactly
- [ ] File size is below 200 KB
- [ ] Image renders on the article card and article page

---

## Visual style guide

### Layout
- Background: `#101116`
- Left panel: dark mock UI
- Right panel: featured card + 2×2 comparison cards
- Bottom bar: solid accent color, title in bold white
- Cards use circle helper with tool initials

### Accent colors by silo
| Silo | Color |
|------|-------|
| Security | `#8b5cf6` |
| Business | `#10b981` |
| Cloud | `#3b82f6` or `#06b6d4` |
| Creative | `#f97316` |
| Video | `#ef4444` |
| Productivity | `#6366f1` |

### Shared helper module
`scripts/images/image_helpers.py` provides: font loader, text truncation, word-wrap, rounded-rect, circle, draw_chrome, draw_featured_card, draw_grid, draw_bar, and output-path helper. All new generator scripts should use this module.
