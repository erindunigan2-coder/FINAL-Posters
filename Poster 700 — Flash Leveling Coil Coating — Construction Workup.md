---
Project: Plating Posters Inc
Poster Number: 700
Title: "Flash / Leveling -- Coil Coating"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting Coating Clusters -- Watson Research Brief (Cluster 6: Coil Coating, Section 6.7)"
Process Scope: Flash / leveling for coil coating -- the roll coater IS the leveling step
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - CoilCoating
  - FlashLeveling
  - ConstructionWorkup
  - PaintingCoating
  - ClusterCC
---

# Poster #700 -- Construction Workup
## Flash / Leveling -- Coil Coating

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Coil coating has no flash time. The coated strip travels directly from the roll coater into the oven at line speed -- there is no pause, no ambient flash zone, no waiting. Leveling occurs on the roll coater itself: the reverse roll action produces a smooth film, and additional leveling happens in the first seconds of oven entry as the coating heats and viscosity drops. This poster reframes "flash/leveling" as the roll coater mechanics that determine film smoothness, plus the critical first seconds of the cure oven where final leveling occurs.

Hero visual: a timeline strip showing the strip path from roll coater to oven entry, with a viscosity curve overlaid showing the brief leveling window before cross-linking locks the film in place.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Roll coater to oven timeline hero (Block B):** Horizontal strip path showing the zero-flash transition from coater to oven, with a viscosity curve overlaid.
2. **Leveling mechanics panel (Block D):** The three factors that determine film smoothness at the roll coater.
3. **First-seconds-in-oven detail (Block E):** What happens to the coating during the initial heating phase.
4. **Defect strip (Block F):** 4 leveling-related defects.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Flash/Level position highlighted (Amber)
ZONE 3 -- COATER-TO-OVEN TIMELINE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- LEVELING MECHANICS (14.5"--20.5" / ~6.0")
ZONE 5 -- FIRST SECONDS IN THE OVEN (20.5"--26.5" / ~6.0")
ZONE 6 -- LEVELING DEFECTS (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `FLASH / LEVELING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Coil Coating -- No Flash. No Wait. The Roll Coater IS the Leveling Step.` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `From roll coater to cure oven in zero seconds. Leveling happens on the roll and in the first moments of heating. There is no ambient flash zone -- the strip never stops.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Flash/Leveling position highlighted between Stages 6/8 (Application) and 7/9 (Cure): fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Wet film on strip leaving roll coater  -->  After: Film entering oven, viscosity dropping, final leveling in progress`

---

### ZONE 3 -- Coater-to-Oven Timeline Hero

**Section label:** `FROM ROLL COATER TO CURE OVEN -- THE LEVELING WINDOW` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Timeline with Viscosity Curve (Y: 5.0" to 14.0")**

Full-width rounded rect, W: 23.0", H: 8.5", fill `#1E2435`, top accent 4 pt `#E8A020`.

**Top half -- Strip Path Diagram (Y: 5.5" to 8.5"):**
- Horizontal strip line (`#C8D0D8`, 3 pt) with directional arrow
- Three labeled zones along the strip:

Zone A (X: 1.0", W: 6.0"):
- Label: `ROLL COATER` Barlow SemiBold 14 pt `#E8A020`
- Simplified roll icon
- `Film applied` JetBrains Mono 11 pt `#F0EDE8`
- `Leveling by reverse roll shear`

Zone B (X: 7.5", W: 2.0"):
- Label: `~0 sec` Barlow Condensed ExtraBold 24 pt `#E05C5C`
- `NO FLASH ZONE` JetBrains Mono 11 pt `#E05C5C`
- Vertical dashed line marking immediate transition

Zone C (X: 10.0", W: 12.0"):
- Label: `CURE OVEN` Barlow SemiBold 14 pt `#27AE60`
- Oven box shape with heat waves
- `Final leveling in first 3-5 sec as viscosity drops`
- `Then cross-linking begins, film locks`

**Bottom half -- Viscosity Curve (Y: 9.0" to 13.5"):**
- X-axis: `TIME IN OVEN (seconds)` -- 0 to 60 sec
- Y-axis: `VISCOSITY` (high to low to high)
- Curve shape:
  - Starts high (wet film as-applied)
  - Drops rapidly in first 3-5 seconds (heating lowers viscosity)
  - Reaches minimum viscosity at ~5-10 sec (LEVELING WINDOW)
  - Rises sharply as cross-linking begins (~10-15 sec)
  - Plateaus at high viscosity (cured film)

Curve color: `#E8A020` 3 pt line
Minimum point annotation: `LEVELING WINDOW` with arrow pointing to the viscosity minimum, Barlow SemiBold 14 pt `#E8A020`
Cure onset annotation: `CROSS-LINK ONSET` with arrow at the rising portion, `#27AE60`

Axis labels: JetBrains Mono 11 pt `#F0EDE8`.

Caption: `The leveling window is measured in seconds, not minutes. Coating viscosity drops as the strip heats, allowing brief flow and leveling. Then cross-linking drives viscosity up and the film freezes in place.` Inter Regular 13 pt `#F0EDE8`.

---

### ZONE 4 -- Leveling Mechanics

**Section label:** `THREE FACTORS THAT DETERMINE FILM SMOOTHNESS` -- Y: 14.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK D -- Three Factor Cards (Y: 15.3" to 20.3")**

Three cards. Each: Rounded rect, W: 7.33", H: 4.5", fill `#1E2435`, top accent 4 pt.

**Card 1 -- Roll Speed Ratio (X: 0.5", accent `#E8A020`):**
- Title: `ROLL SPEED RATIO` Barlow SemiBold 18 pt `#E8A020`
- Big stat: `1.05-1.25:1` Barlow Condensed ExtraBold 36 pt `#E8A020`
- Body (Inter Regular 13 pt `#F0EDE8`):
  - `Applicator roll speed / strip speed`
  - `Higher ratio = more shearing = smoother film`
  - `Too high = chatter marks (ribbing)`
  - `The single most important leveling control`

**Card 2 -- Nip Pressure (X: 8.16", accent `#2EC4B6`):**
- Title: `NIP PRESSURE` Barlow SemiBold 18 pt `#2EC4B6`
- Big stat: `20-100 pli` Barlow Condensed ExtraBold 36 pt `#2EC4B6`
- Body:
  - `Pounds per linear inch at the roll/strip contact`
  - `Controls film thickness AND uniformity`
  - `Uneven nip = DFT variation across strip width`
  - `Roll crown compensates for deflection`

**Card 3 -- Coating Viscosity (X: 15.83", accent `#27AE60`):**
- Title: `COATING VISCOSITY` Barlow SemiBold 18 pt `#27AE60`
- Big stat: `30-80 sec` Barlow Condensed ExtraBold 36 pt `#27AE60`
- Subtitle: `Zahn #2 cup` Inter Regular 14 pt `#F0EDE8` at 60%
- Body:
  - `Lower viscosity = better flow and leveling`
  - `Higher viscosity = thicker film, less leveling`
  - `Temperature-sensitive -- monitor at 77 F (25 C)`
  - `Solvent evaporation increases viscosity over time`

---

### ZONE 5 -- First Seconds in the Oven

**Section label:** `WHAT HAPPENS IN THE FIRST 10 SECONDS OF THE OVEN` -- Y: 20.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK E -- Timeline Breakdown (Y: 21.3" to 26.3")**

Full-width rounded rect, fill `#1E2435`, left accent `#27AE60` 0.06".

Four time-phase columns:

**0-3 sec (X: 1.0", W: 5.0"):**
- Header: `0-3 SECONDS` Barlow SemiBold 16 pt `#E8A020`
- `Strip enters oven at 200-700 ft/min`
- `Surface temperature begins rising`
- `Solvent starts evaporating from film surface`
- `Viscosity begins dropping`
- Inter Regular 12 pt `#F0EDE8`

**3-8 sec (X: 6.5", W: 5.5"):**
- Header: `3-8 SECONDS` Barlow SemiBold 16 pt `#E8A020`
- `Viscosity reaches minimum -- LEVELING WINDOW`
- `Coating flows and levels on the strip surface`
- `Orange peel is determined in this window`
- `Solvent evaporation rate is highest`
- Inter Regular 12 pt `#F0EDE8`

**8-15 sec (X: 12.5", W: 5.0"):**
- Header: `8-15 SECONDS` Barlow SemiBold 16 pt `#27AE60`
- `Cross-linking begins`
- `Viscosity rises rapidly`
- `Film structure locks in`
- `No further leveling possible`
- Inter Regular 12 pt `#F0EDE8`

**15-60 sec (X: 18.0", W: 5.0"):**
- Header: `15-60 SECONDS` Barlow SemiBold 16 pt `#27AE60`
- `Full cross-linking proceeds`
- `PMT reached (400-480 F)`
- `Film fully cured`
- `Strip exits oven to water quench`
- Inter Regular 12 pt `#F0EDE8`

Bottom callout: `The entire "flash/leveling" window in coil coating is 3-8 seconds inside the oven. Compare this to 5-15 minutes of ambient flash in liquid spray painting. Speed is the defining characteristic of coil coating at every stage.` Inter Medium 13 pt `#E8A020`.

---

### ZONE 6 -- Leveling Defects

**Section label:** `WHAT GOES WRONG -- 4 LEVELING DEFECTS` -- Y: 26.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK F -- Four Problem Cards (Y: 27.3" to 30.3")**

Each card: Rounded rect, W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | ORANGE PEEL | Insufficient leveling time (oven ramp too fast) or viscosity too high | Reduce initial oven zone temperature; lower coating viscosity |
| 2 | 6.33" | CHATTER / RIBBING | Roll speed ratio too high or roll surface wear | Reduce ratio toward 1.05:1; re-grind roll surface |
| 3 | 12.16" | SOLVENT POP | Too much solvent trapped when surface skins over in oven | Adjust solvent blend for slower evaporation; check oven zone 1 temp |
| 4 | 18.0" | UNEVEN GLOSS | Viscosity variation across reservoir or uneven roll contact | Agitate reservoir; verify roll alignment and nip pressure uniformity |

**Key insight callout (Y: 30.6" to 32.3"):**
- Text: `In coil coating, "leveling" is not a separate step -- it is a property of the roll coater and the first seconds of the oven. You do not control leveling by waiting. You control it by roll speed, nip pressure, viscosity, and oven zone 1 temperature.` -- Inter Medium, 14 pt, `#E8A020`

---

### ZONE 7 -- Footer

Standard. Title: `Flash / Leveling -- Coil Coating`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Flash Leveling Coil Coating -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster exists because the series template has a flash/leveling slot and coil coating's answer to that slot is fundamentally different: there is no flash. The viscosity curve overlaid on the strip timeline is the hero concept -- it makes visible the invisible 3-8 second window where leveling actually happens inside the oven. The three-factor cards (roll speed, nip pressure, viscosity) are the actionable takeaway. The four-phase oven timeline in Zone 5 tells the complete story of what happens to a coating film in under a minute.

---

*Alaina -- Poster #700 -- Construction Workup v1.0 -- 2026-04-26*
