---
Project: Plating Posters Inc
Poster Number: 317
Title: "Anodize -- PAA (Bonding Surface)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 5: PAA, Section 5.7)"
Technical Source: Phosphoric acid anodize main tank. H3PO4 100--120 g/L, 20--25 C, 10--15V (BAC 5555: 10V +/- 1V), 20--25 min. Produces open columnar whisker-like pore structure for adhesive mechanical interlocking. Bond strength > 40 MPa.
Process Scope: Anodize -- PAA main tank (Stage 6 of PAA sequence)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Anodizing
  - PAA
  - MainTank
  - Anodize
  - ConstructionWorkup
  - ClusterAnodPAA
---

# Poster #317 -- Construction Workup
## Anodize -- PAA (Bonding Surface)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 6 of the PAA sequence. This is the heart of the PAA process -- the tank where the open, columnar oxide structure is grown. Unlike Type II or Type III anodizing, the goal is NOT a thick, protective coating. The goal is a specific pore morphology -- whisker-like protrusions 10--50 nm tall that provide mechanical interlocking for structural adhesives. The oxide is intentionally thin (0.5--1.5 um) and intentionally porous.

Hero visual: a PAA anodize tank cross-section with labeled components, plus a pore morphology diagram showing the whisker structure.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **PAA tank cross-section hero (Block B):** Tank with anode (workpiece), counter-electrode (cathode), voltage-controlled power supply, and labeled parameters. Built with rectangles, lines, arrows.
2. **Pore morphology diagram (Block C):** Cross-section of PAA oxide showing open columnar pores with whisker tips -- the key visual for this poster.
3. **Operating window panel (Block D):** All critical parameters.
4. **How PAA creates bond surfaces (Block E):** The mechanism explained.
5. **Failure modes grid (Block F):** 4 common PAA anodize failures.

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
ZONE 3 -- PAA TANK HERO + PORE MORPHOLOGY (4.2"--14.5" / ~10.3")
ZONE 4 -- OPERATING WINDOW (14.5"--20.5" / ~6.0")
ZONE 5 -- HOW PAA CREATES BOND SURFACES (20.5"--26.5" / ~6.0")
ZONE 6 -- FAILURE MODES + CONTAMINATION (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ANODIZE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `PAA Bonding Surface -- Stage 6 of 7` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `Grow the whiskers. 10--15 volts, 20 minutes, and you have the best adhesive bonding surface in aerospace.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 6 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean, contaminant-free aluminum surface  -->  After: Open-pore PAA oxide with whisker morphology (0.5--1.5 um)`

---

### ZONE 3 -- PAA Tank Hero + Pore Morphology

**Section label:** `THE PHOSPHORIC ACID ANODIZE TANK` -- Y: 4.4".

**BLOCK B -- Tank Cross-Section (Left Half)**

X: 0.5", Y: 5.0", W: 12.0", H: 8.5".

**Tank body:**
- Rounded rect, X: 1.0", Y: 5.5", W: 11.0", H: 6.5"
- Fill: `#252B3D` (H3PO4 solution)
- Border: 2 pt `#C8D0D8`

**Anode / Workpiece (center of tank):**
- Vertical rect, X: 5.5", Y: 6.0", W: 1.5", H: 5.0"
- Fill: `#27AE60` at 30%, border 2 pt `#27AE60`
- Label above: `ANODE (+) — WORKPIECE` Barlow SemiBold 12 pt `#27AE60`

**Cathode / Counter-electrode (both sides):**
- Two vertical rects, X: 2.0" and 9.5", Y: 6.0", W: 0.8", H: 5.0"
- Fill: `#C8D0D8` at 40%, border 1 pt `#C8D0D8`
- Label: `STAINLESS STEEL or CARBON` JetBrains Mono 10 pt `#C8D0D8`
- Sub-label: `(NOT aluminum -- dissolves in H3PO4)` Inter Regular 10 pt `#E05C5C`

**Power supply (above tank):**
- Small rect, X: 4.5", Y: 5.0", W: 3.5", H: 0.6", fill `#1E2435`, border 1 pt `#E8A020`
- Text: `VOLTAGE-CONTROLLED DC` Barlow SemiBold 11 pt `#E8A020`

**Bath parameters inside tank:**
- `H3PO4: 100--120 g/L` JetBrains Mono 12 pt `#27AE60`
- `Temp: 20--25 C (68--77 F)` JetBrains Mono 12 pt `#F0EDE8`
- `Voltage: 10--15V` JetBrains Mono 12 pt `#E8A020`
- `BAC 5555: 10V +/- 1V` JetBrains Mono 11 pt `#E8A020`
- `Time: 20--25 min` JetBrains Mono 12 pt `#F0EDE8`

**BLOCK C -- Pore Morphology Diagram (Right Half)**

X: 13.0", Y: 5.0", W: 10.5", H: 8.5".

- Rounded rect background, fill `#1E2435`
- Title: `PAA OXIDE PORE STRUCTURE` Barlow Condensed ExtraBold 18 pt `#F0EDE8`
- Subtitle: `The whisker morphology that makes PAA work` Inter Regular 12 pt `#F0EDE8` at 60%

Diagram description (built with rectangles and lines):

**Layer stack (bottom to top):**
1. `ALUMINUM SUBSTRATE` -- thick horizontal rect, fill `#C8D0D8`
2. `BARRIER LAYER` -- thin horizontal rect, fill `#E8A020` at 40%, label `~10 nm`
3. `POROUS OXIDE` -- medium rect with vertical columns representing pore walls, fill `#3A4055` at 60%
4. `WHISKER TIPS` -- at the top of each column, small protruding elements extending upward, fill `#27AE60`
5. Above whiskers: `ADHESIVE PRIMER` zone labeled with arrows showing interlocking

Labels:
- `Whisker height: 10--50 nm` JetBrains Mono 11 pt `#27AE60`
- `Open pores: NOT sealed` JetBrains Mono 11 pt `#E05C5C`
- `Total oxide: 0.5--1.5 um` JetBrains Mono 11 pt `#E8A020`
- `Adhesive interlocks with whiskers` Inter Medium 12 pt `#27AE60`

**Bottom callout (Y: 13.5"):**
- `PAA oxide provides almost ZERO standalone corrosion protection. Its only purpose is adhesive mechanical interlocking.` Inter Medium 14 pt `#E8A020`

---

### ZONE 4 -- Operating Window

**Section label:** `OPERATING PARAMETERS` -- Y: 14.7".

**Full-width parameter table (Y: 15.3" to 20.3"):**

**Left -- Critical Parameters (X: 0.5", W: 11.0"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#27AE60` 0.06"
- Title: `PAA ANODIZE PARAMETERS` Barlow SemiBold 18 pt `#27AE60`

| Parameter | Control Range | Notes |
|---|---|---|
| Electrolyte | H3PO4 100--120 g/L (10--12% w/v) | Some specs: 5--15% by weight |
| Temperature | 20--25 C (68--77 F) | Room temperature range |
| Voltage | 10--15V; BAC 5555: 10V +/- 1V | VOLTAGE-CONTROLLED (not current) |
| Current density | 0.5--1.5 A/dm2 (5--15 ASF) | Self-regulating under voltage control |
| Time | 20--25 min | Per specification |
| Coating thickness | 0.5--1.5 um | Measured by weight gain, not eddy current |
| Dissolved aluminum | < 10 g/L | Bath maintenance |

Data: JetBrains Mono 12 pt `#F0EDE8`.

**Right -- What Makes PAA Different (X: 12.0", W: 11.5"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `PAA VS. TYPE II -- KEY DIFFERENCES` Barlow SemiBold 18 pt `#E8A020`

| Parameter | PAA | Type II |
|---|---|---|
| Electrolyte | H3PO4 (weak acid) | H2SO4 (strong acid) |
| Voltage | 10--15V | 15--18V |
| Thickness | 0.5--1.5 um | 5--25 um |
| Pore structure | Open whiskers | Ordered hexagonal |
| Sealed | NEVER | Always |
| Purpose | Bond surface | Protection/decoration |

Data: JetBrains Mono 11 pt. PAA column: `#E8A020`. Type II column: `#2EC4B6`.

---

### ZONE 5 -- How PAA Creates Bond Surfaces

**Section label:** `THE MECHANISM -- HOW PAA CREATES BOND SURFACES` -- Y: 20.7".

**Full-width panel (Y: 21.3" to 26.3"):**
- Rounded rect, X: 0.5", W: 23.0", H: 4.8", fill `#1E2435`

**Three-column mechanism:**

*Column 1 -- The Chemistry (X: 1.0", W: 7.0"):*
- Title: `THE CHEMISTRY` Barlow SemiBold 16 pt `#27AE60`
- Body (Inter Regular 13 pt `#F0EDE8`, line height 155%):

> Phosphoric acid is weaker than sulfuric acid. It dissolves the outer oxide layer more aggressively relative to growth.
>
> This creates an open, columnar pore structure at the surface -- whisker-like protrusions of aluminum oxide, 10--50 nm tall.
>
> These whiskers are the mechanical interlocking sites for adhesive primers.

*Column 2 -- The Interlocking (X: 8.5", W: 7.0"):*
- Title: `THE INTERLOCKING` Barlow SemiBold 16 pt `#E8A020`
- Body:

> When adhesive primer is applied to PAA oxide:
>
> 1. Primer wets the whisker surfaces
> 2. Primer flows into the open pores
> 3. As primer cures, it mechanically locks around the whiskers
> 4. The resulting joint combines chemical affinity + mechanical grip
>
> Bond strength exceeds 40 MPa (6,000 psi) in aluminum-to-aluminum joints.

*Column 3 -- Why It Works (X: 16.0", W: 7.0"):*
- Title: `WHY PAA EXCELS` Barlow SemiBold 16 pt `#2EC4B6`
- Body:

> PAA oxide is superior to:
> -- Grit-blasted surfaces (inconsistent roughness)
> -- FPL etch alone (no oxide interlocking)
> -- Type II anodize (pores sealed; no interlocking)
>
> The combination of nano-scale roughness + open pore chemistry + chemical compatibility with epoxy primers makes PAA the aerospace standard.

---

### ZONE 6 -- Failure Modes + Contamination

**Section label:** `WHAT GOES WRONG` -- Y: 26.7".

**Two-column layout (Y: 27.3" to 32.3"):**

**Left -- Failure Modes (X: 0.5", W: 11.0"):**
- Title: `PAA ANODIZE FAILURES` Barlow Condensed ExtraBold 22 pt `#F0EDE8`

| Failure | Cause | Bond Impact |
|---|---|---|
| Over-anodizing | Too long or too high voltage | Dissolves whisker structure; REDUCED bond strength |
| Thin/absent oxide | H3PO4 > 15%; dissolved Al too high | No interlocking sites; bond failure |
| Contaminated surface | Organic film on parts | Adhesive wetting reduced; weak bond |
| Delayed priming | > 72 hours after anodize | Atmospheric hydration closes pores; must restart |

4-row table with Coral left accent. Data: Inter Regular 12 pt.

**Right -- Bath Contamination (X: 12.0", W: 11.5"):**
- Title: `BATH CONTAMINATION LIMITS` Barlow Condensed ExtraBold 22 pt `#F0EDE8`

| Contaminant | Limit | Source | Effect |
|---|---|---|---|
| Dissolved Al | < 10 g/L | Normal process | Reduced efficiency |
| Chloride | < 25 ppm | Process water | Pitting attack |
| Fluoride | 0 ppm (trace) | HF desmut dragover | Oxide destruction |
| Organic | None visible | Cleaner carryover | Blocks oxide growth |

Data: JetBrains Mono 12 pt. Limit values in `#E05C5C`.

---

### ZONE 7 -- Footer

Standard. Title: `Anodize -- PAA (Bonding Surface)`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; ASTM D3933; Boeing BAC 5555. PAA anodize parameters are voltage-controlled and specification-dependent. Consult your applicable OEM specification for exact requirements.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Anodize PAA -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the most technically interesting poster in the PAA cluster. The pore morphology diagram (Block C) is the single most important visual -- it explains WHY PAA works at a level that most operators never see. The whisker structure is what distinguishes PAA from every other anodizing process. The comparison table against Type II reinforces that PAA is fundamentally different -- thinner, weaker, unsealed, and purposeful. The over-anodizing failure mode is counterintuitive (more anodizing = worse bond) and should be highlighted.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #317 -- Construction Workup v1.0*
*2026-04-26*
