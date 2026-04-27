---
Project: Plating Posters Inc
Poster Number: 476
Title: "Removal & Separation -- Electroforming"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 8: Electroforming, Sections 8.7-8.8)"
Technical Source: Electroforming mandrel separation -- the defining step that distinguishes electroforming from electroplating. Covers mechanical separation (flex, pry, thermal differential), chemical dissolution (Al in NaOH, Zn in HCl, wax in solvents), and low-melt alloy melt-out. Each mandrel type requires a different separation strategy, and damage to either the electroform or reusable mandrel is the primary risk.
Process Scope: Electroforming mandrel separation (Stage 8 of 10)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Electroforming
  - Separation
  - MandrelRemoval
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #476 -- Construction Workup
## Removal & Separation -- Electroforming

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 8 of 10. The deposit has reached target thickness. Now the mandrel must be separated from the electroform without damaging either one (if the mandrel is reusable) or just the electroform (if expendable). This is the step that makes electroforming electroforming -- the moment the deposit becomes a free-standing part. Each mandrel type has its own separation method, and choosing the wrong approach can destroy hours or days of work.

Hero visual: three-pathway separation decision tree by mandrel type.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Separation pathway diagram (Block B -- HERO):** Three paths for permanent, expendable, and low-melt mandrels.
2. **Mechanical separation techniques (Block C):** Flex, pry, thermal differential.
3. **Chemical dissolution methods (Block D):** Chemistry and parameters for Al, Zn, wax dissolution.
4. **Handling the separated electroform (Block E):** Protecting the interior surface.
5. **Common separation failures (Block F).**

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE STRIP (2.9"--4.2")
  Separation stage highlighted (Teal)
ZONE 3 -- SEPARATION PATHWAY HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- MECHANICAL + CHEMICAL METHODS (14.5"--22.0" / ~7.5")
ZONE 5 -- HANDLING + RINSING (22.0"--28.5" / ~6.5")
ZONE 6 -- COMMON SEPARATION FAILURES (28.5"--32.5" / ~4.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `REMOVAL & SEPARATION` -- 72 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Electroforming -- Freeing the Electroform from the Mandrel` -- 32 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `In electroplating, the deposit stays. In electroforming, the deposit leaves. This is the moment of truth -- the mandrel comes out, and a free-standing metal part remains.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Sequence Orientation Strip

Separation stage highlighted (Teal). Others dimmed.
Below: `Before: Target thickness reached, part removed from bath and rinsed (Stage 7) --> After: Mandrel separated, electroform is a free-standing part`

---

### ZONE 3 -- Separation Pathway Hero

**Section label:** `SEPARATION BY MANDREL TYPE` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Three Pathway Panels (Y: 5.0" to 14.0")**

Three tall panels:

**Panel 1 -- Permanent Mandrel (X: 0.5", W: 7.33", H: 8.5"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#27AE60`
- Title: `PERMANENT MANDREL` Barlow SemiBold 20 pt `#27AE60`
- Subtitle: `SS, Ni, Chrome-plated` Inter Medium 12 pt `#F0EDE8` at 60%

Separation flow (Inter Regular 13 pt `#F0EDE8`, line height 160%):
```
METHOD 1: MECHANICAL
  Apply gentle prying force at edge.
  Mandrel must have draft angle (1-3 deg)
  to allow release.
  Use plastic or wood tools -- never
  steel on precision mandrel.

METHOD 2: THERMAL DIFFERENTIAL
  Heat assembly to 150-200 C.
  Ni deposit (CTE 13 um/m/C) expands
  less than SS mandrel (CTE 16 um/m/C).
  Gap forms at interface.
  Cool rapidly -- differential increases.
  Pry gently after thermal cycling.

METHOD 3: FLEX
  For thin-walled electroforms on
  cylindrical mandrels: flex the
  electroform slightly to break the
  release agent bond. Slide off.

MANDREL REUSE:
  Inspect, re-polish if needed,
  apply fresh release agent.
  Hundreds of cycles possible.
```

**Panel 2 -- Expendable Mandrel (X: 8.33", W: 7.33", H: 8.5"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#E8A020`
- Title: `EXPENDABLE MANDREL` Barlow SemiBold 20 pt `#E8A020`
- Subtitle: `Al, Zn, Wax, Plastic` Inter Medium 12 pt `#F0EDE8` at 60%

Separation flow:
```
ALUMINUM MANDREL:
  Dissolve in 10-20% NaOH at 60-80 C.
  Reaction: 2Al + 2NaOH + 2H2O ->
  2NaAlO2 + 3H2 (gas)
  CAUTION: H2 gas evolution -- ventilate!
  Time: hours to days for thick mandrels.

ZINC MANDREL:
  Dissolve in 10-20% HCl at ambient.
  Faster than Al dissolution.
  H2 evolution -- ventilate!

WAX MANDREL:
  Melt out at > mp of wax.
  Or dissolve in appropriate solvent
  (trichloroethylene, naphtha).
  Collect wax for re-use.

3D-PRINTED POLYMER:
  Dissolve in appropriate solvent
  (acetone for ABS; NaOH for PLA).
  Or burn out at > 300 C in oven
  (if electroform tolerates temperature).
```

**Panel 3 -- Low-Melt Alloy (X: 16.16", W: 7.33", H: 8.5"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#2EC4B6`
- Title: `LOW-MELT ALLOY` Barlow SemiBold 20 pt `#2EC4B6`
- Subtitle: `Cerrolow, Cerrobend, Wood's Metal` Inter Medium 12 pt `#F0EDE8` at 60%

Separation flow:
```
PRINCIPLE:
  Mandrel alloy melts at 47-70 C
  (well below Ni or Cu deposit
  working temperature).

PROCEDURE:
  Heat assembly in water bath or oven
  to 10-20 C above mandrel mp.
  Alloy melts and drains out.

ADVANTAGES:
  - No mechanical force on electroform
  - Complex internal geometries OK
  - Alloy is re-cast for next mandrel
  - Non-destructive to electroform

CAUTION:
  Wood's metal contains LEAD and CADMIUM.
  Handle with gloves. Dispose per
  hazardous waste regulations.
  Cerrolow 117 (47 C mp) is Bi-Pb-Sn-In
  -- also contains lead.
  Lead-free alternatives: Cerrolow 136
  (58 C mp, Bi-Sn-In, lead-free).
```

**Bottom insight (Y: 13.2" to 14.0"):**
- Full-width rounded rect, fill `#252B3D`, left accent `#2EC4B6`
- `The separation method must be chosen BEFORE mandrel fabrication. A permanent mandrel needs draft angles and release agent designed in. An expendable mandrel needs compatible dissolution chemistry. Plan the separation from the start.` Inter Medium 13 pt `#2EC4B6`

---

### ZONE 4 -- Mechanical + Chemical Details

**Two-column layout (Y: 14.5" to 21.8"):**

**Left -- Mechanical Techniques (X: 0.5", W: 11.0")**

**Section label:** `MECHANICAL SEPARATION DETAILS` -- Y: 14.7".

**BLOCK C -- Mechanical Panel (Y: 15.3" to 21.5"):**

Rounded rect, fill `#1E2435`, left accent `#27AE60`.

Body (Inter Regular 13 pt `#F0EDE8`, line height 160%):
```
DRAFT ANGLE:
  1-3 deg taper on mandrel allows
  the electroform to slide off.
  No taper = mechanical lock = no
  separation without damage.

THERMAL DIFFERENTIAL:
  CTE VALUES:
    Nickel deposit:   13.0 um/m/C
    Stainless steel:  16.0 um/m/C
    Aluminum:         23.0 um/m/C
    Copper:           16.5 um/m/C

  Heat to 150-200 C then quench in
  cold water. SS mandrel contracts
  more than Ni deposit.
  Repeat 2-3 cycles if needed.

TOOLS:
  Plastic wedges, wooden dowels,
  rubber mallets -- NEVER metal tools
  on the precision interior surface.

LUBRICATION:
  DI water or light oil at the interface
  can assist separation on tight fits.
```

**Right -- Chemical Dissolution (X: 12.0", W: 11.5")**

**Section label:** `CHEMICAL DISSOLUTION PARAMETERS` -- Y: 14.7".

**BLOCK D -- Dissolution Table (Y: 15.3" to 21.5"):**

| Mandrel | Chemistry | Temp | Rate | Safety |
|---|---|---|---|---|
| Aluminum | 10-20% NaOH | 60-80 C | 0.5-2 mm/hr (depends on alloy, concentration) | H2 gas -- ventilate! NaOH is strong alkali -- gloves, goggles, face shield |
| Zinc | 10-20% HCl | Ambient | Faster than Al | H2 gas. HCl fumes. Ventilate. |
| Wax | Heat > mp, or solvent (trichloroethylene, naphtha) | Varies | Minutes to hours | Solvent fumes -- fume hood. Fire risk with naphtha. |
| ABS plastic | Acetone | Ambient | Hours | Flammable. Fume hood. |
| PLA plastic | 5-10% NaOH | 60 C | Hours | Same as Al dissolution |
| Low-melt alloy | Heat above mp (47-70 C) | Water bath | Minutes | Lead/cadmium exposure -- gloves, containment |

Header: Barlow SemiBold 10 pt, fill `#3A4055`. Data: Inter Regular 11 pt `#F0EDE8`.

---

### ZONE 5 -- Handling + Rinsing

**Section label:** `POST-SEPARATION HANDLING` -- Y: 22.2". Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`.

**Two-column layout (Y: 22.8" to 28.3"):**

**Left -- Rinsing Protocol (X: 0.5", W: 11.0"):**

Rounded rect, fill `#1E2435`, left accent `#2EC4B6`.

```
AFTER CHEMICAL DISSOLUTION:
  Rinse electroform thoroughly in
  running DI water to remove all
  traces of NaOH, HCl, or solvent.
  Multiple rinses. Check pH of rinse
  water -- should be neutral.

AFTER MECHANICAL SEPARATION:
  Rinse interior surface gently.
  Remove any release agent residue
  with mild solvent wipe (IPA).

DRY:
  Blow dry with filtered compressed air
  or N2. Handle interior surface with
  CLEAN GLOVES ONLY.

CAUTION:
  The interior surface is now EXPOSED.
  It is the precision surface.
  Any scratch, fingerprint, or
  contamination is permanent.
```

**Right -- Interior Surface Protection (X: 12.0", W: 11.5"):**

Rounded rect, fill `#1E2435`, left accent `#E8A020`.

```
THE INTERIOR SURFACE IS THE PRODUCT.

It was formed against the mandrel and
replicates the mandrel's surface finish
exactly.

PROTECT IT:
- Store with interior surface wrapped
  in lint-free tissue or clean PE film
- Never stack electroforms interior-to-
  interior or interior-to-anything hard
- Mark exterior vs. interior clearly
- If interior will be exposed in final
  application (reflector, waveguide):
  DO NOT TOUCH IT. EVER.

INSPECTION WINDOW:
  This is the best time to inspect
  the interior surface before
  post-processing begins.
  Photograph under oblique light.
  Document any defects.
```

---

### ZONE 6 -- Common Separation Failures

**Section label:** `SEPARATION FAILURES` -- Y: 28.7".

**Four Problem Cards (Y: 29.3" to 32.0")**

Each card: Rounded rect W: 5.5", H: 2.5", fill `#1E2435`, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | CANNOT SEPARATE | Release agent failed; deposit bonded to mandrel | Thermal cycling; stronger prying (risk of damage); may need to scrap |
| 2 | 6.33" | INTERIOR SURFACE SCRATCHED | Metal tools used; rough handling during separation | Plastic tools only; train operators; document procedure |
| 3 | 12.16" | ELECTROFORM DISTORTED | Forced mechanical separation; internal stress release | Gentler technique; anneal before attempting separation |
| 4 | 18.0" | INCOMPLETE DISSOLUTION | Expendable mandrel residue trapped in recesses | Extend dissolution time; agitate; increase temperature or concentration |

---

### ZONE 7 -- Footer

Standard. Title: `Removal & Separation -- Electroforming`. Version `v1.0 -- 2026`.

Disclaimer: `Source: Watson Research Brief (Cluster 8); ASTM B832. Chemical dissolution generates H2 gas -- ensure adequate ventilation. Lead-containing alloys require hazardous waste handling.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Removal Separation Electroforming -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The three-pathway hero structure mirrors the mandrel-type-specific approach used in the Cleaning poster (472). This creates visual consistency across the cluster and reinforces the principle that mandrel type drives every decision. The CTE table in the mechanical section provides the physics behind thermal differential separation -- operators can see that SS contracts more than Ni and understand why the method works. The Wood's metal / Cerrolow lead warning is important -- many shops are unaware of the toxicity of these convenient alloys.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #476 -- Construction Workup v1.0*
*2026-04-26*
