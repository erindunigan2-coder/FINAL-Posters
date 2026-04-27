---
Project: Plating Posters Inc
Poster Number: 405
Title: "Parameter Setup -- PVD"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 1: PVD, Sections 1.2, 1.5)"
Technical Source: PVD parameter setup including ion etching (pre-deposition), substrate bias, gas ratios, power settings, temperature control, and recipe structure for TiN and TiAlN.
Process Scope: PVD parameter setup including ion etch (Stage 5 of 10)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - PVD
  - Parameters
  - IonEtch
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #405 -- Construction Workup
## Parameter Setup -- PVD

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 5 of 10. After pump-down, the first active step is ion etching -- high-bias Ar+ bombardment to strip surface oxides and activate the substrate. Then the deposition parameters are set: target power, reactive gas flow, substrate bias, temperature, and rotation speed. This poster covers both ion etching and deposition recipe setup with two representative recipes (TiN by arc, TiAlN by sputtering).

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Ion etch parameter panel (Block B):** Detailed parameters for the ion etching step.
2. **Recipe comparison -- TiN vs. TiAlN (Block C -- HERO):** Side-by-side recipe cards for two representative coatings.
3. **Parameter interaction matrix (Block D):** How key parameters affect coating properties.
4. **Substrate bias guide (Block E):** Visual showing bias voltage effects on film properties.
5. **Gas ratio control (Block F):** Reactive gas management.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 10.5" / 21.0" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 5 highlighted (Amber -- parameters)
ZONE 3 -- ION ETCH PARAMETERS (4.2"--10.5" / ~6.3")
ZONE 4 -- RECIPE COMPARISON / HERO (10.5"--21.0" / ~10.5")
ZONE 5 -- PARAMETER EFFECTS + BIAS GUIDE (21.0"--27.0" / ~6.0")
ZONE 6 -- GAS RATIO CONTROL + TIPS (27.0"--32.5" / ~5.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `PARAMETER SETUP` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `PVD -- Stage 5 of 10 -- Ion Etch, Power, Gas, Bias, Temperature` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `The recipe defines the coating. Ion etch for adhesion, reactive gas for composition, bias for density, temperature for structure. Every parameter matters.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 5 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Chamber at base vacuum (Stage 4) --> After: Ion etch complete, deposition recipe loaded and running`

---

### ZONE 3 -- Ion Etch Parameters

**Section label:** `ION ETCHING -- THE ADHESION FOUNDATION` -- Y: 4.4".

**BLOCK B -- Ion Etch Panel (Y: 5.0" to 10.3")**

Two-column layout:

**Left -- Argon Ion Etch (standard) (X: 0.5", W: 11.0"):**
- Rounded rect H: 5.0", fill `#1E2435`, left accent `#E8A020`
- Title: `ARGON ION ETCH` Barlow SemiBold 20 pt `#E8A020`
- Subtitle: `Standard for sputtering systems` Inter Regular 14 pt `#F0EDE8` at 60%

| Parameter | Value |
|---|---|
| Gas | Ar (argon) |
| Pressure | 1-5 mTorr |
| Substrate bias | -800 to -1200 V DC |
| Duration | 5-30 min |
| Temperature rise | ~100-200 C (substrate heating from bombardment) |
| Purpose | Remove native oxide; activate surface for adhesion |

JetBrains Mono 14 pt `#F0EDE8`. Labels: Inter Medium 13 pt `#F0EDE8` at 60%.

**Right -- Metal Ion Etch (arc systems) (X: 12.0", W: 11.5"):**
- Rounded rect H: 5.0", fill `#1E2435`, left accent `#2EC4B6`
- Title: `METAL ION ETCH (Ti/Cr)` Barlow SemiBold 20 pt `#2EC4B6`
- Subtitle: `Arc systems only -- creates implantation zone` Inter Regular 14 pt `#F0EDE8` at 60%

| Parameter | Value |
|---|---|
| Source | Ti or Cr arc cathode |
| Substrate bias | -800 to -1200 V DC |
| Arc current | 60-80 A |
| Duration | 2-10 min |
| Effect | Shallow metal implantation into substrate surface |
| Benefit | Superior adhesion vs. Ar etch alone |

Bottom callout (full width):
- `Ion etching at -800 to -1200 V creates a graded interface between substrate and coating -- the key to PVD adhesion.` Inter Medium 15 pt `#E8A020`

---

### ZONE 4 -- Recipe Comparison (HERO)

**Section label:** `TWO REPRESENTATIVE RECIPES -- TiN (ARC) VS. TiAlN (SPUTTERING)` -- Y: 10.7".

**BLOCK C -- Side-by-Side Recipe Cards (Y: 11.3" to 20.8")**

**Left -- TiN by Cathodic Arc (X: 0.5", W: 11.0"):**
- Rounded rect H: 9.2", fill `#1E2435`, left accent `#E8A020`
- Title: `TiN -- CATHODIC ARC` Barlow SemiBold 22 pt `#E8A020`
- Subtitle: `Gold-colored nitride -- the classic PVD hard coating` Inter Regular 14 pt `#F0EDE8` at 60%
- Color swatch: small rect 0.5" x 0.5", fill `#C8A020` (approximate gold)

Recipe table:

| Parameter | Value |
|---|---|
| Target | Pure Ti (99.5%+) |
| Base pressure | < 5 x 10^-5 Torr |
| N2 flow | 100-300 sccm |
| Arc current | 60-80 A per cathode |
| Substrate bias (dep) | -50 to -150 V DC |
| Substrate temp | 350-450 C |
| Deposition rate | 2-6 um/hr |
| Working pressure | 5-50 mTorr |
| Rotation | 3-10 rpm |
| Typical thickness | 1-5 um (tooling) |
| Total cycle time | 3-8 hr (all phases) |

Properties callout:
- `Hardness: 2000-2500 HV` JetBrains Mono 14 pt `#E8A020`
- `Max service temp: 600 C`
- `Friction coeff: 0.4-0.6`
- `Applications: drills, end mills, inserts, decorative hardware`

**Right -- TiAlN by Magnetron Sputtering (X: 12.0", W: 11.5"):**
- Rounded rect H: 9.2", fill `#1E2435`, left accent `#2EC4B6`
- Title: `TiAlN -- MAGNETRON SPUTTERING` Barlow SemiBold 22 pt `#2EC4B6`
- Subtitle: `Violet-gray -- high-temperature performance champion` Inter Regular 14 pt `#F0EDE8` at 60%
- Color swatch: small rect 0.5" x 0.5", fill `#7A6A8A` (approximate violet-gray)

| Parameter | Value |
|---|---|
| Target | TiAl alloy (50:50 or 33:67 at%) |
| Base pressure | < 5 x 10^-5 Torr |
| Ar:N2 ratio | 1:1 to 1:3 |
| Power density | 10-30 W/cm2 |
| Substrate bias (dep) | -80 to -150 V |
| Substrate temp | 300-500 C |
| Deposition rate | 0.5-2 um/hr |
| Working pressure | 2-5 mTorr |
| Rotation | 3-10 rpm |
| Typical thickness | 1-5 um |
| Total cycle time | 4-10 hr |

Properties callout:
- `Hardness: 2800-3200 HV` JetBrains Mono 14 pt `#2EC4B6`
- `Max service temp: 800 C`
- `Friction coeff: 0.3-0.5`
- `Applications: high-speed dry machining, aerospace tooling`

---

### ZONE 5 -- Parameter Effects + Bias Guide

**Section label:** `HOW PARAMETERS AFFECT THE COATING` -- Y: 21.2".

**BLOCK D -- Parameter Matrix (Y: 21.8" to 26.8")**

| Parameter | Increase Effect | Decrease Effect | Typical Range |
|---|---|---|---|
| Substrate bias | Denser, harder film; higher stress | Porous, softer film; lower stress | -50 to -300 V |
| Reactive gas (N2) | More complete nitride; risk of target poisoning | Metal-rich film; reduced hardness | Ar:N2 1:1 to 1:3 |
| Substrate temp | Better crystallinity; higher adhesion | Amorphous film; lower adhesion | 200-500 C |
| Power/current | Higher deposition rate; more macroparticles (arc) | Lower rate; fewer defects | System dependent |
| Working pressure | More collisions; lower film density | Fewer collisions; more energetic bombardment | 1-10 mTorr |

Header: Barlow SemiBold 13 pt, fill `#3A4055`. Data: Inter Regular 12 pt. Range: JetBrains Mono 12 pt `#E8A020`.

Bottom callout:
- `Every PVD recipe is a balance of rate, quality, and stress. Changing one parameter shifts the balance -- always verify with test coupons.` Inter Medium 14 pt `#E8A020`

---

### ZONE 6 -- Gas Ratio Control + Tips

**Section label:** `REACTIVE GAS MANAGEMENT` -- Y: 27.2".

**BLOCK F -- Two-Column (Y: 27.7" to 32.3")**

**Left -- Gas Ratio Rules (X: 0.5", W: 11.0"):**
- Rounded rect H: 4.4", fill `#1E2435`, left accent `#27AE60`

Rules:
- `Ar is always the sputtering/plasma gas -- never deposit without Ar`
- `N2 creates nitrides (TiN, CrN, TiAlN)`
- `O2 creates oxides (Al2O3) -- very reactive, use low flow`
- `C2H2 creates carbides or DLC -- flammable, purge lines`
- `MFC calibration is critical -- 5% flow error changes film composition`

**Right -- Operator Tips (X: 12.0", W: 11.5"):**
- Rounded rect H: 4.4", fill `#1E2435`, left accent `#2EC4B6`

Tips:
- `Log every recipe run with gas flows, pressures, and bias`
- `Run test coupons with every production batch`
- `Monitor target voltage during deposition -- drift = target erosion or poisoning`
- `Replace targets at 40-60% erosion depth -- don't run to failure`
- `Color is your first diagnostic -- wrong color = wrong recipe`

---

### ZONE 7 -- Footer

Standard footer. Title: `Parameter Setup -- PVD`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Parameter Setup PVD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is one of the most technical posters in the PVD cluster. The two-recipe comparison (TiN arc vs. TiAlN sputtering) is the hero because it shows operators the concrete differences between the two dominant PVD methods with actual numbers. The parameter effects matrix helps operators understand cause and effect -- essential for troubleshooting. The ion etch section is separated because it is a distinct pre-deposition step that directly controls adhesion.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #405 -- Construction Workup v1.0*
*2026-04-26*
