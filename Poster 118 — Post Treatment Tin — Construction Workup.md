---
Project: Plating Posters Inc
Poster Number: 118
Title: "Post Treatment -- Tin"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Process Scope: Post-treatment for acid tin plating (Stages 7--8 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - TinPlating
  - PostTreatment
  - ConstructionWorkup
  - Series2
  - ClusterEP11
---

# Poster #118 -- Construction Workup
## Post Treatment -- Tin

*Alaina -- Plating Posters Inc*
*v1.0 -- 2026-04-26*

Stages 7--8 of 8. Post-treatment for tin plating covers two critical operations: anti-tarnish treatment (preserves solderability) and reflow (melts the tin deposit, eliminating porosity and -- critically -- mitigating tin whisker growth). This poster has the most consequential content in the cluster because tin whiskers are a billion-dollar reliability problem in electronics. Pure tin on copper grows conductive whiskers that short-circuit components over months to years. This poster explains the problem and every known mitigation.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Post-treatment sequence hero (Block B):** Two-stage flow: anti-tarnish dip followed by reflow/dry, with a branching decision (reflow vs. air dry) based on application.
2. **Tin whisker deep-dive panel (Block D):** The centerpiece -- what whiskers are, why they grow, and every mitigation strategy.
3. **Anti-tarnish chemistry callout (Block E):** What the dip does and why it matters for shelf life.
4. **Reflow parameters and methods (Block F):** Hot air leveling, IR reflow, and oven reflow.

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
  Stages 7--8 highlighted (Amber)
ZONE 3 -- POST-TREATMENT SEQUENCE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- TIN WHISKERS -- THE #1 RELIABILITY RISK (14.5"--22.0" / ~7.5")
ZONE 5 -- ANTI-TARNISH + REFLOW PARAMETERS (22.0"--28.5" / ~6.5")
ZONE 6 -- APPLICATION DECISION MATRIX (28.5"--32.5" / ~4.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `POST TREATMENT` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Tin Plating -- Stages 7--8 of 8` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Anti-tarnish preserves the surface. Reflow kills the whiskers. Skip either one and the tin will fail you -- maybe not today, but eventually.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stages 7 and 8 both highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Freshly plated, rinsed tin surface  -->  After: Protected, reflowed (or dried) finished part`

---

### ZONE 3 -- Post-Treatment Sequence Hero

**Section label:** `THE FINAL TWO STAGES` -- Y: 4.4".

**BLOCK B -- Two-Stage Sequence with Decision Branch**

Y: 5.0" to 14.0".

**Stage 7 -- Anti-Tarnish (left half):**
- Large rounded rect, X: 0.5", Y: 5.0", W: 11.0", H: 8.5", fill `#1E2435`, top accent 4 pt `#E8A020`
- Badge: `STAGE 7` fill `#E8A020`, text `#1A1F2E`
- Title: `Anti-Tarnish Dip` Barlow SemiBold 22 pt `#F0EDE8`

Parameters:
- `Type: Proprietary anti-tarnish / anti-oxidant dip` JetBrains Mono 13 pt `#F0EDE8`
- `Temperature: Ambient` JetBrains Mono 13 pt `#F0EDE8`
- `Time: 15--30 sec immersion` JetBrains Mono 13 pt `#F0EDE8`
- `pH: Per supplier TDS` JetBrains Mono 13 pt `#F0EDE8`

Purpose block:
- `Deposits a thin organic or chromate-free protective film on the tin surface`
- `Prevents tarnishing and oxidation during storage`
- `Preserves solderability for weeks to months`
- `Required for all electronics and connector applications`

Note: `Without anti-tarnish, tin tarnishes within hours in humid environments. Solderability degrades rapidly.` Inter Medium 13 pt `#E8A020`

**Arrow from Stage 7 to Decision:**
- Right-pointing, 3 pt `#3A4055`

**Decision diamond (center):**
- Diamond shape (rotated square), X: 11.75", Y: 8.0", W: 1.5", H: 1.5", fill `#E8A020` at 30%, border 2 pt `#E8A020`
- Text: `REFLOW?` Barlow SemiBold 14 pt `#E8A020`

**Stage 8A -- Reflow (upper-right):**
- Rounded rect, X: 13.5", Y: 5.0", W: 10.0", H: 3.8", fill `#1E2435`, top accent 4 pt `#E05C5C`
- Badge: `STAGE 8A` fill `#E05C5C`, text `#F0EDE8`
- Title: `Reflow (Fuse)` Barlow SemiBold 20 pt `#F0EDE8`
- `450--500 F (232--260 C)` JetBrains Mono 14 pt `#E05C5C`
- `Hot air, IR, or oven`
- `Melts tin -- eliminates porosity`
- `PRIMARY TIN WHISKER MITIGATION` Barlow SemiBold 13 pt `#E05C5C`

**Stage 8B -- Air Dry (lower-right):**
- Rounded rect, X: 13.5", Y: 9.5", W: 10.0", H: 3.8", fill `#1E2435`, top accent 4 pt `#2EC4B6`
- Badge: `STAGE 8B` fill `#2EC4B6`, text `#1A1F2E`
- Title: `Air Dry` Barlow SemiBold 20 pt `#F0EDE8`
- `Forced warm air or ambient`
- `No melting -- deposit remains as-plated`
- `Acceptable for non-critical applications`
- `DOES NOT mitigate whisker risk` Inter Medium 13 pt `#E05C5C`

Arrows from diamond: upward-right to 8A, downward-right to 8B.
Labels on arrows: `YES -- electronics, connectors` (to 8A), `NO -- decorative, food-contact` (to 8B).

---

### ZONE 4 -- Tin Whiskers

**Section label:** `TIN WHISKERS -- THE #1 RELIABILITY RISK IN PURE TIN` -- Y: 14.7".

**BLOCK D -- Tin Whisker Deep Dive (Y: 15.3" to 21.5")**

Full-width panel, fill `#1E2435`, left accent `#E05C5C`, radius 8.

**Title bar:**
- `WHAT ARE TIN WHISKERS?` Barlow Condensed ExtraBold 24 pt `#E05C5C`

**Three-column content layout:**

**Column 1 -- The Problem:**
- Header: `THE THREAT` Barlow SemiBold 16 pt `#E05C5C`
- `Conductive crystalline filaments that grow from pure tin surfaces`
- `Length: up to several millimeters`
- `Growth: spontaneous, over weeks to years`
- `Cause: compressive stress in the tin deposit (from copper-tin intermetallic growth)`
- `Result: short circuits, arcing, equipment failure`
- `Documented failures: satellites, medical devices, nuclear systems, automotive`

**Column 2 -- Risk Factors:**
- Header: `WHEN IT HAPPENS` Barlow SemiBold 16 pt `#E8A020`
- `Pure tin (>99% Sn) on copper or copper alloy substrate`
- `No barrier layer between tin and copper`
- `Thin deposit (< 2 microns highest risk)`
- `Elevated temperature cycling`
- `High humidity environments`
- `Mechanical stress (bent leads, press-fit connectors)`

**Column 3 -- Mitigations:**
- Header: `HOW TO PREVENT IT` Barlow SemiBold 16 pt `#27AE60`
- `1. REFLOW -- melt and resolidify tin (best single mitigation)`
- `2. Nickel barrier underplate (1--3 microns Ni between Cu and Sn)`
- `3. Alloy with 1--3% bismuth (Bi) or silver (Ag)`
- `4. Anneal at 150 C (302 F) for 1 hour`
- `5. Minimum deposit thickness > 8 microns`
- `6. Conformal coat over tin (reduces but does not eliminate)`

**Bottom warning banner:**
- Full-width, fill `#E05C5C` at 15%, border 1 pt `#E05C5C`
- Text: `RoHS eliminated tin-lead. Pure tin replaced it. Tin whiskers are the trade-off. Every tin plater must understand this.` Inter Medium 14 pt `#E05C5C`

---

### ZONE 5 -- Anti-Tarnish + Reflow Parameters

**Section label:** `PROCESS PARAMETERS` -- Y: 22.2".

**Two-column layout (Y: 22.8" to 28.3"):**

**Left -- Anti-Tarnish Detail:**
- Rounded rect, X: 0.5", W: 11.0", H: 5.3", fill `#1E2435`, left accent `#E8A020`
- Title: `ANTI-TARNISH` Barlow SemiBold 18 pt `#E8A020`

| Parameter | Value |
|---|---|
| Type | Proprietary organic anti-tarnish |
| Temperature | Ambient |
| Time | 15--30 sec |
| Rinse after | Optional -- per supplier |
| Shelf life added | 2--12 weeks (humidity dependent) |
| RoHS note | Chromate-free anti-tarnish for RoHS compliance |

Note: `Anti-tarnish is NOT a substitute for reflow in whisker-critical applications.` Inter Medium 12 pt `#E05C5C`

**Right -- Reflow Methods:**
- Rounded rect, X: 12.0", W: 11.5", H: 5.3", fill `#1E2435`, left accent `#E05C5C`
- Title: `REFLOW METHODS` Barlow SemiBold 18 pt `#E05C5C`

| Method | Temp | Time | Application |
|---|---|---|---|
| Hot air leveling (HASL) | 450--500 F | Seconds | PCB, connector strip |
| IR reflow oven | 450--500 F | 30--90 sec | Component leads |
| Convection oven | 450--500 F | 1--3 min | Bulk parts |
| Hot oil (legacy) | 450--500 F | 5--15 sec | Rarely used today |

Note: `Reflow temperature must exceed 449 F (232 C) -- the melting point of tin. Below that, nothing happens.` Inter Medium 12 pt `#E8A020`

---

### ZONE 6 -- Application Decision Matrix

**Section label:** `WHICH POST-TREATMENT FOR YOUR APPLICATION?` -- Y: 28.7".

**BLOCK G -- Decision Matrix (4 columns)**

Y: 29.4" to 32.3".

| Application | Anti-Tarnish | Reflow | Ni Underplate |
|---|---|---|---|
| Electronics (solder) | REQUIRED | REQUIRED | RECOMMENDED |
| Connectors (contact) | REQUIRED | REQUIRED | REQUIRED |
| Food contact / can lining | OPTIONAL | NOT NEEDED | NOT NEEDED |
| Decorative | OPTIONAL | NOT NEEDED | NOT NEEDED |
| Corrosion protection (steel) | RECOMMENDED | OPTIONAL | OPTIONAL |

Header: `#3A4055`. Values color-coded: REQUIRED = `#E05C5C`, RECOMMENDED = `#E8A020`, OPTIONAL = `#2EC4B6`, NOT NEEDED = `#F0EDE8` at 50%.

---

### ZONE 7 -- Footer

Standard. Title: `Post Treatment -- Tin`. Version `v1.0 -- 2026`.

Disclaimer: `Tin whisker information reflects current industry understanding as of 2026. Mitigation strategies continue to evolve. Consult iNEMI and JEDEC standards for latest whisker test requirements.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Post Treatment Tin -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the most consequential poster in the EP-11 cluster. Tin whiskers have caused satellite failures, pacemaker recalls, and nuclear plant incidents. The three-column whisker deep-dive is the visual centerpiece and the reason this poster exists. The decision branch (reflow vs. air dry) in the hero visual makes the application-dependent nature of post-treatment immediately clear. The application decision matrix in Zone 6 is the quick-reference takeaway -- a supervisor can check it in 5 seconds and know what is required for their parts.

---

*Alaina -- Plating Posters Inc*
*Poster #118 -- Construction Workup v1.0*
*2026-04-26*
