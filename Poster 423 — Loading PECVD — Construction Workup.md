---
Project: Plating Posters Inc
Poster Number: 423
Title: "Loading -- PECVD"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 3: PECVD, Section 3.2)"
Technical Source: PECVD chamber loading, fixturing on electrode/substrate holder, pump-down procedures, and base vacuum verification. Electrode gap (10--50 mm) is a critical parameter affecting plasma uniformity.
Process Scope: PECVD substrate loading, fixturing, chamber closure, and pump-down
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - PECVD
  - Loading
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #423 -- Construction Workup
## Loading -- PECVD

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 3 of the PECVD sequence. Loading a PECVD chamber is not just "put the part in and close the door." Electrode gap, thermal contact, substrate positioning, and pump-down protocol all directly affect film quality. This poster covers the physical loading process and the transition from atmosphere to base vacuum.

Hero visual: PECVD parallel-plate chamber cross-section showing electrode gap, substrate position, and gas inlet.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Chamber cross-section hero (Block B):** Simplified parallel-plate reactor showing top electrode (showerhead/gas inlet), bottom electrode (substrate holder), substrate position, and labeled gap dimension.
2. **Loading sequence (Block C):** Step-by-step loading procedure.
3. **Pump-down protocol (Block D):** From atmosphere to base vacuum -- timeline and checkpoints.
4. **Electrode gap reference (Block E):** Why gap matters and typical values.
5. **Common loading mistakes (Block F):** 4-card defect strip.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 3 highlighted (Silver)
ZONE 3 -- CHAMBER CROSS-SECTION HERO (4.2"--14.5" / ~10.3")
  Block B: Parallel-plate reactor diagram
ZONE 4 -- LOADING SEQUENCE + PUMP-DOWN (14.5"--22.0" / ~7.5")
  Block C: Step-by-step loading
  Block D: Pump-down protocol
ZONE 5 -- ELECTRODE GAP + COMMON MISTAKES (22.0"--32.5" / ~10.5")
  Block E: Gap reference
  Block F: Common loading mistakes
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `LOADING` -- 88 pt `#F0EDE8`.
**Subheading:** `PECVD -- Stage 3 of 10 -- Fixturing, Chamber Closure, and Pump-Down` -- 28 pt `#C8D0D8` (Silver).
**Tagline:** `The electrode gap sets the plasma. The pump-down sets the purity. Get both right before you strike a glow.` -- 20 pt `#F0EDE8` at 65%.

**Rule Card:**
- Big number: `10-50` -- 60 pt, `#E8A020`
- Label: `mm ELECTRODE GAP` -- JetBrains Mono, 14 pt
- Sub-label: `Controls plasma uniformity` -- Inter Regular, 12 pt

---

### ZONE 2 -- Orientation Strip

Stage 3 (`Loading`): fill `#C8D0D8`, text `#1A1F2E`. Others dimmed.
Below: `Input: Clean substrate  -->  Output: Substrate mounted in chamber at base vacuum`

---

### ZONE 3 -- Chamber Cross-Section Hero

**Section label:** `THE PECVD PARALLEL-PLATE REACTOR` -- Y: 4.4".

**BLOCK B -- Chamber Diagram**

Y: 5.0" to 14.3".

**Chamber body:**
- Rounded rect, X: 3.0", Y: 5.5", W: 18.0", H: 7.5", fill `#252B3D`, border 2 pt `#C8D0D8`

**Top electrode (showerhead / gas distributor):**
- Rect, X: 4.0", Y: 6.0", W: 16.0", H: 0.8", fill `#3A4055`, border 1 pt `#C8D0D8`
- Label above: `TOP ELECTRODE (SHOWERHEAD)` Barlow SemiBold, 14 pt, `#C8D0D8`
- Small circles (gas holes) in row across bottom of electrode: 8 circles, 0.2" dia, fill `#1A1F2E`
- Label: `Gas inlet -- uniform distribution` Inter Regular, 11 pt, `#F0EDE8` at 60%

**Bottom electrode (substrate holder):**
- Rect, X: 4.0", Y: 11.0", W: 16.0", H: 0.8", fill `#3A4055`, border 1 pt `#E8A020`
- Label below: `BOTTOM ELECTRODE (SUBSTRATE HOLDER)` Barlow SemiBold, 14 pt, `#E8A020`
- Sub-label: `Temperature-controlled; RF or DC biased` Inter Regular, 11 pt, `#F0EDE8` at 60%

**Substrate (on bottom electrode):**
- Rect, X: 6.0", Y: 10.5", W: 12.0", H: 0.4", fill `#2EC4B6` at 40%, border 2 pt `#2EC4B6`
- Label: `SUBSTRATE` Barlow SemiBold, 12 pt, `#2EC4B6`

**Electrode gap dimension:**
- Double-headed arrow between bottom of top electrode and top of substrate
- Label: `GAP: 10--50 mm` JetBrains Mono Regular, 16 pt, `#E8A020`
- Note: `Smaller gap = higher power density. Larger gap = more uniform but lower rate.` Inter Regular, 12 pt, `#F0EDE8` at 70%

**RF power connection:**
- Line from external label to bottom electrode
- Label: `RF POWER (13.56 MHz)` JetBrains Mono, 12 pt, `#E8A020`
- `100--2000 W` JetBrains Mono, 11 pt, `#F0EDE8`

**Pump port:**
- Arrow at bottom of chamber pointing down
- Label: `TO VACUUM PUMP` Inter Medium, 12 pt, `#C8D0D8`
- `Roots blower + rotary vane` Inter Regular, 11 pt, `#F0EDE8` at 60%

**Gas inlet label (top):**
- Arrow from above chamber pointing into showerhead
- `PROCESS GAS (SiH4, NH3, Ar, etc.)` JetBrains Mono, 12 pt, `#2EC4B6`
- `Via MFC -- mass flow controlled` Inter Regular, 11 pt, `#F0EDE8` at 60%

**Plasma glow region (between electrodes):**
- Rounded rect, X: 5.0", Y: 7.2", W: 14.0", H: 3.0", fill `#2EC4B6` at 8%, border 1 pt `#2EC4B6` at 30%, dashed
- Label: `PLASMA REGION` Barlow SemiBold, 14 pt, `#2EC4B6` at 50%

---

### ZONE 4 -- Loading Sequence + Pump-Down

**BLOCK C -- Loading Sequence (Left, X: 0.5", W: 11.0")**

Section label: `LOADING PROCEDURE` -- Y: 14.7".

Seven steps in vertical flow:

1. `Open chamber (verify plasma OFF, gases OFF, RF OFF)`
2. `Inspect electrode surfaces -- clean if buildup visible`
3. `Place substrate on lower electrode -- verify full contact`
4. `Apply thermal paste or use clamping ring if required`
5. `Verify electrode gap setting (measure or confirm fixture)`
6. `Close chamber -- check O-ring seating`
7. `Begin pump-down sequence`

Each step: numbered badge + text in callout row.

**BLOCK D -- Pump-Down Protocol (Right, X: 12.0", W: 11.5")**

Section label: `PUMP-DOWN PROTOCOL` -- Y: 14.7".

Timeline/sequence:

| Phase | Pressure | Time | Action |
|---|---|---|---|
| Roughing | Atm -> 1 Torr | 2--5 min | Rotary vane or scroll pump |
| Crossover | 1 Torr -> 50 mTorr | 5--15 min | Roots blower engages |
| Base vacuum | < 50 mTorr | 10--30 min | Turbo (if equipped) for final pump |
| Leak check | Rate of rise < 5 mTorr/min | 2 min | Isolate pump; watch pressure gauge |
| Bake-out (optional) | At base vacuum | 15--30 min | Heat substrate to process temp; outgas |

Target: `< 50 mTorr base pressure. For high-quality films: < 1 mTorr.`

Note: `If base pressure is not achieved within expected time -- suspect a leak (O-ring, viewport, feedthrough) or outgassing (contaminated substrate or chamber).` -- Inter Medium, 12 pt, `#E05C5C`

---

### ZONE 5 -- Electrode Gap + Common Mistakes

**BLOCK E -- Electrode Gap Reference (Y: 22.2" to 27.0")**

Section label: `ELECTRODE GAP -- WHY IT MATTERS` -- Y: 22.4".

Two-column callout:

Left -- The Physics:
```
Smaller gap (10--20 mm):
  Higher power density at substrate
  Faster deposition rate
  Less uniform across large areas
  Risk of arcing if too small

Larger gap (30--50 mm):
  Better uniformity across substrate
  Lower deposition rate
  More gas-phase reactions (particles!)
  Standard for large-area (>300 mm) depositions
```

Right -- Typical Settings by Application:

| Application | Gap | Substrate Size |
|---|---|---|
| Semiconductor (wafer) | 15--25 mm | 200--300 mm |
| Solar cell (panel) | 20--40 mm | 300+ mm |
| DLC on parts | 20--30 mm | Variable |
| Barrier coating (roll-to-roll) | 10--20 mm | Web width |

**BLOCK F -- Common Loading Mistakes (Y: 27.5" to 32.3")**

Section label: `LOADING MISTAKES THAT RUIN FILMS` -- Barlow Condensed ExtraBold, 22 pt, `#E05C5C`. Y: 27.7".

Four cards in single row:

| Card | Problem | Cause | Fix |
|---|---|---|---|
| 1 | POOR THERMAL CONTACT | Substrate not flat on electrode; air gap | Use thermal paste, clamping ring, or He backside cooling |
| 2 | FINGERPRINTS ON SUBSTRATE | Handling after final clean | ALWAYS wear clean nitrile gloves during loading |
| 3 | O-RING SEAL FAILURE | Dirty, cracked, or misaligned O-ring | Inspect and lube O-rings per schedule; replace annually |
| 4 | SLOW PUMP-DOWN | Virtual leak from trapped gas or outgassing | Check for blind holes, trapped volumes; bake if needed |

Card format: same as Poster 419 troubleshooting cards.

---

### ZONE 6 -- Footer

Standard. Title: `Loading -- PECVD`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Loading PECVD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The chamber cross-section is the hero -- it must clearly show the parallel-plate geometry because this is what makes PECVD different from PVD or thermal CVD chambers. The electrode gap dimension should be the most prominent measurement on the diagram. The pump-down timeline is practical content that operators reference daily.

---

*Alaina -- Poster #423 -- Construction Workup v1.0 -- 2026-04-26*
