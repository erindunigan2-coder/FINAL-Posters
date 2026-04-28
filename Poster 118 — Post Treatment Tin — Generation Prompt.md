---
Project: Plating Posters Inc
Poster Number: 118
Title: "Post Treatment -- Tin"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-28T00:00:00
Source: Poster 118 -- Post Treatment Tin -- Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - TinPlating
  - PostTreatment
  - Series2
  - ClusterEP11
  - v1
---

# Claude Chat Generation Prompt -- Poster #118
## Post Treatment -- Tin
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
### Step 2 -- `Tin Plating -- Stages 7--8 of 8` -- `32` pt `#E8A020`. Y: **1.4"**.
### Step 3 -- `Anti-tarnish preserves the surface. Reflow kills the whiskers. Skip either one and the tin will fail you -- maybe not today, but eventually.` -- `20` pt at 65%. Y: **2.1"**.

---

## Phase 3 -- Orientation Strip

**Stages 7 AND 8 both highlighted** (fill `#E8A020`). Below: `Before: Freshly plated, rinsed tin surface  -->  After: Protected, reflowed (or dried) finished part`

---

## Phase 4 -- Post-Treatment Sequence Hero

Y: 4.2" to 14.5". Section: `THE FINAL TWO STAGES`.

**Stage 7 -- Anti-Tarnish (left half, X: 0.5", W: 11.0"):** H: 8.5", fill `#1E2435`, top accent `#E8A020`. Badge: `STAGE 7`. Title: `Anti-Tarnish Dip`.
Params: `Proprietary anti-tarnish dip` / `Ambient` / `15--30 sec` / `pH per TDS`.
Purpose: Deposits thin protective film / Prevents tarnishing / Preserves solderability for weeks to months / Required for electronics.
Note: `Without anti-tarnish, tin tarnishes within hours in humid environments.`

**Decision diamond (center):** `REFLOW?` in `#E8A020`.

**Stage 8A -- Reflow (upper-right, X: 13.5", W: 10.0"):** Top accent `#E05C5C`. Badge: `STAGE 8A`. Title: `Reflow (Fuse)`.
`450--500 F (232--260 C)` / `Hot air, IR, or oven` / `Melts tin -- eliminates porosity` / `PRIMARY TIN WHISKER MITIGATION`.

**Stage 8B -- Air Dry (lower-right, X: 13.5", W: 10.0"):** Top accent `#2EC4B6`. Badge: `STAGE 8B`. Title: `Air Dry`.
`Forced warm air or ambient` / `No melting -- as-plated` / `Acceptable for non-critical` / `DOES NOT mitigate whisker risk` (Coral).

Arrow labels: `YES -- electronics, connectors` (to 8A) / `NO -- decorative, food-contact` (to 8B).

---

## Phase 5 -- Tin Whiskers Deep Dive

Y: 14.5" to 22.0". Section: `TIN WHISKERS -- THE #1 RELIABILITY RISK IN PURE TIN`.

Full-width panel, fill `#1E2435`, left accent `#E05C5C`. Title: `WHAT ARE TIN WHISKERS?`

Three columns:

**Column 1 -- THE THREAT (`#E05C5C`):** Conductive crystalline filaments from pure tin / Up to several mm / Spontaneous over weeks to years / Cause: compressive stress from Cu-Sn intermetallic / Result: short circuits, arcing, failure / Documented: satellites, medical devices, nuclear, automotive.

**Column 2 -- WHEN IT HAPPENS (`#E8A020`):** Pure tin (>99%) on copper / No barrier layer / Thin deposit <2 microns highest risk / Temperature cycling / High humidity / Mechanical stress (bent leads, press-fit).

**Column 3 -- HOW TO PREVENT IT (`#27AE60`):** 1. REFLOW (best single mitigation) / 2. Nickel barrier 1--3 um / 3. Alloy with Bi or Ag / 4. Anneal 150 C, 1 hr / 5. Min thickness >8 um / 6. Conformal coat (reduces, does not eliminate).

Bottom banner (Coral): `RoHS eliminated tin-lead. Pure tin replaced it. Tin whiskers are the trade-off. Every tin plater must understand this.`

---

## Phase 6 -- Anti-Tarnish + Reflow Parameters

Y: 22.0" to 28.5". Section: `PROCESS PARAMETERS`.

**Left -- Anti-Tarnish (X: 0.5", W: 11.0"):** Accent `#E8A020`.

| Parameter | Value |
|---|---|
| Type | Proprietary organic anti-tarnish |
| Temperature | Ambient |
| Time | 15--30 sec |
| Rinse after | Optional -- per supplier |
| Shelf life added | 2--12 weeks (humidity dependent) |
| RoHS note | Chromate-free for compliance |

Note (Coral): `Anti-tarnish is NOT a substitute for reflow in whisker-critical applications.`

**Right -- Reflow Methods (X: 12.0", W: 11.5"):** Accent `#E05C5C`.

| Method | Temp | Time | Application |
|---|---|---|---|
| Hot air leveling (HASL) | 450--500 F | Seconds | PCB, connector strip |
| IR reflow oven | 450--500 F | 30--90 sec | Component leads |
| Convection oven | 450--500 F | 1--3 min | Bulk parts |
| Hot oil (legacy) | 450--500 F | 5--15 sec | Rarely used today |

Note: `Reflow temp must exceed 449 F (232 C) -- the melting point of tin.`

---

## Phase 7 -- Application Decision Matrix

Y: 28.5" to 32.5". Section: `WHICH POST-TREATMENT FOR YOUR APPLICATION?`

| Application | Anti-Tarnish | Reflow | Ni Underplate |
|---|---|---|---|
| Electronics (solder) | REQUIRED | REQUIRED | RECOMMENDED |
| Connectors (contact) | REQUIRED | REQUIRED | REQUIRED |
| Food contact / can lining | OPTIONAL | NOT NEEDED | NOT NEEDED |
| Decorative | OPTIONAL | NOT NEEDED | NOT NEEDED |
| Corrosion protection (steel) | RECOMMENDED | OPTIONAL | OPTIONAL |

Color code: REQUIRED = `#E05C5C` | RECOMMENDED = `#E8A020` | OPTIONAL = `#2EC4B6` | NOT NEEDED = `#F0EDE8` at 50%.

---

## Phase 8 -- Footer

Standard. Title: `Post Treatment -- Tin`. Version `v1.0 -- 2026`.
Disclaimer adds: `Tin whisker information reflects current industry understanding as of 2026. Consult iNEMI and JEDEC standards for latest requirements.`

---

## Phase 9 -- Review

- [ ] Stages 7+8 highlighted
- [ ] Decision branch hero (anti-tarnish -> reflow vs. air dry)
- [ ] Tin whisker deep-dive (3-column, Coral-accented)
- [ ] Anti-tarnish + reflow parameter panels
- [ ] Application decision matrix (5 rows, color-coded)
- [ ] Footer with whisker disclaimer

---

## Phase 10 -- Light Remap & Export

Standard remap. Six files: `Post Treatment Tin -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-28 | Initial. |
