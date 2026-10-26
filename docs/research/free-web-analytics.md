# Research notes: free-web-analytics

Brief
- Audit date: 2026-10-26 (Asia/Bangkok).
- Article: `content/business/free-web-analytics.md`.
- Reader's question: traffic, search, or behavior reporting, and who maintains the server?
- Must not change: ranking, publication date, routes, and unrelated prose.
- Scope: Business rotation. Sources opened; US dollars except Matomo's regional quote.

| Tool | Existing claim | Verified finding / claim as it should read | Source | Read on | Status | Classification / decision |
|---|---|---|---|---|---|---|
| GA4 | "up to 500 distinct event types per property" | No distinct-event-name cap applies to web streams; the 500-event limit is per app user for app streams. Correct the website comparison's claim. | https://support.google.com/analytics/answer/9267744?hl=en | 2026-10-26 | Narrowed | Confirmed outdated / Update |
| Umami | "Hobby ... one website and 100,000 events a month"; "Pro ... $20 ... 1 million ... 20 websites ... 10 team members" | These hosted limits/prices match. Business remains $200 monthly and adds replays/heatmaps. | https://umami.is/pricing | 2026-10-26 | Confirmed | Confirmed current / No change |
| Matomo | "Cloud ... From €22 ... 50,000 hits" | Official pricing page opened, but dynamic calculator did not expose a stable current euro price for this hit volume. | https://matomo.org/pricing/ | 2026-10-26 | Needs evidence | Unverifiable / Needs manual verification |

Research gaps
- GA4 retention settings, Search Console's 16-month window, and Clarity traffic-source/recording-retention statements require individual help pages; they are not established by the source reads above.
- Matomo's pricing page carries an October PHP security update notice. Existing article already assigns server security/updates to operators; no recommendation change follows without investigating affected PHP versions and deployment context.
