---
Project: Plating Posters Inc
Poster Number: 313
Title: "Rinse -- PAA -- Pre-Treatment"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 5: PAA, Section 5.3)"
Technical Source: Pre-etch rinse stage for phosphoric acid anodizing. Removes alkaline cleaner chemistry before etch to prevent cross-contamination and streaking.
Process Scope: Rinse -- Pre-Treatment (Stage 2 of PAA sequence)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Anodizing
  - PAA
  - Rinse
  - ConstructionWorkup
  - ClusterAnodPAA
---

# Poster #313 -- Construction Workup
## Rinse -- PAA -- Pre-Treatment

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 2 of the PAA sequence. This is the rinse between alkaline cleaning and the etch/grit blast step. Its purpose is to remove alkaline cleaner chemistry before the next stage. Rinse posters are simpler than main-tank posters but must convey why this "boring" step matters -- cross-contamination and streaking originate here.

Hero visual: cascade rinse tank diagram showing counter-flow water movement and dragout control.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cascade rinse tank hero (Block B):** Double-cascade rinse with counter-flow arrows, overflow weir, parts on rack. Built with rectangles, lines, arrows.
2. **Operating window panel (Block D):** Compact parameter card.
3. **Dragout control tips (Block E):** Best practices for reducing chemical carryover.
4. **Conductivity monitoring panel (Block F):** Why and how to measure rinse quality.
5. **Contamination cascade (Block G):** What happens downstream if this rinse fails.

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
  Stage 2 highlighted (Teal)
ZONE 3 -- CASCADE RINSE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- OPERATING WINDOW + WATER QUALITY (14.5"--20.5" / ~6.0")
ZONE 5 -- DRAGOUT CONTROL + CONDUCTIVITY (20.5"--26.5" / ~6.0")
ZONE 6 -- CONTAMINATION CASCADE (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `PAA Pre-Treatment Rinse -- Stage 2 of 7` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Remove the cleaner before it contaminates the etch. Dwell, drain, rinse -- in that order.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 2 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean surface with residual alkaline cleaner  -->  After: Rinse-free surface ready for etch or grit blast`

---

### ZONE 3 -- Cascade Rinse Hero

**Section label:** `THE CASCADE RINSE` -- Y: 4.4".

**BLOCK B -- Double-Cascade Rinse Diagram**

Y: 5.0" to 13.5".

**Two rinse tanks side by side:**

*Tank 1 (first rinse -- dirtier):*
- Rounded rect, X: 1.5", Y: 5.5", W: 9.5", H: 6.5"
- Fill: `#252B3D` at 80%
- Border: 2 pt `#C8D0D8`
- Label: `RINSE 1 (DRAG-OUT)` Barlow SemiBold 14 pt `#2EC4B6`

*Tank 2 (second rinse -- cleaner):*
- Rounded rect, X: 13.0", Y: 5.5", W: 9.5", H: 6.5"
- Fill: `#252B3D` at 40%
- Border: 2 pt `#C8D0D8`
- Label: `RINSE 2 (FINAL)` Barlow SemiBold 14 pt `#27AE60`

**Counter-flow arrows:**
- Arrow from Tank 2 overflow to Tank 1: Stroke 3 pt `#2EC4B6`, arrowhead left
- Label above arrow: `COUNTER-FLOW: Fresh water enters Tank 2, overflows to Tank 1` Inter Regular 12 pt `#2EC4B6`

**Fresh water inlet (Tank 2 bottom-right):**
- Arrow pointing into Tank 2 from right
- Label: `FRESH WATER IN` JetBrains Mono 12 pt `#27AE60`

**Drain (Tank 1 bottom-left):**
- Arrow pointing out of Tank 1 to left
- Label: `TO DRAIN / WASTE TREATMENT` JetBrains Mono 12 pt `#F0EDE8` at 60%

**Parts on rack (in each tank):**
- 2 vertical rects per tank, `#C8D0D8` at 40%
- Arrow between tanks showing part movement direction (left to right)

**Dwell zone (above Tank 1):**
- Dashed outline rectangle above Tank 1, X: 1.5", Y: 4.8", W: 9.5", H: 0.6"
- Label: `DWELL 10--15 sec over cleaner tank before rinsing -- reduces dragout 50--80%` Inter Medium 13 pt `#E8A020`

**Bath parameter labels inside tanks:**

Tank 1:
- `City water acceptable` JetBrains Mono 13 pt `#F0EDE8`
- `Ambient temp` JetBrains Mono 13 pt `#F0EDE8` at 70%

Tank 2:
- `DI preferred for quality work` JetBrains Mono 13 pt `#27AE60`
- `Target: < 500 uS/cm` JetBrains Mono 13 pt `#E8A020`

**Bottom callout (Y: 12.5"):**
- `Counter-flow rinsing is the most water-efficient method -- fresh water only enters the final stage.` Inter Medium 14 pt `#2EC4B6`

---

### ZONE 4 -- Operating Window + Water Quality

**Section label:** `OPERATING PARAMETERS` -- Y: 14.7".

**Two-column layout (Y: 15.3" to 20.3"):**

**Left -- Operating Window (X: 0.5", W: 11.0"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#2EC4B6` 0.06"
- Title: `RINSE PARAMETERS` Barlow SemiBold 18 pt `#2EC4B6`

| Parameter | Value |
|---|---|
| Water quality | City water acceptable; DI preferred |
| Temperature | Ambient (room temperature) |
| Time | 30--60 seconds with agitation |
| Method | Double cascade (counter-flow) preferred |
| Conductivity target | < 500 uS/cm in final rinse |
| Agitation | Part movement or air sparging |

Labels: Inter Medium 13 pt `#F0EDE8` at 60%. Values: JetBrains Mono 13 pt `#F0EDE8`.

**Right -- Water Quality Matters (X: 12.0", W: 11.5"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `WHY WATER QUALITY MATTERS` Barlow SemiBold 18 pt `#E8A020`

Body (Inter Regular 14 pt `#F0EDE8`, line height 155%):

> Alkaline cleaner dragged into the etch bath:
> -- Accelerates etch rate (uncontrolled)
> -- Contaminates etch with surfactants
> -- Produces streaking on the etched surface
>
> For PAA, surface uniformity directly affects oxide uniformity, which directly affects bond uniformity.
>
> Every contamination source in the pre-treatment stages is amplified by the thin (0.5--1.5 um) PAA oxide.

---

### ZONE 5 -- Dragout Control + Conductivity

**Section label:** `DRAGOUT CONTROL + RINSE VERIFICATION` -- Y: 20.7".

**Two-column layout (Y: 21.3" to 26.3"):**

**Left -- Dragout Reduction (X: 0.5", W: 11.0"):**
- Title: `REDUCING DRAGOUT` Barlow Condensed ExtraBold 22 pt `#F0EDE8`

Four tip cards stacked vertically:

| Tip | Detail | Impact |
|---|---|---|
| Dwell over cleaner tank | 10--15 sec drain time | Reduces carryover 50--80% |
| Slow withdrawal | Lift rack slowly from cleaner | Thin film vs. thick drops |
| Rack design | Minimize horizontal surfaces | Less pooling, less carryover |
| Rinse agitation | Air sparging or part movement | Faster contamination removal |

Each: rounded rect H: 1.0", fill `#1E2435`, left accent `#2EC4B6` 0.06". Data: Inter Regular 13 pt.

**Right -- Conductivity Monitoring (X: 12.0", W: 11.5"):**
- Title: `CONDUCTIVITY CHECK` Barlow Condensed ExtraBold 22 pt `#F0EDE8`
- Rounded rect, H: 4.0", fill `#1E2435`, left accent `#E8A020` 0.06"

Body (Inter Regular 14 pt `#F0EDE8`, line height 155%):

> A conductivity meter is the simplest, fastest way to verify rinse quality.
>
> **Target:** < 500 uS/cm in final rinse stage
>
> **How to read it:**
> -- Rising conductivity = dragout accumulating
> -- Steady low conductivity = rinse is working
> -- Spike after rack enters = normal; should recover in 30--60 sec
>
> If conductivity stays elevated, increase fresh water flow rate or add a rinse stage.

Key value callout: `< 500 uS/cm` JetBrains Mono 22 pt `#E8A020`

---

### ZONE 6 -- Contamination Cascade

**Section label:** `WHAT HAPPENS IF THIS RINSE FAILS` -- Y: 26.7".

**BLOCK G -- Three-step cascade (Y: 27.3" to 32.3"):**

Three connected cards showing the downstream chain reaction:

| Step | Card Title | Detail | Color |
|---|---|---|---|
| 1 | ALKALINE CARRYOVER | Residual cleaner enters etch bath; etch rate becomes uncontrolled; streaking on surface | `#E8A020` |
| 2 | NON-UNIFORM ETCH | Streaked surface produces non-uniform PAA oxide growth; pore structure varies across part | `#E05C5C` |
| 3 | BOND FAILURE | Non-uniform oxide = non-uniform adhesive interlocking = weak bonds = potential in-service failure | `#E05C5C` |

Each card: Rounded rect W: 7.33", H: 4.0", fill `#1E2435`, top accent 4 pt in card color.
Arrows between cards: 3 pt `#3A4055`, pointing right.

Card interior:
- Number badge: Barlow Condensed ExtraBold 36 pt, card color
- Title: Barlow SemiBold 18 pt, card color
- Detail: Inter Regular 13 pt `#F0EDE8`

Bottom summary:
- `A 30-second rinse prevents a 30-day rework cycle. Rinse thoroughly.` Inter Medium 14 pt `#27AE60`

---

### ZONE 7 -- Footer

Standard. Title: `Rinse -- PAA -- Pre-Treatment`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; ASTM D3933. Rinse parameters shown are typical values for counter-flow cascade rinsing before anodizing pre-treatment.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse PAA Pre-Treatment -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Rinse posters must fight the perception that rinsing is trivial. The contamination cascade (Zone 6) is the key educational element -- it connects a "boring" rinse step to catastrophic bond failure in three logical steps. The dragout reduction tips are immediately actionable for any operator. Conductivity monitoring gives them a number to hit.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #313 -- Construction Workup v1.0*
*2026-04-26*
