---
Project: Plating Posters Inc
Poster Number: 110
Title: "Post Treatment -- Copper (Alkaline)"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-10 technical reference (alkaline non-cyanide copper)"
  - "Watson Research Brief -- Electroplating Clusters"
Technical Source: Post-treatment for alkaline non-cyanide copper -- almost always an intermediate layer, not a final finish. Three primary paths after copper strike: (1) acid dip + acid copper plate, (2) direct to nickel plating, (3) standalone anti-tarnish. No unique ASTM for alkaline non-CN copper; coatings covered by ASTM B734, AMS 2418, MIL-C-14550. The step that connects the strike to everything downstream.
Process Scope: Post-treatment for alkaline non-cyanide copper plating (Stage 7-8 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - CopperPlating
  - AlkalineCopper
  - NonCyanide
  - PostTreatment
  - ConstructionWorkup
  - Series2
  - ClusterEP10
---

# Poster #110 -- Construction Workup
## Post Treatment -- Copper (Alkaline)

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stages 7--8 of 8. The final poster in the EP-10 Alkaline Non-Cyanide Copper cluster. Unlike hard chrome (where post-treatment is grinding and HE baking) or zinc (where post-treatment is chromate conversion), alkaline non-cyanide copper is almost never the final finish. It is an intermediate layer -- a bridge that enables everything that comes next. Post-treatment here means: transitioning the copper-struck part to its next plating step (acid copper, nickel, chrome) or, in the rare standalone case, applying an anti-tarnish coating.

The design challenge is that this poster is about routing and decision-making, not a single chemical process. The hero visual is a decision tree: "Where does this part go next?" Three paths, each with its own preparation requirements.

The final rinse/dry (Stage 8) is folded into this poster since it shares the same design space and the drying step is trivial for a strike that's heading into another bath.

Hero visual: three-path decision tree with preparation requirements for each downstream destination.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Three-path decision tree hero (Block B):** Acid copper / Nickel / Standalone routes.
2. **Path preparation details (Block C, D, E):** Acid dip specs, activation notes, anti-tarnish.
3. **Inspection / adhesion testing callout (Block F).**
4. **Specification reference (Block G).**
5. **Orientation strip:** Stages 7--8 highlighted (Amber).

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stages 7--8 highlighted (Amber)
ZONE 3 -- THREE-PATH DECISION TREE HERO (4.2"--14.5" / ~10.3")
  Block B: Decision tree
  Block C: Path 1 -- To Acid Copper
  Block D: Path 2 -- To Nickel
  Block E: Path 3 -- Standalone (Anti-Tarnish)
ZONE 4 -- FINAL RINSE + DRY (14.5"--20.5" / ~6.0")
  Block F: Inspection and adhesion testing
  Block F2: Final rinse/dry parameters
ZONE 5 -- SPECIFICATIONS + COMMON FAILURES (20.5"--27.0" / ~6.5")
  Block G: Specification reference
  Block H: Common post-treatment failures
ZONE 6 -- TRANSITION CHECKLIST + SAFETY (27.0"--32.5" / ~5.5")
  Block I: Pre-transition checklist
  Block J: Safety
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `POST TREATMENT` -- Barlow Condensed ExtraBold, 80 pt, `#F0EDE8`, letter spacing -4. X: 0.5", Y: 0.5".

**Subheading:** `Copper (Alkaline) -- Stages 7--8 of 8 -- Where the Strike Goes Next` -- Barlow SemiBold, 30 pt, `#E8A020`. X: 0.5", Y: 1.3".

**Tagline:** `The copper strike is a bridge -- it enables everything downstream. Where the part goes next determines what you do here.` -- Barlow SemiBold, 18 pt, `#F0EDE8` at 65%. X: 0.5", Y: 2.0", W: 23.0".

---

### ZONE 2 -- Orientation Strip

Stages 7--8 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Rinsed copper strike surface  -->  After: Prepared for acid copper, nickel, or final finish`

---

### ZONE 3 -- Three-Path Decision Tree Hero

**Section label:** `WHERE DOES THE PART GO NEXT?` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Decision Tree Root**

Y: 5.0" to 6.0". Center of poster.

Rounded rect (W: 10.0", H: 1.0"), centered horizontally, fill `#252B3D`, border 2 pt `#E8A020`.
Text: `COPPER STRIKE COMPLETE -- CHOOSE PATH` Barlow SemiBold 18 pt `#E8A020`, centered.

Three arrows descend to three path cards below.

**BLOCK C -- Path 1: To Acid Copper (X: 0.5", Y: 6.5", W: 7.0", H: 7.5")**

Rounded rect, fill `#1E2435`, border 2 pt `#27AE60`.
Title: `PATH 1: TO ACID COPPER` Barlow Condensed ExtraBold 20 pt `#27AE60`
Subtitle: `Most common route` Inter Medium 12 pt `#27AE60` at 60%

Body (Inter Regular 12 pt `#F0EDE8`, line height 155%):

**Step sequence:**
1. `Rinse (completed at Stage 6)`
2. `Acid dip: 5--10% H2SO4, ambient, 15--30 sec`
3. `Purpose: neutralize alkaline film, micro-etch copper surface`
4. `Rinse: brief overflow`
5. `Enter acid copper bath`

**Key notes:**
- `Acid dip prevents alkaline carry-over to acid Cu bath`
- `Do NOT use HCl -- attacks copper surface`
- `Transfer to acid copper within 2 min of acid dip`
- `Typical result: 0.5--2.0 mil bright acid copper over 0.1--0.3 mil strike`

JetBrains Mono 11 pt for step values.

**BLOCK D -- Path 2: To Nickel (X: 8.0", Y: 6.5", W: 7.0", H: 7.5")**

Rounded rect, fill `#1E2435`, border 2 pt `#2EC4B6`.
Title: `PATH 2: TO NICKEL` Barlow Condensed ExtraBold 20 pt `#2EC4B6`
Subtitle: `Common for decorative Cu-Ni-Cr` Inter Medium 12 pt `#2EC4B6` at 60%

Body:

**Step sequence:**
1. `Rinse (completed at Stage 6)`
2. `Mild acid activation: 3--5% H2SO4, 10--15 sec`
3. `Rinse: brief overflow`
4. `Enter nickel bath (Watts, sulfamate, or semi-bright)`

**Key notes:**
- `Copper surface must be clean and active -- tarnish causes Ni adhesion failure`
- `Some shops skip the acid dip and go direct to nickel if transfer is fast`
- `Acid activation removes any thin oxide formed during rinse`
- `Typical stack: Cu strike (0.1--0.3 mil) -> Ni (0.3--1.0 mil) -> Cr`

**BLOCK E -- Path 3: Standalone (X: 15.5", Y: 6.5", W: 8.0", H: 7.5")**

Rounded rect, fill `#1E2435`, border 2 pt `#E8A020`.
Title: `PATH 3: STANDALONE COPPER` Barlow Condensed ExtraBold 20 pt `#E8A020`
Subtitle: `Rare -- copper is usually an undercoat` Inter Medium 12 pt `#E8A020` at 60%

Body:

**Step sequence:**
1. `Rinse (completed at Stage 6)`
2. `Anti-tarnish dip: benzotriazole (BTA) solution, 0.1--0.5%, ambient, 30--60 sec`
3. `Rinse: brief DI water`
4. `Dry: forced air or warm air (120--140 F)`

**Key notes:**
- `Copper tarnishes rapidly without protection`
- `BTA forms a thin protective film that inhibits oxidation`
- `For longer-term protection: lacquer or clear coat`
- `Applications: EMI shielding, thermal conductivity, solderability`
- `Inspect per ASTM B734`

---

### ZONE 4 -- Final Rinse + Dry / Inspection

**Section label:** `INSPECTION AND FINAL RINSE` -- Y: 14.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK F -- Inspection and Adhesion Testing**

Y: 15.3" to 18.5".

Two-column layout:

**Left -- Adhesion Testing (X: 0.5", W: 14.0"):**

Rounded rect, fill `#1E2435`, left accent `#E05C5C`.
Title: `ADHESION TESTING -- CATCH FAILURES HERE` Barlow SemiBold 18 pt `#E05C5C`

Body (Inter Regular 13 pt `#F0EDE8`, line height 155%):
- `Bend test (ASTM B571): Bend test coupon 180 degrees. No peeling, flaking, or lifting at the bend.`
- `Tape test: Apply adhesive tape firmly to scored copper surface. Pull sharply. No copper removal.`
- `Thermal cycle test: Heat to 300 F (150 C) for 30 min, quench in room-temp water. No blistering.`
- `When to test: Every new setup, every substrate change, after any process adjustment.`
- `Zinc die castings: test EVERY batch until process is proven stable.`

Bottom highlight: `If adhesion fails, look backward: activation time (Poster #106), rinse quality (Poster #107), live entry (Poster #108).` Inter Medium 12 pt `#E8A020`.

**Right -- Final Rinse/Dry (X: 15.5", W: 8.0"):**

**BLOCK F2**

Rounded rect, fill `#1E2435`, border 1 pt `#2EC4B6`.
Title: `FINAL RINSE / DRY` Barlow SemiBold 16 pt `#2EC4B6`

| Parameter | Value |
|---|---|
| Final rinse | Ambient, DI preferred |
| Dry method | Forced air or warm air (120--140 F) |
| Hot water rinse | Optional -- aids drying |
| Time to next step | Minimize -- copper tarnishes fast |

JetBrains Mono 11 pt `#F0EDE8`.

Note: `If copper must wait before next plating step, apply anti-tarnish (BTA dip) or store in sealed bag with desiccant. Do not leave bare copper exposed to shop air.` Inter Regular 11 pt `#E8A020`.

---

### ZONE 5 -- Specifications + Common Failures

**Two-column layout (Y: 20.7" to 26.8"):**

**Left -- Common Post-Treatment Failures (X: 0.5", W: 14.0"):**

Section label: `WHAT GOES WRONG AFTER THE COPPER STRIKE` Barlow Condensed ExtraBold 20 pt `#F0EDE8`.

| Failure | Root Cause | Consequence |
|---|---|---|
| Copper peeling in acid Cu bath | Poor adhesion from over-etching (Stage 3) | Entire multi-layer stack fails |
| Tarnish before next step | Slow transfer; no anti-tarnish | Adhesion failure at Cu/Ni interface |
| Nickel peeling over copper | Tarnished copper surface; skipped acid activation | Decorative stack rejects |
| Blistering in thermal cycle | Immersion copper under strike (no live entry) | Latent defect -- may not appear until end use |
| Incomplete rinse before acid dip | Alkaline residue neutralizes acid dip | Acid dip ineffective; alkaline carry-over to acid Cu |

Cards: fill `#1E2435`, alternating `#252B3D`. Failure: `#E05C5C`. Cause: `#F0EDE8`. Consequence: `#E8A020`.

**Right -- Specification Reference (X: 15.5", W: 8.0"):**

Section label: `APPLICABLE SPECIFICATIONS` Barlow Condensed ExtraBold 18 pt `#E8A020`.

Rounded rect, fill `#1E2435`, border 1 pt `#E8A020`:

| Specification | Coverage |
|---|---|
| ASTM B734 | Electrodeposited copper for engineering use |
| AMS 2418 | Copper plating |
| MIL-C-14550 | Copper plating (federal) |
| ASTM B571 | Adhesion testing of metallic coatings |
| ASTM B487 | Thickness by cross-section |
| ASTM B567 | Thickness by beta backscatter |

JetBrains Mono 10 pt `#F0EDE8`.

Note: `No unique ASTM or AMS exists for alkaline non-cyanide copper specifically. The deposit is evaluated under general copper plating specifications.` Inter Regular 11 pt at 60%.

---

### ZONE 6 -- Transition Checklist + Safety

**Two-column layout (Y: 27.2" to 32.3"):**

**Left -- Pre-Transition Checklist (X: 0.5", W: 14.0"):**

Section label: `BEFORE THE PART MOVES ON` Barlow Condensed ExtraBold 20 pt `#F0EDE8`.

Callout box, fill `#1E2435`, left accent `#27AE60`:

Checklist (Inter Regular 13 pt `#F0EDE8`):
- `[ ] Copper deposit is uniform color (pink to salmon) -- no dark spots, no bare areas`
- `[ ] Adhesion tested per ASTM B571 (bend test or tape test) -- PASS`
- `[ ] Thickness verified (X-ray or magnetic) -- per specification`
- `[ ] Surface is clean, rinsed, and free of bath residue`
- `[ ] Next step identified: acid copper / nickel / standalone`
- `[ ] Acid dip prepared (if proceeding to acid copper or nickel)`
- `[ ] Transfer time minimized -- copper does not wait`

**Right -- Safety (X: 15.5", W: 8.0"):**

Rounded rect, fill `#1E2435`, border 1 pt `#2EC4B6`, radius 8.
Title: `SAFETY` Barlow Condensed ExtraBold 18 pt `#2EC4B6`
Body (Inter Regular 12 pt `#F0EDE8`, line height 150%):

> - Acid dip (H2SO4): corrosive. PPE required.
> - Anti-tarnish (BTA): low toxicity; avoid skin contact.
> - Copper dust (from handling/buffing): respiratory irritant.
> - Wastewater from this stage: contains copper; route to waste treatment.
> - No unique hazards beyond standard plating shop practices.
> - PPE: chemical splash goggles, rubber gloves, apron.

---

### ZONE 7 -- Footer

Standard footer. Title: `Post Treatment -- Copper (Alkaline)`. Version `v1.0 -- 2026`.

Disclaimer: `This poster covers post-treatment for alkaline non-cyanide copper plating. The copper strike is typically an intermediate layer -- consult the relevant downstream process poster (acid copper, nickel, etc.) for full specifications on the next plating step.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table (see Poster #103).
**Export:** Six files -- `Post Treatment Copper Alkaline -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster is structurally different from the other post-treatment posters in the series. Hard chrome post-treatment (Poster #94) is about HE baking and grinding -- big, defined steps. Zinc post-treatment is about chromate conversion. But alkaline non-cyanide copper post-treatment is about ROUTING -- the strike is a bridge, and what happens next depends entirely on the application.

The three-path decision tree (Block B--E) is the hero because it answers the question the operator actually has: "I just pulled this part from the copper strike tank. What do I do now?" Each path card gives a step-by-step sequence with key notes. This is practical, actionable reference material.

The adhesion testing callout (Block F) is intentionally prominent. Alkaline non-cyanide copper on zinc die castings is where adhesion failures live. If the adhesion fails here, it was lost at activation (Poster #106) or live entry (Poster #108). The backward-looking note connects this poster to the rest of the cluster.

Watson's brief: "Alkaline non-cyanide copper is almost always an intermediate layer. No post-treatment specific to this step -- proceed to acid copper, nickel, or other plating."

-> Watson: Confirm BTA (benzotriazole) concentration range for copper anti-tarnish dip (I have 0.1--0.5% from domain knowledge). Also confirm whether ASTM B734 is the correct primary spec for electrodeposited copper.

-> Tyler: If Drew's lab has run adhesion testing on A Brite's alkaline non-CN copper (Nortex work from 2026-04-08), Tyler's empirical data would strengthen the adhesion testing section.

---

*Alaina -- Poster #110 -- Construction Workup v1.0 -- 2026-04-26*
