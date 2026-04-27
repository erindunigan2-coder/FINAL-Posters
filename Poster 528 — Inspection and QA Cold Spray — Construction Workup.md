---
Project: Plating Posters Inc
Poster Number: 528
Title: "Inspection and QA -- Cold Spray"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 5: Cold Spray)"
Technical Source: Cold spray inspection and quality assurance methods including ASTM C633 bond strength, ASTM E2109 porosity, ASTM E384 microhardness, electrical conductivity testing, metallographic cross-section evaluation, and MIL-STD-3021 aerospace cold spray repair standard.
Process Scope: Cold spray -- inspection, testing, and quality assurance
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document.
tags:
  - PosterDesign
  - ColdSpray
  - ThermalSpray
  - InspectionQA
  - ConstructionWorkup
  - ClusterTS05
---

# Poster #528 -- Construction Workup
## Inspection and QA -- Cold Spray

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Inspection and QA poster for Cold Spray. Hero element: the comprehensive test matrix covering bond strength, porosity, hardness, electrical conductivity, microstructure, and tensile testing. Cold spray is unique among thermal spray processes in that deposits can be tensile-tested (ASTM E8) as machined specimens -- approaching wrought material properties after heat treatment. MIL-STD-3021 is the key aerospace standard and should be prominently featured.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Inspection test matrix (Block B -- HERO):** Comprehensive table of all test methods, ASTM standards, and acceptance criteria by material.
2. **Material-specific acceptance criteria (Block C):** Breakout table showing Cu, Al, and Ti criteria side by side.
3. **MIL-STD-3021 callout (Block D):** Teal callout for the US military cold spray repair standard.
4. **Metallographic cross-section guide (Block E):** What to look for in a cold spray cross-section -- particle deformation, interface quality, porosity distribution.
5. **Reject criteria strip (Block F):** Common rejection reasons with visual descriptions.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- INSPECTION TEST MATRIX (2.9"--14.0" / ~11.1")
  Block B: Master test matrix table
  Block D: MIL-STD-3021 callout
ZONE 3 -- MATERIAL-SPECIFIC CRITERIA (14.0"--22.0" / ~8.0")
  Block C: Cu vs. Al vs. Ti acceptance criteria
ZONE 4 -- METALLOGRAPHY + REJECT CRITERIA (22.0"--32.5" / ~10.5")
  Block E: Cross-section interpretation guide
  Block F: Common rejection reasons strip
ZONE 5 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `INSPECTION & QA` -- 80 pt `#F0EDE8`.
**Subheading:** `Cold Spray -- Verify Coating Integrity From Bond to Surface` -- 32 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `Bond strength, porosity, hardness, conductivity, microstructure. Cold spray deposits can even be tensile-tested like wrought metal.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Inspection Test Matrix

**Section label:** `INSPECTION TEST MATRIX` -- Y: 3.1".

**BLOCK B -- Master Test Matrix (Full width, X: 0.5", W: 15.5")**

Y: 3.8" to 12.5". Full data table.

Header row: `#3A4055`. Columns: Test (3.5") | Method / Standard (3.5") | Acceptance Criteria (4.5") | Notes (4.0")

| Test | Method / Standard | Acceptance Criteria | Notes |
|---|---|---|---|
| Bond strength | ASTM C633 (tensile adhesion) | Cu: > 40 MPa; Al: > 30 MPa | Often exceeds epoxy strength (~70 MPa); report as "> epoxy" |
| Porosity | ASTM E2109 (image analysis) | Cu: < 0.5%; Al: 0.5--2%; Ti: 1--3% | Measured on metallographic cross-section |
| Thickness | Eddy current, mag-gauge, or ASTM B487 | Per drawing tolerance | Non-destructive (eddy/mag) or destructive (cross-section) |
| Hardness | ASTM E384 (Vickers microhardness) | Material-dependent; typically above bulk annealed values | HV300 load standard; multiple indents across deposit |
| Microstructure | Metallographic cross-section (etched) | Evaluate particle deformation, interface quality, porosity distribution | SEM recommended for high-resolution evaluation |
| Electrical conductivity | 4-point probe or eddy current | Cu: > 80% IACS (as-sprayed); > 95% IACS (annealed) | Application-specific; critical for electrical applications |
| Visual | Unaided eye + 10x magnification | No bare spots, delamination, or surface irregularities | First-line inspection before any destructive testing |
| Tensile testing | ASTM E8 (machined specimens from deposit) | Approach wrought properties after heat treatment | Unique to cold spray -- no other thermal spray can do this |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Test names: Inter Medium, 13 pt. ASTM numbers in `#2EC4B6`.

**ASTM E8 callout (below table, Y: 12.8" to 13.8"):**
Rounded rect, full width 15.5", H: 0.8", fill `#27AE60` at 10%, border 1 pt `#27AE60`, radius 8.

`UNIQUE: Cold spray is the only thermal spray process where deposits can be machined into tensile test specimens (ASTM E8) and tested like bulk material. Post-anneal properties approach wrought values.` Inter Medium, 13 pt, `#27AE60`, center.

**BLOCK D -- MIL-STD-3021 Callout (Right, X: 16.5", W: 7.0")**

Y: 3.8" to 10.0". Rounded rect, fill `#1E2435`, radius 8, left accent 4 pt `#2EC4B6`.
Teal-tinted glass.

Title: `MIL-STD-3021` Barlow Condensed ExtraBold, 32 pt, `#2EC4B6`.
Subtitle: `Cold Spray Repair Standard` Barlow SemiBold, 16 pt, `#F0EDE8`.

Body (Inter Regular, 13 pt, `#F0EDE8`, line height 155%):
```
US military standard specifically
for cold spray repair of aerospace
components.

Key requirements:
- Process qualification per part
- Destructive test coupons sprayed
  with each production batch
- Operator certification
- Equipment calibration records
- Full traceability of powder lot
  to finished repair

Applications:
- Helicopter gearbox housing repair
- Structural aluminum restoration
- Corrosion damage dimensional rebuild
```

`MIL-STD-3021 is the first military standard written specifically for cold spray` Inter Medium, 12 pt, `#2EC4B6`. Y: 9.5".

**Cross-reference callout (below, Y: 10.5" to 13.5"):**
Rounded rect, fill `#1E2435`, left accent `#E8A020`.

Title: `RELATED STANDARDS` Barlow SemiBold, 16 pt, `#E8A020`.

Standards list (JetBrains Mono Regular, 12 pt, `#F0EDE8`, line height 160%):
```
ASTM C633   Bond strength (tensile adhesion)
ASTM E2109  Porosity (image analysis)
ASTM E384   Microhardness (Vickers/Knoop)
ASTM B487   Thickness (cross-section)
ASTM E8     Tensile testing (machined specimens)
AMS 2484    Cold spray -- general (emerging)
```

ASTM numbers in `#E8A020`.

---

### ZONE 3 -- Material-Specific Criteria

**Section label:** `ACCEPTANCE CRITERIA BY MATERIAL` -- Y: 14.2".

**BLOCK C -- Three-Material Comparison (Full width)**

Y: 14.8" to 21.5". Three side-by-side material cards.

Each card: W: 7.3", H: 6.5", fill `#1E2435`, radius 6, top accent 4 pt.

**Card 1 -- Copper (X: 0.5")**
Top accent: `#E8A020`.
Material badge: Rounded rect, W: 2.5", H: 0.4", fill `#E8A020`. Text: `COPPER` Barlow Condensed ExtraBold, 14 pt, `#1A1F2E`.

| Property | Criteria |
|---|---|
| Bond strength | > 40 MPa (often > epoxy) |
| Porosity | < 0.5% |
| Hardness (as-sprayed) | 100--150 HV |
| Hardness (annealed) | 60--90 HV |
| Conductivity | > 80% IACS (as-sprayed) |
| Conductivity | > 95% IACS (annealed) |

`Benchmark cold spray material. Near-bulk properties achievable.` Inter Regular, 12 pt, `#E8A020` at 80%.

**Card 2 -- Aluminum (X: 8.1")**
Top accent: `#2EC4B6`.
Material badge: fill `#2EC4B6`. Text: `ALUMINUM`.

| Property | Criteria |
|---|---|
| Bond strength | > 30 MPa |
| Porosity | 0.5--2% |
| Hardness | 80--130 HV (alloy-dependent) |
| Temper | Per alloy spec (T6, T7 after anneal) |
| Visual | No delamination at repair interface |
| Tensile (ASTM E8) | > 80% of wrought (post-anneal) |

`Primary aerospace repair material. MIL-STD-3021 compliance required for defense.` Inter Regular, 12 pt, `#2EC4B6` at 80%.

**Card 3 -- Titanium (X: 15.7")**
Top accent: `#27AE60`.
Material badge: fill `#27AE60`. Text: `TITANIUM`.

| Property | Criteria |
|---|---|
| Bond strength | > 30 MPa |
| Porosity | 1--3% (higher than Cu/Al) |
| Hardness | 250--400 HV (work-hardened) |
| Oxygen content | Monitor -- no oxidation in spray but anneal atmosphere critical |
| Microstructure | Severe particle deformation visible; good inter-particle bonding |
| Anneal | Vacuum mandatory; 500--700 C |

`Titanium cold spray requires helium carrier gas for adequate velocity. Nitrogen alone insufficient for Ti and Ti-6Al-4V.` Inter Regular, 12 pt, `#27AE60` at 80%.

Data in each card: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Property names: Inter Medium, 12 pt.

---

### ZONE 4 -- Metallography + Reject Criteria

**Left -- Cross-Section Interpretation (X: 0.5", W: 12.0")**

Section label: `METALLOGRAPHIC CROSS-SECTION -- WHAT TO LOOK FOR` Y: 22.2".

**BLOCK E -- Interpretation Guide**

Y: 22.8" to 31.0". Six feature cards, vertically stacked.

Each card: W: 11.5", H: 1.2", fill `#1E2435`, radius 6, left accent 4 pt.

| Feature | Accent | What It Tells You | Good vs. Bad |
|---|---|---|---|
| PARTICLE DEFORMATION | `#27AE60` | Severe flattening = high impact velocity = good bonding | Good: pancake-shaped particles. Bad: round particles (insufficient velocity) |
| INTERFACE QUALITY | `#2EC4B6` | Substrate-coating boundary should show intimate contact | Good: continuous contact, no voids. Bad: gaps or oxide film at interface |
| POROSITY DISTRIBUTION | `#E8A020` | Pores should be isolated, not interconnected | Good: rare, isolated pores < 0.5%. Bad: connected porosity channels |
| INTER-PARTICLE BONDING | `#27AE60` | Boundaries between particles should be tight | Good: minimal contrast at boundaries. Bad: visible gaps between particles |
| OXIDE INCLUSIONS | `#E05C5C` | Should be virtually absent in cold spray | Good: no oxide stringers. Bad: any oxide layer = process problem |
| COATING UNIFORMITY | `#2EC4B6` | Consistent thickness and microstructure across deposit | Good: uniform thickness. Bad: thin spots or density variations |

Feature: Barlow SemiBold, 14 pt, accent color.
What It Tells You: Inter Regular, 12 pt, `#F0EDE8`.
Good vs. Bad: Inter Medium, 11 pt. "Good:" in `#27AE60`, "Bad:" in `#E05C5C`.

**Right -- Reject Criteria (X: 13.0", W: 10.5")**

Section label: `COMMON REJECTION REASONS` Y: 22.2".

**BLOCK F -- Reject Cards (stacked)**

Y: 22.8" to 32.0". Five reject cards.

| Rejection | Color | Description | Likely Root Cause |
|---|---|---|---|
| BOND STRENGTH BELOW SPEC | `#E05C5C` | ASTM C633 result below minimum MPa requirement | Surface contamination; insufficient velocity; excessive time between blast and spray |
| POROSITY ABOVE SPEC | `#E05C5C` | Image analysis shows porosity exceeding material limit | Velocity too low; wrong powder morphology; non-optimized parameters |
| HARDNESS OUT OF RANGE | `#E8A020` | Microhardness too high (not annealed when required) or too low | Anneal schedule incorrect; verify time, temperature, and atmosphere |
| BARE SPOTS OR DELAMINATION | `#E05C5C` | Visual inspection finds uncovered areas or coating liftoff | Masking error; nozzle clog; contaminated substrate |
| CONDUCTIVITY BELOW TARGET | `#E8A020` | 4-point probe shows IACS below specification (Cu applications) | Anneal not performed or insufficient; porosity higher than expected |

Each card: H: 1.7", fill `#1E2435`, left accent rejection color.
Rejection: Barlow SemiBold, 14 pt, rejection color.
Description: Inter Regular, 12 pt, `#F0EDE8`.
Root Cause: Inter Medium, 12 pt, `#E8A020`.

---

### ZONE 5 -- Footer Band

Standard footer. Title: `Inspection and QA -- Cold Spray`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 5 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Inspection and QA Cold Spray -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The test matrix table is the anchor of this poster -- it is the reference a QA technician will consult most often. The ASTM E8 tensile testing callout should pop because it is genuinely unique to cold spray (no other thermal spray deposit can be machined into a dog-bone specimen and pull-tested). MIL-STD-3021 deserves its own prominent callout because it signals that cold spray has matured enough for military acceptance, which carries weight with aerospace customers. The three-material card layout in Zone 3 allows quick lookup by material -- operators will know what they're spraying and can go directly to the relevant card.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #528 -- Construction Workup v1.0*
*2026-04-26*
