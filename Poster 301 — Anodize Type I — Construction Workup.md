---
Project: Plating Posters Inc
Poster Number: 301
Title: "Anodize -- Chromic Acid Anodizing (Type I) -- Main Tank"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 3, Section 3.7)"
Process Scope: Chromic acid anodize main tank -- Stage 6 of 8
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Anodizing
  - ChromicAcid
  - TypeI
  - MainTank
  - ConstructionWorkup
  - ClusterAnodize03
---

# Poster #301 -- Construction Workup
## Anodize -- Chromic Acid Anodizing (Type I) -- Main Tank

*Alaina -- Plating Posters Inc*
*v1.0 -- 2026-04-26*

Stage 6 of 8. The heart of the process. This is the most content-dense poster in the Type I cluster. The defining feature of chromic acid anodizing is the 5-step voltage ramp profile -- this is the hero visual. Unlike Type II (constant current), Type I is voltage-controlled. The thin, fatigue-friendly coating and the self-healing Cr(VI) reservoir make this process unique. The Cr(VI) safety content is extensive and non-negotiable on this poster.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Voltage ramp profile hero (Block B):** A stepped graph showing the 5-step ramp (0->5V->20V->hold->40V->hold). This is THE defining visual of chromic acid anodizing.
2. **Tank cross-section with operating parameters (Block C):** CrO3 bath with cathode/anode setup.
3. **Contamination thresholds table (Block D):** Bath chemistry limits.
4. **Defect grid (Block F):** 4 main-tank failure modes.
5. **Cr(VI) safety panel (Block G):** Extensive safety content -- engineering controls, PPE, waste.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 6 highlighted (Emerald)
ZONE 3 -- VOLTAGE RAMP + TANK HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- BATH CHEMISTRY + CONTAMINATION (14.5"--20.5" / ~6.0")
ZONE 5 -- DEFECT GRID + TYPE IB VARIANT (20.5"--26.5" / ~6.0")
ZONE 6 -- Cr(VI) SAFETY PANEL (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ANODIZE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Chromic Acid (Type I) -- Main Tank -- Stage 6 of 8` -- 32 pt `#27AE60`. Y: 1.4".
**Tagline:** `Voltage ramp to 40V. CrO3 electrolyte. The thinnest anodize film in the book -- and the only one with a self-healing Cr(VI) reservoir.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

**Cr(VI) flag:** Standard coral badge.

---

### ZONE 2 -- Orientation Strip

Stage 6 highlighted: fill `#27AE60`, text `#1A1F2E`.
Below: `Before: Clean, desmutted aluminum  -->  After: 2--7 um anodic oxide (MIL min 0.5 um) with residual Cr(VI) corrosion protection`

---

### ZONE 3 -- Voltage Ramp + Tank Hero

**Section label:** `THE CHROMIC ACID ANODIZE TANK` -- Y: 4.4".

**BLOCK B -- 5-Step Voltage Ramp Profile (LEFT, X: 0.5", W: 12.0")**

Y: 5.0" to 13.0".

Stepped line graph showing voltage (Y-axis, 0--40V) vs. time (X-axis, 0--60 min):

| Step | Time | Voltage | Duration |
|---|---|---|---|
| 1 | 0--5 min | 0 to 5V | 5 min ramp |
| 2 | 5--10 min | 5 to 20V | 5 min ramp |
| 3 | 10--15 min | Hold at 20V | 5 min hold |
| 4 | 15--25 min | 20 to 40V | 10 min ramp |
| 5 | 25--60 min | Hold at 40V | 20--35 min hold |

Graph construction:
- Background: `#1E2435` rounded rect, border 1 pt `#3A4055`
- Y-axis: `0V` to `40V` labels, JetBrains Mono 12 pt `#F0EDE8` at 60%
- X-axis: `0` to `60 min` labels, same
- Gridlines: 1 pt `#3A4055` at 30%
- Ramp line: 3 pt `#27AE60` solid
- Hold segments: 3 pt `#E8A020` solid
- Step labels: Barlow SemiBold 12 pt at each segment

**Below graph:**
- `Type I: Voltage-controlled -- NOT current-controlled` Inter Medium 14 pt `#27AE60`
- `Current density (3--10 ASF) is self-limiting -- do not set current` Inter Regular 13 pt `#F0EDE8` at 80%
- `The ramp prevents burning. Applying 40V instantly burns edges and protrusions.` Inter Medium 13 pt `#E05C5C`

**BLOCK C -- Tank Cross-Section (RIGHT, X: 13.0", W: 10.5")**

Y: 5.0" to 13.0".

Tank body: Rounded rect, W: 9.5", H: 6.5", fill `#252B3D`, border 2 pt `#C8D0D8`.

Anode (parts, center): Rect, fill `#27AE60` at 25%, border 2 pt `#27AE60`.
Cathodes (left and right): Rects, fill `#C8D0D8`.
- Label: `LEAD OR STAINLESS CATHODES` JetBrains Mono 11 pt
- Sub-label: `NO lead-antimony -- Sb contaminates bath` Inter Regular 10 pt `#E05C5C`

Bath parameters inside tank:
- `CrO3: 40--80 g/L (5--10 oz/gal)` JetBrains Mono 13 pt `#27AE60`
- `Temp: 89--100 F (32--38 C)` JetBrains Mono 13 pt `#E8A020`
- `Film: 2--7 um typical (MIL min 0.5 um / 0.02 mil)` JetBrains Mono 13 pt `#F0EDE8`
- `Time: 30--60 min (incl. ramp)` JetBrains Mono 12 pt `#F0EDE8` at 70%

Tank material note: `PVC-lined, polypropylene, or lead-lined steel` Inter Regular 11 pt `#F0EDE8` at 60%

---

### ZONE 4 -- Bath Chemistry + Contamination

**Two-column layout (Y: 14.7" to 20.3"):**

**Left -- Bath Chemistry Table (X: 0.5", W: 11.0"):**

Section label: `BATH CHEMISTRY CONTROL` Barlow Condensed ExtraBold 22 pt.

| Parameter | Control Range | Notes |
|---|---|---|
| CrO3 | 40--80 g/L (5--10 oz/gal) | Typical target: 50--60 g/L |
| Temperature | 89--100 F (32--38 C) | > 40 C: dissolution dominates growth |
| Voltage | Ramp to 40V (Type I) / 22V max (Type IB) | Voltage-controlled |
| Dissolved Al | < 10 g/L preferred | Monitor and adjust |
| Cr3+ | < 20 g/L (some specs: < 5% of total Cr) | Reduces efficiency |
| MIL-A-8625F minimum thickness | 0.5 um (0.02 mil) | Thinnest anodize spec |

**Right -- Contamination Thresholds (X: 12.0", W: 11.5"):**

Section label: `CONTAMINATION LIMITS` Barlow Condensed ExtraBold 22 pt.

| Contaminant | Limit | Effect |
|---|---|---|
| Sulfate (SO4 2-) | < 0.5 g/L | Promotes dissolution; thins coating |
| Chloride (Cl-) | < 25 ppm (tight: < 10 ppm) | Pitting attack |
| Cr3+ | < 20 g/L | Reduces current efficiency; soft coating |
| Dissolved Al | < 10 g/L | Gray coatings; reduced thickness |
| Organics | Zero | Reduce Cr(VI) to Cr(III) |

Threshold values: JetBrains Mono 12 pt `#E05C5C`.

---

### ZONE 5 -- Defect Grid + Type IB Variant

**Left -- Defect Grid (X: 0.5", W: 12.5", 2x2):**

Section label: `WHAT GOES WRONG -- 4 ANODIZE FAILURES`

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | BURNING | `#E05C5C` | Voltage applied too fast (ramp skipped) | Follow 5-step ramp exactly |
| R1C2 | THIN/NO COATING | `#E8A020` | Sulfate > 0.5 g/L; high Cr3+; high temp | Analyze bath; cool; control Cr3+ |
| R2C1 | DISCOLORATION | `#E8A020` | High dissolved Al; organic contamination | Partial dump; carbon treat |
| R2C2 | SOFT COATING | `#2EC4B6` | Excessive Cr3+; temperature too high | Monitor Cr3+/total Cr ratio |

**Right -- Type IB Variant (X: 13.5", W: 10.0"):**

Amber-tinted callout, fill `#1E2435`, left accent `#E8A020`:
- Title: `TYPE IB -- LOW VOLTAGE VARIANT` Barlow SemiBold 18 pt `#E8A020`
- `Maximum 22V (vs. 40V for standard Type I)` JetBrains Mono 14 pt `#E8A020`
- `Used for complex geometry and assemblies with crevices` Inter Regular 13 pt `#F0EDE8`
- `Lower voltage reduces burning risk in recessed areas` Inter Regular 13 pt `#F0EDE8`
- `Allows electrolyte to penetrate blind holes and lap joints` Inter Regular 13 pt `#F0EDE8`
- `MIL-A-8625F Type IB; AMS 2473` JetBrains Mono 12 pt `#F0EDE8` at 60%
- `Thinner coating than standard Type I -- even more fatigue-friendly` Inter Medium 13 pt `#27AE60`

---

### ZONE 6 -- Cr(VI) Safety Panel

**Section label:** `HEXAVALENT CHROMIUM -- SAFETY REQUIREMENTS` -- Y: 26.7".

Full-width coral-tinted panel, fill `#E05C5C` at 10%, border 2 pt `#E05C5C`, Y: 27.3" to 32.3":

**Three-column safety layout:**

*Column 1 -- Engineering Controls (X: 0.8", W: 7.0"):*
- Title: `ENGINEERING CONTROLS` Barlow SemiBold 16 pt `#E05C5C`
- `Enclosed tanks with lids` Inter Regular 13 pt
- `Chromic acid mist suppressants (PFOS-free)` Inter Regular 13 pt
- `HEPA filtration on exhaust` Inter Regular 13 pt
- `Local exhaust ventilation at tank rim` Inter Regular 13 pt
- `Continuous air monitoring recommended` Inter Regular 13 pt

*Column 2 -- PPE (X: 8.3", W: 7.0"):*
- Title: `PERSONAL PROTECTION` Barlow SemiBold 16 pt `#E05C5C`
- `Respiratory: P100 half-face or supplied air` Inter Regular 13 pt
- `Eyes: chemical splash goggles + face shield` Inter Regular 13 pt
- `Hands: Cr(VI)-rated gloves (neoprene/butyl)` Inter Regular 13 pt
- `Body: Cr(VI)-rated apron or suit` Inter Regular 13 pt
- `No skin exposure to electrolyte` Inter Regular 13 pt

*Column 3 -- Regulatory (X: 15.8", W: 7.7"):*
- Title: `REGULATORY` Barlow SemiBold 16 pt `#E05C5C`
- `OSHA PEL: 0.005 mg/m3 (8-hr TWA)` JetBrains Mono 13 pt `#E05C5C`
- `IARC Group 1 carcinogen` Inter Medium 13 pt
- `Medical surveillance: REQUIRED (1910.1026)` Inter Medium 13 pt
- `Waste: EPA hazardous D007` Inter Medium 13 pt
- `Cr(VI) -> Cr(III) reduction before discharge` Inter Regular 13 pt

**Bottom callout:**
- `The self-healing property of Type I comes from residual Cr(VI) in the sealed coating. If scratched, Cr(VI) leaches into the scratch and passivates the aluminum. No other anodize process does this. This is why aerospace still uses chromated coatings despite the regulatory burden.` Inter Medium 13 pt `#F0EDE8`

---

### ZONE 7 -- Footer

Standard. Title: `Anodize -- Chromic Acid Anodizing (Type I) -- Main Tank`. Version `v1.0 -- 2026`.

Disclaimer: `Parameters per MIL-A-8625F Type I and AMS 2470. Cr(VI) safety requirements are regulatory minimums. Consult facility EHS program and applicable OEM specifications.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Anodize Type I -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The voltage ramp profile is the hero visual that defines chromic acid anodizing. No other anodize process uses a multi-step voltage ramp -- it is THE distinguishing operational feature. The graph must be clear and readable at 6 feet. The Cr(VI) safety panel on this poster is the most detailed in the cluster because this is the stage where Cr(VI) exposure risk is highest. The self-healing callout at the bottom is the "why" that justifies the regulatory burden -- it is a technically elegant property that no replacement (including BSAA) can replicate.

---

*Alaina -- Plating Posters Inc*
*Poster #301 -- Construction Workup v1.0*
*2026-04-26*
