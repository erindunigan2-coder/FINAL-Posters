---
Project: Plating Posters Inc
Poster Number: 244
Title: "Main Tank -- Electroless Copper Bath"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters -- Watson Research Brief (Process 4: Electroless Copper, Poster 6)"
Technical Source: Formaldehyde-based electroless copper bath chemistry. Autocatalytic Cu deposition via HCHO reducing agent in alkaline EDTA-complexed solution. Covers bath composition, operating parameters, deposit properties, deposition reaction, and formaldehyde safety. Watson-verified formaldehyde concentration: 3-15 mL/L of 37% formaldehyde solution (NOT 4-8 g/L). IPC-TM-650 reference.
Process Scope: Electroless copper -- Stage 6 of 8 (main plating tank)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ElectrolessCopper
  - MainTank
  - Formaldehyde
  - ConstructionWorkup
  - Series2
  - ClusterEL-Cu
---

# Poster #244 -- Construction Workup
## Main Tank -- Electroless Copper Bath

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 6 of the electroless copper process -- the main event. This is where metallic copper deposits on the Pd-catalyzed surface through autocatalytic reduction using formaldehyde (HCHO) as the reducing agent. The chemistry is fundamentally different from EN-P: formaldehyde instead of hypophosphite, strongly alkaline instead of acid, EDTA instead of organic acids, and the deposit is pure copper (>99.5% Cu) with no alloy constituents.

The E-Cu bath is the most chemically sensitive bath in the electroless family. It operates at pH 11.5-13.0, uses a volatile and toxic reducing agent (formaldehyde -- IARC Group 1 carcinogen), and has a shorter bath life (1-4 MTO) than EN-P. Bath stability is the central operational challenge. Spontaneous decomposition (plate-out on tank walls) is a constant risk.

The formaldehyde safety callout is non-negotiable -- OSHA PEL 0.75 ppm TWA, with classification as a known human carcinogen. This is the most hazardous reducing agent in all of electroless plating.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Bath composition table (Block B -- HERO):** Full formulation with roles.
2. **Orientation strip (Block C):** 8-stage strip, Stage 6 highlighted.
3. **Deposition reaction mechanism (Block D):** The core autocatalytic reaction.
4. **Operating parameters and deposit properties (Block E).**
5. **Formaldehyde safety (Block F):** Mandatory safety callout.
6. **Troubleshooting strip (Block G).**

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 22.0" / 28.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 6 highlighted (Emerald)
ZONE 3 -- BATH CHEMISTRY HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- DEPOSITION REACTION + OPERATING PARAMETERS (14.5"--22.0" / ~7.5")
ZONE 5 -- DEPOSIT PROPERTIES + FORMALDEHYDE SAFETY (22.0"--28.0" / ~6.0")
ZONE 6 -- TROUBLESHOOTING (28.0"--32.5" / ~4.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `MAIN TANK` -- Barlow Condensed ExtraBold, 88 pt, `#F0EDE8`. X: 0.5", Y: 0.5".

**Subheading:** `Electroless Copper -- Formaldehyde-Based Alkaline Bath -- Stage 6 of 8` -- Barlow SemiBold, 28 pt, `#27AE60` (Emerald). X: 0.5", Y: 1.4".

**Tagline:** `Pure copper from an alkaline bath. No electricity. No anodes. Formaldehyde reduces Cu2+ to metallic copper at every Pd-catalyzed site. The deposit is >99.5% Cu with excellent conductivity.` -- Barlow SemiBold, 20 pt, `#F0EDE8` at 65%. X: 0.5", Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 6 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.

Below: `Before: Clean, Pd-activated surface from accelerator  -->  After: Thin-film copper deposit (0.5-2.5 um) -- conductive seed for electrolytic buildup`

---

### ZONE 3 -- Bath Chemistry Hero

**Section label:** `ELECTROLESS COPPER BATH COMPOSITION` -- Y: 4.4".

**BLOCK B -- Bath Composition Table (Y: 5.0" to 12.0")**

Large rounded rectangle: X: 0.5", Y: 5.0", W: 23.0", H: 6.8", fill `#1E2435`, radius 8.

**Bath composition table:**

Column widths: Component (5.5") | Concentration (4.5") | Role (13.0")

| Component | Concentration | Role |
|---|---|---|
| Copper sulfate (CuSO4 . 5H2O) | 7-12 g/L (1.5-3.0 g/L Cu2+) | Metal ion source -- provides Cu2+ for reduction |
| Formaldehyde (37% solution) | 3-15 mL/L | Reducing agent -- oxidized to formate (HCOO-); consumed + volatile loss |
| NaOH | 5-10 g/L | pH control -- provides OH- consumed in the deposition reaction |
| EDTA (tetrasodium salt) | 25-40 g/L | Primary complexant -- prevents Cu(OH)2 precipitation at high pH |
| 2,2'-Bipyridyl or proprietary | 10-30 mg/L | Stabilizer -- prevents spontaneous decomposition (replaces cyanide) |
| Surfactant (wetting agent) | 0.01-0.1 g/L | Reduces hydrogen pitting by promoting H2 bubble release |

Data: JetBrains Mono 12 pt `#F0EDE8`. Component names: Inter Medium 13 pt `#27AE60`.
Headers: Barlow SemiBold 14 pt, fill `#3A4055`.
Alternating rows: `#1E2435` / `#252B3D`.

**Formaldehyde concentration callout (below table, Y: 12.0"):**
- Rounded rect, X: 0.5", W: 23.0", H: 0.8", fill `#E8A020` at 20%, border-left 0.06" `#E8A020`
- `FORMALDEHYDE: 3-15 mL/L of 37% solution (3-8 mL/L light/PCB seed; 10-15 mL/L standard/heavy-build). Volatile and consumed rapidly -- replenish frequently. Monitor by titration or colorimetric test.` Inter Medium 13 pt `#E8A020`

**Legacy stabilizer note (Y: 13.0"):**
- `NOTE: Some older formulations use trace sodium cyanide (10-20 mg/L) as a stabilizer. Modern E-Cu baths are overwhelmingly cyanide-free, using bipyridyl or proprietary organic stabilizers instead.` Inter Regular 11 pt `#F0EDE8` at 60%

---

### ZONE 4 -- Deposition Reaction + Operating Parameters

**Section label:** `THE AUTOCATALYTIC REACTION` -- Y: 14.7".

**BLOCK D -- Reaction Mechanism (Y: 15.3" to 18.0")**

Large equation panel: X: 0.5", W: 23.0", H: 2.5", fill `#252B3D`, radius 8.

Center-aligned equation:
- `Cu2+ + 2 HCHO + 4 OH-  -->  Cu0 + 2 HCOO- + 2 H2O + H2` JetBrains Mono 22 pt `#27AE60`

Below equation, four annotation labels:

| Label | Color | Text |
|---|---|---|
| Left | `#27AE60` | Cu2+ reduced to metallic copper |
| Center-left | `#E8A020` | Formaldehyde oxidized to formate |
| Center-right | `#2EC4B6` | Hydroxide consumed (pH drops during plating) |
| Right | `#F0EDE8` at 60% | Hydrogen gas evolved (bubbles) |

**Key insight callout (Y: 18.2"):**
- Rounded rect, X: 0.5", W: 23.0", H: 1.0", fill `#1E2435`, left accent `#E8A020`
- `The reaction consumes OH- -- pH drops continuously during plating. NaOH addition is required to maintain pH 11.5-13.0. Automatic pH control is strongly recommended.` Inter Medium 14 pt `#E8A020`

**BLOCK E -- Operating Parameters (Y: 19.5" to 21.8")**

Two side-by-side tables.

**Left -- Operating Parameters (X: 0.5", W: 11.0"):**
Header: `OPERATING PARAMETERS` fill `#3A4055`.

| Parameter | Target | Tolerance |
|---|---|---|
| pH | 11.5-13.0 | +/- 0.3 |
| Temperature | 28-45 C (82-113 F) | +/- 2 C |
| Cu2+ concentration | 1.5-3.0 g/L | +/- 0.3 g/L |
| Formaldehyde | 3-15 mL/L of 37% HCHO | Replenish frequently |
| Deposition rate | 1-5 um/hr (thin-film) | Up to 5-8 um/hr (heavy-build) |
| Bath life | 1-4 MTO | Shorter than EN |
| Air agitation | Required | Replenishes HCHO; removes H2 |

**Right -- Key Differences from EN (X: 12.0", W: 11.5"):**
Header: `HOW E-Cu DIFFERS FROM EN-P` fill `#3A4055`.

| Factor | Electroless Copper | Electroless Nickel (Mid-P) |
|---|---|---|
| Reducing agent | Formaldehyde (HCHO) | Sodium hypophosphite |
| pH | 11.5-13.0 (strongly alkaline) | 4.5-5.5 (acid) |
| Complexant | EDTA | Organic acids |
| Deposit | Pure Cu (>99.5%) | Ni-P alloy (6-9% P) |
| Bath life | 1-4 MTO | 4-8 MTO |
| Stability | Lower (prone to decomposition) | Higher (more forgiving) |
| Typical thickness | 0.5-2.5 um (seed layer) | 12-50 um (functional) |

Data: JetBrains Mono 11 pt.

---

### ZONE 5 -- Deposit Properties + Formaldehyde Safety

**Section label:** `DEPOSIT PROPERTIES & FORMALDEHYDE SAFETY` -- Y: 22.2".

**Left -- Deposit Properties (X: 0.5", W: 11.0", Y: 22.8" to 27.8"):**
- Rounded rect, H: 4.6", fill `#1E2435`, left accent `#27AE60`
- Title: `DEPOSIT CHARACTERISTICS` Barlow SemiBold 18 pt `#27AE60`

| Property | Value |
|---|---|
| Composition | Pure copper (>99.5% Cu) |
| Conductivity | Excellent -- 90-95% IACS |
| Typical thickness (PCB) | 0.5-2.5 um (seed layer) |
| Typical thickness (heavy-build) | 25-50 um (EMI shielding) |
| Adhesion to FR4 laminate | Good with proper desmear + activation |
| Ductility | Moderate; improves with annealing |
| Appearance | Bright pink-copper; oxidizes rapidly in air |

Data: JetBrains Mono 12 pt.

Application note: `In PCB manufacturing, the E-Cu deposit is purely a conductive bridge. It provides the electrical path for subsequent electrolytic acid copper buildup to 25-50 um final thickness.` Inter Medium 12 pt `#E8A020`

**Right -- Formaldehyde Safety (X: 12.0", W: 11.5", Y: 22.8" to 27.8"):**
- Rounded rect, H: 4.6", fill `#E05C5C` at 15%, border 3 pt `#E05C5C`
- Title: `FORMALDEHYDE SAFETY -- MANDATORY` Barlow Condensed ExtraBold 20 pt `#E05C5C`

Content (Inter Medium 14 pt `#F0EDE8`):
```
OSHA PEL: 0.75 ppm (8-hr TWA)
OSHA STEL: 2 ppm (15-min short-term)
Classification: IARC Group 1
  (known human carcinogen)
```

Requirements (Inter Regular 13 pt `#F0EDE8`):
```
LOCAL EXHAUST VENTILATION -- required
  Slot ventilation at tank lip preferred

CONTINUOUS AIR MONITORING -- required
  Personal and area sampling

RESPIRATORY PROTECTION -- if PEL exceeded
  Half-face respirator with organic vapor
  cartridge minimum

PPE: chemical splash goggles, face shield,
     neoprene or nitrile gloves, apron

ALTERNATIVE: Glyoxylic acid-based E-Cu
  baths (formaldehyde-free) are gaining
  market share for health/safety reasons
```

---

### ZONE 6 -- Troubleshooting

**Section label:** `WHAT GOES WRONG AT THE MAIN TANK` -- Y: 28.2".

**Five problem cards (Y: 28.8" to 32.3"):**

| Card | X | W | Problem | Cause | Fix |
|---|---|---|---|---|---|
| 1 | 0.5" | 4.4" | NO DEPOSITION | Pd catalyst stripped; pH too low; HCHO depleted | Check Pd activation; adjust pH; replenish HCHO |
| 2 | 5.2" | 4.4" | SPONTANEOUS DECOMPOSITION | Bath instability; contamination; temp spike | Filter; add stabilizer; check temperature control |
| 3 | 9.9" | 4.4" | ROUGH / NODULAR DEPOSIT | Particles in bath; Cu(OH)2 precipitates | Filter (1 um); check pH; clean tank walls |
| 4 | 14.6" | 4.4" | POOR ADHESION | Inadequate desmear; weak Pd activation | Improve desmear; check catalyst and accelerator |
| 5 | 19.3" | 4.2" | HYDROGEN PITTING | H2 bubbles trapped on surface | Add/check surfactant; increase air agitation |

Card construction: Rounded rect, H: 3.2", fill `#1E2435`, left accent 0.04" `#E05C5C`.
Problem: Barlow SemiBold 12 pt `#E05C5C`. Cause/Fix: Inter Regular 11 pt `#F0EDE8`.

---

### ZONE 7 -- Footer

Standard footer. Title: `Main Tank -- Electroless Copper Bath`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Bath composition and operating parameters shown are typical for formaldehyde-based electroless copper plating for PCB and plastics metallization. Formaldehyde concentration: 3-15 mL/L of 37% solution (Watson-verified). Proprietary bath formulations vary by supplier. Consult your supplier TDS and SDS. Source: IPC-TM-650; general industry practice.`

---

## Parts 5-7

**Grouping:** 7 zones.
**Light Remap:** Standard table. Safety panel border `#E05C5C` -> `#C0392B`.
**Export:** Six files -- `Main Tank E-Cu -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the crown jewel of the EL-04 Electroless Copper cluster. The bath composition table is the primary reference element -- every E-Cu operator needs this on the wall. The Watson-verified formaldehyde concentration of 3-15 mL/L of 37% solution is called out explicitly with a dedicated callout bar to prevent the common literature error of reporting 4-8 g/L (which conflates HCHO gas content with the 37% solution volume).

The deposition reaction equation is given hero treatment at 22 pt because this is the core chemistry. The four annotation labels below the equation make it readable for operators who do not have chemistry backgrounds.

The formaldehyde safety panel is the largest safety callout in the entire electroless series. This is deliberate -- formaldehyde is the most hazardous reducing agent used in any autocatalytic plating process, and every poster on this wall should remind operators of that fact.

The EN-P comparison table in Zone 4 is valuable context for shops that run both processes. The differences are fundamental (alkaline vs. acid, HCHO vs. hypophosphite, pure Cu vs. Ni-P alloy), and laying them side by side prevents the dangerous assumption that E-Cu operates "like EN but with copper."

---

*Alaina -- Poster #244 -- Construction Workup v1.0 -- 2026-04-26*
