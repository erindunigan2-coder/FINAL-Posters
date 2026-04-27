---
Project: Plating Posters Inc
Poster Number: 276
Title: "EN Boron -- Main Tank"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters -- Watson Research Brief v1.1 (Process 8: EN-B, Poster 6)"
Technical Source: Industry-standard EN-B bath chemistry. DMAB and borohydride variants. ASTM B841. Deposit properties including hardness, friction, and wear data. EN-B vs. EN-P vs. hard chrome comparison. Watson domain expertise. Watson flagged deposition rates for Tyler spot-check.
Process Scope: Main tank -- EN-B plating bath (Stage 5 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ElectrolessNickelBoron
  - MainTank
  - ConstructionWorkup
  - Series2
  - ClusterEL08
---

# Poster #276 -- Construction Workup
## EN Boron -- Main Tank

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 5 of 8. This is the centerpiece poster of the EN-B cluster -- the plating bath itself. EN-B is the hardest electroless nickel variant: 700-850 HV as-plated, 1000-1300 HV heat-treated. It is a legitimate competitor to hard chrome for wear applications, without the hexavalent chromium. The poster must clearly present TWO EN-B bath chemistries side by side: DMAB-based (the commercial standard) and sodium borohydride-based (higher boron, higher hardness, more difficult to control). The EN-B vs. EN-P vs. hard chrome comparison is the educational core -- it is the single most important table for any engineer evaluating alternatives to hard chrome.

Design philosophy: dual-bath comparison as the hero, with the EN-B vs. EN-P vs. hard chrome comparison as the secondary anchor, bath stability management callout, and a troubleshooting strip.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Dual-bath comparison hero (Block B):** DMAB vs. borohydride -- two large side-by-side panels.
2. **EN-B vs. EN-P vs. hard chrome comparison (Block D):** The money table -- hardness, friction, corrosion, cost, environmental.
3. **Bath stability management (Block E):** DMAB decomposition risk, filtration, loading rules.
4. **Troubleshooting strip (Block F):** 4 common EN-B bath problems.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 5 highlighted (Emerald)
ZONE 3 -- DUAL-BATH COMPARISON HERO (4.2"--15.5" / ~11.3")
ZONE 4 -- EN-B vs. EN-P vs. HARD CHROME (15.5"--22.0" / ~6.5")
ZONE 5 -- BATH STABILITY MANAGEMENT (22.0"--28.5" / ~6.5")
ZONE 6 -- TROUBLESHOOTING STRIP (28.5"--32.5" / ~4.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `MAIN TANK` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `EN Boron -- Stage 5 of 8` -- 36 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `The hardest electroless nickel. 700-850 HV as-plated. 1000-1300 HV heat-treated. A legitimate hard chrome alternative -- without the hex chrome.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 5 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Rinsed, activated surface  -->  After: EN-B coated surface (Ni-B alloy, 0.5-8% B)`

---

### ZONE 3 -- Dual-Bath Comparison Hero

**Section label:** `TWO EN-B CHEMISTRIES -- DMAB vs. BOROHYDRIDE` -- Y: 4.4".

**BLOCK B -- DMAB vs. Borohydride**

Y: 5.0" to 15.0".

**Left -- DMAB Bath (X: 0.5", Y: 5.0", W: 11.0", H: 9.5"):**
- Rounded rect, fill `#1E2435`, top accent `#27AE60` 4 pt
- Title: `DMAB-BASED EN-B` Barlow SemiBold 20 pt `#27AE60`
- Subtitle: `Most Common Commercial` Barlow Condensed ExtraBold 14 pt `#F0EDE8` at 50%

**Reaction equation:**
- `Ni2+ + (CH3)2NHBH3 + H2O --> Ni0 + (CH3)2NH + H3BO3 + ...` JetBrains Mono 13 pt `#27AE60`

**Bath composition table:**

| Component | Concentration | Role |
|---|---|---|
| Nickel chloride (NiCl2 . 6H2O) or NiSO4 | 20-30 g/L Ni2+ | Metal ion source |
| DMAB ((CH3)2NHBH3) | 2-5 g/L | Reducing agent |
| Ethylenediamine (EDA) | 30-60 g/L | Primary complexant |
| NaOH | As needed | pH adjustment |
| Thallium acetate or lead acetate | 0.5-2 ppm | Stabilizer |
| Thiodiglycolic acid | 1-5 mg/L | Co-stabilizer |

**Operating parameters:**

| Parameter | Value |
|---|---|
| pH | 6.0-8.0 (mildly acidic to mildly alkaline) |
| Temperature | 60-75 C (140-167 F) |
| Ni concentration | 4-6 g/L Ni2+ |
| Deposition rate | 10-20 um/hr |
| Boron content | 0.5-3 wt% B |
| Bath life | 3-5 MTO |
| Loading | 0.2-0.5 dm2/L |

**Deposit properties:**

| Property | Value |
|---|---|
| Hardness (as-plated) | 700-800 HV |
| Hardness (HT 350-400 C / 1 hr) | 1000-1200 HV |
| Structure | Microcrystalline to amorphous |
| CoF (dry) | 0.08-0.12 |
| Solderability | Good |
| Salt spray (25 um) | 200-500 hours |

Data: JetBrains Mono 11 pt `#F0EDE8`. Labels: Inter Medium 11 pt `#F0EDE8` at 60%.

**Right -- Borohydride Bath (X: 12.0", Y: 5.0", W: 11.5", H: 9.5"):**
- Rounded rect, fill `#1E2435`, top accent `#E8A020` 4 pt
- Title: `BOROHYDRIDE-BASED EN-B` Barlow SemiBold 20 pt `#E8A020`
- Subtitle: `Higher Boron -- Higher Hardness -- Harder to Control` Barlow Condensed ExtraBold 14 pt `#F0EDE8` at 50%

**Reaction equation:**
- `Ni2+ + NaBH4 + ... --> Ni0 + B0 + ...` JetBrains Mono 13 pt `#E8A020`
- `(Complex multi-step mechanism)` Inter Regular 11 pt `#F0EDE8` at 60%

**Bath composition table:**

| Component | Concentration | Role |
|---|---|---|
| Nickel chloride (NiCl2 . 6H2O) | 20-30 g/L Ni2+ | Metal ion source |
| Sodium borohydride (NaBH4) | 0.5-1.5 g/L | Reducing agent |
| Ethylenediamine | 40-80 g/L | Complexant |
| NaOH | 40-90 g/L | pH control (strongly alkaline) |
| Thallium nitrate | 1-5 ppm | Stabilizer |

**Operating parameters:**

| Parameter | Value |
|---|---|
| pH | 12.0-14.0 (STRONGLY alkaline) |
| Temperature | 90-95 C (194-203 F) |
| Ni concentration | 4-6 g/L Ni2+ |
| Deposition rate | 20-30 um/hr |
| Boron content | 3-8 wt% B |
| Bath life | 2-4 MTO |
| Loading | 0.2-0.5 dm2/L |

**Deposit properties:**

| Property | Value |
|---|---|
| Hardness (as-plated) | 750-850 HV |
| Hardness (HT 350-400 C / 1 hr) | 1100-1300 HV |
| Structure | Amorphous |
| CoF (dry) | 0.05-0.10 |
| Solderability | Good |
| Salt spray (25 um) | 300-600 hours |

- Bottom warning: `NaBH4 is EXTREMELY flammable. Explosive H2 evolution on contact with acid. Strongly alkaline bath (pH 12-14). Full PPE required.` Inter Medium 12 pt `#E05C5C`

---

### ZONE 4 -- EN-B vs. EN-P vs. Hard Chrome

**Section label:** `THE COMPARISON THAT MATTERS -- EN-B vs. EN-P vs. HARD CHROME` -- Y: 15.7".

**BLOCK D -- Comparison Table (Y: 16.3" to 21.8")**

Full-width table. Column widths (23.0" total):
- Property (5.0") | EN-B (HT) (6.0") | EN High-P (HT) (6.0") | Hard Chrome (6.0")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.55".

| Property | EN-B (Heat-Treated) | EN High-P (Heat-Treated) | Hard Chrome |
|---|---|---|---|
| Hardness (HV) | 1000-1200 | 800-900 | 900-1100 |
| CoF (dry) | 0.05-0.12 | 0.10-0.15 | 0.12-0.16 |
| Corrosion (NSS, 25 um) | 200-500 hrs | 1,000+ hrs | 24-100 hrs (micro-cracked) |
| Wear resistance | Excellent | Good | Excellent |
| Thickness uniformity | Excellent (+/-1-2 um) | Excellent (+/-1-2 um) | Poor (build on edges/points) |
| Environmental concern | Low | Low | HIGH (Cr6+ chemistry) |
| Relative cost | High (DMAB) | Moderate | Low-moderate |
| Hex chrome? | No | No | YES -- IARC Group 1 carcinogen |

Data: JetBrains Mono 12 pt `#F0EDE8`. Property labels: Inter Medium 13 pt `#F0EDE8`.

**Bottom callout (Y: 21.0"):**
- Full width, fill `#27AE60` at 10%, border 1 pt `#27AE60`
- `EN-B: harder than hard chrome, lower friction, no hex chrome. The tradeoff: higher cost and lower corrosion resistance. Where wear matters more than corrosion, EN-B wins.` Inter Medium 14 pt `#27AE60`

---

### ZONE 5 -- Bath Stability Management

**Section label:** `BATH STABILITY -- THE EN-B CHALLENGE` -- Y: 22.2".

**BLOCK E -- Two Panels (Y: 22.9" to 28.3")**

**Left -- Decomposition Risk (X: 0.5", W: 11.0", H: 5.2"):**
- Rounded rect, fill `#1E2435`, left accent `#E05C5C` 0.06"
- Title: `DECOMPOSITION RISK` Barlow SemiBold 18 pt `#E05C5C`
- Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):
  - `DMAB decomposes slowly at operating temperature even without a catalytic surface`
  - `Bath must NOT idle at temp without parts or dummy load`
  - `DMAB baths are more susceptible to metallic contamination (Fe, Cu) than EN-P`
  - `Under-loaded baths (<0.1 dm2/L) are at highest decomposition risk`
  - `Decomposition is EXOTHERMIC -- can be violent`
  - `Black nickel powder + rapid gas evolution = fire/explosion hazard`
- Warning box:
  - Rounded rect, W: 10.0", H: 0.6", fill `#E05C5C` at 15%, border 1 pt `#E05C5C`
  - `NEVER leave EN-B bath at operating temperature without load` Inter Medium 13 pt `#E05C5C`

**Right -- Stability Rules (X: 12.0", W: 11.5", H: 5.2"):**
- Rounded rect, fill `#1E2435`, left accent `#27AE60` 0.06"
- Title: `STABILITY MANAGEMENT RULES` Barlow SemiBold 18 pt `#27AE60`
- Numbered list (Inter Regular 14 pt `#F0EDE8`, line height 155%):
  - `1. Cool bath to <40 C when not in use` JetBrains Mono 13 pt `#F0EDE8`
  - `2. Maintain stabilizer per supplier protocol` Inter Regular 14 pt `#F0EDE8`
  - `3. Filter continuously (1-5 um) -- remove metallic fines` Inter Regular 14 pt `#F0EDE8`
  - `4. Loading: 0.2-0.5 dm2/L optimal; <0.1 dm2/L = danger zone` JetBrains Mono 13 pt `#E8A020`
  - `5. Check stabilizer every shift -- do not rely on weekly analysis` Inter Regular 14 pt `#F0EDE8`
  - `6. Inspect heater elements -- hot spots nucleate decomposition` Inter Regular 14 pt `#F0EDE8`
  - `7. NiCl2 preferred over NiSO4 in many EN-B formulations` Inter Regular 14 pt `#F0EDE8`
  - `8. Borate accumulates as byproduct -- monitor viscosity` Inter Regular 14 pt `#F0EDE8`

---

### ZONE 6 -- Troubleshooting Strip

**Section label:** `QUICK TROUBLESHOOTING -- 4 COMMON EN-B BATH PROBLEMS` -- Y: 28.7".

**BLOCK F -- Four Problem Cards (Y: 29.4" to 32.3")**

Four cards in a single row. Gap: 0.33".

Each card: Rounded rect, W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | SKIP PLATING | Contaminated surface; poor activation; depleted DMAB | Improve cleaning; verify activation; replenish DMAB |
| 2 | 6.33" | BATH DECOMPOSITION | Idle at temp; low stabilizer; metallic contamination; under-loaded | Cool bath; check stabilizer; filter; maintain loading |
| 3 | 12.16" | ROUGH / NODULAR DEPOSIT | Particulate in bath; inadequate filtration; high MTO | Filter (1-5 um); check MTO; remove metallic fines |
| 4 | 18.0" | LOW HARDNESS | Boron content out of spec; low DMAB; temperature drift | Verify DMAB concentration; check temp; analyze B% by ICP |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 7 -- Footer

Standard footer. Title: `EN Boron -- Main Tank`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Process parameters shown are typical industry values for electroless nickel-boron (EN-B) plating baths. Specific formulations, concentrations, and process limits vary by proprietary product. Consult your process supplier for application-specific guidance. Source: General industry knowledge; ASTM B841. Watson flagged deposition rates for Tyler spot-check.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `EN Boron Main Tank -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the most technically dense poster in the EN-B cluster. The dual-bath comparison (DMAB vs. borohydride) is the hero -- operators need to understand the two variants and their tradeoffs. The EN-B vs. EN-P vs. hard chrome table in Zone 4 is the educational anchor of the entire cluster: it answers the question "why would I choose EN-B over EN-P or hard chrome?" in a single scannable table. The answer: EN-B offers the hardest deposit and lowest friction of any electroless nickel, exceeding hard chrome in both metrics, without hexavalent chromium. The tradeoff is cost (DMAB) and corrosion resistance (EN High-P still wins for corrosion). The bath stability callout is essential because EN-B decomposition risk is real and dangerous. Watson flagged deposition rates for Tyler spot-check -- these should be verified before final generation.

---

*Alaina -- Poster #276 -- Construction Workup v1.0 -- 2026-04-26*
