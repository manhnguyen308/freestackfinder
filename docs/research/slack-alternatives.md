# Research notes: slack-alternatives

Brief
- Audit date: 2026-10-26 (Asia/Bangkok).
- Reader question: Which current free limits and paid boundaries affect the existing comparison?
- Scope: targeted priority verification during weekly maintenance, not every historical or qualitative claim.
- Must not change: article structure, rankings without material evidence, publication date, URL, affiliate behavior, images and genuine dated screenshot observations.
- Article: `content/productivity/slack-alternatives.md`.

| Product | Article/location | Exact existing statement | Verified finding | Official source | Read on | Claim status | Finding classification | Decision |
|---|---|---|---|---|---|---|---|---|
| Slack | content/productivity/slack-alternatives.md:21 | [Slack's current free plan](https://slack.com/help/articles/27204752526611-Feature-limitations-on-the-free-version-of-Slack) hides messages and files older than 90 days and deletes data older than one year, so upgrading later will not bring the oldest material back. A team that needs a durable conversation archive has to pay, export what Slack permits, or move. | Free retains90-day visibility and deletes data older than one year. | https://slack.com/help/articles/27204752526611-Feature-limitations-on-the-free-version-of-Slack | 2026-10-26 | Confirmed | Confirmed current | No change |
| Slack | content/productivity/slack-alternatives.md:135 | Enterprise compliance requirements are the other strong argument for Slack paid. Data retention policies, eDiscovery, audit logs, and SSO integrations are available on Slack's Business+ and Enterprise Grid plans at a level that free tools cannot always match with the same reliability and support guarantees. | Current highest plan is Enterprise+, not Enterprise Grid. Pro7.25 annual/8.75monthly and Business+15/18 remain listed US prices. | https://slack.com/pricing | 2026-10-26 | Confirmed | Confirmed outdated | Replace obsolete plan name only; preserve pricing |
| Mattermost | content/productivity/slack-alternatives.md:86 | Team Edition provides channels, direct messages, threads, file sharing, and clients for major desktop and mobile platforms. The [current edition documentation](https://docs.mattermost.com/product-overview/editions-and-offerings.html) describes it as a free self-hosted option for fewer than 250 activated users when single sign-on is not required. | Team Edition remains free self-hosted, intended under250 activated users without SSO; sensitive commercial workloads not recommended. | https://docs.mattermost.com/product-overview/editions-and-offerings | 2026-10-26 | Confirmed | Confirmed current | No change |
| Rocket.Chat | content/productivity/slack-alternatives.md:101 | The [current plan documentation](https://docs.rocket.chat/our-plans) limits Starter to 50 users and describes Community as core messaging for up to 100 concurrent users. Community supports video calls through Jitsi or BigBlueButton and has limited app integrations. Rocket.Chat says Community is intended for hobbyist, educational, or small non-production deployments. | Starter50 users and Community100concurrent remain; both require hosting, Community scope is core messaging. | https://docs.rocket.chat/our-plans | 2026-10-26 | Confirmed | Confirmed current | No change |

Research gaps
- Only the listed claims are checked. Other prices or features remain outside this targeted verification; an inaccessible page is not a current verification.
- US prices are stated only where the opened official page displayed USD; region-limited pricing is recorded above.
- Original September screenshot captions remain dated observations, without any new testing claim.

Workflow
- Applied AGENTS.md, CLAUDE.md, docs/AGENT-WORKFLOW.md, docs/SKILL.md, website-content-humanizer.md, docs/CONTENT-RESEARCH-WRITING.md, docs/FRESHNESS-CHECKS.md and the configured researcher role. OpenAI Docs used for OpenAI facts, with the user-authorized official vendor pricing/help-source scope.
- Research only. Lead reviews evidence before publication; no article copy or front matter edited.

Evidence details
- https://slack.com/pricing currently lists Enterprise+ at lines 194-202, not Enterprise Grid. Limit and lower-price claims are unchanged.
