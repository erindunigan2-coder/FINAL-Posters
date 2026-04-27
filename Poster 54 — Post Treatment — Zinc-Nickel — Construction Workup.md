---
Project: Plating Posters Inc
Poster Number: 54
Title: "Post Treatment -- Zinc-Nickel"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-03 technical reference (zinc-nickel alloy plating)"
  - "Watson Research Brief -- Electroplating Clusters"
Technical Source: Post-treatment for zinc-nickel alloy plating -- trivalent passivation, topcoat sealer, HE bake, and cure. This is where the 1,000+ hour salt spray performance is created. The plating alone provides only partial protection; the passivation + sealer system multiplies it.
Process Scope: Post-treatment for zinc-nickel plating (Stages 7--8 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ZincNickelPlating
  - PostTreatment
  - Passivation
  - ConstructionWorkup
  - Series2
  - ClusterEP03
---

# Poster #54 -- Construction Workup
## Post Treatment -- Zinc-Nickel

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stages 7--8 of 8. This is the final poster in the EP-03 cluster and it covers the most value-creating steps: trivalent passivation, topcoat sealer, HE bake (if required), and cure. The plating gives you the alloy; the post-treatment gives you the performance. Watson's brief shows the performance multiplier: Zn-Ni alone might give 200--400 hours to red rust. Add trivalent passivation: 500--1,000 hours. Add sealer: 1,000--2,000+ hours.

Hexavalent chromates are almost universally prohibited for Zn-Ni in automotive and aerospace -- trivalent is the standard. This poster does not cover hexavalent passivation.

Hero visual: performance waterfall chart showing the salt spray hours added at each step (plate -> passivate -> seal).

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Performance waterfall hero (Block B):** Visual showing cumulative salt spray hours: plate alone -> + passivation -> + sealer.
2. **Trivalent passivation parameters (Block C):** Clear, iridescent, and black variants with salt spray performance.
3. **Topcoat sealer parameters (Block D):** Application and cure specifications.
4. **HE bake callout (Block E):** Full bake requirements with ASTM B850 / AMS 2759/9 timing.
5. **Applicable specifications table (Block G).**
6. **Orientation strip:** Stages 7--8 highlighted (Amber).

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 13.5" / 20.0" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stages 7--8 highlighted (Amber)
ZONE 3 -- PERFORMANCE WATERFALL HERO + PASSIVATION (4.2"--13.5" / ~9.3")
  Block B: Salt spray performance waterfall
  Block C: Trivalent passivation parameters and types
ZONE 4 -- SEALER + CURE (13.5"--20.0" / ~6.5")
  Block D: Topcoat sealer parameters
  Block D2: Cure/dry specifications
ZONE 5 -- HE BAKE + COMMON FAILURES (20.0"--27.0" / ~7.0")
  Block E: Hydrogen embrittlement bake requirements
  Block F: Common post-treatment failures
ZONE 6 -- SPECIFICATIONS + SAFETY (27.0"--32.5" / ~5.5")
  Block G: Applicable specifications table
  Block H: Safety callout
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `POST TREATMENT` -- 80 pt `#F0EDE8`, letter spacing -4. X: 0.5", Y: 0.5".
**Subheading:** `Zinc-Nickel -- Stages 7--8 of 8 -- Passivation, Seal, Bake, Cure` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `The plating gives you the alloy. The post-treatment gives you the performance. 1,000+ hours salt spray starts here.` -- 20 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stages 7--8 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Freshly plated Zn-Ni alloy  -->  After: Passivated, sealed, cured -- full corrosion protection system`

---

### ZONE 3 -- Performance Waterfall + Passivation

**Section label:** `THE CORROSION PROTECTION SYSTEM` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Salt Spray Performance Waterfall**

Y: 5.0" to 8.5". Full width.

Three stacked horizontal bars showing cumulative salt spray (red rust) hours:

- Bar 1: `Zn-Ni plate only` -- width proportional to 200--400 hr -- fill `#27AE60` at 40%
  - Label: `200--400 hr` JetBrains Mono 14 pt `#27AE60`

- Bar 2: `+ Trivalent passivation` -- extends to 500--1,000 hr -- fill `#E8A020` at 40%
  - Label: `500--1,000 hr` JetBrains Mono 14 pt `#E8A020`

- Bar 3: `+ Topcoat sealer` -- extends to 1,000--2,000+ hr -- fill `#2EC4B6` at 40%
  - Label: `1,000--2,000+ hr` JetBrains Mono 14 pt `#2EC4B6`

Right of bars: `ASTM B841 Class 2` JetBrains Mono 12 pt `#F0EDE8` at 60%.

**BLOCK C -- Trivalent Passivation Parameters**

Y: 9.0" to 13.3".

Section sublabel: `TRIVALENT PASSIVATION -- THE STANDARD FOR Zn-Ni` Barlow SemiBold 18 pt `#E8A020`.

| Passivation Type | Salt Spray (White) | Salt Spray (Red Rust) | Notes |
|---|---|---|---|
| Trivalent clear | 120--200 hr | 500--1,000 hr | Automotive standard; transparent to iridescent |
| Trivalent iridescent | 200--400 hr | 720--1,500 hr | Higher protection; slight yellow-green |
| Trivalent black | 96--200 hr | 500--1,000 hr | Appearance applications; lower corrosion |
| Trivalent + topcoat sealer | 400--1,000 hr | 1,000--2,000+ hr | Premium automotive / aerospace |

Data: JetBrains Mono 12 pt `#F0EDE8`. Headers: Barlow SemiBold 13 pt `#F0EDE8` on `#3A4055`.

Below table:

Common passivation parameters (rounded rect, fill `#1E2435`, left accent `#E8A020`):
```
pH: 1.5--3.0 (trivalent Cr3+ solution)
Temperature: 70--110 F (21--43 C)
Immersion time: 30--90 sec
Agitation: Mild -- do not damage passivation film during dip
Rinse after: Gentle -- passivation film is soft until cured
```
JetBrains Mono 13 pt `#F0EDE8`.

Note: `Hexavalent chromates are almost universally PROHIBITED for Zn-Ni in automotive and aerospace. This poster covers trivalent passivation only.` Inter Medium 12 pt `#E05C5C`.

---

### ZONE 4 -- Sealer + Cure

**Section label:** `TOPCOAT SEALER AND CURE` -- Y: 13.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK D -- Topcoat Sealer Parameters**

Y: 14.3" to 17.5".

Rounded rect, fill `#1E2435`, left accent `#2EC4B6`, W: 23.0".

| Parameter | Value |
|---|---|
| Type | Proprietary organic or inorganic sealer (per supplier TDS) |
| Application | Dip, spray, or flood |
| Temperature | 150--180 F (66--82 C) for dip application |
| Immersion time | 30--60 sec |
| Purpose | Seals micro-porosity in passivation; adds organic barrier layer |
| Performance boost | Doubles or triples salt spray hours vs. passivation alone |
| Note | Sealer is almost always REQUIRED for Zn-Ni per OEM specs |

Data: JetBrains Mono 12 pt `#F0EDE8`.

**BLOCK D2 -- Cure/Dry Specifications**

Y: 17.8" to 19.8".

Two side-by-side callouts:

Left -- `HOT AIR DRY` (W: 11.0", fill `#1E2435`, left accent `#2EC4B6`):
- `Temperature: 150--170 F (66--77 C)`
- `Time: 15--20 min`
- `Purpose: Cure passivation + sealer; drive off water`
- `CRITICAL: Do not exceed 250 F -- passivation degrades`

Right -- `OVEN CURE` (W: 11.5", fill `#1E2435`, left accent `#E8A020`):
- `Some sealers require dedicated oven cure`
- `Temperature: per TDS (typically 150--200 F)`
- `Time: per TDS (typically 10--30 min)`
- `Verify: finger-touch dry =/= fully cured`

---

### ZONE 5 -- HE Bake + Common Failures

**Two-column layout (Y: 20.2" to 26.8"):**

**Left -- HE Bake Requirements (X: 0.5", W: 14.0"):**

Section label: `HYDROGEN EMBRITTLEMENT BAKE` Barlow Condensed ExtraBold 22 pt `#E05C5C`.

Full panel, fill `#1E2435`, border 2 pt `#E05C5C`:

Title: `BAKE BEFORE PASSIVATION` Barlow SemiBold 18 pt `#E05C5C`

Body (Inter Regular 13 pt `#F0EDE8`, line height 155%):
- `Zn-Ni is predominantly applied to high-strength steel.`
- `HE bake is the DEFAULT assumption.`
- `Bake BEFORE passivation -- heat degrades conversion coatings.`
- `REQUIREMENTS:`
  - `Temperature: 375 +/- 25 F (190 +/- 14 C)`
  - `Aerospace: within 1 HOUR of plating (AMS 2759/9)`
  - `Automotive / general: within 4 HOURS of plating (ASTM B850)`
  - `Hold: 8--24 hr (aerospace typically 23 hr min at >= 39 HRC)`
  - `After bake: proceed to passivation within a few hours`

Key specs: `ASTM B850 | AMS 2759/9 | ASTM B841` JetBrains Mono 12 pt `#E05C5C`.

**Right -- Common Post-Treatment Failures (X: 15.5", W: 8.0"):**

Section label: `WHAT GOES WRONG` Barlow Condensed ExtraBold 18 pt `#F0EDE8`.

| Failure | Cause |
|---|---|
| Passivate flaking | NaOH drag-in; pH out of range; overexposure |
| Poor salt spray | Alloy out of spec; passivate exhausted; no sealer |
| Sealer haze | Over-applied; wrong cure temp |
| HE failure in service | Bake skipped or delayed; insufficient time |
| Passivate discoloration | Contaminated passivation bath; Ni or Fe buildup |

Cards: fill `#1E2435`. Failure: `#E05C5C`. Cause: `#F0EDE8`.

---

### ZONE 6 -- Specifications + Safety

**Two-column layout (Y: 27.2" to 32.3"):**

**Left -- Applicable Specifications (X: 0.5", W: 14.0"):**

Section label: `APPLICABLE SPECIFICATIONS` Barlow Condensed ExtraBold 20 pt `#F0EDE8`.

| Specification | Coverage |
|---|---|
| ASTM B841 | Zn-Ni alloy coatings (general) |
| ASTM B850 | HE relief baking |
| AMS 2417 | Zinc-nickel plating (aerospace) |
| GM 6191M | GM OEM zinc-nickel |
| Ford WSS-M21P38-A2 | Ford OEM zinc-nickel |
| VW TL 233 / TL 244 | European automotive |
| Boeing BAC 5748 | Aerospace zinc-nickel |

Data: JetBrains Mono 12 pt `#F0EDE8`.

**Right -- Safety (X: 15.5", W: 8.0"):**

- Rounded rect, fill `#E05C5C` at 10%, border 1 pt `#E05C5C`, radius 8
- Title: `SAFETY` Barlow Condensed ExtraBold 20 pt `#E05C5C`
- Body:

> - Trivalent passivation: Cr(III) is low toxicity but acidic (pH 1.5--3.0). Acid burn hazard.
> - Sealer: generally low toxicity; check SDS for specific product.
> - HE bake ovens: burn hazard at 375 F. Lockout/tagout for maintenance.
> - Waste treatment: Cr(III) precipitates as hydroxide at pH 8--9.
> - PPE: acid-resistant gloves, goggles, apron for passivation.

---

### ZONE 7 -- Footer

Standard footer. Title: `Post Treatment -- Zinc-Nickel`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Post-treatment parameters shown are typical industry values for zinc-nickel alloy plating. Salt spray values are representative ranges and depend on plating thickness, alloy composition, passivation type, and sealer system. Consult your process supplier for application-specific guidance.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table (see Poster #47).
**Export:** Six files -- `Post Treatment Zinc-Nickel -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the capstone poster for EP-03 and it carries the series' headline performance number: 1,000--2,000+ hours salt spray. The performance waterfall (Block B) is the hero visual -- it makes the cumulative value of each post-treatment step immediately visible. Shops that skip the sealer (to save cost or cycle time) need to see what they're leaving on the table.

The HE bake callout emphasizes "BAKE BEFORE PASSIVATION" because this is a common mistake: shops passivate first, then bake, and the heat destroys the conversion coating. Watson's brief: "Bake BEFORE passivation."

Key specs (ASTM B841, AMS 2417, GM 6191M, etc.) are included in this poster specifically because the post-treatment step is where most OEM spec compliance is measured -- salt spray testing happens on finished parts.

---

*Alaina -- Plating Posters Inc Creative Lead*
*Poster #54 -- Construction Workup v1.0*
*2026-04-26*
