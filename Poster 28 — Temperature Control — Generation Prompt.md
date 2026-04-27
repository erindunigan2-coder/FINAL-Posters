---
Project: Plating Posters Inc
Poster Number: 28
Title: "Temperature Control -- The Overlooked Variable"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-25T00:00:00
Source: Poster 28 -- Temperature Control -- Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - TemperatureControl
  - ProcessControl
  - BathManagement
  - v1
---

# Claude Chat Generation Prompt -- Poster #28
## Temperature Control -- The Overlooked Variable
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-25).*

---

> **IMPORTANT:** Generate as SVG or HTML visual artifact. 24 x 36" portrait. Dark edition first. Seven zones. The hero visual is a six-property temperature effects matrix -- horizontal effect bars, not a table.

---

## Phase 0 -- Design System

Follow the canonical Series Design Prompt in full: `Plating Posters - Series Design Prompt.md`. Key rules:

- **Stage:** 1200x1800 CSS px in `.stage`, scaled via `transform: scale()`.
- **Fonts (Google CDN):** Barlow Condensed 800/900, Barlow 600/700, Inter 400/500/600, JetBrains Mono 400/500.
- **Palette:** `#1A1F2E` (bg), `#F0EDE8` (text), `#E8A020` (amber), `#2EC4B6` (teal), `#27AE60` (emerald), `#E05C5C` (coral), `#3A4055` (slate), `#0D1020` (navy), `#1E2435` (callout), `#252B3D` (altrow), `#C8D0D8` (silver).
- **Background:** Three ambient orbs (teal 14%, amber 12%, coral 10%) + faint 50x50 grid with radial mask.
- **Glass surfaces:** `rgba(30,36,53,.55)` solid fallback + gradient + border + `backdrop-filter` on EVERY card. NEVER `color-mix()`. NEVER `opacity` on absolutely-positioned pseudo-elements.
- **Print CSS:** `@page { size: 12.5in 18.75in; margin:0; }`. Full print block per design system.
- **Tweaks panel:** Floating bottom-right. Dark/Light toggle + Grid toggle + Print button. Wire postMessage protocol.
- **Light edition:** `body[data-edition="light"]` CSS overrides (darker accents, `#F5F4F0` background).
- **Safe zone:** 25px padding inside poster frame.

---

## Phase 1 -- Header (Zone 1)

### Step 1 -- Headline
`TEMPERATURE CONTROL` -- `84` pt Barlow Condensed ExtraBold `#F0EDE8`. Y: **0.5"**.

### Step 2 -- Subheading
`The Overlooked Variable -- Affecting Every Deposit in Your Shop` -- `30` pt Barlow SemiBold `#E8A020`. Y: **1.5"**.

### Step 3 -- Tagline
`You wouldn't run a bath 2 points off pH. Why run it 20 degrees off temperature?` -- `20` pt at 65% opacity. Y: **2.1"**.

---

## Phase 2 -- Temperature Effects Matrix / HERO (Zone 2)

Y: 2.9" to 10.5". Section label: `WHAT TEMPERATURE CHANGES -- THE SIX KEY EFFECTS` -- Barlow Condensed ExtraBold 28pt centered.

### Step 4 -- Six effect bars

Six full-width horizontal glass containers stacked vertically. Each bar:
- Property label on left (Barlow 600, ~20px)
- Horizontal bar with three colored zones: Teal (cool) -> Emerald (optimal) -> Amber/Coral (hot)
- Arrow showing direction of change
- Cool-end note in teal on left edge
- Hot-end note in amber/coral on right edge

| Row | Property | Low Temp (Teal) | High Temp (Amber/Coral) | Direction |
|---|---|---|---|---|
| 1 | CONDUCTIVITY | Lower -- higher voltage needed | Higher -- better distribution | Increases with temp |
| 2 | DEPOSITION RATE | Slower plating | Faster plating | Increases with temp |
| 3 | ADDITIVE CONSUMPTION | Lower breakdown rate | Faster breakdown -- higher cost | Increases with temp |
| 4 | THROWING POWER | Generally worse | Generally improved (most baths) | Increases with temp |
| 5 | INTERNAL STRESS | Varies by system | Generally decreases (more ductile) | Decreases with temp |
| 6 | BRIGHTNESS | Peaks at optimal temperature -- degrades at both extremes | | Non-linear |

Bar construction: Left 20% teal at 25% -> Center 40% emerald at 20% -> Right 40% amber at 25% to coral at 20%.

### Step 5 -- Arrhenius rule callout strip

Full-width amber-tinted glass strip below the six bars. JetBrains Mono 14pt `#E8A020`:

`Rule of thumb: Chemical reaction rates roughly double for every 10C (18F) increase -- applies to additive breakdown, bath aging, and electroless plating rate (not electrolytic deposition rate, which is governed by current)`

---

## Phase 3 -- Process Temperature Reference Chart (Zone 3)

Y: 10.5" to 15.0". Section label: `OPERATING TEMPERATURES BY PROCESS` -- Barlow Condensed ExtraBold 28pt centered.

### Step 6 -- Temperature table

Full-width glass table. Header row: slate `#3A4055`.
Columns: `Process` | `Min (F)` | `Optimal (F)` | `Max (F)` | `C Range` | `Critical Notes`.
Min values in teal `#2EC4B6`. Optimal in emerald `#27AE60`. Max in amber `#E8A020`.
Process names: Inter Medium 14pt. Data: JetBrains Mono 13pt. Notes: Inter Regular 12pt. Alternating rows.

| Process | Min | Optimal | Max | C | Notes |
|---|---|---|---|---|---|
| Acid copper sulfate | 70 | 75-85 | 95 | 21-35 | Higher temp = better throwing power but faster additive breakdown |
| Watts nickel (bright) | 110 | 130-140 | 155 | 43-68 | Additive consumption doubles per 10C rise. Below 110F efficiency drops severely. |
| Hard chrome | 120 | 130-140 | 150 | 49-66 | Too hot = low efficiency; too cold = poor coverage |
| Acid zinc (chloride) | 70 | 75-90 | 100 | 21-38 | Higher temp improves brightness range |
| Alkaline zinc (non-CN) | 70 | 75-85 | 100 | 24-38 | Excessive heat degrades organic additives |
| Electroless nickel | 180 | 185-190 | 200 | 82-88 | MOST temperature-sensitive process. Above 195F approaches decomposition threshold. +/- 2F matters. |
| Alkaline non-CN copper | 110 | 130-145 | 160 | 43-71 | Cold bath = poor throwing power |
| Tin (acid) | 60 | 65-80 | 90 | 16-32 | Sensitive to overheating -- grain coarsens rapidly |
| Gold (acid hard) | 100 | 110-130 | 150 | 38-66 | Higher temp = brighter deposit |
| Anodize Type II (sulfuric) | 60 | 68-72 | 75 | 16-24 | Temperature rise during anodizing must be controlled |

---

## Phase 4 -- Deep Dive (Zone 4)

Y: 15.0" to 21.5". Section label: `THE DEEP DIVE -- HOW TEMPERATURE SHAPES YOUR DEPOSIT` -- Barlow Condensed ExtraBold 28pt centered.

### Step 7 -- 2x2 deep-dive grid

Four glass cards, each with left-border accent and role-tinted glass.

| Position | Accent | Title | Content |
|---|---|---|---|
| Top-left | `#2EC4B6` teal | CONDUCTIVITY AND VOLTAGE | Temperature increases ion mobility. Higher conductivity = lower voltage for same current. A 10C rise in Watts nickel drops cell voltage by 0.5-1.0V. |
| Top-right | `#E8A020` amber | ADDITIVE STABILITY | Organic additives decompose faster at higher temps. In Watts nickel, brightener consumption roughly doubles per 10C. Running hot saves energy but costs more in additives. |
| Bottom-left | `#27AE60` emerald | DEPOSIT PROPERTIES | Higher temp = more ductile, lower-stress deposits (Ni, Cu). Hard chrome is the exception -- temperature controls efficiency vs hardness balance. |
| Bottom-right | `#E05C5C` coral | WHEN HEAT BECOMES THE ENEMY | EN > 200F = spontaneous decomposition. Tin: overheating coarsens grain rapidly. Anodize: heat softens oxide film -- inadequate cooling = burning. |

Title: Barlow SemiBold 18pt in accent color. Body: Inter Regular 14pt `#F0EDE8`.

---

## Phase 5 -- Heating and Cooling Equipment (Zone 5)

Y: 21.5" to 27.0". Section label: `HEATING AND COOLING -- THE HARDWARE` -- Barlow Condensed ExtraBold 24pt centered.

### Step 8 -- Four equipment cards

Four glass cards side by side, each with accent-color border.

| Card | Accent | Title | Content |
|---|---|---|---|
| 1 | `#E05C5C` coral | IMMERSION HEATERS | Electric elements submerged in tank. 5-50 W/gal. Ti or quartz sheath. Risk: local overheating at element surface. |
| 2 | `#E8A020` amber | STEAM / HOT WATER COILS | Indirect heating via coils. Gentler, more uniform. Slower response than electric. |
| 3 | `#2EC4B6` teal | CHILLERS | Active refrigeration. Essential for anodize, tin, high-amperage baths. Undersized chillers = #1 cause of summer temp drift. |
| 4 | `#27AE60` emerald | HEAT EXCHANGERS | Plate-and-frame or shell-and-tube. Can heat or cool. Best for EN, chrome. |

Card title: Barlow Condensed ExtraBold 18pt in accent. Card body: Inter Regular 13pt `#F0EDE8`.

### Step 9 -- Thermocouple placement callout strip

Full-width glass strip below equipment cards. Title: `WHERE YOU MEASURE MATTERS` (Barlow SemiBold 18pt `#E8A020`).

Body: `Place sensor mid-tank, mid-depth -- not near heater, not near surface. RTD or thermocouple with chemical-resistant sheath. Calibrate annually against NIST-traceable reference. Digital controller: +/- 1F resolution minimum. +/- 0.5F for EN.`

---

## Phase 6 -- Best Practices and Common Mistakes (Zone 6)

Y: 27.0" to 32.5".

### Step 10 -- Best practices (left column)

Emerald left-border glass card. Title: `TEMPERATURE CONTROL BEST PRACTICES` (Barlow SemiBold 20pt `#27AE60`).

Seven bullets (Inter Regular 14pt):
1. Install temperature controller with high AND low alarms
2. Log bath temperature at start, middle, and end of each shift
3. Allow bath to reach operating temperature before plating -- cold starts cause rejects
4. Size heating/cooling to maintain temp under maximum production load, not idle
5. Insulate tank tops -- evaporation is the biggest heat loss mechanism
6. Use tank covers when not plating -- reduces heat loss by 50-70%
7. Schedule chiller maintenance before summer -- don't wait for the first hot day

### Step 11 -- Common mistakes (right column)

Coral left-border glass card. Title: `THE TEMPERATURE MISTAKES THAT COST YOU` (Barlow SemiBold 20pt `#E05C5C`).

Five-row table with slate header:

| Mistake | Consequence |
|---|---|
| Plating in a cold bath | Dull deposits, poor coverage, high stress |
| Running too hot "for faster plating" | Additive breakdown, increased chemical cost, possible decomposition |
| Sensor near heater element | Reads hot -- controller cycles off too soon -- bath actually cold |
| No high-temp alarm on EN tank | Spontaneous decomposition -- replace bath ($$$) and clean tank |
| Ignoring seasonal temperature swing | Summer runs hotter than winter -- different reject patterns |

---

## Phase 7 -- Footer (Zone 7)

Standard dark navy `#0D1020` footer, full-bleed.

**Disclaimer:** `This poster is an educational reference tool. Operating temperature ranges are typical industry values. Specific temperature requirements vary by proprietary bath formulation, additive system, and application. Consult your chemical supplier for application-specific temperature ranges and tolerances.`

**Brand line:** `Temperature Control -- The Overlooked Variable | Metal Finishing Reference Series | PP`

**Meta:** `Poster #28 | v1.0 -- 2026 | Plating Posters Inc`

---

## Phase 8 -- Review Checklist

- [ ] Headline `TEMPERATURE CONTROL` 84pt warm white
- [ ] Subheading amber, tagline 65% opacity
- [ ] Six effect bars with teal/emerald/amber zones and directional arrows
- [ ] Arrhenius callout strip -- qualified as "chemical reaction rates" only
- [ ] Process temperature table -- 10 rows, all values match CW exactly
- [ ] Watts Ni min = 110F, EN min = 180F, EN optimal = 185-190F
- [ ] 2x2 deep-dive grid with correct accent borders
- [ ] Four equipment cards (coral/amber/teal/emerald)
- [ ] Thermocouple placement callout strip
- [ ] Best practices: 7 bullets (emerald)
- [ ] Common mistakes: 5-row table (coral)
- [ ] Footer complete with disclaimer
- [ ] Glass surfaces on ALL cards (solid fallback + gradient + border + backdrop-filter)
- [ ] Three ambient background orbs + grid
- [ ] Tweaks panel: Dark/Light + Grid + Print
- [ ] Print CSS: @page 12.5in x 18.75in
- [ ] Light edition via body[data-edition="light"] overrides
- [ ] No color-mix(). No opacity on pseudo-elements.

---

## Phase 9 -- Light Remap & Export

Standard remap. Six files: `Temperature Control -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-25 | Initial. |
