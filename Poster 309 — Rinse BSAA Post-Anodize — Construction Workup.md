---
Project: Plating Posters Inc
Poster Number: 309
Title: "Rinse (Post-Anodize) -- Boric-Sulfuric Acid Anodizing (BSAA)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 4)"
Process Scope: Post-anodize rinse for BSAA -- Stage 7 of 8
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Anodizing
  - BSAA
  - TypeIC
  - Rinse
  - PostAnodize
  - ConstructionWorkup
  - ClusterAnodize04
---

# Poster #309 -- Construction Workup
## Rinse (Post-Anodize) -- Boric-Sulfuric Acid Anodizing (BSAA)

*Alaina -- Plating Posters Inc*
*v1.0 -- 2026-04-26*

Stage 7 of 8. The post-anodize rinse removes residual H2SO4 and H3BO3 electrolyte from the freshly anodized oxide before sealing. This is the last rinse before the pores are permanently closed. Any acid residue carried into the seal tank degrades seal quality and can cause seal bloom. BSAA operates at lower acid concentration (40--100 g/L H2SO4) than Type II, so drag-out volume is lower -- but the boric acid component introduces a unique contamination concern for the seal tank. DI water is mandatory at this stage for aerospace work.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Rinse tank hero (Block B):** Cascade rinse cross-section showing DI water path.
2. **Acid drag-out to seal chain (Block D):** What happens when acid reaches the seal tank.
3. **BSAA-specific rinse concerns (Block E):** Boric acid carry-over and its effect on seal chemistry.
4. **Rinse quality monitoring (Block F):** Conductivity and pH targets.

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
  Stage 7 highlighted (Teal)
ZONE 3 -- RINSE TANK HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- ACID DRAG-OUT TO SEAL (14.5"--20.5" / ~6.0")
ZONE 5 -- BSAA RINSE CONCERNS (20.5"--26.5" / ~6.0")
ZONE 6 -- RINSE QUALITY MONITORING (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Boric-Sulfuric Acid Anodizing (BSAA) -- Stage 7 of 8 -- Post-Anodize` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `The last rinse before the seal. Acid residue in the seal tank causes bloom, poor corrosion resistance, and rejected parts. DI water. Thorough rinse. No shortcuts.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Eight-stage strip. Stage 7 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.

Below: `Before: Freshly anodized oxide coated with residual H2SO4 + H3BO3  -->  After: Clean oxide surface ready for seal`

---

### ZONE 3 -- Rinse Tank Hero

**Section label:** `THE POST-ANODIZE RINSE STATION` -- Y: 4.4".

**BLOCK B -- Cascade Rinse Tank Cross-Section**

Same construction as Poster 305 (pre-etch rinse), adapted for post-anodize context:
- Dual cascade tanks (Stage 1 captures acid drag-out, Stage 2 DI final rinse)
- Overflow arrows, fresh DI water inlet, conductivity meter on Stage 2 outlet
- Parts moving from anodize tank through rinse toward seal

**Parameter summary:**

| Parameter | Value |
|---|---|
| **Type** | Flowing DI water rinse (DI preferred; city water acceptable for commercial) |
| **Temperature** | Ambient (60--85 F / 15--30 C) |
| **Time** | 60--120 sec immersion; agitate rack 3--5 times |
| **Conductivity target** | < 50 uS/cm for aerospace; < 100 uS/cm for commercial |
| **Flow** | Counter-flow dual rinse preferred |

---

### ZONE 4 -- Acid Drag-Out to Seal

**Section label:** `WHAT ACID DRAG-OVER DOES TO THE SEAL` Barlow Condensed ExtraBold 22 pt `#F0EDE8`. Y: 14.7".

**BLOCK D -- Downstream Contamination Chain**

Three connected callout boxes:

Box 1 -- Rinse Failure:
- Left accent `#E8A020`
- Title: `INADEQUATE RINSE`
- Content: `H2SO4 and H3BO3 residue carried on part surface and in blind holes/recesses. BSAA uses 40--100 g/L H2SO4 -- lower than Type II (165--225 g/L), so drag-out acid concentration is lower but still significant.`

Box 2 -- Seal Tank Impact:
- Left accent `#E05C5C`
- Title: `SEAL TANK CONTAMINATION`
- Content: `Acid carry-over lowers seal tank pH below the 5.5--6.5 operating range. Low pH causes: seal bloom (white haze), incomplete pore closure, and accelerated attack on thin BSAA oxide. Hot water seal at near-boiling temperature amplifies acid attack on the thin oxide.`

Box 3 -- Final Result:
- Left accent `#E05C5C`
- Title: `FAILED SEAL`
- Content: `Poor corrosion resistance. Dye spot test fails. Parts absorb contaminants in service. For aerospace work per MIL-A-8625F Type IC, this means rejection.`

Arrows between boxes: 2 pt `#3A4055`, right-pointing.

---

### ZONE 5 -- BSAA Rinse Concerns

**Section label:** `BSAA-SPECIFIC RINSE CONCERNS` Barlow Condensed ExtraBold 22 pt. Y: 20.7".

**Two-column layout:**

**Left -- Boric Acid Carry-Over (X: 0.5", W: 11.0"):**

Callout box, fill `#1E2435`, left accent `#E8A020`:

Title: `BORIC ACID IN THE RINSE` Barlow SemiBold 16 pt `#E8A020`

Content (Inter Regular 13 pt `#F0EDE8`, line height 155%):
- `The BSAA electrolyte contains 5--10 g/L H3BO3 in addition to H2SO4.`
- `Boric acid has low solubility at room temperature (~50 g/L at 20 C).`
- `In a cold rinse, concentrated boric acid drag-out can crystallize on part surfaces if rinse water temperature is low and drag-out is heavy.`
- `Borate crystals trapped in pores before sealing act as contaminants.`
- ``
- `Solution:` Inter Medium 13 pt `#27AE60`
- `Ensure adequate rinse volume and agitation to dilute boric acid below its crystallization point. Room temperature rinse water is sufficient for normal drag-out volumes.`

**Right -- DI vs. City Water (X: 12.0", W: 11.5"):**

Callout box, fill `#1E2435`, left accent `#2EC4B6`:

Title: `DI WATER -- WHY IT MATTERS HERE` Barlow SemiBold 16 pt `#2EC4B6`

| Factor | City Water | DI Water |
|---|---|---|
| Chlorides | 10--250 ppm | < 0.1 ppm |
| Hardness (Ca/Mg) | 50--500 ppm | < 1 ppm |
| Silica | 5--50 ppm | < 0.01 ppm |

Below table:
- `Chlorides from city water cause pitting corrosion on unsealed oxide.` Inter Medium 12 pt `#E05C5C`
- `Hardness minerals cause seal bloom (white deposits) in the seal tank.` Inter Medium 12 pt `#E8A020`
- `For aerospace/MIL-A-8625F Type IC: DI water is effectively mandatory at this stage.` Inter Medium 12 pt `#27AE60`

---

### ZONE 6 -- Rinse Quality Monitoring

**Section label:** `RINSE MONITORING -- TWO SIMPLE TOOLS` Barlow Condensed ExtraBold 22 pt. Y: 26.7".

**Two-column layout:**

**Left -- Conductivity (X: 0.5", W: 11.0"):**

Callout box, fill `#1E2435`, left accent `#2EC4B6`:

Title: `CONDUCTIVITY METER` Barlow SemiBold 16 pt `#2EC4B6`

Content:
- `Inline or handheld conductivity meter on final rinse stage.` Inter Regular 13 pt `#F0EDE8`
- `Target: < 50 uS/cm (aerospace) | < 100 uS/cm (commercial)` JetBrains Mono 14 pt `#F0EDE8`
- `Rising conductivity = insufficient water flow or increasing drag-out.`
- `If conductivity exceeds target: increase flow rate, verify DI system, reduce drag-out.`

**Right -- pH (X: 12.0", W: 11.5"):**

Callout box, fill `#1E2435`, left accent `#E8A020`:

Title: `pH CHECK` Barlow SemiBold 16 pt `#E8A020`

Content:
- `Post-anodize rinse water should recover to near-neutral pH (5.0--7.0).` Inter Regular 13 pt `#F0EDE8`
- `If pH stays below 4.0: acid drag-out is excessive.`
- `Check: drain time over anodize tank (minimum 10--15 sec), rinse water flow rate, cascade function.`
- ``
- `SIMPLE RULE:` Inter Medium 14 pt `#E8A020`
- `If your rinse water looks, smells, or tests like dilute acid, your parts are not ready for the seal tank.`

---

### ZONE 7 -- Footer

Standard. Title: `Rinse (Post-Anodize) -- Boric-Sulfuric Acid Anodizing (BSAA)`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Rinse water quality requirements vary by specification and facility. BSAA H2SO4 concentration: 40--100 g/L per Watson-verified data (some sources cite narrower ranges). Consult your process supplier and applicable spec.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse BSAA Post-Anodize -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The post-anodize rinse is the mirror image of the pre-etch rinse (Poster 305), but the stakes are different. Pre-etch rinse protects the etch and anodize tanks from cleaner contamination. Post-anodize rinse protects the seal tank from acid contamination. The boric acid crystallization concern (Zone 5) is unique to BSAA -- no other anodize process has a buffer component that can crystallize at rinse temperatures. This is the kind of non-obvious, practical detail that makes the poster series valuable. The DI vs. city water comparison reinforces the aerospace-grade quality message that runs through the entire BSAA cluster.

---

*Alaina -- Plating Posters Inc*
*Poster #309 -- Construction Workup v1.0*
*2026-04-26*
