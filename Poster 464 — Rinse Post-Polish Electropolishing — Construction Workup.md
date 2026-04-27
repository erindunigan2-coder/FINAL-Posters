---
Project: Plating Posters Inc
Poster Number: 464
Title: "Rinse -- Post-Polish -- Electropolishing"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters — Watson Research Brief (Cluster 7, Sections 7.6--7.8)"
Technical Source: Post-electropolishing rinse stages. Immediate rinse after EP is time-critical -- delay causes staining and streaking from concentrated acid drying on the freshly polished surface. Covers drag-out recovery, DI water requirements, and cascade rinse configuration for post-EP.
Process Scope: Electropolishing -- post-polish rinse (Stage 6 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Electropolishing
  - Rinse
  - PostPolish
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #464 -- Construction Workup
## Rinse -- Post-Polish -- Electropolishing

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the post-polish rinse poster -- arguably the most time-critical rinse in the entire EP process. When a part exits the EP tank, it is coated in concentrated hot phosphoric/sulfuric acid. Every second of delay allows that acid to continue uncontrolled dissolution, dry on the surface, and cause irreversible staining or streaking. The poster's single loudest message: RINSE IMMEDIATELY.

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

1. **Drag-out recovery + cascade rinse diagram (Block B -- HERO):** Two-tank visual showing drag-out recovery tank flowing into clean rinse tank, with timing callout.
2. **Time-critical warning panel (Block C):** Prominent coral callout emphasizing no delay.
3. **Rinse parameter table (Block D):** Compact table for post-EP rinse stages.
4. **Water quality requirements (Block E):** DI water specs for pharma/biotech vs. industrial.
5. **Staining failure examples (Block F):** What happens when rinse is delayed.

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
| Amber | `#E8A020` | Current/voltage parameters, key warnings |
| Teal | `#2EC4B6` | Cleaning & rinse stages, structural positives |
| Emerald | `#27AE60` | Electropolishing stage, optimal reference |
| Coral | `#E05C5C` | Problems, defects, safety callouts |
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
- 4.2" -- Zone 2/Zone 3 boundary
- 14.5" -- Zone 3/Zone 4 boundary
- 22.0" -- Zone 4/Zone 5 boundary
- 28.5" -- Zone 5/Zone 6 boundary
- 32.5" -- Zone 6/Zone 7 boundary
- 35.5" -- bottom safe zone margin

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- SEQUENCE STRIP (2.9"--4.2")
  Stage 6 highlighted (Teal)

ZONE 3 -- POST-POLISH RINSE HERO (4.2"--14.5" / ~10.3")
  Block B: Drag-out recovery + cascade rinse diagram
  Block C: Time-critical warning panel

ZONE 4 -- RINSE PARAMETERS & WATER QUALITY (14.5"--22.0" / ~7.5")
  Block D: Rinse parameter table
  Block E: Water quality requirements by application

ZONE 5 -- WHAT HAPPENS WHEN RINSE FAILS (22.0"--28.5" / ~6.5")
  Block F: Staining/streaking failure modes

ZONE 6 -- DRAG-OUT ECONOMICS (28.5"--32.5" / ~4.0")
  Block G: Acid recovery + waste reduction

ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Dimensions:** Full page width. Y: 0" to 2.9".
**Background:** Same as page (`#1A1F2E`).

---

**BLOCK A -- Headline**

- Element type: Text box
- Position: X: 0.5". Y: 0.5"
- Width: 23.0"
- Font: Barlow Condensed ExtraBold
- Size: 88 pt
- Color: `#F0EDE8`
- Letter spacing: -4
- Text (all caps):

> RINSE -- POST-POLISH

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 36 pt
- Color: `#2EC4B6` (Teal)
- Text:

> Electropolishing -- Stage 6 of 8 -- Immediate Rinse After EP Tank

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8` at 65%
- Text:

> Every second counts. Concentrated hot acid on a freshly polished surface continues dissolving metal uncontrollably until rinsed.

---

### ZONE 2 -- Sequence Orientation Strip

**Dimensions:** Y: 2.9" to 4.2".

Eight mini-boxes in a row. Stage 6 (`Rinse Post-EP`) highlighted: fill `#2EC4B6`, text `#1A1F2E`. All others dimmed: fill `#252B3D`, text `#F0EDE8` at 40%.

Below strip: `Before: Freshly electropolished surface coated in concentrated acid --> After: Acid-free surface ready for neutralization/passivation` -- Inter Regular, 13 pt, `#F0EDE8` at 60%.

---

### ZONE 3 -- Post-Polish Rinse Hero

**Section label:**
- Centered horizontally. Y: 4.4"
- Font: Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`, Center
- Text:

> POST-POLISH RINSE SYSTEM

---

**BLOCK B -- Drag-Out Recovery + Cascade Rinse Diagram**

Y: 5.0" to 11.5" (~6.5" tall).

Three-element visual showing the rinse path from EP tank exit:

**EP Tank (source -- left):**
- Rounded rect, X: 0.5", Y: 5.5", W: 5.5", H: 4.5", fill `#27AE60` at 15%, border 2 pt `#27AE60`
- Label: `EP TANK` Barlow SemiBold 16 pt `#27AE60`
- Sub-label: `H3PO4/H2SO4 at 65--80 C` JetBrains Mono 11 pt `#F0EDE8` at 60%

**Drag-Out Recovery Tank (center):**
- Rounded rect, X: 7.5", Y: 5.5", W: 7.0", H: 4.5", fill `#252B3D`, border 2 pt `#E8A020`
- Label: `DRAG-OUT RECOVERY` Barlow SemiBold 16 pt `#E8A020`
- Interior text (JetBrains Mono 12 pt `#F0EDE8`):
```
Still water (no overflow)
Captures concentrated acid
Return to EP tank when
  specific gravity rises
Reduces chemical cost 20--40%
```

**Clean Rinse Tank (right):**
- Rounded rect, X: 16.0", Y: 5.5", W: 7.5", H: 4.5", fill `#252B3D`, border 2 pt `#2EC4B6`
- Label: `CLEAN RINSE` Barlow SemiBold 16 pt `#2EC4B6`
- Interior text (JetBrains Mono 12 pt `#F0EDE8`):
```
Flowing DI or city water
Cascade overflow to drain
Conductivity target: < 50 uS/cm
Removes all residual acid
```

**Flow arrows between tanks:**
- EP Tank to Drag-Out: Arrow, 3 pt `#3A4055`, arrowhead filled right
- Drag-Out to Clean Rinse: Arrow, 3 pt `#3A4055`, arrowhead filled right
- Label on first arrow: `DRIP 10--15 sec` Inter Medium 12 pt `#E8A020`
- Label on second arrow: `IMMERSE + AGITATE` Inter Medium 12 pt `#2EC4B6`

**Timing callout below diagram (Y: 10.5"):**
- Rounded rect, X: 0.5", W: 23.0", H: 0.8", fill `#E05C5C` at 20%, border 2 pt `#E05C5C`
- Text centered: `TOTAL TIME FROM EP TANK TO CLEAN RINSE: < 30 SECONDS. No air-drying. No delay. No exceptions.` Barlow SemiBold 15 pt `#E05C5C`

---

**BLOCK C -- Time-Critical Warning Panel**

Y: 11.8" to 14.0".

Rounded rect, X: 0.5", W: 23.0", H: 2.0", fill `#1E2435`, left accent 0.06" `#E05C5C`.

Title: `WHY IMMEDIATE RINSE IS NON-NEGOTIABLE` Barlow SemiBold 20 pt `#E05C5C`

Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):

```
1. ACID CONCENTRATION: Drag-out film is full-strength H3PO4/H2SO4. As water evaporates, concentration INCREASES.
2. CONTINUED DISSOLUTION: Uncontrolled etching continues outside the polishing plateau -- causes orange peel and matte spots.
3. STAINING: Dissolved metal salts (Fe, Cr, Ni phosphates) precipitate as the acid dries -- leaves permanent stains.
4. STREAKING: Gravity causes acid to run and pool -- creates visible flow lines on the polished surface.
```

Bottom note: `Even 60 seconds of air exposure at 65 C can cause visible staining on 316L stainless steel.` Inter Medium 13 pt `#E05C5C`

---

### ZONE 4 -- Rinse Parameters & Water Quality

**Section label:**
- Centered. Y: 14.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> RINSE PARAMETERS + WATER QUALITY

---

**BLOCK D -- Rinse Parameter Table (Y: 15.3" to 18.5")**

Table -- columns: Parameter (5.0") | Drag-Out Recovery (8.5") | Clean Rinse (9.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

| Parameter | Drag-Out Recovery | Clean Rinse |
|---|---|---|
| Water type | DI or city water | DI water (pharma); city water (industrial) |
| Temperature | Ambient | Ambient |
| Flow | Static (no overflow) | Flowing cascade or overflow |
| Time | 10--30 sec immersion | 30--60 sec immersion |
| Agitation | Part agitation (dip/withdraw) | Part agitation recommended |
| Conductivity target | N/A (will be high) | < 50 uS/cm |
| pH target | N/A | 6--8 (neutral) |
| Purpose | Recover concentrated acid | Remove all residual acid |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Parameter labels: Inter Medium, 13 pt.

---

**BLOCK E -- Water Quality by Application (Y: 19.0" to 21.8")**

Two side-by-side cards:

**Left -- Industrial EP (X: 0.5", W: 11.0"):**
- Rounded rect, H: 2.5", fill `#1E2435`, left accent `#2EC4B6`
- Title: `INDUSTRIAL` Barlow SemiBold 18 pt `#2EC4B6`
- Body (Inter Regular 13 pt `#F0EDE8`):
```
City water acceptable for both rinse stages
Conductivity < 200 uS/cm adequate
Visual check: no discoloration or residue
Cost-effective for general fabrication
```

**Right -- Pharma/Biotech/Semiconductor (X: 12.0", W: 11.5"):**
- Rounded rect, H: 2.5", fill `#1E2435`, left accent `#27AE60`
- Title: `PHARMA / BIOTECH / SEMICONDUCTOR` Barlow SemiBold 18 pt `#27AE60`
- Body (Inter Regular 13 pt `#F0EDE8`):
```
DI water required: > 1 MOhm-cm (< 1 uS/cm)
ASME BPE requires DI final rinse
Multi-stage cascade: 2--3 tanks minimum
Conductivity monitoring on final rinse tank
SEMI F19 specs for semiconductor
```

---

### ZONE 5 -- What Happens When Rinse Fails

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> WHEN THE RINSE FAILS -- DEFECT GALLERY

---

**BLOCK F -- Four Defect Cards (Y: 22.9" to 28.0")**

2x2 grid:

| Position | Defect | Accent | Description | Root Cause | Prevention |
|---|---|---|---|---|---|
| R1C1 | ACID STAINING | `#E05C5C` | Brown/yellow discoloration, often concentrated at bottom of part | Acid dried on surface; metal phosphates precipitated | Immediate rinse; no air-drying |
| R1C2 | FLOW STREAKS | `#E05C5C` | Visible lines running vertically down the surface | Gravity drain of concentrated acid before rinse | Immerse quickly; do not let acid run |
| R2C1 | WATER SPOTS | `#E8A020` | Circular marks from water droplets drying on surface | Non-DI water for final rinse; slow drying | Use DI water; immediate blow-dry |
| R2C2 | UNEVEN FINISH | `#E8A020` | Matte patches amid bright areas -- inconsistent appearance | Contaminated rinse water; insufficient rinsing | Monitor rinse conductivity; cascade system |

Each card: Rounded rect, W: 11.0", H: 2.3", fill `#1E2435`, left accent 0.06".

Interior per card:
- Defect name: Barlow SemiBold, 16 pt, accent color
- Description: Inter Regular, 12 pt, `#F0EDE8`
- Root Cause: Inter Regular, 12 pt, `#F0EDE8` at 70%
- Prevention: Inter Medium, 12 pt, `#27AE60`

---

### ZONE 6 -- Drag-Out Economics

**Section label:**
- Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`

> DRAG-OUT RECOVERY -- COST AND ENVIRONMENTAL BENEFIT

---

**BLOCK G -- Two-Card Strip (Y: 29.4" to 32.0")**

**Card 1 -- Chemical Recovery (X: 0.5", W: 11.0"):**
- Rounded rect, H: 2.3", fill `#1E2435`, left accent `#27AE60`
- Title: `ACID RECOVERY` Barlow SemiBold 16 pt `#27AE60`
- Body: `Drag-out recovery tank captures 60--80% of carried-out acid. When specific gravity in recovery tank reaches ~1.4, return contents to EP tank. Reduces chemical purchase cost 20--40% annually.` Inter Regular 13 pt `#F0EDE8`

**Card 2 -- Waste Reduction (X: 12.5", W: 11.0"):**
- Rounded rect, H: 2.3", fill `#1E2435`, left accent `#2EC4B6`
- Title: `WASTEWATER REDUCTION` Barlow SemiBold 16 pt `#2EC4B6`
- Body: `Less acid in the rinse water = lower wastewater treatment cost. Phosphoric acid in discharge requires treatment to meet EPA phosphorus limits. Drag-out recovery is the single most effective waste-reduction step in the EP line.` Inter Regular 13 pt `#F0EDE8`

---

### ZONE 7 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Rinse parameters are typical industry values for post-electropolishing rinse of stainless steel. Specific rinse requirements vary by specification (ASME BPE, SEMI F19) and application. Consult your process supplier for site-specific guidance.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Rinse -- Post-Polish -- Electropolishing

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
| Zone 2 - Sequence Strip | 8-stage orientation bar |
| Zone 3 - Rinse Hero | Section label, rinse diagram, timing callout, warning panel |
| Zone 4 - Parameters | Section label, parameter table, water quality cards |
| Zone 5 - Failure Gallery | Section label, four defect cards |
| Zone 6 - Economics | Section label, two benefit cards |
| Zone 7 - Footer | Footer band, disclaimer, title, series, logo, version |

---

## Part 6 -- Light Edition Color Remap Table

| Dark Hex | Light Hex | Notes |
|----------|-----------|-------|
| `#1A1F2E` | `#F5F4F0` | Background and all BG-colored elements |
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

Stage badges: Verify text legibility on darkened fills -- may need `#F5F4F0` text.

---

## Part 7 -- Export Checklist

| File Name | Mode | Quality | Bleed |
|---|---|---|---|
| `Rinse Post-Polish Electropolishing -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Rinse Post-Polish Electropolishing -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Rinse Post-Polish Electropolishing -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Rinse Post-Polish Electropolishing -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Rinse Post-Polish Electropolishing -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Rinse Post-Polish Electropolishing -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

The single loudest message on this poster is RINSE IMMEDIATELY. The timing callout (Block B bottom) must be impossible to miss -- it is the operational equivalent of a fire alarm. The drag-out recovery economics (Zone 6) add business justification: good rinsing practice saves money and reduces wastewater treatment burden. The defect gallery (Zone 5) gives the operator visual anchors for what goes wrong when this step is skipped or delayed.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #464 -- Construction Workup v1.0*
*2026-04-26*
