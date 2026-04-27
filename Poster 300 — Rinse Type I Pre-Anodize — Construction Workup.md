---
Project: Plating Posters Inc
Poster Number: 300
Title: "Rinse -- Chromic Acid Anodizing (Type I) -- Pre-Anodize"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 3, Section 3.6)"
Process Scope: Pre-anodize rinse for chromic acid anodizing -- Stage 5 of 8
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Anodizing
  - ChromicAcid
  - TypeI
  - Rinse
  - PreAnodize
  - ConstructionWorkup
  - ClusterAnodize03
---

# Poster #300 -- Construction Workup
## Rinse -- Chromic Acid Anodizing (Type I) -- Pre-Anodize

*Alaina -- Plating Posters Inc*
*v1.0 -- 2026-04-26*

Stage 5 of 8. The most critical rinse in the entire Type I sequence. The chromic acid bath has specific contamination limits that are tighter than sulfuric acid baths. Sulfate, chloride, and fluoride dragover all degrade the thin coating. DI water is mandatory. Triple cascade is common for aerospace.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Triple cascade rinse hero (Block B):** Three-tank cascade diagram with conductivity targets at each stage.
2. **Contamination limits table (Block D):** What each contaminant does to the chromic acid bath.
3. **Fluoride dragover callout (Block E):** Special warning for HF desmut residue.
4. **Defect grid (Block F):** 4 rinse-failure-to-anodize-defect connections.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 5 highlighted (Teal)
ZONE 3 -- TRIPLE CASCADE RINSE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- CONTAMINATION LIMITS TABLE (14.5"--20.5" / ~6.0")
ZONE 5 -- DEFECT GRID + FLUORIDE WARNING (20.5"--26.5" / ~6.0")
ZONE 6 -- MONITORING + BEST PRACTICES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Chromic Acid Anodizing (Type I) -- Pre-Anodize -- Stage 5 of 8` -- 30 pt `#2EC4B6`. Y: 1.4".
**Tagline:** `The last line of defense before the chromic acid bath. Every contaminant that survives this rinse degrades the electrolyte.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

**Cr(VI) flag:** Standard coral badge.

---

### ZONE 2 -- Orientation Strip

Stage 5 highlighted: fill `#2EC4B6`, text `#1A1F2E`.
Below: `Before: Desmutted surface carrying trace acid/fluoride  -->  After: Ultra-clean surface ready for chromic acid anodize`

---

### ZONE 3 -- Triple Cascade Rinse Hero

**Section label:** `TRIPLE CASCADE RINSE -- AEROSPACE STANDARD` -- Y: 4.4".

**BLOCK B -- Three-Tank Cascade Diagram**

Y: 5.0" to 13.5".

Three tanks left to right:

Tank 1 (drag-out, X: 1.0", W: 6.5"):
- Fill: `#252B3D`, border 2 pt `#C8D0D8`
- Label: `RINSE 1` Barlow SemiBold 16 pt
- `Highest contamination` Inter Regular 12 pt `#F0EDE8` at 60%

Tank 2 (intermediate, X: 8.5", W: 6.5"):
- Fill: `#252B3D` slightly lighter, border 2 pt `#C8D0D8`
- Label: `RINSE 2` Barlow SemiBold 16 pt
- `Intermediate quality` Inter Regular 12 pt `#F0EDE8` at 60%

Tank 3 (final, X: 16.0", W: 6.5"):
- Fill: `#252B3D` lightest, border 2 pt `#2EC4B6`
- Label: `RINSE 3 (FINAL)` Barlow SemiBold 16 pt `#2EC4B6`
- `Target: < 100 uS/cm` JetBrains Mono 14 pt `#27AE60`
- `DI water inlet` JetBrains Mono 12 pt `#2EC4B6`

Water flow arrows: Fresh DI enters Tank 3, overflows to Tank 2, overflows to Tank 1, Tank 1 to drain.
Part travel: arrow above all three tanks left to right.

**Operating parameters callout (Y: 12.0"):**
- `Water: DI water MANDATORY` JetBrains Mono 14 pt `#E05C5C`
- `Temperature: Ambient` JetBrains Mono 13 pt `#F0EDE8`
- `Time: 60--120 seconds minimum per stage` JetBrains Mono 13 pt `#F0EDE8`
- `Final rinse conductivity: < 100 uS/cm` JetBrains Mono 13 pt `#27AE60`
- `Aerospace standard: triple cascade` JetBrains Mono 13 pt `#E8A020`

---

### ZONE 4 -- Contamination Limits Table

**Section label:** `WHAT CONTAMINANTS DO TO THE CHROMIC ACID BATH` -- Y: 14.7".

Full-width table (Y: 15.3" to 20.3"):

| Contaminant | Limit in CrO3 Bath | Primary Source | Effect on Coating |
|---|---|---|---|
| Sulfate (SO4 2-) | < 0.5 g/L | Drag-over from sulfuric acid processes | Promotes dissolution; thins coating |
| Chloride (Cl-) | < 25 ppm (tight specs: < 10 ppm) | Process water; cleaner residue | Pitting attack on substrate |
| Fluoride (F-) | Trace only | HF desmut drag-over | Attacks growing oxide; degrades quality |
| Dissolved metals | Minimize | Aluminum, copper from parts | Reduces efficiency; discoloration |
| Organics | Zero | Cleaner residue; lubricants | Reduces Cr(VI) to Cr(III); loss of capacity |

Header: Barlow SemiBold 13 pt on `#3A4055`. Limits: JetBrains Mono 12 pt `#E05C5C`. Effects: Inter Regular 12 pt.

Below table callout:
- `The chromic acid bath is MORE sensitive to contamination than sulfuric acid baths. The dilute electrolyte (40--80 g/L CrO3) means even small dragover has proportionally larger impact.` Inter Medium 14 pt `#E8A020`

---

### ZONE 5 -- Defect Grid + Fluoride Warning

**Left -- Defect Grid (X: 0.5", W: 12.5", 2x2):**

Section label: `RINSE FAILURE --> ANODIZE DEFECT`

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | PITTING IN ANODIZE | `#E05C5C` | Chloride drag-over from rinse water | Switch to DI; add rinse stage |
| R1C2 | THIN COATING | `#E8A020` | Sulfate contaminating CrO3 bath | Improve rinse; trace sulfate source |
| R2C1 | SOFT COATING | `#E8A020` | Organic contamination reducing Cr(VI) to Cr(III) | Carbon treat anodize bath; improve pre-rinse |
| R2C2 | DEGRADED OXIDE | `#E05C5C` | Fluoride from HF desmut in anodize bath | Extend rinse time; add rinse stage after desmut |

**Right -- Fluoride Warning (X: 13.5", W: 10.0"):**

Coral-tinted callout:
- Title: `FLUORIDE DRAGOVER -- SILENT KILLER` Barlow SemiBold 18 pt `#E05C5C`
- `If your desmut uses HF (for 2024, 7075), fluoride trace in the rinse water attacks the growing chromic acid oxide.`
- `Even parts-per-million fluoride degrades coating quality.`
- `Triple cascade rinse after HF desmut is not optional -- it is mandatory.`
- `Monitor: conductivity meter confirms rinse quality but does NOT detect fluoride specifically. If processing Cu alloys through HF, periodic fluoride testing of the final rinse is recommended.`

Inter Regular 13 pt `#F0EDE8`, line height 155%.

---

### ZONE 6 -- Monitoring + Best Practices

**Section label:** `BEST PRACTICES FOR THE CRITICAL RINSE` -- Y: 26.7".

Three callout boxes in a row:

| Box | Title | Content |
|---|---|---|
| 1 (X: 0.5", W: 7.33") | `MONITOR` | `Inline conductivity meter on the final rinse tank. High reading = poor rinsing = contamination reaching the anodize bath. Track daily. Set alarm at > 100 uS/cm.` |
| 2 (X: 8.16", W: 7.33") | `DRAIN` | `Dwell parts over the desmut tank 10--15 sec before entering rinse. Reduces dragover by 50--80%. For barrel: slow extraction, 15--20 sec drain. Every drop you prevent from entering the rinse saves the anodize bath.` |
| 3 (X: 15.83", W: 7.67") | `REFRESH` | `DI water feed rate must exceed dragover volume. If the rinse conductivity keeps climbing, the refresh rate is too low. Bleed-and-feed or batch dump on schedule. Never let the rinse become a holding tank for contaminants.` |

Each: Rounded rect, H: 5.0", fill `#1E2435`, left accent `#2EC4B6`, radius 6.
Title: Barlow SemiBold 18 pt `#2EC4B6`.
Body: Inter Regular 13 pt `#F0EDE8`, line height 155%.

---

### ZONE 7 -- Footer

Standard. Title: `Rinse -- Chromic Acid Anodizing (Type I) -- Pre-Anodize`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Type I Pre-Anodize -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the "critical rinse" poster -- the one that connects pre-treatment quality to anodize bath integrity. The triple cascade diagram is a clean hero visual. The contamination limits table is the reference core -- a technician can look up any contaminant and see the limit, the source, and the effect. The fluoride dragover warning is a targeted callout that many shops overlook until they have a quality problem.

---

*Alaina -- Plating Posters Inc*
*Poster #300 -- Construction Workup v1.0*
*2026-04-26*
