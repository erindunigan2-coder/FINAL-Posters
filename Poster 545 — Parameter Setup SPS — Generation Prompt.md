---
Project: Plating Posters Inc
Poster Number: 545
Title: "Parameter Setup -- Suspension Plasma Spray (SPS)"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-30T00:00:00
Source: Poster 545 — Parameter Setup SPS — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - ThermalSpray
  - SPS
  - Parameters
  - ClusterTS07
  - v1
---

# Claude Chat Generation Prompt -- Poster #545
## Parameter Setup -- Suspension Plasma Spray (SPS)
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-30).*

---

> **IMPORTANT:** Generate as HTML artifact. 24 x 36" portrait. Dark edition first.

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E`, locked palette, 0.5" safe zone. iOS Liquid Glass aesthetic. Fonts: Barlow Condensed 800 (headlines), Barlow 600 (subheads), Inter 400/500 (body), JetBrains Mono 400 (data/params).

---

## Phase 2 -- Header

### Step 1 -- `PARAMETER SETUP` -- `88` pt `#F0EDE8`. Y: **0.5"**.
### Step 2 -- `Suspension Plasma Spray (SPS) -- Process Variables & Control` -- `32` pt `#2EC4B6`. Y: **1.4"**.
### Step 3 -- `Same plasma gun. Different rules. Closer standoff, liquid feed instead of carrier gas, and narrower process windows. Get the parameters right or the columnar structure never forms.` -- `20` pt at 65%. Y: **2.1"**.

Rule card (right): Big number `13` 72pt `#2EC4B6`. Label: `key process variables -- each compared against conventional APS`.

---

## Phase 3 -- Orientation Strip

Poster 7 of 10 highlighted. Stage 7 highlighted (Teal -- parameters).

---

## Phase 4 -- Parameter Table (HERO)

Y: 3.8" to 15.3". Section label: `SPS OPERATING PARAMETERS -- WITH APS COMPARISON`.

13-row table. Columns: Parameter (5.5") | SPS Range (5.5") | APS Range (5.0") | Notes (7.0").

| Parameter | SPS Range | APS Range | Notes |
|---|---|---|---|
| Arc current | 400-700 A | 400-800 A | Similar range |
| Arc voltage | 50-80 V | 50-80 V | Gas-dependent |
| Power | 30-60 kW | 25-60 kW | Higher for SPS -- solvent evaporation |
| Primary gas (Ar) | 40-60 SLPM | 35-60 SLPM | Similar |
| Secondary gas (H2) | 6-14 SLPM | 5-15 SLPM | Higher H2 for enthalpy |
| Secondary gas (He) | 20-50 SLPM | 20-50 SLPM | Alternative to H2 |
| Suspension flow rate | 20-100 mL/min | N/A (powder) | LIQUID FEED -- no carrier gas |
| Solids loading | 5-30 wt% | N/A | Higher = faster but clogging risk |
| Standoff distance | 40-80 mm | 75-150 mm | MUCH CLOSER |
| Traverse speed | 500-2000 mm/s | 200-1000 mm/s | Faster; thin layers/pass |
| Step increment | 2-4 mm | 3-6 mm | Finer spray footprint |
| Deposition rate | 0.5-3 kg/hr | 2-10 kg/hr | Lower than APS |
| Deposition efficiency | 20-50% | 40-70% | Lower due to overspray |

Rows where SPS diverges significantly (standoff, traverse, suspension flow, deposition): highlight SPS cell `#27AE60` at 10%. Header fill `#3A4055`.

---

## Phase 5 -- Suspension Feed Parameters

Y: 15.5" to 22.0". Section label: `SUSPENSION FEED -- THE CORE SPS VARIABLE`.

**Left -- Suspension Characteristics (W: 11.0", accent `#27AE60`):**

| Variable | Range | Impact |
|---|---|---|
| Particle size | 50 nm-5 um | Finer = more columnar; coarser = denser |
| Solids loading | 5-30 wt% | Higher = faster; clogging risk |
| Carrier liquid | Ethanol or water | Ethanol: better atomization; water: safer |
| Flow rate | 20-100 mL/min | Must match plasma enthalpy |
| Shelf life | LIMITED | Sedimentation; agitate before use |

Ethanol note in `#E05C5C`: requires explosion-proof handling.

**Right -- Injection Configuration (W: 11.5", accent `#E8A020`):**

*Mechanical Stream:* Continuous liquid into plume. Simpler, more common. Fragmentation by plasma momentum. Radial external injection.

*Atomizing:* Pre-atomized spray. Better droplet control. More complex; higher gas use. R&D/optimization.

Note: `Injection is typically radial (external) -- not through gun like APS powder` `#2EC4B6`.

---

## Phase 6 -- Gas Console + Troubleshooting

### Gas Flow Settings (Left, Y: 22.0"-28.5")

| Gas | Role in SPS | Flow Rate |
|---|---|---|
| Primary (Ar) | Stabilizes arc; plasma forming | 40-60 SLPM |
| Secondary (H2) | Enthalpy for solvent evaporation | 6-14 SLPM |
| Secondary (He) | Alternative; gentler heating | 20-50 SLPM |
| Carrier (Ar) | NOT USED IN SPS | -- |

"NOT USED" row: `#E8A020` background 15%.

### No Carrier Gas Callout (Right, accent `#27AE60`)

In APS: carrier gas (Ar) delivers dry powder. In SPS: LIQUID SUSPENSION replaces carrier gas entirely -- injected as stream or spray, plasma evaporates solvent and melts particles. No powder feeder. No carrier gas line.

`No powder feeder. No carrier gas. Liquid in, coating out.` JetBrains Mono 14pt `#27AE60`.

### Troubleshooting (Y: 28.5"-32.5")

Section label: `PARAMETER PROBLEMS -- 4 COMMON ISSUES`. Four cards:

| Problem | Cause | Fix |
|---|---|---|
| LAMELLAR INSTEAD OF COLUMNAR | Standoff too far; particles too large | Reduce standoff 40-60 mm; verify size < 5 um |
| LOW DEPOSITION RATE | Low solids loading; insufficient flow | Increase loading 15-25 wt%; increase flow |
| INJECTOR CLOGGING | Sedimentation; high loading; aged suspension | Agitate; reduce loading; check shelf life |
| SUBSTRATE OVERHEATING | Standoff too close; poor cooling; slow traverse | Increase cooling; increase traverse; temp < 400 degC |

Problem: `#E05C5C`. Fix: `#27AE60`.

---

## Phase 7 -- Footer

Standard. Title: `Parameter Setup -- Suspension Plasma Spray (SPS)`. Version `v1.0 -- 2026`.
Disclaimer: `SPS parameters are less standardized than conventional APS. Ranges shown are representative of current research and early-production practice. Consult your coating supplier and OEM for application-specific settings.`

---

## Phase 8 -- Review

- [ ] Headline `PARAMETER SETUP` 88pt
- [ ] 13 rule card
- [ ] 13-row SPS vs. APS parameter table with divergence highlights
- [ ] Suspension characteristics table (5 variables)
- [ ] Injection configuration comparison (mechanical vs. atomizing)
- [ ] Gas console table (4 rows) with "NOT USED" highlight
- [ ] "No carrier gas" callout
- [ ] 4 troubleshooting cards
- [ ] Footer with disclaimer and version

---

## Phase 9 -- Light Remap & Export

Standard remap. Verify accent legibility on light background.

Six files: `Parameter Setup SPS -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-30 | Initial. |
