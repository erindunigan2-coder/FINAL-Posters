---
Project: Plating Posters Inc
Poster Number: 425
Title: "Parameter Setup -- PECVD"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 3: PECVD, Section 3.6)"
Technical Source: PECVD recipe programming -- gas flow rates, RF power, pressure, substrate temperature, and their effects on film properties. Representative recipes for SiO2 and Si3N4. Key tuning relationships between parameters and film quality (refractive index, stress, hydrogen content, deposition rate).
Process Scope: PECVD deposition parameter programming and recipe optimization
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - PECVD
  - ParameterSetup
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #425 -- Construction Workup
## Parameter Setup -- PECVD

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 5 of the PECVD sequence. This poster is where physics meets practice. Every knob the operator turns -- gas flow, RF power, pressure, temperature -- maps to a specific film property. Change the SiH4:N2O ratio and the refractive index shifts. Crank RF power and the film gets denser but more stressed. This poster makes those relationships explicit with two representative recipes (SiO2 and Si3N4) and a tuning-relationships reference.

Hero visual: two side-by-side recipe cards -- SiO2 and Si3N4 -- with all parameters specified.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Two representative recipe cards (Block B -- HERO):** SiO2 and Si3N4 recipes with full parameter tables.
2. **Tuning relationships panel (Block C):** "Turn this knob, get this result" reference.
3. **Precursor gas-to-film chart (Block D):** Which gases produce which films.
4. **Film property targets (Block E):** Refractive index, dielectric constant, stress targets for common PECVD films.
5. **SiH4 safety reminder (Block F):** Persistent safety callout for pyrophoric gas handling during parameter changes.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.5" / 21.5" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 5 highlighted (Amber)
ZONE 3 -- REPRESENTATIVE RECIPES HERO (4.2"--15.5" / ~11.3")
  Block B: SiO2 + Si3N4 recipe cards side by side
ZONE 4 -- TUNING RELATIONSHIPS (15.5"--21.5" / ~6.0")
  Block C: Parameter-to-property tuning reference
ZONE 5 -- GAS-TO-FILM + FILM TARGETS (21.5"--32.5" / ~11.0")
  Block D: Precursor gas chart
  Block E: Film property targets
  Block F: SiH4 safety reminder
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `PARAMETER SETUP` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `PECVD -- Stage 5 of 10 -- Gas Flows, RF Power, Pressure, and Temperature` -- 28 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Every parameter controls a film property. Change one, measure the result, build the recipe. PECVD is a four-knob instrument -- learn what each knob does.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

**Rule Card (top right):**
- Rounded rect, X: 17.0", Y: 0.5", W: 6.5", H: 2.2", fill `#1E2435`, border 1 pt `#E8A020`
- Big number: `4` -- Barlow Condensed ExtraBold, 72 pt, `#E8A020`
- Label: `KEY PARAMETERS` -- JetBrains Mono Regular, 14 pt, `#F0EDE8` at 70%
- Sub-label: `Gas flow | RF power | Pressure | Temperature` -- Inter Regular, 12 pt, `#F0EDE8` at 50%

---

### ZONE 2 -- Orientation Strip

Stage 5 (`Parameter Setup`): fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Input: System at base vacuum, plasma hardware verified  -->  Output: Recipe loaded, all parameters at setpoint`

---

### ZONE 3 -- Representative Recipes Hero

**Section label:** `REPRESENTATIVE RECIPES -- SiO2 AND Si3N4` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Two Recipe Cards**

Y: 5.0" to 15.3". Two large panels side by side.

**Left -- PECVD SiO2 Recipe (X: 0.5", W: 11.0")**

Rounded rect, fill `#1E2435`, top accent 4 pt `#2EC4B6`, radius 8.

Title: `PECVD SILICON DIOXIDE (SiO2)` -- Barlow SemiBold, 22 pt, `#2EC4B6`
Subtitle: `Interlayer dielectric | Passivation | Barrier` -- Inter Regular, 14 pt, `#F0EDE8` at 60%

Parameter table:

| Parameter | Value |
|---|---|
| Precursor 1 | SiH4 at 30--100 sccm |
| Precursor 2 | N2O at 300--1000 sccm |
| SiH4 : N2O ratio | 1:5 to 1:10 |
| Carrier gas | N2 or Ar |
| RF power | 100--300 W (13.56 MHz) |
| Pressure | 1--3 Torr |
| Substrate temp | 300--400 degC |
| Electrode gap | 15--25 mm |
| Deposition rate | 50--200 nm/min |

Target properties (JetBrains Mono, 13 pt, `#2EC4B6`):
```
Refractive index:  n = 1.46--1.47
Dielectric const:  k = 4.0--4.5
Film stress:       < 200 MPa (compressive)
```

Bottom note: `Higher N2O ratio = more stoichiometric SiO2, lower refractive index, lower etch rate in BOE.` -- Inter Medium, 12 pt, `#2EC4B6`

**Right -- PECVD Si3N4 Recipe (X: 12.0", W: 11.5")**

Rounded rect, fill `#1E2435`, top accent 4 pt `#E8A020`, radius 8.

Title: `PECVD SILICON NITRIDE (Si3N4)` -- Barlow SemiBold, 22 pt, `#E8A020`
Subtitle: `Passivation | Etch stop | Solar AR coating` -- Inter Regular, 14 pt, `#F0EDE8` at 60%

Parameter table:

| Parameter | Value |
|---|---|
| Precursor 1 | SiH4 at 50--200 sccm |
| Precursor 2 | NH3 at 20--100 sccm |
| Dilution gas | N2 at 500--2000 sccm |
| SiH4 : NH3 ratio | 1:1 to 5:1 (tunable) |
| RF power | 100--500 W (13.56 MHz) |
| Pressure | 1--3 Torr |
| Substrate temp | 300--400 degC |
| Electrode gap | 15--25 mm |
| Deposition rate | 10--50 nm/min |

Target properties (JetBrains Mono, 13 pt, `#E8A020`):
```
Refractive index:  n = 1.85--2.05 (tunable)
Dielectric const:  k = 6.0--7.5
Film stress:       < 300 MPa (compressive)
```

Bottom note: `SiH4:NH3 ratio controls stoichiometry. Si-rich = higher n, higher absorption (good for solar AR). N-rich = lower n, better dielectric.` -- Inter Medium, 12 pt, `#E8A020`

Table data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Parameter labels: Inter Medium, 13 pt. Header row: `#3A4055`. Data rows: alternating `#1E2435` / `#252B3D`.

---

### ZONE 4 -- Tuning Relationships

**Section label:** `TURN THE KNOB -- SEE THE RESULT` -- Y: 15.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK C -- Tuning Reference Panel**

Y: 16.3" to 21.3". Rounded rect, fill `#1E2435`, X: 0.5", W: 23.0".

Six tuning relationships in a 3x2 grid. Each: Rounded rect, W: 7.33", H: 2.2", fill `#252B3D`, radius 6, top accent 3 pt.

| Position | Parameter Change | Effect on Film | Accent |
|---|---|---|---|
| R1C1 | INCREASE RF POWER | Denser film, higher stress, faster rate, less hydrogen | `#E8A020` |
| R1C2 | INCREASE TEMPERATURE | Less hydrogen, denser, more stable, higher refractive index | `#E05C5C` |
| R1C3 | INCREASE PRESSURE | More gas-phase reactions, risk of particles, better step coverage | `#C8D0D8` |
| R2C1 | INCREASE SiH4 : N2O RATIO | Si-rich SiOx -- higher n, higher leakage current | `#2EC4B6` |
| R2C2 | INCREASE SiH4 : NH3 RATIO | Si-rich SiNx -- higher n, higher absorption | `#2EC4B6` |
| R2C3 | INCREASE ELECTRODE GAP | Better uniformity, lower rate, more particles at extreme | `#27AE60` |

Card interior:
- Parameter change: Barlow SemiBold, 14 pt, accent color
- Effect: Inter Regular, 12 pt, `#F0EDE8`

---

### ZONE 5 -- Gas-to-Film Chart + Film Targets + Safety

**BLOCK D -- Precursor Gas-to-Film Chart (Left, X: 0.5", W: 11.0")**

Section label: `WHICH GASES MAKE WHICH FILMS?` -- Y: 21.7".

Y: 22.3" to 27.5".

| Film | Precursors | Carrier | Notes |
|---|---|---|---|
| SiO2 | SiH4 + N2O | N2 or Ar | Or TEOS + O2 for better step coverage |
| Si3N4 | SiH4 + NH3 | N2 | Or SiH4 + N2 (lower quality) |
| SiON | SiH4 + N2O + NH3 | N2 | Tunable n between SiO2 and Si3N4 |
| a-Si:H | SiH4 | H2 or Ar | Amorphous silicon for TFT, solar |
| SiC | SiH4 + CH4 | Ar | Hard, chemically resistant |
| DLC (a-C:H) | C2H2 or CH4 | Ar | Diamond-like carbon; see Cluster 5 |

Header: `#3A4055`. Data: alternating fills. Film names: Inter Medium, 13 pt, accent varies by film. Data: JetBrains Mono, 11 pt, `#F0EDE8`.

**BLOCK E -- Film Property Targets (Right, X: 12.0", W: 11.5")**

Section label: `FILM PROPERTY TARGETS` -- Y: 21.7".

Y: 22.3" to 27.5".

| Film | Refractive Index (n) | Dielectric Constant (k) | Hardness | BOE Etch Rate |
|---|---|---|---|---|
| PECVD SiO2 | 1.46--1.47 | 4.0--4.5 | 6--8 GPa | 200--400 nm/min |
| PECVD Si3N4 | 1.85--2.05 | 6.0--7.5 | 15--25 GPa | Very slow |
| PECVD SiNx:H (solar) | 2.0--2.1 | 5--7 | 12--18 GPa | -- |
| PECVD a-Si:H | 3.5--4.5 | 11--12 | -- | -- |
| PECVD DLC (a-C:H) | 1.8--2.4 | 3--5 | 10--30 GPa | -- |

Note: `Refractive index is the primary in-line quality check. If n is on target, stoichiometry is correct.` -- Inter Medium, 13 pt, `#27AE60`

Reference: `Thermal SiO2 BOE etch rate ~100 nm/min. PECVD SiO2 etches 2--4x faster -- lower density due to hydrogen content.` -- Inter Regular, 12 pt, `#F0EDE8` at 70%

**BLOCK F -- SiH4 Safety Reminder (Full width, Y: 28.0" to 32.3")**

Section label: `SAFETY REMINDER -- PARAMETER CHANGES INVOLVE GAS FLOW CHANGES` -- Barlow Condensed ExtraBold, 22 pt, `#E05C5C`. Y: 28.2".

Callout panel: Rounded rect, X: 0.5", Y: 28.8", W: 23.0", H: 3.0", fill `#1E2435`, left accent 0.06" `#E05C5C`.

Two columns:

Left (X: 1.5", W: 10.0"):
- `SiH4 FLOW CHANGES` -- Barlow SemiBold, 18 pt, `#E05C5C`
- `Changing SiH4 flow rate means adjusting a PYROPHORIC gas line.` -- Inter Regular, 14 pt, `#F0EDE8`
- `Verify:` -- Inter Medium, 14 pt, `#F0EDE8`
```
MFC responding correctly
No pressure spikes during flow change
Exhaust scrubber running
LEL detector reading zero
```

Right (X: 12.5", W: 10.5"):
- `RECIPE VALIDATION` -- Barlow SemiBold, 18 pt, `#E8A020`
- `Never run a new recipe on production parts.` -- Inter Medium, 14 pt, `#F0EDE8`
- `Always:` -- Inter Medium, 14 pt, `#F0EDE8`
```
Test on dummy substrates first
Measure film properties (n, thickness, stress)
Compare to target before committing
Log all recipe changes with date and operator
```

---

### ZONE 6 -- Footer

Standard. Title: `Parameter Setup -- PECVD`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Process parameters shown are typical industry values for PECVD. Specific recipes vary by equipment manufacturer and application. Consult your equipment manual for exact parameter ranges.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Parameter Setup PECVD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster is the recipe book. The two side-by-side recipe cards should look like something you would pin to a process bench -- clear, complete, immediately actionable. The tuning relationships grid is the educational core: it teaches operators the WHY behind each parameter, not just the value. The SiH4 safety reminder at the bottom is deliberate redundancy -- every PECVD poster in this cluster should remind operators that they are working with a pyrophoric gas.

---

*Alaina -- Poster #425 -- Construction Workup v1.0 -- 2026-04-26*
