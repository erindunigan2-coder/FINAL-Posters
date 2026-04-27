---
Project: Plating Posters Inc
Poster Number: 26
Title: "Chromate and Conversion Coatings -- Hex, Tri, and Beyond"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-25T00:00:00
Source: Poster 26 -- Chromate and Conversion Coatings -- Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - ChromateConversion
  - Trivalent
  - Hexavalent
  - RoHS
  - Passivation
  - v1
---

# Claude Chat Generation Prompt -- Poster #26
## Chromate and Conversion Coatings -- Hex, Tri, and Beyond
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-25).*

---

> **IMPORTANT:** Generate as a single self-contained HTML file (visual artifact). 24 x 36" portrait. Dark edition first. This poster is the most regulatory-sensitive in the series -- accuracy on RoHS scope, self-healing claims, and SST performance ranges is critical. Reference the canonical Series Design Prompt (`Plating Posters - Series Design Prompt.md`) for visual identity, glass surfaces, layout system, scaling, tweaks panel, and print CSS.

---

## Phase 0 -- Design System Reference

Before building, internalize the full Series Design Prompt. Key rules that govern this poster:

- **Palette:** `--bg: #1A1F2E`, `--text: #F0EDE8`, `--amber: #E8A020`, `--teal: #2EC4B6`, `--emerald: #27AE60`, `--coral: #E05C5C`, `--slate: #3A4055`, `--navy: #0D1020`, `--callout: #1E2435`, `--altrow: #252B3D`, `--silver: #C8D0D8`
- **Glass surfaces:** `rgba(30,36,53,.55)` solid fallback + gradient + border + backdrop-filter + box-shadow on every card. NEVER `color-mix()`.
- **Background:** Three ambient orbs (teal top-left, amber top-right, coral bottom-center) + faint 50x50px grid with radial mask.
- **Fonts (CDN):** Barlow Condensed 800/900, Barlow 600/700, Inter 400/500/600, JetBrains Mono 400/500.
- **Scaling:** `.stage` flex container wrapping a fixed 1200x1800 CSS px `.poster`. Scale-to-fit via `transform: scale()`.
- **Print CSS:** `@page { size: 12.5in 18.75in; margin: 0; }` + all print-safe fallbacks per design prompt.
- **Tweaks panel:** Floating bottom-right. Dark/Light toggle + Grid On/Off + Print button.
- **Light edition:** `body[data-edition="light"]` CSS overrides per CW remap table.

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E`, locked palette, 25px safe zone inside poster frame. Footer full-bleed (negative margins).

---

## Phase 2 -- Header (Zone 1)

### Step 1 -- Headline
`CHROMATE AND CONVERSION COATINGS` -- Barlow Condensed 800, large (80-96px), `#F0EDE8`. Y: top of poster inside safe zone.

### Step 2 -- Subheading
`Hexavalent, Trivalent, and Beyond -- The Final Line of Defense` -- Barlow 600, 28-32px, `#E8A020`. Below headline.

### Step 3 -- Regulatory Hero Callout
Full-width coral glass banner spanning the header zone:
- Glass card with coral tint (coral border, coral-tinted background at ~12%)
- Text centered: `HEXAVALENT CHROMIUM IS A KNOWN CARCINOGEN -- REGULATORY RESTRICTIONS ARE INCREASING WORLDWIDE`
- Barlow Condensed 800, 18-20px, `#E05C5C`
- This callout is intentionally prominent -- it builds credibility by not shying away from the health reality.

---

## Phase 3 -- Coating Types at a Glance (Zone 2 -- HERO)

Section label: `THE COATING TYPES AT A GLANCE` -- Barlow Condensed 800, 28px, centered.

### Step 4 -- Four Coating Type Cards

Four glass cards arranged in a row (2x2 or 1x4 as space allows). Each card has an accent border color: amber for hexavalent types, teal for trivalent types.

**Card 1 -- HEX CLEAR / BLUE** (amber border):
- Title: `HEX CLEAR / BLUE` in `#E8A020`
- Cross-section diagram: three stacked CSS rectangles:
  - Bottom: `#3A4055` labeled `SUBSTRATE`
  - Middle: `#C8D0D8` labeled `ZINC`
  - Top: pale blue-tinted `#B8D8E8` at 50% -- thin layer
- Data (JetBrains Mono): `Film: 0.05-0.25 um` | `SST: 8-24 hrs` | `RoHS: NON-COMPLIANT` (coral badge `#E05C5C`)

**Card 2 -- HEX YELLOW / IRIDESCENT** (amber border):
- Title: `HEX YELLOW / IRIDESCENT` in `#E8A020`
- Cross-section: same substrate + zinc, top layer golden amber `#E8A020` at 60% -- thicker
- Data: `Film: 0.25-0.75 um` | `SST: 96-500+ hrs` | `RoHS: NON-COMPLIANT` (coral badge)

**Card 3 -- TRI CLEAR** (teal border):
- Title: `TRI CLEAR` in `#2EC4B6`
- Cross-section: top layer pale teal `#D0E8E4` at 50% -- thin
- Data: `Film: 0.05-0.25 um` | `SST: 24-96 hrs (no sealer) / 96-200+ hrs (with sealer)` | `RoHS: COMPLIANT` (emerald badge `#27AE60`)

**Card 4 -- TRI BLACK** (teal border):
- Title: `TRI BLACK` in `#2EC4B6`
- Cross-section: top layer near-black `#2A2A2A` at 80% -- medium thickness
- Data: `Film: 0.5-1.5 um` | `SST: 96-400 hrs` | `RoHS: COMPLIANT` (emerald badge)

### Step 5 -- Color Appearance Swatch Strip

Below the four cards. A horizontal glass strip with 6 color swatches:

| Swatch | Fill | Label |
|---|---|---|
| 1 | `#D0DFE8` | Clear / Blue-bright |
| 2 | `#D4A830` | Yellow / Iridescent |
| 3 | `#6B702A` | Olive Drab (mil-spec) |
| 4 | `#C8E0D8` | Tri Clear |
| 5 | `#282828` | Tri Black |
| 6 | `#A0B0C0` | + Sealer / Topcoat |

Each swatch: small rounded rectangle with the fill color + label in Inter 400, small size.

---

## Phase 4 -- Mechanism (Zone 3)

Section label: `HOW CONVERSION COATINGS WORK` -- Barlow Condensed 800, 24px, centered.

### Step 6 -- Two Mechanism Callout Boxes (side-by-side)

**Left -- HEXAVALENT MECHANISM** (amber left-border):
- Title: `HEXAVALENT MECHANISM` -- Barlow 600, 18px, `#E8A020`
- Body (Inter 400, 14-15px, `#F0EDE8`):
> Zinc dissolves into the acidic chromate solution. Cr6+ is reduced to Cr3+ at the surface, forming a mixed Cr6+/Cr3+ oxide gel film. The residual Cr6+ in the film provides "self-healing" -- if the film is scratched, soluble Cr6+ migrates to the damaged area and re-forms the barrier.

**Right -- TRIVALENT MECHANISM** (teal left-border):
- Title: `TRIVALENT MECHANISM` -- Barlow 600, 18px, `#2EC4B6`
- Body:
> Similar acid dissolution of zinc surface. Cr3+ precipitates as a chromium (III) oxide/hydroxide film. No Cr6+ present at any stage -- fully RoHS compliant. No self-healing mechanism. Performance enhanced by topcoat sealers (silicate, silane, or organic-based) that add a secondary barrier layer.

---

## Phase 5 -- Head-to-Head Comparison Table (Zone 4)

Section label: `HEAD-TO-HEAD -- HEXAVALENT VS. TRIVALENT` -- Barlow Condensed 800, 28px, centered.

### Step 7 -- Comparison Table

Full-width glass table. Three columns: `Property` | `HEXAVALENT (Cr6+)` | `TRIVALENT (Cr3+)`.

Column headers: Barlow 700. Hex header subtly amber-tinted at 15%; Tri header teal-tinted at 15%.

13 rows (alternating `#1E2435` / `#252B3D`):

| Property | Hexavalent (Cr6+) | Trivalent (Cr3+) |
|---|---|---|
| Active chemistry | Cr6+ (chromic acid based) | Cr3+ (chromium chloride or sulfate based) |
| RoHS status | Non-compliant for EEE. Military, aerospace, industrial may have exemptions -- verify. | RoHS compliant (EEE applications). |
| Self-healing | Yes -- Cr6+ reservoir migrates to damage sites | No -- film is inert once formed |
| Color options | Clear, yellow/iridescent, olive drab, black | Clear, light blue, black (yellow NOT achievable without hex) |
| Salt spray (clear on Zn) | 8-24 hours | Without sealer: 24-96 hrs. With sealer: 96-200+ hrs. |
| Salt spray (high-perf on Zn) | 96-500+ hours | N/A -- no true yellow; black tri: 96-400 hrs |
| Film thickness | 0.05-0.75 um (varies by type) | 0.05-1.5 um (varies by type) |
| Topcoat / sealer | Optional (improves already-good base) | Often required to match hex yellow performance |
| Heat resistance | Degrades > 150 F (65 C) -- Cr6+ converts to Cr3+ | More heat-stable -- no Cr6+ to reduce |
| Torque tension | Well-characterized, predictable | Can vary -- test with fastener coatings |
| Bath life | Long -- forgiving, self-replenishing Cr6+ | Shorter -- sensitive to drag-in, pH drift |
| Process control | Moderate -- wide operating window | Tighter -- pH, temp, immersion time all critical |
| Health hazard | Carcinogen (OSHA PEL: 5 ug/m3) | Low hazard -- irritant, not carcinogen |

**Critical:** RoHS "Non-compliant" in `#E05C5C`. "RoHS compliant" in `#27AE60`. The RoHS row must qualify scope as EEE-specific with exemption note for other sectors. "Carcinogen" in `#E05C5C`.

Data font: Inter 400, 12-13px. Property labels: Inter 500. This is the most space-intensive element -- text must remain legible.

---

## Phase 6 -- Self-Healing and Regulatory Timeline (Zone 5)

Two-column layout.

### Step 8 -- Left: THE SELF-HEALING ADVANTAGE (amber border)

Glass card with amber left-border accent.
- Title: `THE SELF-HEALING ADVANTAGE` -- Barlow 600, 16px, `#E8A020`
- Subtitle in smaller text: `(AND WHY IT MATTERS LESS THAN IT USED TO)`
- Body (Inter 400, 14px, `#F0EDE8`):

> Hex chrome films contain a reservoir of soluble Cr6+. When the film is scratched or abraded, Cr6+ migrates to the damaged site and re-oxidizes to form new barrier. This is genuine self-healing -- no other conversion coating does this.
>
> But modern trivalent systems with topcoat sealers have closed the gap significantly. The sealer provides a secondary physical barrier that compensates for the lack of chemical self-healing. Many automotive and electronics OEMs have successfully transitioned to tri + sealer with no field performance loss.

Key callout (JetBrains Mono 400, 12px, `#E8A020`, with amber left-border accent line):
> Self-healing is real but not magic -- it does not survive extreme abrasion or high-temperature baking

### Step 9 -- Right: REGULATORY TIMELINE (coral border)

Glass card with coral left-border accent.
- Title: `REGULATORY TIMELINE` -- Barlow 600, 18px, `#E05C5C`

Vertical timeline with backbone line (1pt `#3A4055`) and coral dot markers:

| Date | Event |
|---|---|
| 2003 | EU RoHS Directive adopted -- Cr6+ restricted in electronics |
| 2006 | RoHS enforcement begins -- 1000 ppm max Cr6+ |
| 2007 | EU REACH regulation -- Cr6+ on SVHC candidate list |
| 2013 | Cr6+ added to REACH Annex XIV (authorization required) |
| 2017 | REACH authorization sunset for many Cr6+ uses |
| 2024+ | Ongoing exemption reviews; automotive and aerospace still use hex under exemptions |

Date: JetBrains Mono 400, 12px, `#E05C5C`. Event: Inter 400, 12px, `#F0EDE8`.

Bottom closer (Inter 500, 13px, `#27AE60`):
> The trend is clear: the window for hex chrome is closing. Build your tri capability now.

---

## Phase 7 -- Application Best Practices (Zone 6)

Two-column layout.

### Step 10 -- Left: CRITICAL PROCESS CONTROLS (emerald border)

Glass card with emerald left-border accent.
- Title: `CRITICAL PROCESS CONTROLS` -- Barlow 600, 18px, `#27AE60`

Six bullets (Inter 400, 13-14px):
1. **pH** -- Most critical for trivalent. Maintain within +/- 0.2 of target. Out-of-range pH = poor film formation or excessive coating.
2. **Temperature** -- Hex: 60-80 F (wide). Tri: tighter -- typically 70-85 F. Too hot = patchy film.
3. **Immersion time** -- Hex: 15-60 sec (forgiving). Tri: 30-90 sec (timing matters more).
4. **Drag-in** -- Rinse thoroughly before chromating. Nickel or iron drag-in poisons tri baths rapidly.
5. **Agitation** -- Gentle rack or barrel agitation. Avoid air agitation in hex (Cr6+ mist hazard).
6. **Drying** -- Do not force-dry above 150 F for hex films. Tri films more tolerant but check supplier spec.

### Step 11 -- Right: WHAT GOES WRONG (coral border)

Glass card with coral left-border accent.
- Title: `WHAT GOES WRONG` -- Barlow 600, 18px, `#E05C5C`

6-row table:

| Failure | Cause | Fix |
|---|---|---|
| Patchy / uneven film | Poor rinsing; zinc surface passivated | Improve rinse; reduce transfer time |
| Film too thin (poor SST) | Low conc, low time, low temp | Analyze and replenish; extend dip; check heater |
| Iridescent / rainbow (on clear) | Over-immersion or over-concentration | Reduce dip time or dilute bath |
| Powdery / chalky film | pH too high; heavy zinc drag-in | Adjust pH; improve pre-chromate rinse |
| Color inconsistency | Temp variation; uneven agitation; aging | Stabilize temp; check barrel; schedule maintenance |
| White rust in SST too early | Inadequate film + no sealer; poor rinse | Optimize chromate params; add sealer topcoat |

Header: Barlow 600, 12px, on `#3A4055`. Data: Inter 400, 12px. Failure column: Inter 500, `#E05C5C`. Alternating rows.

---

## Phase 8 -- Footer (Zone 7)

Standard footer per Series Design Prompt. Dark navy glass band, full-bleed.

### Step 12 -- Disclaimer
Centered, muted:
> This poster is an educational reference tool. Chromate types, performance data, and regulatory information are typical industry values as of 2026. Conversion coating performance varies by zinc deposit type, bath chemistry, and application conditions. RoHS and REACH regulations are subject to revision -- verify current exemption status with your regulatory compliance team. Consult your chemical supplier for application-specific guidance.

### Step 13 -- Brand line
`Chromate and Conversion Coatings -- Hex, Tri, and Beyond | Plating Posters Inc` + PP logo mark (36px gradient square with "PP" in Barlow Condensed 900).

### Step 14 -- Meta row
JetBrains Mono: `Poster #26 | v1.0 -- 2026 | Plating Posters Inc`

---

## Phase 9 -- Review Checklist

- [ ] Headline `CHROMATE AND CONVERSION COATINGS` large, warm white
- [ ] Subheading amber, mentions hex/tri/beyond
- [ ] Coral regulatory hero callout banner prominent in header
- [ ] Four coating type cards with cross-section diagrams (hex amber-border, tri teal-border)
- [ ] RoHS badges: NON-COMPLIANT in coral, COMPLIANT in emerald
- [ ] Color appearance swatch strip (6 swatches)
- [ ] Mechanism callout boxes -- hex (amber) and tri (teal) side-by-side
- [ ] Head-to-head comparison table -- 13 rows, full width
- [ ] RoHS row qualifies scope as EEE-specific with exemption note
- [ ] Self-healing card with amber accent and "not magic" callout
- [ ] Regulatory timeline with 6 dates (2003-2024+)
- [ ] Critical process controls -- 6 bullets, emerald accent
- [ ] What goes wrong -- 6-row failure table, coral accent
- [ ] Footer: disclaimer, brand, meta
- [ ] Three ambient orbs in background
- [ ] Glass surfaces on all cards/tables
- [ ] Tweaks panel: Dark/Light + Grid + Print
- [ ] Light edition CSS overrides per remap table
- [ ] Print CSS with @page size and backdrop-filter fallbacks
- [ ] No brand names, no supplier names anywhere
- [ ] Zero use of `color-mix()`

---

## Phase 10 -- Light Remap & Export

Apply `body[data-edition="light"]` overrides per CW Part 6 remap table:

| Dark | Light | Notes |
|---|---|---|
| `#1A1F2E` | `#F5F4F0` | Background |
| `#F0EDE8` | `#1A1F2E` | Primary text |
| `#1E2435` | `#ECEEF4` | Card fills |
| `#252B3D` | `#E8E8F0` | Alt rows |
| `#0D1020` | `#1A1F2E` | Footer |
| `#E8A020` | `#C8860A` | Amber |
| `#2EC4B6` | `#1A8C82` | Teal |
| `#27AE60` | `#1E7A47` | Emerald |
| `#E05C5C` | `#B83E3E` | Coral |
| `#3A4055` | `#D0D4DE` | Slate |
| `#C8D0D8` | `#C8D0D8` | Silver -- unchanged |
| `#6B702A` | `#6B702A` | Olive Drab -- unchanged |

Color appearance swatches (Block C): retain real-world coating colors on both editions.

Six export files: `Chromate and Conversion Coatings -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-25 | Initial. |
