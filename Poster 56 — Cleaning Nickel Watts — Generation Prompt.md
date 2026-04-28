---
Project: Plating Posters Inc
Poster Number: 56
Title: "Cleaning -- Nickel (Watts)"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-28T00:00:00
Source: Poster 56 -- Cleaning Nickel Watts -- Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - NickelPlating
  - Watts
  - Cleaning
  - Series2
  - ClusterEP03
  - v1
---

# Claude Chat Generation Prompt -- Poster #56
## Cleaning -- Nickel (Watts)
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-28).*

---

> **IMPORTANT:** Generate as SVG or HTML visual artifact. 24 x 36" portrait. Dark edition first.

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E`, locked palette, 0.5" safe zone.

---

## Phase 2 -- Header

### Step 1 -- `CLEANING` -- `88` pt `#F0EDE8`. Y: **0.5"**.
### Step 2 -- `Nickel (Watts) -- Stage 1 of 8` -- `36` pt `#2EC4B6`. Y: **1.5"**.
### Step 3 -- `Nickel is the most unforgiving deposit on your line. If it is not water-break-free, do not plate it.` -- `22` pt at 65%. Y: **2.2"**.

---

## Phase 3 -- Orientation Strip

**Stage 1 highlighted** (fill `#2EC4B6`). Below: `Before: Oily, oxidized substrate --> After: Water-break-free surface ready for activation`

---

## Phase 4 -- Cleaning Tanks Hero

Y: 4.2" to 14.5". Section: `THE TWO-STEP CLEANING SEQUENCE`.

### Step 5 -- Dual tank diagram (Y: 5.0" to 12.0")

**Left -- Soak Clean Tank (X: 0.5", W: 11.0", H: 6.5"):**
Rounded rect fill `#252B3D`, border 2pt `#2EC4B6`.
- Title: `STEP 1: ALKALINE SOAK CLEAN` `#2EC4B6`
- Params (JetBrains Mono 14pt):
  - Type: Non-chelated or mild chelated
  - Concentration: 4--8 oz/gal (30--60 g/L)
  - Temperature: 140--190 F (60--88 C)
  - Time: 3--10 min (soak) / 1--3 min (spray)
  - pH: 12--14
  - Agitation: Air or mechanical
- Purpose: `Removes oils, drawing compounds, rust preventatives, shop soil`

**Right -- Electrocleaner Tank (X: 12.5", W: 11.0", H: 6.5"):**
Rounded rect fill `#252B3D`, border 2pt `#E8A020`.
- Title: `STEP 2: ELECTROCLEANER` `#E8A020`
- Params:
  - Concentration: 4--8 oz/gal (30--60 g/L)
  - Temperature: 140--180 F (60--82 C)
  - Current density: 30--80 ASF
  - Time: 1--3 min
  - Polarity: Anodic (reverse) preferred
- Purpose: `Final clean -- gas scrubbing action at workpiece surface`

### Step 6 -- Water-break test callout (Y: 12.3" to 14.3")

Full-width rounded rect, H: 1.8", fill `#27AE60` at 15%, border 2pt `#27AE60`, radius 8.
- Title: `THE WATER-BREAK TEST -- YOUR GO / NO-GO` `#27AE60`
- Body: `Rinse the part. Watch the water film. A fully clean surface holds a continuous, unbroken sheet of water for 30+ seconds with zero beading or breaking. Any break = contamination remains. Do not proceed to activation. Re-clean.`

---

## Phase 5 -- Substrate-Specific Cleaning

Y: 14.5" to 20.5". Section: `CLEANING ADJUSTMENTS BY SUBSTRATE`.

Table. Columns: Substrate (4.5") | Cleaner Notes (6.5") | Electrocleaner Notes (6.5") | Watch For (5.5%).

| Substrate | Cleaner Notes | Electrocleaner Notes | Watch For |
|---|---|---|---|
| Steel (mild) | Standard alkaline | Anodic final preferred | Rust inhibitor residues |
| High-strength steel (>31 HRC) | Standard alkaline | Cathodic first, anodic final -- minimize total time | H-embrittlement risk from cathodic clean |
| Copper / Brass | Non-etch alkaline preferred | Anodic only -- cathodic embeds metals | Tarnish films -- may need acid pre-dip |
| Zinc die cast | Mild alkaline, lower temp (120--140 F) | Low CD (20--40 ASF), short time | Aggressive cleaning attacks zinc surface |
| Stainless steel | Standard alkaline | Anodic -- then Wood's strike mandatory | Passive oxide film reforms immediately |

---

## Phase 6 -- Anodic vs. Cathodic + Contamination Types

Y: 20.5" to 26.5". Two-column layout.

**Left -- Anodic vs. Cathodic (X: 0.5", W: 11.0"):**
Section label: `ANODIC VS. CATHODIC CLEANING`.

Two stacked callout boxes:

*Anodic (Reverse):* fill `#1E2435`, accent `#27AE60`.
- `Generates O2 at workpiece. Scrubbing action. Removes smut. Does not embed metal contaminants. Preferred for final clean on all substrates.`
- Tag: `RECOMMENDED FOR NICKEL` `#27AE60`

*Cathodic (Direct):* fill `#1E2435`, accent `#E8A020`.
- `Generates H2 at workpiece. Better for heavy soil removal. CAN embed metal contaminants (Cu, Fe) and CAUSE hydrogen embrittlement on high-strength steel.`
- Tag: `USE FIRST FOR HEAVY SOIL ONLY` `#E8A020`

**Right -- Contamination Types (X: 12.5", W: 11.0"):**
Section label: `WHAT YOU ARE REMOVING`.

| Contaminant | Effect If Left | Removal |
|---|---|---|
| Stamping oils | Skip plating, pitting | Soak clean (surfactant action) |
| Oxide films | Poor adhesion, peeling | Electrocleaner + acid activation |
| Shop soil / dust | Roughness, inclusions | Soak clean |
| Fingerprints | Skip plating (local) | Soak clean -- handle with gloves |
| Rust preventative | Hazy deposit, poor adhesion | Extended soak, higher temp |

---

## Phase 7 -- Common Failures + Safety

Y: 26.5" to 32.5". Two-column layout.

**Left -- 4 Cleaning Failures (X: 0.5", W: 14.0"):**
Section label: `WHAT GOES WRONG`.

| Failure | Root Cause | Result in Nickel Bath |
|---|---|---|
| Incomplete oil removal | Cleaner too dilute, temp too low, time too short | Pitting, skip plating |
| Silicate residue | Used silicated cleaner | Skip plating -- nearly impossible to remove |
| Metal embedding (cathodic) | Excessive cathodic cleaning | Dark spots, peeling, roughness |
| Over-etching (zinc die cast) | Cleaner too aggressive | Pitted substrate, poor adhesion |

Cards: fill `#1E2435`, accent `#E05C5C`. Failure: `#E05C5C`. Cause: `#F0EDE8`. Result: `#E8A020`.

**Right -- Safety (X: 15.5", W: 8.0"):**
Coral-tinted glass callout.
- Alkaline cleaners: caustic burn hazard (pH 12--14). Gloves, goggles, apron required.
- Electrocleaner generates gas at workpiece. Ensure adequate ventilation.
- Hot solutions (140--190 F): splash burn risk. Fill slowly, never add water to concentrated cleaner.

---

## Phase 8 -- Footer

Standard. Title: `Cleaning -- Nickel (Watts)`. Version `v1.0 -- 2026`.

---

## Phase 9 -- Review

- [ ] Headline `CLEANING` 88pt
- [ ] Stage 1 highlighted (Teal)
- [ ] Dual tank hero: soak clean + electrocleaner side by side
- [ ] Water-break test callout -- most visible element after headline
- [ ] Substrate-specific cleaning table (5 rows)
- [ ] Anodic vs. cathodic comparison panels
- [ ] Contamination types table (5 rows)
- [ ] 4 cleaning failure cards
- [ ] Safety panel
- [ ] Footer complete

---

## Phase 10 -- Light Remap & Export

Standard remap.

Six files: `Cleaning Nickel Watts -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-28 | Initial. |
