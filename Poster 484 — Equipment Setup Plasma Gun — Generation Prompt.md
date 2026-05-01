---
Project: Plating Posters Inc
Poster Number: 484
Title: "Equipment Setup -- Plasma Gun"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-30T00:00:00
Source: Poster 484 — Equipment Setup Plasma Gun — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - ThermalSpray
  - PlasmaSpray
  - APS
  - Equipment
  - PlasmaGun
  - ClusterTS01
  - v1
---

# Claude Chat Generation Prompt -- Poster #484
## Equipment Setup -- Plasma Gun
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-30).*

---

> **IMPORTANT:** Generate as HTML artifact. 24 x 36" portrait. Dark edition first.

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E`, locked palette, 0.5" safe zone. iOS Liquid Glass aesthetic. Fonts: Barlow Condensed 800 (headlines), Barlow 600 (subheads), Inter 400/500 (body), JetBrains Mono 400 (data/params).

---

## Phase 2 -- Header

### Step 1 -- `EQUIPMENT SETUP` -- `80` pt `#F0EDE8`. Y: **0.5"**.
### Step 2 -- `Plasma Spray Gun & System Components -- Stage 4 of 10` -- `32` pt `#C8D0D8`. Y: **1.4"**.
### Step 3 -- `A DC arc, two gases, a powder feeder, a robot, and a lot of cooling water. Here is how it all connects.` -- `20` pt at 65%. Y: **2.1"**.

Rule card (right): Big number `40-80` 64pt `#E8A020`. Label: `kW DC power -- the engine of the plasma jet`.

---

## Phase 3 -- Orientation Strip

Poster 6 of 10 highlighted. Stage 4 highlighted (`#C8D0D8` fill, `#1A1F2E` text).

---

## Phase 4 -- System Components + Gun Anatomy (HERO)

Y: 4.2" to 15.5". Section label: `PLASMA SPRAY SYSTEM -- 8 MAJOR COMPONENTS`.

**System Component Diagram (Y: 5.0"-11.5"):** Eight labeled boxes connected by flow lines. Each: 5.0" x 2.0", fill `#1E2435`, top accent 4pt.

| Component | Accent | Key Specs |
|---|---|---|
| 1. PLASMA GUN | `#E8A020` | Cathode: 2% thoriated W. Anode: OFHC Cu. Powder injector port(s). |
| 2. POWER SUPPLY | `#E8A020` | 40-80 kW DC. 400-800 A at 50-80 V. |
| 3. GAS CONSOLE | `#2EC4B6` | Mass flow controllers. Primary: Ar or N2. Secondary: H2, He, or N2. |
| 4. POWDER FEEDER | `#2EC4B6` | Volumetric or gravimetric. Carrier gas: Ar. 20-80 g/min. |
| 5. ROBOT | `#27AE60` | 6-axis industrial. Traverse speed, standoff, spray angle. |
| 6. COOLING SYSTEM | `#2EC4B6` | Closed-loop water. 15-25 L/min at 15-20 degC. |
| 7. SPRAY BOOTH | `#3A4055` | Enclosed. Dust collection (HEPA/cartridge). Downdraft preferred. |
| 8. CONTROL SYSTEM | `#3A4055` | PLC or proprietary. Real-time parameter monitoring. |

Connection lines: 2pt dashed `#3A4055` labeled DC POWER, GAS, POWDER+CARRIER, COOLING WATER, ROBOT ARM.

**Gun Anatomy (Y: 12.0"-15.3"):** Simplified cross-section, W: 18.0". Labels L-R: CATHODE (W-2%Th), ARC ZONE, ANODE (Cu OFHC), GAS INJECTION, POWDER INJECTOR, PLASMA PLUME exit. JetBrains Mono 11pt with leader lines.

---

## Phase 5 -- Gas Selection Guide

Y: 15.5" to 22.0". Section label: `GAS SELECTION -- PRIMARY AND SECONDARY`.

| Gas | Role | Typical Flow | Effect on Plasma | When to Use |
|---|---|---|---|---|
| Argon (Ar) | Primary | 35-60 SLPM | Stabilizes arc; low enthalpy/unit | Standard primary for all APS |
| Nitrogen (N2) | Primary (alt) | 30-50 SLPM | Higher enthalpy than Ar; cheaper | Non-reactive coatings; cost-sensitive |
| Hydrogen (H2) | Secondary | 5-15 SLPM | Dramatically increases enthalpy | Ceramics (YSZ, Al2O3); high-melt-point |
| Helium (He) | Secondary | 20-50 SLPM | Moderate enthalpy; gentler than H2 | Sensitive substrates |
| Nitrogen (N2) | Secondary | 5-20 SLPM | Lower cost alt to H2/He | Budget; metallic coatings |

Callout: `CAUTION: Hydrogen is flammable. Leak detection mandatory. Never use H2 without flash-back arrestors and ventilation.` `#E05C5C`.

---

## Phase 6 -- Startup Sequence + Troubleshooting

### Startup Sequence (Y: 22.0"-28.5")

Section label: `PRE-SPRAY STARTUP SEQUENCE`. Two columns, 5 steps each. Alternating fills.

| Step | Action |
|---|---|
| 1 | Verify cooling water flow and temp (15-25 L/min, 15-20 degC) |
| 2 | Open gas supply; check cylinder pressure and regulators |
| 3 | Set primary gas flow (Ar) on MFC |
| 4 | Set secondary gas flow (H2/He) on MFC |
| 5 | Power on control system; load recipe |
| 6 | HF arc start; verify stable arc |
| 7 | Adjust power to target (verify V and A) |
| 8 | Start powder feeder; set carrier gas and feed rate |
| 9 | Test passes on sacrificial coupon |
| 10 | Begin production after coupon passes |

### Troubleshooting (Y: 28.5"-32.5")

Four coral-accented cards:

| Problem | Cause | Fix |
|---|---|---|
| ARC WON'T START | Gas flow too low; electrode worn; HF fault | Check gas; inspect cathode/anode; test HF igniter |
| UNSTABLE ARC | Worn anode/cathode; gas flow fluctuation | Replace consumables; verify MFCs |
| POWDER CLOGGING | Moisture; carrier gas too low; injector buildup | Dry powder; increase carrier; clean injector |
| OVERHEATING GUN | Cooling water insufficient; temp too high | Check pump/flow; verify chiller |

---

## Phase 7 -- Footer

Standard. Title: `Equipment Setup -- Plasma Gun`. Version `v1.0 -- 2026`.
Disclaimer: `This poster is an educational reference tool. Equipment specifications shown are typical for atmospheric plasma spray systems. Specific systems vary by manufacturer. Consult your equipment supplier documentation. Source: ASM Handbook Vol 5A; ITSA references.`

---

## Phase 8 -- Review

- [ ] Headline `EQUIPMENT SETUP` 80pt
- [ ] 40-80 kW rule card
- [ ] Orientation strip with Stage 4 highlighted
- [ ] 8-component system diagram with connection lines
- [ ] Gun anatomy cross-section
- [ ] 5-row gas selection table with H2 caution
- [ ] 10-step startup checklist
- [ ] 4 troubleshooting cards
- [ ] Footer with disclaimer and version

---

## Phase 9 -- Light Remap & Export

Standard remap. Verify accent legibility on light background.

Six files: `Equipment Setup Plasma Gun -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-30 | Initial. |
