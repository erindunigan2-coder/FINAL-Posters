---
Project: Plating Posters Inc
Poster Number: 391
Title: "Inspection & Handling -- Ultrasonic Cleaning"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster CT-7 technical reference (ultrasonic cleaning)"
  - "Chemical Treatment Clusters — Watson Research Brief"
Process Scope: Ultrasonic cleaning -- cleanliness verification, cavitation monitoring, part handling post-clean
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - UltrasonicCleaning
  - Inspection
  - Handling
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT07
---

# Poster #391 -- Construction Workup
## Inspection & Handling -- Ultrasonic Cleaning

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

The final poster in the Ultrasonic Cleaning cluster. Cleaning is only as good as your ability to verify it. This poster covers four cleanliness verification methods (water break, UV fluorescence, particle count, NVR), four cavitation monitoring tools (foil test, cavitation meter, power meter, temperature monitoring), and handling rules that prevent re-contamination after all that work.

Hero visual: a four-panel cleanliness verification guide showing each test method with pass/fail criteria.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cleanliness verification panel (Block B -- HERO):** Four verification methods with pass/fail visual indicators.
2. **Cavitation monitoring tools (Block D):** Four tools for monitoring the ultrasonic system itself.
3. **Handling rules (Block E):** Post-clean handling to prevent re-contamination.
4. **Substrate compatibility reference (Block F):** Quick frequency guide by substrate.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts per series design system.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.5" / 22.0" / 28.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 6 highlighted (Amber) -- "Inspect & Handle"
ZONE 3 -- CLEANLINESS VERIFICATION HERO (4.2"--15.5" / ~11.3")
ZONE 4 -- CAVITATION MONITORING TOOLS (15.5"--22.0" / ~6.5")
ZONE 5 -- HANDLING RULES (22.0"--28.0" / ~6.0")
ZONE 6 -- SUBSTRATE COMPATIBILITY (28.0"--32.5" / ~4.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `INSPECTION & HANDLING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Ultrasonic Cleaning -- Verify the Clean, Protect the Surface` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `If you cannot prove it is clean, it is not clean. And if you touch it wrong after cleaning, it is not clean anymore.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 6 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Cleaned and dried parts --> After: Verified clean parts ready for next process`

---

### ZONE 3 -- Cleanliness Verification Hero

**Section label:** `FOUR WAYS TO VERIFY CLEANLINESS` -- Y: 4.4".

**BLOCK B -- Four Verification Panels**

Y: 5.0" to 15.3". 2x2 grid of verification method panels.

Each panel: Rounded rect, W: 11.0", H: 4.8", fill `#1E2435`, left accent 0.06", radius 6.

| Panel | Position | Method | Accent |
|---|---|---|---|
| 1 | R1C1 (X: 0.5", Y: 5.0") | WATER BREAK TEST | `#2EC4B6` |
| 2 | R1C2 (X: 12.0", Y: 5.0") | UV FLUORESCENCE (365 nm) | `#E8A020` |
| 3 | R2C1 (X: 0.5", Y: 10.3") | PARTICLE COUNT | `#27AE60` |
| 4 | R2C2 (X: 12.0", Y: 10.3") | NVR (NON-VOLATILE RESIDUE) | `#E05C5C` |

*Panel 1 -- Water Break Test:*
- Title: `WATER BREAK TEST` Barlow SemiBold 20 pt `#2EC4B6`
- Subtitle: `Simplest and most common` Inter Regular 14 pt `#F0EDE8` at 60%
- Method: `Rinse part with clean water. Observe water film behavior.`
- PASS: `Water sheets uniformly -- no breaks, no beading` `#27AE60`
- FAIL: `Water beads up or pulls away from areas -- oil/contaminant present` `#E05C5C`
- Applicability: `All aqueous-cleaned parts before plating`
- Limitation: `Cannot detect sub-micron particles or light ionic contamination`

*Panel 2 -- UV Fluorescence:*
- Title: `UV FLUORESCENCE` Barlow SemiBold 20 pt `#E8A020`
- Subtitle: `Detects organic contamination` Inter Regular 14 pt `#F0EDE8` at 60%
- Method: `Inspect part under 365 nm UV (black light) in darkened area.`
- PASS: `No fluorescence -- surface is free of organic residue` `#27AE60`
- FAIL: `Blue-white or yellow fluorescence -- oil, grease, or organic film present` `#E05C5C`
- Applicability: `Quick check for organic contamination after degreasing/cleaning`
- Limitation: `Not all contaminants fluoresce; some substrates auto-fluoresce`

*Panel 3 -- Particle Count:*
- Title: `PARTICLE COUNT` Barlow SemiBold 20 pt `#27AE60`
- Subtitle: `Precision applications` Inter Regular 14 pt `#F0EDE8` at 60%
- Method: `Rinse part with known-clean solvent; analyze rinse for particle size and count.`
- Standards: `ASTM E1216 (general) / ISO 16232 (automotive) / IEST-STD-CC1246 (aerospace)`
- Applicability: `Semiconductor, medical, optical, aerospace`
- Note: `Requires lab equipment or external testing service` JetBrains Mono 12 pt `#F0EDE8` at 60%

*Panel 4 -- NVR (Non-Volatile Residue):*
- Title: `NVR TEST` Barlow SemiBold 20 pt `#E05C5C`
- Subtitle: `Measures total organic residue` Inter Regular 14 pt `#F0EDE8` at 60%
- Method: `Rinse part with high-purity solvent; evaporate solvent; weigh residue.`
- Standards: `ASTM F331 / IEST-STD-CC1246 Level requirements`
- Applicability: `Aerospace, semiconductor, medical implants`
- Note: `Gold standard for organic cleanliness verification` JetBrains Mono 12 pt `#E8A020`

Interior per panel:
- Title: Barlow SemiBold, 20 pt, accent color
- Method: Inter Regular, 14 pt, `#F0EDE8`
- Pass/Fail: Inter Medium, 13 pt, color-coded
- Standards: JetBrains Mono, 12 pt, `#F0EDE8` at 70%

---

### ZONE 4 -- Cavitation Monitoring Tools

**Section label:** `MONITOR YOUR ULTRASONICS -- 4 TOOLS` -- Y: 15.7".

**BLOCK D -- Four-Tool Table**

Y: 16.3" to 21.8". Column widths (23.0" total):
- Tool (5.0") | Measures (6.0") | Use (7.0") | Frequency (5.0")

Header row: fill `#3A4055`, H: 0.5".

| Tool | Measures | Use | Frequency |
|---|---|---|---|
| Aluminum foil test | Qualitative cavitation distribution | Quick shop-floor check | Monthly or after service |
| Cavitation meter | Intensity in watts/cm2 | Quantitative process validation | Quarterly or troubleshooting |
| Power meter | Actual power to tank (watts) | Verifies generator output vs. spec | After install; annually |
| Temperature monitoring | Solution temp vs. time | Detects heating from ultrasonic input; process window | Continuous or per batch |

Data: Inter Regular 13 pt. Tool names: Barlow SemiBold 14 pt.

**Callout (Y: 21.3"):**
- `The aluminum foil test costs nothing and takes 60 seconds. Every shop should do it monthly. See Poster #388 for detailed procedure.` Inter Medium 14 pt `#E8A020`

---

### ZONE 5 -- Handling Rules

**Section label:** `POST-CLEAN HANDLING -- DO NOT UNDO YOUR WORK` -- Y: 22.2".

**BLOCK E -- Handling Rules Grid**

Y: 22.8" to 27.8". Six rule cards in 2x3 grid.

Each card: Rounded rect, W: 7.33", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06".

| Card | Position | Rule | Accent |
|---|---|---|---|
| 1 | R1C1 | Clean gloves ONLY -- fingerprints are oil contamination | `#E05C5C` |
| 2 | R1C2 | Handle by edges or fixtures, never plating surfaces | `#E8A020` |
| 3 | R1C3 | Process to next step WITHOUT DELAY | `#E05C5C` |
| 4 | R2C1 | Store in clean, covered containers if hold > 30 min | `#2EC4B6` |
| 5 | R2C2 | Never blow on parts -- breath = moisture + organics | `#E05C5C` |
| 6 | R2C3 | If contaminated or dropped, RE-CLEAN from scratch | `#E8A020` |

Rule: Inter Medium, 14 pt, `#F0EDE8`. Accent on left border per card.

---

### ZONE 6 -- Substrate Compatibility Quick Reference

**Section label:** `SUBSTRATE FREQUENCY QUICK REFERENCE` -- Y: 28.2".

**BLOCK F -- Compatibility Table**

Y: 28.8" to 32.3". Column widths:
- Substrate (5.0") | Recommended Frequency (5.0") | Caution (13.0")

| Substrate | Frequency | Caution |
|---|---|---|
| Hardened steel | 25--40 kHz (any) | Generally safe at all frequencies |
| Soft aluminum / thin-wall | 40--80 kHz preferred | 25 kHz can cause cavitation erosion on thin sections |
| Zinc die cast | 40+ kHz | Porous casting traps solution; limit time |
| Plastics / polymers | 40--80 kHz | Some plastics absorb ultrasonic energy; verify |
| Electronics / PCBs | 80--170 kHz (megasonic) | Low frequency damages wire bonds, solder joints, MEMS |

Data: JetBrains Mono 12 pt. Substrate names: Inter Medium 13 pt.

---

### ZONE 7 -- Footer

Standard. Title: `Inspection & Handling -- Ultrasonic Cleaning`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Cleanliness verification methods and acceptance criteria vary by application, specification, and customer requirements. Consult applicable standards for specific pass/fail criteria.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Inspection Handling Ultrasonic -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster closes the Ultrasonic Cleaning cluster by answering "how do I know it worked?" The four verification methods scale from shop-floor simple (water break test -- free, takes 5 seconds) to laboratory-grade (NVR -- requires a lab, but is the gold standard). The substrate compatibility table at the bottom serves as a quick-reference wrap for the entire cluster. Cross-reference callout to Poster #388 for the aluminum foil test keeps the cluster connected.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #391 -- Construction Workup v1.0*
*2026-04-26*
