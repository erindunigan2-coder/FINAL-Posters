---
Project: Plating Posters Inc
Poster Number: 330
Title: "Etch -- Integral Color Anodizing"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 7, Section 7.4)"
Technical Source: Industry-standard caustic etch (NaOH) for aluminum prior to integral color anodizing. Etch uniformity is the single most critical factor for color consistency. Parameters are typical ranges.
Process Scope: Integral color anodizing -- Stage 3 of 8 (Etch)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Anodizing
  - IntegralColor
  - Etch
  - ConstructionWorkup
  - AnodizingCluster
---

# Poster #330 -- Construction Workup
## Etch -- Integral Color Anodizing

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 3 of 8. Standard caustic etch -- but uniformity is CRITICAL for integral color. Inconsistent etching produces color variation across the part and from part to part. Different alloy heats of 6063 can produce different integral colors even with identical processing -- this is the biggest quality challenge.

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
  Stage 3 highlighted (Amber)
ZONE 3 -- ETCH PROCESS HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- ALLOY ETCH BEHAVIOR + REACTION (14.5"--20.5" / ~6.0")
ZONE 5 -- DEFECT DIAGNOSIS GRID (20.5"--26.5" / ~6.0")
ZONE 6 -- ETCH CONTROL FOR COLOR + SAFETY (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CAUSTIC ETCH` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Integral Color Anodizing -- Stage 3 of 8` -- 34 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Etch uniformity IS color uniformity. In integral color, the etch step determines whether you get consistent bronze or a patchwork of shades.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 3 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean, oil-free aluminum surface --> After: Uniform matte finish, mill variation removed`

---

### ZONE 3 -- Etch Process Hero

**Section label:** `CAUSTIC ETCH -- OPERATING PARAMETERS` -- Y: 4.4".

**BLOCK B -- Parameter Panel + Etch Reaction**

Y: 5.0" to 14.0". Large rounded rect, fill `#1E2435`.

**Left column (X: 1.0", W: 11.0") -- Parameter Table:**

| Parameter | Value |
|---|---|
| Chemistry | Sodium hydroxide (NaOH) -- caustic etch |
| Concentration | 40--80 g/L (5.3--10.7 oz/gal); typical 50--60 g/L |
| Temperature | 130--150 F (55--65 C) |
| Time | 1--5 minutes (alloy-dependent) |
| Dissolved aluminum | Monitor; > 50 g/L = sluggish; partial dump |
| Etch rate | ~0.5--1.0 mil/min (12--25 um/min) on 6061 at 60 C |
| Agitation | Mild air |

Parameter labels: Inter Medium, 14 pt, `#F0EDE8` at 60%. Values: JetBrains Mono Regular, 15 pt, `#F0EDE8`.

**Right column (X: 12.5", W: 10.5") -- Etch Reaction:**

Rounded rect, fill `#252B3D`, border 1 pt `#E8A020`.

Title: `THE ETCH REACTION` Barlow SemiBold 18 pt `#E8A020`.

Chemical equation (JetBrains Mono 16 pt `#F0EDE8`, centered):
```
2Al + 2NaOH + 2H2O --> 2NaAlO2 + 3H2 (gas)
```

Annotations below (Inter Regular 13 pt):
- `Aluminum dissolves in caustic solution` `#F0EDE8`
- `Hydrogen gas evolution is vigorous` `#E05C5C`
- `Sodium aluminate is the byproduct -- builds up over time` `#F0EDE8` at 70%
- `VENTILATION REQUIRED -- H2 is flammable` `#E05C5C`

**Key Rules Stack (below reaction, Y: 10.0"):**

*Rule 1 (Coral):*
- `ETCH UNIFORMITY IS NON-NEGOTIABLE` Barlow SemiBold 16 pt `#E05C5C`
- `For integral color: etch time must be controlled to +/- 15 seconds. Temperature to +/- 1 C. This is tighter than standard Type II.` Inter Regular 13 pt `#F0EDE8`

*Rule 2 (Amber):*
- `ALLOY LOT CONTROL` Barlow SemiBold 16 pt `#E8A020`
- `Different heats/lots of 6063 extrusions produce different integral colors even with identical etch and anodize conditions. Match lots.` Inter Regular 13 pt `#F0EDE8`

**Bottom callout (Y: 13.5"):**
- `The etch step is where integral color quality is won or lost. Tighter controls here than any other anodizing process.` Inter Medium 14 pt `#E8A020`

---

### ZONE 4 -- Alloy Etch Behavior + Control

**Section label:** `ALLOY-SPECIFIC ETCH BEHAVIOR` -- Y: 14.7".

**Left (X: 0.5", W: 14.0") -- Alloy Table:**

| Alloy | Etch Time | Etch Notes |
|---|---|---|
| 6061 | 2--3 min | Standard etch; uniform matte finish |
| 6063 | 2--3 min | Architectural standard; best for integral color |
| 5005 | 2--3 min | Good color match with 6063 |
| 2024 | 1--2 min | Heavy dark smut (copper); aggressive desmut required |
| 7075 | 1--2 min | Zinc and copper smut; shorter time recommended |
| Cast (high Si) | NOT RECOMMENDED | Silicon not dissolved by NaOH; rough, gritty |

JetBrains Mono 13 pt for times. Inter Regular 13 pt for notes. "NOT RECOMMENDED" in `#E05C5C`.

**Right (X: 15.0", W: 8.5") -- Dissolved Aluminum Gauge:**

Rounded rect, fill `#1E2435`, left accent `#E8A020`.
Title: `DISSOLVED ALUMINUM` Barlow SemiBold 16 pt `#E8A020`.

Vertical gauge (bar):
- Green zone: `< 30 g/L -- Optimal` `#27AE60`
- Yellow zone: `30--50 g/L -- Monitor` `#E8A020`
- Red zone: `> 50 g/L -- Sluggish; dump/decant` `#E05C5C`

Note: `High dissolved Al slows etch rate and changes surface texture, producing color variation in the integral color step.` Inter Regular 12 pt `#F0EDE8` at 70%.

---

### ZONE 5 -- Defect Diagnosis Grid

**Section label:** `WHAT GOES WRONG -- ETCH FAILURES` -- Y: 20.7".

**BLOCK F -- 3x2 Grid**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | OVER-ETCHING | `#E05C5C` | Excessive time or temp | Reduce time; check thermostat |
| R1C2 | UNDER-ETCHING | `#E8A020` | Short time or low NaOH | Extend time; replenish NaOH |
| R1C3 | STREAKING | `#E05C5C` | Non-uniform etch (dead zones) | Improve agitation; check load placement |
| R2C1 | PITTING | `#E05C5C` | Grain boundary attack; over-etch | Reduce time; check alloy temper |
| R2C2 | HEAVY SMUT | `#E8A020` | Cu/Zn alloys (2024, 7075) | Normal on copper alloys; aggressive desmut |
| R2C3 | COLOR VARIATION | `#E05C5C` | Etch non-uniformity | Tighten time/temp; match alloy lots |

Each card: Rounded rect W: 7.33", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06".

---

### ZONE 6 -- Etch Control for Color + Safety

**Two-column layout (Y: 26.7" to 32.3"):**

**Left -- Etch Control Checklist:**

Rounded rect, fill `#1E2435`, left accent `#27AE60`.
Title: `ETCH CONTROL FOR INTEGRAL COLOR` Barlow SemiBold 18 pt `#27AE60`.

Checklist (Inter Regular 14 pt `#F0EDE8`):
- `Temperature: +/- 1 C (tighter than standard Type II)`
- `Time: +/- 15 seconds per load`
- `NaOH concentration: titrate weekly minimum`
- `Dissolved Al: test weekly; partial dump above 50 g/L`
- `Alloy lot tracking: tag each rack with alloy heat number`
- `Agitation: verify uniform flow across all parts`

**Right -- Safety:**

Coral-tinted panel:
- Title: `SAFETY` Barlow SemiBold 18 pt `#E05C5C`
- `NaOH is highly caustic -- severe chemical burns`
- `Full-face shield + chemical goggles + rubber gloves`
- `Hydrogen gas is flammable -- NO open flames near etch tank`
- `Adequate ventilation for H2 dispersion`
- `Emergency shower and eyewash within 10 seconds`
- Amber closer: `Follow SDS for your specific etch product` `#E8A020`

---

### ZONE 7 -- Footer

Standard. Title: `Etch -- Integral Color Anodizing`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; ASM Handbook Vol. 5; typical caustic etch parameters for aluminum anodizing.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Etch Integral Color -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster drives home the single most important message for integral color etch: UNIFORMITY. The +/- 15 second time tolerance and +/- 1 C temperature tolerance are tighter than standard Type II and need visual emphasis. The alloy lot control callout addresses the #1 quality problem in architectural integral color work.

---

*Alaina -- Poster #330 -- Construction Workup v1.0 -- 2026-04-26*
