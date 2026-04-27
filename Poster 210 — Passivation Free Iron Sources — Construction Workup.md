---
Project: Plating Posters Inc
Poster Number: 210
Title: "Passivation (Stainless Steel) -- Free Iron Sources"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Conversion Coating Clusters — Watson Research Brief (CC-08 Section 8.4)"
Technical Source: Understanding free iron contamination on stainless steel -- what it is, where it comes from, and why passivation exists to remove it. Educational/conceptual poster (no physical tank stage).
Process Scope: Stainless steel passivation -- Stage 3 educational (free iron sources and surface conditioning context)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Passivation
  - StainlessSteel
  - FreeIron
  - Education
  - ConstructionWorkup
  - ClusterCC08
---

# Poster #210 -- Construction Workup
## Passivation (Stainless Steel) -- Free Iron Sources

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the educational poster for CC-08. Unlike every other "Stage 3" poster in the conversion coating series, this one does not correspond to a physical tank. It answers the fundamental question: WHY do we passivate stainless steel?

The answer: free iron contamination. Every manufacturing operation that contacts stainless steel with carbon steel tools, fixtures, or environments deposits metallic iron particles on the surface. These particles are NOT part of the alloy -- they sit ON the chromium-rich surface and block the passive film from forming. When exposed to moisture, the free iron rusts, creating the paradox of "rust on stainless steel."

Passivation dissolves this free iron and allows the natural Cr2O3 passive film to reform over the entire surface. This poster makes that mechanism visible and tangible.

---

## Part 1 -- Workflow Orientation

### Design Capabilities for This Poster

Standard capability set.

### Limitations to Flag

1. **Free iron concept diagram (Block B -- HERO):** Visual showing free iron particles sitting on the stainless surface, blocking passive film formation.
2. **Sources of free iron contamination (Block C):** 8 contamination sources with visual icons.
3. **The passive film explained (Block D):** What Cr2O3 is and how it works.
4. **Free iron vs. alloyed iron (Block E):** Critical distinction.
5. **Troubleshooting strip (Block F).**

---

## Part 2 -- Document Setup Instructions

Standard: 24x36", `#1A1F2E`, locked palette and fonts. Standard guides.

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- FREE IRON CONCEPT / HERO (2.9"--15.5" / ~12.6" tall)
  Block B: Concept diagram (free iron on surface, passive film blocked)
  Block C: Sources of free iron contamination (8 sources)

ZONE 3 -- THE PASSIVE FILM EXPLAINED (15.5"--22.0" / ~6.5" tall)
  Block D: Cr2O3 passive film -- what it is, how it forms, why it matters

ZONE 4 -- FREE IRON vs. ALLOYED IRON (22.0"--28.5" / ~6.5" tall)
  Block E: The critical distinction that explains why "stainless" rusts

ZONE 5 -- TROUBLESHOOTING QUICK HITS (28.5"--32.5" / ~4.0" tall)
  Block F: 4-problem strip (free iron detection methods)

ZONE 6 -- FOOTER BAND (32.5"--36.0" / ~3.5" tall)
  Block G: Disclaimer + footer
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**BLOCK A -- Headline**
- Font: Barlow Condensed ExtraBold, 72 pt, `#F0EDE8`, letter spacing -4
- Text: `PASSIVATION (STAINLESS STEEL)`
- X: 0.5", Y: 0.5", W: 23.0"

**BLOCK A -- Subheading**
- Font: Barlow SemiBold, 36 pt, `#E8A020` (Amber)
- Text: `Understanding Free Iron -- Why We Passivate`
- Y: 1.5"

**BLOCK A -- Tagline**
- Font: Barlow SemiBold, 20 pt, `#F0EDE8` at 65%
- Text: `Stainless steel does not rust. Free iron on stainless steel does. Passivation removes the iron. The chromium does the rest.`
- Y: 2.2"

---

### ZONE 2 -- Free Iron Concept (HERO)

**Section label:**
- Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `FREE IRON -- THE PROBLEM PASSIVATION SOLVES`

---

**BLOCK B -- Concept Diagram**

Y: 3.8" to 8.5". Full width.

Large rounded rectangle: X: 0.5", Y: 3.8", W: 23.0", H: 4.5", fill `#1E2435`, radius 8.

Educational badge:
- Rounded rect 2.2" x 0.4", fill `#E8A020`
- Text: `EDUCATIONAL -- NOT A TANK STAGE` -- Barlow Condensed ExtraBold, 12 pt, `#1A1F2E`

Three conceptual panels across the width:

**Panel 1 -- "Clean" Stainless (X: 1.0", W: 6.5"):**
- Title: `IDEAL: CLEAN SURFACE` -- Barlow SemiBold, 16 pt, `#27AE60`
- Description (Inter Regular 13 pt `#F0EDE8`):
```
Chromium-rich alloy surface (11--30% Cr)
exposed to air forms Cr2O3 passive film
(1--5 nm thick).

This invisible film is the ENTIRE source
of stainless steel's corrosion resistance.

Self-healing: if scratched, Cr reacts with
O2 and reforms the film in seconds.
```

**Panel 2 -- Contaminated Surface (X: 8.5", W: 6.5"):**
- Title: `REALITY: FREE IRON ON SURFACE` -- Barlow SemiBold, 16 pt, `#E05C5C`
- Description (Inter Regular 13 pt `#F0EDE8`):
```
Manufacturing operations deposit metallic
iron particles ON the surface:

  Machining (carbon steel tooling)
  Grinding (iron-laden abrasives)
  Handling (steel fixtures, racks)

These particles BLOCK passive film formation.
When wet, the free iron rusts -- creating
the paradox of "rust on stainless."
```

**Panel 3 -- After Passivation (X: 16.0", W: 6.5"):**
- Title: `AFTER PASSIVATION` -- Barlow SemiBold, 16 pt, `#27AE60`
- Description (Inter Regular 13 pt `#F0EDE8`):
```
Passivation acid dissolves the free iron
(and only the free iron -- chromium and
nickel resist the acid).

With iron removed, the chromium-enriched
surface reacts with dissolved oxygen to
form a fresh, continuous Cr2O3 passive film.

Corrosion resistance: RESTORED.
```

---

**BLOCK C -- Sources of Free Iron Contamination**

Y: 9.0" to 15.0". Eight source cards in a 4x2 grid.

Each card: Rounded rect, W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

Row 1 (Y: 9.0"):
| Card | X | Source | How |
|---|---|---|---|
| 1 | 0.5" | MACHINING TOOLS | Carbon steel cutting tools, drills, taps transfer iron particles to the stainless surface at every contact |
| 2 | 6.33" | GRINDING / POLISHING | Iron-laden abrasive media embeds metallic iron into the surface; wire brushing with carbon steel wheels |
| 3 | 12.16" | CARBON STEEL CONTACT | Storage racks, handling fixtures, vises, and clamps made of carbon steel transfer iron by direct contact |
| 4 | 18.0" | SHOP ENVIRONMENT | Iron particles suspended in air from nearby grinding, welding, or blasting operations settle on stainless |

Row 2 (Y: 12.0"):
| Card | X | Source | How |
|---|---|---|---|
| 5 | 0.5" | WELDING | Weld spatter, heat tint, and filler wire residue all deposit iron on the surface |
| 6 | 6.33" | FORMING / STAMPING | Carbon steel dies and forming tools press iron particles into the stainless surface |
| 7 | 12.16" | BLASTING MEDIA | Recycled blast media contaminated with carbon steel particles from previous jobs |
| 8 | 18.0" | HANDLING | Bare hands (sweat = NaCl + iron from tools); carbon steel-soiled gloves; magnetic chucks |

Interior per card:
- Source: Barlow SemiBold 14 pt `#E05C5C`
- How: Inter Regular 12 pt `#F0EDE8`

---

### ZONE 3 -- The Passive Film Explained

**Section label:**
- Centered. Y: 15.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `THE PASSIVE FILM -- Cr2O3`

**BLOCK D -- Passive Film Panel**

Y: 16.3" to 21.8". Two panels.

**Left -- What It Is:**
- Rounded rect, X: 0.5", Y: 16.3", W: 11.0", H: 5.2", fill `#1E2435`, left accent `#27AE60`
- Title: `WHAT IS THE PASSIVE FILM?` -- Barlow SemiBold, 20 pt, `#27AE60`

Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):
```
Composition: Cr2O3-rich amorphous oxide
Thickness:   1--5 nm (10--50 Angstroms)
Appearance:  INVISIBLE (no visible coating)
Formation:   Spontaneous in air or dissolved O2

The passive film is a chromium-enriched oxide
that forms naturally when the alloy's chromium
content exceeds ~10.5% (the minimum for
"stainless" designation).

At 1--5 nm, it is thinner than a virus.
But it provides ALL of the corrosion
resistance that makes stainless "stainless."
```

**Right -- How It Works:**
- Rounded rect, X: 12.0", Y: 16.3", W: 11.5", H: 5.2", fill `#1E2435`, left accent `#E8A020`
- Title: `HOW DOES IT PROTECT?` -- Barlow SemiBold, 20 pt, `#E8A020`

Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):
```
1. BARRIER: The Cr2O3 film is chemically inert --
   it does not dissolve in most environments.

2. SELF-HEALING: If scratched, the exposed
   chromium reacts with oxygen and reforms the
   film in seconds (as long as the surface is
   free of contamination).

3. SELECTIVE: Chromium oxidizes preferentially
   over iron. The more chromium at the surface,
   the better the passive film.

PASSIVATION ENRICHES THE SURFACE IN CHROMIUM
by removing the iron that dilutes it. This is
the mechanism -- not adding something, but
REMOVING the contaminant that prevents the
natural film from forming.
```

---

### ZONE 4 -- Free Iron vs. Alloyed Iron

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `FREE IRON vs. ALLOYED IRON -- THE CRITICAL DISTINCTION`

**BLOCK E -- Comparison Panel**

Y: 22.9" to 28.3". Two panels.

**Left -- Alloyed Iron (Not the Problem):**
- Rounded rect, X: 0.5", Y: 22.9", W: 11.0", H: 5.0", fill `#1E2435`, left accent `#27AE60`
- Title: `ALLOYED IRON` -- Barlow SemiBold, 20 pt, `#27AE60`
- Subtitle: `Part of the Steel -- Not the Problem` -- Inter Regular 14 pt `#F0EDE8` at 60%

Content (Inter Regular 14 pt `#F0EDE8`):
```
Iron is the BASE METAL of stainless steel
(60--80% of the alloy by weight).

This iron is atomically bonded into the
crystal lattice with chromium, nickel,
molybdenum, and other alloying elements.

Alloyed iron participates in the passive
film formation -- it is protected BY the
chromium alongside it.

Passivation does NOT remove alloyed iron.
It cannot -- the acid preferentially attacks
free (unalloyed) iron on the surface.
```

**Right -- Free Iron (The Problem):**
- Rounded rect, X: 12.0", Y: 22.9", W: 11.5", H: 5.0", fill `#1E2435`, left accent `#E05C5C`
- Title: `FREE IRON` -- Barlow SemiBold, 20 pt, `#E05C5C`
- Subtitle: `Foreign Contamination -- The Target` -- Inter Regular 14 pt `#F0EDE8` at 60%

Content (Inter Regular 14 pt `#F0EDE8`):
```
Free iron is metallic iron deposited ON
the stainless surface from external sources.

It is NOT part of the alloy. It sits on top,
embedded in scratches, pores, and surface
irregularities.

Free iron:
  - Has NO chromium to protect it
  - Rusts when exposed to moisture
  - Creates galvanic cells with the stainless
  - BLOCKS the passive film from forming beneath it

Passivation REMOVES free iron. This is its
entire purpose. The acid dissolves the foreign
iron and leaves the alloy's chromium exposed
to form a fresh passive film.
```

---

### ZONE 5 -- Troubleshooting Quick Hits

**Section label:**
- Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`
- Text: `FREE IRON DETECTION -- 4 METHODS`

**BLOCK F -- Four Detection Method Cards**

Y: 29.4" to 32.3". Same construction as Poster #207.

| Card | X | Method | How It Works | Result |
|---|---|---|---|---|
| 1 | 0.5" | COPPER SULFATE TEST | Immerse in CuSO4/H2SO4 for 6 min; copper deposits on free iron | Pink/red = FAIL (free iron); no color = PASS |
| 2 | 6.33" | FERROXYL TEST | Apply K3Fe(CN)6 + HNO3 solution; Turnbull's blue forms on iron | Blue spots = free iron present |
| 3 | 12.16" | WATER IMMERSION | Immerse part in clean water for 24 hr | Rust spots = free iron |
| 4 | 18.0" | HIGH HUMIDITY | 24 hr at 95% RH, 95 F | Rust spots = free iron (most sensitive short-term test) |

Interior per card:
- Method: Barlow SemiBold 14 pt `#E8A020`
- How: Inter Regular 12 pt `#F0EDE8`
- Result: Inter Medium 12 pt `#27AE60`

---

### ZONE 6 -- Footer Band

Standard footer. Title: `Passivation (Stainless Steel) -- Free Iron Sources`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool explaining the science behind stainless steel passivation. Free iron contamination is universal in manufacturing environments. Detection methods per ASTM A967, ASTM A380. Consult your process supplier for application-specific guidance.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Passivation Free Iron Sources -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is one of the most conceptually important posters in the entire passivation cluster. It answers the question that confuses every new operator: "Why does stainless steel rust?" The three-panel concept diagram (clean surface / contaminated / after passivation) is the visual hook. The free iron vs. alloyed iron distinction in Zone 4 is the "aha" moment -- once an operator understands that free iron is FOREIGN contamination, not part of the alloy, the entire passivation process makes intuitive sense.

The detection methods in Zone 5 are repurposed as the "troubleshooting" section -- on an educational poster, the troubleshooting equivalent is "how do I know if I have the problem?"

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #210 -- Construction Workup v1.0*
*2026-04-26*
