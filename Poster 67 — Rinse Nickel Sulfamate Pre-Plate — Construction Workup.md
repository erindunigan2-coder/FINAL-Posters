---
Project: Plating Posters Inc
Poster Number: 67
Title: "Rinse -- Nickel (Sulfamate) -- Pre-Plate"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-05 technical reference (Sulfamate nickel)"
  - "Watson Research Brief -- Electroplating Clusters EP-02 through EP-15"
Technical Source: Single overflow rinse between acid activation and sulfamate nickel plating tank. Prevents acid drag-in that lowers bath pH. Special consideration: chloride drag-in from HCl activation increases stress in sulfamate baths.
Process Scope: Pre-plate rinse for sulfamate nickel plating (Stage 4 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - NickelPlating
  - Sulfamate
  - Rinse
  - PrePlate
  - ConstructionWorkup
  - Series2
  - ClusterEP05
---

# Poster #67 -- Construction Workup
## Rinse -- Nickel (Sulfamate) -- Pre-Plate

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 4 of 8. The rinse between activation and plating is MORE critical for sulfamate than for Watts. The pH concern is the same (acid drag-in lowers pH), but sulfamate baths have an additional vulnerability: chloride drag-in from HCl activation increases internal stress. Many sulfamate baths operate with zero or minimal chloride specifically to minimize stress -- any chloride carry-over undermines this.

This is the poster where the Watts vs. sulfamate rinse difference is most stark. Poster #59 (Watts pre-plate rinse) noted that chloride drag-in is harmless for Watts. Here, chloride drag-in is harmful for sulfamate. Different bath, different rules.

Hero visual: rinse tank with emphasis on both pH impact AND chloride stress impact.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
Same construction as Poster #59. Rinse tank hero, pH impact visual, rinse parameters. Unique element: chloride drag-in stress impact callout -- the critical differentiation from the Watts version.

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
ZONE 3 -- RINSE TANK HERO + DUAL IMPACT (4.2"--15.0" / ~10.8")
  Block B: Tank cross-section
  Block C: pH impact gauge
  Block D: Chloride stress impact callout
ZONE 4 -- RINSE PARAMETERS + CHLORIDE-FREE CONTEXT (15.0"--21.0" / ~6.0")
  Block E: Parameters table
  Block F: Why some sulfamate baths run chloride-free
ZONE 5 -- WATTS VS. SULFAMATE RINSE RULES + FAILURES (21.0"--27.0" / ~6.0")
  Block G: Side-by-side rinse rule comparison
  Block H: 4 failure modes
ZONE 6 -- PRACTICAL TIPS + SAFETY (27.0"--32.5" / ~5.5")
  Block I: Tips
  Block J: Safety
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Nickel (Sulfamate) -- Pre-Plate -- Stage 4 of 8` -- 36 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `Chloride drag-in is harmless in Watts nickel. In sulfamate, it increases stress. Different bath, different rules.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 4 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Acid-wet, activated surface --> After: Acid-free, chloride-free surface ready for sulfamate deposition`

---

### ZONE 3 -- Rinse Tank Hero + Dual Impact

**Section label:** `THE PRE-PLATE RINSE -- TWO THINGS TO REMOVE` -- Y: 4.4".

**BLOCK B -- Tank Cross-Section**

Same construction as Poster #59. Parameters:
```
Type: Single overflow minimum; double preferred for sulfamate
Temperature: Ambient
Conductivity target: < 100 microS/cm (tighter than Watts)
Time: 30--60 sec with agitation
Stages: 2 preferred (counterflow)
```

Note the tighter conductivity target vs. Poster #59 (< 100 vs. < 200 microS/cm).

**BLOCK C -- pH Impact Gauge**

Same gauge as Poster #59:
- Red: `< 3.5` -- `LOW: hydrolysis risk + poor efficiency`
- Green: `3.8--4.2` -- `OPTIMAL`
- Yellow: `4.2--4.5` -- `MARGINAL`
- Red: `> 4.5` -- `HIGH: dark deposit, Ni(OH)2`

**BLOCK D -- Chloride Stress Impact Callout**

Y: 12.0" to 14.8". Full-width callout -- the unique hero element.
- Rounded rect, fill `#E05C5C` at 12%, border 2 pt `#E05C5C`, radius 8

Title: `CHLORIDE DRAG-IN INCREASES STRESS` Barlow Condensed ExtraBold 24 pt `#E05C5C`

Body (Inter Medium 14 pt `#F0EDE8`, line height 160%):

> HCl activation leaves chloride ions on the part surface. In a Watts bath (which contains 37--55 g/L NiCl2), this is negligible. In a sulfamate bath -- especially one running zero chloride for minimum stress -- even small chloride additions shift the deposit toward higher tensile stress.
>
> Chloride effect on sulfamate stress: increasing NiCl2 from 0 to 30 g/L can shift stress from near-zero to moderate tensile. Every gram of chloride matters for electroforming and fatigue-critical applications.
>
> The pre-plate rinse is your last line of defense against chloride contamination of the sulfamate bath.

---

### ZONE 4 -- Parameters + Chloride-Free Context

**Two-column layout (Y: 15.2" to 20.8"):**

**Left -- Parameter Summary (X: 0.5", W: 11.0"):**

| Parameter | Target | Why (Sulfamate-Specific) |
|---|---|---|
| Rinse stages | 2 minimum (counterflow) | Tighter rinse for chloride removal |
| Conductivity | < 100 microS/cm | Stricter than Watts (< 200) |
| Water type | DI preferred | Reduces all dissolved ions |
| Overflow rate | High -- continuous overflow | Must dilute chloride effectively |
| Immersion time | 30--60 sec with agitation | Balance speed with thoroughness |

**Right -- Why Some Sulfamate Baths Run Chloride-Free (X: 12.5", W: 11.0"):**

- Rounded rect, fill `#1E2435`, left accent `#E8A020`
- Title: `ZERO-CHLORIDE SULFAMATE` Barlow SemiBold 18 pt `#E8A020`
- Body (Inter Regular 13 pt `#F0EDE8`, line height 155%):

> High-purity electroforming baths often operate with ZERO nickel chloride. Instead of soluble nickel anodes (which need chloride to prevent passivation), they use:
>
> - Insoluble titanium mesh anodes
> - Nickel sulfamate concentrate added to maintain metal level
>
> This eliminates the chloride variable entirely. In these baths, ANY chloride contamination -- from activation, from rinse water, from cross-contamination -- degrades deposit quality.
>
> For zero-chloride baths: consider DI water rinsing exclusively and a dedicated pre-plate rinse tank not shared with any other process.

---

### ZONE 5 -- Watts vs. Sulfamate Rinse Rules + Failures

**Two-column layout (Y: 21.2" to 26.8"):**

**Left -- Rinse Rule Comparison (X: 0.5", W: 11.0"):**

- Rounded rect, fill `#1E2435`, border 1 pt `#3A4055`
- Title: `DIFFERENT BATHS, DIFFERENT RINSE RULES` Barlow SemiBold 18 pt `#F0EDE8`

| Factor | Watts | Sulfamate |
|---|---|---|
| Acid drag-in | Bad (lowers pH) | Bad (lowers pH + hydrolysis risk) |
| Chloride drag-in | Harmless (bath contains chloride) | HARMFUL (increases stress) |
| Conductivity target | < 200 microS/cm | < 100 microS/cm |
| Recommended stages | 1 minimum | 2 minimum (counterflow) |
| Water type | City OK | DI preferred |
| Overall rinse urgency | Moderate | HIGH |

Table: JetBrains Mono 12 pt. "HARMFUL" in `#E05C5C`.

**Right -- 4 Failure Modes (X: 12.5", W: 11.0"):**

| Problem | Cause | Effect |
|---|---|---|
| Chloride contamination | HCl drag-in not removed | Stress increase in sulfamate deposit |
| Acid drag-in (pH drop) | Inadequate rinse | pH below 3.0 causes sulfamate hydrolysis |
| Re-oxidation | Parts air-dried between rinse and plate | Adhesion failure |
| Cross-process contamination | Shared rinse with Watts or other bath | Mixed chemistry drag-in |

---

### ZONE 6 -- Practical Tips + Safety

**Left -- Tips (X: 0.5", W: 14.0"):**

> - For chloride-free sulfamate baths: use DI water exclusively for this rinse.
> - Two-stage counterflow rinse is the minimum for sulfamate lines.
> - If you activated with HCl: the rinse must remove ALL chloride. Consider an extended immersion or additional rinse stage.
> - Keep parts wet between rinse and plating. Activated surfaces re-oxidize in air.
> - Monitor sulfamate bath chloride levels weekly. If chloride is rising, your rinse is not doing its job.

**Right -- Safety (X: 15.5", W: 8.0"):**

> - Rinse water is acidic from activation drag-in.
> - Route overflow to waste treatment.
> - Nickel-containing rinse water: treated as hazardous waste.

---

### ZONE 7 -- Footer

Standard footer. Title: `Rinse -- Nickel (Sulfamate) -- Pre-Plate`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Nickel Sulfamate Pre-Plate -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the rinse poster with the biggest delta from its Watts counterpart. The chloride stress impact callout is the hero -- it is the insight that separates a Watts plater from a sulfamate plater. The side-by-side rinse rule comparison (Watts vs. Sulfamate) is a powerful visual that makes the difference concrete and unmissable. This poster earns its place in the series by articulating a rule that many platers learn the hard way.

---

*Alaina -- Plating Posters Inc Creative Lead*
*Poster #67 -- Construction Workup v1.0*
*2026-04-26*
