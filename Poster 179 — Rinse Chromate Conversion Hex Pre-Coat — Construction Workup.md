---
Project: Plating Posters Inc
Poster Number: 179
Title: "Rinse -- Chromate Conversion (Hex) -- Pre-Coat"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster CC-04 technical reference (hexavalent chromate conversion coating on aluminum)"
Process Scope: Pre-coat rinse stage for hexavalent chromate conversion coating on aluminum (Stage 4 of 7)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ChromateConversion
  - Hexavalent
  - Aluminum
  - Rinse
  - PreCoat
  - ConstructionWorkup
  - ClusterCC04
---

# Poster #179 -- Construction Workup
## Rinse -- Chromate Conversion (Hex) -- Pre-Coat

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 4 of 7. This rinse removes acid, dissolved metals (copper, iron, silicon), and fluoride residues from the deoxidize step before the chromate coating bath. Unlike the zinc phosphate "no rinse" situation, this rinse absolutely DOES exist and is critical. Acid carryover accelerates chromate bath consumption; dissolved metals (especially copper) contaminate the bath and cause dark, sooty coatings.

The time-critical element: aluminum re-oxidizes almost instantly in water. Minimize transit time between deoxidize rinse and chromate coating -- ideally less than 5 minutes. This creates an operational tension between "rinse thoroughly" and "move fast."

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Pre-coat rinse diagram (Block B -- HERO):** Double-rinse tank showing removal of acid, metals, and fluoride with a transit time countdown.
2. **What the rinse must remove (Block D):** Panel showing acid, dissolved Cu/Fe/Si, and fluoride contaminants.
3. **Time-critical transfer (Block E):** Re-oxidation visual and 5-minute window.
4. **Monitoring and troubleshooting (Block F):** Control parameters and failure modes.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 4 highlighted (Teal)
ZONE 3 -- PRE-COAT RINSE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- WHAT THE RINSE REMOVES (14.5"--20.5" / ~6.0")
ZONE 5 -- TIME-CRITICAL TRANSFER (20.5"--26.5" / ~6.0")
ZONE 6 -- MONITORING & TROUBLESHOOTING (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Chromate Conversion (Hex) -- Pre-Coat Rinse -- Stage 4 of 7` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Remove the acid, the dissolved metals, and the fluoride. Then move fast -- aluminum re-oxidizes in seconds, and you have less than 5 minutes to get parts into the chromate bath.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 4 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Acid-wet, freshly deoxidized aluminum  -->  After: Clean, active aluminum surface (5-minute window to chromate)`

Cr(VI) warning badge (right): `Cr(VI) PROCESS -- SEE SAFETY NOTE` `#E05C5C`

---

### ZONE 3 -- Pre-Coat Rinse Hero

**Section label:** `THE PRE-COAT RINSE -- CLEAN AND FAST` -- Y: 4.4".

**BLOCK B -- Double Rinse + Transit Timer (Y: 5.0" to 14.0")**

**Two tanks (double rinse standard):**

*Tank 1 (X: 1.0", W: 10.0", Y: 6.0", H: 4.5"):*
- Rounded rect, fill `#2EC4B6` at 8%, border 2 pt `#2EC4B6`
- Label: `RINSE TANK 1` Barlow SemiBold 14 pt `#2EC4B6`
- `Removes bulk acid and dissolved metals` Inter Regular 13 pt `#F0EDE8`

*Tank 2 (X: 13.0", W: 10.0", Y: 6.0", H: 4.5"):*
- Rounded rect, fill `#2EC4B6` at 15%, border 2 pt `#2EC4B6`
- Label: `RINSE TANK 2` Barlow SemiBold 14 pt `#2EC4B6`
- `Final acid removal; clean surface` Inter Regular 13 pt `#27AE60`

**Transit timer callout (Y: 11.0"):**
- Large rounded rect, W: 22.0", H: 2.0", fill `#E05C5C` at 10%, border 2 pt `#E05C5C`, centered
- `< 5 MIN` Barlow Condensed ExtraBold 48 pt `#E05C5C`, centered
- `Maximum transit time from deoxidize rinse to chromate coating bath` Inter Medium 16 pt `#F0EDE8`, centered
- `Aluminum re-oxidizes almost instantly in water. Fresh oxide reduces chromate coating quality.` Inter Regular 13 pt `#F0EDE8` at 70%, centered

**Key parameters (Y: 13.0"):**
- `Temperature: Ambient` JetBrains Mono 14 pt `#F0EDE8`
- `Method: Double immersion (standard)` JetBrains Mono 14 pt `#2EC4B6`
- `Must be thorough -- acid carryover accelerates chromate bath consumption` Inter Medium 13 pt `#E8A020`

---

### ZONE 4 -- What the Rinse Removes

**Section label:** `THREE CONTAMINANTS -- ALL MUST GO` -- Y: 14.7".

**BLOCK D -- Three Contaminant Cards (Y: 15.3" to 20.3")**

Three cards in a row:

**Card 1 -- Acid Residue (X: 0.5", W: 7.33"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `ACID RESIDUE` Barlow SemiBold 18 pt `#E8A020`
- `HNO3 and/or HF from deoxidizer` Inter Regular 14 pt `#F0EDE8`
- `If carried into chromate bath:` Inter Regular 13 pt `#F0EDE8`
- `Accelerates bath consumption` Inter Regular 13 pt `#E05C5C`
- `Disrupts pH control` Inter Regular 13 pt `#E05C5C`
- `Shortens bath life` Inter Regular 13 pt `#E05C5C`

**Card 2 -- Dissolved Metals (X: 8.16", W: 7.33"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E05C5C` 0.06"
- Title: `DISSOLVED METALS` Barlow SemiBold 18 pt `#E05C5C`
- `Copper, iron, silicon from alloy dissolution` Inter Regular 14 pt `#F0EDE8`
- `If carried into chromate bath:` Inter Regular 13 pt `#F0EDE8`
- `Copper causes dark/sooty coatings` Inter Regular 13 pt `#E05C5C`
- `Iron contaminates the bath` Inter Regular 13 pt `#E05C5C`
- `Leads to reject parts and bath dumps` Inter Regular 13 pt `#E05C5C`

**Card 3 -- Fluoride (X: 15.83", W: 7.67"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#2EC4B6` 0.06"
- Title: `FLUORIDE` Barlow SemiBold 18 pt `#2EC4B6`
- `From HF in deoxidizer` Inter Regular 14 pt `#F0EDE8`
- `If carried into chromate bath:` Inter Regular 13 pt `#F0EDE8`
- `Excess fluoride over-activates the chromate reaction` Inter Regular 13 pt `#E8A020`
- `Can cause powdery/chalky coating` Inter Regular 13 pt `#E8A020`
- `Some F- is desirable in chromate bath -- but controlled, not random drag-in` Inter Regular 12 pt `#F0EDE8` at 60%

---

### ZONE 5 -- Time-Critical Transfer

**Section label:** `THE RE-OXIDATION CLOCK` -- Y: 20.7".

**BLOCK E -- Two-Column Layout (Y: 21.3" to 26.3")**

**Left -- Why Time Matters (X: 0.5", W: 11.0"):**

Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E05C5C` 0.06".
Title: `ALUMINUM RE-OXIDIZES IN SECONDS` Barlow SemiBold 18 pt `#E05C5C`

Content:
- `The deoxidize step removes the natural Al2O3 oxide layer.` Inter Regular 14 pt `#F0EDE8`
- `The moment aluminum contacts air or water, a new oxide begins forming.` Inter Regular 14 pt `#F0EDE8`
- `Thick oxide = slower chromate reaction = thinner, less protective coating` Inter Medium 14 pt `#E05C5C`
- `Timeline:` Barlow SemiBold 14 pt `#F0EDE8`
- `0--30 sec: Minimal re-oxidation (ideal)` JetBrains Mono 12 pt `#27AE60`
- `1--5 min: Acceptable (still active)` JetBrains Mono 12 pt `#E8A020`
- `5--15 min: Significant oxide regrowth` JetBrains Mono 12 pt `#E05C5C`
- `> 15 min: May need to re-deoxidize` JetBrains Mono 12 pt `#E05C5C`

**Right -- Operational Best Practices (X: 12.0", W: 11.5"):**

Rounded rect, H: 4.8", fill `#1E2435`, left accent `#27AE60` 0.06".
Title: `BEST PRACTICES` Barlow SemiBold 18 pt `#27AE60`

Content:
- `Position rinse tanks as close to chromate bath as possible` Inter Regular 14 pt `#F0EDE8`
- `Process parts in small lots to minimize queue time` Inter Regular 14 pt `#F0EDE8`
- `Do not allow parts to air-dry between rinse and chromate` Inter Medium 14 pt `#E05C5C`
- `Keep parts wet (submerged in rinse) until ready to transfer` Inter Regular 14 pt `#F0EDE8`
- `If > 5 min elapsed: consider re-rinsing through deox rinse` Inter Regular 13 pt `#E8A020`
- `If > 15 min elapsed: re-deoxidize the parts` Inter Medium 13 pt `#E05C5C`

---

### ZONE 6 -- Monitoring & Troubleshooting

**Section label:** `PRE-COAT RINSE MONITORING` -- Y: 26.7".

**BLOCK F -- Control Table (Y: 27.3" to 30.0")**

| Parameter | Method | Frequency | Target |
|---|---|---|---|
| pH | pH meter | Every 4 hours | Neutral (6.0--8.0) |
| Conductivity | Conductivity meter | Every 4 hours | < 200 uS/cm |
| Dissolved metals | Lab analysis | Weekly | Cu < 5 ppm; Fe < 10 ppm |
| Fluoride | Ion electrode | Daily (if HF deox used) | < 10 ppm in rinse |
| Transfer time | Timer / observation | Every load | < 5 min |

**BLOCK F2 -- Quick Troubleshooting (Y: 30.5" to 32.3")**

| Problem | Cause | Fix |
|---|---|---|
| Dark/sooty chromate downstream | Copper drag-in from deox | Improve rinse; increase overflow; check dissolved Cu |
| Thin/patchy chromate | Re-oxidation (too slow transfer) | Speed up transfer; keep parts wet |
| Chromate bath pH rising | Acid carryover insufficient (pH-neutral rinse) | Normal -- adjust chromate bath pH per schedule |

---

### ZONE 7 -- Footer

Standard Cr(VI) footer.

Title: `Rinse -- Chromate Conversion (Hex) -- Pre-Coat`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Chromate Conversion Hex Pre-Coat -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The transit timer in the hero zone (< 5 MIN in 48 pt coral) is the attention-getter. This rinse poster has a built-in urgency that most rinse posters lack -- the re-oxidation clock is ticking from the moment the deoxidize step finishes. The three contaminant cards in Zone 4 give operators a clear mental model of WHAT they are removing and WHY each matters. The re-oxidation timeline in Zone 5 converts the abstract "move fast" instruction into a concrete time scale that operators can actually use.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #179 -- Construction Workup v1.0*
*2026-04-26*
