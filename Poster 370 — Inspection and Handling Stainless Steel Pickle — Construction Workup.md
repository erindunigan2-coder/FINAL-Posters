---
Project: Plating Posters Inc
Poster Number: 370
Title: "Inspection & Handling -- Acid Pickling (Stainless Steel)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Chemical Treatment Clusters -- Watson Research Brief (CT-4.7)"
Technical Source: Industry-standard post-pickle and post-passivation inspection criteria for stainless steel. Visual inspection per ASTM A380, passivation verification per ASTM A967, clean handling protocols to prevent re-contamination, and common defect identification with root cause mapping.
Process Scope: Post-pickle / post-passivation inspection and handling for stainless steel
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - AcidPickling
  - StainlessSteel
  - Inspection
  - Handling
  - QualityControl
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT04
---

# Poster #370 -- Construction Workup
## Inspection & Handling -- Acid Pickling (Stainless Steel)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Poster 7 of 7 in the CT-04 cluster. The final poster. Everything upstream -- the pickle, the rinse, the passivation -- converges here. This poster answers two questions: "How do I know it worked?" and "How do I keep it working?" The hero visual is a defect identification gallery showing the five most common stainless-specific post-pickle defects with visual descriptions and root cause mapping. The handling section drives home the iron contamination rule: carbon steel tooling on passivated stainless is sabotage.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Defect identification gallery (Block B -- HERO):** Five defect cards with visual descriptions, cause, and root cause mapping to upstream process stages.
2. **Visual inspection criteria (Block D):** Pass/fail standards per ASTM A380.
3. **Handling rules (Block E):** Iron contamination prevention, glove requirements, storage.
4. **Cross-reference strip (Block F):** Links back to verification testing (Poster 369) and safety (Poster 365).

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
  Poster 7 of 7 highlighted (Emerald -- quality/inspection)
ZONE 3 -- DEFECT IDENTIFICATION GALLERY / HERO (4.2"--15.0" / ~10.8")
ZONE 4 -- VISUAL INSPECTION CRITERIA (15.0"--21.5" / ~6.5")
ZONE 5 -- HANDLING RULES (21.5"--27.0" / ~5.5")
ZONE 6 -- CROSS-REFERENCE + KEY PRINCIPLES (27.0"--32.5" / ~5.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `INSPECTION & HANDLING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Stainless Steel -- The Final Quality Gate` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `Good pickling is invisible. If you can see it, something went wrong. Know what to look for, know what caused it, and know how to protect what you have achieved.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Poster 7 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Freshly passivated stainless surface  -->  After: Verified, inspected, and protected for delivery or next process`

---

### ZONE 3 -- Defect Identification Gallery (HERO)

**Section label:** `WHAT WENT WRONG -- 5 STAINLESS-SPECIFIC DEFECTS` -- Y: 4.4". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK B -- Five Defect Cards (Y: 5.0" to 14.5")**

2x3 grid (2 rows, 3 columns top row + 2 columns bottom row centered):

**Top Row (Y: 5.0" to 9.5"):**

| Card | X | W | Defect | Visual | Cause | Upstream Stage |
|---|---|---|---|---|---|---|
| 1 | 0.5" | 7.33" | TEA STAINING | Rust-colored spots or streaks on otherwise bright surface | Free iron contamination from carbon steel tooling, grinding wheels, or handling | Handling / Tooling |
| 2 | 8.0" | 7.33" | INTERGRANULAR ATTACK (IGA) | Visible grain boundaries; rough, sugary texture; grains may flake | Sensitized material over-pickled; HNO3 too high relative to HF | Pickle (Stage 4) |
| 3 | 15.5" | 8.0" | ORANGE PEEL | Dimpled, textured surface resembling citrus skin | Excessive HF concentration; excessive pickle time; uneven grain size | Pickle (Stage 4) |

**Bottom Row (Y: 10.0" to 14.5"):**

| Card | X | W | Defect | Visual | Cause | Upstream Stage |
|---|---|---|---|---|---|---|
| 4 | 2.75" | 8.0" | WELD LINE ATTACK | Preferential dissolution along weld and heat-affected zone; visible groove or depression | HAZ metallurgy differs from base metal; acid attacks preferentially | Pickle (Stage 4) |
| 5 | 11.25" | 8.0" | RESIDUAL SCALE / INCOMPLETE PICKLE | Patches of heat tint or oxide remaining on surface | Acid depleted; metals too high; time too short; wrong acid for alloy | Pickle (Stage 4) |

Each card: Rounded rect H: 4.0", fill `#1E2435`, radius 6, left accent 0.06".
Defect name: Barlow SemiBold 16 pt `#E05C5C`.
Visual description: Inter Regular 12 pt `#F0EDE8` -- italic style note.
Cause: Inter Regular 12 pt `#F0EDE8`.
Upstream Stage: JetBrains Mono 11 pt, color-coded by stage accent.

---

### ZONE 4 -- Visual Inspection Criteria

**Section label:** `VISUAL INSPECTION -- PASS / FAIL CRITERIA` -- Y: 15.2". Barlow Condensed ExtraBold 24 pt `#F0EDE8`.

**Two-column layout (Y: 15.8" to 21.3"):**

**Left -- PASS Criteria (X: 0.5", W: 11.0"):**

Callout box, fill `#1E2435`, left accent `#27AE60`:

Title: `ACCEPTABLE SURFACE` Barlow SemiBold 18 pt `#27AE60`

Content (Inter Regular 13 pt `#F0EDE8`, line height 155%):
- `Uniformly bright and metallic (austenitic grades -- 304, 316)`
- `Uniformly matte gray (ferritic grades -- 430, 409)`
- `No residual heat tint, scale, or oxide`
- `No rust spots, staining, or discoloration`
- `No preferential weld attack or grain boundary grooving`
- `No pitting or surface roughening`
- `Passes copper sulfate test per ASTM A967 Practice E`
- ``
- `Reference: ASTM A380 -- Standard Practice for Cleaning, Descaling, and Passivation of Stainless Steel` Inter Regular 11 pt `#F0EDE8` at 50%

**Right -- FAIL Criteria (X: 12.0", W: 11.5"):**

Callout box, fill `#1E2435`, left accent `#E05C5C`:

Title: `REJECTABLE CONDITIONS` Barlow SemiBold 18 pt `#E05C5C`

Content:
- `Any rust spots or tea staining` Inter Medium 13 pt `#E05C5C`
- `Copper deposit on copper sulfate test (free iron present)` Inter Medium 13 pt `#E05C5C`
- `Residual scale or heat tint` Inter Medium 13 pt `#E05C5C`
- `Grain boundary grooving (IGA)` Inter Medium 13 pt `#E05C5C`
- `Pitting from over-pickling or crevice attack` Inter Medium 13 pt `#E05C5C`
- `Orange peel texture` Inter Medium 13 pt `#E05C5C`
- ``
- `Action: identify root cause (defect gallery above), correct upstream process, and re-process.` Inter Regular 13 pt `#F0EDE8`
- `IGA and pitting may be IRREVERSIBLE -- parts may require scrapping.` Inter Medium 12 pt `#E05C5C`

---

### ZONE 5 -- Handling Rules

**Section label:** `HANDLING -- PROTECT THE PASSIVE FILM` -- Y: 21.7". Barlow Condensed ExtraBold 24 pt `#F0EDE8`.

**Three handling cards in a row (Y: 22.3" to 26.8"):**

| Card | X | W | Title | Accent | Content |
|---|---|---|---|---|---|
| IRON CONTAMINATION | 0.5" | 7.33" | `THE #1 ENEMY` | `#E05C5C` | Carbon steel tooling, fixtures, grinding wheels, wire brushes, and work surfaces transfer free iron to passivated stainless. This iron rusts and stains the surface. USE STAINLESS-ONLY TOOLS: SS wire brushes, SS clamps, SS work tables. NEVER set passivated stainless on a carbon steel bench. |
| GLOVES & HANDLING | 8.0" | 7.33" | `CLEAN HANDLING` | `#2EC4B6` | Wear clean nitrile or cotton gloves at all times. Fingerprints on passivated stainless can cause localized corrosion. Do not touch the passive surface with bare hands. If plating follows: transfer to strike plating within 30 minutes. |
| STORAGE | 15.5" | 8.0" | `STORAGE` | `#E8A020` | Store passivated parts in a clean, dry environment. Wrap in VCI (vapor corrosion inhibitor) paper for long-term storage. Avoid plastic wrap in direct contact (traps moisture). Do not stack parts -- contact areas can create crevice conditions. |

Each card: Rounded rect H: 4.0", fill `#1E2435`, radius 6, left accent 0.06".
Title: Barlow SemiBold 16 pt, accent color.
Content: Inter Regular 12 pt `#F0EDE8`.

---

### ZONE 6 -- Cross-Reference + Key Principles

**Two-column layout (Y: 27.2" to 32.3"):**

**Left -- Cross-Reference to Cluster (X: 0.5", W: 11.0"):**

Callout box, fill `#1E2435`, left accent `#2EC4B6`:

Title: `CT-04 CLUSTER CROSS-REFERENCE` Barlow SemiBold 16 pt `#2EC4B6`

| Poster | Topic |
|---|---|
| #364 | Process Flow (complete sequence) |
| #365 | Safety & PPE (HF hazard -- CRITICAL) |
| #366 | Bath Preparation & Control |
| #367 | Pickling Stage (scale removal) |
| #368 | Rinse (triple rinse, fluoride testing) |
| #369 | Passivation (Cr2O3 restoration) |
| #370 | Inspection & Handling (THIS POSTER) |

**Right -- Key Principles (X: 12.0", W: 11.5"):**

Four principle cards stacked vertically.

| Principle | Accent |
|---|---|
| Good pickling is invisible. If the surface looks wrong, something upstream failed. | `#27AE60` |
| The copper sulfate test takes 6 seconds. There is no excuse for shipping without it. | `#E8A020` |
| Carbon steel tooling on passivated stainless undoes everything the pickle and passivation achieved. | `#E05C5C` |
| IGA and crevice pitting are irreversible. Prevention (correct acid ratio, correct time) is the only cure. | `#E05C5C` |

Each card: Rounded rect H: 1.1", fill `#1E2435`, left accent 0.06".
Content: Inter Medium 13 pt, `#F0EDE8`.

---

### ZONE 7 -- Footer

Standard. Title: `Inspection & Handling -- Acid Pickling (Stainless Steel)`. Version `v1.0 -- 2026`.
Disclaimer: `Source: ASTM A380; ASTM A967; general industry knowledge. Inspection criteria and handling requirements vary by customer specification and end-use application. IGA and pitting damage from over-pickling may be irreversible. Consult your metallurgist and process supplier for alloy-specific guidance.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Inspection Handling Stainless Steel Pickle -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster closes the CT-04 cluster with the quality gate. The defect gallery (Zone 3) is the visual anchor -- five defects that a shop floor inspector can reference immediately when something looks wrong. The root cause mapping (which upstream stage caused the defect) ties each defect back to the process poster where the fix lives. The iron contamination card (Zone 5) is the most practical piece of advice on the poster and the most commonly violated rule in stainless fabrication shops. The cross-reference table (Zone 6) turns the individual poster into a series navigation tool -- useful when this poster is hanging on a wall and the inspector needs to look up rinse details or safety protocols.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #370 -- Construction Workup v1.0*
*2026-04-26*
