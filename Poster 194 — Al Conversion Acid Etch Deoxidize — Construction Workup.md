---
Project: Plating Posters Inc
Poster Number: 194
Title: "Aluminum Conversion Coating -- Acid Etch / Deoxidize"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Conversion Coating Clusters — Watson Research Brief (CC-06 Section 6.4)"
Technical Source: Acid etch and deoxidize (desmut) stage for Ti/Zr and non-chromate aluminum conversion coating lines. Covers HNO3, HNO3/HF, ferric sulfate, and acidic fluoride activation systems. Alloy-specific chemistry selection.
Process Scope: Aluminum conversion coating -- Stage 3 acid etch / deoxidize (surface conditioning)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ConversionCoating
  - AluminumConversion
  - Deoxidize
  - SurfaceConditioning
  - ConstructionWorkup
  - ClusterCC06
---

# Poster #194 -- Construction Workup
## Aluminum Conversion Coating -- Acid Etch / Deoxidize

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the surface conditioning poster for CC-06. On aluminum, "surface conditioning" means deoxidizing -- stripping away the native aluminum oxide layer and any smut (dark residue from alloying elements) left by cleaning. This exposes a fresh, active aluminum surface for the Ti/Zr conversion reaction.

The critical teaching point: different aluminum alloys produce different smuts. High-copper alloys (2xxx, 7xxx) produce tenacious copper-rich smut that requires HF-containing deoxidizers. Low-alloy grades (6xxx) clean up easily with mild acids. The deoxidizer must be matched to the alloy family.

For multi-metal automotive lines, the deoxidize/activation step may use an acidic fluoride rinse (H2TiF6 or H2ZrF6) that works on all substrates simultaneously.

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

1. **Stage detail panel (Block B -- HERO):** Purpose, mechanism, and general parameters.
2. **Deoxidizer chemistry options table (Block C):** Side-by-side comparison of 4+ deox chemistries.
3. **Alloy-specific selection guide (Block D):** Alloy family -> recommended deoxidizer matrix.
4. **Multi-metal activation callout (Block E):** Acidic fluoride rinse for automotive lines.
5. **Troubleshooting strip (Block F).**

---

## Part 2 -- Document Setup Instructions

Standard: 24x36", `#1A1F2E`, locked palette and fonts. Standard guides.

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- DEOXIDIZE STAGE DETAIL / HERO (2.9"--15.5" / ~12.6" tall)
  Block B: Stage detail panel (mechanism, purpose, critical controls)
  Block C: Deoxidizer chemistry options comparison

ZONE 3 -- ALLOY SELECTION GUIDE (15.5"--22.0" / ~6.5" tall)
  Block D: Alloy family -> deoxidizer matrix

ZONE 4 -- MULTI-METAL ACTIVATION (22.0"--28.5" / ~6.5" tall)
  Block E: Acidic fluoride activation for automotive multi-metal lines

ZONE 5 -- TROUBLESHOOTING QUICK HITS (28.5"--32.5" / ~4.0" tall)
  Block F: 4-problem strip

ZONE 6 -- FOOTER BAND (32.5"--36.0" / ~3.5" tall)
  Block G: Disclaimer + footer
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**BLOCK A -- Headline**
- Font: Barlow Condensed ExtraBold, 76 pt, `#F0EDE8`, letter spacing -4
- Text: `ALUMINUM CONVERSION COATING`
- X: 0.5", Y: 0.5", W: 23.0"

**BLOCK A -- Subheading**
- Font: Barlow SemiBold, 36 pt, `#E8A020` (Amber)
- Text: `Stage 3 -- Acid Etch / Deoxidize`
- Y: 1.5"

**BLOCK A -- Tagline**
- Font: Barlow SemiBold, 20 pt, `#F0EDE8` at 65%
- Text: `Strip the oxide. Remove the smut. Expose fresh aluminum for the conversion reaction. Match the deoxidizer to the alloy.`
- Y: 2.2"

---

### ZONE 2 -- Deoxidize Stage Detail (HERO)

**Section label:**
- Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `ACID ETCH / DEOXIDIZE -- SURFACE ACTIVATION`

---

**BLOCK B -- Stage Detail Panel**

Y: 3.8" to 8.5". Full width within margins.

Large rounded rectangle: X: 0.5", Y: 3.8", W: 23.0", H: 4.5", fill `#1E2435`, radius 8, left accent 0.06" `#E8A020`.

Stage badge:
- Rounded rect 1.8" x 0.4", fill `#E8A020`
- Text: `STAGE 3 -- DEOXIDIZE` -- Barlow Condensed ExtraBold, 14 pt, `#1A1F2E`
- Y: 4.2"

Left side -- What this stage does (Inter Regular 14 pt `#F0EDE8`, line height 160%):
```
1. Dissolves the natural aluminum oxide (Al2O3) layer
   -- This oxide reforms in seconds on bare aluminum
   -- The deoxidizer removes it immediately before coating

2. Removes smut (dark residue from alloying elements)
   -- Copper, silicon, iron, manganese in the alloy
   -- These elements do not dissolve in the cleaner
   -- The deoxidizer dissolves or loosens them

3. Exposes fresh, active aluminum for Zr deposition
   -- The Ti/Zr reaction REQUIRES bare aluminum contact
   -- Oxide or smut = no coating
```

Right side -- Key control callout (rounded rect W: 10.0", H: 2.5", fill `#252B3D`, top accent `#E05C5C`):
- Title: `TIME-CRITICAL` -- Barlow SemiBold, 16 pt, `#E05C5C`
- Body: Inter Medium 14 pt `#F0EDE8`
- Text: `Aluminum re-oxidizes almost instantly in water. Minimize transit time from deoxidize rinse to conversion coating bath -- ideally < 5 minutes. If parts sit in air or water between deox and coating, the fresh oxide layer reforms and coating adhesion suffers.`

---

**BLOCK C -- Deoxidizer Chemistry Options**

Y: 9.0" to 15.0". Four chemistry panels.

| Chemistry | X | W | Accent | Key Data |
|---|---|---|---|---|
| Nitric Acid (HNO3) | 0.5" | 5.5" | `#E8A020` | 30--50% by vol, ambient, 1--5 min. Standard for 6xxx alloys. Does not remove Si or Cu smut alone. |
| Nitric + HF | 6.25" | 5.5" | `#E05C5C` | 30% HNO3 + 1--3% HF, ambient, 30 sec--3 min. Required for high-Cu (2xxx, 7xxx) and cast Al (high Si). HF dissolves Al2O3, SiO2, and Cu-rich smut. SAFETY: HF is extremely hazardous. |
| Non-Chrome (Ferric Sulfate) | 12.0" | 5.5" | `#27AE60` | Per supplier, ambient--120 F, 1--5 min. Cr-free deox for compliance. Good for 6xxx. May need longer contact for 2xxx/7xxx. Growing market share. |
| Acidic Fluoride (ZrF/TiF) | 17.75" | 5.75" | `#2EC4B6` | pH 2.5--4.5, H2TiF6 or H2ZrF6 at 0.1--0.5 g/L, ambient--100 F, 30 sec--2 min. Multi-metal activation for automotive. Works on Al + steel + galvanized. |

Each panel: Rounded rect, H: 5.5", fill `#1E2435`, radius 6, top accent 4 pt.

Interior per panel:
- Chemistry name: Barlow SemiBold 16 pt in accent color
- Concentration: JetBrains Mono 12 pt `#F0EDE8`
- Temp/Time: JetBrains Mono 12 pt `#F0EDE8`
- Best for: Inter Medium 13 pt `#F0EDE8`
- Limitation: Inter Regular 12 pt `#F0EDE8` at 70%

Safety tag on Nitric + HF panel:
- Small rounded rect, fill `#E05C5C`, text `HAZARDOUS -- HF` in Barlow Condensed ExtraBold 11 pt `#F0EDE8`

---

### ZONE 3 -- Alloy Selection Guide

**Section label:**
- Centered. Y: 15.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `ALLOY FAMILY -- DEOXIDIZER SELECTION`

**BLOCK D -- Alloy-Deoxidizer Matrix**

Y: 16.3" to 21.8". Column widths (23.0" total): Alloy Family (3.5") | Examples (3.5") | Smut Character (4.5") | Recommended Deox (5.0") | Notes (6.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.
Data rows: alternating `#1E2435` / `#252B3D`, H: 1.0".

| Alloy Family | Examples | Smut Character | Recommended Deox | Notes |
|---|---|---|---|---|
| 6xxx (low alloy) | 6061, 6063 | Light gray; easy to remove | HNO3 or non-chrome (ferric sulfate) | Most common automotive alloy family |
| 2xxx (high copper) | 2024, 2014 | Dark, Cu-rich; tenacious | HNO3/HF required | Aerospace -- Cu smut resists mild acids |
| 7xxx (zinc-copper) | 7075, 7050 | Dark, Cu-rich; tenacious | HNO3/HF required | Same as 2xxx -- copper drives the chemistry |
| Cast Al (high Si) | 356, A356 | Gray; silicon particles embedded | HNO3/HF (HF dissolves SiO2) | Cast parts need HF to attack Si inclusions |
| Multi-metal (automotive) | Mixed in one line | Varies by substrate | Acidic fluoride (ZrF/TiF) | One activation bath for all substrates |

Data: Inter Regular 13 pt. Alloy examples: JetBrains Mono 12 pt.

---

### ZONE 4 -- Multi-Metal Activation

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `MULTI-METAL ACTIVATION -- ONE BATH, EVERY SUBSTRATE`

**BLOCK E -- Multi-Metal Activation Panel**

Y: 22.9" to 28.3".

**Left -- How It Works:**
- Rounded rect, X: 0.5", Y: 22.9", W: 11.0", H: 5.0", fill `#1E2435`, left accent `#2EC4B6`
- Title: `ACIDIC FLUORIDE ACTIVATION` -- Barlow SemiBold, 20 pt, `#2EC4B6`

Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):
```
Automotive body-in-white lines process steel, galvanized,
and aluminum panels on the same conveyor.

A separate deoxidizer for each substrate is impractical.

Solution: a dilute acidic fluoride rinse containing
H2TiF6 or H2ZrF6 at 0.1--0.5 g/L.

This bath activates ALL substrates simultaneously:
- Dissolves Al2O3 on aluminum
- Activates iron on steel
- Etches zinc oxide on galvanized
```

Parameters (JetBrains Mono 13 pt `#F0EDE8`):
```
pH:          2.5--4.5
Temperature: Ambient to 100 F
Time:        30 sec--2 min
Method:      Spray or immersion
```

**Right -- Substrate Response:**
- Rounded rect, X: 12.0", Y: 22.9", W: 11.5", H: 5.0", fill `#1E2435`, left accent `#E8A020`
- Title: `WHAT HAPPENS ON EACH METAL` -- Barlow SemiBold, 20 pt, `#E8A020`

Three mini callouts inside:

1. `ALUMINUM` -- Amber badge
   `Fluoride dissolves the Al2O3 oxide layer; acid removes smut. Fresh Al exposed for Zr deposition.`

2. `STEEL` -- Teal badge
   `Acid activates the iron surface; removes light oxide. Prepares for Zr deposition on steel.`

3. `GALVANIZED` -- Emerald badge
   `Acid etches zinc oxide; fluoride activates the surface. Zr deposits uniformly on zinc.`

Each mini callout: rounded rect, W: 10.0", H: 1.2", fill `#252B3D`, left accent 0.06" in badge color.

---

### ZONE 5 -- Troubleshooting Quick Hits

**Section label:**
- Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`
- Text: `QUICK TROUBLESHOOTING -- 4 COMMON PROBLEMS`

**BLOCK F -- Four Problem Cards**

Y: 29.4" to 32.3". Same construction as Poster #191.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | DARK SMUT REMAINS | Wrong deoxidizer for alloy; HF needed for Cu/Si alloys | Match deoxidizer to alloy family; add HF if needed |
| 2 | 6.33" | OVER-ETCHED SURFACE | Acid too concentrated; time too long; temp too high | Reduce concentration/time/temp; check solution age |
| 3 | 12.16" | COATING ADHESION FAILURE | Re-oxidation between deox and coating (> 5 min transit) | Minimize transit time; keep parts wet |
| 4 | 18.0" | PITTING ON ALUMINUM | Chloride contamination in deoxidizer; sulfate attack on Cu-alloys | Use chloride-free reagents; check water quality |

---

### ZONE 6 -- Footer Band

Standard footer. Title: `Aluminum Conversion Coating -- Acid Etch / Deoxidize`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Parameters shown are typical for acid etch/deoxidize stages prior to Ti/Zr conversion coating on aluminum. Deoxidizer chemistry must be matched to alloy family and process specification. HF-containing deoxidizers require specialized safety protocols. Consult your process supplier.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Al Conversion Acid Etch Deox -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster is where the alloy-specific complexity of aluminum pretreatment comes alive. The four-panel chemistry comparison and the alloy-deoxidizer matrix are the educational centerpieces. Most shops working with 6xxx alloys may not realize they need HF for 2xxx/7xxx -- and the safety implications of HF are significant. The multi-metal activation section speaks directly to the automotive audience that represents the largest market for Zr conversion coatings.

The time-critical callout about re-oxidation (< 5 min transit) is one of the most important practical tips on any poster in this cluster. Aluminum is not steel -- it re-oxidizes in seconds.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #194 -- Construction Workup v1.0*
*2026-04-26*
