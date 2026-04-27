---
Project: Plating Posters Inc
Poster Number: 29
Title: "Anode Chemistry and Maintenance — Soluble, Insoluble, and Everything Between"
Document Type: Construction Workup
Status: v1.0 — Ready for Elara
Created: 2026-04-24T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - General industry knowledge (anode types, anode bag care, passivation, dissolution efficiency, insoluble anode chemistry)
Technical Source: General industry knowledge — soluble vs. insoluble anode chemistry, anode dissolution efficiency, passivation causes and prevention, anode bag materials and maintenance, titanium basket anodes, DSA anodes for chrome. Nickel Institute Nickel Plating Handbook 2023 (anode chapter). Products Finishing reference articles.
Watson Flags: TWO OPEN — (1) Confirm the dissolution efficiency ranges for electrolytic nickel S-Rounds (95-100%) vs. carbonyl nickel (slightly lower) against the Nickel Institute Handbook. (2) Verify the recommended anode-to-cathode area ratios for common processes (2:1 for nickel, 1:1 for copper, etc.) against standard references — this overlaps with Poster #5 but the data must be independently confirmed for this context. Both non-blocking.
Tyler Flags: ONE OPEN — (1) Validate the anode bag maintenance schedule and inspection criteria ("inspect weekly, replace when discolored or flow-restricted") against Tyler's shop experience. Non-blocking.
Process Scope: Anode types, chemistry, maintenance, and troubleshooting for electroplating processes (universal)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow: Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - AnodeChemistry
  - AnodeMaintenance
  - SolubleAnode
  - InsolubleAnode
  - ConstructionWorkup
---

# Poster #29 — Construction Workup
## Anode Chemistry and Maintenance — Soluble, Insoluble, and Everything Between

*Alaina — Plating Posters Inc Creative Lead*
*v1.0 — 2026-04-24*

This document is the construction workup for Poster #29. Anodes are the other electrode — the one that gets far less attention than the cathode (the part being plated) even though anode problems cause just as many defects. This poster gives anodes the spotlight they deserve: what types exist, how they work, how they fail, and how to keep them running.

> **Workflow note:** Poster generation uses claude.ai chat (SVG/HTML visual artifacts). These specs feed the Claude Chat Generation Prompt engineered by Elara.

**What makes this poster valuable:** Anode problems are sneaky. A passivated anode doesn't announce itself — it just quietly starves the bath of metal, and the operator blames the chemistry. A torn anode bag doesn't set off an alarm — it just lets particles into the bath, and the operator blames the filter. This poster teaches operators to look at the anode end of the tank first when troubleshooting.

**Who it's for:** Line operators, process engineers, and maintenance staff. Especially valuable in shops that run multiple bath types (each with different anode requirements) where cross-contamination of anode knowledge is common.

**Relationship to existing posters:** Companion to Poster #5 (Anode-to-Cathode Ratio). That poster covers the geometry and ratio; this one covers the chemistry, types, and maintenance. Together they form the complete anode reference.

---

## Part 1 — Workflow Orientation

### Design Capabilities for This Poster

- Text boxes with precise font, size, weight, color, and spacing control
- Solid-color rectangles and rounded rectangles for callout boxes, comparison cards, and table rows
- Simple shapes for anode cross-section diagrams (rectangles for anodes, circles for S-Rounds, triangle for basket shape)
- Color fills set to exact hex values
- Export at print-quality PDF (300 DPI equivalent via print export)

### Limitations to Flag for Elara

1. **Soluble vs. Insoluble comparison (Block B — HERO):** Two large side-by-side panels showing the two anode categories with cross-section diagrams. Soluble anode = solid rectangle dissolving (shown by dashed/irregular right edge). Insoluble anode = solid rectangle with coating layer. Simplified schematic.

2. **Anode type gallery (Block C):** Six anode types shown as simple iconic shapes (bar = rectangle, S-Rounds = circles in a rectangle basket, ball = circles, chip = small rectangles in basket, DSA = rectangle with stripe pattern for coating, platinized Ti = rectangle with thin border). Each is a simplified shape, not photorealistic.

3. **Standard construction throughout.** No novel challenges.

---

## Part 2 — Document Setup Instructions (for Elara's prompt)

### Step 1-3 — Standard (24x36", `#1A1F2E` background, standard font stack)

### Step 4 — Color palette

Standard series palette. Additional note:
- Amber used for soluble anode category accents
- Teal used for insoluble anode category accents
- Emerald for proper maintenance / best practice
- Coral for anode failure / passivation / contamination

### Step 5 — Ruler guides

**Horizontal guides:**
- 0.5" / 2.9" / 11.0" / 16.0" / 21.5" / 27.0" / 32.5" / 35.5"

---

## Part 3 — Layout Zones and Build Order

```
ZONE 1 — HEADER BAND (0"–2.9")
  Block A: Headline + subheading + tagline

ZONE 2 — SOLUBLE VS. INSOLUBLE (2.9"–11.0" / ~8.1" tall)
  Block B: Side-by-side comparison panels (HERO)
  Block C: Anode type gallery (six types)

ZONE 3 — ANODE SELECTION BY PROCESS (11.0"–16.0" / ~5.0" tall)
  Block D: Process-to-anode matching table

ZONE 4 — ANODE PASSIVATION (16.0"–21.5" / ~5.5" tall)
  Block E: What is passivation + causes (left half)
  Block F: Prevention and recovery (right half)

ZONE 5 — ANODE BAG CARE AND MAINTENANCE (21.5"–27.0" / ~5.5" tall)
  Block G: Anode bag reference (left half)
  Block H: Maintenance schedule and inspection criteria (right half)

ZONE 6 — TROUBLESHOOTING (27.0"–32.5" / ~5.5" tall)
  Block I: Anode-related defect diagnosis table

ZONE 7 — FOOTER BAND (32.5"–36.0" / ~3.5" tall)
  Block J: Standard footer
```

---

## Part 4 — Zone-by-Zone Build Specifications

### ZONE 1 — Header Band

**BLOCK A — Headline**

- Font: Barlow Condensed ExtraBold, 72 pt, `#F0EDE8`
- Text (all caps):

> ANODE CHEMISTRY AND MAINTENANCE

**BLOCK A — Subheading**

- Font: Barlow SemiBold, 34 pt, `#E8A020` (Amber)
- Text:

> Soluble, Insoluble, and Everything Between

**BLOCK A — Tagline**

- Font: Barlow SemiBold, 22 pt, `#F0EDE8` at 65%
- Text:

> When the deposit goes wrong, check the anodes before you blame the bath.

---

### ZONE 2 — Soluble vs. Insoluble (HERO)

**Dimensions:** Y: 2.9" to 11.0" (~8.1" tall).

---

**Section label:**
- Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text:

> THE TWO FAMILIES OF ANODES

---

**BLOCK B — Side-by-Side Comparison Panels**

Y: 3.6" to 8.0" (~4.4" tall). Two large panels.

**Left — Soluble Anodes:**
- X: 0.5". Width: 11.0". Height: 4.2". Fill: `#1E2435`. Border: 2 pt `#E8A020`. Corner radius: 6 pt.

Title: `SOLUBLE ANODES` — Barlow Condensed ExtraBold, 28 pt, `#E8A020`
Subtitle: `The anode dissolves to replenish metal in the bath` — Barlow SemiBold, 16 pt, `#F0EDE8` at 60%

Cross-section diagram (centered, 8.0" wide x 1.5" tall):
- Left side: Solid rectangle (anode), `#C8D0D8`, with label `Ni / Cu / Zn / Sn`
- Arrow pointing right: `->` `#E8A020`
- Center: Label `M -> M²⁺ + 2e⁻` — JetBrains Mono Regular, 16 pt, `#E8A020`
- Right side: Cloud/wave shape (solution) with `M²⁺` ions — `#E8A020` at 30%

Key characteristics (bullet list below diagram):
- Inter Regular, 15 pt, `#F0EDE8`, line height 140%

> - Anode metal dissolves during plating — replenishes bath concentration
> - Metal balance: dissolution rate ideally matches deposition rate
> - Produces sludge/fines — MUST use anode bags
> - Purity matters — impurities dissolve into the bath
> - Requires chloride (in nickel) to prevent passivation

**Right — Insoluble Anodes:**
- X: 12.0". Width: 11.5". Height: 4.2". Fill: `#1E2435`. Border: 2 pt `#2EC4B6`. Corner radius: 6 pt.

Title: `INSOLUBLE ANODES` — Barlow Condensed ExtraBold, 28 pt, `#2EC4B6`
Subtitle: `The anode conducts current but does not dissolve` — Barlow SemiBold, 16 pt, `#F0EDE8` at 60%

Cross-section diagram:
- Left side: Solid rectangle with coating layer, `#2EC4B6`/`#3A4055`, labels `Pt / IrO₂ / PbO₂`
- Arrow pointing right: `->` `#2EC4B6`
- Center: Label `2H₂O -> O₂ + 4H⁺ + 4e⁻` — JetBrains Mono Regular, 14 pt, `#2EC4B6`
- Right side: O₂ bubble symbols

Key characteristics:
> - Anode does NOT dissolve — no sludge, no anode bags needed
> - Metal replenished by chemical addition (salts) or proprietary replenishers
> - Bath chemistry requires more active management (metal level drops during plating)
> - Generates O₂ and acid at the anode — must account for pH drift
> - Longer life but higher initial cost

---

**BLOCK C — Anode Type Gallery**

Y: 8.3" to 10.8" (~2.5" tall). Six small cards in a single row.

Each card: Width: 3.67". Height: 2.2". Fill: `#1E2435`. Corner radius: 4 pt.

| Card | X | Accent | Type | Shape Description | Used In |
|---|---|---|---|---|---|
| 1 | 0.5" | `#E8A020` | `SOLID BARS / SLABS` | Tall rectangle | Zinc, copper, tin |
| 2 | 4.33" | `#E8A020` | `S-ROUNDS / CHIPS` | Small circles in rectangle basket | Nickel (in Ti baskets) |
| 3 | 8.17" | `#E8A020` | `CAST / ROLLED SHEET` | Wide thin rectangle | Copper, tin |
| 4 | 12.0" | `#2EC4B6` | `PLATINIZED TITANIUM` | Rectangle with thin bright border | Precious metals, EN |
| 5 | 15.83" | `#2EC4B6` | `DSA (Mixed Oxide)` | Rectangle with stripe pattern | Hard chrome, electrogalvanizing |
| 6 | 19.67" | `#2EC4B6` | `LEAD / LEAD ALLOY` | Solid dark rectangle | Hard chrome (traditional) |

Card title: Barlow SemiBold, 14 pt, accent color.
"Used in" label: Inter Regular, 12 pt, `#F0EDE8` at 60%.
Shape: Simplified geometric element (rectangle, circles, etc.) in `#C8D0D8` or accent color at 30%.

---

### ZONE 3 — Anode Selection by Process

**Dimensions:** Y: 11.0" to 16.0" (~5.0" tall).

---

**Section label:**
- Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text:

> WHICH ANODE FOR WHICH PROCESS?

---

**BLOCK D — Process-to-Anode Table**

Y: 11.8" to 15.8" (~4.0" tall).

Header: `Process` | `Anode Type` | `Material` | `A:C Ratio` | `Key Notes`

| Process | Type | Material | A:C | Notes |
|---|---|---|---|---|
| Watts nickel (bright) | Soluble | Electrolytic Ni S-Rounds in Ti baskets + PP bags | 2:1 | Chloride prevents passivation; S-Rounds dissolve more evenly than cast |
| Acid copper sulfate | Soluble | OFHC copper (P-deoxidized) | 1:1 | Phosphorus content (0.04-0.06%) controls dissolution; too low = rough dissolution |
| Acid zinc (chloride) | Soluble | Special high-grade (SHG) zinc slabs | 1:1 to 2:1 | Zinc dissolves readily; watch for sludge buildup |
| Alkaline zinc (non-CN) | Soluble | SHG zinc in steel baskets | 1:1 | Steel baskets — NOT titanium (zinc attacks Ti) |
| Hard chrome | Insoluble | Lead-antimony (6-8% Sb) or DSA | N/A | Chromic acid replenished by chemical addition |
| Gold (acid) | Insoluble | Platinized titanium | Per spec | Gold replenished by gold salt addition |
| Silver (cyanide) | Soluble | Fine silver (99.9%) bars | 2:1 | Anode bags critical — silver sludge is expensive to lose |
| Tin (acid) | Soluble | Pure tin bars or balls | 1:1 to 2:1 | Tin passivates easily — maintain adequate Sn²⁺ |
| Electroless nickel | Insoluble | None (chemical reduction — no external anode) | N/A | No anodes. Reducing agent (NaH₂PO₂) provides electrons. |

Data font: Inter Regular, 13 pt, `#F0EDE8`. "Soluble" in `#E8A020`, "Insoluble" in `#2EC4B6`. A:C ratios in JetBrains Mono Regular, 13 pt, `#27AE60`. Alternating rows.

---

### ZONE 4 — Anode Passivation

**Dimensions:** Y: 16.0" to 21.5" (~5.5" tall).

---

**Section label:**
- Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text:

> ANODE PASSIVATION — THE SILENT BATH KILLER

---

**BLOCK E — What Is Passivation** (left half)

Callout container: Width: 11.0". Height: 4.8". Fill: `#1E2435`. Left-border: `#E05C5C`.

Title: `WHAT HAPPENS AND WHY` — Barlow SemiBold, 20 pt, `#E05C5C`

Body (Inter Regular, 15 pt, `#F0EDE8`, line height 145%):

> A passive anode develops an oxide film on its surface that blocks metal dissolution. Current still flows — but it goes to oxygen evolution instead of metal dissolution. The bath slowly starves of metal ions while the operator sees normal amperage on the meter.
>
> **Symptoms:**
> - Rising bath voltage (same amps, higher volts)
> - Declining metal concentration despite normal plating load
> - Darkening or filming on anode surface
> - Gray or black sludge on anode surface
> - pH drop (acid generation from O₂ evolution instead of metal dissolution)

**Causes (JetBrains Mono Regular, 13 pt, `#E05C5C`):**

> - Low chloride (nickel) — below 30 g/L NiCl₂
> - Excessive current density on anode (too small anode area)
> - Contaminated anode surface (oil, grease, oxide)
> - Wrong anode composition (Ni: carbonyl vs electrolytic matters)
> - Stagnant solution at anode surface (poor agitation)

---

**BLOCK F — Prevention and Recovery** (right half)

Callout container: Width: 11.5". Height: 4.8". Fill: `#1E2435`. Left-border: `#27AE60`.

Title: `PREVENTION AND RECOVERY` — Barlow SemiBold, 20 pt, `#27AE60`

Body (Inter Regular, 15 pt, `#F0EDE8`, line height 145%):

**Prevention:**
> - Maintain chloride concentration at or above minimum (nickel: 30+ g/L NiCl₂)
> - Size anodes to maintain proper A:C ratio — never run undersized
> - Use correct anode composition for the bath (electrolytic Ni, not carbonyl, for Watts)
> - Ensure solution circulation reaches anode surface
> - Keep anodes clean — remove buildup during scheduled maintenance

**Recovery:**
> - Remove anodes from tank
> - Scrub or acid-dip to remove oxide/film (10% HCl for nickel anodes)
> - Inspect for unusual corrosion patterns — pitting means impure anode
> - Verify chloride level before re-installing
> - Consider activating anodes in a "break-in" period at low current before full production

Key callout (JetBrains Mono Regular, 13 pt, `#27AE60`):

> Prevention is cheaper than recovery — a $5 chloride addition prevents a $500 bath adjustment

---

### ZONE 5 — Anode Bag Care and Maintenance

**Dimensions:** Y: 21.5" to 27.0" (~5.5" tall).

---

**Section label:**
- Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`
- Text:

> ANODE BAGS — YOUR FIRST LINE OF FILTRATION

---

**BLOCK G — Anode Bag Reference** (left half)

Callout container: Width: 11.0". Height: 4.8". Fill: `#1E2435`. Left-border: `#2EC4B6`.

Title: `ANODE BAG MATERIALS AND SELECTION` — Barlow SemiBold, 18 pt, `#2EC4B6`

Table (4 rows):

| Material | Used For | Micron Rating | Notes |
|---|---|---|---|
| Polypropylene (PP) | Nickel, copper, general | 1-10 micron | Most common; chemical-resistant; heat-resistant to 200°F |
| Polyester (PE) | General, lower-temp baths | 1-10 micron | Less heat-resistant than PP; good for acid zinc |
| Cotton / Dynel | Traditional; being phased out | Variable | Can shed fibers — not recommended for critical applications |
| Nylon | Acid baths | 5-25 micron | Good strength; not suitable for strong alkali |

Data font: Inter Regular, 13 pt, `#F0EDE8`. Alternating rows.

Below table — key fact:
- JetBrains Mono Regular, 13 pt, `#2EC4B6`
- Text:

> Double-bag anodes in bright nickel — the inner bag catches fines, the outer bag catches anything the inner misses

---

**BLOCK H — Maintenance Schedule** (right half)

Callout container: Width: 11.5". Height: 4.8". Fill: `#1E2435`. Left-border: `#E8A020`.

Title: `ANODE BAG MAINTENANCE` — Barlow SemiBold, 18 pt, `#E8A020`

Checklist (Inter Regular, 15 pt, `#F0EDE8`, line height 145%):

> **Daily:**
> - Visual check — bags submerged, no tears, no collapse
>
> **Weekly:**
> - Remove and inspect bags for discoloration, holes, or clogging
> - Check for sludge buildup inside bags — if heavy, clean or replace
> - Verify bag is not restricting solution flow around anode
>
> **Monthly or as needed:**
> - Replace bags showing discoloration, reduced porosity, or physical damage
> - Rinse new bags in DI water before use (removes sizing compounds)
> - Replace ALL bags at the same time — mixing old and new changes flow distribution
>
> **Warning sign:** If you see black or gray particles on plated parts, check anode bags FIRST.

---

### ZONE 6 — Troubleshooting

**Dimensions:** Y: 27.0" to 32.5" (~5.5" tall).

---

**Section label:**
- Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text:

> ANODE-RELATED DEFECTS — DIAGNOSIS TABLE

---

**BLOCK I — Defect Diagnosis Table**

Y: 27.8" to 32.3" (~4.5" tall). Full safe zone width.

| Symptom | Anode Cause | Check | Fix |
|---|---|---|---|
| Rough deposits / particles | Torn anode bags; anode sludge in bath | Inspect bags; check bath clarity | Replace bags; filter bath; clean anodes |
| Thin deposits / slow plating | Passivated anodes; insufficient anode area | Check voltage (rising?); check metal level | Activate anodes; add anode area; replenish chloride |
| Uneven thickness | Poor anode placement; mismatched A:C ratio | Compare HCD/LCD; check anode positioning | Reposition anodes; adjust A:C ratio per Poster #5 |
| High voltage / high power consumption | Passivated anodes; poor connection | Check bus bar contacts; check anode surface | Clean contacts; de-passivate anodes |
| Dark deposits at LCD | Anode impurities dissolving into bath | Analyze bath for contaminants; check anode purity cert | Dummy plate to remove contaminants; switch to higher-purity anodes |
| pH dropping unexpectedly | Passivated anodes (O₂ evolution generates acid) | Check anode dissolution rate vs. deposition rate | De-passivate; correct metal balance |
| Anode sludge excessive | Wrong anode composition; current density too high on anode | Check anode spec sheet; check A:C ratio | Use correct anode type; increase anode area |

Header: Barlow SemiBold, 13 pt, `#F0EDE8` on `#3A4055`. Data: Inter Regular, 13 pt, `#F0EDE8`. Symptom column: Inter Medium, 13 pt, `#E05C5C`. Alternating rows.

---

### ZONE 7 — Footer Band

Standard footer per series convention.

**Disclaimer:**
> This poster is an educational reference tool. Anode types, compositions, and maintenance procedures are typical industry values. Specific anode requirements vary by bath chemistry, proprietary formulation, and application. Consult your anode supplier and process chemical supplier for application-specific guidance. Anode-to-cathode ratios shown are general guidelines — verify against your specific process specification.

**Poster title:** Anode Chemistry and Maintenance — Soluble, Insoluble, and Everything Between

**Version:** v1.0 — 2026

---

## Part 5 — Grouping and Naming Convention

| Group Name | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline |
| Zone 2 - Soluble vs Insoluble | Section label, two comparison panels, six-type gallery |
| Zone 3 - Process Selection | Section label, process-to-anode table |
| Zone 4 - Passivation | Section label, passivation causes, prevention and recovery |
| Zone 5 - Anode Bags | Section label, bag materials table, maintenance schedule |
| Zone 6 - Troubleshooting | Section label, defect diagnosis table |
| Zone 7 - Footer | Standard footer elements |

---

## Part 6 — Light Edition Color Remap Table

Standard remap per series convention. No special notes.

---

## Part 7 — Export Checklist

Standard six files. File name prefix: `Anode Chemistry and Maintenance`

---

## Design Notes

This poster is the natural companion to Poster #5 (Anode-to-Cathode Ratio). Where #5 focuses on geometry and ratio, #29 goes deep on the chemistry, types, and maintenance. A shop that hangs both posters has a complete anode reference. Cross-references to Poster #5 appear in the process table (Zone 3) and troubleshooting table (Zone 6) — this is intentional continuity.

The passivation section (Zone 4) is the poster's strongest diagnostic content. Passivation is one of those problems that looks like a chemistry problem but is actually an electrode problem — and it fools even experienced platers. Making the symptoms, causes, and recovery visible on the wall prevents the classic mistake of dumping chemicals into a bath that actually has an anode problem.

The anode bag section (Zone 5) may seem mundane, but anode bag neglect is one of the top 3 causes of roughness in nickel plating. The double-bagging recommendation for bright nickel is the kind of practical detail that separates a well-run line from a mediocre one.

---

*Alaina — Plating Posters Inc Creative Lead*
*Poster #29 — Anode Chemistry and Maintenance — Construction Workup v1.0*
*2026-04-24*
