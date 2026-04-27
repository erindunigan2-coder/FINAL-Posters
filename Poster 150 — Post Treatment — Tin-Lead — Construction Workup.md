---
Project: Plating Posters Inc
Poster Number: 150
Title: "Post Treatment -- Tin-Lead"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Process Scope: Post-treatment for tin-lead plating (Stages 7--8 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - TinLeadPlating
  - PostTreatment
  - ConstructionWorkup
  - Series2
  - ClusterEP15
---

# Poster #150 -- Construction Workup
## Post Treatment -- Tin-Lead

*Alaina -- Plating Posters Inc*
*v1.0 -- 2026-04-26*

Stages 7--8 of 8. Post-treatment for tin-lead plating covers two operations: hot water rinse / dry (Stage 7) and reflow / inspection (Stage 8). Reflow is the defining post-treatment step for solder plate -- it melts the tin-lead coating at 400--450 F, producing a bright, dense, fully fused solder surface. Unlike pure tin, where reflow is primarily a whisker mitigation, tin-lead reflow is about solderability performance. The fused solder surface is dramatically better for wetting and joint formation. This poster also covers the critical inspection step: alloy verification by XRF and solderability testing. And a note that no chromate post-treatment is needed -- the tin-lead alloy is inherently solderable and corrosion-resistant in electronics environments.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Post-treatment sequence hero (Block B):** Two-stage flow: hot rinse/dry followed by reflow/inspect, with reflow method options (IR, hot air, oven) shown as sub-branches.
2. **Reflow parameters and methods (Block D):** The centerpiece -- what reflow does and every method available.
3. **Solderability and inspection callout (Block E):** XRF alloy verification, solderability testing (dip-and-look, wetting balance), and applicable specifications.
4. **Application decision matrix (Block F):** Which post-treatment for which application.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stages 7--8 highlighted (Amber)
ZONE 3 -- POST-TREATMENT SEQUENCE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- REFLOW -- THE DEFINING STEP (14.5"--22.0" / ~7.5")
ZONE 5 -- INSPECTION + SOLDERABILITY TESTING (22.0"--28.5" / ~6.5")
ZONE 6 -- APPLICATION DECISION MATRIX (28.5"--32.5" / ~4.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `POST TREATMENT` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Tin-Lead Plating -- Stages 7--8 of 8` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Hot rinse dries the surface. Reflow fuses the solder. Inspection proves the alloy. No chromate needed -- this deposit is born solderable.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stages 7 and 8 both highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Freshly plated, rinsed solder surface  -->  After: Fused, inspected, solderable finished part`

---

### ZONE 3 -- Post-Treatment Sequence Hero

**Section label:** `THE FINAL TWO STAGES` -- Y: 4.4".

**BLOCK B -- Two-Stage Sequence with Reflow Method Branches**

Y: 5.0" to 14.0".

**Stage 7 -- Hot Water Rinse / Dry (left half):**
- Large rounded rect, X: 0.5", Y: 5.0", W: 11.0", H: 8.5", fill `#1E2435`, top accent 4 pt `#E8A020`
- Badge: `STAGE 7` fill `#E8A020`, text `#1A1F2E`
- Title: `Hot Water Rinse / Dry` Barlow SemiBold 22 pt `#F0EDE8`

Parameters:
- `Hot DI water: 140--160 F (60--71 C)` JetBrains Mono 13 pt `#F0EDE8`
- `Time: 1--3 min immersion` JetBrains Mono 13 pt `#F0EDE8`
- `Or: forced warm air dry` JetBrains Mono 13 pt `#F0EDE8`

Purpose block:
- `Removes residual rinse water quickly`
- `Hot water accelerates drying -- prevents water spots`
- `DI water prevents mineral deposits on solder surface`
- `Prepares surface for reflow or direct use`

Note: `Hot water rinse is faster and cleaner than ambient air dry. Water spots on solder impair solderability.` Inter Medium 13 pt `#E8A020`

**Arrow from Stage 7 to Stage 8:**
- Right-pointing, 3 pt `#3A4055`

**Stage 8 -- Reflow / Inspect (right half, with three sub-branches):**
- Large rounded rect, X: 12.5", Y: 5.0", W: 11.0", H: 8.5", fill `#1E2435`, top accent 4 pt `#E05C5C`
- Badge: `STAGE 8` fill `#E05C5C`, text `#F0EDE8`
- Title: `Reflow / Inspect` Barlow SemiBold 22 pt `#F0EDE8`

Three reflow method sub-boxes inside (stacked vertically):

Sub-box A -- `Infrared (IR) Reflow`:
- Rounded rect, fill `#252B3D`, H: 1.8"
- `400--450 F (204--232 C)` JetBrains Mono 12 pt `#E05C5C`
- `2--5 sec exposure`
- `Best for: component leads, connector strips`

Sub-box B -- `Hot Air Leveling`:
- Rounded rect, fill `#252B3D`, H: 1.8"
- `400--450 F (204--232 C)` JetBrains Mono 12 pt `#E05C5C`
- `Seconds -- continuous pass`
- `Best for: PCB surface finish`

Sub-box C -- `Convection Oven`:
- Rounded rect, fill `#252B3D`, H: 1.8"
- `400--450 F (204--232 C)` JetBrains Mono 12 pt `#E05C5C`
- `30--90 sec in oven`
- `Best for: bulk parts, discrete components`

**Inspection callout (below sub-boxes, inside Stage 8 rect):**
- `INSPECT: XRF alloy verification + solderability test` Barlow SemiBold 13 pt `#E8A020`
- `ASTM B579 | SAE AS5272 | IPC J-STD-001` JetBrains Mono 11 pt `#F0EDE8` at 60%

---

### ZONE 4 -- Reflow -- The Defining Step

**Section label:** `REFLOW -- WHAT IT DOES AND WHY IT MATTERS` -- Y: 14.7".

**BLOCK D -- Reflow Deep Dive (Y: 15.3" to 21.5")**

Full-width panel, fill `#1E2435`, left accent `#E05C5C`, radius 8.

**Title bar:**
- `SOLDER REFLOW TRANSFORMS THE DEPOSIT` Barlow Condensed ExtraBold 24 pt `#E05C5C`

**Three-column content layout:**

**Column 1 -- Before Reflow:**
- Header: `AS-PLATED` Barlow SemiBold 16 pt `#E8A020`
- `Matte, porous, granular microstructure`
- `Porosity allows moisture ingress`
- `Surface may tarnish quickly`
- `Adequate but not optimal solderability`
- `Grain boundaries visible under microscope`

**Column 2 -- During Reflow:**
- Header: `THE MELT` Barlow SemiBold 16 pt `#E05C5C`
- `Temperature exceeds Sn-Pb melting point`
- `60/40 eutectic: 361 F (183 C) melting point`
- `90/10: higher liquidus (~455 F / 235 C)`
- `Reflow temp: 400--450 F (204--232 C)`
- `Duration: 2--5 seconds (IR/hot air) or 30--90 sec (oven)`
- `Entire deposit liquefies and resolidifies`

**Column 3 -- After Reflow:**
- Header: `FUSED SOLDER` Barlow SemiBold 16 pt `#27AE60`
- `Bright, smooth, dense surface`
- `Porosity eliminated -- sealed deposit`
- `Superior solderability and wetting`
- `Improved corrosion resistance`
- `Extended shelf life before assembly`
- `The finish that made PCBs reliable for decades`

**Bottom note:**
- `The 60/40 eutectic alloy melts at 361 F (183 C) -- the lowest melting point of any Sn-Pb composition. This is why 60/40 became the standard solder alloy.` Inter Medium 14 pt `#E8A020`

---

### ZONE 5 -- Inspection + Solderability Testing

**Section label:** `INSPECTION -- PROVE THE DEPOSIT` -- Y: 22.2".

**Two-column layout (Y: 22.8" to 28.3"):**

**Left -- Alloy Verification:**
- Rounded rect, X: 0.5", W: 11.0", H: 5.3", fill `#1E2435`, left accent `#E8A020`
- Title: `ALLOY VERIFICATION` Barlow SemiBold 18 pt `#E8A020`

| Test | Method | Frequency |
|---|---|---|
| Alloy composition | XRF (non-destructive) | Every lot |
| Thickness | XRF or beta backscatter | Every lot |
| Adhesion | Tape test or bend test | Per specification |
| Visual | 10x magnification | Every rack/reel |

Note: `XRF is the workhorse. 30 seconds per measurement. No sample prep. Measures Sn, Pb, and thickness simultaneously on most instruments.` Inter Medium 12 pt `#27AE60`

**Right -- Solderability Testing:**
- Rounded rect, X: 12.0", W: 11.5", H: 5.3", fill `#1E2435`, left accent `#27AE60`
- Title: `SOLDERABILITY TESTING` Barlow SemiBold 18 pt `#27AE60`

| Test | Standard | Description |
|---|---|---|
| Dip-and-look | IPC J-STD-002 | Dip sample in molten solder, inspect wetting visually |
| Wetting balance | IPC J-STD-002 | Measures wetting force vs. time -- quantitative |
| Steam aging | IPC J-STD-002 | 8 hrs steam exposure, then dip-and-look -- simulates shelf life |
| Solderability after reflow | Application-specific | Verify reflow did not degrade wetting |

Note: `Solderability is the entire reason this plating exists. If the deposit does not wet properly, the plating is worthless regardless of thickness or alloy.` Inter Medium 12 pt `#E05C5C`

---

### ZONE 6 -- Application Decision Matrix

**Section label:** `WHICH POST-TREATMENT FOR YOUR APPLICATION?` -- Y: 28.7".

**BLOCK G -- Decision Matrix (4 columns)**

Y: 29.4" to 32.3".

| Application | Hot Rinse/Dry | Reflow | XRF Alloy Check |
|---|---|---|---|
| PCB surface finish (HASL) | REQUIRED | REQUIRED (hot air leveling) | REQUIRED |
| Connector pins (mil/aero) | REQUIRED | REQUIRED (IR or oven) | REQUIRED |
| Component leads | RECOMMENDED | REQUIRED | REQUIRED |
| Wire/cable solder coat | OPTIONAL | RECOMMENDED | RECOMMENDED |
| Rework / touch-up | OPTIONAL | OPTIONAL | RECOMMENDED |

Header: `#3A4055`. Values color-coded: REQUIRED = `#E05C5C`, RECOMMENDED = `#E8A020`, OPTIONAL = `#2EC4B6`.

**Note below matrix:**
- `No chromate conversion coating needed. Tin-lead alloy is inherently solderable and corrosion-resistant for electronics environments. Anti-tarnish dip is also typically unnecessary for reflowed solder.` Inter Medium 13 pt `#27AE60`

---

### ZONE 7 -- Footer

Standard. Title: `Post Treatment -- Tin-Lead`. Version `v1.0 -- 2026`.

Disclaimer: `Lead is restricted under EU RoHS (Directive 2011/65/EU). Tin-lead solder plating is permitted under exemptions for military, aerospace, and high-reliability applications. Applicable specifications: ASTM B579, SAE AS5272, IPC J-STD-001. Consult your quality and compliance teams.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Post Treatment Tin-Lead -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster differs from the pure tin post-treatment poster (#118) in several important ways. First, there is no tin whisker deep-dive -- tin-lead alloys with >3% Pb are inherently resistant to whisker growth, so the issue does not apply. Second, the reflow deep-dive focuses on solderability improvement rather than whisker mitigation -- that is the functional reason for reflowing solder. Third, the "no chromate needed" note is unique to tin-lead -- the alloy provides its own corrosion protection in electronics environments. The 60/40 eutectic melting point (361 F / 183 C) is a foundational fact of soldering that belongs on this poster -- it is the reason 60/40 became the standard. The inspection zone gives solderability testing equal weight to alloy verification because solderability IS the product.

---

*Alaina -- Plating Posters Inc*
*Poster #150 -- Construction Workup v1.0*
*2026-04-26*
