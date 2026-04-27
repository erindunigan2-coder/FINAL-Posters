---
Project: Plating Posters Inc
Poster Number: 74
Title: "Activation -- Nickel-Cobalt"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-06 technical reference (nickel-cobalt alloy plating)"
Technical Source: Activation stage for nickel-cobalt alloy plating. Standard HCl activation for steel substrates. Wood's nickel strike mandatory for Inconel, Waspaloy, and titanium -- the aerospace superalloys that dominate NiCo applications. HF/HNO3 etch required for titanium before Wood's strike. Stage 3 of 8.
Process Scope: Activation for nickel-cobalt alloy plating (Stage 3 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - NickelCobaltPlating
  - Activation
  - ConstructionWorkup
  - Series2
  - ClusterEP06
---

# Poster #74 -- Construction Workup
## Activation -- Nickel-Cobalt

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 3 of 8. This is where NiCo diverges from general nickel plating. The substrates being plated are frequently aerospace superalloys -- Inconel 718, Waspaloy, titanium alloys -- that form tenacious passive oxide films. Standard HCl activation works for steel, but superalloys require a Wood's nickel strike (or in the case of titanium, a specialized HF/HNO3 etch followed by Wood's strike). Getting activation wrong on these materials means the deposit peels off -- there is no second chance.

Hero visual: a decision flowchart -- "What is your substrate?" branching to the correct activation path.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Substrate decision flowchart hero (Block B):** A branching flowchart from substrate type to activation method. Built with rounded rectangles and arrows.
2. **Activation methods detail panel (Block D):** Three methods side-by-side: HCl acid dip, Wood's nickel strike, titanium etch sequence.
3. **Wood's strike parameter table (Block E):** Full operating parameters for the Wood's nickel strike bath.
4. **Common activation failures (Block F):** 4-card strip.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts per series design system.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 3 highlighted (Amber)
ZONE 3 -- SUBSTRATE DECISION FLOWCHART HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- ACTIVATION METHODS DETAIL (14.5"--20.5" / ~6.0")
ZONE 5 -- WOOD'S STRIKE PARAMETERS (20.5"--26.5" / ~6.0")
ZONE 6 -- COMMON ACTIVATION FAILURES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ACTIVATION` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Nickel-Cobalt Plating -- Stage 3 of 8` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Superalloys form passive oxide films that laugh at mild acid. Wood's strike is your only way through. Get this wrong and the deposit peels.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Y: 2.9" to 4.2".

Eight mini boxes. Stage 3 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.

Below: `Before: Clean, rinsed surface with residual oxide film  -->  After: Oxide-free, active surface ready for plating`

---

### ZONE 3 -- Substrate Decision Flowchart Hero

**Section label:** `WHAT IS YOUR SUBSTRATE? -- CHOOSE YOUR ACTIVATION PATH` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Decision Flowchart**

Y: 5.0" to 14.0".

**Start node (top center):**
- Rounded rect, X: 8.5", Y: 5.0", W: 7.0", H: 1.2", fill `#E8A020`, radius 8
- Text: `WHAT IS THE SUBSTRATE?` Barlow Condensed ExtraBold 20 pt `#1A1F2E`

**Three branches below, arrows down from start node:**

**Branch 1 -- Steel (left):**
- Arrow from start node down-left to:
- Rounded rect, X: 0.5", Y: 7.0", W: 6.5", H: 1.5", fill `#1E2435`, top accent 4 pt `#2EC4B6`
- Title: `CARBON / ALLOY STEEL` Barlow SemiBold 18 pt `#2EC4B6`
- Arrow down to:
- Rounded rect, X: 0.5", Y: 9.0", W: 6.5", H: 3.5", fill `#1E2435`, left accent 0.06" `#2EC4B6`
- Method: `HCl ACID DIP` Barlow SemiBold 16 pt `#F0EDE8`
- `HCl 20--50% v/v` JetBrains Mono 14 pt `#2EC4B6`
- `Ambient temperature`
- `15--60 sec`
- `Remove native oxide`
- Arrow down to:
- Rounded rect, X: 0.5", Y: 13.0", W: 6.5", H: 0.8", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- `READY FOR RINSE --> PLATE` Inter Medium 14 pt `#27AE60`

**Branch 2 -- Superalloys (center):**
- Arrow from start node straight down to:
- Rounded rect, X: 8.0", Y: 7.0", W: 8.0", H: 1.5", fill `#1E2435`, top accent 4 pt `#E8A020`
- Title: `INCONEL / WASPALOY / Ni-BASED SUPERALLOYS` Barlow SemiBold 16 pt `#E8A020`
- Arrow down to:
- Rounded rect, X: 8.0", Y: 9.0", W: 8.0", H: 3.5", fill `#1E2435`, left accent 0.06" `#E8A020`
- Method: `HCl DIP + WOOD'S STRIKE` Barlow SemiBold 16 pt `#F0EDE8`
- `1. HCl 20--50% v/v, 15--30 sec` JetBrains Mono 13 pt `#E8A020`
- `2. Rinse`
- `3. Wood's nickel strike (see Zone 5)`
- `4. Transfer LIVE to NiCo bath`
- Check: `DO NOT BREAK CURRENT between Wood's and plate` Inter Medium 12 pt `#E05C5C`
- Arrow down to ready box

**Branch 3 -- Titanium (right):**
- Arrow from start node down-right to:
- Rounded rect, X: 17.0", Y: 7.0", W: 6.5", H: 1.5", fill `#1E2435`, top accent 4 pt `#E05C5C`
- Title: `TITANIUM ALLOYS` Barlow SemiBold 18 pt `#E05C5C`
- Arrow down to:
- Rounded rect, X: 17.0", Y: 9.0", W: 6.5", H: 3.5", fill `#1E2435`, left accent 0.06" `#E05C5C`
- Method: `HF/HNO3 ETCH + WOOD'S STRIKE` Barlow SemiBold 14 pt `#F0EDE8`
- `1. HF/HNO3 etch (specialized)` JetBrains Mono 13 pt `#E05C5C`
- `2. Rinse`
- `3. Wood's nickel strike (see Zone 5)`
- `4. Transfer LIVE to NiCo bath`
- Check: `CAUTION: HF is extremely hazardous -- specialized training required` Inter Medium 11 pt `#E05C5C`
- Arrow down to ready box

**H-embrittlement warning banner (Y: 13.8"):**
- Full-width rounded rect, X: 0.5", W: 23.0", H: 0.6", fill `#E05C5C` at 15%, border 1 pt `#E05C5C`
- Text: `HIGH-STRENGTH STEEL (>=40 HRC): H-embrittlement risk during acid activation. Bake 375 F for 4+ hr within 4 hr of plating.` Inter Medium 13 pt `#E05C5C`

---

### ZONE 4 -- Activation Methods Detail

**Section label:** `ACTIVATION METHODS -- DETAIL` -- Y: 14.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK D -- Three-Column Detail (Y: 15.3" to 20.3")**

| Method | X | W | Accent | Title |
|---|---|---|---|---|
| HCl Acid Dip | 0.5" | 7.33" | `#2EC4B6` | ACID DIP |
| Wood's Nickel Strike | 8.0" | 7.33" | `#E8A020` | WOOD'S STRIKE |
| Titanium Etch | 15.5" | 8.0" | `#E05C5C` | TITANIUM ETCH |

Each box: Rounded rect H: 4.8", fill `#1E2435`, left accent 0.06".

*Acid Dip box:*
- `HCl 20--50% v/v` JetBrains Mono 16 pt `#2EC4B6`
- `Ambient temperature`
- `15--60 sec immersion`
- `Substrates: carbon steel, alloy steel, low-alloy steel`
- `Removes native Fe oxide; exposes clean Fe surface`
- `Simple, reliable, universally understood`

*Wood's Strike box:*
- `NiCl2 240 g/L + HCl 125 mL/L` JetBrains Mono 14 pt `#E8A020`
- `Ambient to 80 F`
- `20--60 ASF, 2--5 min`
- `Substrates: Inconel, Waspaloy, stainless, titanium (after etch)`
- `Deposits thin, highly adherent Ni layer through oxide film`
- `MANDATORY for passive alloys -- no substitute`

*Titanium Etch box:*
- `HF 2--5% + HNO3 20--35% v/v` JetBrains Mono 14 pt `#E05C5C`
- `Ambient, 30--120 sec`
- `Removes TiO2 passive film`
- `IMMEDIATELY rinse and Wood's strike -- Ti re-passivates in seconds`
- `HF SAFETY: burns cause deep tissue necrosis`
- `Calcium gluconate gel MUST be on-site` (`#E05C5C`)

---

### ZONE 5 -- Wood's Strike Parameter Table

**Section label:** `WOOD'S NICKEL STRIKE -- FULL PARAMETERS` -- Y: 20.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK E -- Parameter Table (Y: 21.3" to 26.3")**

Column widths (23.0" total):
- Parameter (6.0") | Range (5.5") | Optimal Target (5.5") | Notes (6.0")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.7".

| Parameter | Range | Optimal | Notes |
|---|---|---|---|
| NiCl2 * 6H2O | 200--280 g/L | 240 g/L | Sole nickel source |
| HCl (conc.) | 80--160 mL/L | 125 mL/L | Keeps pH very low |
| pH | < 1.0 | < 0.5 | Do not adjust upward |
| Temperature | Ambient--80 F | Ambient | Do not heat |
| Current density | 15--60 ASF | 20--40 ASF | Lower for complex parts |
| Time | 2--5 min | 3 min | Thin strike (~0.1 mil) |
| Anodes | Nickel (S-rounds in Ti baskets) | -- | Dissolve to maintain Ni |
| Agitation | Cathode rod or air | -- | Gentle only |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Parameter names: Inter Medium, 13 pt.

**Below table callout:**
- Rounded rect, W: 23.0", H: 0.6", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `Transfer parts LIVE (current on) from Wood's strike directly to the NiCo plating bath. Breaking current allows re-passivation.` Inter Medium 13 pt `#E8A020`

---

### ZONE 6 -- Common Activation Failures

**Section label:** `WHAT GOES WRONG` -- Y: 26.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK F -- Four Problem Cards (Y: 27.3" to 32.3")**

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | DEPOSIT PEELING | Passive oxide not removed; current broken during transfer | Verify Wood's strike; maintain live transfer |
| 2 | 6.33" | BLISTERING | Hydrogen trapped under deposit; insufficient bake | Bake 375 F / 4+ hr for high-strength steel |
| 3 | 12.16" | DARK STRIKE | HCl depleted in Wood's bath; NiCl2 too low | Replenish HCl; analyze NiCl2 concentration |
| 4 | 18.0" | TI RE-PASSIVATION | Delay between HF etch and Wood's strike | Reduce transfer time to under 30 sec |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 7 -- Footer Band

Standard. Title: `Activation -- Nickel-Cobalt`. Version `v1.0 -- 2026`.

**Disclaimer:**

> This poster is an educational reference tool. Activation parameters shown are typical industry values. Substrate-specific etch sequences and Wood's strike parameters vary by OEM specification. HF handling requires specialized safety training and equipment. Consult your process supplier and governing specification for application-specific guidance. Source: General industry knowledge; ASM Handbook Vol. 5; AMS 2424.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Activation NiCo -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the most technically distinctive poster in the NiCo cluster. The substrate decision flowchart is the hero because the activation path is entirely substrate-dependent -- and NiCo is applied to a wider range of exotic substrates than most plating processes. The Wood's strike table gets its own zone because it is effectively a sub-process with its own bath, its own parameters, and its own failure modes. The HF safety callout for titanium is non-negotiable -- HF burns are among the most dangerous injuries in metal finishing.

Watson's brief notes "same as nickel processes, Wood's strike required for same substrates" and lists Inconel/Waspaloy and titanium specifically. I expanded the titanium etch detail from standard aerospace practice.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #74 -- Construction Workup v1.0*
*2026-04-26*
