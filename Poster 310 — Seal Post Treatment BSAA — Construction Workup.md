---
Project: Plating Posters Inc
Poster Number: 310
Title: "Seal / Post Treatment -- Boric-Sulfuric Acid Anodizing (BSAA)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 4, Section 4.6)"
Process Scope: Seal and post-treatment for BSAA anodizing -- Stage 8 of 8
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Anodizing
  - BSAA
  - TypeIC
  - Seal
  - PostTreatment
  - ConstructionWorkup
  - ClusterAnodize04
---

# Poster #310 -- Construction Workup
## Seal / Post Treatment -- Boric-Sulfuric Acid Anodizing (BSAA)

*Alaina -- Plating Posters Inc*
*v1.0 -- 2026-04-26*

Stage 8 of 8. The final step. Sealing closes the pores of the thin BSAA oxide, converting the open porous structure into a corrosion-resistant barrier. The hero concept for this poster is the "No Dichromate" rule: BSAA exists specifically to eliminate Cr(VI) from the process. Using a dichromate seal on a BSAA oxide defeats the entire purpose. Hot DI water and nickel acetate are the only permitted seal methods. The pore structure diagram from Poster 286 (Type II seal) translates directly -- same mechanism, thinner oxide.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Seal method comparison hero (Block B):** Three methods side by side -- hot DI water, nickel acetate, trivalent Cr. Dichromate shown as crossed-out / prohibited.
2. **BSAA thin oxide seal sensitivity (Block D):** Why sealing a 200--700 mg/ft2 oxide is different from sealing a 0.7 mil Type II oxide.
3. **Seal quality testing (Block E):** Dye spot test, admittance, acid dissolution.
4. **Failure modes (Block F):** Seal bloom, over-seal, under-seal.

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
  Stage 8 highlighted (Amber)
ZONE 3 -- SEAL METHOD COMPARISON / HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- BSAA THIN OXIDE SEAL SENSITIVITY (14.5"--20.5" / ~6.0")
ZONE 5 -- SEAL QUALITY TESTING (20.5"--26.5" / ~6.0")
ZONE 6 -- FAILURE MODES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `SEAL / POST TREATMENT` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `BSAA -- Stage 8 of 8 -- Chromate-Free Seal Only` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `You eliminated hexavalent chromium from the anodize tank. Do not bring it back in the seal tank. Hot water. Nickel acetate. Trivalent Cr. That is the entire list.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Eight-stage strip. Stage 8 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.

Below: `Before: Open porous BSAA oxide (200--700 mg/ft2)  -->  After: Sealed, corrosion-resistant coating -- chromate-free from start to finish`

---

### ZONE 3 -- Seal Method Comparison (HERO)

**Section label:** `SEAL OPTIONS FOR BSAA -- THREE PERMITTED, ONE PROHIBITED` -- Y: 4.4".

**BLOCK B -- Four-Column Comparison (Y: 5.0" to 14.0")**

Four callout boxes in a row:

**Box 1 -- Hot DI Water (X: 0.5", W: 5.5"):**
- Rounded rect H: 8.5", fill `#1E2435`, left accent `#27AE60`
- Title: `HOT DI WATER` Barlow SemiBold 18 pt `#27AE60`
- Badge: `STANDARD` fill `#27AE60`, text `#1A1F2E`
- Content:

| Parameter | Value |
|---|---|
| Temperature | 200--212 F (93--100 C) |
| Water quality | DI < 50 uS/cm |
| pH | 5.5--6.5 |
| Time | 15 min minimum |
| Salt spray (B117) | 336+ hours |

- Note: `Simplest method. Pores hydrate to boehmite (AlOOH). Standard for most BSAA work.` Inter Regular 12 pt `#F0EDE8`

**Box 2 -- Nickel Acetate (X: 6.25", W: 5.5"):**
- Rounded rect H: 8.5", fill `#1E2435`, left accent `#2EC4B6`
- Title: `NICKEL ACETATE` Barlow SemiBold 18 pt `#2EC4B6`
- Badge: `AEROSPACE PREFERRED` fill `#2EC4B6`, text `#1A1F2E`
- Content:

| Parameter | Value |
|---|---|
| Chemistry | 5--8 g/L Ni(CH3COO)2 |
| Temperature | 180--200 F (82--93 C) |
| pH | 5.5--6.0 |
| Time | 15--20 min |
| Salt spray (B117) | 750+ hours |

- Note: `Superior corrosion resistance. Nickel co-precipitates with boehmite in pores. Preferred for BAC 5632.` Inter Regular 12 pt `#F0EDE8`

**Box 3 -- Trivalent Cr Seal (X: 12.0", W: 5.5"):**
- Rounded rect H: 8.5", fill `#1E2435`, left accent `#E8A020`
- Title: `TRIVALENT Cr SEAL` Barlow SemiBold 18 pt `#E8A020`
- Badge: `EMERGING` fill `#E8A020`, text `#1A1F2E`
- Content:

| Parameter | Value |
|---|---|
| Chemistry | Cr(III) proprietary solution |
| Temperature | Per vendor TDS |
| pH | Per vendor TDS |
| Time | Per vendor TDS |
| Salt spray (B117) | Up to 3000+ hours reported |

- Note: `Self-healing corrosion inhibition without Cr(VI). Still emerging -- fewer field data than nickel acetate. Maintains the Cr(VI)-free commitment.` Inter Regular 12 pt `#F0EDE8`

**Box 4 -- DICHROMATE (PROHIBITED) (X: 17.75", W: 5.75"):**
- Rounded rect H: 8.5", fill `#E05C5C` at 15%, border 2 pt `#E05C5C`
- Title: `DICHROMATE` Barlow SemiBold 18 pt `#E05C5C`
- Badge: `PROHIBITED` fill `#E05C5C`, text `#F0EDE8`
- Large X overlay or strikethrough across entire box
- Content:

```
Na2Cr2O7 seal contains
HEXAVALENT CHROMIUM.

The entire BSAA process was
developed to ELIMINATE Cr(VI).

Using dichromate seal on BSAA
defeats the purpose, reinstates
the regulatory burden, and
generates D007 hazardous waste.

DO NOT USE.
```

- JetBrains Mono 16 pt `#E05C5C`: `Cr(VI) = PROHIBITED`

---

### ZONE 4 -- BSAA Thin Oxide Seal Sensitivity

**Section label:** `SEALING A THIN OXIDE -- WHAT IS DIFFERENT` Barlow Condensed ExtraBold 22 pt `#F0EDE8`. Y: 14.7".

**Two-column layout (Y: 15.3" to 20.3"):**

**Left -- Thin Oxide Concerns (X: 0.5", W: 11.0"):**

Callout box, fill `#1E2435`, left accent `#E8A020`:

Title: `BSAA OXIDE IS THIN` Barlow SemiBold 18 pt `#E8A020`

Content (Inter Regular 13 pt `#F0EDE8`, line height 155%):
- `BSAA coating weight: 200--700 mg/ft2 (approximately 0.2--2.0 um thick)`
- `Type II coating: 5--25 um thick (10--100x thicker)`
- ``
- `Consequences for sealing:` Inter Medium 13 pt `#E8A020`
- `-- Less pore depth = less seal material needed` JetBrains Mono 12 pt `#F0EDE8`
- `-- Thin oxide is more vulnerable to over-sealing (thermal damage)` JetBrains Mono 12 pt `#E05C5C`
- `-- Hot water at 212 F can dissolve a thin oxide if exposure is excessive` JetBrains Mono 12 pt `#E05C5C`
- `-- Seal time should follow specification -- do not over-extend` JetBrains Mono 12 pt `#F0EDE8`
- ``
- `BSAA sealing is gentler and shorter than Type II sealing. The oxide is thin by design -- protect it during seal.`

**Right -- BSAA vs. Type II Seal Comparison (X: 12.0", W: 11.5"):**

| Factor | Type II | BSAA |
|---|---|---|
| Coating thickness | 5--25 um | 0.2--2.0 um |
| Coating weight | N/A (thickness spec) | 200--700 mg/ft2 |
| Seal time (hot water) | 2--3 min/um; min 15 min | 15 min minimum |
| Over-seal risk | Low (thick oxide tolerates extended seal) | HIGHER (thin oxide vulnerable to dissolution) |
| Permitted seals | Hot water, NiAc, cold seal, dichromate (legacy) | Hot water, NiAc, Cr(III) ONLY -- no dichromate |
| Primary application | Corrosion + dye retention | Paint adhesion base |

Header: Barlow SemiBold 11 pt. Data: JetBrains Mono 11 pt.
"HIGHER" in `#E05C5C`. "no dichromate" in `#E05C5C`.

---

### ZONE 5 -- Seal Quality Testing

**Section label:** `SEAL QUALITY TESTING -- VERIFY THE SEAL` Barlow Condensed ExtraBold 22 pt. Y: 20.7".

**BLOCK E -- Three Test Cards (Y: 21.3" to 26.3")**

| Card | X | W | Test | Standard | Method | Pass |
|---|---|---|---|---|---|---|
| 1 | 0.5" | 7.33" | DYE SPOT TEST | ASTM B680 | Drop acid dye on sealed surface; compare absorption vs. unsealed reference | Sealed surface shows no dye absorption (or minimal vs. reference) |
| 2 | 8.0" | 7.33" | ADMITTANCE (STEP) | ISO 2931 | Impedance measurement of oxide | Lower admittance value = better seal quality |
| 3 | 15.5" | 8.0" | ACID DISSOLUTION | ASTM B680 | Weight loss after phosphoric-chromic acid exposure | Weight loss below specification limit (< 30 mg/dm2) |

Each card: Rounded rect H: 4.5", fill `#1E2435`, radius 6, left accent 0.06" `#2EC4B6`.
Test name: Barlow SemiBold 16 pt `#2EC4B6`.
Standard: JetBrains Mono 12 pt `#F0EDE8` at 60%.
Method/Pass: Inter Regular 12 pt `#F0EDE8`.

Below cards: `The dye spot test is the fastest field check. If a drop of acid dye stains your sealed surface, the pores are still open. Re-seal.` Inter Medium 13 pt `#E8A020`.

---

### ZONE 6 -- Failure Modes

**Section label:** `WHAT GOES WRONG -- 5 SEAL FAILURES` -- Y: 26.7".

**BLOCK F -- Failure Table (Y: 27.3" to 32.3")**

| Failure | Cause | Fix |
|---|---|---|
| Seal bloom (white haze) | Tap water minerals (Ca, Mg); pH outside 5.5--6.5 range | Use DI water; adjust pH with acetic acid |
| Over-seal (oxide dissolution) | Seal time too long; temperature too high; thin BSAA oxide dissolves | Follow spec time exactly; verify temperature; do not extend seal on thin oxide |
| Incomplete seal (dye spot fails) | Seal time too short; temperature too low; rinse contamination | Extend time to specification minimum; verify temperature at operating level |
| Color shift after seal | Normal -- slight change in oxide appearance | Expected; document baseline for customer acceptance |
| Corrosion failure after seal | Oxide too thin (low coating weight); seal incomplete; pre-treatment contamination | Verify coating weight before seal; re-test seal quality; review entire process upstream |

Each row: Rounded rect H: 0.8", alternating fills `#1E2435` / `#252B3D`.
Failure: Barlow SemiBold 14 pt `#E05C5C`. Cause: Inter Regular 12 pt `#F0EDE8`. Fix: Inter Medium 12 pt `#27AE60`.

---

### ZONE 7 -- Footer

Standard. Title: `Seal / Post Treatment -- Boric-Sulfuric Acid Anodizing (BSAA)`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Seal parameters shown are typical for MIL-A-8625F Type IC per Boeing BAC 5632. BSAA electrolyte H2SO4 concentration: 40--100 g/L per Watson-verified data. Seal quality requirements vary by specification and customer. Dichromate seal is not compatible with the chromate-free intent of BSAA. Consult your process supplier and applicable spec.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Seal Post Treatment BSAA -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the bookend to the BSAA cluster and the place where the "zero Cr(VI)" message reaches its crescendo. The entire cluster has been building toward this: no Cr(VI) in the desmut, no Cr(VI) in the anodize, and now no Cr(VI) in the seal. The prohibited dichromate box (Box 4 in Zone 3) is the visual anchor -- a bold Coral-bordered panel with a clear "DO NOT USE" that closes the loop on the regulatory story. The thin oxide sensitivity section (Zone 4) provides the practical nuance: BSAA oxide is thin by design, so sealing it requires more care than the thick Type II oxide most anodizers are accustomed to. Over-sealing is the trap -- operators used to 30+ minute seal times on Type II may cook a BSAA oxide.

---

*Alaina -- Plating Posters Inc*
*Poster #310 -- Construction Workup v1.0*
*2026-04-26*
