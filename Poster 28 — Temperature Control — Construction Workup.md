---
Project: Plating Posters Inc
Poster Number: 28
Title: "Temperature Control — The Overlooked Variable"
Document Type: Construction Workup
Status: v1.0 — Ready for Elara
Created: 2026-04-24T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - General industry knowledge (temperature effects on plating baths, heating/cooling equipment, thermocouple placement)
Technical Source: General industry knowledge — temperature effects on reaction kinetics, conductivity, additive stability, deposit properties; heating and cooling equipment types; thermocouple and RTD measurement; typical operating ranges across all major plating processes.
Watson Flags: TWO OPEN — (1) Confirm the Arrhenius relationship simplified statement ("reaction rate roughly doubles per 10°C increase") as applicable to electroplating bath chemistry — this is a general chemistry rule but confirm it's a fair approximation for the poster audience. (2) Verify the specific temperature ranges in the process reference table (especially hard chrome 120-140°F and electroless nickel 180-195°F) against current industry standards. Both non-blocking.
Tyler Flags: ONE OPEN — (1) Validate the additive breakdown callout: "brightener consumption increases approximately 2x for every 10°C rise in Watts nickel" — Tyler's shop experience may have more nuanced data. Non-blocking.
Process Scope: Temperature measurement, control, and effects across all plating and finishing processes (universal)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow: Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - TemperatureControl
  - ProcessControl
  - BathManagement
  - ConstructionWorkup
---

# Poster #28 — Construction Workup
## Temperature Control — The Overlooked Variable

*Alaina — Plating Posters Inc Creative Lead*
*v1.0 — 2026-04-24*

This document is the construction workup for Poster #28. Temperature is the variable that touches everything in a plating shop — conductivity, reaction rate, additive stability, deposit stress, throwing power — yet it's the one most shops control least carefully. This poster makes the invisible visible and gives operators a reason to care about the thermometer.

> **Workflow note:** Poster generation uses claude.ai chat (SVG/HTML visual artifacts). These specs feed the Claude Chat Generation Prompt engineered by Elara.

**What makes this poster valuable:** Every other process variable (pH, CD, concentration) gets its own analysis and control protocol. Temperature is often just "heat it up until it works." This poster demonstrates that temperature is not a set-and-forget parameter — it actively shapes every deposit in the shop. It also connects temperature to additive cost, which is the argument that gets management's attention.

**Who it's for:** Operators, process engineers, maintenance staff (who manage heating/cooling equipment), and shop managers who approve chemical budgets. The operator learns why temperature matters; the manager learns why fixing the chiller saves money.

---

## Part 1 — Workflow Orientation

### Design Capabilities for This Poster

- Text boxes with precise font, size, weight, color, and spacing control
- Solid-color rectangles and rounded rectangles for callout boxes, table rows, and temperature zone indicators
- Simple shapes for thermometer graphic (tall rectangle with circle base), heating/cooling equipment diagrams
- Line elements for temperature range bars
- Color fills set to exact hex values
- Export at print-quality PDF (300 DPI equivalent via print export)

### Limitations to Flag for Elara

1. **Temperature effects matrix (Block B — HERO):** A visual showing how temperature affects six key properties (conductivity, deposition rate, additive consumption, throwing power, internal stress, brightness). Built as six horizontal bar-style indicators, each showing "low temp" to "high temp" with the effect direction. Same approach as the ripple gauge in Poster #24.

2. **Process temperature reference chart (Block D):** A large table — the poster's primary reference value. Straightforward construction.

3. **Heating/cooling equipment comparison (Block F):** Four equipment type cards. Same pattern as filter cards in Poster #25.

4. **Standard construction techniques throughout.** No novel visual challenges.

---

## Part 2 — Document Setup Instructions (for Elara's prompt)

### Step 1-3 — Standard (24x36", `#1A1F2E` background, standard font stack)

### Step 4 — Color palette

| Color Name | Hex | Primary Use |
|---|---|---|
| Gunmetal Dark | `#1A1F2E` | Background (Dark edition) |
| Warm White | `#F0EDE8` | All primary text (Dark edition) |
| Amber | `#E8A020` | High temperature zone, caution, additive consumption warnings |
| Teal | `#2EC4B6` | Low temperature zone, cooling indicators, measurement data |
| Emerald | `#27AE60` | Optimal temperature zone, best practice, proper control |
| Coral | `#E05C5C` | Overheating danger, equipment failure, critical warnings |
| Mid Slate | `#3A4055` | Table headers, thermometer outlines, divider lines |
| Deep Navy | `#0D1020` | Footer band background |
| Dark Callout | `#1E2435` | Callout box fills |
| Alt Row | `#252B3D` | Alternating table rows |
| Bright Silver | `#C8D0D8` | Neutral elements |

### Step 5 — Ruler guides

**Horizontal guides:**
- 0.5" / 2.9" / 10.5" / 15.0" / 21.5" / 27.0" / 32.5" / 35.5"

---

## Part 3 — Layout Zones and Build Order

```
ZONE 1 — HEADER BAND (0"–2.9")
  Block A: Headline + subheading + tagline

ZONE 2 — TEMPERATURE EFFECTS MATRIX (2.9"–10.5" / ~7.6" tall)
  Block B: Six-property effects visualization (HERO)
  Block C: The Arrhenius rule callout

ZONE 3 — PROCESS TEMPERATURE REFERENCE CHART (10.5"–15.0" / ~4.5" tall)
  Block D: Temperature ranges by process (the daily reference table)

ZONE 4 — WHAT TEMPERATURE DOES TO YOUR BATH (15.0"–21.5" / ~6.5" tall)
  Block E: Deep-dive callouts — conductivity, additives, stress, deposit quality (2x2 grid)

ZONE 5 — HEATING AND COOLING EQUIPMENT (21.5"–27.0" / ~5.5" tall)
  Block F: Four equipment type cards
  Block FF: Thermocouple placement callout

ZONE 6 — BEST PRACTICES AND COMMON MISTAKES (27.0"–32.5" / ~5.5" tall)
  Block G: Temperature control best practices (left half)
  Block H: Common mistakes and consequences (right half)

ZONE 7 — FOOTER BAND (32.5"–36.0" / ~3.5" tall)
  Block J: Standard footer
```

---

## Part 4 — Zone-by-Zone Build Specifications

### ZONE 1 — Header Band

**BLOCK A — Headline**

- Font: Barlow Condensed ExtraBold, 84 pt, `#F0EDE8`
- Text (all caps):

> TEMPERATURE CONTROL

**BLOCK A — Subheading**

- Font: Barlow SemiBold, 36 pt, `#E8A020` (Amber)
- Text:

> The Overlooked Variable — Affecting Every Deposit in Your Shop

**BLOCK A — Tagline**

- Font: Barlow SemiBold, 22 pt, `#F0EDE8` at 65%
- Text:

> You wouldn't run a bath 2 points off pH. Why run it 20 degrees off temperature?

---

### ZONE 2 — Temperature Effects Matrix (HERO)

**Dimensions:** Y: 2.9" to 10.5" (~7.6" tall).

---

**Section label:**
- Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text:

> WHAT TEMPERATURE CHANGES — THE SIX KEY EFFECTS

---

**BLOCK B — Six-Property Effects Visualization**

Y: 3.6" to 9.5" (~5.9" tall). Six horizontal effect bars, each showing how a property changes from low to high temperature.

Each effect bar is a self-contained row:

Structure per row:
- Property label (left): Barlow SemiBold, 20 pt, `#F0EDE8`. Width: 5.0".
- Horizontal bar (center): 15.0" wide x 0.8" tall. Rounded rectangle, `#252B3D`, corner radius 4 pt.
  - Inside the bar: a gradient-like zone from Teal (left/cool) through Emerald (center/optimal) to Amber/Coral (right/hot). Built as three adjacent colored rectangles within the bar container.
  - Arrow or indicator showing the direction of the effect
- Effect label (right): Inter Regular, 14 pt. Width: 3.0".

| Row | Property | Low Temp Effect | High Temp Effect | Direction |
|---|---|---|---|---|
| 1 | CONDUCTIVITY | Lower — higher voltage needed | Higher — better distribution | Increases with temp |
| 2 | DEPOSITION RATE | Slower plating | Faster plating | Increases with temp |
| 3 | ADDITIVE CONSUMPTION | Lower breakdown rate | Faster breakdown — higher cost | Increases with temp |
| 4 | THROWING POWER | Generally worse | Generally improved | Increases with temp |
| 5 | INTERNAL STRESS | Varies by system | Generally decreases (more ductile) | Decreases with temp |
| 6 | BRIGHTNESS | May be duller (brighteners less active) | Initially better, then degraded (additive breakdown) | Peaks at optimal, drops at extremes |

Each bar has:
- Left zone (20%): Teal `#2EC4B6` at 25% — represents cool end
- Center zone (40%): Emerald `#27AE60` at 20% — represents optimal range
- Right zone (40%): Amber `#E8A020` at 25% transitioning to Coral `#E05C5C` at 20% — represents too hot

Effect direction arrow: Small triangle element inside the bar pointing in the direction of increase.

Low-temp note (left of bar): Inter Regular, 12 pt, `#2EC4B6`
High-temp note (right of bar): Inter Regular, 12 pt, `#E8A020`

Row spacing: 0.95" per row (total 6 rows = 5.7" + labels = fits in 5.9").

---

**BLOCK C — The Arrhenius Rule Callout**

Y: 9.7" to 10.3" (~0.6" tall).

- Centered. Width: 18.0". Fill: `#252B3D`. Corner radius: 4 pt. Height: 0.5".
- Text: JetBrains Mono Regular, 16 pt, `#E8A020`

> Rule of thumb: Chemical reaction rates roughly double for every 10°C (18°F) increase — applies to additive breakdown, bath aging, and electroless plating rate (not electrolytic deposition rate, which is governed by current)

---

### ZONE 3 — Process Temperature Reference Chart

**Dimensions:** Y: 10.5" to 15.0" (~4.5" tall).

---

**Section label:**
- Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text:

> OPERATING TEMPERATURES BY PROCESS

---

**BLOCK D — Temperature Reference Table**

Y: 11.2" to 14.8" (~3.6" tall). The poster's primary daily-reference table.

Header row: Fill `#3A4055`. Labels: `Process` | `Min (°F)` | `Optimal (°F)` | `Max (°F)` | `°C Range` | `Critical Notes`
Column widths: 5.5" | 2.0" | 2.5" | 2.0" | 2.5" | 8.5". Total: 23.0".

| Process | Min | Optimal | Max | °C | Notes |
|---|---|---|---|---|---|
| Acid copper sulfate | 70 | 75-85 | 95 | 21-35 | Higher temp = better throwing power but faster additive breakdown |
| Watts nickel (bright) | 110 | 130-140 | 155 | 43-68 | Additive consumption doubles per 10°C rise. Below 110°F, efficiency drops severely and deposits darken. |
| Hard chrome | 120 | 130-140 | 150 | 49-66 | Too hot = low efficiency; too cold = poor coverage |
| Acid zinc (chloride) | 70 | 75-90 | 100 | 21-38 | Higher temp improves brightness range |
| Alkaline zinc (non-CN) | 70 | 75-85 | 100 | 24-38 | Excessive heat degrades organic additives |
| Electroless nickel | 180 | 185-190 | 200 | 82-88 | Most temperature-sensitive process — +/- 2°F matters. Above 195°F approaches decomposition threshold. |
| Alkaline non-CN copper | 110 | 130-145 | 160 | 43-71 | Cold bath = poor throwing power |
| Tin (acid) | 60 | 65-80 | 90 | 16-32 | Sensitive to overheating — grain coarsens rapidly |
| Gold (acid hard) | 100 | 110-130 | 150 | 38-66 | Higher temp = brighter deposit |
| Anodize Type II (sulfuric) | 60 | 68-72 | 75 | 16-24 | Temperature rise during anodizing must be controlled |

Data font: JetBrains Mono Regular, 13 pt, `#F0EDE8`. Min values in `#2EC4B6`. Optimal in `#27AE60`. Max in `#E8A020`. Process names: Inter Medium, 14 pt, `#F0EDE8`. Notes: Inter Regular, 12 pt, `#F0EDE8`. Alternating rows.

---

### ZONE 4 — What Temperature Does to Your Bath

**Dimensions:** Y: 15.0" to 21.5" (~6.5" tall).

---

**Section label:**
- Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text:

> THE DEEP DIVE — HOW TEMPERATURE SHAPES YOUR DEPOSIT

---

**Block E — 2x2 Deep-Dive Grid**

Y: 15.8" to 21.3" (~5.5" tall). Four callout boxes in a 2x2 grid.

Each box: Width: 11.25". Height: 2.5". Fill: `#1E2435`. Corner radius: 6 pt. Left-border accent.
Column gap: 0.5". Row gap: 0.3".

| Position | Accent | Title | Content |
|---|---|---|---|
| R1C1 (X: 0.5", Y: 15.8") | `#2EC4B6` | `CONDUCTIVITY AND VOLTAGE` | Temperature increases ion mobility in solution. Higher conductivity means lower voltage needed for the same current — reducing energy cost and improving current distribution. A 10°C rise in a Watts nickel bath can drop cell voltage by 0.5-1.0V. |
| R1C2 (X: 12.0", Y: 15.8") | `#E8A020` | `ADDITIVE STABILITY` | Organic additives (brighteners, carriers, wetters) decompose faster at higher temperatures. In Watts nickel, brightener consumption roughly doubles per 10°C. Running hot saves energy but costs more in additives — find the balance point. |
| R2C1 (X: 0.5", Y: 18.6") | `#27AE60` | `DEPOSIT PROPERTIES` | Temperature affects grain structure, ductility, hardness, and internal stress. Higher temperatures generally produce more ductile, lower-stress deposits (nickel, copper). Hard chrome is the exception — temperature controls the balance between efficiency and hardness. |
| R2C2 (X: 12.0", Y: 18.6") | `#E05C5C` | `WHEN HEAT BECOMES THE ENEMY` | Electroless nickel: exceeding 200°F risks spontaneous decomposition (plate-out on tank walls, heaters, everything). Acid tin: overheating coarsens grain rapidly — dull, grainy deposits. Anodize: heat generated during anodizing softens the oxide film — inadequate cooling = burning. |

Title: Barlow SemiBold, 18 pt, accent color.
Body: Inter Regular, 15 pt, `#F0EDE8`, line height 140%.

---

### ZONE 5 — Heating and Cooling Equipment

**Dimensions:** Y: 21.5" to 27.0" (~5.5" tall).

---

**Section label:**
- Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`
- Text:

> HEATING AND COOLING — THE HARDWARE

---

**BLOCK F — Four Equipment Cards**

Y: 22.2" to 25.5" (~3.3" tall). Four cards side by side.

Each card: Width: 5.5". Height: 3.0". Fill: `#1E2435`. Corner radius: 6 pt. Border: 2 pt in accent color.

| Card | X | Accent | Equipment | Content |
|---|---|---|---|---|
| 1 | 0.5" | `#E05C5C` | `IMMERSION HEATERS` | Electric elements submerged in tank. Direct, efficient. Titanium or quartz sheath for corrosive baths. Risk: local overheating at element surface — keep element clean and solution circulating. Size: 5-50 watts/gallon typical. |
| 2 | 6.25" | `#E8A020` | `STEAM / HOT WATER COILS` | Indirect heating via coils in tank. Gentler, more uniform. Common in larger tanks. Titanium, Teflon-lined, or Hastelloy for corrosive baths. Slower response than electric. |
| 3 | 12.0" | `#2EC4B6` | `CHILLERS` | Active refrigeration for heat removal. Essential for anodize, bright acid tin, and high-amperage baths that generate excess heat. Undersized chillers are the #1 cause of temperature drift in summer. |
| 4 | 17.75" | `#27AE60` | `HEAT EXCHANGERS` | External plate-and-frame or shell-and-tube units. Solution circulates through exchanger, returns to tank. Allows cooling OR heating. Best for temperature-critical processes (EN, chrome). |

Card title: Barlow Condensed ExtraBold, 18 pt, accent color.
Card body: Inter Regular, 13 pt, `#F0EDE8`.

---

**BLOCK FF — Thermocouple Placement Callout**

Y: 25.8" to 26.8" (~1.0" tall).

- Width: 23.0". Fill: `#252B3D`. Corner radius: 4 pt.
- Left section (icon placeholder + title): Barlow SemiBold, 18 pt, `#E8A020`: `WHERE YOU MEASURE MATTERS`
- Right section: Inter Regular, 15 pt, `#F0EDE8`:

> Place temperature sensor MID-TANK, MID-DEPTH — not near the heater, not near the surface. Use RTD or thermocouple with chemical-resistant sheath. Calibrate against a NIST-traceable reference thermometer annually. Digital controllers with +/- 1°F resolution are minimum — +/- 0.5°F for EN.

---

### ZONE 6 — Best Practices and Common Mistakes

**Dimensions:** Y: 27.0" to 32.5" (~5.5" tall).

---

**BLOCK G — Best Practices** (left half)

Callout container: Width: 11.0". Fill: `#1E2435`. Left-border: `#27AE60`.

Title: `TEMPERATURE CONTROL BEST PRACTICES` — Barlow SemiBold, 20 pt, `#27AE60`

Bullets (Inter Regular, 15 pt, `#F0EDE8`, line height 145%):

> - Install temperature controller with high AND low alarms
> - Log bath temperature at start, middle, and end of each shift
> - Allow bath to reach operating temperature before plating — cold starts cause rejects
> - Size heating/cooling to maintain temp under maximum production load, not idle
> - Insulate tank tops — evaporation is the biggest heat loss mechanism
> - Use tank covers when not plating — reduces heat loss by 50-70%
> - Schedule chiller maintenance before summer — don't wait for the first hot day

---

**BLOCK H — Common Mistakes** (right half)

Callout container: Width: 11.5". Fill: `#1E2435`. Left-border: `#E05C5C`.

Title: `THE TEMPERATURE MISTAKES THAT COST YOU` — Barlow SemiBold, 20 pt, `#E05C5C`

Table (5 rows):

| Mistake | Consequence |
|---|---|
| Plating in a cold bath | Dull deposits, poor coverage, high stress |
| Running too hot "for faster plating" | Additive breakdown, increased chemical cost, possible decomposition |
| Sensor near heater element | Reads hot — controller cycles off too soon — bath actually cold |
| No high-temperature alarm on EN tank | Spontaneous decomposition — replace bath ($$$) and clean tank |
| Ignoring seasonal temperature swing | Summer production runs hotter than winter — different reject patterns |

Header: Barlow SemiBold, 13 pt, `#F0EDE8` on `#3A4055`. Data: Inter Regular, 14 pt, `#F0EDE8`. Mistake column: Inter Medium, `#E05C5C`. Alternating rows.

---

### ZONE 7 — Footer Band

Standard footer per series convention.

**Disclaimer:**
> This poster is an educational reference tool. Operating temperature ranges are typical industry values. Specific temperature requirements vary by proprietary bath formulation, additive system, and application. Consult your chemical supplier for application-specific temperature ranges and tolerances.

**Poster title:** Temperature Control — The Overlooked Variable

**Version:** v1.0 — 2026

---

## Part 5 — Grouping and Naming Convention

| Group Name | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline |
| Zone 2 - Effects Matrix | Section label, six-property effect bars, Arrhenius callout |
| Zone 3 - Process Temperatures | Section label, temperature reference table |
| Zone 4 - Deep Dive | Section label, 2x2 deep-dive callout grid |
| Zone 5 - Equipment | Section label, four equipment cards, thermocouple callout |
| Zone 6 - Best Practices | Best practices callout, common mistakes table |
| Zone 7 - Footer | Standard footer elements |

---

## Part 6 — Light Edition Color Remap Table

Standard remap per series convention. No special notes.

---

## Part 7 — Export Checklist

Standard six files. File name prefix: `Temperature Control`

The process temperature reference table (Zone 3) is the poster's highest-value daily-reference element. Verify it remains fully legible at 18x24".

---

## Design Notes

This poster makes a strong case for something most shops take for granted. The tagline ("You wouldn't run a bath 2 points off pH. Why run it 20 degrees off temperature?") is designed to be quotable — the kind of line a process engineer uses to make the case for a better chiller.

The hero visual (Zone 2) is unconventional for the series — it's not a diagram or a table but a set of effect-direction indicators. This visual language works because the message is fundamentally about relationships ("as temperature goes up, X changes like this"). The six-property matrix makes the invisible visible at a glance.

The process temperature table (Zone 3) will be the section operators reach for daily. It deliberately includes Fahrenheit as primary with Celsius in a separate column — the U.S. plating shop floor still runs on Fahrenheit, and converting on the fly introduces errors. Both units are there for international audiences or lab reporting.

The electroless nickel warnings appear in two places (the table and the deep-dive grid) because EN decomposition from overheating is one of the most expensive single-event failures in a plating shop. Redundancy is intentional.

---

*Alaina — Plating Posters Inc Creative Lead*
*Poster #28 — Temperature Control — Construction Workup v1.0*
*2026-04-24*
