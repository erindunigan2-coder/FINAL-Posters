---
Project: Plating Posters Inc
Poster Number: 318
Title: "Post Treatment (Bond Prep) -- PAA"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 5: PAA, Section 5.6)"
Technical Source: Post-treatment for phosphoric acid anodizing. PAA is NEVER sealed and NEVER dyed. Post-treatment consists of DI rinse, controlled drying, and primer application within the specification time window (typically 2--72 hours). The open pore structure is the desired end state for adhesive bonding.
Process Scope: Post treatment / bond prep -- Stage 7 of PAA sequence (final stage)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Anodizing
  - PAA
  - PostTreatment
  - BondPrep
  - ConstructionWorkup
  - ClusterAnodPAA
---

# Poster #318 -- Construction Workup
## Post Treatment (Bond Prep) -- PAA

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 7 of 7 -- the final stage of the PAA sequence. This poster covers everything that happens AFTER the anodize tank: rinse, dry, and primer application. The entire PAA process exists to create a bonding surface, and this stage is where that surface meets its purpose. The 72-hour prime window is the defining constraint. Sealing is PROHIBITED. Dyeing is PROHIBITED. The open pore structure with its whisker morphology must remain intact for adhesive interlocking.

Hero visual: a timeline diagram showing the critical window from PAA anodize to primer application, with degradation indicators at key time points.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 7 highlighted (Amber)
ZONE 3 -- BOND PREP TIMELINE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- POST-ANODIZE STEPS (14.5"--20.5" / ~6.0")
ZONE 5 -- WHAT NOT TO DO + FAILURE MODES (20.5"--26.5" / ~6.0")
ZONE 6 -- PRIMER APPLICATION + SPECIFICATIONS (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `POST TREATMENT` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `PAA Bond Prep -- Stage 7 of 7 (Final Stage)` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `The clock starts the moment parts leave the anodize tank. Prime within the window or restart from scratch.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 7 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Fresh PAA oxide with open whisker pores  -->  After: Primed surface ready for structural adhesive bonding`

---

### ZONE 3 -- Bond Prep Timeline Hero

**Section label:** `THE CRITICAL WINDOW -- PAA TO PRIMER` -- Y: 4.4".

**BLOCK B -- Timeline Diagram**

Y: 5.0" to 14.0". A horizontal timeline spanning the full width showing elapsed time from PAA anodize completion to primer application, with degradation markers.

Rounded rect background, X: 0.5", Y: 5.0", W: 23.0", H: 8.5", fill `#1E2435`, radius 8.

**Timeline bar:**
- Horizontal rect, X: 1.5", Y: 8.5", W: 21.0", H: 0.4"
- Gradient fill conceptual: left `#27AE60` fading to right `#E05C5C`
- Built as two adjacent rects: left half `#27AE60`, right half `#E8A020` fading to `#E05C5C`

**Time markers along timeline (vertical tick marks + labels):**

| Time | X | Status | Color | Note |
|---|---|---|---|---|
| 0 min | 1.5" | PAA COMPLETE | `#27AE60` | Parts exit anodize tank |
| 30 min | 5.0" | RINSE + DRY | `#2EC4B6` | DI rinse, warm air dry |
| 1 hour | 7.5" | OPTIMAL PRIME | `#27AE60` | Best bond strength -- prime now |
| 4 hours | 11.0" | GOOD | `#27AE60` | BAC 5555 maximum without controlled storage |
| 24 hours | 15.0" | CAUTION | `#E8A020` | Controlled humidity storage required |
| 72 hours | 19.0" | MAXIMUM | `#E05C5C` | Absolute limit per most specs |
| > 72 hours | 22.0" | RESTART | `#E05C5C` | Strip and re-anodize -- pores hydrated |

Each marker: vertical line 0.3" tall, 2 pt stroke. Label above: Barlow SemiBold 14 pt. Note below: Inter Regular 12 pt `#F0EDE8`.

**Above timeline -- degradation explanation:**
- `As time passes, atmospheric moisture hydrates the open pores (boehmite formation). Hydrated pores cannot interlock with adhesive.` Inter Regular 14 pt `#F0EDE8` at 70%.

**Below timeline -- key stats:**
- Left: `OPTIMAL: Prime within 1 hour of anodize` JetBrains Mono 14 pt `#27AE60`
- Center: `MAXIMUM: 72 hours (most specs)` JetBrains Mono 14 pt `#E8A020`
- Right: `EXPIRED: > 72 hours = strip and restart` JetBrains Mono 14 pt `#E05C5C`

---

### ZONE 4 -- Post-Anodize Steps

**Section label:** `THE THREE POST-ANODIZE STEPS` -- Y: 14.7".

**Three-column layout (Y: 15.3" to 20.3"):**

*Column 1 -- DI Rinse (X: 0.5", W: 7.33"):*
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#2EC4B6` 0.06"
- Title: `STEP 1: DI RINSE` Barlow SemiBold 18 pt `#2EC4B6`

| Parameter | Value |
|---|---|
| Water quality | DI water (< 50 uS/cm) |
| Temperature | Ambient |
| Method | Immersion or spray |
| Time | 60--120 sec |

Note: `Thorough rinsing prevents phosphoric acid residue from interfering with primer adhesion.` Inter Regular 13 pt `#F0EDE8` at 70%.

*Column 2 -- Dry (X: 8.16", W: 7.33"):*
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `STEP 2: DRY` Barlow SemiBold 18 pt `#E8A020`

| Parameter | Value |
|---|---|
| Method | Warm, filtered air |
| Temperature | < 140 F (60 C) |
| Duration | Until visually dry |
| Handling | Clean gloves only -- no bare hands |

Note: `Do NOT oven-dry at elevated temperature -- excessive heat promotes premature pore hydration.` Inter Medium 13 pt `#E05C5C`.

*Column 3 -- Prime (X: 15.83", W: 7.33"):*
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#27AE60` 0.06"
- Title: `STEP 3: PRIME` Barlow SemiBold 18 pt `#27AE60`

| Parameter | Value |
|---|---|
| Primer | BR 127 or equivalent epoxy primer |
| Application | Spray or brush per spec |
| Cure | Per primer TDS (typically 60 min @ 250 F) |
| Window | Within 1--72 hours of anodize |

Note: `Primer flows into the open whisker pores and cures in place -- mechanical interlocking.` Inter Regular 13 pt `#27AE60`.

---

### ZONE 5 -- What NOT To Do + Failure Modes

**Section label:** `WHAT NOT TO DO -- AND WHAT GOES WRONG` -- Y: 20.7".

**Two-column layout (Y: 21.3" to 26.3"):**

**Left -- Prohibited Actions (X: 0.5", W: 11.0"):**
- Title: `PROHIBITED -- PAA POST TREATMENT` Barlow Condensed ExtraBold 22 pt `#E05C5C`

Three stacked Coral-accented cards:

*Card 1:*
- `NEVER SEAL` Barlow SemiBold 18 pt `#E05C5C`
- `Sealing closes the pores that provide mechanical interlocking for adhesive. Sealed PAA = failed bonds.` Inter Regular 13 pt `#F0EDE8`

*Card 2:*
- `NEVER DYE` Barlow SemiBold 18 pt `#E05C5C`
- `PAA has no decorative function. Dye molecules contaminate the bond surface and block adhesive penetration.` Inter Regular 13 pt `#F0EDE8`

*Card 3:*
- `NEVER TOUCH WITH BARE HANDS` Barlow SemiBold 18 pt `#E05C5C`
- `Fingerprint oils are organic contaminants. They reduce adhesive wetting and create weak boundary layers in the bond.` Inter Regular 13 pt `#F0EDE8`

**Right -- Failure Modes (X: 12.0", W: 11.5"):**
- Title: `POST-TREATMENT FAILURES` Barlow Condensed ExtraBold 22 pt `#F0EDE8`

| Failure | Cause | Bond Impact |
|---|---|---|
| Delayed priming | > 72 hours after anodize | Pores hydrate; must strip and restart |
| Excessive dry temperature | > 60 C oven drying | Premature boehmite formation |
| Contaminated surface | Bare-hand contact or dirty storage | Weak boundary layer; disbonding |
| Primer cure failure | Incorrect cure temp/time | Incomplete interlock; reduced peel strength |

4-row table. Data: Inter Regular 12 pt `#F0EDE8`.

---

### ZONE 6 -- Primer Application + Specifications

**Section label:** `PRIMER APPLICATION -- THE FINAL LINK` -- Y: 26.7".

**Two-column layout (Y: 27.3" to 32.3"):**

**Left -- Primer Details (X: 0.5", W: 11.0"):**

Rounded rect, fill `#1E2435`, left accent `#27AE60`.
Title: `ADHESIVE PRIMER` Barlow SemiBold 18 pt `#27AE60`.

Body (Inter Regular 14 pt `#F0EDE8`, line height 160%):

> The primer bridges the PAA oxide and the structural adhesive. Common primers:
>
> -- BR 127 (Cytec/Solvay): Corrosion-inhibiting epoxy primer; aerospace standard
> -- EC-3924B (3M): Structural adhesive primer
> -- Various OEM-specified primers per customer spec
>
> Primer cures at 250 F (121 C) for 60 min typical. After cure, parts may be stored indefinitely before bonding (sealed by primer).

Key stat: `Bond strength with proper PAA + primer: > 40 MPa (6,000 psi) lap shear` JetBrains Mono 13 pt `#27AE60`.

**Right -- Applicable Specifications (X: 12.0", W: 11.5"):**

Rounded rect, fill `#1E2435`, left accent `#E8A020`.
Title: `APPLICABLE SPECIFICATIONS` Barlow SemiBold 18 pt `#E8A020`.

| Specification | Description |
|---|---|
| Boeing BAC 5555 | Phosphoric acid anodizing (defines prime window) |
| ASTM D3933 | PAA for structural adhesive bonding |
| Boeing BAC 5514 | Structural adhesive bonding |

Below: `The prime window varies by OEM specification. Some require priming within ONE SHIFT. Always verify against your applicable spec.` Inter Medium 13 pt `#E8A020`.

**Bottom callout:**
- `CONTROLLED HUMIDITY STORAGE: If priming cannot occur within 4 hours, store parts in humidity-controlled environment (< 40% RH) until primer application.` Inter Medium 14 pt `#E8A020`

---

### ZONE 7 -- Footer

Standard. Title: `Post Treatment (Bond Prep) -- Phosphoric Acid Anodizing (PAA)`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; ASTM D3933; Boeing BAC 5555. Post-treatment requirements are specification-dependent. Prime window varies by OEM. Consult your applicable specification.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Post Treatment Bond Prep PAA -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the capstone poster of the PAA cluster -- every preceding stage was building toward this moment. The timeline hero is the most important visual in the entire poster because it communicates the urgency of the prime window in a way that a table of parameters cannot. The NEVER SEAL / NEVER DYE cards echo the critical rules from Poster #311 (process flow) but in a deeper, more detailed context. The three-step post-anodize sequence (rinse, dry, prime) is deceptively simple -- the complexity is in the constraints around it.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #318 -- Construction Workup v1.0*
*2026-04-26*
