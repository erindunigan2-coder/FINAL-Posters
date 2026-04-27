---
Project: Plating Posters Inc
Poster Number: 718
Title: "Application -- Protective Coatings"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster 8 technical reference (Protective Coatings -- Epoxy / Urethane) -- Watson Research Brief (Section 8.6)"
Process Scope: Application for protective coatings -- Stage 5 of 8
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ProtectiveCoatings
  - Application
  - ConstructionWorkup
  - PaintingCoating
  - Cluster8
---

# Poster #718 -- Construction Workup
## Application -- Protective Coatings

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 5 of 8. This is big-iron spraying. Airless at 2,000-3,500 psi, building 3-10 mils per coat, targeting total systems of 6-20+ mils. Two-component reactive chemistries (epoxy and urethane) with pot lives measured in minutes to hours. The application stage covers epoxy primer/intermediate, polyurethane topcoat, and the special case of solventless (100% solids) epoxy for tank lining and concrete floors -- heated plural-component spray systems that mix at the gun.

Hero visual: multi-coat system architecture diagram showing the three-layer stack (zinc-rich primer + epoxy intermediate + urethane topcoat) with DFT targets and chemistry at each layer, paired with application parameter tables.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Multi-coat system architecture hero (Block B):** Cross-section of the full protective coating system showing three layers with DFT, chemistry, and purpose.
2. **Epoxy application parameters table (Block D):** Standard, high-build, and tank lining specifications.
3. **Polyurethane topcoat and solventless epoxy panel (Block E):** Topcoat parameters and the heated plural-component special case.
4. **Defect strip (Block F):** 4 application defects.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 21.0" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 5 highlighted (Amber)
ZONE 3 -- MULTI-COAT SYSTEM HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- EPOXY APPLICATION PARAMETERS (14.5"--21.0" / ~6.5")
ZONE 5 -- URETHANE TOPCOAT + SOLVENTLESS (21.0"--27.0" / ~6.0")
ZONE 6 -- APPLICATION DEFECTS (27.0"--32.5" / ~5.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `APPLICATION` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Protective Coatings -- Stage 5 of 8` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Two components. One pot life. Airless spray at 3,000 psi. Building 6-20 mils of barrier between the steel and everything the world throws at it.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 5 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Profiled, primed substrate  -->  After: Multi-coat system applied to target DFT, ready for cure`

---

### ZONE 3 -- Multi-Coat System Hero

**Section label:** `THE PROTECTIVE COATING SYSTEM -- LAYER BY LAYER` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- System Architecture Diagram (Y: 5.0" to 14.0")**

Full-width rounded rect, W: 23.0", H: 8.5", fill `#1E2435`, top accent 4 pt `#E8A020`.

**Left -- Cross-Section Stack (X: 1.0", W: 10.0", Y: 5.5" to 13.0"):**

Stacked horizontal layers (bottom to top):

Layer 0 -- Substrate (Y: 12.0"):
- Rect fill `#3A4055`, H: 1.0", W: 9.0"
- Label: `STEEL SUBSTRATE` JetBrains Mono 12 pt `#F0EDE8`
- Profile texture on top edge

Layer 1 -- Primer (Y: 10.5"):
- Rect fill `#E8A020` at 20%, H: 1.2", W: 9.0"
- Label: `PRIMER` Barlow SemiBold 14 pt `#E8A020`
- Callout: `Zinc-rich (IOZ/OZ) or epoxy | 2-4 mils | Galvanic or barrier protection`
- JetBrains Mono 11 pt `#F0EDE8`

Layer 2 -- Intermediate (Y: 8.8"):
- Rect fill `#2EC4B6` at 20%, H: 1.5", W: 9.0"
- Label: `INTERMEDIATE / BUILD COAT` Barlow SemiBold 14 pt `#2EC4B6`
- Callout: `High-build epoxy | 4-8 mils per coat | Barrier + chemical resistance`

Layer 3 -- Topcoat (Y: 7.0"):
- Rect fill `#27AE60` at 20%, H: 1.0", W: 9.0"
- Label: `TOPCOAT / FINISH` Barlow SemiBold 14 pt `#27AE60`
- Callout: `Aliphatic polyurethane | 2-3 mils | UV, color, gloss retention`

Total DFT bracket on right side:
- Bracket spanning all three coating layers
- `TOTAL SYSTEM: 6-20+ mils` Barlow SemiBold 16 pt `#E8A020`

**Right -- System Performance (X: 12.0", W: 10.5"):**

| System | Total DFT | B117 Salt Spray |
|---|---|---|
| Epoxy primer + epoxy build (industrial) | 6-12 mils | 2,000-4,000 hr |
| IOZ + epoxy + urethane (marine/bridge) | 10-14 mils | 5,000-10,000+ hr |
| Solventless epoxy tank lining | 12-20+ mils | 5,000-10,000+ hr |
| High-build epoxy on concrete (floors) | 10-15 mils | N/A (chemical resistance) |

JetBrains Mono 11 pt `#F0EDE8`.

**Aliphatic vs. Aromatic callout (Y: 12.5"):**
- Pill, fill `#252B3D`, W: 10.0", H: 0.5"
- Text: `Aliphatic urethane (topcoat): UV-stable, non-yellowing, exterior. Aromatic urethane: yellows in UV, interior or under topcoat only.` Inter Regular 12 pt `#F0EDE8`

---

### ZONE 4 -- Epoxy Application Parameters

**Section label:** `EPOXY APPLICATION -- THREE TIERS` -- Y: 14.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK D -- Three-Tier Table**

Y: 15.3" to 20.8". Column widths (23.0" total):
- Parameter (4.5") | Standard Build (5.5") | High-Build (5.5") | Tank Lining (7.5")

| Parameter | Standard Build | High-Build | Tank Lining |
|---|---|---|---|
| DFT per coat | 3-5 mils | 5-10 mils | 4-8 mils |
| Total system DFT | 6-12 mils | 10-20 mils | 12-20+ mils |
| Number of coats | 2-3 | 2-3 | 3-4 |
| Mix ratio (A:B by volume) | 1:1 to 4:1 | Same | Same |
| Pot life at 77 F | 30 min - 4 hr | 20 min - 2 hr | 30 min - 2 hr |
| Induction time | 15-30 min (polyamide) | Varies | Per TDS |
| Spray pressure (airless) | 2,000-3,000 psi | 2,500-3,500 psi | 2,500-3,500 psi |
| Tip size | 0.017-0.025" | 0.021-0.031" | 0.019-0.025" |
| Volume solids | 60-80% | 85-100% | 90-100% (solventless) |

Data: JetBrains Mono 11 pt `#F0EDE8`.

Footnote: `Induction time: after mixing A+B, allow 15-30 min of "sweat-in" before application (polyamide-cured epoxy). Amine-adduct hardeners require NO induction time. Always check TDS.` Inter Regular 12 pt `#E8A020`.

---

### ZONE 5 -- Urethane Topcoat + Solventless Epoxy

**Section label:** `TOPCOAT AND SOLVENTLESS -- TWO SPECIAL CASES` -- Y: 21.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK E -- Two-Column Panel**

Y: 21.8" to 26.8".

**Left -- Polyurethane Topcoat (X: 0.5", W: 11.0"):**
- Rounded rect, fill `#1E2435`, left accent `#27AE60` 0.06"
- Title: `POLYURETHANE TOPCOAT` Barlow SemiBold 18 pt `#27AE60`

| Parameter | Range |
|---|---|
| DFT per coat | 2.0-3.0 mils |
| Coats | 1-2 |
| Mix ratio (A:B) | 2:1 to 5:1 (varies) |
| Pot life at 77 F | 1-4 hr (aliphatic); 30 min - 2 hr (aromatic) |
| Application | Airless, HVLP, conventional air spray |
| Volume solids | 50-75% |

JetBrains Mono 11 pt `#F0EDE8`.

Key note: `Aliphatic isocyanate (HDI, IPDI): UV-stable, non-yellowing, excellent gloss. Used for ALL exterior topcoats. Aromatic (MDI, TDI): yellows, chalks in UV. Interior or under-topcoat only.` Inter Regular 12 pt `#F0EDE8`.

**Right -- Solventless / 100% Solids Epoxy (X: 12.0", W: 11.5"):**
- Rounded rect, fill `#1E2435`, left accent `#E05C5C` 0.06"
- Title: `SOLVENTLESS EPOXY (100% SOLIDS)` Barlow SemiBold 18 pt `#E05C5C`

Bullet list (Inter Regular 13 pt `#F0EDE8`, line height 155%):
- `Zero VOC -- no solvents to evaporate`
- `Used for: tank lining, concrete floor coatings, immersion service`
- `High viscosity requires HEATED spray equipment`
- `Plural-component proportioning system: mixes A+B at the gun or in a static mixer`
- `Material heated to 100-140 F to reduce viscosity for spray`
- `Pot life: MINUTES, not hours -- mixing happens continuously at point of application`
- `NSF/ANSI 61 compliant formulations available for potable water tanks`

Warning: `Solventless epoxy application requires specialized equipment (heated hoses, proportioners, static mixers). Do not attempt with standard pot-and-spray setups.` Inter Medium 13 pt `#E05C5C`.

---

### ZONE 6 -- Application Defects

**Section label:** `WHAT GOES WRONG -- 4 APPLICATION DEFECTS` -- Y: 27.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK F -- Four Problem Cards (Y: 27.8" to 30.5")**

Each card: Rounded rect, W: 5.5", H: 2.5", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | POT LIFE EXCEEDED (GELLED) | Mixed material too long ago; temperature too high | Reduce batch size; track pot life timer; keep material cool |
| 2 | 6.33" | DFT TOO THICK (SAGS / CURTAINS) | Spray too close, too slow, or too much overlap | Increase gun distance; increase travel speed; reduce overlap to 50% |
| 3 | 12.16" | DFT TOO THIN (HOLIDAYS) | Insufficient overlap, gun too far, or pressure too low | Stripe coat edges/welds first; verify tip size and pressure; slow down |
| 4 | 18.0" | WRONG MIX RATIO (OFF-RATIO) | Proportioner out of calibration or manual mix error | Verify ratio by weight or volume before each batch; calibrate proportioner |

**Key insight callout (Y: 31.0" to 32.3"):**
- Text: `Every defect in protective coating application is either too much or too little. Too thick = sags, mud cracking, solvent entrapment. Too thin = holidays, premature failure at thin spots. The DFT gauge is the most important tool in the applicator's hand -- not the spray gun.` -- Inter Medium, 14 pt, `#E8A020`

---

### ZONE 7 -- Footer

Standard. Title: `Application -- Protective Coatings`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Application Protective Coatings -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The multi-coat system cross-section is the hero concept because protective coatings are systems, not single products. The three-layer stack -- primer, intermediate, topcoat -- with DFT and chemistry at each layer makes the architecture visible. The three-tier epoxy table (standard, high-build, tank lining) serves three different audiences from the same poster. The solventless epoxy panel addresses the specialized world of heated plural-component application -- a completely different equipment set from standard pot-and-spray.

---

*Alaina -- Poster #718 -- Construction Workup v1.0 -- 2026-04-26*
