---
Project: Plating Posters Inc
Poster Number: 407
Title: "Cooling & Unloading -- PVD"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 1: PVD, Section 1.8)"
Technical Source: PVD post-deposition cooling under vacuum, controlled venting, thermal shock prevention, unloading procedures, hot-surface PPE, and visual color verification upon removal.
Process Scope: PVD cooling and unloading (Stage 9 of 10)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - PVD
  - Cooling
  - Unloading
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #407 -- Construction Workup
## Cooling & Unloading -- PVD

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 9 of 10. The coating is deposited -- now it must be cooled without ruining it. Venting a PVD chamber to atmosphere while parts are above 200 C oxidizes the fresh coating surface and discolors it. Cooling under vacuum (or controlled inert gas backfill) is mandatory. This poster covers the cool-down sequence, venting protocol, unloading safety, and what the operator should look for immediately upon opening the chamber.

Design philosophy: a cool-down timeline as the hero showing temperature vs. time from deposition end to chamber open, a clear "DO NOT VENT" temperature threshold, unloading safety rules, and a visual color verification strip showing expected coating colors.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cool-down timeline (Block B -- HERO):** Horizontal timeline showing temperature decreasing from 500 C to ambient, with key thresholds marked. Built from rectangles and text -- no complex curves.
2. **Venting protocol (Block C):** Decision flow -- when to vent, how to vent, inert backfill option.
3. **Unloading safety rules (Block D):** PPE and handling checklist.
4. **Color verification strip (Block E):** Expected colors for common PVD coatings -- TiN (gold), TiAlN (violet), CrN (silver), TiCN (blue-gray), DLC (black), ZrN (gold-yellow).
5. **Common cooling failures (Block F):** Four failure cards.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.0" / 20.0" / 25.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 9 highlighted (Amber -- post-treatment)
ZONE 3 -- COOL-DOWN TIMELINE / HERO (4.2"--14.0" / ~9.8")
ZONE 4 -- VENTING PROTOCOL + UNLOADING SAFETY (14.0"--20.0" / ~6.0")
ZONE 5 -- COLOR VERIFICATION STRIP (20.0"--25.5" / ~5.5")
ZONE 6 -- COMMON COOLING FAILURES (25.5"--32.5" / ~7.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `COOLING & UNLOADING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `PVD -- Stage 9 of 10 -- Vacuum Cool-Down, Venting, and Safe Removal` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Never vent above 200 C. A perfect coating can be ruined in the last 30 minutes by impatience. Cool under vacuum, verify color on removal, and handle with heat-rated gloves.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 9 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Deposition complete (Stage 8) --> After: Parts cooled, chamber vented, parts removed for inspection`

---

### ZONE 3 -- Cool-Down Timeline (HERO)

**Section label:** `COOL-DOWN SEQUENCE -- FROM DEPOSITION TO CHAMBER OPEN` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Timeline Diagram (Y: 5.0" to 13.8")**

Horizontal timeline spanning full width within margins (X: 0.5" to 23.5").

**Timeline base:** Rectangle, X: 0.5", Y: 9.0", W: 23.0", H: 0.08", fill `#C8D0D8`.

**Temperature axis (left side, vertical):**
- Y: 5.5" to 12.5" (7.0" tall)
- Labels (JetBrains Mono 12 pt `#F0EDE8` at 60%): `500 C` at top, `400 C`, `300 C`, `200 C`, `150 C`, `100 C`, `Ambient` at bottom
- Horizontal dashed lines at each temp level, stroke 1 pt `#3A4055`

**Time axis (bottom):**
- Labels: `0 min`, `30 min`, `60 min`, `90 min`, `120 min`, `150 min`
- JetBrains Mono 12 pt `#F0EDE8` at 60%

**Cool-down curve:** Stepped rectangles descending from 500 C to ambient, simulating exponential decay. Each step is a filled rectangle showing the temperature range for that time segment.

**Key threshold markers:**

*200 C threshold -- CRITICAL:*
- Full-height dashed line at ~90 min mark, stroke 3 pt `#E05C5C`
- Label box: Rounded rect, fill `#E05C5C`, text `#F0EDE8`
- Text: `200 C -- MINIMUM VENT TEMPERATURE` Barlow SemiBold 16 pt
- Below: `DO NOT open chamber above this temperature` Inter Medium 14 pt `#E05C5C`

*150 C threshold -- RECOMMENDED:*
- Full-height dashed line at ~105 min mark, stroke 2 pt `#E8A020`
- Label: `150 C -- RECOMMENDED VENT TEMP` Barlow SemiBold 14 pt `#E8A020`
- Below: `Preferred for oxidation-sensitive coatings` Inter Regular 12 pt `#E8A020`

**Three phase labels along the timeline:**

| Phase | X Range | Fill | Label |
|---|---|---|---|
| VACUUM HOLD | 0.5" to 10.0" | `#1E2435` | `Cool under vacuum (< 10^-2 mbar)` |
| INERT BACKFILL (optional) | 10.0" to 16.0" | `#252B3D` | `Ar or N2 backfill to accelerate cooling` |
| VENT TO ATMOSPHERE | 16.0" to 23.5" | `#1E2435` | `Controlled vent once below 150-200 C` |

Phase labels: Barlow SemiBold 14 pt, accent color. Descriptions: Inter Regular 12 pt `#F0EDE8` at 70%.

**Key metrics callout (right side):**
- Rounded rect, X: 16.5", Y: 5.5", W: 7.0", H: 3.0", fill `#1E2435`, left accent `#E8A020`
- Title: `TYPICAL COOL-DOWN` Barlow SemiBold 16 pt `#E8A020`
- Data: JetBrains Mono 13 pt `#F0EDE8`
```
Total time: 30-180 min
Rate: 1-5 C/min (radiative)
With Ar backfill: 2-3x faster
Load mass dependent
```

---

### ZONE 4 -- Venting Protocol + Unloading Safety

**Section label:** `VENTING AND UNLOADING` -- Y: 14.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**Two-column layout (Y: 14.8" to 19.8"):**

**Left -- Venting Protocol (X: 0.5", W: 11.0"):**
- Rounded rect H: 4.8", fill `#1E2435`, left accent `#E8A020`
- Title: `VENTING PROTOCOL` Barlow SemiBold 20 pt `#E8A020`

Steps (Inter Medium 14 pt `#F0EDE8`, numbered):
1. `Confirm substrate temp < 200 C (prefer < 150 C)`
2. `Close all gas valves (Ar, N2, reactive gases)`
3. `Close high-vacuum valve (gate valve to turbo/cryo)`
4. `Open vent valve slowly -- controlled atmospheric backfill`
5. `Wait for pressure to equalize to atmospheric`
6. `Open chamber door`

Bottom warning:
- `NEVER vent while turbo pump is at full speed -- spin-down first or use soft-vent valve` Inter Medium 12 pt `#E05C5C`

**Right -- Unloading Safety (X: 12.0", W: 11.5"):**
- Rounded rect H: 4.8", fill `#1E2435`, left accent `#E05C5C`
- Title: `UNLOADING SAFETY` Barlow SemiBold 20 pt `#E05C5C`

Rules (Inter Medium 14 pt `#F0EDE8`):
- `Heat-resistant gloves (Kevlar or silicone, rated > 250 C)`
- `Parts may still be 100-200 C even after venting`
- `Use IR thermometer to verify surface temp before bare-hand contact`
- `Never reach into chamber with bare forearms -- hot fixtures`
- `Verify rotation has stopped before reaching in`
- `Place parts on heat-resistant tray -- not directly on workbench`

Bottom callout:
- `Burns from "cool" PVD parts are the #1 unloading injury -- always verify with thermometer` Inter Medium 13 pt `#E05C5C`

---

### ZONE 5 -- Color Verification Strip

**Section label:** `VISUAL COLOR CHECK -- FIRST QUALITY GATE` -- Y: 20.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK E -- Six Coating Color Cards (Y: 20.8" to 25.3")**

Six cards in a single row. Each: Rounded rect W: 3.67", H: 4.3", fill `#1E2435`, radius 6.

| Card | X | Coating | Color Swatch Hex | Expected Color Name | Off-Color Means |
|---|---|---|---|---|---|
| 1 | 0.5" | TiN | `#C8A020` | Gold | Blue/gray = N2 excess; silver = metallic Ti |
| 2 | 4.5" | TiAlN | `#7A6A8A` | Dark violet / gray | Brown = oxidized; too light = Al-rich |
| 3 | 8.5" | CrN | `#A8B0B8` | Silver / light gray | Dark = Cr-rich; iridescent = thin/non-uniform |
| 4 | 12.5" | TiCN | `#5A6A8A` | Blue-gray | Brown = carbon-rich; green = off-stoich |
| 5 | 16.5" | DLC | `#2A2A2A` | Black / dark gray | Brown tint = too much H; iridescent = too thin |
| 6 | 20.5" | ZrN | `#D4B830` | Gold-yellow | Green tint = off-stoich; dull = contamination |

Interior per card:
- Color swatch: Rounded rect, W: 2.5", H: 1.2", fill with swatch hex, centered at top of card
- Coating name: Barlow SemiBold 16 pt `#F0EDE8`, centered
- Expected: Inter Regular 12 pt `#27AE60`
- Off-color warning: Inter Regular 11 pt `#E05C5C`

---

### ZONE 6 -- Common Cooling Failures

**Section label:** `COOLING FAILURES -- WHAT GOES WRONG` -- Y: 25.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK F -- Four Failure Cards (Y: 26.3" to 32.3")**

Each card: Rounded rect W: 5.5", H: 5.8", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Failure | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | COATING DISCOLORATION | Vented to air above 200 C -- surface oxidation | Always verify temp < 200 C before venting; prefer < 150 C |
| 2 | 6.33" | THERMAL STRESS CRACKING | Cooled too fast (external cooling water on chamber while hot) | Use radiative cooling or gentle Ar backfill; never quench |
| 3 | 12.16" | DELAMINATION ON COOLING | Thermal expansion mismatch between coating and substrate | Multilayer architecture distributes stress; controlled cool rate |
| 4 | 18.0" | BURNS / SAFETY INCIDENT | Handling parts before temperature verification | Mandatory IR thermometer check; heat-rated gloves always |

Interior per card:
- Failure: Barlow SemiBold 15 pt `#E05C5C`
- Cause: Inter Regular 13 pt `#F0EDE8`
- Fix: Inter Medium 13 pt `#27AE60`

---

### ZONE 7 -- Footer

Standard footer. Title: `Cooling & Unloading -- PVD`. Version `v1.0 -- 2026`.

**Disclaimer:** `This poster is an educational reference tool. Cooling times and vent temperatures shown are typical industry values for PVD hard coatings. Specific procedures vary by equipment manufacturer and coating type. Consult your system manual for application-specific cooling protocols.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cooling Unloading PVD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The cool-down timeline is the hero because it communicates the single most actionable rule in PVD post-processing: do not vent above 200 C. The visual threshold lines make this impossible to miss from across the room. The color verification strip is unique to this poster and highly practical -- operators check color immediately upon opening the chamber, and this strip tells them what each coating should look like and what deviations mean. The unloading safety section addresses the most common PVD injury (burns from "cool" parts that are still 100-200 C).

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #407 -- Construction Workup v1.0*
*2026-04-26*
