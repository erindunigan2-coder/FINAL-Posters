---
Project: Plating Posters Inc
Poster Number: 25
Title: "Filtration and Purification -- Keeping Your Bath Clean"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-25T00:00:00
Source: Poster 25 -- Filtration and Purification -- Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - Filtration
  - Purification
  - CarbonTreatment
  - BathMaintenance
  - Series1
  - v1
---

# Claude Chat Generation Prompt -- Poster #25
## Filtration and Purification -- Keeping Your Bath Clean
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-25).*

---

> **IMPORTANT:** Generate as a single self-contained HTML file. 1200x1800 CSS px poster in a `.stage` flex container that scales to fit via `transform: scale()`. Dark edition first, Light via `body[data-edition="light"]` overrides. Include Tweaks panel (Dark/Light toggle, Grid toggle, Print button) floating bottom-right outside the stage.

---

## Phase 0 -- Series Design System

Reference the canonical design file: `Plating Posters - Series Design Prompt.md`.

**Key requirements carried forward:**
- **Output:** Single self-contained HTML file (not SVG)
- **Aesthetic:** Industrial-technical meets iOS 18 Liquid Glass
- **Poster size:** 1200x1800 CSS px in a `.stage` flex container; `transform: scale()` to fit viewport
- **Fonts (Google Fonts CDN):** Barlow Condensed 800/900, Barlow 600/700, Inter 400/500/600, JetBrains Mono 400/500
- **Locked palette (Dark):** `#1A1F2E` bg, `#F0EDE8` text, `#E8A020` amber, `#2EC4B6` teal, `#27AE60` emerald, `#E05C5C` coral, `#3A4055` slate, `#0D1020` deep navy, `#1E2435` dark callout, `#252B3D` alt row, `#C8D0D8` silver
- **Glass surfaces on EVERY card/callout:** `rgba(30,36,53,.55)` bg, `linear-gradient(145deg, rgba(255,255,255,.055), rgba(255,255,255,.015))`, `border: 1px solid rgba(255,255,255,.12)`, `backdrop-filter: blur(18px) saturate(140%)`, full box-shadow stack, `border-radius: 14px`
- **Background:** Three ambient color orbs (teal, amber, coral) via radial-gradient, plus faint 50x50px grid with radial mask, on `#1A1F2E` base
- **Print CSS:** `@page { size: 12.5in 18.75in; margin: 0; }` -- every glass surface must have solid rgba fallback. NEVER `color-mix()`. Backdrop-filter stripped at print; solid backgrounds carry the look
- **Tweaks panel:** Floating bottom-right outside the stage. Dark/Light toggle, Grid toggle, Print button
- **Icons:** Inline SVG only, 1.5-2px monoline stroke, `currentColor`. No raster, no emoji

---

## Phase 1 -- Foundation

Standard: 1200x1800 CSS px, `#1A1F2E` background, locked palette, 25px safe zone padding. Three ambient orbs + faint grid overlay.

---

## Phase 2 -- Header (Zone 1)

### Step 1 -- Headline
`FILTRATION AND PURIFICATION` -- Barlow Condensed 800, large (scale to fit ~72-84px equivalent), `#F0EDE8`. Top of poster inside safe zone.

### Step 2 -- Subheading
`Keeping Your Bath Clean -- The Most Underrated Quality Tool in the Shop` -- Barlow 600, ~24-28px, `#2EC4B6` (Teal).

### Step 3 -- Tagline
`If you can see particles in your solution, your filter stopped working two weeks ago.` -- Inter 400, ~16-18px, `#F0EDE8` at 65% opacity.

---

## Phase 3 -- Filter Type Comparison / HERO (Zone 2)

Section label: `FILTER TYPES -- KNOW YOUR OPTIONS` -- Barlow Condensed 800, 20px, centered, `#F0EDE8`.

### Step 4 -- Four Filter Type Cards

Four tall glass cards arranged side by side, evenly distributed across poster width. Each card has a colored top border (2-3px) in its accent color.

| Card | Accent | Title | Rating / Specs | Description | Best For |
|---|---|---|---|---|---|
| 1 | `#2EC4B6` Teal | CARTRIDGE FILTER | Rating: 1-50 micron / Type: Depth or pleated / Flow: Low to moderate | The workhorse. Disposable or cleanable. Depth cartridges trap particles throughout the media; pleated cartridges capture on the surface for higher flow rates. Most common in individual tank filtration. | Individual tank circulation loops |
| 2 | `#E8A020` Amber | BAG FILTER | Rating: 1-200 micron / Type: Surface capture / Flow: High volume | Lower cost per change than cartridges. Higher flow capacity. Less efficient at fine filtration but excellent for heavy-solids baths (barrel plating, acid copper). Easy to change -- just pull the bag. | High-flow, heavy-particle applications |
| 3 | `#27AE60` Emerald | CARBON CANISTER | Media: Granular activated carbon / Purpose: Organic removal / Method: Continuous or batch | Removes organic contamination -- brightener breakdown products, oil, surfactant residue. Continuous carbon filtration runs solution through a GAC bed 24/7. Batch carbon treatment uses powdered carbon mixed directly into the bath, then filtered out. | Organic contamination control (nickel, copper) |
| 4 | `#E05C5C` Coral | PUMP & FILTER UNIT | Pump type: Centrifugal (mag-drive) or air-operated / Media: Cartridge or bag (interchangeable) / Flow: Sized to tank volume | The complete package -- pump, housing, and filter media as an integrated unit. Mag-drive pumps are standard for corrosive plating solutions. Air-operated diaphragm pumps for viscous or heated solutions. Size the pump to achieve target turnover rate. | Dedicated tank filtration systems |

Each card includes a simplified schematic diagram built with CSS shapes or inline SVG:
- Card 1: Tall narrow housing with internal pleated zigzag lines, inlet/outlet arrows
- Card 2: Trapezoidal bag shape inside rectangular housing, inlet top / outlet bottom
- Card 3: Cylindrical vessel with dots representing GAC media, inlet bottom / outlet top
- Card 4: Pump circle connected to filter rectangle with flow arrows and return line

Specs in JetBrains Mono 400, 11-12px. Description in Inter 400, 12-13px. "Best for" line in Inter 500, accent color.

### Step 5 -- Micron Rating Quick Reference Strip

Horizontal glass strip below cards. Four color-coded data points:

| Color | Text |
|---|---|
| `#2EC4B6` | `1 micron = fine Ni/Cr filtration` |
| `#27AE60` | `5 micron = standard plating filtration` |
| `#E8A020` | `10-25 micron = acid copper / barrel` |
| `#E05C5C` | `>25 micron = coarse pre-filtration only` |

JetBrains Mono 400, 11-12px, respective colors. Small colored dot or bar before each entry.

---

## Phase 4 -- Turnover Rates and Sizing (Zone 3)

Section label: `HOW MUCH FILTRATION IS ENOUGH?` -- Barlow Condensed 800, 20px, centered.

### Step 6 -- Turnover Rate Table

Full-width glass table. Header row with amber (`#E8A020`) text on slate (`#3A4055`) background.

Columns: `Process` | `Min Turnovers/hr` | `Target` | `Filter Rating` | `Notes`

| Process | Min | Target | Rating | Notes |
|---|---|---|---|---|
| Watts nickel (bright) | 3 | 5 | 1-5 micron | Continuous; carbon canister recommended |
| Hard chrome | 2 | 3 | 5-10 micron | Trivalent chrome higher -- consult supplier |
| Acid copper | 2 | 3-4 | 5-10 micron | Carbon treatment as needed for organics |
| Zinc (acid chloride) | 2 | 3 | 5-10 micron | Filter before and after carbon treatment |
| Zinc (alkaline) | 1 | 2-3 | 10-25 micron | Lower requirements; watch for carbonate buildup |
| Electroless nickel | 3 | 10-20 | 1-5 micron | CRITICAL -- particles nucleate out-plating |
| Gold / Precious metals | 3 | 5 | 1 micron | Filter media must be compatible with cyanide |

Target values in `#27AE60`. Alternating rows: `#1E2435` / `#252B3D`. EN row should have subtle coral left-border or highlight to signal criticality.

### Step 7 -- Sizing Formula Bar

Amber glass pill or bar below the table:
`Pump flow rate (GPM) = Tank volume (gal) x Turnovers/hr / 60`
JetBrains Mono 500, 14-15px, `#E8A020`.

---

## Phase 5 -- Carbon Treatment Procedure (Zone 4)

Section label: `CARBON TREATMENT -- THE ORGANIC DETOX` -- Barlow Condensed 800, 20px, centered.

### Step 8 -- Six-Step Flowchart

Two rows of three steps. Each step is a glass card with colored border and numbered badge (radial gradient circle, accent color, white number).

**Row 1:**

| Step | Border | Title | Body |
|---|---|---|---|
| 1 | `#2EC4B6` | ANALYZE | Test Hull cell for organic symptoms: hazy deposits, skip plate, reduced ductility |
| 2 | `#E8A020` | ADJUST pH | Lower pH to 3.0-3.5 with dilute sulfuric acid (nickel) -- promotes iron co-precipitation and maximizes carbon adsorption efficiency |
| 3 | `#27AE60` | ADD CARBON | Add 2-5 g/L powdered activated carbon. Stir 2-4 hours minimum |

**Row 2:**

| Step | Border | Title | Body |
|---|---|---|---|
| 4 | `#27AE60` | FILTER | Filter through 1-5 micron media to remove ALL carbon particles |
| 5 | `#E8A020` | RE-ADJUST | Raise pH to operating range with nickel carbonate. Replenish ALL organic additives -- brighteners, carrier, and wetting agent |
| 6 | `#2EC4B6` | VERIFY | Run Hull cell to confirm organic removal |

Arrows between steps (right-pointing between cards in a row, down-and-right between rows).

Step title: Barlow 600, 14px, accent color. Step body: Inter 400, 11-12px. Number badge: Barlow Condensed 800 on accent circle.

### Step 9 -- Do's and Don'ts Strip

Two side-by-side glass cards below the flowchart.

**Left -- DO (emerald left border `#27AE60`):**
- Test Hull cell BEFORE and AFTER treatment
- Replenish all organic additives
- Use food-grade or reagent-grade carbon
- Filter until clear

**Right -- DON'T (coral left border `#E05C5C`):**
- Return bath to service without removing ALL carbon by filtration
- Skip post-treatment pH adjustment back to operating range
- Use carbon treatment as metallic contamination substitute

Title: Barlow 600, 14px, accent color. Bullets: Inter 400, 11-12px.

---

## Phase 6 -- Dummy Plating and Advanced Purification (Zone 5)

Two-column layout.

### Step 10 -- Left: Dummy Plating Card

Teal-bordered glass card (`#2EC4B6`).

Title: `DUMMY PLATING` -- Barlow 700, 18px, `#2EC4B6`.

Key parameters in JetBrains Mono:
- Current density: 2-5 ASF
- Cathode: Corrugated mild steel
- Duration: 4-24 hours
- Removes: Cu, Pb, Cd, and other contaminant metals

Body text (Inter 400): explains that dummy plating removes metallic contaminants by depositing them on a sacrificial cathode at low current density.

Callout (amber): `Run at LCD -- you want the contaminants, not good metal.`

### Step 11 -- Right: Advanced Purification Methods Card

Amber-bordered glass card (`#E8A020`).

Title: `ADVANCED PURIFICATION METHODS` -- Barlow 700, 18px, `#E8A020`.

Four mini-entries stacked vertically:

| Method | Description |
|---|---|
| Permanganate treatment | Oxidizes organics that carbon cannot remove |
| Hydrogen peroxide | Fe2+ to Fe3+ for precipitation; caution -- excess decomposes nickel brighteners rapidly |
| Electrodialysis | Capital-intensive, high-value baths (gold, palladium) |
| Freezing | Alkaline zinc carbonate removal |

Method names: Inter 500, amber. Descriptions: Inter 400, 12px.

---

## Phase 7 -- Maintenance Schedule (Zone 6)

### Step 12 -- Left (two-thirds): Maintenance Schedule Table

Section label: `MAINTENANCE SCHEDULE` -- Barlow Condensed 800, 18px.

Glass table, 6 rows:

| Task | Frequency | Notes |
|---|---|---|
| Check filter pressure differential | Daily | Replace when delta-P exceeds manufacturer spec |
| Inspect filter housing seals | Weekly | Bypass leaks defeat the filter entirely |
| Change cartridge/bag filters | As needed (pressure) | Run on pressure differential, NOT calendar |
| Carbon canister media replacement | Monthly or by Hull cell | Replace when Hull cell shows organic symptoms |
| Clean pump strainer / inlet screen | Weekly | Clogged strainer starves the pump |
| Full system inspection | Quarterly | Pump seals, hose connections, housing cracks |

Frequency values in `#E8A020` (amber).

### Step 13 -- Right (one-third): Warning Signs Callout

Coral-bordered glass card (`#E05C5C`).

Title: `YOUR FILTER IS FAILING WHEN...` -- Barlow 600, 14px, `#E05C5C`.

Six bullets:
- Rough deposits appear that weren't there last week
- Filter pressure gauge reads zero (bypass or clogged)
- Solution clarity decreases visibly
- Hull cell panel shows pitting or roughness
- Flow rate from return line drops noticeably
- You can't remember the last filter change

Key callout (JetBrains Mono, coral):
`The cheapest filter change you'll ever do is the one you do on time.`

---

## Phase 8 -- Footer (Zone 7)

Standard series footer. Dark navy (`#0D1020`) glass band, full-bleed.

Three stacked blocks:
1. **Disclaimer** (centered, muted 50%): This poster is an educational reference tool. Filter types, turnover rates, and purification procedures are typical industry values. Consult your chemical supplier and filter manufacturer for application-specific guidance.
2. **Brand line**: `Filtration and Purification -- Keeping Your Bath Clean` | `Plating Posters Inc -- Metal Finishing Reference Series` | PP logo mark (36px gradient square with "PP" in Barlow Condensed 900)
3. **Meta** (JetBrains Mono, 50%): `v1.0 -- 2026 | Poster #25 -- Filtration and Purification | Plating Posters Inc`

---

## Phase 9 -- Review Checklist

- [ ] Headline `FILTRATION AND PURIFICATION` large, `#F0EDE8`
- [ ] Subheading in teal, tagline at 65% opacity
- [ ] Four filter type cards with schematics, specs, descriptions, "best for" lines
- [ ] Micron rating quick reference strip (4 color-coded entries)
- [ ] Turnover rate table (7 processes, target values in emerald)
- [ ] Sizing formula bar in amber
- [ ] Carbon treatment 6-step flowchart (2 rows of 3, numbered badges)
- [ ] Do / Don't strip (emerald / coral)
- [ ] Dummy plating card with key parameters and LCD callout
- [ ] Advanced purification methods (4 entries)
- [ ] Maintenance schedule table (6 rows, frequency in amber)
- [ ] Warning signs callout (6 bullets + key callout in coral)
- [ ] Footer with disclaimer, brand line, PP mark, version
- [ ] Glass surfaces on every card and callout
- [ ] Three ambient orbs + grid overlay
- [ ] Print CSS with solid fallbacks, no color-mix()
- [ ] Tweaks panel (Dark/Light toggle, Grid toggle, Print)
- [ ] Light edition via `body[data-edition="light"]` overrides
- [ ] All technical values match CW exactly (carbon pH 3.0-3.5, dosage 2-5 g/L, contact 2-4 hrs, EN turnover 10-20)
- [ ] Zero brand/supplier names in content

---

## Phase 10 -- Light Remap & Export

**Light edition remap (via CSS overrides on `body[data-edition="light"]`):**

| Dark Hex | Light Hex | Notes |
|----------|-----------|-------|
| `#1A1F2E` | `#F5F4F0` | Background |
| `#F0EDE8` | `#1A1F2E` | Primary text |
| `#1E2435` | `#ECEEF4` | Callout fills |
| `#252B3D` | `#E8E8F0` | Alt rows |
| `#0D1020` | `#1A1F2E` | Footer band |
| `#E8A020` | `#C8860A` | Amber accents |
| `#2EC4B6` | `#1A8C82` | Teal accents |
| `#27AE60` | `#1E7A47` | Emerald accents |
| `#E05C5C` | `#B83E3E` | Coral accents |
| `#3A4055` | `#D0D4DE` | Table headers, dividers |
| `#C8D0D8` | `#C8D0D8` | Silver -- unchanged |

Glass surfaces in light mode: adjust background-color to `rgba(236,238,244,.65)`, border to `rgba(0,0,0,.08)`, box-shadow highlights inverted.

**Export files:**
- `Filtration and Purification -- Dark -- 24x36 -- Print.pdf`
- `Filtration and Purification -- Dark -- 18x24 -- Print.pdf`
- `Filtration and Purification -- Dark -- Digital.pdf`
- `Filtration and Purification -- Light -- 24x36 -- Print.pdf`
- `Filtration and Purification -- Light -- 18x24 -- Print.pdf`
- `Filtration and Purification -- Light -- Digital.pdf`

---

| v1.0 | 2026-04-25 | Initial. |
