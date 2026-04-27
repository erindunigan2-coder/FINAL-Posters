---
Project: Plating Posters Inc
Poster Number: 212
Title: "Passivation (Stainless Steel) -- Passivation Bath (Main Stage)"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Conversion Coating Clusters — Watson Research Brief (CC-08 Section 8.6)"
Technical Source: Passivation bath chemistry and operation -- nitric acid and citric acid processes per ASTM A967 and AMS 2700. Covers chemical mechanisms, bath formulations (Nitric Types 1--4, Citric Types 1--4), alloy-specific selection, and film characteristics.
Process Scope: Stainless steel passivation -- Stage 5 passivation bath (main stage)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Passivation
  - StainlessSteel
  - MainStage
  - NitricAcid
  - CitricAcid
  - ConstructionWorkup
  - ClusterCC08
---

# Poster #212 -- Construction Workup
## Passivation (Stainless Steel) -- Passivation Bath (Main Stage)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the main event of the CC-08 cluster -- the passivation bath itself. This poster covers both nitric acid and citric acid passivation with equal weight, presents the ASTM A967 bath types, provides the alloy-specific selection guide, and explains the chemical mechanisms.

The two mechanisms are fundamentally different: nitric acid is an OXIDIZING acid that dissolves iron AND promotes passive film formation simultaneously. Citric acid is a CHELATING acid that only sequesters iron -- passive film formation relies on dissolved oxygen. Both achieve the same endpoint for most alloys. This distinction is the educational centerpiece.

---

## Part 1 -- Workflow Orientation

### Design Capabilities for This Poster

Standard capability set.

### Limitations to Flag

1. **Dual mechanism diagram (Block B -- HERO):** Nitric (oxidizing) vs. citric (chelating) side by side.
2. **ASTM A967 bath types table (Block C):** All 8 bath types (Nitric 1--4, Citric 1--4).
3. **Alloy selection guide (Block D):** Alloy family -> recommended passivation bath.
4. **Film characteristics (Block E).**
5. **Troubleshooting strip (Block F).**

---

## Part 2 -- Document Setup Instructions

Standard: 24x36", `#1A1F2E`, locked palette and fonts. Standard guides.

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- DUAL MECHANISM / HERO (2.9"--15.5" / ~12.6" tall)
  Block B: Nitric vs. citric mechanism diagrams (side by side)
  Block C: ASTM A967 bath types table

ZONE 3 -- ALLOY SELECTION GUIDE (15.5"--22.0" / ~6.5" tall)
  Block D: Alloy family -> recommended bath matrix

ZONE 4 -- FILM CHARACTERISTICS (22.0"--28.5" / ~6.5" tall)
  Block E: What passivation produces (the passive film) + industry trend

ZONE 5 -- TROUBLESHOOTING QUICK HITS (28.5"--32.5" / ~4.0" tall)
  Block F: 4-problem strip

ZONE 6 -- FOOTER BAND (32.5"--36.0" / ~3.5" tall)
  Block G: Disclaimer + footer
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**BLOCK A -- Headline**
- Font: Barlow Condensed ExtraBold, 72 pt, `#F0EDE8`, letter spacing -4
- Text: `PASSIVATION (STAINLESS STEEL)`
- X: 0.5", Y: 0.5", W: 23.0"

**BLOCK A -- Subheading**
- Font: Barlow SemiBold, 36 pt, `#27AE60` (Emerald)
- Text: `Stage 5 -- Passivation Bath (Main Stage)`
- Y: 1.5"

**BLOCK A -- Tagline**
- Font: Barlow SemiBold, 20 pt, `#F0EDE8` at 65%
- Text: `Two acids. Two mechanisms. One goal: remove the free iron and let the chromium do its job.`
- Y: 2.2"

---

### ZONE 2 -- Dual Mechanism (HERO)

**Section label:**
- Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `TWO PATHS TO PASSIVATION`

---

**BLOCK B -- Dual Mechanism Diagram**

Y: 3.8" to 10.0". Two side-by-side mechanism panels.

**Left -- Nitric Acid (HNO3):**
- Rounded rect, X: 0.5", Y: 3.8", W: 11.0", H: 6.0", fill `#1E2435`, left accent `#E8A020`
- Title: `NITRIC ACID (HNO3)` -- Barlow SemiBold, 22 pt, `#E8A020`
- Subtitle: `Oxidizing Acid -- Dissolves AND Oxidizes` -- Inter Regular 14 pt `#F0EDE8` at 60%

Mechanism steps (Inter Regular 13 pt `#F0EDE8`, numbered):
```
1. IRON DISSOLUTION:
   Fe + dilute HNO3 --> Fe(NO3)2 + H2
   Iron dissolves readily in nitric acid.
   Chromium and nickel resist dissolution.

2. OXIDIZING ENVIRONMENT:
   HNO3 is an oxidizing acid -- it ACTIVELY
   promotes Cr2O3 formation while dissolving iron.

3. PASSIVE FILM FORMATION:
   As free iron is removed, the surface becomes
   chromium-enriched. Nitric acid's oxidizing
   power drives Cr + O2 --> Cr2O3 (passive film).

RESULT: Simultaneous iron removal + passive
film formation in one step.
```

**Right -- Citric Acid (C6H8O7):**
- Rounded rect, X: 12.0", Y: 3.8", W: 11.5", H: 6.0", fill `#1E2435`, left accent `#27AE60`
- Title: `CITRIC ACID (C6H8O7)` -- Barlow SemiBold, 22 pt, `#27AE60`
- Subtitle: `Chelating Acid -- Sequesters Iron` -- Inter Regular 14 pt `#F0EDE8` at 60%

Mechanism steps (Inter Regular 13 pt `#F0EDE8`, numbered):
```
1. IRON CHELATION:
   Fe3+ + citrate --> Fe(citrate) complex
   Citric acid chelates free iron from the
   surface, pulling it into solution as a
   stable, soluble complex.

2. NOT AN OXIDIZER:
   Citric acid does NOT provide the oxidizing
   environment. Passive film formation relies
   on DISSOLVED OXYGEN in the solution and air.

3. PASSIVE FILM FORMATION:
   With iron removed, exposed chromium reacts
   with dissolved O2 --> Cr2O3 (passive film).
   Same result, different mechanism.

RESULT: Iron removed by chelation; passive
film forms via dissolved oxygen exposure.
```

---

**BLOCK C -- ASTM A967 Bath Types**

Y: 10.5" to 15.3". Full width table.

Rounded rect, X: 0.5", Y: 10.5", W: 23.0", H: 4.6", fill `#1E2435`, radius 8.

Title: `ASTM A967 BATH TYPES` -- Barlow SemiBold, 18 pt, `#F0EDE8`, Y: 10.8"

Two sub-tables side by side:

**Nitric Acid Baths (left):**

| Type | HNO3 Concentration | Na2Cr2O7 | Temperature | Time Min |
|---|---|---|---|---|
| Nitric 1 | 20--25% vol | 2.0--3.0 oz/gal | 120--130 F | 20 min |
| Nitric 2 | 20--25% vol | None | 120--140 F | 20 min |
| Nitric 3 | 20--45% vol | None | 70--90 F | 30 min |
| Nitric 4 | 20--45% vol | None | 120--140 F | 30 min |

**Citric Acid Baths (right):**

| Type | Citric Acid | Temperature | Time Min |
|---|---|---|---|
| Citric 1 | 4--10% wt | 70--120 F | 4 min |
| Citric 2 | 4--10% wt | 120--150 F | 4--10 min |
| Citric 3 | 4--10% wt | 70--160 F | 4--20 min |
| Citric 4 | 10--20% wt | 70--160 F | 4--20 min |

Data: JetBrains Mono 11 pt. Type labels: Inter Medium 12 pt `#E8A020` (nitric) / `#27AE60` (citric).

Dichromate note below Nitric table: `Nitric 1 uses sodium dichromate (Cr6+). Required for difficult alloys (303, 416). Adds hazardous waste burden.` -- Inter Regular 11 pt `#E05C5C`

---

### ZONE 3 -- Alloy Selection Guide

**Section label:**
- Centered. Y: 15.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `ALLOY FAMILY -- BATH SELECTION GUIDE`

**BLOCK D -- Alloy-Bath Matrix**

Y: 16.3" to 21.8". Full width.

| Alloy Family | Grade Examples | Preferred Bath | Notes |
|---|---|---|---|
| Austenitic (300-series) | 304, 304L, 316, 316L, 321, 347 | Citric 1--3 or Nitric 2/3 | Easy to passivate; high Cr + Ni |
| Ferritic (400-series) | 430, 434, 444 | Nitric 3 or 4 | Moderate; lower Ni, moderate Cr |
| Martensitic (400-series) | 410, 420, 440C | Nitric 1 or 2 (with dichromate) or Citric 4 | Harder to passivate; low Cr (~12%) |
| Precipitation Hardening | 17-4 PH, 15-5 PH, PH 13-8 Mo | Citric or Nitric 2/3 | Similar to austenitic |
| Duplex | 2205, 2507 | Citric or Nitric 3 | Mixed austenite/ferrite; straightforward |
| Free-Machining | 303, 416, 420F | Nitric 1 or 2 (with dichromate) | Sulfur/Se inclusions make passivation difficult; longer times |

Data: Inter Regular 13 pt. Grade examples: JetBrains Mono 12 pt.
Alternating rows: `#1E2435` / `#252B3D`.

Below table:
- Text: `Free-machining grades (303, 416) are the most difficult to passivate. The sulfur and selenium inclusions create preferential attack sites. Nitric 1 (with dichromate) is often the only reliable option. Citric acid may require longer times or higher concentrations.` -- Inter Medium 12 pt `#E8A020`

---

### ZONE 4 -- Film Characteristics

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `WHAT PASSIVATION PRODUCES`

**BLOCK E -- Film Properties + Industry Trend**

Y: 22.9" to 28.3". Two panels.

**Left -- Film Properties:**
- Rounded rect, X: 0.5", Y: 22.9", W: 11.0", H: 5.0", fill `#1E2435`, left accent `#27AE60`
- Title: `THE PASSIVE FILM` -- Barlow SemiBold, 20 pt, `#27AE60`

| Property | Value |
|---|---|
| Composition | Cr2O3-rich amorphous oxide |
| Thickness | 1--5 nm (10--50 Angstroms) |
| Appearance | NONE -- invisible (no color change) |
| Dimensional change | None measurable |
| Self-healing | YES -- reforms in seconds if scratched |
| Bath pH (citric) | 1.5--3.0 (self-buffering) |

Data: JetBrains Mono 12 pt.

Key message: `Passivation does NOT add anything to the surface. It REMOVES contamination and allows the natural passive film to form. The part looks identical before and after.` -- Inter Medium 13 pt `#E8A020`

**Right -- Industry Trend:**
- Rounded rect, X: 12.0", Y: 22.9", W: 11.5", H: 5.0", fill `#1E2435`, left accent `#2EC4B6`
- Title: `THE CITRIC ACID TREND` -- Barlow SemiBold, 20 pt, `#2EC4B6`

Content (Inter Regular 14 pt `#F0EDE8`):
```
Citric acid is gaining market share rapidly:

  SAFETY:     Mild organic acid vs. fuming HNO3
  WASTE:      Non-hazardous, biodegradable
  COST:       Similar or lower per gallon
  REGULATORY: Minimal (no HNO3 fume reporting)
  SPEC:       Full ASTM A967 coverage (Types 5--8)

Citric acid is now an EQUAL option under
ASTM A967 -- not an "alternative."

The industry is moving toward citric for:
  - New installations
  - Shops replacing aging nitric systems
  - Medical and food processing
  - Any application where safety and waste
    reduction matter

Nitric acid remains dominant in:
  - Legacy aerospace programs
  - Free-machining grades
  - Shops with established nitric infrastructure
```

---

### ZONE 5 -- Troubleshooting Quick Hits

**Section label:**
- Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`
- Text: `QUICK TROUBLESHOOTING -- 4 COMMON PROBLEMS`

**BLOCK F -- Four Problem Cards**

Y: 29.4" to 32.3". Same construction.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | CuSO4 TEST FAILURE | Free iron remaining; insufficient time/concentration | Increase time/conc/temp; replace exhausted bath |
| 2 | 6.33" | PITTING DURING PASSIVATION | Chloride contamination; bath temp too high for alloy | Use chloride-free reagents; reduce temp; check water |
| 3 | 12.16" | ETCHING / MATTE FINISH | Acid too strong; temp too high; time too long | Reduce conc/temp/time; try citric for sensitive grades |
| 4 | 18.0" | NON-UNIFORM APPEARANCE | Mixed alloy loads; incomplete cleaning | Separate alloys; improve cleaning; consider electropolish |

---

### ZONE 6 -- Footer Band

Standard footer. Title: `Passivation (Stainless Steel) -- Passivation Bath (Main Stage)`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Bath types per ASTM A967/A967M. Alloy-specific guidance is general -- consult your material supplier and specification for exact bath selection. AMS 2700 references ASTM A967 methods. Consult your process supplier.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Passivation Main Stage -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the crown jewel of the CC-08 cluster. The dual mechanism diagram in Zone 2 is the educational centerpiece -- showing nitric (oxidizing) and citric (chelating) side by side makes the chemical difference immediately clear. The ASTM A967 bath types table gives operators a direct reference to specification requirements.

The alloy selection guide in Zone 3 is the most actionable content -- it answers "which bath do I use for my alloy?" in a single glance. The citric acid trend callout in Zone 4 presents the market shift fairly while noting where nitric remains the better choice.

The Nitric vs. Citric comparison in Poster 207 (Process Flow) introduced the decision. This poster provides the detailed data to make it.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #212 -- Construction Workup v1.0*
*2026-04-26*
