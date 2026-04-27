---
Project: Plating Posters Inc
Poster Number: 177
Title: "Rinse -- Chromate Conversion (Hex) -- Pre-Deox"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster CC-04 technical reference (hexavalent chromate conversion coating on aluminum)"
Process Scope: Pre-deoxidize rinse stage for hexavalent chromate conversion coating on aluminum (Stage 2 of 7)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ChromateConversion
  - Hexavalent
  - Aluminum
  - Rinse
  - ConstructionWorkup
  - ClusterCC04
---

# Poster #177 -- Construction Workup
## Rinse -- Chromate Conversion (Hex) -- Pre-Deox

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 2 of 7. This rinse removes alkaline cleaner residues before the acid deoxidize step. Alkaline carryover into the deoxidizer neutralizes the acid and reduces its effectiveness. The aerospace standard is a double rinse (two immersion tanks). DI or RO water is preferred because chloride and sulfate contamination in the rinse water can cause pitting on aluminum -- a defect that no amount of downstream processing can fix.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Rinse stage diagram (Block B -- HERO):** Double-rinse cross-section showing aerospace-standard two-tank setup.
2. **Water quality panel (Block D):** DI/RO requirement, chloride/sulfate limits, pitting risk.
3. **Double rinse rationale (Block E):** Why aerospace mandates two tanks.
4. **Monitoring table (Block F):** Rinse quality control parameters.

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
  Stage 2 highlighted (Teal)
ZONE 3 -- RINSE MECHANISM HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- WATER QUALITY FOR ALUMINUM (14.5"--20.5" / ~6.0")
ZONE 5 -- DOUBLE RINSE + PITTING RISK (20.5"--26.5" / ~6.0")
ZONE 6 -- MONITORING & TROUBLESHOOTING (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Chromate Conversion (Hex) -- Pre-Deoxidize Rinse -- Stage 2 of 7` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Chlorides in rinse water pit aluminum. Alkaline carryover poisons the deoxidizer. Double rinse with DI or RO water is the aerospace standard for a reason.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 2 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Alkaline-wet aluminum surface  -->  After: Neutral, contaminant-free surface ready for acid deoxidize`

Cr(VI) warning badge (right): `Cr(VI) PROCESS -- SEE SAFETY NOTE` `#E05C5C`

---

### ZONE 3 -- Rinse Mechanism Hero

**Section label:** `THE PRE-DEOXIDIZE RINSE -- AEROSPACE STANDARD` -- Y: 4.4".

**BLOCK B -- Double Rinse Diagram (Y: 5.0" to 14.0")**

Two immersion tanks side by side:

**Tank 1 -- First Rinse (X: 1.0", W: 10.0", Y: 6.0", H: 5.0"):**
- Rounded rect, fill `#2EC4B6` at 8%, border 2 pt `#2EC4B6`
- Label: `RINSE TANK 1` Barlow SemiBold 14 pt `#2EC4B6`
- Part entering from left with alkaline residue
- `Removes bulk cleaner drag-out` Inter Regular 13 pt `#F0EDE8`

**Tank 2 -- Second Rinse (X: 13.0", W: 10.0", Y: 6.0", H: 5.0"):**
- Rounded rect, fill `#2EC4B6` at 15%, border 2 pt `#2EC4B6`
- Label: `RINSE TANK 2 (DI/RO PREFERRED)` Barlow SemiBold 14 pt `#2EC4B6`
- Part exiting right, clean
- `Final cleaner removal; spot-free surface` Inter Regular 13 pt `#27AE60`

**Key parameters (Y: 12.0"):**
- `Temperature: Ambient to 80 F (27 C)` JetBrains Mono 14 pt `#F0EDE8`
- `Water type: DI or RO water preferred (aerospace)` JetBrains Mono 14 pt `#E8A020`
- `Chloride: < 50 ppm` JetBrains Mono 14 pt `#E8A020`
- `Sulfate: < 50 ppm` JetBrains Mono 14 pt `#E8A020`
- `Double immersion rinse is standard for aerospace processing` Inter Medium 13 pt `#2EC4B6`

**Bottom callout (Y: 13.0"):**
- `CHLORIDES AND SULFATES IN RINSE WATER CAUSE PITTING ON ALUMINUM. This damage is permanent. No downstream step can repair it.` Inter Medium 14 pt `#E05C5C`

---

### ZONE 4 -- Water Quality for Aluminum

**Section label:** `WATER QUALITY -- ALUMINUM IS NOT STEEL` -- Y: 14.7".

**BLOCK D -- Water Quality Panel (Y: 15.3" to 20.3")**

**Left -- DI/RO Requirement (X: 0.5", W: 11.0"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `WATER QUALITY REQUIREMENTS` Barlow SemiBold 20 pt `#E8A020`

| Parameter | Target | Why |
|---|---|---|
| Conductivity | < 200 uS/cm | Lower = fewer dissolved contaminants |
| Chloride | < 50 ppm | Chloride pits aluminum |
| Sulfate | < 50 ppm | Sulfate attacks aluminum grain boundaries |
| pH | < 9.0 after rinse | Alkaline residue indicator |
| Type | DI or RO preferred | Municipal water often exceeds Cl-/SO4 limits |

Note: `Tap water may be acceptable for non-aerospace work if chloride and sulfate are confirmed low. Test your supply.` Inter Regular 12 pt `#F0EDE8` at 60%.

**Right -- Aluminum vs. Steel Rinse Comparison (X: 12.0", W: 11.5"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#2EC4B6` 0.06"
- Title: `ALUMINUM IS MORE SENSITIVE` Barlow SemiBold 20 pt `#2EC4B6`

| Factor | Steel (Phosphate) | Aluminum (Chromate) |
|---|---|---|
| Rinse stages | 1--2 | 2 (mandatory aerospace) |
| Water type | Tap is usually fine | DI/RO preferred |
| Chloride sensitivity | Low | HIGH -- causes pitting |
| Sulfate sensitivity | Low | MODERATE -- grain boundary attack |
| Consequence of poor rinse | Uneven coating | Pitting (irreversible) |

---

### ZONE 5 -- Double Rinse + Pitting Risk

**Two-column layout (Y: 20.7" to 26.3"):**

**Left -- Why Double Rinse? (X: 0.5", W: 11.0"):**

Section label: `DOUBLE RINSE RATIONALE` Barlow Condensed ExtraBold 22 pt `#27AE60`.

Rounded rect, H: 5.0", fill `#1E2435`, left accent `#27AE60` 0.06".

Content:
- `Aerospace processing specifications (AMS 2473, MIL-DTL-5541F) require double rinse stages at every transition.` Inter Regular 14 pt `#F0EDE8`
- `Why:` Barlow SemiBold 14 pt `#27AE60`
- `Single rinse leaves ~10% drag-out contamination on surface` Inter Regular 13 pt `#F0EDE8`
- `Double rinse reduces to < 1%` Inter Regular 13 pt `#27AE60`
- `Alkaline carryover into acid deoxidizer neutralizes acid and reduces effectiveness` Inter Regular 13 pt `#F0EDE8`
- `Contaminated deox produces uneven smut removal` Inter Regular 13 pt `#F0EDE8`
- `Result: uneven chromate coating = reject` Inter Medium 13 pt `#E05C5C`

**Right -- Pitting -- The Permanent Defect (X: 12.0", W: 11.5"):**

Section label: `PITTING ON ALUMINUM` Barlow Condensed ExtraBold 22 pt `#E05C5C`.

Rounded rect, H: 5.0", fill `#1E2435`, left accent `#E05C5C` 0.06".

Content:
- `Pitting caused by chloride or sulfate contamination in rinse water:` Inter Regular 14 pt `#F0EDE8`
- `Mechanism: Cl- ions penetrate the aluminum oxide film and initiate localized corrosion cells` Inter Regular 13 pt `#F0EDE8`
- `Appearance: Small, bright pits visible under magnification; sometimes visible to naked eye` Inter Regular 13 pt `#F0EDE8`
- `Effect on chromate: Chromate covers the pits but does not fill them -- corrosion initiates under the coating` Inter Regular 13 pt `#E05C5C`
- `PITTING IS IRREVERSIBLE. Once pitted, the part must be rejected.` Barlow SemiBold 14 pt `#E05C5C`
- `Prevention: DI/RO water in all aluminum rinse stages.` Inter Medium 14 pt `#27AE60`

---

### ZONE 6 -- Monitoring & Troubleshooting

**Section label:** `RINSE MONITORING` -- Y: 26.7".

**BLOCK F -- Control Table (Y: 27.3" to 30.5")**

| Parameter | Method | Frequency | Target |
|---|---|---|---|
| Conductivity | Conductivity meter | Every 4 hours | < 200 uS/cm |
| pH | pH meter | Every 4 hours | < 9.0 |
| Chloride | Ion test strip or lab | Weekly | < 50 ppm |
| Sulfate | Ion test strip or lab | Weekly | < 50 ppm |
| Overflow rate | Flow meter | Continuous | Per system design |

**BLOCK F2 -- Quick Troubleshooting (Y: 31.0" to 32.3")**

| Problem | Cause | Fix |
|---|---|---|
| Pitting on aluminum after rinse | Chloride/sulfate in water | Switch to DI/RO; test water supply |
| Uneven deox downstream | Alkaline carryover from poor rinse | Increase overflow; verify double rinse |

---

### ZONE 7 -- Footer

Standard Cr(VI) footer.

**Disclaimer:**
> This poster is an educational reference tool. Hexavalent chromium (Cr6+) is a known human carcinogen. Process parameters shown are typical industry values per MIL-DTL-5541F Type I. Specific formulations vary by product. Consult your process supplier and safety data sheets. Follow all applicable OSHA, EPA, and local regulations.

Title: `Rinse -- Chromate Conversion (Hex) -- Pre-Deox`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Chromate Conversion Hex Pre-Deox -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The pitting warning is what makes this rinse poster more than generic. Aluminum pitting from chloride contamination is a real, permanent, costly defect -- and it starts at the rinse stage that most operators consider the simplest part of the line. The aluminum vs. steel comparison in Zone 4 is important context for operators transitioning from steel phosphate to aluminum chromate work. The double rinse rationale gives aerospace operators the spec-backed justification they need to maintain (and defend) their rinse systems.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #177 -- Construction Workup v1.0*
*2026-04-26*
