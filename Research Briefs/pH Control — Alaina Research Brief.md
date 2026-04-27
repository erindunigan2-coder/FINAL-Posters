---
created: 2026-04-03T00:00:00
updated: 2026-04-11
version: v2
poster: "#12 — The pH Control Poster"
tags:
  - pHControl
  - PosterResearch
  - ResearchBrief
---

# pH Control — Alaina Research Brief

**Poster**: #12 -- The pH Control Poster
**Prepared by**: Watson (`watson-chemistry-researcher`)
**Date**: 2026-04-03 (v1); 2026-04-11 (v2)
**Version**: v2 -- publishable quality; collaboration flags resolved; product names removed from poster content per standing rule; pH ranges cross-verified against Nickel Institute Nickel Plating Handbook 2023 (nickel pH 3.8--4.5 confirmed), 1993 Metal Finishing Guidebook, and Drew's Quick Reference Notes; acid copper confirmed as concentration-controlled (not pH-controlled); NiCO3 confirmed as preferred pH raise agent for nickel; sticky facts section added
**Source documents**: Nickel Institute Nickel Plating Handbook 2023 (vault); 1993 Metal Finishing Guidebook and Directory (vault); Drew's Quick Reference Metal Finishing Notes (vault); domain expertise

---

## Why This Poster Matters

Every plating bath has a target pH, and every operator knows to check it. But many operators treat pH as a number to hit rather than a control variable they understand. This poster answers the questions:
- What is pH, really?
- Why does it matter for my specific process?
- What happens if it drifts high or low?
- How do I adjust it?

---

## What pH Actually Is

**pH** = a measure of hydrogen ion concentration in solution, on a logarithmic scale from 0 to 14.

```
pH = -log[H+]
```

| pH Value | Character | H+ Concentration |
|---|---|---|
| 0--1 | Strongly acidic | Very high |
| 2--4 | Moderately acidic | Moderate |
| 5--6 | Weakly acidic | Low |
| 7 | Neutral (pure water) | 10^-7 mol/L |
| 8--9 | Weakly alkaline | Low OH- |
| 10--12 | Moderately alkaline | Moderate OH- |
| 13--14 | Strongly alkaline | Very high OH- |

**The key concept**: The scale is **logarithmic** -- each whole number represents a **10x change** in H+ concentration. A bath at pH 4.0 has 10x more H+ than a bath at pH 5.0, and 100x more than pH 6.0. Small pH numbers = big chemical changes.

---

## pH Ranges for Every Major Plating Process

This is the master reference table -- the core content of the poster.

### Acid Processes

| Process | pH Range | Target | Adjustment (raise) | Adjustment (lower) |
|---|---|---|---|---|
| **Acid Chloride Zinc (KCl)** | 4.8--5.8 | 5.2--5.4 | NaOH or KOH (dilute) | HCl (dilute) |
| **Bright Acid Copper (CuSO4)** | Not pH-controlled | N/A | N/A -- controlled by H2SO4 concentration | Sulfuric acid additions |
| **Watts Nickel (bright)** | 3.8--4.5 | 4.0--4.2 | NiCO3 (nickel carbonate) or NaOH (dilute) | H2SO4 or HCl (dilute) |
| **Nickel Sulfamate** | 3.5--4.5 | 4.0 | NiCO3 | Sulfamic acid |
| **Matte Tin (acid)** | 0.5--2.0 | 1.0--1.5 | N/A -- low pH by design | Acid additions |
| **Hard Chrome (hex)** | <1.0 | Not pH-controlled | N/A -- sulfate ratio controls, not pH | CrO3/H2SO4 ratio |

### Alkaline Processes

| Process | pH Range | Target | Adjustment (raise) | Adjustment (lower) |
|---|---|---|---|---|
| **Alkaline Non-Cyanide Zinc** | 12.5--14.0 | 13.0--13.5 | NaOH | N/A -- rarely needs lowering |
| **Alkaline Cyanide Zinc** | 12.0--13.5 | 12.5--13.0 | NaOH | N/A |
| **Cyanide Copper Strike** | 11.0--13.0 | 12.0--12.5 | NaOH or KOH | N/A |
| **Silver Cyanide** | 11.5--13.0 | 12.0--12.5 | KOH | N/A |
| **Alkaline Cleaners** | 10--13 | 11--12 | NaOH additions | N/A |

### Electroless and Conversion Processes

| Process | pH Range | Target | Adjustment (raise) | Adjustment (lower) |
|---|---|---|---|---|
| **Electroless Nickel (Mid-P)** | 4.5--5.2 | 4.7--5.0 | NaOH or NH4OH | H2SO4 (dilute) |
| **Electroless Nickel (High-P)** | 4.2--5.0 | 4.4--4.8 | NaOH | H2SO4 |
| **Electroless Nickel (Low-P)** | 6.0--9.0 | Variable | NaOH or NH4OH | Acid |
| **Trivalent Passivation** | 1.5--2.5 | 1.8--2.2 | NaOH (dilute, very carefully) | HCl or H2SO4 |
| **Hexavalent Passivation** | 0.5--2.0 | Process-dependent | NaOH | HCl |

---

## What Happens When pH Drifts

### pH Too Low (More Acidic Than Target)

| Process | Effect of Low pH |
|---|---|
| **Acid zinc** | Excessive zinc dissolution from anodes; zinc concentration rises uncontrollably; hydrogen evolution increases |
| **Watts nickel** | Increased hydrogen evolution; pitting; reduced throwing power; hydrogen embrittlement risk on steel substrates |
| **EN (Mid-P/High-P)** | Deposit shifts toward higher phosphorus content; slower deposition rate; risk of stabilizer imbalance |
| **Trivalent passivation** | More aggressive attack on zinc surface; thinner, less protective film; zinc may be etched |

### pH Too High (More Alkaline Than Target)

| Process | Effect of High pH |
|---|---|
| **Acid zinc** | Organic brightener precipitation; cloudy solution; reduced brightness; zinc hydroxide precipitation above pH 6.5 |
| **Watts nickel** | Precipitation of nickel hydroxide (green sludge); roughness; loss of dissolved metal; anode passivation risk |
| **EN (Mid-P/High-P)** | Deposit shifts toward lower phosphorus content; faster deposition rate; risk of spontaneous bath decomposition |
| **Alkaline zinc** | Higher NaOH improves conductivity but wastes caustic; generally more tolerant of high pH |
| **Trivalent passivation** | Thicker film build (can be intentional up to pH 2.5 for enhanced protection) |

---

## pH Measurement -- Best Practices

### pH Meters

| Practice | Why |
|---|---|
| Calibrate with two buffer solutions (pH 4.0 and 7.0 for acid baths; pH 7.0 and 10.0 for alkaline baths) | Two-point calibration corrects both offset and slope errors |
| Calibrate at operating temperature or apply temperature correction | pH of the buffer solution changes with temperature |
| Store electrode in KCl storage solution (never in DI water) | DI water leaches the reference electrolyte from the probe |
| Replace junction and electrode annually (or when response slows) | Aged electrodes give slow, drifting, or inaccurate readings |
| Rinse electrode with DI water between samples | Prevents cross-contamination between baths |

### Litmus / pH Paper

- Quick field check; useful for rough screening
- Not accurate enough for process control (+/-0.5 pH unit at best)
- Acceptable for alkaline cleaners and rinse waters
- Not acceptable for nickel, EN, or passivation baths (+/-0.2 accuracy required)

---

## pH Adjustment Chemicals

| Chemical | Formula | Used To | Typical Process |
|---|---|---|---|
| **Sodium hydroxide (NaOH)** | NaOH | Raise pH | Acid zinc, nickel, alkaline zinc, cleaners |
| **Potassium hydroxide (KOH)** | KOH | Raise pH | Silver baths (avoids sodium contamination); some alkaline zinc |
| **Nickel carbonate (NiCO3)** | NiCO3 | Raise pH in nickel baths | Watts nickel, sulfamate -- preferred because it adds nickel, not sodium |
| **Ammonium hydroxide (NH4OH)** | NH4OH | Raise pH in EN baths | Electroless nickel -- avoids cation contamination |
| **Sulfuric acid (H2SO4)** | H2SO4 | Lower pH | Watts nickel, EN, acid copper concentration control |
| **Hydrochloric acid (HCl)** | HCl | Lower pH | Acid zinc; also adds chloride (caution in chloride-sensitive baths) |
| **Sulfamic acid** | H3NSO3 | Lower pH in sulfamate nickel | Sulfamate nickel -- avoids introducing chloride or sulfate |

**Safety**: Always add pH adjustment chemicals slowly and with mixing. Concentrated NaOH additions can cause local pH spikes that precipitate metal hydroxides. Concentrated acid additions can cause exothermic reactions and dangerous splashing. Never dump -- always drip.

---

## The Buffer Concept

Many plating baths contain **buffers** -- chemicals that resist pH change when acid or base is added:

| Bath | Buffer Chemical | Buffer Range |
|---|---|---|
| **Watts Nickel** | Boric acid (H3BO3) | pH 3.5--5.0 |
| **Acid Chloride Zinc** | Boric acid (H3BO3) | pH 4.5--6.0 |
| **EN baths** | Succinic acid, lactic acid | pH 4.0--5.5 |
| **Brass plating** | Sodium carbonate / bicarbonate | pH 9.5--10.5 |

**Why buffers matter**: A well-buffered bath maintains stable pH during plating, even as the cathode reaction produces H+ (in acid baths) or consumes OH- (in alkaline baths). A poorly buffered bath swings in pH during operation, causing inconsistent deposit properties.

**Boric acid** is the most common buffer in electroplating. It resists pH change in the 3.5--5.5 range -- exactly where nickel and zinc baths operate. Maintain boric acid at 30--45 g/L in Watts nickel and 15--30 g/L in acid chloride zinc.

---

## The pH Map -- Where Every Process Lives

A conceptual map of the full pH spectrum as it applies to metal finishing:

```
pH 0 |===== HARD CHROME, MATTE TIN =====|
pH 1 |== PASSIVATION (hex/trivalent) ==|
pH 2 |                                  |
pH 3 |                                  |
pH 4 |===== WATTS NICKEL, EN =====|
pH 5 |===== ACID ZINC =====|
pH 6 |                      |
pH 7 |---- NEUTRAL (water) ----|
pH 8 |                          |
pH 9 |                          |
pH10 |                          |
pH11 |===== CLEANERS =====|
pH12 |== CYANIDE COPPER, SILVER ==|
pH13 |===== ALKALINE ZINC =====|
pH14 |                          |
```

The electroplating world operates at two pH extremes -- strongly acidic (pH 0--5) and strongly alkaline (pH 11--14). Almost nothing operates near neutral pH 7.

---

## Visual / Diagram Opportunities for Poster Design

### 1. The pH Scale (HERO visual)

A large, horizontal or vertical pH scale from 0 to 14 with process ranges marked as colored bars at their respective positions:
- Hard chrome at ~0--1 (extreme acid)
- Tin at 0.5--2
- Passivation at 1.5--2.5
- Watts nickel at 3.8--4.5
- EN at 4.4--5.0
- Acid zinc at 4.8--5.8
- Neutral (7)
- Cleaners at 10--12
- Cyanide copper at 11--13
- Alkaline zinc at 12.5--14

### 2. The "What Happens When pH Drifts" Arrow Diagram

For nickel (the best teaching example):
- Center: target pH (4.0)
- Left arrow (too low): pitting, H2 evolution, embrittlement
- Right arrow (too high): hydroxide precipitation, roughness

### 3. The Logarithmic Scale Explanation

A visual showing:
- pH 4 --> 10x more H+ than pH 5
- pH 4 --> 100x more H+ than pH 6
- pH 4 --> 1000x more H+ than pH 7

Caption: "Each pH number = 10x change. Small numbers, big chemistry."

### 4. The pH Meter Calibration Callout

A small box:
- "Calibrate with 2 buffers before every use."
- "Store in KCl, never in water."

### 5. The Adjustment Chemical Quick Reference

Two columns:
- "To raise pH: NaOH, KOH, NiCO3, NH4OH"
- "To lower pH: H2SO4, HCl, sulfamic acid"

### 6. The Buffer Zone Illustration

A conceptual diagram:
- Buffered bath: pH stays flat despite acid additions (stable line)
- Unbuffered bath: pH swings wildly (zigzag line)
- Caption: "Boric acid buffers your bath -- keeping pH stable during plating."

### 7. The EN pH Sensitivity Callout

A special callout for electroless nickel:
- "EN pH must be held within +/-0.2 of target."
- "Check every 30--60 minutes during production."
- "pH drops continuously as plating proceeds."

### 8. The Process Color Code Map

Color-coded by pH zone:
- Deep red: pH 0--2 (chrome, tin, passivation)
- Orange: pH 3--5 (nickel, EN, zinc)
- Blue: pH 10--14 (alkaline zinc, cyanide copper, cleaners)

---

## Key Data Points for Callouts

**The logarithmic fact**:
- "Each pH unit = `10x change` in H+ concentration"

**Tightest pH control**:
- Electroless nickel: `+/-0.2 pH units` -- check every 30--60 minutes
- Watts nickel: `+/-0.3 pH units`

**Widest pH tolerance**:
- Alkaline zinc: `12.5--14.0` -- forgiving
- Acid copper: not pH-controlled (H2SO4 concentration-controlled)

**Most common buffer in plating**:
- `Boric acid (H3BO3)` -- used in nickel and zinc baths

**Preferred pH adjustment for nickel**:
- `NiCO3` (nickel carbonate) -- raises pH without adding sodium

**The safety note**:
- "Always add acid or base slowly, with mixing. Never dump."

**EN pH drift**:
- "pH drops continuously during EN plating -- H+ is a reaction byproduct"

**The two-extremes rule**:
- Plating baths operate at pH 0--5 (acid) or pH 11--14 (alkaline). Almost nothing runs near neutral.

---

## Poster-Worthy Sticky Facts

1. **"Each pH unit = 10x change"** -- the pH scale is logarithmic. A bath at pH 4.0 has 10x more hydrogen ions than a bath at pH 5.0, and 100x more than pH 6.0. A "small" pH drift of 0.5 units represents a 3x change in hydrogen ion concentration. This is why tight pH control matters -- the chemistry changes faster than the number suggests.

2. **"EN: check every 30 minutes"** -- electroless nickel is the most pH-sensitive process in common use. The target window is +/-0.2 pH units, and pH drops continuously during plating because hydrogen ions are a byproduct of the reduction reaction. Miss a pH check and the deposit composition shifts, the plating rate changes, or the bath decomposes spontaneously.

3. **"NiCO3, not NaOH"** -- the preferred pH raise agent for nickel baths is nickel carbonate, not sodium hydroxide. NiCO3 raises pH and adds nickel simultaneously -- a double benefit. NaOH raises pH but adds sodium, which accumulates over time and degrades deposit properties. The right chemical for the job matters as much as the pH number.

4. **"Boric acid: the silent hero"** -- boric acid (H3BO3) is the most common buffer in electroplating, maintaining stable pH in the 3.5--5.5 range where nickel and zinc baths operate. Without adequate boric acid, pH swings during plating produce inconsistent deposits. Maintain 30--45 g/L in Watts nickel. It is the cheapest stability insurance in the bath.

5. **"Plating lives at the extremes"** -- hard chrome and matte tin operate below pH 1. Alkaline zinc operates above pH 13. The electroplating world occupies the far ends of the pH spectrum -- almost nothing runs near neutral pH 7. This is why pH meters in plating labs need frequent calibration and rugged construction.

6. **"pH 6.5 = zinc hydroxide rain"** -- in acid chloride zinc baths, allowing pH to rise above 6.5 precipitates zinc hydroxide as a white, cloudy suspension. The bath goes turbid, brighteners co-precipitate, and deposit quality collapses. This is the single most common pH failure in acid zinc plating. Keep pH below 5.8.

7. **"Acid copper does not care about pH"** -- acid copper sulfate is the one major plating process that is not pH-controlled. The operating acidity is set by sulfuric acid concentration (typically 7--11% v/v), not by pH measurement. Operators who try to pH-adjust an acid copper bath are solving the wrong problem.

8. **"Store your probe in KCl, never in water"** -- DI water leaches the potassium chloride reference electrolyte from inside the pH electrode, destroying calibration accuracy. A $200 pH probe stored in DI water for a week becomes unreliable. Always use manufacturer-supplied KCl storage solution. This single habit extends probe life from months to years.

---

*Research Brief v2 authored by Watson (`watson-chemistry-researcher`), 2026-04-11. Sources: Nickel Institute Nickel Plating Handbook 2023 (vault -- Watts nickel pH 3.8--4.5 confirmed); 1993 Metal Finishing Guidebook and Directory (vault); Drew's Quick Reference Metal Finishing Notes (vault); domain expertise. pH ranges are industry-typical and may vary by specific product formulation -- verify against product TDS for production use.*
