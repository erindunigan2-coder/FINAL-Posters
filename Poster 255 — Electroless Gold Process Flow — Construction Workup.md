---
Project: Plating Posters Inc
Poster Number: 255
Title: "Electroless Gold -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters — Watson Research Brief (Process 6: Electroless Gold)"
Technical Source: Industry-standard electroless gold processes -- covering BOTH immersion gold (displacement/self-limiting) and autocatalytic gold (true electroless). Critical distinction between the two is the central educational purpose of this poster.
Process Scope: Electroless gold -- complete process flow (8 stages)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ElectrolessGold
  - ProcessFlow
  - ConstructionWorkup
  - Series2
  - ENIG
  - ENEPIG
---

# Poster #255 -- Construction Workup
## Electroless Gold -- Process Flow

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for Electroless Gold. The single most important thing this poster must communicate is the CRITICAL DISTINCTION between immersion gold (a displacement reaction that is self-limiting and produces ultra-thin films) and autocatalytic gold (a true electroless process using a reducing agent for unlimited thickness). Most people conflate these two processes. This poster separates them clearly.

Immersion gold is the "gold" in ENIG (Electroless Nickel / Immersion Gold) -- the dominant PCB surface finish. It works by galvanic displacement: gold ions steal electrons from the underlying nickel, depositing gold while dissolving nickel. It stops when the gold layer covers the nickel completely. This is why ENIG gold is only 0.03-0.1 um thick.

Autocatalytic gold uses a chemical reducing agent (DMAB, hypophosphite, or ascorbic acid) and is truly autocatalytic -- deposition continues as long as chemistry is maintained, allowing 1-5+ um deposits for wire bonding and high-reliability electronics.

Design philosophy: U-flow diagram as hero (same 8-stage layout), a prominent "Immersion vs. Autocatalytic" comparison callout that is the real centerpiece, and a black pad mechanism callout in the troubleshooting strip.

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

1. **Process flow diagram (Block B -- HERO):** Eight rounded rectangles in a U-flow. Same geometry as Poster #247.
2. **Parameter summary table (Block D):** 8-row table.
3. **"Immersion vs. Autocatalytic" comparison callout (Block E):** The most important zone on the poster. Two side-by-side callout boxes with clear visual differentiation.
4. **Troubleshooting quick-hit strip (Block F):** 4 problems including BLACK PAD.
5. **Standard layout conventions per Series Design Prompt.**

---

## Part 2 -- Document Setup Instructions

### Step 1 -- Create the document
- Width: **24 inches**. Height: **36 inches**.

### Step 2 -- Set the background color
- **`#1A1F2E`** (Gunmetal Dark)

### Step 3 -- Upload fonts
Standard locked set: Barlow Condensed ExtraBold, Barlow SemiBold, Inter Regular/Medium, JetBrains Mono Regular. Fallback: Courier Prime.

### Step 4 -- Set up color palette
Standard locked palette per Series Design Prompt.

### Step 5 -- Set ruler guides
Standard vertical (0.5", 23.5") and horizontal (0.5", 2.9", 15.5", 22.0", 28.5", 32.5", 35.5") guides.

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

ZONE 4 -- IMMERSION vs. AUTOCATALYTIC (22.0"--28.5" / ~6.5" tall)
  Block E: Critical distinction comparison

ZONE 5 -- TROUBLESHOOTING QUICK HITS (28.5"--32.5" / ~4.0" tall)
  Block F: 4-problem strip with one-line fixes (includes BLACK PAD)

ZONE 6 -- FOOTER BAND (32.5"--36.0" / ~3.5" tall)
  Block G: Disclaimer + poster title + series name + logo placeholder + version
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**BLOCK A -- Headline**
- Position: X: 0.5". Y: 0.5". Width: 23.0"
- Font: Barlow Condensed ExtraBold, 88 pt, `#F0EDE8`, letter spacing -4
- Text: `ELECTROLESS GOLD`

**BLOCK A -- Subheading**
- Y: 1.5". Barlow SemiBold, 36 pt, `#27AE60` (Emerald)
- Text: `Complete Process Flow -- Immersion Gold & Autocatalytic Gold`

**BLOCK A -- Tagline**
- Y: 2.2". Barlow SemiBold, 22 pt, `#F0EDE8` at 65%
- Text: `Two processes share a name but not a mechanism. Know which one you are running -- your solder joints depend on it.`

---

### ZONE 2 -- Process Flow Diagram (HERO)

**Section label:** Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`, Center.
Text: `THE COMPLETE PROCESS -- STAGE BY STAGE`

**BLOCK B -- Eight-Stage U-Flow Diagram**

Y: 3.8" to 14.0". Same geometry as Poster #247.

**Top Row (Y: 3.8" to 8.3") -- Stages 1-4:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Cleaning | Box 1 | 0.5" | `#2EC4B6` (Teal) | Cleaning |
| 2. Rinse (Pre-Act) | Box 2 | 6.0" | `#2EC4B6` (Teal) | Rinse |
| 3. Activation | Box 3 | 11.5" | `#E8A020` (Amber) | Activation |
| 4. Rinse (Pre-Plate) | Box 4 | 17.0" | `#2EC4B6` (Teal) | Rinse |

**Bottom Row (Y: 9.5" to 14.0") -- Stages 5-8:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 5. Gold Deposition | Box 5 | 17.0" | `#27AE60` (Emerald) | Plating |
| 6. Rinse (Post-Plate) | Box 6 | 11.5" | `#2EC4B6` (Teal) | Rinse |
| 7. Post Treatment | Box 7 | 6.0" | `#E8A020` (Amber) | Post-Treatment |
| 8. Dry/Storage | Box 8 | 0.5" | `#E8A020` (Amber) | Post-Treatment |

Arrows and connector: standard U-flow pattern.

**Inside each flow box:**

*Box 1 -- Cleaning:*
- Badge: `STAGE 1`, fill `#2EC4B6`
- Name: `Cleaning`
- Parameters: `Alkaline soak clean` / `60--80 C (140--176 F)` / `3--10 min`
- Purpose: `Remove oils, soils, organic contaminants`
- Check: `No silicate cleaners -- residue causes wire bond failure`

*Box 2 -- Rinse (Pre-Activation):*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Activation`
- Parameters: `DI counterflow` / `Ambient`
- Purpose: `Remove cleaner residue`
- Check: `For ENIG: rinse after EN, before Au`

*Box 3 -- Activation:*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Activation`
- Parameters: `Immersion Au (ENIG): none -- EN is driving force` / `Autocatalytic: Pd activation or Sn/Pd colloidal`
- Purpose: `Create surface for Au deposition`
- Check: `ENIG needs NO activation -- displacement from EN surface` (Emerald)

*Box 4 -- Rinse (Pre-Plate):*
- Badge: `STAGE 4`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Plate`
- Parameters: `DI preferred` / `Ambient`
- Purpose: `Remove drag-in before Au bath`
- Check: `Hypophosphite drag-in = uncontrolled Au reduction`

*Box 5 -- Gold Deposition (Main Tank):*
- Badge: `STAGE 5`, fill `#27AE60`
- Name: `Gold Deposition` / Subtitle: `Main Tank`
- Parameters: `Immersion: 0.5--2.0 g/L Au, 80--90 C, 5--15 min` / `Autocatalytic: 1--5 g/L Au, 60--80 C, per spec` / `Immersion: 0.03--0.1 um (self-limiting)` / `Autocatalytic: 1--5+ um`
- Purpose: `Deposit gold -- by displacement or by reducing agent`
- Check: `Know your process: immersion STOPS; autocatalytic CONTINUES`

*Box 6 -- Rinse (Post-Plate):*
- Badge: `STAGE 6`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Post-Plate`
- Parameters: `DI counterflow` / `Gold recovery rinse first!`
- Purpose: `Remove Au bath drag-out; stop reaction`
- Check: `Gold recovery rinse = economic necessity at $80--100+/g`

*Box 7 -- Post Treatment:*
- Badge: `STAGE 7`, fill `#E8A020`
- Name: `Post Treatment`
- Parameters: `ENIG/ENEPIG: no heat treatment` / `Autocatalytic: optional anneal 150--200 C for wire bonding`
- Purpose: `Application-specific finishing`
- Check: `Store ENIG in N2 or vacuum-sealed`

*Box 8 -- Dry/Storage:*
- Badge: `STAGE 8`, fill `#E8A020`
- Name: `Dry / Storage`
- Parameters: `Air knife + oven 60--80 C` / `N2 atmosphere or vacuum bags`
- Purpose: `Remove moisture; prevent contamination`
- Check: `Shelf life 6--12 months (spec-dependent)`

---

**BLOCK C -- Stage Legend Strip**
Y: 14.3" to 15.3". Standard legend per Poster #247.

---

### ZONE 3 -- Parameter Summary Table

**Section label:** Y: 15.7". `AT-A-GLANCE PARAMETERS`

**BLOCK D -- 8-Row Parameter Table**

Y: 16.3" to 21.8". Column widths: Stage (3.5") | Chemistry (5.5") | Temperature (3.0") | Time (2.5") | Thickness (4.0") | Key Control (4.5")

| Stage | Chemistry | Temp | Time | Thickness | Key Control |
|---|---|---|---|---|---|
| 1. Cleaning | Alkaline soak + surfactant | 60--80 C | 3--10 min | -- | No silicate cleaners |
| 2. Rinse | DI counterflow | Ambient | 30--60 sec | -- | <50 uS/cm |
| 3. Activation | ENIG: none; Auto: Pd or Sn/Pd | Varies | Varies | -- | Substrate-dependent |
| 4. Rinse | DI counterflow | Ambient | 30--60 sec | -- | Remove hypo drag-in |
| 5. Gold Deposition | Au 0.5--5.0 g/L | 60--90 C | 5--15 min (imm) | 0.03--5+ um | Immersion vs. autocatalytic |
| 6. Rinse | DI + recovery rinse | Ambient | 30--60 sec | -- | Gold recovery critical |
| 7. Post Treatment | Application-specific | Varies | Varies | -- | ENIG: no HT |
| 8. Dry/Storage | Air knife + oven | 60--80 C | Per spec | -- | N2 or vacuum storage |

---

### ZONE 4 -- Immersion vs. Autocatalytic Gold

**Section label:** Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
Text: `THE CRITICAL DISTINCTION -- IMMERSION vs. AUTOCATALYTIC`

**BLOCK E -- Side-by-Side Comparison**

Y: 22.9" to 28.3".

**Left -- Immersion Gold (Displacement):**
- Rounded rect, X: 0.5", Y: 22.9", W: 11.0", H: 5.2", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `IMMERSION GOLD (DISPLACEMENT)` Barlow SemiBold, 20 pt, `#E8A020`
- Subtitle: `Self-Limiting -- NOT Autocatalytic` Barlow Condensed ExtraBold, 14 pt, `#E05C5C`

| Property | Value |
|---|---|
| Mechanism | Galvanic displacement: Ni dissolves, Au deposits |
| Reaction | 3 Ni0 + 2 Au3+ --> 3 Ni2+ + 2 Au0 |
| Reducing agent | NONE -- Ni substrate IS the reductant |
| Self-limiting | YES -- stops when Au covers Ni |
| Thickness | 0.03--0.1 um (30--100 nm) |
| Bath Au conc. | 0.5--2.0 g/L |
| Temperature | 80--90 C (176--194 F) |
| pH | 4.5--6.0 (acid) or 7.0--8.0 (neutral) |
| Application | ENIG, ENEPIG surface finish |
| Risk | BLACK PAD if Ni over-corroded |

Bottom highlight:
- Fill `#E8A020` at 15%, border 1 pt `#E8A020`
- `ENIG standard -- IPC-4552B. Ultra-thin, cost-effective, solderable. Black pad is the existential risk.` Inter Medium, 13 pt, `#E8A020`

**Right -- Autocatalytic Gold (True Electroless):**
- Rounded rect, X: 12.0", Y: 22.9", W: 11.5", H: 5.2", fill `#1E2435`
- Left accent: `#27AE60`, 0.06"
- Title: `AUTOCATALYTIC GOLD (TRUE ELECTROLESS)` Barlow SemiBold, 20 pt, `#27AE60`
- Subtitle: `Continuous Deposition -- Uses Reducing Agent` Barlow Condensed ExtraBold, 14 pt, `#27AE60`

| Property | Value |
|---|---|
| Mechanism | Chemical reduction: Au+ reduced by DMAB, hypo, or ascorbic acid |
| Reaction | Au+ + reducing agent --> Au0 + byproducts |
| Reducing agent | DMAB, hypophosphite, ascorbic acid, thiosulfate |
| Self-limiting | NO -- continues as long as chemistry maintained |
| Thickness | 1--5+ um |
| Bath Au conc. | 1--5 g/L |
| Temperature | 60--80 C (140--176 F) |
| pH | 6.0--8.0 (neutral to slightly alkaline) |
| Application | Wire bonding pads, high-reliability electronics |
| Risk | High cost; bath instability |

Bottom highlight:
- Fill `#27AE60` at 15%, border 1 pt `#27AE60`
- `Thick gold for wire bonding and high-reliability contacts. Expensive -- bath economics are critical.` Inter Medium, 13 pt, `#27AE60`

---

### ZONE 5 -- Troubleshooting Quick Hits

**Section label:** Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`
Text: `QUICK TROUBLESHOOTING -- 4 CRITICAL PROBLEMS`

**BLOCK F -- Four Problem Cards**

Y: 29.4" to 32.3". Four cards in a row. Gap: 0.33".

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | BLACK PAD | Aggressive immersion Au over-corrodes Ni; P-enriched interface | Control Au concentration, temp, pH; verify EN P% per IPC-4552B |
| 2 | 6.33" | THIN GOLD (ENIG) | Low Au concentration or short immersion time | Replenish Au; extend time; check bath activity |
| 3 | 12.16" | SKIP PLATING (AUTO) | Poor activation on non-catalytic substrate | Verify Pd activation; check catalytic surface |
| 4 | 18.0" | BATH DECOMPOSITION (AUTO) | Low stabilizer, overheating, contamination | Check stabilizer ppm; reduce temp; filter bath |

Interior: Problem in Barlow SemiBold 16 pt `#E05C5C`. Cause in Inter Regular 13 pt `#F0EDE8`. Fix in Inter Medium 13 pt `#27AE60`.

---

### ZONE 6 -- Footer Band

Standard footer. Title: `Electroless Gold -- Process Flow`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Process parameters are typical industry values. Immersion gold and autocatalytic gold are distinct processes with different mechanisms. Consult IPC-4552B (ENIG), IPC-4556 (ENEPIG), and your process supplier.`

---

## Part 5 -- Grouping and Naming Convention

| Group Name | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline |
| Zone 2 - Process Flow | Section label, eight flow boxes, arrows, legend strip |
| Zone 3 - Parameter Table | Section label, 8-row table |
| Zone 4 - Immersion vs Autocatalytic | Section label, two comparison callouts |
| Zone 5 - Troubleshooting | Section label, four problem cards |
| Zone 6 - Footer | Footer band, disclaimer, title, series, logo, version |

---

## Part 6 -- Light Edition Color Remap Table

Standard remap table per Series Design Prompt.

---

## Part 7 -- Export Checklist

| File Name | Mode | Quality | Bleed |
|---|---|---|---|
| `Electroless Gold Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Electroless Gold Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Electroless Gold Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Electroless Gold Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Electroless Gold Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Electroless Gold Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

Zone 4 is the heart of this poster. The immersion vs. autocatalytic distinction is the single most misunderstood concept in electroless gold plating. The left panel (immersion gold) should visually feel "thinner" or "lighter" to reinforce that it produces ultra-thin films. The right panel (autocatalytic) should feel "heavier" to convey thick deposits. The BLACK PAD card in the troubleshooting strip is the number one quality concern in ENIG worldwide -- it deserves the first position.

---

*Alaina -- Poster #255 -- Construction Workup v1.0 -- 2026-04-26*
