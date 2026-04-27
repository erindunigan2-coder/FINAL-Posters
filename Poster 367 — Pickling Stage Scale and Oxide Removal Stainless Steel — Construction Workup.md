---
Project: Plating Posters Inc
Poster Number: 367
Title: "Pickling Stage -- Scale & Oxide Removal (Stainless Steel)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Chemical Treatment Clusters -- Watson Research Brief (CT-4.4)"
Technical Source: Industry-standard operating parameters and chemistry for the acid pickling stage of stainless steel. Covers HNO3/HF mechanism, immersion times by scale severity and alloy, part loading, and common failures including intergranular attack and preferential weld attack.
Process Scope: Acid pickling treatment stage -- stainless steel scale and oxide removal
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - AcidPickling
  - StainlessSteel
  - PicklingStage
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT04
---

# Poster #367 -- Construction Workup
## Pickling Stage -- Scale & Oxide Removal (Stainless Steel)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Poster 4 of 7 in the CT-04 cluster. This is the "main tank" poster -- the pickling operation itself. The hero visual is a dual-mechanism diagram showing how HNO3 and HF work together: HNO3 oxidizes and passivates while HF dissolves the refractory scale matrix. The immersion time table is the most complex in the series -- it varies by BOTH scale severity AND alloy family. The failure table covers intergranular attack, preferential weld attack, orange peel, and over-pickling -- defects unique to stainless steel pickling.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Dual-mechanism diagram (Block B -- HERO):** Split visual -- HNO3 action (oxidation/passivation) and HF action (scale dissolution) working simultaneously.
2. **Immersion time matrix (Block D):** Scale severity vs. alloy family.
3. **Part loading rules (Block E):** Rack vs. basket, no barrel, crevice warnings.
4. **Failure/fix table (Block F):** Five stainless-specific failures.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.5" / 22.0" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Poster 4 of 7 highlighted (Coral -- main pickle step)
ZONE 3 -- DUAL-MECHANISM DIAGRAM / HERO (4.2"--15.5" / ~11.3")
ZONE 4 -- IMMERSION TIME MATRIX (15.5"--22.0" / ~6.5")
ZONE 5 -- PART LOADING RULES (22.0"--27.0" / ~5.0")
ZONE 6 -- COMMON FAILURES (27.0"--32.5" / ~5.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `THE PICKLING STAGE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Stainless Steel -- Where Nitric Meets Hydrofluoric` -- 32 pt `#E05C5C` (Coral). Y: 1.4".
**Tagline:** `Two acids, two mechanisms, one goal: strip the scale and restore the passive film. Control the process or the process controls you.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Poster 4 highlighted: fill `#E05C5C`, text `#1A1F2E`. Others dimmed.
Below: `Before: Scaled/oxidized stainless surface (weld tint, anneal scale) --> After: Clean, bright, active metal ready for passivation`

---

### ZONE 3 -- Dual-Mechanism Diagram (HERO)

**Section label:** `HOW HNO3 AND HF WORK TOGETHER -- TWO ACIDS, TWO ROLES` -- Y: 4.4".

**Two-column hero (Y: 5.0" to 15.0"):**

**Left -- HNO3 (Nitric Acid) Action (X: 0.5", W: 11.0"):**

Rounded rect H: 9.5", fill `#1E2435`, left accent 0.06" `#E8A020`.

Title: `NITRIC ACID (HNO3)` Barlow Condensed ExtraBold 24 pt `#E8A020`.
Subtitle: `The Oxidizer -- Dissolves and Passivates` Barlow SemiBold 16 pt `#F0EDE8` at 60%.

**Key reactions (JetBrains Mono 13 pt):**
```
Fe (iron contamination) + HNO3 -> dissolved
Cr-depleted layer + HNO3 -> dissolved
Fresh Cr surface + HNO3 -> Cr2O3 passive film
```

**Key points below reactions:**
- Inter Regular 13 pt `#F0EDE8`, line height 155%:
```
- Oxidizes and dissolves iron contamination
- Removes the chromium-depleted surface layer
- Simultaneously PASSIVATES the fresh surface
- Creates the protective Cr2O3 film
- This dual action is unique to HNO3
- Used alone for light scale and passivation
```

**Right -- HF (Hydrofluoric Acid) Action (X: 12.0", W: 11.5"):**

Rounded rect H: 9.5", fill `#1E2435`, left accent 0.06" `#E05C5C`.

Title: `HYDROFLUORIC ACID (HF)` Barlow Condensed ExtraBold 24 pt `#E05C5C`.
Subtitle: `The Scale Breaker -- Attacks What HNO3 Cannot` Barlow SemiBold 16 pt `#F0EDE8` at 60%.

**Key points:**
```
- Dissolves siliceous scale that HNO3 alone
  cannot penetrate
- Attacks silicon-bearing inclusions in the
  scale matrix
- Breaks the scale structure from within
  so HNO3 can oxidize the underlayer
- Without HF, heavy anneal scale removal
  is impractically slow
- HF provides the speed; HNO3 provides
  the passivation
```

Warning: `HF IS THE HAZARD. HNO3 IS THE PROTECTOR. The HNO3:HF ratio must be maintained -- too much HF without enough HNO3 causes aggressive attack without passivation.` Inter Medium 12 pt `#E05C5C`

**Bottom callout spanning both columns (Y: 14.5"):**
- Rounded rect W: 23.0", H: 0.8", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- `Together, HNO3 and HF lift the entire scale layer: HF attacks the oxide matrix, HNO3 oxidizes the exposed iron and chromium, and the passive Cr2O3 film reforms immediately on the clean surface.` Inter Medium 13 pt `#E8A020`

---

### ZONE 4 -- Immersion Time Matrix

**Section label:** `IMMERSION TIME -- BY SCALE SEVERITY AND ALLOY` -- Y: 15.7".

**BLOCK D -- Time Matrix (Y: 16.3" to 21.8")**

Column widths (23.0" total):
- Scale Condition (5.0") | Austenitic (4.5") | Ferritic (4.5") | Martensitic (4.5") | Duplex/PH (4.5")

Header row: fill `#3A4055`, H: 0.5".

| Condition | Austenitic (304/316) | Ferritic (430/409) | Martensitic (410/420) | Duplex / PH |
|---|---|---|---|---|
| Light heat tint | 5-15 min | 5-10 min | 3-10 min | 5-15 min |
| Medium weld scale | 15-30 min | 10-20 min | 10-15 min | 15-25 min |
| Heavy anneal scale | 30-60 min | 20-40 min | 15-30 min | 25-45 min |
| HNO3 only (light) | 15-30 min | 15-30 min | 10-20 min | 15-30 min |
| HNO3 only (heavy) | NOT PRACTICAL | NOT PRACTICAL | N/A | NOT PRACTICAL |

Data: JetBrains Mono 12 pt `#F0EDE8`. "NOT PRACTICAL" in `#E05C5C`.
Row labels: Inter Medium 13 pt, color-coded by severity.

**Caution callout:**
- `Over-pickling causes grain boundary attack, orange peel texture, and dimensional loss. When in doubt, SHORTER TIME and re-check. You can always pickle longer -- you cannot un-pickle.` Inter Medium 12 pt `#E05C5C`

---

### ZONE 5 -- Part Loading Rules

**Section label:** `PART LOADING -- CREVICE CORROSION IS THE ENEMY` -- Y: 22.2".

**BLOCK E -- Three Loading Cards (Y: 22.8" to 26.8")**

| Card | X | W | Title | Content |
|---|---|---|---|---|
| RACK (Preferred) | 0.5" | 7.0" | `RACK MOUNTING` `#27AE60` | Preferred method. Space parts to avoid overlapping. No rubber bands, wire ties, or anything creating crevice geometry. Acid trapped in crevices causes accelerated attack and pitting. |
| BASKET (Small Parts) | 8.0" | 7.0" | `BASKET IMMERSION` `#2EC4B6` | Acceptable for small parts. Use perforated baskets with maximum open area. Agitate periodically to redistribute parts and prevent nesting. Parts touching = crevice corrosion. |
| BARREL (NOT Recommended) | 15.5" | 8.0" | `BARREL -- NOT RECOMMENDED` `#E05C5C` | Barrel pickling of stainless steel creates crevice corrosion between parts. Parts nest and trap acid in contact areas. If barrel is the only option, limit time severely and inspect every part individually. |

Each card: Rounded rect H: 3.5", fill `#1E2435`, radius 6, left accent 0.06".
Title: Barlow SemiBold 16 pt, accent color.
Content: Inter Regular 12 pt `#F0EDE8`.

---

### ZONE 6 -- Common Failures

**Section label:** `WHAT GOES WRONG -- 5 STAINLESS-SPECIFIC FAILURES` -- Y: 27.2".

**BLOCK F -- Failure Table (Y: 27.8" to 32.3")**

| Failure | Cause | Fix |
|---|---|---|
| Over-pickling (rough, matte surface) | HF too high; time too long; temperature too high | Reduce HF; shorten time; lower temperature; inspect more frequently |
| Intergranular attack (IGA) | Sensitized material (304 not stabilized); HNO3 too high relative to HF | Metallurgical issue -- may require stabilized grade (321, 347); adjust HNO3:HF ratio |
| Preferential weld attack | Heat-affected zone has different metallurgy; acid imbalance | Pre-grind weld scale mechanically before acid pickle; adjust acid ratio; reduce time on welds |
| Orange peel texture | Excessive HF; excessive time; uneven grain size in material | Reduce HF; reduce time; metallurgical review of base material |
| Incomplete scale removal | Acid depleted; metals too high; time too short | Check both free acids; replace if metals >40 g/L; extend time cautiously |

Each row: Rounded rect H: 0.8", alternating fills.
Failure: Barlow SemiBold 14 pt `#E05C5C`. Cause: Inter Regular 12 pt `#F0EDE8`. Fix: Inter Medium 12 pt `#27AE60`.

---

### ZONE 7 -- Footer

Standard. Title: `Pickling Stage -- Scale & Oxide Removal (Stainless Steel)`. Version `v1.0 -- 2026`.
Disclaimer: `Source: ASTM A380; ASTM A967; ASM Handbook Vol. 5; general industry knowledge. Immersion times are typical ranges -- actual times vary by specific alloy, scale thickness, and acid condition. Over-pickling of sensitized material can cause intergranular attack that is irreversible. Consult your metallurgist and process supplier.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Pickling Stage Scale Oxide Removal Stainless Steel -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The dual-mechanism hero distinguishes this poster from CT-03's scale removal poster (360). Carbon steel pickling is straightforward acid dissolution; stainless steel pickling is a two-acid system where each acid has a distinct role and the ratio between them matters. The immersion time matrix is more complex than CT-03's because stainless pickling varies by both scale severity AND alloy family. The crevice corrosion warning in the loading section is the most practical piece of advice on this poster -- many shops barrel-pickle stainless steel and wonder why they get pitting.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #367 -- Construction Workup v1.0*
*2026-04-26*
