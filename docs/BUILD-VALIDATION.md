# Build Validation

## Hugo version

- **Required:** Hugo Extended 0.160.1
- **Cloudflare Pages env var:** `HUGO_VERSION` = `0.160.1`
- **Build command:** `hugo --minify`
- **Output directory:** `public`

Use the versioned official Hugo v0.160.1 release archive and verify its SHA-256 against the checksum published with that release. On 64-bit Windows, use `hugo_extended_0.160.1_windows-amd64.zip`; place the extracted binary in a versioned tools folder. After adding that folder to PATH, open a new terminal and verify the version. An older machine-level PATH entry can still take precedence over the user-level entry; avoid broad PATH edits and call the versioned binary explicitly until an administrator removes or reorders that specific old entry. Package-manager installs are not version-pinned.

```powershell
hugo version
# Expected: hugo v0.160.1+extended ...
# Or verify the pinned binary directly (current workspace path):
& 'C:\Website projects\Library\hugo_extended_0.160.1_windows-amd64\hugo.exe' version
```

`docker-compose.yml` also pins `hugomods/hugo:base-0.160.1`, which provides Extended Hugo without additional Go, Node, or Git tools. With Docker Compose installed, run `docker compose run --rm hugo version` to check it, `docker compose run --rm --service-ports hugo server -D --bind 0.0.0.0` for preview, or `docker compose run --rm hugo --minify` for a production build.

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
4. Article count matches tracker (see `freestackfinder-progress-log.md` Current state)
5. Search index JSON builds (`public/index.json` present)
6. Start Here page builds (`public/start-here/`)
7. Category hub pages build (one per silo)
8. `comparison-table` and `verdict` shortcodes render without error
9. Schema/JSON-LD partial produces no build warnings
10. Any newly published article appears in `public/<silo>/<slug>/index.html`

## Static asset cache versioning

The shared Hugo asset URL partial appends a 12-character SHA-256 query value to the stylesheet, main script, and search script URLs. Their files keep stable paths; the URL changes when file contents change so browsers request the updated asset. After changing these files, inspect generated HTML to confirm the versioned URLs are present.

## Deployment response checks

- `static/_headers` configures `Strict-Transport-Security: max-age=300` for `https://freestackfinder.com/*`. Confirm the deployed apex response includes the header before considering any HSTS duration increase.
- Verify both apex and `www` HTTP and HTTPS after deployment. The www hostname needs correct DNS, certificate, and an edge redirect to the apex configured in the Cloudflare account; repository files alone do not establish that configuration. Do not report www routing as fixed until live responses confirm it.
