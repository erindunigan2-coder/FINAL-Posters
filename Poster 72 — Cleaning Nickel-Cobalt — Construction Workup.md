---
Project: Plating Posters Inc
Poster Number: 72
Title: "Cleaning -- Nickel-Cobalt"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-06 technical reference (nickel-cobalt alloy plating)"
Technical Source: Cleaning stage for nickel-cobalt alloy plating. Same cleaning requirements as Watts/sulfamate nickel -- alkaline soak clean, electrocleaner, and solvent degrease options. Aerospace substrates (Inconel, Waspaloy, titanium) may require specialized pre-cleaning. Stage 1 of 8.
Process Scope: Cleaning for nickel-cobalt alloy plating (Stage 1 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - NickelCobaltPlating
  - Cleaning
  - ConstructionWorkup
  - Series2
  - ClusterEP06
---

# Poster #72 -- Construction Workup
## Cleaning -- Nickel-Cobalt

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 1 of 8. Cleaning for NiCo plating follows the same principles as any nickel process -- the substrate must be oil-free, oxide-free, and water-break-free before moving forward. The twist with NiCo is the substrate mix: aerospace parts are often Inconel, Waspaloy, titanium, or hardened steel -- materials that demand more aggressive cleaning and specific electrocleaner polarities.

Hero visual: a cleaning tank cross-section showing immersion cleaning with agitation, with callout labels for chemistry, temperature, and contamination sources.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Cleaning tank cross-section hero (Block B):** Large tank with parts immersed, agitation arrows, contamination labels (oil film, shop soil, machining compound). Built with rectangles, lines, and text labels.
2. **Cleaning methods comparison (Block D):** Three-column layout comparing soak clean, electrocleaner, and solvent/vapor degrease.
3. **Substrate decision table (Block E):** Which cleaning method for which substrate -- steel, Inconel, titanium.
4. **Common cleaning failures (Block F):** 4-card strip.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts per series design system.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 1 highlighted (Teal)
ZONE 3 -- CLEANING TANK HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- CLEANING METHODS COMPARISON (14.5"--20.5" / ~6.0")
ZONE 5 -- SUBSTRATE DECISION TABLE (20.5"--26.5" / ~6.0")
ZONE 6 -- COMMON CLEANING FAILURES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CLEANING` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Nickel-Cobalt Plating -- Stage 1 of 8` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `No shortcut exists. Skip the clean, ruin the deposit. Aerospace substrates demand aerospace-grade preparation.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Y: 2.9" to 4.2".

Eight mini boxes in a row. Stage 1 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed: fill `#252B3D`, text `#F0EDE8` at 40%.

Below: `Before: Raw substrate with oils, oxides, shop soil  -->  After: Water-break-free surface ready for activation`

Inter Medium, 14 pt, `#F0EDE8` at 60%.

---

### ZONE 3 -- Cleaning Tank Hero

**Section label:** `THE ALKALINE SOAK CLEAN` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Tank Cross-Section**

Y: 5.0" to 14.0".

**Tank body:**
- Rounded rect, X: 1.5", Y: 5.5", W: 21.0", H: 7.0"
- Fill: `#252B3D` (cleaning solution)
- Border: 3 pt `#2EC4B6`

**Parts rack (center):**
- Vertical rect, X: 10.0", Y: 6.0", W: 4.0", H: 5.5", fill `#C8D0D8` at 30%, border 2 pt `#C8D0D8`
- Label above: `PARTS (RACKED)` Barlow SemiBold 14 pt `#F0EDE8`
- Sub-label: `Turbine blades, housings, mold inserts` Inter Regular 12 pt `#F0EDE8` at 60%

**Contamination labels (left side, X: 2.5"):**
- Arrow pointing to part surface: `Machining oil` Inter Medium 13 pt `#E05C5C`
- Arrow pointing to part surface: `Shop soil / fingerprints` Inter Medium 13 pt `#E05C5C`
- Arrow pointing to part surface: `Oxide film` Inter Medium 13 pt `#E8A020`

**Agitation arrows (bottom of tank):**
- 4 upward curved arrows, stroke 2 pt `#2EC4B6`, dashed
- Label: `Air or mechanical agitation` Inter Regular 12 pt `#2EC4B6`

**Bath parameter labels (right side, X: 15.0", Y: 7.0"):**
- `Concentration: 4--8 oz/gal (30--60 g/L)` JetBrains Mono 14 pt `#2EC4B6`
- `Temperature: 140--180 F (60--82 C)` JetBrains Mono 14 pt `#F0EDE8`
- `Time: 3--10 min (soak)` JetBrains Mono 14 pt `#F0EDE8`
- `pH: 12--14` JetBrains Mono 14 pt `#F0EDE8` at 70%
- `Type: Non-silicated alkaline` JetBrains Mono 13 pt `#E8A020`

**Heater element (bottom-left):**
- Small rect, X: 2.5", Y: 12.0", W: 3.0", H: 0.4", fill `#E8A020` at 30%, border 1 pt `#E8A020`
- Label: `Heater -- maintain 140--180 F` Inter Regular 11 pt `#E8A020`

**Bottom callout (Y: 13.5"):**
- `The water-break test is your only reliable indicator. If the rinse water sheets evenly off the part, you are clean. If it beads -- go back.` Inter Medium 14 pt `#2EC4B6`

---

### ZONE 4 -- Cleaning Methods Comparison

**Section label:** `THREE CLEANING METHODS -- KNOW YOUR OPTIONS` -- Y: 14.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK D -- Three-Column Comparison (Y: 15.3" to 20.3")**

Three side-by-side callout boxes:

| Method | X | W | Accent | Title |
|---|---|---|---|---|
| Alkaline Soak Clean | 0.5" | 7.33" | `#2EC4B6` | SOAK CLEAN |
| Electrocleaner | 8.0" | 7.33" | `#E8A020` | ELECTROCLEANER |
| Solvent / Vapor Degrease | 15.5" | 8.0" | `#C8D0D8` | SOLVENT DEGREASE |

Each box: Rounded rect H: 4.8", fill `#1E2435`, left accent 0.06".

*Soak Clean box:*
- `4--8 oz/gal` JetBrains Mono 16 pt `#2EC4B6`
- `140--180 F, 3--10 min`
- `Non-silicated alkaline cleaner`
- `Role: Primary cleaning step for most substrates`
- `Removes bulk oil, soil, and organic contamination`
- `Limitation: May not remove heavy lapping compound alone`

*Electrocleaner box:*
- `4--8 oz/gal` JetBrains Mono 16 pt `#E8A020`
- `120--160 F, 1--3 min`
- `Anodic (preferred) or cathodic`
- `Role: Gas scrubbing action dislodges embedded soil`
- `Anodic: safer -- no hydrogen embrittlement risk`
- `Cathodic: more aggressive but RISK of H-embrittlement on high-strength steel` (`#E05C5C`)

*Solvent Degrease box:*
- `Vapor or immersion` JetBrains Mono 16 pt `#C8D0D8`
- `Per solvent spec`
- `Trichloroethylene or nPB (legacy); aqueous preferred`
- `Role: Precision degreasing for heavy machining oils`
- `Still used in some aerospace shops under EPA permits`
- `Being phased out in favor of aqueous systems`

---

### ZONE 5 -- Substrate Decision Table

**Section label:** `SUBSTRATE-SPECIFIC CLEANING -- WHAT CHANGES?` -- Y: 20.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK E -- Decision Table (Y: 21.3" to 26.3")**

Column widths (23.0" total):
- Substrate (4.0") | Soak Clean (5.0") | Electrocleaner (5.0") | Special Requirement (9.0")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 1.0".

| Substrate | Soak Clean | Electrocleaner | Special Requirement |
|---|---|---|---|
| Carbon/alloy steel | Standard 4--8 oz/gal | Anodic preferred | None -- straightforward |
| Hardened steel (>40 HRC) | Standard | Anodic ONLY -- no cathodic | H-embrittlement risk -- bake 375 F / 4 hr if cathodic used |
| Inconel / Waspaloy | Standard + extended time | Anodic | Wood's nickel strike required after activation |
| Titanium | Standard | Optional | HF/HNO3 etch after clean; Wood's strike mandatory |
| Copper alloys | Standard | Anodic | Avoid excessive alkalinity -- can tarnish Cu |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Substrate names: Inter Medium, 13 pt.
Special requirement column: coral text (`#E05C5C`) for warnings.

---

### ZONE 6 -- Common Cleaning Failures

**Section label:** `WHAT GOES WRONG` -- Y: 26.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK F -- Four Problem Cards (Y: 27.3" to 32.3")**

Four cards in a single row. Gap: 0.33".

Each card: Rounded rect, W: 5.5", H: 4.5", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | WATER BREAK | Insufficient cleaning or exhausted cleaner | Increase time/temp; replenish cleaner concentration |
| 2 | 6.33" | SKIP PLATING | Silicate residue from silicated cleaner | Switch to non-silicated cleaner; acid dip to remove film |
| 3 | 12.16" | ADHESION FAILURE | Oil not fully removed; wrong polarity on electrocleaner | Extend soak time; verify anodic vs. cathodic selection |
| 4 | 18.0" | PITTING ON DEPOSIT | Organic contamination carried into plating bath | Carbon treat cleaning bath periodically; improve rinsing |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 7 -- Footer Band

Standard. Title: `Cleaning -- Nickel-Cobalt`. Version `v1.0 -- 2026`.

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Cleaning parameters shown are typical industry values for nickel-cobalt plating preparation. Specific substrate requirements and cleaning chemistries vary by OEM specification and proprietary product. Consult your process supplier for application-specific guidance. Source: General industry knowledge; ASM Handbook Vol. 5.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Cleaning -- Nickel-Cobalt

**Series name:** Inter Regular, 14 pt, `#F0EDE8` at 70%, Center. Y: 34.2"

> Plating Posters Inc -- Metal Finishing Reference Series

**Logo placeholder:** Rectangle, X: 22.5", Y: 33.3", W: 0.83", H: 0.42", fill `#3A4055`. Text: `[LOGO]`

**Version:** JetBrains Mono Regular, 11 pt, `#F0EDE8` at 50%. X: 0.5", Y: 35.0"

> v1.0 -- 2026

---

## Parts 5--7

**Grouping:** 7 zones as shown.

**Light Remap:** Standard table (same as Poster #71).

**Export:** Six files -- `Cleaning NiCo -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Cleaning for NiCo is functionally identical to cleaning for any nickel process. The poster earns its place by addressing the substrate diversity -- NiCo is disproportionately applied to aerospace superalloys and hardened steels that require more careful cleaning protocols. The substrate decision table is the unique value-add here. Watson's brief notes "same as Watts/sulfamate nickel" for cleaning, so I expanded from standard nickel cleaning knowledge plus the aerospace substrate notes from the activation section.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #72 -- Construction Workup v1.0*
*2026-04-26*
