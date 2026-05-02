# Free Stack Finder — Design System Reference

Permanent design rules for the Hugo production site. Source of truth is `static/css/style.css`.

---

## Color tokens

CSS custom properties defined in `static/css/style.css`. Never rename — every layout, partial, and shortcode references them.

| Token | Value | Usage |
|---|---|---|
| `--primary` | `#0F766E` | Teal — links, active nav, CTAs, chips, trust elements |
| `--primary-dark` | `#0D5C57` | Hover state for teal elements |
| `--primary-light` | `#14B8A6` | Card hover border |
| `--primary-bg` | `#E6F7F5` | Chip backgrounds, light teal fills |
| `--accent` | `#F59E0B` | Amber — one affiliate CTA button per article only |
| `--accent-dark` | `#D97706` | Amber hover |
| `--text` | `#1E293B` | Body text |
| `--text-muted` | `#64748B` | Muted / meta text |
| `--text-light` | `#94A3B8` | Placeholder / light text |
| `--bg` | `#FFFFFF` | Page background |
| `--bg-2` | `#F8FAFC` | Alternate section background |
| `--bg-3` | `#F1F5F9` | Nav hover, table headers |
| `--border` | `#E2E8F0` | Default border |
| `--border-dark` | `#CBD5E1` | Hover border |
| `--success` | `#16A34A` | Verdict: good |
| `--success-bg` | `#F0FDF4` | Verdict good background |
| `--warning` | `#D97706` | Verdict: caution |
| `--warning-bg` | `#FFFBEB` | Verdict caution background |
| `--danger` | `#DC2626` | Verdict: avoid |
| `--danger-bg` | `#FEF2F2` | Verdict avoid background |

**Token name note:** Production tokens use longer names (`--primary`, `--text`, `--border`) rather than the short-form names in the handoff spec (`--p`, `--t`, `--bd`). Do not alias or rename — would break all selectors.

---

## Typography

System font stack — no webfont loaded (AdSense compliance, page speed).

```
'Segoe UI', system-ui, -apple-system, BlinkMacSystemFont, sans-serif
```

| Element | Size | Weight | Notes |
|---|---|---|---|
| Hero H1 | `clamp(28px, 5vw, 44px)` | 800 | `letter-spacing: -0.8px` |
| Article H1 | `clamp(26px, 4vw, 38px)` | 800 | `letter-spacing: -0.5px` |
| Section H2 | `clamp(21px, 3vw, 26px)` | 700 | Desktop border-top rule |
| Body | 17px | 400 | `line-height: 1.7` |
| Meta / small | 12–14px | 400–600 | `color: var(--text-muted)` |
| Eyebrow labels | 11–12px | 700 | UPPERCASE, `letter-spacing: 0.07em` |

**Article H2 treatment:** `border-top: 2px solid var(--border); padding-top: 14px` at `min-width: 601px` (desktop only). Do not remove.

**Amber CTA rule:** `--accent` is reserved for the single affiliate CTA button per article page. Never use amber for nav, chips, verdict labels, or editorial elements.

---

## Category icon accent colors

Used only on icon stroke and icon background circle. Not used in UI chrome anywhere else.

| Category | Slug | Stroke | Background tint |
|---|---|---|---|
| Creative & Design | `creative` | `#D95B35` | `#FEF0EB` |
| Productivity | `productivity` | `#2A9461` | `#EDFAF3` |
| Video & Recording | `video` | `#7C3AED` | `#F3EEFF` |
| Business Tools | `business` | `#C27B0A` | `#FEF7E6` |
| Security & Privacy | `security` | `#0E7E73` | `#E6F7F5` |
| Cloud & Storage | `cloud` | `#1D6FBA` | `#EAF3FB` |

Icon container: 44×44px circle (`border-radius: 50%`), background = matching tint. SVGs are stroke-based inline, `stroke-width="1.8"`, `stroke-linecap="round"`, `stroke-linejoin="round"`, `currentColor`. No emoji fallback. No icon font. No CDN icons in production.

---

## Layout and spacing

- **Container:** max-width 1100px
- **Reading column:** 720px (article body)
- **Sidebar:** 280px fixed, collapses below 960px
- **Article two-column:** collapses to single-column below 960px
- **Section rhythm:** `padding: 56px 0`
- **Category grid:** `repeat(auto-fill, minmax(160px, 1fr))`, 14px gap
- **Article card grid:** `repeat(auto-fill, minmax(290px, 1fr))`, 24px gap
- **Corner radii:** 4px (code/badges) · 8px (buttons/inputs) · 12px (cards/widgets) · 20–999px (chips/tags) · 50% (icon circles)

---

## Header and footer rules

**Header:** Sticky, 64px height. Logo: `FreeStackFinder` wordmark, "Finder" in `var(--primary)` teal, 22px weight 800. Nav: one item per silo slug. Search: inline SVG icon button. Mobile: hamburger toggle.

**Footer:** 3-column dark-slate (`#0F172A`) grid. Columns: brand + tagline / categories / site links. Trust pill links row. Affiliate disclosure note with `/disclaimer/` link. All footer links must resolve to real Hugo routes — no `href="#"` placeholders.

**Trust/legal routes** (do not change these URLs):
- `/about/`
- `/disclaimer/`
- `/privacy-policy/`
- `/terms/`
- `/contact/`

These differ from the handoff spec's `/how-we-test/`, `/disclosure/`, `/privacy/` — the production routes are intentionally kept to avoid breaking existing indexed URLs.

---

## Component rules

**Left-border accents (3–4px solid teal):** Used on `.editorial-note`, `.verdict`, `.affiliate-cta`, `blockquote`. Always with a neutral background. Editorial motif — do not change to rounded corners or remove.

**Verdict boxes:** `.verdict.good` / `.verdict.caution` / `.verdict.avoid`. Text-only with left-border color. No image banners.

**Affiliate CTA block:** Plain-text editorial aside, never an image banner. One amber button per article. Structure:
```html
<div class="affiliate-cta">
  <div class="affiliate-cta-content">
    <p class="affiliate-cta-title">Title</p>
    <p class="affiliate-cta-desc">Description.</p>
    <a href="URL" class="affiliate-cta-btn" rel="sponsored noopener" target="_blank">CTA →</a>
  </div>
</div>
```

**Hover states:** Cards lift `translateY(-3px)` + shadow bump + border darken. `transition: all 0.15–0.2s ease`.

**No dark mode. No glass. No blur. No gradients** except the barely-perceptible hero (`#F8FAFC → #E8F7F5`).

---

## Article structure (preserve for all silo articles)

1. Hook / context (1–2 paragraphs)
2. Quick verdict (`.verdict.good` box)
3. Comparison table (`.compare-wrap`)
4. "Why people look for alternatives"
5. Numbered tool sections: What it is · Free version · What's limited · Best for · Try link
6. Inline `.verdict` callouts
7. "Who should still pay?" (`.pay-box`)
8. "Our final recommendation"
9. FAQ (`<details>`), footnotes, byline, tags

---

## Image rules

- Feature images: 1200×630 WebP, below 200KB, saved to `static/img/<slug>.webp`
- Use per-silo accent colors on dark backgrounds (image assets only, not UI chrome)
- Never replace with generic stock photography
- Set `image: "/img/<slug>.webp"` in front matter
- Do not move or rename existing WebP paths — breaks `check_feature_images.py`

---

## Raw HTML in Markdown caution

Hugo goldmark is configured with `unsafe = true` (see `hugo.toml`). However, CommonMark HTML blocks end at the first blank line. If raw HTML in a `.md` file has blank lines between nested elements, the parser re-enters Markdown mode and may treat indented tags (4+ spaces) as code blocks, escaping them as visible text.

**Rule:** When using raw HTML blocks in Markdown, do not leave blank lines between parent and child elements within the same block structure. Close tags and open the next element without a blank line between them.

---

## AdSense compliance cautions

- No webfont that blocks rendering
- No complex animations or interstitial elements
- AdSense slot HTML, order, and `data-ad-*` attributes must not change
- `showAds` flag in `hugo.toml` controls slot visibility — do not hardcode slots outside the existing template logic
