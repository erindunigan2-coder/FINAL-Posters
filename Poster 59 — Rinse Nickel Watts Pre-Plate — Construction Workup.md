---
Project: Plating Posters Inc
Poster Number: 59
Title: "Rinse -- Nickel (Watts) -- Pre-Plate"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-04 technical reference (Watts nickel)"
  - "Watson Research Brief -- Electroplating Clusters EP-02 through EP-15"
Technical Source: Standard single overflow rinse between acid activation and Watts nickel plating tank. Prevents acid drag-in that lowers bath pH.
Process Scope: Pre-plate rinse for Watts nickel plating (Stage 4 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - NickelPlating
  - Watts
  - Rinse
  - PrePlate
  - ConstructionWorkup
  - Series2
  - ClusterEP04
---

# Poster #59 -- Construction Workup
## Rinse -- Nickel (Watts) -- Pre-Plate

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 4 of 8. The rinse between activation and plating removes residual acid. The Watts bath already contains chloride, so small amounts of HCl drag-in are not catastrophic -- but acid drag-in lowers pH, and pH is the single most critical Watts bath parameter. This poster follows the same rinse template as Poster #57 but with nickel-specific context.

Hero visual: rinse tank with emphasis on the pH impact of acid carry-over into the Watts bath.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Rinse tank hero (Block B):** Single overflow tank with parameter callouts.
2. **pH impact callout (Block C):** Visual showing how acid drag-in shifts Watts bath pH.
3. **Rinse vs. speed tradeoff (Block D):** The tension between thorough rinsing and preventing oxide reformation on activated parts.
4. **Failure modes (Block E):** 4 common problems.

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
  Stage 4 highlighted (Teal)
ZONE 3 -- RINSE TANK HERO + pH IMPACT (4.2"--15.0" / ~10.8")
  Block B: Tank cross-section
  Block C: pH impact visual
ZONE 4 -- RINSE PARAMETERS + SPEED TRADEOFF (15.0"--21.0" / ~6.0")
  Block D: Parameters table
  Block E: Speed vs. thoroughness callout
ZONE 5 -- CHLORIDE CONTEXT + FAILURE MODES (21.0"--27.0" / ~6.0")
  Block F: Why chloride drag-in is less harmful than you think
  Block G: 4 failure modes
ZONE 6 -- PRACTICAL TIPS + SAFETY (27.0"--32.5" / ~5.5")
  Block H: Tips
  Block I: Safety
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Nickel (Watts) -- Pre-Plate -- Stage 4 of 8` -- 36 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `The last chance to protect your Watts bath pH. Acid drag-in is the slow killer of nickel plating consistency.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 4 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Acid-wet, activated surface --> After: Acid-free, active surface ready for nickel deposition`

---

### ZONE 3 -- Rinse Tank Hero + pH Impact

**Section label:** `THE PRE-PLATE RINSE` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Tank Cross-Section**

Y: 5.0" to 10.5". Same construction as Poster #57 tank but labeled for pre-plate context.

Parameter labels (JetBrains Mono 14 pt `#F0EDE8`):
```
Type: Single overflow, ambient
Temperature: Ambient
Stages: 1 tank minimum
Conductivity target: < 200 microS/cm
Time: 30--60 sec
Agitation: Rack movement (3--4 dips)
```

**BLOCK C -- pH Impact Visual**

Y: 11.0" to 14.8". Full-width callout with pH gauge.

- Rounded rect, fill `#1E2435`, border 1 pt `#3A4055`, radius 8

Title: `HOW ACID DRAG-IN AFFECTS YOUR WATTS BATH` Barlow Condensed ExtraBold 22 pt `#F0EDE8`

pH bar gauge (horizontal):
- Red zone left: `< 3.5` fill `#E05C5C` at 40% -- `LOW: poor efficiency, brittle, poor LCD`
- Green zone: `3.8 -- 4.2` fill `#27AE60` at 40% -- `OPTIMAL`
- Yellow zone: `4.2 -- 4.5` fill `#E8A020` at 30% -- `MARGINAL`
- Red zone right: `> 4.5` fill `#E05C5C` at 40% -- `HIGH: dark deposit, Ni(OH)2 co-deposition`
- Optimal marker: triangle at `4.0` -- `#27AE60`

Below gauge: `Every 100 mL of 30% HCl drag-in per 1000 gallons of Watts bath drops pH approximately 0.1--0.2 units. Consistent acid carry-over accumulates. Rinse well.` Inter Medium 13 pt `#E8A020`.

Note: `Chloride drag-in from HCl activation is NOT harmful -- the Watts bath already contains NiCl2. It is the hydrogen ion (acid) that matters.` Inter Regular 13 pt `#2EC4B6`.

---

### ZONE 4 -- Parameters + Speed Tradeoff

**Section label:** `BALANCING SPEED AND QUALITY` -- Y: 15.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK D -- Parameter Summary**

Y: 15.8" to 18.0". Compact table.

| Parameter | Target | Why |
|---|---|---|
| Rinse stages | 1 minimum (2 preferred for high volume) | More stages = less acid carry-over |
| Conductivity | < 200 microS/cm | Lower target than pre-activation rinse |
| Water type | City water acceptable; DI preferred | DI reduces total dissolved solids |
| Overflow rate | Continuous, adequate to dilute drag-in | Adjust based on production throughput |
| Immersion time | 30--60 sec with rack agitation | Balance speed with thoroughness |

**BLOCK E -- The Speed vs. Thoroughness Tradeoff**

Y: 18.3" to 20.8". Two side-by-side callouts.

*Left -- The Problem:*
- Rounded rect, fill `#1E2435`, left accent `#E05C5C`
- Title: `THE RISK OF RUSHING` Barlow SemiBold 16 pt `#E05C5C`
- Body: `Activated surfaces re-oxidize in air. The longer parts sit between activation and plating, the worse adhesion gets. Stainless steel re-passivates in seconds. This creates pressure to rush through the rinse -- but acid drag-in is cumulative and invisible until your pH drifts out of spec.`

*Right -- The Solution:*
- Rounded rect, fill `#1E2435`, left accent `#27AE60`
- Title: `THE BALANCE` Barlow SemiBold 16 pt `#27AE60`
- Body: `For most substrates (mild steel, copper, brass), 30--60 seconds of rinse with agitation is adequate and will not cause re-oxidation. For stainless/Inconel after Wood's strike, transfer to Watts within 30 seconds -- the strike layer protects the surface. The Wood's strike buys you time.`

---

### ZONE 5 -- Chloride Context + Failure Modes

**Two-column layout (Y: 21.2" to 26.8"):**

**Left -- Chloride in Context (X: 0.5", W: 11.0"):**

- Rounded rect, fill `#1E2435`, left accent `#2EC4B6`
- Title: `WHY CHLORIDE DRAG-IN IS LESS HARMFUL THAN YOU THINK` Barlow SemiBold 16 pt `#2EC4B6`
- Body (Inter Regular 14 pt `#F0EDE8`, line height 155%):

> The Watts bath operates at 37--55 g/L NiCl2. A small amount of HCl drag-in adds a negligible amount of chloride relative to what is already there.
>
> Contrast this with sulfamate nickel (EP-05) where chloride-free operation is sometimes required. In sulfamate baths, even small chloride drag-in increases internal stress. Different bath, different rules.
>
> For Watts: focus on the acid (pH impact), not the chloride.

**Right -- 4 Failure Modes (X: 12.5", W: 11.0"):**

| Problem | Cause | Effect |
|---|---|---|
| Acid drag-in to Watts bath | Inadequate rinse or no overflow | pH depression; poor LCD coverage |
| Re-oxidation | Parts air-dried between rinse and plate | Peeling, adhesion failure |
| Water spotting | Hard water deposits dry on surface | Visible marks under nickel |
| Contaminated rinse | Rinse water not changed; no overflow | Parts enter Watts bath with dissolved metals |

Cards: fill `#1E2435`, left accent `#E05C5C`.

---

### ZONE 6 -- Practical Tips + Safety

**Left -- Tips (X: 0.5", W: 14.0"):**

Callout box, fill `#1E2435`, left accent `#27AE60`:

> - Keep parts wet between rinse and plating -- never let them air-dry.
> - For stainless after Wood's strike: straight into the Watts bath. Do not linger.
> - If running high volume, consider a two-stage counterflow rinse to protect the Watts bath long-term.
> - Monitor Watts bath pH at least twice per shift. If pH is trending down, check your rinse quality.

**Right -- Safety (X: 15.5", W: 8.0"):**

Standard safety callout:

> - Rinse water is acidic from activation drag-in. Avoid skin contact.
> - Route overflow to waste treatment.
> - Wet floors -- maintain drainage and non-slip surfaces.

---

### ZONE 7 -- Footer

Standard footer. Title: `Rinse -- Nickel (Watts) -- Pre-Plate`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Nickel Watts Pre-Plate -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The pH impact gauge is the hero element -- it makes the abstract concept of "acid drag-in" tangible and visual. The chloride context callout is unique to Watts nickel and differentiates this rinse poster from the sulfamate version (Poster #67). The speed vs. thoroughness tradeoff is a real-world tension every plater faces and gives this poster practical credibility.

---

*Alaina -- Plating Posters Inc Creative Lead*
*Poster #59 -- Construction Workup v1.0*
*2026-04-26*
