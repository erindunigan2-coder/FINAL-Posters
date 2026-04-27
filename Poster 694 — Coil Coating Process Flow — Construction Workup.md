---
Project: Plating Posters Inc
Poster Number: 694
Title: "Coil Coating -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting Coating Clusters -- Watson Research Brief (Cluster 6: Coil Coating)"
Technical Source: Industry-standard continuous coil coating (prepaint) process. Covers the complete 9-stage sequence from uncoiler through recoiler. Values are typical ranges for steel and aluminum coil at 200-700 ft/min line speed.
Process Scope: Coil coating -- complete process flow (9 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - CoilCoating
  - ProcessFlow
  - ConstructionWorkup
  - PaintingCoating
  - ClusterCC
---

# Poster #694 -- Construction Workup
## Coil Coating -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for Coil Coating (prepaint). The fastest, highest-volume organic coating process in the world -- coating flat metal coil at 200-700 ft/min before it is ever formed into a product. Building panels, appliance housings, beverage cans, garage doors. The coating has to be tough enough to survive roll-forming and stamping after curing. The poster maps the complete line from uncoiler to recoiler.

Design philosophy: horizontal flow diagram (left-to-right, matching actual line direction) as the hero, a compact parameter summary table, a key products panel showing what coil-coated metal becomes, and a troubleshooting quick-hit strip.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Process flow diagram (Block B -- HERO):** Nine rounded rectangles in a horizontal flow (top row L-to-R stages 1-5, vertical connector, bottom row R-to-L stages 6-9). U-flow pattern matching Poster #686.
2. **Parameter summary table (Block D):** Compact 9-row table (one row per stage).
3. **"What Gets Made From Prepainted Coil" panel (Block E):** Product examples with end-use applications.
4. **Troubleshooting quick-hit strip (Block F):** 4 common problems.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 15.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- PROCESS FLOW DIAGRAM / HERO (2.9"--15.5" / ~12.6" tall)
  Block B: Nine-stage U-flow diagram (top row 5, bottom row 4)
  Block C: Stage legend strip

ZONE 3 -- PARAMETER SUMMARY TABLE (15.5"--22.0" / ~6.5" tall)
  Block D: 9-row parameter table

ZONE 4 -- WHAT GETS MADE (22.0"--28.5" / ~6.5" tall)
  Block E: End products of coil coating

ZONE 5 -- TROUBLESHOOTING QUICK HITS (28.5"--32.5" / ~4.0" tall)
  Block F: 4-problem strip

ZONE 6 -- FOOTER BAND (32.5"--36.0" / ~3.5" tall)
  Block G: Standard footer
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**BLOCK A -- Headline**
- Font: Barlow Condensed ExtraBold, 88 pt, `#F0EDE8`
- Position: X: 0.5", Y: 0.5", W: 23.0"
- Text: `COIL COATING`

**BLOCK A -- Subheading**
- Font: Barlow SemiBold, 36 pt, `#E8A020`
- Position: X: 0.5", Y: 1.5", W: 23.0"
- Text: `Complete Process Flow -- 9 Stages from Uncoil to Recoil`

**BLOCK A -- Tagline**
- Font: Barlow SemiBold, 22 pt, `#F0EDE8` at 65%
- Position: X: 0.5", Y: 2.2", W: 23.0"
- Text: `Pre-paint. Pre-form. 200-700 ft/min. The fastest organic coating process in the world -- and the coating still has to survive being bent into a building panel.`

---

### ZONE 2 -- Process Flow Diagram (HERO)

**Section label:**
- Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `THE COMPLETE COIL LINE -- STAGE BY STAGE`

**BLOCK B -- Nine-Stage U-Flow Diagram**

Y: 3.8" to 14.0". Top row of five boxes, bottom row of four boxes.

Each flow box:
- Rounded rectangle, W: 4.2", H: 4.0"
- Fill: `#1E2435`
- Corner radius: 8 pt
- Top border accent: 4 pt colored strip

**Top Row (Y: 3.8" to 7.8") -- Stages 1-5, left to right:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Uncoil / Accumulator | Box 1 | 0.5" | `#2EC4B6` | Setup |
| 2. Clean (Spray + Brush) | Box 2 | 5.1" | `#2EC4B6` | Cleaning |
| 3. Rinse | Box 3 | 9.7" | `#2EC4B6` | Rinse |
| 4. Conversion Coating | Box 4 | 14.3" | `#E8A020` | Treatment |
| 5. Dry / Preheat | Box 5 | 18.9" | `#2EC4B6` | Dry |

**Bottom Row (Y: 9.0" to 13.0") -- Stages 6-9, right to left:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 6. Prime Coat (Roll) | Box 6 | 18.9" | `#E8A020` | Application |
| 7. Prime Oven + Quench | Box 7 | 14.3" | `#27AE60` | Cure |
| 8. Finish Coat (Roll) | Box 8 | 9.7" | `#E8A020` | Application |
| 9. Finish Oven + Quench + Recoil | Box 9 | 5.1" | `#27AE60` | Cure |

Inspection callout card (X: 0.5", Y: 9.0"):
- Same box dimensions, fill `#1E2435`, top accent `#27AE60`
- Badge: `QC` + `IN-LINE + PER COIL`
- Text: DFT / Gloss / Color / T-bend / Adhesion / MEK rub

**Inside each flow box:**

*Box 1 -- Uncoil / Accumulator:*
- Badge: `STAGE 1` fill `#2EC4B6`
- Name: `Uncoil / Accumulator`
- Parameters: `Payoff reel feeds strip` / `Accumulator: continuous run during coil changes` / `Line speed: 200-700 ft/min`
- Check: `Strip threading and tension control`

*Box 2 -- Clean:*
- Badge: `STAGE 2` fill `#2EC4B6`
- Name: `Clean`
- Parameters: `Alkaline spray + brush scrub` / `130-160 F, pH 10-12` / `2-4 brush stages, counter-rotating`
- Check: `Residual oil < 5 mg/m2`

*Box 3 -- Rinse:*
- Badge: `STAGE 3` fill `#2EC4B6`
- Name: `Rinse`
- Parameters: `DI water spray, 2 stages` / `Counterflow design` / `Conductivity < 30 uS/cm final`
- Check: `Water break test on strip samples`

*Box 4 -- Conversion Coating:*
- Badge: `STAGE 4` fill `#E8A020`
- Name: `Conversion Coating`
- Parameters: `Chrome-free Ti/Zr (new standard)` / `Roll-apply or spray` / `5-15 mg/ft2 (nanoceramic)`
- Check: `Coating weight per supplier spec`

*Box 5 -- Dry / Preheat:*
- Badge: `STAGE 5` fill `#2EC4B6`
- Name: `Dry / Preheat`
- Parameters: `IR or convection dryer` / `100-120 F strip temp` / `Completely dry before prime`
- Check: `No water droplets -- causes uneven treatment`

*Box 6 -- Prime Coat:*
- Badge: `STAGE 6` fill `#E8A020`
- Name: `Prime Coat (Roll)`
- Parameters: `Reverse roll coater` / `DFT: 0.15-0.30 mil` / `Roll speed ratio: 1.05-1.25:1`
- Check: `Wet film gauge check; nip pressure`

*Box 7 -- Prime Oven + Quench:*
- Badge: `STAGE 7` fill `#27AE60`
- Name: `Prime Oven + Quench`
- Parameters: `PMT: 400-450 F` / `15-40 sec in oven` / `Water quench to ambient`
- Check: `MEK rub 100+ (full cure)`

*Box 8 -- Finish Coat:*
- Badge: `STAGE 8` fill `#E8A020`
- Name: `Finish Coat (Roll)`
- Parameters: `Reverse roll coater` / `DFT: 0.60-1.0 mil` / `Viscosity: 30-60 sec Zahn #2`
- Check: `Color match; wet film thickness`

*Box 9 -- Finish Oven + Quench + Recoil:*
- Badge: `STAGE 9` fill `#27AE60`
- Name: `Finish Oven + Recoil`
- Parameters: `PMT: 430-480 F` / `20-60 sec in oven` / `Water quench -> recoiler`
- Check: `PMT by IR pyrometer; T-bend; gloss; adhesion`

*QC Callout Card:*
- Badge: `QC` fill `#27AE60`
- Name: `In-Line + Per Coil`
- Parameters: `DFT: beta-backscatter (continuous)` / `Gloss: in-line glossmeter` / `T-bend, hardness, adhesion: per coil`
- Check: `100+ MEK rubs = fully cured`

---

**BLOCK C -- Stage Legend Strip**

Y: 13.5" to 14.3".
Rounded rect fill `#252B3D`, W: 23.0", H: 0.7", radius 4.

| Swatch | Label |
|---|---|
| `#2EC4B6` | `Preparation & Rinse` |
| `#E8A020` | `Application & Treatment` |
| `#27AE60` | `Cure & Inspection` |
| `#E05C5C` | `Caution / Defect` |

---

### ZONE 3 -- Parameter Summary Table

**Section label:** `AT-A-GLANCE PARAMETERS` -- Y: 15.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK D -- 9-Row Parameter Table**

Y: 16.3" to 21.8". Column widths (23.0" total):
- Stage (3.5") | Method (5.0") | Temperature (3.0") | Time (2.5") | Key Metric (4.0") | Key Control (5.0")

| Stage | Method | Temp | Time | Key Metric | Key Control |
|---|---|---|---|---|---|
| 1. Uncoil | Payoff + accumulator | Ambient | Continuous | Line speed 200-700 ft/min | Strip tension |
| 2. Clean | Alkaline spray + brush | 130-160 F | Seconds (at speed) | Oil < 5 mg/m2 | Free alkalinity |
| 3. Rinse | DI spray, 2 stages | Ambient | Seconds | Conductivity < 30 uS/cm | Counterflow |
| 4. Conversion | Ti/Zr or chromate roll-apply | Ambient-110 F | Seconds | Coating weight 5-30 mg/ft2 | Chemistry concentration |
| 5. Dry/Preheat | IR or convection | 100-120 F strip | Seconds | Bone dry | No water droplets |
| 6. Prime Coat | Reverse roll coater | Ambient | At line speed | 0.15-0.30 mil DFT | Roll ratio, nip pressure |
| 7. Prime Oven | Gas-fired convection | PMT 400-450 F | 15-40 sec | MEK 100+ rubs | PMT by IR pyrometer |
| 8. Finish Coat | Reverse roll coater | Ambient | At line speed | 0.60-1.0 mil DFT | Viscosity, roll ratio |
| 9. Finish Oven | Gas-fired convection | PMT 430-480 F | 20-60 sec | T-bend, gloss, adhesion | PMT, afterburner |

---

### ZONE 4 -- What Gets Made

**Section label:** `WHAT GETS MADE FROM PRE-PAINTED COIL` -- Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK E -- Product Applications Grid**

Y: 22.9" to 28.3". Two rows of three callout cards.

Each card: Rounded rect, W: 7.33", H: 2.3", fill `#1E2435`, left accent 0.06".

**Row 1:**

Card 1 (X: 0.5", accent `#E8A020`):
- Title: `BUILDING PANELS` -- Barlow SemiBold, 16 pt, `#E8A020`
- Body: `Roofing, siding, wall panels, curtain walls. PVDF (Kynar 500) for 30-40 year color retention. SMP for 25-30 year economy.` -- Inter Regular, 12 pt, `#F0EDE8`

Card 2 (X: 8.16", accent `#2EC4B6`):
- Title: `APPLIANCES` -- Barlow SemiBold, 16 pt, `#2EC4B6`
- Body: `Refrigerator panels, washer/dryer housings, HVAC enclosures. Polyester or polyurethane for formability and scratch resistance.` -- Inter Regular, 12 pt, `#F0EDE8`

Card 3 (X: 15.83", accent `#27AE60`):
- Title: `GARAGE DOORS` -- Barlow SemiBold, 16 pt, `#27AE60`
- Body: `Embossed and roll-formed from prepainted galvanized coil. Polyester topcoat over epoxy primer. 0T-2T bend flexibility required.` -- Inter Regular, 12 pt, `#F0EDE8`

**Row 2:**

Card 4 (X: 0.5", accent `#E8A020`):
- Title: `GUTTERS & DOWNSPOUTS` -- Barlow SemiBold, 16 pt, `#E8A020`
- Body: `Roll-formed from prepainted aluminum or galvanized coil. Must survive decades of UV and moisture without peeling.` -- Inter Regular, 12 pt, `#F0EDE8`

Card 5 (X: 8.16", accent `#2EC4B6`):
- Title: `BEVERAGE CANS` -- Barlow SemiBold, 16 pt, `#2EC4B6`
- Body: `Exterior decoration coil-coated before stamping. Inks and clear overprint varnish applied by coil coater. Billions of cans per year.` -- Inter Regular, 12 pt, `#F0EDE8`

Card 6 (X: 15.83", accent `#27AE60`):
- Title: `AUTOMOTIVE TRIM` -- Barlow SemiBold, 16 pt, `#27AE60`
- Body: `Door panels, trim pieces, structural liners. Polyurethane for flexibility and impact resistance during stamping.` -- Inter Regular, 12 pt, `#F0EDE8`

---

### ZONE 5 -- Troubleshooting Quick Hits

**Section label:** `QUICK TROUBLESHOOTING -- 4 COMMON PROBLEMS` -- Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK F -- Four Problem Cards**

Y: 29.4" to 32.3". Four cards, gap 0.33".
Each card: W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | COATING CRACKING AFTER FORMING | Insufficient flexibility; overcure or wrong chemistry | Verify T-bend per spec; check PMT (overcure embrittles); switch to higher-flexibility chemistry |
| 2 | 6.33" | DFT VARIATION ACROSS WIDTH | Uneven nip pressure or roll deflection | Check roll alignment; adjust nip pressure profile; inspect roll surface condition |
| 3 | 12.16" | POOR ADHESION | Conversion coating failure or cleaner residue | Check coating weight; verify oil removal < 5 mg/m2; inspect conversion chemistry |
| 4 | 18.0" | COLOR SHIFT BETWEEN COILS | Batch-to-batch coating variation or PMT drift | Verify Delta E < 1.0 per coil; monitor PMT continuously; standardize coating batch |

---

### ZONE 6 -- Footer

Standard footer band. Title: `Coil Coating -- Process Flow`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Process parameters shown are typical industry values for continuous coil coating lines. Specific chemistries, PMT windows, and line speeds vary by coater and coating manufacturer. Consult your coating supplier for application-specific guidance.`

---

## Parts 5--7

**Grouping:** 6 zones per standard layout.
**Light Remap:** Standard table.
**Export:** Six files -- `Coil Coating Process Flow -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Coil coating is the industrial painting world's Formula 1 -- everything happens fast, at scale, and with precision. 200-700 ft/min line speeds. PMTs reached in seconds. The U-flow diagram must convey that sense of speed and scale. The "What Gets Made" panel connects the abstract process to tangible everyday products -- the viewer has seen coil-coated metal every day of their life without knowing it. The troubleshooting strip leads with formability because that is the unique challenge: the coating must survive being bent and stamped AFTER curing.

---

*Alaina -- Poster #694 -- Construction Workup v1.0 -- 2026-04-26*
