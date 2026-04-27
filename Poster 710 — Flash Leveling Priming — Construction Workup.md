---
Project: Plating Posters Inc
Poster Number: 710
Title: "Flash / Leveling -- Priming"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster 7 technical reference (Industrial Priming Systems) -- Watson Research Brief"
Technical Source: Flash and leveling behavior of zinc-rich and epoxy primers. IOZ cures by hydrolysis requiring moisture -- fundamentally different from liquid paint leveling. Mud cracking is the signature defect when IOZ is over-applied. OZ cures by binder mechanism with better leveling but still rough due to zinc loading.
Process Scope: Flash / leveling for industrial priming -- Stage 6 of 8
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - IndustrialPriming
  - FlashLeveling
  - ConstructionWorkup
  - PaintingCoating
  - Cluster7
---

# Poster #710 -- Construction Workup
## Flash / Leveling -- Priming

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 6 of 8. This poster explains what happens between the moment the primer hits the substrate and the moment it begins to cure. For IOZ primers, there is no "leveling" in the traditional sense -- the high zinc loading produces a rough, matte, porous film by design. The critical parameter is flash time before recoat or topcoat. The hero concept: a visual showing why IOZ does not level like liquid paint, and why that rough, porous surface is actually correct.

The signature defect of this stage is mud cracking -- IOZ applied too thick shrinks during cure and cracks like dried riverbed mud. This poster makes that failure mode viscerally clear.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **IOZ vs. liquid paint leveling hero (Block B):** Side-by-side cross-section showing smooth liquid paint film vs. rough porous IOZ film -- both are "correct" for their type. Built with layered rectangles and texture fills.
2. **Flash time comparison table (Block D):** Time between application and recoat/topcoat for each primer type.
3. **Mud cracking deep-dive (Block E):** The mechanism, the threshold (> 5 mils), and the fix.
4. **Amine blush warning (Block F):** Epoxy primer blush in cool/humid conditions.
5. **Moisture and cure acceleration (Block G):** IOZ requires moisture to cure -- mist coating with water.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 21.0" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 6 highlighted (Emerald)
ZONE 3 -- IOZ SURFACE BEHAVIOR HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- FLASH TIME TABLE + RECOAT WINDOWS (14.5"--21.0" / ~6.5")
ZONE 5 -- MUD CRACKING DEEP DIVE (21.0"--27.0" / ~6.0")
ZONE 6 -- AMINE BLUSH + MOISTURE CURE (27.0"--32.5" / ~5.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `FLASH / LEVELING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Industrial Priming -- Stage 6 of 8` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `IOZ primer does not level. It is not supposed to. That rough, porous film is the galvanic engine doing its job.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 6 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Wet primer film on substrate  -->  After: Flash-off complete, film setting, cure beginning`

---

### ZONE 3 -- IOZ Surface Behavior Hero

**Section label:** `WHY IOZ PRIMER LOOKS DIFFERENT -- AND THAT IS CORRECT` -- Y: 4.4".

**BLOCK B -- Side-by-Side Cross-Section (Y: 5.0" to 14.0")**

Two large panels:

**Left -- Liquid Paint (X: 0.5", W: 11.0", H: 8.5"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#2EC4B6`
- Title: `LIQUID PAINT` Barlow SemiBold 22 pt `#2EC4B6`
- Subtitle: `Levels to a smooth, glossy film` Inter Regular 14 pt `#F0EDE8` at 50%

Cross-section description:
- Steel substrate base: Rectangle, fill `#3A4055`
- Smooth paint film above: Rectangle with smooth top edge, fill `#2EC4B6` at 30%
- Labels: `Solvent evaporates` / `Resin flows and levels` / `Smooth continuous film`
- Inter Regular 13 pt `#F0EDE8`

Behavior bullets:
- `Solvent flash: 10--30 min (drives leveling)`
- `Surface tension pulls film smooth`
- `Result: uniform gloss, smooth profile`
- `Leveling = good (expected outcome)`
- JetBrains Mono 12 pt `#F0EDE8`

**Right -- IOZ Primer (X: 12.0", W: 11.5", H: 8.5"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#27AE60`
- Title: `INORGANIC ZINC PRIMER` Barlow SemiBold 22 pt `#27AE60`
- Subtitle: `Rough, matte, porous -- by design` Inter Regular 14 pt `#F0EDE8` at 50%

Cross-section description:
- Steel substrate base: Rectangle, fill `#3A4055`
- Rough primer film above: Irregular top edge with scattered zinc particles (small circles, fill `#C8D0D8`)
- Labels: `Solvent flash-off` / `Zinc particles remain packed` / `Porous, matte surface`
- Inter Regular 13 pt `#F0EDE8`

Behavior bullets:
- `Solvent flash: 30--60 min at 50% RH`
- `75--85% zinc by weight = more metal than binder`
- `Film cannot flow -- zinc particles interlock`
- `Result: rough, matte, porous (CORRECT)`
- `Porosity enables moisture cure (hydrolysis)`
- JetBrains Mono 12 pt `#F0EDE8`

Key insight callout (bottom, full width Y: 13.2"):
- Rounded rect, fill `#27AE60` at 15%, border 1 pt `#27AE60`, W: 23.0", H: 0.6"
- Text: `Do not judge IOZ primer by liquid paint standards. Rough and matte IS the correct appearance.` Inter Medium 14 pt `#27AE60`

---

### ZONE 4 -- Flash Time Table + Recoat Windows

**Section label:** `FLASH TIME AND RECOAT WINDOWS` -- Y: 14.7".

**BLOCK D -- Flash/Recoat Table (Y: 15.3" to 20.8")**

| Primer Type | Flash Time (between coats) | Min Recoat | Max Recoat | Exceeding Max Recoat |
|---|---|---|---|---|
| IOZ (ethyl silicate) | 30--60 min at 50% RH | 30 min | 4--8 hours | Must be fully cured (24 hr) before topcoat |
| IOZ (alkali silicate) | 30--60 min | 30 min | 4--8 hours | Same as ethyl silicate |
| OZ (2K epoxy-zinc) | Per binder pot life | 4--24 hours | Per TDS | Scuff sand if max exceeded |
| OZ (1K moisture-cure) | Overnight | 24 hours | Per TDS | Scuff sand |
| Epoxy primer (2K) | 30 min--4 hr | 4--24 hours | 3--7 days | Scuff sand 80--120 grit |
| Chromated epoxy (aero) | 30--60 min | Per TDS | Per TDS | Per spec |

Header: `#3A4055`. Alternating rows `#1E2435` / `#252B3D`. Data: JetBrains Mono 12 pt.

Bottom note: `Always consult the specific product TDS for exact recoat windows. Temperature and humidity significantly affect these times.` Inter Regular 12 pt `#F0EDE8` at 60%.

---

### ZONE 5 -- Mud Cracking Deep Dive

**Section label:** `MUD CRACKING -- THE SIGNATURE IOZ DEFECT` -- Y: 21.2".

**BLOCK E -- Full-Width Panel (Y: 21.8" to 26.8")**

Two side-by-side panels:

**Left -- The Mechanism (X: 0.5", W: 11.0"):**
- Rounded rect, fill `#1E2435`, left accent `#E05C5C`
- Title: `WHAT CAUSES MUD CRACKING` Barlow SemiBold 18 pt `#E05C5C`

Content (Inter Regular 14 pt `#F0EDE8`, line height 165%):
- `IOZ binder (ethyl silicate) shrinks during cure as hydrolysis and condensation proceed`
- `At normal DFT (2.5--4.0 mils), shrinkage stress is manageable`
- `Above 5 mils DFT, shrinkage stress exceeds the film's cohesive strength`
- `The film cracks in a pattern resembling dried mud in a riverbed`
- `Cracked film has ZERO barrier protection and compromised galvanic protection`

Threshold stat:
- `> 5 mils = MUD CRACKING ZONE` Barlow Condensed ExtraBold 24 pt `#E05C5C`

**Right -- Prevention and Repair (X: 12.0", W: 11.5"):**
- Rounded rect, fill `#1E2435`, left accent `#27AE60`
- Title: `PREVENTION AND REPAIR` Barlow SemiBold 18 pt `#27AE60`

Prevention (Inter Regular 14 pt `#F0EDE8`):
- `Apply IOZ at 2.5--4.0 mils DFT -- never exceed 5 mils`
- `Check wet film thickness during application (ASTM D4414)`
- `Apply two thin coats rather than one thick coat`
- `Reduce spray pressure and increase passes for uniform thin build`

Repair:
- `Mud-cracked IOZ must be completely removed`
- `Re-blast to specification`
- `Reapply at correct DFT`
- `There is no "touch-up" fix for mud cracking`
- Inter Medium 13 pt `#E05C5C`

---

### ZONE 6 -- Amine Blush + Moisture Cure

**Two-column layout (Y: 27.2" to 32.3"):**

**Left -- Amine Blush (Epoxy Primers) (X: 0.5", W: 11.0"):**

Section label: `AMINE BLUSH -- THE EPOXY HAZARD` Barlow Condensed ExtraBold 22 pt `#E8A020`.

Callout, fill `#1E2435`, left accent `#E8A020`:
- `What: Waxy film on curing epoxy surface`
- `When: Cool temperatures (< 50 deg F) + high humidity (> 80% RH)`
- `Cause: Amine hardener reacts with CO2 and moisture at the surface`
- `Forms: Amine carbamate (waxy, greasy feel)`
- `Risk: Intercoat adhesion failure if overcoated without removal`
- Inter Regular 13 pt `#F0EDE8`

Removal:
- `Water wash with scrub pad (warm water preferred)`
- `Solvent wipe (MEK, xylene)`
- `Must remove BEFORE applying next coat`
- Inter Medium 13 pt `#E8A020`

**Right -- IOZ Moisture Cure Acceleration (X: 12.0", W: 11.5"):**

Section label: `IOZ NEEDS MOISTURE TO CURE` Barlow Condensed ExtraBold 22 pt `#27AE60`.

Callout, fill `#1E2435`, left accent `#27AE60`:
- `IOZ cures by hydrolysis of ethyl silicate binder`
- `Atmospheric moisture is REQUIRED -- dry environments (< 30% RH) inhibit cure`
- `Cure acceleration: mist coat the IOZ surface with clean water`
- `In arid climates, provide humidity tenting or mist spray`
- `Waterborne IOZ (alkali silicate) is less moisture-sensitive`
- Inter Regular 13 pt `#F0EDE8`

RH guideline:
| RH Range | Cure Speed |
|---|---|
| < 30% | Very slow -- may not cure; add moisture |
| 30--50% | Slow but adequate |
| 50--80% | Optimal cure speed |
| > 80% | Fast cure; watch for trapped moisture under topcoat |

Data: JetBrains Mono 12 pt `#F0EDE8`.

---

### ZONE 7 -- Footer

Standard. Title: `Flash / Leveling -- Priming`. Version `v1.0 -- 2026`.
Disclaimer note: `Source: General industry knowledge; SSPC-PS 12.01; ASTM D4414; Watson Research Brief.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Flash Leveling Priming -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster tackles the most misunderstood stage in industrial priming: the flash/leveling period. Operators trained on liquid paint expect a smooth, glossy result. IOZ primer is rough, matte, and porous -- and that is correct. The side-by-side hero makes this contrast unmissable. Mud cracking gets a full panel because it is the single most expensive application failure in IOZ -- once cracked, the entire coating must be stripped and reapplied. The amine blush panel serves epoxy users who may encounter this insidious adhesion killer in the field.

---

*Alaina -- Poster #710 -- Construction Workup v1.0 -- 2026-04-26*
