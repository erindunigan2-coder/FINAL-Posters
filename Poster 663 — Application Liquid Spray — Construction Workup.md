---
Project: Plating Posters Inc
Poster Number: 663
Title: "Application -- Liquid Spray Painting"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting & Organic Coating Clusters — Watson Research Brief, Cluster 2.6"
Technical Source: Spray application methods for liquid painting -- conventional air spray, HVLP, airless, air-assisted airless, and electrostatic rotary bell. Includes DFT targets, viscosity control, wet film measurement, and the Faraday cage analogy from electrostatic powder applied to liquid.
Process Scope: Application for liquid spray painting (Stage 5 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - LiquidSprayPainting
  - Application
  - ConstructionWorkup
  - PaintingClusters
  - ClusterPC02
---

# Poster #663 -- Construction Workup
## Application -- Liquid Spray Painting

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 5 of 8. This is the poster where the paint meets the part. Five spray methods span the entire transfer efficiency spectrum -- from 25% conventional air spray (finest finish, most waste) to 95% electrostatic rotary bell (automotive OEM standard). The hero is a five-method comparison with transfer efficiency as the decision driver. Application parameter tables for primer, basecoat, and clearcoat give the painter specific targets. Viscosity control and wet film measurement round out the practical toolset.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Five spray methods comparison (Block B -- HERO):** Conventional, HVLP, airless, air-assisted airless, electrostatic rotary bell -- side-by-side with transfer efficiency as the headline metric.
2. **Application parameter table (Block C):** Primer vs. basecoat vs. clearcoat targets.
3. **Viscosity control + wet film measurement (Block D):** Two practical shop-floor tools.
4. **Defect grid (Block F):** 6 application defects.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.5" / 21.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage highlighted: Application (Emerald)
ZONE 3 -- FIVE SPRAY METHODS HERO (4.2"--15.5" / ~11.3")
ZONE 4 -- APPLICATION PARAMETERS TABLE (15.5"--21.5" / ~6.0")
ZONE 5 -- VISCOSITY + WET FILM TOOLS (21.5"--26.5" / ~5.0")
ZONE 6 -- DEFECT GRID (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `APPLICATION` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Liquid Spray Painting -- Five Methods from 25% to 95% Transfer Efficiency` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `Conventional air spray gives you the finest finish. Electrostatic rotary bell gives you 95% material utilization. Choose by the job, not by habit.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage highlighted: Application -- fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Pretreated, dry surface ready for coating --> After: Wet paint film deposited at target DFT`

---

### ZONE 3 -- Five Spray Methods Hero

**Section label:** `FIVE SPRAY METHODS -- MATCHED TO YOUR APPLICATION` -- Y: 4.4".

**BLOCK B -- Five Cards (Y: 5.0" to 15.0")**

Top row of 3, bottom row of 2.

**Top Row:**

*Conventional Air Spray (X: 0.5", W: 7.33"):*
- Fill: `#1E2435`, top accent `#E8A020`
- Title: `CONVENTIONAL AIR SPRAY` -- Barlow SemiBold, 20 pt, `#E8A020`
- Parameters (JetBrains Mono 12 pt):
```
Atomizing pressure: 30--60 psi at cap
Fluid delivery: 8--15 psi (siphon/pressure)
Transfer efficiency: 25--45%
Finish quality: Excellent (finest atomization)
```
- Best for: `High-quality topcoats, small parts, detail work`
- Trade-off: `Best finish, worst material efficiency`

*HVLP (X: 8.17", W: 7.33"):*
- Fill: `#1E2435`, top accent `#27AE60`
- Title: `HVLP (HIGH VOLUME LOW PRESSURE)` -- Barlow SemiBold, 20 pt, `#27AE60`
- Parameters:
```
Max air pressure at cap: 10 psi
Fluid delivery: Gravity cup or pressure pot
Transfer efficiency: 65%+ (EPA minimum)
Finish quality: Very good
```
- Best for: `General industrial, regulatory compliance`
- Note: `EPA minimum transfer efficiency for many jurisdictions`

*Airless (X: 15.83", W: 7.67"):*
- Fill: `#1E2435`, top accent `#2EC4B6`
- Title: `AIRLESS SPRAY` -- Barlow SemiBold, 20 pt, `#2EC4B6`
- Parameters:
```
Fluid pressure: 1,500--3,000 psi
No compressed air for atomization
Transfer efficiency: 50--70%
Finish quality: Good (coarser atomization)
```
- Best for: `Large surface areas, high production rates`
- Trade-off: `Fast coverage, coarser finish`

**Bottom Row:**

*Air-Assisted Airless (X: 0.5", W: 11.0"):*
- Fill: `#1E2435`, top accent `#E8A020`
- Title: `AIR-ASSISTED AIRLESS` -- Barlow SemiBold, 20 pt, `#E8A020`
- Parameters:
```
Air assist: 5--30 psi
Fluid pressure: 500--1,500 psi
Transfer efficiency: 60--75%
Finish quality: Very good (finer than pure airless)
```
- Best for: `Heavy industrial, shipyard, structural steel`

*Electrostatic Rotary Bell (X: 12.0", W: 11.5"):*
- Fill: `#1E2435`, top accent `#27AE60`
- Title: `ELECTROSTATIC ROTARY BELL` -- Barlow SemiBold, 20 pt, `#27AE60`
- Parameters:
```
Turbine atomizer: 20,000--60,000 RPM
Metered pump fluid delivery
Transfer efficiency: 85--95%
Finish quality: Excellent
```
- Best for: `Automotive OEM, highest efficiency + finish`
- Note: `The gold standard: 95% material utilization + excellent appearance`

---

### ZONE 4 -- Application Parameters Table

**Section label:** `APPLICATION PARAMETERS BY COAT TYPE` -- Y: 15.7".

**BLOCK C -- Three-Column Table (Y: 16.3" to 21.3")**

| Parameter | Primer | Basecoat (Color) | Clearcoat |
|---|---|---|---|
| Target DFT (mils) | 0.8--2.0 | 0.5--1.5 | 1.5--2.5 |
| Number of coats | 1--2 | 2--3 (metallic may need 3+) | 2 |
| Flash between coats | 5--15 min | 3--10 min | 5--15 min |
| Gun distance (inches) | 8--12 | 6--10 | 8--12 |
| Pattern overlap | 50% | 50--75% | 50% |
| Booth air velocity | 75--125 fpm crossdraft | Same | Same |

Header row: fill `#3A4055`, Barlow SemiBold 14 pt `#F0EDE8`.
Data: JetBrains Mono 12 pt. Alternating rows: `#1E2435` / `#252B3D`.

---

### ZONE 5 -- Viscosity + Wet Film Tools

**Section label:** `TWO ESSENTIAL SHOP-FLOOR TOOLS` -- Y: 21.7".

**Two-column layout (Y: 22.3" to 26.3"):**

**Left -- Viscosity Control (X: 0.5", W: 11.0"):**

Callout box, fill `#1E2435`, border 2 pt `#E8A020`.
Title: `VISCOSITY CONTROL` -- Barlow SemiBold, 20 pt, `#E8A020`

- `Zahn Cup (ASTM D4212):`
- `  #2 cup: 12--20 sec (light coatings)`
- `  #4 cup: 15--25 sec (heavier coatings)`
- `Ford Cup (ASTM D1200):`
- `  #4 Ford cup: 15--30 sec for spray viscosity`
- `Calibrate to 77 F (25 C) -- viscosity is temperature-sensitive`

Warning (Coral): `Cold paint sprays thick and sags. Hot paint sprays thin and runs. Temperature matters.`

**Right -- Wet Film Measurement (X: 12.0", W: 11.5"):**

Callout box, fill `#1E2435`, left accent `#27AE60`.
Title: `WET FILM GAUGE (ASTM D4414)` -- Barlow SemiBold, 18 pt, `#27AE60`

- `Notched gauge pressed into wet paint`
- `Read the highest notch that is wetted`
- `Predict DFT from wet film thickness:`
- `  DFT = WFT x (% Volume Solids / 100)`
- `Example: 4 mil WFT x 60% solids = 2.4 mil DFT`

Note: `The wet film gauge is your real-time thickness check. Do not wait for dry film measurement to discover you sprayed too thin or too thick.`

---

### ZONE 6 -- Defect Grid

**Section label:** `WHEN APPLICATION GOES WRONG -- 6 SPRAY DEFECTS` -- Y: 26.7".

**BLOCK F -- 3x2 Grid (Y: 27.3" to 32.3")**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | RUNS / SAGS | `#E05C5C` | Too heavy a coat, gun too close, or gun speed too slow | Reduce fluid flow; increase gun speed; check viscosity |
| R1C2 | ORANGE PEEL | `#E8A020` | Fast solvent evap, low atomization pressure, gun too far | Slow thinner; increase atomizing pressure; reduce distance |
| R1C3 | DRY SPRAY | `#E05C5C` | Gun too far, too low pressure, or paint too viscous | Reduce distance; increase pressure; thin paint |
| R2C1 | OVERSPRAY TEXTURE | `#E8A020` | Overspray from adjacent pass landing on wet film | Adjust pattern overlap; maintain consistent distance |
| R2C2 | FISH-EYE / CRATERING | `#E05C5C` | Silicone or oil contamination on surface | Identify contamination source; clean surface; fish-eye additive |
| R2C3 | SOLVENT POP | `#2EC4B6` | Solvent trapped under skin of fast-drying topcoat | Flash between coats; force flash before bake; slow thinner |

Each card: Rounded rect W: 7.33", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06" in defect color.

---

### ZONE 7 -- Footer

Standard. Title: `Application -- Liquid Spray Painting`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; ASTM D4212, D4414. Spray pressures, tip sizes, and viscosity targets are coating-specific -- consult manufacturer TDS.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Application Liquid Spray -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The five-method comparison is the wall reference for any paint shop supervisor choosing spray equipment. Transfer efficiency is the headline metric because it directly translates to material cost: a shop switching from conventional (30%) to HVLP (65%) roughly halves its paint waste. The electrostatic rotary bell at 95% is the aspirational benchmark. The viscosity/wet film tools section gives the painter two immediate, practical instruments to control quality in real time -- no lab required, just a Zahn cup and a notched gauge.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #663 -- Construction Workup v1.0*
*2026-04-26*
