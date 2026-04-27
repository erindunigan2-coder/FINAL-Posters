---
Project: Plating Posters Inc
Poster Number: 706
Title: "Cleaning -- Priming"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster 7 technical reference (Industrial Priming Systems) -- Watson Research Brief"
Technical Source: Cleaning requirements for industrial priming. SSPC-SP1 solvent cleaning before blast, post-blast blow-down, oil-free air verification (ASTM D4285), and the critical rule that no chemical cleaning follows blasting for zinc-rich primers.
Process Scope: Cleaning for industrial priming -- Stages 1 and 3 of 8
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - IndustrialPriming
  - Cleaning
  - ConstructionWorkup
  - PaintingCoating
  - Cluster7
---

# Poster #706 -- Construction Workup
## Cleaning -- Priming

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stages 1 and 3 of 8. This poster covers the two cleaning steps in the priming sequence: pre-blast solvent cleaning (SSPC-SP1) and post-blast blow-down/vacuum. The key rule: blasting cannot remove oil and grease -- solvent cleaning MUST come first. After blasting, no chemical cleaning -- go directly to prime.

Hero visual: a two-phase cleaning sequence diagram showing solvent wipe (before blast) and compressed air blow-down (after blast) with the blast step in between.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Two-phase cleaning sequence hero (Block B):** Three-panel horizontal layout: Solvent Clean -> BLAST (dimmed center) -> Blow-Down. Arrows connecting them.
2. **Solvent cleaning methods panel (Block D):** Wipe, immersion, vapor degrease comparison.
3. **Oil-free air verification (Block E):** ASTM D4285 blotter test visual.
4. **Contamination sources table (Block F):** Common contaminants and their effects on primer adhesion.
5. **"What NOT to Do" callout (Block G):** Common mistakes in cleaning for priming.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 13.5" / 20.0" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stages 1 and 3 highlighted (Teal)
ZONE 3 -- TWO-PHASE CLEANING HERO (4.2"--13.5" / ~9.3")
ZONE 4 -- SOLVENT METHODS + OIL-FREE AIR (13.5"--20.0" / ~6.5")
ZONE 5 -- CONTAMINATION TABLE (20.0"--26.5" / ~6.5")
ZONE 6 -- WHAT NOT TO DO + SAFETY (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CLEANING` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Industrial Priming -- Stages 1 & 3 of 8` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Blasting cannot remove oil. Compressed air can carry oil. Clean first, verify second -- or watch your primer fail.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stages 1 and 3 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Stage 1: Remove oils before blast  |  Stage 3: Remove blast dust before prime`

---

### ZONE 3 -- Two-Phase Cleaning Hero

**Section label:** `TWO CLEANING STEPS -- ONE BEFORE BLAST, ONE AFTER` -- Y: 4.4".

**BLOCK B -- Three-Panel Sequence (Y: 5.0" to 13.0")**

Three large panels in a horizontal row connected by arrows:

**Panel 1 -- Solvent Clean (X: 0.5", W: 7.0", H: 7.5"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#2EC4B6`
- Badge: `STAGE 1` fill `#2EC4B6`
- Title: `SOLVENT CLEAN` Barlow SemiBold 24 pt `#F0EDE8`
- Subtitle: `SSPC-SP1` JetBrains Mono 16 pt `#2EC4B6`
- Content (Inter Regular 14 pt `#F0EDE8`, line height 160%):
  - `Purpose: Remove oils, greases, waxes, drawing compounds`
  - `Method: Wipe with solvent-dampened cloth, or vapor degrease, or immersion in solvent tank`
  - `Criterion: No visible oil or residue`
  - `Timing: BEFORE abrasive blasting -- always`
- Bottom callout: `Why first? Blasting over oil drives contamination INTO the profile -- worse than not blasting at all.` Inter Medium 13 pt `#E8A020`

**Center -- Blast (dimmed, X: 8.5", W: 7.0"):**
- Rounded rect, fill `#252B3D`, top accent 4 pt `#3A4055`
- Title: `ABRASIVE BLAST` Barlow SemiBold 20 pt `#F0EDE8` at 40%
- Subtitle: `(Covered in Poster #705)` Inter Regular 14 pt `#F0EDE8` at 30%
- Dimmed to indicate this is not the focus of this poster

**Panel 3 -- Blow-Down (X: 16.5", W: 7.0", H: 7.5"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#2EC4B6`
- Badge: `STAGE 3` fill `#2EC4B6`
- Title: `BLOW-DOWN` Barlow SemiBold 24 pt `#F0EDE8`
- Subtitle: `Post-Blast Cleaning` JetBrains Mono 14 pt `#2EC4B6`
- Content:
  - `Purpose: Remove blast dust, abrasive fragments, and loose particles`
  - `Method: Oil-free compressed air OR industrial vacuum`
  - `Verify air: ASTM D4285 blotter test`
  - `Timing: Immediately after blast, before priming`
- Bottom callout: `Oil in the air line deposits an invisible film that kills adhesion. The blotter test catches it.` Inter Medium 13 pt `#E8A020`

**Arrows:** Large right-pointing arrows between panels, 3 pt `#3A4055`.

---

### ZONE 4 -- Solvent Methods + Oil-Free Air

**Two-column layout (Y: 13.7" to 19.8"):**

**Left -- Solvent Cleaning Methods (X: 0.5", W: 11.0"):**

Section label: `SSPC-SP1 METHODS` Barlow Condensed ExtraBold 22 pt `#2EC4B6`.

| Method | Best For | Limitation |
|---|---|---|
| Solvent wipe (rag) | Small areas, field work | Labor-intensive; rag reuse spreads contamination |
| Vapor degrease | Production parts, consistent clean | Equipment cost; solvent VOC/regulatory |
| Immersion tank | Bulk parts, heavy soils | Solvent bath must be maintained; disposal |
| Emulsion clean | Heavy oils with water rinse | Requires thorough rinse and dry before blast |

Data: Inter Regular 13 pt. Headers: Barlow SemiBold 13 pt `#2EC4B6`.

Key rule callout:
- `RULE: Use clean solvent and clean rags. A dirty rag just redistributes oil.` Inter Medium 14 pt `#E8A020`

**Right -- ASTM D4285 Blotter Test (X: 12.0", W: 11.5"):**

Section label: `OIL-FREE AIR VERIFICATION` Barlow Condensed ExtraBold 22 pt `#E8A020`.

Visual: Simple diagram showing compressed air nozzle aimed at white blotter paper.

Steps:
1. `Hold clean white blotter paper 18" from air nozzle`
2. `Direct air stream onto paper for 60 seconds`
3. `Inspect paper for oil stains or moisture`
4. `PASS: Paper remains clean and dry`
5. `FAIL: Any discoloration = oil or water in line`

JetBrains Mono 13 pt `#F0EDE8`. Step numbers in `#E8A020`.

Fail action: `If blotter test fails: drain moisture traps, replace compressor oil separator, re-test before proceeding.` Inter Medium 13 pt `#E05C5C`.

---

### ZONE 5 -- Contamination Sources Table

**Section label:** `CONTAMINANTS AND THEIR EFFECTS ON PRIMER` -- Y: 20.2".

**BLOCK F -- Contamination Table (Y: 20.8" to 26.3")**

| Contaminant | Source | Effect on Primer | Detection |
|---|---|---|---|
| Cutting oil / drawing compound | Fabrication residue | Adhesion failure, delamination | Visual, UV fluorescence |
| Mill scale | Hot-rolled steel surface | Electrical barrier (defeats IOZ galvanic) | Visual -- dark blue-gray flakes |
| Flash rust | Humid air on blasted steel | Weak bond under primer | Visual -- orange-brown staining |
| Soluble salts (Cl-, SO4 2-) | Marine air, chemical exposure | Osmotic blistering, underfilm corrosion | Bresle patch (ISO 8502-6) |
| Weld spatter / slag | Welding residue | Primer bridges over -- corrosion underneath | Visual, scraper test |
| Compressed air oil | Compressor lubricant carry-over | Invisible adhesion barrier | ASTM D4285 blotter test |

Header: `#3A4055`. Alternating rows. Data: Inter Regular 12 pt.

---

### ZONE 6 -- What NOT to Do + Safety

**Two-column layout (Y: 26.7" to 32.3"):**

**Left -- Common Mistakes (X: 0.5", W: 11.0"):**

Section label: `WHAT NOT TO DO` Barlow Condensed ExtraBold 22 pt `#E05C5C`.

Four mistake cards (vertical stack):

| Mistake | Why It Fails |
|---|---|
| Blast without solvent cleaning first | Oil gets hammered into the profile |
| Use dirty rags for solvent wipe | Redistributes contamination |
| Skip the blotter test | Invisible oil from air line kills adhesion |
| Chemical clean after blast | Wets the blasted surface; causes flash rust |

Each: small rounded rect, fill `#1E2435`, left accent `#E05C5C`. Mistake: Barlow SemiBold 14 pt `#E05C5C`. Why: Inter Regular 13 pt `#F0EDE8`.

**Right -- Safety (X: 12.0", W: 11.5"):**

Section label: `SAFETY -- CLEANING SOLVENTS` Barlow Condensed ExtraBold 22 pt `#E05C5C`.

- Rounded rect, fill `#1E2435`, left accent `#E05C5C`
- Hazards:
  - `Solvent vapors: flammable and toxic -- ventilate work area`
  - `Skin contact: dermatitis from repeated exposure -- gloves mandatory`
  - `VOC regulations: check local air permit limits before solvent cleaning`
  - `Vapor degreasing: declining due to VOC/HAP restrictions`
  - `Compressed air: never direct at skin -- injection hazard at high pressure`
- Inter Regular 13 pt `#F0EDE8`

---

### ZONE 7 -- Footer

Standard. Title: `Cleaning -- Priming`. Version `v1.0 -- 2026`.
Disclaimer note: `Source: General industry knowledge; SSPC-SP1; ASTM D4285; Watson Research Brief.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cleaning Priming -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster covers two stages (1 and 3) because they are both cleaning steps bookending the blast operation. The three-panel hero makes the sequence unmistakable: clean -> blast -> clean again. The blotter test visual is a practical detail that separates a good shop from a mediocre one -- most coatings people know about SSPC-SP1 but fewer actually verify their air lines.

---

*Alaina -- Poster #706 -- Construction Workup v1.0 -- 2026-04-26*
