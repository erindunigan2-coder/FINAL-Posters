---
Project: Plating Posters Inc
Poster Number: 678
Title: "Cleaning -- Dip Coating"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting & Organic Coating Clusters -- Watson Research Brief (Cluster 4, Section 4.3)"
Technical Source: Cleaning methods for dip coating applications. Covers batch soak cleaning, continuous wire line cleaning with ultrasonic assist, and cleanliness verification.
Process Scope: Cleaning for dip coating -- Stage 2 of 7
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - DipCoating
  - Cleaning
  - ConstructionWorkup
  - PaintingCoating
  - ClusterPC04
---

# Poster #678 -- Construction Workup
## Cleaning -- Dip Coating

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 2 of 7. Cleaning for dip coating is more forgiving than for thin-film processes -- a 20-mil plastisol coating can bridge minor contamination that would ruin a 1-mil spray finish. But adhesion still demands a clean surface. The two cleaning worlds here are batch (soak tanks for discrete parts) and continuous (in-line for wire and cable at hundreds of feet per minute). Both must deliver a water-break-free surface.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Batch vs. continuous cleaning comparison (Block B -- HERO):** Two large side-by-side callout boxes comparing batch soak cleaning and continuous wire line cleaning.
2. **Cleanliness verification methods (Block C):** Three-card strip showing water-break test, UV inspection, and visual check.
3. **Chemistry panel (Block D):** Cleaner composition and control.
4. **Defect grid (Block F):** 6 cleaning defects.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 19.5" / 25.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 2 highlighted (Teal)
ZONE 3 -- BATCH VS. CONTINUOUS HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- CLEANLINESS VERIFICATION (14.5"--19.5" / ~5.0")
ZONE 5 -- CHEMISTRY + CONTROLS (19.5"--25.5" / ~6.0")
ZONE 6 -- DEFECT DIAGNOSIS GRID (25.5"--32.5" / ~7.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CLEANING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Dip Coating -- Batch & Continuous Cleaning -- Stage 2 of 7` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Thick coatings forgive thin sins -- but adhesion never forgives a dirty surface. Clean it right or watch it peel.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 2 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Parts with oils, greases, drawing compounds, mill scale residue  -->  After: Water-break-free surface ready for priming and dipping`

---

### ZONE 3 -- Batch vs. Continuous Hero

**Section label:** `TWO CLEANING WORLDS -- BATCH AND CONTINUOUS` -- Y: 4.4".

**BLOCK B -- Two-Panel Comparison (Y: 5.0" to 14.0")**

**Left -- Batch Soak Cleaning (X: 0.5", W: 11.0", H: 8.5"):**
- Rounded rect, fill `#1E2435`, left accent 0.06" `#E8A020`
- Title: `BATCH SOAK CLEANING` Barlow SemiBold 22 pt `#E8A020`
- Subtitle: `Discrete Parts -- Tool Handles, Racks, Fixtures` 14 pt `#F0EDE8` at 50%

Parameters (JetBrains Mono 14 pt `#F0EDE8`):
```
Type:           Alkaline soak immersion
Chemistry:      pH 10--12, 2--5% concentration
Temperature:    120--160 F (49--71 C)
Time:           5--15 min immersion
Agitation:      Mechanical or air sparging
```

Process steps (Inter Regular 14 pt `#F0EDE8`, line height 155%):
```
1. Load parts into basket/rack
2. Immerse in heated alkaline cleaner
3. Soak for 5--15 min with agitation
4. Lift and drain
5. Transfer to rinse tank
6. Two-stage rinse (city + DI)
7. Dry (oven or air blow-off)
```

Key controls (Inter Medium 13 pt `#2EC4B6`):
- `Free alkalinity by titration: maintain per supplier spec`
- `Oil loading: dump bath when oil > 5 g/L`
- `Water-break test after rinse to confirm cleanliness`

**Right -- Continuous Wire/Cable Cleaning (X: 12.0", W: 11.5", H: 8.5"):**
- Rounded rect, fill `#1E2435`, left accent 0.06" `#2EC4B6`
- Title: `CONTINUOUS WIRE LINE CLEANING` Barlow SemiBold 22 pt `#2EC4B6`
- Subtitle: `Wire & Cable -- In-Line at 100--1,000+ ft/min` 14 pt `#F0EDE8` at 50%

Parameters:
```
Type:           In-line alkaline spray
Assist:         Ultrasonic (optional)
Chemistry:      pH 10--12, 1--3%
Temperature:    130--150 F (54--66 C)
Line speed:     100--1,000+ ft/min
Contact time:   1--5 sec (at speed)
```

Process steps:
```
1. Wire feeds through spray nozzle bank
2. Alkaline solution impinges at pressure
3. Ultrasonic transducers (if equipped)
   cavitate at wire surface
4. DI water spray rinse
5. Hot air or IR dryer
6. Wire proceeds to coating head
```

Key controls:
- `Nozzle alignment: full wire circumference coverage`
- `Ultrasonic frequency: 25--40 kHz typical`
- `Drawing lubricant is the primary contaminant -- monitor removal`

---

### ZONE 4 -- Cleanliness Verification

**Section label:** `HOW TO VERIFY CLEANLINESS` -- Y: 14.7".

**BLOCK C -- Three Verification Cards (Y: 15.3" to 19.3")**

Three side-by-side callout boxes:

| Test | X | W | Accent | Title | Content |
|---|---|---|---|---|---|
| Water-Break Test | 0.5" | 7.33" | `#27AE60` | WATER-BREAK TEST (ASTM F22) | `The gold standard. Spray or dip surface in clean water. PASS: unbroken water sheet for 30 sec. FAIL: water beads, breaks, or pulls back. Test every batch or per control plan.` |
| UV Inspection | 8.0" | 7.33" | `#E8A020` | UV INSPECTION (365 nm) | `Fluorescent oils and compounds glow under UV lamp. Quick screening method for gross contamination. Does not detect all soil types -- use as supplement to water-break test, not replacement.` |
| Visual Check | 15.5" | 8.0" | `#2EC4B6` | VISUAL CHECK | `Look for water beading, oily sheen, discoloration, or particulate residue under good lighting. Simple but effective for obvious contamination. Not sensitive enough for trace oils.` |

Each box: Rounded rect H: 3.8", fill `#1E2435`, left accent 0.06".
Title: Barlow SemiBold 18 pt in accent color. Content: Inter Regular 14 pt `#F0EDE8`.

---

### ZONE 5 -- Chemistry + Controls

**Section label:** `CLEANER CHEMISTRY AND CRITICAL CONTROLS` -- Y: 19.7".

**Two-column layout (Y: 20.3" to 25.3"):**

**Left -- Cleaner Chemistry (X: 0.5", W: 11.0", H: 4.8"):**
- Rounded rect, fill `#1E2435`, left accent 0.06" `#E8A020`
- Title: `ALKALINE CLEANER CHEMISTRY` Barlow SemiBold 20 pt `#E8A020`

Content:
```
Builders:
  NaOH, sodium metasilicate, trisodium
  phosphate (TSP)

Surfactants:
  Non-ionic or anionic blend
  Emulsify oils and greases

Chelating agents:
  EDTA, citrate, or gluconate
  Sequester hard water minerals

pH: 10--12 operating range
Concentration: 2--5% by volume
```

**Right -- Critical Controls (X: 12.0", W: 11.5", H: 4.8"):**
- Rounded rect, fill `#1E2435`, left accent 0.06" `#27AE60`
- Title: `CRITICAL CONTROL POINTS` Barlow SemiBold 20 pt `#27AE60`

| Control | Method | Target |
|---|---|---|
| Free Alkalinity | Titration to phenolphthalein | Per supplier spec |
| Total Alkalinity | Titration to bromocresol green | Per supplier spec |
| Oil Loading | Visual + titration | < 5 g/L |
| Temperature | Thermometer | 120--160 F |
| Water-Break Test | ASTM F22 | Pass on every batch |

Note: `Cleanliness requirements are less critical for thick dip coatings (8--40 mils) than for thin spray coatings (1--3 mils), but adhesion still requires a clean substrate.` Inter Regular 13 pt `#F0EDE8` at 60%.

---

### ZONE 6 -- Defect Diagnosis Grid

**Section label:** `WHAT GOES WRONG -- 6 CLEANING DEFECTS` -- Y: 25.7".

**BLOCK F -- 3x2 Grid (Y: 26.3" to 32.3")**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | COATING DELAMINATION | `#E05C5C` | Residual oil at coating-substrate interface | Increase clean time/temp; verify water-break-free |
| R1C2 | BLISTERING IN SERVICE | `#E05C5C` | Trapped cleaning solution under coating | Rinse thoroughly; dry completely before priming |
| R1C3 | FISH EYES / CRATERS | `#E8A020` | Silicone or oil contamination on surface | Identify contamination source; use silicone-free cleaners |
| R2C1 | POOR WETTING (BARE SPOTS) | `#E8A020` | Incomplete cleaning or water-break failure | Re-clean; extend soak time; increase temperature |
| R2C2 | WIRE COATING ADHESION LOSS | `#2EC4B6` | Drawing lubricant residue on wire | Verify ultrasonic assist; increase spray pressure |
| R2C3 | CLEANER FOAMING | `#2EC4B6` | Wrong surfactant type for agitation method | Switch to low-foam surfactant; reduce air agitation |

Each card: Rounded rect W: 7.33", H: 2.8", fill `#1E2435`, radius 4, left accent 0.06" in defect color.

---

### ZONE 7 -- Footer

Standard. Title: `Cleaning -- Dip Coating`. Version `v1.0 -- 2026`.

Disclaimer note: `Source: General industry knowledge. Cleaner chemistry and control parameters vary by supplier formulation and substrate type.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cleaning Dip Coating -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The batch vs. continuous split is the defining structural choice for this poster. Most dip coating shops are batch operations (soak tanks), but the wire/cable industry runs continuous lines at extraordinary speeds where cleaning contact time is measured in seconds, not minutes. The cleanliness verification section reinforces that the water-break test is the universal standard regardless of process speed. The note about dip coating being more forgiving than spray is honest and practical -- it sets realistic expectations without undermining the importance of cleaning.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #678 -- Construction Workup v1.0*
*2026-04-26*
