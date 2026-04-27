---
Project: Plating Posters Inc
Poster Number: 51
Title: "Rinse -- Zinc-Nickel -- Pre-Plate"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-03 technical reference (zinc-nickel alloy plating)"
  - "Watson Research Brief -- Electroplating Clusters"
Technical Source: Pre-plate rinse between acid activation and zinc-nickel alloy plating bath. Prevents acid drag-in that crashes pH in the alkaline Zn-Ni bath. Double counterflow rinse is mandatory -- acid into alkaline Zn-Ni bath causes localized pH drop and alloy composition shift.
Process Scope: Pre-plate rinse for zinc-nickel plating (Stage 4 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ZincNickelPlating
  - Rinse
  - PrePlate
  - ConstructionWorkup
  - Series2
  - ClusterEP03
---

# Poster #51 -- Construction Workup
## Rinse -- Zinc-Nickel -- Pre-Plate

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 4 of 8. The pre-plate rinse for zinc-nickel is more critical than for plain zinc because the alkaline Zn-Ni bath operates at very high pH (>13 with NaOH at 100--150 g/L). Any acid drag-in from the HCl activation step causes a localized pH crash that shifts the Zn:Ni alloy ratio. The result: nickel-rich deposits in the drag-in zone (dark spots, variable corrosion performance) or zinc-rich deposits that fail salt spray.

Double counterflow rinse is mandatory for alkaline Zn-Ni. For acid Zn-Ni (pH 5.5--6.5), the acid tolerance is slightly higher, but drag-in still shifts alloy composition. Watson's brief states: "Dragout of acid into the alkaline ZnNi bath will cause localized pH drop and alloy composition shift."

Hero visual: rinse tank with pH impact diagram showing what happens when acid reaches the Zn-Ni bath.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Rinse tank hero (Block B):** Double counterflow rinse tank diagram with flow arrows and parameter callouts.
2. **pH impact diagram (Block C):** Visual showing acid drag-in path and its effect on the Zn-Ni bath -- pH crash, alloy shift.
3. **Alkaline vs. acid Zn-Ni rinse comparison (Block E):** Different rinse requirements depending on the bath type.
4. **Conductivity monitoring callout (Block D):** < 500 uS/cm target for alkaline bath; < 200 uS/cm preferred.
5. **Orientation strip:** Stage 4 highlighted.

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
ZONE 3 -- RINSE TANK HERO + pH IMPACT (4.2"--14.5" / ~10.3")
  Block B: Double counterflow rinse tank diagram
  Block C: pH impact visual -- acid drag-in path
ZONE 4 -- RINSE PARAMETERS + MONITORING (14.5"--20.5" / ~6.0")
  Block D: Rinse parameter table + conductivity monitoring
ZONE 5 -- ALKALINE VS. ACID Zn-Ni RINSE COMPARISON (20.5"--26.5" / ~6.0")
  Block E: Two-column comparison of rinse requirements
  Block F: Common rinse failures
ZONE 6 -- DRAG-OUT ECONOMICS + SAFETY (26.5"--32.5" / ~6.0")
  Block G: Drag-out recovery economics callout
  Block H: Safety callout
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Zinc-Nickel -- Stage 4 of 8 -- Pre-Plate` -- 34 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Acid into an alkaline Zn-Ni bath is not a drag-in problem -- it is an alloy composition problem. Double rinse. Every time.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Y: 2.9" to 4.2".

Eight mini-boxes in a horizontal row. Stage 4 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed: fill `#1E2435`, text `#F0EDE8` at 40%.

Below strip: `Before: Active, oxide-free surface with acid residue  -->  After: Clean, neutral surface ready for Zn-Ni alloy deposition`
- Inter Medium, 14 pt, `#F0EDE8` at 60%

---

### ZONE 3 -- Rinse Tank Hero + pH Impact

**Section label:** `THE PRE-PLATE RINSE -- PROTECTING THE ALLOY` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Double Counterflow Rinse Tank Diagram**

Y: 5.0" to 10.5".

- Two rounded rectangles representing Rinse Tank 1 and Rinse Tank 2 in counterflow arrangement.
- Rinse Tank 1 (X: 0.5", W: 11.0", H: 5.0"): fill `#252B3D`, border 2 pt `#2EC4B6`
  - Title: `RINSE TANK 1 (FIRST CONTACT)` Barlow SemiBold 18 pt `#2EC4B6`
  - Parameters (JetBrains Mono 14 pt `#F0EDE8`):
    ```
    Type: Overflow (cascade to drain)
    Temperature: Ambient (65--85 F)
    Water source: Municipal OK (< 500 uS/cm)
    Receives: Most of the acid drag-in
    ```
- Rinse Tank 2 (X: 12.5", W: 11.0", H: 5.0"): fill `#252B3D`, border 2 pt `#27AE60`
  - Title: `RINSE TANK 2 (FINAL CONTACT)` Barlow SemiBold 18 pt `#27AE60`
  - Parameters:
    ```
    Type: Overflow (fresh water in)
    Temperature: Ambient
    Water source: DI preferred for aerospace
    Parts exit: Ready for Zn-Ni bath
    ```
- Flow arrows: fresh water enters Tank 2 -> overflows to Tank 1 -> overflows to drain. Parts move Tank 1 -> Tank 2.

**BLOCK C -- pH Impact Visual**

Y: 11.0" to 14.3".

- Rounded rect, full width, H: 3.0", fill `#E05C5C` at 10%, border 2 pt `#E05C5C`, radius 8
- Title: `WHAT ACID DRAG-IN DOES TO THE ALKALINE Zn-Ni BATH` Barlow Condensed ExtraBold, 22 pt, `#E05C5C`
- Three-column impact chain:

| Acid enters bath | pH drops locally | Alloy shifts |
|---|---|---|
| HCl from activation drag-in | NaOH neutralized locally; pH drops from >13 to <12 | Low-pH zone deposits Ni-rich (>18% Ni); HCD areas go dark |

- Bottom line: `Result: Parts fail XRF alloy check. Salt spray drops. Rework or scrap.` Inter Medium 14 pt `#E05C5C`

---

### ZONE 4 -- Rinse Parameters + Monitoring

**Section label:** `RINSE PARAMETERS AND QUALITY MONITORING` -- Y: 14.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK D -- Parameter Table**

Y: 15.3" to 20.3".

| Parameter | Alkaline Zn-Ni Line | Acid Zn-Ni Line |
|---|---|---|
| Rinse stages | 2 minimum (double counterflow) | 1 minimum (single overflow) |
| Water temperature | Ambient | Ambient |
| Water quality | Municipal (< 500 uS/cm); DI for aerospace final | Municipal acceptable |
| Target conductivity (final tank) | < 200 uS/cm | < 500 uS/cm |
| Immersion time | 30--60 sec per tank | 30--60 sec |
| Agitation | Moderate -- parts dip or air sparging | Same |
| Key risk | HCl into NaOH bath = pH crash = alloy shift | Acid into pH 5.5--6.5 bath = mild pH shift |

Data: JetBrains Mono Regular 12 pt `#F0EDE8`. Headers: Barlow SemiBold 13 pt `#F0EDE8`.

**Conductivity monitoring callout (below table):**
- Rounded rect, W: 23.0", H: 0.8", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- Text: `Install a conductivity meter in the final rinse tank. Rising conductivity = rising drag-in = rising risk. Target < 200 uS/cm for alkaline Zn-Ni.` Inter Medium 13 pt `#27AE60`

---

### ZONE 5 -- Alkaline vs. Acid Zn-Ni + Common Failures

**Two-column layout (Y: 20.7" to 26.3"):**

**Left -- Why This Rinse Is Different (X: 0.5", W: 11.0"):**

Section label: `WHY THIS RINSE IS CRITICAL` Barlow Condensed ExtraBold 20 pt `#F0EDE8`.

Callout box, fill `#1E2435`, left accent `#E8A020`:
- Title: `ALKALINE Zn-Ni VULNERABILITY` Barlow SemiBold 16 pt `#E8A020`
- Body (Inter Regular 13 pt `#F0EDE8`, line height 155%):
  - `The alkaline Zn-Ni bath operates at NaOH 100--150 g/L (pH > 13).`
  - `Acid drag-in is immediately neutralized -- consuming NaOH, dropping local pH.`
  - `The Zn:Ni alloy ratio is pH-sensitive. Even a 0.5 pH-unit drop in the cathode film shifts the nickel percentage.`
  - `Acid Zn-Ni (pH 5.5--6.5) is more tolerant but still affected.`

**Right -- Common Rinse Failures (X: 12.5", W: 11.0"):**

Section label: `WHAT GOES WRONG` Barlow Condensed ExtraBold 20 pt `#F0EDE8`.

| Failure | Root Cause | Result |
|---|---|---|
| Single rinse instead of double | Cost-cutting or line layout | Acid drag-in exceeds bath buffering |
| Rinse water not flowing | Valve closed, flow meter broken | Rinse becomes contaminated sump |
| Parts sit in air between rinse and bath | Slow transfer, rack backup | Flash oxide forms; adhesion loss |
| Drag-out not recovered | No drag-out tank before rinse | Zn-Ni chemistry lost to drain; cost increase |

Cards: fill `#1E2435`, left accent `#E05C5C`. Failure: Barlow SemiBold 13 pt `#E05C5C`. Cause: Inter Regular 12 pt `#F0EDE8`. Result: Inter Medium 12 pt `#E8A020`.

---

### ZONE 6 -- Drag-Out Economics + Safety

**Two-column layout (Y: 26.7" to 32.3"):**

**Left -- Drag-Out Recovery Economics (X: 0.5", W: 14.0"):**

Section label: `DRAG-OUT RECOVERY -- THE BUSINESS CASE` Barlow Condensed ExtraBold 20 pt `#F0EDE8`.

Callout box, fill `#1E2435`, left accent `#27AE60`:
- Body (Inter Regular 13 pt `#F0EDE8`):
  - `Zn-Ni baths are expensive -- proprietary complexants, NaOH, nickel salts.`
  - `Triple rinse recommended: drag-out recovery tank + double counterflow.`
  - `The drag-out recovery tank captures concentrated Zn-Ni solution.`
  - `Periodically return this tank to the plating bath to recover chemistry.`
  - `ROI: pays for itself within months on a production barrel line.`

**Right -- Safety (X: 15.5", W: 8.0"):**

- Rounded rect, fill `#E05C5C` at 10%, border 1 pt `#E05C5C`, radius 8
- Title: `SAFETY` Barlow Condensed ExtraBold 20 pt `#E05C5C`
- Body (Inter Regular 13 pt `#F0EDE8`, line height 155%):

> - Rinse water may contain residual HCl -- handle as acidic.
> - Zinc-nickel drag-out contains nickel compounds (dermal sensitizer; IARC Group 2B).
> - Gloves (neoprene), goggles, apron required.
> - Rinse water drainage goes to waste treatment -- not sanitary sewer.

---

### ZONE 7 -- Footer

Standard footer. Title: `Rinse -- Zinc-Nickel -- Pre-Plate`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Process parameters shown are typical industry values for zinc-nickel alloy plating pre-plate rinse. Consult your process supplier for application-specific guidance.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table (see Poster #47).
**Export:** Six files -- `Rinse Zinc-Nickel Pre-Plate -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the rinse poster that hammers home the alkaline vulnerability. The pH impact visual in Zone 3 must make the connection visceral: acid + NaOH = pH crash = alloy shift = failed parts. The conductivity monitoring callout is the actionable takeaway -- shops that monitor rinse water conductivity catch drag-in problems before they reach the plating bath.

Watson's brief confirms: "Dragout of acid into the alkaline ZnNi bath will cause localized pH drop and alloy composition shift." For acid ZnNi, "single rinse after acid dip is acceptable if acid activation and bath share compatible chemistry."

---

*Alaina -- Plating Posters Inc Creative Lead*
*Poster #51 -- Construction Workup v1.0*
*2026-04-26*
