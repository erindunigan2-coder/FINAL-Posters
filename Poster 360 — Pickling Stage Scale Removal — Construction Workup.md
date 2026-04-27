---
Project: Plating Posters Inc
Poster Number: 360
Title: "Pickling Stage -- Scale Removal (Carbon Steel)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Chemical Treatment Clusters -- Watson Research Brief (CT-3.4)"
Technical Source: Industry-standard operating parameters and chemistry for the acid pickling stage of carbon steel. Covers HCl and H2SO4 operating windows, scale types, dissolution chemistry, and common failures.
Process Scope: Acid pickling treatment stage -- carbon steel scale removal
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - AcidPickling
  - CarbonSteel
  - PicklingStage
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT03
---

# Poster #360 -- Construction Workup
## Pickling Stage -- Scale Removal (Carbon Steel)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the main treatment poster -- the tank where the work happens. The hero is a side-by-side operating parameter comparison (HCl vs. H2SO4). A scale-type reference table helps operators match their incoming material to the right approach. The dissolution chemistry reactions are shown in a clean, readable format -- operators do not need to be chemists, but understanding "acid eats oxide AND base metal" is critical. A failure mode grid rounds out the reference.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Operating parameter comparison (Block B -- HERO):** Side-by-side HCl vs. H2SO4 parameter cards.
2. **Scale type table (Block D):** 4-row table keyed by scale description and difficulty.
3. **Dissolution chemistry (Block E):** Chemical equations in JetBrains Mono with plain-language explanations.
4. **Failure mode grid (Block F):** 5 failure cards in a strip.
5. **Print size -- 24x36".**

---

## Part 2 -- Document Setup Instructions

(Same as Poster #357: 24x36", `#1A1F2E` background, standard fonts, standard palette.)

### Step 5 -- Set ruler guides

**Horizontal guides:**
- 0.5" / 2.9" / 14.0" / 20.5" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- OPERATING PARAMETERS / HERO (2.9"--14.0" / ~11.1" tall)
  Block B: HCl operating card (left)
  Block C: H2SO4 operating card (right)

ZONE 3 -- SCALE TYPES (14.0"--20.5" / ~6.5" tall)
  Block D: Scale type identification table

ZONE 4 -- DISSOLUTION CHEMISTRY (20.5"--27.0" / ~6.5" tall)
  Block E: Chemical reactions + plain-language explanation

ZONE 5 -- FAILURE MODES (27.0"--32.5" / ~5.5" tall)
  Block F: 5 failure mode cards

ZONE 6 -- FOOTER BAND (32.5"--36.0" / ~3.5" tall)
  Block G: Disclaimer + poster title + series name + logo + version
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**BLOCK A -- Headline**
- Barlow Condensed ExtraBold, 88 pt, `#F0EDE8`, letter spacing -4
- Text: `PICKLING STAGE`

**BLOCK A -- Subheading**
- Barlow SemiBold, 36 pt, `#E8A020` (Amber)
- Text: `Scale Removal -- Carbon Steel`

**BLOCK A -- Tagline**
- Barlow SemiBold, 22 pt, `#F0EDE8` at 65%
- Text: `The acid dissolves the oxide. The inhibitor saves the metal. Time and temperature are your levers.`

---

### ZONE 2 -- Operating Parameters (HERO)

**Section label:**
- Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `OPERATING PARAMETERS -- HCL VS. H2SO4`

---

**BLOCK B -- HCl Operating Card (Left)**

- Rounded rect, X: 0.5", Y: 3.8", W: 11.0", H: 9.7", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `HCl PICKLE` -- Barlow SemiBold, 24 pt, `#E8A020`

Parameter rows (JetBrains Mono Regular, 15 pt, `#F0EDE8`, line height 180%):
```
Temperature     68--95 F (20--35 C)
                AMBIENT -- no heating required

Concentration   15--30% v/v

Time            5--30 min
                (scale-dependent)

Agitation       None to mild

Iron Capacity   ~200 g/L FeCl2
```

Advantage callout:
- Rounded rect, fill `#E8A020` at 12%, border 1 pt `#E8A020`
- Text: `Faster at room temp. Good on all scale types including tight mill scale.` -- Inter Medium, 13 pt, `#E8A020`

Disadvantage callout:
- Rounded rect, fill `#E05C5C` at 10%, border 1 pt `#E05C5C`
- Text: `HIGH fume generation -- requires local exhaust ventilation at ALL times.` -- Inter Medium, 13 pt, `#E05C5C`

**BLOCK C -- H2SO4 Operating Card (Right)**

- Rounded rect, X: 12.0", Y: 3.8", W: 11.5", H: 9.7", fill `#1E2435`
- Left accent: `#2EC4B6`, 0.06"
- Title: `H2SO4 PICKLE` -- Barlow SemiBold, 24 pt, `#2EC4B6`

```
Temperature     120--175 F (50--80 C)
                REQUIRES HEATING

Concentration   10--25% v/v

Time            10--45 min
                (scale-dependent)

Agitation       Mild air agitation
                improves uniformity

Iron Capacity   ~120 g/L FeSO4
```

Advantage callout:
- Text: `Low fume generation. Lower acid cost per gallon. Better on heavy, thick scale.` -- Inter Medium, 13 pt, `#2EC4B6`

Disadvantage callout:
- Text: `Slower at room temp. Higher H-embrittlement risk (longer exposure + heat).` -- Inter Medium, 13 pt, `#E05C5C`

---

### ZONE 3 -- Scale Types

**Section label:**
- Centered. Y: 14.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `SCALE TYPE IDENTIFICATION`

**Sublabel:**
- Centered. Y: 14.7". Inter Regular, 16 pt, `#F0EDE8` at 60%
- Text: `Match the incoming scale to the right approach. Heavy scale = longer time or mechanical pre-treatment.`

---

**BLOCK D -- Scale Type Table**

Y: 15.5" to 20.3". Column widths (23.0" total):
- Scale Type (5.0") | Description (6.0") | Difficulty (3.5") | Preferred Acid (4.0") | Notes (4.5")

Header row: Rectangle fill `#3A4055`, H: 0.5".

| Scale Type | Description | Difficulty | Preferred | Notes |
|---|---|---|---|---|
| Mill scale (FeO/Fe2O3/Fe3O4) | Blue-black tight oxide from hot rolling | Difficult | HCl preferred | May need mechanical pre-treatment |
| Weld scale | Discolored zone around welds; mixed oxides | Moderate | Either acid | Responds well to both |
| Light rust (hydrated Fe2O3) | Red/brown surface oxide | Easy | Either acid | Any acid removes quickly |
| Heat-treat scale | From hardening, tempering, stress relief | Moderate--Difficult | Inhibited pickle | Often requires longer soak |

Difficulty color coding:
- Easy: `#27AE60`
- Moderate: `#E8A020`
- Difficult: `#E05C5C`

---

### ZONE 4 -- Dissolution Chemistry

**Section label:**
- Centered. Y: 20.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `WHAT HAPPENS IN THE TANK`

---

**BLOCK E -- Chemical Reactions**

Two side-by-side callout boxes:

**Left -- HCl Reactions:**
- Rounded rect, X: 0.5", Y: 21.4", W: 11.0", H: 5.0", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `HCl DISSOLUTION` -- Barlow SemiBold, 18 pt, `#E8A020`

Reactions (JetBrains Mono Regular, 14 pt, `#F0EDE8`):
```
OXIDE:
Fe2O3 + 6HCl -> 2FeCl3 + 3H2O
(Dissolves the scale)

BASE METAL:
Fe + 2HCl -> FeCl2 + H2 (gas)
(This is what inhibitor reduces)
```

Plain-language note:
- Inter Regular, 13 pt, `#F0EDE8` at 70%
- Text: `The first reaction is desired -- oxide removal. The second is wasteful and dangerous -- it attacks good metal and generates explosive hydrogen gas.`

**Right -- H2SO4 Reactions:**
- Rounded rect, X: 12.0", Y: 21.4", W: 11.5", H: 5.0", fill `#1E2435`
- Left accent: `#2EC4B6`, 0.06"
- Title: `H2SO4 DISSOLUTION` -- Barlow SemiBold, 18 pt, `#2EC4B6`

```
OXIDE:
Fe2O3 + 3H2SO4 -> Fe2(SO4)3 + 3H2O
(Dissolves the scale)

BASE METAL:
Fe + H2SO4 -> FeSO4 + H2 (gas)
(This is what inhibitor reduces)
```

**Spanning callout:**
- Rounded rect, X: 0.5", Y: 26.0", W: 23.0", H: 0.7", fill `#E05C5C` at 12%, border 1 pt `#E05C5C`
- Text: `Both acids generate hydrogen gas from base metal attack. Inhibitor is not optional -- it reduces H2 generation by up to 90%.` -- Inter Medium, 14 pt, `#E05C5C`, center

---

### ZONE 5 -- Failure Modes

**Section label:**
- Centered. Y: 27.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`
- Text: `COMMON FAILURES`

---

**BLOCK F -- Five Failure Cards**

Y: 27.9" to 32.3". Five cards in a row. Card width: 4.3", gap: 0.25".

| Card | X | Failure | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | OVER-ETCH | Too long; acid too strong; no inhibitor | Reduce time; add inhibitor |
| 2 | 5.05" | UNDER-PICKLE | Acid spent; iron too high; temp low | Replenish acid; check iron |
| 3 | 9.6" | H-EMBRITTLEMENT | No inhibitor; no bake; high-strength steel | Inhibitor + bake per B849 |
| 4 | 14.15" | FLASH RUST | Delay after pickle | Rinse immediately; move fast |
| 5 | 18.7" | BLACK SMUT | Iron redeposited; poor rinse | Check iron; improve rinse |

Each card: Rounded rect, H: 4.0", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

Interior:
- Failure: Barlow SemiBold, 15 pt, `#E05C5C`
- Cause: Inter Regular, 12 pt, `#F0EDE8`
- Fix: Inter Medium, 12 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

(Same structure as Poster #357.)

**Disclaimer:**
> This poster is an educational reference tool. Operating parameters shown are typical industry values for acid pickling of carbon steel. Specific process limits vary by proprietary product and application. Consult your process supplier for guidance.

**Poster title:** `Pickling Stage -- Scale Removal (Carbon Steel)`

**Version:** `v1.0 -- 2026`

---

## Part 5 -- Grouping and Naming Convention

| Group Name | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline |
| Zone 2 - Operating Params | Section label, HCl card, H2SO4 card |
| Zone 3 - Scale Types | Section label, sublabel, scale type table |
| Zone 4 - Chemistry | Section label, HCl reactions, H2SO4 reactions, spanning callout |
| Zone 5 - Failures | Section label, five failure cards |
| Zone 6 - Footer | Footer band, disclaimer, title, series, logo, version |

---

## Part 6 -- Light Edition Color Remap Table

(Same remap table as Poster #357.)

---

## Part 7 -- Export Checklist

| File Name | Mode | Quality | Bleed |
|---|---|---|---|
| `Pickling Stage Scale Removal Steel -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Pickling Stage Scale Removal Steel -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Pickling Stage Scale Removal Steel -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Pickling Stage Scale Removal Steel -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Pickling Stage Scale Removal Steel -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Pickling Stage Scale Removal Steel -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

The chemistry reactions section is educational gold. Most shop floor workers have never seen the actual equations -- but when you show them "Fe + 2HCl -> FeCl2 + H2" and say "that H2 is what makes parts brittle and also what makes the tank explode," the light goes on. The plain-language annotations below each equation are what make this poster work for a high school education level.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #360 -- Construction Workup v1.0*
*2026-04-26*
