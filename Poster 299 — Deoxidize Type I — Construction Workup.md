---
Project: Plating Posters Inc
Poster Number: 299
Title: "Deoxidize -- Chromic Acid Anodizing (Type I)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 3, Section 3.5)"
Process Scope: Desmut / deoxidize for chromic acid anodizing -- Stage 4 of 8
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Anodizing
  - ChromicAcid
  - TypeI
  - Deoxidize
  - ConstructionWorkup
  - ClusterAnodize03
---

# Poster #299 -- Construction Workup
## Deoxidize -- Chromic Acid Anodizing (Type I)

*Alaina -- Plating Posters Inc*
*v1.0 -- 2026-04-26*

Stage 4 of 8. Desmut is critical even when the etch was light or skipped -- residual smut under a 1--2 um coating is immediately visible as discoloration. For copper alloys (2024, 7075), HNO3/HF desmut is the standard. The legacy chromic-sulfuric acid deox is still permitted in Type I lines since the process already uses Cr(VI).

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Desmut chemistry comparison hero (Block B):** Three panels showing standard HNO3, HNO3/HF (copper alloys), and chromic-sulfuric acid deox (legacy).
2. **Alloy routing table (Block D):** Which alloy gets which desmut.
3. **HF safety callout (Block E):** Prominent coral-tinted safety panel for hydrofluoric acid.
4. **Defect grid (Block F):** 4 desmut-related failures.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 4 highlighted (Amber)
ZONE 3 -- DESMUT CHEMISTRY HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- ALLOY ROUTING + LEGACY DEOX (14.5"--20.5" / ~6.0")
ZONE 5 -- DEFECT GRID + HF SAFETY (20.5"--26.5" / ~6.0")
ZONE 6 -- KEY PRINCIPLES + Cr(VI) REMINDER (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `DEOXIDIZE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Chromic Acid Anodizing (Type I) -- Stage 4 of 8` -- 32 pt `#E8A020`. Y: 1.4".
**Tagline:** `Smut under a 1 um coating is a billboard. Clean the surface now or see every speck after anodizing.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

**Cr(VI) flag:** Standard coral badge.

---

### ZONE 2 -- Orientation Strip

Stage 4 highlighted: fill `#E8A020`, text `#1A1F2E`.
Below: `Before: Etched surface with smut residue (if etched) or clean surface with native oxide  -->  After: Bright, smut-free aluminum ready for rinse`

---

### ZONE 3 -- Desmut Chemistry Hero

**Section label:** `THREE DESMUT APPROACHES` -- Y: 4.4".

**BLOCK B -- Three Chemistry Panels**

Y: 5.0" to 13.5". Three side-by-side panels.

*Panel 1 -- Standard HNO3 (X: 0.5", W: 7.33"):*
- Rounded rect, H: 8.0", fill `#1E2435`, left accent `#2EC4B6`, radius 6
- Title: `NITRIC ACID (STANDARD)` Barlow SemiBold 18 pt `#2EC4B6`
- Subtitle: `For 6xxx and general alloys` Barlow Condensed ExtraBold 13 pt `#F0EDE8` at 50%
- Parameters:
  - `HNO3: 25--50% v/v` JetBrains Mono 15 pt `#2EC4B6`
  - `Temperature: Ambient` JetBrains Mono 14 pt `#F0EDE8`
  - `Time: 30--120 seconds` JetBrains Mono 14 pt `#F0EDE8`
- How it works: `Dissolves aluminum oxide and light smut. Does NOT dissolve metallic copper particles.` Inter Regular 13 pt `#F0EDE8` at 80%
- Best for: `6061, 6063, 5052, 1100 -- standard wrought alloys without significant copper content` Inter Regular 12 pt `#F0EDE8` at 70%

*Panel 2 -- HNO3/HF (X: 8.16", W: 7.33"):*
- Rounded rect, same dims, left accent `#E8A020`
- Title: `NITRIC + HYDROFLUORIC` Barlow SemiBold 18 pt `#E8A020`
- Subtitle: `For copper-bearing alloys` Barlow Condensed ExtraBold 13 pt `#F0EDE8` at 50%
- Parameters:
  - `HNO3: 25--50% v/v` JetBrains Mono 15 pt `#E8A020`
  - `HF: 1--3% v/v (40% HF)` JetBrains Mono 15 pt `#E8A020`
  - `Temperature: Ambient` JetBrains Mono 14 pt `#F0EDE8`
  - `Time: 60--180 seconds` JetBrains Mono 14 pt `#F0EDE8`
- How it works: `HF attacks metallic copper and silicon particles directly. Essential for heavy copper smut on 2024 and 7075.` Inter Regular 13 pt `#F0EDE8` at 80%
- Safety flag: `HF is a SYSTEMIC TOXIN -- see safety panel below` Inter Medium 12 pt `#E05C5C`

*Panel 3 -- Chromic-Sulfuric Acid Deox (X: 15.83", W: 7.67"):*
- Rounded rect, same dims, left accent `#E05C5C`
- Title: `CHROMIC-SULFURIC (LEGACY)` Barlow SemiBold 18 pt `#E05C5C`
- Subtitle: `Permitted in Type I lines (already Cr6+)` Barlow Condensed ExtraBold 13 pt `#F0EDE8` at 50%
- Parameters:
  - `Na2Cr2O7: 30--60 g/L` JetBrains Mono 15 pt `#E05C5C`
  - `H2SO4: 300--450 g/L` JetBrains Mono 14 pt `#F0EDE8`
  - `Temperature: 140--160 F (60--70 C)` JetBrains Mono 14 pt `#F0EDE8`
  - `Time: 5--10 minutes` JetBrains Mono 14 pt `#F0EDE8`
- How it works: `Excellent deox performance. Attacks all smut components including Cu and Si. Permitted in Type I since Cr(VI) is already in the process.` Inter Regular 13 pt `#F0EDE8` at 80%
- Legacy flag: `Contains Cr(VI) -- being phased out in new installations` Inter Medium 12 pt `#E05C5C`

---

### ZONE 4 -- Alloy Routing + Legacy Deox Context

**Two-column layout (Y: 14.7" to 20.3"):**

**Left -- Alloy Routing Table (X: 0.5", W: 13.0"):**

Section label: `WHICH DESMUT FOR WHICH ALLOY?` Barlow Condensed ExtraBold 22 pt.

| Alloy | Recommended Desmut | Time | Notes |
|---|---|---|---|
| 6061 / 6063 | HNO3 (standard) | 30--120 sec | No copper smut to worry about |
| 5052 | HNO3 (standard) | 30--90 sec | Light magnesium residue |
| 1100 | HNO3 (standard) | 30--60 sec | Minimal smut on pure aluminum |
| 2024 | HNO3/HF (mandatory) | 60--180 sec | Heavy copper smut -- HNO3 alone insufficient |
| 7075 | HNO3/HF (recommended) | 60--180 sec | Zinc + copper smut |
| Cast (A356) | Not typical for Type I | -- | If attempted: HNO3/HF for silicon |

**Right -- Why Desmut Matters More for Type I (X: 14.0", W: 9.5"):**

Callout box, fill `#1E2435`, left accent `#E8A020`:
- Title: `WHY IT MATTERS MORE` Barlow SemiBold 18 pt `#E8A020`
- `Type I coating: 0.5--2.5 um` JetBrains Mono 14 pt `#E8A020`
- `Type II coating: 5--25 um` JetBrains Mono 14 pt `#F0EDE8` at 60%
- `Type III coating: 25--100 um` JetBrains Mono 14 pt `#F0EDE8` at 40%
- Separator
- `The thinner the coating, the more visible every surface defect.` Inter Medium 14 pt `#F0EDE8`
- `Residual smut under 1--2 um of Type I oxide is immediately visible as discoloration.` Inter Regular 13 pt `#E05C5C`
- `Thorough desmut is non-negotiable even when the etch was light or skipped.` Inter Medium 13 pt `#27AE60`

---

### ZONE 5 -- Defect Grid + HF Safety

**Left -- Defect Grid (X: 0.5", W: 12.5", 2x2):**

Section label: `WHAT GOES WRONG -- 4 DESMUT FAILURES`

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | MOTTLED COATING | `#E05C5C` | Residual copper smut on 2024 | HNO3/HF desmut; extend time |
| R1C2 | DISCOLORATION | `#E8A020` | Incomplete smut removal | Verify chemistry; replace spent bath |
| R2C1 | PITTING (after anodize) | `#E05C5C` | HF over-attack on thin walls | Reduce HF concentration or time |
| R2C2 | REDUCED CORROSION RESISTANCE | `#E8A020` | Smut carried into anodize tank | Improve desmut + post-desmut rinse |

**Right -- HF Safety Panel (X: 13.5", W: 10.0"):**

Coral-tinted callout, fill `#E05C5C` at 12%, border 2 pt `#E05C5C`, radius 6:
- Title: `HYDROFLUORIC ACID (HF) -- EXTREME HAZARD` Barlow Condensed ExtraBold 20 pt `#E05C5C`
- Body (Inter Medium 13 pt `#F0EDE8`, line height 160%):
```
Skin absorption causes systemic fluoride poisoning
Bone damage and cardiac arrest possible from small exposures
Calcium gluconate gel MUST be available at the station
HF training is MANDATORY before any personnel work this tank
Buddy system required -- never work HF alone
Burns may not be immediately painful -- delayed onset is common
```
- Bottom: `If skin contact occurs: flush immediately, apply calcium gluconate, seek emergency medical attention` Inter Medium 12 pt `#E05C5C`

---

### ZONE 6 -- Key Principles + Cr(VI) Reminder

**Two-column layout (Y: 26.7" to 32.3"):**

**Left -- Proprietary Alternatives (X: 0.5", W: 11.0"):**

Callout box, fill `#1E2435`, left accent `#27AE60`:
- Title: `NON-HF ALTERNATIVES` Barlow SemiBold 18 pt `#27AE60`
- `Ferric sulfate + sulfuric acid desmuts (non-HF) are gaining market share` Inter Regular 13 pt `#F0EDE8`
- `Work well on 6xxx alloys` Inter Regular 13 pt `#27AE60`
- `May be insufficient for heavy copper smut on 2024` Inter Regular 13 pt `#E8A020`
- `Must be validated for the specific alloy and specification` Inter Regular 13 pt `#F0EDE8` at 70%
- `Eliminates HF safety burden -- a significant operational advantage` Inter Medium 13 pt `#27AE60`

**Right -- Cr(VI) Process Context (X: 12.0", W: 11.5"):**

Coral-tinted callout:
- Title: `DOWNSTREAM: Cr(VI) ANODIZE BATH` Barlow SemiBold 18 pt `#E05C5C`
- `The next wet step after the pre-anodize rinse is the chromic acid bath.`
- `Chromic acid bath contamination limits are tighter than sulfuric acid:`
- `Sulfate (SO4 2-): < 0.5 g/L` JetBrains Mono 13 pt `#E05C5C`
- `Chloride (Cl-): < 25 ppm (some specs: < 10 ppm)` JetBrains Mono 13 pt `#E05C5C`
- `Cr3+: < 20 g/L` JetBrains Mono 13 pt `#F0EDE8`
- `Everything that leaves the desmut tank and survives the rinse reaches the chromic acid bath.`

---

### ZONE 7 -- Footer

Standard. Title: `Deoxidize -- Chromic Acid Anodizing (Type I)`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Deoxidize Type I -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The three-chemistry hero panel is the visual anchor. Shop operators need to know which desmut chemistry to use for which alloy -- the routing table makes this an instant lookup. The HF safety panel is visually prominent and earned: HF is one of the most dangerous chemicals in a plating shop. The thickness comparison (Type I vs. II vs. III) in the "why it matters more" callout is a simple but powerful visual that connects desmut quality to coating thickness.

---

*Alaina -- Plating Posters Inc*
*Poster #299 -- Construction Workup v1.0*
*2026-04-26*
