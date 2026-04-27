---
Project: Plating Posters Inc
Poster Number: 56
Title: "Cleaning -- Nickel (Watts)"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-04 technical reference (Watts nickel)"
  - "Watson Research Brief -- Electroplating Clusters EP-02 through EP-15"
Technical Source: Alkaline soak clean and electrocleaner for Watts nickel plating. Nickel is the most demanding deposit regarding surface cleanliness -- any residue causes pitting, skip plating, or peeling.
Process Scope: Cleaning stage for Watts nickel plating (Stage 1 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - NickelPlating
  - Watts
  - Cleaning
  - ConstructionWorkup
  - Series2
  - ClusterEP04
---

# Poster #56 -- Construction Workup
## Cleaning -- Nickel (Watts)

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 1 of 8. Cleaning for nickel plating is not optional -- it is the single most common root cause of nickel plating failures. This poster covers the two-step cleaning sequence: alkaline soak clean followed by electrocleaner. The water-break test is the go/no-go criterion. If the surface is not water-break-free, nothing downstream will work.

Hero visual: side-by-side comparison of soak clean tank and electrocleaner tank with labeled parameters.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Dual-tank hero (Block B):** Two rounded rectangles representing soak clean and electrocleaner tanks, side by side with parameter callouts.
2. **Water-break test callout (Block C):** A prominent visual showing pass/fail criteria.
3. **Anodic vs. cathodic electrocleaning comparison (Block E):** Two-column callout.
4. **Substrate-specific notes (Block D):** Table of cleaning adjustments by substrate.
5. **Contamination types panel (Block F):** What each contaminant type looks like and how it affects downstream plating.

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
ZONE 3 -- CLEANING TANKS HERO (4.2"--14.5" / ~10.3")
  Block B: Soak clean + electrocleaner side-by-side
  Block C: Water-break test callout
ZONE 4 -- CLEANING PARAMETERS TABLE (14.5"--20.5" / ~6.0")
  Block D: Substrate-specific cleaning table
ZONE 5 -- ANODIC VS CATHODIC + CONTAMINATION (20.5"--26.5" / ~6.0")
  Block E: Anodic vs. cathodic comparison
  Block F: Contamination types
ZONE 6 -- COMMON FAILURES + SAFETY (26.5"--32.5" / ~6.0")
  Block G: 4 cleaning failure modes
  Block H: Safety callout
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CLEANING` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Nickel (Watts) -- Stage 1 of 8` -- 36 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `Nickel is the most unforgiving deposit on your line. If it is not water-break-free, do not plate it.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Y: 2.9" to 4.2".

Eight mini-boxes in a horizontal row. Stage 1 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed: fill `#1E2435`, text `#F0EDE8` at 40%.

Below strip: `Before: Oily, oxidized substrate --> After: Water-break-free surface ready for activation`
- Inter Medium, 14 pt, `#F0EDE8` at 60%

---

### ZONE 3 -- Cleaning Tanks Hero

**Section label:** `THE TWO-STEP CLEANING SEQUENCE` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Dual Tank Diagram**

Y: 5.0" to 12.0".

**Left -- Soak Clean Tank (X: 0.5", W: 11.0", H: 6.5"):**
- Rounded rect, fill `#252B3D`, border 2 pt `#2EC4B6`
- Title inside: `STEP 1: ALKALINE SOAK CLEAN` Barlow SemiBold 18 pt `#2EC4B6`
- Parameter labels (JetBrains Mono 14 pt `#F0EDE8`):
```
Type: Non-chelated or mild chelated
Concentration: 4--8 oz/gal (30--60 g/L)
Temperature: 140--190 F (60--88 C)
Time: 3--10 min (soak)
      1--3 min (spray)
pH: 12--14
Agitation: Air or mechanical
```
- Purpose note: `Removes oils, drawing compounds, rust preventatives, shop soil` Inter Regular 13 pt `#F0EDE8` at 70%

**Right -- Electrocleaner Tank (X: 12.5", W: 11.0", H: 6.5"):**
- Rounded rect, fill `#252B3D`, border 2 pt `#E8A020`
- Title inside: `STEP 2: ELECTROCLEANER` Barlow SemiBold 18 pt `#E8A020`
- Parameter labels (JetBrains Mono 14 pt `#F0EDE8`):
```
Concentration: 4--8 oz/gal (30--60 g/L)
Temperature: 140--180 F (60--82 C)
Current density: 30--80 ASF
Time: 1--3 min
Polarity: Anodic (reverse) preferred
```
- Purpose note: `Final clean -- gas scrubbing action at workpiece surface` Inter Regular 13 pt `#F0EDE8` at 70%

**BLOCK C -- Water-Break Test Callout**

Y: 12.3" to 14.3".
- Rounded rect, full width, H: 1.8", fill `#27AE60` at 15%, border 2 pt `#27AE60`, radius 8
- Title: `THE WATER-BREAK TEST -- YOUR GO / NO-GO` Barlow Condensed ExtraBold, 22 pt, `#27AE60`
- Body (Inter Medium 14 pt `#F0EDE8`):

> Rinse the part. Watch the water film. A fully clean surface holds a continuous, unbroken sheet of water for 30+ seconds with zero beading or breaking. Any break = contamination remains. Do not proceed to activation. Re-clean.

---

### ZONE 4 -- Substrate-Specific Cleaning

**Section label:** `CLEANING ADJUSTMENTS BY SUBSTRATE` -- Y: 14.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK D -- Substrate Table**

Y: 15.3" to 20.3". Column widths (23.0" total):
- Substrate (4.5") | Cleaner Notes (6.5") | Electrocleaner Notes (6.5") | Watch For (5.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 13 pt, `#F0EDE8`.

| Substrate | Cleaner Notes | Electrocleaner Notes | Watch For |
|---|---|---|---|
| Steel (mild) | Standard alkaline | Anodic final preferred | Rust inhibitor residues |
| High-strength steel (>31 HRC) | Standard alkaline | Cathodic first, anodic final -- minimize total time | H-embrittlement risk from cathodic clean |
| Copper / Brass | Non-etch alkaline preferred | Anodic only -- cathodic embeds metals | Tarnish films -- may need acid pre-dip |
| Zinc die cast | Mild alkaline, lower temp (120--140 F) | Low CD (20--40 ASF), short time | Aggressive cleaning attacks zinc surface |
| Stainless steel | Standard alkaline | Anodic -- then Wood's strike mandatory | Passive oxide film reforms immediately |

Data: Inter Regular, 12 pt, `#F0EDE8`. Alternating rows `#1E2435` / `#252B3D`.

---

### ZONE 5 -- Anodic vs. Cathodic + Contamination Types

**Two-column layout (Y: 20.7" to 26.3"):**

**Left -- Anodic vs. Cathodic (X: 0.5", W: 11.0"):**

Section label: `ANODIC VS. CATHODIC CLEANING` Barlow Condensed ExtraBold 20 pt `#F0EDE8`.

Two stacked callout boxes:

*Anodic (Reverse):*
- Rounded rect, H: 2.2", fill `#1E2435`, left accent `#27AE60`
- Title: `ANODIC (REVERSE)` Barlow SemiBold 16 pt `#27AE60`
- Body: `Generates O2 at workpiece. Scrubbing action. Removes smut. Does not embed metal contaminants. Preferred for final clean on all substrates.` Inter Regular 13 pt `#F0EDE8`
- Tag: `RECOMMENDED FOR NICKEL` Inter Medium 12 pt `#27AE60`

*Cathodic (Direct):*
- Rounded rect, H: 2.2", fill `#1E2435`, left accent `#E8A020`
- Title: `CATHODIC (DIRECT)` Barlow SemiBold 16 pt `#E8A020`
- Body: `Generates H2 at workpiece. Better for heavy soil removal. CAN embed metal contaminants (Cu, Fe) and CAUSE hydrogen embrittlement on high-strength steel.` Inter Regular 13 pt `#F0EDE8`
- Tag: `USE FIRST FOR HEAVY SOIL ONLY` Inter Medium 12 pt `#E8A020`

**Right -- Contamination Types (X: 12.5", W: 11.0"):**

Section label: `WHAT YOU ARE REMOVING` Barlow Condensed ExtraBold 20 pt `#F0EDE8`.

| Contaminant | Effect If Left | Removal |
|---|---|---|
| Stamping oils | Skip plating, pitting | Soak clean (surfactant action) |
| Oxide films | Poor adhesion, peeling | Electrocleaner + acid activation |
| Shop soil / dust | Roughness, inclusions | Soak clean |
| Fingerprints | Skip plating (local) | Soak clean -- handle with gloves |
| Rust preventative | Hazy deposit, poor adhesion | Extended soak, higher temp |

Table: Inter Regular 12 pt, alternating rows.

---

### ZONE 6 -- Common Failures + Safety

**Two-column layout (Y: 26.7" to 32.3"):**

**Left -- 4 Cleaning Failure Modes (X: 0.5", W: 14.0"):**

Section label: `WHAT GOES WRONG` Barlow Condensed ExtraBold 22 pt `#F0EDE8`.

| Failure | Root Cause | Result in Nickel Bath |
|---|---|---|
| Incomplete oil removal | Cleaner too dilute, temp too low, time too short | Pitting, skip plating |
| Silicate residue | Used silicated cleaner | Skip plating -- nearly impossible to remove |
| Metal embedding (cathodic) | Excessive cathodic cleaning | Dark spots, peeling, roughness |
| Over-etching (zinc die cast) | Cleaner too aggressive | Pitted substrate, poor adhesion |

Cards: Rounded rect, fill `#1E2435`, left accent `#E05C5C`. Failure: Barlow SemiBold 14 pt `#E05C5C`. Cause: Inter Regular 12 pt `#F0EDE8`. Result: Inter Medium 12 pt `#E8A020`.

**Right -- Safety Callout (X: 15.5", W: 8.0"):**

- Rounded rect, fill `#E05C5C` at 10%, border 1 pt `#E05C5C`, radius 8
- Title: `SAFETY` Barlow Condensed ExtraBold 20 pt `#E05C5C`
- Body (Inter Regular 13 pt `#F0EDE8`, line height 155%):

> - Alkaline cleaners: caustic burn hazard (pH 12--14). Gloves, goggles, apron required.
> - Electrocleaner generates gas at the workpiece. Ensure adequate ventilation.
> - Hot solutions (140--190 F): splash burn risk. Fill slowly, never add water to concentrated cleaner.

---

### ZONE 7 -- Footer

Standard footer. Title: `Cleaning -- Nickel (Watts)`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Specific formulations vary by supplier. Consult your process supplier for application-specific guidance.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table (see Poster 55).
**Export:** Six files -- `Cleaning Nickel Watts -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster establishes the critical message of the entire Watts nickel cluster: cleanliness is everything. The water-break test callout must be the single most visible element after the headline. Nickel plating failures trace back to cleaning more than any other root cause. The anodic vs. cathodic comparison answers a question every plater asks. The substrate table provides actionable guidance -- different parts need different handling.

---

*Alaina -- Plating Posters Inc Creative Lead*
*Poster #56 -- Construction Workup v1.0*
*2026-04-26*
