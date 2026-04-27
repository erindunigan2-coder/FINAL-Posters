---
Project: Plating Posters Inc
Poster Number: 512
Title: "Grit Blasting -- Arc Spray"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Thermal Spray Clusters -- Watson Research Brief (Cluster 4: Arc Spray)"
Process Scope: Grit blasting / surface preparation for arc spray -- media, profiles, field blasting, environmental compliance
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ThermalSpray
  - ArcSpray
  - GritBlasting
  - ConstructionWorkup
  - ClusterTS04
---

# Poster #512 -- Construction Workup
## Grit Blasting -- Arc Spray

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Grit blasting for arc spray. Arc spray shares the same bonding mechanism as flame spray -- mechanical interlocking -- so a robust anchor profile is critical. The difference: arc spray work is often done in the field on massive structural steel, so this poster covers field blasting considerations (containment, lead paint testing, spent media disposal, dew point rules) alongside standard shop parameters. Steel grit is preferred for structural work because it is recyclable.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Blast parameter table (Block B -- HERO):** Large reference table with media, pressure, profile, and cleanliness specifications.
2. **Field blasting considerations (Block C):** Environmental and regulatory panel.
3. **Media selection guide (Block D):** Steel grit vs. alumina -- when to use each.
4. **Profile verification methods (Block E):** Three measurement techniques.
5. **Ambient conditions strip (Block F):** Dew point rule and weather hold criteria.

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
  Block B: Blast parameter table
  Block C: Field blasting considerations
ZONE 4 -- MEDIA SELECTION (14.0"--20.5" / ~6.5")
  Block D: Steel grit vs. alumina comparison
ZONE 5 -- PROFILE VERIFICATION (20.5"--27.0" / ~6.5")
  Block E: Three verification methods
ZONE 6 -- AMBIENT CONDITIONS (27.0"--32.5" / ~5.5")
  Block F: Dew point and weather rules
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `GRIT BLASTING` -- 88 pt `#F0EDE8`.
**Subheading:** `Arc Spray -- Creating the Anchor Profile` -- 36 pt `#2EC4B6` (Teal).
**Tagline:** `Arc spray coatings bond by mechanical interlocking -- the anchor profile IS the bond. No profile, no coating. This step is not optional and it is not negotiable.` -- 22 pt `#F0EDE8` at 65%.

---

### ZONE 2 -- Orientation Strip

Stage 2 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Surface cleaned and dried --> After: Anchor profile created, ready for masking or immediate spray`

---

### ZONE 3 -- Blast Parameters (HERO)

**Section label:** `BLAST SPECIFICATION FOR ARC SPRAY` -- Y: 4.4".

**BLOCK B -- Blast Parameter Table**

Y: 5.0" to 9.5". Full width.

| Parameter | Typical Range | Notes |
|---|---|---|
| Media | Angular steel grit (G25, G40) or aluminum oxide (24--36 mesh) | Steel grit preferred for structural work -- recyclable |
| Blast pressure | 60--100 PSI (415--690 kPa) | More aggressive than APS/HVOF; compensates for lower particle velocity |
| Nozzle distance | 150--300 mm (6--12 in) | Closer for deeper profile; farther for broader coverage |
| Blast angle | 60--90 degrees to surface | 90 degrees optimal; minimum 45 degrees |
| Anchor profile (Ra) | 4--12 microns (175--500 microinches) | Rougher profile needed -- low particle velocity relies on mechanical interlock |
| Surface cleanliness | SSPC-SP 5 (White Metal) per AWS C2.18 | SP 10 (Near-White) acceptable for some specifications |

Table header: fill `#3A4055`, H: 0.6". Barlow SemiBold, 14 pt, `#F0EDE8`.
Data rows: alternating `#1E2435` / `#252B3D`, H: 0.65".
Parameter names: Inter Medium 14 pt `#F0EDE8`. Values: JetBrains Mono 13 pt `#E8A020`. Notes: Inter Regular 12 pt at 70%.

**BLOCK C -- Field Blasting Considerations**

Y: 10.0" to 13.5". Rounded rect, fill `#1E2435`, left accent `#E8A020`, W: 23.0".

Title: `FIELD BLASTING -- ENVIRONMENTAL & REGULATORY` Barlow SemiBold 18 pt `#E8A020`.

Bullet list (Inter Regular 14 pt, line height 160%):
- `Containment required: blast curtains, vacuum recovery, or full enclosure for lead paint removal`
- `Spent blast media must be tested for lead and hexavalent chromium before disposal`
- `Steel grit is recyclable -- alumina is not. Cost advantage for steel grit on large jobs.`
- `Dust suppression: wet blasting or vacuum recovery to control airborne particulate`
- `Worker exposure monitoring: silica, lead, and metal fumes per OSHA PEL`
- `All waste disposal per local and federal regulations (RCRA if hazardous)`

---

### ZONE 4 -- Media Selection

**Section label:** `MEDIA SELECTION -- STEEL GRIT VS. ALUMINA` -- Y: 14.2".

**BLOCK D -- Side-by-Side Comparison**

Y: 14.8" to 20.0".

**Left -- Steel Grit (X: 0.5", W: 11.0"):**
- Rounded rect, fill `#1E2435`, left accent `#E8A020`
- Title: `ANGULAR STEEL GRIT (G25--G40)` Barlow SemiBold 16 pt `#E8A020`
- `Hardness: 7--8 Mohs`
- `Recyclable: 100+ cycles before replacement`
- `Aggressive profile on carbon and low-alloy steel`
- `Lower per-use cost for large-area work`
- `NOT for use on stainless steel, aluminum, or titanium (ferrous contamination)`
- `Standard for bridge and infrastructure work`

**Right -- Aluminum Oxide (X: 12.0", W: 11.5"):**
- Rounded rect, fill `#1E2435`, left accent `#2EC4B6`
- Title: `ALUMINUM OXIDE (24--36 MESH)` Barlow SemiBold 16 pt `#2EC4B6`
- `Hardness: 9 Mohs (harder than steel grit)`
- `Not recyclable: single-use for most applications`
- `Self-sharpening: fractures to expose fresh cutting edges`
- `No ferrous contamination -- safe for all substrates`
- `Required for stainless steel and non-ferrous metals`
- `Higher per-use cost; preferred for shop/precision work`

Below panels:
- Callout: `For structural steel corrosion protection (the primary arc spray market), steel grit is the standard choice -- it is cheaper, recyclable, and produces an excellent profile on carbon steel.` Inter Regular 13 pt `#F0EDE8` at 60%.

---

### ZONE 5 -- Profile Verification

**Section label:** `PROFILE VERIFICATION METHODS` -- Y: 20.7".

**BLOCK E -- Three Verification Methods**

Y: 21.3" to 26.5". Three cards in a row.

**Card 1 -- Testex Replica Tape (X: 0.5", W: 7.3"):**
- Rounded rect, fill `#1E2435`, top accent `#27AE60`
- Title: `TESTEX REPLICA TAPE` Barlow SemiBold 16 pt `#27AE60`
- `Field-portable; fast; no power required`
- `Press tape onto blasted surface; measure thickness with spring micrometer`
- `Subtract tape backing (2 mils / 50 um)`
- `Accuracy: +/- 0.5 mil (+/- 12.5 um)`
- `Coarse grade for Ra 4--12 um range`

**Card 2 -- Surface Profilometer (X: 8.15", W: 7.3"):**
- Rounded rect, fill `#1E2435`, top accent `#2EC4B6`
- Title: `SURFACE PROFILOMETER` Barlow SemiBold 16 pt `#2EC4B6`
- `Electronic measurement of Ra and Rz`
- `Higher accuracy than replica tape`
- `Requires calibration and clean surface`
- `Preferred for shop work and specification disputes`
- `Records data for QA documentation`

**Card 3 -- Visual Comparator (X: 15.85", W: 7.3"):**
- Rounded rect, fill `#1E2435`, top accent `#E8A020`
- Title: `VISUAL COMPARATOR (SSPC-VIS 1)` Barlow SemiBold 16 pt `#E8A020`
- `Reference plates showing standard surface profiles`
- `Quick field check -- compare blasted surface to reference`
- `Subjective; not for final acceptance`
- `Useful for operator training and initial assessment`
- `Always confirm with replica tape or profilometer for spec compliance`

---

### ZONE 6 -- Ambient Conditions

**Section label:** `AMBIENT CONDITIONS -- WHEN TO HOLD` -- Y: 27.2".

**BLOCK F -- Environmental Rules**

Y: 27.8" to 32.0". Four cards in a row.

Each card: W: 5.5", H: 3.5", fill `#1E2435`, left accent varies.

| Card | X | Rule | Detail | Accent |
|---|---|---|---|---|
| 1 | 0.5" | DEW POINT RULE | Do not blast if surface temperature is within 3 degC (5 degF) of dew point. Condensation on blasted surface causes instant flash rust. | `#E05C5C` |
| 2 | 6.33" | RAIN / SNOW HOLD | Stop blasting in precipitation. Wet surfaces cannot be blasted to SSPC-SP 5. Resume only after surface is confirmed dry. | `#E05C5C` |
| 3 | 12.16" | WIND HOLD | High winds (>25 mph) scatter blast media and reduce operator control. Containment may be required by local regulation. | `#E8A020` |
| 4 | 18.0" | TEMPERATURE MINIMUM | Surface temperature >5 degC (40 degF) minimum for most specifications. Cold steel is harder to clean and flash rusts faster. | `#E8A020` |

Rule: Barlow SemiBold 14 pt accent color. Detail: Inter Regular 13 pt `#F0EDE8`.

---

### ZONE 7 -- Footer

Standard footer. Title: `Grit Blasting -- Arc Spray`. Version `v1.0 -- 2026`.
Disclaimer: `Source: AWS C2.18; SSPC surface preparation standards; SSPC-PA 2; general industry knowledge. Profile and cleanliness requirements vary by specification. Always follow the applicable coating specification and local environmental regulations.`

---

## Parts 5--7

**Grouping:** 7 zones. **Light Remap:** Standard. **Export:** Six files.

---

*Alaina -- Poster #512 -- Construction Workup v1.0 -- 2026-04-26*
