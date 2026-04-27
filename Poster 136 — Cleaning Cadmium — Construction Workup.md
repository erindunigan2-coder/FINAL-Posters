---
Project: Plating Posters Inc
Poster Number: 136
Title: "Cleaning -- Cadmium"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Process Scope: Cleaning stage for cyanide cadmium plating (Stage 1 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - CadmiumPlating
  - Cyanide
  - Cleaning
  - ConstructionWorkup
  - ClusterEP14
---

# Poster #136 -- Construction Workup
## Cleaning -- Cadmium

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 1 of 8. Cleaning for cadmium plating follows the same general sequence as zinc plating but with one critical constraint: the primary substrate is high-strength steel (>200 ksi / >1380 MPa), which is extremely susceptible to hydrogen embrittlement. Every cleaning step must minimize hydrogen exposure -- short electroclean times, anodic polarity preferred, and minimal acid contact time.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **High-strength steel cleaning path (Block B -- HERO):** Single-path cleaning sequence with HE risk callouts at every hydrogen-generating step.
2. **Cleaning parameters panel (Block D):** Soak clean + electroclean with HE-aware time limits.
3. **Hydrogen embrittlement primer (Block E):** What HE is and why cleaning matters.
4. **Common errors (Block F).**
5. **DUAL BADGES:** Cyanide + Restricted Substance, same as Poster #135.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 1 highlighted (Teal)
ZONE 3 -- CLEANING SEQUENCE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- CLEANING PARAMETERS (14.5"--20.5" / ~6.0")
ZONE 5 -- HE PRIMER (20.5"--26.5" / ~6.0")
ZONE 6 -- COMMON ERRORS (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CLEANING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Cadmium Plating -- Stage 1 of 8` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `High-strength steel. Hydrogen is the enemy from step one. Every second in acid or at the cathode adds risk.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".
**DUAL BADGES:** Cyanide + Restricted Substance, same spec as Poster #135.

---

### ZONE 2 -- Orientation Strip

Stage 1 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Contaminated high-strength steel  -->  After: Clean, oxide-free surface with minimal hydrogen exposure`

---

### ZONE 3 -- Cleaning Sequence Hero

**Section label:** `CLEANING FOR HIGH-STRENGTH STEEL -- MINIMIZE HYDROGEN` -- Y: 4.4".

**BLOCK B -- Sequential Cleaning Steps (Y: 5.0" to 14.0")**

Vertical stack of 6 step boxes, each W: 22.0", H: 1.3", fill `#1E2435`.

| Step | Left Accent | Parameters | HE Risk Flag |
|---|---|---|---|
| 1. Vapor Degrease or Soak Clean | `#2EC4B6` | Vapor degrease preferred; soak 4--8 oz/gal, 140--160 F, 3--5 min | LOW -- no hydrogen generation |
| 2. Rinse | `#2EC4B6` | Ambient, flowing | NONE |
| 3. Electroclean (Anodic) | `#E8A020` | Anodic, 20--50 ASF, 3--5 min | MODERATE -- anodic generates O2 not H2, but some H2 at edges |
| 4. Rinse | `#2EC4B6` | Ambient, flowing | NONE |
| 5. Acid Activation | `#E05C5C` | HCl 10--20%, 15--30 sec MAXIMUM | HIGH -- acid generates H2 on steel surface |
| 6. Rinse | `#2EC4B6` | Ambient, flowing, then to Cd plate | NONE |

HE Risk flags: color-coded badges at right side of each step box.
- LOW: `#27AE60`
- MODERATE: `#E8A020`
- HIGH: `#E05C5C`

**Bottom callout:**
- `Vapor degreasing avoids ALL hydrogen risk during soil removal. If soak cleaning is used, keep time short.` Inter Medium 14 pt `#27AE60`

---

### ZONE 4 -- Cleaning Parameters

**Section label:** `OPERATING WINDOWS -- HE-AWARE LIMITS` -- Y: 14.7".

**BLOCK D -- Two-Panel (Y: 15.3" to 20.3")**

**Left -- Soak Clean / Vapor Degrease:**
- Rounded rect, H: 4.5", fill `#1E2435`, left accent `#2EC4B6`
- Title: `CLEANING METHOD` Barlow SemiBold 18 pt `#2EC4B6`

| Parameter | Vapor Degrease | Soak Clean |
|---|---|---|
| Method | Solvent vapor | Alkaline immersion |
| Temperature | Solvent BP | 140--160 F |
| Time | Until condensate clear | 3--5 min |
| H2 Risk | ZERO | LOW |

`Vapor degrease is preferred for cadmium substrates when available.`

**Right -- Electroclean:**
- Rounded rect, H: 4.5", fill `#1E2435`, left accent `#E8A020`
- Title: `ELECTROCLEANING` Barlow SemiBold 18 pt `#E8A020`

| Parameter | Range | Notes |
|---|---|---|
| Polarity | ANODIC (reverse) | Mandatory -- cathodic generates H2 |
| Current | 20--50 ASF | Standard |
| Time | 3--5 min | Keep SHORT |
| Temperature | 140--160 F | Standard |

`NEVER use cathodic electroclean on cadmium substrates. Cathodic polarity generates hydrogen directly on the part surface.` Inter Medium 13 pt `#E05C5C`

---

### ZONE 5 -- HE Primer

**Section label:** `HYDROGEN EMBRITTLEMENT -- WHY IT STARTS AT CLEANING` -- Y: 20.7".

**BLOCK E -- Three-Panel (Y: 21.3" to 26.3")**

**Left -- What Is HE?:**
- Rounded rect, W: 7.33", H: 4.5", fill `#1E2435`, left accent `#E05C5C`
- Title: `WHAT IS HE?` Barlow SemiBold 18 pt `#E05C5C`
- `Hydrogen atoms generated during acid contact or cathodic processes diffuse into the steel lattice.`
- `At grain boundaries, hydrogen recombines into H2 molecules -- too large to diffuse back out.`
- `Internal pressure builds. The steel cracks without warning under normal service loads.`
- `Failure is delayed -- hours, days, or weeks after plating.`

**Center -- Where H2 Comes From:**
- Rounded rect, W: 7.33", H: 4.5", fill `#1E2435`, left accent `#E8A020`
- Title: `H2 SOURCES IN CLEANING` Barlow SemiBold 18 pt `#E8A020`
- `1. Acid activation (HCl dissolves metal + releases H2)`
- `2. Cathodic electroclean (H2 evolves at cathode = the part)`
- `3. Plating itself (co-deposition of H2 at cathode)`
- `Total hydrogen absorbed = sum of ALL steps`

**Right -- The Fix:**
- Rounded rect, W: 7.67", H: 4.5", fill `#1E2435`, left accent `#27AE60`
- Title: `CONTROLLING HE IN CLEANING` Barlow SemiBold 18 pt `#27AE60`
- `1. Vapor degrease when possible (zero H2)`
- `2. Anodic electroclean only (O2 at anode, not H2)`
- `3. Minimize acid activation time (15--30 sec MAX)`
- `4. BAKE after plating (Stage 8) -- drives H2 out`
- `The bake fixes it. But minimizing absorption makes the bake more effective.`

---

### ZONE 6 -- Common Errors

**Section label:** `CLEANING ERRORS ON CADMIUM SUBSTRATES` -- Y: 26.7".

**BLOCK F -- Four Cards (Y: 27.3" to 32.3")**

| Card | Problem | Cause | Fix |
|---|---|---|---|
| 1 | CATHODIC ELECTROCLEAN | Operator reversed polarity | Verify anodic before every load |
| 2 | EXCESSIVE ACID TIME | Parts left in acid >30 sec | Timer at acid tank; strict SOP |
| 3 | SKIP ELECTROCLEAN | Shortcut -- soak only | Electroclean is required for adhesion |
| 4 | CONTAMINATED CLEANER | Oil buildup reduces cleaning | Monitor cleaner concentration; change on schedule |

---

### ZONE 7 -- Footer

Standard. Title: `Cleaning -- Cadmium`. Version `v1.0 -- 2026`.
Disclaimer includes cadmium carcinogen and cyanide warnings.

---

## Parts 5--7

**Grouping:** 7 zones. **Light Remap:** Standard. **Export:** Six files.

---

## Design Notes

The HE risk flags on each cleaning step are unique to cadmium (and other high-strength steel processes). This visual device -- a color-coded badge at the right of each step box -- makes the hydrogen risk visible at every stage. The HE primer in Zone 5 is educational content that will resonate with quality engineers and supervisors who need to understand the mechanism, not just the rule.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #136 -- Construction Workup v1.0*
*2026-04-26*
