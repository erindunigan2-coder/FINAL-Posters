---
Project: Plating Posters Inc
Poster Number: 144
Title: "Cleaning -- Tin-Lead"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Process Scope: Cleaning stage for tin-lead plating (Stage 1 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - TinLeadPlating
  - Cleaning
  - ConstructionWorkup
  - Series2
  - ClusterEP15
---

# Poster #144 -- Construction Workup
## Cleaning -- Tin-Lead

*Alaina -- Plating Posters Inc*
*v1.0 -- 2026-04-26*

Stage 1 of 8. Tin-lead plating is predominantly applied to copper, copper alloys, and nickel-plated substrates in electronics manufacturing. The cleaning requirements are lighter than steel plating lines but demand absolute residue freedom -- ionic contamination on PCBs or connectors causes field failures. This poster covers substrate-specific cleaning paths for tin-lead applications: copper/brass components, PCB panels (conveyorized), and discrete rack-plated parts.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Substrate-specific cleaning flowchart (Block B -- HERO):** Three parallel paths (copper/brass components, PCB panels, nickel-plated parts) converging at the rinse stage. Built with rounded rectangles and branching arrows.
2. **Parameter table (Block D):** Cleaning parameters by substrate type.
3. **Cleaner chemistry callout (Block E):** What goes into the cleaner and why residue-free cleaning is critical for solder plating.
4. **Common mistakes strip (Block F):** 4 cleaning mistakes that cause tin-lead plating defects downstream.

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
**Subheading:** `Tin-Lead Plating -- Stage 1 of 8` -- 36 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `Lead-bearing plating on high-value electronics substrates. Clean it like it matters -- because it does.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

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
| Left | 0.5" | 7.33" | Copper / Brass Components | `#E8A020` (Amber) |
| Center | 8.16" | 7.33" | PCB Panels | `#2EC4B6` (Teal) |
| Right | 15.83" | 7.67" | Nickel-Plated Parts | `#27AE60` (Emerald) |

Each column contains 3--4 vertically stacked step boxes with downward arrows.

**Copper/Brass Components Path (most common for tin-lead):**

Step 1: `Alkaline Soak Clean`
- `Mild alkaline, 3--6 oz/gal`
- `120--150 F (49--66 C), 3--5 min`
- `Non-etch formula for copper`

Step 2: `Rinse`
- `Ambient, flowing, DI preferred`

Step 3: `Electroclean (optional)`
- `Anodic, 3--6 V, 1--2 min`
- `For heavy soil or stamping compounds`

Step 4: `Rinse` -> `TO ACTIVATION`

**PCB Panel Path:**

Step 1: `Spray Clean (conveyorized)`
- `Mild alkaline or semi-aqueous`
- `100--130 F (38--54 C), 30--90 sec`
- `Conveyorized spray line`

Step 2: `Spray Rinse`
- `DI water, high-pressure nozzles`

Step 3: `Acid Microetch (optional)`
- `Sodium persulfate or peroxide/sulfuric`
- `Creates copper surface texture for adhesion`

Step 4: `DI Rinse` -> `TO ACTIVATION`

**Nickel-Plated Parts Path:**

Step 1: `Mild Alkaline Soak`
- `Mild alkaline, 2--4 oz/gal`
- `120--140 F (49--60 C), 2--3 min`
- `Light touch -- protect Ni layer`

Step 2: `Rinse`
- `Ambient, flowing`

Step 3: `Mild Acid Dip`
- `5% MSA or H2SO4, 10--15 sec`
- `Remove light tarnish only`

Step 4: `Rinse` -> `TO ACTIVATION`

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
| Copper/Brass | Mild alkaline soak | 3--6 oz/gal | 120--150 F | 3--5 min | Non-etch, non-silicated |
| Copper/Brass (add) | Anodic electroclean (opt.) | Per supplier | 120--140 F | 1--2 min | Heavy soil only |
| PCB panels | Spray alkaline / semi-aqueous | Per supplier | 100--130 F | 30--90 sec | Conveyorized line |
| PCB (add) | Microetch (optional) | Persulfate or peroxide | Ambient | 15--30 sec | Improves adhesion on smooth Cu |
| Nickel-plated | Mild alkaline soak | 2--4 oz/gal | 120--140 F | 2--3 min | Protect Ni undercoat |

Header: `#3A4055`. Alternating rows: `#1E2435` / `#252B3D`.

---

### ZONE 5 -- Cleaner Chemistry Callout

**Section label:** `WHAT IS IN THE CLEANER -- AND WHAT MATTERS FOR SOLDER PLATE` -- Y: 22.2".

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
| Inhibitors | Prevent copper/brass etch attack |

**Right Panel -- Critical Rules for Tin-Lead:**
- Rounded rect, X: 12.0", W: 11.5", H: 5.2", fill `#1E2435`, left accent `#E8A020`
- Title: `RULES FOR SOLDER PLATE SUBSTRATES` Barlow SemiBold 18 pt `#E8A020`

Rules list (Inter Medium 14 pt `#F0EDE8`, line height 160%):
- `Non-silicated cleaners only -- silicate films cause skip plating`
- `Low alkalinity for copper/brass -- prevent etch and roughening`
- `Residue-free is mandatory for electronics -- ionic residue causes field failures`
- `DI water rinse after cleaning for electronics-grade substrates`
- `Water-break-free test is the ONLY acceptance criterion`
- `Lead safety: wear PPE even at the cleaning stage -- parts may have lead residue from previous processing`

Bottom note: `If the part is not water-break-free, it is not clean. Period.` Inter Medium 14 pt `#E05C5C`

---

### ZONE 6 -- Common Mistakes

**Section label:** `4 CLEANING MISTAKES THAT RUIN SOLDER DEPOSITS` -- Y: 28.7".

**BLOCK F -- Four Mistake Cards**

Y: 29.4" to 32.3". Same format as process flow poster.

| Card | X | Mistake | Result | Fix |
|---|---|---|---|---|
| 1 | 0.5" | SILICATED CLEANER | Skip plating, bare spots on copper | Switch to non-silicated formula |
| 2 | 6.33" | OVER-ETCHING COPPER | Rough substrate, grainy solder deposit | Reduce temp, time, or alkalinity |
| 3 | 12.16" | IONIC RESIDUE LEFT | Electrochemical migration, field failure | Use DI water rinse, verify conductivity |
| 4 | 18.0" | SKIPPING ELECTROCLEAN | Organic film trapped under solder, blistering | Electroclean heavy-soil copper parts |

---

### ZONE 7 -- Footer

Standard. Title: `Cleaning -- Tin-Lead`. Version `v1.0 -- 2026`.

Disclaimer: `Process parameters shown are typical industry values for cleaning prior to tin-lead (solder) plating. Consult your process supplier for application-specific guidance. Lead safety PPE is required per OSHA 29 CFR 1910.1025.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cleaning Tin-Lead -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Tin-lead plating is an electronics process -- copper and nickel-plated substrates dominate. The three-path hero visual reflects this: no steel path here (unlike the tin cluster). The ionic residue mistake card is unique to this cluster -- solder plating on electronics demands residue-free cleaning because ionic contamination causes electrochemical migration and field failures years later. The lead safety note at the cleaning stage reminds operators that lead awareness starts at Stage 1, not just at the plating tank.

---

*Alaina -- Plating Posters Inc*
*Poster #144 -- Construction Workup v1.0*
*2026-04-26*
