---
Project: Plating Posters Inc
Poster Number: 150
Title: "Post Treatment -- Tin-Lead"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-28T00:00:00
Source: Poster 150 -- Post Treatment -- Tin-Lead -- Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - TinLeadPlating
  - PostTreatment
  - ClusterEP15
  - v1
---

# Claude Chat Generation Prompt -- Poster #150
## Post Treatment -- Tin-Lead
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-28).*

---

> **IMPORTANT:** Generate as SVG or HTML visual artifact. 24 x 36" portrait. Dark edition first.

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E`, locked palette, 0.5" safe zone.

---

## Phase 2 -- Header

### Step 1 -- `POST TREATMENT` -- `80` pt `#F0EDE8`. Y: **0.5"**.
### Step 2 -- `Tin-Lead Plating -- Stages 7--8 of 8` -- `32` pt `#E8A020`. Y: **1.4"**.
### Step 3 -- `Hot rinse dries the surface. Reflow fuses the solder. Inspection proves the alloy. No chromate needed -- this deposit is born solderable.` -- `20` pt at 65%. Y: **2.1"**.

---

## Phase 3 -- Orientation Strip

Stages 7 AND 8 both highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Freshly plated, rinsed solder surface  -->  After: Fused, inspected, solderable finished part`

---

## Phase 4 -- Post-Treatment Sequence Hero

Y: 4.2" to 14.5". Section: `THE FINAL TWO STAGES`.

Two large side-by-side panels:

**Left -- Stage 7: Hot Water Rinse / Dry (X: 0.5", W: 11.0", H: 8.5"):**
- Fill `#1E2435`, top accent 4 pt `#E8A020`
- Badge: `STAGE 7` fill `#E8A020`
- Title: `Hot Water Rinse / Dry`
- Params: `Hot DI water: 140--160 F (60--71 C)` / `Time: 1--3 min immersion` / `Or: forced warm air dry`
- Purpose: removes rinse water, prevents water spots, DI prevents mineral deposits
- Note: `Hot water rinse is faster and cleaner than ambient air dry.` `#E8A020`

Arrow from Stage 7 to Stage 8: 3 pt `#3A4055`.

**Right -- Stage 8: Reflow / Inspect (X: 12.5", W: 11.0", H: 8.5"):**
- Fill `#1E2435`, top accent 4 pt `#E05C5C`
- Badge: `STAGE 8` fill `#E05C5C`, text `#F0EDE8`
- Title: `Reflow / Inspect`

Three reflow method sub-boxes stacked (fill `#252B3D`):
1. `Infrared (IR) Reflow` -- `400--450 F (204--232 C)` / `2--5 sec` / `Best for: component leads, connector strips`
2. `Hot Air Leveling` -- `400--450 F` / `Seconds -- continuous pass` / `Best for: PCB surface finish`
3. `Convection Oven` -- `400--450 F` / `30--90 sec in oven` / `Best for: bulk parts, discrete components`

Inspection callout: `INSPECT: XRF alloy verification + solderability test` `#E8A020` / `ASTM B579 | SAE AS5272 | IPC J-STD-001`

---

## Phase 5 -- Reflow Deep Dive

Y: 14.5" to 22.0". Section: `REFLOW -- WHAT IT DOES AND WHY IT MATTERS`.

Full-width panel, fill `#1E2435`, left accent `#E05C5C`. Title: `SOLDER REFLOW TRANSFORMS THE DEPOSIT` 24pt `#E05C5C`.

Three columns:

**AS-PLATED (`#E8A020`):** Matte, porous, granular microstructure. Porosity allows moisture ingress. Surface may tarnish quickly. Adequate but not optimal solderability.

**THE MELT (`#E05C5C`):** Temp exceeds melting point. 60/40 eutectic: 361 F (183 C). 90/10: higher liquidus (~455 F / 235 C). Reflow temp: 400--450 F. Duration: 2--5 sec (IR/hot air) or 30--90 sec (oven). Entire deposit liquefies and resolidifies.

**FUSED SOLDER (`#27AE60`):** Bright, smooth, dense surface. Porosity eliminated. Superior solderability and wetting. Improved corrosion resistance. Extended shelf life. The finish that made PCBs reliable for decades.

Bottom: `The 60/40 eutectic alloy melts at 361 F (183 C) -- the lowest melting point of any Sn-Pb composition. This is why 60/40 became the standard solder alloy.` `#E8A020`

---

## Phase 6 -- Inspection + Solderability Testing

Y: 22.0" to 28.5". Section: `INSPECTION -- PROVE THE DEPOSIT`.

**Left -- Alloy Verification (X: 0.5", W: 11.0"):**
- Fill `#1E2435`, left accent `#E8A020`. Title: `ALLOY VERIFICATION`

| Test | Method | Frequency |
|---|---|---|
| Alloy composition | XRF (non-destructive) | Every lot |
| Thickness | XRF or beta backscatter | Every lot |
| Adhesion | Tape test or bend test | Per specification |
| Visual | 10x magnification | Every rack/reel |

Note: `XRF is the workhorse. 30 seconds per measurement. No sample prep.` `#27AE60`

**Right -- Solderability Testing (X: 12.0", W: 11.5"):**
- Fill `#1E2435`, left accent `#27AE60`. Title: `SOLDERABILITY TESTING`

| Test | Standard | Description |
|---|---|---|
| Dip-and-look | IPC J-STD-002 | Dip in molten solder, inspect wetting |
| Wetting balance | IPC J-STD-002 | Measures wetting force vs. time |
| Steam aging | IPC J-STD-002 | 8 hr steam, then dip-and-look |
| Solderability after reflow | Application-specific | Verify reflow did not degrade wetting |

Note: `Solderability is the entire reason this plating exists. If it does not wet, the plating is worthless.` `#E05C5C`

---

## Phase 7 -- Application Decision Matrix

Y: 28.5" to 32.5". Section: `WHICH POST-TREATMENT FOR YOUR APPLICATION?`.

| Application | Hot Rinse/Dry | Reflow | XRF Alloy Check |
|---|---|---|---|
| PCB surface finish (HASL) | REQUIRED | REQUIRED (hot air leveling) | REQUIRED |
| Connector pins (mil/aero) | REQUIRED | REQUIRED (IR or oven) | REQUIRED |
| Component leads | RECOMMENDED | REQUIRED | REQUIRED |
| Wire/cable solder coat | OPTIONAL | RECOMMENDED | RECOMMENDED |
| Rework / touch-up | OPTIONAL | OPTIONAL | RECOMMENDED |

Values color-coded: REQUIRED = `#E05C5C`, RECOMMENDED = `#E8A020`, OPTIONAL = `#2EC4B6`.

Note: `No chromate conversion coating needed. Tin-lead alloy is inherently solderable and corrosion-resistant for electronics environments.` `#27AE60`

---

## Phase 8 -- Footer

Standard. Title: `Post Treatment -- Tin-Lead`. Version `v1.0 -- 2026`.
Disclaimer: `Lead is restricted under EU RoHS (Directive 2011/65/EU). Tin-lead solder plating is permitted under exemptions for military, aerospace, and high-reliability applications. Applicable specifications: ASTM B579, SAE AS5272, IPC J-STD-001.`

---

## Phase 9 -- Review

- [ ] Headline `POST TREATMENT` 80pt
- [ ] Stages 7+8 both highlighted (Amber)
- [ ] Two-panel hero with Stage 7 and Stage 8 side by side
- [ ] Three reflow method sub-boxes inside Stage 8
- [ ] Three-column before/during/after reflow deep dive
- [ ] Eutectic melting point callout (361 F)
- [ ] Alloy verification + solderability testing panels
- [ ] Application decision matrix with color-coded values
- [ ] "No chromate needed" note
- [ ] Footer with RoHS exemption disclaimer

---

## Phase 10 -- Light Remap & Export

Standard remap. Decision matrix color-coding: verify legibility on light.

Six files: `Post Treatment Tin-Lead -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-28 | Initial. |
