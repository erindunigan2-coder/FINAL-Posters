---
Project: Plating Posters Inc
Poster Number: 362
Title: "Neutralization & Secondary Treatment -- Carbon Steel"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Chemical Treatment Clusters -- Watson Research Brief (CT-3.6)"
Technical Source: Industry-standard secondary treatments after acid pickling of carbon steel. Covers acid activation dip, complex part rinsing, environmental disposal, and hydrogen embrittlement bake protocol.
Process Scope: Neutralization and secondary treatment after carbon steel pickling
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - AcidPickling
  - CarbonSteel
  - Neutralization
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT03
---

# Poster #362 -- Construction Workup
## Neutralization & Secondary Treatment -- Carbon Steel

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This poster covers everything between the pickle rinse and the next major process step. The hero is a decision flowchart: does this part need a neutralizing rinse? An acid activation dip? An H-embrittlement bake? The environmental section covers spent acid disposal -- a topic every shop manager needs but few operators understand. The H-embrittlement bake protocol gets repeated here because Watson flagged it as "so critical it bears repeating."

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Decision flowchart (Block B -- HERO):** Simple yes/no decision tree determining next steps after pickle rinse.
2. **Acid activation dip reference (Block D):** Quick-reference parameters.
3. **Environmental disposal section (Block E):** Spent acid handling, discharge limits.
4. **H-embrittlement bake protocol (Block F):** ASTM B849 requirements -- repeated from Poster #357 for standalone reference.
5. **Print size -- 24x36".**

---

## Part 2 -- Document Setup Instructions

(Same as Poster #357: 24x36", `#1A1F2E` background, standard fonts, standard palette.)

### Step 5 -- Set ruler guides

**Horizontal guides:**
- 0.5" / 2.9" / 13.5" / 19.5" / 26.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- DECISION FLOWCHART / HERO (2.9"--13.5" / ~10.6" tall)
  Block B: Post-pickle decision tree

ZONE 3 -- ACID ACTIVATION DIP (13.5"--19.5" / ~6.0" tall)
  Block C: Section label
  Block D: Acid activation reference

ZONE 4 -- ENVIRONMENTAL DISPOSAL (19.5"--26.0" / ~6.5" tall)
  Block E: Spent acid handling and discharge limits

ZONE 5 -- H-EMBRITTLEMENT BAKE PROTOCOL (26.0"--32.5" / ~6.5" tall)
  Block F: ASTM B849 bake requirements

ZONE 6 -- FOOTER BAND (32.5"--36.0" / ~3.5" tall)
  Block G: Disclaimer + poster title + series name + logo + version
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**BLOCK A -- Headline**
- Barlow Condensed ExtraBold, 80 pt, `#F0EDE8`, letter spacing -4
- Text: `NEUTRALIZATION & SECONDARY`

**BLOCK A -- Subheading**
- Barlow SemiBold, 36 pt, `#E8A020` (Amber)
- Text: `Carbon Steel -- What Comes After the Pickle`

**BLOCK A -- Tagline**
- Barlow SemiBold, 22 pt, `#F0EDE8` at 65%
- Text: `The pickle stripped the scale. Now protect the surface, bake out hydrogen, and dispose of the acid responsibly.`

---

### ZONE 2 -- Decision Flowchart (HERO)

**Section label:**
- Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `POST-PICKLE DECISION TREE`

---

**BLOCK B -- Decision Flowchart**

Y: 3.8" to 13.0". Flow runs top-to-bottom with yes/no branches.

Start node:
- Rounded rect, X: 8.5", Y: 3.8", W: 7.0", H: 1.2", fill `#2EC4B6`, radius 8
- Text: `PART EXITS PICKLE RINSE` -- Barlow SemiBold, 18 pt, `#1A1F2E`, center

Decision 1 (Y: 5.5"):
- Diamond shape (rotated square), center X: 12.0", W/H: 2.5", fill `#1E2435`, border 2 pt `#E8A020`
- Text: `Complex geometry?` -- Inter Medium, 14 pt, `#F0EDE8`
- YES arrow (left): leads to Neutralizing Rinse box
- NO arrow (down): leads to Decision 2

Neutralizing Rinse box (left branch):
- Rounded rect, X: 0.5", Y: 5.0", W: 5.5", H: 2.5", fill `#1E2435`, left accent `#E8A020`
- Title: `NEUTRALIZING RINSE` -- Barlow SemiBold, 16 pt, `#E8A020`
- Params: `1--3% NaHCO3, ambient, 30--60 sec` -- JetBrains Mono, 12 pt
- Note: `Then clean water rinse` -- Inter Regular, 12 pt
- Arrow reconnects to Decision 2

Decision 2 (Y: 8.5"):
- Diamond, center X: 12.0", fill `#1E2435`, border 2 pt `#E05C5C`
- Text: `Steel >= 40 HRC?` -- Inter Medium, 14 pt, `#F0EDE8`
- YES arrow (left): leads to H-Embrittlement Bake box
- NO arrow (down): leads to Decision 3

H-Embrittlement Bake box (left branch):
- Rounded rect, X: 0.5", Y: 8.0", W: 5.5", H: 2.5", fill `#1E2435`, left accent `#E05C5C`
- Title: `BAKE -- MANDATORY` -- Barlow SemiBold, 16 pt, `#E05C5C`
- Params: `375--410 F, 8--24 hrs` / `Within 4 hrs of exposure` -- JetBrains Mono, 12 pt
- Note: `Per ASTM B849` -- Inter Medium, 12 pt, `#E05C5C`
- Arrow reconnects to Decision 3

Decision 3 (Y: 11.5"):
- Diamond, center X: 12.0", fill `#1E2435`, border 2 pt `#2EC4B6`
- Text: `Proceeding to plate?` -- Inter Medium, 14 pt, `#F0EDE8`
- YES arrow (right): leads to Acid Activate box
- NO arrow (down): leads to Hold box

Acid Activate box (right branch):
- Rounded rect, X: 17.0", Y: 11.0", W: 6.5", H: 2.0", fill `#1E2435`, left accent `#27AE60`
- Title: `ACID ACTIVATE` -- Barlow SemiBold, 16 pt, `#27AE60`
- Params: `3--10% HCl or H2SO4, ambient, 15--30 sec` -- JetBrains Mono, 12 pt
- Arrow: `PROCEED TO PLATING` -- Inter Medium, 14 pt, `#27AE60`

Hold box (bottom):
- Rounded rect, X: 8.5", Y: 13.0", W: 7.0", H: 1.0", fill `#1E2435`, border 1 pt `#E8A020`
- Text: `HOLD in dilute acid (1--3%) until ready` -- Inter Medium, 14 pt, `#E8A020`

---

### ZONE 3 -- Acid Activation Dip

**Section label:**
- Centered. Y: 13.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `ACID ACTIVATION DIP -- REFRESHING THE SURFACE`

**Sublabel:**
- Centered. Y: 14.2". Inter Regular, 16 pt, `#F0EDE8` at 60%
- Text: `This is NOT pickling. It is a brief dip to remove the thin oxide that forms in seconds on clean steel.`

---

**BLOCK D -- Activation Reference**

- Rounded rect, X: 0.5", Y: 15.0", W: 23.0", H: 4.0", fill `#1E2435`, radius 6
- Left accent: `#27AE60`, 0.06"

Two-column layout:

Left -- Parameters (JetBrains Mono, 15 pt, `#F0EDE8`):
```
Acid:           HCl 3--10% or H2SO4 3--10%
Temperature:    Ambient
Time:           15--30 seconds
Agitation:      Gentle movement of parts
```

Right -- Key Points (Inter Regular, 14 pt, `#F0EDE8`):
```
- Refreshes the oxide-free surface just before plating
- Also called "acid dip" or "acid activate"
- Must be followed immediately by plating
- Do NOT use the same tank as the pickle bath
  (contaminated with dissolved iron)
```

---

### ZONE 4 -- Environmental Disposal

**Section label:**
- Centered. Y: 19.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `SPENT ACID DISPOSAL -- ENVIRONMENTAL COMPLIANCE`

---

**BLOCK E -- Disposal Reference**

Y: 20.5" to 25.8". Two side-by-side callout boxes.

**Left -- Spent HCl:**
- Rounded rect, X: 0.5", Y: 20.5", W: 11.0", H: 5.0", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `SPENT HCl PICKLE` -- Barlow SemiBold, 18 pt, `#E8A020`

Content (Inter Regular, 13 pt, `#F0EDE8`):
```
- Typically sent to acid reclamation
  (roasting recovers HCl + iron oxide)
- If no reclaimer: neutralize with
  lime or NaOH
- pH adjust to 6--9 before discharge
- Iron discharge limit: typically
  1--5 mg/L in municipal permits
```

**Right -- Spent H2SO4:**
- Rounded rect, X: 12.0", Y: 20.5", W: 11.5", H: 5.0", fill `#1E2435`
- Left accent: `#2EC4B6`, 0.06"
- Title: `SPENT H2SO4 PICKLE` -- Barlow SemiBold, 18 pt, `#2EC4B6`

Content:
```
- Neutralize with lime; iron sulfate
  precipitates as sludge
- pH adjust to 6--9 before discharge
- Pickle sludge: characterize for RCRA
  hazardous waste
- Typically non-hazardous but check
  TCLP metals if alloy steels were pickled
```

**Spanning callout:**
- Rounded rect, X: 0.5", Y: 25.2", W: 23.0", H: 0.6", fill `#E8A020` at 12%, border 1 pt `#E8A020`
- Text: `Check your local discharge permit. Limits vary by municipality. When in doubt, call your waste hauler.` -- Inter Medium, 13 pt, `#E8A020`, center

---

### ZONE 5 -- H-Embrittlement Bake Protocol

**Section label:**
- Centered. Y: 26.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `HYDROGEN EMBRITTLEMENT BAKE -- ASTM B849`

**Sublabel:**
- Centered. Y: 26.7". Inter Regular, 16 pt, `#E05C5C`
- Text: `This is so critical it appears on this poster AND on the Process Flow poster. Non-negotiable for high-strength steel.`

---

**BLOCK F -- Bake Requirements**

- Rounded rect, X: 0.5", Y: 27.4", W: 23.0", H: 4.8", fill `#E05C5C` at 8%, border 2 pt `#E05C5C`, radius 8

Content layout -- 3 columns:

Column 1 -- When (W: 7.0"):
- Barlow SemiBold, 16 pt, `#E05C5C`: `WHEN:`
- Inter Regular, 14 pt, `#F0EDE8`:
```
- Any steel >= 40 HRC that has been
  acid pickled
- Within 4 hours of the LAST
  hydrogen-generating step
- Required by ASTM B849, AS9100D,
  NADCAP, automotive, and fastener specs
```

Column 2 -- How (W: 8.0"):
- Barlow SemiBold, 16 pt, `#E8A020`: `HOW:`
- JetBrains Mono Regular, 14 pt, `#F0EDE8`:
```
Temperature: 375--410 F (190--210 C)
Duration:    4--24 hrs (hardness-dependent)
  31--39 HRC: 4--8 hrs
  40--50 HRC: 8--24 hrs
  > 50 HRC:  Avoid acid pickle entirely
```

Column 3 -- Why (W: 7.0"):
- Barlow SemiBold, 16 pt, `#2EC4B6`: `WHY:`
- Inter Regular, 14 pt, `#F0EDE8`:
```
- Hydrogen atoms absorbed during
  pickling migrate to grain boundaries
- Under stress, hydrogen causes
  delayed brittle fracture
- Baking drives hydrogen out of the
  lattice before it causes damage
```

---

### ZONE 6 -- Footer Band

(Same structure as Poster #357.)

**Disclaimer:**
> This poster is an educational reference tool. Bake requirements per ASTM B849 are shown as general guidance. Specific bake times and temperatures depend on steel grade, hardness, part geometry, and customer specification. Always consult the applicable specification and your quality engineer.

**Poster title:** `Neutralization & Secondary Treatment -- Carbon Steel`

**Version:** `v1.0 -- 2026`

---

## Part 5 -- Grouping and Naming Convention

| Group Name | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline |
| Zone 2 - Decision Flow | Section label, decision flowchart |
| Zone 3 - Acid Activate | Section label, sublabel, activation reference |
| Zone 4 - Environmental | Section label, HCl disposal, H2SO4 disposal, spanning callout |
| Zone 5 - Bake Protocol | Section label, sublabel, 3-column bake reference |
| Zone 6 - Footer | Footer band, disclaimer, title, series, logo, version |

---

## Part 6 -- Light Edition Color Remap Table

(Same remap table as Poster #357.)

---

## Part 7 -- Export Checklist

| File Name | Mode | Quality | Bleed |
|---|---|---|---|
| `Neutralization Steel -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Neutralization Steel -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Neutralization Steel -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Neutralization Steel -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Neutralization Steel -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Neutralization Steel -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

The decision flowchart is the star of this poster. A foreman looks at this and instantly knows: complex geometry? neutralize. High-strength steel? bake. Going to plate? activate. The flowchart replaces the mental checklist that experienced platers carry in their heads and novice platers do not yet have. The environmental section is included because spent pickle is one of the most common waste streams in a plating shop and the regulatory landscape is not optional.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #362 -- Construction Workup v1.0*
*2026-04-26*
