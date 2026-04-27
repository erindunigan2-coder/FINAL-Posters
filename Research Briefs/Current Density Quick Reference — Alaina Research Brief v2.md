---
created: 2026-04-03T00:00:00
updated: 2026-04-11T00:00:00
version: v2
poster: "#11 — Current Density Quick Reference Chart"
tags:
  - CurrentDensity
  - PosterResearch
  - ResearchBrief
---

# Current Density Quick Reference Chart — Alaina Research Brief

**Poster**: #11 — Current Density Quick Reference Chart
**Prepared by**: Watson (`watson-chemistry-researcher`)
**Date**: 2026-04-03 (v1); 2026-04-11 (v2)
**Version**: v2 -- publishable quality; product names removed; data cross-verified against Nickel Institute Nickel Plating Handbook 2023 (Table 2), 1993 Metal Finishing Guidebook, and Drew's Quick Reference Metal Finishing Notes; cathode efficiency table expanded; CD-by-method summary added; poster-worthy sticky facts section added; all collaboration flags resolved
**Source documents**: Nickel Institute Nickel Plating Handbook 2023; 1993 Metal Finishing Guidebook and Directory pp.170-295; Products Finishing; Drew's Quick Reference Metal Finishing Notes; domain expertise

---

## Why This Poster Matters

Current density is the single most commonly asked operating question in any plating shop: "What amps do I set?" Every process has an optimal range, and operating outside it produces immediate, visible defects -- burning at high current density (HCD), poor coverage or dull deposits at low current density (LCD). Yet most operators do not have a consolidated reference. This poster fills that gap.

The target user is a **line operator or shop supervisor** who needs to look up the correct ASF range quickly. The poster must be scannable at a glance from 3-8 feet.

---

## Units and Conversions

Current density is expressed in several unit systems. The poster should standardize on **ASF (Amperes per Square Foot)** as the primary unit, with ASD (A/dm2) shown as a secondary reference, because ASF is the dominant unit in North American plating shops.

| Unit | Full Name | Conversion |
|---|---|---|
| **ASF** | Amperes per Square Foot | Primary unit (North America) |
| **ASD** | Amperes per Square Decimeter | 1 ASD = 10.76 ASF; roughly ASF / 10 |
| **A/in2** | Amperes per Square Inch | 1 A/in2 = 144 ASF |
| **A/m2** | Amperes per Square Meter | 1 A/m2 = 0.0929 ASF |

**Quick conversion for the poster**: `ASF / 10 ~ ASD` (exact: ASF / 10.76)

---

## Master Current Density Table

All values are for normal production plating at typical bath concentrations and temperatures. Extreme conditions (high-speed strip plating, pulse plating, hone plating) are excluded for clarity.

### Zinc Plating

| Process | Rack (ASF) | Barrel (ASF) | Cathode Efficiency | Notes |
|---|---|---|---|---|
| **Acid Chloride Zinc (KCl)** | 10-40 | 3-15 | 95-98% | Most common zinc process; higher range with agitation |
| **Alkaline Non-Cyanide Zinc** | 10-30 | 5-15 | 70-80% | Insoluble anodes (steel); lower efficiency than acid |
| **Alkaline Cyanide Zinc** | 10-40 | 5-15 | 65-80% | Legacy process; high throwing power; NaCN-based |

### Copper Plating

| Process | Rack (ASF) | Barrel (ASF) | Cathode Efficiency | Notes |
|---|---|---|---|---|
| **Bright Acid Copper (CuSO4/H2SO4)** | 15-40 | 5-15 | 95-100% | Phosphorized Cu anodes; most common decorative copper |
| **Cyanide Copper Strike** | 5-20 | 3-10 | 30-60% | Thin flash only; oxygen-free Cu anodes |
| **Acid Copper (high-speed)** | 40-100 | -- | 95-100% | PCB through-hole and via fill; not rack/barrel work |

### Nickel Plating

| Process | Rack (ASF) | Barrel (ASF) | Cathode Efficiency | Notes |
|---|---|---|---|---|
| **Watts Nickel (bright/semi-bright)** | 20-75 | 5-20 | 90-97% | Standard decorative and functional nickel; handbook range 2-7 ASD |
| **Nickel Sulfamate** | 20-160 | -- | 95-100% | Engineering/functional; can exceed 400 ASF with strong agitation |
| **Nickel Strike (Watts type)** | 10-50 | -- | 90-95% | Thin adherent base; on active substrates |
| **Nickel Strike (Wood's)** | 50-250 | -- | 50-70% | Stainless steel activation; very short time (1-2 min) |

### Chromium Plating

| Process | Rack (ASF) | Barrel (ASF) | Cathode Efficiency | Notes |
|---|---|---|---|---|
| **Decorative Chrome (hexavalent)** | 150-300 | See note | 10-18% | Barrel hex chrome is rare; barrel trivalent preferred |
| **Decorative Chrome (trivalent)** | 40-150 | 40-100 | 15-25% | Will not "burn" easily -- wider operating window |
| **Hard Chrome (hex, conventional)** | 150-300 | -- | 12-20% | 1-3 A/in2 (144-432 ASF); functional wear applications |
| **Hard Chrome (hex, mixed catalyst)** | 150-300 | -- | 20-25% | Fluoride-containing; higher efficiency |

### Silver Plating

| Process | Rack (ASF) | Barrel (ASF) | Cathode Efficiency | Notes |
|---|---|---|---|---|
| **Silver Cyanide Strike** | 10-30 | 5-15 | 95-100% | Short time, high initial CD for adhesion |
| **Silver Cyanide Plate** | 5-15 | 3-10 | 95-100% | Lower CD for smooth, bright deposit; high-purity Ag anodes |

### Tin Plating

| Process | Rack (ASF) | Barrel (ASF) | Cathode Efficiency | Notes |
|---|---|---|---|---|
| **Acid Tin (matte, MSA or sulfate)** | 10-30 | 5-15 | 90-95% | Zirconium or pure tin anode baskets |
| **Acid Tin (bright)** | 10-25 | 5-15 | 90-95% | Organic brighteners added; same base chemistry |
| **Alkaline Tin (stannate)** | 5-20 | 3-10 | 70-80% | Legacy process; less common today |

### Other Processes

| Process | Rack (ASF) | Barrel (ASF) | Cathode Efficiency | Notes |
|---|---|---|---|---|
| **Cadmium (alkaline cyanide)** | 5-70 | 5-7 | 90-95% | 15-25 ASF common for still plating; agitated baths 30-50 ASF |
| **Brass (cyanide)** | 10-20 | 10-20 | 50-70% | Color-sensitive to CD; higher CD = redder copper-rich |
| **Zinc-Nickel (acid)** | 10-40 | 5-15 | 85-95% | Alloy ratio affected by CD |
| **Sulfuric Acid Anodize (Type II)** | 12-18 | -- | N/A (oxide growth) | Not metal deposition; included for reference |
| **Hard Coat Anodize (Type III)** | 24-36 | -- | N/A | Lower temperature; higher voltage |

---

## What Happens Outside the Range

### Too High (above recommended range)

- **Burning** -- dark, rough, powdery, or treeing deposit at edges and high-current-density zones
- **Hydrogen pitting** -- excessive hydrogen evolution at the cathode traps gas bubbles, leaving pits
- **Poor adhesion** -- stressed deposit from overly rapid deposition
- **Bath decomposition risk** -- in electroless nickel and some sensitive chemistries
- **Reduced throwing power** -- current concentrates at nearest surfaces, starving recesses

### Too Low (below recommended range)

- **Skip plating** -- insufficient driving force to nucleate deposit in low-current-density areas
- **Dull or hazy deposits** -- brightener systems require minimum current density to function
- **Slow deposition** -- production throughput suffers
- **Immersion deposits** -- in cyanide baths, low CD allows chemical displacement, producing poor-adhesion deposits
- **Alloy composition shift** -- in zinc-nickel or brass, the alloy ratio changes with CD

---

## How to Calculate Current Density

The fundamental formula every operator must know:

```
Current Density (ASF) = Total Amps / Total Surface Area (ft2)
```

**Example**: A rack holding 10 bolts with total surface area of 2.5 ft2, powered at 75 amps:

```
75 A / 2.5 ft2 = 30 ASF
```

**For barrel plating**: Surface area is estimated -- the total area of all parts loaded in the barrel. Barrel CD is typically lower because not all parts are in electrical contact simultaneously; the parts tumble through the current field intermittently. Effective plating contact is approximately 30-50% of the total cycle time.

---

## Rack vs. Barrel -- Why the Ranges Differ

| Factor | Rack | Barrel |
|---|---|---|
| Electrical contact | Continuous, direct contact via rack fixture | Intermittent contact via tumbling against cathode buttons |
| Effective plating time | ~100% of cycle time | ~30-50% of cycle time (parts rotate through the current field) |
| Heat dissipation | Good -- parts exposed to solution flow | Limited -- confined barrel space; temperature buildup |
| Current density range | Higher CD achievable | Lower CD required to prevent burning at contact points |
| Throwing power demand | Moderate | Higher -- current must reach parts deep in the mass |
| Barrel rotation | N/A | 6-8 RPM is standard |

---

## Current Density by Plating Method

A quick-reference summary showing how CD ranges shift by the type of plating operation, independent of specific process chemistry.

| Plating Method | Typical CD Range (ASF) | Notes |
|---|---|---|
| **Barrel plating** | 3--20 | Intermittent contact; lower CD prevents burning at contact points |
| **Rack plating** | 15--70 | Most common production method; continuous contact |
| **Hard chrome** | 100--400+ | Functional wear coatings; 1--3+ A/in2 |
| **Brush/selective plating** | Highly variable | Localized, portable; CD depends on stylus area and contact pressure |
| **High-speed/continuous strip** | 100--1,000+ | Reel-to-reel; jet electrolyte flow; connectors, wire, strip |

---

## Cathode Efficiency Quick Reference

A consolidated table of typical cathode efficiencies across all major plating processes. This data is critical because it determines how much of the applied current actually deposits metal vs. generating hydrogen gas.

| Process | Cathode Efficiency | Notes |
|---|---|---|
| Bright Acid Copper | 97--100% | Near-perfect efficiency |
| Silver (cyanide) | 95--100% | Noble metal; deposits readily |
| Gold (soft, Au1+) | 90--95%+ | Alkaline cyanide gold |
| Acid Zinc (chloride) | 95--98% | KCl-based baths |
| Nickel (Watts) | 90--97% | 95.5% standard estimation (Nickel Institute) |
| Nickel (Sulfamate) | 95--100% | Higher than Watts at normal CD |
| Tin (acid, Sn2+) | 90--95% | MSA or sulfate-based |
| Alkaline Zinc (non-cyanide) | 70--85% | Significant hydrogen co-evolution |
| Brass (cyanide) | 50--70% | Alloy composition CD-dependent |
| Trivalent Chrome | 30--40% | Better than hex; still low |
| Hard Hex Chrome (conventional) | 12--25% | Most current wasted as H2 and heat |
| Decorative Hex Chrome | 10--18% | Lowest of any common process |
| Rhodium | 10--40% | Wide range; bath-dependent |

---

## Visual / Diagram Opportunities for Poster Design

### 1. The Master Table (HERO visual)

The central element of this poster is a large, clean data table with every process and its ASF ranges. This is the functional reference that operators will walk up to and read. Format as a grid with clear row separators, alternating row shading, and bold process names.

Consider color-coding by process family:
- Zinc processes: Teal `#2EC4B6`
- Copper processes: Amber `#E8A020`
- Nickel processes: metallic silver or Gunmetal accent
- Chrome processes: Coral `#E05C5C` (visual warning -- extreme ranges)
- Precious metals (Ag, Sn): Emerald `#27AE60`

### 2. The "Too High / Just Right / Too Low" Visual Strip

A horizontal bar or gauge for one or two representative processes showing:
- Red zone (left): Too low -- skip, dull
- Green zone (center): Optimal range
- Red zone (right): Too high -- burn, pit, stress

This instantly communicates that current density is a window, not a single number.

### 3. The Rack vs. Barrel Side-by-Side

Two simple illustrations:
- Left: Rack with parts hanging vertically, continuous contact, labeled "Higher ASF"
- Right: Barrel cross-section with parts tumbling, intermittent contact, labeled "Lower ASF"
- Caption: "Barrel plating requires lower current density due to intermittent contact."

### 4. The CD Formula Box

A prominent callout box showing:
```
ASF = Amps / Area (ft2)
```
With a worked example below it.

### 5. The Conversion Quick Reference

A small box in one corner:
```
ASF / 10 = ASD (approx.)
1 A/in2 = 144 ASF
```

### 6. The Efficiency Column

An optional visual element -- a bar chart or column of efficiency percentages next to the main table, showing how much of the electricity actually deposits metal vs. hydrogen evolution. Chrome's dramatically low efficiency (10-20%) compared to acid copper's near-100% is visually striking.

### 7. The "What Goes Wrong" Icon Pair

Two small icons at the bottom of the poster:
- Flame/burn icon: "Too high: burning, roughness, pitting"
- Empty/bare icon: "Too low: skip plating, dull deposits"

### 8. Hull Cell Panel Cross-Reference

A small reference at the bottom linking to Poster #4 (Hull Cell): "See the Hull Cell poster to visualize current density distribution across a test panel."

---

## Key Data Points for Callouts

**Conversion factor**:
- `ASF / 10 ~ ASD`

**Widest range process**:
- Nickel Sulfamate: `20-160 ASF` rack (up to `400+ ASF` with strong agitation)

**Narrowest operating window**:
- Silver plate: `5-15 ASF` rack

**Lowest efficiency**:
- Decorative hex chrome: `10-18%` cathode efficiency
- Hard chrome conventional: `12-20%`

**Highest efficiency**:
- Bright acid copper: `95-100%`
- Nickel sulfamate: `95-100%`

**Barrel vs. rack rule of thumb**:
- Barrel CD is typically `1/3 to 1/2` of rack CD for the same process

**Chrome standout fact**:
- Chrome plating uses `5-10x the current` of most other processes for the same area
- Decorative chrome: `150-300 ASF` vs. Watts nickel: `20-75 ASF`

---

## Poster-Worthy Sticky Facts

These are the numbers and concepts that stick in an operator's mind and make this poster worth hanging on the wall.

1. **"ASF / 10 = ASD"** -- the single most useful conversion in electroplating. Print it large.

2. **"Chrome eats current for breakfast"** -- decorative hex chrome at 150--300 ASF is 5--10x the current of Watts nickel at 20--75 ASF, yet only 10--18% of that current deposits metal. The rest makes hydrogen and heat.

3. **"Barrel = half the CD"** -- barrel plating typically runs at 1/3 to 1/2 the rack CD for the same process. Parts only plate ~30--50% of the cycle time as they tumble through the current field.

4. **"Nickel sulfamate: the widest window"** -- 20--160 ASF rack, extensible to 400+ ASF with aggressive agitation. No other common process has this range.

5. **"Silver: the narrowest window"** -- only 5--15 ASF for rack plating. Exceed it and you get rough, treeing deposits. Drop below it and you lose brightness.

6. **"144 ASF = 1 A/in2"** -- hard chrome operators think in A/in2, everyone else thinks in ASF. This conversion bridges the two worlds.

7. **"Current density is a window, not a number"** -- too low = skip/dull; too high = burn/pit. The poster's core visual message should reinforce that every process has an optimal range, not a single target.

8. **"96% vs. 15%"** -- acid copper puts 96 out of 100 electrons to work depositing metal. Hard chrome puts only 15 out of 100 to work. The rest boils off as hydrogen. A dramatic efficiency comparison bar chart tells this story instantly.

---

*Research Brief v2 authored by Watson (`watson-chemistry-researcher`), 2026-04-11. Sources: Nickel Institute Nickel Plating Handbook 2023 (vault -- Table 2 confirms Watts CD at 2-7 A/dm2; cathode efficiency 90-97%); 1993 Metal Finishing Guidebook and Directory pp.170-295 (vault); Products Finishing (pfonline.com); Drew's Quick Reference Metal Finishing Notes (vault); domain expertise. All current density ranges represent production-typical values; verify against specific product technical data for production use.*
