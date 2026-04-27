---
Project: Plating Posters Inc
Poster Number: 702
Title: "Inspection & Handling -- Coil Coating"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting Coating Clusters -- Watson Research Brief (Cluster 6: Coil Coating, Section 6.9)"
Process Scope: Inspection and handling for coil coating -- Stage 9 QC + post-cure handling
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - CoilCoating
  - Inspection
  - Handling
  - ConstructionWorkup
  - PaintingCoating
  - ClusterCC
---

# Poster #702 -- Construction Workup
## Inspection & Handling -- Coil Coating

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

The final poster of the Coil Coating cluster. Quality control at line speed means in-line automated instruments for DFT, gloss, and color -- you cannot stop the line to measure. Per-coil tests (T-bend, hardness, adhesion, MEK rub) are pulled at the recoiler. Qualification tests (salt spray, humidity, UV weathering) are run per lot. And after all that, the coated coil must be handled, stored, and shipped without scratching the finish that 9 stages of chemistry and engineering just put there.

Hero visual: QC flowchart showing the three tiers of testing (in-line continuous, per-coil, per-lot qualification) with test names, standards, and targets.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Three-tier QC flowchart hero (Block B):** Hierarchical diagram showing in-line, per-coil, and per-lot testing tiers.
2. **Test parameters table (Block D):** Complete list of tests with standards, methods, and targets.
3. **Handling and storage panel (Block E):** Post-cure handling requirements to protect the coated coil.
4. **Defect strip (Block F):** 4 inspection/handling issues.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 21.0" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  QC position highlighted (Emerald)
ZONE 3 -- THREE-TIER QC HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- TEST PARAMETERS TABLE (14.5"--21.0" / ~6.5")
ZONE 5 -- HANDLING AND STORAGE (21.0"--27.0" / ~6.0")
ZONE 6 -- INSPECTION / HANDLING ISSUES (27.0"--32.5" / ~5.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `INSPECTION & HANDLING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Coil Coating -- Final QC + Post-Cure Handling` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `Three tiers of testing: continuous in-line, per-coil destructive, and per-lot qualification. Then handle the coated coil like you spent 9 stages making it -- because you did.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

QC position highlighted after Stage 9: fill `#27AE60`, text `#1A1F2E`. Inspect badge illuminated. Others dimmed.
Below: `Before: Cured and quenched strip exiting finish oven  -->  After: Tested, verified, recoiled, and ready for fabrication`

---

### ZONE 3 -- Three-Tier QC Hero

**Section label:** `THREE TIERS OF QUALITY CONTROL` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Three-Tier Diagram (Y: 5.0" to 14.0")**

Three stacked panels representing testing tiers.

**Tier 1 -- In-Line Continuous (Y: 5.0" to 7.8"):**
- Full-width rounded rect, W: 23.0", H: 2.5", fill `#1E2435`, left accent `#27AE60` 0.06"
- Badge: `TIER 1 -- CONTINUOUS` fill `#27AE60`, text `#1A1F2E`
- Title: `IN-LINE AUTOMATED INSTRUMENTS` Barlow SemiBold 18 pt `#27AE60`
- Three test items (horizontal row):
  - `DFT: beta-backscatter or XRF (continuous)` JetBrains Mono 12 pt `#F0EDE8`
  - `GLOSS: in-line 60 deg glossmeter` JetBrains Mono 12 pt `#F0EDE8`
  - `COLOR: in-line spectrophotometer or per-coil handheld` JetBrains Mono 12 pt `#F0EDE8`
- Frequency: `EVERY FOOT OF STRIP` Inter Medium 13 pt `#27AE60`

**Tier 2 -- Per-Coil Destructive (Y: 8.3" to 11.1"):**
- Full-width rounded rect, W: 23.0", H: 2.5", fill `#1E2435`, left accent `#E8A020` 0.06"
- Badge: `TIER 2 -- PER COIL` fill `#E8A020`, text `#1A1F2E`
- Title: `DESTRUCTIVE TESTS ON CUT SAMPLES` Barlow SemiBold 18 pt `#E8A020`
- Test items (horizontal row):
  - `T-BEND (ASTM D4145)` | `PENCIL HARDNESS (D3363)` | `ADHESION (D3359)` | `MEK RUB (D4752)` | `REVERSE IMPACT (D2794)`
- JetBrains Mono 11 pt `#F0EDE8`
- Frequency: `EVERY COIL -- cut sample at recoiler` Inter Medium 13 pt `#E8A020`

**Tier 3 -- Per-Lot Qualification (Y: 11.6" to 14.0"):**
- Full-width rounded rect, W: 23.0", H: 2.1", fill `#1E2435`, left accent `#2EC4B6` 0.06"
- Badge: `TIER 3 -- QUALIFICATION` fill `#2EC4B6`, text `#1A1F2E`
- Title: `LONG-TERM PERFORMANCE TESTS` Barlow SemiBold 18 pt `#2EC4B6`
- Test items:
  - `SALT SPRAY (B117): 500-3,000 hr` | `HUMIDITY (D2247): 1,000-2,000 hr` | `UV WEATHERING (G154/G155): 2,000-10,000 hr`
- JetBrains Mono 11 pt `#F0EDE8`
- Frequency: `PER LOT or qualification batch` Inter Medium 13 pt `#2EC4B6`

---

### ZONE 4 -- Test Parameters Table

**Section label:** `COMPLETE TEST MATRIX` -- Y: 14.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK D -- Full Test Table**

Y: 15.3" to 20.8". Column widths (23.0" total):
- Test (4.0") | Standard (3.0") | Frequency (3.0") | Target (5.5") | Tier (2.5") | Notes (5.0")

| Test | Standard | Frequency | Target | Tier | Notes |
|---|---|---|---|---|---|
| DFT | In-line beta/XRF | Continuous | 0.7-1.0 mil (typical) | 1 | Per spec for each chemistry |
| Gloss | ASTM D523 (60 deg) | Continuous or per coil | Per spec (high/semi/matte) | 1 | In-line glossmeter |
| Color | ASTM D2244 | Per coil minimum | Delta E < 1.0 (CIE L*a*b*) | 1-2 | Spectrophotometer |
| T-bend | ASTM D4145 | Per coil | 0T to 2T (spec dependent) | 2 | Tightest bend without cracking |
| Pencil hardness | ASTM D3363 | Per coil | F to 2H typical | 2 | Relates to cure degree |
| Adhesion | ASTM D3359 | Per coil | 5B | 2 | Crosshatch tape pull |
| MEK double rub | ASTM D4752 | Per coil | 100+ double rubs | 2 | Primary cure verification |
| Reverse impact | ASTM D2794 | Per coil | 40-80 in-lb | 2 | Spec dependent |
| Salt spray | ASTM B117 | Per lot / qualification | 500-3,000 hr | 3 | Scribed panels |
| Humidity resistance | ASTM D2247 | Per lot | 1,000-2,000 hr | 3 | -- |
| UV weathering | ASTM G154 / G155 | Qualification | 2,000-10,000 hr | 3 | Gloss and color retention |

Data: JetBrains Mono Regular, 11 pt, `#F0EDE8`. Header: Barlow SemiBold 13 pt.

---

### ZONE 5 -- Handling and Storage

**Section label:** `POST-CURE HANDLING -- PROTECTING THE FINISH` -- Y: 21.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK E -- Two-Column Panel**

Y: 21.8" to 26.8".

**Left -- Recoiling and Interleaving (X: 0.5", W: 11.0"):**
- Rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `RECOILING` -- Barlow SemiBold, 18 pt, `#E8A020`

Bullet list (Inter Regular 13 pt `#F0EDE8`, line height 155%):
- `Coated coil is rewound with paper interleaving to prevent face-to-face contact`
- `Interleaving paper must be acid-free and low-moisture`
- `Tension control at recoiler prevents telescoping (uneven edge alignment)`
- `Coil OD (outer diameter) must match order specification`
- `Eye orientation (inner wrap / outer wrap) per customer requirement`

**Right -- Storage and Shipping (X: 12.0", W: 11.5"):**
- Rounded rect, fill `#1E2435`, left accent `#2EC4B6` 0.06"
- Title: `STORAGE AND SHIPPING` -- Barlow SemiBold, 18 pt, `#2EC4B6`

Bullet list:
- `Store indoors, dry, temperature-controlled`
- `Avoid condensation (coil sweating) -- coil temperature must exceed dew point before unwrapping`
- `Do not store on concrete floor without pallets or cradles`
- `Protect coil edges from damage during handling`
- `Forming: fabricator must use polished rolls and Teflon-coated dies to avoid scratching`
- `Any handling scratch is a warranty claim -- the finish is the product`

---

### ZONE 6 -- Inspection / Handling Issues

**Section label:** `WHAT GOES WRONG -- 4 INSPECTION / HANDLING ISSUES` -- Y: 27.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK F -- Four Problem Cards (Y: 27.8" to 30.5")**

Each card: Rounded rect, W: 5.5", H: 2.5", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | MEK RUB FAILURE (< 100) | Undercure -- PMT too low or line speed too fast | Check PMT with IR pyrometer; reduce line speed or increase oven temp |
| 2 | 6.33" | T-BEND CRACKING | Overcure (embrittlement) or wrong coating chemistry | Verify PMT history; consider higher-flexibility chemistry (PVDF or PU) |
| 3 | 12.16" | COIL SWEATING (CONDENSATION) | Cold coil moved to warm/humid environment | Acclimate coil to ambient before unwrapping; monitor dew point |
| 4 | 18.0" | SCRATCH ON COATED SURFACE | Handling damage at coater, in transit, or at fabricator | Paper interleave; protect edges; require polished forming tools |

**Key insight callout (Y: 31.0" to 32.3"):**
- Text: `A coil coating line can produce 50,000+ square feet per hour. Every defect that passes inspection multiplies at that rate. The three-tier QC system exists because no single test catches everything -- continuous instruments catch drift, per-coil destructive tests catch property failures, and qualification tests prove long-term performance.` -- Inter Medium, 14 pt, `#E8A020`

---

### ZONE 7 -- Footer

Standard. Title: `Inspection & Handling -- Coil Coating`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Inspection Handling Coil Coating -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster closes the Coil Coating cluster. The three-tier QC hero is the unique value -- it organizes the overwhelming list of coil coating tests into a logical hierarchy that any quality manager can reference at a glance. Tier 1 runs at line speed (automated), Tier 2 requires stopping to cut samples (per coil), Tier 3 takes weeks or months (qualification). The handling section reminds everyone that 9 stages of precision coating can be destroyed by one careless forklift operator or one unpolished forming die.

---

*Alaina -- Poster #702 -- Construction Workup v1.0 -- 2026-04-26*
