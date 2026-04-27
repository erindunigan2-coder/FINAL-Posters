---
Project: Plating Posters Inc
Poster Number: 238
Title: "Post Treatment -- EN (High Phos)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Electroless Clusters — Watson Research Brief (Process 3: EN High-P)"
Technical Source: Post-treatment options for EN High-P deposits including hydrogen embrittlement relief, hardness heat treatment, passivation, and critical limitations for non-magnetic and maximum-corrosion applications. ASTM B733, ASTM B849, ASTM B850. No brand names.
Process Scope: Post-treatment stage for electroless nickel high-phosphorus process (Stage 7-8 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ElectrolessNickel
  - HighPhosphorus
  - PostTreatment
  - ConstructionWorkup
  - Series2
  - ClusterEN03
---

# Poster #238 -- Construction Workup
## Post Treatment -- EN (High Phos)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 7-8 of 8. Post-treatment for EN High-P is where the application defines the path. For oil/gas downhole tools requiring non-magnetic properties: do NOT heat treat above 260 C or the amorphous structure crystallizes and becomes magnetic. For maximum corrosion applications: do NOT heat treat at all -- the as-plated amorphous state has the best corrosion resistance. For high-strength steel substrates: hydrogen embrittlement relief at 190-210 C is MANDATORY within 4 hours of plating. These rules are critical and contradictory enough that they deserve prominent visual treatment.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Decision tree hero (Block B):** "What is your application?" branching to different post-treatment paths.
2. **Heat treatment matrix (Block D):** Temperature/time chart for different objectives (ASTM B733 classes).
3. **The 260 C warning (Block E):** Critical temperature above which amorphous structure crystallizes.
4. **Hydrogen embrittlement relief detail (Block F):** Time-critical bake requirements.

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
  Stages 7-8 highlighted (Amber)
ZONE 3 -- APPLICATION DECISION TREE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- HEAT TREATMENT MATRIX (14.5"--20.5" / ~6.0")
ZONE 5 -- THE 260 C CRYSTALLIZATION WARNING (20.5"--26.5" / ~6.0")
ZONE 6 -- HYDROGEN EMBRITTLEMENT RELIEF (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `POST TREATMENT` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `EN (High Phos) -- Stages 7-8 of 8` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `The application defines the path. Non-magnetic? Do not heat treat. Maximum corrosion? Do not heat treat. High-strength steel? You MUST heat treat.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stages 7-8 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Freshly plated EN High-P deposit  -->  After: Application-ready deposit (baked, passivated, or as-plated)`

---

### ZONE 3 -- Application Decision Tree Hero

**Section label:** `WHAT IS YOUR APPLICATION? -- THE PATH SPLITS HERE` -- Y: 4.4".

**BLOCK B -- Decision Tree**

Y: 5.0" to 14.0".

**Root node (top center):**
- Rounded rect, X: 7.0", Y: 5.0", W: 10.0", H: 1.2", fill `#E8A020` at 30%, border 2 pt `#E8A020`
- Text: `WHAT DOES YOUR APPLICATION REQUIRE?` Barlow Condensed ExtraBold 20 pt `#E8A020`

**Three branch nodes (Y: 7.0"):**

| Branch | X | W | Accent | Application | Post-Treatment |
|---|---|---|---|---|---|
| Left | 0.5" | 7.33" | `#27AE60` | MAXIMUM CORROSION | Do NOT heat treat. As-plated amorphous state = best corrosion. Optional: trivalent chromate passivation. |
| Center | 8.17" | 7.33" | `#2EC4B6` | NON-MAGNETIC (MWD) | Do NOT heat treat above 260 C. HE relief at 190-210 C is safe. Verify P% >= 10.5% and ASTM F2088. |
| Right | 15.83" | 7.67" | `#E8A020` | MAXIMUM HARDNESS | Heat treat at 350-400 C for 1 hr. Achieves 800-900 HV. WARNING: destroys amorphous structure + non-magnetic property. |

Each branch: Rounded rect, H: 6.5", fill `#1E2435`, left accent 0.06".

**Inside each branch:**

*Maximum Corrosion:*
- Badge: `LEAVE IT ALONE` fill `#27AE60`
- `DO NOT HEAT TREAT` Barlow SemiBold 18 pt `#27AE60`
- `As-plated amorphous structure = zero grain boundaries` Inter Regular 13 pt `#F0EDE8`
- `Corrosion attacks grain boundaries. No boundaries = no attack path.` Inter Regular 13 pt `#F0EDE8`
- `Salt spray: 1,000+ hours at 25 um` JetBrains Mono 14 pt `#27AE60`
- `Chemical resistance: HCl, H2SO4, acetic, phosphoric` Inter Regular 12 pt `#F0EDE8`
- `Optional: trivalent chromate passivation for enhanced corrosion` Inter Medium 12 pt `#E8A020`
- `Applications: chemical processing, offshore, pipeline, food processing` Inter Regular 11 pt `#F0EDE8` at 70%

*Non-Magnetic (MWD):*
- Badge: `TEMPERATURE LIMIT: 260 C` fill `#2EC4B6`
- `HE RELIEF: 190--210 C, 2--23 hr` JetBrains Mono 14 pt `#2EC4B6`
- `This is BELOW crystallization temperature -- SAFE` Inter Medium 13 pt `#27AE60`
- `DO NOT EXCEED 260 C (500 F)` Inter Medium 14 pt `#E05C5C`
- `Above 260 C: amorphous --> crystalline --> MAGNETIC` Inter Regular 13 pt `#E05C5C`
- `Verify: P% >= 10.5% by XRF or ICP` JetBrains Mono 12 pt `#F0EDE8`
- `Verify: non-magnetic per ASTM F2088` JetBrains Mono 12 pt `#F0EDE8`
- `Applications: MWD tools, downhole surveys, MRI-compatible` Inter Regular 11 pt `#F0EDE8` at 70%

*Maximum Hardness:*
- Badge: `350-400 C / 1 HOUR` fill `#E8A020`
- `As-plated: 450--550 HV` JetBrains Mono 14 pt `#F0EDE8`
- `After HT: 800--900 HV` JetBrains Mono 14 pt `#E8A020`
- `Ni3P phase precipitates in nickel matrix` Inter Regular 13 pt `#F0EDE8`
- `WARNING: Crystallization DESTROYS:` Inter Medium 13 pt `#E05C5C`
- `  -- Non-magnetic property (deposit becomes magnetic)` Inter Regular 12 pt `#E05C5C`
- `  -- Corrosion resistance (grain boundaries reappear)` Inter Regular 12 pt `#E05C5C`
- `Use only when hardness is the primary requirement` Inter Medium 12 pt `#E8A020`
- `Applications: wear surfaces, valves, pump components` Inter Regular 11 pt `#F0EDE8` at 70%

---

### ZONE 4 -- Heat Treatment Matrix

**Section label:** `ASTM B733 HEAT TREATMENT CLASSES` -- Y: 14.7".

**BLOCK D -- Heat Treatment Table (Y: 15.3" to 20.3")**

Column widths: Class (2.5") | Purpose (5.0") | Temp (3.5") | Time (3.0") | Notes (9.0")

| Class | Purpose | Temperature | Time | Notes |
|---|---|---|---|---|
| Class 1 | As-plated (no HT) | -- | -- | Maximum corrosion resistance; amorphous preserved |
| Class 2 | Maximum hardness | 350-400 C (660-750 F) | 1 hr | Crystallizes deposit; 800-900 HV; destroys non-magnetic |
| Class 3 | HE relief | 190-210 C (375-410 F) | 2-23 hr | Mandatory for high-strength steel; within 4 hr of plating |
| Class 4-5 | Adhesion (Al) | 120-150 C (250-300 F) | 1-2 hr | Improves adhesion on age-hardened aluminum |
| Class 6 | Adhesion (Ti) | 300-320 C (570-610 F) | 1-4 hr | Titanium alloys; above 260 C crystallization threshold |

Data: JetBrains Mono Regular, 12 pt. Notes column: Inter Regular 12 pt.

**Warning bar below table:**
- `Aluminum substrates: do not exceed 290 C (554 F) -- differential thermal expansion causes delamination` Inter Medium 13 pt `#E05C5C`

---

### ZONE 5 -- The 260 C Crystallization Warning

**Section label:** `THE CRYSTALLIZATION THRESHOLD -- 260 C` -- Y: 20.7".

**BLOCK E -- Temperature Scale Visual (Y: 21.3" to 26.3")**

**Large horizontal temperature bar (W: 22.0", H: 1.0"):**
- `25 C (as-plated)` to `400 C`
- Green zone: 25-260 C -- `AMORPHOUS: Non-magnetic, maximum corrosion resistance`
- Red transition zone: 260-320 C -- `CRYSTALLIZATION BEGINS: Ni3P phase precipitates`
- Amber zone: 320-400 C -- `FULLY CRYSTALLINE: Maximum hardness but magnetic + reduced corrosion`

**Critical marker at 260 C:**
- Triangle marker, `#E05C5C`
- Label: `260 C (500 F) -- THE LINE YOU MUST NOT CROSS FOR NON-MAGNETIC APPLICATIONS` Barlow SemiBold 14 pt `#E05C5C`

**Below the bar -- two-column callout:**

Left (X: 0.5", W: 11.0"):
- `BELOW 260 C` Barlow SemiBold 20 pt `#27AE60`
- `Structure: Fully amorphous (metallic glass)` Inter Regular 14 pt `#F0EDE8`
- `Magnetic: Non-magnetic (paramagnetic)` Inter Regular 14 pt `#F0EDE8`
- `Corrosion: Maximum (no grain boundaries)` Inter Regular 14 pt `#F0EDE8`
- `Hardness: 450-550 HV (as-plated)` JetBrains Mono 13 pt `#F0EDE8`

Right (X: 12.0", W: 11.5"):
- `ABOVE 260 C` Barlow SemiBold 20 pt `#E05C5C`
- `Structure: Crystalline (Ni3P precipitates)` Inter Regular 14 pt `#F0EDE8`
- `Magnetic: MAGNETIC (ferromagnetic)` Inter Regular 14 pt `#E05C5C`
- `Corrosion: Reduced (grain boundaries reform)` Inter Regular 14 pt `#F0EDE8`
- `Hardness: 800-900 HV (heat treated)` JetBrains Mono 13 pt `#F0EDE8`

---

### ZONE 6 -- Hydrogen Embrittlement Relief

**Section label:** `HYDROGEN EMBRITTLEMENT RELIEF -- THE NON-NEGOTIABLE BAKE` -- Y: 26.7".

**BLOCK F -- HE Relief Detail (Y: 27.3" to 32.3")**

**Main callout (X: 0.5", W: 15.0"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E05C5C`
- Title: `MANDATORY FOR HIGH-STRENGTH STEEL` Barlow SemiBold 20 pt `#E05C5C`

Parameters (JetBrains Mono 16 pt `#F0EDE8`):
- `Temperature: 190--210 C (375--410 F)`
- `Time: Minimum 4 hours (ASTM B849/B850)`
- `Extended: 2--23 hours per specification`
- `WITHIN 4 HOURS OF PLATING COMPLETION` JetBrains Mono 14 pt `#E05C5C`

**Substrate threshold:**
- `Applies when: UTS > 1000 MPa OR hardness > 40 HRC` Inter Medium 14 pt `#E8A020`
- `Per: ASTM B849 / ASTM B850 / AMS 2759/9` JetBrains Mono 12 pt `#F0EDE8` at 70%

**Side callout (X: 16.0", W: 7.5"):**
- Rounded rect, H: 4.8", fill `#E05C5C` at 15%, border 2 pt `#E05C5C`
- Title: `WHY THIS MATTERS` Barlow SemiBold 16 pt `#E05C5C`
- `Hydrogen absorbed during cleaning and plating sits in the steel lattice.` Inter Regular 13 pt `#F0EDE8`
- `Under tensile stress, hydrogen migrates to stress concentrators.` Inter Regular 13 pt `#F0EDE8`
- `Result: delayed brittle fracture -- catastrophic, without warning.` Inter Medium 13 pt `#E05C5C`
- `Baking drives hydrogen out of the lattice before it can cause damage.` Inter Regular 13 pt `#F0EDE8`
- `190-210 C is safely below the 260 C crystallization threshold.` Inter Medium 12 pt `#27AE60`

---

### ZONE 7 -- Footer

Standard. Title: `Post Treatment -- EN (High Phos)`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Heat treatment parameters shown are per ASTM B733, B849, and B850. Specific requirements vary by application specification and customer drawing. Always verify post-treatment requirements with the applicable engineering specification. Source: ASTM B733; ASTM B849; ASTM B850; AMS 2404; Nickel Plating Handbook.`

---

## Parts 5-7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Post Treatment EN High-P -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is one of the most consequential posters in the entire series. The three post-treatment paths are mutually exclusive and the wrong choice can be catastrophic: heat treating a non-magnetic MWD tool above 260 C destroys the non-magnetic property that makes the tool functional; failing to HE-bake high-strength steel can cause a delayed fracture that kills someone. The temperature scale visual with the 260 C crystallization threshold is the hero element -- it needs to be the thing an operator remembers when they are programming an oven.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #238 -- Construction Workup v1.0*
*2026-04-26*
