# Free plan star ratings

Every tool section in an article carries a free plan rating of 1 to 5 stars in half steps, written as `{{< rating 4.5 >}}` on its own line under the tool heading (under the `verdict` badge when a section has one). The shortcode lives in `layouts/shortcodes/rating.html`, fails the build on any value outside 1 to 5 in half steps, and links to the public rubric at `/about/#star-ratings`.

## Rubric

The stars score the free plan only, measured against the job the page covers. The public version of this rubric is in `content/about.md`; keep the two in step.

| Stars | Meaning |
|---|---|
| 5 | The free version does the whole job, with no cap a typical user reaches |
| 4 | Covers the job for one person or a small team; limits appear only with heavier use, more people, or extras |
| 3 | Usable, but a published cap on storage, records, exports, users, or branding is likely to come up in regular use |
| 2 | Covers part of the job; core features are paid or the cap arrives quickly |
| 1 | Free in name only, such as a short trial, a paid-only feature, or output you cannot use |

Half stars sit between two levels.

## Rules

- Base each score on the limits stated in the tool's own section, which come from vendor pricing and help pages. Do not score from hands-on impressions, and do not imply testing.
- Affiliate status never raises a score. NordPass, an active affiliate program, scores 2.5 because of its one-session limit.
- The same tool can score differently on two pages only when the job differs, such as Notion for solo notes (4) versus team projects (3). Give the reason in the table below.
- A section written as the page's paid boundary, such as Backblaze on the backup page, gets no rating. Tools listed in "a note on" or "tools we did not include" sections are not rated either.
- When a freshness check changes a free limit, recheck that tool's score and its row here in the same change.
- New articles: add a rating under every tool heading and a table here. `scripts/publish_checklist.py` fails a numbered tool section without a rating unless its heading calls it a paid option.

## Scores by article

Scores and reasons as of 2026-09-26.

### Productivity

**free-ai-writing-tools**
| Tool | Stars | Reason |
|---|---|---|
| ChatGPT | 4.5 | Everyday text chats uncapped under abuse safeguards; files, images, voice, and analysis have separate limits |
| Claude | 3.5 | Rolling usage allowance that sustained drafting reaches; projects and model choice are paid |
| Microsoft Copilot | 4 | Free on web and in Edge under credits and peak-time rules; desktop Office integration is paid |
| Rytr | 2.5 | 10,000 characters a month, which a long document uses up; custom use cases paid |
| Google Gemini | 4 | Current models at standard limits; 32k context without a Google AI plan |

**free-calendar-app**
| Tool | Stars | Reason |
|---|---|---|
| Google Calendar | 5 | Events, shared calendars, Meet links, and one booking page; paid adds only business admin |
| Notion Calendar | 4 | Free, but needs a Notion account and leans on Google Calendar; Outlook sync limited |
| Apple Calendar | 4.5 | No paid tier; sync is Apple-only |
| Proton Calendar | 3.5 | Three personal calendars; more calendars and sharing are paid |
| Zoho Calendar | 4.5 | Free with a Zoho account including team view; no stated cap |

**free-chatgpt-alternatives**
| Tool | Stars | Reason |
|---|---|---|
| Claude | 3.5 | Rolling five-hour allowance that heavy document work reaches; five projects |
| Microsoft Copilot | 4 | Free service under credits and peak-time rules; Office app integration is paid |
| Google Gemini | 4 | 32k context; limits refresh every five hours up to a weekly cap |
| Perplexity AI | 4 | Basic search without a quota; five Pro Searches and three uploads a day |
| Grok | 3.5 | Search at a lower allowance, watermarked images, no published cap, training opt-out only on business plans |

**free-pdf-editor-alternatives**
| Tool | Stars | Reason |
|---|---|---|
| PDFgear | 5 | Text editing, forms, signing, OCR, and conversion with no page limit, watermark, or login |
| PDF24 Tools | 4 | 25+ free tools with no account; one task at a time makes text edits awkward |
| Sejda | 3 | Three tasks an hour, 200 pages, 50 MB |
| LibreOffice Draw | 3.5 | Fully free and offline, but no form-filling or signing workflow and messy layers on complex PDFs |
| Xodo | 3 | Free reader annotates and signs but barely edits text; web tools allow one action a day |

**grammarly-alternatives**
| Tool | Stars | Reason |
|---|---|---|
| LanguageTool | 4 | Grammar in 30+ languages with a text-length cap; advanced phrasing is Premium |
| ProWritingAid | 2.5 | 500 words per check and each report twice a day |
| Hemingway Editor | 3.5 | Full readability analysis free in the browser, but no grammar checking or extension |
| Google Docs built-in | 3.5 | Spelling and grammar inside Docs only; basic style checks |

**notion-alternatives**
| Tool | Stars | Reason |
|---|---|---|
| Obsidian | 4.5 | Local notes free with no account; Sync and Publish are paid add-ons |
| Logseq | 4 | No paid feature tier, but database views lag Notion and sync needs third-party storage |
| Anytype | 4.5 | Local storage and peer-to-peer sync free; hosted network resources have plan limits |
| Superhuman Docs | 3.5 | Personal docs unlimited; shared docs capped at 50 objects and 1,000 rows, 7-day history |
| Joplin | 3.5 | Free with sync through storage you have, but no database views or boards for a Notion-style workspace |

**microsoft-office-alternatives**
| Tool | Stars | Reason |
|---|---|---|
| Google Docs, Sheets, Slides | 4.5 | Full browser suite; 15 GB shared with Gmail and Photos, no Power Query or VBA |
| LibreOffice | 5 | No subscription or premium tier; full offline suite |
| OnlyOffice | 4.5 | Free desktop editors; cloud collaboration limited on free |
| WPS Office | 3 | Free editors with subscription promotions in the interface and 1 GB cloud storage |

**slack-alternatives**
| Tool | Stars | Reason |
|---|---|---|
| Discord | 4.5 | No 90-day history window; some upload and streaming features need Nitro |
| Microsoft Teams free | 4 | Chat and file sharing on the free plan; caps on group-call length, participants, recording, and storage |
| Google Chat | 4 | Personal accounts can create spaces; fewer integrations and managed features |
| Mattermost Team Edition | 4 | Free self-hosted for fewer than 250 users; no SSO, and you run the server |
| Rocket.Chat | 3 | Starter capped at 50 users; Community at 100 concurrent and meant for non-production |

**free-note-taking-apps**
| Tool | Stars | Reason |
|---|---|---|
| Google Keep | 4.5 | No paid tier or note cap; no Markdown, folders, or long notes |
| Apple Notes | 4 | Free on Apple devices; sync limited by 5 GB shared iCloud storage |
| Standard Notes | 3 | Plain-text editor only; Markdown, checklists, and attachments are paid |
| Simplenote | 4.5 | No paid tier; text only |
| Notion | 4 | Unlimited blocks for one person; 7-day history, 5 MB uploads, 1,000 blocks once a second member joins |

### Business

**free-accounting-software**
| Tool | Stars | Reason |
|---|---|---|
| Wave | 4 | Unlimited invoices, bills, and records on Starter; bank imports and receipt capture are paid |
| Zoho Books | 3.5 | Free up to $50,000 revenue, one user plus accountant, 1,000 invoices a year; no live bank feeds |
| Akaunting | 2.5 | One company, one user, 1,000 invoices; chart of accounts, balance sheet, and ledger are a paid app |
| Manager | 5 | Desktop edition has no limit on transactions, businesses, reports, or modules |
| GnuCash | 4.5 | No license fee or caps; no bank connections or sync |

**quickbooks-alternatives**
| Tool | Stars | Reason |
|---|---|---|
| Wave | 4 | As in the accounting guide |
| Zoho Books | 3.5 | Revenue threshold, one user plus accountant, 1,000 invoices a year |
| Invoice Ninja | 2.5 | Hosted plan stops at five clients with branding; bookkeeping and reports are narrow for accounting |
| GnuCash | 4.5 | No caps; manual CSV imports and no sync |
| FreshBooks | 1 | 30-day trial only, no permanent free plan |

**free-invoicing-software**
| Tool | Stars | Reason |
|---|---|---|
| Wave | 4 | Unlimited invoices; automatic reminders and bank imports are paid |
| Zoho Invoice | 3.5 | Two users, three projects, 500 invoices a year, branding, deletion after 180 idle days |
| Invoice Ninja | 3 | Unlimited invoices but five hosted clients; self-hosting removes the cap |
| Square Invoices | 4 | Unlimited invoices, estimates, contracts, and users; payment fees and paid milestones |
| PayPal Invoicing | 4 | No fee to send, reminders included; fees when paid |
| Stripe Invoicing | 3 | 0.4% per paid invoice on top of processing fees |

**free-crm-software**
| Tool | Stars | Reason |
|---|---|---|
| HubSpot CRM Free | 3.5 | Two users and 1,000 contacts |
| Zoho CRM Free | 3.5 | Three users; automation and forecasting paid |
| Freshsales Free | 3 | Three users, and the free plan is missing from the main pricing page |
| Bitrix24 Free | 3 | Seat limit published inconsistently; 5 GB shared |

**free-hr-software**
| Tool | Stars | Reason |
|---|---|---|
| Zoho People | 3 | Five users; records, documents, and leave only |
| OrangeHRM Starter | 4 | Unlimited employees and full HRIS modules; self-hosted with community support |
| Homebase | 3 | One location, 10 employees, basic scheduling and time clock |
| Bitrix24 | 3 | Broad but shallow HR layer; seat limit unclear |
| Google Sheets | 2 | Free spreadsheet with no HR workflows, self-service, or audit trail |

**free-project-management-software**
| Tool | Stars | Reason |
|---|---|---|
| Trello | 3.5 | 10 boards and 10 collaborators; timeline and table views paid |
| Asana Personal | 3 | Two users |
| Notion | 3 | Unlimited for one member; a shared workspace gets only a block trial |
| ClickUp | 3.5 | Unlimited tasks and members; 60 MB storage |
| Linear | 3 | 250 issues and two teams |

**free-resume-builders**
| Tool | Stars | Reason |
|---|---|---|
| Canva | 4.5 | PDF export without watermark; some templates are Pro |
| Google Docs | 4.5 | PDF and Word export with no cap; few templates, no guidance |
| Indeed Resume Builder | 4 | Free PDF download; basic design tied to Indeed |
| Resume.com | 3.5 | Free PDF from basic templates; premium templates and upgrade prompts |

**free-social-media-scheduling**
| Tool | Stars | Reason |
|---|---|---|
| Buffer | 3 | Three channels, 10 queued posts each, one user |
| Metricool | 3 | One brand, 20 posts a month, no LinkedIn or X |
| Later | 2.5 | Limited scheduling with no published number; team features paid |
| Meta Business Suite | 4 | No fee for publishing and inbox; Facebook and Instagram only |

**free-spreadsheet-alternatives**
| Tool | Stars | Reason |
|---|---|---|
| Google Sheets | 4.5 | Full formulas and collaboration; 15 GB shared storage, no Power Query |
| LibreOffice Calc | 5 | No subscription or feature limits |
| Zoho Sheet | 4 | Full formulas and collaboration; 5 GB storage |
| ONLYOFFICE Docs | 3.5 | Cloud free tier has storage and user limits |
| Airtable | 3 | 1,000 records per base, 5 editors, 100 automation runs |

**free-time-tracking-software**
| Tool | Stars | Reason |
|---|---|---|
| Clockify | 4 | Five users with unlimited projects; billing rates paid, one-month report range |
| Toggl Track | 4 | Up to five people with unlimited entries; billing and profitability paid |
| RescueTime Lite | 3 | Two weeks of history; blocking and goals paid |
| TimeCamp | 3.5 | Unlimited users but top-level projects only |
| Harvest | 2.5 | One seat and two active projects |

**free-visio-alternatives**
| Tool | Stars | Reason |
|---|---|---|
| draw.io | 5 | No paid tier, document cap, or watermark; all shape libraries |
| Lucidchart Free | 2 | Three documents of 75 shapes; Visio import paid |
| Miro Free | 2.5 | Three editable boards |
| Whimsical Free | 2.5 | 50 new objects a month and watermarked exports |

**free-website-builders**
| Tool | Stars | Reason |
|---|---|---|
| Wix | 3 | Full editor; Wix ads, subdomain, 1 GB bandwidth |
| Google Sites | 4 | No builder ads and free domain connection; fixed layouts |
| WordPress.com | 3 | Ads, subdomain, 1 GB, no plugins |
| Carrd | 3 | Three one-page sites; forms and domains paid |
| Canva Websites | 3 | Subdomain only; custom domain and insights need Pro |

**free-web-analytics**
| Tool | Stars | Reason |
|---|---|---|
| Google Analytics 4 | 5 | No pageview or seat cap |
| Google Search Console | 5 | Full search data for 16 months at no cost |
| Microsoft Clarity | 4.5 | No stated session cap; recordings can expire |
| Umami | 4.5 | Unlimited sites and pageviews self-hosted; you run the server |
| Matomo On-Premise | 4 | Core free with no data cap; funnels and heatmaps are paid plugins |

### Creative

**canva-alternatives**
| Tool | Stars | Reason |
|---|---|---|
| Adobe Express | 4 | Templates, basic photo and video tools, some Adobe Stock; premium assets, brand tools, and bulk resize paid |
| Photopea | 3.5 | Full layered editor with ads, but no stock library, brand controls, or template workflow |
| Microsoft Designer | 3.5 | AI drafts within usage limits; lighter manual layout |
| Pixlr | 3.5 | Ads and upgrade prompts; more AI tools paid |
| Picsart | 3 | Premium assets and upgrades promoted; weak for documents and brand layouts |

**figma-alternatives**
| Tool | Stars | Reason |
|---|---|---|
| Penpot | 4.5 | Eight members on hosted free plan, unlimited files within storage, free self-hosting |
| Lunacy | 4 | Free desktop app; ten cloud documents, 30-day history, attribution for bundled graphics |
| Plasmic | 3.5 | Unlimited projects, three collaborators |
| Quant UX | 3.5 | Free and open source, but prototyping only and no multiplayer editing |
| Figma Starter | 3 | Three shared files of three pages each |

**free-font-websites**
| Tool | Stars | Reason |
|---|---|---|
| Google Fonts | 5 | Every family open source and cleared for commercial use |
| Font Squirrel | 4.5 | Catalog picked for commercial use; smaller and download-only |
| DaFont | 3 | Many fonts are personal-use only, with unclear labels |
| Fontsource | 4.5 | Open-source families as npm packages; needs a build pipeline |
| 1001 Fonts | 3.5 | License labels per font, but a mixed catalog |

**free-stock-photos**
| Tool | Stars | Reason |
|---|---|---|
| Unsplash | 5 | Free commercial use without attribution or registration |
| Pexels | 5 | Photos and video under one free license |
| Pixabay | 4.5 | Broadest free media under one license; uneven quality and more ads |
| Burst | 4 | Free commercial use, but a small commerce-focused library |

**illustrator-alternatives**
| Tool | Stars | Reason |
|---|---|---|
| Inkscape | 5 | Full SVG editor with no paid tier; .ai files need a PDF or SVG step |
| LibreOffice Draw | 3 | Free, but path and illustration tools are shallow |
| SVG-edit | 2.5 | Free and offline, but basic shapes only and no layers |
| Canva free tier | 2 | No SVG export or path editing on free |

**photoshop-alternatives**
| Tool | Stars | Reason |
|---|---|---|
| Photopea | 4.5 | PSD editing with layers and masks; ads on free |
| GIMP | 4.5 | Full desktop editor with no paid tier; weak CMYK and non-destructive editing |
| Krita | 4 | Complete painting app; photo retouching is not its focus |
| Pixlr | 3.5 | Ads and upgrade prompts; AI features paid |

**freecad-alternatives**
| Tool | Stars | Reason |
|---|---|---|
| Onshape | 3.5 | Full parametric CAD, but every document is public and use is non-commercial |
| Autodesk Fusion | 3.5 | Ten active documents, non-commercial, some exports paid |
| Tinkercad | 3 | Free, but primitive-shape modeling without a feature tree |
| SolveSpace | 3.5 | GPL with no commercial limit; narrow feature set |
| OpenSCAD | 4 | GPL, full scripted modeling; no interactive sketching |
| LibreCAD | 3.5 | Complete free 2D drafting; no 3D |

**canva-free-vs-paid**
| Tool | Stars | Reason |
|---|---|---|
| Canva Free | 4 | Finishes most single projects; background removal at volume, Magic Resize, brand kits, and Content Planner are paid |

### Security

**best-free-2fa-apps**
| Tool | Stars | Reason |
|---|---|---|
| Aegis | 4.5 | Free, open source, encrypted local vault; Android only |
| Ente Auth | 5 | Free, open source, encrypted sync on every platform with an offline mode |
| 2FAS | 4.5 | Free with optional backup to iCloud or Google Drive; cross-platform moves need an export |
| Bitwarden TOTP | 1 | Requires Premium ($19.80 a year); Bitwarden Free has no TOTP |
| Authy | 3 | Free on mobile, but no token export and no desktop apps |

**free-antivirus-software**
| Tool | Stars | Reason |
|---|---|---|
| Microsoft Defender | 5 | Built into Windows with real-time and offline scans at no cost |
| Malwarebytes Free | 2.5 | On-demand scans only; real-time protection is paid |
| Avast Free | 4 | Real-time shields, core firewall, ransomware protection; advanced firewall paid |
| AVG Free | 4 | Same engine and free feature set as Avast |
| Bitdefender Free | 4 | Real-time and ransomware protection; Windows only, basic tier |

**free-password-managers**
| Tool | Stars | Reason |
|---|---|---|
| Bitwarden | 4.5 | Unlimited passwords and devices; TOTP, attachments, and emergency access paid |
| KeePassXC | 4.5 | No paid tier; sync and mobile access are up to you |
| Proton Pass | 4 | Unlimited logins and devices, two vaults, ten aliases; TOTP paid |
| NordPass | 2.5 | One active session at a time |

**free-password-managers-teams**
| Tool | Stars | Reason |
|---|---|---|
| Bitwarden Free Organizations | 2.5 | Two members and two collections |
| Vaultwarden | 4 | Unlimited users self-hosted; unofficial and community-supported |
| Passbolt Community Edition | 3.5 | Unlimited users self-hosted; mobile apps and SSO paid |
| KeePassXC shared vault | 2 | Free, but one shared master password, no user management, edit conflicts |

**free-vpn**
| Tool | Stars | Reason |
|---|---|---|
| Proton VPN Free | 4 | No data cap; no server choice, fewer simultaneous connections, no specialist servers |
| Windscribe Free | 3.5 | Country choice with 10 GB a month after email confirmation |
| TunnelBear Free | 2 | 2 GB a month and no country choice |

**free-security-audit-tools**
| Tool | Stars | Reason |
|---|---|---|
| OWASP ZAP | 5 | No paid scanner tier |
| Nmap | 5 | Full scanner and scripting engine at no cost |
| Lynis | 4.5 | Open-source client audits one host; central management is Enterprise |
| Nikto | 5 | Open-source scanner with all plugins |
| Greenbone Community Edition | 4 | Community feed without completeness warranty; commercial feed paid |
| SSL Labs and SecurityHeaders.com | 5 | Free with no account |

### Cloud

**dropbox-alternatives**
| Tool | Stars | Reason |
|---|---|---|
| MEGA | 4 | 20 GB with client-side encryption; variable transfer quota, link controls paid |
| Google Drive | 3.5 | Up to 15 GB shared with Gmail and Photos (5 GB until phone verification) |
| OneDrive | 3 | 5 GB that also holds Outlook.com attachments |
| Proton Drive | 3 | 2 GB at sign-up, 5 GB after three setup tasks |
| Box Free | 3.5 | 10 GB with a 250 MB upload limit |

**free-cloud-storage-comparison**
| Tool | Stars | Reason |
|---|---|---|
| MEGA | 4 | As in the Dropbox guide |
| Google Drive | 3.5 | As in the Dropbox guide |
| Box | 3.5 | As in the Dropbox guide |
| OneDrive | 3 | As in the Dropbox guide |
| Proton Drive | 3 | As in the Dropbox guide |
| iCloud | 2.5 | 5 GB shared with device backups and photos |
| Dropbox | 2 | 2 GB on Basic |

**free-backup-software** (Backblaze Personal Backup is the page's paid option and has no rating)
| Tool | Stars | Reason |
|---|---|---|
| Google Drive | 3 | Folder sync into up to 15 GB shared storage; not a full-system backup |
| Duplicati | 5 | Free, open-source scheduled encrypted backups to any destination |
| iCloud Backup | 2.5 | 5 GB shared, which may not fit one device |
| Duplicacy | 3.5 | Command-line edition free for personal use; GUI is licensed after a trial |

**free-ai-email-tools**
| Tool | Stars | Reason |
|---|---|---|
| Gmail Smart Compose and Smart Reply | 3.5 | No caps, but completions and short replies only; summaries need a paid plan |
| Compose AI | 2.5 | 1,500 generated words and 25 rephrases a month |
| ChatGPT free tier | 4 | Full drafting on the free plan; no inbox integration |
| Boomerang | 2.5 | 10 scheduling credits a month; advanced scores paid |
| Spike | 2 | 10 queries per AI feature and one address |

**free-email-service**
| Tool | Stars | Reason |
|---|---|---|
| Gmail | 4.5 | Up to 15 GB shared; custom domains paid |
| Proton Mail | 3 | 1 GB, one address, daily sending limit |
| Outlook.com | 4 | 15 GB mailbox; ads on free accounts |
| Zoho Mail | 3.5 | Custom domain for five users at 5 GB each; web and mobile only |
| Tuta | 3 | 1 GB and one address |

**free-email-signature**
| Tool | Stars | Reason |
|---|---|---|
| HubSpot Email Signature Generator | 4.5 | Unlimited, no account, no branding; nothing saved |
| MySignature | 3 | One saved signature with a promotional badge |
| WiseStamp | 1 | 14-day trial, no free version |
| Newoldstamp | 1 | Seven-day evaluation; signatures cannot be used before upgrading |
| Signature Maker | 4 | Unlimited with no account or branding; basic templates |

**free-team-email**
| Tool | Stars | Reason |
|---|---|---|
| Zoho Mail | 3.5 | Five custom-domain users at 5 GB; no IMAP |
| Spike Teamspace | 2.5 | Three members on a spike.team domain; no custom domain |
| Proton Mail Free | 2 | One personal inbox per account; no domain or team admin |
| Tuta | 2 | One personal inbox per account; no domain or team admin |
| Gmail delegate access | 2.5 | Up to ten delegates on one inbox, with no queue or assignment |

### Video

**free-open-source-video-editors**
| Tool | Stars | Reason |
|---|---|---|
| Kdenlive | 4.5 | No paid tier; full multi-track editor with proxies; no auto-captions or advanced grading |
| Shotcut | 4 | No paid tier; limited color tools and a harder timeline |
| OpenShot | 3.5 | No paid tier; limited proxy, color, and audio tools on heavy projects |
| Blender VSE | 3.5 | Free, but slow going as a primary editor |
| Olive | 2 | Pre-release; files from earlier versions have had compatibility issues with later builds |

**free-screen-recording-software**
| Tool | Stars | Reason |
|---|---|---|
| OBS Studio | 5 | No time cap, watermark, or paid tier |
| ShareX | 4.5 | No watermark or time limit; Windows only |
| Loom Free | 2 | Five minutes per video and 25 videos |
| Screencastify | 2 | Ten videos of 30 minutes, watermarked |
| Clipchamp | 4 | 30 minutes per clip, 1080p export, no watermark |

**free-video-editing-software**
| Tool | Stars | Reason |
|---|---|---|
| DaVinci Resolve | 4.5 | No watermark; 8-bit formats up to UHD 60 fps, AI tools in Studio |
| CapCut Desktop | 3.5 | Plain edits export clean; templates and stock can add a watermark |
| OpenShot | 3.5 | As in the open-source guide |
| Kdenlive | 4.5 | As in the open-source guide |
| Shotcut | 4 | As in the open-source guide |

**premiere-pro-alternatives**: same five editors and ratings as free-video-editing-software.

**zoom-alternatives**
| Tool | Stars | Reason |
|---|---|---|
| Google Meet | 4 | 100 people for 60 minutes, 24-hour one-to-one calls; recording paid |
| Jitsi Meet | 4 | No published time or participant limit; no recording, quality drops with large groups |
| Microsoft Teams free | 4 | 100 people for 60 minutes; recording paid |
| Discord | 4 | No duration cap; 25 video participants at 720p |
| Whereby | 2 | One room, four participants, 30 minutes |

**free-video-conferencing**
| Tool | Stars | Reason |
|---|---|---|
| Google Meet | 4 | As in the Zoom guide |
| Jitsi Meet | 4 | As in the Zoom guide |
| Microsoft Teams Free | 4 | As in the Zoom guide, plus 5 GB storage |
| Whereby | 2 | As in the Zoom guide |
| Zoho Meeting | 4 | 100 people for 60 minutes, polls, 20-attendee webinars; recording paid |
| Discord | 4 | As in the Zoom guide |

**free-video-editing-mac**
| Tool | Stars | Reason |
|---|---|---|
| iMovie | 4 | Free with 4K export; no multicam, proxies, or plugins |
| DaVinci Resolve | 4.5 | As in the video editing guide |
| CapCut Desktop | 3.5 | As in the video editing guide |
| Kdenlive | 4.5 | As in the open-source guide |
| Shotcut | 4 | As in the open-source guide |

