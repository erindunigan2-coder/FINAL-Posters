---
Project: Plating Posters Inc
Poster Number: 444
Title: "Vacuum / Plasma Setup -- DLC"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters — Watson Research Brief (Cluster 5: DLC, Sections 5.2, 5.5)"
Process Scope: Vacuum system operation and plasma preparation for DLC coating
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - DLC
  - VacuumSetup
  - PlasmaSetup
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #444 -- Construction Workup
## Vacuum / Plasma Setup -- DLC

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This poster covers the vacuum system from door close to plasma-ready: pump-down sequence, base vacuum verification, leak-rate check, substrate heating (if applicable), and the critical Ar+ ion etch that removes surface oxides and activates the substrate for adhesion. Two system types covered side-by-side: PECVD and filtered cathodic arc.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Pump-down sequence flow (Block B -- HERO):** Vertical flow from chamber close through base vacuum to ion etch.
2. **PECVD vs. Arc system comparison (Block D):** Side-by-side vacuum specs.
3. **Ion etch parameters (Block E):** The critical surface activation step.
4. **Vacuum system checklist (Block F):** Pre-run verification.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 15.0" / 21.0" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- PUMP-DOWN SEQUENCE HERO (2.9"--15.0" / ~12.1")
  Block B: Vertical pump-down flow
ZONE 3 -- PECVD vs. ARC COMPARISON (15.0"--21.0" / ~6.0")
  Block D: Side-by-side system specs
ZONE 4 -- ION ETCH PARAMETERS (21.0"--27.0" / ~6.0")
  Block E: Ar+ etch detail -- the adhesion enabler
ZONE 5 -- PRE-RUN CHECKLIST (27.0"--32.5" / ~5.5")
  Block F: Vacuum system verification
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `VACUUM / PLASMA SETUP` -- 80 pt `#F0EDE8`.
**Subheading:** `Diamond-Like Carbon -- Chamber Preparation & Ion Etching` -- 32 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `From atmosphere to base vacuum to plasma-ready. The ion etch is where adhesion begins -- or fails.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Pump-Down Sequence Hero

**Section label:** `CHAMBER PREPARATION SEQUENCE` -- Y: 3.1".

**BLOCK B -- Vertical Flow (6 Steps)**

Y: 3.8" to 14.8". Six stacked cards with downward arrows.

Each card: Rounded rect, X: 0.5", W: 23.0", H: 1.6", fill `#1E2435`, radius 6.

| Step | Name | Accent | Key Parameters | Detail |
|---|---|---|---|---|
| 1 | Chamber Close & Seal | `#2EC4B6` | Door sealed; O-rings inspected | Verify no tools, rags, or foreign objects inside. Check O-ring condition. |
| 2 | Roughing Pump | `#2EC4B6` | Atmosphere -> 50--100 mTorr | Rotary vane or scroll pump. 5--15 min typical. Monitor for leaks (pressure rise test). |
| 3 | High-Vacuum Pump | `#E8A020` | 50 mTorr -> base vacuum | Turbomolecular pump. PECVD: < 10^-5 Torr. Arc: < 10^-6 Torr. 30--90 min. |
| 4 | Leak Rate Check | `#E8A020` | < 2 x 10^-5 Torr-L/s acceptable | Isolate pump; monitor pressure rise over 5 min. If fail: check O-rings, feedthroughs, gas lines. |
| 5 | Substrate Heating (if req.) | `#E8A020` | 80--200 C target (PECVD) | Radiant or resistive heaters. Stabilize 10--15 min. Not always required -- depends on recipe. |
| 6 | Ar+ Ion Etch | `#E05C5C` | -400 to -800 V bias, 5--20 min | CRITICAL. Removes oxide layer. Activates surface. Creates micro-roughness for interlayer bonding. |

Step number: Barlow Condensed ExtraBold, 22 pt, accent color.
Name: Barlow SemiBold, 18 pt, `#F0EDE8`.
Parameters: JetBrains Mono Regular, 13 pt, `#F0EDE8`.
Detail: Inter Regular, 12 pt, `#F0EDE8` at 70%.

Arrows: 3 pt `#3A4055`, filled down.

---

### ZONE 3 -- PECVD vs. Arc Comparison

**Section label:** `TWO SYSTEMS -- TWO VACUUM REQUIREMENTS` -- Y: 15.2".

**BLOCK D -- Side-by-Side**

Y: 15.8" to 20.8".

**Left -- PECVD System (X: 0.5", W: 11.0"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#2EC4B6`
- Title: `PECVD SYSTEM` -- Barlow SemiBold, 20 pt, `#2EC4B6`
- Properties (JetBrains Mono 13 pt `#F0EDE8`):

| Parameter | Value |
|---|---|
| Base vacuum | < 10^-5 Torr |
| Working pressure | 100--500 mTorr |
| Power | RF 13.56 MHz, 200--800 W |
| Substrate bias | -200 to -400 V (self-bias) |
| Process gas | C2H2 + Ar |
| DLC type produced | a-C:H (hydrogenated) |
| Substrate temp | 80--150 C |

**Right -- Filtered Cathodic Arc System (X: 12.0", W: 11.5"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E8A020`
- Title: `FILTERED ARC SYSTEM` -- Barlow SemiBold, 20 pt, `#E8A020`
- Properties:

| Parameter | Value |
|---|---|
| Base vacuum | < 10^-6 Torr |
| Working pressure | < 1 mTorr (arc in vacuum) |
| Power | Arc: 40--100 A, 20--30 V |
| Substrate bias | -50 to -2000 V |
| Process gas | None (solid C cathode) |
| DLC type produced | ta-C (hydrogen-free) |
| Substrate temp | RT--150 C |

---

### ZONE 4 -- Ion Etch Parameters

**Section label:** `THE ION ETCH -- WHERE ADHESION BEGINS` -- Y: 21.2".

**BLOCK E -- Etch Detail**

Y: 21.8" to 26.8".

**Main etch parameter panel (X: 0.5", W: 15.0", H: 4.8"):**
- Rounded rect, fill `#1E2435`, left accent `#E05C5C`
- Title: `ARGON ION ETCH` -- Barlow SemiBold, 22 pt, `#E05C5C`

| Parameter | Value |
|---|---|
| Gas | Ar (argon) |
| Pressure | 1--5 mTorr |
| Substrate bias | -400 to -800 V (PECVD) / -800 to -1200 V (arc) |
| Duration | 5--20 min |
| Mechanism | Ar+ ions bombard substrate, sputtering away surface oxide and contaminants |
| Result | Clean, activated metal surface with micro-roughness for interlayer adhesion |
| Temperature rise | Monitor -- bias heating can raise substrate 50--100 C |

JetBrains Mono 13 pt for values. Inter Regular 12 pt for mechanism/result.

**Right callout (X: 16.0", W: 7.5", H: 4.8"):**
- Rounded rect, fill `#E05C5C` at 15%, border 1 pt `#E05C5C`
- Title: `SKIP THE ETCH = LOSE THE COATING` -- Barlow SemiBold, 16 pt, `#E05C5C`
- Text: `The Ar+ ion etch is the single most important adhesion step in the entire DLC process. It removes the invisible native oxide that blocks bonding between the interlayer and substrate. Insufficient etch time or low bias voltage = delamination within days.` -- Inter Regular, 13 pt, `#F0EDE8`

---

### ZONE 5 -- Pre-Run Checklist

**Section label:** `PRE-RUN VACUUM SYSTEM CHECK` -- Y: 27.2".

**BLOCK F -- Checklist**

Y: 27.8" to 32.3". Two columns.

**Left column:**
1. `O-rings inspected -- no cracks, debris, or flat spots`
2. `Chamber interior clean -- no flaking from previous runs`
3. `Gas lines purged -- no moisture or air contamination`
4. `Leak rate within spec (< 2 x 10^-5 Torr-L/s)`

**Right column:**
5. `Pump oil level checked (rotary vane)`
6. `Turbo pump at operating speed before opening gate valve`
7. `Substrate thermocouple functional and calibrated`
8. `Bias power supply tested -- interlock verified`

Each item: Rounded rect row, H: 1.0", fill `#1E2435`, left accent `#E8A020`.

---

### ZONE 6 -- Footer

Standard. Title: `Vacuum / Plasma Setup -- DLC`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Vacuum Plasma Setup DLC -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The ion etch callout (Zone 4) is the emotional center of this poster. Every DLC failure story starts with either poor cleaning or insufficient ion etching. The PECVD vs. Arc comparison (Zone 3) helps operators understand that these are fundamentally different systems with different vacuum requirements -- a PECVD system at 10^-5 Torr is a different world from a filtered arc at 10^-6 Torr.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #444 -- Construction Workup v1.0*
*2026-04-26*
