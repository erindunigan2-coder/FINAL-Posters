---
Project: Plating Posters Inc
Poster Number: 521
Title: "Cleaning -- Cold Spray"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 5: Cold Spray)"
Technical Source: Pre-spray cleaning requirements for cold spray. Cleanliness is critical because bonding is 100% solid-state -- any contamination directly prevents metallurgical bonding.
Process Scope: Cold spray -- pre-spray cleaning sequence
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document.
tags:
  - PosterDesign
  - ColdSpray
  - ThermalSpray
  - Cleaning
  - ConstructionWorkup
  - ClusterTS05
---

# Poster #521 -- Construction Workup
## Cleaning -- Cold Spray

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Cleaning poster for the Cold Spray cluster. Surface cleanliness is MORE critical for cold spray than for any conventional thermal spray process because bonding is entirely solid-state. Contamination that would be "burned off" or "encapsulated" by a molten splat in plasma or HVOF becomes a direct bond-preventer in cold spray.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cleaning sequence flowchart (Block B -- HERO):** Vertical 4-step flowchart with decision gates.
2. **"Why Cleanliness Matters More" callout (Block C):** Amber callout emphasizing the solid-state bonding linkage.
3. **Substrate-specific cleaning notes (Block D):** 4 callout cards for Al aerospace, Cu electrical, Ti, and composites.
4. **Time windows strip (Block E):** Critical time limits between cleaning steps.
5. **Verification methods (Block F):** Water-break-free test and alternatives.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 14.5" / 18.0" / 25.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- CLEANING SEQUENCE HERO (2.9"--14.5" / ~11.6")
  Block B: 4-step vertical flowchart
  Block C: "Why Cleanliness Matters More" callout
ZONE 3 -- SUBSTRATE-SPECIFIC NOTES (14.5"--18.0" / ~3.5" -- REMOVED, MERGED INTO ZONE 4)
ZONE 4 -- SUBSTRATE CARDS + TIME WINDOWS (14.5"--25.5" / ~11.0")
  Block D: 4 substrate-specific cards (2x2 grid)
  Block E: Time windows strip
ZONE 5 -- VERIFICATION METHODS (25.5"--32.5" / ~7.0")
  Block F: Water-break-free test + alternatives
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `CLEANING` -- 88 pt `#F0EDE8`.
**Subheading:** `Cold Spray -- Surface Prep Starts Here` -- 36 pt `#2EC4B6`. Y: 1.5".
**Tagline:** `Solid-state bonding has zero tolerance for contamination. What a molten splat burns through, a cold particle bounces off.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Cleaning Sequence Hero

**Section label:** `THE CLEANING SEQUENCE` -- Y: 3.1".

**BLOCK B -- 4-Step Vertical Flowchart (Left, X: 0.5", W: 14.0")**

Y: 3.8" to 14.0". Four large step boxes connected by vertical arrows.

Each box: Rounded rect, W: 13.5", H: 2.2", fill `#1E2435`, radius 8, left accent 4 pt.

| Step | Accent | Title | Details | Check |
|---|---|---|---|---|
| 1. SOLVENT DEGREASE | `#2EC4B6` | Solvent Degrease | Aqueous alkaline clean preferred (environmentally). Vapor degrease (legacy -- perchloroethylene/trichloroethylene). Remove all oils, greases, machining fluids, fingerprints. | No visible residue; no odor |
| 2. ALKALINE WASH | `#2EC4B6` | Alkaline Wash | Immersion or spray wash. 50--70 C, pH 10--12, 5--15 minutes. Rinse thoroughly with DI water for aerospace components. | Conductivity check on final rinse |
| 3. INSPECTION | `#E8A020` | Water-Break-Free Test | Surface must sheet water uniformly with no beading (ASTM F22 equivalent). Any break indicates residual contamination -- reclean. | PASS = uniform sheet. FAIL = reclean. |
| 4. DRY | `#27AE60` | Forced Air Dry | Forced air or oven dry. No moisture at time of grit blast. | Completely dry before any further steps |

Arrows between boxes: 3 pt `#3A4055`, arrowhead down.

Step number badge: Rounded rect, fill accent color, `STEP 1` in Barlow Condensed ExtraBold 14 pt `#1A1F2E`.
Title: Barlow SemiBold, 20 pt, `#F0EDE8`.
Details: Inter Regular, 13 pt, `#F0EDE8`.
Check: Inter Medium, 12 pt, accent color.

**BLOCK C -- "Why Cleanliness Matters More" Callout (Right, X: 15.0", W: 8.5")**

Y: 3.8" to 8.0". Rounded rect, fill `#1E2435`, radius 8, left accent 4 pt `#E8A020`.

Title: `WHY IT MATTERS MORE` Barlow Condensed ExtraBold, 22 pt, `#E8A020`.

Body (Inter Regular, 14 pt, `#F0EDE8`, line height 165%):

```
In plasma or HVOF, molten droplets
can burn through thin contamination
layers and still bond.

In cold spray, particles are SOLID.
They cannot burn through anything.

Any contamination film = a bond-
prevention layer.

Cleanliness is not "best practice"
in cold spray -- it is the ONLY path
to adhesion.
```

Bottom stat: `< 2 hr` Barlow Condensed ExtraBold, 48 pt, `#E8A020`.
Label: `Preferred time from clean to spray` Inter Medium, 14 pt, `#F0EDE8` at 60%.

---

### ZONE 4 -- Substrate Cards + Time Windows

**Section label:** `SUBSTRATE-SPECIFIC CLEANING NOTES` -- Y: 14.7".

**BLOCK D -- 4 Substrate Cards (2x2 Grid)**

Y: 15.3" to 21.5". Each card: W: 11.25", H: 2.8", fill `#1E2435`, radius 6, left accent 0.06".

| Card | Position | Accent | Substrate | Notes |
|---|---|---|---|---|
| 1 | R1C1 (X: 0.5") | `#2EC4B6` | ALUMINUM AEROSPACE | Solvent wipe + alkaline clean + DI rinse + forced air dry. Primary CS application: corrosion pit repair on gearbox housings, structural components. |
| 2 | R1C2 (X: 12.25") | `#E8A020` | COPPER ELECTRICAL | Avoid residual cleaning agents that increase contact resistance. Acetone wipe + mild alkaline + DI rinse. CS goal: restore conductivity. |
| 3 | R2C1 (X: 0.5") | `#C8D0D8` | TITANIUM | Standard cleaning sequence. Ti oxidizes rapidly -- minimize exposure time after cleaning. Grit blast within 2 hours of clean. |
| 4 | R2C2 (X: 12.25") | `#27AE60` | POLYMERS / COMPOSITES | Cold spray is the ONLY thermal spray option for these substrates. Light solvent wipe only -- aggressive alkaline can damage substrate. Mechanical abrasion for surface activation. |

Substrate title: Barlow SemiBold, 16 pt, accent color.
Notes: Inter Regular, 13 pt, `#F0EDE8`.

**BLOCK E -- Time Windows Strip**

Y: 22.0" to 25.3". Full width.
Rounded rect, fill `#1E2435`, radius 8, top accent 4 pt `#E05C5C`.

Title: `CRITICAL TIME WINDOWS` Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`.

| Window | Time Limit | Consequence |
|---|---|---|
| Clean to grit blast | Same shift (< 4 hr) | Recontamination from airborne oils, handling |
| Grit blast to spray | < 2 hours preferred | Oxide regrowth; moisture pickup |
| Handling after blast | NEVER bare hands | Skin oils = adhesion failure |

Time limits: JetBrains Mono Regular, 16 pt, `#E05C5C`.
Consequence: Inter Regular, 13 pt, `#F0EDE8`.

Note: `Wear clean lint-free gloves at all times after grit blast.` Inter Medium, 14 pt, `#27AE60`.

---

### ZONE 5 -- Verification Methods

**Section label:** `VERIFICATION METHODS` -- Y: 25.7".

**BLOCK F -- Verification Table**

Y: 26.3" to 32.3".

Two side-by-side cards:

**Left -- Water-Break-Free Test (PRIMARY):**
X: 0.5", W: 11.0", H: 5.5", fill `#1E2435`, left accent `#27AE60`.

Title: `WATER-BREAK-FREE TEST` Barlow SemiBold, 20 pt, `#27AE60`.
Subtitle: `ASTM F22 equivalent` JetBrains Mono 12 pt `#F0EDE8` at 60%.

Procedure:
```
1. Rinse surface with clean water
2. Observe water film behavior
3. PASS: Water sheets uniformly
4. FAIL: Water beads or breaks
```

Visual indicator:
- `PASS` in large text, fill `#27AE60` at 20%, `#27AE60` text
- `FAIL` in large text, fill `#E05C5C` at 20%, `#E05C5C` text
- `Any break = reclean entire part` Inter Medium 14 pt `#E05C5C`

**Right -- Alternative Methods:**
X: 12.0", W: 11.5", H: 5.5", fill `#1E2435`, left accent `#E8A020`.

Title: `ALTERNATIVE VERIFICATION` Barlow SemiBold, 20 pt, `#E8A020`.

| Method | Application |
|---|---|
| UV fluorescence | Detects residual oils under UV light |
| Contact angle measurement | Quantitative cleanliness metric |
| Solvent wipe + visual | Quick field verification |
| FTIR surface analysis | Laboratory confirmation |

Note: `Water-break-free is the universal field standard. Use alternatives when specification requires quantitative data.` Inter Regular, 12 pt, `#F0EDE8` at 70%.

---

### ZONE 6 -- Footer Band

Standard footer. Title: `Cleaning -- Cold Spray`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Cleaning requirements vary by substrate material, application specification, and equipment manufacturer. Always consult applicable specifications (MIL-STD-3021, OEM documentation) for detailed cleaning procedures.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cleaning Cold Spray -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The hero message is that cleanliness matters MORE in cold spray than in any other thermal spray process. The "Why It Matters More" callout should be the most visually impactful element after the headline. The molten-vs-solid comparison is the key pedagogical hook: what a molten droplet burns through, a solid particle bounces off.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #521 -- Construction Workup v1.0*
*2026-04-26*
