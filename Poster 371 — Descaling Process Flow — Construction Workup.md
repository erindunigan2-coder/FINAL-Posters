---
Project: Plating Posters Inc
Poster Number: 371
Title: "Descaling / Heavy Oxide Removal -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster CT-5 technical reference (descaling / heavy oxide removal)"
Technical Source: Industry-standard descaling and heavy oxide removal processes. Covers mechanical (blast), chemical (alkaline permanganate, molten salt), and combination approaches. Values are typical ranges for carbon and alloy steel descaling prior to plating.
Process Scope: Descaling / heavy oxide removal -- complete process flow (decision tree + 6-stage combination sequence)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Descaling
  - SurfacePreparation
  - ProcessFlow
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT05
---

# Poster #371 -- Construction Workup
## Descaling / Heavy Oxide Removal -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for CT-5: Descaling / Heavy Oxide Removal. It presents the complete decision tree for choosing a descaling method based on scale severity, followed by the most common combination sequence (blast + acid pickle). A shop foreman looks at this poster and knows immediately: what type of scale am I dealing with, and what sequence do I run? This poster is the "map" that the remaining 6 posters (#372--#377) zoom into.

Design philosophy: decision tree as the hero (which method for which scale condition), followed by a 6-stage combination flow, a blast media selection table, and a troubleshooting quick-hit strip. Dense but scannable -- the descaling department's wall reference.

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

1. **Decision tree (Block B -- HERO):** Five rows showing scale condition --> primary method --> follow-up. Built with rounded rectangles and connecting arrows. Each row color-coded by severity.

2. **Combination flow sequence (Block C):** Six rounded rectangles in a horizontal flow: Blast --> Clean --> Rinse --> Pickle --> Rinse --> Activate. Arrows between each stage.

3. **Blast media selection table (Block D):** A 5-row table comparing steel shot, steel grit, aluminum oxide, glass bead, and garnet.

4. **Troubleshooting quick-hit strip (Block F):** Four common descaling problems with one-line fixes.

5. **4 pt left-border accents on callout boxes:** Same technique as all previous posters.

6. **Global Colors / swatch remap for Light edition:** Manual recolor per remap table.

7. **JetBrains Mono font:** Ensure font is available. Fallback: Courier Prime.

8. **Print size -- 24x36":** Set to exactly 24 inches wide by 36 inches tall at document creation.

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
| Amber | `#E8A020` | Chemical method stages, warning headers |
| Teal | `#2EC4B6` | Mechanical method stages, rinse steps |
| Emerald | `#27AE60` | Optimal results, pass states |
| Coral | `#E05C5C` | Problems, defects, hazard callouts |
| Mid Slate | `#3A4055` | Table headers, dividers, flow arrows |
| Deep Navy | `#0D1020` | Footer band background |
| Dark Callout | `#1E2435` | Callout box fills, flow box fills |
| Alt Row | `#252B3D` | Alternating table rows |
| Bright Silver | `#C8D0D8` | Neutral metallic accents |

### Step 5 -- Set ruler guides

**Vertical guides (from left edge):**
- 0.5" -- left safe zone margin
- 23.5" -- right safe zone margin

**Horizontal guides (from top edge):**
- 0.5" -- top safe zone margin
- 2.9" -- Zone 1/Zone 2 boundary
- 16.0" -- Zone 2/Zone 3 boundary
- 22.0" -- Zone 3/Zone 4 boundary
- 28.5" -- Zone 4/Zone 5 boundary
- 32.5" -- Zone 5/Zone 6 boundary
- 35.5" -- bottom safe zone margin

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- DECISION TREE + COMBINATION FLOW / HERO (2.9"--16.0" / ~13.1" tall)
  Block B: Scale-condition decision tree (5 rows)
  Block C: 6-stage combination flow diagram

ZONE 3 -- BLAST MEDIA SELECTION TABLE (16.0"--22.0" / ~6.0" tall)
  Block D: 5-row media comparison table

ZONE 4 -- SURFACE PREP GRADES (22.0"--28.5" / ~6.5" tall)
  Block E: SSPC surface preparation grades reference

ZONE 5 -- TROUBLESHOOTING QUICK HITS (28.5"--32.5" / ~4.0" tall)
  Block F: 4-problem strip with one-line fixes

ZONE 6 -- FOOTER BAND (32.5"--36.0" / ~3.5" tall)
  Block G: Disclaimer + poster title + series name + logo placeholder + version
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Dimensions:** Full page width. Y: 0" to 2.9".
**Background:** Same as page (`#1A1F2E`) -- no separate fill needed.

---

**BLOCK A -- Headline**

- Element type: Text box
- Position: X: 0.5". Y: 0.5"
- Width: 23.0"
- Font: Barlow Condensed ExtraBold
- Size: 80 pt
- Color: `#F0EDE8`
- Letter spacing: -4
- Text (all caps):

> DESCALING / HEAVY OXIDE REMOVAL

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 34 pt
- Color: `#2EC4B6` (Teal)
- Text:

> Process Flow -- From Scale Assessment to Clean Metal

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 20 pt
- Color: `#F0EDE8` at 65%
- Text:

> Mill scale, forge scale, heat-treat scale -- choose the right method for the right condition. Get this wrong and nothing downstream works.

---

### ZONE 2 -- Decision Tree + Combination Flow (HERO)

**Dimensions:** Full page width within margins. Y: 2.9" to 16.0" (~13.1" tall).

---

**Section label:**
- Centered horizontally. Y: 3.1"
- Font: Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`, Center
- Text:

> WHICH METHOD FOR WHICH SCALE?

---

**BLOCK B -- Scale Condition Decision Tree**

Y: 3.8" to 10.8" (~7.0" tall). Five rows, each showing a scale condition, the primary descaling method, and the follow-up step.

Each row: Rounded rectangle, X: 0.5", W: 23.0", H: 1.2", fill `#1E2435`, radius 6.

Row structure (left to right within each row):
- Scale condition badge: Rounded rect, W: 6.0", fill varies by severity
- Arrow: 2 pt `#3A4055`, right-pointing
- Primary method: Rounded rect, W: 7.5", fill `#1E2435`, left accent 0.06" in method color
- Arrow: 2 pt `#3A4055`, right-pointing
- Follow-up: Rounded rect, W: 6.5", fill `#1E2435`, left accent 0.06" `#27AE60`

| Row | Y | Scale Condition | Badge Fill | Primary Method | Method Accent | Follow-Up |
|---|---|---|---|---|---|---|
| 1 | 3.8" | Light oxide / heat tint | `#27AE60` at 25% | Chemical pickle (acid dip) | `#E8A020` | None required |
| 2 | 5.2" | Medium mill scale (hot-rolled) | `#E8A020` at 25% | Acid pickle (extended) or mechanical blast | `#E8A020` | Brief acid activation |
| 3 | 6.6" | Heavy forge / casting scale | `#E05C5C` at 25% | Mechanical blast (grit or shot) | `#2EC4B6` | Acid pickle to clean pits |
| 4 | 8.0" | Heavy scale on complex geometry | `#E05C5C` at 30% | Alkaline permanganate condition | `#E8A020` | Acid pickle (rinse between) |
| 5 | 9.4" | Heat-treat scale on alloy steel | `#E05C5C` at 40% | Molten salt descale (400--500 C) | `#E05C5C` | Water quench --> acid pickle |

Text inside each badge/box:
- Scale condition: Barlow SemiBold, 16 pt, `#F0EDE8`
- Method: Inter Medium, 15 pt, method accent color
- Follow-up: Inter Regular, 14 pt, `#F0EDE8`

Severity labels (far left, outside badge):
- JetBrains Mono Regular, 12 pt, badge fill color at 80%
- Row 1: `MILD` | Row 2: `MODERATE` | Row 3: `HEAVY` | Row 4: `HEAVY+` | Row 5: `EXTREME`

---

**Section label (combination flow):**
- Centered. Y: 11.0". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`

> THE MOST COMMON SEQUENCE -- BLAST + PICKLE

**Sublabel:**
- Inter Regular, 14 pt, `#F0EDE8` at 60%

> Mechanical descaling followed by chemical cleaning -- covers 80% of heavy descaling jobs

---

**BLOCK C -- Six-Stage Combination Flow**

Y: 11.8" to 15.5" (~3.7" tall). Six rounded rectangles in a single horizontal row.

Each flow box: Rounded rect, W: 3.5", H: 3.2", fill `#1E2435`, radius 6, top border accent 4 pt.

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Blast Descale | Box 1 | 0.5" | `#2EC4B6` (Teal) | Mechanical |
| 2. Alkaline Clean | Box 2 | 4.3" | `#E8A020` (Amber) | Chemical |
| 3. Rinse | Box 3 | 8.1" | `#2EC4B6` (Teal) | Rinse |
| 4. Acid Pickle | Box 4 | 11.9" | `#E8A020` (Amber) | Chemical |
| 5. Rinse | Box 5 | 15.7" | `#2EC4B6` (Teal) | Rinse |
| 6. Activate + Plate | Box 6 | 19.5" | `#27AE60` (Emerald) | Go |

Arrows between boxes: Stroke 3 pt `#3A4055`, arrowhead filled, right.

**Inside each flow box (top to bottom):**

*Box 1 -- Blast Descale:*
- Badge: `STAGE 1` fill `#2EC4B6`, Barlow Condensed ExtraBold 13 pt `#1A1F2E`
- Name: `Blast Descale` Barlow SemiBold 18 pt `#F0EDE8`
- Params: `SSPC-SP 10 min` JetBrains Mono 12 pt `#F0EDE8`
- Purpose: `Remove visible scale` Inter Regular 12 pt `#F0EDE8` at 70%
- Check: `100% coverage` Inter Medium 11 pt `#2EC4B6`

*Box 2 -- Alkaline Clean:*
- Badge: `STAGE 2` fill `#E8A020`
- Name: `Alkaline Clean`
- Params: `140--160 F | 3--10 min`
- Purpose: `Remove blast dust and oil`
- Check: `Water-break-free after rinse`

*Box 3 -- Rinse:*
- Badge: `STAGE 3` fill `#2EC4B6`
- Name: `Rinse`
- Params: `Ambient | Flowing`
- Purpose: `Remove alkaline carry-over`
- Check: `pH < 9.0 in final rinse`

*Box 4 -- Acid Pickle:*
- Badge: `STAGE 4` fill `#E8A020`
- Name: `Acid Pickle`
- Params: `HCl 10--20% or H2SO4 10--25%` / `Ambient--160 F`
- Purpose: `Dissolve residual oxide in pits`
- Check: `CAUTION: H-embrittlement on high-strength steel` (Coral `#E05C5C`)

*Box 5 -- Rinse:*
- Badge: `STAGE 5` fill `#2EC4B6`
- Name: `Rinse`
- Params: `Ambient | Multi-stage`
- Purpose: `Remove acid carry-over`
- Check: `Thorough -- acid drag-in ruins plating bath`

*Box 6 -- Activate + Plate:*
- Badge: `STAGE 6` fill `#27AE60`
- Name: `Activate + Plate`
- Params: `Per process spec`
- Purpose: `Final oxide removal and plate`
- Check: `Process within 4 hours of blast`

---

### ZONE 3 -- Blast Media Selection Table

**Dimensions:** Y: 16.0" to 22.0" (~6.0" tall).

---

**Section label:**
- Centered. Y: 16.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> BLAST MEDIA SELECTION -- CHOOSE YOUR WEAPON

---

**BLOCK D -- 5-Row Media Table**

Y: 16.9" to 21.8". Column widths (23.0" total):
- Media (4.0") | Size Range (3.5") | Hardness (2.5") | Best For (6.0") | Surface Profile (7.0")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.8".

| Media | Size Range | Hardness | Best For | Surface Profile |
|---|---|---|---|---|
| Steel Shot (S-110 to S-780) | 0.3--2.0 mm | 40--55 HRC | General descaling of steel | Peened, smooth, rounded dimples |
| Steel Grit (G-10 to G-80) | 0.3--2.0 mm | 55--65 HRC | Aggressive scale removal; profile for coating | Angular, aggressive profile |
| Aluminum Oxide | 40--120 grit | 9 Mohs | Stainless, aluminum, precision parts | Angular, controlled profile |
| Glass Bead | 40--325 mesh | 5.5--6 Mohs | Light cleaning; cosmetic; no profile change | Smooth, peened |
| Garnet | 36--120 grit | 7--8 Mohs | General purpose; good recyclability | Moderate angular profile |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Media names: Inter Medium, 13 pt.

---

### ZONE 4 -- Surface Prep Grades

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> SSPC SURFACE PREPARATION GRADES

**Sublabel:**
- Inter Regular, 14 pt, `#F0EDE8` at 60%

> For plating pre-treatment: SP-5 or SP-10 is typically required

---

**BLOCK E -- Four Grade Cards**

Y: 23.0" to 28.3". Four side-by-side callout boxes.

Each card: Rounded rect, W: 5.5", H: 5.0", fill `#1E2435`, radius 6, top accent 4 pt.

| Card | X | Grade | Accent | Coverage | Description |
|---|---|---|---|---|---|
| 1 | 0.5" | SP-5 / NACE No. 1 | `#27AE60` | White Metal Blast | No visible mill scale, rust, paint, or contaminants. Uniform metallic color. |
| 2 | 6.33" | SP-10 / NACE No. 2 | `#2EC4B6` | Near-White Blast | 95% of each area free of visible residues. Slight staining permitted. |
| 3 | 12.16" | SP-6 / NACE No. 3 | `#E8A020` | Commercial Blast | 67% of each area free of visible residues. |
| 4 | 18.0" | SP-7 / NACE No. 4 | `#3A4055` | Brush-Off Blast | Removes loose mill scale, rust, paint. Tight scale may remain. |

Interior per card:
- Grade code: JetBrains Mono Regular, 16 pt, accent color
- Grade name: Barlow SemiBold, 18 pt, `#F0EDE8`
- Description: Inter Regular, 13 pt, `#F0EDE8` at 80%, line height 150%
- Plating note (cards 1 and 2 only): Inter Medium, 12 pt, `#27AE60`
  - Card 1: `RECOMMENDED for plating`
  - Card 2: `MINIMUM for plating`

---

### ZONE 5 -- Troubleshooting Quick Hits

**Dimensions:** Y: 28.5" to 32.5" (~4.0" tall).

---

**Section label:**
- Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`

> QUICK TROUBLESHOOTING -- 4 COMMON PROBLEMS

---

**BLOCK F -- Four Problem Cards**

Y: 29.4" to 32.3". Four cards in a single row. Gap: 0.33".

Each card: Rounded rect, W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | EMBEDDED MEDIA | Wrong media on soft substrate; too aggressive | Use softer media; reduce pressure |
| 2 | 6.33" | RESIDUAL SCALE IN RECESSES | Blast cannot reach internal features | Follow with chemical pickle; vibratory finish |
| 3 | 12.16" | FLASH RUST AFTER BLAST | Humid environment; delay to next step | Process within 4 hrs; keep RH < 60% |
| 4 | 18.0" | PROFILE TOO DEEP | Over-blast with aggressive angular grit | Reduce pressure; increase distance; finer grit |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for descaling and heavy oxide removal on carbon and alloy steels. Specific media, equipment settings, and chemical concentrations vary by application. Consult your process supplier and applicable SSPC/NACE standards. Source: General industry knowledge; SSPC standards.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Descaling / Heavy Oxide Removal -- Process Flow

**Series name:** Inter Regular, 14 pt, `#F0EDE8` at 70%, Center. Y: 34.2"

> Plating Posters Inc -- Metal Finishing Reference Series

**Logo placeholder:** Rectangle, X: 22.5", Y: 33.3", W: 0.83", H: 0.42", fill `#3A4055`. Text: `[LOGO]` -- Inter Regular, 10 pt, `#F0EDE8` at 50%

**Version:** JetBrains Mono Regular, 11 pt, `#F0EDE8` at 50%. X: 0.5", Y: 35.0"

> v1.0 -- 2026

---

## Part 5 -- Grouping and Naming Convention

| Group Name | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline |
| Zone 2 - Decision Tree + Flow | Section labels, decision tree rows, 6-stage flow boxes, arrows |
| Zone 3 - Media Table | Section label, 5-row media selection table |
| Zone 4 - Prep Grades | Section label, four SSPC grade cards |
| Zone 5 - Troubleshooting | Section label, four problem cards |
| Zone 6 - Footer | Footer band, disclaimer, title, series, logo, version |

---

## Part 6 -- Light Edition Color Remap Table

| Dark Hex | Light Hex | Notes |
|----------|-----------|-------|
| `#1A1F2E` | `#F5F4F0` | Background and all BG-colored elements |
| `#F0EDE8` | `#1A1F2E` | All primary text |
| `#1E2435` | `#ECEEF4` | Callout/flow box fills |
| `#252B3D` | `#E8E8F0` | Alternate rows |
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
| `Descaling Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Descaling Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Descaling Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Descaling Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Descaling Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Descaling Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the entire Descaling cluster. The decision tree is the hero -- it answers the question every shop has: "What do I do with THIS kind of scale?" The combination flow (blast + pickle) covers the majority of real-world descaling jobs. The SSPC grades are essential reference material that shops tape to the wall. Flash rust after blasting is the most common time-sensitive failure in descaling -- the 4-hour window must be prominent.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #371 -- Construction Workup v1.0*
*2026-04-26*
