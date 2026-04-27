---
Project: Plating Posters Inc
Poster Number: 30
Title: "Bath Analysis Methods — What to Test, How Often, and Why It Matters"
Document Type: Construction Workup
Status: v1.0 — Ready for Elara
Created: 2026-04-24T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - General industry knowledge (plating bath analysis, Hull cell testing, titration methods, instrumental analysis)
Technical Source: General industry knowledge — titration methods (EDTA, iodometric, acid-base), Hull cell evaluation, spectrophotometric and AA analysis, pH measurement, specific gravity, temperature, contamination testing. IPC-TM-650 Method 2.4.18.1 (Hull cell standard), ASTM B764 (deposit compositional analysis). Products Finishing analytical best practices. Note: ASTM B750 is not a relevant reference (it covers Galfan wire coating specification — removed).
Watson Flags: TWO OPEN — (1) Confirm the recommended analysis frequencies in the process table (e.g., nickel sulfate weekly, pH daily, brightener per Hull cell) against current NASF/industry best practice guides. (2) Verify the instrumental analysis descriptions (AA vs. ICP-OES vs. XRF for bath analysis) are accurately characterized for the poster audience. Both non-blocking.
Tyler Flags: TWO OPEN — (1) Validate the "analysis frequency by process" table against Tyler's current lab procedures — Tyler's actual analysis schedules may differ from published guidelines, and the poster should reflect realistic shop practice. (2) Confirm the Hull cell testing conditions listed (267 mL, 2A, 5-10 min) match the standard Tyler uses across bath types. Both non-blocking but important — this poster directly overlaps Tyler's core expertise.
Process Scope: Analytical methods and testing protocols for monitoring and controlling plating bath chemistry (universal)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow: Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - BathAnalysis
  - Titration
  - HullCell
  - QualityControl
  - LaboratoryMethods
  - ConstructionWorkup
---

# Poster #30 — Construction Workup
## Bath Analysis Methods — What to Test, How Often, and Why It Matters

*Alaina — Plating Posters Inc Creative Lead*
*v1.0 — 2026-04-24*

This document is the construction workup for Poster #30, the capstone of the initial 30-poster series. If the other posters teach operators what each process IS, this poster teaches them how to KNOW their bath is right. Analytical control is the difference between a plating shop that reacts to problems and one that prevents them.

> **Workflow note:** Poster generation uses claude.ai chat (SVG/HTML visual artifacts). These specs feed the Claude Chat Generation Prompt engineered by Elara.

**What makes this poster valuable:** Most plating defects start as chemistry drift. A bath that worked Monday can produce rejects by Friday if nobody checked the metal concentration, pH, or additive level. This poster puts the testing schedule and methods on the wall — the visual reminder that "if you didn't test it, you don't know it."

**Who it's for:** Lab technicians, process engineers, operators, and quality managers. The lab tech gets a method reference; the operator gets a testing frequency guide; the quality manager gets a visual argument for investing in analytical capability.

**Relationship to existing posters:** Complements Poster #4 (Hull Cell), Poster #12 (pH Control), Poster #7 (Metallic Contamination), and Poster #25 (Filtration/Purification). This poster ties them all together with the "what to test and when" framework.

---

## Part 1 — Workflow Orientation

### Design Capabilities for This Poster

- Text boxes with precise font, size, weight, color, and spacing control
- Solid-color rectangles and rounded rectangles for callout boxes, table rows, and method cards
- Simple shapes for Hull cell icon (small rectangle), beaker/flask shapes (rectangle + triangle), pH meter (rectangle + circle)
- Color fills set to exact hex values
- Export at print-quality PDF (300 DPI equivalent via print export)

### Limitations to Flag for Elara

1. **Analysis method cards (Block B — HERO):** Six method cards showing the major analytical techniques. Same card construction as previous posters.

2. **Analysis frequency matrix (Block D):** A large table — the poster's primary reference value. Wide format with process types as rows and test parameters as columns. Will be the most space-intensive element. Same construction as Poster #22's comparison table.

3. **Standard construction throughout.** No novel visual challenges.

---

## Part 2 — Document Setup Instructions (for Elara's prompt)

### Step 1-3 — Standard (24x36", `#1A1F2E` background, standard font stack)

### Step 4 — Color palette

Standard series palette. Additional usage notes:
- Amber for critical/high-frequency tests
- Teal for instrument-based methods
- Emerald for routine/preventive testing
- Coral for failure indicators and missed-test warnings

### Step 5 — Ruler guides

**Horizontal guides:**
- 0.5" / 2.9" / 11.0" / 13.5" / 22.5" / 27.5" / 32.5" / 35.5"

---

## Part 3 — Layout Zones and Build Order

```
ZONE 1 — HEADER BAND (0"–2.9")
  Block A: Headline + subheading + tagline

ZONE 2 — THE ANALYTICAL TOOLKIT (2.9"–11.0" / ~8.1" tall)
  Block B: Six method cards (HERO) — the analysis methods available
  Block C: Method hierarchy callout ("which method for which question")

ZONE 3 — THE HULL CELL: YOUR DAILY DIAGNOSTIC (11.0"–13.5" / ~2.5" tall)
  Block CC: Hull cell as the universal diagnostic — bridge to Poster #4

ZONE 4 — ANALYSIS FREQUENCY MATRIX (13.5"–22.5" / ~9.0" tall)
  Block D: Comprehensive "what to test, how often" table by process

ZONE 5 — SAMPLING AND TECHNIQUE (22.5"–27.5" / ~5.0" tall)
  Block E: Proper sampling procedure (left half)
  Block F: Common analytical errors (right half)

ZONE 6 — THE BUSINESS CASE FOR ANALYSIS (27.5"–32.5" / ~5.0" tall)
  Block G: Cost of testing vs. cost of not testing
  Block H: Building an analysis program callout

ZONE 7 — FOOTER BAND (32.5"–36.0" / ~3.5" tall)
  Block J: Standard footer
```

---

## Part 4 — Zone-by-Zone Build Specifications

### ZONE 1 — Header Band

**BLOCK A — Headline**

- Font: Barlow Condensed ExtraBold, 78 pt, `#F0EDE8`
- Text (all caps):

> BATH ANALYSIS METHODS

**BLOCK A — Subheading**

- Font: Barlow SemiBold, 34 pt, `#2EC4B6` (Teal)
- Text:

> What to Test, How Often, and Why It Matters

**BLOCK A — Tagline**

- Font: Barlow SemiBold, 22 pt, `#F0EDE8` at 65%
- Text:

> If you didn't test it, you don't know it. If you don't know it, you can't control it.

---

### ZONE 2 — The Analytical Toolkit (HERO)

**Dimensions:** Y: 2.9" to 11.0" (~8.1" tall).

---

**Section label:**
- Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text:

> THE SIX ESSENTIAL ANALYSIS METHODS

---

**BLOCK B — Six Method Cards**

Y: 3.6" to 9.0" (~5.4" tall). Six cards in a 3x2 grid.

Each card: Width: 7.33". Height: 2.5". Fill: `#1E2435`. Corner radius: 6 pt.
Column gap: 0.25". Row gap: 0.25".

Row 1 Y: 3.6". Row 2 Y: 6.4".

| Position | Accent | Method | Description | What It Tells You |
|---|---|---|---|---|
| R1C1 (X: 0.5") | `#E8A020` | `TITRATION` | Classic wet chemistry. Add a reagent drop by drop until a color change signals the endpoint. EDTA titration for metals, acid-base for pH chemicals, iodometric for oxidizers. | Metal concentration (Ni, Cu, Zn), acid/alkali content, oxidizer levels. The backbone of bath analysis. |
| R1C2 (X: 8.0") | `#2EC4B6` | `pH MEASUREMENT` | Electrode-based. Immerse calibrated pH probe in sample. Fastest and most frequently used measurement in the shop. | Hydrogen ion concentration. Critical for every plating bath, every day. See Poster #12. |
| R1C3 (X: 15.5") | `#27AE60` | `HULL CELL` | Electrochemical. Plate a test panel from a sample of the bath at controlled conditions. Read the panel for brightness, coverage, burning, pitting. | Overall bath health — the only test that shows you the deposit itself. See Poster #4. |
| R2C1 (X: 0.5") | `#2EC4B6` | `SPECIFIC GRAVITY` | Physical measurement. Hydrometer or digital SG meter in a sample. Quick, non-destructive. | Total dissolved solids (indirect). Useful for monitoring concentration trends and detecting dilution. |
| R2C2 (X: 8.0") | `#E8A020` | `ATOMIC ABSORPTION (AA) / ICP-OES` | Instrumental. Sample is aspirated into a flame or plasma. Measures individual metals at ppm level. Requires laboratory equipment. | Trace metal contamination (Cu, Zn, Fe, Pb, Cr in nickel). Also primary metals at high precision. The gold standard for contaminant detection. |
| R2C3 (X: 15.5") | `#E05C5C` | `SPECTROPHOTOMETRY / COLORIMETRY` | Instrumental. Chemical reagent produces a color proportional to analyte concentration. Measured by light absorption. | Specific ions (Cr⁶⁺, Fe²⁺/Fe³⁺, cyanide). Useful for process-specific tests where titration is impractical. |

Card title: Barlow Condensed ExtraBold, 20 pt, accent color.
Description: Inter Regular, 13 pt, `#F0EDE8`.
"What it tells you": Inter Medium, 12 pt, accent color.
Left-border accent: 0.06" wide, accent color.

---

**BLOCK C — Method Hierarchy Callout**

Y: 9.3" to 10.8" (~1.5" tall).

- Element type: Rounded rectangle
- Width: 23.0". Height: 1.3". Fill: `#252B3D`. Corner radius: 4 pt.

Three data points spaced evenly:

| Level | Color | Text |
|---|---|---|
| Daily / Every Shift | `#E8A020` | `pH + temperature + Hull cell = your daily minimum` |
| Weekly / Bi-Weekly | `#2EC4B6` | `Titration (metal conc.) + SG + additive check` |
| Monthly / As Needed | `#E05C5C` | `AA/ICP contaminant scan + full chemistry audit` |

Font: Inter Medium, 15 pt, respective colors.
Separator lines between the three levels: 1 pt, `#3A4055`.

---

### ZONE 3 — The Hull Cell: Your Daily Diagnostic

**Dimensions:** Y: 11.0" to 13.5" (~2.5" tall).

---

**BLOCK CC — Hull Cell Bridge**

A single wide callout box — serves as a bridge between Poster #4 (Hull Cell) and this poster's analysis framework.

- Width: 23.0". Height: 2.0". Fill: `#1E2435`. Corner radius: 6 pt. Left-border: `#27AE60`.

Title: `THE HULL CELL IS YOUR MOST POWERFUL DAILY DIAGNOSTIC` — Barlow SemiBold, 20 pt, `#27AE60`

Body (Inter Regular, 16 pt, `#F0EDE8`, line height 140%):

> No single test tells you more about your bath's health than a Hull cell panel. It integrates every variable — metal concentration, additive balance, contamination, pH, temperature — into one visual result you can read in 30 seconds. Run one every shift on critical baths. If you can only do one test, make it this one.

Key data strip below body text:
- JetBrains Mono Regular, 14 pt, `#27AE60`

> Standard conditions: 267 mL sample | 2 A (standard for most baths — some processes use 1A, 3A, or 5A; consult your supplier's test procedure) | 5-10 min | Bath temperature | Brass or steel cathode per process

Cross-reference: `For panel interpretation, see Poster #4 — Reading Your Hull Cell Panel` — Inter Regular, 13 pt, `#F0EDE8` at 50%

---

### ZONE 4 — Analysis Frequency Matrix

**Dimensions:** Y: 13.5" to 22.5" (~9.0" tall). This is the poster's primary reference table.

---

**Section label:**
- Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text:

> THE ANALYSIS SCHEDULE — WHAT TO TEST AND WHEN

---

**BLOCK D — Analysis Frequency Table**

Y: 14.2" to 22.3" (~8.1" tall).

This is a wide, detailed table. Column structure:

| Column | Width | Header |
|---|---|---|
| Process | 3.5" | `Process` |
| pH | 2.0" | `pH` |
| Metal Conc. | 2.5" | `Metal` |
| Additives | 2.5" | `Additives` |
| Hull Cell | 2.0" | `Hull Cell` |
| SG | 1.5" | `SG` |
| Contaminants | 2.5" | `Contaminants` |
| Temperature | 2.0" | `Temp` |
| Special | 4.5" | `Special Tests` |

Total: 23.0"

Header row: Fill `#3A4055`. Barlow SemiBold, 13 pt, `#F0EDE8`.

Frequency coding (color-coded text):
- `Every shift` or `Daily` = `#E8A020` (Amber) — critical
- `Weekly` or `2x/week` = `#2EC4B6` (Teal) — routine
- `Monthly` = `#27AE60` (Emerald) — periodic
- `As needed` = `#F0EDE8` at 60% — situational

| Process | pH | Metal | Additives | Hull Cell | SG | Contaminants | Temp | Special |
|---|---|---|---|---|---|---|---|---|
| Watts nickel (bright) | Every shift | Weekly (NiSO₄, NiCl₂, H₃BO₃) | Per Hull cell (brightener, carrier, wetter) | Every shift | Weekly | Monthly (AA: Cu, Zn, Fe, Pb) | Every shift | Surface tension (weekly) |
| Acid copper sulfate | — (strongly acidic — pH not meaningful; monitor free H₂SO₄ by titration) | Weekly (CuSO₄, H₂SO₄) | Per Hull cell | Every shift | Bi-weekly | Monthly (AA: Cl⁻, Fe, organics) | Every shift | Chloride (weekly) |
| Hard chrome | Daily | Weekly (CrO₃, SO₄²⁻) | N/A | Weekly or as needed | Weekly | Monthly (Fe, Cu, trivalent Cr) | Every shift | CrO₃:SO₄ ratio (daily in production — this is the single most critical hard chrome parameter) |
| Acid zinc (chloride) | Daily | Weekly (Zn, KCl or NaCl) | Per Hull cell | Daily | Weekly | Monthly (Cu, Fe, Pb) | Daily | Baume (daily) |
| Alkaline zinc (non-CN) | Daily | Weekly (Zn, NaOH) | Per Hull cell | Daily | Weekly | Monthly (Cu, Fe, carbonate) | Daily | Carbonate (monthly) |
| Electroless nickel | Every 2-4 hr (active plating) | Every 2-4 hr or before each load (Ni, NaH₂PO₂) | N/A | Per lot | Every shift | Bi-weekly (metals, stabilizer) | Continuous | MTO tracking (replenish by area plated, not time) |
| Gold (acid) | Daily | Daily (Au) | Per Hull cell | Per lot | Weekly | Monthly (base metals) | Every shift | Gold content = money — track closely |
| Silver (cyanide) | Daily | Weekly (Ag, free CN) | Per Hull cell | Weekly | Weekly | Monthly (Cu, carbonates) | Daily | Free cyanide ratio critical |

Data font: Inter Regular, 12 pt. Process names: Inter Medium, 13 pt, `#F0EDE8`. Alternating rows: `#1E2435` / `#252B3D`.

---

### ZONE 5 — Sampling and Technique

**Dimensions:** Y: 22.5" to 27.5" (~5.0" tall).

---

**BLOCK E — Proper Sampling Procedure** (left half)

Callout container: Width: 11.0". Height: 4.5". Fill: `#1E2435`. Left-border: `#27AE60`.

Title: `HOW TO TAKE A GOOD SAMPLE` — Barlow SemiBold, 20 pt, `#27AE60`

Numbered steps (Inter Regular, 15 pt, `#F0EDE8`, line height 145%):

> 1. **Sample from a representative location** — mid-tank, mid-depth. Not at the surface (concentration stratification). Not near a heater or sparger.
> 2. **Use clean, dedicated labware** — glass or polyethylene. Never share containers between different baths. Rinse with DI water, then rinse with the bath solution, then take the sample.
> 3. **Sample at operating temperature** — results at room temp may not reflect hot-bath chemistry.
> 4. **Filter particulates if required** — for AA/ICP analysis, filter through 0.45 micron membrane. For titration, typically unfiltered.
> 5. **Label immediately** — bath name, date, time, operator. An unlabeled sample is a wasted sample.
> 6. **Analyze promptly** — some constituents change with time (dissolved gases, unstable complexes).

---

**BLOCK F — Common Analytical Errors** (right half)

Callout container: Width: 11.5". Height: 4.5". Fill: `#1E2435`. Left-border: `#E05C5C`.

Title: `COMMON ERRORS THAT GIVE BAD RESULTS` — Barlow SemiBold, 20 pt, `#E05C5C`

Bullets (Inter Regular, 15 pt, `#F0EDE8`, line height 145%):

> - **Stale pH calibration** — calibrate pH meter DAILY with fresh buffers. Old buffer = wrong reading.
> - **Wrong indicator** — using the wrong endpoint indicator for a titration gives the wrong answer. Follow the procedure exactly.
> - **Contaminated glassware** — a pipette rinsed in nickel solution then used for copper gives a nickel reading in the copper bath.
> - **Ignoring temperature correction** — SG and some titrations are temperature-dependent. Correct to standard temperature per method.
> - **Sampling from the surface** — evaporation concentrates the surface layer. Sample from depth.
> - **Rushing the Hull cell** — incomplete deposition time, wrong amperage, or a dirty cathode panel all invalidate the result.

Key callout (JetBrains Mono Regular, 13 pt, `#E05C5C`):

> A wrong analytical result is worse than no result — it tells you the wrong thing with confidence.

---

### ZONE 6 — The Business Case for Analysis

**Dimensions:** Y: 27.5" to 32.5" (~5.0" tall).

---

**BLOCK G — Cost of Testing vs. Not Testing** (left half)

Callout container: Width: 11.0". Height: 4.5". Fill: `#1E2435`. Left-border: `#E8A020`.

Title: `THE MATH IS SIMPLE` — Barlow SemiBold, 20 pt, `#E8A020`

Body (Inter Regular, 16 pt, `#F0EDE8`, line height 145%):

> **Cost of a daily Hull cell test:**
> ~$0.50 in panel + solution + 15 minutes of technician time
>
> **Cost of a production run with an out-of-spec bath:**
> Scrap parts, rework time, re-plating, customer complaints, delivery delays, reputation damage
>
> **The ratio:** Prevention costs pennies. Reaction costs dollars.
>
> A $5/day testing program prevents $5,000 reject events. That is not an opinion — it is the lived experience of every plating shop that has tried both approaches.

Key stat (JetBrains Mono Regular, 16 pt, `#E8A020`):

> Testing budget target: 1-3% of total plating chemical spend

---

**BLOCK H — Building an Analysis Program** (right half)

Callout container: Width: 11.5". Height: 4.5". Fill: `#1E2435`. Left-border: `#27AE60`.

Title: `STARTING FROM ZERO? BUILD IN THIS ORDER` — Barlow SemiBold, 18 pt, `#27AE60`

Numbered list (Inter Regular, 15 pt, `#F0EDE8`, line height 145%):

> 1. **pH meter and buffers** — measure every bath, every day. Cost: ~$200.
> 2. **Hull cell kit** — 267 mL cell, DC supply, panels. Run daily on critical baths. Cost: ~$300.
> 3. **Titration kit** — burette, standards, indicators for your primary metals. Run weekly. Cost: ~$500.
> 4. **Hydrometer set** — specific gravity daily. Cost: ~$50.
> 5. **Thermometer (calibrated)** — measure temperature at start and end of every shift. Cost: ~$75.
> 6. **Send out for AA/ICP** — monthly contaminant scans. Use a commercial lab until volume justifies in-house. Cost: ~$50-150/sample.

Total startup: `~$1,200 + $100/month lab outsourcing = comprehensive bath control` — JetBrains Mono Regular, 13 pt, `#27AE60`

---

### ZONE 7 — Footer Band

Standard footer per series convention.

**Disclaimer:**
> This poster is an educational reference tool. Analysis methods, frequencies, and procedures are typical industry values and general best practices. Specific analytical requirements vary by bath chemistry, proprietary formulations, customer specifications, and regulatory obligations. Consult your chemical supplier, quality specifications, and laboratory procedures for application-specific analysis requirements.

**Poster title:** Bath Analysis Methods — What to Test, How Often, and Why It Matters

**Version:** v1.0 — 2026

---

## Part 5 — Grouping and Naming Convention

| Group Name | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline |
| Zone 2 - Analytical Toolkit | Section label, six method cards, method hierarchy callout |
| Zone 3 - Hull Cell Bridge | Hull cell daily diagnostic callout |
| Zone 4 - Frequency Matrix | Section label, analysis frequency table |
| Zone 5 - Sampling and Technique | Proper sampling procedure, common errors |
| Zone 6 - Business Case | Cost comparison, building an analysis program |
| Zone 7 - Footer | Standard footer elements |

---

## Part 6 — Light Edition Color Remap Table

Standard remap per series convention. No special notes.

---

## Part 7 — Export Checklist

Standard six files. File name prefix: `Bath Analysis Methods`

The analysis frequency matrix (Zone 4) is the widest table in the series — 9 columns across 23". At 18x24" resize, font sizes will be tight. Elara should test readability at that scale and flag if any column drops below 11 pt after resize.

---

## Design Notes

This is a fitting capstone for the initial 30-poster series. It ties together themes from at least five other posters (Hull Cell, pH Control, Metallic Contamination, Filtration, and Temperature Control) into an overarching framework: analytical discipline is the thread that connects every process variable.

The two Tyler flags are particularly important for this poster. Tyler's actual lab practice is the closest thing we have to ground truth for analysis frequencies. The published "recommended frequencies" in industry guides are sometimes aspirational — Tyler can tell us what a well-run lab actually does, which is more honest and more useful for the poster audience.

The "Building an Analysis Program" callout (Zone 6) is deliberately structured as a budget-friendly progression. Many small plating shops believe that analytical control requires a $100,000 lab — this poster shows that comprehensive bath control starts at $1,200. That message has commercial value for the poster product itself: it positions Plating Posters Inc as a company that understands and serves the small-to-medium shop market.

The business case section is unusual for the series — it's the only poster that directly argues ROI. I included it because bath analysis is uniquely vulnerable to budget cuts ("we'll save money by testing less"). Making the cost-of-not-testing argument visible on the wall gives the lab technician ammunition when the cost question comes up.

---

*Alaina — Plating Posters Inc Creative Lead*
*Poster #30 — Bath Analysis Methods — Construction Workup v1.0*
*2026-04-24*
