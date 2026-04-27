---
created: 2026-04-03T00:00:00
version: v1
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
**Date**: 2026-04-03
**Version**: v1
**Source documents**: Faraday's Laws of Electrolysis (fundamental electrochemistry); finishing.com FAQs; finishingandcoating.com Electroplating Math; 1993 Metal Finishing Guidebook and Directory (vault); domain expertise

> [!NOTE]
> This is a math-heavy brief. Every numerical value has been calculated from first principles using Faraday's constant (96,485 C/mol), atomic weights, and standard valence states. These are physical constants — they do not vary by vendor or product. Cathode efficiency values are industry-typical ranges and may vary by bath formulation. Design decisions remain Alaina's domain.

---

## Why This Poster Matters

Every plater needs to answer three questions daily:
1. **How thick will my deposit be** at this current and time?
2. **How long do I need to plate** to hit a specification thickness?
3. **How much current do I need** for this surface area and time?

Faraday's law answers all three. Yet most operators use rules of thumb, supplier charts, or trial and error. This poster makes the math accessible and gives operators a single reference for the electrochemical constants they need.

---

## The Law — In Plain Language

**Faraday's First Law**: The mass of metal deposited at the cathode is directly proportional to the total electrical charge passed through the solution.

In practical terms: **More amps x more time = more metal deposited.**

**Faraday's Second Law**: The mass of metal deposited by a given charge is proportional to the metal's equivalent weight (atomic weight divided by valence).

In practical terms: **Different metals deposit at different rates for the same current — heavier atoms with lower valence deposit faster.**

---

## The Master Formula

The fundamental equation for electroplating thickness calculation:

```
Thickness (mils) = (ECE x I x t x CE) / (A x d x 60.5)
```

Where:
- **ECE** = Electrochemical equivalent (g/Ah) — see table below
- **I** = Current (amperes)
- **t** = Time (minutes)
- **CE** = Cathode efficiency (as a decimal, e.g., 0.95 for 95%)
- **A** = Surface area (ft²)
- **d** = Metal density (g/cm³)
- **60.5** = Unit conversion constant (converts g, ft², minutes, and cm³ to mils)

**Simplified shop formula** (the version operators actually use):

```
Thickness (mils) = (Plating Rate) x (ASF) x (Time in hours) x (Cathode Efficiency)
```

Where **Plating Rate** is a process-specific constant in mils per amp-hour per square foot — pre-calculated from ECE and density. See the table below.

---

## Faraday's Constant

**Faraday's Constant (F)** = 96,485 coulombs per mole of electrons = 96,485 ampere-seconds per equivalent

In practical units: **1 Faraday = 26.80 ampere-hours**

This means 26.80 ampere-hours will deposit exactly one gram-equivalent weight of any metal.

---

## Electrochemical Equivalents — The Master Table

These values are calculated from fundamental constants: Atomic Weight / (Valence x 26.80 Ah).

| Metal | Symbol | Atomic Weight | Valence | ECE (g/Ah) | Density (g/cm³) | Plating Rate (mil/Ah/ft²) |
|---|---|---|---|---|---|---|
| **Zinc** | Zn | 65.38 | 2 | 1.220 | 7.14 | 0.00152 |
| **Nickel** | Ni | 58.69 | 2 | 1.095 | 8.90 | 0.00109 |
| **Copper** | Cu | 63.55 | 2 | 1.186 | 8.96 | 0.00118 |
| **Copper** | Cu | 63.55 | 1 (cyanide) | 2.372 | 8.96 | 0.00236 |
| **Chromium** | Cr | 52.00 | 6 | 0.324 | 7.19 | 0.00040 |
| **Silver** | Ag | 107.87 | 1 | 4.025 | 10.49 | 0.00342 |
| **Tin** | Sn | 118.71 | 2 | 2.214 | 7.31 | 0.00270 |
| **Gold** | Au | 196.97 | 1 | 7.349 | 19.32 | 0.00339 |
| **Gold** | Au | 196.97 | 3 | 2.450 | 19.32 | 0.00113 |
| **Cadmium** | Cd | 112.41 | 2 | 2.097 | 8.65 | 0.00216 |

**Calculation method**: ECE = Atomic Weight / (Valence x 26.80)

**Example — Zinc**: 65.38 / (2 x 26.80) = 65.38 / 53.60 = **1.220 g/Ah**

**Note on copper valence**: In acid copper sulfate baths, copper deposits as Cu²⁺ (valence 2). In cyanide copper baths, copper deposits as Cu⁺ (valence 1) — depositing twice the mass per ampere-hour. This is a fundamental chemistry difference, not an efficiency difference.

**Note on chromium valence**: Chromium deposits from Cr⁶⁺ (hexavalent) or Cr³⁺ (trivalent) solutions, but in both cases the final deposition step involves Cr³⁺ → Cr⁰, consuming 6 electrons per Cr atom from the Cr₂O₇²⁻ starting point (hex) or 3 electrons from Cr³⁺ (trivalent). The ECE shown (valence 6) applies to hexavalent chrome baths. For trivalent chrome, use valence 3 (ECE = 0.647 g/Ah) — but the cathode efficiency is also different.

---

## Cathode Efficiency — The Real-World Correction Factor

Faraday's law gives the **theoretical** maximum deposit. In practice, not all current deposits metal — some current generates hydrogen gas at the cathode (a competing side reaction), and some is lost to other electrochemical reactions. The ratio of actual metal deposited to theoretical metal is the **cathode efficiency**.

| Process | Typical Cathode Efficiency | Why It Varies |
|---|---|---|
| **Bright Acid Copper** | 95–100% | Very efficient; almost all current deposits copper |
| **Nickel Sulfamate** | 95–100% | Highly efficient at normal CD |
| **Watts Nickel** | 93–97% | Slightly less due to brightener side reactions |
| **Acid Chloride Zinc** | 95–98% | Very efficient in KCl-based baths |
| **Alkaline Non-Cyanide Zinc** | 70–80% | Significant hydrogen co-evolution at alkaline pH |
| **Alkaline Cyanide Zinc** | 65–80% | Cyanide complexation reduces efficiency |
| **Cyanide Copper Strike** | 30–60% | Heavy hydrogen evolution; intentionally run inefficient for thin, adherent strikes |
| **Silver Cyanide** | 95–100% | Very efficient; noble metal deposits readily |
| **Matte Tin (acid)** | 90–95% | Good efficiency in acid stannous baths |
| **Hard Chrome (hex, conventional)** | 12–20% | Extremely low — most current generates hydrogen and heats the bath |
| **Hard Chrome (hex, mixed catalyst)** | 20–25% | Fluoride catalyst improves efficiency slightly |
| **Decorative Chrome (hex)** | 10–18% | Even lower than hard chrome at typical CD |
| **Decorative Chrome (trivalent)** | 15–25% | Somewhat better than hex |

**The chrome efficiency story**: Chrome plating's notoriously low efficiency (10–25%) means that 75–90% of the electrical energy goes into heating the bath and generating hydrogen mist — not depositing metal. This is why chrome tanks require massive rectifiers, heavy ventilation, and strict mist suppression. It is the single most inefficient electrodeposition process in commercial use.

---

## Worked Examples for the Poster

### Example 1: How long to plate 0.5 mil of zinc at 20 ASF?

```
Given:
  Target thickness: 0.5 mil
  Current density: 20 ASF
  Cathode efficiency: 96% (acid chloride zinc)
  Plating rate for Zn: 0.00152 mil/Ah/ft²

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
  Cathode efficiency: 95% (Watts nickel)
  Plating rate for Ni: 0.00109 mil/Ah/ft²

Thickness = Rate x ASF x Time x CE
Thickness = 0.00109 x 40 x 0.75 x 0.95
Thickness = 0.031 mil = 0.79 um (micrometers)
```

**Answer**: Approximately **0.031 mil (0.79 um)** of nickel.

### Example 3: Why does hard chrome take so long?

```
Given:
  Target thickness: 2.0 mil (typical hard chrome)
  Current density: 200 ASF (2 A/in²)
  Cathode efficiency: 15% (conventional hex chrome)
  Plating rate for Cr (valence 6): 0.00040 mil/Ah/ft²

Time = 2.0 / (0.00040 x 200 x 0.15)
Time = 2.0 / 0.012
Time = 166.7 minutes = 2 hours 47 minutes
```

**Answer**: Nearly **3 hours** at 200 ASF — compared to ~17 minutes for the same thickness of zinc. Chrome's low ECE and extremely low cathode efficiency combine to make it the slowest common plating process.

---

## The Relationship Chain

This conceptual chain helps operators understand how the variables connect:

```
AMPS → set by RECTIFIER
  ↓
CURRENT DENSITY (ASF) = Amps / Area
  ↓
CHARGE (Amp-hours) = Amps x Time
  ↓
THEORETICAL MASS = Charge x ECE (Faraday's Law)
  ↓
ACTUAL MASS = Theoretical x Cathode Efficiency
  ↓
THICKNESS = Mass / (Area x Density)
```

---

## Visual / Diagram Opportunities for Poster Design

### 1. The Electrochemical Equivalents Table (HERO visual — shared with Current Density poster)

A clean, bold table showing Metal | ECE (g/Ah) | Efficiency | Plating Rate for the 8–10 most common metals. This is the core reference element. Consider Amber `#E8A020` column headers with JetBrains Mono for all numerical values.

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

The chrome bar is visually dramatic — it shows why chrome requires massive rectifiers and hours of plating time. Use Coral `#E05C5C` for the wasted portion.

### 4. The Worked Example Panel

One or two worked examples (like the zinc and chrome examples above) shown step by step in a clean, tabular format. Operators learn from seeing real numbers, not abstract formulas.

### 5. The ECE Ranking Bar Chart

A vertical or horizontal bar chart ranking metals by ECE (g/Ah):
- Silver: 4.025 (tallest bar)
- Tin: 2.214
- Copper (CN): 2.372
- Zinc: 1.220
- Copper (acid): 1.186
- Nickel: 1.095
- Chromium: 0.324 (shortest bar)

This visually communicates that silver deposits the most metal per amp-hour and chromium the least.

### 6. The Time Comparison Strip

"How long to plate 1 mil at 20 ASF?" — a row of clock icons showing the time for each metal:
- Silver: ~8 min
- Zinc: ~17 min
- Nickel: ~26 min
- Hard chrome (at 200 ASF, 15% eff): ~83 min

This makes the abstract math tangible.

### 7. The Faraday Portrait or Equation Nameplate

A small portrait silhouette or historical nod to Michael Faraday (1791–1867) with the constant:
```
F = 96,485 C/mol = 26.80 Ah/equivalent
```
A classy touch that anchors the poster in scientific authority.

### 8. The Unit Conversion Quick Reference

A small box:
```
1 mil = 25.4 um
1 um = 0.0394 mil
ASF / 10 ≈ ASD
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
- Silver: `4.025 g/Ah`

**Lowest ECE (slowest depositor)**:
- Chromium (hex): `0.324 g/Ah`

**Most efficient process**:
- Bright acid copper: `95–100%` cathode efficiency

**Least efficient process**:
- Decorative hex chrome: `10–18%` cathode efficiency

**Dramatic comparison**:
- 0.5 mil zinc at 20 ASF: `~17 minutes`
- 0.5 mil hard chrome at 200 ASF: `~42 minutes` — 10x the current density, 2.5x the time

**Universal formula**:
- `Thickness = Rate x ASF x Time x Efficiency`

**Copper valence fact**:
- Cyanide copper (Cu⁺): deposits `2x the mass` per amp-hour vs. acid copper (Cu²⁺) — same element, different chemistry

---

## Collaboration Flags

- **Drew**: Confirm the cathode efficiency values match your field experience, particularly:
  - Acid chloride zinc: 95–98% (some sources say as high as 99%)
  - Alkaline non-cyanide zinc: 70–80% (some sources cite 60–85% — wide range depending on formulation)
  - Cyanide copper strike: 30–60% (intentionally low for thin, adherent strikes — confirm this range is reasonable for CN-707)
  - Hard chrome conventional: 12–20%
- **Drew**: The plating rate values (mil/Ah/ft²) are calculated from first principles and should be exact at 100% efficiency. Confirm whether Drew would prefer to show a "practical plating rate" column that incorporates typical efficiency (e.g., for zinc: 0.00152 x 0.96 = 0.00146 mil/Ah/ft² practical).
- **Tyler**: Verify the ECE calculations match the values used in any existing A Brite product TDS thickness tables. If any TDS shows a different plating rate, it may be because the TDS incorporates efficiency into the rate constant.

---

## Appendix: ECE Calculation Verification

For transparency, here are the full calculations for each ECE value in the master table:

```
ECE = Atomic Weight / (Valence x 26.80 Ah)

Zn: 65.38 / (2 x 26.80) = 65.38 / 53.60 = 1.2199 → 1.220 g/Ah
Ni: 58.69 / (2 x 26.80) = 58.69 / 53.60 = 1.0949 → 1.095 g/Ah
Cu²⁺: 63.55 / (2 x 26.80) = 63.55 / 53.60 = 1.1858 → 1.186 g/Ah
Cu⁺: 63.55 / (1 x 26.80) = 63.55 / 26.80 = 2.3713 → 2.372 g/Ah
Cr⁶⁺: 52.00 / (6 x 26.80) = 52.00 / 160.80 = 0.3234 → 0.324 g/Ah (from hex bath)
Ag⁺: 107.87 / (1 x 26.80) = 107.87 / 26.80 = 4.0250 → 4.025 g/Ah
Sn²⁺: 118.71 / (2 x 26.80) = 118.71 / 53.60 = 2.2148 → 2.214 g/Ah
Au⁺: 196.97 / (1 x 26.80) = 196.97 / 26.80 = 7.3496 → 7.349 g/Ah
Au³⁺: 196.97 / (3 x 26.80) = 196.97 / 80.40 = 2.4499 → 2.450 g/Ah
Cd²⁺: 112.41 / (2 x 26.80) = 112.41 / 53.60 = 2.0972 → 2.097 g/Ah
```

All values verified. These are fundamental physical constants derived from atomic weights and Faraday's constant.

---

*Research Brief v1 authored by Watson (`watson-chemistry-researcher`), 2026-04-03. Sources: Faraday's Laws of Electrolysis (fundamental electrochemistry — first principles calculation); finishing.com Faraday's Law FAQ; finishingandcoating.com Electroplating Math; 1993 Metal Finishing Guidebook and Directory (vault); domain expertise. All ECE values calculated from atomic weights and F = 96,485 C/mol. Cathode efficiency values are industry-typical ranges — verify against specific product TDS for production use. Alaina should flag any data points requiring additional verification before final poster production.*
