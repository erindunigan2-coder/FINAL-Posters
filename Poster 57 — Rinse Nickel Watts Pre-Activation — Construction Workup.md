---
Project: Plating Posters Inc
Poster Number: 57
Title: "Rinse -- Nickel (Watts) -- Pre-Activation"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-04 technical reference (Watts nickel)"
  - "Watson Research Brief -- Electroplating Clusters EP-02 through EP-15"
Technical Source: Standard double overflow rinse between alkaline cleaning and acid activation for Watts nickel plating.
Process Scope: Pre-activation rinse for Watts nickel plating (Stage 2 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - NickelPlating
  - Watts
  - Rinse
  - PreActivation
  - ConstructionWorkup
  - Series2
  - ClusterEP04
---

# Poster #57 -- Construction Workup
## Rinse -- Nickel (Watts) -- Pre-Activation

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 2 of 8. The rinse between cleaning and activation is a bridge -- it removes alkaline residues before the part enters acid. Alkaline drag-in wastes acid, causes staining, and compromises activation effectiveness. This poster elevates rinsing from an afterthought to a controlled process step.

Hero visual: rinse tank cross-section with overflow/counterflow mechanics, conductivity monitoring, and drag-out volume concepts.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Rinse tank cross-section hero (Block B):** Rounded rectangle tank with overflow weir, inlet/outlet flow arrows, and conductivity probe.
2. **Rinse efficiency principles (Block C):** Drag-out volume, dilution ratio, counterflow concept.
3. **Conductivity monitoring callout (Block D):** Target values and what they mean.
4. **Rinse failure modes (Block E):** 4 common problems.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.0" / 21.0" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 2 highlighted (Teal)
ZONE 3 -- RINSE TANK HERO (4.2"--15.0" / ~10.8")
  Block B: Tank cross-section with flow mechanics
  Block C: Rinse efficiency principles
ZONE 4 -- CONDUCTIVITY + RINSE WATER QUALITY (15.0"--21.0" / ~6.0")
  Block D: Conductivity monitoring
  Block E: Water quality requirements
ZONE 5 -- RINSE TYPES + FAILURE MODES (21.0"--27.0" / ~6.0")
  Block F: Rinse type comparison (single, double, counterflow, cascade)
  Block G: 4 failure modes
ZONE 6 -- PRACTICAL TIPS + SAFETY (27.0"--32.5" / ~5.5")
  Block H: Shop-floor rinse tips
  Block I: Safety notes
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Nickel (Watts) -- Pre-Activation -- Stage 2 of 8` -- 36 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `The bridge between clean and activate. Alkaline drag-in kills your acid bath and stains your parts.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 2 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Alkaline-wet, clean surface --> After: Neutral, alkaline-free surface ready for acid activation`

---

### ZONE 3 -- Rinse Tank Hero

**Section label:** `THE PRE-ACTIVATION RINSE` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Tank Cross-Section**

Y: 5.0" to 12.5".

- Rounded rect tank body, X: 2.0", Y: 5.5", W: 20.0", H: 6.0", fill `#252B3D`, border 2 pt `#2EC4B6`
- Overflow weir on right side: stepped rectangle showing water spilling over
- Fresh water inlet arrow (bottom left): `#2EC4B6` arrow pointing right, labeled `FRESH WATER IN`
- Overflow outlet arrow (top right): `#3A4055` arrow pointing right, labeled `TO DRAIN / TREATMENT`
- Conductivity probe: small rectangle inside tank, right side, labeled `CONDUCTIVITY PROBE`

Parameter labels inside tank (JetBrains Mono 14 pt `#F0EDE8`):
```
Type: Overflow or counterflow
Temperature: Ambient
Stages: 1--2 rinse tanks
Conductivity target: < 500 microS/cm
Time: 30--60 sec immersion
Agitation: Rack movement (3--4 dips)
```

**BLOCK C -- Rinse Efficiency Principles**

Y: 12.8" to 14.8". Three side-by-side callout boxes:

| Principle | X | W | Accent |
|---|---|---|---|
| Drag-Out | 0.5" | 7.33" | `#E8A020` |
| Dilution Ratio | 8.0" | 7.33" | `#2EC4B6` |
| Counterflow Advantage | 15.5" | 8.0" | `#27AE60` |

*Drag-Out:*
- Title: `DRAG-OUT VOLUME` Barlow SemiBold 16 pt `#E8A020`
- Body: `Every part carries a film of process solution into the rinse. Thicker film = more contamination. Drain time over the tank (5--10 sec) reduces drag-out by 50--80%.`

*Dilution Ratio:*
- Title: `DILUTION RATIO` Barlow SemiBold 16 pt `#2EC4B6`
- Body: `Rinse water volume / drag-out volume. Target 1000:1 minimum for nickel pre-treatment. Two counterflow stages achieve this with far less water than a single overflow.`

*Counterflow Advantage:*
- Title: `COUNTERFLOW SAVES WATER` Barlow SemiBold 16 pt `#27AE60`
- Body: `Fresh water enters the final (cleanest) tank and overflows backward to the first (dirtiest). Same rinsing quality, 60--80% less water consumption.`

---

### ZONE 4 -- Conductivity + Water Quality

**Section label:** `MONITORING YOUR RINSE` -- Y: 15.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK D -- Conductivity Monitoring**

Y: 15.8" to 18.5". Full-width callout.
- Rounded rect, fill `#1E2435`, left accent `#2EC4B6`

Horizontal bar gauge (similar to Poster 36 ratio gauge):
- Green zone: `< 500 microS/cm` fill `#27AE60` at 40% -- `GOOD: alkaline residues adequately removed`
- Yellow zone: `500--1000 microS/cm` fill `#E8A020` at 30% -- `MARGINAL: increase flow rate or add rinse stage`
- Red zone: `> 1000 microS/cm` fill `#E05C5C` at 40% -- `FAIL: alkaline carry-over will neutralize activation`

Note below gauge: `Conductivity readings are the fastest, cheapest rinse quality check. A handheld meter costs less than one batch of rejected parts.` Inter Medium 14 pt `#27AE60`.

**BLOCK E -- Water Quality**

Y: 18.8" to 20.8".
- Rounded rect, fill `#1E2435`, left accent `#E8A020`
- Title: `RINSE WATER QUALITY` Barlow SemiBold 16 pt `#E8A020`
- Table:

| Parameter | Target |
|---|---|
| Source | City water or DI (DI preferred for final rinse) |
| Hardness | < 200 ppm as CaCO3 for city water |
| Chloride | < 50 ppm (high chloride can stain) |
| Temperature | Ambient (60--85 F) |

---

### ZONE 5 -- Rinse Types + Failure Modes

**Two-column layout (Y: 21.2" to 26.8"):**

**Left -- Rinse Type Comparison (X: 0.5", W: 11.0"):**

Section label: `RINSE CONFIGURATIONS` Barlow Condensed ExtraBold 20 pt `#F0EDE8`.

Four stacked mini-cards:

| Type | Efficiency | Water Use | Best For |
|---|---|---|---|
| Single overflow | Low | High | Low-volume, non-critical |
| Double overflow | Moderate | Moderate | Standard pre-activation |
| Counterflow (2-stage) | High | Low | Recommended for nickel lines |
| Spray rinse | Very high | Very low | Rack lines with good drainage |

Cards: Rounded rect H: 1.1", fill `#1E2435`, left accent colored by efficiency (coral to emerald).

**Right -- 4 Failure Modes (X: 12.5", W: 11.0"):**

Section label: `WHAT GOES WRONG` Barlow Condensed ExtraBold 20 pt `#F0EDE8`.

| Problem | Cause | Downstream Effect |
|---|---|---|
| Alkaline drag-in to acid | Insufficient rinse time or volume | Acid bath weakened; surface staining |
| Water spotting | Hard water + air dry between rinses | Visible marks under nickel deposit |
| Contamination buildup | No overflow; stagnant rinse | Rinse tank becomes a dilute process tank |
| Cross-contamination | Shared rinse between incompatible processes | Chemical reactions on part surface |

Cards: Rounded rect, fill `#1E2435`, left accent `#E05C5C`.

---

### ZONE 6 -- Practical Tips + Safety

**Two-column layout (Y: 27.2" to 32.3"):**

**Left -- Shop-Floor Tips (X: 0.5", W: 14.0"):**

Section label: `RINSE LIKE YOU MEAN IT` Barlow Condensed ExtraBold 22 pt `#F0EDE8`.

Callout box, fill `#1E2435`, left accent `#27AE60`:

> - Drain parts over the process tank for 5--10 seconds before transferring to rinse.
> - Dip racks 3--4 times in the rinse tank -- do not just dunk and pull.
> - Check overflow rate daily. A clogged drain = a dead rinse.
> - If rinsing barrels, rotate barrel slowly in rinse to flush all parts.
> - A conductivity meter is your best friend. Mount one permanently if volume justifies it.

**Right -- Safety (X: 15.5", W: 8.0"):**

- Rounded rect, fill `#E05C5C` at 10%, border 1 pt `#E05C5C`
- Title: `SAFETY` Barlow Condensed ExtraBold 20 pt `#E05C5C`
- Body:

> - Rinse water after alkaline cleaning is mildly caustic. Avoid skin contact.
> - Overflow water must be routed to waste treatment -- not floor drain.
> - Wet floors around rinse tanks are a slip hazard. Maintain drainage.

---

### ZONE 7 -- Footer

Standard footer. Title: `Rinse -- Nickel (Watts) -- Pre-Activation`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Nickel Watts Pre-Activation -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Rinse posters risk being "boring" -- the content is less dramatic than plating or troubleshooting. Combat this with the conductivity gauge visual (color-coded, immediately scannable) and the counterflow diagram showing water savings. The practical tips section should feel like advice from a veteran plater, not a textbook. Every rinse poster in the series follows this template structure for consistency.

---

*Alaina -- Plating Posters Inc Creative Lead*
*Poster #57 -- Construction Workup v1.0*
*2026-04-26*
