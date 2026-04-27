---
Project: Plating Posters Inc
Poster Number: 106
Title: "Activation -- Copper (Alkaline)"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Process Scope: Activation / acid dip for alkaline non-cyanide copper plating line (Stage 3 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - CopperPlating
  - AlkalineCopper
  - NonCyanide
  - Activation
  - ConstructionWorkup
  - Series2
  - ClusterEP10
---

# Poster #106 -- Construction Workup
## Activation -- Copper (Alkaline)

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 3 of the alkaline non-cyanide copper process. This is the highest-risk step in the entire EP-10 cluster. Activation for alkaline copper strike is intensely substrate-dependent, and the margin for error on zinc die castings is razor-thin.

- **Steel:** Standard HCl dip (10--30%, 15--30 sec). Forgiving.
- **Zinc die cast:** Mild HCl (1--3%, 5--10 sec MAXIMUM). Over-etching the zinc substrate is the #1 cause of adhesion failure. The acid removes the thin zinc oxide layer -- but too much acid dissolves zinc itself, creating a porous, weakened surface that the copper strike cannot bond to.
- **Brass:** Mild H2SO4 (5--10%, 15--30 sec).
- **Stainless steel:** May require cathodic alkaline activation or Wood's nickel strike first.

Hero visual: substrate activation matrix with a prominent "danger zone" callout for zinc die castings.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Substrate activation matrix hero (Block B):** Same format as Poster #98 but with zinc die cast prominently featured.
2. **Orientation strip (Block C):** Stage 3 highlighted.
3. **Activation parameter table (Block D).**
4. **Zinc die cast danger zone callout (Block E):** Large coral-bordered warning.
5. **Problems + Safety.**

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.0" / 20.5" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 3 highlighted
ZONE 3 -- SUBSTRATE ACTIVATION HERO (4.2"--14.0")
ZONE 4 -- ACTIVATION PARAMETERS (14.0"--20.5")
ZONE 5 -- ZINC DC DANGER ZONE + PROBLEMS (20.5"--27.0")
ZONE 6 -- SAFETY (27.0"--32.5")
ZONE 7 -- FOOTER (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `ACTIVATION` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".

**Subheading:** `Copper (Alkaline) -- Stage 3 of 8` -- 34 pt `#E8A020`. Y: 1.4".

**Tagline:** `Five seconds too long in the acid dip and the zinc die casting is ruined. This is the step where adhesion is won or lost.` -- 20 pt at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 3 highlighted (fill `#E8A020`). Others dimmed.

Below strip: `Before: Clean, rinsed surface  -->  After: Oxide-free, activated -- ready for copper strike`

---

### ZONE 3 -- Substrate Activation Hero

**Section label:** `ACTIVATION BY SUBSTRATE -- CRITICAL DIFFERENCES` -- Y: 4.4".

**BLOCK B -- Substrate Cards (Y: 5.0" to 13.5")**

Four substrate rows, each a rounded rect card (full width, H: 1.8", fill `#1E2435`):

**Row 1 -- Steel (X: 0.5", Y: 5.0"):**
- Left accent: `#2EC4B6`
- Substrate: `STEEL` -- Barlow SemiBold 20 pt `#2EC4B6`
- Acid: `10--30% HCl, ambient, 15--30 sec` -- JetBrains Mono 14 pt
- Note: `Standard activation. Most forgiving substrate for this process.`
- Risk level: `LOW` -- Inter Medium 14 pt `#27AE60`

**Row 2 -- Zinc Die Cast (X: 0.5", Y: 7.0"):**
- Left accent: `#E05C5C`
- Border: 2 pt `#E05C5C` (extra emphasis)
- Substrate: `ZINC DIE CAST` -- Barlow SemiBold 22 pt `#E05C5C`
- Acid: `1--3% HCl, ambient, 5--10 sec MAXIMUM` -- JetBrains Mono 16 pt `#E05C5C`
- Note: `THE CRITICAL STEP. Over-etching dissolves zinc, creates porous surface, destroys adhesion. Time this with a stopwatch.`
- Risk level: `EXTREME -- this is where adhesion failures originate` -- Inter Medium 14 pt `#E05C5C`

**Row 3 -- Brass (X: 0.5", Y: 9.2"):**
- Left accent: `#E8A020`
- Substrate: `BRASS` -- Barlow SemiBold 20 pt `#E8A020`
- Acid: `5--10% H2SO4, ambient, 15--30 sec` -- JetBrains Mono 14 pt
- Note: `Light activation removes tarnish. Do not use HCl on brass (dezincification risk).`
- Risk level: `LOW TO MODERATE` -- `#E8A020`

**Row 4 -- Stainless Steel (X: 0.5", Y: 11.2"):**
- Left accent: `#3A4055`
- Substrate: `STAINLESS STEEL` -- Barlow SemiBold 20 pt `#C8D0D8`
- Acid: `Cathodic alkaline activation or Wood's Ni strike may be needed first` -- JetBrains Mono 14 pt
- Note: `Passive oxide film on stainless is difficult to activate. Alkaline non-CN copper alone may not achieve adequate adhesion. Consult process supplier.`
- Risk level: `HIGH -- requires special protocol` -- `#E8A020`

---

### ZONE 4 -- Activation Parameters

**Section label:** `ACTIVATION PARAMETERS -- DETAILED` -- Y: 14.2".

**Full-width table (X: 0.5", W: 23.0"):**

| Parameter | Steel | Zinc Die Cast | Brass |
|---|---|---|---|
| Acid type | HCl | HCl (dilute) | H2SO4 |
| Concentration | 10--30% v/v | 1--3% v/v | 5--10% v/v |
| Temperature | Ambient (65--85 F) | Ambient | Ambient |
| Time | 15--30 sec | 5--10 sec MAXIMUM | 15--30 sec |
| Agitation | None to mild | NONE (do not agitate) | None to mild |
| Purpose | Remove oxide, activate surface | Remove thin ZnO -- nothing more | Remove tarnish, activate |
| Key risk | Minimal | Over-etching dissolves zinc | Dezincification if HCl used |
| Transfer time | Normal | FAST -- enter strike within 30 sec | Normal |

**Below table:**
- `Zinc die cast rule: dip, count to 10, pull, rinse, into the strike. No exceptions.` -- Inter Medium 16 pt `#E05C5C`

---

### ZONE 5 -- Zinc DC Danger Zone + Problems

**BLOCK E -- Zinc Die Cast Danger Zone (Y: 20.7" to 23.5")**

Full-width callout, fill `#1E2435`, border 2 pt `#E05C5C`.

Title: `ZINC DIE CAST -- THE ACTIVATION DANGER ZONE` -- Barlow Condensed ExtraBold 24 pt `#E05C5C`

Two-column interior:

**Left -- What Happens If You Over-Etch:**
- `HCl attacks zinc metal, not just zinc oxide`
- `Surface becomes porous and spongy`
- `Copper strike deposits INTO pores, not ON surface`
- `Result: weak mechanical bond, not true adhesion`
- `Deposit peels under tape test, bending, or thermal cycling`

**Right -- How to Get It Right:**
- `Use 1--3% HCl only -- never stronger`
- `Time: 5--10 seconds maximum -- use a timer`
- `No agitation -- do not accelerate the etch`
- `Rinse immediately after activation`
- `Enter copper strike within 30 seconds of rinsing`
- `If in doubt, err on the short side -- 5 sec is better than 15`

Bottom rule: `Adhesion testing (ASTM B571 bend test) should be run on every new setup and after any process change.` Inter Medium 13 pt `#2EC4B6`

**BLOCK F -- Problem Table (Y: 23.8" to 26.8")**

| Problem | Cause | Fix |
|---|---|---|
| Copper peeling on zinc DC | Over-etching in acid dip | Reduce HCl to 1%; reduce time to 5 sec |
| Poor adhesion on steel | Under-activation (oxide still present) | Increase HCl concentration or time |
| Staining on brass | HCl dezincification | Switch to H2SO4 for brass |
| Re-oxidation before strike | Parts drying between rinse and strike | Minimize transfer time; keep parts wet |
| Pitting on zinc DC surface | Acid attack on porosity | Reduce acid concentration; improve cleaning |

---

### ZONE 6 -- Safety

**Left -- Acid Handling:**
- `HCl: corrosive, fumes, ventilation required`
- `H2SO4: corrosive, add acid to water`
- `Dilute acids still cause burns on prolonged contact`
- `Zinc + acid = H2 gas generation -- ensure ventilation`

**Right -- PPE:**
- `Chemical splash goggles or face shield`
- `Acid-resistant gloves`
- `Acid-resistant apron`
- `Local exhaust ventilation over HCl tanks`
- `Eyewash and emergency shower within 10 sec`

---

### ZONE 7 -- Footer

Standard. Title: `Activation -- Copper (Alkaline)`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones. **Light Remap:** Standard table. **Export:** Six files -- `Activation Copper Alkaline -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the most critical poster in the EP-10 cluster. The zinc die cast activation danger zone earns its full-width coral treatment because over-etching is the #1 failure mode in alkaline copper plating on zinc die castings. Every plating shop that processes zinc die castings has learned this lesson the hard way at least once. The poster should make the lesson stick without requiring a pile of rejected parts.

-> Tyler: Validate 1--3% HCl / 5--10 sec for zinc die cast activation before alkaline non-CN copper strike. This parameter is critical and comes from domain knowledge -- would benefit from lab validation or published source confirmation.

---

*Alaina -- Poster #106 -- Construction Workup v1.0 -- 2026-04-26*
