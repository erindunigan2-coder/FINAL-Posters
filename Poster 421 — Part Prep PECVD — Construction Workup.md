---
Project: Plating Posters Inc
Poster Number: 421
Title: "Part Prep -- PECVD"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 3: PECVD, Section 3.4)"
Technical Source: PECVD substrate preparation requirements. Broad substrate compatibility (Si wafers, glass, polymers, Al alloys, steel) is PECVD's strength -- but each substrate type has different prep needs. Particulate control is critical because thin films (~nm to um) cannot bury particles.
Process Scope: PECVD substrate inspection, compatibility verification, masking, and pre-process preparation
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - PECVD
  - PartPrep
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #421 -- Construction Workup
## Part Prep -- PECVD

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 1 of the PECVD sequence. This poster covers what happens before anything enters the cleanroom or vacuum chamber: substrate inspection, compatibility checks, masking, and pre-qualification. PECVD's low temperature opens it to substrates that thermal CVD cannot touch -- but each substrate type has prep requirements.

Hero visual: substrate compatibility matrix showing temperature limits for each substrate family.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Substrate compatibility matrix (Block B -- HERO):** Table/grid showing substrate types vs. max PECVD temperature.
2. **Pre-process checklist (Block C):** Visual inspection and preparation steps.
3. **Substrate-specific notes panel (Block D):** Callout boxes for Si wafers, polymers, glass, metals.
4. **Contamination sensitivity callout (Block E):** Why particles are fatal to thin films.
5. **Masking guidance (Block F):** When and how to mask areas that should not be coated.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 13.5" / 19.5" / 26.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 1 highlighted (Teal)
ZONE 3 -- SUBSTRATE COMPATIBILITY HERO (4.2"--13.5" / ~9.3")
  Block B: Substrate type vs. temperature matrix
ZONE 4 -- PRE-PROCESS INSPECTION (13.5"--19.5" / ~6.0")
  Block C: Visual inspection checklist
  Block D: Substrate-specific notes (4 callout boxes)
ZONE 5 -- CONTAMINATION + MASKING (19.5"--32.5" / ~13.0")
  Block E: Contamination sensitivity callout
  Block F: Masking guidance
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `PART PREPARATION` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `PECVD -- Stage 1 of 10 -- Substrate Inspection & Qualification` -- 30 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `PECVD coats what CVD cannot -- polymers, glass, assembled devices. But every substrate has rules. Know them before you load the chamber.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

**Rule Card (top right):**
- Rounded rect, X: 17.0", Y: 0.5", W: 6.5", H: 2.2", fill `#1E2435`, border 1 pt `#2EC4B6`
- Big number: `25-400` -- Barlow Condensed ExtraBold, 60 pt, `#2EC4B6`
- Label: `degC RANGE` -- JetBrains Mono Regular, 14 pt, `#F0EDE8` at 70%
- Sub-label: `Substrate temperature window` -- Inter Regular, 12 pt, `#F0EDE8` at 50%

---

### ZONE 2 -- Orientation Strip

Y: 2.9" to 4.2". Ten stage indicators, Stage 1 highlighted.
- Stage 1 (`Part Prep`): fill `#2EC4B6`, text `#1A1F2E`
- All others: fill `#252B3D`, text `#F0EDE8` at 50%

Below strip: `Input: Raw substrates (wafers, panels, parts)  -->  Output: Inspected, qualified, ready for cleaning`

---

### ZONE 3 -- Substrate Compatibility Hero

**Section label:** `SUBSTRATE COMPATIBILITY -- WHAT CAN YOU COAT?` -- Y: 4.4".

**BLOCK B -- Compatibility Matrix**

Y: 5.0" to 13.3". Rounded rect panel, fill `#1E2435`.

Table with 7 rows:

| Substrate | Max Temp (degC) | Typical PECVD Films | Prep Notes | Accent |
|---|---|---|---|---|
| Silicon wafers | 400 | SiO2, Si3N4, a-Si:H | Standard semiconductor clean (RCA); Class 100 cleanroom | `#2EC4B6` |
| Glass (soda-lime, borosilicate) | 350--400 | SiO2, Si3N4, ITO | Solvent clean; avoid Na migration above 350 degC | `#2EC4B6` |
| Polymers (PET, PC, PMMA) | 80--150 | SiOx barrier, DLC | O2 plasma activation CRITICAL for adhesion; handle with gloves | `#E8A020` |
| Aluminum alloys | 200--350 | SiO2, DLC, barrier | Alkaline clean; avoid exceeding age-hardening temp | `#27AE60` |
| Steel / tool steel | 300--400 | DLC (a-C:H), SiCN | Must not exceed tempering temperature; alkaline + IPA clean | `#27AE60` |
| Assembled devices | 80--200 | Passivation, encapsulation | Verify all components survive process temp; no outgassing materials | `#E05C5C` |
| Temperature-sensitive components | 25--100 | Ultra-thin barriers | Plasma-enhanced at lowest temps; verify adhesion carefully | `#E05C5C` |

Header: Barlow SemiBold, 14 pt, `#F0EDE8`, fill `#3A4055`.
Data rows: alternating `#1E2435` / `#252B3D`. Left accent strip 4 pt per row.
Max Temp: JetBrains Mono Regular, 14 pt, accent color (bold).
All other data: Inter Regular, 12 pt, `#F0EDE8`.

Bottom callout:
- `The lower your substrate's temperature limit, the more important plasma pre-cleaning becomes -- you cannot bake off contamination, so plasma must do the work.` -- Inter Medium, 13 pt, `#E8A020`

---

### ZONE 4 -- Pre-Process Inspection

**Section label:** `PRE-PROCESS INSPECTION CHECKLIST` -- Y: 13.7".

**BLOCK C -- Inspection Steps (Left, X: 0.5", W: 11.0")**

Y: 14.3" to 19.3". Six inspection items in vertical list.

Each item: Rounded rect, W: 11.0", H: 0.7", fill `#1E2435`, left accent 3 pt `#2EC4B6`.

1. `Visual inspection: no cracks, chips, burrs, or delamination` -- `REJECT parts with visible defects`
2. `Surface contamination: no fingerprints, oils, water spots` -- `Handle only with clean nitrile gloves`
3. `Dimensional check: parts fit fixture/electrode holder` -- `Verify thermal contact surface area`
4. `Masking applied: non-coat areas protected` -- `Use vacuum-compatible tape or fixtures`
5. `Outgassing check: no adhesives, polymers that off-gas in vacuum` -- `Outgassing contaminates the entire chamber`
6. `Documentation: substrate type, target film, recipe logged` -- `Traceability for QA`

**BLOCK D -- Substrate-Specific Notes (Right, X: 12.0", W: 11.5")**

Four small callout boxes stacked vertically:

| Substrate | Key Note | Accent |
|---|---|---|
| Si Wafers | Store in FOUP or cassette. Handle by edges only. N2 purge storage for HF-last surfaces. | `#2EC4B6` |
| Polymers | O2 plasma activation 1--5 min dramatically improves adhesion. Without it, films peel. | `#E8A020` |
| Glass | Clean with lint-free wipes + IPA. Particulates on glass = pinholes in film. | `#2EC4B6` |
| Metals | Alkaline ultrasonic 50--70 degC, 10--15 min. Rinse thoroughly. Vacuum dry. | `#27AE60` |

Each box: Rounded rect, W: 11.5", H: 1.1", fill `#1E2435`, left accent 0.06".

---

### ZONE 5 -- Contamination Sensitivity + Masking

**BLOCK E -- Contamination Sensitivity (Y: 19.7" to 25.5")**

Section label: `WHY PARTICLES KILL THIN FILMS` -- Barlow Condensed ExtraBold, 24 pt, `#E05C5C`. Y: 19.9".

Large callout panel: Rounded rect, X: 0.5", Y: 20.5", W: 23.0", H: 4.8", fill `#1E2435`, left accent 0.06" `#E05C5C`.

Left (X: 1.5", W: 10.0"):
- Barlow SemiBold, 20 pt, `#E05C5C`: `PECVD films are 0.01--5 um thick.`
- Inter Regular, 14 pt, `#F0EDE8`: `A 10 um particle is a mountain on a 100 nm film. The film conformally coats the particle, creating a bump defect. In semiconductor devices, one particle = one dead chip.`
- JetBrains Mono, 13 pt, `#F0EDE8`: `Cleanroom classes for PECVD:`
```
Semiconductor: Class 100 (ISO 5)
Display/solar: Class 1000 (ISO 6)
Industrial DLC: Class 10,000 (ISO 7) min
```

Right (X: 12.5", W: 10.5"):
- Barlow SemiBold, 18 pt, `#F0EDE8`: `Contamination Sources`
```
Fingerprints (oils + salt crystals)
Airborne dust (fibers, skin flakes)
Packaging debris (cardboard, foam)
Tool marks (metal particles from handling)
Outgassing (adhesives, plastics, lubricants)
Previous process residue (etch byproducts)
```
Each source: Inter Regular, 13 pt, `#F0EDE8`. Bullet: `#E05C5C`.

**BLOCK F -- Masking Guidance (Y: 26.0" to 32.3")**

Section label: `MASKING -- PROTECTING NON-COAT AREAS` -- Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`. Y: 26.2".

Two-column layout:

Left -- When to Mask (X: 0.5", W: 11.0"):
- Callout box, fill `#1E2435`, left accent `#E8A020`
- Items:
```
Electrical contacts that must remain uncoated
Threaded holes or precision bores
Sealing surfaces (O-ring grooves)
Areas requiring subsequent bonding/welding
Backside of wafers (if single-side coat)
```

Right -- Masking Materials (X: 12.0", W: 11.5"):
- Table:

| Material | Max Temp | Notes |
|---|---|---|
| Kapton tape | 400 degC | Gold standard for PECVD masking |
| Aluminum foil | 400+ degC | Conforms well; may leave residue |
| Shadow masks (metal) | 400+ degC | Best for production; custom machined |
| Fixture design | 400+ degC | Parts held so only target surface exposed |

Note at bottom: `All masking materials must be vacuum-compatible -- no outgassing. Test new materials with RGA (residual gas analyzer) before production use.` -- Inter Medium, 12 pt, `#E8A020`

---

### ZONE 6 -- Footer

Standard. Title: `Part Prep -- PECVD`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Part Prep PECVD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

PECVD's substrate flexibility is its superpower -- this poster should celebrate that range while making clear that each substrate type has its own rules. The contamination callout (Block E) should be visually arresting -- the "mountain on a plain" analogy is the key mental image. Polymer substrates get special attention because plasma activation is a make-or-break step that many newcomers skip.

---

*Alaina -- Poster #421 -- Construction Workup v1.0 -- 2026-04-26*
