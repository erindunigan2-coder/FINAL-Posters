---
Project: Plating Posters Inc
Poster Number: 119
Title: "Gold Plating -- Process Flow"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-12 technical reference (acid hard gold plating)"
Technical Source: Industry-standard acid hard gold plating process. Covers the complete 8-stage sequence from cleaning through post-treatment. Values are typical ranges for cobalt-hardened acid gold -- the dominant gold plating system for electronics and connectors.
Process Scope: Acid hard gold plating -- complete process flow (8 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - GoldPlating
  - ProcessFlow
  - ConstructionWorkup
  - Series2
  - ClusterEP12
---

# Poster #119 -- Construction Workup
## Gold Plating -- Process Flow

*Alaina -- Plating Posters Inc*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for EP-12: Gold Plating (Acid Hard). It shows the complete 8-stage process sequence at a glance. Gold plating is the most expensive electroplating process by a wide margin -- every poster in this cluster hammers the message: control the bath, recover the drag-out, track the gold. The process flow poster sets that tone from the start.

Design philosophy: clean U-flow diagram as the hero, a compact parameter summary table, a "gold economics" callout (cost awareness is inseparable from gold plating), and a troubleshooting quick-hit strip. Every gold poster must reinforce: gold content = money.

---

## Part 1 -- Workflow Orientation

### Design Capabilities for This Poster

- Text boxes with precise font, size, weight, color, and spacing control
- Solid-color rectangles and rounded rectangles for flow boxes, callout panels, table rows, and accent borders
- Arrow/line elements connecting flow boxes in sequence
- Color fills set to exact hex values
- Background page color set to exact hex
- Export at print-quality PDF (300 DPI equivalent via print export)

### Limitations to Flag

1. **Process flow diagram (Block B -- HERO):** Eight rounded rectangles in a U-flow. Same geometry as Poster #111 (Tin) and #31 (Zinc).

2. **Parameter summary table (Block D):** 8-row table.

3. **"Gold Economics" callout (Block E):** Cost-focused panel -- gold content tracking, drag-out recovery value, replenishment cost.

4. **Troubleshooting quick-hit strip (Block F):** 4 common gold plating problems.

5. **4 pt left-border accents on callout boxes.**

6. **Global Colors / swatch remap for Light edition.**

7. **JetBrains Mono font.** Fallback: Courier Prime.

8. **Print size -- 24x36".**

---

## Part 2 -- Document Setup Instructions

### Step 1 -- Create the document
- Width: **24 inches**. Height: **36 inches**.

### Step 2 -- Set the background color
- **`#1A1F2E`** (Gunmetal Dark)

### Step 3 -- Upload fonts
- **Barlow Condensed ExtraBold** -- all headlines and section labels
- **Barlow SemiBold** -- all subheadings, callout titles
- **Inter Regular** and **Inter Medium** -- all body text, table data, and descriptions
- **JetBrains Mono Regular** -- all parameter data, chemical formulas, concentration ranges, version number

If JetBrains Mono upload fails, substitute **Courier Prime**.

### Step 4 -- Set up color palette

| Color Name | Hex | Primary Use |
|---|---|---|
| Gunmetal Dark | `#1A1F2E` | Background (Dark edition) |
| Warm White | `#F0EDE8` | All primary text (Dark edition) |
| Amber | `#E8A020` | Activation & post-treatment, gold-themed accents |
| Teal | `#2EC4B6` | Cleaning & rinse stages |
| Emerald | `#27AE60` | Plating stage, optimal reference |
| Coral | `#E05C5C` | Problems, defects, cost warnings |
| Mid Slate | `#3A4055` | Table headers, dividers, flow arrows |
| Deep Navy | `#0D1020` | Footer band background |
| Dark Callout | `#1E2435` | Callout box fills, flow box fills |
| Alt Row | `#252B3D` | Alternating table rows |
| Bright Silver | `#C8D0D8` | Neutral metallic accents |

### Step 5 -- Set ruler guides

**Vertical guides:** 0.5" / 23.5"
**Horizontal guides:** 0.5" / 2.9" / 15.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- PROCESS FLOW DIAGRAM / HERO (2.9"--15.5" / ~12.6" tall)
  Block B: Eight-stage U-flow diagram (2 rows of 4)
  Block C: Stage legend strip (color key)

ZONE 3 -- PARAMETER SUMMARY TABLE (15.5"--22.0" / ~6.5" tall)
  Block D: 8-row parameter table (one row per stage)

ZONE 4 -- GOLD ECONOMICS (22.0"--28.5" / ~6.5" tall)
  Block E: Cost awareness, drag-out recovery, gold tracking

ZONE 5 -- TROUBLESHOOTING QUICK HITS (28.5"--32.5" / ~4.0" tall)
  Block F: 4-problem strip with one-line fixes

ZONE 6 -- FOOTER BAND (32.5"--36.0" / ~3.5" tall)
  Block G: Disclaimer + poster title + series name + logo placeholder + version
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Dimensions:** Full page width. Y: 0" to 2.9".

---

**BLOCK A -- Headline**

- Position: X: 0.5". Y: 0.5"
- Width: 23.0"
- Font: Barlow Condensed ExtraBold, 88 pt, `#F0EDE8`, Letter spacing: -4
- Text (all caps):

> GOLD PLATING

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Font: Barlow SemiBold, 36 pt, `#E8A020` (Amber)
- Text:

> Complete Process Flow -- 8 Stages from Cleaning to Inspection

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Font: Barlow SemiBold, 22 pt, `#F0EDE8` at 65%
- Text:

> Acid hard gold -- cobalt-hardened for wear-resistant contacts and connectors. Every gram tracked. Every rinse recovered. Gold content is money.

---

### ZONE 2 -- Process Flow Diagram (HERO)

**Dimensions:** Full page width within margins. Y: 2.9" to 15.5".

---

**Section label:**
- Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> THE COMPLETE PROCESS -- STAGE BY STAGE

---

**BLOCK B -- Eight-Stage U-Flow Diagram**

Y: 3.8" to 14.0". Same geometry as Poster #111.

**Top Row (Y: 3.8" to 8.3") -- Stages 1-4:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Alkaline Clean | Box 1 | 0.5" | `#2EC4B6` (Teal) | Cleaning |
| 2. Rinse (Pre-Act) | Box 2 | 6.0" | `#2EC4B6` (Teal) | Rinse |
| 3. Acid Activation | Box 3 | 11.5" | `#E8A020` (Amber) | Activation |
| 4. Rinse (Pre-Plate) | Box 4 | 17.0" | `#2EC4B6` (Teal) | Rinse |

**Bottom Row (Y: 9.5" to 14.0") -- Stages 5-8:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 5. Gold Plate | Box 5 | 17.0" | `#27AE60` (Emerald) | Plating |
| 6. Rinse (Post-Plate) | Box 6 | 11.5" | `#2EC4B6` (Teal) | Rinse |
| 7. Hot Water Rinse | Box 7 | 6.0" | `#E8A020` (Amber) | Post-Treatment |
| 8. Dry / Inspect | Box 8 | 0.5" | `#E8A020` (Amber) | Post-Treatment |

Arrows and vertical connector: same as Poster #111.

**Inside each flow box:**

*Box 1 -- Alkaline Clean:*
- Badge: `STAGE 1`, fill `#2EC4B6`
- Name: `Alkaline Clean`
- Parameters: `130--150 F (54--66 C)` / `3--5 oz/gal` / `3--5 min`
- Purpose: `Remove oils, fingerprints, shop soil`
- Check: `CHECK: Water-break-free after rinse`

*Box 2 -- Rinse (Pre-Activation):*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Activation`
- Parameters: `Ambient temp` / `Flowing or cascade`
- Purpose: `Remove alkaline cleaner residue`
- Check: `Prevents cleaner drag-in to acid activation`

*Box 3 -- Acid Activation:*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Acid Activation`
- Parameters: `5--10% H2SO4` / `Ambient, 15--30 sec`
- Purpose: `Remove nickel oxide from underplate surface`
- Check: `NEVER use HCl -- chloride destroys gold baths` (Coral `#E05C5C`)

*Box 4 -- Rinse (Pre-Plate):*
- Badge: `STAGE 4`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Plate (DI)`
- Parameters: `DI water required` / `Flowing`
- Purpose: `Remove acid; prevent mineral drag-in`
- Check: `DI only -- tap water minerals contaminate gold bath`

*Box 5 -- Gold Plate (Main Tank):*
- Badge: `STAGE 5`, fill `#27AE60`
- Name: `Gold Plate` / Subtitle: `Main Tank`
- Parameters: `Au: 8--12 g/L` / `pH: 4.0--4.5` / `100--120 F (38--49 C)` / `5--10 ASF (rack)`
- Purpose: `Electrodeposit hard gold alloy`
- Check: `Gold content: track daily. Every gram counts.`

*Box 6 -- Rinse (Post-Plate):*
- Badge: `STAGE 6`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Drag-Out Recovery`
- Parameters: `DI water, stagnant recovery` / `Then flowing DI rinse`
- Purpose: `Capture gold drag-out for return to bath`
- Check: `CRITICAL: Gold in rinse water = gold lost` (Coral `#E05C5C`)

*Box 7 -- Hot Water Rinse:*
- Badge: `STAGE 7`, fill `#E8A020`
- Name: `Hot Water Rinse`
- Parameters: `140--160 F (60--71 C)` / `DI water, 30--60 sec`
- Purpose: `Remove residual chemistry; accelerate drying`
- Check: `Hot DI rinse prevents water spots on gold`

*Box 8 -- Dry / Inspect:*
- Badge: `STAGE 8`, fill `#E8A020`
- Name: `Dry / Inspect`
- Parameters: `Forced warm air` / `or vacuum dry`
- Purpose: `Dry without staining; inspect deposit`
- Check: `Thickness measurement (XRF or beta backscatter)`

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.3". Same format as Poster #111.

---

### ZONE 3 -- Parameter Summary Table

**Section label:** `AT-A-GLANCE PARAMETERS` -- Y: 15.7".

**BLOCK D -- 8-Row Parameter Table**

Y: 16.3" to 21.8".

| Stage | Chemistry | Temp | Time | CD | Key Control |
|---|---|---|---|---|---|
| 1. Alk Clean | Alk cleaner 3--5 oz/gal | 130--150 F | 3--5 min | -- | Water-break-free |
| 2. Rinse | DI or city water | Ambient | 30--60 sec | -- | No alkaline carry-over |
| 3. Activation | H2SO4 5--10% (NO HCl) | Ambient | 15--30 sec | -- | Chloride-free mandatory |
| 4. Rinse (DI) | DI water only | Ambient | 30--60 sec | -- | DI only -- no tap water |
| 5. Gold Plate | Au 8--12 g/L, pH 4.0--4.5 | 100--120 F | Per spec | 5--10 ASF | Daily Au analysis |
| 6. Rinse (recovery) | DI water | Ambient | 30--60 sec | -- | Capture drag-out |
| 7. Hot DI Rinse | DI water | 140--160 F | 30--60 sec | -- | Spot-free drying |
| 8. Dry/Inspect | -- | Warm air | Per spec | -- | XRF thickness |

---

### ZONE 4 -- Gold Economics

**Section label:** `GOLD ECONOMICS -- EVERY GRAM TRACKED` -- Y: 22.2".

**BLOCK E -- Three-Panel Economics Callout**

Y: 22.9" to 28.3". Three side-by-side panels.

**Panel 1 -- The Cost:**
- Rounded rect, X: 0.5", W: 7.33", H: 5.2", fill `#1E2435`, left accent `#E05C5C`
- Title: `THE COST` Barlow SemiBold 18 pt `#E05C5C`

Content:
- `Gold: ~$70--90/troy oz (fluctuates daily)`
- `KAu(CN)2: ~$100--150/troy oz Au content`
- `A single gallon of operating bath: $200--800+ in gold alone`
- `Drag-out loss per rack: 0.1--0.5 mL/sq ft`
- `At 10 g/L Au, each mL lost = $0.02--0.03 in gold`

Note: `Gold metal prices as of 2025 reference. Verify current spot price.` Inter Regular 11 pt `#F0EDE8` at 50%

**Panel 2 -- Tracking:**
- Rounded rect, X: 8.0", W: 7.33", H: 5.2", fill `#1E2435`, left accent `#E8A020`
- Title: `GOLD TRACKING` Barlow SemiBold 18 pt `#E8A020`

Content:
- `Analyze gold content DAILY by AA or titration`
- `Track ampere-hours plated vs. gold consumed`
- `Theoretical consumption: 12.25 g Au per 1000 amp-min`
- `Replenish based on analysis, not schedule`
- `Maintain gold ledger: additions, analyses, tank volume`

Note: `Gold accountability is not optional. It is the foundation of gold plating economics.` Inter Medium 13 pt `#E8A020`

**Panel 3 -- Recovery:**
- Rounded rect, X: 15.5", W: 8.0", H: 5.2", fill `#1E2435`, left accent `#27AE60`
- Title: `DRAG-OUT RECOVERY` Barlow SemiBold 18 pt `#27AE60`

Content:
- `Stagnant DI recovery rinse after plating`
- `Return concentrated rinse to bath periodically`
- `Economic threshold: >1 ppm Au in rinse = worth recovering`
- `Methods: return to bath, electrolytic recovery, ion exchange`
- `All gold waste (filters, anode bags, sludge) must be collected for reclamation`

Note: `A good gold shop recovers 95%+ of all gold used. The rest is waste -- and waste is money.` Inter Medium 13 pt `#27AE60`

---

### ZONE 5 -- Troubleshooting Quick Hits

**Section label:** `QUICK TROUBLESHOOTING -- 4 COMMON PROBLEMS` -- Y: 28.7".

**BLOCK F -- Four Problem Cards**

Y: 29.4" to 32.3".

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | DARK / DISCOLORED | Metallic contamination (Cu, Fe, Zn), organic | Dummy plate; carbon treat; check drag-in |
| 2 | 6.33" | SOFT DEPOSIT | Low hardener (Co or Ni), low CD | Analyze Co/Ni; increase CD |
| 3 | 12.16" | ROUGH / NODULAR | Low gold, poor filtration, particulate | Replenish Au; increase filtration |
| 4 | 18.0" | POOR ADHESION | Ni underplate oxidized, bad activation | Re-activate; check time between Ni and Au |

---

### ZONE 6 -- Footer Band

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:**

> This poster is an educational reference tool. Process parameters shown are typical industry values for acid hard gold plating. Gold content values and costs are approximate -- verify current market prices. Consult your process supplier for application-specific guidance.

**Poster title:** `Gold Plating -- Process Flow`
**Series name:** `Plating Posters Inc -- Metal Finishing Reference Series`
**Version:** `v1.0 -- 2026`

---

## Part 5 -- Grouping and Naming Convention

| Group Name | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline |
| Zone 2 - Process Flow | Section label, eight flow boxes, arrows, legend strip |
| Zone 3 - Parameter Table | Section label, 8-row table |
| Zone 4 - Gold Economics | Section label, three economics panels |
| Zone 5 - Troubleshooting | Section label, four problem cards |
| Zone 6 - Footer | Footer band, disclaimer, title, series, logo, version |

---

## Part 6 -- Light Edition Color Remap Table

| Dark Hex | Light Hex | Notes |
|----------|-----------|-------|
| `#1A1F2E` | `#F5F4F0` | Background |
| `#F0EDE8` | `#1A1F2E` | All primary text |
| `#1E2435` | `#ECEEF4` | Callout/flow box fills |
| `#252B3D` | `#E8E8F0` | Alternate rows, legend strip |
| `#0D1020` | `#1A1F2E` | Footer background |
| `#E8A020` | `#C8860A` | Amber accents |
| `#2EC4B6` | `#1A8C82` | Teal accents |
| `#27AE60` | `#1E7A47` | Emerald accents |
| `#E05C5C` | `#B83E3E` | Coral accents |
| `#3A4055` | `#D0D4DE` | Table headers, dividers, arrows |
| `#C8D0D8` | `#C8D0D8` | Bright Silver -- **unchanged** |

---

## Part 7 -- Export Checklist

| File Name | Mode | Quality | Bleed |
|---|---|---|---|
| `Gold Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gold Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gold Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Gold Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gold Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gold Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

Gold plating is the most expensive process in the series. The economics panel replaces the typical "comparison" zone used in other process flow posters because the #1 question in gold plating is not "which chemistry?" -- it is "how do we control cost?" The answer: daily analysis, drag-out recovery, and gold accountability. The "NEVER use HCl" warning in the activation box and the "DI water only" callout in the pre-plate rinse are the two most critical cross-contamination warnings in the entire cluster. Chloride contamination and mineral drag-in are gold bath killers.

---

*Alaina -- Plating Posters Inc*
*Poster #119 -- Construction Workup v1.0*
*2026-04-26*
