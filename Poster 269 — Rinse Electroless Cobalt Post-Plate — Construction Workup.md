---
Project: Plating Posters Inc
Poster Number: 269
Title: "Rinse -- Electroless Cobalt -- Post-Plate"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters -- Watson Research Brief v1.1 (Process 7: Electroless Cobalt, Poster 7)"
Technical Source: Post-plate rinse after electroless cobalt deposition. Cobalt surfaces oxidize readily in air -- handle carefully. Standard DI counterflow rinse. Watson domain expertise.
Process Scope: Post-plate rinse (Stage 6 of 8) for electroless cobalt plating
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ElectrolessCobalt
  - Rinse
  - PostPlate
  - ConstructionWorkup
  - Series2
  - ClusterEL07
---

# Poster #269 -- Construction Workup
## Rinse -- Electroless Cobalt -- Post-Plate

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 6 of 8. The post-plate rinse removes residual cobalt bath chemistry from the freshly plated surface before post-treatment. The key concern unique to cobalt: the freshly deposited Co-P or Co-W-P surface oxidizes readily in air. Handle carefully -- do not air-dry before rinsing.

Hero visual: rinse tank with emphasis on the oxidation-sensitive cobalt surface -- color gradient showing tarnish progression if exposed to air.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Rinse tank hero with oxidation warning (Block B):** Tank with caution overlay showing cobalt surface tarnish risk.
2. **Bath chemistry removal (Block D):** What residual chemistry must be removed and why.
3. **Handling precautions (Block E):** Cobalt-specific handling rules vs. generic EN post-plate rinse.
4. **Waste treatment preview (Block F):** Cobalt rinse water treatment requirements.

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
  Stage 6 highlighted (Teal)
ZONE 3 -- RINSE TANK HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- RESIDUAL CHEMISTRY REMOVAL (14.5"--20.5" / ~6.0")
ZONE 5 -- COBALT-SPECIFIC HANDLING (20.5"--26.5" / ~6.0")
ZONE 6 -- WASTE TREATMENT + RINSE SPECS (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Electroless Cobalt -- Post-Plate -- Stage 6 of 8` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Fresh cobalt deposits oxidize rapidly. Rinse immediately -- do not air-dry. Handle with clean gloves only.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 6 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Freshly plated Co-P or Co-W-P surface (bath-wet)  -->  After: Rinsed surface ready for anneal or passivation`

---

### ZONE 3 -- Rinse Tank Hero

**Section label:** `POST-PLATE RINSE -- HANDLE WITH CARE` -- Y: 4.4".

**BLOCK B -- Rinse Tank with Oxidation Warning**

Y: 5.0" to 14.0".

**Tank body:**
- Rounded rect, X: 3.0", Y: 6.0", W: 18.0", H: 6.5", fill `#252B3D`, border 3 pt `#C8D0D8`

**Parts on rack (center):**
- Rack with freshly plated parts, fill `#27AE60` at 30%, border 2 pt `#27AE60`
- Label: `Freshly plated cobalt deposit` Inter Regular 12 pt `#27AE60`

**Oxidation warning (top, spanning full width):**
- Rounded rect, X: 1.0", Y: 5.0", W: 22.0", H: 1.0", fill `#E05C5C` at 15%, border 1 pt `#E05C5C`
- Text: `WARNING: Cobalt surfaces oxidize readily in air -- transfer directly from bath to rinse. Do not air-dry.` Inter Medium 14 pt `#E05C5C`

**Bath parameters (inside tank):**
- `DI counterflow` JetBrains Mono 14 pt `#2EC4B6`
- `Ambient temperature` JetBrains Mono 14 pt `#F0EDE8`
- `30--60 sec per stage` JetBrains Mono 14 pt `#E8A020`

**Transfer arrows:**
- Left: `FROM COBALT BATH` `#27AE60`
- Right: `TO POST-TREATMENT` `#E8A020`

**Bottom callout (Y: 13.2"):**
- `Cold rinse preferred to arrest any residual autocatalytic reaction on the surface.` Inter Medium 14 pt `#2EC4B6`

---

### ZONE 4 -- Residual Chemistry Removal

**Section label:** `WHAT YOU ARE RINSING OFF` -- Y: 14.7".

**BLOCK D -- Chemistry Table (Y: 15.3" to 20.3")**

| Residual Chemistry | Why It Must Be Removed | Risk If Not Removed |
|---|---|---|
| Cobalt ions (Co2+) | Prevent staining or uncontrolled deposition during drying | Surface discoloration; uneven passivate |
| Hypophosphite / DMAB | Stop autocatalytic reaction; prevent surface nodules | Rough surface; continued deposition |
| Orthophosphite / borate | Byproduct film; interferes with passivation adhesion | Poor passivate quality |
| Citrate / complexant | Organic residue; attracts contaminants during storage | Staining; adhesion issues with next layer |
| Stabilizer residue (thallium, lead) | Toxic metals; must not remain on finished part | Contamination; regulatory non-compliance |

Header: `#3A4055`. Alternating rows `#1E2435` / `#252B3D`.
Risk column: `#E05C5C`.

---

### ZONE 5 -- Cobalt-Specific Handling

**Section label:** `HANDLING RULES -- COBALT IS NOT NICKEL` -- Y: 20.7".

**BLOCK E -- Three Rule Cards (Y: 21.3" to 26.3")**

| Card | Accent | Rule | Detail |
|---|---|---|---|
| 1 | `#E05C5C` | DO NOT AIR-DRY BEFORE RINSE | Cobalt oxidizes faster than nickel; oxide film forms within seconds of air exposure; tarnish may be irreversible |
| 2 | `#E8A020` | CLEAN GLOVES ONLY | Fingerprint contamination on fresh cobalt deposit is visible and permanent; use fresh nitrile gloves for all handling |
| 3 | `#2EC4B6` | COLD RINSE PREFERRED | Cold water arrests residual autocatalytic activity faster than warm; prevents surface roughening from continued deposition |

Each card: Rounded rect W: 7.33", H: 4.5", fill `#1E2435`, top accent 4 pt.
Rule: Barlow SemiBold 18 pt, accent color. Detail: Inter Regular 14 pt `#F0EDE8`.

---

### ZONE 6 -- Waste Treatment + Rinse Specs

**Two-column layout (Y: 26.7" to 32.3"):**

**Left -- Rinse Specifications (X: 0.5", W: 11.0"):**

| Parameter | Specification |
|---|---|
| Type | Counterflow (2-stage minimum) |
| Water quality | DI preferred |
| Temperature | Ambient (cold preferred) |
| Time | 30--60 seconds per stage |
| Agitation | Gentle overflow |
| Special | Position rinse tank directly adjacent to Co bath |

**Right -- Waste Treatment Notes (X: 12.0", W: 11.5"):**

Section label: `COBALT RINSE WATER TREATMENT` Barlow Condensed ExtraBold 18 pt `#E8A020`.

| Waste Stream | Treatment | Limit |
|---|---|---|
| Cobalt (Co2+) | Hydroxide precipitation at pH 8.5--9.5 | 0.5--2.0 mg/L (per NPDES permit) |
| Thallium / lead (from stabilizer) | Sulfide precipitation or ion exchange | Tl: 0.002--0.01 mg/L (very strict) |
| Phosphite / borate | Oxidize phosphite to phosphate; precipitate as Ca3(PO4)2 | 1--5 mg/L total P |

Note: `Thallium is a priority pollutant under the Clean Water Act. If your cobalt bath uses thallium stabilizer, segregate rinse water and treat separately.` Inter Medium 12 pt `#E05C5C`

---

### ZONE 7 -- Footer

Standard. Title: `Rinse -- Electroless Cobalt -- Post-Plate`. Version `v1.0 -- 2026`.

Disclaimer note: `Source: General industry knowledge; cobalt rinse water treatment parameters per EPA 40 CFR guidelines. Check local NPDES permit for specific discharge limits.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Electroless Cobalt Post-Plate -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The post-plate rinse for cobalt has a unique angle vs. other electroless rinse posters: the oxidation sensitivity of fresh cobalt deposits. Watson specifically notes "handle carefully -- cobalt surfaces oxidize readily in air." The thallium waste treatment note is a valuable regulatory callout -- thallium has extremely strict discharge limits and many operators may not realize their cobalt bath stabilizer contains it.

---

*Alaina -- Plating Posters Inc Creative Lead*
*Poster #269 -- Construction Workup v1.0*
*2026-04-26*
