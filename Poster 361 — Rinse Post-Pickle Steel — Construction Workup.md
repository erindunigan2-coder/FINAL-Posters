---
Project: Plating Posters Inc
Poster Number: 361
Title: "Rinse -- Post-Pickle (Carbon Steel)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Chemical Treatment Clusters -- Watson Research Brief (CT-3.5)"
Technical Source: Industry-standard rinse protocols after acid pickling of carbon steel. Covers rinse staging, pH monitoring, conductivity targets, drag-out recovery, and neutralizing rinse options.
Process Scope: Post-pickle rinse for carbon steel
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - AcidPickling
  - CarbonSteel
  - Rinse
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT03
---

# Poster #361 -- Construction Workup
## Rinse -- Post-Pickle (Carbon Steel)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Rinse posters can feel mundane, but bad rinsing after pickle is one of the top three causes of plating defects. This poster earns its wall space by making the case that rinsing is not "just water" -- it is an engineered process with measurable targets. The hero is a rinse stage flow diagram showing drag-out capture, counterflow staging, and optional neutralizing rinse. A monitoring targets panel gives operators actual numbers to chase.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Rinse stage flow (Block B -- HERO):** 3-4 stage horizontal flow (drag-out still rinse -> counterflow 1 -> counterflow 2 -> optional neutralize).
2. **Monitoring targets panel (Block D):** Quick-reference parameter targets.
3. **Drag-out recovery callout (Block E):** Economics and technique.
4. **Neutralizing rinse section (Block F):** When and why to use NaHCO3.
5. **Print size -- 24x36".**

---

## Part 2 -- Document Setup Instructions

(Same as Poster #357: 24x36", `#1A1F2E` background, standard fonts, standard palette.)

### Step 5 -- Set ruler guides

**Horizontal guides:**
- 0.5" / 2.9" / 14.5" / 21.0" / 27.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- RINSE STAGE FLOW / HERO (2.9"--14.5" / ~11.6" tall)
  Block B: Rinse stage flow diagram (4 stages horizontal)
  Block C: Timing callout banner

ZONE 3 -- MONITORING TARGETS (14.5"--21.0" / ~6.5" tall)
  Block D: Rinse quality monitoring table

ZONE 4 -- DRAG-OUT RECOVERY (21.0"--27.5" / ~6.5" tall)
  Block E: Drag-out recovery callout + economics

ZONE 5 -- NEUTRALIZING RINSE (27.5"--32.5" / ~5.0" tall)
  Block F: Neutralizing rinse reference

ZONE 6 -- FOOTER BAND (32.5"--36.0" / ~3.5" tall)
  Block G: Disclaimer + poster title + series name + logo + version
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**BLOCK A -- Headline**
- Barlow Condensed ExtraBold, 88 pt, `#F0EDE8`, letter spacing -4
- Text: `RINSE -- POST-PICKLE`

**BLOCK A -- Subheading**
- Barlow SemiBold, 36 pt, `#2EC4B6` (Teal)
- Text: `Carbon Steel -- Stop the Acid Before It Stops You`

**BLOCK A -- Tagline**
- Barlow SemiBold, 22 pt, `#F0EDE8` at 65%
- Text: `Acid that dries on the surface causes flash rust, staining, and plating adhesion failures. Rinse immediately, rinse thoroughly.`

---

### ZONE 2 -- Rinse Stage Flow (HERO)

**Section label:**
- Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `RINSE SEQUENCE -- FROM PICKLE TANK TO NEXT STEP`

---

**BLOCK B -- Four-Stage Rinse Flow**

Y: 3.8" to 12.5". Four boxes in a horizontal row with arrows.

Each flow box: Rounded rect, W: 5.0", H: 8.0", fill `#1E2435`, radius 8, top accent 4 pt.

| Stage | Box | X | Top Accent | Title |
|---|---|---|---|---|
| Drag-Out (Still Rinse) | Box 1 | 0.5" | `#E8A020` | `DRAG-OUT RINSE` |
| Counterflow Rinse 1 | Box 2 | 6.0" | `#2EC4B6` | `COUNTERFLOW 1` |
| Counterflow Rinse 2 | Box 3 | 11.5" | `#2EC4B6` | `COUNTERFLOW 2` |
| Neutralize (Optional) | Box 4 | 17.0" | `#E8A020` | `NEUTRALIZE` |

Arrows: 3 pt, `#3A4055`, filled right arrowhead.

**Box 1 -- Drag-Out (Still Rinse):**
- Badge: `STAGE 1`, fill `#E8A020`
- Name: `Drag-Out Rinse` / Subtitle: `Still Tank`
- Parameters:
```
Ambient temperature
No water flow (still)
Captures 50--70% of drag-out acid
```
- Purpose: `Recover acid chemistry; reduce waste`
- Check: `Return to pickle tank when iron level permits` (`#27AE60`)

**Box 2 -- Counterflow Rinse 1:**
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Running Rinse` / Subtitle: `First Stage`
- Parameters:
```
Ambient, flowing water
City or DI water
Continuous overflow to drain
```
- Purpose: `Dilute remaining acid`
- Check: `pH should be rising toward neutral`

**Box 3 -- Counterflow Rinse 2:**
- Badge: `STAGE 3`, fill `#2EC4B6`
- Name: `Running Rinse` / Subtitle: `Final Stage`
- Parameters:
```
Ambient, flowing water
Cleanest water in series
Target: pH 4.0--7.0
```
- Purpose: `Final acid removal`
- Check: `pH below 4.0 = insufficient rinsing -- increase flow`

**Box 4 -- Neutralize (Optional):**
- Badge: `OPTIONAL`, fill `#E8A020`
- Name: `Neutralizing Rinse`
- Parameters:
```
1--3% NaHCO3 (sodium bicarbonate)
Ambient, 30--60 sec
Followed by clean water rinse
```
- Purpose: `Neutralize acid in crevices, threads, blind holes`
- Check: `Critical for complex geometry parts` (`#E8A020`)

**BLOCK C -- Timing Callout Banner**

Y: 12.8" to 14.3"
- Rounded rect, X: 0.5", W: 23.0", H: 1.2", fill `#E05C5C` at 12%, border 2 pt `#E05C5C`, radius 6
- Title: `TIMING IS EVERYTHING` -- Barlow SemiBold, 20 pt, `#E05C5C`
- Body: `Steel begins to flash rust in 5--15 minutes in humid shop air. Parts must proceed to the next process step (activation, plating) without delay. If delay is unavoidable, hold parts in dilute acid (1--3% HCl or H2SO4) until ready.` -- Inter Regular, 14 pt, `#F0EDE8`

---

### ZONE 3 -- Monitoring Targets

**Section label:**
- Centered. Y: 14.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `RINSE QUALITY -- WHAT TO MEASURE`

---

**BLOCK D -- Monitoring Table**

Y: 15.5" to 20.8". Column widths (23.0" total):
- Parameter (5.5") | Target (5.5") | Method (6.0") | If Out of Spec (6.0")

Header row: fill `#3A4055`, H: 0.5".

| Parameter | Target | Method | If Out of Spec |
|---|---|---|---|
| Final rinse pH | 4.0--7.0 | pH meter or pH paper | < 4.0 = increase water flow or add rinse stage |
| Conductivity | < 200 microsiemens/cm | Conductivity meter | High conductivity = acid carry-through; increase flow |
| Visual | No acid film, no drying marks | Visual inspection | Streaks or drying = inadequate rinse volume or timing |
| Rinse water temp | Ambient to 40 C (104 F) | Thermometer | Warm rinse improves drying but not required |

Data: JetBrains Mono Regular, 13 pt. Parameter names: Inter Medium, 14 pt. Action column: Inter Regular, 13 pt, `#E8A020`.

---

### ZONE 4 -- Drag-Out Recovery

**Section label:**
- Centered. Y: 21.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `DRAG-OUT RECOVERY -- SAVE CHEMISTRY, SAVE MONEY`

---

**BLOCK E -- Drag-Out Callout**

- Rounded rect, X: 0.5", Y: 22.0", W: 23.0", H: 5.0", fill `#1E2435`, radius 6
- Left accent: `#27AE60`, 0.06"

Content (Inter Regular, 15 pt, `#F0EDE8`, line height 160%):

```
WHAT IS DRAG-OUT?
Parts leaving the pickle tank carry a film of acid solution on their surface.
Typical drag-out: 50--200 mL per square meter of part surface area.

WHY RECOVER IT?
A drag-out (still) rinse tank captures 50--70% of this acid chemistry.
Periodically return the drag-out rinse to the pickle tank to:
  - Extend acid bath life by 20--40%
  - Reduce acid purchases
  - Reduce wastewater treatment load

WHEN NOT TO RETURN:
If iron content in the drag-out rinse is already high, returning it
accelerates bath exhaustion. Monitor iron before returning.
```

Key numbers in JetBrains Mono, `#27AE60`: `50--200 mL/m2`, `50--70%`, `20--40%`.

---

### ZONE 5 -- Neutralizing Rinse

**Section label:**
- Centered. Y: 27.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`
- Text: `NEUTRALIZING RINSE -- WHEN TO USE IT`

---

**BLOCK F -- Neutralizing Rinse Reference**

- Rounded rect, X: 0.5", Y: 28.4", W: 23.0", H: 3.6", fill `#1E2435`, radius 6
- Left accent: `#E8A020`, 0.06"

Two-column layout inside:

Left column (when to use):
- Barlow SemiBold, 16 pt, `#E8A020`: `USE WHEN:`
- Inter Regular, 14 pt, `#F0EDE8`:
```
- Parts have blind holes, tubes, or crevices
- Threading or complex geometry traps acid
- Extended dwell before next process step
- Parts going to alkaline plating (acid residue kills the bath)
```

Right column (recipe):
- Barlow SemiBold, 16 pt, `#2EC4B6`: `RECIPE:`
- JetBrains Mono Regular, 14 pt, `#F0EDE8`:
```
1--3% sodium bicarbonate (NaHCO3)
Ambient temperature
30--60 seconds immersion
MUST be followed by clean water rinse
```

---

### ZONE 6 -- Footer Band

(Same structure as Poster #357.)

**Disclaimer:**
> This poster is an educational reference tool. Rinse parameters shown are typical industry values. Specific requirements vary by process specification and local discharge permits. Consult your process supplier and environmental compliance officer.

**Poster title:** `Rinse -- Post-Pickle (Carbon Steel)`

**Version:** `v1.0 -- 2026`

---

## Part 5 -- Grouping and Naming Convention

| Group Name | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline |
| Zone 2 - Rinse Flow | Section label, four flow boxes, arrows, timing banner |
| Zone 3 - Monitoring | Section label, monitoring targets table |
| Zone 4 - Drag-Out | Section label, drag-out recovery callout |
| Zone 5 - Neutralize | Section label, neutralizing rinse reference |
| Zone 6 - Footer | Footer band, disclaimer, title, series, logo, version |

---

## Part 6 -- Light Edition Color Remap Table

(Same remap table as Poster #357.)

---

## Part 7 -- Export Checklist

| File Name | Mode | Quality | Bleed |
|---|---|---|---|
| `Rinse Post-Pickle Steel -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Rinse Post-Pickle Steel -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Rinse Post-Pickle Steel -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Rinse Post-Pickle Steel -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Rinse Post-Pickle Steel -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Rinse Post-Pickle Steel -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

The "timing is everything" banner is this poster's emotional anchor. Flash rust in 5--15 minutes is something every plater has seen but few think about systematically. The drag-out recovery section gives operators a tangible cost savings argument -- 20--40% acid savings is real money on a high-volume line.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #361 -- Construction Workup v1.0*
*2026-04-26*
