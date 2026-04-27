---
Project: Plating Posters Inc
Poster Number: 50
Title: "Activation -- Zinc-Nickel"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Process Scope: Acid activation for zinc-nickel plating line (Stage 3 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ZincNickelPlating
  - Activation
  - ConstructionWorkup
  - Series2
  - ClusterEP03
---

# Poster #50 -- Construction Workup
## Activation -- Zinc-Nickel

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 3 of the zinc-nickel process. HCl activation for alkaline Zn-Ni baths (10--30% v/v); HCl or H2SO4 for acid Zn-Ni baths (5--15% v/v). The hydrogen embrittlement warning is more prominent here than on any other zinc poster because Zn-Ni is almost always applied to high-strength steel -- automotive fasteners, brake calipers, aerospace components. HE baking is the default assumption, not the exception.

Hero visual: same before/after surface cross-section as Posters #34 and #42. The HE warning zone is larger and more emphatic.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Surface cross-section hero (Block B):** Before/after oxide removal.
2. **Alkaline vs. acid activation callout (Block E):** Different activation parameters depending on the Zn-Ni bath type.
3. **H-embrittlement warning (Block G):** Largest HE callout in the series -- Zn-Ni parts are overwhelmingly high-strength steel.
4. **Orientation strip:** Stage 3 highlighted.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 3 highlighted
ZONE 3 -- SURFACE CROSS-SECTION HERO (4.2"--13.5")
ZONE 4 -- ACTIVATION PARAMETERS (13.5"--21.0")
ZONE 5 -- COMMON PROBLEMS & FIXES (21.0"--27.0")
ZONE 6 -- H-EMBRITTLEMENT WARNING + SAFETY (27.0"--32.5")
ZONE 7 -- FOOTER (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header

**Headline:** `ACTIVATION` -- 80 pt `#F0EDE8`. Y: 0.5".
**Subheading:** `Zinc-Nickel -- Stage 3 of 8` -- 34 pt `#E8A020`. Y: 1.4".
**Tagline:** `Zinc-nickel parts are almost always high-strength steel. Every second in acid counts. Minimize exposure. Bake is not optional.` -- 20 pt at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 3 highlighted: fill `#E8A020`. Others dimmed.
Below: `Before: Clean surface with invisible oxide  -->  After: Bare metal, oxide-free, ready for Zn-Ni alloy deposition`

---

### ZONE 3 -- Surface Cross-Section Hero

**Section label:** `WHAT ACTIVATION DOES -- THE SURFACE UP CLOSE` -- Y: 4.4".

**BLOCK B -- Before/After Diagram**

Same layout as Poster #42. Before (oxide present) left, after (clean metal) right, center divider with acid attack formula.

Acid reaction detail:
- `Fe2O3 + 6HCl --> 2FeCl3 + 3H2O` JetBrains Mono 14 pt `#E8A020`
- `Oxide removed. Clean, active surface ready for Zn-Ni alloy adhesion.` Inter Regular 14 pt `#F0EDE8`

---

### ZONE 4 -- Activation Parameters

**Section label:** `ACTIVATION PARAMETERS` -- Y: 13.7".

**Two-column layout: Alkaline Zn-Ni (left) vs. Acid Zn-Ni (right).**

**Left -- For Alkaline Zn-Ni Bath (X: 0.5", W: 11.0"):**

Rounded rect fill `#1E2435`, left accent `#E8A020`.
Header: `ACTIVATION FOR ALKALINE Zn-Ni`

| Parameter | Value |
|---|---|
| Acid type | HCl (hydrochloric) preferred |
| Concentration | 10--30% v/v |
| Temperature | Ambient (65--85 F) |
| Time | 15--60 sec |
| Agitation | None to mild |
| Rinse after | Immediate -- do not let parts dry |
| Note | Higher HCl concentration than plain zinc activation |

**Right -- For Acid Zn-Ni Bath (X: 12.0", W: 11.5"):**

Rounded rect fill `#1E2435`, left accent `#2EC4B6`.
Header: `ACTIVATION FOR ACID Zn-Ni`

| Parameter | Value |
|---|---|
| Acid type | H2SO4 or HCl |
| Concentration | 5--15% v/v |
| Temperature | Ambient |
| Time | 15--30 sec |
| Agitation | None to mild |
| Rinse after | Immediate |
| Note | Shorter time -- acid Zn-Ni bath is less tolerant of acid drag-in |

**Bottom note (spanning both columns):**
- `For both bath types: minimize activation time on high-strength steel. 15--30 seconds maximum for parts >= 31 HRC.` Inter Medium 14 pt `#E05C5C`

---

### ZONE 5 -- Common Problems & Fixes

**Section label:** `WHAT GOES WRONG AT ACTIVATION` -- Y: 21.2".

| Problem | Symptom | Cause | Fix |
|---|---|---|---|
| Under-activation | Zn-Ni peels, blisters on bend test | Acid too weak or time too short | Increase HCl concentration; extend to 30 sec |
| Over-activation | Rough Zn-Ni, pitting | Time too long or acid too strong | Reduce time; dilute acid |
| H-embrittlement | Delayed brittle fracture in service | Hydrogen absorbed during acid contact | 15--30 sec max; bake 375 F within 1--4 hr |
| Smut on surface | Dark residue after activation | Carbon smut from high-C or case-hardened steel | De-smutter dip; light anodic electroclean |
| Flash rust | Orange tint before reaching Zn-Ni tank | Parts dried between activation and rinse | Immediate transfer; never air-dry |

---

### ZONE 6 -- H-Embrittlement Warning + Safety

**Section label:** `CRITICAL SAFETY -- HYDROGEN EMBRITTLEMENT` -- Barlow Condensed ExtraBold 24 pt `#E05C5C`. Y: 27.2".

**BLOCK G -- H-Embrittlement Panel (X: 0.5", W: 23.0", H: 3.5")**

This is a FULL-WIDTH warning panel -- larger than on Posters #34 and #42.

- Rounded rect fill `#1E2435`, FULL border 3 pt `#E05C5C`
- Title: `HYDROGEN EMBRITTLEMENT -- THE DEFAULT ASSUMPTION FOR Zn-Ni` Barlow SemiBold 22 pt `#E05C5C`
- Body (Inter Regular 14 pt `#F0EDE8`, line height 155%):
  - `Zinc-nickel is specified on high-strength steel in the vast majority of applications.`
  - `HE baking is the DEFAULT, not the exception.`
  - `REQUIREMENTS:`
  - `* Limit acid activation to 15--30 seconds maximum`
  - `* Bake at 375 +/- 25 F (190 +/- 14 C)`
  - `* Aerospace: within 1 HOUR of plating (AMS 2759/9)`
  - `* Automotive/general: within 4 HOURS of plating (ASTM B850)`
  - `* Hold bake for 8--24 hours (automotive typically 23 hr min at >= 39 HRC)`
  - `* Never skip. Never delay. Parts WILL fail in service.`
- Key specs: `ASTM B850 | AMS 2759/9 | ASTM B841` JetBrains Mono 12 pt `#E05C5C`

**Safety sidebar (below or right of HE panel, Y: 31.0"):**
- `Acid handling: HCl fumes corrosive -- ventilation required` / `H2SO4: add acid to water` / `PPE: goggles, face shield, gloves, apron` / `Eyewash within 10 sec`
- Inter Regular 13 pt `#F0EDE8`

---

### ZONE 7 -- Footer

Standard. Title: `Activation -- Zinc-Nickel`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table. Full-width HE border (`#E05C5C` -> `#B83E3E`) at 3 pt -- verify visibility.
**Export:** Six files -- `Activation Zinc-Nickel -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster has the largest hydrogen embrittlement warning in the entire series. The full-width, 3 pt coral border is deliberate. Watson's brief states plainly: "ZnNi is almost always applied to high-strength steel. HE baking is the default assumption, not the exception." The 1-hour aerospace oven window (vs. 4-hour general) is critical for shops running AMS 2417 work.

The dual-column activation parameters (alkaline vs. acid bath type) is a feature unique to the Zn-Ni cluster -- the other zinc clusters only run one bath type.

---

*Alaina -- Plating Posters Inc Creative Lead*
*Poster #50 -- Construction Workup v1.0*
*2026-04-26*
