---
Project: Plating Posters Inc
Poster Number: 683
Title: "Cure -- Dip Coating"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting & Organic Coating Clusters -- Watson Research Brief (Cluster 4, Section 4.8)"
Technical Source: Cure methods for dip coating -- PVC plastisol fusion (gel -> fusion -> over-fusion), thermoplastic solidification by cooling, thermoset cross-linking (epoxy, rubber vulcanization, silicone), and the critical PVC fusion temperature window.
Process Scope: Cure for dip coating -- Stage 6 of 7
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - DipCoating
  - Cure
  - ConstructionWorkup
  - PaintingCoating
  - ClusterPC04
---

# Poster #683 -- Construction Workup
## Cure -- Dip Coating

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 6 of 7. The cure stage for dip coating spans three radically different mechanisms: PVC plastisol fusion (a physical process where PVC particles solvate into plasticizer), thermoplastic solidification by cooling (no chemistry, just physics), and thermoset cross-linking (epoxy, rubber, silicone). The hero is a cure parameter table covering all six major dip coating materials. The PVC fusion window gets its own detail panel because the gel-fusion-overfusion sequence is the most important quality concept in plastisol dip coating, and overfusion releases toxic HCl gas.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Six-material cure parameter table (Block B -- HERO):** PVC plastisol, nylon, PE, epoxy solution, rubber, silicone.
2. **PVC plastisol fusion detail (Block C):** Gel -> fusion -> over-fusion with temperature windows.
3. **Thermoplastic vs. thermoset cure comparison (Block D):** Fundamental mechanism contrast.
4. **Defect grid (Block F):** 6 cure defects.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.5" / 21.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 6 highlighted (Amber)
ZONE 3 -- SIX-MATERIAL CURE TABLE HERO (4.2"--15.5" / ~11.3")
ZONE 4 -- PVC PLASTISOL FUSION DETAIL (15.5"--21.5" / ~6.0")
ZONE 5 -- THERMOPLASTIC vs. THERMOSET (21.5"--26.5" / ~5.0")
ZONE 6 -- DEFECT GRID (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CURE` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Dip Coating -- Fusion, Solidification, and Cross-Linking -- Stage 6 of 7` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `PVC fuses at 350 F. Nylon freezes on cooling. Epoxy cross-links at 300 F. Three cure mechanisms, three temperature stories -- and one critical warning: PVC above 420 F releases toxic HCl gas.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 6 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Drained, excess-removed wet coating --> After: Fully cured, hardened coating ready for inspection`

---

### ZONE 3 -- Six-Material Cure Table Hero

**Section label:** `CURE PARAMETERS BY COATING TYPE` -- Y: 4.4".

**BLOCK B -- Six-Row Table (Y: 5.0" to 15.0")**

Full-width table (23.0"):

| Coating | Cure Temp | Cure Time (at metal temp) | Mechanism | Critical Limit |
|---|---|---|---|---|
| PVC Plastisol | 350--400 F (177--204 C) | 10--20 min | Fusion: PVC particles solvate into plasticizer | Over-fusion > 420 F: HCl gas, degradation |
| Nylon 11/12 | Melt on hot part, cool | Cooling time varies | Thermoplastic solidification | Melt point ~350--365 F |
| Polyethylene | Melt on hot part, cool | Cooling time varies | Thermoplastic solidification | Melt point ~230--275 F |
| Epoxy (solution dip) | 300--400 F (149--204 C) | 15--30 min | Thermoset cross-linking | Undercure = poor chemical resistance |
| Rubber (latex dip) | 250--350 F (121--177 C) | 15--30 min | Vulcanization (sulfur cross-linking) | Under-vulcanized = soft, weak film |
| Silicone | 300--400 F (149--204 C) | 10--30 min | Condensation or addition cure | Per manufacturer spec |

Header row: fill `#3A4055`, Barlow SemiBold 13 pt `#F0EDE8`.
Data: JetBrains Mono 11 pt. Alternating rows: `#1E2435` / `#252B3D`.

Below table (Inter Medium 14 pt `#E8A020`):
`Always define cure by METAL TEMPERATURE, not oven air temperature. Heavy parts take longer to reach target metal temp than the oven setpoint suggests.`

---

### ZONE 4 -- PVC Plastisol Fusion Detail

**Section label:** `PVC PLASTISOL -- THE FUSION WINDOW` -- Y: 15.7".

**BLOCK C -- Three-Phase Diagram (Y: 16.3" to 21.3")**

Full-width horizontal strip showing three phases left to right:

**Phase 1 -- Gel (X: 0.5", W: 7.33"):**
- Fill: `#1E2435`, top accent `#E8A020`
- Title: `GEL POINT` -- Barlow SemiBold, 20 pt, `#E8A020`
- Temperature: `~250 F (121 C)`
- Description: `PVC particles begin to absorb plasticizer. Material gels and becomes semi-solid. Film is porous and weak at this stage.`
- Warning: `Parts removed at gel point have INADEQUATE properties -- the film is not fused.`

**Phase 2 -- Fusion (X: 8.17", W: 7.33"):**
- Fill: `#1E2435`, top accent `#27AE60`
- Title: `FUSION POINT` -- Barlow SemiBold, 20 pt, `#27AE60`
- Temperature: `~350 F (177 C)`
- Description: `Complete solvation -- PVC particles fully dissolve into plasticizer, forming a continuous, homogeneous, tough film. This is the TARGET.`
- Note: `Below fusion temperature = weak, porous, inadequate film. The part MUST reach fusion temp at the metal surface.`

**Phase 3 -- Over-Fusion (X: 15.83", W: 7.67"):**
- Fill: `#1E2435`, top accent `#E05C5C`
- Title: `OVER-FUSION` -- Barlow SemiBold, 20 pt, `#E05C5C`
- Temperature: `> 420 F (216 C)`
- Description: `Thermal degradation begins. PVC decomposes and releases TOXIC HYDROGEN CHLORIDE (HCl) GAS. Film discolors (brown/black), becomes brittle.`
- Safety warning (JetBrains Mono 13 pt `#E05C5C`): `HCl GAS IS CORROSIVE AND TOXIC. Over-fusion is a safety hazard, not just a quality defect. Monitor oven temperature closely.`

---

### ZONE 5 -- Thermoplastic vs. Thermoset

**Section label:** `TWO FUNDAMENTALLY DIFFERENT CURE MECHANISMS` -- Y: 21.7".

**Two-column layout (Y: 22.3" to 26.3"):**

**Left -- Thermoplastic (X: 0.5", W: 11.0"):**

Callout box, fill `#1E2435`, left accent `#2EC4B6`.
Title: `THERMOPLASTIC CURE` -- Barlow SemiBold, 20 pt, `#2EC4B6`

- `No chemical reaction -- just physics`
- `Coating melts on hot part, solidifies on cooling`
- `CAN be remelted (reversible)`
- `Materials: Nylon, PE, PP, PVC (plastisol fusion is unique hybrid)`
- `Cure verification: Visual -- smooth, continuous film; no powder residue`
- `Over-cure: Not possible in the traditional sense (except PVC decomposition)`

**Right -- Thermoset (X: 12.0", W: 11.5"):**

Callout box, fill `#1E2435`, left accent `#E8A020`.
Title: `THERMOSET CURE` -- Barlow SemiBold, 20 pt, `#E8A020`

- `Chemical cross-linking reaction -- irreversible`
- `Coating chemically bonds into a 3D network`
- `CANNOT be remelted once cured`
- `Materials: Epoxy, rubber (vulcanization), silicone`
- `Cure verification: MEK rub test, hardness, chemical resistance`
- `Undercure: Poor chemical resistance, soft film, premature failure`
- `Overcure: Possible -- embrittlement, discoloration`

---

### ZONE 6 -- Defect Grid

**Section label:** `WHAT GOES WRONG -- 6 CURE DEFECTS` -- Y: 26.7".

**BLOCK F -- 3x2 Grid (Y: 27.3" to 32.3")**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | PVC UNDER-FUSION | `#E05C5C` | Metal temp did not reach 350 F; inadequate soak time | Thermocouple verify metal temp; extend oven time |
| R1C2 | PVC OVER-FUSION / HCl | `#E05C5C` | Metal temp exceeded 420 F | Reduce oven temp; profile with data logger; separate thin/thick parts |
| R1C3 | BLISTERING DURING CURE | `#E8A020` | Trapped moisture or air boiling under coating | Pre-dry parts completely; pre-bake porous substrates |
| R2C1 | EPOXY UNDERCURE | `#E8A020` | Insufficient time at temperature | MEK rub test to verify; extend cure |
| R2C2 | UNEVEN NYLON THICKNESS | `#2EC4B6` | Non-uniform cooling rate across part geometry | Control cooling rate; forced air cooling for uniformity |
| R2C3 | RUBBER UNDER-VULCANIZED | `#2EC4B6` | Oven temp too low or sulfur crosslinker depleted | Verify oven profile; check compound formulation |

Each card: Rounded rect W: 7.33", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06" in defect color.

---

### ZONE 7 -- Footer

Standard. Title: `Cure -- Dip Coating`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge. Cure temperatures and times are material-specific. PVC decomposition temperature varies by formulation -- consult supplier TDS. ALWAYS ensure adequate ventilation in plastisol cure ovens.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cure Dip Coating -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The PVC fusion window (gel -> fusion -> over-fusion) is the poster's defining educational element. The three-phase horizontal strip makes the temperature relationship visually intuitive: green at 350 F (target), red above 420 F (danger). The HCl safety warning is not optional decoration -- PVC decomposition is a real safety hazard in plastisol operations. The thermoplastic vs. thermoset comparison drives home the fundamental distinction that shapes everything about dip coating cure: one is reversible physics, the other is irreversible chemistry.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #683 -- Construction Workup v1.0*
*2026-04-26*
