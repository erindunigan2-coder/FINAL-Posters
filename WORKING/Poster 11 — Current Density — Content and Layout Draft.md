---
Project: Plating Posters Inc
Poster Number: 11
Title: "Current Density Quick Reference Chart"
Document Type: Content and Layout Draft
Status: v1.0 — Ready for Canva Construction Workup
Created: 2026-04-03T00:00:00
Author: Alaina (poster-designer)
Technical Source: Watson — Current Density Quick Reference — Alaina Research Brief v1 (2026-04-03)
Watson Flags: NONE — all data sourced directly from Research Brief v1; Drew confirmation requested on CD ranges but not blocking
Process Scope: Multi-process reference chart — exception to one-process-per-poster rule (this is a cross-reference chart, not a single-process deep dive)
Editions: Dark + Light
tags:
  - PosterDesign
  - CurrentDensity
  - ContentDraft
---

# Poster #11 — Content and Layout Draft
## Current Density Quick Reference Chart

*Alaina — Plating Posters Inc Creative Lead*
*v1.0 — 2026-04-03*
*All data sourced from Watson's Research Brief v1 (2026-04-03). Drew confirmation requested on CD ranges (courtesy flag, not blocking). This document is the authoritative content source for the Canva Construction Workup.*

---

## Section 1 — Watson Flag Status and Design Decisions

**Status: NO BLOCKING FLAGS.**

Watson has requested Drew confirm that CD ranges match field experience and A Brite product recommendations. This is a courtesy confirmation — all values are sourced from the 1993 Metal Finishing Guidebook, Products Finishing, and established industry references. The poster can proceed to build; Drew can adjust specific ranges if needed during review.

Watson also noted that Drew's Quick Reference gives zinc rack as 15-20 ASF and barrel as 5-10 ASF, which is narrower than the 10-40 / 3-15 ranges in the brief. I am using Watson's wider industry ranges because this is a universal reference poster, not an A Brite-specific document. Drew may want to narrow certain ranges based on his field experience — that is a Stage 7 revision, not a blocker.

**Design decisions:**

- **Process scope exception:** This poster is a multi-process cross-reference chart. It lists current density ranges for every major plating process on a single wall chart. This is explicitly different from the series rule "one process per poster" — a current density reference chart that only covered one process would miss its entire value proposition. The rule exists to prevent cramming two process deep-dives onto one poster; this poster is a data reference, not a process overview. The exception is justified.

- **Layout: Data table dominant, NOT horizontal bar chart.** Watson suggests a horizontal bar chart format. I considered this carefully and rejected it for this poster. A bar chart is visually appealing but functionally inferior for this use case: an operator walking up to the poster needs to find their process name, scan right, and read the ASF number. That is a table lookup, not a visual comparison. The bar chart format makes the comparison between processes visually interesting but makes the individual lookup slower. The HERO element is the master table — clean, scannable, no-nonsense.

- **Process family color coding:** Adopted from Watson's suggestion. Zinc = Teal left accent. Copper = Amber. Nickel = Warm White (neutral — the most common metal). Chrome = Coral (highest CD, most extreme). Precious/Other = Emerald. This color coding maps to the locked series palette and provides visual grouping without introducing new colors.

- **"Too High / Too Low" summary:** Included as Block D — a compact two-column callout below the master table. Not a separate zone-width chart. The consequences of wrong CD are important context but must not compete with the table for attention.

- **CD Formula callout:** Included as Block B in the header zone — the formula is simple enough to fit alongside the headline and important enough to earn header-band real estate.

- **Rack vs. Barrel visual:** Omitted as a separate illustration. The master table already has separate Rack and Barrel columns — the visual comparison is built into the data structure. Adding a separate illustration would consume space without adding information.

---

## Section 2 — Layout Zone Map

### Overall Artboard Architecture (24x36" master)

```
+------------------------------------------------------------------------+
| ZONE 1 — HEADER BAND (~0-8% / top 2.9")                                |
| BLOCK A: Headline + subheading + tagline (left 60%)                     |
| BLOCK B: CD Formula callout box (right 40%)                             |
+------------------------------------------------------------------------+
| ZONE 2 — MASTER CURRENT DENSITY TABLE (~8-78% / ~25.2" band)           |
| BLOCK C: HERO DATA TABLE — all processes, rack + barrel columns         |
| 7 process family sections, 21 process rows                              |
+------------------------------------------------------------------------+
| ZONE 3 — "WHAT GOES WRONG" + CONVERSION (~78-91% / ~4.7" band)         |
| BLOCK D: Too High / Too Low callout (left 60%)                          |
| BLOCK E: Conversion quick reference + cross-ref (right 40%)             |
+------------------------------------------------------------------------+
| ZONE 4 — FOOTER BAND (~91-100% / ~3.2")                                |
| BLOCK F: Disclaimer + Series name + Logo placeholder + Version          |
+------------------------------------------------------------------------+
```

**Zone height summary:**
| Zone | Content | % Height | Approx Inches |
|------|---------|----------|---------------|
| 1 — Header | Headline + formula | 8% | 2.9" |
| 2 — Master Table | HERO data table | 70% | 25.2" |
| 3 — What Goes Wrong + Conversion | Two-column callouts | 13% | 4.7" |
| 4 — Footer | Disclaimer + metadata | 9% | 3.2" |
| **Total** | | **100%** | **36.0"** |

**Design note:** This poster is 70% table. That is intentional. This is the most data-dense poster in the series — its value is density of reference. The table must be impeccably formatted, scannable, and readable at 4-6 feet. Every fraction of an inch of visual clarity matters.

---

## Section 3 — Content Blocks

---

### BLOCK A — Headline and Subheading

**Headline (Barlow Condensed ExtraBold, 96 pt, `#F0EDE8` Dark / `#1A1F2E` Light):**

> CURRENT DENSITY

**Subheading (Barlow SemiBold, 40 pt, `#E8A020` Dark / `#C8860A` Light):**

> Quick Reference Chart

**Tagline (Barlow SemiBold, 22 pt, `#F0EDE8` at 65% opacity):**

> Right range. Right deposit. Every time.

---

### BLOCK B — CD Formula Callout Box (Header-Zone Right)

**Callout box styling:**
- Fill: `#1E2435` Dark Callout / `#ECEEF4` Light
- Border: `#2EC4B6` Teal, 1.5 pt
- Corner radius: 8 pt
- Internal padding: 20 pt

**Callout title (Barlow SemiBold, 20 pt, `#2EC4B6` Dark / `#1A8C82` Light):**

> THE FORMULA

**Formula (JetBrains Mono Regular, 28-30 pt, `#F0EDE8` Dark / `#1A1F2E` Light, centered):**

> ASF = Amps / Area (ft²)

**Worked example (Inter Regular, 16-17 pt, `#F0EDE8` at 80% opacity):**

> 10 bolts at 2.5 ft² total, 75 A applied:
> 75 / 2.5 = 30 ASF

**Conversion note (JetBrains Mono Regular, 14 pt, `#E8A020`):**

> ASF / 10 ~ ASD

---

### BLOCK C — Master Current Density Table (HERO — Zone 2)

**Section label (Barlow Condensed ExtraBold, 32-34 pt, `#F0EDE8`, centered above table):**

> CURRENT DENSITY RANGES BY PROCESS

**Table structure:**

The table has 5 columns:
1. **Process** (left, ~35% width) — Inter Medium, 18-20 pt
2. **Rack ASF** (~16% width) — JetBrains Mono Regular, 18-20 pt, centered
3. **Barrel ASF** (~16% width) — JetBrains Mono Regular, 18-20 pt, centered
4. **Cathode Efficiency** (~16% width) — JetBrains Mono Regular, 16-18 pt, centered
5. **Notes** (~17% width) — Inter Regular, 14-16 pt

**Column header row:**
- Fill: `#3A4055` Mid Slate
- Text: Barlow SemiBold, 20-22 pt, `#E8A020` Amber
- Headers: `PROCESS` | `RACK (ASF)` | `BARREL (ASF)` | `EFFICIENCY` | `NOTES`

**Process family section headers:**
- Full-width row, fill: accent color at 15% opacity over `#1A1F2E`
- Left accent bar: 6 pt in process family color
- Text: Barlow Condensed ExtraBold, 22-24 pt, process family accent color

**Data rows:**
- Alternating: `#1A1F2E` base / `#252B3D` alt
- Left accent bar: 4 pt, process family color
- Text colors per column specification above

---

**SECTION: ZINC PLATING** (Teal `#2EC4B6`)

| Process | Rack (ASF) | Barrel (ASF) | Efficiency | Notes |
|---------|-----------|-------------|------------|-------|
| Acid Chloride Zinc (KCl) | 10-40 | 3-15 | 95-98% | Most common zinc process |
| Alkaline Non-Cyanide Zinc | 10-30 | 5-15 | 70-80% | Insoluble anodes; lower eff. |
| Alkaline Cyanide Zinc | 10-40 | 5-15 | 65-80% | Legacy NaCN; high throwing power |

**SECTION: COPPER PLATING** (Amber `#E8A020`)

| Process | Rack (ASF) | Barrel (ASF) | Efficiency | Notes |
|---------|-----------|-------------|------------|-------|
| Bright Acid Copper | 15-40 | 5-15 | 95-100% | CuSO₄/H₂SO₄; phosphorized anodes |
| Cyanide Copper Strike | 5-20 | 3-10 | 30-60% | Thin flash — adhesion layer only |

**SECTION: NICKEL PLATING** (Warm White `#F0EDE8` accent — neutral for the workhorse)

| Process | Rack (ASF) | Barrel (ASF) | Efficiency | Notes |
|---------|-----------|-------------|------------|-------|
| Watts Nickel (bright/semi-bright) | 20-60 | 5-20 | 93-97% | Standard decorative + functional |
| Nickel Sulfamate | 20-140 | — | 95-100% | Engineering; 400+ ASF w/ agitation |
| Nickel Strike (Watts) | 10-50 | — | 90-95% | Active substrates |
| Nickel Strike (Wood's) | 50-250 | — | 50-70% | Stainless steel activation |

**SECTION: CHROMIUM PLATING** (Coral `#E05C5C`)

| Process | Rack (ASF) | Barrel (ASF) | Efficiency | Notes |
|---------|-----------|-------------|------------|-------|
| Decorative Chrome (hex) | 150-300 | — | 10-18% | 5-10x current of other processes |
| Decorative Chrome (trivalent) | 40-150 | 40-100 | 15-25% | Wider window; won't burn |
| Hard Chrome (conventional) | 150-300 | — | 12-20% | 1-3 A/in²; functional |
| Hard Chrome (mixed catalyst) | 150-300 | — | 20-25% | Fluoride catalyst; higher eff. |

**SECTION: SILVER PLATING** (Emerald `#27AE60`)

| Process | Rack (ASF) | Barrel (ASF) | Efficiency | Notes |
|---------|-----------|-------------|------------|-------|
| Silver Cyanide Strike | 10-30 | 5-15 | 95-100% | High initial CD; short time |
| Silver Cyanide Plate | 5-15 | 3-10 | 95-100% | Low CD for smooth deposit |

**SECTION: TIN PLATING** (Emerald `#27AE60`)

| Process | Rack (ASF) | Barrel (ASF) | Efficiency | Notes |
|---------|-----------|-------------|------------|-------|
| Acid Tin (matte, MSA/sulfate) | 10-30 | 5-15 | 90-95% | Zirconium anode baskets |
| Acid Tin (bright) | 10-25 | 5-15 | 90-95% | Organic brighteners added |

**SECTION: OTHER PROCESSES** (Mid Slate `#3A4055` — neutral grouping)

| Process | Rack (ASF) | Barrel (ASF) | Efficiency | Notes |
|---------|-----------|-------------|------------|-------|
| Cadmium (alkaline cyanide) | 5-70 | 5-7 | 90-95% | 15-25 ASF common for still |
| Brass (cyanide) | 10-20 | 10-20 | 50-70% | Color shifts with CD |
| Zinc-Nickel (acid) | 10-40 | 5-15 | 85-95% | Alloy ratio affected by CD |
| Sulfuric Acid Anodize (Type II) | 12-18 | — | N/A | Oxide growth, not deposition |
| Hard Coat Anodize (Type III) | 24-36 | — | N/A | Lower temp, higher voltage |

**Table total:** 7 sections, 21 data rows.

**Table footnote (Inter Regular, 13-14 pt, `#F0EDE8` at 60% opacity):**

> *All ranges are for normal production plating at typical bath concentrations and temperatures. Extreme conditions (high-speed, pulse, hone) excluded. Barrel CD typically 1/3 to 1/2 of rack CD. "—" = process not typically run in barrel. Efficiency = cathode efficiency (% of current depositing metal vs. evolving hydrogen). N/A = not applicable (anodizing is oxide growth, not metal deposition).*

---

### BLOCK D — "What Goes Wrong" (Zone 3 — Left)

**Callout box styling:**
- Fill: `#1E2435` Dark Callout / `#ECEEF4` Light
- No border — the two columns inside provide visual structure
- Corner radius: 8 pt
- Width: ~60% of page (left side)

**Section label (Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`, centered above):**

> WHAT GOES WRONG

**Two-column layout inside the callout:**

**Left sub-column — TOO HIGH (Coral accent)**

Title (Barlow SemiBold, 18 pt, `#E05C5C`):
> TOO HIGH

Bullet list (Inter Regular, 16 pt, `#F0EDE8`):
> - Burning — dark, rough, powdery edges
> - Hydrogen pitting — trapped gas bubbles
> - Poor adhesion — stressed deposit
> - Reduced throwing power

**Right sub-column — TOO LOW (Teal accent)**

Title (Barlow SemiBold, 18 pt, `#2EC4B6`):
> TOO LOW

Bullet list (Inter Regular, 16 pt, `#F0EDE8`):
> - Skip plating — bare spots in LCD zones
> - Dull or hazy deposits
> - Slow deposition — throughput loss
> - Alloy composition shift

**Design note:** The Coral/Teal split mirrors the HCD/LCD convention from Poster #4. Operators familiar with the Hull Cell poster will immediately recognize the color-meaning mapping.

---

### BLOCK E — Conversion + Cross-Reference (Zone 3 — Right)

**Callout box styling:**
- Fill: `#1E2435` Dark Callout / `#ECEEF4` Light
- Border: `#3A4055` Mid Slate, 1 pt
- Corner radius: 8 pt
- Width: ~40% of page (right side)

**Conversion title (Barlow SemiBold, 18 pt, `#E8A020`):**

> QUICK CONVERSIONS

**Conversion data (JetBrains Mono Regular, 17-18 pt, `#F0EDE8`):**

> ASF / 10 ~ ASD (exact: / 10.76)
> 1 A/in² = 144 ASF
> 1 A/m² = 0.0929 ASF

**Cross-reference (Inter Regular, 15-16 pt, `#2EC4B6`, with Teal left accent rule 2 pt):**

> See Poster #4 — Reading Your Hull Cell Panel — to visualize current density distribution across a test panel.

---

### BLOCK F — Footer Content

**Band fill:** `#0D1020` Deep Navy (Dark) / `#1A1F2E` Charcoal (Light)

**Left — Poster title (Barlow SemiBold, 16-18 pt, `#F0EDE8`):**

> Current Density Quick Reference Chart

**Center — Series name (Inter Regular, 14-15 pt, `#F0EDE8` at 70% opacity):**

> Plating Posters Inc — Metal Finishing Reference Series

**Far right — Logo placeholder:**

> [LOGO]

**Disclaimer (Inter Regular, 11-12 pt, `#F0EDE8` at 50% opacity):**

> This poster is a technical reference tool. Current density ranges reflect general industry practice — consult your process supplier's TDS for product-specific recommendations. Not a substitute for process qualification.

**Version (JetBrains Mono Regular, 11 pt, `#F0EDE8` at 50% opacity):**

> v1.0 — 2026

---

## Section 4 — Light Edition Notes

Standard remap table applies. No overrides required — this poster does not use accent colors as column header fills (unlike Poster #10). The process family section header rows use accent colors at 15% opacity over the base background — remap both the background tint and the text color per the standard table.

---

## Section 5 — Collaboration Flags

**Watson:** All data confirmed via Research Brief v1. Drew confirmation requested on specific CD ranges (courtesy, not blocking).

**Drew:** Watson asks you to confirm the CD ranges match your field experience, especially acid chloride zinc (10-40 / 3-15), bright acid copper (15-40), nickel sulfamate (20-140), and hard chrome (150-300). Your Quick Reference shows narrower zinc ranges (15-20 / 5-10) — the poster uses wider industry ranges; narrow if preferred.

**Tyler:** No validation required.

---

*Alaina — Plating Posters Inc Creative Lead*
*Poster #11 — Current Density Quick Reference Chart — Content and Layout Draft v1.0*
*2026-04-03*
