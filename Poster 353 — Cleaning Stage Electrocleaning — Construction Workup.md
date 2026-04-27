---
Project: Plating Posters Inc
Poster Number: 353
Title: "Cleaning Stage -- Electrocleaning"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Chemical Treatment Clusters -- Watson Research Brief (CT-2.4)"
Technical Source: Industry-standard operating parameters and electrochemistry for the electrocleaning stage. Covers anodic, cathodic, and periodic reverse modes, current density ranges, gas evolution mechanisms, and common failures.
Process Scope: Electrocleaning treatment stage -- operating parameters, mode selection, and diagnostics
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Electrocleaning
  - CleaningStage
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT02
---

# Poster #353 -- Construction Workup
## Cleaning Stage -- Electrocleaning

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Poster 4 of 7 in the CT-02 cluster. This is the "main tank" poster -- the electrocleaning operation itself. The hero visual is a gas evolution mechanism diagram showing the electrochemical reactions at the cathode and anode. The mode selection table is the heart of this poster -- it is the detailed version of the mode comparison introduced in the overview poster (350). The immersion time table covers substrate-specific limits, and the failure/fix table covers the five most common electrocleaning problems.

This is the densest poster in the CT-02 cluster. A technician troubleshooting poor adhesion should be able to look at this poster and determine whether the electrocleaning mode, current density, or time is the culprit.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Gas evolution diagram (Block B -- HERO):** Split visual -- left side shows cathodic reaction (H2 generation), right side shows anodic reaction (O2 generation). Text-based chemistry diagrams using rectangles, arrows, and labels.
2. **Mode selection decision table (Block D):** When to use anodic, cathodic, or periodic reverse, with substrate-specific recommendations.
3. **Immersion time by substrate (Block E):** Four-substrate table.
4. **Failure/fix table (Block F):** Five common electrocleaning failures.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.5" / 22.0" / 27.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Poster 4 of 7 highlighted (Amber -- main step)
ZONE 3 -- GAS EVOLUTION MECHANISM / HERO (4.2"--15.5" / ~11.3")
ZONE 4 -- MODE SELECTION DECISION TABLE (15.5"--22.0" / ~6.5")
ZONE 5 -- IMMERSION TIME BY SUBSTRATE (22.0"--27.5" / ~5.5")
ZONE 6 -- COMMON FAILURES (27.5"--32.5" / ~5.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `THE CLEANING STAGE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Electrocleaning -- Gas Bubbles Do the Heavy Lifting` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Hydrogen at the cathode, oxygen at the anode. Both scrub the surface. Choose your mode based on substrate, hardness, and downstream process.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Poster 4 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Soak-cleaned parts with residual trace contamination --> After: Pristine surface with all monolayer films, smut, and particles removed`

---

### ZONE 3 -- Gas Evolution Mechanism (HERO)

**Section label:** `HOW ELECTROCLEANING ACTUALLY WORKS -- THE ELECTROCHEMISTRY` -- Y: 4.4".

**Two-column hero (Y: 5.0" to 15.0"):**

**Left -- Cathodic Reaction (X: 0.5", W: 11.0"):**

Rounded rect H: 9.5", fill `#1E2435`, left accent 0.06" `#E05C5C`.

Title: `CATHODIC (Work = Cathode -)` Barlow Condensed ExtraBold 24 pt `#E05C5C`.
Subtitle: `Hydrogen Evolution at the Workpiece` Barlow SemiBold 16 pt `#F0EDE8` at 60%.

**Reaction diagram (Y: 6.0" to 8.5"):**

Three boxes connected by arrows:

| Box | Content | Color |
|---|---|---|
| Reactant | `2H2O + 2e-` | `#2EC4B6` |
| Arrow | `-->` | `#3A4055` |
| Product | `H2 (gas)` `+ 2OH-` | `#E05C5C` |

Each box: Rounded rect W: 3.0", H: 2.0", fill `#252B3D`.
Text: JetBrains Mono 14 pt.

**Key points below diagram:**
- Inter Regular 13 pt `#F0EDE8`, line height 155%:
```
- More gas volume than anodic (2x per mole of electrons)
- Aggressive mechanical scrubbing action
- RISK: Hydrogen embrittlement on high-strength steel
- RISK: Cathodic smut -- dissolved metals plate onto work
- NEVER use as final step before nickel plating
```

**Right -- Anodic Reaction (X: 12.0", W: 11.5"):**

Rounded rect H: 9.5", fill `#1E2435`, left accent 0.06" `#27AE60`.

Title: `ANODIC (Work = Anode +)` Barlow Condensed ExtraBold 24 pt `#27AE60`.
Subtitle: `Oxygen Evolution at the Workpiece` Barlow SemiBold 16 pt `#F0EDE8` at 60%.

**Reaction diagram:**

| Box | Content | Color |
|---|---|---|
| Reactant | `2OH-` | `#2EC4B6` |
| Arrow | `-->` | `#3A4055` |
| Product | `H2O + 1/2 O2 (gas)` `+ 2e-` | `#27AE60` |

**Key points:**
```
- Less gas volume but larger O2 bubbles
- Effective scrubbing with lower explosion risk
- Slight metal dissolution -- exposes fresh surface
- NO hydrogen embrittlement risk
- NO cathodic smut
- REQUIRED as final step before nickel plating
```

**Bottom callout spanning both columns (Y: 14.5"):**
- Rounded rect W: 23.0", H: 0.8", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- `Periodic Reverse (PR) alternates cathodic and anodic -- gets the aggressive cathodic scrub followed by the anodic finish. Typical cycle: 10 sec cathodic / 10 sec anodic.` Inter Medium 13 pt `#E8A020`

---

### ZONE 4 -- Mode Selection Decision Table

**Section label:** `WHICH MODE? -- MATCH TO YOUR APPLICATION` -- Y: 15.7".

**BLOCK D -- Decision Table (Y: 16.3" to 21.8")**

Column widths (23.0" total):
- Application (5.5") | Recommended Mode (4.5") | Current Density (4.5") | Voltage (3.0") | Time (3.0") | Key Note (2.5")

Header row: fill `#3A4055`, H: 0.5". Barlow SemiBold 13 pt.

| Application | Mode | CD (ASF / A/dm2) | Voltage | Time | Note |
|---|---|---|---|---|---|
| Steel before Ni/Cr plate | ANODIC | 30-75 / 3.2-8.1 | 6-12 V | 60-120 sec | REQUIRED anodic before Ni |
| Steel -- heavy soil | CATHODIC then ANODIC | 20-50 / 2.2-5.4 | 6-9 V | 30-60 sec each | Final phase MUST be anodic |
| High-strength steel (>40 HRC) | ANODIC ONLY | 20-50 / 2.2-5.4 | 6-9 V | 30-60 sec | NO cathodic -- H embrittlement |
| Copper / brass | ANODIC | 20-40 / 2.2-4.3 | 6-9 V | 30-90 sec | Light touch -- avoid dissolution |
| Zinc die cast | ANODIC | 10-30 / 1.1-3.2 | 3-6 V | 15-30 sec | VERY short -- alkaline attack |
| Highly polished surfaces | CATHODIC | 20-50 / 2.2-5.4 | 6-9 V | 30-60 sec | When anodic etch is unacceptable |
| General / difficult soils | PERIODIC REVERSE | 20-50 / 2.2-5.4 | 6-12 V | 60-120 sec total | Best overall; final phase anodic |

Data: JetBrains Mono 12 pt. Mode names color-coded: ANODIC `#27AE60`, CATHODIC `#E05C5C`, PERIODIC REVERSE `#2EC4B6`.
"REQUIRED", "NO cathodic" in bold accent colors.

---

### ZONE 5 -- Immersion Time by Substrate

**Section label:** `TIME LIMITS -- SUBSTRATE SENSITIVITY` -- Y: 22.2".

**BLOCK E -- Four-Substrate Cards (Y: 22.8" to 27.3")**

Four side-by-side callout boxes.

| Substrate | X | W | Accent | Time | Caution |
|---|---|---|---|---|---|
| Steel / Iron | 0.5" | 5.5" | `#2EC4B6` | 30-120 sec standard; up to 3 min heavy soil | Most forgiving. Limit cathodic time on >40 HRC. |
| Copper / Brass | 6.25" | 5.5" | `#27AE60` | 30-90 sec | Anodic mode can dissolve thin flash copper. Use light current. |
| Zinc Die Cast | 12.0" | 5.5" | `#E05C5C` | 15-30 sec MAX | Alkaline dissolution risk. Keep current density LOW and time SHORT. |
| Stainless Steel | 17.75" | 5.75" | `#E8A020` | 30-90 sec | May require higher CD (50-75 ASF) for passive film removal. |

Each box: Rounded rect H: 4.0", fill `#1E2435`, left accent 0.06".
Substrate name: Barlow SemiBold 16 pt, accent color.
Time: JetBrains Mono 14 pt `#F0EDE8`.
Caution: Inter Regular 12 pt, accent or `#E05C5C` for warnings.

---

### ZONE 6 -- Common Failures

**Section label:** `WHAT GOES WRONG -- 5 COMMON FAILURES` -- Y: 27.7".

**BLOCK F -- Failure Table (Y: 28.3" to 32.3")**

| Failure | Cause | Fix |
|---|---|---|
| Adhesion failure after plating | Cathodic smut from dissolved metals; cathodic mode used as final step before nickel | Switch to anodic for final step; carbon treat bath to remove organics; check metal contamination |
| Hydrogen embrittlement | Cathodic cleaning on high-strength steel (>40 HRC); excessive cathodic time | Use anodic ONLY for >40 HRC; bake 375 +/- 25 F within 4 hrs per ASTM B850 |
| Etching / pitting | Chloride contamination (>10 g/L); low alkalinity; excessive voltage | Titrate chlorides; maintain alkalinity; reduce voltage; partial dump if chlorides high |
| No gas evolution (dead tank) | Open circuit; bad bus bar contact; blown fuse; rack tips corroded | Check electrical connections; clean rack tips; verify rectifier output with ammeter |
| Excessive foam / overflow | Surfactant overdose; oil drag-in from upstream soak cleaner | Reduce surfactant; improve soak cleaner maintenance; use low-foam grade |

Each row: Rounded rect H: 0.7", alternating fills.
Failure: Barlow SemiBold 14 pt `#E05C5C`. Cause: Inter Regular 12 pt `#F0EDE8`. Fix: Inter Medium 12 pt `#27AE60`.

---

### ZONE 7 -- Footer

Standard. Title: `Cleaning Stage -- Electrocleaning`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; ASTM B850/B849 (hydrogen embrittlement); Metal Finishing Guidebook. Mode selection and current density depend on substrate, soil type, and downstream process. Consult your process supplier for application-specific guidance.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cleaning Stage Electrocleaning -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The gas evolution hero diagram is the unique visual for this poster -- it makes the invisible (electrochemical reactions) visible. The cathodic vs. anodic split layout mirrors the choice operators face every time they set up the rectifier. The mode selection table is the most detailed reference on this poster and the most frequently consulted -- an engineer specifying a new plating line should be able to read this table and write the mode into the process spec. The five failure entries cover the complete diagnostic space for electrocleaning problems.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #353 -- Construction Workup v1.0*
*2026-04-26*
