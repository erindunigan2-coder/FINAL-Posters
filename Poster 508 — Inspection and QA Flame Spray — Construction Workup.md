---
Project: Plating Posters Inc
Poster Number: 508
Title: "Inspection & QA -- Flame Spray"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Thermal Spray Clusters -- Watson Research Brief (Cluster 3: Flame Spray)"
Process Scope: Inspection and quality assurance for flame spray coatings -- test methods, acceptance criteria, fused vs. as-sprayed
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ThermalSpray
  - FlameSpray
  - Inspection
  - QualityAssurance
  - ConstructionWorkup
  - ClusterTS03
---

# Poster #508 -- Construction Workup
## Inspection & QA -- Flame Spray

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

The final stage in the flame spray cluster -- where you prove the coating meets specification. The hero is a comprehensive test methods table with acceptance criteria split into as-sprayed and fused columns. Flame spray inspection is simpler than HVOF or plasma (less stringent specs, more forgiving porosity) but still requires disciplined QA. The fuse quality check (visual "sweat" + metallographic section) is unique to this process.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Test methods table (Block B -- HERO):** 7-row table with ASTM methods, as-sprayed criteria, and fused criteria.
2. **Visual inspection guide (Block C):** What to look for at the unaided eye and 10x magnification.
3. **Fuse quality verification (Block D):** Specific checks for fused self-fluxing alloy coatings.
4. **Documentation checklist (Block E):** QA record-keeping requirements.
5. **Reject criteria strip (Block F):** 4 conditions that require stripping and re-spraying.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 8 highlighted (Teal)
ZONE 3 -- TEST METHODS TABLE / HERO (4.2"--15.5" / ~11.3")
  Block B: 7-row test methods and acceptance criteria
  Block C: Visual inspection guide
ZONE 4 -- FUSE QUALITY VERIFICATION (15.5"--22.0" / ~6.5")
  Block D: Fused coating-specific inspection
ZONE 5 -- DOCUMENTATION CHECKLIST (22.0"--28.5" / ~6.5")
  Block E: QA documentation requirements
ZONE 6 -- REJECT CRITERIA (28.5"--32.5" / ~4.0")
  Block F: 4 reject condition cards
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `INSPECTION & QA` -- 88 pt `#F0EDE8`.
**Subheading:** `Flame Spray -- Proving the Coating Meets Specification` -- 36 pt `#2EC4B6` (Teal).
**Tagline:** `The coating is only as good as the inspection that confirms it. Visual first, instruments second, documentation always.` -- 22 pt `#F0EDE8` at 65%.

---

### ZONE 2 -- Orientation Strip

Stage 8 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Coating post-treated (sealed, fused, or machined) --> After: Coating verified and documented, part released`

---

### ZONE 3 -- Test Methods Table (HERO)

**Section label:** `INSPECTION TEST METHODS & ACCEPTANCE CRITERIA` -- Y: 4.4".

**BLOCK B -- 7-Row Test Methods Table**

Y: 5.0" to 12.5". Full width within margins (23.0").

Column widths: Test (3.5") | Method (4.0") | As-Sprayed Criteria (5.5") | Fused Criteria (5.5") | Notes (4.5")

| Test | Method | As-Sprayed | Fused | Notes |
|---|---|---|---|---|
| Bond strength | ASTM C633 (tensile adhesion) | >10 MPa | >35 MPa (typically >70 MPa) | Fused = metallurgical bond |
| Porosity | ASTM E2109 (image analysis) | 5--15% (expected) | <2% (typically <1%) | Cross-section required |
| Thickness | Mag-gauge, eddy current, ASTM B487 | Per specification | Per specification | In-process + final |
| Hardness | ASTM E384 (Vickers, HV300) | Material-dependent | NiCrBSi: 700--900 HV | Micro-indentation on cross-section |
| Visual | Unaided eye + 10x loupe | Uniform coverage; no bare spots, blistering, or excessive orange peel | Fully wetted "sweat" surface; uniform gloss | First test performed |
| Bend test | Mandrel bend (qualification) | Per specification (qualitative) | Fused coatings may crack at sharp bends | Not a production test -- qualification only |
| Surface roughness | Profilometer (Ra) | 8--20 um (as-sprayed) | Ra per machining spec | Only if finish machined |

Table header: fill `#3A4055`, H: 0.6". Barlow SemiBold, 14 pt, `#F0EDE8`.
Data rows: alternating `#1E2435` / `#252B3D`, H: 0.85".
Test names: Inter Medium 13 pt `#F0EDE8`. ASTM methods: JetBrains Mono 12 pt `#E8A020`. Criteria: Inter Regular 13 pt. Notes: Inter Regular 12 pt `#F0EDE8` at 70%.

**BLOCK C -- Visual Inspection Guide**

Y: 13.0" to 15.3". Full width.

Section sublabel: `VISUAL INSPECTION -- ALWAYS FIRST` Barlow SemiBold 18 pt `#2EC4B6`. Y: 13.0".

Two-column layout:

**Left -- Unaided Eye (X: 0.5", W: 11.0"):**
- Rounded rect, fill `#1E2435`, left accent `#2EC4B6`
- Title: `UNAIDED EYE CHECK` Barlow SemiBold 16 pt `#2EC4B6`
- Check items (Inter Regular 14 pt, bullet list):
  - `Complete coverage -- no bare substrate visible`
  - `Uniform color and texture across entire area`
  - `No blistering, flaking, or delamination`
  - `No excessive orange peel or rough patches`
  - `Edge buildup within acceptable limits`

**Right -- 10x Magnification (X: 12.0", W: 11.5"):**
- Rounded rect, fill `#1E2435`, left accent `#E8A020`
- Title: `10x LOUPE CHECK` Barlow SemiBold 16 pt `#E8A020`
- Check items:
  - `No unmelted particles embedded in surface`
  - `No visible macro-porosity (pinholes)`
  - `No interface separation at coating edges`
  - `Uniform splat structure (no cold particles)`
  - `No contamination inclusions (fibers, grit)`

---

### ZONE 4 -- Fuse Quality Verification

**Section label:** `FUSED COATING VERIFICATION -- SELF-FLUXING ALLOYS` -- Y: 15.7".

**BLOCK D -- Fuse-Specific Inspection**

Y: 16.3" to 21.5".

Three panels in a row.

**Panel 1 -- Visual Sweat Test (X: 0.5", W: 7.3"):**
- Rounded rect, fill `#1E2435`, top accent `#E8A020`
- Title: `VISUAL "SWEAT" TEST` Barlow SemiBold 16 pt `#E8A020`
- `During torch fusing, the coating surface transitions from matte to glossy ("sweating") when the alloy remelts`
- `PASS: Entire surface shows uniform gloss; no matte (unfused) areas`
- `FAIL: Patchy appearance -- matte areas indicate incomplete fusion`
- `This is operator judgment -- experience matters`

**Panel 2 -- Metallographic Section (X: 8.15", W: 7.3"):**
- Rounded rect, fill `#1E2435`, top accent `#2EC4B6`
- Title: `METALLOGRAPHIC CROSS-SECTION` Barlow SemiBold 16 pt `#2EC4B6`
- `Cut, mount, and polish a cross-section from a test coupon sprayed and fused alongside the production part`
- `Examine at 100--500x magnification`
- `PASS: Fully wetted interface; <2% porosity; no unfused zones; uniform microstructure`
- `FAIL: Visible interface line; residual porosity >2%; large voids`

**Panel 3 -- Hardness Verification (X: 15.85", W: 7.3"):**
- Rounded rect, fill `#1E2435`, top accent `#27AE60`
- Title: `HARDNESS CHECK` Barlow SemiBold 16 pt `#27AE60`
- `Vickers microhardness (HV300) on polished cross-section`
- `NiCrBSi as-sprayed: 300--500 HV`
- `NiCrBSi properly fused: 700--900 HV`
- `If hardness is below 600 HV, fusing was incomplete -- re-fuse or investigate`
- `Minimum 5 indentations across coating thickness`

---

### ZONE 5 -- Documentation Checklist

**Section label:** `QA DOCUMENTATION REQUIREMENTS` -- Y: 22.2".

**BLOCK E -- Documentation Checklist**

Y: 22.8" to 28.0". Two columns of checklist items.

| Item | Record |
|---|---|
| Feedstock material and lot number | Certificate of conformance from wire/powder supplier |
| Pre-spray surface prep | Blast media type, grit size, profile (Ra), cleanliness standard achieved |
| Spray parameters | Gas pressures, wire/powder feed rate, standoff, traverse speed |
| In-process thickness measurements | Readings at multiple locations; comparison to target |
| Substrate temperature log | Peak temperature recorded during spray and any cooling interventions |
| Post-treatment performed | Seal type and application time, fuse temperature and method, or machining spec |
| Final inspection results | Bond strength, porosity, thickness, hardness, visual -- all per specification |
| Operator identification | Name/ID of spray operator and inspector |
| Date and time stamps | For each process step (clean, blast, spray, seal/fuse, inspect) |

Checklist items: Inter Medium 13 pt `#F0EDE8`. Records: Inter Regular 13 pt `#F0EDE8` at 70%.
Each row has a checkbox indicator: rounded rect 0.3" x 0.3", border 1 pt `#2EC4B6`, fill transparent.

Below checklist:
- Callout: `Good documentation is your evidence that the process was followed. If it is not recorded, it did not happen.` Inter Medium 13 pt `#2EC4B6`.

---

### ZONE 6 -- Reject Criteria

**Section label:** `REJECT CONDITIONS -- STRIP AND RE-SPRAY` -- Y: 28.7".

Four cards, W: 5.5", H: 2.5", left accent `#E05C5C`.

| Card | X | Condition | Action |
|---|---|---|---|
| 1 | 0.5" | BOND STRENGTH BELOW MINIMUM | Strip coating by grit blast or chemical strip; investigate root cause (contamination, profile, parameters); re-blast and re-spray |
| 2 | 6.33" | POROSITY EXCEEDS SPECIFICATION | If sealable, seal and retest; if specification requires <2% and coating is 5--15%, fusing was required but not performed or was incomplete |
| 3 | 12.16" | DELAMINATION OR BLISTERING | Strip completely; do not attempt to spray over delaminated coating; investigate interface contamination or substrate overheating |
| 4 | 18.0" | INCOMPLETE FUSING | Re-fuse with torch or furnace if substrate can tolerate a second thermal cycle; if not, strip and re-spray with proper fusing procedure |

---

### ZONE 7 -- Footer

Standard footer. Title: `Inspection & QA -- Flame Spray`. Version `v1.0 -- 2026`.
Disclaimer: `Source: ASM Handbook Vol 5A; ASTM C633, E2109, B487, E384; AWS C2.18; general industry knowledge. Acceptance criteria shown are typical ranges. Actual acceptance criteria are defined by the applicable coating specification for each application.`

---

## Parts 5--7

**Grouping:** 7 zones. **Light Remap:** Standard. **Export:** Six files.

---

*Alaina -- Poster #508 -- Construction Workup v1.0 -- 2026-04-26*
