# Research notes: illustrator-alternatives

Audit date: 2026-10-26
Article: `content/creative/illustrator-alternatives.md`

Brief
- Scope: High-impression page: correct import/export and offline claims without changing rankings.
- Reader: comparing useful free software and its upgrade boundaries.
- Preserve: article structure, rankings, publication date, URLs, images, legitimate screenshot evidence, affiliate and advertising behavior.
- Method: opened original official sources; this is a risk-based claim check, not verification of every sentence.

| Product | Exact existing claim or table text | Verified finding | Official source | Checked date | Classification | Decision | Status |
|---|---|---|---|---|---|---|---|
| Inkscape | but it cannot open native .ai files. | Official guide lists Illustrator9+ (*.ai) import; PDF-compatible AI files can open, but native AI export is not supported. | https://inkscape-manuals.readthedocs.io/en/latest/import-other-formats.html | 2026-10-26 | Confirmed outdated | Narrow description and body to import limits and lack of native AI export | Narrowed |
| Inkscape | Illustrator files must be exported as PDF or SVG first | Current source registers .ai using the PDF importer (AI Input, lines851-864). A separate export is not always necessary; PDF-compatible AI files can open directly. | https://gitlab.com/inkscape/inkscape/-/raw/master/src/extension/internal/pdfinput/pdf-input.cpp | 2026-10-26 | Confirmed outdated | Correct the bullet and migration paragraph; keep compatibility caveats | Narrowed |
| SVG-edit | No layer management | Official LayersPanel code wires creation, deletion, renaming, movement, cloning and merging layers. | https://github.com/SVG-Edit/svgedit/blob/master/src/editor/panels/LayersPanel.js | 2026-10-26 | Confirmed outdated | Replace with plain statement that layers are supported; retain simpler-editor boundary | Confirmed |
| Canva Free | \| Canva Free \| Shapes only \| No \| No \| PNG, JPEG, PDF \| Non-designer templates \| | US pricing explicitly lists Canva Offline under Free; capability completeness and platform exclusions not established. | https://www.canva.com/pricing/?countryCode=us | 2026-10-26 | Confirmed outdated | Correct Offline cell narrowly to limited offline support, no blanket full offline promise | Narrowed |
| Affinity | Canva now gives away free to individuals on Mac and Windows | Official site confirms free individual version, both desktop platforms and AI/PSD import. | https://www.affinity.studio/ | 2026-10-26 | Confirmed current | No change | Confirmed |
| Adobe Illustrator | $22.99 a month, annual plan billed monthly | Opened plans page rendered Japanese yen despite English URL; US amount not independently reverified. | https://www.adobe.com/products/illustrator/plans.html | 2026-10-26 | Unverifiable for US price | Needs manual verification; no price replacement | Needs evidence |

Research gaps
- Inkscape main FAQ returned403; official guide and current source were accessible. Old Current_PDF_Support wiki is marked outdated and is not the basis for current publication.
- Update docs/RATINGS.md Inkscape/SVG-edit reasons with lead ownership; scores can remain5 and2.5 because SVG-edit remains a basic editor.
- Search all content for Inkscape AI claims, SVG-edit no-layers claims and Canva offline claims.

Editorial handoff
- Only Confirmed or Narrowed rows support a correction. Needs evidence rows remain unresolved; no replacement fact is authorized.
- Review changed sentences and related tables under website-content-humanizer.md before publication.
