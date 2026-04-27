---
Project: Plating Posters Inc
Poster Number: 27
Title: "Wastewater Treatment Fundamentals — From Rinse Tank to Discharge"
Document Type: Construction Workup
Status: v1.0 — Ready for Elara
Created: 2026-04-24T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - General industry knowledge (metal finishing wastewater treatment, EPA categorical standards, hydroxide precipitation)
Technical Source: General industry knowledge — metal hydroxide precipitation, pH adjustment, flocculation, clarification, sludge handling, EPA 40 CFR Part 433 categorical standards for metal finishing, cyanide destruction chemistry, hexavalent chrome reduction. NASF/AESF environmental compliance references.
Watson Flags: THREE OPEN — (1) Confirm current EPA 40 CFR Part 433 daily maximum discharge limits for key metals (Cu, Ni, Cr, Zn, Cd, Pb, Ag) — these are federal categorical pretreatment standards but local POTWs may be stricter. (2) Verify the optimal precipitation pH ranges for each metal hydroxide (Cu ~8.5-9.5, Ni ~9.0-10.0, Cr³⁺ ~7.5-8.5, Zn ~8.5-9.5, etc.) against current technical references. (3) Confirm alkaline chlorination cyanide destruction two-stage chemistry (CN⁻ to CNO⁻ at pH >10, then CNO⁻ to CO₂ + N₂ at pH 8.0-8.5). All three are foundational to the poster's accuracy — flag as important.
Tyler Flags: NONE — wastewater treatment is outside Tyler's lab chemistry scope.
Process Scope: Wastewater treatment systems for metal finishing operations (universal — applies to every plating shop that discharges wastewater)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow: Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - WastewaterTreatment
  - EnvironmentalCompliance
  - HydroxidePrecipitation
  - CyanideDestruction
  - ConstructionWorkup
---

# Poster #27 — Construction Workup
## Wastewater Treatment Fundamentals — From Rinse Tank to Discharge

*Alaina — Plating Posters Inc Creative Lead*
*v1.0 — 2026-04-24*

This document is the construction workup for Poster #27. Wastewater treatment is the least glamorous but most legally consequential process in any plating shop. Permit violations carry fines, shutdowns, and criminal liability. This poster puts the fundamentals on the wall where they belong — a clear, visual reference that makes the treatment process understandable and the discharge limits visible.

> **Workflow note:** Poster generation uses claude.ai chat (SVG/HTML visual artifacts). These specs feed the Claude Chat Generation Prompt engineered by Elara.

**What makes this poster valuable:** Every plating shop generates regulated wastewater. Many shops — especially smaller ones — rely on a single operator who learned the treatment system by trial and error. This poster provides the structured reference that operator never got in training. It is also a visible compliance artifact: hanging it on the treatment room wall demonstrates a culture of environmental responsibility.

**Who it's for:** Wastewater treatment operators, environmental compliance managers, plant managers, and shop owners. The operator gets a daily reference for chemical treatment steps; the manager gets a wall-visible reminder that discharge limits are non-negotiable.

---

## Part 1 — Workflow Orientation

### Design Capabilities for This Poster

- Text boxes with precise font, size, weight, color, and spacing control
- Solid-color rectangles and rounded rectangles for callout boxes, table rows, and process flow steps
- Simple shapes for treatment system flow diagram (tanks = rectangles, flow arrows = triangles/lines, mixers = small circle on a line)
- Color fills set to exact hex values
- Background page color set to exact hex
- Export at print-quality PDF (300 DPI equivalent via print export)

### Limitations to Flag for Elara

1. **Treatment system flow diagram (Block B — HERO):** A horizontal/L-shaped process flow showing wastewater moving through treatment stages (equalization tank -> pH adjustment -> flocculation -> clarification -> filter press -> discharge). Each stage is a labeled rectangle connected by flow arrows. Simple schematic construction — same approach as Poster #1's flowchart but larger and more detailed.

2. **pH-solubility relationship visual (Block D):** Conceptual representation of the "minimum solubility" concept — a simplified graph-like shape showing that each metal has an optimal precipitation pH. This can be built as a series of dashed vertical lines at different pH positions on a horizontal bar, each labeled with a metal name. Not a true plotted curve — a schematic reference.

3. **4 pt left-border accents.** Standard.

4. **Print size — 24x36".** Standard.

---

## Part 2 — Document Setup Instructions (for Elara's prompt)

### Step 1-3 — Standard (24x36", `#1A1F2E` background, standard font stack)

### Step 4 — Color palette

| Color Name | Hex | Primary Use |
|---|---|---|
| Gunmetal Dark | `#1A1F2E` | Background (Dark edition) |
| Warm White | `#F0EDE8` | All primary text (Dark edition) |
| Amber | `#E8A020` | pH values, caution indicators, chrome reduction stage |
| Teal | `#2EC4B6` | Flow indicators, treatment stage accents, discharge parameters |
| Emerald | `#27AE60` | Compliant discharge indicators, best practice callouts |
| Coral | `#E05C5C` | Discharge limit violations, regulatory warnings, cyanide hazard |
| Mid Slate | `#3A4055` | Table headers, tank outlines, divider lines |
| Deep Navy | `#0D1020` | Footer band background |
| Dark Callout | `#1E2435` | Callout box fills, treatment stage backgrounds |
| Alt Row | `#252B3D` | Alternating table rows |
| Bright Silver | `#C8D0D8` | Pipe/flow connections, neutral elements |

### Step 5 — Ruler guides

**Horizontal guides:**
- 0.5" / 3.0" / 12.0" / 16.5" / 22.5" / 27.5" / 32.5" / 35.5"

---

## Part 3 — Layout Zones and Build Order

```
ZONE 1 — HEADER BAND (0"–3.0")
  Block A: Headline + subheading + compliance callout

ZONE 2 — TREATMENT SYSTEM FLOW DIAGRAM (3.0"–12.0" / ~9.0" tall)
  Block B: Process flow schematic (HERO)
  Block C: Stage-by-stage key chemistry notes

ZONE 3 — THE pH-PRECIPITATION SWEET SPOT (12.0"–16.5" / ~4.5" tall)
  Block D: Metal hydroxide precipitation pH reference
  Block DD: Why pH matters callout

ZONE 4 — SPECIAL WASTE STREAMS (16.5"–22.5" / ~6.0" tall)
  Block E: Cyanide destruction procedure (left half)
  Block F: Hexavalent chrome reduction procedure (right half)

ZONE 5 — DISCHARGE LIMITS (22.5"–27.5" / ~5.0" tall)
  Block G: EPA categorical discharge limits table
  Block GG: Local limits warning callout

ZONE 6 — OPERATOR BEST PRACTICES (27.5"–32.5" / ~5.0" tall)
  Block H: Daily checklist (left half)
  Block HH: Common mistakes (right half)

ZONE 7 — FOOTER BAND (32.5"–36.0" / ~3.5" tall)
  Block J: Standard footer
```

---

## Part 4 — Zone-by-Zone Build Specifications

### ZONE 1 — Header Band

**BLOCK A — Headline**

- Font: Barlow Condensed ExtraBold, 72 pt, `#F0EDE8`
- Text (all caps):

> WASTEWATER TREATMENT FUNDAMENTALS

**BLOCK A — Subheading**

- Font: Barlow SemiBold, 34 pt, `#2EC4B6`
- Text:

> From Rinse Tank to Discharge — Every Drop Is Regulated

**BLOCK A — Compliance Callout**

- Element type: Rounded rectangle
- Width: 23.0". Height: 0.8"
- Fill: `#E05C5C` at 12%
- Border: 2 pt, `#E05C5C`
- Text (centered): Barlow Condensed ExtraBold, 22 pt, `#E05C5C`

> PERMIT VIOLATIONS CARRY FINES UP TO $50,000/DAY AND CRIMINAL LIABILITY — KNOW YOUR LIMITS

---

### ZONE 2 — Treatment System Flow Diagram (HERO)

**Dimensions:** Y: 3.0" to 12.0" (~9.0" tall).

---

**Section label:**
- Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text:

> THE TREATMENT PROCESS — STEP BY STEP

---

**BLOCK B — Process Flow Schematic**

Y: 3.8" to 9.5" (~5.7" tall).

A process flow built from labeled rectangles (tanks) connected by arrows. Layout in two rows for readability:

**Row 1 (Y: 3.8", left to right):**

| Stage | Width | Fill | Border | Label |
|---|---|---|---|---|
| 1. Collection / Equalization | 4.5" x 2.5" | `#1E2435` | 2 pt `#3A4055` | `EQUALIZATION TANK` |
| Arrow | -> | | | |
| 2. pH Adjustment | 4.5" x 2.5" | `#1E2435` | 2 pt `#E8A020` | `pH ADJUSTMENT` |
| Arrow | -> | | | |
| 3. Chemical Addition | 4.5" x 2.5" | `#1E2435` | 2 pt `#2EC4B6` | `COAGULANT / FLOCCULANT` |
| Arrow (down) | | | | |

**Row 2 (Y: 7.0", right to left — forms an L or U shape):**

| Stage | Width | Fill | Border | Label |
|---|---|---|---|---|
| 4. Clarifier / Settling | 5.0" x 2.5" | `#1E2435` | 2 pt `#27AE60` | `CLARIFIER` |
| Arrow | <- | | | |
| 5. Filter Press | 4.0" x 2.5" | `#1E2435` | 2 pt `#E8A020` | `FILTER PRESS` |
| Arrow | -> | | | |
| 6. Final pH Check | 3.5" x 2.5" | `#1E2435` | 2 pt `#27AE60` | `FINAL pH CHECK` |
| Arrow | -> | | | |
| 7. Discharge | 3.0" x 2.5" | `#27AE60` at 20% | 2 pt `#27AE60` | `DISCHARGE` |

Inside each tank rectangle, brief description:
- Font: Inter Regular, 13 pt, `#F0EDE8`

Stage 1: `Mix all waste streams. Equalize flow rate and chemistry.`
Stage 2: `Raise pH with NaOH or Ca(OH)₂ to precipitation target.`
Stage 3: `Add polymer flocculant. Gentle mixing to form settable floc.`
Stage 4: `Gravity separation. Clear water rises; sludge settles.`
Stage 5: `Dewater sludge for disposal. Filtrate returns to system.`
Stage 6: `Verify pH 6.0-9.0 before release.`
Stage 7: `To POTW or direct discharge per permit.`

Sludge output from Stage 5:
- Arrow pointing down from filter press
- Label: `SLUDGE TO HAZARDOUS WASTE DISPOSAL` — Inter Medium, 13 pt, `#E05C5C`
- Small hazard badge: Rectangle, `#E05C5C`, with `HAZ` text

Flow arrows: Triangle elements, `#C8D0D8`, connecting stages. Stroke: 2 pt, `#C8D0D8`.

---

**BLOCK C — Stage Chemistry Notes** (below flow diagram)

Y: 9.8" to 11.8" (~2.0" tall). Three compact callout cards:

| Card | X | Width | Accent | Title | Content |
|---|---|---|---|---|---|
| 1 | 0.5" | 7.33" | `#E8A020` | `pH ADJUSTMENT` | `NaOH (caustic soda) or Ca(OH)₂ (lime). Caustic = cleaner sludge, higher chemical cost. Lime = cheaper, more sludge volume. Most shops use 25-50% NaOH solution.` |
| 2 | 8.0" | 7.33" | `#2EC4B6` | `FLOCCULATION` | `Anionic polymer (most common). Dose: 1-5 mg/L typical. Overdosing breaks floc apart. Jar test to optimize dose. Mix gently — high shear destroys floc.` |
| 3 | 15.5" | 7.5" | `#27AE60` | `CLARIFICATION` | `Retention time: 30-60 min minimum. Sludge blanket must not reach weir. Lamellar plate clarifiers reduce footprint. Effluent turbidity < 25 NTU target.` |

Card fill: `#1E2435`. Left-border accent in respective color. Title: Barlow SemiBold, 16 pt. Body: Inter Regular, 13 pt, `#F0EDE8`.

---

### ZONE 3 — The pH-Precipitation Sweet Spot

**Dimensions:** Y: 12.0" to 16.5" (~4.5" tall).

---

**Section label:**
- Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text:

> THE pH SWEET SPOT — WHERE METALS FALL OUT OF SOLUTION

---

**BLOCK D — Metal Hydroxide Precipitation pH Reference**

Y: 12.8" to 15.5" (~2.7" tall).

A horizontal bar representing pH scale from 6.0 to 11.0, with colored zones showing optimal precipitation pH for each metal:

Overall bar:
- Width: 23.0". Height: 0.6". Fill: `#252B3D`. Corner radius: 4 pt.
- pH labels along bottom edge: `6.0` | `7.0` | `8.0` | `9.0` | `10.0` | `11.0` — JetBrains Mono Regular, 12 pt, `#F0EDE8`

Metal precipitation zones (horizontal colored bars stacked above the pH scale):

| Metal | Color | pH Range | Optimal |
|---|---|---|---|
| Cr³⁺ (Chromium) | `#2EC4B6` | 7.5–8.5 | 8.0 |
| Cu²⁺ (Copper) | `#E8A020` | 8.0–10.0 | 8.5 |
| Zn²⁺ (Zinc) | `#C8D0D8` | 8.0–9.5 | 9.0 |
| Ni²⁺ (Nickel) | `#27AE60` | 9.0–10.5 | 9.5 |
| Cd²⁺ (Cadmium) | `#E05C5C` | 9.0–11.0 | 10.0 |
| Fe²⁺/³⁺ (Iron) | `#E8A020` at 60% | 7.0–9.0 | 8.0 |

Each metal zone: Horizontal rectangle at 25% opacity of its color, positioned on the pH scale at the correct range. Metal label at the left edge. Optimal pH marked with a small vertical line or dot in full color.

Height of each zone bar: 0.25". Stacked with 0.05" gaps.

---

**BLOCK DD — Why pH Matters Callout**

Y: 15.7" to 16.3"

- Centered. Width: 18.0". Fill: `#252B3D`. Corner radius: 4 pt. Height: 0.5".
- Text: JetBrains Mono Regular, 14 pt, `#E8A020`

> Mixed metals bath? Target pH 8.5–9.5 for best overall precipitation — but zinc re-dissolves above pH 10 (amphoteric behavior). Chromium (III) also re-dissolves above ~pH 9.5 as chromite — raising pH for nickel can re-dissolve already-precipitated chrome.

---

### ZONE 4 — Special Waste Streams

**Dimensions:** Y: 16.5" to 22.5" (~6.0" tall).

---

**Section label:**
- Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text:

> SPECIAL WASTE STREAMS — TREAT SEPARATELY BEFORE MIXING

---

**BLOCK E — Cyanide Destruction** (left half, X: 0.5" to 11.5")

Y: 17.2" to 22.3"

Callout container: Width: 11.0". Height: 4.8". Fill: `#1E2435`. Corner radius: 6 pt. Left-border: `#E05C5C`.

Title: `ALKALINE CHLORINATION — CYANIDE DESTRUCTION` — Barlow SemiBold, 18 pt, `#E05C5C`

**Two-stage process:**

*Stage 1 badge:* Rounded rectangle, `#E05C5C`, small badge with `STAGE 1` — Barlow Condensed ExtraBold, 14 pt, `#1A1F2E`

Stage 1 text (Inter Regular, 15 pt, `#F0EDE8`):

> **Oxidize CN⁻ to CNO⁻ (cyanate)**
> - Add NaOCl (sodium hypochlorite / bleach)
> - Maintain pH > 10 (add NaOH as needed)
> - ORP target: +350 to +400 mV
> - Contact time: 15-30 minutes minimum
> - CN⁻ + OCl⁻ -> CNO⁻ + Cl⁻

*Stage 2 badge:* `STAGE 2`

Stage 2 text:

> **Oxidize CNO⁻ to CO₂ + N₂**
> - Continue NaOCl addition
> - LOWER pH to 8.0-8.5 (critical — Stage 2 does not work above pH 10)
> - ORP target: +600 mV
> - Contact time: 30-60 minutes
> - 2CNO⁻ + 3OCl⁻ -> 2CO₂ + N₂ + 3Cl⁻

Warning callout (Inter Medium, 13 pt, `#E05C5C`):

> NEVER mix cyanide waste with acid waste — generates HCN gas (lethal)

---

**BLOCK F — Chrome Reduction** (right half, X: 12.0" to 23.5")

Y: 17.2" to 22.3"

Callout container: Width: 11.5". Height: 4.8". Fill: `#1E2435`. Corner radius: 6 pt. Left-border: `#E8A020`.

Title: `CHROME REDUCTION — Cr⁶⁺ TO Cr³⁺` — Barlow SemiBold, 18 pt, `#E8A020`

Process (Inter Regular, 15 pt, `#F0EDE8`):

> Hexavalent chromium cannot be precipitated directly — it must first be reduced to trivalent chromium (Cr³⁺), which can then be precipitated as Cr(OH)₃.
>
> **Reducing agent:** Sodium metabisulfite (Na₂S₂O₅) or ferrous sulfate (FeSO₄)
>
> **Step 1:** Lower pH to 2.0-3.0 with H₂SO₄
> **Step 2:** Add reducing agent. ORP target: +250 to +300 mV
> **Step 3:** Contact time: 20-30 minutes
> **Step 4:** Verify complete reduction (diphenylcarbazide spot test — no purple = complete)
> **Step 5:** Raise pH to 8.0-8.5 for Cr(OH)₃ precipitation
>
> Cr⁶⁺ is chemically reduced to Cr³⁺ by sodium metabisulfite under acidic conditions (simplified reaction — see below for ratio)

Key fact (JetBrains Mono Regular, 13 pt, `#E8A020`):

> 2.5–3.0 lbs sodium metabisulfite per lb of Cr⁶⁺ (theoretical ~2.8 lbs; add 10–20% excess for complete reduction)

---

### ZONE 5 — Discharge Limits

**Dimensions:** Y: 22.5" to 27.5" (~5.0" tall).

---

**Section label:**
- Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text:

> DISCHARGE COMPLIANCE — KNOW YOUR PERMIT

---

**BLOCK G — Jurisdictional Disclaimer Panel** (left two-thirds, X: 0.5" to 16.0")

Y: 23.2" to 26.5" (~3.3" tall).

Callout container: Width: 15.5". Height: 3.0". Fill: `#1E2435`. Corner radius: 6 pt. Left-border: `#E8A020`.

Title: `DISCHARGE LIMITS VARY — DO NOT RELY ON A POSTER FOR COMPLIANCE` — Barlow SemiBold, 18 pt, `#E8A020`

Body (Inter Regular, 15 pt, `#F0EDE8`, line height 145%):

> Discharge limits for metals, pH, cyanide, and Total Toxic Organics (TTO) are set by multiple overlapping regulatory frameworks:
>
> - **Federal:** EPA categorical pretreatment standards set minimum national thresholds
> - **State:** State environmental agencies may impose stricter requirements
> - **Local POTW:** Your Publicly Owned Treatment Works sets the permit limits you actually operate under — and these are often tighter than federal standards
>
> **Limits also change over time** as regulations are updated, exemptions expire, and receiving water quality standards evolve.
>
> The values in your facility's **individual discharge permit** are the only numbers that matter legally. Always operate to permit — not to any published reference, table, or poster.

---

**BLOCK GG — How to Find Your Limits** (right third, X: 16.5" to 23.5")

Y: 23.2" to 26.5"

Callout container: Width: 7.0". Height: 3.0". Fill: `#1E2435`. Corner radius: 6 pt. Left-border: `#E05C5C`.

Title: `WHERE TO FIND YOUR LIMITS` — Barlow SemiBold, 16 pt, `#E05C5C`

Body (Inter Regular, 15 pt, `#F0EDE8`, line height 145%):

> 1. **Your discharge permit** — issued by your POTW or state agency. Keep a copy in the treatment room.
> 2. **Your state environmental agency** — publishes current categorical standards
> 3. **Your POTW's industrial pretreatment coordinator** — call them directly
> 4. **Your environmental consultant or attorney** — for compliance questions
>
> If you don't have a current copy of your permit on the wall — get one today.

---

### ZONE 6 — Operator Best Practices

**Dimensions:** Y: 27.5" to 32.5" (~5.0" tall).

---

**BLOCK H — Daily Operator Checklist** (left half, X: 0.5" to 11.5")

Y: 27.5" to 32.3"

Callout container: Width: 11.0". Height: 4.5". Fill: `#1E2435`. Corner radius: 6 pt. Left-border: `#27AE60`.

Title: `DAILY OPERATOR CHECKLIST` — Barlow SemiBold, 20 pt, `#27AE60`

Bullets (Inter Regular, 15 pt, `#F0EDE8`, line height 145%):

> - Check and record influent pH before treatment begins
> - Verify chemical feed systems are functioning (pumps, lines, tanks)
> - Test effluent pH — must be 6.0-9.0 before discharge
> - Check clarifier for sludge blanket level — pump sludge before overflow
> - Sample and test effluent for metals per permit schedule
> - Record all chemical additions, pH readings, and flow rates
> - Inspect filter press — dewater when press is full; weigh and log sludge
> - Report any spill, upset, or unusual discharge IMMEDIATELY

---

**BLOCK HH — Common Mistakes** (right half, X: 12.0" to 23.5")

Y: 27.5" to 32.3"

Callout container: Width: 11.5". Height: 4.5". Fill: `#1E2435`. Corner radius: 6 pt. Left-border: `#E05C5C`.

Title: `THE MISTAKES THAT CAUSE VIOLATIONS` — Barlow SemiBold, 20 pt, `#E05C5C`

Bullets (Inter Regular, 15 pt, `#F0EDE8`, line height 145%):

> - Treating all waste streams in one batch without segregating cyanide and chrome
> - Not adjusting pH before polymer addition (floc won't form at wrong pH)
> - Overdosing polymer (breaks floc — effluent goes cloudy)
> - Discharging without final pH check (most common violation)
> - Poor recordkeeping — if you didn't write it down, it didn't happen
> - Running out of treatment chemicals on Friday and "catching up" Monday
> - Ignoring chelated metals — EDTA and NTA chelators prevent precipitation at normal pH

Key callout (JetBrains Mono Regular, 13 pt, `#E05C5C`):

> The EPA does not accept "the treatment system was down" as an excuse for non-compliant discharge.

---

### ZONE 7 — Footer Band

Standard footer per series convention.

**Disclaimer:**
> This poster is an educational reference tool covering treatment process fundamentals. No specific discharge limits are shown — discharge limits vary by jurisdiction, are set by your individual discharge permit, and change over time. Always operate in accordance with your facility's specific discharge permit and applicable federal, state, and local regulations. Consult your environmental engineer and local regulatory authority for application-specific requirements.

**Poster title:** Wastewater Treatment Fundamentals — From Rinse Tank to Discharge

**Version:** v1.0 — 2026

---

## Part 5 — Grouping and Naming Convention

| Group Name | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, compliance callout |
| Zone 2 - Treatment Flow | Section label, process flow schematic, stage chemistry cards |
| Zone 3 - pH Precipitation | Section label, pH-precipitation reference, amphoteric callout |
| Zone 4 - Special Streams | Section label, cyanide destruction, chrome reduction |
| Zone 5 - Discharge Compliance | Section label, jurisdictional disclaimer panel, how-to-find-your-limits callout |
| Zone 6 - Operator Practices | Daily checklist, common mistakes |
| Zone 7 - Footer | Standard footer elements |

---

## Part 6 — Light Edition Color Remap Table

Standard remap per series convention. No special notes.

| Dark Hex | Light Hex | Notes |
|----------|-----------|-------|
| `#1A1F2E` | `#F5F4F0` | Background |
| `#F0EDE8` | `#1A1F2E` | Primary text |
| `#1E2435` | `#ECEEF4` | Callout fills |
| `#252B3D` | `#E8E8F0` | Alt rows |
| `#0D1020` | `#1A1F2E` | Footer |
| `#E8A020` | `#C8860A` | Amber |
| `#2EC4B6` | `#1A8C82` | Teal |
| `#27AE60` | `#1E7A47` | Emerald |
| `#E05C5C` | `#B83E3E` | Coral |
| `#3A4055` | `#D0D4DE` | Headers/dividers |
| `#C8D0D8` | `#C8D0D8` | Bright Silver — **unchanged** |

---

## Part 7 — Export Checklist

Standard six files. File name prefix: `Wastewater Treatment Fundamentals`

The treatment flow diagram (Zone 2) is the most complex visual element — verify all stage labels and chemistry notes remain legible at 18x24" resize.

---

## Design Notes

This poster addresses a topic that every plating shop deals with but few discuss proudly. The tone is serious without being preachy — the compliance callout in the header sets the stakes, and the rest of the poster equips the reader to meet them.

The pH-precipitation ranges (Block D) are the poster's most practically useful reference — an operator who knows that nickel needs pH 9.5 to precipitate completely will not undershoot and send nickel out the door. Note: Zone 5 intentionally omits specific discharge limit values. Limits vary by jurisdiction and change over time — citing specific numbers on a reference poster risks misleading operators or creating liability if the poster outlasts the regulation. The section directs operators to their actual permit instead.

The cyanide and chrome sections (Zone 4) are deliberately separated from the main treatment flow because they are segregated waste streams — mixing them into the general flow would be both technically wrong and dangerous. The "NEVER mix cyanide waste with acid" warning is the single most important safety message on the poster.

This poster pairs naturally with Poster #14 (Safety in the Plating Shop) and Poster #16 (Rinsing Efficiency) — rinsing practices directly affect wastewater volume and contaminant loading.

---

*Alaina — Plating Posters Inc Creative Lead*
*Poster #27 — Wastewater Treatment Fundamentals — Construction Workup v1.0*
*2026-04-24*
