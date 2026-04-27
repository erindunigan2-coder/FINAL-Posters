---
Project: Plating Posters Inc
Poster Number: 164
Title: "Zinc Phosphate -- Conversion Stage"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster CC-02 technical reference (zinc phosphate conversion coating)"
Process Scope: Zinc phosphate conversion coating main stage -- bath chemistry, operating parameters, crystal formation mechanism, coating weight control, phosphophyllite vs. hopeite (Stage 4 of 8 in the actual bath sequence, poster slot 5 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ZincPhosphate
  - ConversionCoating
  - MainStage
  - ConstructionWorkup
  - ClusterCC02
---

# Poster #164 -- Construction Workup
## Zinc Phosphate -- Conversion Stage

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

The main event of the CC-02 cluster. This poster covers the zinc phosphate coating formation mechanism -- a multi-step dissolution-reprecipitation reaction that produces a crystalline hopeite/phosphophyllite film on the steel surface. This is the densest poster in the cluster, covering: the 4-step mechanism, bath chemistry (zinc, phosphoric acid, nickel, manganese, accelerators, fluoride), spray vs. immersion parameters, the free acid/total acid ratio, the P-ratio (phosphophyllite to hopeite), coating weight ranges, and crystal structure.

The parallel to Poster #156 (Iron Phosphate Conversion Stage) is clear, but the zinc phosphate version is significantly more complex -- more bath components, tighter control ranges, crystalline vs. amorphous coating, and multi-substrate capability.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Coating formation hero (Block B -- HERO):** Tank cross-section showing phosphate solution attacking steel, with a magnified inset of the crystallization mechanism.
2. **Bath chemistry panel (Block D):** Multi-component table with concentrations and functions.
3. **Free acid / Total acid ratio gauge (Block E):** Visual ratio representation + P-ratio explanation.
4. **Coating weight interpretation chart (Block F):** Range bar showing light / medium / heavy / OEM target.
5. **Defect grid (Block G):** 6 common coating defects.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Coating stage highlighted (Amber)
ZONE 3 -- COATING FORMATION HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- BATH CHEMISTRY + FA/TA RATIO (14.5"--20.5" / ~6.0")
ZONE 5 -- COATING WEIGHT + P-RATIO (20.5"--26.5" / ~6.0")
ZONE 6 -- DEFECT DIAGNOSIS GRID (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ZINC PHOSPHATE` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Conversion Coating Stage -- Crystalline Protection` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Hopeite and phosphophyllite crystals, controlled by acid ratios and nucleation, forming the hardest-working paint primer in the automotive world. Control the ratio. Control the crystal.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Coating stage highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Ti-conditioned steel surface  -->  After: Crystalline Zn3(PO4)2 coating (medium gray, 150--350 mg/ft2 OEM target)`

---

### ZONE 3 -- Coating Formation Hero

**Section label:** `HOW THE COATING FORMS` -- Y: 4.4".

**BLOCK B -- Tank Cross-Section + Mechanism Inset**

Y: 5.0" to 14.0".

**Tank body:**
- Rounded rect, X: 1.5", Y: 5.5", W: 21.0", H: 5.5"
- Fill: `#E8A020` at 8%
- Border: 2 pt `#E8A020`
- Label: `ZINC PHOSPHATE SOLUTION` Barlow SemiBold 16 pt `#E8A020`

**Steel part (inside tank):**
- Rectangle, X: 8.0", Y: 6.5", W: 8.0", H: 3.0", fill `#C8D0D8`, border 2 pt `#3A4055`
- Ti nucleation sites shown as small dots on surface
- Label above: `Ti-CONDITIONED STEEL WORKPIECE` Barlow SemiBold 14 pt `#F0EDE8`

**Solution parameters (left side of tank):**
- `pH: 2.5--3.5` JetBrains Mono 14 pt `#E8A020`
- `Temp: 95--200 F (35--93 C)` JetBrains Mono 14 pt `#F0EDE8`
- `Free acid: 0.5--2.0 pts` JetBrains Mono 13 pt `#F0EDE8`
- `Total acid: 15--40 pts` JetBrains Mono 13 pt `#F0EDE8`
- `FA:TA ratio: 1:10 to 1:20` JetBrains Mono 13 pt `#E8A020`

**Mechanism inset (X: 1.0", Y: 11.5", W: 22.0", H: 2.3"):**
- Rounded rect, fill `#1E2435`, border 1 pt `#E8A020`
- Title: `CRYSTALLIZATION MECHANISM` Barlow SemiBold 14 pt `#E8A020`

Four numbered steps:
```
1. ACID ATTACK: H3PO4 dissolves Fe --> Fe2+ + 2e-; 2H+ + 2e- --> H2
2. pH RISE: Local pH at metal surface rises from ~3.0 to ~5.5+
3. CRYSTAL NUCLEATION: Zn3(PO4)2 crystallizes on Ti nucleation sites
4. ACCELERATOR: NO2-/NO3- oxidize Fe2+ to Fe3+, depolarize cathode
```

Step numbers: `#E8A020`. Text: `#F0EDE8`. JetBrains Mono 12 pt.

**Crystal types callout (Y: 13.5"):**
- `ON STEEL: Zn2Fe(PO4)2.4H2O (phosphophyllite) -- harder, better adhesion` JetBrains Mono 12 pt `#27AE60`
- `ON ALL SUBSTRATES: Zn3(PO4)2.4H2O (hopeite) -- softer, less alkali-resistant` JetBrains Mono 12 pt `#2EC4B6`

---

### ZONE 4 -- Bath Chemistry + FA/TA Ratio

**Section label:** `BATH CHEMISTRY -- MULTI-COMPONENT CONTROL` -- Y: 14.7".

**BLOCK D -- Component Table (Y: 15.3" to 18.5")**

Full-width parameter table:

| Component | Concentration | Function |
|---|---|---|
| Zinc (Zn2+) | 0.8--2.0 g/L (spray) | Primary coating cation |
| Phosphoric acid (total PO4) | 10--25 g/L | Film-forming anion |
| Nickel (Ni2+) | 0.5--1.5 g/L | Grain refinement; promotes phosphophyllite |
| Manganese (Mn2+) | 0.5--1.5 g/L | Grain refinement; improves corrosion resistance |
| Nitrite (NO2-) | 0.05--0.15 g/L | Accelerator (immersion baths) |
| Nitrate (NO3-) | 3--8 g/L | Accelerator (spray systems) |
| Fluoride (F-) | 0.5--2.0 g/L | Required for aluminum/galvanized substrates |

Header: Barlow SemiBold 14 pt `#F0EDE8`, fill `#3A4055`. Data: JetBrains Mono 12 pt `#F0EDE8`, alternating rows.

**BLOCK E -- Free Acid / Total Acid Ratio Gauge (Y: 18.8" to 20.3")**

- Rounded rect, full width, H: 1.3", fill `#1E2435`
- Title left: `THE CRITICAL RATIO` Barlow Condensed ExtraBold 18 pt `#F0EDE8`
- Subtitle: `Free Acid : Total Acid` JetBrains Mono 14 pt `#F0EDE8`

Horizontal bar gauge (X: 6.0", W: 17.0", H: 0.5"):
- Red zone left: `< 1:10` fill `#E05C5C` at 40% -- `High free acid = heavy/powdery coating`
- Green zone center: `1:10 to 1:20` fill `#27AE60` at 40% -- `OPTIMAL`
- Red zone right: `> 1:20` fill `#E05C5C` at 40% -- `Low free acid = light/no coating`
- Optimal marker: triangle at `1:15` -- `#27AE60`

---

### ZONE 5 -- Coating Weight + P-Ratio

**Section label:** `COATING WEIGHT AND CRYSTAL QUALITY` -- Y: 20.7".

**BLOCK F -- Two-Column Layout (Y: 21.3" to 26.3")**

**Left -- Coating Weight Range Bar (X: 0.5", W: 11.0"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `COATING WEIGHT` Barlow SemiBold 20 pt `#E8A020`

Vertical range bar:
- `100--200 mg/ft2` fill `#E8A020` at 20% -- `Light -- cold forming, light-duty paint`
- `200--500 mg/ft2` fill `#27AE60` at 40% -- `MEDIUM -- automotive OEM target (150--350)`
- `500--1000+ mg/ft2` fill `#E8A020` at 20% -- `Heavy -- oil retention, military`

Additional properties:
| Property | Value |
|---|---|
| Thickness | 2--25 um (0.08--1.0 mil) |
| Crystal size (conditioned) | 2--10 um |
| Color | Medium to dark gray |
| Bare salt spray | 4--48 hours |
| With e-coat + topcoat | 500--1500+ hours |

**Right -- P-Ratio and Spray vs. Immersion (X: 12.0", W: 11.5"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#2EC4B6` 0.06"
- Title: `P-RATIO & APPLICATION METHOD` Barlow SemiBold 20 pt `#2EC4B6`

**P-Ratio section:**
- `Phosphophyllite : Hopeite Ratio (P-ratio)` Barlow SemiBold 14 pt `#F0EDE8`
- `P-ratio = phosphophyllite / (phosphophyllite + hopeite)` JetBrains Mono 12 pt `#F0EDE8`
- `P-ratio > 0.5 preferred for automotive OEM` JetBrains Mono 12 pt `#27AE60`
- `Measured by XRD or chemical dissolution` Inter Regular 12 pt `#F0EDE8` at 60%
- `Higher Ni in bath promotes phosphophyllite on steel` Inter Regular 12 pt `#F0EDE8` at 60%

**Spray vs. Immersion:**
| Parameter | Spray | Immersion |
|---|---|---|
| Temperature | 95--130 F | 130--200 F |
| Time | 1--3 min | 3--10 min |
| Free acid | 0.5--1.5 pts | 0.8--2.0 pts |
| Total acid | 15--30 pts | 20--40 pts |

---

### ZONE 6 -- Defect Diagnosis Grid

**Section label:** `WHAT GOES WRONG -- 6 COMMON DEFECTS` -- Y: 26.7".

**BLOCK G -- Defect Cards (Y: 27.3" to 32.3")**

Top row: 3 cards. Bottom row: 3 cards.

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | COARSE CRYSTALS | `#E05C5C` | Conditioner failure; pH wrong; no conditioner | Check/replace conditioner; verify pH 7.5--9.5 |
| R1C2 | LIGHT COATING | `#E8A020` | Low TA; low temp; short time; high FA | Increase TA; reduce FA; increase time/temp |
| R1C3 | HEAVY/POWDERY | `#E8A020` | Low FA; excess zinc; excess time | Increase FA; reduce time; check zinc |
| R2C1 | INCOMPLETE COVERAGE | `#E05C5C` | Oil contamination; cleaner failure; passive substrate | Improve cleaning; check substrate condition |
| R2C2 | EXCESS SLUDGE | `#E05C5C` | High iron carryover; insufficient filtration | Improve filtration; reduce drag-over |
| R2C3 | MUD CRACKING | `#E05C5C` | Coating too heavy; dried too fast at high temp | Reduce coating weight; lower initial oven temp |

Each card: Rounded rect, W: 7.33", H: 2.3", fill `#1E2435`, left accent 0.06" in defect color.
Problem: Barlow SemiBold 14 pt in accent color. Cause: Inter Regular 12 pt `#F0EDE8`. Fix: Inter Medium 12 pt `#27AE60`.

---

### ZONE 7 -- Footer

Standard. Title: `Zinc Phosphate -- Conversion Stage`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; Products Finishing; MIL-DTL-16232; GM 6041M; ASTM D2092. Zinc phosphate bath chemistry is proprietary -- consult your process supplier for product-specific parameters.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Zinc Phosphate Conversion Stage -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the densest poster in the CC-02 cluster -- comparable to Poster #156 (Iron Phosphate Conversion Stage) but with significantly more complexity. The multi-component bath chemistry table, the FA:TA ratio gauge, and the P-ratio explanation are the three analytical pillars. The crystal mechanism inset must show the key difference from iron phosphate: crystalline precipitation on nucleation sites rather than amorphous film formation by direct acid attack.

The phosphophyllite vs. hopeite distinction is real shop-floor knowledge -- operators who understand this can explain why their zinc phosphate coating performs differently on steel vs. galvanized substrates. The P-ratio callout connects the bath chemistry (nickel level) to the coating quality metric (phosphophyllite content), which is the kind of insight that makes this poster genuinely useful rather than just decorative.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #164 -- Construction Workup v1.0*
*2026-04-26*
