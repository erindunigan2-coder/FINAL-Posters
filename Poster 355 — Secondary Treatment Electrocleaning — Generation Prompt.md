---
Project: Plating Posters Inc
Poster Number: 355
Title: "Secondary Treatment -- Electrocleaning (HE Bake & Acid Activation)"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-28T00:00:00
Source: Poster 355 -- Secondary Treatment Electrocleaning -- Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - Electrocleaning
  - SecondaryTreatment
  - HydrogenEmbrittlement
  - ChemicalTreatment
  - ClusterCT02
  - v1
---

# Claude Chat Generation Prompt -- Poster #355
## Secondary Treatment -- Electrocleaning (HE Bake & Acid Activation)
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-28). Hydrogen embrittlement decision tree + acid activation handoff. Catastrophic failure prevention.*

---

> **IMPORTANT:** Generate as SVG or HTML visual artifact. 24 x 36" portrait. Dark edition first.

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E`, locked palette, 0.5" safe zone. iOS 18 Liquid Glass aesthetic.

---

## Phase 2 -- Header

### Step 1 -- `SECONDARY TREATMENT` -- `80` pt `#F0EDE8`. Y: **0.5"**.
### Step 2 -- `After Electrocleaning -- Hydrogen Embrittlement and the Path to Acid Activate` -- `30` pt `#E8A020`. Y: **1.4"**.
### Step 3 -- `Cathodic cleaning saves time. It can also destroy parts. Know when to bake and when to worry.` -- `20` pt at 65%. Y: **2.1"**.

---

## Phase 3 -- Orientation Strip

Seven boxes. **Box 6 highlighted** (fill `#E8A020`, text `#1A1F2E`). Others dimmed.

Below: `Conditional step -- HE bake applies only when cathodic cleaning was used on high-strength steel`

---

## Phase 4 -- HE Decision Flowchart (HERO)

Y: 4.2" to 14.0". Section label: `DOES YOUR PART NEED A HYDROGEN EMBRITTLEMENT BAKE?`

Entry: `PARTS ELECTROCLEANED` (teal glass box).

**Decision 1:** `WAS CATHODIC MODE USED? (even briefly)`
- NO -> `No HE risk. Proceed to rinse and acid activate.` (`#27AE60`)
- YES -> Decision 2

**Decision 2:** `IS SUBSTRATE HIGH-STRENGTH STEEL? (Rc >= 39 or tensile >= 180 ksi)`
- NO -> `Low HE risk. Proceed normally. Note cathodic time in process record.` (`#27AE60`)
- YES -> Decision 3

**Decision 3:** `BAKE REQUIRED per ASTM B850` (coral border diamond)
- Bake box: `375 +/- 25 F (190 +/- 14 C) | 4-24 hours | Within 4 hours of cathodic exposure` (coral-tinted glass, JetBrains Mono 14 pt)
- `See Zone 4 for time by tensile strength`

---

## Phase 5 -- Bake Specification Table

Y: 14.0" to 20.5". Section label: `ASTM B850 BAKE SCHEDULE -- BY TENSILE STRENGTH`.

Glass table with coral-tinted header:

| Tensile Strength | Hardness (Rc) | Bake Temp | Bake Time | Timing |
|---|---|---|---|---|
| 150-180 ksi | 39-43 | 375 +/- 25 F | 4 hours minimum | Within 4 hours |
| 180-220 ksi | 43-48 | 375 +/- 25 F | 8 hours minimum | Within 4 hours |
| > 220 ksi | > 48 | 375 +/- 25 F | 12-24 hours | Within 4 hours |
| Ultra-high (>260 ksi) | > 52 | Per engineering spec | 24 hours or per spec | ASAP -- within 2 hours |

Callout below: `THE 4-HOUR CLOCK STARTS when the part exits the cathodic process. Bake within this window or hydrogen becomes permanently trapped in the lattice. Late baking is better than no baking -- but on-time baking is the specification.`

---

## Phase 6 -- Acid Activation Handoff

Y: 20.5" to 27.0". Section label: `THE NEXT STEP -- ACID ACTIVATION`.

Two glass cards.

**Left -- What Acid Activation Does** (amber-accented):
- Removes remaining oxide film / Creates chemically active surface / Promotes adhesion
- Typical acids: HCl 10-25% v/v (most common) / H2SO4 5-10% v/v / HF blends for stainless (see CT-04)
- Time: 15-60 seconds (just a dip)

**Right -- The Complete Sequence** (emerald-accented):
JetBrains Mono flow:
`Soak Clean (CT-01)` -> `Electroclean (CT-02)` -> `Rinse` -> `Acid Activate` -> `Rinse` -> `PLATE`
Process names color-coded (Teal, Amber, Emerald).

---

## Phase 7 -- Cathodic Mode Consequences

Y: 27.0" to 32.5". Section label: `WHY CATHODIC MODE CREATES THE PROBLEM`.

Full-width glass card with coral top accent, three columns:

**The Reaction** (`#E05C5C`):
`2H2O + 2e- -> H2 + 2OH-`
Most H2 bubbles off. Some atomic H absorbs into steel lattice BEFORE forming H2 bubbles.

**The Consequence** (`#E8A020`):
Atomic hydrogen migrates to grain boundaries and stress concentrators. At high-stress points, causes delayed brittle fracture -- often hours or days after plating. Catastrophic in fasteners, springs, landing gear.

**The Fix** (`#27AE60`):
1. Use ANODIC whenever possible
2. If cathodic necessary, minimize time
3. Bake per ASTM B850 within 4 hours
4. Document cathodic exposure time
5. For Rc >= 39: no cathodic unless engineering-approved with bake

---

## Phase 8 -- Footer

Standard. Title: `Secondary Treatment -- Electrocleaning`. Version `v1.0 -- 2026`.
Disclaimer: `Source: ASTM B850 (hydrogen embrittlement relief); AMS 2759/9; general industry knowledge. Bake requirements vary by specification. Aerospace requires documentation of all hydrogen-generating steps.`

---

## Phase 9 -- Review

- [ ] Headline `SECONDARY TREATMENT` 80 pt
- [ ] HE decision flowchart with 3 diamonds
- [ ] Bake specification: `375 +/- 25 F` / `Within 4 hours`
- [ ] Four-row ASTM B850 bake schedule table
- [ ] 4-hour clock callout in coral
- [ ] Acid activation handoff with complete sequence flow
- [ ] Three-column cathodic consequences panel
- [ ] Electrochemical reaction equation
- [ ] ASTM B850 and AMS references

---

## Phase 10 -- Light Remap & Export

Standard remap. Bake box coral tint: verify on light. Decision diamonds: verify amber on light background.

Six files: `Secondary Treatment Electrocleaning -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-28 | Initial. |
