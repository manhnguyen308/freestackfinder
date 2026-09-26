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
| `--primary-fill` | `#0F766E` | Solid teal behind white text: buttons, table heads, active chips, pagination, back-to-top |
| `--primary-fill-hover` | `#0D5C57` | Hover for `--primary-fill` |
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

**Fill vs. text teal:** Use `--primary` for teal text, links, borders, stars, and focus outlines. Use `--primary-fill` for any solid teal background that carries white text. In light mode they are the same color; in dark mode `--primary` turns bright for contrast on the dark page while `--primary-fill` stays brand teal so white text keeps 5.5:1 contrast.

### Dark theme

`html[data-theme="dark"]` swaps the tokens in section 35 of `style.css`. An inline script in `head.html` sets the attribute before first paint from the reader's saved choice (`localStorage` key `theme`), or from the system `prefers-color-scheme` setting when there is none. The dark rules sit inside `@media screen`, so printing always uses the light palette.

| Token | Dark value |
|---|---|
| `--primary` | `#2DD4BF` |
| `--primary-dark` | `#5EEAD4` (lighter, because it is the hover and tinted-text color) |
| `--primary-light` | `#14B8A6` |
| `--primary-bg` | `#0F2D30` |
| `--primary-fill` / `--primary-fill-hover` | `#0F766E` / `#115E59` |
| `--text` / `--text-muted` / `--text-light` | `#E2E8F0` / `#94A3B8` / `#7F8EA3` |
| `--bg` / `--bg-2` / `--bg-3` | `#0F172A` / `#152033` / `#1E293B` |
| `--border` / `--border-dark` | `#26334A` / `#3A4A63` |
| `--success` / `--success-bg` | `#4ADE80` / `#0F2A1C` |
| `--warning` / `--warning-bg` | `#FBBF24` / `#2A2110` |
| `--danger` / `--danger-bg` | `#F87171` / `#2D1618` |

Contrast on `--bg`: body text 14.5:1, muted text 7:1, teal links 9.6:1. `--accent` amber is unchanged, and the amber button keeps dark slate text in both themes. New components must use tokens rather than hex values; any color that cannot be a token needs a `:root[data-theme="dark"]` override in section 35.

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

**Header:** Sticky, 64px height. Logo: `FreeStackFinder` wordmark, "Finder" in `var(--primary)` teal, 22px weight 800. Nav: one item per silo slug. Search: inline SVG icon button. Theme toggle: 36px icon button after search (`#theme-toggle`, `aria-pressed` for dark), showing a moon in light mode and a sun in dark mode; hidden when JavaScript is off. Mobile: hamburger toggle.

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

**Tool CTA button:** Each tool section ends with a Markdown link on its own line, such as `[Download Obsidian free →](https://obsidian.md)`. `layouts/_default/single.html` turns any paragraph that holds only one external link into `<p class="tool-cta"><a class="tool-cta-btn">`, drops a trailing `→` or `->` from the text, adds an arrow icon, and opens the link in a new tab. Style: `--primary-bg` fill, `--primary` border, `--primary-dark` text, solid `--primary` on hover, 44px tall, full width below 640px. Keep it tinted so the solid affiliate button stays the strongest action. To keep a link inline, put it inside a sentence; to skip the button for a standalone link, give it a title (`[text](url "title")`).

**Free plan star rating:** `{{< rating 4.5 >}}` on its own line under a tool heading renders `<div class="tool-rating">`: an uppercase "Free plan" label, five 18px inline SVG stars (half stars use a left-half polygon), the score as "4.5/5", and a muted "How we rate" link to `/about/#star-ratings`. Filled stars use `--primary` and empty ones `--border-dark`; stars stay teal because amber is reserved for the affiliate button. Screen readers get "Free plan rating: 4.5 out of 5" and the SVGs are hidden. The shortcode fails the build on any score outside 1 to 5 in half steps. Scores and their reasons live in `docs/RATINGS.md`.

**Hover states:** Cards lift `translateY(-3px)` + shadow bump + border darken. `transition: all 0.15–0.2s ease`.

**Dark mode through tokens only** (see "Dark theme" above). **No glass. No blur. No gradients** except the barely-perceptible hero (`#F8FAFC → #E8F7F5`).

---

## Article structure (preserve for all silo articles)

1. Hook / context (1–2 paragraphs)
2. Quick verdict (`.verdict.good` box)
3. Comparison table (`.compare-wrap`)
4. "Why people look for alternatives"
5. Numbered tool sections: What it is · Free version · What's limited · Best for · Try link (a standalone Markdown link, rendered as a tool CTA button)
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
