---
Project: Plating Posters Inc
Poster Number: 108
Title: "Copper (Alkaline) -- Main Tank"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-10 technical reference (alkaline non-cyanide copper)"
  - "Watson Research Brief -- Electroplating Clusters"
Technical Source: Alkaline non-cyanide copper main tank. Two bath types -- copper pyrophosphate (pH 8-9, Cu2P2O7 53-84 g/L, P2O7:Cu ratio 7:1 to 8:1, 70-90% CE) and copper HEDP/chelant (pH 9-13, Cu 5-30 g/L, 30-70% CE). Operates at 100-160 F, 5-80 ASF. Strike at high pH (12-13) with live entry for active metals. The cyanide-free alternative that makes everything downstream possible.
Process Scope: Main plating tank for alkaline non-cyanide copper (Stage 5 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - CopperPlating
  - AlkalineCopper
  - NonCyanide
  - MainTank
  - ConstructionWorkup
  - Series2
  - ClusterEP10
---

# Poster #108 -- Construction Workup
## Copper (Alkaline) -- Main Tank

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 5 of 8. This is the heart of the EP-10 cluster -- the alkaline non-cyanide copper plating bath. Two distinct bath types exist: copper pyrophosphate (the older, well-proven system) and copper HEDP/chelant (the newer, simpler system that directly replaces cyanide copper strike). Both hold copper in solution at alkaline pH using complexants, preventing the immersion deposition that makes acid copper unusable on active metals.

The critical concept for this poster is "live entry" -- current must be applied to the part BEFORE it enters the solution. At pH 12--13, the alkaline bath can plate directly onto steel without immersion displacement. But if the part enters without current, even a moment of contact with the alkaline copper solution at lower pH can deposit a thin, non-adherent immersion copper layer. That layer is the kiss of death for adhesion.

Hero visual: side-by-side bath comparison (pyrophosphate vs. HEDP) with live entry callout as the centerpiece safety/quality element.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Dual bath comparison hero (Block B):** Side-by-side pyrophosphate vs. HEDP/chelant.
2. **Live entry callout (Block C):** Critical technique explanation.
3. **Operating parameter tables (Block D).**
4. **Defect table (Block E).**
5. **Analytical methods + anode management (Block F, G).**
6. **Orientation strip:** Stage 5 highlighted (Emerald).

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 5 highlighted (Emerald)
ZONE 3 -- DUAL BATH COMPARISON + LIVE ENTRY (4.2"--14.5" / ~10.3")
  Block B: Pyrophosphate vs. HEDP side-by-side
  Block C: Live entry callout
ZONE 4 -- OPERATING PARAMETERS + DEFECTS (14.5"--20.5" / ~6.0")
  Block D: Operating parameter table
  Block E: Common defects
ZONE 5 -- ANALYTICAL METHODS + ANODE MANAGEMENT (20.5"--27.0" / ~6.5")
  Block F: Analytical methods
  Block G: Anode management
ZONE 6 -- CONTAMINATION + SAFETY (27.0"--32.5" / ~5.5")
  Block H: Contamination and bath maintenance
  Block I: Safety
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `COPPER (ALKALINE) MAIN TANK` -- Barlow Condensed ExtraBold, 72 pt, `#F0EDE8`, letter spacing -4. X: 0.5", Y: 0.5".

**Subheading:** `Alkaline Non-Cyanide -- Stage 5 of 8 -- The Cyanide-Free Copper Strike` -- Barlow SemiBold, 30 pt, `#27AE60`. X: 0.5", Y: 1.3".

**Tagline:** `Two bath types. One mission: get an adherent copper layer on active metals without cyanide. Live entry is non-negotiable.` -- Barlow SemiBold, 18 pt, `#F0EDE8` at 65%. X: 0.5", Y: 2.0", W: 23.0".

---

### ZONE 2 -- Orientation Strip

Stage 5 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Activated, rinsed surface  -->  After: Adherent copper strike layer (0.1--0.3 mil)`

---

### ZONE 3 -- Dual Bath Comparison + Live Entry

**Section label:** `TWO BATH TYPES -- ONE PURPOSE` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Side-by-Side Bath Comparison**

Y: 5.0" to 11.0".

**Left -- Copper Pyrophosphate (X: 0.5", W: 11.0", H: 5.5"):**

Rounded rect, fill `#1E2435`, border 2 pt `#E8A020`.
Title: `COPPER PYROPHOSPHATE` Barlow Condensed ExtraBold 22 pt `#E8A020`
Subtitle: `The Proven System` Inter Medium 13 pt `#E8A020` at 60%

| Component | Concentration |
|---|---|
| Copper pyrophosphate (Cu2P2O7) | 53--84 g/L (7--11 oz/gal) |
| Potassium pyrophosphate (K4P2O7) | 200--350 g/L (27--47 oz/gal) |
| Ammonium hydroxide (NH4OH) | 1--5 mL/L |
| Potassium nitrate (KNO3) | 5--15 g/L |
| Copper metal (as Cu) | 22--34 g/L |
| P2O7:Cu ratio | 7:1 to 8:1 (critical control) |

JetBrains Mono 11 pt `#F0EDE8`.

Key parameters below table:
- `pH: 8.0--9.0` / `Temp: 100--140 F (38--60 C)` / `CD: 10--80 ASF` / `CE: 70--90%`
- `Anode: copper (OFHC or phosphorized)` JetBrains Mono 11 pt `#E8A020`

**Right -- Copper HEDP / Chelant (X: 12.0", W: 11.5", H: 5.5"):**

Rounded rect, fill `#1E2435`, border 2 pt `#27AE60`.
Title: `COPPER HEDP / CHELANT` Barlow Condensed ExtraBold 22 pt `#27AE60`
Subtitle: `The Modern Replacement` Inter Medium 13 pt `#27AE60` at 60%

| Component | Concentration |
|---|---|
| Copper (as Cu metal) | 5--30 g/L |
| HEDP (chelant) | 50--100 g/L |
| Auxiliary chelant (citrate/tartrate) | 10--30 g/L |
| NaOH or KOH | 30--80 g/L |
| Conductive salt (K2CO3 or KNO3) | 15--30 g/L |

JetBrains Mono 11 pt `#F0EDE8`.

Key parameters below table:
- `pH: 9.0--13.0 (strike at 12--13)` / `Temp: 100--160 F (38--71 C)` / `CD: 5--30 ASF` / `CE: 30--70%`
- `Anode: copper (OFHC) or insoluble (MMO/platinized Ti)` JetBrains Mono 11 pt `#27AE60`

**BLOCK C -- Live Entry Callout**

Y: 11.5" to 14.3".

Rounded rect, full width, H: 2.5", fill `#E05C5C` at 10%, border 2 pt `#E05C5C`, radius 8.
Title: `LIVE ENTRY -- THE MOST IMPORTANT TECHNIQUE IN THIS BATH` Barlow Condensed ExtraBold, 22 pt, `#E05C5C`

Two-column interior:

**Left -- What It Means:**
- `Current must be ON before the part touches the solution.`
- `Connect the part to the cathode bar above the solution.`
- `Apply current (initial strike CD: 20--30 ASF for pyro; 15--20 ASF for HEDP).`
- `Lower part into the bath while current is flowing.`
- `This prevents immersion copper from forming on contact.`
Barlow SemiBold 13 pt for first bullet, Inter Regular 12 pt for rest. `#F0EDE8`.

**Right -- Why It Matters:**
- `Without current, Cu2+ ions displace substrate metal (steel, zinc) on contact.`
- `This immersion copper is thin, powdery, and NON-ADHERENT.`
- `Everything plated on top will peel.`
- `Live entry ensures the first atomic layers of copper are electrodeposited, not immersion deposited.`
- `At pH > 12 (HEDP strike), the risk is lower -- but live entry is still best practice.`
Inter Regular 12 pt `#F0EDE8`. "NON-ADHERENT" in `#E05C5C`.

---

### ZONE 4 -- Operating Parameters + Defects

**Section label:** `OPERATING PARAMETERS AND COMMON DEFECTS` -- Y: 14.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK D -- Operating Parameter Comparison Table**

Y: 15.3" to 17.8".

| Parameter | Pyrophosphate | HEDP / Chelant |
|---|---|---|
| Temperature | 100--140 F (38--60 C); typical 120--130 F | 100--160 F (38--71 C); typical 120--140 F |
| pH | 8.0--9.0 | 9.0--13.0; strike at pH 12--13 |
| Cathode CD | 10--80 ASF; typical 20--40 ASF | 5--30 ASF; typical 10--20 ASF |
| Voltage | 3--8 V | 3--8 V |
| Agitation | Air or mechanical | Air or mechanical |
| Anode:cathode ratio | 1:1 to 2:1 | 1:1 to 2:1 |
| Cathodic efficiency | 70--90% | 30--70% (varies with CD) |
| Deposit quality | Semi-bright, good leveling | Matte to semi-bright |
| Plating time (strike) | 1--5 min (0.1--0.3 mil) | 1--5 min (0.1--0.3 mil) |

JetBrains Mono 11 pt `#F0EDE8`. Headers: Barlow SemiBold 13 pt on `#3A4055`.

**BLOCK E -- Common Defects**

Y: 18.2" to 20.3".

| Defect | Cause | Corrective Action |
|---|---|---|
| No adhesion on steel | pH too low; no live entry; immersion Cu formed | Raise pH to 12+ for strike; ensure live entry |
| Immersion copper (powdery) | Part entered bath without current at low pH | Use live entry; increase strike CD |
| Dull deposits | Low temperature; depleted organic additives | Raise temp; replenish additives per TDS |
| Roughness | Particulates; orthophosphate buildup (pyro bath) | Filter; monitor ortho:pyro ratio |
| Poor throwing power (pyro) | P2O7:Cu ratio out of range | Correct ratio to 7:1--8:1 |

Cards: fill `#1E2435`, alternating `#252B3D`. Defect: `#E05C5C`. Cause: `#F0EDE8`. Fix: `#27AE60`.

---

### ZONE 5 -- Analytical Methods + Anode Management

**Two-column layout (Y: 20.7" to 26.8"):**

**Left -- Analytical Methods (X: 0.5", W: 14.0"):**

Section label: `ANALYTICAL CONTROL` Barlow Condensed ExtraBold 22 pt `#F0EDE8`.

Callout box, fill `#1E2435`, left accent `#2EC4B6`:

| Analysis | Method |
|---|---|
| Copper metal | Iodometric titration (Na2S2O3 / starch) or EDTA |
| Free pyrophosphate (pyro bath) | Acid titration method |
| pH | Calibrated pH meter |
| P2O7:Cu ratio (pyro) | Calculate from Cu and P2O7 analyses |
| Orthophosphate (pyro) | Spectrophotometric (molybdate blue) |
| Hull cell | 267 mL, 1--2A, 5--10 min at bath temp |
| Temperature | Thermometer or RTD probe |

Inter Regular 12 pt `#F0EDE8`. Method values: JetBrains Mono 11 pt.

Below: `P2O7:Cu ratio is the primary control parameter for pyrophosphate baths. For HEDP baths, pH and Cu metal are the primary controls -- chelant concentration is usually maintained by replenishment per TDS.` Inter Medium 12 pt `#E8A020`.

**Right -- Anode Management (X: 15.5", W: 8.0"):**

Section label: `ANODES` Barlow Condensed ExtraBold 18 pt `#E8A020`.

Rounded rect, fill `#1E2435`, border 1 pt `#E8A020`:

**Pyrophosphate bath:**
- `OFHC copper or phosphorized copper`
- `Anode bags: polypropylene (mandatory -- prevents particle shedding)`
- `Anode:cathode ratio: 1:1 to 2:1`
- `Monitor anode film: should be smooth dark brown`

**HEDP / Chelant bath:**
- `OFHC copper (soluble) OR insoluble (MMO/platinized Ti)`
- `Insoluble anodes require Cu replenishment via CuSO4 or CuCO3`
- `Anode bags on soluble anodes`
- `Anode:cathode ratio: 1:1 to 2:1`

Inter Regular 11 pt `#F0EDE8`.

---

### ZONE 6 -- Contamination + Safety

**Two-column layout (Y: 27.2" to 32.3"):**

**Left -- Contamination and Bath Maintenance (X: 0.5", W: 14.0"):**

Section label: `CONTAMINATION AND MAINTENANCE` Barlow Condensed ExtraBold 20 pt `#F0EDE8`.

| Contaminant | Threshold | Effect | Remedy |
|---|---|---|---|
| Orthophosphate (pyro bath) | > 100 g/L | Roughness, reduced throwing power | Partial dump; prevent by maintaining pH > 8 and temp < 140 F |
| Iron | > 50 ppm | Dark deposits, pitting | Carbon treatment + filtration |
| Organic contamination | Any significant | Dull deposits, pitting | Activated carbon treatment (1--3 g/L, stir, filter) |
| Chloride | > 50 ppm (pyro) | Pitting | Dilute or silver chloride precipitation |
| Acid drag-in | pH drop | Complexant decomposition; immersion Cu | Improve pre-plate rinse; readjust pH with NaOH/KOH |

JetBrains Mono 10 pt `#F0EDE8`.

**Right -- Safety (X: 15.5", W: 8.0"):**

Rounded rect, fill `#1E2435`, border 1 pt `#2EC4B6`, radius 8.
Title: `SAFETY` Barlow Condensed ExtraBold 18 pt `#2EC4B6`
Body (Inter Regular 12 pt `#F0EDE8`, line height 150%):

> - NO CYANIDE -- this is the primary safety advantage.
> - Alkaline solution (pH 8--13): caustic burn hazard at high pH.
> - PPE: chemical splash goggles, rubber gloves, apron.
> - Copper compounds: toxic by ingestion; aquatic toxicity -- do not discharge.
> - Wastewater: copper precipitation at pH 8.5--9.5.
> - HEDP/pyrophosphate are chelants -- they keep copper in solution through standard hydroxide precipitation. May require sulfide precipitation, electrowinning, or ion exchange to meet Cu discharge limits.
> - Heated bath: burn hazard from hot solution (up to 160 F).

---

### ZONE 7 -- Footer

Standard footer. Title: `Copper (Alkaline) -- Main Tank`. Version `v1.0 -- 2026`.

Disclaimer: `This poster covers alkaline non-cyanide copper plating. Bath compositions shown are typical industry ranges. Proprietary formulations vary -- consult your process supplier's TDS for specific operating parameters. Cyanide copper processes are NOT covered here.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table (see Poster #103).
**Export:** Six files -- `Copper Alkaline Main Tank -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the most chemistry-dense poster in the EP-10 cluster, and it earns that density. Two distinct bath formulations side by side, each with its own control parameters -- the dual-panel layout is the right call here, same pattern used in Poster #92 for conventional vs. high-concentration hard chrome.

The live entry callout (Block C) is the teaching moment. Every experienced plater knows about live entry, but it's rarely explained well on shop reference material. The "what it means" / "why it matters" split makes it actionable for operators who've never heard the term, and a refresher for those who have.

Watson's brief: "Can plate directly on steel at high pH (>12) without immersion displacement." "No adhesion on steel: pH too low (immersion copper forms), insufficient CD at start -- raise pH for strike step, ensure live entry (current on before part enters)."

-> Watson: Confirm typical orthophosphate limit for copper pyrophosphate baths (I have > 100 g/L from domain knowledge). Also confirm HEDP chelant concentration range (50--100 g/L) against published sources.

-> Tyler: Validate Hull cell parameters for alkaline non-CN copper (267 mL, 1--2A, 5--10 min). Tyler's lab experience with A Brite's alkaline copper products would be especially valuable here.

---

*Alaina -- Poster #108 -- Construction Workup v1.0 -- 2026-04-26*
