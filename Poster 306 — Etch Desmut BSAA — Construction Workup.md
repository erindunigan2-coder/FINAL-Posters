---
Project: Plating Posters Inc
Poster Number: 306
Title: "Etch / Desmut -- Boric-Sulfuric Acid Anodizing (BSAA)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 4, Sections 4.2--4.4)"
Process Scope: Caustic etch and acid desmut for BSAA anodizing -- Stages 3--4 of 8 (combined)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Anodizing
  - BSAA
  - TypeIC
  - Etch
  - Desmut
  - ConstructionWorkup
  - ClusterAnodize04
---

# Poster #306 -- Construction Workup
## Etch / Desmut -- Boric-Sulfuric Acid Anodizing (BSAA)

*Alaina -- Plating Posters Inc*
*v1.0 -- 2026-04-26*

Stages 3--4 of 8 (combined). Same pre-treatment as Type I: light caustic etch (30--60 sec) to minimize material removal and preserve fatigue life, followed by a chromate-free desmut. The critical difference from Type I: the desmut MUST be chromate-free. Using a chromic acid desmut before a BSAA anodize defeats the entire purpose of the chromate-free process. The concept hook: "Every step in the BSAA line must be Cr(VI)-free. If your desmut contains chromic acid, you haven't actually replaced Type I."

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Dual-tank hero (Block B):** Etch and desmut side by side -- same as Poster 290 but with Cr-free emphasis.
2. **Chromate-free desmut options table (Block D):** Side-by-side comparison of HNO3, ferric sulfate, and proprietary alternatives.
3. **Etch time control callout (Block E):** Short etch for fatigue retention.
4. **Smut character by alloy table (Block F).**
5. **Cr-free chain verification strip (Block G).**

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
  Stages 3 and 4 highlighted (Amber)
ZONE 3 -- ETCH + DESMUT DUAL-TANK HERO (4.2"--15.5" / ~11.3")
ZONE 4 -- CHROMATE-FREE DESMUT OPTIONS (15.5"--22.0" / ~6.5")
ZONE 5 -- SMUT TABLE + ETCH TIME CONTROL (22.0"--28.5" / ~6.5")
ZONE 6 -- DEFECT GRID + Cr-FREE CHAIN (28.5"--32.5" / ~4.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ETCH / DESMUT` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Boric-Sulfuric Acid Anodizing (BSAA) -- Stages 3 & 4 of 8` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Light etch for fatigue retention. Chromate-free desmut -- no exceptions. If your desmut contains Cr(VI), you haven't replaced Type I.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Eight-stage strip. Stages 3 and 4 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.

Below: `Before: Clean surface  -->  After: Etched, smut-free, activated aluminum ready for BSAA anodize`

---

### ZONE 3 -- Etch + Desmut Dual-Tank Hero

**Section label:** `TWO TANKS, BOTH Cr(VI)-FREE` -- Y: 4.4".

**Left -- Etch Tank (X: 0.5", Y: 5.0", W: 10.5", H: 9.5"):**

Tank body:
- Rounded rect, fill `#252B3D`, border 2 pt `#C8D0D8`
- Title: `CAUSTIC ETCH` Barlow SemiBold 20 pt `#E8A020`
- Subtitle: `(LIGHT -- 30--60 sec)` Barlow SemiBold 14 pt `#E8A020` at 60%

Parameter labels:
- `NaOH 22--45 g/L (3--6 oz/gal)` JetBrains Mono 14 pt `#F0EDE8`
- `130--150 F (55--66 C)` JetBrains Mono 14 pt `#E8A020`
- `30--60 sec (VERY SHORT)` JetBrains Mono 13 pt `#F0EDE8`

Fatigue callout (bottom of etch area, Y: 12.5"):
- Rounded rect, W: 10.0", H: 1.5", fill `#E8A020` at 12%, border 1 pt `#E8A020`
- Title: `WHY SHORT ETCH?` Barlow SemiBold 14 pt `#E8A020`
- `BSAA replaces Type I on fatigue-critical aerospace parts.` Inter Medium 12 pt `#F0EDE8`
- `Excessive etch removes material and introduces stress risers.` Inter Medium 12 pt `#F0EDE8`
- `Some specs require NO etch -- clean + desmut only.` Inter Medium 12 pt `#E8A020`

**Right -- Desmut Tank (X: 12.0", Y: 5.0", W: 11.5", H: 9.5"):**

Tank body:
- Rounded rect, fill `#252B3D`, border 2 pt `#C8D0D8`
- Title: `DESMUT / DEOXIDIZE` Barlow SemiBold 20 pt `#E8A020`
- Subtitle: `(CHROMATE-FREE ONLY)` Barlow SemiBold 14 pt `#27AE60`

Parameter labels:
- `HNO3 25--50% v/v (standard)` JetBrains Mono 14 pt `#F0EDE8`
- `or Ferric sulfate + H2SO4` JetBrains Mono 14 pt `#F0EDE8`
- `Ambient temp (60--85 F)` JetBrains Mono 13 pt `#F0EDE8`
- `15--60 sec (HNO3)` JetBrains Mono 13 pt `#F0EDE8`
- `2--10 min (ferric sulfate)` JetBrains Mono 12 pt `#F0EDE8` at 70%

Cr-free callout (bottom of desmut area, Y: 12.5"):
- Rounded rect, W: 11.0", H: 1.5", fill `#27AE60` at 12%, border 1 pt `#27AE60`
- Title: `NO CHROMIC ACID DESMUT` Barlow SemiBold 14 pt `#27AE60`
- `Chromic-sulfuric desmut (Na2Cr2O7 + H2SO4) is the legacy method.` Inter Medium 12 pt `#F0EDE8`
- `Using it before BSAA introduces Cr(VI) into the process chain.` Inter Medium 12 pt `#E05C5C`
- `Use HNO3 or ferric sulfate-based alternatives ONLY.` Inter Medium 12 pt `#27AE60`

---

### ZONE 4 -- Chromate-Free Desmut Options

**Section label:** `CHROMATE-FREE DESMUT OPTIONS` Barlow Condensed ExtraBold 22 pt `#F0EDE8`. Y: 15.7".

**BLOCK D -- Three-Option Comparison**

Y: 16.3" to 21.8". Three tall callout boxes:

**Option 1 -- Nitric Acid (X: 0.5", W: 7.33"):**
- Fill `#1E2435`, top accent 4 pt `#27AE60`
- Title: `NITRIC ACID (HNO3)` Barlow SemiBold 16 pt `#27AE60`
- Concentration: `25--50% v/v` JetBrains Mono 13 pt `#F0EDE8`
- Temperature: `Ambient` JetBrains Mono 12 pt `#F0EDE8`
- Time: `15--60 sec` JetBrains Mono 12 pt `#F0EDE8`
- Best for: `6061, 6063, 5052 (light smut)` Inter Regular 12 pt `#F0EDE8`
- Add HF: `1--3% for Cu/Si alloys (2024, 7075, cast)` Inter Regular 12 pt `#E8A020`
- Pros: `Fast, effective, widely available` Inter Regular 12 pt `#27AE60`
- Cons: `HF variant requires special PPE; NOx fumes` Inter Regular 12 pt `#E05C5C`

**Option 2 -- Ferric Sulfate (X: 8.33", W: 7.33"):**
- Fill `#1E2435`, top accent 4 pt `#2EC4B6`
- Title: `FERRIC SULFATE` Barlow SemiBold 16 pt `#2EC4B6`
- Concentration: `3--6 oz/gal Fe2(SO4)3 + 10--15% H2SO4` JetBrains Mono 12 pt `#F0EDE8`
- Temperature: `80--100 F (27--38 C)` JetBrains Mono 12 pt `#F0EDE8`
- Time: `2--10 min` JetBrains Mono 12 pt `#F0EDE8`
- Best for: `All alloys including high-Cu` Inter Regular 12 pt `#F0EDE8`
- Pros: `No HF needed; effective on 2024, 7075` Inter Regular 12 pt `#27AE60`
- Cons: `Slower; requires temperature control; iron buildup` Inter Regular 12 pt `#E05C5C`

**Option 3 -- Proprietary Cr-Free (X: 16.16", W: 7.33"):**
- Fill `#1E2435`, top accent 4 pt `#E8A020`
- Title: `PROPRIETARY Cr-FREE` Barlow SemiBold 16 pt `#E8A020`
- Concentration: `Per vendor TDS` JetBrains Mono 12 pt `#F0EDE8`
- Temperature: `Per vendor TDS` JetBrains Mono 12 pt `#F0EDE8`
- Time: `Per vendor TDS` JetBrains Mono 12 pt `#F0EDE8`
- Chemistry: `Peroxide, persulfate, or ferric-based formulations` Inter Regular 12 pt `#F0EDE8`
- Pros: `Designed for Cr-free lines; vendor support` Inter Regular 12 pt `#27AE60`
- Cons: `Higher cost; proprietary = vendor-dependent` Inter Regular 12 pt `#E05C5C`

---

### ZONE 5 -- Smut Table + Etch Time Control

**Two-column layout (Y: 22.2" to 28.3"):**

**Left -- Smut Character by Alloy (X: 0.5", W: 11.0"):**

Section label: `ALLOY SMUT TABLE` Barlow Condensed ExtraBold 20 pt `#F0EDE8`.

| Alloy | Smut | Recommended Desmut | Notes |
|---|---|---|---|
| **6061** | Light gray | HNO3 50% | Standard BSAA substrate |
| **5052** | Light gray | HNO3 50% | Good BSAA response |
| **2024** | Heavy (Cu) | HNO3 + HF or ferric sulfate | BSAA preferred over Type II for 2024 |
| **7075** | Moderate (Cu/Zn) | HNO3 + HF or ferric sulfate | BSAA works well on 7xxx |
| **1100** | Very light | HNO3 50% | Excellent |

Header: Barlow SemiBold 11 pt. Data: Inter Regular 12 pt, alternating rows.

**Right -- Etch Time vs. Fatigue (X: 12.0", W: 11.5"):**

Section label: `ETCH TIME AND FATIGUE LIFE` Barlow Condensed ExtraBold 20 pt `#F0EDE8`.

Callout box, fill `#1E2435`, left accent `#E8A020`:

Content (Inter Regular 13 pt `#F0EDE8`, line height 155%):
- `BSAA exists to replace Type I on fatigue-critical parts.`
- `Type I was chosen for these parts BECAUSE the thin coating minimizes stress concentration.`
- `Excessive etch adds a SECOND source of fatigue degradation: material removal creates stress risers in the substrate.`
- ``
- `GUIDELINES:` Inter Medium 13 pt `#E8A020`
- `-- Standard parts: 30--60 sec etch`
- `-- Fatigue-critical: 30 sec maximum or NO ETCH`
- `-- Per customer spec: follow the spec (some prohibit etch)`
- ``
- `If etch is skipped, the desmut step still removes native oxide and activates the surface. The BSAA oxide will form on a non-etched surface.`

---

### ZONE 6 -- Defect Grid + Cr-Free Chain

**Two-section layout (Y: 28.7" to 32.3"):**

**Top -- 4 Defect Cards (Y: 28.7" to 30.7"):**

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | POOR PAINT ADHESION | Incomplete smut removal; residual contamination | Improve desmut; verify Cr-free chemistry is effective |
| 2 | 6.33" | BARE SPOTS | Silicate from etch/desmut cross-contamination | Verify no silicates in any upstream chemistry |
| 3 | 12.16" | UNEVEN OXIDE | Uneven etch pattern | Improve etch agitation; verify NaOH concentration |
| 4 | 18.0" | Cr(VI) DETECTION | Chromic acid desmut contamination | REMOVE chromic acid desmut from line; decontaminate |

Each card: Rounded rect, W: 5.5", H: 1.8", fill `#1E2435`, radius 4, left accent 0.06" in color. Card 4 accent: `#E05C5C`.

**Bottom -- Cr-Free Chain Verification (Y: 31.0" to 32.3"):**

Rounded rect, full width, H: 1.2", fill `#27AE60` at 12%, border 1 pt `#27AE60`.

Title: `Cr(VI)-FREE CHAIN VERIFICATION` Barlow SemiBold 14 pt `#27AE60`

Horizontal chain: `Cleaner: Cr-FREE` --> `Etch: Cr-FREE (NaOH)` --> `Desmut: Cr-FREE (HNO3 or ferric)` --> `Anodize: Cr-FREE (H2SO4 + H3BO3)` --> `Seal: Cr-FREE (hot water or NiAc)`

Each step in a small rounded rect with check mark icon. All `#27AE60`.

---

### ZONE 7 -- Footer

Standard. Title: `Etch / Desmut -- Boric-Sulfuric Acid Anodizing (BSAA)`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Etch and desmut procedures are the same as for conventional anodizing, with the CRITICAL requirement that all chemistries be chromate-free. HF is extremely hazardous -- follow all OSHA requirements. Consult your process supplier.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Etch Desmut BSAA -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The hero message of this poster is the Cr(VI)-free chain. Every chemistry in the BSAA pre-treatment must be chromate-free, and the most common mistake during a Type I to BSAA transition is leaving the chromic-sulfuric desmut in the line. The three-option desmut comparison is actionable: a shop making the transition can see their alternatives at a glance. The Cr-free chain verification strip at the bottom visually confirms every step from clean to seal is chromate-free -- this is the visual equivalent of a NADCAP auditor's checklist.

---

*Alaina -- Plating Posters Inc*
*Poster #306 -- Construction Workup v1.0*
*2026-04-26*
