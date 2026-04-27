---
Project: Plating Posters Inc
Poster Number: 593
Title: "Gas Nitriding -- Cooling (No Quench)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 4: Gas Nitriding, Section 4.8)"
Technical Source: Gas nitriding has NO quench. This poster explains why -- no phase transformation occurs, hardness is from nitride precipitates, not martensite. Parts are furnace cooled under ammonia to 300 F then air cooled. This is a fundamental departure from carburizing, induction, and flame hardening.
Process Scope: Gas nitriding -- cooling / no quench (Stage 8 deep-dive)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - GasNitriding
  - Cooling
  - NoQuench
  - ConstructionWorkup
  - DiffusionHeatTreatment
---

# Poster #593 -- Construction Workup
## Gas Nitriding -- Cooling (No Quench)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This poster makes one thing absolutely clear: GAS NITRIDING HAS NO QUENCH. This is the single most important distinction between nitriding and every other surface hardening process in this series. Parts are furnace cooled slowly under ammonia atmosphere, then air cooled. No oil, no water, no polymer, no gas quench. Zero.

Design philosophy: massive hero statement "NO QUENCH" dominates the top half. Below it, the scientific explanation of why quenching is unnecessary (precipitation hardening vs. transformation hardening), the actual cooling procedure, distortion comparison against quench-based processes, and a "what if you quenched anyway?" troubleshooting note.

---

## Part 1 -- Workflow Orientation

### Design Capabilities for This Poster

- Text boxes with precise font, size, weight, color, and spacing control
- Solid-color rectangles and rounded rectangles for panels, table rows, and accent borders
- Color fills set to exact hex values
- Background page color set to exact hex
- Export at print-quality PDF (300 DPI equivalent via print export)

### Limitations to Flag

1. **"NO QUENCH" hero statement (Block B):** Massive typographic statement.
2. **Scientific explanation (Block C):** Why quenching is unnecessary.
3. **Cooling procedure (Block D):** Step-by-step cooling sequence.
4. **Distortion comparison table (Block E).**
5. **Standard formatting: accents, color remap, JetBrains Mono, 24x36".**

---

## Part 2 -- Document Setup Instructions

Standard setup per Poster #586: 24x36", `#1A1F2E` background, four-font stack, series color palette.

### Step 5 -- Set ruler guides
Standard margins. Zone boundaries: 2.9", 13.5", 20.0", 27.0", 32.5".

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- NO QUENCH HERO + EXPLANATION (2.9"--13.5" / ~10.6" tall)
  Block B: "NO QUENCH" typographic hero
  Block C: Scientific explanation panels

ZONE 3 -- COOLING PROCEDURE (13.5"--20.0" / ~6.5" tall)
  Block D: Step-by-step cooling sequence

ZONE 4 -- DISTORTION COMPARISON (20.0"--27.0" / ~7.0" tall)
  Block E: Nitriding vs. quench-based processes distortion comparison

ZONE 5 -- FAQ / WHAT-IF (27.0"--32.5" / ~5.5" tall)
  Block F: Common questions about nitriding cooling

ZONE 6 -- FOOTER BAND (32.5"--36.0" / ~3.5" tall)
  Block G: Disclaimer + poster title + series name + logo placeholder + version
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**BLOCK A -- Headline**
- Barlow Condensed ExtraBold, 88 pt, `#F0EDE8`, letter spacing -4
- Text: `GAS NITRIDING`

**BLOCK A -- Subheading**
- Barlow SemiBold, 36 pt, `#2EC4B6` (Teal)
- Text: `Cooling -- No Quench Required. No Quench Permitted. No Quench Needed.`

**BLOCK A -- Tagline**
- Barlow SemiBold, 20 pt, `#F0EDE8` at 65%
- Text: `The entire gas nitriding process occurs below the lower critical temperature. No austenite forms. No martensite is needed. Furnace cool and walk away.`

---

### ZONE 2 -- No Quench Hero + Explanation

**Dimensions:** Y: 2.9" to 13.5" (~10.6" tall).

---

**BLOCK B -- "NO QUENCH" Typographic Hero**

Y: 3.2" to 7.0".

- Full-width text box, X: 0.5", W: 23.0"
- Font: Barlow Condensed ExtraBold
- Size: 140 pt
- Color: `#E8A020` (Amber)
- Letter spacing: -6
- Text alignment: Center
- Text: `NO QUENCH`

Below, smaller:
- Font: Barlow SemiBold, 32 pt, `#F0EDE8` at 60%
- Text alignment: Center
- Text: `Furnace Cool Under Ammonia to 300 F -- Then Air Cool to Ambient`

---

**BLOCK C -- Explanation Panels**

Y: 7.5" to 13.3". Two side-by-side panels.

**Left -- Why No Quench (X: 0.5", W: 11.0"):**
- Rounded rect, H: 5.6", fill `#1E2435`, radius 8
- Left accent: 4 pt `#27AE60`
- Title: `WHY NO QUENCH IS NEEDED` -- Barlow SemiBold, 22 pt, `#27AE60`

Content (Inter Regular, 14 pt, `#F0EDE8`, line height 170%):
```
Gas nitriding operates at 925--1050 F
-- entirely below the lower critical
temperature (Ac1 ~ 1333 F / 723 C).

At these temperatures:
- Steel remains FERRITIC (not austenitic)
- No phase transformation occurs
- No austenite exists to transform

Hardness comes from nitride PRECIPITATES:
- Al, Cr, Mo, V react with nitrogen
- Fine, coherent precipitates form
  IN the ferrite lattice during the hold
- Precipitates are stable on cooling
- They do not require quenching to exist

This is PRECIPITATION hardening.
Not TRANSFORMATION hardening.
```

**Right -- What Quenching Would Do (X: 12.5", W: 11.0"):**
- Rounded rect, H: 5.6", fill `#1E2435`, radius 8
- Left accent: 4 pt `#E05C5C`
- Title: `WHAT IF YOU QUENCHED ANYWAY?` -- Barlow SemiBold, 22 pt, `#E05C5C`

Content (Inter Regular, 14 pt, `#F0EDE8`, line height 170%):
```
Quenching a nitrided part would:

1. Provide ZERO additional hardness
   (no austenite to transform)

2. Cause THERMAL SHOCK -- sudden
   cooling from 925--1050 F creates
   thermal gradients and stress

3. Risk CRACKING -- especially at
   case/core transition zone

4. Risk DISTORTION -- the very thing
   nitriding is chosen to avoid

5. Waste time and money

Bottom line:
If you quench a nitrided part,
you have achieved nothing good
and risked everything nitriding
was selected to protect.
```

---

### ZONE 3 -- Cooling Procedure

**Dimensions:** Y: 13.5" to 20.0" (~6.5" tall).

---

**Section label:**
- Centered. Y: 13.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`
- Text: `COOLING PROCEDURE -- STEP BY STEP`

---

**BLOCK D -- Cooling Steps**

Y: 14.4" to 19.8". Four step cards in a row. Gap: 0.33".

Each card: Rounded rect, W: 5.5", H: 5.2", fill `#1E2435`, radius 8, top accent 4 pt.

*Card 1 (X: 0.5"):*
- Top accent: `#E8A020`
- Badge: `STEP 1` on `#E8A020`
- Title: `MAINTAIN ATMOSPHERE` -- Barlow SemiBold, 17 pt, `#E8A020`
- Content: `Keep ammonia flowing during cool-down. NH3 atmosphere prevents oxidation of the nitrided surface. Parts remain bright and clean.` -- Inter Regular, 13 pt, `#F0EDE8`
- Key data: `NH3 flow ON until 300 F` -- JetBrains Mono, 12 pt, `#E8A020`

*Card 2 (X: 6.33"):*
- Top accent: `#2EC4B6`
- Badge: `STEP 2` on `#2EC4B6`
- Title: `FURNACE COOL` -- Barlow SemiBold, 17 pt, `#2EC4B6`
- Content: `Allow furnace to cool naturally with parts inside. Do not open furnace door. Cooling rate is determined by furnace thermal mass -- typically 4-8 hours to reach 300 F.` -- Inter Regular, 13 pt, `#F0EDE8`
- Key data: `Cool to 300 F (149 C)` -- JetBrains Mono, 12 pt, `#2EC4B6`

*Card 3 (X: 12.16"):*
- Top accent: `#2EC4B6`
- Badge: `STEP 3` on `#2EC4B6`
- Title: `STOP NH3 / OPEN FURNACE` -- Barlow SemiBold, 17 pt, `#2EC4B6`
- Content: `At 300 F, shut off ammonia supply. Verify burn-off pilot consumes remaining H2. Open furnace for air cooling. Parts are safe to handle with standard thermal PPE.` -- Inter Regular, 13 pt, `#F0EDE8`
- Key data: `Burn-off pilot stays lit until purged` -- JetBrains Mono, 12 pt, `#E05C5C`

*Card 4 (X: 18.0"):*
- Top accent: `#27AE60`
- Badge: `STEP 4` on `#27AE60`
- Title: `AIR COOL TO AMBIENT` -- Barlow SemiBold, 17 pt, `#27AE60`
- Content: `Parts air cool from 300 F to ambient temperature. 1-2 hours depending on part mass. No forced air or water cooling needed. Parts are ready for inspection.` -- Inter Regular, 13 pt, `#F0EDE8`
- Key data: `Proceed to inspection` -- JetBrains Mono, 12 pt, `#27AE60`

---

### ZONE 4 -- Distortion Comparison

**Dimensions:** Y: 20.0" to 27.0" (~7.0" tall).

---

**Section label:**
- Centered. Y: 20.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`
- Text: `DISTORTION COMPARISON -- NITRIDING VS. QUENCH-BASED PROCESSES`

---

**BLOCK E -- Comparison Table**

Y: 20.9" to 26.8". Column widths (23.0" total):
- Process (4.5") | Quench Type (4.0") | Typical Distortion (5.0") | Distortion Cause (9.5")

Header row: `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.7".

| Process | Quench Type | Typical Distortion | Distortion Cause |
|---|---|---|---|
| Gas Nitriding | NONE (furnace cool) | Near zero (< 0.0005 in) | Thermal gradient during ramp only |
| Plasma Nitriding | NONE (vacuum cool) | Near zero | Same as gas nitriding |
| Gas Carburizing | Oil quench (fast) | 0.002--0.010+ in | Phase transformation + thermal shock |
| Vacuum Carburizing | Gas quench (moderate) | 0.001--0.005 in | Phase transformation (less thermal shock) |
| Induction Hardening | Spray quench (fast) | 0.001--0.005 in | Localized transformation + thermal gradient |
| Carbonitriding | Oil quench (fast) | 0.001--0.008 in | Phase transformation + thermal shock |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Gas Nitriding row: highlight `#27AE60` background at 10%.

Note below table (Inter Medium, 14 pt, `#27AE60`):
```
Gas nitriding is chosen specifically BECAUSE of near-zero distortion.
When tight tolerances are non-negotiable and post-process grinding
is unacceptable, nitriding is the answer.
```

---

### ZONE 5 -- FAQ / What-If

**Dimensions:** Y: 27.0" to 32.5" (~5.5" tall).

---

**Section label:**
- Centered. Y: 27.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`
- Text: `FREQUENTLY ASKED QUESTIONS`

---

**BLOCK F -- Three FAQ Cards**

Y: 27.9" to 32.3". Three cards in a row. Gap: 0.35".

Each card: Rounded rect, W: 7.3", H: 4.2", fill `#1E2435`, radius 8, top accent 4 pt `#2EC4B6`.

*Card 1 (X: 0.5"):*
- Question: `Does the part need tempering after nitriding?` -- Barlow SemiBold, 16 pt, `#2EC4B6`
- Answer: `NO. The nitriding hold itself is essentially a long, low-temperature soak. No quench stress exists to relieve. The core retains its pre-nitriding Q&T hardness unchanged.` -- Inter Regular, 13 pt, `#F0EDE8`

*Card 2 (X: 8.2"):*
- Question: `Can I speed up cooling with forced air or water?` -- Barlow SemiBold, 16 pt, `#2EC4B6`
- Answer: `Not recommended. Rapid cooling risks thermal shock and surface cracking on the hard, brittle nitrided case. Furnace cool under NH3 is standard. Patience is part of the process.` -- Inter Regular, 13 pt, `#F0EDE8`

*Card 3 (X: 15.9"):*
- Question: `What about sub-zero treatment after nitriding?` -- Barlow SemiBold, 16 pt, `#2EC4B6`
- Answer: `Not applicable. Sub-zero treatment converts retained austenite to martensite. Gas nitriding operates in the ferritic range -- no austenite exists to convert. Sub-zero is a carburizing tool, not a nitriding tool.` -- Inter Regular, 13 pt, `#F0EDE8`

---

### ZONE 6 -- Footer Band

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Cooling procedures shown are standard for gas nitriding per AMS 2759/6D. Specific cooling requirements may vary by specification and part geometry. Consult your process engineer and applicable standards.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"
> Gas Nitriding -- Cooling (No Quench)

**Series name:** Inter Regular, 14 pt, `#F0EDE8` at 70%, Center. Y: 34.2"
> Plating Posters Inc -- Metal Finishing Reference Series

**Logo placeholder:** Rectangle, X: 22.5", Y: 33.3", W: 0.83", H: 0.42", fill `#3A4055`. Text: `[LOGO]`

**Version:** JetBrains Mono Regular, 11 pt, `#F0EDE8` at 50%. X: 0.5", Y: 35.0"
> v1.0 -- 2026

---

## Part 5 -- Grouping and Naming Convention

| Group Name | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline |
| Zone 2 - No Quench Hero | Typographic hero, two explanation panels |
| Zone 3 - Cooling Procedure | Section label, four step cards |
| Zone 4 - Distortion Comparison | Section label, comparison table |
| Zone 5 - FAQ | Section label, three FAQ cards |
| Zone 6 - Footer | Footer band, disclaimer, title, series, logo, version |

---

## Part 6 -- Light Edition Color Remap Table

Standard remap per Poster #586.

---

## Part 7 -- Export Checklist

| File Name | Mode | Quality | Bleed |
|---|---|---|---|
| `Gas Nitriding Cooling No Quench -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Nitriding Cooling No Quench -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Nitriding Cooling No Quench -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Gas Nitriding Cooling No Quench -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Nitriding Cooling No Quench -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Nitriding Cooling No Quench -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

The 140 pt "NO QUENCH" typographic hero is deliberately oversized. This is the single most important thing on the poster. An operator who remembers nothing else should walk away knowing that gas nitriding does not use a quench.

The "What If You Quenched Anyway?" panel uses Coral accent to signal danger -- quenching a nitrided part is not just useless, it is harmful. Make this point clearly but without condescension; many experienced heat treaters from carburizing backgrounds instinctively reach for the quench.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #593 -- Construction Workup v1.0*
*2026-04-26*
