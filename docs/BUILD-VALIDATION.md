# Build Validation

## Hugo version

- **Required:** Hugo Extended 0.160.1
- **Cloudflare Pages env var:** `HUGO_VERSION` = `0.160.1`
- **Build command:** `hugo --minify`
- **Output directory:** `public`

Verify local installation:

```bash
hugo version
# Expected: hugo v0.160.1+extended ...
```

## QA scripts

Run before every deploy:

```bash
python3 scripts/run_quality_checks.py --with-counts
```

All three checks must pass:
- Front matter validation (`scripts/validate_front_matter.py`)
- Internal link check (`scripts/check_internal_links.py`)
- Feature image check (`scripts/check_feature_images.py`)

Known non-blocking warnings (do not act on):
- 3 image orphans (known: `default-article.jpg`, `nordpass-banner.png`, `nordvpn-banner.png`)

Optional maintenance reports:

```bash
python3 scripts/run_quality_checks.py --with-stale
```

The stale content report is informational only. It flags published silo articles whose `lastmod` date is 183+ days old and does not affect the QA runner exit code.

## Future-dated articles

Hugo excludes future-dated content from normal production builds. Before deploy, do not rely on a successful build alone when publishing a new article:

- `scripts/validate_front_matter.py` fails live articles whose `date` or `lastmod` is after the current UTC build date
- scheduled drafts should remain `draft: true` until publish day
- after `hugo --minify`, confirm any newly published article exists at `public/<silo>/<slug>/index.html`
- if tracker counts and built output disagree, trust the source files, then document whether the missing article is future-dated or truly broken

## Validation checklist

Before marking a deployment complete:

1. `git diff --check` clean
2. `python3 scripts/run_quality_checks.py --with-counts` — 3 passed · 0 failed
3. `hugo --minify` — no errors, no deprecation warnings
4. Article count matches tracker (currently 43)
5. Search index JSON builds (`public/index.json` present)
6. Start Here page builds (`public/start-here/`)
7. Category hub pages build (one per silo)
8. `comparison-table` and `verdict` shortcodes render without error
9. Schema/JSON-LD partial produces no build warnings
10. Any newly published article appears in `public/<silo>/<slug>/index.html`
