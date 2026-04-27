---
Project: Plating Posters Inc
Poster Number: 601
Title: "Cooling -- Plasma Nitriding"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 5)"
Process Scope: Cooling and post-cycle shutdown for plasma nitriding -- no quench required
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - PlasmaNitriding
  - Cooling
  - ConstructionWorkup
  - DiffusionHeatTreatment
---

# Poster #601 -- Construction Workup
## Cooling -- Plasma Nitriding

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

The cooling stage in plasma nitriding is beautifully simple compared to carburizing or induction hardening: there is no quench. Hardness comes from precipitation, not martensite. Parts cool slowly in the vacuum chamber under protective atmosphere. This poster drives home why that matters -- zero quench distortion, zero quench cracking risk, and minimal dimensional change.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cooling profile hero (Block B):** Time-temperature curve showing slow cool-down from nitriding temp to safe unloading temp.
2. **"No Quench" comparison callout (Block D):** Side-by-side showing plasma nitriding vs. carburizing cooling.
3. **Dimensional change data (Block E).**
4. **Shutdown procedure checklist (Block F).**

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- COOLING PROFILE HERO (2.9"--15.5")
ZONE 3 -- NO QUENCH COMPARISON (15.5"--22.0")
ZONE 4 -- DIMENSIONAL CHANGE + SHUTDOWN (22.0"--32.5")
ZONE 5 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `COOLING` -- 88 pt `#F0EDE8`.
**Subheading:** `Plasma Nitriding -- No Quench. No Cracking. No Distortion.` -- 32 pt `#2EC4B6` (Teal).
**Tagline:** `The hardness is already locked in by precipitation. All you need now is a controlled cool-down.` -- 20 pt `#F0EDE8` at 65%.

**Rule card (right):**
- Big number: `0` -- 72 pt `#27AE60`
- Label: `Quench cracking risk -- zero, because there is no quench` -- 14 pt `#F0EDE8`

---

### ZONE 2 -- Cooling Profile (HERO)

**Section label:** `COOLING PROFILE -- SLOW AND CONTROLLED` -- Y: 3.1".

**BLOCK B -- Time-Temperature Curve (Y: 3.8" to 15.3")**

Simplified graph area:

**Axes:**
- Y-axis (left): Temperature, 0--1100 F, labeled at 200 F intervals. JetBrains Mono 12 pt `#F0EDE8` at 60%.
- X-axis (bottom): Time (hours), 0--8 hr. JetBrains Mono 12 pt `#F0EDE8` at 60%.
- Axis lines: 2 pt `#3A4055`

**Curve:**
- Starts at ~970 F (nitriding temperature), Y: ~5.5"
- Gradual descent (convex curve) to ~300 F at ~4--6 hours, then flatten
- Curve: 3 pt stroke `#2EC4B6`

**Zone annotations along curve:**

| Time Range | Annotation | Color |
|---|---|---|
| 0--0.5 hr | DC power off; plasma extinguished | `#E8A020` |
| 0--1 hr | Cool under N2 or N2/H2 protective atmosphere | `#2EC4B6` |
| 1--4 hr | Slow radiative + convective cooling in vacuum | `#2EC4B6` |
| 4--6 hr | Below 300 F -- safe to backfill to atmospheric | `#27AE60` |
| 6+ hr | Open door; unload parts with heat-resistant gloves | `#27AE60` |

Annotations: callout lines from curve to text boxes (rounded rect, fill `#1E2435`, H: 0.8").

**Key callout (centered, Y: 14.0"):**
- Rounded rect, W: 18.0", H: 1.0", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- Text: `COOLING RATE: 1--4 F per minute -- no forced cooling needed. The vacuum vessel is the insulator.` Inter Medium 14 pt `#27AE60`

---

### ZONE 3 -- No Quench Comparison

**Section label:** `WHY NO QUENCH? -- THE FUNDAMENTAL DIFFERENCE` -- Y: 15.7".

**BLOCK D -- Two-Panel Comparison (Y: 16.3" to 21.8")**

**Left -- Plasma Nitriding (Emerald):**
- Rounded rect, X: 0.5", W: 11.0", H: 5.3", fill `#1E2435`, left accent `#27AE60`
- Title: `PLASMA NITRIDING` Barlow SemiBold 20 pt `#27AE60`
- `Hardness source: Nitride PRECIPITATION in ferrite`
- `Phase: Ferrite throughout -- no austenite formed`
- `Cooling: Slow cool in furnace (hours)`
- `Quench: NONE`
- `Distortion: Near zero`
- `Cracking risk: ZERO`
- `Dimensional change: 0.0001--0.0005 inch/surface`
- Badge: `PRECIPITATION HARDENING` JetBrains Mono 12 pt `#27AE60`

**Right -- Carburizing (for comparison) (Amber):**
- Rounded rect, X: 12.0", W: 11.5", H: 5.3", fill `#1E2435`, left accent `#E8A020`
- Title: `CARBURIZING (for comparison)` Barlow SemiBold 20 pt `#E8A020`
- `Hardness source: MARTENSITE formation (phase transformation)`
- `Phase: Austenite -> Martensite on quench`
- `Cooling: Rapid quench in oil or gas (seconds)`
- `Quench: REQUIRED -- the whole point`
- `Distortion: Significant (requires grinding allowance)`
- `Cracking risk: Real -- quench cracks are a reject condition`
- `Dimensional change: Variable; requires post-grind`
- Badge: `TRANSFORMATION HARDENING` JetBrains Mono 12 pt `#E8A020`

---

### ZONE 4 -- Dimensional Change + Shutdown

**Two-column layout (Y: 22.2" to 32.3")**

**Left -- BLOCK E: Dimensional Change Data (X: 0.5", W: 11.0")**

Section label: `DIMENSIONAL CHANGE` -- Barlow Condensed ExtraBold 22 pt.

Callout box, H: 9.5", fill `#1E2435`, left accent `#27AE60`:

- `Typical growth: 0.0001--0.0005 inch per surface` JetBrains Mono 16 pt `#27AE60`
- `Growth is from nitrogen absorption -- lattice expansion` Inter Regular 14 pt `#F0EDE8`
- `Predictable and consistent for a given process` Inter Regular 14 pt `#F0EDE8`
- `Parts CAN be finish-machined before nitriding` Inter Medium 14 pt `#27AE60`
- `This is a major advantage for precision components:` Inter Regular 14 pt `#F0EDE8`
  - `Gears, shafts, valve components, die/mold surfaces`
  - `No post-nitriding grinding required in most cases`
  - `Surface finish essentially unchanged`

Bottom note:
- `Compare to carburizing: requires 0.005--0.015 inch grinding stock per surface` Inter Regular 13 pt `#E8A020`

**Right -- BLOCK F: Shutdown Procedure (X: 12.0", W: 11.5")**

Section label: `SHUTDOWN PROCEDURE` -- Barlow Condensed ExtraBold 22 pt.

Numbered checklist:

| Step | Action | Note |
|---|---|---|
| 1 | De-energize DC power supply | Plasma extinguished; parts still at nitriding temp |
| 2 | Maintain protective atmosphere (N2 or N2/H2) | Prevents oxidation during cool-down |
| 3 | Monitor temperature via thermocouples | Record cool-down rate; verify uniformity |
| 4 | Below 300 F: safe to backfill chamber to atmospheric pressure | Do NOT open at higher temp -- oxidation risk |
| 5 | Backfill with nitrogen to atmospheric | Slow bleed; equalize pressure |
| 6 | Open door | Parts may still be warm; use heat-resistant gloves |
| 7 | Unload parts | Inspect for any visible anomalies (discoloration, staining) |
| 8 | Transfer to inspection | Microhardness, white layer check per spec |

Each row: H: 1.1", alternating fills. Step number: `#E8A020`.

---

### ZONE 5 -- Footer

Standard footer. Title: `Cooling -- Plasma Nitriding`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 5 zones. **Light Remap:** Standard table. **Export:** Six files.

---

*Alaina -- Poster #601 -- Construction Workup v1.0 -- 2026-04-26*
