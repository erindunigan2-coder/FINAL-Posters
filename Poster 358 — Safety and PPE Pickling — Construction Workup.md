---
Project: Plating Posters Inc
Poster Number: 358
Title: "Safety & PPE -- Acid Pickling (Carbon Steel)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Chemical Treatment Clusters -- Watson Research Brief (CT-3.2)"
Technical Source: Industry-standard safety and PPE requirements for HCl and H2SO4 pickling of carbon steel. OSHA PELs, ACGIH TLVs, GHS hazard classifications, and emergency procedures.
Process Scope: Safety and PPE for carbon steel acid pickling
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - AcidPickling
  - CarbonSteel
  - Safety
  - PPE
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT03
---

# Poster #358 -- Construction Workup
## Safety & PPE -- Acid Pickling (Carbon Steel)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This poster covers the complete safety picture for carbon steel acid pickling -- chemical hazards for HCl and H2SO4, PPE requirements, ventilation, hydrogen gas explosion risk, and emergency first aid. The hero is a full-body PPE diagram with callouts. The hydrogen gas warning is prominent -- pickling generates H2 at 4--75% explosive range.

Design philosophy: PPE diagram as hero, chemical hazard table for both acids, ventilation requirements, emergency procedures, and a hydrogen gas explosion warning strip. This poster saves lives -- every element must be unmissable.

---

## Part 1 -- Workflow Orientation

### Design Capabilities for This Poster

- Text boxes with precise font, size, weight, color, and spacing control
- Solid-color rectangles and rounded rectangles for callout panels, table rows, and accent borders
- Color fills set to exact hex values
- Background page color set to exact hex
- Export at print-quality PDF (300 DPI equivalent via print export)

### Limitations to Flag

1. **PPE diagram (Block B -- HERO):** Stylized full-body figure using geometric shapes (rectangles, circles, rounded rects). Callout lines point to each PPE item. Not a photograph -- built from simple shapes in the series industrial style.

2. **Chemical hazard table (Block D):** 4-row table for HCl, H2SO4, H2 gas, and iron salts.

3. **Hydrogen gas warning banner (Block E):** Full-width coral-tinted glass banner with explosion hazard callout.

4. **Emergency procedures (Block F):** Four emergency cards (skin, eyes, inhalation, spill).

5. **4 pt left-border accents on callout boxes:** Same technique as all previous posters.

6. **Print size -- 24x36".**

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
- **JetBrains Mono Regular** -- all parameter data, chemical formulas, version number

If JetBrains Mono upload fails, substitute **Courier Prime**.

### Step 4 -- Set up color palette

(Same palette as Poster #357 -- see standard palette table.)

### Step 5 -- Set ruler guides

**Vertical guides (from left edge):**
- 0.5" -- left safe zone margin
- 23.5" -- right safe zone margin

**Horizontal guides (from top edge):**
- 0.5" -- top safe zone margin
- 2.9" -- Zone 1/Zone 2 boundary
- 14.0" -- Zone 2/Zone 3 boundary
- 20.5" -- Zone 3/Zone 4 boundary
- 24.5" -- Zone 4/Zone 5 boundary
- 32.5" -- Zone 5/Zone 6 boundary
- 35.5" -- bottom safe zone margin

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- PPE DIAGRAM / HERO (2.9"--14.0" / ~11.1" tall)
  Block B: Full-body PPE figure with callouts
  Block C: PPE requirements list

ZONE 3 -- CHEMICAL HAZARD TABLE (14.0"--20.5" / ~6.5" tall)
  Block D: Chemical hazard table (4 chemicals)

ZONE 4 -- HYDROGEN GAS WARNING (20.5"--24.5" / ~4.0" tall)
  Block E: Explosion hazard banner + ventilation requirements

ZONE 5 -- EMERGENCY PROCEDURES (24.5"--32.5" / ~8.0" tall)
  Block F: Four emergency procedure cards

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
- Font: Barlow Condensed ExtraBold, 88 pt, `#F0EDE8`, letter spacing -4
- Text (all caps):

> SAFETY & PPE

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Font: Barlow SemiBold, 36 pt, `#E05C5C` (Coral)
- Text:

> Acid Pickling -- Carbon Steel

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Font: Barlow SemiBold, 22 pt, `#F0EDE8` at 65%
- Text:

> HCl fumes corrode everything they touch. H2 gas explodes. Respect the pickle tank.

---

### ZONE 2 -- PPE Diagram (HERO)

**Dimensions:** Y: 2.9" to 14.0" (~11.1" tall).

---

**Section label:**
- Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> REQUIRED PERSONAL PROTECTIVE EQUIPMENT

---

**BLOCK B -- PPE Figure with Callouts**

Y: 3.8" to 12.5". Centered on page.

Stylized human figure (geometric shapes): head circle, body rectangle, arm/leg rectangles. Gray fill (`#3A4055`) with PPE items highlighted in color.

Six callout boxes arranged around the figure, connected by 2 pt lines (`#C8D0D8`):

| Callout | Position | PPE Item | Color | Detail |
|---|---|---|---|---|
| 1 | Upper-left | Full-Face Shield + Goggles | `#E05C5C` | Chemical splash goggles AND face shield; HCl fumes attack eyes |
| 2 | Upper-right | Respirator | `#E05C5C` | HCl: half-face with OV/AG cartridge; H2SO4: P100 filter for acid mist |
| 3 | Mid-left | Acid-Resistant Gloves | `#E8A020` | PVC or butyl rubber -- NOT nitrile alone (degrades in concentrated HCl) |
| 4 | Mid-right | Acid-Resistant Apron | `#E8A020` | Full-length chemical apron |
| 5 | Lower-left | Acid-Resistant Boots | `#E8A020` | Steel-toe with chemical-resistant soles |
| 6 | Lower-right | Ventilation | `#2EC4B6` | Local exhaust at tank rim -- push-pull hood or slot ventilation |

Each callout box:
- Rounded rect, W: 4.5", H: 1.2", fill `#1E2435`, radius 6
- Left accent: 0.06", color per callout
- PPE item name: Barlow SemiBold, 16 pt, callout color
- Detail: Inter Regular, 12 pt, `#F0EDE8`

**BLOCK C -- PPE Summary Strip**

Y: 12.8" to 13.8"
- Rounded rect, X: 0.5", Y: 12.8", W: 23.0", H: 0.8", fill `#E05C5C` at 15%, border 1 pt `#E05C5C`, radius 4
- Text: `NO EXPOSED SKIN in the pickle area. Acid burns are immediate. HCl fume damage is cumulative.` -- Inter Medium, 15 pt, `#E05C5C`, center

---

### ZONE 3 -- Chemical Hazard Table

**Dimensions:** Y: 14.0" to 20.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 14.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> CHEMICAL HAZARDS -- KNOW WHAT YOU ARE WORKING WITH

---

**BLOCK D -- 4-Row Hazard Table**

Y: 15.0" to 20.3". Column widths (23.0" total):
- Chemical (5.0") | Hazard (6.0") | Exposure Limit (5.5") | GHS (6.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 1.1".

| Chemical | Hazard | Exposure Limit | GHS Signal |
|---|---|---|---|
| Hydrochloric acid (HCl) 15--35% | Corrosive; toxic HCl gas fumes at ALL temperatures | OSHA PEL: 5 ppm ceiling; ACGIH TLV: 2 ppm ceiling | GHS05 Corrosion + GHS06 Toxic |
| Sulfuric acid (H2SO4) 10--25% | Corrosive; violent exotherm when mixing with water; acid mist | OSHA PEL: 1 mg/m3 (mist) | GHS05 Corrosion |
| Hydrogen gas (H2) | Explosive at 4--75% concentration in air | LEL 4% / UEL 75% -- widest explosive range of any common gas | Flammable gas |
| Iron chloride / Iron sulfate | Low acute toxicity; environmental concern; regulated waste | N/A (low acute) | GHS07 Irritant |

Data: Inter Regular, 13 pt, `#F0EDE8`. Chemical names: Inter Medium, 14 pt, `#F0EDE8`. GHS: JetBrains Mono Regular, 12 pt.

---

### ZONE 4 -- Hydrogen Gas Warning

**Dimensions:** Y: 20.5" to 24.5" (~4.0" tall).

---

**BLOCK E -- Explosion Hazard Banner**

Full-width banner:
- Rounded rect, X: 0.5", Y: 20.7", W: 23.0", H: 3.5", fill `#E05C5C` at 12%, border 2 pt `#E05C5C`, radius 8

Left section (icon area, W: 3.0"):
- Triangle warning icon: simple geometric triangle with exclamation mark, stroke `#E05C5C`, 2 pt

Right section (text, W: 19.0"):

Title:
- Barlow Condensed ExtraBold, 32 pt, `#E05C5C`
- Text: `HYDROGEN GAS -- EXPLOSION HAZARD`

Body (Inter Regular, 15 pt, `#F0EDE8`, line height 155%):
```
Acid + iron = hydrogen gas. H2 is explosive at 4--75% in air -- the widest
flammable range of any common gas. A single spark near an unventilated pickle
tank can cause a catastrophic explosion.
```

Ventilation requirement:
- Inter Medium, 14 pt, `#E8A020`
- Text: `VENTILATION IS NOT OPTIONAL. Local exhaust ventilation at the tank rim is required for ALL acid pickling operations.`

---

### ZONE 5 -- Emergency Procedures

**Dimensions:** Y: 24.5" to 32.5" (~8.0" tall).

---

**Section label:**
- Centered. Y: 24.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> EMERGENCY FIRST AID

---

**BLOCK F -- Four Emergency Cards**

Y: 25.4" to 32.3". 2x2 grid layout. Gap: 0.4".

Each card: Rounded rect, W: 11.0", H: 3.2", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | Position | Emergency | Action |
|---|---|---|---|
| 1 | Top-left (X: 0.5", Y: 25.4") | SKIN CONTACT | Flush immediately with large volumes of water for 15+ minutes. Do NOT attempt to neutralize acid on skin (exothermic risk). Remove contaminated clothing. Seek medical attention. |
| 2 | Top-right (X: 12.0", Y: 25.4") | EYE CONTACT | Flush with eyewash station for minimum 15 minutes. Hold eyelids open during flush. Seek IMMEDIATE medical attention. |
| 3 | Bottom-left (X: 0.5", Y: 29.0") | HCl INHALATION | Move to fresh air immediately. If breathing difficulty, administer oxygen if available. Seek medical attention. Do NOT re-enter area without respiratory protection. |
| 4 | Bottom-right (X: 12.0", Y: 29.0") | ACID SPILL | Contain with absorbent material. Neutralize residual with soda ash (Na2CO3) or lime. Ventilate area. Do NOT use water on large H2SO4 spills (exothermic). |

Interior per card:
- Emergency type: Barlow SemiBold, 18 pt, `#E05C5C`
- Action text: Inter Regular, 13 pt, `#F0EDE8`, line height 150%

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool and does not replace site-specific safety training, SDS review, or compliance with OSHA regulations. Exposure limits shown are OSHA PEL and ACGIH TLV values current at time of publication. Always consult current SDS for each chemical in your shop.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Safety & PPE -- Acid Pickling (Carbon Steel)

**Series name:** Inter Regular, 14 pt, `#F0EDE8` at 70%, Center. Y: 34.2"

> Plating Posters Inc -- Metal Finishing Reference Series

**Logo placeholder:** Rectangle, X: 22.5", Y: 33.3", W: 0.83", H: 0.42", fill `#3A4055`. Text: `[LOGO]`

**Version:** JetBrains Mono Regular, 11 pt, `#F0EDE8` at 50%. X: 0.5", Y: 35.0"

> v1.0 -- 2026

---

## Part 5 -- Grouping and Naming Convention

| Group Name | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline |
| Zone 2 - PPE Diagram | Section label, PPE figure, callouts, summary strip |
| Zone 3 - Chemical Hazards | Section label, 4-row hazard table |
| Zone 4 - H2 Warning | Explosion hazard banner with ventilation req |
| Zone 5 - Emergency | Section label, four emergency cards |
| Zone 6 - Footer | Footer band, disclaimer, title, series, logo, version |

---

## Part 6 -- Light Edition Color Remap Table

(Same remap table as Poster #357.)

---

## Part 7 -- Export Checklist

| File Name | Mode | Quality | Bleed |
|---|---|---|---|
| `Safety PPE Pickling Steel -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Safety PPE Pickling Steel -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Safety PPE Pickling Steel -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Safety PPE Pickling Steel -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Safety PPE Pickling Steel -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Safety PPE Pickling Steel -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

Safety posters must be unmissable. The coral accent dominates this poster by design. The hydrogen gas warning banner is the single most important element -- H2 at 4--75% explosive range is genuinely terrifying, and many shop workers do not know their pickle tank is generating it. The PPE figure must be readable from 8+ feet -- this is the poster that gets hung next to the tank.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #358 -- Construction Workup v1.0*
*2026-04-26*
