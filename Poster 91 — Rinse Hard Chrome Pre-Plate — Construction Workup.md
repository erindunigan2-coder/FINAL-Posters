---
Project: Plating Posters Inc
Poster Number: 91
Title: "Rinse -- Hard Chrome -- Pre-Plate"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-08 technical reference (hard chrome plating)"
Technical Source: Pre-plate rinse for hard chrome -- NOT APPLICABLE in most hard chrome operations. Standard practice is reverse etch (anodic) followed by polarity reversal to plating, all in the same chrome bath. No transfer, no rinse between activation and plating. This poster documents WHY this stage is skipped and when the exception (external acid etch) requires a rinse.
Process Scope: Pre-plate rinse -- Stage 4 of 8 (typically skipped)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - HardChrome
  - Rinse
  - PrePlate
  - ConstructionWorkup
  - ClusterEP08
---

# Poster #91 -- Construction Workup
## Rinse -- Hard Chrome -- Pre-Plate

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 4 of 8. This stage is typically NOT a separate operation in hard chrome plating. When reverse etch activation is used (95%+ of hard chrome work), the etch and plate happen in the same tank -- there is no rinse between them. Polarity is simply reversed from anodic (etch) to cathodic (plate) without removing the part. This poster documents that reality and explains the exception: when external acid etch IS used, a single rinse before the chrome bath is needed.

Hero visual: a decision tree similar to Poster #83 (decorative chrome pre-plate rinse), showing the standard path (no rinse) vs. the exception path (rinse needed after external acid etch).

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Decision tree hero (Block B):** "Did you use reverse etch (in-tank)?" Yes -> no rinse needed. No (external acid etch) -> rinse before chrome bath.
2. **Why no rinse is needed (Block D):** The elegance of in-tank activation -- etch and plate in the same solution.
3. **Exception path details (Block E):** When external acid etch requires a rinse.
4. **Acid drag-in risks (Block F):** What happens if acid reaches the chrome bath.

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
  Stage 4 highlighted (Teal)
ZONE 3 -- DECISION TREE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- WHY NO RINSE IS NEEDED (14.5"--20.5" / ~6.0")
ZONE 5 -- EXCEPTION: EXTERNAL ACID ETCH PATH (20.5"--26.5" / ~6.0")
ZONE 6 -- ACID DRAG-IN RISKS (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Hard Chrome -- Pre-Plate -- Stage 4 of 8` -- 32 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `In standard hard chrome, this stage does not exist. Reverse etch and plating happen in the same tank. No transfer. No rinse.` -- 20 pt `#F0EDE8` at 65%. Y: 2.2".

**Safety note (right side):**
- Rounded rect, X: 18.0", Y: 0.6", W: 5.5", H: 0.5", fill `#E05C5C` at 10%, border 1 pt `#E05C5C`
- Text: `Cr(VI) CARCINOGEN -- see Main Tank poster` JetBrains Mono 10 pt `#E05C5C`

---

### ZONE 2 -- Orientation Strip

Stage 4 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Activated surface (from reverse etch or external acid etch)  -->  After: Surface ready for chrome deposition`

---

### ZONE 3 -- Decision Tree Hero

**Section label:** `DO YOU NEED THIS RINSE?` -- Y: 4.4".

**BLOCK B -- Decision Tree (Y: 5.0" to 14.0")**

**Central question box:**
- Rounded rect, X: 5.0", Y: 5.0", W: 14.0", H: 1.8", fill `#E8A020` at 15%, border 2 pt `#E8A020`, radius 8
- Text: `WHAT ACTIVATION METHOD DID YOU USE?` -- Barlow SemiBold, 22 pt, `#E8A020`

**Left -- Reverse Etch (Standard Path -- 95% of jobs):**
- Arrow down-left
- Rounded rect, X: 0.5", Y: 7.5", W: 10.5", H: 5.5", fill `#27AE60` at 8%, border 2 pt `#27AE60`
- Title: `REVERSE ETCH (IN-TANK)` -- Barlow SemiBold, 20 pt, `#27AE60`
- Badge: `STANDARD -- 95% OF HARD CHROME` -- rounded rect, fill `#27AE60`, 11 pt

Content:
```
Etch and plate in same tank
No part removal between steps
No rinse needed
Polarity reversal = immediate plating

THIS STAGE IS SKIPPED
```

Large centered text: `SKIP THIS STAGE` -- Barlow Condensed ExtraBold, 36 pt, `#27AE60`

**Right -- External Acid Etch (Exception -- 5% of jobs):**
- Arrow down-right
- Rounded rect, X: 12.5", Y: 7.5", W: 11.0", H: 5.5", fill `#E8A020` at 8%, border 2 pt `#E8A020`
- Title: `EXTERNAL ACID ETCH` -- Barlow SemiBold, 20 pt, `#E8A020`
- Badge: `EXCEPTION -- 5% OF HARD CHROME` -- rounded rect, fill `#E8A020`, 11 pt

Content:
```
Separate acid tank before chrome bath
Part must be rinsed to remove acid
Single rinse, ambient, 15--30 sec
Then into chrome bath for plating

RINSE IS NEEDED
```

Large centered text: `RINSE REQUIRED` -- Barlow Condensed ExtraBold, 28 pt, `#E8A020`

---

### ZONE 4 -- Why No Rinse Is Needed

**Section label:** `WHY REVERSE ETCH ELIMINATES THIS STAGE` -- Y: 14.7".

**BLOCK D -- Explanation Panel (Y: 15.3" to 20.3")**

Rounded rect, X: 0.5", W: 23.0", H: 4.8", fill `#1E2435`, left accent `#27AE60`.

**Three advantages of in-tank activation:**

| Advantage | Explanation |
|---|---|
| NO TRANSFER | Part never leaves the chrome bath between etch and plate -- zero re-contamination risk |
| NO RINSE CONTAMINATION | No acid drag-in to worry about |
| NO RE-OXIDATION | Surface stays immersed in chrome solution -- no air exposure, no oxide reformation |
| THERMAL CONTINUITY | Part stays at bath temperature -- no thermal shock from cold rinse water |

Bottom insight:
- `Reverse etch is the reason hard chrome lines are physically shorter than most plating lines. Fewer tanks. Fewer transfers. Fewer failure points.` -- Inter Medium, 14 pt, `#E8A020`

---

### ZONE 5 -- Exception: External Acid Etch Path

**Section label:** `EXCEPTION PATH -- RINSE AFTER EXTERNAL ACID ETCH` -- Y: 20.7".

**BLOCK E -- Exception Details (Y: 21.3" to 26.3")**

Rounded rect, X: 0.5", W: 23.0", H: 4.8", fill `#1E2435`, left accent `#E8A020`.

**When external acid etch is used (and rinse is needed):**

| Scenario | Acid | Time | Rinse |
|---|---|---|---|
| Heavy oxide from heat treatment | 20--50% HCl | 1--5 min | Single rinse, ambient, 15--30 sec |
| Hardened tool steel (> 60 HRC) | 10--30% H2SO4 | 1--3 min | Single rinse, ambient, 15--30 sec |
| Case-hardened surfaces | 20--30% HCl | 2--5 min | Single rinse, ambient, 15--30 sec |
| Heavy corrosion/scale | 20--50% HCl | 3--5 min | Single rinse, ambient, 30--60 sec |

**Rinse parameters:**
- `Single overflow, ambient, 15--30 sec`
- `Goal: remove acid -- not a thorough multi-stage rinse`
- `Move to chrome bath promptly after rinse`

Note: `After external acid etch, the part still gets reverse etched in the chrome bath (brief, 15--30 sec) before polarity reversal to plating. The acid etch supplements the reverse etch; it does not replace it.` -- Inter Medium, 13 pt, `#2EC4B6`

---

### ZONE 6 -- Acid Drag-In Risks

**Section label:** `ACID DRAG-IN RISKS (EXTERNAL ETCH ONLY)` -- Y: 26.7".

**BLOCK F -- Risk Panel (Y: 27.3" to 32.3")**

| Contaminant | Effect on Chrome Bath | Severity |
|---|---|---|
| HCl drag-in | Chloride attacks lead anodes; disrupts anode film | HIGH (`#E05C5C`) |
| H2SO4 drag-in | Increases sulfate -- shifts CrO3:SO4 ratio | MODERATE (`#E8A020`) |
| Iron salts | Adds to iron contamination already present from reverse etch | LOW (`#2EC4B6`) |

Key callout:
- `Chloride is the killer. If you use HCl for external acid etch, your rinse quality is critical. H2SO4 is less damaging because the chrome bath already contains sulfate as a catalyst.` -- Inter Medium, 14 pt, `#E05C5C`

Recommendation:
- `For external acid etch, prefer H2SO4 over HCl when possible. Sulfate drag-in is easier to manage than chloride.` -- Inter Medium, 13 pt, `#E8A020`

---

### ZONE 7 -- Footer

Standard. Title: `Rinse -- Hard Chrome -- Pre-Plate`. Version `v1.0 -- 2026`.

Disclaimer note: `Source: General industry knowledge; hard chrome process engineering practice. Hard chrome uses hexavalent chromium -- comply with all OSHA and EPA regulations.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Hard Chrome Rinse Pre-Plate -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster and Poster #83 (decorative chrome pre-plate rinse) share the same structural approach: a decision tree that honestly says "you probably skip this stage." The difference: decorative chrome skips it because of in-tank activation (a convenience choice). Hard chrome skips it because reverse etch is the standard process (a process engineering reality). The large "SKIP THIS STAGE" text in the standard path makes the poster immediately useful -- an operator glances at it and knows the answer. The exception path gives the detail for the 5% of jobs that need it. The H2SO4 over HCl recommendation is a practical tip that will earn this poster wall space.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #91 -- Construction Workup v1.0*
*2026-04-26*
