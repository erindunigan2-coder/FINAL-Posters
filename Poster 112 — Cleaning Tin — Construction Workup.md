---
Project: Plating Posters Inc
Poster Number: 112
Title: "Cleaning -- Tin"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Process Scope: Cleaning stage for acid tin plating (Stage 1 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - TinPlating
  - Cleaning
  - ConstructionWorkup
  - Series2
  - ClusterEP11
---

# Poster #112 -- Construction Workup
## Cleaning -- Tin

*Alaina -- Plating Posters Inc*
*v1.0 -- 2026-04-26*

Stage 1 of 8. Tin is plated on a wider range of substrates than most processes -- copper, brass, steel, and nickel-plated parts all come through the line. Each substrate has different cleaning needs. Copper and brass (the most common tin substrates for electronics) are softer metals that require milder cleaning than steel. This poster covers all substrate paths.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Substrate-specific cleaning flowchart (Block B -- HERO):** Three parallel paths (copper/brass, steel, electronics) converging at the rinse stage. Built with rounded rectangles and branching arrows.
2. **Parameter table (Block D):** Cleaning parameters by substrate type.
3. **Cleaner chemistry callout (Block E):** What goes into the cleaner and why it matters for tin.
4. **Common mistakes strip (Block F):** 4 cleaning mistakes that cause tin plating defects downstream.

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
  Stage 1 highlighted (Teal)
ZONE 3 -- SUBSTRATE CLEANING PATHS HERO (4.2"--15.5" / ~11.3")
ZONE 4 -- CLEANING PARAMETER TABLE (15.5"--22.0" / ~6.5")
ZONE 5 -- CLEANER CHEMISTRY CALLOUT (22.0"--28.5" / ~6.5")
ZONE 6 -- COMMON MISTAKES (28.5"--32.5" / ~4.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CLEANING` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Tin Plating -- Stage 1 of 8` -- 36 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `Every tin defect starts with a dirty part. Clean it right or plate it wrong -- there is no middle ground.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Y: 2.9" to 4.2". Eight small boxes representing the 8-stage process.

Stage 1 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Oily, oxidized substrate  -->  After: Water-break-free surface ready for activation`

---

### ZONE 3 -- Substrate Cleaning Paths (HERO)

**Section label:** `CLEANING BY SUBSTRATE -- THREE PATHS` -- Y: 4.4".

**BLOCK B -- Three Parallel Cleaning Paths**

Y: 5.0" to 15.0". Three vertical columns, each a different substrate path.

| Column | X | W | Substrate | Accent |
|---|---|---|---|---|
| Left | 0.5" | 7.33" | Copper / Brass | `#E8A020` (Amber) |
| Center | 8.16" | 7.33" | Steel | `#2EC4B6` (Teal) |
| Right | 15.83" | 7.67" | Electronics / Connectors | `#27AE60` (Emerald) |

Each column contains 3--4 vertically stacked step boxes with downward arrows.

**Copper/Brass Path (most common for tin):**

Step 1: `Alkaline Soak Clean`
- `Mild alkaline, 3--6 oz/gal`
- `130--160 F (54--71 C), 3--5 min`
- `Non-etch formula -- copper is soft`

Step 2: `Rinse`
- `Ambient, flowing`

Step 3: `Acid Dip`
- `5--10% H2SO4, ambient`
- `15--30 sec`
- `Removes light tarnish and oxides`

Step 4: `Rinse` -> `TO TIN PLATE`

**Steel Path:**

Step 1: `Alkaline Soak Clean`
- `Standard alkaline, 4--8 oz/gal`
- `140--180 F (60--82 C), 3--10 min`

Step 2: `Rinse`

Step 3: `Electroclean`
- `Anodic, 3--6 V, 1--3 min`
- `Final soil removal`

Step 4: `Rinse`

Step 5: `Acid Activation`
- `HCl 10--20% or H2SO4 5--15%`
- `15--60 sec`

Step 6: `Rinse` -> `TO TIN PLATE`

**Electronics/Connectors Path:**

Step 1: `Mild Aqueous Clean`
- `Semi-aqueous or mild alkaline`
- `100--130 F (38--54 C), 1--3 min`
- `Residue-free critical`

Step 2: `Rinse (DI water)`

Step 3: `Mild Acid Dip`
- `5% H2SO4, 10--20 sec`

Step 4: `DI Rinse` -> `TO TIN PLATE`

Each step box: Rounded rect, fill `#1E2435`, left accent in column color, radius 6.
Step name: Barlow SemiBold 16 pt, accent color.
Parameters: JetBrains Mono 12 pt `#F0EDE8`.
Notes: Inter Regular 12 pt `#F0EDE8` at 70%.

---

### ZONE 4 -- Cleaning Parameter Table

**Section label:** `CLEANING PARAMETERS AT A GLANCE` -- Y: 15.7".

**BLOCK D -- Parameter Table**

Y: 16.3" to 21.5".

| Substrate | Cleaner Type | Concentration | Temp | Time | Notes |
|---|---|---|---|---|---|
| Copper/Brass | Mild alkaline soak | 3--6 oz/gal | 130--160 F | 3--5 min | Non-etch, non-silicated |
| Steel | Standard alkaline soak | 4--8 oz/gal | 140--180 F | 3--10 min | Heavier soil load |
| Steel (add) | Anodic electroclean | Per supplier | 140--160 F | 1--3 min | Removes smut and embedded soil |
| Nickel-plated | Mild alkaline soak | 2--4 oz/gal | 120--140 F | 2--3 min | Light touch -- protect Ni |
| Electronics | Mild aqueous / semi-aqueous | Per supplier | 100--130 F | 1--3 min | Residue-free mandatory |

Header: `#3A4055`. Alternating rows: `#1E2435` / `#252B3D`.

---

### ZONE 5 -- Cleaner Chemistry Callout

**Section label:** `WHAT IS IN THE CLEANER -- AND WHAT MATTERS FOR TIN` -- Y: 22.2".

**BLOCK E -- Two-Panel Callout**

Y: 22.9" to 28.3".

**Left Panel -- Cleaner Components:**
- Rounded rect, X: 0.5", W: 11.0", H: 5.2", fill `#1E2435`, left accent `#2EC4B6`
- Title: `ALKALINE CLEANER COMPONENTS` Barlow SemiBold 18 pt `#2EC4B6`

| Component | Function |
|---|---|
| NaOH / KOH | Saponifies oils, provides alkalinity |
| Surfactants | Emulsify non-saponifiable oils |
| Chelators | Complex hard water ions |
| Phosphates | Water conditioning, buffering |
| Inhibitors | Prevent copper/brass attack |

**Right Panel -- Critical Rules for Tin:**
- Rounded rect, X: 12.0", W: 11.5", H: 5.2", fill `#1E2435`, left accent `#E8A020`
- Title: `RULES FOR TIN SUBSTRATES` Barlow SemiBold 18 pt `#E8A020`

Rules list (Inter Medium 14 pt `#F0EDE8`, line height 160%):
- `Non-silicated cleaners only -- silicate films cause skip plating`
- `Low alkalinity for copper/brass -- prevent etch attack`
- `No excessive soak time on copper -- surface roughening`
- `Electroclean is optional for copper -- required for heavy steel soil`
- `Water-break-free test is the ONLY acceptance criterion`

Bottom note: `If the part is not water-break-free, it is not clean. Period.` Inter Medium 14 pt `#E05C5C`

---

### ZONE 6 -- Common Mistakes

**Section label:** `4 CLEANING MISTAKES THAT RUIN TIN DEPOSITS` -- Y: 28.7".

**BLOCK F -- Four Mistake Cards**

Y: 29.4" to 32.3". Same format as process flow poster.

| Card | X | Mistake | Result | Fix |
|---|---|---|---|---|
| 1 | 0.5" | SILICATED CLEANER | Skip plating, bare spots | Switch to non-silicated formula |
| 2 | 6.33" | OVER-ETCHING COPPER | Rough substrate, grainy tin | Reduce temp, time, or alkalinity |
| 3 | 12.16" | SKIPPING ACID DIP | Oxide film remains, poor adhesion | Always acid dip copper/brass |
| 4 | 18.0" | POOR RINSE AFTER CLEAN | Alkaline drag-in, pH spike in acid bath | Improve rinse flow and time |

---

### ZONE 7 -- Footer

Standard. Title: `Cleaning -- Tin`. Version `v1.0 -- 2026`.

Disclaimer: `Process parameters shown are typical industry values for cleaning prior to acid tin plating. Consult your process supplier for application-specific guidance.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cleaning Tin -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Tin plating serves a wider substrate range than most processes -- the three-path hero visual makes this immediately clear. Copper/brass is the dominant substrate in electronics tin plating. The "non-silicated cleaner" rule is one of the most commonly violated rules in acid plating shops. Call it out hard.

---

*Alaina -- Plating Posters Inc*
*Poster #112 -- Construction Workup v1.0*
*2026-04-26*
