---
Project: Plating Posters Inc
Poster Number: 368
Title: "Rinse / Post-Pickle -- Acid Pickling (Stainless Steel)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Chemical Treatment Clusters -- Watson Research Brief (CT-4.5)"
Technical Source: Industry-standard rinse requirements after HNO3/HF stainless steel pickling. Triple rinse minimum for HF residue removal. Fluoride testing, conductivity targets, and drag-out capture for HF-bearing waste. ASTM A380 reference.
Process Scope: Post-pickle rinse for stainless steel -- fluoride removal and drag-out capture
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - AcidPickling
  - StainlessSteel
  - Rinse
  - PostPickle
  - FluorideRemoval
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT04
---

# Poster #368 -- Construction Workup
## Rinse / Post-Pickle -- Acid Pickling (Stainless Steel)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Poster 5 of 7 in the CT-04 cluster. This is NOT a standard rinse poster. When HF is in the pickle, HF is in the drag-out. HF residue on parts is a personnel safety hazard and an environmental compliance issue. The hero concept is the triple rinse system -- three stages minimum, with the first stage dedicated to drag-out capture. The fluoride ion testing requirement distinguishes this poster from every other rinse poster in the series: conductivity alone is not sufficient. You must verify that fluoride is below limits before parts leave the rinse section.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Triple rinse system hero (Block B):** Three-tank cascade with drag-out capture first stage.
2. **Fluoride testing panel (Block D):** Why conductivity alone is insufficient; fluoride-specific ion electrode or colorimetric test required.
3. **HF drag-out safety (Block E):** HF residue on parts is a contact hazard for downstream operators.
4. **Waste stream considerations (Block F):** Fluoride-bearing rinse water requires special treatment.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.0" / 21.5" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Poster 5 of 7 highlighted (Teal -- rinse context)
ZONE 3 -- TRIPLE RINSE SYSTEM HERO (4.2"--15.0" / ~10.8")
ZONE 4 -- FLUORIDE TESTING (15.0"--21.5" / ~6.5")
ZONE 5 -- HF DRAG-OUT SAFETY (21.5"--27.0" / ~5.5")
ZONE 6 -- WASTE STREAM CONSIDERATIONS (27.0"--32.5" / ~5.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE -- POST-PICKLE` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Stainless Steel -- Triple Rinse Minimum for HF Removal` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `When your pickle contains hydrofluoric acid, your rinse is not just about cleanliness. It is about safety. HF on parts is HF on the next operator's hands. Three rinses minimum. Test for fluoride.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Poster 5 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Parts coated with HNO3/HF residue (HAZARDOUS)  -->  After: Acid-free, fluoride-free surface ready for passivation`

---

### ZONE 3 -- Triple Rinse System Hero

**Section label:** `TRIPLE RINSE -- THREE STAGES, THREE FUNCTIONS` -- Y: 4.4". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK B -- Three-Tank Cascade Diagram (Y: 5.0" to 14.5")**

Three tank rectangles in a row:

**Tank 1 -- Drag-Out Capture (X: 0.5", W: 7.33"):**
- Rounded rect H: 9.0", fill `#252B3D`, border 2 pt `#E05C5C`
- Title inside top: `STAGE 1 -- DRAG-OUT CAPTURE` Barlow SemiBold 16 pt `#E05C5C`
- Badge: `STAGNANT` fill `#E05C5C`, text `#F0EDE8`
- Content:
```
Type: Stagnant or slow-flow
Purpose: Capture concentrated HNO3/HF drag-out
Water: City water acceptable
This tank gets DIRTY -- that is its job

Drag-out from this tank can be:
  - Returned to pickle tank (extends bath life)
  - Collected for waste treatment

DO NOT overflow this tank into the
general rinse drain. HF waste requires
SEPARATE treatment.
```

**Tank 2 -- Counterflow Rinse 1 (X: 8.16", W: 7.17"):**
- Rounded rect H: 9.0", fill `#252B3D`, border 1 pt `#2EC4B6`
- Title: `STAGE 2 -- COUNTERFLOW RINSE` Barlow SemiBold 16 pt `#2EC4B6`
- Badge: `FLOWING` fill `#2EC4B6`, text `#1A1F2E`
- Content:
```
Type: Flowing counterflow
Purpose: Remove bulk acid residue
Water: City water
Overflow from Stage 3 feeds this tank

Conductivity target: < 200 uS/cm
```

**Tank 3 -- Final Rinse (X: 15.66", W: 7.84"):**
- Rounded rect H: 9.0", fill `#252B3D`, border 2 pt `#27AE60`
- Title: `STAGE 3 -- FINAL RINSE` Barlow SemiBold 16 pt `#27AE60`
- Badge: `DI PREFERRED` fill `#27AE60`, text `#1A1F2E`
- Content:
```
Type: DI water (preferred) or clean city water
Purpose: Final cleanliness before passivation
Fresh water enters HERE (cleanest stage)

Conductivity target: < 50 uS/cm
FLUORIDE TEST: Must pass (see Zone 4)

Parts exiting this tank must be
free of acid residue and safe to handle.
```

**Part flow (top, left to right):** Arrow 4 pt `#F0EDE8` with label `PARTS MOVE THIS WAY -->`
**Water flow (bottom, right to left):** Arrow 4 pt `#2EC4B6` with label `<-- FRESH WATER IN` at Tank 3, `TO WASTE TREATMENT -->` at Tank 1

---

### ZONE 4 -- Fluoride Testing

**Section label:** `FLUORIDE TESTING -- CONDUCTIVITY ALONE IS NOT ENOUGH` -- Y: 15.2". Barlow Condensed ExtraBold 24 pt `#E8A020`.

**Two-column layout (Y: 15.8" to 21.3"):**

**Left -- Why Fluoride Testing Matters (X: 0.5", W: 11.0"):**

Callout box, fill `#1E2435`, left accent `#E8A020`:

Title: `THE FLUORIDE PROBLEM` Barlow SemiBold 18 pt `#E8A020`

Content (Inter Regular 13 pt `#F0EDE8`, line height 155%):
- `Conductivity meters measure total dissolved ions.`
- `They do NOT distinguish fluoride from sulfate, nitrate, or chloride.`
- `A rinse can read < 50 uS/cm and still contain enough residual fluoride to:`
- `  -- Cause corrosion on the stainless surface`
- `  -- Violate POTW discharge limits (typically 10--20 mg/L fluoride)`
- `  -- Present a skin contact hazard to downstream operators`
- ``
- `You need a fluoride-specific test.` Inter Medium 14 pt `#E05C5C`

**Right -- Test Methods (X: 12.0", W: 11.5"):**

Callout box, fill `#1E2435`, left accent `#2EC4B6`:

Title: `FLUORIDE TEST OPTIONS` Barlow SemiBold 18 pt `#2EC4B6`

| Method | Equipment | Range | Speed |
|---|---|---|---|
| Fluoride ISE (ion-selective electrode) | ISE probe + meter | 0.1--10,000 ppm | 2--3 min |
| Colorimetric test kit | Reagent kit (SPADNS or Alizarin) | 0--5 ppm (typical kit) | 5--10 min |
| Lab analysis (IC) | Send to lab (ion chromatography) | ppb to ppm | 1--3 days |

Data: JetBrains Mono 12 pt. Method names: Inter Medium 13 pt.

Below: `For daily production, a fluoride ISE probe on the final rinse stage is the best investment. For smaller shops, a colorimetric kit works. Either way -- TEST.` Inter Medium 12 pt `#27AE60`

---

### ZONE 5 -- HF Drag-Out Safety

**Section label:** `HF DRAG-OUT -- THE HIDDEN HAZARD` -- Y: 21.7". Barlow Condensed ExtraBold 24 pt `#E05C5C`.

**BLOCK E -- Full-Width Safety Panel (Y: 22.3" to 26.8")**

Rounded rect W: 23.0", H: 4.0", fill `#E05C5C` at 12%, border 2 pt `#E05C5C`, radius 8.

**Three-column interior:**

**Left -- The Risk (W: 7.0"):**
- Title: `THE RISK` Barlow SemiBold 16 pt `#E05C5C`
- Content:
```
Parts exiting the pickle carry HNO3
and HF on their surfaces.

If rinsing is inadequate, the NEXT
operator who handles these parts
contacts HF residue.

HF skin contact can be fatal.
(See Safety Poster #365)
```

**Center -- Drain Time (W: 7.0"):**
- Title: `DRAIN OVER PICKLE TANK` Barlow SemiBold 16 pt `#E8A020`
- Content:
```
MINIMUM 15 seconds drain time
above the pickle tank before
transferring to rinse.

This reduces drag-out volume by
60-80% and reduces the HF load
on all three rinse stages.

Slow withdrawal. Full drain.
No dripping onto the floor.
```

**Right -- Handling (W: 7.0"):**
- Title: `DOWNSTREAM HANDLING` Barlow SemiBold 16 pt `#27AE60`
- Content:
```
After triple rinse and fluoride
verification:
  - Parts are safe to handle with
    standard nitrile gloves
  - No HF-rated PPE required
    downstream of verified rinse

BEFORE verification:
  - Treat all parts as HF-contaminated
  - Butyl rubber gloves required
  - No bare skin contact
```

---

### ZONE 6 -- Waste Stream Considerations

**Section label:** `FLUORIDE WASTE -- SPECIAL TREATMENT REQUIRED` -- Y: 27.2". Barlow Condensed ExtraBold 22 pt `#F0EDE8`.

**Two-column layout (Y: 27.8" to 32.3"):**

**Left -- Treatment Method (X: 0.5", W: 11.0"):**

Callout box, fill `#1E2435`, left accent `#E8A020`:

Title: `FLUORIDE PRECIPITATION` Barlow SemiBold 16 pt `#E8A020`

Content:
- `Fluoride-bearing rinse water cannot be discharged directly.`
- `POTW discharge limit: typically 10--20 mg/L fluoride (check local permit).`
- ``
- `Treatment method:` Inter Medium 13 pt `#F0EDE8`
- `Add calcium chloride (CaCl2) to precipitate calcium fluoride (CaF2):` JetBrains Mono 12 pt
- `2F- + Ca2+ --> CaF2 (insoluble precipitate)` JetBrains Mono 13 pt `#E8A020`
- `CaF2 settles; remove by clarification.`
- `Sludge disposal: per local hazardous waste regulations.`

**Right -- Segregation (X: 12.0", W: 11.5"):**

Callout box, fill `#1E2435`, left accent `#E05C5C`:

Title: `WASTE SEGREGATION` Barlow SemiBold 16 pt `#E05C5C`

Content:
- `HF-bearing rinse water must be SEGREGATED from general acid rinse water.` Inter Medium 13 pt `#E05C5C`
- ``
- `Reason: fluoride requires dedicated treatment (calcium precipitation) that general acid waste does not.` Inter Regular 13 pt `#F0EDE8`
- ``
- `Drag-out tank (Stage 1) overflow should route to a dedicated fluoride waste collection system, NOT the general acid drain.`
- ``
- `If your shop also runs cyanide processes: triple segregation is required -- cyanide, fluoride, general acid. All three are incompatible.`

---

### ZONE 7 -- Footer

Standard. Title: `Rinse / Post-Pickle -- Acid Pickling (Stainless Steel)`. Version `v1.0 -- 2026`.
Disclaimer: `Source: ASTM A380; general industry knowledge. Fluoride discharge limits are set by local POTW permits and may be more restrictive than federal minimums. Fluoride waste treatment methods must comply with EPA and state regulations. Consult your environmental compliance officer.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Post-Pickle Stainless Steel -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This rinse poster has more in common with a safety poster than a typical rinse poster. The HF drag-out hazard (Zone 5) transforms what would normally be a water-quality discussion into a life-safety discussion. The fluoride testing requirement (Zone 4) is the single most actionable piece of information: conductivity is not enough. Every other rinse poster in the series relies on conductivity as the primary quality metric. This poster says "conductivity plus fluoride." The triple rinse diagram (Zone 3) visually separates the three stages by function: capture, clean, verify. The waste segregation note (Zone 6) closes the loop -- HF waste is not general acid waste and must be treated differently.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #368 -- Construction Workup v1.0*
*2026-04-26*
