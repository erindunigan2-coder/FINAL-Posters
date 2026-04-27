---
created: 2026-04-03T00:00:00
version: v1
poster: "#11 — Current Density Quick Reference Chart"
tags:
  - CurrentDensity
  - PosterResearch
  - ResearchBrief
---

# Current Density Quick Reference Chart — Alaina Research Brief

**Poster**: #11 — Current Density Quick Reference Chart
**Prepared by**: Watson (`watson-chemistry-researcher`)
**Date**: 2026-04-03
**Version**: v1
**Source documents**: 1993 Metal Finishing Guidebook and Directory (vault — pp.170–295); Products Finishing; Columbia Chemical (Nicol Sulfamate TDS); Nickel Institute Nickel Plating Handbook 2023; Drew's Quick Reference Metal Finishing Notes (vault); domain expertise

> [!NOTE]
> This brief provides the comprehensive current density reference data for Poster #11. The poster's value proposition is simple: a single wall chart that tells an operator "what ASF do I run?" for every major process in the shop. Design decisions remain Alaina's domain.

---

## Why This Poster Matters

Current density is the single most commonly asked operating question in any plating shop: "What amps do I set?" Every process has an optimal range, and operating outside it produces immediate, visible defects — burning at high current density (HCD), poor coverage or dull deposits at low current density (LCD). Yet most operators do not have a consolidated reference. This poster fills that gap.

The target user is a **line operator or shop supervisor** who needs to look up the correct ASF range quickly. The poster must be scannable at a glance from 3–8 feet.

---

## Units and Conversions

Current density is expressed in several unit systems. The poster should standardize on **ASF (Amperes per Square Foot)** as the primary unit, with ASD (A/dm²) shown as a secondary reference, because ASF is the dominant unit in North American plating shops.

| Unit | Full Name | Conversion |
|---|---|---|
| **ASF** | Amperes per Square Foot | Primary unit (North America) |
| **ASD** | Amperes per Square Decimeter | 1 ASD = 10.76 ASF; roughly ASF / 10 |
| **A/in²** | Amperes per Square Inch | 1 A/in² = 144 ASF |
| **A/m²** | Amperes per Square Meter | 1 A/m² = 0.0929 ASF |

**Quick conversion for the poster**: `ASF / 10 ~ ASD` (exact: ASF / 10.76)

---

## Master Current Density Table

This is the core content of the poster. All values are for normal production plating at typical bath concentrations and temperatures. Extreme conditions (high-speed strip plating, pulse plating, hone plating) are excluded for clarity.

### Zinc Plating

| Process | Rack (ASF) | Barrel (ASF) | Cathode Efficiency | Notes |
|---|---|---|---|---|
| **Acid Chloride Zinc (KCl)** | 10–40 | 3–15 | 95–98% | Most common zinc process; higher range with agitation |
| **Alkaline Non-Cyanide Zinc** | 10–30 | 5–15 | 70–80% | Insoluble anodes (steel); lower efficiency than acid |
| **Alkaline Cyanide Zinc** | 10–40 | 5–15 | 65–80% | Legacy process; high throwing power; NaCN-based |

### Copper Plating

| Process | Rack (ASF) | Barrel (ASF) | Cathode Efficiency | Notes |
|---|---|---|---|---|
| **Bright Acid Copper (CuSO₄/H₂SO₄)** | 15–40 | 5–15 | 95–100% | A Brite: Brite-Copper AC 12-E; phosphorized Cu anodes |
| **Cyanide Copper Strike** | 5–20 | 3–10 | 30–60% | A Brite: Brite-Copper CN-707; thin flash only; O₂-free Cu anodes |
| **Acid Copper (high-speed)** | 40–100 | — | 95–100% | PCB through-hole and via fill; not rack/barrel work |

### Nickel Plating

| Process | Rack (ASF) | Barrel (ASF) | Cathode Efficiency | Notes |
|---|---|---|---|---|
| **Watts Nickel (bright/semi-bright)** | 20–60 | 5–20 | 93–97% | Standard decorative and functional nickel |
| **Nickel Sulfamate** | 20–140 | — | 95–100% | Engineering/functional; can go much higher with agitation (up to 400+ ASF) |
| **Nickel Strike (Watts type)** | 10–50 | — | 90–95% | Thin adherent base; on active substrates |
| **Nickel Strike (Wood's)** | 50–250 | — | Low (50–70%) | Stainless steel activation; very short time |

### Chromium Plating

| Process | Rack (ASF) | Barrel (ASF) | Cathode Efficiency | Notes |
|---|---|---|---|---|
| **Decorative Chrome (hex)** | 150–300 | See note | 10–18% | Barrel hex chrome limited; barrel trivalent preferred |
| **Decorative Chrome (trivalent)** | 40–150 | 40–100 | 15–25% | Will not "burn" — wider operating window |
| **Hard Chrome (hex, conventional)** | 150–300 | — | 12–20% | 1–3 A/in² (144–432 ASF); functional use |
| **Hard Chrome (hex, mixed catalyst)** | 150–300 | — | 20–25% | Fluoride-containing; higher efficiency |

### Silver Plating

| Process | Rack (ASF) | Barrel (ASF) | Cathode Efficiency | Notes |
|---|---|---|---|---|
| **Silver Cyanide Strike** | 10–30 | 5–15 | 95–100% | A Brite: Brite-Silver AG-1; short time, high initial CD |
| **Silver Cyanide Plate** | 5–15 | 3–10 | 95–100% | Lower CD for smooth, bright deposit; >99.9% Ag anodes |

### Tin Plating

| Process | Rack (ASF) | Barrel (ASF) | Cathode Efficiency | Notes |
|---|---|---|---|---|
| **Acid Tin (matte, MSA or sulfate)** | 10–30 | 5–15 | 90–95% | A Brite: Brite-Tin SN-M; zirconium anode baskets |
| **Acid Tin (bright)** | 10–25 | 5–15 | 90–95% | Organic brighteners added; same base chemistry |
| **Alkaline Tin (stannate)** | 5–20 | 3–10 | 70–80% | Legacy process; less common today |

### Other Processes

| Process | Rack (ASF) | Barrel (ASF) | Cathode Efficiency | Notes |
|---|---|---|---|---|
| **Cadmium (alkaline cyanide)** | 5–70 | 5–7 | 90–95% | 15–25 ASF common for still plating; agitated baths 30–50 ASF |
| **Brass (cyanide)** | 10–20 | 10–20 | 50–70% | Color-sensitive to CD; higher CD = redder copper-rich |
| **Zinc-Nickel (acid)** | 10–40 | 5–15 | 85–95% | Alloy ratio affected by CD |
| **Sulfuric Acid Anodize (Type II)** | 12–18 | — | N/A (oxide growth) | Not a metal deposition process; included for reference |
| **Hard Coat Anodize (Type III)** | 24–36 | — | N/A | Lower temperature; higher voltage |

---

## What Happens Outside the Range

This section provides the "why it matters" content — the consequences of wrong current density.

### Too High (above recommended range)

- **Burning** — dark, rough, powdery, or treeing deposit at edges and high-current-density zones
- **Hydrogen pitting** — excessive hydrogen evolution at the cathode traps gas bubbles, leaving pits
- **Poor adhesion** — stressed deposit from overly rapid deposition
- **Bath decomposition risk** — in EN and some sensitive chemistries
- **Reduced throwing power** — current concentrates at nearest surfaces, starving recesses

### Too Low (below recommended range)

- **Skip plating** — insufficient driving force to nucleate deposit in low-current-density areas
- **Dull or hazy deposits** — brightener systems require minimum current density to function
- **Slow deposition** — production throughput suffers
- **Immersion deposits** — in cyanide baths, low CD allows chemical (non-electrochemical) displacement, producing poor-adhesion deposits
- **Alloy composition shift** — in zinc-nickel or brass, the alloy ratio changes with CD

---

## How to Calculate Current Density

This is the fundamental formula every operator must know:

```
Current Density (ASF) = Total Amps / Total Surface Area (ft²)
```

**Example**: A rack holding 10 bolts with total surface area of 2.5 ft², powered at 75 amps:

```
75 A / 2.5 ft² = 30 ASF
```

**For barrel plating**: Surface area is estimated — the total area of all parts loaded in the barrel. Barrel CD is typically lower because not all parts are in electrical contact simultaneously, and the parts tumble through the current field intermittently.

---

## Rack vs. Barrel — Why the Ranges Differ

| Factor | Rack | Barrel |
|---|---|---|
| Electrical contact | Continuous, direct contact via rack fixture | Intermittent contact via tumbling against cathode buttons |
| Effective plating time | ~100% of cycle time | ~30–50% of cycle time (parts rotate through the current field) |
| Heat dissipation | Good — parts exposed to solution flow | Limited — confined barrel space; temperature buildup |
| Current density range | Higher CD achievable | Lower CD required to prevent burning at contact points |
| Throwing power demand | Moderate | Higher — current must reach parts deep in the mass |

---

## Visual / Diagram Opportunities for Poster Design

### 1. The Master Table (HERO visual)

The central element of this poster is a large, clean data table with every process and its ASF ranges. This is the functional reference that operators will walk up to and read. Format as a grid with clear row separators, alternating row shading, and bold process names.

Consider color-coding by process family:
- Zinc processes: Teal `#2EC4B6`
- Copper processes: Amber `#E8A020`
- Nickel processes: metallic silver or Gunmetal accent
- Chrome processes: Coral `#E05C5C` (visual warning — extreme ranges)
- Precious metals (Ag, Sn): Emerald `#27AE60`

### 2. The "Too High / Just Right / Too Low" Visual Strip

A horizontal bar or gauge for one or two representative processes showing:
- Red zone (left): Too low — skip, dull
- Green zone (center): Optimal range
- Red zone (right): Too high — burn, pit, stress

This instantly communicates that current density is a window, not a single number.

### 3. The Rack vs. Barrel Side-by-Side

Two simple illustrations:
- Left: Rack with parts hanging vertically, continuous contact, labeled "Higher ASF"
- Right: Barrel cross-section with parts tumbling, intermittent contact, labeled "Lower ASF"
- Caption: "Barrel plating requires lower current density due to intermittent contact."

### 4. The CD Formula Box

A prominent callout box showing:
```
ASF = Amps / Area (ft²)
```
With a worked example below it.

### 5. The Conversion Quick Reference

A small box in one corner:
```
ASF / 10 = ASD (approx.)
1 A/in² = 144 ASF
```

### 6. The Efficiency Column

An optional visual element — a bar chart or column of efficiency percentages next to the main table, showing how much of the electricity actually deposits metal vs. hydrogen evolution. Chrome's dramatically low efficiency (10–20%) compared to acid copper's near-100% is visually striking.

### 7. The "What Goes Wrong" Icon Pair

Two small icons at the bottom of the poster:
- Flame/burn icon → "Too high: burning, roughness, pitting"
- Empty/bare icon → "Too low: skip plating, dull deposits"

### 8. Hull Cell Panel Reference Strip

A small reference at the bottom linking to Poster #4: "See Poster #4 — Reading Your Hull Cell Panel — to visualize current density distribution across a test panel."

---

## Key Data Points for Callouts

**Conversion factor**:
- `ASF / 10 ~ ASD`

**Widest range process**:
- Nickel Sulfamate: `20–140 ASF` rack (up to `400+ ASF` with agitation)

**Narrowest operating window**:
- Silver plate: `5–15 ASF` rack

**Lowest efficiency**:
- Decorative hex chrome: `10–18%` cathode efficiency
- Hard chrome conventional: `12–20%`

**Highest efficiency**:
- Bright acid copper: `95–100%`
- Nickel sulfamate: `95–100%`

**Barrel vs. rack rule of thumb**:
- Barrel CD is typically `1/3 to 1/2` of rack CD for the same process

**Chrome standout fact**:
- Chrome plating uses `5–10x the current` of most other processes for the same area
- Decorative chrome: `150–300 ASF` vs. Watts nickel: `20–60 ASF`

---

## Collaboration Flags

- **Drew**: Please confirm the following current density ranges match your field experience and A Brite product recommendations:
  - Acid chloride zinc KCl: 10–40 ASF rack / 3–15 ASF barrel
  - Alkaline non-cyanide zinc: 10–30 ASF rack / 5–15 ASF barrel
  - Bright acid copper (AC 12-E): 15–40 ASF rack
  - Cyanide copper strike (CN-707): 5–20 ASF rack
  - Nickel sulfamate: 20–140 ASF rack
  - Decorative chrome hex: 150–300 ASF
  - Hard chrome: 150–300 ASF (1–3 A/in²)
  - Silver cyanide (AG-1): 5–15 ASF rack plate / 10–30 ASF strike
  - Matte tin (SN-M): 10–30 ASF rack
- **Drew**: The Quick Reference notes say zinc rack = 15–20 ASF and barrel = 5–10 ASF. The ranges I've provided are wider to cover the full commercial range seen across vendors — confirm whether Drew prefers to narrow these to A Brite-specific recommendations.
- **Tyler**: No direct validation needed. If any A Brite product TDS specifies a current density range that conflicts with the values above, flag it.

---

*Research Brief v1 authored by Watson (`watson-chemistry-researcher`), 2026-04-03. Sources: 1993 Metal Finishing Guidebook and Directory pp.170–295 (vault); Products Finishing (pfonline.com); Columbia Chemical Nicol Sulfamate TDS; Nickel Institute Nickel Plating Handbook 2023 (vault); Drew's Quick Reference Metal Finishing Notes (vault); domain expertise. Alaina should flag any data points requiring additional verification before final poster production.*
