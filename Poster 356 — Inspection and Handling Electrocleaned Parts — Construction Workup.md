---
Project: Plating Posters Inc
Poster Number: 356
Title: "Inspection & Handling -- Electrocleaned Parts"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Chemical Treatment Clusters -- Watson Research Brief (CT-2.7)"
Technical Source: Industry-standard inspection and handling procedures after electrolytic cleaning. Water break test as the definitive pass/fail gate, visual criteria for smut and etching, and the 5-minute transfer rule.
Process Scope: Quality verification and part handling after electrocleaning
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Electrocleaning
  - Inspection
  - Handling
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT02
---

# Poster #356 -- Construction Workup
## Inspection & Handling -- Electrocleaned Parts

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Poster 7 of 7 in the CT-02 cluster. This poster closes the electrocleaning cluster with the final quality gate: the water break test after electrocleaning is the MOST CRITICAL pass/fail checkpoint on the entire plating line. If the part fails here, every subsequent process will fail. The hero visual is the same pass/fail water break comparison used in CT-01 (Poster 349) but with additional electrocleaning-specific visual criteria: smut, gas pitting, and etching. The 5-minute transfer rule is the unique handling callout -- parts must reach acid activation within 5 minutes to prevent oxide formation.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Water break test diagram (Block B -- HERO):** Pass vs. fail visual, same pattern as Poster 349.
2. **Electrocleaning-specific visual criteria (Block D):** Smut, gas pitting, etching -- defects unique to electrocleaning.
3. **The 5-minute rule (Block E):** Transfer timing callout.
4. **Handling rules (Block F):** Post-electroclean part handling dos and don'ts.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.0" / 25.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Poster 7 of 7 highlighted (Emerald)
ZONE 3 -- WATER BREAK TEST / HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- ELECTROCLEANING-SPECIFIC VISUAL CRITERIA (14.5"--20.0" / ~5.5")
ZONE 5 -- THE 5-MINUTE RULE (20.0"--25.0" / ~5.0")
ZONE 6 -- HANDLING RULES (25.0"--32.5" / ~7.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `INSPECTION & HANDLING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Electrocleaned Parts -- The Final Gate Before Plating` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `The water break test after electrocleaning is the most important quality check on the plating line. Fail here and nothing downstream can save the job.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Poster 7 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Electrocleaned and rinsed parts --> After: Verified clean, handled properly, transferred to acid activation within 5 minutes`

---

### ZONE 3 -- Water Break Test (HERO)

**Section label:** `THE WATER BREAK TEST -- THE DEFINITIVE QUALITY GATE` -- Y: 4.4".

**BLOCK B -- Side-by-Side Pass/Fail Visual (Y: 5.0" to 14.0")**

Same structure as Poster 349 with the following content:

**Left -- PASS (X: 0.5", W: 11.0"):**

Rounded rect H: 8.5", fill `#1E2435`, border 2 pt `#27AE60`, radius 8.

Title: `PASS` Barlow Condensed ExtraBold 36 pt `#27AE60`, centered.

**Surface diagram (Y: 6.5" to 9.0"):**
- Metal surface rectangle with continuous water film
- Label: `Water sheets uniformly -- no breaks` Barlow SemiBold 16 pt `#F0EDE8`
- Sub-label: `Continuous film for minimum 30 seconds` Inter Regular 14 pt `#27AE60`

**Below diagram:**
```
WHAT YOU SEE:
  Bright, clean metallic surface
  Water drains in a smooth, unbroken sheet
  No discoloration, no haze, no smut

WHAT IT MEANS:
  All organic contamination removed
  Surface is chemically active
  PROCEED to acid activation immediately
```

**Right -- FAIL (X: 12.0", W: 11.5"):**

Rounded rect H: 8.5", fill `#1E2435`, border 2 pt `#E05C5C`, radius 8.

Title: `FAIL` Barlow Condensed ExtraBold 36 pt `#E05C5C`, centered.

**Surface diagram:**
- Metal surface with broken water patches and droplets
- Label: `Water breaks, beads, or pulls away` Barlow SemiBold 16 pt `#F0EDE8`
- Sub-label: `DO NOT PROCEED -- return to cleaning` Inter Regular 14 pt `#E05C5C`

**Below diagram:**
```
WHAT YOU SEE:
  Water beading or breaking on any area
  Dark smut (gray or black residue)
  Etching or pitting (dull, rough areas)
  Gas pitting (tiny pinholes from excess CD)

WHAT IT MEANS:
  Contamination remains OR electrocleaner
  has damaged the surface
  DIAGNOSE before re-cleaning
```

---

### ZONE 4 -- Electrocleaning-Specific Visual Criteria

**Section label:** `VISUAL CRITERIA -- DEFECTS UNIQUE TO ELECTROCLEANING` -- Y: 14.7".

**BLOCK D -- Four Defect Cards (Y: 15.3" to 19.8")**

Four cards in a single row.

| Card | X | Defect | Appearance | Cause | Action |
|---|---|---|---|---|---|
| 1 | 0.5" | CATHODIC SMUT | Dark gray or black residue on surface | Dissolved metals plating out during cathodic mode | Switch to anodic; carbon treat bath; partial dump |
| 2 | 6.33" | GAS PITTING | Tiny pinholes or dimples in surface | Excessive current density; gas bubbles impinging too aggressively | Reduce CD; improve solution agitation |
| 3 | 12.16" | ETCHING | Dull, rough, or matte surface that should be bright | Chloride contamination; low alkalinity; excessive voltage | Check chlorides (>10 g/L = dump); check alkalinity; reduce voltage |
| 4 | 18.0" | STAINING | Discolored spots or streaks after rinse | Metal contamination in electrocleaner; inadequate rinsing | Carbon treat bath; improve rinse; check dissolved metals |

Each card: Rounded rect W: 5.5", H: 4.0", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

Interior per card:
- Defect name: Barlow SemiBold 16 pt `#E05C5C`
- Appearance: Inter Regular 12 pt `#F0EDE8`
- Cause: Inter Regular 12 pt `#E8A020`
- Action: Inter Medium 12 pt `#27AE60`

---

### ZONE 5 -- The 5-Minute Rule

**Section label:** `THE 5-MINUTE RULE -- TIME IS YOUR ENEMY` -- Y: 20.2".

**BLOCK E -- Full-Width Warning Panel (Y: 20.8" to 24.8")**

Rounded rect W: 23.0", H: 3.5", fill `#E05C5C` at 10%, border 2 pt `#E05C5C`, radius 8.

**Three-column interior:**

**Left -- The Rule (W: 7.0"):**
- Title: `5 MINUTES` Barlow Condensed ExtraBold 36 pt `#E05C5C`
- Body: Inter Medium 16 pt `#F0EDE8`:
```
Transfer to acid activation
within 5 minutes of
electrocleaning.

Oxide formation begins
immediately on clean metal.
```

**Center -- Why It Matters (W: 7.0"):**
- Title: `WHAT HAPPENS AT 5+ MIN` Barlow SemiBold 16 pt `#E8A020`
- Body: Inter Regular 13 pt `#F0EDE8`:
```
Steel: light oxide film forms
Copper: tarnish begins
Zinc die cast: white oxide
Aluminum: native oxide reforms

Any of these require re-cleaning
or more aggressive acid activation
to achieve proper adhesion.
```

**Right -- Prevention (W: 7.0"):**
- Title: `HOW TO COMPLY` Barlow SemiBold 16 pt `#27AE60`
- Body:
```
- Stage electrocleaner near acid tank
- Do not allow cleaned parts to air-dry
- If delay is unavoidable, keep parts
  submerged in clean rinse water
- Never allow parts to sit on bench
  between electroclean and acid activate
```

---

### ZONE 6 -- Handling Rules

**Section label:** `HANDLING AFTER ELECTROCLEANING -- THE RULES` -- Y: 25.2".

**BLOCK F -- Handling Rules Grid (Y: 25.8" to 32.3")**

Two rows of three cards.

| Card | Position | Rule |
|---|---|---|
| CLEAN GLOVES ONLY | R1C1 | Wear clean cotton or nitrile gloves. Any fingerprint on an electrocleaned surface is an instant water break failure. Change gloves if contaminated. |
| NO AIR-DRYING | R1C2 | Never let electrocleaned parts dry in air. Air-dried surfaces oxidize and require re-cleaning. Keep parts wet from electroclean through acid activate. |
| NO BARE HANDS | R1C3 | NEVER touch electrocleaned surfaces. Skin oils create organic films invisible to the eye but detected by the water break test. |
| RACK TIPS CLEAN | R2C1 | Inspect rack tips before every load. Corroded or contaminated rack tips cause poor contact (uneven gas evolution) and transfer contamination to parts. |
| PROCESS IMMEDIATELY | R2C2 | The 5-minute rule is not a suggestion. Stage your line so electrocleaned parts move directly to acid activation without pause. |
| DOCUMENT FAILURES | R2C3 | Log every water break failure with date, rack, and mode used. Patterns reveal root causes: recurring failures = systemic bath or process problem. |

Each card: Rounded rect W: 7.33", H: 2.8", fill `#1E2435`, radius 6.
- Rule name: Barlow SemiBold 14 pt `#E8A020`
- Rule text: Inter Regular 12 pt `#F0EDE8`
- Cards with "NO" or "NEVER": left accent `#E05C5C`. Others: left accent `#2EC4B6`.

---

### ZONE 7 -- Footer

Standard. Title: `Inspection & Handling -- Electrocleaned Parts`. Version `v1.0 -- 2026`.
Disclaimer: `Source: ASTM F22 (water break test); general industry knowledge; Metal Finishing Guidebook. Transfer timing varies by facility layout and substrate sensitivity. 5-minute maximum is a general guideline -- tighter for aerospace applications.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Inspection Handling Electrocleaned Parts -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster closes the CT-02 cluster with the same structural DNA as CT-01's closer (Poster 349) but with electrocleaning-specific content. The four defect cards in Zone 4 are new -- cathodic smut, gas pitting, etching, and staining are defects that do not exist after soak cleaning. The 5-minute rule panel is more aggressive than CT-01's "15-30 minute" flash rust warning because the electroclean-to-acid-activate transition is tighter and more sensitive. The handling rules emphasize documentation -- a pattern the series builds toward as posters become more process-critical.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #356 -- Construction Workup v1.0*
*2026-04-26*
