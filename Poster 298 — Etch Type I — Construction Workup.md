---
Project: Plating Posters Inc
Poster Number: 298
Title: "Etch -- Chromic Acid Anodizing (Type I)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 3, Section 3.4)"
Process Scope: Etch (light or none) for chromic acid anodizing -- Stage 3 of 8
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Anodizing
  - ChromicAcid
  - TypeI
  - Etch
  - ConstructionWorkup
  - ClusterAnodize03
---

# Poster #298 -- Construction Workup
## Etch -- Chromic Acid Anodizing (Type I)

*Alaina -- Plating Posters Inc*
*v1.0 -- 2026-04-26*

Stage 3 of 8. This is the stage where Type I diverges most from Type II. Most Type I specifications call for NO caustic etch or only a very light etch. The thin coating (0.5--2.5 um) cannot hide surface roughness, and Type I is often applied to fatigue-critical parts where metal removal must be minimized. The poster's hero concept is the decision tree: etch or skip?

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Decision tree hero (Block B):** "To etch or not to etch?" -- a visual decision flowchart showing when to etch, when to skip, and the parameters for each approach.
2. **Etch approach comparison (Block D):** Three approaches side by side (no etch / light etch / standard etch) with when-to-use guidance.
3. **Alloy-specific etch behavior (Block E):** Table showing 2024, 6061, 7075 behavior.
4. **Defect grid (Block F):** 4 etch-related failures specific to Type I.

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
ZONE 3 -- ETCH DECISION TREE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- THREE ETCH APPROACHES (14.5"--20.5" / ~6.0")
ZONE 5 -- ALLOY BEHAVIOR + CHEMISTRY (20.5"--26.5" / ~6.0")
ZONE 6 -- DEFECT GRID + KEY PRINCIPLES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ETCH` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Chromic Acid Anodizing (Type I) -- Stage 3 of 8` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Most Type I specs say: skip it. When you do etch, keep it light. The thin coating reveals everything the etch does to the surface.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

**Cr(VI) flag:** Standard coral badge.

---

### ZONE 2 -- Orientation Strip

Stage 3 highlighted: fill `#E8A020`, text `#1A1F2E`.
Below: `Before: Clean, rinsed aluminum surface  -->  After: Prepared surface (as-received finish or lightly matted)`

---

### ZONE 3 -- Etch Decision Tree Hero

**Section label:** `TO ETCH OR NOT TO ETCH -- THE TYPE I DECISION` -- Y: 4.4".

**BLOCK B -- Decision Tree**

Y: 5.0" to 13.5".

Central decision diamond (or rounded rect with question):
- X: 7.0", Y: 5.5", W: 10.0", H: 1.5", fill `#E8A020` at 20%, border 2 pt `#E8A020`, radius 8
- Text: `Does the specification require a caustic etch?` Barlow SemiBold 20 pt `#E8A020`, center

**YES branch (left, Y: 7.5"):**
- Arrow down-left from diamond
- Box: `Is dimensional tolerance tight?` (secondary decision)
  - YES -> `LIGHT ETCH` box (Amber-tinted)
  - NO -> `STANDARD ETCH` box (Amber-tinted, dimmer)

**NO branch (right, Y: 7.5"):**
- Arrow down-right from diamond
- Box: `NO ETCH -- Clean + Desmut Only` (Teal-tinted, `#2EC4B6`)

**Three outcome boxes (Y: 9.5" to 13.0"):**

*NO ETCH (rightmost):*
- Rounded rect, X: 16.0", W: 7.5", H: 3.0", fill `#1E2435`, left accent `#2EC4B6`
- Title: `NO ETCH` Barlow SemiBold 20 pt `#2EC4B6`
- `Skip to desmut (Stage 4)`
- `Preserves machined/polished finish`
- `Used for: fatigue-critical parts, tight tolerance, inspection surfaces`
- `Most common approach for Type I`

*LIGHT ETCH (center):*
- Rounded rect, X: 8.0", W: 7.5", H: 3.0", fill `#1E2435`, left accent `#E8A020`
- Title: `LIGHT ETCH` Barlow SemiBold 20 pt `#E8A020`
- `NaOH 20--40 g/L`
- `50--55 C (120--130 F)`
- `15--60 seconds`
- `Used for: moderate surface prep, slight matte acceptable`

*STANDARD ETCH (leftmost):*
- Rounded rect, X: 0.5", W: 7.0", H: 3.0", fill `#1E2435`, left accent `#E8A020` at 50%
- Title: `STANDARD ETCH` Barlow SemiBold 20 pt `#F0EDE8` at 70%
- `NaOH 40--60 g/L`
- `55--60 C (130--140 F)`
- `1--2 minutes`
- `Used for: when spec requires matte finish`
- `Less common for Type I`

---

### ZONE 4 -- Three Etch Approaches Detail

**Section label:** `WHY TYPE I MINIMIZES ETCHING` -- Y: 14.7".

Full-width callout, fill `#1E2435`, Y: 15.3" to 20.3":

Three key reasons in a row:

| Reason | Number | Text |
|---|---|---|
| Thin Coating | `1` | `The 0.5--2.5 um Type I coating does NOT hide surface irregularities. Heavy etching creates roughness the coating cannot smooth.` |
| Fatigue | `2` | `Type I is often applied to fatigue-critical parts. Metal removal must be minimized. Caustic etch removes 0.5--1.0 mil/min -- unacceptable for precision components.` |
| Inspection | `3` | `Type I coating is used as an inspection tool. The thin, translucent coating reveals substrate defects. Heavy etching removes the evidence.` |

Each: Rounded rect W: 7.33", H: 4.5", fill `#252B3D`.
Number: Large Barlow Condensed ExtraBold 48 pt `#E8A020` at 30%.
Body: Inter Regular 13 pt `#F0EDE8`, line height 155%.

---

### ZONE 5 -- Alloy Behavior + Chemistry

**Two-column layout (Y: 20.7" to 26.3"):**

**Left -- Alloy-Specific Etch Behavior (X: 0.5", W: 13.0"):**

Section label: `ALLOY BEHAVIOR IN ETCH` Barlow Condensed ExtraBold 22 pt.

| Alloy | Etch Recommendation | Notes |
|---|---|---|
| 6061 / 6063 | Standard or light etch | Uniform matte; 1--2 min if etching |
| 2024 | Light etch or NO etch | Heavy copper smut; difficult to remove before thin coating |
| 7075 | Light etch recommended | Zinc + copper smut; shorter time |
| Cast (high Si) | Not typical for Type I | If attempted, mechanical prep preferred |

Header: Barlow SemiBold 13 pt on `#3A4055`. Data: Inter Regular 12 pt.

**Right -- The Etch Reaction (X: 14.0", W: 9.5"):**

Callout box, fill `#1E2435`, left accent `#E8A020`:
- Title: `THE ETCH REACTION` Barlow SemiBold 18 pt `#E8A020`
- Formula: `2Al + 2NaOH + 2H2O --> 2NaAlO2 + 3H2` JetBrains Mono 14 pt `#F0EDE8`
- `Hydrogen gas evolution is vigorous` Inter Medium 13 pt `#E05C5C`
- `Adequate ventilation is essential` Inter Medium 13 pt `#E05C5C`
- Separator line
- `Monitor dissolved Al in etch bath` Inter Regular 13 pt `#F0EDE8` at 80%
- `> 50 g/L = sluggish etch -- partial dump` JetBrains Mono 12 pt `#E8A020`

---

### ZONE 6 -- Defect Grid + Key Principles

**Left -- Defect Grid (X: 0.5", W: 14.0", 2x2):**

Section label: `WHAT GOES WRONG -- 4 ETCH FAILURES`

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | OVER-ETCHING | `#E05C5C` | Too long, too hot, too concentrated | Reduce time; verify temperature |
| R1C2 | DIMENSIONAL LOSS | `#E05C5C` | Metal removal on precision parts | Switch to no-etch or light etch approach |
| R2C1 | HEAVY SMUT (2024) | `#E8A020` | Copper residue from caustic etch | Use light etch; aggressive desmut follows |
| R2C2 | SURFACE ROUGHNESS | `#E8A020` | Etch reveals grain boundaries | Expected on some alloys; minimize etch time |

**Right -- Key Principle (X: 15.0", W: 8.5"):**

Amber-tinted callout:
- Title: `THE TYPE I RULE` Barlow Condensed ExtraBold 24 pt `#E8A020`
- `When in doubt, skip the etch.` Inter Medium 18 pt `#F0EDE8`
- `A clean, desmutted surface produces better Type I results than an over-etched one.` Inter Regular 14 pt `#F0EDE8` at 80%
- `The thin coating is your inspection tool -- let it reveal the surface, not the etch damage.` Inter Regular 14 pt `#E8A020`

---

### ZONE 7 -- Footer

Standard. Title: `Etch -- Chromic Acid Anodizing (Type I)`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Etch Type I -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster is unique in the series because its hero message is "maybe don't do this step at all." The decision tree hero visual is unusual and engaging -- it guides the reader through the logic rather than just listing parameters. The three-reason panel below (thin coating / fatigue / inspection) gives the "why" that makes the decision tree stick. For a shop that processes both Type I and Type II, this poster clarifies why the etch step is handled so differently.

---

*Alaina -- Plating Posters Inc*
*Poster #298 -- Construction Workup v1.0*
*2026-04-26*
