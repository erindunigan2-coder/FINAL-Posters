---
Project: Plating Posters Inc
Poster Number: 230
Title: "Post Treatment -- EN (Mid Phos)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters -- Watson Research Brief (Process 2: EN Mid-P, Poster 8)"
Process Scope: Post-treatment (heat treatment, passivation, ENIG pathway) for EN mid phosphorus line (Stage 7 of 7)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ElectrolessNickel
  - MidPhosphorus
  - PostTreatment
  - HeatTreatment
  - ConstructionWorkup
  - Series2
  - ClusterEN-MP
---

# Poster #230 -- Construction Workup
## Post Treatment -- EN (Mid Phos)

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 7 of 7. Post-treatment for EN Mid-P has three distinct pathways depending on application: (1) HE relief for high-strength steel, (2) heat treatment for maximum hardness, and (3) ENIG -- where there is NO standalone post-treatment because the EN deposit proceeds directly to immersion gold. This is the only EN class where the "post-treatment" is often another plating step rather than a furnace.

For general engineering applications, heat treatment at 350-400 C for 1 hour achieves 850-1000 HV -- lower than Low-P's 1000-1100 HV peak due to the higher phosphorus content. Chromate passivation is an optional addition for corrosion enhancement.

Hero visual: a decision flowchart showing the three post-treatment pathways, with hardness bar chart comparing as-plated vs. heat-treated.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Post-treatment decision flowchart hero (Block B):** Three branches from EN Mid-P deposit: HE Relief, Maximum Hardness HT, and ENIG (no HT). Built with rectangles and connecting lines.
2. **Hardness comparison bar chart (Block D):** Comparing as-plated and heat-treated hardness.
3. **ASTM B733 class table (Block E):** Heat treatment classes.
4. **ENIG pathway callout (Block F):** Prominent panel explaining why no heat treatment for ENIG.
5. **HE relief timing diagram (Block G):** The 4-hour window.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 7 highlighted
ZONE 3 -- POST-TREATMENT DECISION FLOW HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- ASTM B733 CLASSES + HARDNESS COMPARISON (14.5"--21.0" / ~6.5")
ZONE 5 -- HE RELIEF TIMING + ENIG PATHWAY (21.0"--27.5" / ~6.5")
ZONE 6 -- COMMON PROBLEMS + SAFETY (27.5"--32.5" / ~5.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `POST TREATMENT` -- Barlow Condensed ExtraBold, 76 pt, `#F0EDE8`. Y: 0.5".

**Subheading:** `EN (Mid Phos) -- Heat Treatment, Passivation & ENIG Pathway -- Stage 7 of 7` -- 28 pt `#E8A020` (Amber). Y: 1.4".

**Tagline:** `Three paths after Mid-P: furnace for hardness, furnace for hydrogen relief, or straight to gold. The application decides.` -- 20 pt at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 7 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.

Below: `Before: As-plated Ni-P (500-600 HV, mixed crystalline/amorphous)  -->  After: Heat-treated (850-1000 HV) or ENIG gold overlay`

---

### ZONE 3 -- Post-Treatment Decision Flow Hero

**Section label:** `POST-TREATMENT PATHWAYS` -- Y: 4.4".

**BLOCK B -- Decision Flowchart (Y: 5.0" to 14.0")**

**Starting box (top center):**
- Rounded rect, X: 7.0", W: 10.0", H: 1.2", fill `#E8A020`, radius 8
- Text: `EN MID-P DEPOSIT COMPLETE` Barlow Condensed ExtraBold 22 pt `#1A1F2E`

**Decision diamond (Y: 6.8"):**
- Rotated rect (diamond shape), X: 9.0", W: 6.0", H: 1.5", fill `#1E2435`, border 2 pt `#E8A020`
- Text: `APPLICATION?` Barlow SemiBold 16 pt `#E8A020`

**Three branch boxes below:**

**Branch 1 -- ENIG Pathway (X: 0.5", Y: 9.0", W: 7.0", H: 4.5"):**
- Rounded rect fill `#1E2435`, full border 2 pt `#27AE60`
- Title: `ENIG (PCB)` Barlow SemiBold 20 pt `#27AE60`
- `NO HEAT TREATMENT`
- `EN --> Rinse --> Immersion Gold`
- `Heat would oxidize EN surface`
- `Gold cannot deposit on oxidized Ni-P`
- `Per IPC-4552B`
- Badge: `NO FURNACE` fill `#27AE60`, 12 pt `#1A1F2E`

**Branch 2 -- HE Relief (X: 8.0", Y: 9.0", W: 7.5", H: 4.5"):**
- Rounded rect fill `#1E2435`, full border 2 pt `#E05C5C`
- Title: `HE RELIEF` Barlow SemiBold 20 pt `#E05C5C`
- `High-strength steel (>1000 MPa / >40 HRC)`
- `190-210 C (375-410 F)`
- `2-23 hours`
- `WITHIN 4 HOURS OF PLATING`
- `Per ASTM B849 / B850`
- Badge: `MANDATORY -- SAFETY` fill `#E05C5C`, 12 pt `#1A1F2E`

**Branch 3 -- Maximum Hardness (X: 16.0", Y: 9.0", W: 7.5", H: 4.5"):**
- Rounded rect fill `#1E2435`, top accent 4 pt `#E8A020`
- Title: `MAXIMUM HARDNESS` Barlow SemiBold 20 pt `#E8A020`
- `350-400 C (660-750 F), 1 hr`
- `Achieves 850-1000 HV`
- `Ni3P precipitation hardening`
- `General engineering, aerospace hydraulics`
- `Optional: chromate passivation after`

---

### ZONE 4 -- ASTM B733 Classes + Hardness Comparison

**Left -- ASTM B733 Table (X: 0.5", W: 14.0", Y: 14.7" to 20.8"):**

Section label: `ASTM B733 HEAT TREATMENT CLASSES` Y: 14.7".

| Class | Treatment | Temperature | Time | Purpose | Substrate |
|---|---|---|---|---|---|
| Class 1 | As-plated | None | -- | No HT required | General |
| Class 2 | Maximum hardness | 350-400 C (660-750 F) | 1 hr | Precipitate Ni3P; 850-1000 HV | Steel, iron |
| Class 3 | HE relief | 190-210 C (375-410 F) | 2-23 hr | Drive out hydrogen | High-strength steel |
| Class 4 | Adhesion (Al, non-HT) | 120-150 C (250-300 F) | 1-2 hr | Improve adhesion | Aluminum |
| Class 5 | Adhesion (Al, age-hard) | 120-150 C (250-300 F) | 1-2 hr | Improve adhesion | Aluminum |
| Class 6 | Adhesion (Ti) | 300-320 C (570-610 F) | 1-4 hr | Adhesion | Titanium |

Note: `Classes can be combined. Always perform HE relief FIRST.` Inter Medium 13 pt `#E8A020`.

**Right -- Hardness Bar Chart (X: 15.0", W: 8.5", Y: 14.7" to 20.8"):**

Title: `HARDNESS COMPARISON` Barlow SemiBold 18 pt `#F0EDE8`

| Condition | Hardness (HV) | Bar Color |
|---|---|---|
| As-Plated | 500-600 | `#2EC4B6` |
| HE Relief (190-210 C) | 500-550 | `#E8A020` |
| Maximum HT (350-400 C) | 850-1000 | `#27AE60` |
| Low-P HT (reference) | 1000-1100 | `#3A4055` dashed |
| Hard Chrome (reference) | 850-1000 | `#3A4055` dashed |

Bar note: `Mid-P peak hardness (850-1000 HV) matches hard chrome but is lower than Low-P peak (1000-1100 HV) due to higher P content` Inter Regular 12 pt `#F0EDE8` at 70%.

---

### ZONE 5 -- HE Relief Timing + ENIG Pathway Detail

**Left -- HE Relief Timing (X: 0.5", W: 11.0"):**

Title: `HYDROGEN EMBRITTLEMENT RELIEF -- THE 4-HOUR WINDOW` Barlow SemiBold 20 pt `#E05C5C`

- Rounded rect fill `#1E2435`, FULL border 2 pt `#E05C5C`

Visual timeline:
- `PLATING COMPLETE` -> `0-4 hr: BAKE WINDOW` (fill `#27AE60` at 30%) -> `> 4 hr: RISK ZONE` (fill `#E05C5C` at 40%)

Key rules:
- `High-strength steel (> 1000 MPa UTS or > 40 HRC):`
- `Bake at 190-210 C within 4 hours of plating completion`
- `Minimum hold: 4 hours (per ASTM B849)`
- `Extended hold: up to 23 hours for critical aerospace parts`
- `FAILURE TO BAKE = RISK OF CATASTROPHIC DELAYED BRITTLE FRACTURE`

**Right -- ENIG Pathway Detail (X: 12.0", W: 11.5"):**

Title: `ENIG -- WHY NO HEAT TREATMENT?` Barlow SemiBold 18 pt `#27AE60`

- Rounded rect fill `#1E2435`, left accent 0.06" `#27AE60`

Explanation:
- `In ENIG (Electroless Nickel / Immersion Gold per IPC-4552B):`
- `The EN Mid-P deposit (3-8 um) is immediately followed by immersion gold (0.05-0.1 um)`
- `Heat treatment would oxidize the EN surface`
- `Oxidized Ni-P cannot catalyze the gold displacement reaction`
- `Result: no gold deposition; failed ENIG`
- `RULE: After EN rinse, go directly to Au bath -- no delay, no heat`
- `Passivation? NO -- go to Au. The gold IS the final finish.`

---

### ZONE 6 -- Common Problems + Safety

**Left -- Problems (X: 0.5", W: 14.0"):**

| Problem | Cause | Fix |
|---|---|---|
| Hardness not reached | Temp too low or time too short | Verify furnace calibration; hold full 1 hr at 350-400 C |
| Deposit cracking | Over-temperature or ramp too fast | Ramp gradually; do not exceed 400 C |
| Adhesion loss on Al | Exceeded 290 C | Reduce temperature; use adhesion bake only |
| Delayed fracture (HTS) | HE bake skipped or delayed past 4 hr | Always bake within 4 hr -- no exceptions |
| ENIG gold failure | EN surface oxidized before Au | Do not heat treat ENIG parts; go directly to Au |
| Discoloration | Oxidation during heat treatment | Use inert atmosphere (N2 or Ar) for critical parts |

**Right -- Safety (X: 15.0", W: 8.5"):**
- Title: `FURNACE SAFETY` `#E8A020`
- `Furnace operates at 190-400 C -- severe burn hazard`
- `Use heat-resistant gloves for part handling`
- `Ensure furnace ventilation -- hydrogen gas released during bake`
- `Do not open furnace door rapidly -- thermal shock risk`
- `Inert atmosphere furnaces: asphyxiation hazard -- ventilate`

---

### ZONE 7 -- Footer

Standard. Title: `Post Treatment -- EN (Mid Phos)`. Version `v1.0 -- 2026`.

Disclaimer: `Heat treatment specifications per ASTM B733, ASTM B849, ASTM B850, AMS 2404/2405. ENIG process per IPC-4552B. Always verify requirements against the applicable drawing or purchase order specification.`

---

## Parts 5-7

**Grouping:** 7 zones.
**Light Remap:** Standard table. HE border (#E05C5C -> #B83E3E). ENIG border (#27AE60 -> #1E7A47).
**Export:** Six files -- `Post Treatment EN Mid-P -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The three-pathway decision flow is the structural differentiator from the Low-P Post Treatment poster (#222). Low-P has essentially two paths (HE relief and hardness HT). Mid-P adds the ENIG pathway, which is arguably the most commercially important: ENIG is one of the highest-volume EN applications in the world. The decision flowchart should make it visually clear that ENIG parts never enter a furnace.

The hardness comparison bar chart deliberately includes Low-P and hard chrome as reference lines to provide context. Mid-P at 850-1000 HV matches hard chrome but falls short of Low-P's 1000-1100 HV peak -- a direct consequence of the higher phosphorus content inhibiting Ni3P crystallization at the same degree.

---

*Alaina -- Poster #230 -- Construction Workup v1.0 -- 2026-04-26*
