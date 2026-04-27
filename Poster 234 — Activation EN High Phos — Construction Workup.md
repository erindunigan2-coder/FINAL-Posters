---
Project: Plating Posters Inc
Poster Number: 234
Title: "Activation -- EN (High Phos)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Electroless Clusters — Watson Research Brief (Process 3: EN High-P)"
Technical Source: Acid activation and substrate-specific activation methods for EN High-P plating. Stage 3 of 8. Includes zincate for aluminum, Wood's strike for stainless, and acid dip for steel/copper. No brand names.
Process Scope: Activation stage for electroless nickel high-phosphorus process
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ElectrolessNickel
  - HighPhosphorus
  - Activation
  - ConstructionWorkup
  - Series2
  - ClusterEN03
---

# Poster #234 -- Construction Workup
## Activation -- EN (High Phos)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 3 of 8. Activation in electroless plating is fundamentally different from electrolytic plating. In electrolytic work, current forces deposition regardless of surface condition. In EN, the surface must be catalytically active or deposition will not start -- period. Steel and copper are inherently catalytic; aluminum requires a zincate immersion to create a catalytic zinc film; stainless steel needs a Wood's nickel strike to break through the passive oxide. This poster is about understanding your substrate.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Substrate decision tree hero (Block B):** A branching diagram showing activation path by substrate type.
2. **Zincate process detail (Block D):** Multi-step zincate sequence for aluminum with double-zincate callout.
3. **Steel/copper acid activation panel (Block E):** Simple acid dip parameters.
4. **Stainless steel / specialty panel (Block F):** Wood's strike and Inconel/Monel activation.

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
  Stage 3 highlighted (Amber)
ZONE 3 -- SUBSTRATE DECISION TREE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- ZINCATE FOR ALUMINUM (14.5"--20.5" / ~6.0")
ZONE 5 -- STEEL & COPPER ACTIVATION (20.5"--26.5" / ~6.0")
ZONE 6 -- STAINLESS & SPECIALTY SUBSTRATES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ACTIVATION` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `EN (High Phos) -- Stage 3 of 8` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `No catalytic surface, no deposition. The activation step is where substrate meets chemistry -- and the path splits.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 3 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean, rinsed substrate  -->  After: Catalytically active surface ready for EN deposition`

---

### ZONE 3 -- Substrate Decision Tree Hero

**Section label:** `KNOW YOUR SUBSTRATE -- ACTIVATION PATH DEPENDS ON IT` -- Y: 4.4".

**BLOCK B -- Decision Tree Diagram**

Y: 5.0" to 14.0".

**Root node (top center):**
- Rounded rect, X: 7.5", Y: 5.0", W: 9.0", H: 1.2", fill `#E8A020` at 30%, border 2 pt `#E8A020`
- Text: `WHAT IS YOUR SUBSTRATE?` Barlow Condensed ExtraBold 20 pt `#E8A020`

**Four branch nodes (Y: 7.0"):**

| Branch | X | W | Fill Accent | Substrate | Activation |
|---|---|---|---|---|---|
| Left | 0.5" | 5.5" | `#2EC4B6` | STEEL / IRON | Acid dip (HCl or H2SO4) |
| Center-Left | 6.25" | 5.5" | `#27AE60` | ALUMINUM | Zincate immersion (double) |
| Center-Right | 12.0" | 5.5" | `#E8A020` | COPPER / BRASS | Acid dip (H2SO4) |
| Right | 17.75" | 5.75" | `#E05C5C` | STAINLESS / NICKEL ALLOY | Wood's strike or HCl etch |

Each branch box: Rounded rect, H: 6.0", fill `#1E2435`, left accent 0.06" in branch color.

**Inside each branch:**

*Steel / Iron:*
- Badge: `INHERENTLY CATALYTIC` Barlow Condensed ExtraBold 12 pt, fill `#2EC4B6`
- `HCl 10--20% v/v` JetBrains Mono 14 pt `#F0EDE8`
- `or H2SO4 10--30% v/v` JetBrains Mono 13 pt `#F0EDE8`
- `Ambient, 30--120 sec` JetBrains Mono 13 pt `#F0EDE8`
- `Dissolves oxide; exposes active metal` Inter Regular 12 pt `#F0EDE8` at 70%
- `Oil/gas 4130/4140: HCl 20--50%, 1--2 min` Inter Medium 12 pt `#E8A020`
- `H-embrittlement: bake within 4 hr if >40 HRC` Inter Medium 11 pt `#E05C5C`

*Aluminum:*
- Badge: `NOT CATALYTIC -- ZINCATE REQUIRED` Barlow Condensed ExtraBold 11 pt, fill `#27AE60`
- `1. Acid desmut: HNO3 50% v/v, 30--60 sec`
- `2. Zincate: NaOH 120--150 g/L + ZnO 15--30 g/L, 20--25 C, 30--60 sec`
- `3. Strip: HNO3 50%, 15--30 sec`
- `4. Double zincate: Repeat step 2, 15--30 sec`
- `DOUBLE ZINCATE = finer Zn grain = better EN adhesion` Inter Medium 12 pt `#27AE60`

*Copper / Brass:*
- Badge: `INHERENTLY CATALYTIC` Barlow Condensed ExtraBold 12 pt, fill `#E8A020`
- `H2SO4 10--20% v/v` JetBrains Mono 14 pt `#F0EDE8`
- `Ambient, 30--60 sec` JetBrains Mono 13 pt `#F0EDE8`
- `Copper is catalytic -- no Pd needed` Inter Regular 12 pt `#F0EDE8` at 70%
- `Tarnished copper: bright dip (dilute HNO3 + H2SO4) before activation` Inter Medium 12 pt `#E8A020`

*Stainless / Nickel Alloy:*
- Badge: `PASSIVE OXIDE -- AGGRESSIVE ACTIVATION` Barlow Condensed ExtraBold 11 pt, fill `#E05C5C`
- `Option A: Wood's Ni strike`
- `240 g/L NiCl2 + 125 mL/L HCl`
- `25--35 ASF, 3--5 min`
- `Option B: HCl 20--50%, 1--2 min`
- `Transfer quickly to EN bath` Inter Medium 12 pt `#E05C5C`
- `Inconel/Monel: anodic etch in H2SO4 may be required` Inter Regular 11 pt `#E8A020`

**Connecting lines:** Stroke 2 pt `#3A4055`, from root node to each branch.

---

### ZONE 4 -- Zincate for Aluminum

**Section label:** `THE ZINCATE PROCESS -- ALUMINUM'S SPECIAL PATH` -- Y: 14.7".

**BLOCK D -- 4-Step Zincate Sequence (Y: 15.3" to 20.3")**

Four horizontal step boxes in sequence with arrows between them:

| Step | X | W | Accent | Name | Chemistry | Time |
|---|---|---|---|---|---|---|
| 1 | 0.5" | 5.5" | `#E05C5C` | Acid Desmut | 50% v/v HNO3, ambient | 30-60 sec |
| 2 | 6.17" | 5.5" | `#27AE60` | First Zincate | NaOH 120-150 g/L + ZnO 15-30 g/L, 20-25 C | 30-60 sec |
| 3 | 11.83" | 5.5" | `#E05C5C` | Strip | 50% v/v HNO3, ambient | 15-30 sec |
| 4 | 17.5" | 6.0" | `#27AE60` | Double Zincate | Same as step 2 | 15-30 sec |

Each box: Rounded rect, H: 3.0", fill `#1E2435`, top accent 4 pt.
Arrows: 3 pt `#3A4055`, right-pointing between boxes.

**Bottom explanation (Y: 19.5"):**
- `Why double zincate? The first zincate layer is coarse. Stripping it and re-applying produces a thinner, finer-grained zinc film. This zinc film is catalytic for EN and dissolves as the first atomic layers of nickel deposit -- providing intimate metallurgical bonding.` Inter Regular 13 pt `#F0EDE8`

---

### ZONE 5 -- Steel & Copper Activation

**Section label:** `STEEL AND COPPER -- THE SIMPLE PATH` -- Y: 20.7".

**Two-column layout (Y: 21.3" to 26.3"):**

**Left -- Steel Activation (X: 0.5", W: 11.0"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#2EC4B6`
- Title: `STEEL / IRON ALLOYS` Barlow SemiBold 20 pt `#2EC4B6`
- `HCl: 10--20% v/v, Ambient, 30--120 sec`
- `H2SO4: 10--30% v/v, Ambient, 30--120 sec`
- `Purpose: dissolve surface oxide, micro-etch for adhesion`
- `Steel is inherently catalytic -- EN starts spontaneously on clean steel`
- Warning: `HIGH-STRENGTH STEEL (>40 HRC / >1000 MPa):` `#E05C5C`
- `Acid exposure absorbs hydrogen. HE bake MANDATORY within 4 hours of plating.` `#E05C5C`

**Right -- Copper Activation (X: 12.0", W: 11.5"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E8A020`
- Title: `COPPER / BRASS / BRONZE` Barlow SemiBold 20 pt `#E8A020`
- `H2SO4: 10--20% v/v, Ambient, 30--60 sec`
- `Purpose: remove surface tarnish and oxide`
- `Copper is catalytic for EN -- no palladium activation needed`
- `Heavily tarnished copper: bright dip first (dilute HNO3 + H2SO4)`
- Note: `Copper substrates common in electronics/PCB EN applications` Inter Regular 12 pt `#F0EDE8` at 70%

---

### ZONE 6 -- Stainless & Specialty

**Section label:** `STAINLESS STEEL AND NICKEL ALLOYS -- BREAKING THE PASSIVE OXIDE` -- Y: 26.7".

**BLOCK F -- Wood's Strike Detail (Y: 27.3" to 32.3")**

**Main callout (X: 0.5", W: 15.0"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E05C5C`
- Title: `WOOD'S NICKEL STRIKE` Barlow SemiBold 20 pt `#E05C5C`
- Subtitle: `Recommended for maximum adhesion on stainless and nickel alloys`

Parameters (JetBrains Mono 14 pt `#F0EDE8`):
- `NiCl2 . 6H2O: 240 g/L`
- `HCl (concentrated): 125 mL/L`
- `Current density: 25--35 ASF`
- `Time: 3--5 min`
- `Temperature: Ambient`

Note: `The high HCl concentration dissolves the passive chromium oxide layer while the cathodic current deposits a thin nickel strike. This strike provides an active surface for EN.` Inter Regular 13 pt `#F0EDE8`

**Side callout (X: 16.0", W: 7.5"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E8A020`
- Title: `ALTERNATIVE: ACID ETCH ONLY` Barlow SemiBold 16 pt `#E8A020`
- `HCl 20--50% v/v`
- `Ambient, 1--2 min`
- `Transfer to EN within 30 seconds`
- `Less reliable adhesion than Wood's`
- `Use only when Wood's strike is not available`

---

### ZONE 7 -- Footer

Standard. Title: `Activation -- EN (High Phos)`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Activation parameters shown are typical industry values for substrates entering electroless nickel high-phosphorus plating. Zincate and Wood's strike formulations vary by proprietary product. Consult your process supplier for application-specific guidance.`

---

## Parts 5-7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Activation EN High-P -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The substrate decision tree is the hero -- this is the poster where operators learn that activation is not one-size-fits-all. The zincate sequence for aluminum is the most complex activation path in any EN cluster and deserves its own zone. The High-P-specific callout for oil/gas substrates (4130/4140) and nickel alloys (Inconel, Monel) reflects the reality that High-P EN is disproportionately used on these demanding substrates.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #234 -- Construction Workup v1.0*
*2026-04-26*
