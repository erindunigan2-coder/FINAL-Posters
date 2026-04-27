---
Project: Plating Posters Inc
Poster Number: 120
Title: "Cleaning -- Gold"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Process Scope: Cleaning stage for acid hard gold plating (Stage 1 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - GoldPlating
  - Cleaning
  - ConstructionWorkup
  - Series2
  - ClusterEP12
---

# Poster #120 -- Construction Workup
## Cleaning -- Gold

*Alaina -- Plating Posters Inc*
*v1.0 -- 2026-04-26*

Stage 1 of 8. Gold is almost always plated over a nickel barrier underplate -- not directly onto the base substrate. This means the cleaning stage for gold is really about preparing the nickel surface. The requirements are milder than for base metals but the stakes are higher: contamination that would be tolerable in a zinc or tin bath can be catastrophic in a gold bath operating at $200--800 per gallon in gold content.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cleaning-to-gold pathway hero (Block B):** Vertical flow showing the substrate stack (copper base -> nickel underplate -> gold) and where cleaning fits.
2. **Cleaning parameter table (Block D):** Parameters by substrate type.
3. **Contamination sensitivity callout (Block E):** Why gold baths demand cleaner parts than any other process.
4. **Common mistakes strip (Block F).**

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
  Stage 1 highlighted (Teal)
ZONE 3 -- SUBSTRATE STACK + CLEANING HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- CLEANING PARAMETER TABLE (14.5"--20.5" / ~6.0")
ZONE 5 -- CONTAMINATION SENSITIVITY (20.5"--26.5" / ~6.0")
ZONE 6 -- COMMON MISTAKES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CLEANING` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Gold Plating -- Stage 1 of 8` -- 36 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `Gold baths are the most contamination-sensitive baths in the shop. Cleaning is not a suggestion -- it is survival.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 1 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Nickel-plated part with surface oxides and oils  -->  After: Oxide-free nickel surface ready for gold`

---

### ZONE 3 -- Substrate Stack + Cleaning Hero

**Section label:** `THE GOLD PLATING SUBSTRATE STACK` -- Y: 4.4".

**BLOCK B -- Substrate Stack Diagram**

Y: 5.0" to 14.0".

**Left half (X: 0.5", W: 11.0") -- Substrate Stack Cross-Section:**

Layered horizontal rectangles (bottom to top) representing the plating stack:

| Layer | Fill | Height | Label |
|---|---|---|---|
| Base substrate (copper, Kovar, etc.) | `#C8D0D8` | 2.0" | `BASE METAL (Cu, Kovar, alloy 42)` |
| Nickel underplate | `#2EC4B6` at 30% | 1.0" | `NICKEL BARRIER (0.5--2 um)` |
| Gold (target) | `#E8A020` at 50% | 0.5" | `GOLD DEPOSIT (target)` |

Labels: JetBrains Mono 14 pt, color matching layer.

Arrow pointing to nickel surface: `THIS IS THE SURFACE YOU ARE CLEANING` Barlow SemiBold 16 pt `#E8A020`

Below stack: `Nickel underplate is REQUIRED under gold. It prevents copper migration into the gold deposit and provides a hard, solderable barrier.` Inter Medium 13 pt `#2EC4B6`

**Right half (X: 12.0", W: 11.5") -- Cleaning Steps:**

Vertical flow of 4 steps:

Step 1: `Mild Alkaline Soak Clean`
- `3--5 oz/gal, 130--150 F, 3--5 min`
- `Non-etch, non-silicated`

Step 2: `Rinse`
- `Ambient, flowing water`

Step 3: `Acid Dip (Activation)`
- `5--10% H2SO4, 15--30 sec`
- `NEVER HCl -- chloride kills gold baths`

Step 4: `DI Water Rinse -> Gold Bath`
- `DI water only for final rinse`

Each step: rounded rect, fill `#1E2435`, left accent `#2EC4B6`, radius 6.

Optional branch below Step 2: `Gold Strike` (dashed border, `#E8A020` accent)
- `1--4 g/L Au, pH 3.5--5.0, 90--120 F, 15--60 sec`
- `Flash coat for difficult substrates`

---

### ZONE 4 -- Cleaning Parameter Table

**Section label:** `CLEANING PARAMETERS` -- Y: 14.7".

**BLOCK D -- Parameter Table**

Y: 15.3" to 20.0".

| Substrate | Cleaner | Concentration | Temp | Time | Notes |
|---|---|---|---|---|---|
| Nickel-plated (standard) | Mild alkaline soak | 3--5 oz/gal | 130--150 F | 3--5 min | Most common gold substrate |
| Kovar / alloy 42 | Mild alkaline soak | 3--5 oz/gal | 120--140 F | 3--5 min | Proprietary activators may be needed |
| Copper (direct gold) | Mild alkaline soak | 3--6 oz/gal | 130--160 F | 3--5 min | Rare -- Ni underplate recommended |
| Rework / replating | Mild alkaline soak | 2--4 oz/gal | 120--140 F | 2--3 min | Light clean, do not etch existing gold |

---

### ZONE 5 -- Contamination Sensitivity

**Section label:** `WHY GOLD BATHS DEMAND PERFECT CLEANING` -- Y: 20.7".

**BLOCK E -- Sensitivity Panel**

Y: 21.3" to 26.0". Full-width panel, two columns.

**Left -- Contamination Thresholds:**
- Rounded rect, X: 0.5", W: 11.0", H: 4.5", fill `#1E2435`, left accent `#E05C5C`
- Title: `GOLD BATH SENSITIVITY` Barlow SemiBold 18 pt `#E05C5C`

| Contaminant | Threshold | Effect |
|---|---|---|
| Copper | > 5 ppm | Dark deposit, porosity |
| Iron | > 10 ppm | Dark deposit, roughness |
| Zinc | > 1 ppm | Pitting, discoloration |
| Chloride | > 1 ppm | Catastrophic -- attacks gold complex |
| Organic (oil/grease) | Any visible | Dark, stressed deposit |

Note: `These thresholds are 5--10x lower than zinc or nickel baths. Gold cannot tolerate what other baths can.` Inter Medium 13 pt `#E05C5C`

**Right -- What Perfect Cleaning Looks Like:**
- Rounded rect, X: 12.0", W: 11.5", H: 4.5", fill `#1E2435`, left accent `#27AE60`
- Title: `THE STANDARD` Barlow SemiBold 18 pt `#27AE60`

Content:
- `Water-break-free surface (absolute requirement)`
- `No visible residue under 10x magnification`
- `No alkaline drag-in (pH neutral after rinse)`
- `DI water final rinse (mineral-free)`
- `Parts processed immediately -- no air-dry delay`
- `Gloves worn at all times (fingerprints = oil = contamination)`

Bottom note: `In gold plating, cleaning is not a step. It is a religion.` Inter Medium 14 pt `#E8A020`

---

### ZONE 6 -- Common Mistakes

**Section label:** `4 CLEANING MISTAKES THAT CONTAMINATE GOLD BATHS` -- Y: 26.7".

**BLOCK F -- Four Mistake Cards**

Y: 27.3" to 32.0".

| Card | X | Mistake | Result | Fix |
|---|---|---|---|---|
| 1 | 0.5" | HCl ACTIVATION | Chloride drag-in -- gold bath contamination | H2SO4 only, always |
| 2 | 6.33" | TAP WATER RINSE | Mineral drag-in (Ca, Mg, Fe) | DI water for pre-plate rinse |
| 3 | 12.16" | BARE-HAND CONTACT | Fingerprint oils contaminate bath | Gloves mandatory at all times |
| 4 | 18.0" | DELAYED TRANSFER | Nickel oxidizes in minutes | Process immediately after cleaning |

---

### ZONE 7 -- Footer

Standard. Title: `Cleaning -- Gold`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cleaning Gold -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The substrate stack diagram is unique to this poster and sets up the entire gold cluster. Operators need to understand that they are not cleaning the base metal -- they are cleaning the nickel underplate. The contamination threshold table is the most important technical content on the poster. Every number in that table is a hard limit that can cost hundreds or thousands of dollars if exceeded. The "cleaning is a religion" line is deliberate -- gold plating demands a mindset shift from the casual approach acceptable in zinc or tin.

---

*Alaina -- Plating Posters Inc*
*Poster #120 -- Construction Workup v1.0*
*2026-04-26*
