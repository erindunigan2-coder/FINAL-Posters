---
Project: Plating Posters Inc
Poster Number: 355
Title: "Secondary Treatment -- Electrocleaning (HE Bake & Acid Activation)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Chemical Treatment Clusters -- Watson Research Brief (CT-2.6)"
Technical Source: Industry-standard secondary treatments after electrocleaning. Covers hydrogen embrittlement relief baking per ASTM B850, the electroclean-to-acid-activate transition, and cathodic vs. anodic mode consequences.
Process Scope: Secondary treatment considerations after electrocleaning -- HE bake and acid activation handoff
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Electrocleaning
  - SecondaryTreatment
  - HydrogenEmbrittlement
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT02
---

# Poster #355 -- Construction Workup
## Secondary Treatment -- Electrocleaning (HE Bake & Acid Activation)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Poster 6 of 7 in the CT-02 cluster. This poster covers the "what comes next" after electrocleaning -- specifically hydrogen embrittlement relief baking for high-strength steel and the acid activation step that follows rinsing. The hero visual is a hydrogen embrittlement decision flowchart: "Does your part need a bake?" The acid activation callout bridges CT-02 into the acid pickle clusters (CT-03/CT-04). This is the most critical safety-adjacent poster in the cluster because hydrogen embrittlement can cause catastrophic part failure.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **HE decision flowchart (Block B -- HERO):** "Is baking required?" decision tree based on substrate hardness and cathodic exposure.
2. **Bake specification table (Block D):** ASTM B850 parameters by tensile strength category.
3. **Acid activation handoff (Block E):** What acid activation does and why it follows electrocleaning.
4. **Cathodic mode consequences panel (Block F):** Why cathodic mode creates the HE problem.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.0" / 20.5" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Poster 6 of 7 highlighted (Amber)
ZONE 3 -- HE DECISION FLOWCHART / HERO (4.2"--14.0" / ~9.8")
ZONE 4 -- BAKE SPECIFICATION TABLE (14.0"--20.5" / ~6.5")
ZONE 5 -- ACID ACTIVATION HANDOFF (20.5"--27.0" / ~6.5")
ZONE 6 -- CATHODIC MODE CONSEQUENCES (27.0"--32.5" / ~5.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `SECONDARY TREATMENT` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `After Electrocleaning -- Hydrogen Embrittlement and the Path to Acid Activate` -- 30 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Cathodic cleaning saves time. It can also destroy parts. Know when to bake and when to worry.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Poster 6 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Conditional step -- HE bake applies only when cathodic cleaning was used on high-strength steel`

---

### ZONE 3 -- HE Decision Flowchart (HERO)

**Section label:** `DOES YOUR PART NEED A HYDROGEN EMBRITTLEMENT BAKE?` -- Y: 4.4".

**BLOCK B -- Decision Tree (Y: 5.0" to 13.5")**

Entry point (top center):
- Rounded rect W: 8.0", H: 1.0", fill `#2EC4B6` at 20%, border 2 pt `#2EC4B6`
- Text: `PARTS ELECTROCLEANED` Barlow SemiBold 16 pt `#2EC4B6`

Decision 1 (Y: 6.5"):
- Diamond W: 6.0", H: 1.5", fill `#E8A020` at 20%, border 1 pt `#E8A020`
- Text: `WAS CATHODIC MODE USED?` `(even briefly)` Barlow SemiBold 14 pt `#E8A020`
- NO -> `No HE risk from electrocleaning. Proceed to rinse and acid activate.` (right, `#27AE60`, destination box)
- YES -> Decision 2 (down)

Decision 2 (Y: 8.5"):
- Diamond same style
- Text: `IS SUBSTRATE HIGH-STRENGTH STEEL?` `(Rc >= 39 or tensile >= 180 ksi)`
- NO -> `Low HE risk. Proceed normally. Note cathodic time in process record.` (right, `#27AE60`)
- YES -> Decision 3 (down)

Decision 3 (Y: 10.5"):
- Diamond same style, border `#E05C5C`
- Text: `BAKE REQUIRED` `per ASTM B850`
- Arrow down to bake specification box:

Bake box (Y: 12.0"):
- Rounded rect W: 12.0", H: 1.5", fill `#E05C5C` at 15%, border 2 pt `#E05C5C`
- Text: `375 +/- 25 F (190 +/- 14 C) | 4-24 hours | Within 4 hours of cathodic exposure` JetBrains Mono 14 pt `#E05C5C`
- Sub-text: `See Zone 4 for time by tensile strength` Inter Medium 12 pt `#F0EDE8`

Destination boxes: Rounded rect W: 7.0", H: 1.2", fill `#1E2435`, left accent 0.06" in label color.

---

### ZONE 4 -- Bake Specification Table

**Section label:** `ASTM B850 BAKE SCHEDULE -- BY TENSILE STRENGTH` -- Y: 14.2".

**BLOCK D -- Bake Table (Y: 14.8" to 20.3")**

Column widths (23.0" total):
- Tensile Strength (6.0") | Hardness (4.0") | Bake Temp (5.0") | Bake Time (4.0") | Timing (4.0")

Header row: fill `#E05C5C` at 25%, H: 0.5". Barlow SemiBold 14 pt.

| Tensile Strength | Hardness (Rc) | Bake Temp | Bake Time | Timing |
|---|---|---|---|---|
| 150-180 ksi | 39-43 | 375 +/- 25 F | 4 hours minimum | Within 4 hours |
| 180-220 ksi | 43-48 | 375 +/- 25 F | 8 hours minimum | Within 4 hours |
| > 220 ksi | > 48 | 375 +/- 25 F | 12-24 hours | Within 4 hours |
| Ultra-high (>260 ksi) | > 52 | Per engineering spec | 24 hours or per spec | ASAP -- within 2 hours |

Data: JetBrains Mono 13 pt `#F0EDE8`. "Within 4 hours" and timing: Inter Medium 13 pt `#E05C5C`.

**Callout below table (Y: 19.5"):**
- Rounded rect W: 23.0", H: 0.7", fill `#E05C5C` at 10%, border 1 pt `#E05C5C`
- Text: `THE 4-HOUR CLOCK STARTS when the part exits the cathodic process. Bake within this window or hydrogen becomes permanently trapped in the lattice. Late baking is better than no baking -- but on-time baking is the specification.` Inter Medium 13 pt `#E05C5C`

---

### ZONE 5 -- Acid Activation Handoff

**Section label:** `THE NEXT STEP -- ACID ACTIVATION` -- Y: 20.7".

**BLOCK E -- Two-Column Panel (Y: 21.3" to 26.8")**

**Left -- What Acid Activation Does (X: 0.5", W: 11.0"):**

Rounded rect H: 5.0", fill `#1E2435`, left accent 0.06" `#E8A020`.

Title: `ACID ACTIVATION` Barlow SemiBold 18 pt `#E8A020`
Subtitle: `Also Called: Acid Dip, Acid Pickle, Acid Strike` Inter Regular 14 pt `#F0EDE8` at 60%

Body: Inter Regular 14 pt `#F0EDE8`, line height 155%:
```
After rinsing, parts enter a dilute acid bath:
  - Removes any remaining oxide film
  - Creates a chemically active surface
  - Promotes adhesion of the plated deposit

Typical acids:
  - HCl 10-25% by volume (most common)
  - H2SO4 5-10% by volume
  - HF blends for stainless steel (see CT-04)

Time: 15-60 seconds (just a dip -- not a soak)
```

**Right -- Why It Matters (X: 12.0", W: 11.5"):**

Rounded rect H: 5.0", fill `#1E2435`, left accent 0.06" `#27AE60`.

Title: `THE COMPLETE SEQUENCE` Barlow SemiBold 18 pt `#27AE60`

Body:
```
Soak Clean (CT-01, Posters 343-349)
  removes bulk soil
      |
Electroclean (CT-02, Posters 350-356)
  removes trace contamination
      |
Rinse (this cluster, Poster 354)
  removes all alkaline residue
      |
Acid Activate
  removes oxide, creates active surface
      |
Rinse
  removes acid residue
      |
PLATE
```

Font: JetBrains Mono 12 pt `#F0EDE8`, with arrows in `#3A4055`. Process names in accent colors (Teal, Amber, Emerald).

---

### ZONE 6 -- Cathodic Mode Consequences

**Section label:** `WHY CATHODIC MODE CREATES THE PROBLEM` -- Y: 27.2".

**BLOCK F -- Full-Width Panel (Y: 27.8" to 32.3")**

Rounded rect W: 23.0", H: 4.0", fill `#1E2435`, top accent 4 pt `#E05C5C`.

**Three-column interior:**

**Left -- The Chemistry (W: 7.0"):**
- Title: `THE REACTION` Barlow SemiBold 16 pt `#E05C5C`
- Body: JetBrains Mono 13 pt `#F0EDE8`:
```
2H2O + 2e- -> H2 + 2OH-

Most H2 bubbles off as gas.
Some atomic hydrogen (H)
absorbs into the steel lattice
BEFORE it forms H2 bubbles.
```

**Center -- The Damage (W: 7.0"):**
- Title: `THE CONSEQUENCE` Barlow SemiBold 16 pt `#E8A020`
- Body: Inter Regular 13 pt `#F0EDE8`:
```
Atomic hydrogen migrates to
grain boundaries and stress
concentrators.

At high-stress points, hydrogen
causes delayed brittle fracture --
often hours or days after plating.

This is catastrophic in fasteners,
springs, and landing gear.
```

**Right -- The Prevention (W: 7.0"):**
- Title: `THE FIX` Barlow SemiBold 16 pt `#27AE60`
- Body:
```
1. Use ANODIC mode whenever possible
2. If cathodic is necessary, minimize time
3. Bake per ASTM B850 within 4 hours
4. Document cathodic exposure time
5. For Rc >= 39: no cathodic at all
   unless engineering-approved with bake
```

---

### ZONE 7 -- Footer

Standard. Title: `Secondary Treatment -- Electrocleaning`. Version `v1.0 -- 2026`.
Disclaimer: `Source: ASTM B850 (hydrogen embrittlement relief); AMS 2759/9; general industry knowledge. Bake requirements vary by specification and application. Aerospace parts require documentation of all hydrogen-generating process steps. Consult your engineering specification.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Secondary Treatment Electrocleaning -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Hydrogen embrittlement is the scariest topic in this entire cluster -- parts that look perfect can fail catastrophically days or weeks after plating. The decision flowchart hero forces the viewer to work through the logic: Was cathodic used? Is the steel high-strength? If yes to both, BAKE. The bake specification table is ASTM B850 data presented in a format a plating shop can follow directly. The acid activation handoff section bridges this cluster into the next process step and cross-references CT-03/CT-04. The cathodic consequences panel is the "why" behind the bake requirement -- understanding the mechanism prevents shortcuts.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #355 -- Construction Workup v1.0*
*2026-04-26*
