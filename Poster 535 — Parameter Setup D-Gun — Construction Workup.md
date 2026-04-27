---
Project: Plating Posters Inc
Poster Number: 535
Title: "Parameter Setup -- D-Gun"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 6: Detonation Gun)"
Technical Source: D-Gun operating parameters including detonation frequency (1--15 Hz), O2/C2H2 ratio (1.0--1.5), detonation velocity (~3500 m/s), particle velocity (750--1000 m/s), detonation temperature (3500--4500 C), powder charge (0.5--3 g per cycle), standoff distance (100--200 mm), nitrogen purge volume, deposition rate (1--5 kg/hr), and deposition efficiency (70--90%).
Process Scope: D-Gun -- parameter setup and operating windows
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document.
tags:
  - PosterDesign
  - DGun
  - DetonationGun
  - ThermalSpray
  - Parameters
  - ConstructionWorkup
  - ClusterTS06
---

# Poster #535 -- Construction Workup
## Parameter Setup -- D-Gun

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Parameter poster for D-Gun. Hero concept: the O2/C2H2 ratio is the master control. Stoichiometric to slightly lean mixtures (1.0--1.5) control detonation temperature and oxide content. A lean ratio reduces oxide content in the coating. The secondary story is detonation frequency -- cycles per second directly controls deposition rate and heat input. Everything in D-Gun parameter setup revolves around the controlled explosion.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Master parameter table (Block B -- HERO):** Full operating parameter range.
2. **O2/C2H2 ratio callout (Block C):** The master control variable and its effect on coating quality.
3. **Detonation frequency vs. heat input (Block D):** How cycle rate affects both throughput and substrate temperature.
4. **Material-specific parameter notes (Block E):** WC-Co, Cr2O3, and CrC-NiCr tuning differences.
5. **Parameter interaction summary (Block F):** What happens when you change each key variable.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- PARAMETER TABLE + O2/C2H2 CALLOUT (2.9"--14.0" / ~11.1")
  Block B: Master parameter table
  Block C: O2/C2H2 ratio callout
ZONE 3 -- FREQUENCY vs. HEAT + MATERIAL NOTES (14.0"--22.0" / ~8.0")
  Block D: Frequency vs. heat input
  Block E: Material-specific parameter adjustments
ZONE 4 -- PARAMETER INTERACTIONS + COMMON ERRORS (22.0"--32.5" / ~10.5")
  Block F: Parameter interaction guide
  Block G: Common parameter errors
ZONE 5 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `PARAMETER SETUP` -- 80 pt `#F0EDE8`.
**Subheading:** `D-Gun -- Tuning the Controlled Explosion` -- 32 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `Gas ratio. Frequency. Powder charge. Standoff. Every detonation cycle is a precision event -- parameters determine whether you get the gold standard or a reject.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Parameter Table + O2/C2H2 Callout

**Section label:** `OPERATING PARAMETER RANGES` -- Y: 3.1".

**BLOCK B -- Master Parameter Table (Left, X: 0.5", W: 14.5")**

Y: 3.8" to 12.5". Full data table.

Header row: `#3A4055`. Columns: Parameter (4.0") | Typical Range (4.5") | Notes (6.0")

| Parameter | Typical Range | Notes |
|---|---|---|
| Detonation frequency | 1--15 Hz (cycles/sec) | Higher frequency = higher deposition rate but more heat input |
| O2 fill volume | Barrel-geometry dependent | Precisely metered per cycle; not operator-adjustable in most systems |
| C2H2 fill volume | Barrel-geometry dependent | O2/C2H2 ratio is the key control variable |
| O2/C2H2 ratio | 1.0--1.5 | Stoichiometric to slightly lean; lean = less oxide in coating |
| Detonation velocity | ~3500 m/s (in barrel) | Gas dynamics; inherent to the detonation process |
| Particle velocity | 750--1000 m/s | Highest of all thermal spray processes |
| Detonation temperature | 3500--4500 C | Peak gas temperature during detonation wave |
| Powder charge | 0.5--3 g per cycle | Precisely metered; determines spot thickness |
| Standoff distance | 100--200 mm (4--8 in) | Closer than HVOF; particles decelerate rapidly after exiting barrel |
| N2 purge volume | 1--3x barrel volume | Must completely clear products of previous cycle |
| Deposition rate | 1--5 kg/hr | Lower than HVOF; each cycle deposits a small spot |
| Deposition efficiency | 70--90% | Very high due to high velocity and good melting |
| Spot diameter | ~25 mm (~1 inch) | Per detonation cycle; coating built by overlapping spots |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Parameter names: Inter Medium, 13 pt.

**BLOCK C -- O2/C2H2 Ratio Callout (Right, X: 15.5", W: 8.0")**

Y: 3.8" to 12.5". Rounded rect, fill `#1E2435`, radius 8, left accent 4 pt `#E8A020`.
Amber-tinted glass.

Title: `O2/C2H2 RATIO` Barlow Condensed ExtraBold, 28 pt, `#E8A020`.
Subtitle: `The Master Control Variable` Barlow SemiBold, 16 pt, `#F0EDE8`.

Ratio effects table:
```
RATIO   CONDITION     EFFECT ON COATING
1.0     Stoichio-     Maximum temperature;
        metric        highest particle melting;
                      highest oxide content

1.1     Slightly      Reduced temperature;
        lean          lower oxide; standard
                      for most WC-Co

1.3--   Lean          Lowest oxide content;
1.5                   reduced particle temp;
                      best for oxide-sensitive
                      materials (WC-Co, CrC)
```
JetBrains Mono Regular, 12 pt. RATIO values in `#E8A020`. CONDITION in `#F0EDE8`. EFFECT in `#F0EDE8` at 80%.

Key insight callout:
Rounded rect, H: 1.2", fill `#27AE60` at 10%, border 1 pt `#27AE60`, radius 6.

`LEAN RATIO = LESS OXIDE. For WC-Co coatings, a lean O2/C2H2 ratio reduces decarburization of tungsten carbide grains -- preserving the WC phase that provides hardness and wear resistance.` Inter Medium, 12 pt, `#27AE60`.

---

### ZONE 3 -- Frequency vs. Heat + Material Notes

**Left -- Frequency vs. Heat Input (X: 0.5", W: 11.5")**

Section label: `DETONATION FREQUENCY -- THE THROUGHPUT vs. HEAT TRADE-OFF` Y: 14.2".

**BLOCK D -- Frequency Guide**

Y: 14.8" to 21.0".

Three frequency range cards stacked:

| Range | Accent | Frequency | Deposition Rate | Heat Input | Best For |
|---|---|---|---|---|---|
| LOW | `#27AE60` | 1--4 Hz | 1--2 kg/hr | Minimal | Heat-sensitive substrates; thin coatings; precision work |
| MEDIUM | `#E8A020` | 4--8 Hz | 2--3 kg/hr | Moderate | Standard production; most WC-Co applications |
| HIGH | `#E05C5C` | 8--15 Hz | 3--5 kg/hr | Significant | Maximum throughput; thick coatings; robust substrates only |

Each card: W: 11.0", H: 1.8", fill `#1E2435`, radius 6, left accent 4 pt.
Range badge: Barlow Condensed ExtraBold, 14 pt, accent color on accent-filled rounded rect.
Data: Inter Regular, 12 pt, `#F0EDE8`.

Heat management note:
`At high frequencies, cooling air between cycles becomes critical. Monitor substrate temperature continuously. Pause spray if temperature approaches substrate limit.` Inter Medium, 13 pt, `#E8A020`.

**Right -- Material-Specific Notes (X: 12.5", W: 11.0")**

Section label: `MATERIAL-SPECIFIC PARAMETER ADJUSTMENTS` Y: 14.2".

**BLOCK E -- Material Cards**

Y: 14.8" to 21.0". Three material cards stacked.

Each card: W: 10.5", H: 1.8", fill `#1E2435`, radius 6, top accent 4 pt.

| Material | Accent | Key Adjustment | Rationale |
|---|---|---|---|
| WC-Co (WC-12Co, WC-17Co) | `#E8A020` | Lean O2/C2H2 ratio (1.1--1.5); moderate frequency | Minimize decarburization of WC grains; preserve W2C and WC phases; avoid W formation |
| Cr2O3 (Chrome Oxide) | `#27AE60` | Stoichiometric to slightly lean; higher powder charge | Ceramic requires full melting; larger charge builds thickness faster |
| CrC-NiCr (Chrome Carbide) | `#2EC4B6` | Lean ratio; lower frequency for heat-sensitive substrates | Similar to WC-Co philosophy -- protect carbide phase from decomposition |

Material: Barlow SemiBold, 16 pt, accent color.
Key Adjustment: JetBrains Mono Regular, 12 pt, `#F0EDE8`.
Rationale: Inter Regular, 12 pt, `#F0EDE8` at 80%.

---

### ZONE 4 -- Parameter Interactions + Common Errors

**Left -- Parameter Interaction Guide (X: 0.5", W: 12.0")**

Section label: `PARAMETER INTERACTIONS` Y: 22.2".

**BLOCK F -- Interaction Cards**

Y: 22.8" to 31.5". Six interaction cards.

Each card: W: 11.5", H: 1.3", fill `#1E2435`, radius 6, left accent 3 pt.

| If You Change... | Accent | Effect | Counter-Adjustment |
|---|---|---|---|
| INCREASE frequency | `#E8A020` | Higher deposition rate + higher heat input | Increase cooling air; reduce passes; monitor substrate temp |
| INCREASE O2/C2H2 ratio (leaner) | `#27AE60` | Lower oxide content + lower particle temperature | May need to increase frequency to maintain deposition rate |
| INCREASE powder charge | `#E8A020` | Thicker spot per cycle; higher deposition rate | May reduce particle velocity (more mass to accelerate) |
| DECREASE standoff | `#2EC4B6` | Denser coating; smaller spot; higher heat to substrate | More cooling; slower traverse to maintain coverage |
| INCREASE standoff | `#E05C5C` | Particles decelerate; lower density; larger spot | Reduce standoff or increase velocity (limited by gas dynamics) |
| INCREASE barrel length | `#C8D0D8` | Higher particle velocity; longer acceleration path | Not field-adjustable; equipment design decision |

"If You Change": Barlow SemiBold, 14 pt, accent color.
Effect: Inter Regular, 12 pt, `#F0EDE8`.
Counter: Inter Medium, 12 pt, `#27AE60`.

**Right -- Common Parameter Errors (X: 13.0", W: 10.5")**

Section label: `COMMON PARAMETER ERRORS` Y: 22.2".

**BLOCK G -- Error Cards (stacked)**

Y: 22.8" to 32.0". Five error cards.

| Error | Color | Symptom | Correction |
|---|---|---|---|
| O2/C2H2 RATIO TOO RICH | `#E05C5C` | Excessive oxide content; dark coating color; reduced hardness | Increase O2 or decrease C2H2; verify metering calibration |
| FREQUENCY TOO HIGH | `#E05C5C` | Substrate overheating; coating cracking; thermal distortion | Reduce frequency; increase cooling; pause between passes |
| POWDER CHARGE OVERLOADED | `#E8A020` | Unmelted particles; low density; porosity increase | Reduce charge weight; verify feeder calibration |
| STANDOFF TOO FAR | `#E8A020` | Porous coating; low bond strength; particles decelerate | Reduce standoff to 100--200 mm range; verify robot program |
| N2 PURGE INSUFFICIENT | `#E05C5C` | Premature detonation of next cycle; barrel damage risk | Increase purge volume to 2--3x barrel; verify N2 supply pressure |

Each card: H: 1.7", fill `#1E2435`, left accent error color.
Error: Barlow SemiBold, 14 pt, error color.
Symptom: Inter Regular, 12 pt, `#F0EDE8`.
Correction: Inter Medium, 12 pt, `#27AE60`.

---

### ZONE 5 -- Footer Band

Standard footer. Title: `Parameter Setup -- D-Gun`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 5 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Parameter Setup D-Gun -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The O2/C2H2 ratio callout is the intellectual anchor of this poster -- it is the single most important variable in D-Gun parameter setup, and the lean-ratio-reduces-oxide insight is genuinely valuable technical knowledge. The frequency vs. heat input trade-off is the second key concept: operators need to understand that cranking up the cycle rate is not free -- heat accumulates. The parameter interaction guide gives operators a mental model for how changes propagate through the system. The "insufficient N2 purge" error is flagged in coral because it is a safety hazard, not just a quality issue.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #535 -- Construction Workup v1.0*
*2026-04-26*
