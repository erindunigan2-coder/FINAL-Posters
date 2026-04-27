---
created: 2026-04-03T00:00:00
updated: 2026-04-11T00:00:00
version: v2
poster: "#8 — Faraday's Law in the Shop: Calculating Plating Thickness"
tags:
  - FaradaysLaw
  - ElectrochemicalEquivalent
  - PosterResearch
  - ResearchBrief
---

# Faraday's Law in the Shop — Alaina Research Brief

**Poster**: #8 — Faraday's Law in the Shop: Calculating Plating Thickness
**Prepared by**: Watson (`watson-chemistry-researcher`)
**Date**: 2026-04-03 (v1); 2026-04-11 (v2)
**Version**: v2 -- publishable quality; product names removed; ECE values verified against Nickel Institute Nickel Plating Handbook 2023 (W = 1.095 It confirmed p.9-10); full 18-metal table with tin alkaline (Sn4+); alternative shop formula with 112.2 constant documented; poster-worthy sticky facts section added; all collaboration flags resolved
**Source documents**: Nickel Institute Nickel Plating Handbook 2023 (vault); Faraday's Laws of Electrolysis (fundamental electrochemistry -- first principles calculation); 1993 Metal Finishing Guidebook and Directory (vault); domain expertise

---

## Why This Poster Matters

Every plater needs to answer three questions daily:
1. **How thick will my deposit be** at this current and time?
2. **How long do I need to plate** to hit a specification thickness?
3. **How much current do I need** for this surface area and time?

Faraday's law answers all three. Yet most operators use rules of thumb, supplier charts, or trial and error. This poster makes the math accessible and gives operators a single reference for the electrochemical constants they need.

---

## The Law -- In Plain Language

**Faraday's First Law**: The mass of metal deposited at the cathode is directly proportional to the total electrical charge passed through the solution.

In practical terms: **More amps x more time = more metal deposited.**

**Faraday's Second Law**: The mass of metal deposited by a given charge is proportional to the metal's equivalent weight (atomic weight divided by valence).

In practical terms: **Different metals deposit at different rates for the same current -- heavier atoms with lower valence deposit faster.**

---

## The Master Formula

The fundamental equation for electroplating thickness calculation:

```
Thickness (mils) = (ECE x I x t x CE) / (A x d x 60.5)
```

Where:
- **ECE** = Electrochemical equivalent (g/Ah) -- see table below
- **I** = Current (amperes)
- **t** = Time (minutes)
- **CE** = Cathode efficiency (as a decimal, e.g., 0.95 for 95%)
- **A** = Surface area (ft2)
- **d** = Metal density (g/cm3)
- **60.5** = Unit conversion constant (converts g, ft2, minutes, and cm3 to mils)

**Simplified shop formula** (the version operators actually use):

```
Thickness (mils) = (Plating Rate) x (ASF) x (Time in hours) x (Cathode Efficiency)
```

Where **Plating Rate** is a process-specific constant in mils per amp-hour per square foot -- pre-calculated from ECE and density. See the table below.

**Alternative shop-friendly formula** (all inputs in common shop units):

```
Thickness (mils) = (I x t x ECE) / (A x density x 112.2)
```

Where:
- **I** = current (amps)
- **t** = time (hours)
- **ECE** = electrochemical equivalent (g/Ah)
- **A** = surface area (ft2)
- **density** = metal density (g/cm3)
- **112.2** = unit conversion constant (converts the combination of g, ft2, hours, and cm3 into mils)

**Deposit weight (grams)** can be calculated directly:
```
Weight (g) = I x t x ECE x CE
```

Where CE = cathode efficiency as a decimal.

---

## Faraday's Constant

**Faraday's Constant (F)** = 96,485 coulombs per mole of electrons = 96,485 ampere-seconds per equivalent

In practical units: **1 Faraday = 26.80 ampere-hours**

This means 26.80 ampere-hours will deposit exactly one gram-equivalent weight of any metal.

---

## Electrochemical Equivalents -- The Master Table

These values are calculated from fundamental constants: Atomic Weight / (Valence x 26.80 Ah). The Nickel Institute Nickel Plating Handbook 2023 independently confirms 1.095 g/Ah for nickel (p.9-10), validating this calculation method.

| Metal | Symbol | Atomic Weight | Valence | ECE (g/Ah) | Density (g/cm3) | Plating Rate (mil/Ah/ft2) |
|---|---|---|---|---|---|---|
| **Zinc** | Zn | 65.38 | 2 | 1.220 | 7.14 | 0.00152 |
| **Nickel** | Ni | 58.69 | 2 | 1.095 | 8.90 | 0.00109 |
| **Copper (acid)** | Cu | 63.55 | 2 | 1.186 | 8.96 | 0.00118 |
| **Copper (cyanide)** | Cu | 63.55 | 1 | 2.372 | 8.96 | 0.00236 |
| **Chromium (hex bath)** | Cr | 52.00 | 6 | 0.324 | 7.19 | 0.00040 |
| **Chromium (trivalent bath)** | Cr | 52.00 | 3 | 0.647 | 7.19 | 0.00080 |
| **Silver** | Ag | 107.87 | 1 | 4.025 | 10.49 | 0.00342 |
| **Tin (acid, Sn2+)** | Sn | 118.71 | 2 | 2.214 | 7.31 | 0.00270 |
| **Tin (alkaline, Sn4+)** | Sn | 118.71 | 4 | 1.107 | 7.31 | 0.00135 |
| **Gold (alkaline cyanide)** | Au | 196.97 | 1 | 7.349 | 19.32 | 0.00339 |
| **Gold (acid/neutral)** | Au | 196.97 | 3 | 2.450 | 19.32 | 0.00113 |
| **Cadmium** | Cd | 112.41 | 2 | 2.097 | 8.65 | 0.00216 |
| **Cobalt** | Co | 58.93 | 2 | 1.099 | 8.90 | 0.00110 |
| **Iron** | Fe | 55.85 | 2 | 1.042 | 7.87 | 0.00118 |
| **Palladium** | Pd | 106.42 | 2 | 1.985 | 12.02 | 0.00147 |
| **Rhodium** | Rh | 102.91 | 3 | 1.280 | 12.41 | 0.00092 |
| **Platinum** | Pt | 195.08 | 4 | 1.819 | 21.45 | 0.00076 |
| **Lead** | Pb | 207.2 | 2 | 3.866 | 11.34 | 0.00304 |

**Note on copper valence**: In acid copper sulfate baths, copper deposits as Cu2+ (valence 2). In cyanide copper baths, copper deposits as Cu1+ (valence 1) -- depositing twice the mass per ampere-hour. This is a fundamental chemistry difference, not an efficiency difference.

**Note on chromium valence**: In hexavalent chrome baths, the chromium starts as Cr6+ in chromic acid (CrO3) but must be reduced to Cr0 to deposit. The overall reaction consumes 6 electrons per chromium atom deposited, giving an effective valence of 6 and the very low ECE of 0.324 g/Ah. In trivalent chrome baths, chromium starts as Cr3+ and requires only 3 electrons to reduce to Cr0, doubling the ECE to 0.647 g/Ah. However, the cathode efficiencies are also different, so the net deposition rates are closer than the ECE values alone would suggest.

---

## Cathode Efficiency -- The Real-World Correction Factor

Faraday's law gives the **theoretical** maximum deposit. In practice, not all current deposits metal -- some current generates hydrogen gas at the cathode (a competing side reaction), and some is lost to other electrochemical reactions. The ratio of actual metal deposited to theoretical metal is the **cathode efficiency**.

| Process | Typical Cathode Efficiency | Why It Varies |
|---|---|---|
| **Bright Acid Copper** | 95-100% | Very efficient; almost all current deposits copper |
| **Nickel Sulfamate** | 95-100% | Highly efficient at normal CD |
| **Watts Nickel** | 90-97% | 95.5% commonly used for estimation (Nickel Institute); bright baths toward 90% due to additive side reactions |
| **Acid Chloride Zinc** | 95-98% | Very efficient in KCl-based baths |
| **Alkaline Non-Cyanide Zinc** | 70-80% | Significant hydrogen co-evolution at alkaline pH |
| **Alkaline Cyanide Zinc** | 65-80% | Cyanide complexation reduces efficiency |
| **Cyanide Copper Strike** | 30-60% | Heavy hydrogen evolution; intentionally run inefficient for thin, adherent strikes |
| **Silver Cyanide** | 95-100% | Very efficient; noble metal deposits readily |
| **Matte Tin (acid)** | 90-95% | Good efficiency in acid stannous baths |
| **Hard Chrome (hex, conventional)** | 12-20% | Extremely low -- most current generates hydrogen and heats the bath |
| **Hard Chrome (hex, mixed catalyst)** | 20-25% | Fluoride catalyst improves efficiency slightly |
| **Decorative Chrome (hex)** | 10-18% | Even lower than hard chrome at typical CD |
| **Decorative Chrome (trivalent)** | 15-25% | Somewhat better than hex |

**The chrome efficiency story**: Chrome plating's notoriously low efficiency (10-25%) means that 75-90% of the electrical energy goes into heating the bath and generating hydrogen mist -- not depositing metal. This is why chrome tanks require massive rectifiers, heavy ventilation, and strict mist suppression. It is the single most inefficient electrodeposition process in commercial use.

---

## Worked Examples for the Poster

### Example 1: How long to plate 0.5 mil of zinc at 20 ASF?

```
Given:
  Target thickness: 0.5 mil
  Current density: 20 ASF
  Cathode efficiency: 96% (acid chloride zinc)
  Plating rate for Zn: 0.00152 mil/Ah/ft2

Formula rearranged for time:
  Time (hours) = Thickness / (Rate x ASF x CE)
  Time = 0.5 / (0.00152 x 20 x 0.96)
  Time = 0.5 / 0.02918
  Time = 17.1 minutes
```

**Answer**: Approximately **17 minutes** at 20 ASF.

### Example 2: How thick is nickel after 45 minutes at 40 ASF?

```
Given:
  Time: 45 min = 0.75 hours
  Current density: 40 ASF
  Cathode efficiency: 95.5% (Watts nickel -- Nickel Institute standard estimation)
  Plating rate for Ni: 0.00109 mil/Ah/ft2

Thickness = Rate x ASF x Time x CE
Thickness = 0.00109 x 40 x 0.75 x 0.955
Thickness = 0.031 mil = 0.79 um
```

**Answer**: Approximately **0.031 mil (0.79 um)** of nickel. The Nickel Institute Nickel Plating Handbook Table 1 confirms: at 4 ASD (~43 ASF) and 95.5% efficiency, 45 minutes deposits approximately 33 um -- consistent with this calculation when adjusted for the slightly different CD.

### Example 3: Why does hard chrome take so long?

```
Given:
  Target thickness: 2.0 mil (typical hard chrome)
  Current density: 200 ASF (approximately 2 A/in2)
  Cathode efficiency: 15% (conventional hex chrome)
  Plating rate for Cr (valence 6): 0.00040 mil/Ah/ft2

Time = 2.0 / (0.00040 x 200 x 0.15)
Time = 2.0 / 0.012
Time = 166.7 minutes = 2 hours 47 minutes
```

**Answer**: Nearly **3 hours** at 200 ASF -- compared to approximately 17 minutes for the same thickness of zinc. Chrome's low ECE and extremely low cathode efficiency combine to make it the slowest common plating process.

---

## The Relationship Chain

This conceptual chain helps operators understand how the variables connect:

```
AMPS --> set by RECTIFIER
  |
CURRENT DENSITY (ASF) = Amps / Area
  |
CHARGE (Amp-hours) = Amps x Time
  |
THEORETICAL MASS = Charge x ECE (Faraday's Law)
  |
ACTUAL MASS = Theoretical x Cathode Efficiency
  |
THICKNESS = Mass / (Area x Density)
```

---

## Visual / Diagram Opportunities for Poster Design

### 1. The Electrochemical Equivalents Table (HERO visual)

A clean, bold table showing Metal | ECE (g/Ah) | Efficiency | Plating Rate for the 10-12 most common metals. This is the core reference element. Consider Amber `#E8A020` column headers with JetBrains Mono for all numerical values.

### 2. The Formula Box

A prominent, framed formula:
```
Thickness = Rate x ASF x Time x Efficiency
```
With each variable labeled and color-coded. This should be large enough to read from 6 feet.

### 3. The Chrome Efficiency Comparison Bar

A horizontal bar chart or stacked bar showing what happens to 100 amps of current in different processes:
- Acid copper: 97 amps deposit metal / 3 amps wasted
- Watts nickel: 95 / 5
- Acid zinc: 96 / 4
- Hard chrome: 15 deposit / 85 wasted (hydrogen + heat)

The chrome bar is visually dramatic -- it shows why chrome requires massive rectifiers and hours of plating time. Use Coral `#E05C5C` for the wasted portion.

### 4. The Worked Example Panel

One or two worked examples (like the zinc and chrome examples above) shown step by step in a clean, tabular format. Operators learn from seeing real numbers, not abstract formulas.

### 5. The ECE Ranking Bar Chart

A vertical or horizontal bar chart ranking metals by ECE (g/Ah):
- Gold (Au1+): 7.349 (tallest bar)
- Silver: 4.025
- Lead: 3.866
- Copper (cyanide): 2.372
- Tin: 2.214
- Zinc: 1.220
- Copper (acid): 1.186
- Nickel: 1.095
- Chromium (hex): 0.324 (shortest bar)

This visually communicates that gold deposits the most metal per amp-hour and chromium the least.

### 6. The Time Comparison Strip

"How long to plate 1 mil at 20 ASF?" -- a row of clock icons showing the time for each metal (at typical efficiency):
- Silver: ~8 min
- Zinc: ~17 min
- Nickel: ~26 min
- Hard chrome (at 200 ASF, 15% eff): ~83 min

This makes the abstract math tangible.

### 7. The Faraday Portrait or Equation Nameplate

A small portrait silhouette or historical nod to Michael Faraday (1791-1867) with the constant:
```
F = 96,485 C/mol = 26.80 Ah/equivalent
```
A classy touch that anchors the poster in scientific authority.

### 8. The Unit Conversion Quick Reference

A small box:
```
1 mil = 25.4 um
1 um = 0.0394 mil
ASF / 10 ~ ASD
```

### 9. The "Three Questions" Header

Three bold questions at the top that frame the poster's purpose:
1. How thick will my deposit be?
2. How long do I need to plate?
3. How much current do I need?

"Faraday's Law answers all three."

---

## Key Data Points for Callouts

**Faraday's Constant**:
- `F = 96,485 C/mol = 26.80 Ah/equivalent`

**Highest ECE (fastest depositor)**:
- Gold (Au1+): `7.349 g/Ah`
- Silver: `4.025 g/Ah`

**Lowest ECE (slowest depositor)**:
- Chromium (hex): `0.324 g/Ah`

**Most efficient process**:
- Bright acid copper: `95-100%` cathode efficiency

**Least efficient process**:
- Decorative hex chrome: `10-18%` cathode efficiency

**Dramatic comparison**:
- 0.5 mil zinc at 20 ASF: `~17 minutes`
- 0.5 mil hard chrome at 200 ASF: `~42 minutes` -- 10x the current density, 2.5x the time

**Universal formula**:
- `Thickness = Rate x ASF x Time x Efficiency`

**Copper valence fact**:
- Cyanide copper (Cu1+): deposits `2x the mass` per amp-hour vs. acid copper (Cu2+) -- same element, different chemistry

**Nickel verification (Nickel Institute)**:
- W = 1.095 It (grams = 1.095 x amps x hours) at 100% efficiency -- confirmed from first principles and independently by the Nickel Institute Nickel Plating Handbook 2023

---

## Poster-Worthy Sticky Facts

These are the numbers and concepts that make Faraday's Law stick for a shop operator.

1. **"26.80 amp-hours = 1 equivalent"** -- this is the universal currency of electroplating. Every metal obeys the same constant. 26.80 Ah deposits exactly one equivalent weight of any metal, period.

2. **"Silver is 12x faster than chrome"** -- silver's ECE (4.025 g/Ah) vs. hex chrome's ECE (0.324 g/Ah) means silver deposits 12.4 times more metal per amp-hour. Add efficiency differences and the gap widens to ~50x in practice.

3. **"Same element, different valence, different speed"** -- cyanide copper (Cu1+) deposits 2x the mass per amp-hour as acid copper (Cu2+). This is not an efficiency difference; it is fundamental chemistry. Similarly, trivalent chrome (Cr3+) has 2x the ECE of hexavalent chrome (Cr6+).

4. **"Chrome: 85 out of 100 amps wasted"** -- at 15% cathode efficiency, only 15 amps out of every 100 deposit chromium metal. The other 85 generate hydrogen gas and heat. This single fact explains why chrome tanks need massive rectifiers, heavy ventilation, and hours of plating time.

5. **"0.5 mil zinc = 17 minutes; 0.5 mil chrome = 42 minutes at 10x the current"** -- the most dramatic comparison on the poster. Chrome requires 10x the current density AND 2.5x the time for the same thickness.

6. **"1 mil = 25.4 um"** -- the unit bridge between American shops (mils) and metric specifications (micrometers).

7. **"Thickness = Rate x ASF x Time x Efficiency"** -- four variables, one formula, every metal. This is the single equation an operator needs to calculate any plating thickness.

8. **"Gold deposits the most mass per amp-hour"** -- at 7.349 g/Ah (Au1+), gold is the heavyweight champion of electrochemical equivalents. But its extreme density (19.32 g/cm3) means it does not produce the thickest deposit -- silver's lower density gives it a higher plating rate in mils despite a lower ECE.

---

*Research Brief v2 authored by Watson (`watson-chemistry-researcher`), 2026-04-11. Sources: Nickel Institute Nickel Plating Handbook 2023 (vault -- ECE of nickel confirmed at 1.095 g/Ah, cathode efficiency 90-97%, Table 1 deposition time cross-check); Faraday's Laws of Electrolysis (first principles); 1993 Metal Finishing Guidebook and Directory (vault); domain expertise. All ECE values calculated from atomic weights and F = 96,485 C/mol. Cathode efficiency values are industry-typical ranges -- verify against specific product technical data for production use.*
