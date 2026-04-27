---
Project: Plating Posters Inc
Poster Number: 287
Title: "Hardcoat Anodizing (Type III) -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 2: Type III)"
Technical Source: Industry-standard hardcoat anodizing per MIL-A-8625F Type III. Covers the complete 8-stage sequence from cleaning through seal. Same H2SO4 electrolyte as Type II but near-freezing temperature and high current density produce an engineering-grade wear-resistant oxide.
Process Scope: Hardcoat anodizing (Type III) -- complete process flow (8 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Anodizing
  - TypeIII
  - Hardcoat
  - ProcessFlow
  - ConstructionWorkup
  - ClusterAnodize
---

# Poster #287 -- Construction Workup
## Hardcoat Anodizing (Type III) -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for Hardcoat Anodizing (Type III). It shows the complete 8-stage process sequence at a glance. The concept hook mirrors Poster #279: same H2SO4 electrolyte as Type II, but near-freezing temperature (0--5 C) and double the current density (24--36 ASF) produce a completely different film -- thick (25--100+ um), hard (400--600+ HV, harder than mild steel), and wear-resistant enough for hydraulic cylinders and aerospace components. Temperature control is THE challenge -- refrigeration required. Current ramp-up protocol prevents burning.

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

1. **Process flow diagram (Block B -- HERO):** Eight rounded rectangles in a U-flow. Key difference from Type II: the etch box notes "Light or no etch" and the anodize box shows 0--5 C and 24--36 ASF.
2. **Parameter summary table (Block D).**
3. **"Same Chemistry, Different Film" concept callout (Block E):** Type III vs. Type II side-by-side -- same electrolyte, near-freezing temp, double the current.
4. **Alloy thickness limits callout (Block F):** Critical -- 2024 and 7075 crack above ~50 um.
5. **Troubleshooting quick-hit strip (Block G).**

---

## Part 2 -- Document Setup Instructions

### Step 1 -- Create the document
- Width: **24 inches**. Height: **36 inches**.

### Step 2 -- Set the background color
- **`#1A1F2E`** (Gunmetal Dark)

### Step 3 -- Upload fonts
Standard locked fonts: Barlow Condensed ExtraBold, Barlow SemiBold, Inter Regular/Medium, JetBrains Mono Regular.

### Step 4 -- Set up color palette
Standard locked palette.

### Step 5 -- Set ruler guides
Standard guides: 0.5" / 2.9" / 15.5" / 22.0" / 28.5" / 32.5" / 35.5"

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

ZONE 4 -- SAME CHEMISTRY, DIFFERENT FILM (22.0"--28.5" / ~6.5" tall)
  Block E: Type III vs. Type II side-by-side
  Block F: Alloy thickness limits callout

ZONE 5 -- TROUBLESHOOTING QUICK HITS (28.5"--32.5" / ~4.0" tall)
  Block G: 4-problem strip with one-line fixes

ZONE 6 -- FOOTER BAND (32.5"--36.0" / ~3.5" tall)
  Block H: Disclaimer + poster title + series name + logo placeholder + version
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**BLOCK A -- Headline**
- Font: Barlow Condensed ExtraBold, 80 pt, `#F0EDE8`, letter spacing -4
- Text: `HARDCOAT ANODIZING`

**BLOCK A -- Subheading**
- Font: Barlow SemiBold, 36 pt, `#E8A020` (Amber)
- Text: `Type III -- Complete Process Flow -- 8 Stages from Clean to Seal`

**BLOCK A -- Tagline**
- Font: Barlow SemiBold, 22 pt, `#F0EDE8` at 65%
- Text: `The engineering workhorse. Same electrolyte as Type II -- but near freezing and twice the current. Harder than mild steel. MIL-A-8625F Type III.`

---

### ZONE 2 -- Process Flow Diagram (HERO)

**Section label:** `THE COMPLETE PROCESS -- STAGE BY STAGE`

**BLOCK B -- Eight-Stage U-Flow Diagram**

**Top Row (Y: 3.8" to 8.3") -- Stages 1-4:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Alkaline Clean | Box 1 | 0.5" | `#2EC4B6` (Teal) | Cleaning |
| 2. Rinse (Pre-Etch) | Box 2 | 6.0" | `#2EC4B6` (Teal) | Rinse |
| 3. Etch (Light or None) | Box 3 | 11.5" | `#E8A020` (Amber) | Etch |
| 4. Desmut | Box 4 | 17.0" | `#E8A020` (Amber) | Chemical Treatment |

**Bottom Row (Y: 9.5" to 14.0") -- Stages 5-8:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 5. Rinse (Pre-Anodize) | Box 5 | 17.0" | `#2EC4B6` (Teal) | Rinse |
| 6. Hard Anodize (Main) | Box 6 | 11.5" | `#E8A020` (Amber) | Anodize |
| 7. Rinse (Post-Anodize) | Box 7 | 6.0" | `#2EC4B6` (Teal) | Rinse |
| 8. Seal | Box 8 | 0.5" | `#E8A020` (Amber) | Post-Treatment |

Standard arrows and vertical connector per Poster #279 pattern.

**Inside each flow box:**

*Box 1 -- Alkaline Clean:*
- Badge: `STAGE 1`, fill `#2EC4B6`
- Name: `Alkaline Clean`
- Parameters: `130--160 F (55--70 C)` / `30--60 g/L (4--8 oz/gal)` / `2--10 min soak`
- Purpose: `Remove oils, compounds, fingerprints`
- Check: `EVEN MORE CRITICAL for hardcoat -- defects amplified by thick coating`

*Box 2 -- Rinse (Pre-Etch):*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Etch`
- Parameters: `Ambient temp` / `Cascade preferred`
- Purpose: `Remove cleaner before etch`
- Check: `Same as Type II`

*Box 3 -- Etch (Light or None):*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Etch` / Subtitle: `LIGHT OR NONE`
- Parameters: `Full: NaOH 40--80 g/L, 1--3 min` / `Light: NaOH 20--40 g/L, 30--60 sec` / `None: skip to desmut`
- Purpose: `Surface prep (if dimensional tolerance allows)`
- Check: `PRECISION PARTS: skip etch -- caustic removes 0.5--1.0 mil/min` (Coral `#E05C5C`)

*Box 4 -- Desmut:*
- Badge: `STAGE 4`, fill `#E8A020`
- Name: `Deoxidize / Desmut`
- Parameters: `HNO3 25--50% v/v` / `HF for Cu alloys` / `Ambient, 30--180 sec`
- Purpose: `Remove etch smut completely`
- Check: `Trapped smut under hard coat = delamination` (Coral `#E05C5C`)

*Box 5 -- Rinse (Pre-Anodize):*
- Badge: `STAGE 5`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Anodize (CRITICAL)`
- Parameters: `DI water, triple cascade` / `<100 uS/cm target` / `60--120 sec`
- Purpose: `Prevent electrolyte contamination`
- Check: `F- dragover amplified at hard coat CD -- catastrophic pitting` (Coral `#E05C5C`)

*Box 6 -- Hard Anodize (Main Tank):*
- Badge: `STAGE 6`, fill `#E8A020`
- Name: `Hard Anodize` / Subtitle: `Main Tank`
- Parameters: `H2SO4 150--200 g/L` / `28--41 F (0--5 C) -- REFRIGERATION` / `24--36 ASF (ramp up!)` / `30--120 min`
- Purpose: `Grow thick, hard anodic oxide (25--100+ um)`
- Check: `TEMPERATURE IS EVERYTHING -- chiller required` (Amber `#E8A020`)

*Box 7 -- Rinse (Post-Anodize):*
- Badge: `STAGE 7`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Post-Anodize`
- Parameters: `DI water preferred` / `Remove residual acid`
- Purpose: `Prepare for seal`
- Check: `Standard rinse`

*Box 8 -- Seal:*
- Badge: `STAGE 8`, fill `#E8A020`
- Name: `Seal`
- Parameters: `Hot DI: 205--212 F, 20+ min` / `Ni acetate: 167--185 F` / `PTFE: for low friction`
- Purpose: `Corrosion protection or friction reduction`
- Check: `PTFE seal: CoF drops from 0.4--0.6 to 0.08--0.15`

**BLOCK C -- Stage Legend Strip**
Standard pattern per Poster #279.

---

### ZONE 3 -- Parameter Summary Table

**Section label:** `AT-A-GLANCE PARAMETERS`

| Stage | Chemistry | Temp | Time | Key Control |
|---|---|---|---|---|
| 1. Alkaline Clean | Non-silicated alk cleaner 30--60 g/L | 130--160 F | 2--10 min | Defects amplified by thick coat |
| 2. Rinse (Pre-Etch) | City or DI water | Ambient | 30--60 sec | Cascade preferred |
| 3. Etch | NaOH 20--80 g/L or SKIP | 130--150 F | 0--3 min | Dimensional tolerance drives decision |
| 4. Desmut | HNO3 25--50% (+HF for Cu alloys) | Ambient | 30--180 sec | Complete removal -- no trapped smut |
| 5. Rinse (Pre-Anodize) | DI water (<50 uS/cm) | Ambient | 60--120 sec | Triple cascade for aerospace |
| 6. Hard Anodize | H2SO4 150--200 g/L | 28--41 F | 30--120 min | 24--36 ASF; CURRENT RAMP |
| 7. Rinse (Post-Anodize) | DI water | Ambient | 30--60 sec | Standard rinse |
| 8. Seal | Hot DI or Ni acetate or PTFE | 167--212 F | 20--30 min | Application-specific seal choice |

---

### ZONE 4 -- Same Chemistry, Different Film + Alloy Limits

**Section label:** `SAME CHEMISTRY, DIFFERENT FILM -- TYPE III VS. TYPE II`

**BLOCK E -- Side-by-Side Comparison**

**Left -- Type III (This Poster):**
- Left accent: `#E8A020`, 0.06"
- Title: `TYPE III -- HARDCOAT` Barlow SemiBold 20 pt `#E8A020`
- Subtitle: `The Engineering Workhorse`

| Property | Value |
|---|---|
| Electrolyte | H2SO4 150--200 g/L |
| Temperature | 28--41 F (0--5 C) -- NEAR FREEZING |
| Current density | 24--36 ASF (CURRENT RAMP) |
| Film thickness | 25--100+ um (1.0--4.0+ mil) |
| Hardness | 400--600+ HV -- harder than mild steel |
| Dyeable | Dark colors only |
| Abrasion (Taber) | 1--5 mg/1000 cycles |
| MIL spec | MIL-A-8625F Type III |

Bottom highlight: `Refrigeration required. Current ramp protocol prevents burning.` `#E8A020`

**Right -- Type II (Companion):**
- Left accent: `#27AE60`, 0.06"
- Title: `TYPE II -- SULFURIC ACID` Barlow SemiBold 20 pt `#27AE60`
- Subtitle: `The Decorative Workhorse`

| Property | Value |
|---|---|
| Electrolyte | H2SO4 150--200 g/L (SAME) |
| Temperature | 64--72 F (18--22 C) -- room temp |
| Current density | 12--18 ASF |
| Film thickness | 5--25 um (0.2--1.0 mil) |
| Hardness | 200--350 HV |
| Dyeable | YES -- full color spectrum |
| Abrasion (Taber) | 15--25 mg/1000 cycles |
| MIL spec | MIL-A-8625F Type II |

Bottom highlight: `Same electrolyte -- temperature and current make ALL the difference` `#27AE60`

**BLOCK F -- Alloy Thickness Limits**

Below the comparison (Y: ~27.0" to 28.3"):
- Rounded rect, full width, H: 1.2", fill `#E05C5C` at 12%, border 1 pt `#E05C5C`
- Title: `ALLOY THICKNESS LIMITS` Barlow SemiBold 16 pt `#E05C5C`
- Content: `2024: max ~50 um (cracks above) | 7075: max ~50 um (Zn causes brittleness) | 6061: 75--100+ um (best hard coat alloy) | Cast (high Si): NOT RECOMMENDED`
- JetBrains Mono 13 pt `#F0EDE8`

---

### ZONE 5 -- Troubleshooting Quick Hits

**Section label:** `QUICK TROUBLESHOOTING -- 4 COMMON PROBLEMS`

| Card | Problem | Cause | Fix |
|---|---|---|---|
| 1 | BURNING | Excessive CD, no current ramp, sharp edges | Use ramp protocol; round edges; reduce CD |
| 2 | CRACKING / SPALLING | Thickness exceeds alloy limit; trapped smut | Stay within alloy limits; improve desmut |
| 3 | POWDERING | Temperature >41 F (>5 C) -- control failure | STOP IMMEDIATELY; check chiller; cool bath |
| 4 | NON-UNIFORM THICKNESS | Inadequate agitation; heat buildup zones | Increase agitation; check for dead spots |

Standard card construction per Poster #279.

---

### ZONE 6 -- Footer Band

Standard. Title: `Hardcoat Anodizing (Type III) -- Process Flow`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; MIL-A-8625F; AMS 2469; ASM Handbook Vol. 5. Alloy-specific limits vary; consult your metallurgist for critical applications.`

---

## Part 5 -- Grouping and Naming Convention

| Group Name | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline |
| Zone 2 - Process Flow | Section label, eight flow boxes, arrows, legend strip |
| Zone 3 - Parameter Table | Section label, 8-row table |
| Zone 4 - Type III vs II + Alloy Limits | Section label, comparison callouts, alloy limits strip |
| Zone 5 - Troubleshooting | Section label, four problem cards |
| Zone 6 - Footer | Footer band, disclaimer, title, series, logo, version |

---

## Part 6 -- Light Edition Color Remap Table

Standard remap per Poster #279.

---

## Part 7 -- Export Checklist

| File Name | Mode | Quality | Bleed |
|---|---|---|---|
| `Hardcoat Anodizing Type III Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Hardcoat Anodizing Type III Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Hardcoat Anodizing Type III Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Hardcoat Anodizing Type III Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Hardcoat Anodizing Type III Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Hardcoat Anodizing Type III Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This poster mirrors the Type II process flow (#279) in structure but the content differences are dramatic. The etch stage says "light or none" instead of the full caustic etch. The anodize stage shows near-freezing temperature and a current ramp protocol. The alloy thickness limits strip is unique to Type III -- 2024 and 7075 crack above ~50 um, making them the poster's most important safety-of-process callout. The Type III vs. Type II comparison should visually rhyme with #279's comparison but with Type III on the left (as the "this poster" subject).

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #287 -- Construction Workup v1.0*
*2026-04-26*
