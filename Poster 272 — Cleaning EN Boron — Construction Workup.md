---
Project: Plating Posters Inc
Poster Number: 272
Title: "Cleaning -- EN Boron"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters -- Watson Research Brief v1.1 (Process 8: EN-B, Poster 2)"
Technical Source: Identical cleaning protocols to all EN processes. Alkaline soak clean and electroclean. Watson domain expertise.
Process Scope: Cleaning stage (Stage 1 of 8) for electroless nickel-boron plating
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ElectrolessNickelBoron
  - Cleaning
  - ConstructionWorkup
  - Series2
  - ClusterEL08
---

# Poster #272 -- Construction Workup
## Cleaning -- EN Boron

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 1 of 8. Cleaning for EN-B follows the same universal electroless cleaning protocols as all EN variants. The substrate must be catalytically active for initiation. Watson notes that EN-B cleaning requirements are identical to EN-P -- no unique cleaner requirements. The poster value is placing cleaning in the EN-B context and reinforcing the water-break-free quality gate.

Hero visual: cleaning tank cross-section with immersion soak, agitation, temperature probe, and water-break-free test.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cleaning tank cross-section hero (Block B):** Same layout template as Poster #264 (E-Co Cleaning).
2. **Cleaning methods comparison (Block D):** Soak / Cathodic Electroclean / Anodic Electroclean.
3. **Substrate-specific callouts (Block E):** Steel, aluminum (zincate follows), stainless, plastics.
4. **Critical quality checks (Block F):** Water-break-free + silicate warning.

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
  Stage 1 highlighted (Teal)
ZONE 3 -- CLEANING TANK HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- CLEANING METHODS COMPARISON (14.5"--20.5" / ~6.0")
ZONE 5 -- SUBSTRATE-SPECIFIC NOTES (20.5"--26.5" / ~6.0")
ZONE 6 -- CRITICAL QUALITY CHECKS (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CLEANING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `EN Boron -- Stage 1 of 8` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `EN-B demands the same spotless surface as every electroless process. Skip the prep and you will skip-plate the part. No exceptions.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 1 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Incoming substrate (oils, oxides, soils)  -->  After: Water-break-free surface ready for activation`

---

### ZONE 3 -- Cleaning Tank Hero

**Section label:** `THE ALKALINE SOAK CLEAN` -- Y: 4.4".

**BLOCK B -- Tank Cross-Section**

Y: 5.0" to 14.0". Same construction as Poster #264 (E-Co Cleaning tank hero).

**Bath parameter labels:**
- `NaOH: 30--60 g/L` JetBrains Mono 14 pt `#2EC4B6`
- `Na2CO3: 15--30 g/L` JetBrains Mono 14 pt `#2EC4B6`
- `Surfactant: 1--5 mL/L` JetBrains Mono 14 pt `#2EC4B6`
- `Temp: 140--176 F (60--80 C)` JetBrains Mono 14 pt `#F0EDE8`
- `Time: 3--10 min (soak)` JetBrains Mono 14 pt `#E8A020`

**Bottom callout (Y: 13.5"):**
- `EN-B cleaning is identical to EN-P cleaning. The autocatalytic reaction is the same gatekeeper -- a contaminated surface will not initiate.` Inter Medium 14 pt `#2EC4B6`

---

### ZONE 4 -- Cleaning Methods Comparison

**Section label:** `THREE CLEANING METHODS` -- Y: 14.7".

**BLOCK D -- Three-Column Layout (Y: 15.3" to 20.3")**

Same structure as Poster #264:

*Soak Clean:* `3--10 minutes immersion` / `Air or mechanical agitation` / `No electrical connection` / `Standard for most production`

*Cathodic Electroclean:* `3--6 V, 30--60 seconds` / `H2 scrubbing action` / `CAUTION: H absorption >1000 MPa UTS` (`#E05C5C`)

*Anodic Electroclean:* `3--6 V, 15--30 seconds` / `O2 smut removal` / `Use after cathodic for H removal` / `Preferred for high-strength steel destined for EN-B`

**EN-B specific note below columns:**
- `EN-B wear applications often involve high-strength steel substrates. Hydrogen absorption during cathodic cleaning is a real risk -- prefer anodic cleaning or minimize cathodic time.` Inter Medium 13 pt `#E8A020`

---

### ZONE 5 -- Substrate-Specific Notes

**Section label:** `SUBSTRATE CONSIDERATIONS` -- Y: 20.7".

**BLOCK E -- 2x2 Grid (Y: 21.3" to 26.3")**

| Position | Substrate | Accent | Key Note |
|---|---|---|---|
| R1C1 | Steel / Iron | `#2EC4B6` | Standard alkaline clean. Steel is catalytic for EN-B. HCl or H2SO4 acid activation follows. EN-B is less sensitive to marginal activation than EN-P. |
| R1C2 | Aluminum | `#E8A020` | Non-etch alkaline cleaner (pH <10.5). Double zincate activation follows. Rinse thoroughly before zincate -- residual alkaline causes uncontrolled etching. |
| R2C1 | Stainless Steel | `#27AE60` | Standard alkaline clean. Wood's nickel strike activation follows. SS passive layer must be removed for EN-B adhesion. |
| R2C2 | Plastics (ABS, PC) | `#E05C5C` | Proprietary plastic conditioner. Sn/Pd colloidal activation follows. EN-B on plastics is uncommon but used for wear-resistant housings. |

Each card: Rounded rect W: 11.0", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06".

---

### ZONE 6 -- Critical Quality Checks

**Section label:** `QUALITY GATES -- DO NOT SKIP` -- Y: 26.7".

**Two-column layout (Y: 27.3" to 32.3"):**

**Left -- Water-Break-Free Test (X: 0.5", W: 11.0"):**
Same construction as Poster #264.
- `PASS: Water sheets uniformly` `#27AE60`
- `FAIL: Water beads or breaks` `#E05C5C`
- `The most important 10-second test in electroless plating` Inter Regular 13 pt `#F0EDE8` at 70%

**Right -- Cleaner Compatibility (X: 12.0", W: 11.5"):**

| Warning | Detail |
|---|---|
| Silicate residues | Poison catalytic surface -- rinse thoroughly |
| Foaming agents | Non-foaming type required before electroclean |
| Aluminum cleaners | Non-etch (pH <10.5) to prevent surface attack |
| High-strength steel | Minimize cathodic cleaning -- HE relief will follow EN-B plating anyway, but prevention > cure |

---

### ZONE 7 -- Footer

Standard. Title: `Cleaning -- EN Boron`. Version `v1.0 -- 2026`.

Disclaimer note: `Source: General industry knowledge; electroless plating cleaning protocols are universal across all EN variants including EN-B.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cleaning EN Boron -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

EN-B cleaning is functionally identical to EN-P cleaning. The poster's unique value: (1) placing it in the EN-B context (wear applications on high-strength steel are common), (2) emphasizing the cathodic cleaning hydrogen risk for high-strength steel substrates, and (3) noting that EN-B is less sensitive to marginal activation than EN-P. Layout matches the electroless cleaning template per Watson flag #8.

---

*Alaina -- Plating Posters Inc Creative Lead*
*Poster #272 -- Construction Workup v1.0*
*2026-04-26*
