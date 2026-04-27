---
Project: Plating Posters Inc
Poster Number: 630
Title: "Inspection & QA -- Flame Hardening"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion Heat Treatment Clusters -- Watson Research Brief (Process 8, Section 8.8)"
Technical Source: Flame hardening inspection -- hardness testing (ASTM E18), pattern verification (acid etch), crack detection (MPI/dye penetrant), torch tracking pattern checks, overlap zone assessment in progressive hardening, and surface condition evaluation for oxidation/decarburization.
Process Scope: Flame hardening -- inspection and quality assurance
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - FlameHardening
  - Inspection
  - QualityAssurance
  - ConstructionWorkup
  - ClusterHT08
---

# Poster #630 -- Construction Workup
## Inspection & QA -- Flame Hardening

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Flame hardening inspection has one challenge that induction does not: overlap zones. In progressive hardening, the flame traverses along the part and each pass overlaps the previous one. That overlap zone gets heated twice -- which can mean a hard spot (double austenitization) or a soft spot (the second pass tempers the first). Experienced inspectors know to check there first. This poster covers the full inspection sequence plus the common defect table that ties back to process parameters.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Inspection sequence flowchart (Block B -- HERO):** Five-step inspection sequence from hardness through final release.
2. **Overlap zone diagram (Block C):** Visual showing progressive hardening overlap and what to check.
3. **Common defects reference table (Block D):** Full defect-cause-remedy table from Watson's research.
4. **Acceptance criteria summary (Block E):** Typical pass/fail criteria for flame-hardened parts.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 9 highlighted (Emerald)
ZONE 3 -- INSPECTION SEQUENCE / HERO (4.2"--14.5" / ~10.3")
  Block B: Five-step inspection sequence
  Block C: Overlap zone diagram
ZONE 4 -- DEFECT REFERENCE TABLE (14.5"--22.0" / ~7.5")
  Block D: Defect-cause-remedy table
ZONE 5 -- ACCEPTANCE CRITERIA (22.0"--28.5" / ~6.5")
  Block E: Pass/fail summary
ZONE 6 -- FOOTER BAND (28.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `INSPECTION & QA` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Flame Hardening -- Stage 9 of 9` -- 36 pt `#27AE60` (Emerald). Y: 1.5".
**Tagline:** `Hardness. Pattern. Cracks. Overlap zones. The final gate before the part ships -- or goes back for rework.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 9 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Tempered martensite, process complete  -->  After: Verified, documented, released or rejected`

---

### ZONE 3 -- Inspection Sequence (HERO)

**Section label:** `FIVE-STEP INSPECTION SEQUENCE` -- Y: 4.4".

**BLOCK B -- Five Inspection Steps**

Y: 5.0" to 10.5". Five horizontal cards in a single row.

Each card: Rounded rect W: 4.3", H: 5.0", fill `#1E2435`, radius 6, top accent 4 pt `#27AE60`.

| Step | X | Title | Method | Standard | What to Check |
|---|---|---|---|---|---|
| 1 | 0.5" | HARDNESS | Rockwell C (HRC) | ASTM E18 | Surface hardness at specified locations; minimum and maximum values per drawing |
| 2 | 5.1" | PATTERN | Acid etch (nital or HCl) | Visual / print | Etch reveals hardened zone boundary; compare to pattern template or drawing |
| 3 | 9.7" | CRACK CHECK | MPI (preferred) or dye penetrant | ASTM E1444 (MPI) / ASTM E165 (PT) | Surface and near-surface cracks; focus on section transitions and keyways |
| 4 | 14.3" | CASE DEPTH | File test (production) or microhardness traverse (lab) | ASTM E384 / SAE J423 | Effective case depth to 50 HRC; total case depth to core hardness |
| 5 | 18.9" | OVERLAP ZONES | Visual + hardness traverse across overlap | Per process spec | Soft spots or hard spots at progressive hardening overlap lines |

Card interior:
- Step badge: Rounded rect 0.8" x 0.35", fill `#27AE60`, text `STEP [N]` Barlow Condensed ExtraBold 13 pt `#1A1F2E`
- Title: Barlow SemiBold, 18 pt, `#F0EDE8`
- Method: JetBrains Mono Regular, 12 pt, `#27AE60`
- Standard: JetBrains Mono Regular, 11 pt, `#F0EDE8` at 60%
- What to check: Inter Regular, 12 pt, `#F0EDE8`, line height 150%

**BLOCK C -- Overlap Zone Diagram**

Y: 11.0" to 14.3". Full-width panel.

- Rounded rect W: 23.0", H: 3.0", fill `#1E2435`, radius 6

Section label: `PROGRESSIVE HARDENING -- OVERLAP ZONE INSPECTION` Barlow SemiBold 16 pt `#F0EDE8`.

Visual concept: horizontal bar representing a part surface, divided into three traversal passes. Between each pass, an overlap zone is highlighted.

Pass labels (JetBrains Mono Regular, 12 pt):
- Pass 1 zone: fill `#2EC4B6` at 30%, label `PASS 1`
- Overlap zone 1-2: fill `#E8A020` at 40%, label `OVERLAP`
- Pass 2 zone: fill `#2EC4B6` at 30%, label `PASS 2`
- Overlap zone 2-3: fill `#E8A020` at 40%, label `OVERLAP`
- Pass 3 zone: fill `#2EC4B6` at 30%, label `PASS 3`

Below diagram, two-column callout:

Left (Inter Medium 13 pt `#E05C5C`):
`RISK: Overlap zone heated twice -- second pass may temper (soften) or re-austenitize (harden) the previous pass depending on temperature reached.`

Right (Inter Medium 13 pt `#27AE60`):
`CHECK: Run hardness traverse across overlap. Both soft spots and hard spots are possible. Adjust overlap width and speed to minimize variation.`

---

### ZONE 4 -- Defect Reference Table

**Section label:** `COMMON DEFECTS -- CAUSE AND REMEDY` -- Y: 14.7".

**BLOCK D -- Defect Table**

Y: 15.3" to 21.8". Column widths (23.0" total):
- Defect (4.5") | Cause (8.5") | Remedy (10.0")

Header row: fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

| Defect | Cause | Remedy |
|---|---|---|
| Overheating / melting | Flame too close; dwell too long; wrong tip size | Increase flame distance; increase traverse speed; select proper tip |
| Soft spots | Insufficient temperature; uneven flame coverage; overlap zone temper-back | Verify temperature with pyrometer; improve flame head; adjust overlap |
| Cracking | Quench too severe; section too thin; pre-existing stress risers | Reduce quench; preheat to 300--400 F; stress relieve before hardening |
| Non-uniform case depth | Manual technique variation; inconsistent traverse speed | Automate traverse; use CNC control; verify with test coupons |
| Distortion | Asymmetric heating; heating too deep into thin sections | Balance heat pattern; reduce case depth; support part during process |
| Excessive oxidation | Flame too oxidizing; too many passes; dwell too long | Adjust to neutral flame; reduce exposure time |
| Decarburization | Oxidizing flame; excessive temperature; prolonged heating | Use neutral to slightly reducing flame; minimize heat time |

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.7".
Defect: Barlow SemiBold 13 pt `#E05C5C`. Cause: Inter Regular 12 pt `#F0EDE8`. Remedy: Inter Medium 12 pt `#27AE60`.

---

### ZONE 5 -- Acceptance Criteria

**Section label:** `TYPICAL ACCEPTANCE CRITERIA` -- Y: 22.2".

**BLOCK E -- Pass/Fail Summary**

Y: 22.9" to 28.3". Two-column layout.

**Left -- Acceptance Requirements (X: 0.5", W: 11.0"):**

Rounded rect, H: 5.0", fill `#1E2435`, left accent 0.06" `#27AE60`, radius 6.

Title: `PASS` -- Barlow Condensed ExtraBold 24 pt `#27AE60`

Items (Inter Medium 13 pt `#F0EDE8`):
```
Surface hardness within drawing specification
  (typical: 55--62 HRC for medium-carbon steel)
Case depth within tolerance
  (typical: +/- 0.030 in for manual, +/- 0.020 for auto)
Hardened pattern matches template or drawing
No cracks detected by MPI or dye penetrant
Overlap zone hardness within 3 HRC of adjacent zones
No visible melting, excessive oxidation, or
  decarburization
Distortion within drawing tolerance
```

Data values: JetBrains Mono Regular 12 pt `#27AE60`.

**Right -- Rejection Criteria (X: 12.0", W: 11.5"):**

Rounded rect, H: 5.0", fill `#1E2435`, left accent 0.06" `#E05C5C`, radius 6.

Title: `REJECT / REWORK` -- Barlow Condensed ExtraBold 24 pt `#E05C5C`

Items (Inter Medium 13 pt `#F0EDE8`):
```
Hardness below minimum specification
Case depth below minimum or above maximum
Cracks detected (any size -- zero tolerance)
Melting or gross overheating (scrap -- not reworkable)
Decarburization > 0.005 in (may be reworkable
  by grinding if stock allows)
Pattern deviation > specification
Distortion beyond drawing limits
  (may be straightenable if within material limits)
```

Data values: JetBrains Mono Regular 12 pt `#E05C5C`.

---

### ZONE 6 -- Footer

Standard footer. Title: `Inspection & QA -- Flame Hardening`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Acceptance criteria shown are typical industry values. Actual requirements are defined by the part drawing, customer specification, and applicable standards (ASTM E18, E384, E1444, SAE J423). Source: General industry knowledge; ASM Handbook Vol. 4.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Inspection QA Flame Hardening -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The overlap zone diagram in Block C is unique to flame hardening -- induction doesn't have this problem because the coil defines the pattern exactly. Progressive flame hardening operators must overlap passes to avoid leaving unhardened strips, but that overlap creates a zone of uncertainty. This poster makes the invisible visible. The defect table mirrors Watson's research brief exactly, and the acceptance/rejection split gives QA inspectors a clean pass/fail reference at a glance.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #630 -- Construction Workup v1.0*
*2026-04-26*
