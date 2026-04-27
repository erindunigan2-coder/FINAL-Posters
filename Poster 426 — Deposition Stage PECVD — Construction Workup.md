---
Project: Plating Posters Inc
Poster Number: 426
Title: "Deposition Stage -- PECVD"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 3: PECVD, Sections 3.7, 3.8)"
Technical Source: PECVD film growth -- amorphous films with 1-30 at% hydrogen, plasma-activated surface reactions, in-situ monitoring (laser interferometry, OES, RGA), and common deposition defects. This is the core process stage where the film actually grows.
Process Scope: PECVD deposition execution, film growth monitoring, and in-process quality indicators
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - PECVD
  - Deposition
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #426 -- Construction Workup
## Deposition Stage -- PECVD

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 6 of the PECVD sequence -- the main event. Plasma ignites, precursors dissociate into reactive radicals, and those radicals condense on the substrate surface to build the film atom by atom. This poster covers what happens during deposition: how the film grows, what to monitor, and what can go wrong. The hero visual is a film growth mechanism diagram showing gas-phase dissociation to surface reaction.

Emerald dominates -- this is the core process stage.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Film growth mechanism diagram (Block B -- HERO):** Simplified schematic of gas-phase dissociation -> surface reaction -> film growth, with labeled species.
2. **In-situ monitoring reference (Block C):** Three monitoring techniques with what they measure and when to use each.
3. **Deposition rate reference (Block D):** Film-by-film deposition rates and how to calculate run time.
4. **Common deposition defects (Block E):** 6-defect table with causes and fixes.
5. **Process stability indicators (Block F):** What to watch during a run -- the "dashboard" for operators.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.0" / 20.0" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 6 highlighted (Emerald)
ZONE 3 -- FILM GROWTH MECHANISM HERO (4.2"--14.0" / ~9.8")
  Block B: Growth mechanism diagram
ZONE 4 -- IN-SITU MONITORING + DEPOSITION RATES (14.0"--20.0" / ~6.0")
  Block C: Monitoring techniques
  Block D: Deposition rate reference
ZONE 5 -- DEFECTS + STABILITY INDICATORS (20.0"--32.5" / ~12.5")
  Block E: Common deposition defects table
  Block F: Process stability dashboard
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `DEPOSITION STAGE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `PECVD -- Stage 6 of 10 -- Plasma On, Film Growing` -- 30 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `The plasma breaks the bonds. The surface catches the pieces. Every second of glow discharge builds your film -- angstrom by angstrom.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

**Rule Card (top right):**
- Rounded rect, X: 17.0", Y: 0.5", W: 6.5", H: 2.2", fill `#1E2435`, border 1 pt `#27AE60`
- Big number: `50-200` -- Barlow Condensed ExtraBold, 52 pt, `#27AE60`
- Label: `nm/min (SiO2)` -- JetBrains Mono Regular, 14 pt, `#F0EDE8` at 70%
- Sub-label: `Typical PECVD SiO2 deposition rate` -- Inter Regular, 12 pt, `#F0EDE8` at 50%

---

### ZONE 2 -- Orientation Strip

Stage 6 (`Deposition`): fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Input: All parameters at setpoint, gases flowing  -->  Output: Film deposited to target thickness`

---

### ZONE 3 -- Film Growth Mechanism Hero

**Section label:** `HOW THE FILM GROWS` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Growth Mechanism Diagram**

Y: 5.0" to 13.8". Full width.

Main panel: Rounded rect, X: 0.5", Y: 5.0", W: 23.0", H: 8.5", fill `#1E2435`, radius 8.

**Three-zone vertical diagram (top to bottom):**

*Zone A -- Gas Phase (top third, Y: 5.3" to 7.5"):*
- Label: `GAS PHASE -- PLASMA DISSOCIATION` -- Barlow SemiBold, 18 pt, `#E8A020`
- Background tint: `#E8A020` at 5%

Left column -- SiO2 example:
```
SiH4  -->  SiH3 + H (radical)
N2O   -->  O + N2 (radical + inert)
SiH3 + O  -->  SiH2O (precursor to film)
```

Right column -- Si3N4 example:
```
SiH4  -->  SiH2 + 2H (radical)
NH3   -->  NH2 + H (radical)
SiH2 + NH2  -->  film precursors
```

Text: JetBrains Mono Regular, 13 pt, `#F0EDE8`. Arrow labels: `#E8A020`.

Annotation: `RF plasma provides energy to break molecular bonds. These reactive fragments (radicals) are the building blocks of the film.` -- Inter Regular, 12 pt, `#F0EDE8` at 70%

*Zone B -- Transport (middle strip, Y: 7.7" to 8.5"):*
- Label: `DIFFUSION THROUGH BOUNDARY LAYER` -- Barlow SemiBold, 14 pt, `#C8D0D8`
- Down arrows: 2 pt `#3A4055`
- Note: `Reactive species diffuse from plasma toward substrate surface` -- Inter Regular, 11 pt, `#F0EDE8` at 60%

*Zone C -- Surface (bottom third, Y: 8.7" to 13.5"):*
- Label: `SURFACE REACTION -- FILM FORMATION` -- Barlow SemiBold, 18 pt, `#27AE60`
- Background tint: `#27AE60` at 5%

Surface reaction description:
```
1. Reactive species adsorb on substrate surface
2. Surface migration to energetically favorable sites
3. Chemical bonds form -- Si-O or Si-N network grows
4. Byproducts (H2, CH4) desorb and are pumped away
5. Film grows layer by layer (amorphous structure)
```

Key characteristic callout:
- Rounded rect, W: 22.0", H: 1.2", fill `#27AE60` at 10%, border 1 pt `#27AE60`
- Text: `PECVD films are AMORPHOUS (no crystal structure) and contain 1--30 at% hydrogen. This hydrogen affects density, etch rate, refractive index, and long-term stability.` -- Inter Medium, 13 pt, `#27AE60`

---

### ZONE 4 -- In-Situ Monitoring + Deposition Rates

**BLOCK C -- In-Situ Monitoring (Left, X: 0.5", W: 11.0")**

Section label: `MONITORING DURING DEPOSITION` -- Y: 14.2".

Y: 14.8" to 19.8". Three monitoring technique cards stacked vertically.

Each card: Rounded rect, W: 11.0", H: 1.5", fill `#1E2435`, left accent 3 pt, radius 6.

| Card | Technique | What It Measures | Accent |
|---|---|---|---|
| 1 | LASER INTERFEROMETRY | Film thickness in real-time (fringe counting -- each fringe = lambda/2n) | `#27AE60` |
| 2 | OPTICAL EMISSION (OES) | Plasma species composition -- detects gas ratio drift | `#E8A020` |
| 3 | RESIDUAL GAS ANALYZER (RGA) | Gas-phase composition by mass spectrometry -- detects leaks, contamination | `#2EC4B6` |

Card interior:
- Technique name: Barlow SemiBold, 16 pt, accent color
- What it measures: Inter Regular, 12 pt, `#F0EDE8`

Bottom note: `Most production PECVD tools rely on time-based control: calibrated deposition rate x time = target thickness. Monitor techniques are for recipe development and troubleshooting.` -- Inter Regular, 12 pt, `#F0EDE8` at 70%

**BLOCK D -- Deposition Rate Reference (Right, X: 12.0", W: 11.5")**

Section label: `DEPOSITION RATE REFERENCE` -- Y: 14.2".

| Film | Rate | Time for 100 nm | Time for 1 um |
|---|---|---|---|
| SiO2 (SiH4 + N2O) | 50--200 nm/min | 30 sec--2 min | 5--20 min |
| Si3N4 (SiH4 + NH3) | 10--50 nm/min | 2--10 min | 20--100 min |
| a-Si:H | 5--30 nm/min | 3--20 min | 30--200 min |
| SiNx:H (solar) | 10--30 nm/min | 3--10 min | 30--100 min |
| DLC (a-C:H) | 5--30 nm/min | 3--20 min | 30--200 min |

Rate values: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Film names: Inter Medium, 13 pt.

Calculation callout:
- Rounded rect, fill `#252B3D`, border 1 pt `#27AE60`
- `Thickness = Rate x Time` -- JetBrains Mono, 18 pt, `#27AE60`
- `Example: 100 nm/min x 10 min = 1000 nm = 1 um` -- Inter Regular, 12 pt, `#F0EDE8`

---

### ZONE 5 -- Defects + Stability Indicators

**BLOCK E -- Common Deposition Defects (Y: 20.2" to 27.0")**

Section label: `COMMON DEPOSITION DEFECTS` -- Barlow Condensed ExtraBold, 24 pt, `#E05C5C`. Y: 20.4".

Six-row table:

| Defect | Cause | Prevention | Indicator |
|---|---|---|---|
| Particles in film | Gas-phase nucleation; wall flaking | Lower pressure; clean chamber every 5--50 um accumulated | Particle counts on test wafer |
| Pinholes | Particles on substrate; film too thin | Proper cleaning; minimum 50 nm film thickness | Visual inspection; electrical test |
| High hydrogen content | Low temperature; high SiH4 flow | Increase temp; reduce SiH4 flow; post-anneal at 400--450 degC | FTIR: Si-H peak at ~2100 cm-1 |
| Poor step coverage | Geometry limitations of PECVD | Use TEOS-based SiO2; consider HDP-CVD for gap fill | SEM cross-section of test structure |
| Film cracking | Excessive tensile stress; film too thick | Adjust RF power/pressure for low stress; multilayer approach | Wafer bow measurement (Stoney equation) |
| Non-uniformity | Showerhead clogging; gas flow dead zones | Clean showerhead; optimize electrode spacing | 49-point ellipsometry map |

Header row: `#3A4055`. Data rows: alternating `#1E2435` / `#252B3D`. Defect names: Barlow SemiBold, 13 pt, `#E05C5C`. Data: Inter Regular, 12 pt, `#F0EDE8`.

**BLOCK F -- Process Stability Dashboard (Y: 27.5" to 32.3")**

Section label: `YOUR IN-PROCESS DASHBOARD -- WHAT TO WATCH` -- Barlow Condensed ExtraBold, 22 pt, `#27AE60`. Y: 27.7".

Six indicator cards in 3x2 grid:

| Position | Indicator | Normal | Alarm | Accent |
|---|---|---|---|---|
| R1C1 | RF Forward Power | Stable at setpoint +/- 2% | Drifting or fluctuating | `#27AE60` |
| R1C2 | Reflected Power | < 5% of forward | Rising -- matching network losing tune | `#E05C5C` |
| R1C3 | Chamber Pressure | Stable at recipe pressure +/- 5% | Drifting -- gas flow or pump issue | `#E8A020` |
| R2C1 | Substrate Temperature | At setpoint +/- 3 degC | Drifting -- heater or thermocouple fault | `#E8A020` |
| R2C2 | Gas Flow (MFC readback) | Matches setpoint | Deviation > 2% -- MFC drift | `#2EC4B6` |
| R2C3 | Plasma Glow Color | Consistent, characteristic of recipe | Color shift -- gas ratio changing | `#C8D0D8` |

Each card: Rounded rect, W: 7.33", H: 2.0", fill `#1E2435`, radius 6, left accent 3 pt.
- Indicator name: Barlow SemiBold, 14 pt, accent color
- Normal: Inter Regular, 11 pt, `#27AE60`
- Alarm: Inter Regular, 11 pt, `#E05C5C`

---

### ZONE 6 -- Footer

Standard. Title: `Deposition Stage -- PECVD`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Deposition parameters and rates shown are typical industry values. Actual results depend on specific equipment, gas purity, and chamber condition. Consult your equipment manufacturer for application-specific guidance.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Deposition Stage PECVD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Emerald dominates this poster because this IS the process -- everything else is preparation or post-processing. The film growth mechanism diagram is the educational core and should be immediately legible: gas phase (plasma breaks bonds) -> transport (radicals drift down) -> surface (film forms). The process stability dashboard is designed for operators who monitor runs -- it answers "what should I be watching and what does it mean when something changes?"

The amorphous + hydrogen content callout is the defining characteristic of PECVD films that distinguishes them from thermal CVD or PVD -- this insight sticks with engineers who are comparing deposition methods.

---

*Alaina -- Poster #426 -- Construction Workup v1.0 -- 2026-04-26*
