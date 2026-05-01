---
Project: Plating Posters Inc
Poster Number: 527
Title: "Post-Treatment -- Cold Spray"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-30T00:00:00
Source: Poster 527 — Post-Treatment Cold Spray — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - ColdSpray
  - ThermalSpray
  - PostTreatment
  - ClusterTS05
  - v1
---

# Claude Chat Generation Prompt -- Poster #527
## Post-Treatment -- Cold Spray
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-30).*

---

> **IMPORTANT:** Generate as HTML artifact. 24 x 36" portrait. Dark edition first.

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E`, locked palette, 0.5" safe zone. iOS Liquid Glass aesthetic. Fonts: Barlow Condensed 800 (headlines), Barlow 600 (subheads), Inter 400/500 (body), JetBrains Mono 400 (data/params).

---

## Phase 2 -- Header

### Step 1 -- `POST-TREATMENT` -- `80` pt `#F0EDE8`. Y: **0.5"**.
### Step 2 -- `Cold Spray -- Recover Ductility, Achieve Final Dimensions` -- `32` pt `#E8A020`. Y: **1.5"**.
### Step 3 -- `Anneal for ductility. Machine like wrought metal. No diamond grinding required -- because the deposit was never molten.` -- `22` pt at 65%. Y: **2.2"**.

Rule card (right): Big number `0` 72pt `#27AE60`. Label: `special tools needed -- conventional machining only`.

---

## Phase 3 -- Annealing Schedules + Machining Callout (HERO)

Y: 2.9" to 14.0". Section label: `HEAT TREATMENT SCHEDULES`.

**Left -- Annealing Table (W: 14.5"):**

6-row table. Columns: Material (3.0") | Temperature (3.0") | Time (2.0") | Atmosphere (3.0") | Purpose (3.5").

| Material | Temperature | Time | Atmosphere | Purpose |
|---|---|---|---|---|
| Copper (Cu) | 200--400 C | 1--4 hr | Vacuum or inert (Ar/N2) | Recover ductility; conductivity to ~98% IACS |
| Aluminum (6061) | T6 temper schedule | Per alloy spec | Air or inert | Restore temper properties |
| Aluminum (7075) | T7 temper schedule | Per alloy spec | Air or inert | Overaged temper for SCC resistance |
| Titanium (CP) | 500--700 C | 1--4 hr | Vacuum (mandatory) | Ductility; inter-particle bonding |
| Ti-6Al-4V | 500--700 C | 1--4 hr | Vacuum (mandatory) | Diffusion bonding; ductility recovery |
| Nickel (Inconel 625) | 600--800 C | 1--2 hr | Vacuum or inert | Inter-particle metallurgical bonding |

Temperature values in `#E8A020`. Header fill `#3A4055`.

**Anneal note:** `Heat treatment improves inter-particle bonding through solid-state diffusion -- atoms migrate across interfaces, converting mechanical interlocks into metallurgical bonds.` Amber-bordered banner.

**Vacuum warning:** `TITANIUM: Vacuum atmosphere MANDATORY above 400 C. Ti oxidizes aggressively in air at elevated temperatures.` Coral-bordered banner.

**Right -- "Machines Like Wrought" Callout (W: 8.0"):**

Y: 3.8" to 12.8". Emerald-tinted glass card.
Title: `MACHINES LIKE WROUGHT` Barlow Condensed 800, 28pt, `#27AE60`.

Body: `Cold spray is the ONLY thermal spray where deposits can be machined with conventional tools: Turning, Milling, Drilling, Tapping, Grinding (standard wheels). No diamond grinding. No special tooling. No carbide-specific cutters.`

Comparison (JetBrains Mono 13pt):
```
COLD SPRAY:    Conventional machining
HVOF (WC-Co):  Diamond grinding ONLY
Plasma Spray:  Diamond grinding typical
Flame Spray:   Diamond grinding (fused)
```
"Conventional machining" in `#27AE60`, others at 60%.

---

## Phase 4 -- Decision Flowchart + Sealing

Y: 14.0" to 22.0". Section label: `POST-TREATMENT DECISION GUIDE`.

**Left -- Decision Flowchart (W: 15.0"):**

Four decision diamonds with branching:

| Step | Question | Yes | No |
|---|---|---|---|
| 1 | Ductility recovery needed? | ANNEAL | Step 2 |
| 2 | Dimensional accuracy required? | MACHINE | Step 3 |
| 3 | Electrical/thermal conductivity critical? | ANNEAL (Cu: 200--400 C -> ~98% IACS) | Step 4 |
| 4 | Porosity > 1%? | SEAL | USE AS-SPRAYED |

Outcomes: ANNEAL (`#E8A020`) | MACHINE (`#27AE60`) | SEAL (`#2EC4B6`) | AS-SPRAYED (`#C8D0D8`).

**Right -- Sealing Note (W: 7.5", accent `#2EC4B6`):**

Title: `SEALING -- RARELY NEEDED`.

Porosity reference: Cu < 0.5% | Al 0.5--2% | Ti 1--3%.

`Sealing only when: porosity exceeds spec, hermetic barrier needed, or severe corrosion environment. Method: epoxy vacuum impregnation.`

**Compressive Stress Note (below):** Emerald-accented card.
Title: `WHY NO STRESS RELIEF?`
Body: `Cold spray deposits have COMPRESSIVE residual stress -- opposite of other thermal spray. Compressive stress is beneficial for fatigue life and prevents cracking. No stress relief needed for dimensional stability.`

---

## Phase 5 -- Property Comparison + Issues + Footer

**Left -- Before/After Copper (W: 14.0"):**

Section label: `BEFORE AND AFTER -- COPPER BENCHMARK`.

8-row table. Columns: Property (4.5") | As-Sprayed (4.5") | After Anneal 300 C / 2 hr (5.0").

| Property | As-Sprayed | After Anneal |
|---|---|---|
| Hardness | 100--150 HV | 60--90 HV |
| Ductility (elongation) | 1--5% | 10--25% |
| Electrical conductivity | 80--95% IACS | 95--98% IACS |
| Thermal conductivity | Near bulk | ~bulk (401 W/mK) |
| Bond strength (C633) | > 60 MPa | > 60 MPa |
| Porosity | < 0.5% | < 0.5% |
| Residual stress | Compressive | Relaxed (still beneficial) |
| Machinability | Good (harder) | Excellent (softened) |

As-Sprayed in `#E8A020`. Post-Anneal in `#27AE60`.

Trade-off: `Annealing recovers ductility and conductivity but REDUCES hardness. Choose based on priority -- wear resistance (skip anneal) vs. electrical performance (anneal).` Amber banner.

**Right -- Common Issues (W: 8.5", 4 stacked cards):**

| Issue | Color | Cause | Fix |
|---|---|---|---|
| OVER-ANNEALING | `#E05C5C` | Temp too high / time too long | Reduce; verify with hardness test |
| OXIDATION DURING ANNEAL | `#E05C5C` | Air atmosphere for O2-sensitive material | Vacuum or inert; O2 < 10 ppm |
| CHATTER DURING MACHINING | `#E8A020` | Work-hardened deposit | Anneal first; rigid setup; reduce DOC |
| DIMENSIONAL OVERSHOOT | `#E8A020` | Insufficient machining stock | Plan: final dim + 0.25--0.5 mm/side |

**Footer:** Standard. Title: `Post-Treatment -- Cold Spray`. Version `v1.0 -- 2026`.
Disclaimer: `This poster is an educational reference tool. Heat treatment schedules and machining parameters vary by material, deposit thickness, and application. Consult your metallurgist and process specification.`

---

## Phase 6 -- Review

- [ ] Headline `POST-TREATMENT` 80pt
- [ ] 0 special tools rule card
- [ ] 6-row annealing schedule table
- [ ] Ti vacuum warning (coral)
- [ ] "Machines Like Wrought" callout with 4-process comparison
- [ ] Decision flowchart (4 diamonds, 4 outcomes)
- [ ] Sealing note with porosity reference
- [ ] Compressive stress note
- [ ] 8-row before/after copper benchmark table
- [ ] Trade-off banner
- [ ] 4 common issue cards
- [ ] Footer with disclaimer and version

---

## Phase 7 -- Light Remap & Export

Standard remap. Verify accent legibility on light background.

Six files: `Post-Treatment Cold Spray -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-30 | Initial. |
