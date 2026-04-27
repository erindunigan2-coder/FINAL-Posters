---
Project: Plating Posters Inc
Poster Number: 30
Title: "Bath Analysis Methods -- What to Test, How Often, and Why It Matters"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-25T00:00:00
Source: Poster 30 -- Bath Analysis Methods -- Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - BathAnalysis
  - Titration
  - HullCell
  - QualityControl
  - LaboratoryMethods
  - Series1Capstone
  - v1
---

# Claude Chat Generation Prompt -- Poster #30
## Bath Analysis Methods -- What to Test, How Often, and Why It Matters
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-25).*

---

> **IMPORTANT:** Generate as HTML visual artifact. 24 x 36" portrait. Dark edition first. This is the capstone poster of the initial 30-poster series and the most table-dense poster in the library. The analysis frequency matrix (Zone 4) has 9 columns -- readability at scale is critical.

---

## Phase 0 -- Design System Reference

This poster follows the **Plating Posters Inc Metal Finishing Reference Series** design system. Canonical spec: `Plating Posters - Series Design Prompt.md`. Key rules:

- **Stage:** 1200x1800 CSS px in `.stage`, scaled via `transform: scale()`
- **Fonts (Google CDN):** Barlow Condensed 800/900, Barlow 600/700, Inter 400/500/600, JetBrains Mono 400/500
- **Palette:** `#1A1F2E` bg, `#F0EDE8` text, `#E8A020` amber, `#2EC4B6` teal, `#27AE60` emerald, `#E05C5C` coral, `#3A4055` slate, `#0D1020` navy, `#1E2435` callout, `#252B3D` altrow, `#C8D0D8` silver
- **Glass surfaces:** `rgba(30,36,53,.55)` solid fallback + gradient + border + `backdrop-filter` on EVERY card. NEVER `color-mix()`. NEVER opacity on pseudo-elements.
- **Background:** three ambient orbs (teal 14%, amber 12%, coral 10%) + faint 50x50 grid with radial mask
- **Print CSS:** `@page { size: 12.5in 18.75in; margin:0; }` + all print-safe rules per design system
- **Tweaks panel:** floating bottom-right, Dark/Light + Grid + Print
- **Light edition:** `body[data-edition="light"]` CSS overrides
- **Safe zones:** 25px padding inside poster frame. Footer full-bleed.
- **Icons:** inline SVG only, 1.5-2px monoline stroke, `currentColor`
- **Copy voice:** blunt, direct, workshop-floor-wise. No marketing fluff. No emoji.

**Technical standards note:** Hull cell standard reference is **IPC-TM-650 Method 2.4.18.1** (NOT ASTM B750 -- which covers Galfan wire coating and is not relevant).

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E`, locked palette, 0.5" safe zone equivalent (25px at CSS scale).

---

## Phase 2 -- Header (Zone 1)

### Step 1 -- `BATH ANALYSIS METHODS` -- `78` pt Barlow Condensed 800 `#F0EDE8`. Large, commanding.
### Step 2 -- `What to Test, How Often, and Why It Matters` -- `30` pt Barlow 600 `#2EC4B6`.
### Step 3 -- `If you didn't test it, you don't know it. If you don't know it, you can't control it.` -- `20` pt italic, `#F0EDE8` at 65%.

No rule card on this poster -- the frequency matrix IS the hero data element.

---

## Phase 3 -- The Analytical Toolkit (Zone 2 -- HERO)

Section label: `THE SIX ESSENTIAL ANALYSIS METHODS` -- Barlow Condensed 800 28px, centered.

### Step 4 -- Six method cards (3x2 grid)

Each card: glass surface, ~7.33" wide at full scale, accent left-border strip.

| Position | Accent | Method | Type | Description | Key Insight |
|---|---|---|---|---|---|
| R1C1 | `#E8A020` | TITRATION | Classic wet chemistry | EDTA for metals, acid-base for pH chemicals, iodometric for oxidizers. Add reagent drop by drop until color change signals endpoint. | Metal concentration (Ni, Cu, Zn), acid/alkali content, oxidizer levels. The backbone of bath analysis. |
| R1C2 | `#2EC4B6` | pH MEASUREMENT | Electrode-based | Fastest and most frequently used measurement in the shop. Immerse calibrated probe in sample. | Hydrogen ion concentration. Critical for every bath, every day. Calibrate daily with fresh buffers. |
| R1C3 | `#27AE60` | HULL CELL | Electrochemical | Plate a test panel from bath sample at controlled conditions. Read panel for brightness, coverage, burning, pitting. | The ONLY test that shows the actual deposit. Standard: 267 mL, 2 A (most baths -- some use different amperage; consult supplier), 5-10 min, bath temp, brass or steel cathode. |
| R2C1 | `#2EC4B6` | SPECIFIC GRAVITY | Physical measurement | Hydrometer or digital SG meter. Quick, non-destructive. | Total dissolved solids (indirect). Monitors concentration trends and detects dilution. |
| R2C2 | `#E8A020` | AA / ICP-OES | Instrumental | Sample aspirated into flame or plasma. Measures individual metals at ppm level. | Trace metal contamination at high precision. The gold standard for contaminant detection. Requires lab equipment. |
| R2C3 | `#E05C5C` | SPECTROPHOTOMETRY | Colorimetric | Reagent produces color proportional to analyte concentration. Measured by light absorption. | Specific ions: Cr6+, Fe2+/Fe3+, cyanide. Process-specific tests where titration is impractical. |

Card title: Barlow Condensed 800 20pt, accent color.
Description: Inter 400 13pt `#F0EDE8`.
Key insight: Inter 500 12pt, accent color, with `border-left: 2px solid accent`.

### Step 5 -- Method Hierarchy Strip

Full-width glass strip below cards. Three levels, separated by 1pt `#3A4055` dividers:

| Level | Color | Text |
|---|---|---|
| Every shift / Daily | `#E8A020` | `pH + temperature + Hull cell = your daily minimum` |
| Weekly / Bi-weekly | `#2EC4B6` | `Titration (metal conc.) + SG + additive check` |
| Monthly / As needed | `#E05C5C` | `AA/ICP contaminant scan + full chemistry audit` |

Inter 500 15pt, respective colors.

---

## Phase 4 -- The Hull Cell Bridge (Zone 3)

### Step 6 -- Single wide glass card, emerald left-border

Title: `THE HULL CELL IS YOUR MOST POWERFUL DAILY DIAGNOSTIC` -- Barlow 600 20pt `#27AE60`.

Body (Inter 400 16pt `#F0EDE8`):
> No single test tells you more about your bath's health than a Hull cell panel. It integrates every variable -- metal concentration, additive balance, contamination, pH, temperature -- into one visual result you can read in 30 seconds. Run one every shift on critical baths. If you can only do one test, make it this one.

Key data (JetBrains Mono 400 14pt `#27AE60`):
> Standard conditions: 267 mL sample | 2 A (most baths; some processes use different amperage -- consult your chemical supplier's test procedure) | 5-10 min | Bath temperature | Brass or steel cathode per process

Cross-reference (Inter 400 13pt `#F0EDE8` at 50%):
> For panel interpretation, see Poster #4 -- Reading Your Hull Cell Panel

---

## Phase 5 -- Analysis Frequency Matrix (Zone 4)

Section label: `THE ANALYSIS SCHEDULE -- WHAT TO TEST AND WHEN` -- Barlow Condensed 800 28px, centered.

### Step 7 -- Frequency table (9 columns, 8 process rows)

This is the poster's primary reference value and the widest table in the series.

**Column headers** (Barlow 600 13pt `#F0EDE8`, fill `#3A4055`):
`Process | pH | Metal | Additives | Hull Cell | SG | Contaminants | Temp | Special Tests`

**Frequency color coding:**
- Every shift / Daily = `#E8A020` (amber)
- Weekly / Bi-weekly = `#2EC4B6` (teal)
- Monthly = `#27AE60` (emerald)
- As needed / situational = `#F0EDE8` at 60%

**Row data** (Inter 400 12pt, process names Inter 500 13pt `#F0EDE8`, alternating rows `#1E2435` / `#252B3D`):

| Process | pH | Metal | Additives | Hull Cell | SG | Contaminants | Temp | Special |
|---|---|---|---|---|---|---|---|---|
| Watts nickel (bright) | Every shift | Weekly (NiSO4, NiCl2, H3BO3) | Per Hull cell | Every shift | Weekly | Monthly (AA: Cu, Zn, Fe, Pb) | Every shift | Surface tension (weekly) |
| Acid copper sulfate | -- (strongly acidic; monitor free H2SO4 by titration) | Weekly (CuSO4, H2SO4) | Per Hull cell | Every shift | Bi-weekly | Monthly (AA: Cl-, Fe, organics) | Every shift | Chloride (weekly) |
| Hard chrome | Daily | Weekly (CrO3, SO4 2-) | N/A | Weekly or as needed | Weekly | Monthly (Fe, Cu, trivalent Cr) | Every shift | CrO3:SO4 ratio (DAILY -- most critical hard chrome parameter) |
| Acid zinc (chloride) | Daily | Weekly (Zn, KCl/NaCl) | Per Hull cell | Daily | Weekly | Monthly (Cu, Fe, Pb) | Daily | Baume/SG (daily) |
| Alkaline zinc (non-CN) | Daily | Weekly (Zn, NaOH) | Per Hull cell | Daily | Weekly | Monthly (Cu, Fe, carbonate) | Daily | Carbonate (monthly) |
| Electroless nickel | Every 2-4 hr (active plating) | Every 2-4 hr or before each load (Ni, NaH2PO2) | N/A | Per lot | Every shift | Bi-weekly (metals, stabilizer) | Continuous | MTO tracking (replenish by area plated, not time) |
| Gold (acid) | Daily | Daily (Au) | Per Hull cell | Per lot | Weekly | Monthly (base metals) | Every shift | Gold content = money -- track closely |
| Silver (cyanide) | Daily | Weekly (Ag, free CN) | Per Hull cell | Weekly | Weekly | Monthly (Cu, carbonates) | Daily | Free cyanide ratio critical |

**CRITICAL CORRECTIONS -- verify these are implemented:**
- Acid copper pH = "--" with note (NOT "Daily") -- strongly acidic bath, pH measurement not meaningful
- Watts nickel pH = "Every shift" (NOT "Daily")
- Hard chrome Hull cell = "Weekly or as needed" (NOT "Every shift")
- Hard chrome Special = CrO3:SO4 ratio is DAILY in production
- EN analysis = "Every 2-4 hr or before each load" (NOT standard weekly)
- Hull cell amperage = some processes use different amperages (1A, 3A, 5A) -- note this
- Zero brand names anywhere in the table

---

## Phase 6 -- Sampling and Technique (Zone 5)

Two-column layout.

### Step 8 -- Left: HOW TO TAKE A GOOD SAMPLE

Glass card, emerald left-border. Title: Barlow 600 20pt `#27AE60`.

6 numbered steps (Inter 400 15pt `#F0EDE8`):
1. **Sample from a representative location** -- mid-tank, mid-depth. Not surface. Not near heater or sparger.
2. **Use clean, dedicated labware** -- glass or polyethylene. Rinse with DI water, then bath solution, then sample.
3. **Sample at operating temperature** -- room temp results may not reflect hot-bath chemistry.
4. **Filter if required** -- 0.45 micron membrane for AA/ICP. Typically unfiltered for titration.
5. **Label immediately** -- bath name, date, time, operator. Unlabeled sample = wasted sample.
6. **Analyze promptly** -- some constituents change with time (dissolved gases, unstable complexes).

### Step 9 -- Right: COMMON ERRORS THAT GIVE BAD RESULTS

Glass card, coral left-border. Title: Barlow 600 20pt `#E05C5C`.

6 bullets (Inter 400 15pt `#F0EDE8`):
- **Stale pH calibration** -- calibrate DAILY with fresh buffers. Old buffer = wrong reading.
- **Wrong indicator** -- wrong endpoint indicator = wrong answer. Follow the procedure exactly.
- **Contaminated glassware** -- pipette rinsed in nickel then used for copper = nickel in the copper reading.
- **Ignoring temperature correction** -- SG and some titrations are temperature-dependent.
- **Sampling from the surface** -- evaporation concentrates the surface layer. Sample from depth.
- **Rushing the Hull cell** -- wrong time, wrong amperage, dirty panel = invalid result.

Key callout (JetBrains Mono 400 13pt `#E05C5C`):
> A wrong analytical result is worse than no result -- it tells you the wrong thing with confidence.

---

## Phase 7 -- The Business Case for Analysis (Zone 6)

Two-column layout.

### Step 10 -- Left: THE MATH IS SIMPLE

Glass card, amber left-border. Title: Barlow 600 20pt `#E8A020`.

Body (Inter 400 16pt `#F0EDE8`):
> **Cost of a daily Hull cell test:** ~$0.50 in panel + solution + 15 minutes of technician time
>
> **Cost of a production run with an out-of-spec bath:** Scrap parts, rework, re-plating, customer complaints, delivery delays, reputation damage
>
> **The ratio:** Prevention costs pennies. Reaction costs dollars.
>
> A $5/day testing program prevents $5,000 reject events. That is not an opinion -- it is the lived experience of every plating shop that has tried both approaches.

Key stat (JetBrains Mono 400 16pt `#E8A020`):
> Testing budget target: 1-3% of total plating chemical spend

### Step 11 -- Right: STARTING FROM ZERO? BUILD IN THIS ORDER

Glass card, emerald left-border. Title: Barlow 600 18pt `#27AE60`.

6 numbered items (Inter 400 15pt `#F0EDE8`):
1. **pH meter and buffers** -- measure every bath, every day. Cost: ~$200-500.
2. **Hull cell kit** -- 267 mL cell, DC supply, panels. Run daily. Cost: ~$300.
3. **Titration kit** -- burette, standards, indicators. Run weekly. Cost: ~$500.
4. **Hydrometer set** -- specific gravity daily. Cost: ~$50.
5. **Thermometer (calibrated)** -- every shift. Cost: ~$75.
6. **Send out for AA/ICP** -- monthly contaminant scans. Cost: ~$50-150/sample.

Total (JetBrains Mono 400 13pt `#27AE60`):
> ~$1,200 + $100/month lab outsourcing = comprehensive bath control

---

## Phase 8 -- Footer (Zone 7)

Standard dark navy glass footer per design system.

**Disclaimer:** This poster is an educational reference tool. Analysis methods, frequencies, and procedures are typical industry values and general best practices. Specific requirements vary by bath chemistry, proprietary formulations, customer specifications, and regulatory obligations. Consult your chemical supplier, quality specifications, and laboratory procedures for application-specific requirements.

**Title:** Bath Analysis Methods -- What to Test, How Often, and Why It Matters
**Version:** v1.0 -- 2026 | Poster #30 -- Bath Analysis Methods | Plating Posters Inc

---

## Phase 9 -- Review Checklist

- [ ] Headline `BATH ANALYSIS METHODS` 78pt warm white
- [ ] Subheading teal, tagline muted
- [ ] Six method cards in 3x2 grid with correct accent colors
- [ ] Method hierarchy strip (3 levels, color-coded)
- [ ] Hull cell bridge card with emerald border and cross-reference to Poster #4
- [ ] Hull cell amperage note: "some processes use different amperage"
- [ ] Analysis frequency matrix: 9 columns, 8 process rows
- [ ] Acid copper pH = "--" with note (NOT "Daily")
- [ ] Watts nickel pH = "Every shift" (NOT "Daily")
- [ ] Hard chrome Hull cell = "Weekly or as needed"
- [ ] Hard chrome CrO3:SO4 = "daily in production"
- [ ] EN frequency = "every 2-4 hr or before each load"
- [ ] Frequency color coding: amber/teal/emerald/muted white
- [ ] Sampling procedure (6 steps, emerald)
- [ ] Common errors (6 bullets + callout, coral)
- [ ] Business case: cost comparison + build order with price estimates
- [ ] Footer with disclaimer, version, poster number
- [ ] Glass surfaces on all cards with solid fallback
- [ ] Ambient orbs + grid background
- [ ] Light edition via data-edition toggle
- [ ] Tweaks panel functional
- [ ] Print CSS correct
- [ ] Zero brand names anywhere
- [ ] Hull cell standard = IPC-TM-650 Method 2.4.18.1 (NOT ASTM B750)

---

## Phase 10 -- Light Remap & Export

Standard remap per design system. `body[data-edition="light"]` overrides built into the HTML.

Six export files: `Bath Analysis Methods -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-25 | Initial. Capstone poster for the 30-poster series. |
