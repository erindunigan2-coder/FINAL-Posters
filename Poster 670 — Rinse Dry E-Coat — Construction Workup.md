---
Project: Plating Posters Inc
Poster Number: 670
Title: "Rinse / Dry -- E-Coat"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting & Organic Coating Clusters -- Watson Research Brief (Cluster 3, Section 3.4)"
Technical Source: Industry-standard rinse and UF permeate recovery systems for cathodic e-coat lines. Values are typical ranges for automotive cathodic epoxy electrodeposition.
Process Scope: Rinse stages and UF permeate recovery for cathodic e-coat -- Stage 4 of 9
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ECoating
  - Rinse
  - UltrafiltrationRecovery
  - ConstructionWorkup
  - PaintingCoating
  - ClusterPC03
---

# Poster #670 -- Construction Workup
## Rinse / Dry -- E-Coat

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 4 of 9. E-coat rinse is unique in the coating world -- the body enters the e-coat tank WET (no dry-off oven), and after e-coat, the UF permeate recovery system reclaims >95% of dragged-out paint. This closed-loop recovery makes e-coat the most material-efficient coating process in existence. The UF system is the unsung hero of every e-coat line.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **UF permeate flow diagram (Block B -- HERO):** Large schematic showing 3-stage counterflow rinse fed by UF permeate, with return flow arrows back to the e-coat tank. Simplified membrane cutaway showing resin/pigment rejection.
2. **Pre-e-coat vs. post-e-coat rinse comparison (Block C):** Two-column layout comparing pre-e-coat rinse (standard water) and post-e-coat rinse (UF permeate).
3. **UF membrane parameter table (Block D):** Compact parameter table for UF system operation.
4. **Defect grid (Block F):** 6 rinse-related defects.

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
  Stage 4 highlighted (Teal)
ZONE 3 -- UF PERMEATE RECOVERY HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- PRE-E-COAT VS. POST-E-COAT RINSE (14.5"--20.5" / ~6.0")
ZONE 5 -- UF MEMBRANE PARAMETERS + CONTROLS (20.5"--26.5" / ~6.0")
ZONE 6 -- DEFECT DIAGNOSIS GRID (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE / DRY` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `E-Coat Line -- UF Permeate Recovery & Rinse Stages -- Stage 4 of 9` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `The body enters e-coat wet. After e-coat, the UF system recovers >95% of dragged-out paint. No other coating method comes close.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 4 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Freshly e-coated body with 10--30% wet weight dragout  -->  After: Clean body ready for bake oven, >99% paint utilization`

---

### ZONE 3 -- UF Permeate Recovery Hero

**Section label:** `CLOSED-LOOP UF PERMEATE RECOVERY -- THE E-COAT ADVANTAGE` -- Y: 4.4".

**BLOCK B -- UF Recovery Flow Diagram**

Y: 5.0" to 14.0".

Large flow diagram showing the post-e-coat rinse system. Left-to-right flow:

**E-Coat Tank Box (X: 0.5", W: 5.0", H: 8.0"):**
- Rounded rect, fill `#1E2435`, left accent 0.06" `#E8A020`
- Title: `E-COAT TANK` Barlow SemiBold 20 pt `#E8A020`
- Parameters:
```
18--22% solids
200--400 V DC
85--95 F (29--35 C)
```
JetBrains Mono 13 pt `#F0EDE8`.
- Note: `Body exits with 10--30% wet weight dragout` Inter Regular 13 pt `#F0EDE8` at 70%.

**Arrow to UF Rinse 1:**
- 3 pt stroke `#3A4055`, right arrowhead.
- Label above arrow: `Dragout` Inter Medium 12 pt `#E8A020`.

**UF Rinse Stage 1 (X: 6.5", W: 4.0", H: 8.0"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#2EC4B6`
- Badge: `RINSE 1` fill `#2EC4B6`, text `#1A1F2E`
- Title: `UF Permeate Rinse 1`
- Parameters: `Counterflow from Rinse 2` / `Highest paint concentration`
- Note: `Rinse water returns to e-coat tank` Inter Medium 12 pt `#27AE60`

**Return arrow from Rinse 1 back to E-Coat Tank:**
- Curved arrow, 3 pt stroke `#27AE60`, arrowhead pointing left/back.
- Label: `Recovered paint returns to tank` Inter Medium 11 pt `#27AE60`.

**UF Rinse Stage 2 (X: 11.5", W: 4.0", H: 8.0"):**
- Same styling as Rinse 1
- Badge: `RINSE 2`
- Title: `UF Permeate Rinse 2`
- Parameters: `Counterflow from Rinse 3` / `Medium concentration`

**UF Rinse Stage 3 (X: 16.5", W: 4.0", H: 8.0"):**
- Badge: `RINSE 3`
- Title: `Fresh UF Permeate`
- Parameters: `Fed by fresh permeate from UF membranes` / `Cleanest stage`

**UF Membrane Callout (X: 21.0", W: 2.5", H: 5.0"):**
- Rounded rect, fill `#1E2435`, left accent 0.06" `#E8A020`
- Title: `UF MEMBRANES` Barlow SemiBold 16 pt `#E8A020`
- Parameters:
```
50,000--100,000 MWCO
Polysulfone or PVDF
5--20 gal/min per
  100 ft2 membrane
```
- Note: `Extracts water + small molecules. Rejects resin + pigment.` Inter Regular 12 pt `#F0EDE8` at 70%.

**Final DI Rinse (bottom right, X: 16.5", Y: 11.0", W: 4.0", H: 2.5"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#2EC4B6`
- Title: `DI FINAL RINSE`
- Parameters: `< 20 uS/cm` / `Removes residual permeate before bake`

---

### ZONE 4 -- Pre-E-Coat vs. Post-E-Coat Rinse

**Section label:** `TWO RINSE WORLDS -- BEFORE AND AFTER THE E-COAT TANK` -- Y: 14.7".

**Two-column layout (Y: 15.3" to 20.3"):**

**Left -- Pre-E-Coat Rinse (X: 0.5", W: 11.0", H: 4.8"):**
- Rounded rect, fill `#1E2435`, left accent 0.06" `#2EC4B6`
- Title: `PRE-E-COAT RINSE` Barlow SemiBold 20 pt `#2EC4B6`
- Subtitle: `After Cleaning & Phosphate -- Before E-Coat Tank` Barlow Condensed ExtraBold 14 pt `#F0EDE8` at 50%

Properties (Inter Regular 14 pt `#F0EDE8`, line height 155%):

| Property | Value |
|---|---|
| Rinse type | Standard city water + DI |
| Stages after clean | 2 spray rinse, counterflow |
| Stages after phosphate | 2 immersion + seal rinse + DI |
| DI quality | < 20 uS/cm conductivity |
| Dry-off oven | NO -- body enters e-coat WET |
| Purpose | Remove chemical residuals |

Bottom highlight:
- Rounded rect, W: 10.0", H: 0.6", fill `#2EC4B6` at 15%, border 1 pt `#2EC4B6`
- Text: `No dry-off oven. The wet surface is electrochemically active. E-coat is an aqueous process.` Inter Medium 13 pt `#2EC4B6`

**Right -- Post-E-Coat Rinse (X: 12.0", W: 11.5", H: 4.8"):**
- Rounded rect, fill `#1E2435`, left accent 0.06" `#E8A020`
- Title: `POST-E-COAT RINSE (UF RECOVERY)` Barlow SemiBold 20 pt `#E8A020`
- Subtitle: `After E-Coat Tank -- Before Bake Oven` Barlow Condensed ExtraBold 14 pt `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Rinse type | UF permeate (not water) |
| Stages | 2--3 counterflow + DI final |
| Permeate source | UF membranes on e-coat tank |
| Paint recovery | >95% of dragout recovered |
| Total paint utilization | >99% |
| Purpose | Recover paint + clean body for bake |

Bottom highlight:
- Rounded rect, W: 10.5", H: 0.6", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `Closed-loop recovery. Rinse dragout flows back to the e-coat tank. Near-zero paint waste.` Inter Medium 13 pt `#E8A020`

---

### ZONE 5 -- UF Membrane Parameters + Controls

**Section label:** `UF SYSTEM -- PARAMETERS AND MONITORING` -- Y: 20.7".

**BLOCK D -- UF Parameter Table (Y: 21.3" to 24.5")**

Full-width table. Column widths (23.0" total):
- Parameter (6.0") | Typical Range (6.0") | Method (5.5") | Action Limit (5.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold 14 pt `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.5".

| Parameter | Typical Range | Method | Action Limit |
|---|---|---|---|
| UF pore size (MWCO) | 50,000--100,000 daltons | Manufacturer spec | -- |
| Permeate flow rate | 5--20 gal/min per 100 ft2 | Flow meter | < 70% of baseline = foul |
| Permeate conductivity | 500--2,000 uS/cm | Conductivity meter | Rising trend = membrane damage |
| Permeate pH | 5.8--6.2 (tracks bath) | pH meter | Deviation > 0.5 = investigate |
| Membrane material | Polysulfone or PVDF | -- | -- |
| Trans-membrane pressure | 10--30 psi | Pressure gauge | > 40 psi = fouling |

Data: JetBrains Mono Regular 12 pt `#F0EDE8`. Parameter names: Inter Medium 13 pt.

**BLOCK E -- Critical Controls Strip (Y: 25.0" to 26.3")**

Three side-by-side callout boxes:

| Control | X | W | Accent | Title | Content |
|---|---|---|---|---|---|
| Permeate Quality | 0.5" | 7.33" | `#2EC4B6` | PERMEATE QUALITY | `Monitor conductivity daily. Rising conductivity = membrane integrity loss. Resin/pigment in permeate = replace membrane.` |
| Membrane Cleaning | 8.0" | 7.33" | `#E8A020` | MEMBRANE CLEANING | `Periodic flush with permeate + mild cleaning solution. Frequency: per manufacturer schedule or when flow drops 30%.` |
| DI Final Rinse | 15.5" | 8.0" | `#27AE60` | DI FINAL RINSE | `< 20 uS/cm conductivity. Prevents water spots and defects in cured film. Last rinse before bake oven.` |

Each box: Rounded rect H: 1.3", fill `#1E2435`, left accent 0.06".

---

### ZONE 6 -- Defect Diagnosis Grid

**Section label:** `WHAT GOES WRONG -- 6 RINSE & RECOVERY DEFECTS` -- Y: 26.7".

**BLOCK F -- 3x2 Grid**

Y: 27.3" to 32.3".

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | WATER SPOTS ON CURED FILM | `#E05C5C` | High TDS in final rinse | Verify DI < 20 uS/cm; check DI system |
| R1C2 | PAINT LOSS / LOW RECOVERY | `#E8A020` | UF membranes fouled or damaged | Clean or replace UF membranes; check permeate flow |
| R1C3 | CRATERING AFTER BAKE | `#E05C5C` | Contamination in UF permeate (oil, silicone) | Filter permeate; check for contamination source |
| R2C1 | UNEVEN FILM IN CAVITIES | `#E8A020` | Insufficient rinse coverage in box sections | Verify body drainage paths; increase rinse dwell |
| R2C2 | RISING BATH CONDUCTIVITY | `#2EC4B6` | UF system not removing enough anolyte | Check anode box bleed rate; increase UF throughput |
| R2C3 | MEMBRANE FOULING | `#E05C5C` | Biological growth or resin buildup on membranes | Implement cleaning schedule; check biocide levels |

Each card: Rounded rect W: 7.33", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06" in defect color.

Interior per card:
- Defect: Barlow SemiBold 16 pt in defect color
- Cause: Inter Regular 13 pt `#F0EDE8`
- Fix: Inter Medium 13 pt `#27AE60`

---

### ZONE 7 -- Footer

Standard. Title: `Rinse / Dry -- E-Coat`. Version `v1.0 -- 2026`.

Disclaimer note: `Source: General industry knowledge; automotive e-coat specifications. UF membrane parameters are typical for cathodic epoxy systems.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Dry E-Coat -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The UF permeate recovery system is what makes e-coat fundamentally different from every other coating method. No spray booth, no overspray waste, no solvent emission from application -- just a closed-loop electrical deposition with near-perfect material utilization. The counterflow rinse concept with UF permeate is elegantly simple but absolutely critical to understand. The "no dry-off oven before e-coat" callout is essential -- it catches every powder coater and spray painter off guard.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #670 -- Construction Workup v1.0*
*2026-04-26*
