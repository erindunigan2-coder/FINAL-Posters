---
Project: Plating Posters Inc
Poster Number: 93
Title: "Rinse -- Hard Chrome -- Post-Plate"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-08 technical reference (hard chrome plating)"
  - "Watson Research Brief -- Electroplating Clusters"
Technical Source: Post-plate rinse for hard chrome -- the most environmentally critical rinse in the entire poster series. Chrome bath drag-out contains hexavalent chromium (Cr VI), a regulated carcinogen and EPA hazardous waste. Multi-stage cascade rinse with drag-out recovery is mandatory. Watson brief: "CRITICAL. Chrome bath dragout contains hexavalent chromium -- a regulated carcinogen."
Process Scope: Post-plate rinse for hard chrome plating (Stage 6 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - HardChrome
  - Hexavalent
  - Rinse
  - PostPlate
  - ConstructionWorkup
  - ClusterEP08
---

# Poster #93 -- Construction Workup
## Rinse -- Hard Chrome -- Post-Plate

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 6 of 8. This is the most environmentally regulated rinse step in the entire poster series. Every drop of drag-out from the hard chrome bath contains hexavalent chromium -- a confirmed human carcinogen, EPA hazardous waste (D007), and one of the most tightly regulated substances in plating wastewater.

The rinse system must accomplish three things: (1) recover as much chrome chemistry as possible (economic and environmental), (2) remove all Cr(VI) from the part surface, and (3) ensure all rinse water goes to proper Cr(VI) reduction treatment.

Multi-stage cascade (drag-out recovery + double or triple counterflow) is the standard. DI water final rinse for precision parts.

Hero visual: multi-stage rinse cascade with Cr(VI) regulatory callouts at every step.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Multi-stage rinse cascade hero (Block B):** Drag-out recovery + double/triple counterflow with Cr(VI) labels.
2. **Cr(VI) wastewater treatment callout (Block C):** Reduction + precipitation process.
3. **Drag-out reduction methods (Block D):** Fume suppressants, drain time, rinse design.
4. **Safety banner in Zone 1 (Block A2):** Same Cr(VI) warning as Poster #87.
5. **Orientation strip:** Stage 6 highlighted (Teal).

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline
  Block A2: Safety banner
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 6 highlighted (Teal)
ZONE 3 -- MULTI-STAGE RINSE CASCADE HERO (4.2"--14.5" / ~10.3")
  Block B: Rinse cascade diagram (recovery + counterflow)
  Block C: Cr(VI) wastewater treatment callout
ZONE 4 -- DRAG-OUT REDUCTION + RINSE PARAMETERS (14.5"--20.5" / ~6.0")
  Block D: Drag-out reduction methods
  Block E: Rinse parameter table
ZONE 5 -- COMMON FAILURES + REGULATORY (20.5"--27.0" / ~6.5")
  Block F: Common rinse failures
  Block G: Regulatory requirements summary
ZONE 6 -- RINSE WATER MONITORING + SAFETY (27.0"--32.5" / ~5.5")
  Block H: Monitoring and compliance
  Block I: Safety callout
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**BLOCK A -- Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Hard Chrome -- Stage 6 of 8 -- Post-Plate` -- 34 pt `#2EC4B6`. Y: 1.3".
**Tagline:** `Every drop of drag-out is hexavalent chromium. Recover it. Treat it. Document it. There is no other option.` -- 18 pt at 65%. X: 0.5", Y: 2.0", W: 15.0".

**BLOCK A2 -- Safety Banner:** Same as Poster #87 and #92. X: 15.5", Y: 1.3", W: 8.0".

---

### ZONE 2 -- Orientation Strip

Stage 6 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Hard chrome plate with Cr(VI) drag-out  -->  After: Clean chrome surface ready for HE bake`

---

### ZONE 3 -- Multi-Stage Rinse Cascade Hero

**Section label:** `THE POST-CHROME RINSE -- RECOVERY AND DECONTAMINATION` -- Y: 4.4". Barlow Condensed ExtraBold, 26 pt, `#F0EDE8`.

**BLOCK B -- Rinse Cascade Diagram**

Y: 5.0" to 10.5". Four tank rectangles.

- Tank 1 -- Drag-Out Recovery (X: 0.5", W: 5.25", H: 5.0"): fill `#252B3D`, border 2 pt `#E8A020`
  - Title: `DRAG-OUT RECOVERY` Barlow SemiBold 15 pt `#E8A020`
  - Parameters (JetBrains Mono 12 pt `#F0EDE8`):
    ```
    Type: Static
    Purpose: Capture concentrated CrO3
    Return: To chrome bath periodically
    CONTAINS: Cr(VI) -- handle as hazardous
    ```

- Tank 2 -- Rinse 1 (X: 6.25", W: 5.25", H: 5.0"): fill `#252B3D`, border 2 pt `#2EC4B6`
  - Title: `RINSE 1` Barlow SemiBold 15 pt `#2EC4B6`
  - `Overflow counterflow`

- Tank 3 -- Rinse 2 (X: 12.0", W: 5.25", H: 5.0"): fill `#252B3D`, border 2 pt `#2EC4B6`
  - Title: `RINSE 2` Barlow SemiBold 15 pt `#2EC4B6`
  - `Overflow counterflow`

- Tank 4 -- Rinse 3 / Final (X: 17.75", W: 5.75", H: 5.0"): fill `#252B3D`, border 2 pt `#27AE60`
  - Title: `RINSE 3 (FINAL)` Barlow SemiBold 15 pt `#27AE60`
  - `Fresh water in; DI for precision`
  - Tag: `Parts exit --> HE bake` `#27AE60`

All rinse water arrows labeled: `ALL RINSE WATER --> Cr(VI) REDUCTION TREATMENT` Inter Medium 12 pt `#E05C5C`.

**BLOCK C -- Cr(VI) Wastewater Treatment Callout**

Y: 11.0" to 14.3".

Rounded rect, full width, H: 3.0", fill `#E05C5C` at 10%, border 2 pt `#E05C5C`, radius 8.
Title: `Cr(VI) WASTEWATER TREATMENT -- MANDATORY` Barlow Condensed ExtraBold, 22 pt, `#E05C5C`

Two-step process:

| Step 1: REDUCTION | Step 2: PRECIPITATION |
|---|---|
| Reduce Cr(VI) to Cr(III) | Precipitate Cr(OH)3 |
| Chemical: Na2S2O5 (sodium metabisulfite) or FeSO4 | Raise pH to 8--9 with NaOH |
| pH: < 3.0 during reduction | Cr(III) precipitates as green hydroxide |
| Time: 15--30 min mixing | Filter or settle; sludge is hazardous waste |

- Bottom: `EPA discharge limit: 0.5 mg/L total Cr daily max; 0.2 mg/L monthly average (40 CFR 433)` JetBrains Mono 12 pt `#E05C5C`

---

### ZONE 4 -- Drag-Out Reduction + Rinse Parameters

**Section label:** `REDUCING DRAG-OUT AND RINSE PARAMETERS` -- Y: 14.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK D -- Drag-Out Reduction Methods**

Y: 15.3" to 17.8".

Rounded rect, fill `#1E2435`, left accent `#E8A020`, W: 23.0".
Title: `MINIMIZING Cr(VI) DRAG-OUT` Barlow SemiBold 16 pt `#E8A020`

Body (Inter Regular 13 pt `#F0EDE8`, line height 155%):
- `Fume suppressants: Reduce surface tension; reduce misting AND drag-out. Use PFAS-free fluorosurfactants.`
- `Drain time: Allow parts to drain 10--30 sec over the chrome bath before transfer.`
- `Slow withdrawal: Reduce withdrawal speed from the bath to minimize film thickness on parts.`
- `Air knife/blow-off: Blow excess solution back into the chrome tank (in enclosed area).`
- `Recovery tank design: Heated recovery tank (140 F) evaporates water, concentrating returns.`

**BLOCK E -- Rinse Parameter Table**

Y: 18.2" to 20.3".

| Parameter | Value |
|---|---|
| Rinse configuration | Drag-out recovery + double or triple counterflow |
| Water temperature | Ambient (tanks 1--3); DI for final |
| Target conductivity (final tank) | < 50 uS/cm for precision parts |
| Immersion time per tank | 30--60 sec |
| All rinse water goes to | Cr(VI) reduction + hydroxide precipitation |
| Key regulatory concern | Total Cr < 0.5 mg/L discharge; Cr(VI) must be fully reduced |

---

### ZONE 5 -- Common Failures + Regulatory

**Two-column layout (Y: 20.7" to 26.8"):**

**Left -- Common Failures (X: 0.5", W: 14.0"):**

Section label: `WHAT GOES WRONG` Barlow Condensed ExtraBold 20 pt `#F0EDE8`.

| Failure | Root Cause | Result |
|---|---|---|
| Cr(VI) exceeds discharge limit | Inadequate reduction; rinse water bypass | EPA violation; fines; potential criminal liability |
| Chrome staining on parts | Insufficient rinsing; parts sat in drag-out | Visible yellow-orange stain under inspection |
| Recovery tank contaminated | Iron or tramp metal fell into recovery | Contaminated solution returned to chrome bath |
| No drag-out recovery | Tank skipped or decommissioned | 2--5x higher chrome consumption; waste treatment overload |
| Parts corrode between rinse and bake | Slow transfer; sat in wet state | Flash rust or oxidation before HE bake |

**Right -- Regulatory Summary (X: 15.5", W: 8.0"):**

Section label: `REGULATORY` Barlow Condensed ExtraBold 18 pt `#E05C5C`.

Rounded rect, fill `#E05C5C` at 10%, border 1 pt `#E05C5C`:

| Regulation | Requirement |
|---|---|
| OSHA 29 CFR 1910.1026 | PEL 5 ug/m3 Cr(VI); worker protection |
| EPA 40 CFR 63 Subpart N | NESHAP for hard chrome; emission limits |
| EPA 40 CFR 433 | Metal finishing effluent limits |
| RCRA (D007) | Cr waste is hazardous waste |
| State/local | May be stricter than federal |

JetBrains Mono 10 pt `#F0EDE8`.

---

### ZONE 6 -- Monitoring + Safety

**Two-column layout (Y: 27.2" to 32.3"):**

**Left -- Rinse Water Monitoring (X: 0.5", W: 14.0"):**

Section label: `RINSE WATER MONITORING` Barlow Condensed ExtraBold 20 pt `#F0EDE8`.

Callout box, fill `#1E2435`, left accent `#2EC4B6`:
- `Conductivity meters: Install in rinse tanks 2 and 3. Rising conductivity = rising Cr carry-through.`
- `Cr(VI) spot test: Diphenylcarbazide (DPC) test for Cr(VI) in final rinse. Any positive = inadequate rinsing.`
- `Total Cr in effluent: AA or colorimetric. Test daily during production.`
- `Record keeping: Log all Cr(VI) reduction batch treatments and discharge analyses. Regulatory inspectors will ask.`

Inter Regular 13 pt `#F0EDE8`.

**Right -- Safety (X: 15.5", W: 8.0"):**

- Rounded rect, fill `#E05C5C` at 15%, border 2 pt `#E05C5C`, radius 8
- Title: `SAFETY` Barlow Condensed ExtraBold 18 pt `#E05C5C`
- Body (Inter Regular 12 pt `#F0EDE8`):

> - ALL rinse water contains Cr(VI) until proven otherwise.
> - Splashes: flush skin with water immediately. Cr(VI) penetrates skin rapidly.
> - Chrome ulcers: Cr(VI) creates characteristic painless ulcers on skin. Report immediately.
> - PPE: acid-resistant gloves, splash goggles, face shield, rubber apron.
> - Mist: rinse area should have local exhaust ventilation.
> - Spills: contain and treat as hazardous waste.

---

### ZONE 7 -- Footer

Standard footer. Title: `Rinse -- Hard Chrome -- Post-Plate`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Hard chrome rinse water contains hexavalent chromium -- a known human carcinogen and EPA hazardous waste. All discharge must comply with OSHA, EPA (40 CFR 433), and state/local regulations. Consult your waste treatment provider and regulatory authority.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table (see Poster #87).
**Export:** Six files -- `Rinse Hard Chrome Post-Plate -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the most regulatory-heavy poster in the entire series. The Cr(VI) wastewater treatment callout (Block C) is the educational centerpiece -- many shop floor personnel don't understand WHY rinse water can't go down the drain. The two-step reduction + precipitation process must be crystal clear.

The four-tank rinse cascade is more tanks than any other rinse poster in the series. This is intentional: chrome bath drag-out is heavy (high surface tension), and multi-stage rinsing is the only way to reduce Cr(VI) carry-through to acceptable levels.

Watson's brief: "Post-plate rinse: CRITICAL. Chrome bath dragout contains hexavalent chromium -- a regulated carcinogen." "EPA discharge limit: 0.5 mg/L total Cr (daily max); 0.2 mg/L monthly average (40 CFR 433)."

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #93 -- Construction Workup v1.0*
*2026-04-26*
