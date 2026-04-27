---
Project: Plating Posters Inc
Poster Number: 363
Title: "Inspection & Handling -- Pickled Parts (Carbon Steel)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Chemical Treatment Clusters -- Watson Research Brief (CT-3.7)"
Technical Source: Industry-standard post-pickle inspection and handling for carbon steel. Covers visual criteria for properly pickled surfaces, flash rust prevention, hydrogen blister identification, and the critical requirement to keep pickled parts wet.
Process Scope: Quality verification and part handling after acid pickling of carbon steel
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - AcidPickling
  - CarbonSteel
  - Inspection
  - Handling
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT03
---

# Poster #363 -- Construction Workup
## Inspection & Handling -- Pickled Parts (Carbon Steel)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Poster 7 of 7 in the CT-03 cluster. This poster closes the carbon steel acid pickling cluster with the post-pickle quality gate. The hero visual is a four-panel defect identification guide showing the difference between properly pickled steel, over-pickled steel, under-pickled steel, and flash-rusted steel. The handling rules are dominated by one theme: KEEP PARTS WET. Flash rusting is the #1 post-pickle defect and it begins within minutes of air exposure. The water break test is less definitive after acid pickling than after alkaline cleaning (acid-clean surfaces are inherently hydrophilic), so visual inspection carries more weight here.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Four-panel defect identification (Block B -- HERO):** Side-by-side comparison of correct pickle, over-pickle, under-pickle, and flash rust.
2. **Visual inspection criteria table (Block D):** What to look for on different steel types.
3. **Flash rust prevention panel (Block E):** Timing, humidity, and keep-wet protocol.
4. **Handling rules (Block F):** Post-pickle dos and don'ts.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.0" / 20.5" / 26.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Poster 7 of 7 highlighted (Emerald)
ZONE 3 -- DEFECT IDENTIFICATION GUIDE / HERO (4.2"--15.0" / ~10.8")
ZONE 4 -- VISUAL INSPECTION CRITERIA (15.0"--20.5" / ~5.5")
ZONE 5 -- FLASH RUST PREVENTION (20.5"--26.0" / ~5.5")
ZONE 6 -- HANDLING RULES (26.0"--32.5" / ~6.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `INSPECTION & HANDLING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Pickled Parts (Carbon Steel) -- What Good Looks Like` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `A properly pickled surface tells its own story. Learn to read it -- and learn how fast it can turn on you in open air.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Poster 7 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Pickled and rinsed parts --> After: Inspected, handled properly, transferred to plating or storage`

---

### ZONE 3 -- Defect Identification Guide (HERO)

**Section label:** `POST-PICKLE SURFACE CONDITIONS -- KNOW THE DIFFERENCE` -- Y: 4.4".

**BLOCK B -- Four-Panel Comparison (Y: 5.0" to 14.5")**

Four large panels in a 2x2 grid.

**Top Left -- CORRECT PICKLE (X: 0.5", Y: 5.0", W: 11.0", H: 4.5"):**

Rounded rect, fill `#1E2435`, border 2 pt `#27AE60`, radius 8.

Title: `CORRECT PICKLE` Barlow Condensed ExtraBold 28 pt `#27AE60`, centered.

**Surface description:**
- Barlow SemiBold 16 pt `#F0EDE8`: `Uniformly bright (low-carbon) or matte gray (high-carbon)`
- Inter Regular 13 pt `#F0EDE8`:
```
- No residual scale, rust, or oxide
- No pitting or rough texture
- Clean metallic appearance
- Carbon smut on high-carbon steel is NORMAL
  and acceptable (removed in subsequent steps)
```
- Tag: `PROCEED TO NEXT STEP` Inter Medium 14 pt `#27AE60`

**Top Right -- OVER-PICKLE (X: 12.0", Y: 5.0", W: 11.5", H: 4.5"):**

Rounded rect, fill `#1E2435`, border 2 pt `#E05C5C`, radius 8.

Title: `OVER-PICKLE` Barlow Condensed ExtraBold 28 pt `#E05C5C`, centered.

**Surface description:**
- Barlow SemiBold 16 pt `#F0EDE8`: `Pitted, rough, or etched surface`
- Inter Regular 13 pt `#F0EDE8`:
```
- Visible pitting (tiny holes in surface)
- Rough texture where steel was dissolved
- Excessive metal loss (dimensional change)
- May show hydrogen blisters (raised bumps)
```
- Cause: `Too long, too strong, no inhibitor` Inter Medium 12 pt `#E05C5C`
- Tag: `DO NOT PLATE -- REPORT` Inter Medium 14 pt `#E05C5C`

**Bottom Left -- UNDER-PICKLE (X: 0.5", Y: 10.0", W: 11.0", H: 4.5"):**

Rounded rect, fill `#1E2435`, border 2 pt `#E8A020`, radius 8.

Title: `UNDER-PICKLE` Barlow Condensed ExtraBold 28 pt `#E8A020`, centered.

**Surface description:**
- Barlow SemiBold 16 pt `#F0EDE8`: `Residual scale, patches of dark oxide`
- Inter Regular 13 pt `#F0EDE8`:
```
- Patches of remaining mill scale or rust
- Uneven appearance (clean + dirty areas)
- Scale edges visible (peeling partially)
- Often caused by depleted acid or high iron
```
- Cause: `Time too short, acid depleted, iron too high` Inter Medium 12 pt `#E8A020`
- Tag: `RETURN TO PICKLE -- DO NOT PLATE` Inter Medium 14 pt `#E8A020`

**Bottom Right -- FLASH RUST (X: 12.0", Y: 10.0", W: 11.5", H: 4.5"):**

Rounded rect, fill `#1E2435`, border 2 pt `#E05C5C`, radius 8.

Title: `FLASH RUST` Barlow Condensed ExtraBold 28 pt `#E05C5C`, centered.

**Surface description:**
- Barlow SemiBold 16 pt `#F0EDE8`: `Orange-brown film on recently clean surface`
- Inter Regular 13 pt `#F0EDE8`:
```
- Appears within 5-15 minutes in humid air
- Thin, uniform orange-brown discoloration
- Surface was properly pickled but allowed to dry
- Requires re-pickle or extended acid activation
```
- Cause: `Parts air-dried between pickle and plate` Inter Medium 12 pt `#E05C5C`
- Tag: `PREVENTABLE -- SEE ZONE 5` Inter Medium 14 pt `#E05C5C`

---

### ZONE 4 -- Visual Inspection Criteria

**Section label:** `WHAT TO LOOK FOR -- BY STEEL TYPE` -- Y: 15.2".

**BLOCK D -- Three-Column Table (Y: 15.8" to 20.3")**

Column widths (23.0" total):
- Steel Type (5.0") | Correct Appearance (7.0") | Defects to Watch (7.0") | Carbon Smut? (4.0")

Header row: fill `#3A4055`, H: 0.5". Barlow SemiBold 14 pt.

| Steel Type | Correct Appearance | Defects | Carbon Smut? |
|---|---|---|---|
| Low-Carbon (1008-1020) | Bright, shiny, clean metallic | Pitting = over-pickle; dark patches = under-pickle | No -- should be bright |
| Medium-Carbon (1035-1050) | Bright to slightly matte | Light surface roughening possible; pitting = over-pickle | Light smut possible -- normal |
| High-Carbon (1070-1095) | Matte gray, uniform | Grain boundary attack if over-pickled; rough texture | YES -- dark carbon smut is expected and normal |
| Alloy Steel (4130, 4340, 8620) | Matte, may show alloy pattern | Watch for preferential attack on alloy-rich areas | May show selective smut from alloy elements |

Data: Inter Regular 12 pt `#F0EDE8`. Steel type names: JetBrains Mono 13 pt, accent-colored:
- Low-Carbon: `#27AE60`
- Medium-Carbon: `#2EC4B6`
- High-Carbon: `#E8A020`
- Alloy: `#E05C5C`

---

### ZONE 5 -- Flash Rust Prevention

**Section label:** `FLASH RUST -- THE CLOCK STARTS NOW` -- Y: 20.7".

**BLOCK E -- Full-Width Warning Panel (Y: 21.3" to 25.8")**

Rounded rect W: 23.0", H: 4.0", fill `#E05C5C` at 10%, border 2 pt `#E05C5C`, radius 8.

**Three-column interior:**

**Left -- Timing (W: 7.0"):**
- Title: `HOW FAST?` Barlow Condensed ExtraBold 28 pt `#E05C5C`
- Body: Inter Regular 14 pt `#F0EDE8`:
```
Low humidity (<40% RH):
  Visible rust in 15-30 minutes

Moderate humidity (40-60% RH):
  Visible rust in 10-15 minutes

High humidity (>60% RH):
  Visible rust in 5-10 minutes
```
- JetBrains Mono 16 pt `#E05C5C`: `5-30 MIN`

**Center -- Prevention Protocol (W: 7.0"):**
- Title: `KEEP PARTS WET` Barlow SemiBold 18 pt `#27AE60`
- Body:
```
1. Transfer from rinse to acid activate
   or plating tank IMMEDIATELY
2. If delay is unavoidable, keep parts
   submerged in clean rinse water
3. If parts must be stored: use inhibited
   rinse water or light oil coating
4. NEVER allow pickled parts to air-dry
   on a rack or bench
```

**Right -- If Flash Rust Occurs (W: 7.0"):**
- Title: `RECOVERY` Barlow SemiBold 18 pt `#E8A020`
- Body:
```
Light flash rust:
  Extended acid activation may remove it
  (15-30 sec in dilute HCl)

Heavy flash rust:
  Return to pickle
  Re-rinse and transfer immediately

Prevention is always cheaper than recovery.
Every re-pickle costs time, acid, and
increases hydrogen exposure.
```

---

### ZONE 6 -- Handling Rules

**Section label:** `HANDLING AFTER PICKLING -- THE RULES` -- Y: 26.2".

**BLOCK F -- Handling Rules Grid (Y: 26.8" to 32.3")**

Two rows of three cards.

| Card | Position | Rule |
|---|---|---|
| KEEP PARTS WET | R1C1 | The single most important rule. Pickled steel begins to oxidize immediately in air. Submerge in clean rinse water if any delay occurs between pickle and plate. |
| CLEAN GLOVES | R1C2 | Wear clean nitrile or latex gloves. Fingerprint oils on pickled steel create adhesion failures that show up as blisters after plating. |
| DO NOT STACK | R1C3 | Stacking traps moisture between parts, creating crevice corrosion and uneven drying. Keep parts on racks or in individual positions. |
| MINIMIZE HANDLING | R2C1 | Every time a pickled part is touched, it is a contamination risk. Handle by edges or rack only. Plan the workflow to minimize transfers. |
| LOG PICKLE TIME | R2C2 | Document immersion time for every load. This is required for aerospace (AS9100D) and good practice everywhere. Over-pickle is invisible until plating reveals the damage. |
| CHECK FOR BLISTERS | R2C3 | Hydrogen blisters appear as small raised bumps on the surface. If present, the part has absorbed hydrogen during pickle. High-strength steel: flag for HE bake evaluation. |

Each card: Rounded rect W: 7.33", H: 2.5", fill `#1E2435`, radius 6.
- Rule name: Barlow SemiBold 14 pt `#E8A020`
- Rule text: Inter Regular 12 pt `#F0EDE8`
- "KEEP PARTS WET" card: left accent `#E05C5C` (priority). Others: left accent `#2EC4B6`.

---

### ZONE 7 -- Footer

Standard. Title: `Inspection & Handling -- Pickled Parts (Carbon Steel)`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; Metal Finishing Guidebook; ASTM B850 (hydrogen embrittlement). Flash rust timing varies with humidity, temperature, and alloy composition. Carbon smut on high-carbon steel is normal and does not indicate a pickling defect.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Inspection Handling Pickled Parts Carbon Steel -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster closes the CT-03 cluster. The four-panel hero is a departure from the water break test hero used in CT-01 and CT-02 -- after acid pickling, visual inspection is more informative than the water break test (acid-clean surfaces are hydrophilic by nature, making the water break test less discriminating). The four panels cover the complete diagnostic space: correct, over, under, and flash rust. The flash rust prevention section is the most urgent callout -- this is where most post-pickle defects originate, and it is entirely preventable with proper handling. The carbon smut note for high-carbon steel prevents unnecessary rework of a normal condition.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #363 -- Construction Workup v1.0*
*2026-04-26*
