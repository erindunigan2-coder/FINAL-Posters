---
Project: Plating Posters Inc
Poster Number: 207
Title: "Passivation (Stainless Steel) -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster CC-08 technical reference (passivation -- stainless steel)"
Technical Source: Industry-standard passivation of stainless steel per ASTM A967 and AMS 2700. Covers nitric acid and citric acid processes. Complete 6-stage sequence from cleaning through drying/verification.
Process Scope: Passivation (stainless steel) -- complete process flow (8 poster stages mapped to 6 process stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Passivation
  - StainlessSteel
  - ProcessFlow
  - ConstructionWorkup
  - Series2
  - ClusterCC08
---

# Poster #207 -- Construction Workup
## Passivation (Stainless Steel) -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for CC-08: Passivation (Stainless Steel). Passivation is unique in this series -- it is NOT a coating. It removes free iron contamination and restores the chromium-rich passive film (Cr2O3) that gives stainless steel its corrosion resistance. The process flow is simpler than most conversion coatings but the alloy-specific chemistry selection is more complex. This poster maps the full sequence and introduces the nitric vs. citric decision.

Design philosophy: clean U-flow diagram as the hero (8 boxes -- some stages in this cluster address conceptual content rather than distinct tank stages), a comparison callout (nitric vs. citric acid), an alloy family selection guide, and a troubleshooting quick-hit strip.

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

1. **Process flow diagram (Block B -- HERO):** Eight rounded rectangles in a U-flow. Note: passivation has fewer distinct tank stages than electroplating, so some boxes map to conceptual stages (free iron sources, water quality) rather than physical tanks.
2. **Parameter summary table (Block D).**
3. **Nitric vs. Citric comparison (Block E).**
4. **Troubleshooting quick-hit strip (Block F).**

---

## Part 2 -- Document Setup Instructions

### Step 1 -- Create the document
- Width: **24 inches**. Height: **36 inches**.

### Step 2 -- Set the background color
- **`#1A1F2E`** (Gunmetal Dark)

### Step 3 -- Upload fonts
Standard locked set: Barlow Condensed ExtraBold, Barlow SemiBold, Inter Regular/Medium, JetBrains Mono Regular.

### Step 4 -- Set up color palette
Standard locked palette.

### Step 5 -- Set ruler guides
Standard guide set.

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- PROCESS FLOW DIAGRAM / HERO (2.9"--15.5" / ~12.6" tall)
  Block B: Eight-stage U-flow diagram (2 rows of 4)
  Block C: Stage legend strip (color key)

ZONE 3 -- PARAMETER SUMMARY TABLE (15.5"--22.0" / ~6.5" tall)
  Block D: 8-row parameter table

ZONE 4 -- NITRIC VS. CITRIC ACID (22.0"--28.5" / ~6.5" tall)
  Block E: Side-by-side comparison

ZONE 5 -- TROUBLESHOOTING QUICK HITS (28.5"--32.5" / ~4.0" tall)
  Block F: 4-problem strip

ZONE 6 -- FOOTER BAND (32.5"--36.0" / ~3.5" tall)
  Block G: Footer
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**BLOCK A -- Headline**
- Font: Barlow Condensed ExtraBold, 88 pt, `#F0EDE8`
- Text (all caps):

> PASSIVATION (STAINLESS STEEL)

**BLOCK A -- Subheading**
- Font: Barlow SemiBold, 36 pt, `#27AE60` (Emerald)

> Complete Process Flow -- Cleaning to Verification

**BLOCK A -- Tagline**
- Font: Barlow SemiBold, 22 pt, `#F0EDE8` at 65%

> Not a coating -- a restoration. Remove the free iron. Let the chromium do its job.

---

### ZONE 2 -- Process Flow Diagram (HERO)

**Section label:**
- Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`, Center

> THE COMPLETE PROCESS -- STAGE BY STAGE

**BLOCK B -- Eight-Stage U-Flow Diagram**

**Top Row (Y: 3.8" to 8.3") -- Stages 1-4, left to right:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Alkaline Clean | Box 1 | 0.5" | `#2EC4B6` (Teal) | Cleaning |
| 2. Rinse (Post-Clean) | Box 2 | 6.0" | `#2EC4B6` (Teal) | Rinse |
| 3. Free Iron Sources | Box 3 | 11.5" | `#E8A020` (Amber) | Education |
| 4. Water Quality | Box 4 | 17.0" | `#2EC4B6` (Teal) | Rinse/Prep |

**Bottom Row (Y: 9.5" to 14.0") -- Stages 5-8, right to left:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 5. Passivation Bath | Box 5 | 17.0" | `#27AE60` (Emerald) | Main Stage |
| 6. Rinse (Post-Acid) | Box 6 | 11.5" | `#2EC4B6` (Teal) | Rinse |
| 7. Verification | Box 7 | 6.0" | `#E8A020` (Amber) | QC |
| 8. Drying | Box 8 | 0.5" | `#E8A020` (Amber) | Post-Treatment |

**Inside each flow box:**

*Box 1 -- Alkaline Clean:*
- Badge: `STAGE 1`, fill `#2EC4B6`
- Name: `Alkaline Clean`
- Parameters: `4--8 oz/gal, 130--180 F` / `5--15 min`
- Purpose: `Remove machining oils, cutting fluids, polishing compounds`
- Check: `NO CHLORIDE in cleaner -- chloride pits stainless` (Coral `#E05C5C`)

*Box 2 -- Rinse (Post-Clean):*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Post-Clean`
- Parameters: `Ambient temp` / `Overflow or spray`
- Purpose: `Remove cleaner residues before acid`
- Check: `DI water for aerospace/medical parts`

*Box 3 -- Free Iron Sources:*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Free Iron` / Subtitle: `Understanding the Problem`
- Parameters: (none -- educational stage)
- Purpose: `Free iron on surface = the reason we passivate`
- Check: `Sources: machining tools, grinding, carbon steel contact, shop air`

*Box 4 -- Water Quality:*
- Badge: `STAGE 4`, fill `#2EC4B6`
- Name: `Water Quality` / Subtitle: `Pre-Passivation`
- Parameters: `DI or RO water preferred` / `Conductivity < 500 uS/cm`
- Purpose: `Clean, chloride-free water before acid bath`
- Check: `Chloride in rinse water can pit stainless during passivation`

*Box 5 -- Passivation Bath:*
- Badge: `STAGE 5`, fill `#27AE60`
- Name: `Passivation` / Subtitle: `Nitric or Citric Acid`
- Parameters: `Nitric: 20--45% HNO3` / `Citric: 4--20% C6H8O7` / `70--150 F, 4--30 min`
- Purpose: `Remove free iron; restore Cr2O3 passive film`
- Check: `Alloy family determines acid selection -- see chart below`

*Box 6 -- Rinse (Post-Acid):*
- Badge: `STAGE 6`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Post-Acid`
- Parameters: `Ambient to warm` / `Multiple stages for critical parts`
- Purpose: `Remove all acid residues`
- Check: `Trapped acid in crevices = #1 cause of post-passivation staining`

*Box 7 -- Verification:*
- Badge: `STAGE 7`, fill `#E8A020`
- Name: `Verification` / Subtitle: `Quality Check`
- Parameters: `Copper sulfate test (ASTM A380)` / `Salt spray, high humidity`
- Purpose: `Confirm free iron has been removed`
- Check: `Cu deposits = FAIL (free iron remains)`

*Box 8 -- Drying:*
- Badge: `STAGE 8`, fill `#E8A020`
- Name: `Drying`
- Parameters: `Air dry or warm forced air` / `120--150 F max`
- Purpose: `Remove moisture; prevent crevice corrosion`
- Check: `NO high-temp oven -- thermal oxidation defeats purpose` (Coral `#E05C5C`)

---

**BLOCK C -- Stage Legend Strip**

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Cleaning & Rinse` |
| `#E8A020` (Amber) | `Education, Verification & Post-Treatment` |
| `#27AE60` (Emerald) | `Passivation (Main Stage)` |
| `#E05C5C` (Coral) | `Caution / Failure` |

---

### ZONE 3 -- Parameter Summary Table

**Section label:** `AT-A-GLANCE PARAMETERS`

**BLOCK D -- 8-Row Parameter Table**

| Stage | Chemistry | Temp | Time | Key Control |
|---|---|---|---|---|
| 1. Alkaline Clean | Alk cleaner 4--8 oz/gal | 130--180 F | 5--15 min | No chloride cleaners |
| 2. Rinse | Fresh water (DI preferred) | Ambient | 1--2 min | Low conductivity |
| 3. Free Iron Sources | -- (educational) | -- | -- | Identify contamination sources |
| 4. Water Quality | DI or RO water | Ambient | As needed | < 500 uS/cm; chloride-free |
| 5. Passivation | Nitric 20--45% or Citric 4--20% | 70--150 F | 4--30 min | Alloy determines acid |
| 6. Rinse | Fresh water (DI for critical) | Ambient | Multiple | Thorough -- trapped acid stains |
| 7. Verification | CuSO4 test / salt spray / humidity | Per spec | Per spec | No copper = pass |
| 8. Drying | Forced air | 120--150 F max | Until dry | No high-temp oven |

---

### ZONE 4 -- Nitric vs. Citric Acid

**Section label:** `NITRIC VS. CITRIC -- THE TWO PATHS`

**Left -- Nitric Acid (HNO3):**
- Rounded rect, X: 0.5", W: 11.0", fill `#1E2435`, left accent `#E8A020`
- Title: `NITRIC ACID (HNO3)` Barlow SemiBold, 20 pt, `#E8A020`
- Subtitle: `The Traditional Standard`

| Property | Value |
|---|---|
| Concentration | 20--45% by volume |
| Temperature | 70--150 F (21--66 C) |
| Time | 20--30 min minimum |
| Mechanism | Oxidizing acid -- dissolves iron AND promotes Cr2O3 |
| 300-series | Excellent |
| 400-series martensitic | Good to excellent (with dichromate) |
| Free-machining (303, 416) | Best option (with dichromate) |
| Safety | Fuming, toxic NOx; aggressive |
| Waste | Hazardous (Cr6+ if dichromate used) |
| Bath life | Long (years with maintenance) |
| Governing spec | ASTM A967 Types 1--4; AMS 2700 |

Bottom: `Legacy standard. Still dominant in aerospace. Handles difficult alloys better.` `#E8A020`

**Right -- Citric Acid (C6H8O7):**
- Rounded rect, X: 12.0", W: 11.5", fill `#1E2435`, left accent `#27AE60`
- Title: `CITRIC ACID (C6H8O7)` Barlow SemiBold, 20 pt, `#27AE60`
- Subtitle: `The Modern Alternative`

| Property | Value |
|---|---|
| Concentration | 4--20% by weight |
| Temperature | 70--160 F (21--71 C) |
| Time | 4--20 min minimum |
| Mechanism | Chelates iron; relies on dissolved O2 for Cr2O3 |
| 300-series | Excellent |
| 400-series martensitic | Good (may need longer time/higher conc.) |
| Free-machining (303, 416) | May struggle; longer times needed |
| Safety | Mild organic acid; safe to handle |
| Waste | Non-hazardous; biodegradable |
| Bath life | Moderate (months; iron buildup limits life) |
| Governing spec | ASTM A967 Types 5--8 |

Bottom: `Gaining share rapidly. Preferred for new installations. Safer and cheaper to operate.` `#27AE60`

---

### ZONE 5 -- Troubleshooting Quick Hits

**Section label:** `QUICK TROUBLESHOOTING -- 4 COMMON PROBLEMS`

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | CuSO4 TEST FAILURE | Free iron remaining; insufficient time or concentration | Increase time/conc/temp; replace bath |
| 2 | 6.33" | STAINING AFTER PASSIVATION | Trapped acid in crevices; chloride in rinse water | Improve rinsing; use DI water; dry promptly |
| 3 | 12.16" | PITTING DURING PASSIVATION | Chloride contamination; bath temp too high for alloy | Use chloride-free reagents; reduce temp |
| 4 | 18.0" | ETCHING / MATTE FINISH | Acid too strong; temp too high; time too long | Reduce conc/temp/time; try citric for sensitive grades |

---

### ZONE 6 -- Footer Band

Standard footer. Title: `Passivation (Stainless Steel) -- Process Flow`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Process parameters shown are typical industry values for passivation of stainless steel per ASTM A967 and AMS 2700. Specific formulations and process limits vary by alloy and specification. Consult your process supplier for application-specific guidance.`

---

## Part 5 -- Grouping and Naming Convention

| Group Name | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline |
| Zone 2 - Process Flow | Section label, eight flow boxes, arrows, legend strip |
| Zone 3 - Parameter Table | Section label, 8-row table |
| Zone 4 - Nitric vs Citric | Section label, two comparison callouts |
| Zone 5 - Troubleshooting | Section label, four problem cards |
| Zone 6 - Footer | Footer band, disclaimer, title, series, logo, version |

---

## Part 6 -- Light Edition Color Remap Table

Standard remap table.

---

## Part 7 -- Export Checklist

| File Name | Mode | Quality | Bleed |
|---|---|---|---|
| `Passivation Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Passivation Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Passivation Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Passivation Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Passivation Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Passivation Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

Passivation is conceptually different from every other process in the series: it does not ADD anything to the surface. It REMOVES contamination and lets the natural passive film reform. The tagline ("Not a coating -- a restoration") captures this. The nitric vs. citric comparison is the most important decision framework on the poster -- citric is winning market share fast, and this poster should present both options fairly while noting the trend. The "Free Iron Sources" box (Stage 3) is educational rather than procedural -- it explains WHY passivation exists, which is essential context for shops that may not fully understand the science.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #207 -- Construction Workup v1.0*
*2026-04-26*
