---
Project: Plating Posters Inc
Document Type: Series Standards — Reference
Status: Active — updated as standards are locked
Created: 2026-03-16T00:00:00
Updated: 2026-04-03T00:00:00
Author: Alaina (poster-designer)
tags:
  - PosterDesign
  - SeriesStandards
  - PlatingPosters
---

# Plating Posters Inc — Series Design Standards

*This document captures every series-wide design decision as it is locked. It is the authoritative reference for any new poster entering development. Before drafting any design brief, check this file and apply the locked standards without re-litigating them. Flag any proposed deviation to Drew.*

*Maintained by Alaina — last updated 2026-04-03.*

---

## Locked Standards Index

| Standard | Status | Locked Date | Section |
|----------|--------|-------------|---------|
| Product framing | LOCKED | 2026-03-14 | 1.1 |
| Visual direction | LOCKED | 2026-03-14 | 1.2 |
| Dual editions (Dark + Light) | LOCKED | 2026-03-14 | 1.3 |
| One process per poster | LOCKED | 2026-03-14 | 1.4 |
| Illustration approach | LOCKED | 2026-03-18 (updated from 2026-03-14) | 1.5 |
| Primary design tool — Claude Chat | LOCKED | 2026-04-20 (updated from 2026-03-18) | 2.1 |
| Print resolution standard | LOCKED | 2026-03-14 | 2.2 |
| Standard poster sizes | LOCKED | 2026-03-14 | 2.3 |
| Readability target | LOCKED | 2026-03-14 | 2.4 |
| Color palette — full series | LOCKED | 2026-03-16 | 3 |
| Typography — full series | LOCKED | 2026-03-16 | 4 |
| Page structure and element conventions | LOCKED | 2026-04-03 | 5 |
| Export file convention | LOCKED | 2026-03-16 (updated 2026-04-03) | 6 |
| Accessibility minimum | LOCKED | 2026-03-14 | 7 |
| Production workflow pipeline | LOCKED | 2026-04-03 | 8 |
| Logo placement | PENDING | — | 9 |

---

## 1. Series Rules (All Locked 2026-03-14 unless noted)

### 1.1 Product Framing

Every poster is a **sellable product** — physical print AND digital download. Design for both from the start. Posters are not internal-use-only materials; they are items a plating shop purchases and displays.

Drew's framing: "a given poster may not make the boardroom but it should be a product offering." Every concept receives full product-quality treatment regardless of its intended wall location.

### 1.2 Visual Direction

**Polished and boardroom-quality, with a functional reference layer.**

The benchmark: something you would be proud to hang in an executive conference room that a process engineer would also actually reach for and use. This is not purely decorative, and not purely utilitarian. Both bars must be cleared on every poster.

Two failure modes to avoid:
- Pretty-but-useless infographic (visual without substance)
- Technically dense but visually ugly reference sheet (substance without craft)

### 1.3 Dual Editions — Dark and Light

Every poster is produced in both a **Dark edition** (flagship) and a **Light edition** (accessible print). No exceptions.

- **Dark edition:** premium aesthetic; recommended for professional printing and boardroom display; designed first (master design)
- **Light edition:** accessible print; same layout, same content, same illustrations; color palette remapped for home/office printer compatibility; produced by recoloring every element per the Dark-to-Light remap table (Section 3)

Export standard: **six files per poster** (Dark + Light, each in 24x36" print, 18x24" print, and digital PDF).

### 1.4 One Process Per Poster

Each poster covers exactly one plating process. No mixing of processes on a single poster.

If content from two processes is both relevant and valuable, the answer is two posters — not one crowded poster. This rule allows future "editions" per process (nickel edition, acid zinc edition, EN edition, etc.) as distinct sellable products.

Apply at the concept stage — do not draft content that crosses process lines, even as a "secondary reference."

### 1.5 Illustration Standard — UPDATED 2026-03-18

All technical illustrations are **built from simple geometric shapes** — layered rectangles, lines, arrows, rounded rectangles, and standard icon sets. No external photo reference, no raster source art, no stock photography.

**Geometric build approach:** Validated on Poster #4 (Hull cell panel as layered rectangles with gradient overlays) and Poster #10 (U-channel cross-section as layered rectangles for deposit thickness). All illustrations to date have been successfully built as composites of geometric shapes. This approach provides full editorial control, visual consistency across the series, and no licensing complications.

**Complex illustrations:** If a future poster requires illustration complexity beyond simple shapes, create the illustration in Inkscape (free, open-source SVG editor) and incorporate into the generated output. This fallback has not yet been needed — evaluate per poster.

The same illustration elements are shared between Dark and Light editions — colors are recolored per the remap table; shapes do not change.

*Historical note: This standard originally specified Affinity Designer (2026-03-14), then Canva (2026-03-18). Updated to Claude Chat generation on 2026-04-20. The design decision (all geometric, no stock imagery) is unchanged — only the tool changed.*

---

## 2. Technical Production Standards (All Locked 2026-03-14 unless noted)

### 2.1 Primary Design Tool — UPDATED 2026-04-20

**Claude Chat (visual artifact generation)** — all posters are generated as SVG or HTML visual artifacts in claude.ai chat. Drew generates each poster from Alaina's Construction Workup, with Elara engineering the generation prompt.

Required fonts (specified in generation prompts):
- Barlow Condensed, Barlow, Inter, JetBrains Mono (all from Google Fonts, free)

**Supplementary tools:**
- Inkscape: fallback for complex vector illustrations that exceed generation capabilities (not yet needed)
- GIMP: valid for raster photo editing tasks if poster content ever requires photographic elements (not currently used)

*Historical note: This standard originally specified Affinity Designer (2026-03-14), then Canva (2026-03-18). Production workflow confirmed Claude Chat generation on 2026-04-20. All locked design decisions (palette, typography, layout conventions) remain unchanged — only the build tool changed.*

### 2.2 Print Resolution

**300 DPI minimum** at final output size. No exceptions for print-ready files.

Generated artifacts should be exported at 300 DPI for print-ready files.

Digital (screen) exports: RGB color mode; standard quality PDF or PNG at screen resolution is appropriate.

### 2.3 Standard Poster Sizes

Both sizes are produced for every poster:
- **24x36"** (609.6 x 914.4 mm) — primary; master design built at this size
- **18x24"** (457.2 x 609.6 mm) — secondary; produced by scaling the 24x36" design proportionally, then verifying text sizes meet minimum floors

Design at exactly 24 inches wide by 36 inches tall. For the 18x24" version, scale proportionally and verify all text against the type scale minimums.

Bleed: 0.125" (3.175 mm) all sides on print files. Include crop marks and bleed on print exports.
Safe zone for text and graphics: 0.5" (12.7 mm) inside trim edge.

### 2.4 Readability Target

All text and diagram labels must be **legible from 3-8 feet** at finished print size.

- Headline and section labels: primary 3-8 foot read-from-wall elements
- Table body text and callout text: readable at 4-6 feet; closer approach is acceptable for detailed reference
- Minimum body text on 24x36": 18-20 pt (approximately 7mm character height at print — comfortably readable at 4 feet)
- Scale 18x24" type proportionally at ~75%; body text floor: 14 pt minimum

---

## 3. Color Palette — LOCKED 2026-03-16

*Approved by Drew 2026-03-16. Applied beginning with Poster #4. Use these values on every subsequent poster.*

*Rationale: Gunmetal Dark background with Amber/Teal/Emerald/Coral accent system — conveys industrial precision and technical credibility without heaviness; the dark background gives the poster premium presence on a shop wall; accent colors map to functional roles (warm = HCD/warning, cool = LCD/coverage, green = positive, red = problem) rather than arbitrary decoration.*

### Dark Edition Palette

| Role | Color Name | Hex | Typical Use |
|------|------------|-----|-------------|
| Background | Gunmetal Dark | `#1A1F2E` | Full artboard background; inverted as primary text in Light edition |
| Primary text | Warm White | `#F0EDE8` | All body text, table content, callout body text |
| Illustration base — metallic | Bright Silver | `#C8D0D8` | Hull cell panel surface; zinc deposit representation; unchanged in Light edition |
| HCD accent / Warning | Amber | `#E8A020` | HCD zone; table section headers; subheadings; chemistry-drift row borders |
| LCD accent / Coverage | Teal | `#2EC4B6` | LCD zone; callout box borders and titles; positive structural elements |
| Positive reference | Emerald | `#27AE60` | "Good bath" / positive reference row left-border accents |
| Problem / Contamination | Coral | `#E05C5C` | Contamination problem row left-borders; critical alert elements |
| Table rules / Dividers | Mid Slate | `#3A4055` | Table row rules, column rules, horizontal section dividers |
| Footer strip | Deep Navy | `#0D1020` | Footer band background |
| Callout box backgrounds | Dark Callout | `#1E2435` | Interior fill of all callout boxes |
| Alternate table rows | Alt Row | `#252B3D` | Even-numbered data rows (base rows use `#1A1F2E`) |

### Light Edition Palette

| Role | Color Name | Hex | Notes |
|------|------------|-----|-------|
| Background | Off-White | `#F5F4F0` | |
| Primary text | Charcoal | `#1A1F2E` | Same hex as Dark BG — intentional inversion |
| Illustration base — metallic | Bright Silver | `#C8D0D8` | Unchanged — panel is always metallic |
| HCD accent | Amber Dark | `#C8860A` | Darkened for contrast on light background |
| LCD accent | Teal Dark | `#1A8C82` | Darkened for contrast on light background |
| Positive reference | Forest Green | `#1E7A47` | Darkened for contrast |
| Problem / Contamination | Deep Coral | `#B83E3E` | Darkened for contrast |
| Table rules / Dividers | Light Slate | `#D0D4DE` | |
| Footer strip | Charcoal | `#1A1F2E` | |
| Callout box backgrounds | Light Callout | `#ECEEF4` | |
| Alternate table rows | Alt Row Light | `#E8E8F0` | |

### Color Remap Table (Dark to Light)

Producing the Light edition requires recoloring every element per this table. Work from top to bottom — background first, then text, then fills, then accents.

| Dark Hex | Light Hex | Notes |
|----------|-----------|-------|
| `#1A1F2E` | `#F5F4F0` | Background and all BG-colored elements |
| `#F0EDE8` | `#1A1F2E` | All primary text |
| `#1E2435` | `#ECEEF4` | Callout box fills, row label column fills |
| `#252B3D` | `#E8E8F0` | Alternate table row backgrounds |
| `#0D1020` | `#1A1F2E` | Footer strip background |
| `#E8A020` | `#C8860A` | Amber accent elements |
| `#2EC4B6` | `#1A8C82` | Teal accent elements |
| `#27AE60` | `#1E7A47` | Emerald accent elements |
| `#E05C5C` | `#B83E3E` | Coral accent elements |
| `#3A4055` | `#D0D4DE` | Table rules, dividers, substrate shapes |
| `#C8D0D8` | `#C8D0D8` | Bright Silver — **unchanged** |

**Light edition color override (discovered on Poster #10):** When accent colors (Amber, Teal, Coral) are used as column header *fills* with dark text on them, the standard text remap (`#F0EDE8` to `#1A1F2E`) works correctly. However, when Amber is used as a column header fill on the Light edition, the darkened Amber (`#C8860A`) may have insufficient contrast with `#1A1F2E` text. In those cases, keep the header text as `#F0EDE8` (Warm White) in the Light edition instead of remapping it. Check WCAG contrast at layout time for each accent-fill header.

### Accessibility

- Dark edition: `#F0EDE8` on `#1A1F2E` = ~13:1 contrast ratio — exceeds WCAG AAA (7:1)
- Light edition: `#1A1F2E` on `#F5F4F0` = ~15:1 contrast ratio — exceeds WCAG AAA
- All information conveyed by color must have a secondary indicator (icon, label, position, or pattern) — never rely on color alone

### Color Mode Notes

- Design in RGB throughout production (Claude Chat generates RGB output)
- For print PDF export: export a high-quality RGB PDF at 300 DPI; professional print services can convert to CMYK from this file. If CMYK is specifically required, discuss with the printer
- Verify Amber (`#E8A020`) and Teal (`#2EC4B6`) at first print proof — both are moderately saturated and should convert cleanly, but check the first physical proof before committing to print runs

---

## 4. Typography — LOCKED 2026-03-16

*Option A approved by Drew 2026-03-16. Applied beginning with Poster #4. Use these fonts on every subsequent poster.*

*Rationale: Barlow Condensed's industrial character and distance readability make it ideal for the headline role; Inter's exceptional legibility at small sizes handles the data-dense body text; JetBrains Mono signals technical precision in tables and parameter lists without being inaccessible. All fonts are free and openly licensed.*

### Font Stack

| Role | Font | Weight | Source |
|------|------|--------|--------|
| Poster headlines | Barlow Condensed | ExtraBold | Google Fonts (free) |
| Subheadings / Section labels | Barlow | SemiBold | Google Fonts (free) |
| Body text / Diagnostic tables | Inter | Regular / Medium | Google Fonts (free) |
| Data tables / Parameters | JetBrains Mono | Regular | Google Fonts / JetBrains (free) |

### Font Availability

All four font families are available free from Google Fonts (fonts.google.com). Generation prompts specify these fonts by name; Claude Chat will render them in SVG/HTML output.

**Fallback:** If a font does not render correctly in a generated artifact, substitute Courier Prime for JetBrains Mono. There is no adequate substitute for Barlow Condensed — flag to Drew if issues arise.

### Type Scale — 24x36" Artboard

| Element | Size | Font | Weight |
|---------|------|------|--------|
| Poster headline | 96-120 pt | Barlow Condensed | ExtraBold |
| Poster subheading | 42-48 pt | Barlow | SemiBold |
| Section subheading | 36-42 pt | Barlow | SemiBold |
| Table section title | 28-32 pt | Barlow | SemiBold |
| Table header row | 22-24 pt | Barlow / Inter | SemiBold |
| Table body text | 18-20 pt | Inter | Regular |
| Callout box title | 24-28 pt | Barlow | SemiBold |
| Callout box body | 18-20 pt | Inter | Regular |
| Parameter table data | 18-20 pt | JetBrains Mono | Regular |
| Diagram zone labels | 24-28 pt | Barlow Condensed | ExtraBold |
| Diagram sub-labels | 16-18 pt | JetBrains Mono | Regular |
| Footer series name | 16-18 pt | Barlow | SemiBold |
| Footer disclaimer | 11-12 pt | Inter | Regular / Light |
| Version / date | 11-12 pt | JetBrains Mono | Regular |

### Scale to 18x24"

Reduce all sizes proportionally at ~75%. Absolute minimums:
- Body text: 14 pt floor
- Disclaimer: 9 pt floor
- Zone sub-labels: 12 pt floor

### Typography Notes

- Barlow Condensed headline: use tight letter spacing (approximately -3 to -5) — the font is designed for this and it improves density and readability at distance
- Inter body text: set line height at 1.4-1.5 (140-150%) for comfortable reading across multi-line table cells
- JetBrains Mono: use for all numerical data, parameter values, version numbers, and any content where character-level precision matters visually
- Do not introduce additional fonts in any poster — the four-font stack is the complete system
- **Sub/superscript characters:** For chemical formulas, use Unicode subscript/superscript characters directly (e.g., Ni2+ as Ni²⁺, H2O as H₂O). Provide these characters verbatim in Content and Layout Drafts so Drew can copy-paste.

---

## 5. Page Structure and Element Conventions — LOCKED 2026-04-03

*Established through production of Posters #4 and #10. Replaces the former Affinity Designer layer convention (Section 5, locked 2026-03-16). All subsequent posters must follow these conventions for consistency and maintainability.*

### Page Setup

Every poster begins with:
1. Design canvas: 24 inches wide x 36 inches tall
2. Page background color: `#1A1F2E` (Gunmetal Dark) for the Dark edition
3. Fonts specified per Section 4
4. All series palette colors per Section 3
5. Safe zone margins and zone boundaries per the poster's Construction Workup

### Zone-Based Build Order

Every poster is organized into sequential horizontal zones, built from top to bottom.

Established zone conventions (may vary slightly per poster):
- **Zone 1 — Header Band:** Poster headline + subheading (left ~60%) + orientation/context callout box (right ~40%)
- **Zone 2 — Hero Illustration:** Full-width technical illustration — the poster's primary visual anchor
- **Zone 3 — Hero Data Table:** Full-width data table or comparison chart — the poster's primary reference payload
- **Zone 4 — Secondary Data / Callouts:** Two-column split for supporting parameter tables, gauges, protocol callouts, or decision guides
- **Zone 5 — Applications / Context:** Industry applications, specification references, or contextual information
- **Zone 6 — Footer Band:** Deep Navy `#0D1020` band with poster title, series name, disclaimer, logo placeholder, and version

**Build rule:** Complete one zone before moving to the next. Group each zone logically after completing it.

### Element Grouping Conventions

Use element grouping and naming to maintain organization:

- **Group by zone:** Name each zone descriptively (e.g., "Zone 1 - Header", "Zone 3 - P% Table").
- **Group by block within zones:** Complex zones should have sub-groups (e.g., "Block D - P% Table", "Block E - Bath Parameters").

### Common Element Patterns (Established Across Two Posters)

**Table construction:**
- Build tables as manually constructed grids of rectangles + text boxes for full styling control
- Header row: `#3A4055` Mid Slate fill with Amber or Warm White text
- Alternating data rows: base `#1A1F2E` / alternate `#252B3D`
- Left-border accent: narrow colored rectangle (approximately 0.06" wide / 4 pt equivalent) flush against the left edge of the row rectangle

**Callout boxes:**
- Rounded rectangle: fill `#1E2435` (Dark Callout), border stroke 1.5 pt in accent color (typically Teal `#2EC4B6`), corner radius 8 pt
- Internal padding: 20 pt from all edges
- Title: Barlow SemiBold, accent-colored
- Body: Inter Regular, `#F0EDE8`

**Section labels:**
- Barlow Condensed ExtraBold or Barlow SemiBold
- Amber `#E8A020` or Warm White `#F0EDE8`
- ALL CAPS for primary section labels

**Footer band:**
- Rectangle fill: `#0D1020` Deep Navy
- Height: approximately 2.2-3.6" depending on poster content density
- Left: poster title (Barlow SemiBold, 16-18 pt)
- Center: series name (Inter Regular, 14-15 pt, 70% opacity)
- Right: logo placeholder `[LOGO]`
- Disclaimer: Inter Regular, 11-12 pt, 50% opacity
- Version: JetBrains Mono Regular, 11 pt, 50% opacity

### Light Edition Production Workflow

1. Complete the Dark edition fully — verify all text, element positions, and colors
2. Duplicate the Dark edition design
3. Work through the Color Remap Table (Section 3) from top to bottom
4. Begin with the page background color, then text elements, then fills, then accents
5. Check every accent-fill header for WCAG contrast compliance — apply overrides where needed (see Light Edition Color Override note in Section 3)
6. Verify: no element should remain in its Dark edition color after the remap is complete

---

## 6. Export File Convention — LOCKED 2026-03-16 (updated 2026-04-20)

Six files per poster, every time.

| File Name Pattern | Mode | Quality | Bleed + Marks | Size |
|-------------------|------|---------|---------------|------|
| `[Title] — Dark — 24x36 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes (crop marks and bleed) | 24x36" |
| `[Title] — Dark — 18x24 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes | 18x24" |
| `[Title] — Dark — Digital.pdf` | RGB | PDF Standard | No | 24x36" |
| `[Title] — Light — 24x36 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes | 24x36" |
| `[Title] — Light — 18x24 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes | 18x24" |
| `[Title] — Light — Digital.pdf` | RGB | PDF Standard | No | 24x36" |

**Export steps:**
1. Export the generated artifact (SVG/HTML) to PDF at 300 DPI for print files
2. Include crop marks and bleed for print files only
3. Name per the naming convention above

**PNG alternative:** For digital distribution where PDF is not preferred, export as PNG at the highest available resolution. Name pattern: `[Title] — Dark — Digital.png` / `[Title] — Light — Digital.png`.

**CMYK note:** Generated artifacts are RGB. If a print vendor requires CMYK PDF, convert post-export using a free tool (e.g., Scribus, GIMP with CMYK plugin, or the printer's own conversion service). Most modern digital and offset print services accept high-quality RGB PDF.

Example for Poster #4:
- `Hull Cell Panel — Dark — 24x36 — Print.pdf`
- `Hull Cell Panel — Dark — 18x24 — Print.pdf`
- `Hull Cell Panel — Dark — Digital.pdf`
- `Hull Cell Panel — Light — 24x36 — Print.pdf`
- `Hull Cell Panel — Light — 18x24 — Print.pdf`
- `Hull Cell Panel — Light — Digital.pdf`

---

## 7. Accessibility Minimum — LOCKED 2026-03-14

- WCAG AA contrast minimum (4.5:1) for all text on background — WCAG AAA (7:1) is the target
- No information conveyed by color alone — always add a secondary indicator (icon, label, border, position)
- Verify accent colors against their specific background at layout time — especially after Light edition color remapping
- Icons are used as secondary indicators alongside text labels, never as the sole carrier of information

---

## 8. Production Workflow Pipeline — LOCKED 2026-04-03

*Confirmed through production of Posters #4 and #10. This is the end-to-end pipeline for every poster.*

### Pipeline Stages

| Stage | Owner | Output |
|-------|-------|--------|
| 1. Watson Research Brief | Watson | Technical research document — design input for Alaina |
| 2. Content and Layout Draft | Alaina | All poster copy, zone map, block specifications — authoritative content source |
| 3. Construction Workup | Alaina | Build instructions and design specifications — input for Elara |
| 4. Generation Prompt | Elara | Engineered prompt translating workup into Claude Chat generation instructions |
| 5. Claude Chat Generation (Dark edition) | Drew | Dark edition poster generated as SVG/HTML artifact |
| 6. Light Edition Remap | Drew | Duplicated design with color remap |
| 7. Review and Revision | Drew + Alaina | Visual review, text verification, layout adjustments |
| 8. Six-File Export | Drew | Print + digital PDFs per Section 6 |
| 9. Final Validation | Alaina | Design standards compliance check |

### Document Naming Convention

- Content and Layout Draft: `Poster [#] — [Short Title] — Content and Layout Draft.md`
- Construction Workup: `Poster [#] — [Short Title] — Construction Workup.md`
- Generation Prompt: `Poster [#] — [Short Title] — Generation Prompt.md`

### Content Authority Rule

If any discrepancy exists between the Content and Layout Draft and the Construction Workup, the **Content and Layout Draft governs** for all text content. The Workup governs for build instructions and element positioning.

---

## 9. Logo Placement — PENDING

Logo position and treatment are not yet locked. All posters to date use a `[LOGO]` placeholder in the bottom-right corner of the footer strip (60 pt x 30 pt box, `#3A4055` fill).

Expected decision: bottom-right corner of the footer strip. Confirm when Plating Posters Inc brand identity is established.

---

## Version History

| Date | Change |
|------|--------|
| 2026-03-14 | Series rules and production standards locked (Sections 1-2, 7) |
| 2026-03-16 | Color palette locked (Section 3). Typography locked (Section 4). Layer convention locked (Section 5). Export file convention locked (Section 6). Document created. |
| 2026-03-18 | Primary design tool updated from Affinity Designer to Canva (Section 2.1). Illustration standard updated to geometric build approach (Section 1.5). *(Historical: Canva was later replaced by Claude Chat on 2026-04-20.)* |
| 2026-04-03 | Major revision for production workflow consistency. Section 5 rewritten: page structure and element conventions (validated across Posters #4 and #10). Section 6 updated with export steps. Section 8 added: Production Workflow Pipeline locked. Color remap table updated with workflow and Light edition override note. Typography notes updated with letter spacing and Unicode sub/superscript guidance. All existing LOCKED decisions preserved with original dates. |
| 2026-04-20 | Canva references removed throughout. Primary design tool updated to Claude Chat (visual artifact generation). All Canva-specific instructions replaced with tool-agnostic or Claude Chat-specific language. File naming conventions updated (Canva Construction Workup -> Construction Workup, Canva Build Prompt -> Generation Prompt). |
