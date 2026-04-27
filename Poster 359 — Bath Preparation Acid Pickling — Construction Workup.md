---
Project: Plating Posters Inc
Poster Number: 359
Title: "Bath Preparation -- Acid Pickling (Carbon Steel)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Chemical Treatment Clusters -- Watson Research Brief (CT-3.3)"
Technical Source: Industry-standard bath preparation and analytical control for HCl and H2SO4 pickling baths. Includes inhibitor chemistry, makeup procedures, analytical methods, and dump criteria.
Process Scope: Bath preparation and control for carbon steel acid pickling
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - AcidPickling
  - CarbonSteel
  - BathPreparation
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT03
---

# Poster #359 -- Construction Workup
## Bath Preparation -- Acid Pickling (Carbon Steel)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This poster covers bath makeup and analytical control for both HCl and H2SO4 pickling baths. The hero is a side-by-side bath composition table for both acids. Pickling inhibitors get their own dedicated section -- they are one of the most important additives in the entire metal finishing process and most operators do not understand why they matter. Analytical control and dump criteria round out the reference.

---

## Part 1 -- Workflow Orientation

### Design Capabilities for This Poster

- Text boxes, rounded rectangles, accent borders, table rows
- Color fills set to exact hex values
- Print-quality export

### Limitations to Flag

1. **Bath composition tables (Block B -- HERO):** Two side-by-side tables (HCl bath, H2SO4 bath).
2. **Inhibitor chemistry section (Block D):** 4-row table with mechanism descriptions.
3. **Analytical control table (Block E):** Parameter/method/frequency table.
4. **Dump criteria table (Block F):** Side-by-side dump parameters for both acids.
5. **Print size -- 24x36".**

---

## Part 2 -- Document Setup Instructions

(Same as Poster #357: 24x36", `#1A1F2E` background, standard fonts, standard palette.)

### Step 5 -- Set ruler guides

**Horizontal guides (from top edge):**
- 0.5" -- top safe zone margin
- 2.9" -- Zone 1/Zone 2 boundary
- 13.5" -- Zone 2/Zone 3 boundary
- 21.0" -- Zone 3/Zone 4 boundary
- 27.5" -- Zone 4/Zone 5 boundary
- 32.5" -- Zone 5/Zone 6 boundary
- 35.5" -- bottom safe zone margin

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- BATH COMPOSITION / HERO (2.9"--13.5" / ~10.6" tall)
  Block B: HCl bath composition table (left)
  Block C: H2SO4 bath composition table (right)

ZONE 3 -- PICKLING INHIBITORS (13.5"--21.0" / ~7.5" tall)
  Block D: Inhibitor chemistry table + importance callout

ZONE 4 -- ANALYTICAL CONTROL & DUMP CRITERIA (21.0"--27.5" / ~6.5" tall)
  Block E: Analytical control table
  Block F: Dump criteria (side-by-side HCl / H2SO4)

ZONE 5 -- MAKEUP PROCEDURE (27.5"--32.5" / ~5.0" tall)
  Block G: Step-by-step makeup procedure

ZONE 6 -- FOOTER BAND (32.5"--36.0" / ~3.5" tall)
  Block H: Disclaimer + poster title + series name + logo placeholder + version
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**BLOCK A -- Headline**
- Barlow Condensed ExtraBold, 88 pt, `#F0EDE8`, letter spacing -4
- Text: `BATH PREPARATION`

**BLOCK A -- Subheading**
- Barlow SemiBold, 36 pt, `#E8A020` (Amber)
- Text: `Acid Pickling -- Carbon Steel`

**BLOCK A -- Tagline**
- Barlow SemiBold, 22 pt, `#F0EDE8` at 65%
- Text: `The acid does the work. The inhibitor protects the part. Control both or pay for scrap.`

---

### ZONE 2 -- Bath Composition (HERO)

**Section label:**
- Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `BATH COMPOSITION -- TWO ACIDS, TWO APPROACHES`

---

**BLOCK B -- HCl Bath Composition (Left)**

- Rounded rect, X: 0.5", Y: 3.8", W: 11.0", H: 9.2", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `HCl PICKLING BATH` -- Barlow SemiBold, 22 pt, `#E8A020`
- Subtitle: `Ambient Temperature Operation` -- Inter Regular, 14 pt, `#F0EDE8` at 50%

Composition table inside callout (3 columns: Component | Concentration | Notes):

| Component | Concentration | Notes |
|---|---|---|
| Hydrochloric acid (HCl) | 15--30% v/v | Start high; replenish as consumed |
| Pickling inhibitor | 0.1--1.0% v/v | Per manufacturer; CRITICAL for high-strength steel |
| Water | Balance | Clean water; avoid high chloride/fluoride |

Operating window:
- JetBrains Mono Regular, 14 pt, `#E8A020`
```
TEMP: 68--95 F (20--35 C) ambient
TIME: 5--30 min (scale-dependent)
AGITATION: None to mild
```

Iron capacity callout:
- Inter Medium, 13 pt, `#2EC4B6`
- Text: `Iron capacity: ~200 g/L FeCl2 -- high capacity before dump`

**BLOCK C -- H2SO4 Bath Composition (Right)**

- Rounded rect, X: 12.0", Y: 3.8", W: 11.5", H: 9.2", fill `#1E2435`
- Left accent: `#2EC4B6`, 0.06"
- Title: `H2SO4 PICKLING BATH` -- Barlow SemiBold, 22 pt, `#2EC4B6`
- Subtitle: `Elevated Temperature Operation` -- Inter Regular, 14 pt, `#F0EDE8` at 50%

| Component | Concentration | Notes |
|---|---|---|
| Sulfuric acid (H2SO4) | 10--25% v/v (~150--400 g/L) | ALWAYS add acid to water -- NEVER reverse |
| Pickling inhibitor | 0.1--1.0% v/v | Acid-stable formulation (acetylenic compounds) |
| Water | Balance | ALWAYS add acid to water |

Operating window:
- JetBrains Mono Regular, 14 pt, `#2EC4B6`
```
TEMP: 120--175 F (50--80 C) HEATED
TIME: 10--45 min (scale-dependent)
AGITATION: Mild air improves uniformity
```

Iron capacity callout:
- Inter Medium, 13 pt, `#E8A020`
- Text: `Iron capacity: ~120 g/L FeSO4 -- lower capacity; dumps sooner`

**Safety callout spanning both columns:**
- Rounded rect, X: 0.5", Y: 12.2", W: 23.0", H: 0.8", fill `#E05C5C` at 12%, border 1 pt `#E05C5C`
- Text: `ALWAYS ADD ACID TO WATER. Adding water to concentrated H2SO4 causes a violent exothermic reaction.` -- Inter Medium, 14 pt, `#E05C5C`, center

---

### ZONE 3 -- Pickling Inhibitors

**Section label:**
- Centered. Y: 13.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `PICKLING INHIBITORS -- THE MOST IMPORTANT ADDITIVE`

**Sublabel:**
- Centered. Y: 14.2". Inter Regular, 16 pt, `#F0EDE8` at 60%
- Text: `Without inhibitor: 5--10x more base metal attack, dramatically higher hydrogen absorption, worse surface finish.`

---

**BLOCK D -- Inhibitor Chemistry Table**

Y: 15.0" to 20.8". Column widths (23.0" total):
- Inhibitor Type (5.5") | Chemistry (5.5") | Mechanism (7.0") | Status (5.0")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

| Inhibitor Type | Chemistry | Mechanism | Status |
|---|---|---|---|
| Quaternary ammonium compounds | Cationic surfactants | Adsorb on clean metal surface, block acid attack | Widely used |
| Acetylenic alcohols | Propargyl alcohol, unsaturated organics | Form protective film; very effective H2 absorption inhibitor | Most common |
| Thiourea derivatives | Sulfur-bearing organics | Extremely effective but generate toxic H2S fumes | Declining use |
| Proprietary blends | Mixtures optimized for specific acids/temps | Combined mechanisms; best overall performance | Industry standard |

Data: Inter Regular, 13 pt, `#F0EDE8`. Type names: Inter Medium, 14 pt. Status column: JetBrains Mono, 12 pt.

---

### ZONE 4 -- Analytical Control & Dump Criteria

**Section label:**
- Centered. Y: 21.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `ANALYTICAL CONTROL & DUMP CRITERIA`

---

**BLOCK E -- Analytical Control Table (Left half)**

- Rounded rect, X: 0.5", Y: 22.0", W: 11.0", H: 5.0", fill `#1E2435`
- Left accent: `#2EC4B6`, 0.06"
- Title: `ANALYTICAL CONTROL` -- Barlow SemiBold, 18 pt, `#2EC4B6`

| Parameter | Method | Frequency |
|---|---|---|
| Free acid (HCl or H2SO4) | Titrate with standardized NaOH | Daily on production lines |
| Total iron (Fe2+ and Fe3+) | Permanganate or dichromate titration; or AA | 2--3x per week |
| Inhibitor concentration | Per manufacturer (colorimetric or SG) | Daily or as directed |

Data: Inter Regular, 13 pt. Parameter names: Inter Medium.

**BLOCK F -- Dump Criteria Table (Right half)**

- Rounded rect, X: 12.0", Y: 22.0", W: 11.5", H: 5.0", fill `#1E2435`
- Left accent: `#E05C5C`, 0.06"
- Title: `DUMP CRITERIA` -- Barlow SemiBold, 18 pt, `#E05C5C`

| Parameter | HCl Bath | H2SO4 Bath |
|---|---|---|
| Free acid below | < 5% HCl | < 5% H2SO4 |
| Iron content above | > 80--120 g/L Fe | > 60--80 g/L Fe |
| Pickle time exceeds | 2--3x normal | 2--3x normal |
| Visual indicator | Dark green/brown; sludge | Dark color; crystal edges |

Data: JetBrains Mono Regular, 12 pt. Parameter names: Inter Medium, 13 pt.

---

### ZONE 5 -- Makeup Procedure

**Section label:**
- Centered. Y: 27.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`
- Text: `BATH MAKEUP PROCEDURE`

---

**BLOCK G -- Step-by-Step Procedure**

Y: 28.4" to 32.3". Single callout box.

- Rounded rect, X: 0.5", Y: 28.4", W: 23.0", H: 3.6", fill `#1E2435`, radius 6
- Left accent: `#E8A020`, 0.06"

Six numbered steps (Inter Regular, 14 pt, `#F0EDE8`, line height 165%):

```
1. Fill tank to 2/3 volume with clean water
2. For H2SO4: Add acid SLOWLY to water with agitation (exothermic -- temperature will rise)
   For HCl: Add acid to water (less exothermic but still add slowly)
3. Bring to operating volume
4. Add pickling inhibitor per manufacturer instructions
5. HCl: Ready at ambient. H2SO4: Heat to 120--175 F before use.
6. Titrate to confirm free acid concentration before first production load
```

Safety reminder:
- Inter Medium, 13 pt, `#E05C5C`
- Text: `NEVER add water to concentrated acid. ALWAYS add acid to water.`

---

### ZONE 6 -- Footer Band

(Same structure as Poster #357.)

**Disclaimer:**
> This poster is an educational reference tool. Bath compositions shown are typical industry values. Specific formulations vary by proprietary product. Consult your process supplier and current SDS before preparing any acid bath.

**Poster title:** `Bath Preparation -- Acid Pickling (Carbon Steel)`

**Version:** `v1.0 -- 2026`

---

## Part 5 -- Grouping and Naming Convention

| Group Name | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline |
| Zone 2 - Bath Composition | Section label, HCl table, H2SO4 table, safety callout |
| Zone 3 - Inhibitors | Section label, sublabel, inhibitor chemistry table |
| Zone 4 - Control & Dump | Section label, analytical table, dump criteria table |
| Zone 5 - Makeup | Section label, step procedure, safety reminder |
| Zone 6 - Footer | Footer band, disclaimer, title, series, logo, version |

---

## Part 6 -- Light Edition Color Remap Table

(Same remap table as Poster #357.)

---

## Part 7 -- Export Checklist

| File Name | Mode | Quality | Bleed |
|---|---|---|---|
| `Bath Prep Acid Pickling Steel -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Bath Prep Acid Pickling Steel -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Bath Prep Acid Pickling Steel -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Bath Prep Acid Pickling Steel -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Bath Prep Acid Pickling Steel -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Bath Prep Acid Pickling Steel -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

The inhibitor section is the sleeper hero of this poster. Most operators think of pickle acid as "just acid" -- they do not understand that the inhibitor is what keeps the process from eating the part alive and loading it with hydrogen. The "5--10x more base metal attack without inhibitor" stat is the kind of number that makes someone sit up and pay attention.

-> Watson: Confirm acetylenic alcohol (propargyl alcohol) is still the most common inhibitor chemistry in current commercial formulations. Thiourea declining due to H2S -- confirm this is industry consensus.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #359 -- Construction Workup v1.0*
*2026-04-26*
