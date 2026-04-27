---
Project: Plating Posters Inc
Poster Number: 719
Title: "Flash / Leveling -- Protective Coatings"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster 8 technical reference (Protective Coatings -- Epoxy / Urethane) -- Watson Research Brief (Section 8.7)"
Process Scope: Flash / leveling (recoat windows and stripe coating) for protective coatings -- Stage 6 of 8
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ProtectiveCoatings
  - FlashLeveling
  - RecoatWindows
  - ConstructionWorkup
  - PaintingCoating
  - Cluster8
---

# Poster #719 -- Construction Workup
## Flash / Leveling -- Protective Coatings

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 6 of 8. In protective coatings, "flash/leveling" means recoat windows and stripe coating. The recoat window is the time period within which the next coat can be applied without sanding. Miss the window and the surface is too hard for intercoat adhesion -- you must scuff sand or even re-blast. The windows are chemistry-dependent and temperature-sensitive. Amine blush on epoxy is the silent killer: a waxy carbamate surface that forms in cool/humid conditions and causes intercoat adhesion failure if not removed.

Hero visual: recoat window timeline diagram showing minimum and maximum recoat times for four coating combinations, with amine blush warning zone highlighted, plus a stripe coating technique illustration.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Recoat window timeline hero (Block B):** Four horizontal bars showing min/max recoat windows for different coating-over-coating combinations.
2. **Amine blush deep-dive panel (Block D):** What it is, when it forms, and how to remove it.
3. **Stripe coating technique (Block E):** How and why stripe coats are applied before full spray coats.
4. **Defect strip (Block F):** 4 recoat/flash defects.

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
  Stage 6 highlighted (Amber)
ZONE 3 -- RECOAT WINDOW TIMELINE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- AMINE BLUSH (14.5"--20.5" / ~6.0")
ZONE 5 -- STRIPE COATING TECHNIQUE (20.5"--26.5" / ~6.0")
ZONE 6 -- RECOAT / FLASH DEFECTS (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `FLASH / LEVELING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Protective Coatings -- Stage 6 of 8: Recoat Windows` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Too soon and you trap solvent. Too late and the surface rejects the next coat. The recoat window is the contract between chemistry and time -- and amine blush is the clause nobody reads until it costs them.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 6 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Applied coating curing on substrate  -->  After: Surface within recoat window, ready for next coat`

---

### ZONE 3 -- Recoat Window Timeline Hero

**Section label:** `RECOAT WINDOWS -- MINIMUM AND MAXIMUM AT 77 F` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Four Timeline Bars (Y: 5.0" to 14.0")**

Full-width rounded rect, W: 23.0", H: 8.5", fill `#1E2435`, top accent 4 pt `#E8A020`.

X-axis (shared): `TIME AT 77 F` -- 0 hr to 30 days, logarithmic-style spacing.
- Markers at: 4 hr, 8 hr, 16 hr, 24 hr, 3 days, 7 days, 14 days, 30 days.

**Bar 1 -- Epoxy over Epoxy (Y: 5.5"):**
- Bar height 1.2", left end at 6 hr, right end at 7 days
- Fill `#2EC4B6` at 40%
- Left edge label: `MIN: 6-16 hr` JetBrains Mono 12 pt `#2EC4B6`
- Right edge label: `MAX: 3-7 days` JetBrains Mono 12 pt `#E05C5C`
- Beyond max: hatched red zone labeled `SAND 80-120 GRIT` JetBrains Mono 11 pt `#E05C5C`
- Left label: `EPOXY / EPOXY` Barlow SemiBold 14 pt `#F0EDE8`

**Bar 2 -- Urethane over Epoxy (Y: 7.2"):**
- Same structure
- Left end at 6 hr, right end at 7 days
- Fill `#27AE60` at 40%
- Left: `MIN: 6-16 hr` | Right: `MAX: 3-7 days`
- Beyond max: `SAND 180-320 GRIT`
- Label: `URETHANE / EPOXY`

**Bar 3 -- Epoxy over IOZ (Y: 8.9"):**
- Left end at 24 hr, right end at 30 days
- Fill `#E8A020` at 40%
- Left: `MIN: 24 hr` | Right: `MAX: 30 days`
- Beyond max: `SWEEP BLAST (SP7)`
- Label: `EPOXY / IOZ`

**Bar 4 -- Urethane over Urethane (Y: 10.6"):**
- Left end at 4 hr, right end at 3 days
- Fill `#E05C5C` at 30%
- Left: `MIN: 4-12 hr` | Right: `MAX: 1-3 days`
- Beyond max: `SAND 320 GRIT`
- Label: `URETHANE / URETHANE`

**Danger zone annotation (overlaid on all bars):**
- Vertical band at "too early" zone (before minimum): `TOO EARLY: SOLVENT TRAP` `#E05C5C`
- Vertical band beyond maximum: `TOO LATE: SAND OR BLAST` `#E05C5C`
- Green zone between min and max: `RECOAT WINDOW` `#27AE60`

Bottom callout (Y: 12.5"):
- `These windows are for 77 F (25 C). Higher temperature = shorter windows (pot life rule: halves per 18 F / 10 C increase). Lower temperature = longer windows AND risk of amine blush.` Inter Medium 13 pt `#E8A020`

---

### ZONE 4 -- Amine Blush

**Section label:** `AMINE BLUSH -- THE INVISIBLE ADHESION KILLER` -- Y: 14.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK D -- Full-Width Blush Panel (Y: 15.3" to 20.3")**

Rounded rect, fill `#1E2435`, left accent `#E05C5C` 0.06".

**Three-column layout:**

**Column 1 -- What It Is (X: 1.0", W: 7.0"):**
- Title: `WHAT IS AMINE BLUSH?` Barlow SemiBold 16 pt `#E05C5C`
- Body (Inter Regular 13 pt `#F0EDE8`, line height 155%):
  - `Amine hardener reacts with CO2 and moisture at the film surface`
  - `Forms amine carbamate -- a waxy, greasy layer`
  - `May appear as a haze, bloom, or sticky feel`
  - `Often INVISIBLE -- cannot be detected by eye alone`
  - `Present on the surface means intercoat adhesion failure`

**Column 2 -- When It Forms (X: 8.5", W: 7.0"):**
- Title: `WHEN DOES IT FORM?` Barlow SemiBold 16 pt `#E8A020`
- Conditions (JetBrains Mono 12 pt `#F0EDE8`):
  - `Temperature < 50 F (10 C)`
  - `Relative humidity > 80%`
  - `Cool/damp nights after daytime application`
  - `Dew formation on curing film`
  - `Any time surface temp drops near dew point`
- Warning: `Amine blush can form even when application conditions were acceptable -- overnight cooling is the trigger.` Inter Medium 12 pt `#E05C5C`

**Column 3 -- How to Remove It (X: 16.0", W: 7.0"):**
- Title: `HOW TO REMOVE IT` Barlow SemiBold 16 pt `#27AE60`
- Body:
  - `1. Wash with clean fresh water and scrub pad`
  - `2. Wipe with solvent (MEK or acetone) and clean rag`
  - `3. Allow surface to dry completely`
  - `4. Apply recoat within the recoat window`
  - `5. If window has been exceeded: sand first, then recoat`
- Note: `Some modern epoxy formulations are "blush-free" (non-blushing hardeners). Always verify with the coating TDS.` Inter Regular 12 pt `#2EC4B6`

---

### ZONE 5 -- Stripe Coating Technique

**Section label:** `STRIPE COATING -- PROTECTING THE WEAK POINTS` -- Y: 20.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK E -- Two-Column Panel**

Y: 21.3" to 26.3".

**Left -- What Is Stripe Coating (X: 0.5", W: 11.0"):**
- Rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `STRIPE COATING EXPLAINED` Barlow SemiBold 18 pt `#E8A020`

Bullet list (Inter Regular 13 pt `#F0EDE8`, line height 155%):
- `Before each FULL spray coat, apply a STRIPE coat by brush to:`
  - `All edges, corners, and sharp angles`
  - `Weld seams and bolt heads`
  - `Hard-to-reach areas and crevices`
  - `Any geometry where spray atomization thins the film`
- `DFT is always thinnest at edges and convex surfaces`
- `A stripe coat ensures minimum DFT at the weakest points`
- `Apply stripe coat, flash, THEN full spray coat`

**Right -- Where to Stripe (X: 12.0", W: 11.5"):**
- Rounded rect, fill `#1E2435`, left accent `#2EC4B6` 0.06"
- Title: `STRIPE COAT SEQUENCE` Barlow SemiBold 18 pt `#2EC4B6`

Numbered list:
1. `MIX coating per TDS` JetBrains Mono 12 pt
2. `STRIPE all edges, welds, bolts, and recesses with brush`
3. `FLASH stripe coat per TDS (typically 30-60 min)`
4. `SPRAY full coat over entire surface including striped areas`
5. `MEASURE DFT -- verify minimum at striped locations`

Callout: `Stripe coating is required by most marine, offshore, and infrastructure specifications (ISO 12944, SSPC). It is not optional.` Inter Medium 13 pt `#E8A020`.

---

### ZONE 6 -- Recoat / Flash Defects

**Section label:** `WHAT GOES WRONG -- 4 RECOAT / FLASH DEFECTS` -- Y: 26.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK F -- Four Problem Cards (Y: 27.3" to 30.3")**

Each card: Rounded rect, W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | INTERCOAT ADHESION FAILURE | Amine blush not removed; or recoat window exceeded | Wash/sand surface; remove blush; verify window before application |
| 2 | 6.33" | SOLVENT ENTRAPMENT (BUBBLING) | Topcoat applied before primer fully flashed; or insufficient flash between coats | Extend flash time; verify with solvent rub; reduce DFT per coat |
| 3 | 12.16" | LIFTING / WRINKLING | Strong solvent topcoat attacking undercured primer | Verify primer cure (MEK rub 50+) before topcoating; use compatible system |
| 4 | 18.0" | THIN DFT AT EDGES | Spray atomization thins film at edges and convex surfaces | Stripe coat ALL edges by brush before full spray coat |

**Key insight callout (Y: 30.6" to 32.3"):**
- Text: `The recoat window is the most commonly violated rule in protective coating application. Applicators who treat it as a suggestion -- "it has been a week but it should be fine" -- generate the most expensive rework in the industry. Exceeding the window means sanding or blasting before recoat. Check the TDS. Time the window. No exceptions.` -- Inter Medium, 14 pt, `#E8A020`

---

### ZONE 7 -- Footer

Standard. Title: `Flash / Leveling -- Protective Coatings`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Flash Leveling Protective Coatings -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The recoat window timeline is the centerpiece because it encapsulates the most practical, frequently-needed information for any protective coating applicator. The four bars with their green "safe zone" and red "too early / too late" boundaries make the concept visual and immediate. The amine blush section earns a full zone because this is the single most common cause of intercoat adhesion failure in industrial epoxy application -- and it is invisible. The stripe coating section addresses a practice that separates professional applicators from amateurs.

---

*Alaina -- Poster #719 -- Construction Workup v1.0 -- 2026-04-26*
