---
Project: Plating Posters Inc
Poster Number: 350
Title: "Electrocleaning -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Chemical Treatment Clusters — Watson Research Brief (CT-2)"
Technical Source: Industry-standard electrolytic cleaning process. Covers the complete 7-poster sequence for the CT-02 cluster. Values are typical ranges for NaOH-based electrocleaning with anodic, cathodic, and periodic reverse modes.
Process Scope: Electrocleaning -- complete process flow (cluster overview)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Electrocleaning
  - ProcessFlow
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT02
---

# Poster #350 -- Construction Workup
## Electrocleaning -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for CT-02: Electrocleaning. It shows the complete process sequence from soak clean through electroclean to acid activation, and introduces the critical anodic vs. cathodic decision that dominates this cluster. An operator sees the full flow, a supervisor understands mode selection, a quality engineer sees where adhesion failures originate.

Design philosophy: linear flow diagram as the hero with a prominent mode selection decision tree integrated into the flow, a comparison callout (anodic vs. cathodic vs. periodic reverse), and a troubleshooting quick-hit strip.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Process flow with mode decision (Block B -- HERO):** Linear flow diagram incorporating a decision diamond for anodic/cathodic/PR mode selection.
2. **Mode comparison table (Block D):** Three-mode comparison (anodic, cathodic, periodic reverse).
3. **"Why Electroclean?" callout (Block E):** What electrocleaning does that soak cleaning cannot.
4. **Troubleshooting quick-hit strip (Block F):** 4 common failures.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 15.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")

ZONE 2 -- PROCESS FLOW DIAGRAM / HERO (2.9"--15.5" / ~12.6")
  Block B: Five-stage flow with mode decision diamond
  Block C: Mode legend strip

ZONE 3 -- MODE COMPARISON TABLE (15.5"--22.0" / ~6.5")
  Block D: Anodic vs. Cathodic vs. Periodic Reverse

ZONE 4 -- WHY ELECTROCLEAN? (22.0"--28.5" / ~6.5")
  Block E: Soak clean vs. electroclean comparison

ZONE 5 -- TROUBLESHOOTING QUICK HITS (28.5"--32.5" / ~4.0")
  Block F: 4 common failures

ZONE 6 -- FOOTER BAND (32.5"--36.0")
  Block G: Standard footer
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**BLOCK A -- Headline**
- Position: X: 0.5". Y: 0.5"
- Font: Barlow Condensed ExtraBold, 88 pt, `#F0EDE8`, letter spacing -4
- Text: `ELECTROCLEANING`

**BLOCK A -- Subheading**
- Y: 1.5". Barlow SemiBold, 36 pt, `#2EC4B6` (Teal)
- Text: `Complete Process Flow -- The Final Clean Before Plating`

**BLOCK A -- Tagline**
- Y: 2.2". Barlow SemiBold, 22 pt, `#F0EDE8` at 65%
- Text: `Gas bubbles do what chemistry alone cannot. Electrocleaning is the difference between good cleaning and perfect cleaning.`

---

### ZONE 2 -- Process Flow Diagram (HERO)

**Section label:** `THE ELECTROCLEANING PROCESS -- FLOW AND MODE SELECTION` -- Y: 3.1". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK B -- Five-Stage Flow with Decision (Y: 3.8" to 14.0")**

**Top Row (Y: 3.8" to 7.8") -- Stages 1-3:**

| Stage | Box | X | W | Top Accent | Type |
|---|---|---|---|---|---|
| 1. Soak Clean (Prior Step) | Box 1 | 0.5" | 5.0" | `#3A4055` (Slate) | Prior |
| 2. Rinse | Box 2 | 6.5" | 4.0" | `#2EC4B6` (Teal) | Rinse |
| 3. Electroclean | Box 3 | 11.5" | 6.0" | `#E8A020` (Amber) | Main Step |

Each box: Rounded rect H: 3.5", fill `#1E2435`, radius 8, top accent 4 pt.

*Box 1 -- Soak Clean:*
- Badge: `PRIOR STEP`, fill `#3A4055`
- Name: `Soak Clean`
- Note: `Bulk soil removal complete` / `See Posters #343-349`

*Box 2 -- Rinse:*
- Badge: `RINSE`, fill `#2EC4B6`
- Name: `Rinse`
- Parameters: `Ambient | 30-60 sec`
- Note: `Remove alkaline cleaner before electroclean`

*Box 3 -- Electroclean:*
- Badge: `MAIN STEP`, fill `#E8A020`
- Name: `Electroclean`
- Parameters: JetBrains Mono 13 pt:
```
3-10 A/dm2 (30-100 ASF)
4-12 V DC
30 sec - 3 min
120-175 F (50-80 C)
```
- Check: `SELECT MODE -->` Barlow SemiBold 14 pt `#E8A020` (arrow to decision diamond)

**Mode Selection Decision Diamond (Y: 8.5", center X: 14.5"):**

Diamond W: 5.0", H: 2.5", fill `#E8A020` at 20%, border 2 pt `#E8A020`.
Text: `SELECT MODE` Barlow SemiBold 18 pt `#E8A020`

Three branches:

| Branch | Direction | Label | Destination |
|---|---|---|---|
| Anodic | Left | `ANODIC (+)` `#27AE60` | Box 4A |
| Cathodic | Right | `CATHODIC (-)` `#E05C5C` | Box 4B |
| PR | Down | `PERIODIC REVERSE` `#2EC4B6` | Box 4C |

**Three mode boxes (Y: 11.5" to 14.0"):**

*Box 4A -- Anodic (X: 0.5", W: 7.0"):*
- Fill `#1E2435`, left accent 0.06" `#27AE60`
- Title: `ANODIC` Barlow SemiBold 18 pt `#27AE60`
- Subtitle: `Work = Anode (+)` JetBrains Mono 13 pt `#27AE60`
- Body: `O2 at surface | No H embrittlement | Required before Ni`
- Tag: `PREFERRED FOR MOST PLATING` Inter Medium 12 pt `#27AE60`

*Box 4B -- Cathodic (X: 8.5", W: 7.0"):*
- Fill `#1E2435`, left accent 0.06" `#E05C5C`
- Title: `CATHODIC` Barlow SemiBold 18 pt `#E05C5C`
- Subtitle: `Work = Cathode (-)` JetBrains Mono 13 pt `#E05C5C`
- Body: `H2 at surface | Aggressive scrub | Risk: H embrittlement + smut`
- Tag: `HEAVY SOIL ONLY -- NEVER FINAL STEP BEFORE Ni` Inter Medium 12 pt `#E05C5C`

*Box 4C -- Periodic Reverse (X: 16.5", W: 7.0"):*
- Fill `#1E2435`, left accent 0.06" `#2EC4B6`
- Title: `PERIODIC REVERSE` Barlow SemiBold 18 pt `#2EC4B6`
- Subtitle: `Alternating Polarity` JetBrains Mono 13 pt `#2EC4B6`
- Body: `Cathodic scrub + anodic finish | Best compromise`
- Tag: `FINAL PHASE MUST BE ANODIC` Inter Medium 12 pt `#E8A020`

**All three converge to:**

Arrow down to: `RINSE --> ACID ACTIVATE --> PLATE` (horizontal strip, Y: 14.5")
- Three small boxes: Rinse (`#2EC4B6`) | Acid Activate (`#E8A020`) | Plate (`#27AE60`)

**BLOCK C -- Mode Legend Strip (Y: 14.8" to 15.3")**

Same pattern as Poster 343 legend strip.

| Swatch | Label |
|---|---|
| `#27AE60` | `Anodic (O2 -- Preferred)` |
| `#E05C5C` | `Cathodic (H2 -- Caution)` |
| `#2EC4B6` | `Periodic Reverse (Both)` |
| `#E8A020` | `Decision / Main Step` |

---

### ZONE 3 -- Mode Comparison Table

**Section label:** `ANODIC vs. CATHODIC vs. PERIODIC REVERSE -- THE FULL PICTURE` -- Y: 15.7".

**BLOCK D -- Three-Column Comparison (Y: 16.3" to 21.8")**

Column widths (23.0" total):
- Property (4.0") | Anodic (6.0") | Cathodic (6.0") | Periodic Reverse (7.0")

Header row: fill `#3A4055`, H: 0.5".

| Property | Anodic | Cathodic | Periodic Reverse |
|---|---|---|---|
| Work Polarity | Anode (+) | Cathode (-) | Alternates |
| Gas at Work | O2 (oxygen) | H2 (hydrogen) | Both alternately |
| Gas Volume | Lower (O2) | Higher (H2) -- more scrubbing | Both |
| H Embrittlement Risk | NONE | HIGH on >40 HRC steel | Reduced (anodic final phase) |
| Cathodic Smut Risk | NONE | YES -- dissolved metals plate onto work | Stripped by anodic phase |
| Cleaning Aggressiveness | Moderate | Aggressive | Best overall |
| Pre-Nickel | REQUIRED | NEVER as final step | OK if final phase is anodic |
| Typical Cycle | 60-120 sec | 60-120 sec | 10s cathodic / 10s anodic (or 3:1 ratio) |

Data: JetBrains Mono 12 pt. "NONE" in `#27AE60`. "HIGH" and "YES" in `#E05C5C`. "REQUIRED" in `#27AE60` bold. "NEVER" in `#E05C5C` bold.

---

### ZONE 4 -- Why Electroclean?

**Section label:** `WHY ELECTROCLEAN? -- WHAT SOAK CLEANING CANNOT DO` -- Y: 22.2".

**BLOCK E -- Side-by-Side Comparison (Y: 22.9" to 28.3")**

**Left -- Soak Clean (X: 0.5", W: 11.0"):**
- Rounded rect H: 5.0", fill `#1E2435`, left accent 0.06" `#3A4055`
- Title: `SOAK CLEAN ALONE` Barlow SemiBold 20 pt `#C8D0D8`
- Inter Regular 14 pt `#F0EDE8`:
```
Removes:
  - Bulk oils and greases
  - Drawing compounds
  - Fingerprints
  - Most visible contamination

Cannot remove:
  - Monolayer organic films
  - Embedded smut and particles
  - Oxide films in recesses
  - Contamination trapped in surface roughness
```
- Bottom: `GOOD -- but not good enough for critical plating` Inter Medium 13 pt `#E8A020`

**Right -- Soak Clean + Electroclean (X: 12.0", W: 11.5"):**
- Rounded rect H: 5.0", fill `#1E2435`, left accent 0.06" `#27AE60`
- Title: `SOAK CLEAN + ELECTROCLEAN` Barlow SemiBold 20 pt `#27AE60`
- Inter Regular 14 pt `#F0EDE8`:
```
Soak removes bulk soil THEN
Electroclean removes trace contamination:

  - Gas bubbles physically scrub the surface
  - Anodic dissolution removes a thin metal layer
  - Exposes fresh, active, oxide-free metal
  - Final monolayer contamination eliminated

Result: pristine surface for plating adhesion
```
- Bottom: `THE INDUSTRY STANDARD for decorative Ni/Cr, gold, silver, and all critical deposits` Inter Medium 13 pt `#27AE60`

---

### ZONE 5 -- Troubleshooting Quick Hits

**Section label:** `QUICK TROUBLESHOOTING -- 4 COMMON PROBLEMS` -- Y: 28.7".

**BLOCK F -- Four Problem Cards (Y: 29.4" to 32.3")**

Same layout as Poster 343.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | ADHESION FAILURE | Cathodic smut from dissolved metals; cathodic before nickel | Switch to anodic; carbon treat bath; check metal contamination |
| 2 | 6.33" | H EMBRITTLEMENT | Cathodic cleaning of high-strength steel (>40 HRC) | ALWAYS anodic for HRC >40; bake 375-410 F within 4 hrs per ASTM B849 |
| 3 | 12.16" | UNEVEN GAS | Poor electrical contact; rack tip corrosion; uneven CD | Clean rack tips; check bus bar connections; improve contact |
| 4 | 18.0" | EXCESSIVE FOAM | Surfactant overdose; oil drag-in from soak cleaner | Reduce surfactant; improve soak cleaner maintenance upstream |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

Standard. Title: `Electrocleaning -- Process Flow`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; ASTM B849 (hydrogen embrittlement relief); Metal Finishing Guidebook. Mode selection depends on substrate, downstream process, and soil type. Consult your process supplier.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Electrocleaning Process Flow -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the "map" poster for the Electrocleaning cluster. The mode selection decision diamond integrated into the process flow is the key design choice -- it forces the viewer to confront the anodic/cathodic/PR decision right where it occurs in the actual process sequence. The three-mode comparison table is the reference backbone. The "Why Electroclean?" callout answers the question that justifies this entire cluster's existence. The remaining 6 posters (#351-356) zoom into each aspect.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #350 -- Construction Workup v1.0*
*2026-04-26*
