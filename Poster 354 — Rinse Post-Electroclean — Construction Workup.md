---
Project: Plating Posters Inc
Poster Number: 354
Title: "Rinse -- Post-Electroclean"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Chemical Treatment Clusters -- Watson Research Brief (CT-2.5)"
Technical Source: Industry-standard rinse protocols after electrolytic cleaning. Covers rinse staging, conductivity targets for pre-acid-activation rinse, drag-out recovery, and the critical alkaline-to-acid transition.
Process Scope: Post-electroclean rinse for all substrates
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Electrocleaning
  - Rinse
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT02
---

# Poster #354 -- Construction Workup
## Rinse -- Post-Electroclean

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Poster 5 of 7 in the CT-02 cluster. This rinse poster covers the most critical rinse transition on the plating line: the alkaline-to-acid handoff. After electrocleaning, parts carry alkaline residue. The next step is acid activation. Alkaline carryover into acid baths neutralizes the acid, causes poor activation, and leads to adhesion failure. The hero visual is a counterflow cascade diagram adapted for the electroclean-to-acid-activate transition, with tighter conductivity targets than the post-soak-clean rinse (Poster 347).

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Counterflow cascade diagram with acid transition (Block B -- HERO):** Three rinse tanks with the acid activation tank visible as the destination.
2. **Conductivity targets panel (Block D):** Tighter targets than post-soak rinse, with aerospace vs. general thresholds.
3. **Drag-out recovery callout (Block E):** Same economics as soak clean rinse but with the added urgency of preventing acid neutralization.
4. **Alkaline-to-acid transition warning (Block F):** Why this rinse matters more than any other rinse on the line.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.0" / 21.0" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Poster 5 of 7 highlighted (Teal)
ZONE 3 -- COUNTERFLOW CASCADE DIAGRAM / HERO (4.2"--15.0" / ~10.8")
ZONE 4 -- CONDUCTIVITY & pH TARGETS (15.0"--21.0" / ~6.0")
ZONE 5 -- DRAG-OUT RECOVERY (21.0"--27.0" / ~6.0")
ZONE 6 -- THE ALKALINE-TO-ACID TRANSITION (27.0"--32.5" / ~5.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `THE RINSE STEP` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Post-Electroclean -- The Gateway to Acid Activation` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `This is the most critical rinse on your plating line. Alkaline residue carried into acid means poor activation, poor adhesion, and rejected parts.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Poster 5 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Parts carrying alkaline electrocleaner drag-out --> After: Parts rinsed to near-neutral, ready for acid activation`

---

### ZONE 3 -- Counterflow Cascade Diagram (HERO)

**Section label:** `RINSE DESIGN FOR THE ELECTROCLEAN-TO-ACID TRANSITION` -- Y: 4.4".

**BLOCK B -- Three-Tank Cascade + Acid Destination**

Y: 5.0" to 14.5".

**Four tanks in a row (left to right):**

| Tank | X | Label | Type | Fill Border |
|---|---|---|---|---|
| Tank 1 -- Drag-Out (Still) | 0.5" | `DRAG-OUT RINSE` `(Still)` | Recovery | `#E8A020` border |
| Tank 2 -- Running Rinse 1 | 6.5" | `RUNNING RINSE 1` `(Counterflow)` | Active | `#2EC4B6` border |
| Tank 3 -- Final Rinse | 12.5" | `FINAL RINSE` `(Fresh Water In)` | Final | `#27AE60` border |
| Tank 4 -- Acid Activate (Destination) | 18.5" | `ACID ACTIVATE` `(Next Step)` | Destination | `#E8A020` border, dashed |

Tanks 1-3: Rounded rect W: 5.5", H: 5.5", fill `#252B3D`, border 2 pt.
Tank 4: Rounded rect W: 5.0", H: 5.5", fill `#252B3D`, border 2 pt dashed `#E8A020`.

**Part movement arrows (top, left to right):**
- `PARTS MOVE THIS WAY -->` Barlow SemiBold 16 pt `#F0EDE8`

**Water flow arrows (bottom, right to left):**
- `<-- CLEAN WATER FLOWS THIS WAY` Barlow SemiBold 16 pt `#2EC4B6`

**Inside each tank:**

*Tank 1 -- Drag-Out:*
- `HIGH alkaline concentration` JetBrains Mono 13 pt `#E8A020`
- `Captures 50-70% of electrocleaner drag-out` Inter Regular 12 pt
- `Return to electrocleaner periodically` Inter Medium 12 pt `#E8A020`

*Tank 2 -- Running Rinse 1:*
- `MODERATE dilution` JetBrains Mono 13 pt `#2EC4B6`
- `Counterflow from Tank 3` Inter Regular 12 pt
- `pH < 10` JetBrains Mono 14 pt

*Tank 3 -- Final Rinse:*
- `LOW -- near clean water` JetBrains Mono 13 pt `#27AE60`
- `Fresh water inlet here` Inter Regular 12 pt
- `pH < 9.0` JetBrains Mono 14 pt `#27AE60`
- `Conductivity < 200 uS/cm` JetBrains Mono 13 pt `#27AE60`
- `Aerospace: < 50 uS/cm` JetBrains Mono 12 pt `#E8A020`

*Tank 4 -- Acid Activate (dashed border = destination, not part of rinse):*
- `ACID ACTIVATION` Barlow SemiBold 16 pt `#E8A020`
- `Dilute HCl or H2SO4` JetBrains Mono 13 pt
- `Any alkaline carryover neutralizes acid` Inter Regular 12 pt `#E05C5C`
- `= poor activation = adhesion failure` Inter Medium 12 pt `#E05C5C`

**Bottom callout (Y: 13.0"):**
- Rounded rect W: 23.0", H: 1.2", fill `#E05C5C` at 10%, border 1 pt `#E05C5C`
- Title: `WHY THIS RINSE IS DIFFERENT` Barlow SemiBold 14 pt `#E05C5C`
- Text: `The post-soak-clean rinse feeds into another alkaline tank (electrocleaner). A little alkaline drag-out is tolerable. The post-electroclean rinse feeds into ACID. Any alkaline residue neutralizes the acid, raises pH, and prevents activation. This is the transition that matters most.` Inter Regular 13 pt `#F0EDE8`

---

### ZONE 4 -- Conductivity & pH Targets

**Section label:** `MEASURING RINSE QUALITY -- TIGHTER TARGETS HERE` -- Y: 15.2".

**BLOCK D -- Two-Column Monitoring Panel (Y: 15.8" to 20.8")**

**Left -- General Plating (X: 0.5", W: 11.0"):**

Rounded rect H: 4.5", fill `#1E2435`, left accent 0.06" `#2EC4B6`.

Title: `GENERAL PLATING` Barlow SemiBold 18 pt `#2EC4B6`

- `Final rinse pH: < 9.0` JetBrains Mono 16 pt `#27AE60`
- `Conductivity: < 200 uS/cm` JetBrains Mono 14 pt `#27AE60`
- `Water type: city water acceptable` Inter Regular 13 pt `#F0EDE8`
- `Adequate for decorative Ni/Cr, zinc plating, copper` Inter Regular 12 pt `#F0EDE8` at 70%

**Right -- Aerospace / Critical (X: 12.0", W: 11.5"):**

Rounded rect H: 4.5", fill `#1E2435`, left accent 0.06" `#E8A020`.

Title: `AEROSPACE / CRITICAL` Barlow SemiBold 18 pt `#E8A020`

- `Final rinse pH: < 8.5` JetBrains Mono 16 pt `#E8A020`
- `Conductivity: < 50 uS/cm` JetBrains Mono 14 pt `#E8A020`
- `Water type: DI water preferred for final rinse` Inter Regular 13 pt `#F0EDE8`
- `Required for gold, silver, electronics, aerospace` Inter Regular 12 pt `#F0EDE8` at 70%

---

### ZONE 5 -- Drag-Out Recovery

**Section label:** `DRAG-OUT RECOVERY -- SAME PRINCIPLE, HIGHER STAKES` -- Y: 21.2".

**BLOCK E -- Economics Panel (Y: 21.8" to 26.8")**

Rounded rect, full width, H: 4.5", fill `#1E2435`.

**Three-column layout inside:**

| Column | Content |
|---|---|
| Left (W: 7.0") | `WHY RECOVER DRAG-OUT?` Barlow SemiBold 16 pt `#E8A020`. Body: `Electrocleaner chemistry is expensive -- NaOH + phosphate + chelator. Every part that leaves the tank carries solution with it. A still rinse captures 50-70% of that drag-out for return.` |
| Center (W: 7.0") | `SLOW WITHDRAWAL` Barlow SemiBold 16 pt `#2EC4B6`. Body: `5-10 second drain time over the electrocleaner tank before transferring to rinse. This single habit reduces chemical consumption by 20-30% with zero capital cost.` |
| Right (W: 7.0") | `AIR BLOW-OFF` Barlow SemiBold 16 pt `#27AE60`. Body: `Compressed air blow-off between electrocleaner and rinse removes clingy drag-out from blind holes, recesses, and barrel loads. Reduces rinse loading significantly. Common on automatic lines.` |

---

### ZONE 6 -- The Alkaline-to-Acid Transition

**Section label:** `THE ALKALINE-TO-ACID HANDOFF -- DO NOT SKIP THIS` -- Y: 27.2".

**BLOCK F -- Full-Width Warning Panel (Y: 27.8" to 32.3")**

Rounded rect W: 23.0", H: 4.0", fill `#E05C5C` at 10%, border 2 pt `#E05C5C`, radius 8.

**Two-column interior:**

**Left -- What Happens When Rinse Fails (W: 11.0"):**
- Title: `WHEN ALKALINE MEETS ACID` Barlow SemiBold 18 pt `#E05C5C`
- Body: Inter Regular 14 pt `#F0EDE8`:
```
Alkaline drag-out enters acid activation tank:
  - Neutralizes acid (raises pH)
  - Reduces acid strength
  - Creates uneven activation
  - Parts have spotty acid contact
  - Result: poor adhesion under plate

This failure mode is INVISIBLE at the
electrocleaner -- it shows up as blisters,
peelers, or skip plate AFTER plating.
```

**Right -- Prevention (W: 11.0"):**
- Title: `PREVENTION` Barlow SemiBold 18 pt `#27AE60`
- Body:
```
1. Double or triple counterflow rinse
2. Monitor final rinse conductivity daily
3. Slow withdrawal from electrocleaner
4. Use drag-out rinse before flowing rinse
5. If conductivity rises above target,
   increase water flow before it becomes
   an adhesion problem downstream

The rinse is cheap. The rejects are not.
```

---

### ZONE 7 -- Footer

Standard. Title: `Rinse -- Post-Electroclean`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; Metal Finishing Guidebook. Conductivity targets are guidelines -- critical applications (aerospace, electronics) may require tighter control. Consult your process specification.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Post-Electroclean -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster is structurally similar to the CT-01 rinse poster (347) but with two critical differences: tighter conductivity targets and the alkaline-to-acid transition warning. The dashed-border acid activate tank in the cascade diagram is a deliberate visual choice -- it shows the destination without being part of the rinse system itself. The full-width warning panel in Zone 6 is more aggressive than a typical callout because this failure mode is the most common source of adhesion defects on plating lines, and it is almost always traced back to inadequate rinsing.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #354 -- Construction Workup v1.0*
*2026-04-26*
