---
Project: Plating Posters Inc
Poster Number: 502
Title: "Grit Blasting -- Flame Spray"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Thermal Spray Clusters -- Watson Research Brief (Cluster 3: Flame Spray)"
Process Scope: Grit blasting / surface preparation for flame spray -- media, profiles, standards
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ThermalSpray
  - FlameSpray
  - GritBlasting
  - ConstructionWorkup
  - ClusterTS03
---

# Poster #502 -- Construction Workup
## Grit Blasting -- Flame Spray

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Grit blasting for flame spray. The critical message: flame spray coatings rely heavily on mechanical interlocking because particle velocities are the lowest of any thermal spray method. A rougher anchor profile compensates -- this is not optional, it is the entire bonding mechanism.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Blast parameter table (Block B -- HERO):** Large reference table with media, pressure, profile, and cleanliness specs.
2. **Why rougher profile callout (Block C):** Velocity-vs-profile visual explanation.
3. **Media selection guide (Block D):** Comparison of alumina, steel grit, and garnet.
4. **Profile verification methods (Block E):** Three measurement techniques.
5. **Defect cards (Block F):** 4 blast-related coating failures.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.0" / 20.5" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 2 highlighted (Teal)
ZONE 3 -- BLAST PARAMETERS / HERO (4.2"--14.0" / ~9.8")
  Block B: Blast parameter reference table
  Block C: "Why rougher?" callout
ZONE 4 -- MEDIA SELECTION (14.0"--20.5" / ~6.5")
  Block D: Media comparison (3 columns)
ZONE 5 -- PROFILE VERIFICATION (20.5"--27.0" / ~6.5")
  Block E: 3 measurement methods + standards reference
ZONE 6 -- BLAST-RELATED FAILURES (27.0"--32.5" / ~5.5")
  Block F: 4 defect cards
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `GRIT BLASTING` -- 88 pt `#F0EDE8`.
**Subheading:** `Flame Spray -- Surface Preparation` -- 36 pt `#2EC4B6` (Teal).
**Tagline:** `Flame spray bonds by mechanical interlock -- no profile, no coating. The rougher the anchor, the stronger the grip.` -- 22 pt `#F0EDE8` at 65%.

---

### ZONE 2 -- Orientation Strip

Stage 2 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean, dry substrate --> After: SSPC-SP 5 white metal blast, Ra 4--12 um`

---

### ZONE 3 -- Blast Parameters (HERO)

**Section label:** `GRIT BLAST SPECIFICATION FOR FLAME SPRAY` -- Y: 4.4".

**BLOCK B -- Parameter Reference Table**

Y: 5.0" to 10.5". Full-width table.

| Parameter | Typical Range | Notes |
|---|---|---|
| Media | Angular alumina (Al2O3) or steel grit | Alumina preferred for non-ferrous substrates |
| Grit size | 16--36 mesh | Coarser than HVOF/APS due to lower particle energy |
| Blast pressure | 60--100 PSI (415--690 kPa) | More aggressive than APS or HVOF |
| Nozzle distance | 150--250 mm (6--10 in) | Closer = deeper profile |
| Blast angle | 60--90 degrees to surface | 90 deg for max depth; 60--75 deg for cleaning |
| Anchor profile (Ra) | 4--12 microns (175--500 uin) | Rougher profile needed vs. higher-velocity processes |
| Surface cleanliness | SSPC-SP 5 (White Metal) | Per AWS C2.18 for corrosion protection |

Table construction: Header `#3A4055`, rows alternating `#1E2435`/`#252B3D`.
Parameter names: Barlow SemiBold 14 pt. Values: JetBrains Mono 13 pt. Notes: Inter Regular 12 pt at 70%.

**BLOCK C -- "Why Rougher?" Callout**

Y: 11.0" to 13.5". Full-width rounded rect, fill `#1E2435`, top accent `#E8A020` 4 pt.

Title: `WHY FLAME SPRAY NEEDS A ROUGHER PROFILE` Barlow Condensed ExtraBold 22 pt `#E8A020`.

Two-column inside:

Left column -- `LOW VELOCITY = LOW IMPACT ENERGY`:
- `Flame spray: 40--200 m/s`
- `HVOF: 600--1000 m/s`
- `Plasma: 200--600 m/s`
- `Lower velocity means less "splat" energy to grip the surface`
JetBrains Mono 14 pt `#F0EDE8`.

Right column -- `ROUGHER PROFILE COMPENSATES`:
- `More surface area = more mechanical interlock points`
- `Deeper valleys = better particle anchoring`
- `Ra 4--12 um for flame vs. 3--8 um for APS`
- `The profile IS the bond mechanism`
Inter Medium 14 pt `#27AE60`.

---

### ZONE 4 -- Media Selection Guide

**Section label:** `BLAST MEDIA SELECTION` -- Y: 14.2".

**BLOCK D -- Three-Column Media Comparison**

Y: 14.8" to 20.3". Three callout boxes side by side.

| Media | X | W | Accent | Hardness | Best For | Cost |
|---|---|---|---|---|---|---|
| WHITE ALUMINA | 0.5" | 7.33" | `#2EC4B6` | Mohs 9 | Aerospace; non-ferrous substrates; no Fe contamination | Higher |
| ANGULAR STEEL GRIT | 8.0" | 7.33" | `#E8A020` | Mohs 7--8 | Infrastructure; bridge work; structural steel | Lower (recyclable) |
| GARNET | 15.5" | 8.0" | `#27AE60` | Mohs 7--8 | Non-ferrous substrates; less aggressive; field work | Moderate |

Each box: H: 4.5", fill `#1E2435`, left accent 0.06".
Media name: Barlow SemiBold 18 pt in accent color.
Properties: Inter Regular 14 pt, JetBrains Mono 13 pt for values.

Bottom note (full width): `Steel grit on titanium or nickel alloys = galvanic corrosion risk. Use alumina for non-ferrous work.` Inter Medium 13 pt `#E05C5C`.

---

### ZONE 5 -- Profile Verification

**Section label:** `VERIFY YOUR PROFILE -- THREE METHODS` -- Y: 20.7".

**BLOCK E -- 3 Method Cards + Standards Reference**

Three cards (W: 7.33", H: 3.5") + a standards reference strip below.

| Card | Method | How It Works | Accuracy |
|---|---|---|---|
| 1 | TESTEX REPLICA TAPE | Press tape into blasted surface; measure compressed thickness with micrometer | Field-friendly; +/- 0.5 mil |
| 2 | SURFACE PROFILOMETER | Stylus traces surface; measures Ra, Rz directly | Lab-grade; +/- 0.1 um |
| 3 | VISUAL COMPARATOR | Compare blasted surface to SSPC-VIS 1 reference photos | Quick pass/fail; subjective |

Method name: Barlow SemiBold 16 pt `#2EC4B6`. How/Accuracy: Inter Regular 13 pt.

Standards strip (Y: 25.5"): `#252B3D` bar.
- `SSPC-SP 5 = White Metal Blast | SSPC-SP 10 = Near-White Blast | ISO 8501 Sa 3 = White Metal equivalent`
- JetBrains Mono 13 pt `#F0EDE8`.

---

### ZONE 6 -- Blast-Related Failures

**Section label:** `WHEN BLASTING GOES WRONG` -- Y: 27.2".

Four cards, W: 5.5", H: 2.5", left accent `#E05C5C`.

| Card | Problem | Cause | Fix |
|---|---|---|---|
| 1 | POOR BOND STRENGTH | Insufficient profile depth (Ra too low) | Re-blast with coarser media or higher pressure |
| 2 | EMBEDDED MEDIA | Blast angle too steep or media too soft | Use angular media at 60--75 deg angle |
| 3 | SUBSTRATE DAMAGE | Excessive pressure on thin material | Reduce pressure; increase standoff; finer grit |
| 4 | FLASH RUST | Blast-to-spray time exceeded in humid conditions | Spray within 2--4 hours; monitor humidity |

---

### ZONE 7 -- Footer

Standard footer. Title: `Grit Blasting -- Flame Spray`. Version `v1.0 -- 2026`.
Disclaimer: `Source: ASM Handbook Vol 5A; AWS C2.18; SSPC standards; general industry knowledge.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Grit Blasting Flame Spray -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #502 -- Construction Workup v1.0*
*2026-04-26*
