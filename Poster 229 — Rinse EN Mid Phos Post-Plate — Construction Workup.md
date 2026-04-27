---
Project: Plating Posters Inc
Poster Number: 229
Title: "Rinse -- EN (Mid Phos) -- Post-Plate"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters -- Watson Research Brief (Process 2: EN Mid-P, Poster 7)"
Process Scope: Post-plate rinse for electroless nickel mid phosphorus line (Stage 6 of 7)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ElectrolessNickel
  - MidPhosphorus
  - Rinse
  - ConstructionWorkup
  - Series2
  - ClusterEN-MP
---

# Poster #229 -- Construction Workup
## Rinse -- EN (Mid Phos) -- Post-Plate

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 6 of the EN Mid-P process. The post-plate rinse stops the EN reaction, removes drag-out chemicals, and prepares the surface for post-treatment. The EN Mid-P bath runs at 85-91 C -- hotter than any other EN class -- so the cold rinse quench is a sharper thermal shock. Parts must not air-dry between the EN bath and rinse; dried EN solution at acid pH causes permanent staining that is extremely difficult to remove.

For ENIG applications, the post-plate rinse must be followed immediately by immersion gold -- there is no heat treatment between EN and Au in the ENIG process.

Hero visual: cascade rinse with handling callouts showing the "no touch, no dry" rules, with ENIG pathway notation.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cascade rinse hero (Block B):** Two-stage rinse with emphasis on cold water to stop reaction.
2. **Orientation strip (Block C):** Stage 6 highlighted.
3. **Handling rules panel (Block E):** Critical post-plate handling requirements.
4. **ENIG pathway callout (Block F):** After rinse, ENIG parts go directly to immersion gold -- no heat treatment.
5. **Drag-out recovery callout:** EN drag-out is valuable (nickel + hypophosphite).

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 6 highlighted
ZONE 3 -- RINSE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- RINSE PARAMETERS + HANDLING RULES (14.5"--21.0" / ~6.5")
ZONE 5 -- COMMON PROBLEMS & FIXES (21.0"--27.0" / ~6.0")
ZONE 6 -- ENIG PATHWAY + DRAG-OUT RECOVERY + SAFETY (27.0"--32.5" / ~5.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. Y: 0.5".

**Subheading:** `EN (Mid Phos) -- Post-Plate -- Stage 6 of 7` -- 32 pt `#2EC4B6`. Y: 1.5".

**Tagline:** `The reaction does not stop when the part leaves the bath. Cold water stops it. Air-drying ruins it. ENIG parts go straight to gold -- no heat treatment.` -- 20 pt at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 6 highlighted (fill `#2EC4B6`). Others dimmed.

Below: `Before: Part exits EN bath at 85-91 C with active reaction  -->  After: Reaction stopped; surface clean and ready for post-treatment or immersion gold`

---

### ZONE 3 -- Rinse Hero

**Section label:** `THE POST-PLATE RINSE` -- Y: 4.4".

**BLOCK B -- Cascade Rinse Diagram**

Y: 5.0" to 11.5". Two connected tank cross-sections.

**Tank 1 (First Rinse / Drag-Out Recovery) -- X: 1.5", W: 9.5", H: 5.5":**
- Rounded rect, fill `#252B3D`, border 3 pt `#C8D0D8`
- Interior tinted `#27AE60` at 5% (EN chemistry drag-out)
- Label: `STAGE 1 (DRAG-OUT RECOVERY)` Barlow SemiBold 16 pt `#27AE60`
- Inside: `Recover Ni + hypophosphite for reuse or treatment` Inter Regular 12 pt at 60%

**Tank 2 (Clean Rinse) -- X: 12.0", W: 9.5", H: 5.5":**
- Fill `#252B3D` with `#2EC4B6` tint at 10%
- Label: `STAGE 2 (CLEAN -- COLD)` Barlow SemiBold 16 pt `#2EC4B6`
- `COLD WATER` JetBrains Mono 14 pt `#2EC4B6`
- Fresh water inlet

**Temperature callout between tanks (Y: 9.0"):**
- Arrow showing temperature drop: `85-91 C --> AMBIENT` Barlow SemiBold 16 pt
- `Thermal quench stops autocatalytic reaction` Inter Regular 13 pt `#F0EDE8` at 70%

**Handling rules callout boxes (Y: 12.0" to 14.3"):**

Three boxes in a row:

| Box | X | W | Rule | Accent |
|---|---|---|---|---|
| 1 | 0.5" | 7.33" | `DO NOT AIR-DRY: Dried EN solution stains permanently` | `#E05C5C` |
| 2 | 8.17" | 7.33" | `NO FINGER CONTACT: Fingerprints etch into fresh deposit` | `#E8A020` |
| 3 | 15.84" | 7.66" | `NO WET STACKING: Galvanic attack at contact points` | `#E8A020` |

Each: rounded rect fill `#1E2435`, left accent 0.06". Rule title: Barlow SemiBold 14 pt in accent color. Explanation: Inter Regular 12 pt `#F0EDE8`.

---

### ZONE 4 -- Rinse Parameters + Handling Rules

**Section label:** `RINSE PARAMETERS` -- Y: 14.7".

**Left -- Rinse Parameters (X: 0.5", W: 11.0"):**

Header: `POST-PLATE RINSE` fill `#3A4055`.

| Parameter | Value |
|---|---|
| Type | Double counterflow or spray rinse |
| Water temperature | Ambient -- cold preferred (stops reaction faster) |
| Water quality | DI preferred; municipal acceptable |
| Immersion time | 30-60 sec |
| Agitation | Air or spray |
| First rinse | Can be static drag-out recovery tank |
| Transfer time | Immediate from EN bath -- do not hold parts in air |

**Right -- Post-Plate Handling Checklist (X: 12.0", W: 11.5"):**

Header: `HANDLING RULES -- NON-NEGOTIABLE` fill `#E8A020`.

| Rule | Why |
|---|---|
| No air-drying | Dried acid EN solution (pH 4.6-5.2) stains deposit permanently |
| No finger contact | Fingerprints etch into freshly deposited Ni-P |
| No wet stacking | Contact points create galvanic cells; localized corrosion |
| Immediate rinse | EN reaction continues on part surface until quenched |
| Cold water preferred | Faster thermal quench = sharper reaction stop |
| Rack or basket only | Parts must hang freely; no metal-to-metal contact |

---

### ZONE 5 -- Common Problems & Fixes

**Section label:** `WHAT GOES WRONG AT THE POST-PLATE RINSE` -- Y: 21.2".

**4-Row Problem Table:**

| Problem | Symptom | Root Cause | Fix |
|---|---|---|---|
| Water staining | White/rainbow marks on deposit | Parts air-dried or sat in stagnant rinse | Ensure continuous flow; immediate transfer |
| Fingerprint etching | Visible prints burned into deposit | Bare-hand handling of fresh EN deposit | Gloves at all times; no skin contact |
| Thickness variation | Thin areas near contact points | Parts touching in rinse (galvanic attack) | Space parts on rack; use basket dividers |
| Orange peel on ENIG | Textured surface unacceptable for PCB | Rinse too hot or too long before Au | Cold rinse; minimize time before immersion gold |

Problem: `#E05C5C`. Symptom: `#E8A020`. Cause: `#F0EDE8`. Fix: `#27AE60`.

---

### ZONE 6 -- ENIG Pathway + Drag-Out Recovery + Safety

**Section label:** `ENIG PATHWAY & DRAG-OUT RECOVERY` -- Y: 27.2".

**Left -- ENIG Pathway (X: 0.5", W: 11.0"):**
- Rounded rect fill `#1E2435`, full border 2 pt `#27AE60`
- Title: `ENIG: NO HEAT TREATMENT BETWEEN EN AND GOLD` Barlow SemiBold 18 pt `#27AE60`
- `For PCB ENIG (IPC-4552B):`
- `EN Mid-P deposit --> Rinse --> DIRECTLY to immersion gold bath`
- `DO NOT heat treat between EN and Au`
- `Heat treatment oxidizes EN surface and prevents gold deposition`
- `Post-plate rinse quality is critical -- any residue affects Au adhesion`
- Visual: horizontal flow arrow: `EN BATH` -> `RINSE` -> `IMMERSION GOLD` (all Emerald)

**Right -- Drag-Out Recovery + Safety (X: 12.0", W: 11.5"):**

Title: `DRAG-OUT RECOVERY` Barlow SemiBold 16 pt `#2EC4B6`
- `First rinse tank can serve as drag-out recovery`
- `EN drag-out contains Ni2+ and hypophosphite -- valuable`
- `Return to EN bath (if contamination-free) or send to waste treatment`
- `Typical drag-out: 0.5-2.0 gal/1000 ft2`

Title: `SAFETY` Barlow SemiBold 16 pt `#E8A020`
- `EN drag-out is acidic (pH 4.6-5.2) and contains dissolved nickel`
- `Nickel compounds: skin sensitizer (occupational dermatitis)`
- `Gloves required for all part handling`
- `Rinse overflow: waste treatment, not drain`

---

### ZONE 7 -- Footer

Standard. Title: `Rinse -- EN (Mid Phos) -- Post-Plate`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Process parameters shown are typical industry values for post-plate rinsing in electroless nickel mid phosphorus (5-9% P) plating lines. ENIG process flow per IPC-4552B. Consult your process supplier for application-specific guidance.`

---

## Parts 5-7

**Grouping:** 7 zones.
**Light Remap:** Standard table. ENIG pathway border `#27AE60` -> `#1E7A47`.
**Export:** Six files -- `Rinse EN Mid-P Post-Plate -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The ENIG pathway callout is the unique Mid-P element at this stage. In ENIG processing, the EN deposit goes directly to immersion gold without any heat treatment -- heat would oxidize the EN surface and prevent gold deposition. This is a critical process rule that many operators do not realize. The drag-out recovery option reflects the economic reality that EN chemistry is expensive and Ni/hypophosphite recovery can offset operating costs.

---

*Alaina -- Poster #229 -- Construction Workup v1.0 -- 2026-04-26*
