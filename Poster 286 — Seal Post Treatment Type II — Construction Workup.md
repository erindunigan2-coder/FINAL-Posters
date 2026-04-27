---
Project: Plating Posters Inc
Poster Number: 286
Title: "Seal / Post Treatment -- Type II"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 1, Section 1.8)"
Technical Source: Industry-standard sealing and dyeing for sulfuric acid anodizing (Type II). Covers hot water seal, nickel acetate seal, cold seal, dichromate seal, and organic dyeing.
Process Scope: Seal and post-treatment (Stage 7--8 of 8) for Type II anodizing
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Anodizing
  - TypeII
  - Seal
  - Dyeing
  - ConstructionWorkup
  - ClusterAnodize
---

# Poster #286 -- Construction Workup
## Seal / Post Treatment -- Type II

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 7--8 of 8 (combined: dye + seal). This poster covers both the optional dyeing step and the mandatory seal. The hero concept: the pore structure diagram -- showing hexagonal cells with central pores, dye molecules trapped inside, and seal hydration closing the pore mouths. This single diagram explains BOTH dyeing AND sealing mechanisms. Sealing is what gives the anodized coating its corrosion resistance and dye permanence.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Pore structure diagram hero (Block B):** Cross-section of anodic oxide showing hexagonal pore cells, dye molecules inside pores, and hydration seal closing pore mouths. This is the most important visual in anodizing education.
2. **Dye parameters panel (Block D).**
3. **Seal comparison table (Block E):** Four seal methods side by side.
4. **Seal quality testing (Block F).**
5. **Failure modes strip (Block G).**

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
  Stages 7--8 highlighted (Amber)
ZONE 3 -- PORE STRUCTURE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- DYE PARAMETERS + COLOR MECHANISMS (14.5"--20.5" / ~6.0")
ZONE 5 -- SEAL METHOD COMPARISON (20.5"--26.5" / ~6.0")
ZONE 6 -- SEAL TESTING + FAILURE MODES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `SEAL / POST TREATMENT` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Type II -- Stages 7--8 of 8 (Dye + Seal)` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Dye fills the pores. Seal locks them shut. Without sealing, your anodized coating is an open sponge -- absorbing dirt, losing color, and corroding.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stages 7--8 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Porous anodic oxide (open pores)  -->  After: Sealed coating with trapped dye -- corrosion-resistant and color-permanent`

---

### ZONE 3 -- Pore Structure Hero

**Section label:** `THE ANODIC OXIDE -- PORE STRUCTURE` -- Y: 4.4".

**BLOCK B -- Pore Structure Cross-Section Diagram**

Y: 5.0" to 14.0".

This is a schematic cross-section showing three states side by side:

**Three panels across the width:**

| Panel | X | W | State | Description |
|---|---|---|---|---|
| 1. As-Anodized | 0.5" | 7.33" | Open pores | Hexagonal cells with empty central pores |
| 2. After Dye | 8.0" | 7.33" | Dye in pores | Same structure with colored molecules inside pores |
| 3. After Seal | 15.5" | 8.0" | Sealed | Pore mouths closed by hydration |

Each panel: Rounded rect H: 8.5", fill `#1E2435`, border 1 pt `#3A4055`.

**Panel 1 -- As-Anodized:**
- Title: `AS-ANODIZED` Barlow SemiBold 18 pt `#2EC4B6`
- Schematic: 4--5 hexagonal cells drawn with lines (`#C8D0D8`), central pore (empty circle) in each
- Base layer at bottom labeled `BARRIER LAYER` (`#E8A020`)
- Substrate below: `ALUMINUM SUBSTRATE` (`#C8D0D8`)
- Labels: `Pore mouth (open)` / `Cell wall (Al2O3)` / `Pore (~10--25 nm diameter)` / `Barrier layer (~1 nm/V)`
- Note: `Pores are OPEN -- coating absorbs anything it contacts (dye, dirt, moisture)` Inter Regular 12 pt `#F0EDE8` at 70%

**Panel 2 -- After Dye:**
- Title: `AFTER DYEING` Barlow SemiBold 18 pt `#E8A020`
- Same hex structure but pores filled with colored dots (represent dye molecules)
- Color: use `#E05C5C` as representative dye color
- Labels: `Organic dye molecules` / `Physically trapped in pores (not chemically bonded)` / `Color depth = pore depth x concentration x time`
- Note: `Dye is NOT permanent until sealed -- it will bleed out in hot water` Inter Regular 12 pt `#E05C5C`

**Panel 3 -- After Seal:**
- Title: `AFTER SEAL` Barlow SemiBold 18 pt `#27AE60`
- Same structure but pore mouths closed (swelled shut by hydration)
- Closed pore mouths shown as filled circles at top
- Labels: `Hydrated pore mouth (sealed)` / `Dye locked inside` / `Boehmite (AlOOH) or bayerite (Al(OH)3) forms`
- Note: `Seal = hydration of Al2O3 to AlOOH. Pore walls swell shut, trapping dye and blocking contaminants.` Inter Regular 12 pt `#27AE60`

**Bottom callout (spanning all three panels):**
- `The pore structure is the key to understanding dyeing AND sealing. The oxide is not a solid wall -- it is a forest of nano-scale tubes. Dye fills the tubes. Seal closes them.` Inter Medium 14 pt `#E8A020`

---

### ZONE 4 -- Dye Parameters + Color Mechanisms

**Section label:** `DYEING -- COLOR INSIDE THE OXIDE` -- Y: 14.7".

**Two-column layout:**

**Left -- Dye Operating Parameters (X: 0.5", W: 11.0"):**

| Parameter | Value |
|---|---|
| Chemistry | Organic acid dyes (azo, anthraquinone, phthalocyanine) |
| Concentration | 0.5--5 g/L (typical 1--3 g/L); per dye TDS |
| Temperature | 50--65 C (120--150 F) |
| pH | 5.0--6.5 (adjust with acetic acid or NH4OH) |
| Time | 5--30 minutes (more time = deeper color) |
| Min coating thickness | 8 um (0.3 mil) -- thinner = washed-out color |
| Agitation | Mild -- prevents dye concentration gradients |

**Right -- Dye Color Types (X: 12.0", W: 11.5"):**

| Type | Examples | UV Stability | Palette |
|---|---|---|---|
| Organic dyes | Azo, anthraquinone, phthalocyanine | Moderate | Full spectrum -- any color |
| Inorganic (metal salt) | Ferric ammonium oxalate (gold), cobalt acetate (blue-black) | Excellent | Limited -- gold, bronze, black |
| Two-step electrolytic | SnSO4, CoSO4 (AC coloring) | Excellent | Bronze to black |

Note: `Organic dyes offer unlimited color choice but fade in UV. Inorganic colors are UV-stable but limited to gold/bronze/black range. Choose by application: indoor = organic; outdoor = inorganic.` Inter Regular 13 pt `#F0EDE8`.

---

### ZONE 5 -- Seal Method Comparison

**Section label:** `SEAL OPTIONS -- CHOOSE BY APPLICATION` -- Y: 20.7".

**BLOCK E -- Four-Method Comparison Table**

| Seal Method | Temp | Chemistry | Time | Corrosion (B117) | Dye Retention | Best For |
|---|---|---|---|---|---|---|
| Hot DI water | 205--212 F (96--100 C) | DI water <50 uS/cm; pH 5.5--7.5 | 1--3 min/um; min 15 min | 336+ hrs | Moderate (some bleed) | General purpose |
| Nickel acetate (mid-temp) | 158--185 F (70--85 C) | 5--8 g/L Ni(OAc)2; pH 5.5--7.0 | 15--25 min | 500+ hrs | Excellent | Dyed parts; aerospace |
| Sodium dichromate | 194--205 F (90--96 C) | 50--80 g/L Na2Cr2O7; pH 5.0--6.5 | 15--30 min | 1000+ hrs | Good | Max corrosion (legacy -- Cr6+) |
| Cold seal (proprietary) | 77--86 F (25--30 C) | Nickel fluoride-based; pH 5.5--6.5 | 15--20 min | Good | Good | High volume; energy savings |

Table: Inter Medium 12 pt for labels, JetBrains Mono 12 pt for values.
Dichromate row: left accent `#E05C5C` with note `Contains Cr6+ -- regulatory phase-out`.

Bottom note: `Nickel acetate seal is the modern standard for dyed work. Hot water seal is simplest but can bleed delicate dyes.` Inter Medium 13 pt `#27AE60`.

---

### ZONE 6 -- Seal Testing + Failure Modes

**Two-column layout (Y: 26.7" to 32.3"):**

**Left -- Seal Quality Testing (X: 0.5", W: 11.0"):**

Section label: `SEAL QUALITY TESTING` Barlow Condensed ExtraBold 22 pt.

| Test | Standard | Method | Pass Criteria |
|---|---|---|---|
| Dye spot test | ASTM B680 | Drop dye on sealed surface; compare absorption | Sealed surface resists dye |
| Admittance (STEP) | ISO 2931 | Impedance measurement | Lower admittance = better seal |
| Acid dissolution | ASTM B680 | Weight loss after acid exposure | <30 mg/dm2 loss |

Note: `Dye spot test is the fastest field check. If your sealed surface absorbs dye, the seal is incomplete.` Inter Medium 13 pt `#2EC4B6`.

**Right -- Failure Modes (X: 12.0", W: 11.5"):**

| Failure | Cause | Fix |
|---|---|---|
| Seal bloom (white haze) | Tap water minerals (Ca, Mg); pH too high | Use DI water; check pH 5.5--7.5 |
| Dye bleed during seal | Hot water seal temp too high for dye | Switch to nickel acetate (lower temp) |
| Crazing (fine cracks) | Thermal shock -- cold part into boiling seal | Pre-warm parts in warm rinse first |
| Incomplete seal | Time too short or temp too low | Verify time and temp; re-seal if needed |
| Color shift after seal | Normal -- slight lightening with hot water | Expected 1--3% reflectance change |

---

### ZONE 7 -- Footer

Standard. Title: `Seal / Post Treatment -- Type II`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; MIL-A-8625F; ASM Handbook Vol. 5; ASTM B680. Specific dye and seal formulations vary by supplier.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Seal Post Treatment Type II -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The pore structure diagram is THE most important visual in the entire anodizing poster series. It explains both dyeing (dye fills open pores) and sealing (hydration swells pore walls shut). Watson specifically flagged this as the #1 visual for anodizing education. The three-state progression (as-anodized -> dyed -> sealed) should read left-to-right as a natural narrative. The seal comparison table gives shops a decision framework based on their application requirements. The dichromate seal row carries a Cr6+ warning consistent with the regulatory phase-out theme.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #286 -- Construction Workup v1.0*
*2026-04-26*
