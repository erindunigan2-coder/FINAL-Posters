---
Project: Plating Posters Inc
Poster Number: 447
Title: "Cooling -- DLC"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters — Watson Research Brief (Cluster 5: DLC, Sections 5.1, 5.3)"
Process Scope: Post-deposition cooling and chamber venting for DLC-coated parts
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - DLC
  - Cooling
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #447 -- Construction Workup
## Cooling -- DLC

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

DLC coatings carry extreme compressive internal stress -- 1 to 12 GPa depending on type. Cooling is not just "wait for it to get cold." Rapid cooling introduces thermal stress on top of the already high intrinsic stress, and that combination causes cracking, delamination, or buckling. This poster covers the in-vacuum cooldown sequence, controlled venting protocol, the stress-temperature relationship, and the specific risks of rushing the cooldown. It is a shorter, more focused poster than the deposition or parameter stages but the message is clear: patience here saves parts.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Cooling sequence timeline hero (Block B):** A horizontal timeline showing the cooldown phases from deposition end to chamber open. Built with rectangles and temperature curve annotation.
2. **Stress-temperature relationship (Block D):** Why thermal shock is dangerous for DLC.
3. **Venting protocol (Block E):** Step-by-step chamber venting procedure.
4. **What goes wrong (Block F):** Defects caused by improper cooling.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 14.0" / 20.0" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- COOLING TIMELINE HERO (2.9"--14.0" / ~11.1")
  Block B: Phase-by-phase cooldown sequence
ZONE 3 -- STRESS & THERMAL SHOCK (14.0"--20.0" / ~6.0")
  Block D: Why DLC hates thermal shock
ZONE 4 -- VENTING PROTOCOL (20.0"--26.5" / ~6.5")
  Block E: Step-by-step chamber venting
ZONE 5 -- COOLING DEFECTS (26.5"--32.5" / ~6.0")
  Block F: What goes wrong if you rush
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `COOLING` -- 88 pt `#F0EDE8`.
**Subheading:** `Diamond-Like Carbon -- Post-Deposition Cooldown & Venting` -- 36 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `DLC is under enormous compressive stress. Cool it wrong, and hours of deposition work crack, buckle, or peel off the part.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Cooling Timeline Hero

**Section label:** `THE COOLDOWN SEQUENCE -- PATIENCE PROTECTS THE COATING` -- Y: 3.1".

**BLOCK B -- Cooldown Timeline**

Y: 3.8" to 13.8".

**Full-width timeline (X: 0.5", W: 23.0"):**

Rounded rect container, H: 9.5", fill `#1E2435`.

Horizontal arrow baseline at Y: 8.0", X: 1.5" to 22.5", stroke 3 pt `#3A4055`, arrowhead right.

**Four phase blocks above the timeline:**

| Phase | X | W | Time | Temp Range | Color | Description |
|---|---|---|---|---|---|---|
| 1. Power Off | 1.5" | 4.5" | T = 0 | 150--200 C | `#E05C5C` | Plasma / arc extinguished. Bias voltage off. Gas flow stopped. Parts at peak process temperature. |
| 2. In-Vacuum Cool | 6.5" | 5.5" | 15--60 min | 200 C -> 80 C | `#E8A020` | Chamber remains under vacuum. Cooling is radiative only (no convective gas). Slowest phase. Monitor substrate temperature. |
| 3. Controlled Backfill | 12.5" | 5.0" | 5--15 min | 80 C -> 50 C | `#2EC4B6` | Inert gas (Ar or N2) slowly admitted to chamber. Convective cooling accelerates heat removal. Pressure rises to ~100 Torr. |
| 4. Vent to Atmosphere | 18.0" | 4.5" | 5--10 min | < 50 C | `#27AE60` | Chamber vented to atmosphere through filtered vent. Door opened only when temp < 50 C. Parts safe to handle with gloves. |

Each phase block: Rounded rect, H: 3.5", fill `#1E2435`, top accent 4 pt phase color.
Phase number: Barlow SemiBold, 16 pt, phase color.
Time: JetBrains Mono Regular, 14 pt, `#E8A020`.
Temp: JetBrains Mono Regular, 13 pt, `#F0EDE8`.
Description: Inter Regular, 13 pt, `#F0EDE8`.

**Temperature curve annotation (Y: 8.5" to 10.5"):**
- Conceptual descending curve from left (high) to right (low)
- Label at start: `150--200 C` JetBrains Mono 12 pt `#E05C5C`
- Label at end: `< 50 C` JetBrains Mono 12 pt `#27AE60`
- Annotation: `Total cooldown: 30--120 minutes depending on chamber mass and batch size` -- Inter Medium 13 pt `#F0EDE8`

**Key callout (Y: 11.5" to 13.5"):**
- Rounded rect, full width, fill `#E05C5C` at 15%, border 1 pt `#E05C5C`
- Text: `NEVER open the chamber while parts are above 80 C. Exposing hot DLC to atmosphere can cause oxidation of the interlayer through coating pinholes, leading to delayed delamination days or weeks after coating.` -- Inter Medium, 14 pt, `#E05C5C`

---

### ZONE 3 -- Stress & Thermal Shock

**Section label:** `WHY DLC HATES THERMAL SHOCK` -- Y: 14.2".

**BLOCK D -- Stress Explanation**

Y: 14.8" to 19.8". Three cards in a row.

| Card | X | W | Title | Accent | Content |
|---|---|---|---|---|---|
| 1 | 0.5" | 7.33" | INTRINSIC STRESS | `#E8A020` | DLC is deposited under high compressive stress: 1--3 GPa for a-C:H, 5--12 GPa for ta-C. This stress is inherent to the sp3 bonding structure. It is always present, even at room temperature. |
| 2 | 8.16" | 7.33" | THERMAL STRESS | `#E05C5C` | When temperature changes, the coating and substrate expand/contract at different rates (CTE mismatch). Rapid cooling adds tensile thermal stress on TOP of the compressive intrinsic stress. The combination can exceed the adhesion strength of the interlayer. |
| 3 | 15.83" | 7.33" | THE RESULT | `#27AE60` | Slow cooling allows thermal stress to develop gradually. The interlayer absorbs the differential strain. Fast cooling = stress spike = cracking, buckling, or delamination at the interlayer interface. |

Each card: Rounded rect, H: 4.8", fill `#1E2435`, radius 6, left accent 0.06".
Title: Barlow SemiBold, 18 pt, accent color.
Content: Inter Regular, 14 pt, `#F0EDE8`.

---

### ZONE 4 -- Venting Protocol

**Section label:** `CHAMBER VENTING -- STEP BY STEP` -- Y: 20.2".

**BLOCK E -- Protocol Table**

Y: 20.8" to 26.3".

| Step | Action | Condition / Setpoint | Why |
|---|---|---|---|
| 1 | Extinguish plasma / arc | Power supplies to standby | End deposition; stop energy input |
| 2 | Stop gas flow | Close all MFCs | Prevent continued film growth |
| 3 | Remove substrate bias | Bias supply off | Eliminate ion bombardment |
| 4 | Hold under vacuum | Chamber pressure < 10^-4 Torr | Radiative cooling; no oxidation risk |
| 5 | Monitor substrate temperature | Thermocouple or pyrometer readout | Wait until < 80 C before backfill |
| 6 | Backfill with inert gas | Ar or N2 to 1--100 Torr slowly | Accelerate cooling; inert atmosphere prevents oxidation |
| 7 | Continue monitoring temp | Wait until < 50 C | Ensure parts safe to handle |
| 8 | Vent to atmosphere | Open filtered vent valve | Equalize pressure; prepare to open door |
| 9 | Open chamber door | Verify pressure equalized | Avoid pressure differential damage |
| 10 | Unload with gloves | Clean nitrile or lint-free gloves | Fingerprints on fresh DLC degrade surface |

Header row: fill `#3A4055`, H: 0.5". Barlow SemiBold, 13 pt, `#F0EDE8`.
Data rows: alternating `#1E2435` / `#252B3D`, H: 0.5".
Step: JetBrains Mono 12 pt `#E8A020`.
Action: Inter Medium 13 pt `#F0EDE8`.
Condition: JetBrains Mono 12 pt `#2EC4B6`.
Why: Inter Regular 12 pt `#F0EDE8` at 70%.

---

### ZONE 5 -- Cooling Defects

**Section label:** `WHAT GOES WRONG IF YOU RUSH` -- Y: 26.7".

**BLOCK F -- 4 Defect Cards**

Y: 27.3" to 32.3". Four cards in a row.

| Card | X | W | Defect | Accent | Cause | Prevention |
|---|---|---|---|---|---|---|
| 1 | 0.5" | 5.5" | EDGE CRACKING | `#E05C5C` | Thermal stress concentration at sharp edges during rapid cool | Round all edges before coating; slow cooldown rate |
| 2 | 6.33" | 5.5" | BUCKLING / SPALLING | `#E05C5C` | Combined intrinsic + thermal stress exceeds adhesion | Proper interlayer; limit ta-C thickness to < 2 um; slow cool |
| 3 | 12.16" | 5.5" | DELAYED DELAMINATION | `#E8A020` | Interlayer oxidized through pinholes during hot vent | Never vent above 80 C; use inert backfill gas |
| 4 | 18.0" | 5.5" | SUBSTRATE SOFTENING | `#E8A020` | Parts held at high temp too long (hardened steel > 200 C for extended time) | Monitor temp; use cooling pauses during deposition if needed |

Each card: Rounded rect, H: 4.8", fill `#1E2435`, radius 6, left accent 0.06".
Defect: Barlow SemiBold, 16 pt, `#E05C5C`.
Cause: Inter Regular, 13 pt, `#F0EDE8`.
Prevention: Inter Medium, 13 pt, `#27AE60`.

---

### ZONE 6 -- Footer

Standard. Title: `Cooling -- DLC`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cooling DLC -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Cooling is the unsung hero of DLC quality. Most operators focus on the deposition itself and treat cooldown as "just waiting." This poster must change that mindset. The timeline hero makes the cooldown sequence tangible and visual. The stress explanation (Zone 3) provides the physics that justify the patience. The "never open above 80 C" callout is the single most important operational rule on this poster -- it should hit hard in Coral red. Pair this poster with Poster 446 (Deposition) on the same wall.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #447 -- Construction Workup v1.0*
*2026-04-26*
