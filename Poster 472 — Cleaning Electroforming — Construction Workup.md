---
Project: Plating Posters Inc
Poster Number: 472
Title: "Cleaning -- Electroforming"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters — Watson Research Brief (Cluster 8, Sections 8.3--8.4)"
Technical Source: Pre-electroforming cleaning of mandrels. Contamination on the mandrel surface transfers directly to the electroformed part's interior surface. Alkaline cleaning, solvent wipe, and activation prior to immersion. Cleaning requirements vary by mandrel material.
Process Scope: Electroforming -- mandrel cleaning and activation
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Electroforming
  - Cleaning
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #472 -- Construction Workup
## Cleaning -- Electroforming

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Cleaning for electroforming follows the same principle as cleaning for electropolishing: the process replicates the surface exactly. Any contamination on the mandrel becomes trapped at the interface between the mandrel and the deposit -- causing adhesion failure, pitting, voids, or rough interior surfaces. Since the interior IS the precision surface, contamination at this interface is catastrophic.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cleaning sequence by mandrel type (Block B -- HERO):** Three cleaning pathways for permanent, expendable, and non-conductive mandrels.
2. **Contamination effects table (Block D):** What each type of contamination does to the electroform.
3. **Activation and surface preparation panel (Block E):** Pre-immersion activation steps.
4. **Cleanliness verification (Block F):** Water-break test and visual checks.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE STRIP (2.9"--4.2")
  Cleaning stage highlighted (Teal)
ZONE 3 -- CLEANING SEQUENCES HERO (4.2"--14.5" / ~10.3")
  Block B: Three cleaning pathways by mandrel type
  Block C: Key principle callout
ZONE 4 -- CONTAMINATION EFFECTS (14.5"--22.0" / ~7.5")
  Block D: Contamination effects table
  Block E: Activation and pre-immersion steps
ZONE 5 -- CLEANLINESS VERIFICATION (22.0"--28.5" / ~6.5")
  Block F: Verification methods
  Block G: Mandrel-specific cautions
ZONE 6 -- CLEANING TROUBLESHOOTING (28.5"--32.5" / ~4.0")
  Block H: Common cleaning failures
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CLEANING` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Electroforming -- Mandrel Cleaning & Activation` -- 36 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `The mandrel surface becomes the precision interior of the electroform. Contamination here is trapped -- permanently. Clean like the part depends on it.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Sequence Orientation Strip

Cleaning stage highlighted (Teal). Others dimmed.

Below: `Before: Polished mandrel with release agent or conductive coating --> After: Clean, activated, ready for tank immersion` -- Inter Regular, 13 pt, `#F0EDE8` at 60%.

---

### ZONE 3 -- Cleaning Sequences Hero

**Section label:** `CLEANING BY MANDREL TYPE` -- Y: 4.4".

---

**BLOCK B -- Three Cleaning Pathways (Y: 5.0" to 12.5")**

Three tall panels:

**Panel 1 -- Permanent Metal Mandrel (X: 0.5", W: 7.33"):**
- Rounded rect, H: 7.0", fill `#1E2435`, top accent 4 pt `#27AE60`
- Title: `PERMANENT METAL` Barlow SemiBold 20 pt `#27AE60`
- Subtitle: `SS, Ni, Chrome-Plated` Inter Medium 12 pt `#F0EDE8` at 60%

Cleaning sequence (Inter Regular 13 pt `#F0EDE8`, line height 160%):
```
1. Solvent wipe (IPA or acetone)
   Remove fingerprints, handling marks

2. Alkaline soak clean
   50--65 C, 5--10 min, mild alkaline
   Ultrasonic if available

3. DI water rinse
   Flowing cascade, 30--60 sec

4. Apply fresh release agent
   Chromate dip or proprietary compound
   Per Poster 471 specifications

5. DI water rinse (if dip-type release)

6. Transfer to EF tank immediately
   Minimize air exposure time
```

**Panel 2 -- Expendable Mandrel (X: 8.33", W: 7.33"):**
- Rounded rect, H: 7.0", fill `#1E2435`, top accent 4 pt `#E8A020`
- Title: `EXPENDABLE` Barlow SemiBold 20 pt `#E8A020`
- Subtitle: `Al, Zn, Wax, Plastic` Inter Medium 12 pt `#F0EDE8` at 60%

Cleaning sequence (Inter Regular 13 pt `#F0EDE8`, line height 160%):
```
1. Solvent wipe if organic residue present
   (Skip for freshly machined Al/Zn)

2. Light alkaline clean (Al/Zn)
   30--50 C, 2--5 min, MILD pH only
   CAUTION: Strong alkali dissolves Al

3. DI water rinse

4. Acid activation (Al)
   HNO3 10--25%, ambient, 15--30 sec
   Removes oxide; brightens surface

5. DI water rinse

6. For wax/plastic: ensure conductive
   coating (electroless Ni/Ag paint) is
   clean and intact

7. Transfer to EF tank immediately
```

**Panel 3 -- Non-Conductive Mandrel (X: 16.16", W: 7.33"):**
- Rounded rect, H: 7.0", fill `#1E2435`, top accent 4 pt `#2EC4B6`
- Title: `NON-CONDUCTIVE` Barlow SemiBold 20 pt `#2EC4B6`
- Subtitle: `Wax, Glass, Plastic, 3D-Print` Inter Medium 12 pt `#F0EDE8` at 60%

Cleaning sequence (Inter Regular 13 pt `#F0EDE8`, line height 160%):
```
1. Verify conductive coating is intact
   Check continuity with multimeter
   Bare spots = no deposition there

2. Gentle solvent wipe ONLY
   IPA on lint-free cloth
   Do NOT use ultrasonic -- may damage
   conductive coating on fragile substrates

3. No alkaline soak (may attack coating)
   No acid dip (may attack substrate)

4. If electroless Ni coating:
   Mild acid activation (HCl 2--5%, 10 sec)
   DI rinse immediately

5. Transfer to EF tank immediately
   Handle with clean gloves only
```

---

**BLOCK C -- Key Principle Callout (Y: 12.8" to 14.0")**

Full-width rounded rect, H: 1.0", fill `#2EC4B6` at 15%, border 1 pt `#2EC4B6`.
Text centered: `Every contaminant on the mandrel surface is trapped at the mandrel-deposit interface. Fingerprints become voids. Dust becomes pits. Oil becomes adhesion failures. The interior surface of the electroform is only as clean as the mandrel.` Barlow SemiBold 14 pt `#2EC4B6`.

---

### ZONE 4 -- Contamination Effects

**Section label:** `WHAT CONTAMINATION DOES TO THE ELECTROFORM` -- Y: 14.7".

---

**BLOCK D -- Contamination Effects Table (Y: 15.3" to 19.0")**

Table -- columns: Contaminant (4.0") | Source (4.5") | Effect on Electroform (7.0") | Prevention (7.5")

| Contaminant | Source | Effect | Prevention |
|---|---|---|---|
| Fingerprints (oils, NaCl) | Bare-hand handling | Voids at interface; poor interior finish; corrosion initiation | Lint-free gloves always |
| Dust/particles | Shop air, dirty rags | Embedded particles; pits on interior surface | Clean environment; package until use |
| Oxide film | Air exposure on Al or steel mandrel | Poor initial nucleation; rough deposit start | Acid activate immediately before tank |
| Old release agent | Buildup from previous cycles | Deposit may not separate; or separates unevenly | Fresh release agent each cycle |
| Organic residue | Machining oil, polishing compound | Pitting; gas pocketing; adhesion loss at interface | Thorough alkaline clean; solvent wipe |
| Water spots | Mineral deposits from city water rinse | Rough spots on interior surface | DI water final rinse |

Header: `#3A4055`. Data: Inter Regular 12 pt `#F0EDE8`.

---

**BLOCK E -- Activation Steps (Y: 19.5" to 21.8")**

Two side-by-side cards:

**Left -- Metal Mandrel Activation (X: 0.5", W: 11.0"):**
- Rounded rect, H: 2.0", fill `#1E2435`, left accent `#27AE60`
- Title: `METAL MANDREL ACTIVATION` Barlow SemiBold 16 pt `#27AE60`
- Body (Inter Regular 13 pt `#F0EDE8`):
```
Stainless steel: No acid dip needed after chromate release
Nickel: Mild anodic etch (if electrolytic oxide release used)
Aluminum: HNO3 10--25% dip, ambient, 15--30 sec
  Removes native Al2O3; creates clean, active surface
DI water rinse after ALL activation steps
```

**Right -- Conductive Coating Activation (X: 12.0", W: 11.5"):**
- Rounded rect, H: 2.0", fill `#1E2435`, left accent `#E8A020`
- Title: `CONDUCTIVE COATING ACTIVATION` Barlow SemiBold 16 pt `#E8A020`
- Body (Inter Regular 13 pt `#F0EDE8`):
```
Electroless Ni coating: Mild HCl 2--5%, 10 sec, DI rinse
Silver paint: Gentle -- silver oxidizes easily
  IPA wipe; avoid acid (tarnishes silver)
Graphite: No activation needed (already conductive)
Vacuum-deposited metal: Mild acid per metal type
```

---

### ZONE 5 -- Cleanliness Verification

**Section label:** `VERIFICATION & MANDREL-SPECIFIC CAUTIONS` -- Y: 22.2".

---

**BLOCK F -- Verification Methods (Y: 22.9" to 26.0")**

Three cards in a row:

**Card 1 -- Water-Break Test (X: 0.5", W: 7.33"):**
- Rounded rect, H: 2.8", fill `#1E2435`, left accent `#27AE60`
- Title: `WATER-BREAK TEST` Barlow SemiBold 14 pt `#27AE60`
- Body: `Spray DI water on mandrel surface after cleaning. Water should sheet uniformly with no beading. Any break in the water film indicates organic contamination. Re-clean and re-test.`

**Card 2 -- Visual Inspection (X: 8.33", W: 7.33"):**
- Rounded rect, H: 2.8", fill `#1E2435`, left accent `#2EC4B6`
- Title: `VISUAL INSPECTION` Barlow SemiBold 14 pt `#2EC4B6`
- Body: `Inspect mandrel under bright light at oblique angle. Look for: fingerprints, dust, fibers, scratches, water spots, residual polishing compound. Any visible contamination = re-clean. On permanent mandrels, verify release agent is fresh and uniform.`

**Card 3 -- Continuity Check (X: 16.16", W: 7.33"):**
- Rounded rect, H: 2.8", fill `#1E2435`, left accent `#E8A020`
- Title: `CONTINUITY CHECK` Barlow SemiBold 14 pt `#E8A020`
- Body: `For non-conductive mandrels with conductive coating: check electrical continuity across entire surface with multimeter. Resistance should be < 10 ohm between any two points. High resistance = patchy coating = non-uniform deposition.`

---

**BLOCK G -- Mandrel-Specific Cautions (Y: 26.5" to 28.0")**

Two warning cards:

**Card 1 -- Aluminum Mandrels (X: 0.5", W: 11.0"):**
- Rounded rect, H: 1.3", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Title: `ALUMINUM MANDREL CAUTION` Barlow SemiBold 14 pt `#E8A020`
- Body: `NaOH (even mild alkaline cleaners at pH > 10) dissolves aluminum. Use ONLY mild, low-pH alkaline cleaners. Limit time. Test first. Monitor for surface pitting.`

**Card 2 -- Wax/Plastic Mandrels (X: 12.0", W: 11.5"):**
- Rounded rect, H: 1.3", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Title: `WAX / PLASTIC MANDREL CAUTION` Barlow SemiBold 14 pt `#E8A020`
- Body: `Solvents can dissolve or deform wax and some plastics. Use IPA only -- avoid acetone on wax and acrylic. No ultrasonic cleaning on fragile mandrels. No heat above mandrel softening point.`

---

### ZONE 6 -- Cleaning Troubleshooting

**Section label:** `CLEANING FAILURES` -- Y: 28.7".

---

**BLOCK H -- Four Problem Cards (Y: 29.4" to 32.0")**

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | PITTING ON INTERIOR | Dust or particles on mandrel | Improve cleanliness; clean environment |
| 2 | 6.33" | ROUGH INTERIOR START | Oxide not removed; poor nucleation | Acid activate; reduce time between clean and tank |
| 3 | 12.16" | ADHESION TO MANDREL | Release agent skipped or degraded | Fresh release agent every cycle |
| 4 | 18.0" | GAS POCKETING | Organic contamination decomposing | Thorough alkaline clean; solvent wipe |

Each card: Rounded rect, W: 5.5", H: 2.3", fill `#1E2435`, left accent 0.06" `#E05C5C`.

---

### ZONE 7 -- Footer

Standard. Title: `Cleaning -- Electroforming`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; ASTM B832; ASM Handbook Vol. 5. Cleaning chemistry must be compatible with mandrel material. Test on scrap mandrel first.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cleaning Electroforming -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The aluminum mandrel caution is a real operational trap -- many shops default to standard alkaline cleaners that happily dissolve an aluminum mandrel. The three-pathway structure (Block B) makes mandrel-type-specific cleaning immediately actionable. The contamination effects table (Zone 4) gives concrete cause-and-effect for every common contamination source.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #472 -- Construction Workup v1.0*
*2026-04-26*
