---
Project: Plating Posters Inc
Poster Number: 24
Title: "Rectifier Fundamentals — DC, Pulse, and Periodic Reverse"
Document Type: Construction Workup
Status: v1.0 — Ready for Elara
Created: 2026-04-24T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - General industry knowledge (rectifier operation, waveform types, ripple, PR plating)
Technical Source: General industry knowledge — rectifier types, waveform characteristics, ripple effects, pulse/PR parameters. Products Finishing reference articles on rectifier selection and maintenance.
Watson Flags: TWO OPEN — (1) Confirm typical ripple percentage thresholds (5% for decorative chrome, 10% general, etc.) against current industry guidance. (2) Verify PR plating cathodic-to-anodic ratio ranges for copper and gold applications specifically. Both non-blocking; values presented as industry-typical.
Tyler Flags: ONE OPEN — (1) Validate the "ripple causes roughness in chrome" statement against Tyler's shop experience — confirm this is a fair simplification for a poster audience. Non-blocking.
Process Scope: Rectifier operation, waveform types, and power supply fundamentals for electroplating (universal — applies to every electrolytic process)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow: Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Rectifier
  - PulsePlating
  - PeriodicReverse
  - Waveforms
  - ConstructionWorkup
---

# Poster #24 — Construction Workup
## Rectifier Fundamentals — DC, Pulse, and Periodic Reverse

*Alaina — Plating Posters Inc Creative Lead*
*v1.0 — 2026-04-24*

This document is the construction workup for Poster #24. It covers the power supply side of electroplating — the piece of equipment that every plating line depends on but most operators understand only at the "turn the knob" level. The poster demystifies rectifier types, waveform characteristics, ripple, and the when/why of pulse and periodic reverse plating.

> **Workflow note:** Poster generation uses claude.ai chat (SVG/HTML visual artifacts). These specs feed the Claude Chat Generation Prompt engineered by Elara. If Drew approves the generated output, it proceeds to final production.

**What makes this poster valuable:** Rectifiers are the heartbeat of any plating line. A shop foreman who understands waveforms can diagnose burning, roughness, and poor distribution problems that have nothing to do with chemistry. This poster bridges the gap between "electrical equipment" and "plating quality" — a connection that most training programs treat as an afterthought.

**Who it's for:** Line operators, maintenance electricians, process engineers, and shop supervisors. The electrician learns why the plating engineer cares about ripple; the plating engineer learns what to ask the electrician.

---

## Part 1 — Workflow Orientation

### Design Capabilities for This Poster

- Text boxes with precise font, size, weight, color, and spacing control
- Solid-color rectangles and rounded rectangles for callout boxes, table rows, waveform display backgrounds, and accent borders
- Line elements for waveform diagrams (square waves, sawtooth approximations, pulse trains)
- Circle shapes for ripple percentage gauges or indicator badges
- Color fills set to exact hex values
- Background page color set to exact hex
- Icon library search for lightning bolt, sine wave, gauge, wrench icons
- Export at print-quality PDF (300 DPI equivalent via print export)

### Limitations to Flag for Elara

1. **Waveform comparison panel (Block B — HERO):** Four waveform diagrams side by side showing DC (flat line), pulsed DC (square wave), periodic reverse (alternating positive/negative square wave), and unfiltered DC (rippled sine-ish wave). Each waveform is built from lines and rectangles — the square waves are stepped horizontal/vertical line segments. The rippled wave can be approximated with a series of short angled line segments forming a zigzag. Elara should test the zigzag approach for the ripple wave; if it looks too crude, a simple dashed horizontal line with annotation "contains AC ripple component" is an acceptable fallback.

2. **Ripple effect strip (Block D):** A horizontal bar showing ripple percentage from 0% to 25%+ with green/yellow/red zones. Same construction as Poster #23's parameter gauges — horizontal bar variant.

3. **PR timing diagram (Block F):** A single waveform showing cathodic (above baseline) and anodic (below baseline) pulses with labeled timing. Built from rectangles — positive rectangle above a horizontal centerline, negative rectangle below. Straightforward.

4. **4 pt left-border accents on callout boxes:** Same technique as all previous posters.

5. **Global Colors / swatch remap for Light edition:** Manual recolor per remap table.

6. **JetBrains Mono font:** Ensure font is available. Fallback: Courier Prime.

7. **Print size — 24x36":** Set to exactly 24 inches wide by 36 inches tall at document creation.

---

## Part 2 — Document Setup Instructions (for Elara's prompt)

### Step 1 — Create the document
- Open the design tool. Create a new custom-size design.
- Width: **24 inches**. Height: **36 inches**.

### Step 2 — Set the background color
- Set the page background color to: **`#1A1F2E`** (Gunmetal Dark)

### Step 3 — Upload fonts
Upload from Google Fonts / JetBrains.org (if not already uploaded from previous posters):
- **Barlow Condensed ExtraBold** — all headlines and section labels
- **Barlow SemiBold** — all subheadings, callout titles
- **Inter Regular** and **Inter Medium** — all body text, table data, and descriptions
- **JetBrains Mono Regular** — all parameter data, electrical values, version number

If JetBrains Mono upload fails, substitute **Courier Prime**.

### Step 4 — Set up color palette

| Color Name | Hex | Primary Use |
|---|---|---|
| Gunmetal Dark | `#1A1F2E` | Background (Dark edition) |
| Warm White | `#F0EDE8` | All primary text (Dark edition) |
| Amber | `#E8A020` | Ripple warning zones, caution indicators, pulsed DC accent |
| Teal | `#2EC4B6` | PR waveform accents, cathodic pulse indicators, parameter values |
| Emerald | `#27AE60` | Clean DC waveform, optimal ripple zone, best practice callouts |
| Coral | `#E05C5C` | Danger zones, excessive ripple, fault indicators |
| Mid Slate | `#3A4055` | Table headers, waveform background panels, divider lines |
| Deep Navy | `#0D1020` | Footer band background |
| Dark Callout | `#1E2435` | Callout box fills, waveform display backgrounds |
| Alt Row | `#252B3D` | Alternating table rows |
| Bright Silver | `#C8D0D8` | Baseline reference lines, neutral elements |

### Step 5 — Set ruler guides

**Vertical guides (from left edge):**
- 0.5" — left safe zone margin
- 23.5" — right safe zone margin

**Horizontal guides (from top edge):**
- 0.5" — top safe zone margin
- 2.9" — Zone 1/Zone 2 boundary
- 11.0" — Zone 2/Zone 3 boundary
- 16.5" — Zone 3/Zone 4 boundary
- 21.0" — Zone 4/Zone 5 boundary
- 27.0" — Zone 5/Zone 6 boundary
- 32.5" — Zone 6/Zone 7 boundary
- 35.5" — bottom safe zone margin

---

## Part 3 — Layout Zones and Build Order

Build in this sequence. Each zone is a discrete group of elements. Complete one zone before moving to the next. **Group each zone (Ctrl+G / Cmd+G) after completing it.**

```
ZONE 1 — HEADER BAND (0"–2.9")
  Block A: Headline + subheading + tagline

ZONE 2 — WAVEFORM COMPARISON PANEL (2.9"–11.0" / ~8.1" tall)
  Block B: Four waveform diagrams (DC, Pulsed DC, Periodic Reverse, Unfiltered/Ripple)
  Block C: Key characteristics strip below each waveform

ZONE 3 — RIPPLE: THE HIDDEN ENEMY (11.0"–16.5" / ~5.5" tall)
  Block D: Ripple percentage bar gauge with green/yellow/red zones
  Block DD: Ripple effects callout cards (3 cards)

ZONE 4 — WHEN TO USE WHAT (16.5"–21.0" / ~4.5" tall)
  Block E: Application selection matrix (process vs. recommended waveform)

ZONE 5 — PULSE AND PR DEEP DIVE (21.0"–27.0" / ~6.0" tall)
  Block F: PR timing diagram with labeled parameters
  Block FF: Pulse plating benefits callout + PR benefits callout (side by side)

ZONE 6 — RECTIFIER MAINTENANCE QUICK CHECK (27.0"–32.5" / ~5.5" tall)
  Block G: Maintenance checklist (left half)
  Block H: Troubleshooting quick reference (right half)

ZONE 7 — FOOTER BAND (32.5"–36.0" / ~3.5" tall)
  Block J: Disclaimer + poster title + series name + logo placeholder + version
```

---

## Part 4 — Zone-by-Zone Build Specifications

### ZONE 1 — Header Band

**Dimensions:** Full page width. Y: 0" to 2.9".
**Background:** Same as page (`#1A1F2E`) — no separate fill needed.

---

**BLOCK A — Headline**

- Element type: Text box
- Position: X: 0.5" (left safe zone). Y: 0.5" (top safe zone)
- Width: 23.0" (full safe zone width)
- Font: Barlow Condensed ExtraBold
- Size: 90 pt
- Color: `#F0EDE8`
- Letter spacing: Tight (approximately -4)
- Text (all caps):

> RECTIFIER FUNDAMENTALS

**BLOCK A — Subheading**

- Element type: Text box
- Position: X: 0.5". Y: immediately below headline baseline + 6 pt gap (approximately Y: 1.5")
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 36 pt
- Color: `#E8A020` (Amber)
- Text:

> DC, Pulse, and Periodic Reverse — The Power Behind Every Plated Part

**BLOCK A — Tagline**

- Element type: Text box
- Position: X: 0.5". Y: immediately below subheading baseline + 6 pt gap (approximately Y: 2.3")
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8`
- Transparency: 65%
- Text:

> Your rectifier is not just a power supply — it shapes every atom that lands on the cathode.

---

### ZONE 2 — Waveform Comparison Panel (HERO)

**Dimensions:** Full page width within margins. Y: 2.9" to 11.0" (~8.1" tall).

---

**Section label:**
- Element type: Text box
- Position: Centered horizontally. Y: 3.1"
- Font: Barlow Condensed ExtraBold
- Size: 28 pt
- Color: `#F0EDE8`
- Alignment: Center
- Text:

> THE FOUR WAVEFORMS YOU NEED TO KNOW

---

**BLOCK B — Four Waveform Display Panels**

Y: 3.8" to 8.5" (~4.7" tall). Four rounded-rectangle display panels evenly spaced across the safe zone.

Each panel:
- Element type: Rounded rectangle
- Width: 5.5". Height: 4.5"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 6 pt

| Panel | X Position | Accent Color | Waveform Type |
|---|---|---|---|
| 1 | 0.5" | `#27AE60` (Emerald) | Straight DC |
| 2 | 6.25" | `#E8A020` (Amber) | Pulsed DC |
| 3 | 12.0" | `#2EC4B6` (Teal) | Periodic Reverse |
| 4 | 17.75" | `#E05C5C` (Coral) | Unfiltered (Rippled) DC |

**Inside each panel (top to bottom):**

*Panel 1 — Straight DC:*

Title:
- Font: Barlow Condensed ExtraBold, 22 pt, `#27AE60`
- Text: `STRAIGHT DC`

Waveform area (centered, 4.5" wide x 2.0" tall):
- Background: Rounded rectangle, `#252B3D`, height 2.0"
- Baseline: Horizontal line, 1 pt, `#C8D0D8` at 40% — represents zero volts
- Waveform: A single horizontal line at ~70% height of the waveform area, stroke 3 pt, `#27AE60` — represents constant DC output
- Label on waveform: `V` — JetBrains Mono Regular, 11 pt, `#27AE60`

Description (below waveform):
- Font: Inter Regular, 14 pt, `#F0EDE8`
- Text:

> Steady, uninterrupted current flow. The standard for most plating baths. Simple, reliable, and well-understood.

Key stat:
- Font: JetBrains Mono Regular, 12 pt, `#27AE60`
- Text: `Used in: ~80% of all plating operations`

*Panel 2 — Pulsed DC:*

Title:
- Font: Barlow Condensed ExtraBold, 22 pt, `#E8A020`
- Text: `PULSED DC`

Waveform area:
- Baseline: same as Panel 1
- Waveform: A square wave — alternating between high (70% height) and zero (baseline). 4-5 complete cycles across the width. Built from horizontal and vertical line segments, stroke 3 pt, `#E8A020`.
- Labels: `T-on` above a high segment, `T-off` above a low segment — JetBrains Mono Regular, 10 pt, `#E8A020`

Description:
- Font: Inter Regular, 14 pt, `#F0EDE8`
- Text:

> Current pulses on and off. During T-off, ions replenish at the cathode surface. Finer grain, better throwing power.

Key stat:
- Font: JetBrains Mono Regular, 12 pt, `#E8A020`
- Text: `Duty cycle: T-on / (T-on + T-off) x 100%`

*Panel 3 — Periodic Reverse:*

Title:
- Font: Barlow Condensed ExtraBold, 22 pt, `#2EC4B6`
- Text: `PERIODIC REVERSE`

Waveform area:
- Baseline: centered at 50% height (represents zero)
- Waveform: Rectangles above baseline (cathodic/forward pulses, `#2EC4B6`) and rectangles below baseline (anodic/reverse pulses, `#E05C5C`). Show 3 cycles — cathodic pulse is wider/taller than anodic pulse to show typical asymmetry.
- Labels: `Cathodic` above, `Anodic` below — JetBrains Mono Regular, 10 pt, respective colors

Description:
- Font: Inter Regular, 14 pt, `#F0EDE8`
- Text:

> Current reverses polarity. Anodic pulse selectively dissolves HCD buildup, leveling the deposit. Exceptional for through-hole plating.

Key stat:
- Font: JetBrains Mono Regular, 12 pt, `#2EC4B6`
- Text: `Cathodic:Anodic ratio typically 3:1 to 20:1`

*Panel 4 — Unfiltered (Rippled) DC:*

Title:
- Font: Barlow Condensed ExtraBold, 22 pt, `#E05C5C`
- Text: `UNFILTERED DC (RIPPLE)`

Waveform area:
- Baseline: same as Panel 1
- Waveform: A zigzag line (approximating a rectified sine wave with significant AC component) oscillating around the 70% height mark. Built from short angled line segments, stroke 3 pt, `#E05C5C`. The oscillations should dip below the intended DC level and peak above it.
- Labels: `Peak` at top, `Valley` at bottom of oscillation — JetBrains Mono Regular, 10 pt, `#E05C5C`

Description:
- Font: Inter Regular, 14 pt, `#F0EDE8`
- Text:

> What happens when filtering capacitors or SCRs degrade. The AC ripple component causes uneven deposition — roughness, burning, and poor coverage.

Key stat:
- Font: JetBrains Mono Regular, 12 pt, `#E05C5C`
- Text: `Ripple % = (Peak - Valley) / Avg x 100`

---

**BLOCK C — Characteristics Strip** (below the four panels)

Y: 9.0" to 10.8" (~1.8" tall)

A summary strip with four columns aligned under each panel:

| Column | Accent Color | Content |
|---|---|---|
| Straight DC | `#27AE60` | `Grain size: Standard` / `Throwing power: Standard` / `Equipment cost: Lowest` |
| Pulsed DC | `#E8A020` | `Grain size: Finer` / `Throwing power: Improved` / `Equipment cost: Moderate` |
| Periodic Reverse | `#2EC4B6` | `Grain size: Finest` / `Throwing power: Best` / `Equipment cost: Highest` |
| Unfiltered DC | `#E05C5C` | `Grain size: Coarse/uneven` / `Throwing power: Degraded` / `Equipment cost: N/A (fault)` |

Each column:
- Width: 5.5". Fill: `#252B3D`. Corner radius: 4 pt.
- Font: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Labels in Inter Medium 12 pt at 60%.
- Accent color for the column header label (e.g., `STRAIGHT DC`) in respective color.

---

### ZONE 3 — Ripple: The Hidden Enemy

**Dimensions:** Full page width within margins. Y: 11.0" to 16.5" (~5.5" tall).

---

**Section label:**
- Element type: Text box
- Position: Centered horizontally. Y: 11.2"
- Font: Barlow Condensed ExtraBold
- Size: 28 pt
- Color: `#F0EDE8`
- Alignment: Center
- Text:

> RIPPLE — THE HIDDEN ENEMY OF DEPOSIT QUALITY

---

**BLOCK D — Ripple Percentage Bar Gauge**

Y: 11.8" to 13.0" (~1.2" tall).

A horizontal bar spanning the full safe zone width (23.0"), divided into three colored segments:

- Element type: Rounded rectangle (overall container)
- Position: X: 0.5". Y: 11.8"
- Width: 23.0". Height: 0.8"
- Corner radius: 4 pt
- Fill: `#252B3D`

Inside the bar, three colored segments:

| Segment | Width | Fill | Label Above | Range |
|---|---|---|---|---|
| Green (optimal) | 0"–9.2" (40% of bar) | `#27AE60` at 30% | `ACCEPTABLE` | `0–5% ripple` |
| Yellow (caution) | 9.2"–16.1" (30% of bar) | `#E8A020` at 30% | `CAUTION` | `5–10% ripple` |
| Red (danger) | 16.1"–23.0" (30% of bar) | `#E05C5C` at 30% | `DANGER` | `>10% ripple` |

Labels above each segment:
- Font: Barlow SemiBold, 14 pt, respective accent color

Range labels inside/below each segment:
- Font: JetBrains Mono Regular, 14 pt, `#F0EDE8`

Key callout below gauge:
- Position: Centered, Y: 13.0"
- Font: Inter Medium, 16 pt, `#E05C5C`
- Text:

> Decorative chrome and bright nickel are the most ripple-sensitive processes — keep below 5%. Chrome and bright Ni: target <3%.

---

**BLOCK DD — Ripple Effects Cards** (three cards)

Y: 13.5" to 16.3" (~2.8" tall). Three cards side by side.

Each card:
- Element type: Rounded rectangle
- Width: 7.33". Height: 2.5"
- Fill: `#1E2435`. Corner radius: 6 pt.
- Left-border accent: 0.06" wide, full height

| Card | X | Accent | Title | Content |
|---|---|---|---|---|
| 1 | 0.5" | `#27AE60` | `WHAT CAUSES RIPPLE` | `Aging SCR components` / `Failed filter capacitors` / `Loose bus bar connections` / `Undersized transformer for load` |
| 2 | 8.0" | `#E8A020` | `WHAT RIPPLE DOES` | `Roughness and nodular deposits` / `Burning at HCD areas` / `Reduced brightness in Ni` / `Poor adhesion on thin deposits` / `Inconsistent thickness` |
| 3 | 15.5" | `#E05C5C` | `HOW TO CHECK` | `Oscilloscope across output terminals` / `Compare peak-to-peak vs. DC average` / `Check under FULL LOAD — not idle` / `Measure at rectifier AND at tank` |

Card title: Barlow SemiBold, 18 pt, accent color.
Card body: Inter Regular, 15 pt, `#F0EDE8`, line height 145%.

---

### ZONE 4 — When to Use What

**Dimensions:** Full page width within margins. Y: 16.5" to 21.0" (~4.5" tall).

---

**Section label:**
- Element type: Text box
- Position: Centered horizontally. Y: 16.7"
- Font: Barlow Condensed ExtraBold
- Size: 28 pt
- Color: `#F0EDE8`
- Alignment: Center
- Text:

> CHOOSING THE RIGHT WAVEFORM

---

**BLOCK E — Application Selection Matrix**

Y: 17.3" to 20.8" (~3.5" tall).

A table with process names on the left and waveform recommendations:

Header row:
- Element type: Rectangle, fill `#3A4055`
- Text: Barlow SemiBold, 14 pt, `#F0EDE8`
- Labels: `Process` | `Straight DC` | `Pulsed DC` | `Periodic Reverse` | `Notes`
- Column widths: 5.0" | 3.5" | 3.5" | 3.5" | 7.5"

| Process | DC | Pulse | PR | Notes |
|---|---|---|---|---|
| Acid copper | Standard | Good | Excellent for PCB | PR eliminates dog-boning on through-holes |
| Watts nickel (bright) | Standard | Rarely | No | Additives tuned for DC; PR disrupts brightener system |
| Hard chrome | Standard | Emerging | No | Must have <5% ripple; pulse may improve microcrack density in specialized processes |
| Zinc (acid/alk) | Standard | Good | Good | Pulse improves LCD coverage in barrel |
| Gold (hard) | Standard | Excellent | Good | Pulse gives finer grain, better hardness |
| Tin-lead / Tin | Standard | Good | Good | PR reduces whisker risk in some alloys |
| Copper sulfate (decorative) | Standard | Good | Rarely | Pulse improves leveling |

Data font: Inter Regular, 14 pt, `#F0EDE8`.
Process names: Inter Medium, 14 pt, `#F0EDE8`.
"Standard" in `#27AE60`, "Good" in `#E8A020`, "Excellent" in `#2EC4B6`, "Rarely" / "No" in `#E05C5C`.
Alternating row fills: `#1E2435` / `#252B3D`.

---

### ZONE 5 — Pulse and PR Deep Dive

**Dimensions:** Full page width within margins. Y: 21.0" to 27.0" (~6.0" tall).

---

**Section label:**
- Element type: Text box
- Position: Centered horizontally. Y: 21.2"
- Font: Barlow Condensed ExtraBold
- Size: 28 pt
- Color: `#F0EDE8`
- Alignment: Center
- Text:

> PULSE AND PERIODIC REVERSE — THE DETAILS

---

**BLOCK F — PR Timing Diagram** (left half, X: 0.5" to 11.5")

Y: 21.8" to 26.8" (~5.0" tall).

A single large waveform diagram showing one complete PR cycle with labeled components:

Diagram background:
- Element type: Rounded rectangle
- Position: X: 0.5". Y: 21.8"
- Width: 11.0". Height: 4.8"
- Fill: `#1E2435`. Corner radius: 6 pt.

Baseline (zero current):
- Horizontal line at vertical center of diagram
- Stroke: 1 pt, `#C8D0D8` at 40%
- Label at left end: `0 A` — JetBrains Mono Regular, 11 pt, `#C8D0D8`

Cathodic pulse (above baseline):
- Element type: Rectangle
- Fill: `#2EC4B6` at 25%
- Border top: 3 pt, `#2EC4B6`
- Height: ~40% of diagram height (above baseline)
- Width: ~60% of diagram width
- Label inside: `CATHODIC (FORWARD)` — Barlow SemiBold, 14 pt, `#2EC4B6`
- Current label: `I-cathodic` — JetBrains Mono Regular, 12 pt, `#2EC4B6`
- Time label below: `T-cathodic` with double-headed arrow spanning width — JetBrains Mono Regular, 12 pt, `#F0EDE8`

Anodic pulse (below baseline):
- Element type: Rectangle
- Fill: `#E05C5C` at 25%
- Border bottom: 3 pt, `#E05C5C`
- Height: ~25% of diagram height (below baseline) — shorter than cathodic to show asymmetry
- Width: ~20% of diagram width
- Label inside: `ANODIC (REVERSE)` — Barlow SemiBold, 12 pt, `#E05C5C`
- Time label below: `T-anodic` — JetBrains Mono Regular, 12 pt, `#F0EDE8`

Key parameters listed below diagram:
- Position: X: 0.5". Y: 26.0"
- Font: JetBrains Mono Regular, 13 pt, `#F0EDE8`
- Text:

> Duty cycle = T-cathodic / (T-cathodic + T-anodic)
> Charge ratio = (I-cathodic x T-cathodic) / (I-anodic x T-anodic)
> Net deposition requires charge ratio > 1.0

---

**BLOCK FF — Benefits Callouts** (right half, X: 12.0" to 23.5")

Y: 21.8" to 26.8"

Two stacked callout boxes:

**Top — Pulse Plating Benefits:**
- Element type: Rounded rectangle
- Position: X: 12.0". Y: 21.8"
- Width: 11.5". Height: 2.2"
- Fill: `#1E2435`. Left-border accent: `#E8A020`.
- Title: `PULSE PLATING BENEFITS` — Barlow SemiBold, 18 pt, `#E8A020`
- Body: Inter Regular, 15 pt, `#F0EDE8`, line height 145%
- Text:

> - Finer grain structure — harder, denser deposits
> - Better throwing power — improved LCD coverage
> - Reduced hydrogen embrittlement risk
> - Lower internal stress in many systems
> - Can plate at higher peak CD than DC average would allow

**Bottom — PR Plating Benefits:**
- Element type: Rounded rectangle
- Position: X: 12.0". Y: 24.3"
- Width: 11.5". Height: 2.3"
- Fill: `#1E2435`. Left-border accent: `#2EC4B6`.
- Title: `PERIODIC REVERSE BENEFITS` — Barlow SemiBold, 18 pt, `#2EC4B6`
- Body: Inter Regular, 15 pt, `#F0EDE8`, line height 145%
- Text:

> - Levels HCD/LCD distribution — the reverse pulse "shaves the peaks"
> - Eliminates dog-boning on PCB through-holes
> - Reduces nodule formation in hard chrome
> - Enables plating into deep recesses and blind holes
> - Can replace or supplement thieves in some applications

---

### ZONE 6 — Rectifier Maintenance Quick Check

**Dimensions:** Full page width within margins. Y: 27.0" to 32.5" (~5.5" tall).

---

**BLOCK G — Maintenance Checklist** (left half, X: 0.5" to 11.5")

Y: 27.0" to 32.3"

**Callout container:**
- Element type: Rounded rectangle
- Position: X: 0.5". Y: 27.0"
- Width: 11.0". Height: 5.2"
- Fill: `#1E2435`. Corner radius: 6 pt.
- Left-border accent: `#27AE60` (Emerald)

Callout title:
- Font: Barlow SemiBold, 20 pt, `#27AE60`
- Text:

> PREVENTIVE MAINTENANCE CHECKLIST

Bullet list:
- Font: Inter Regular, 15 pt, `#F0EDE8`
- Line height: 150%
- Text:

> - Check bus bar connections for heat/discoloration (monthly)
> - Measure output ripple under full load (quarterly)
> - Inspect cooling fans and air filters (monthly)
> - Verify ammeter/voltmeter calibration (annually)
> - Check anode and cathode connections for corrosion
> - Inspect SCR/diode modules — replace at first sign of degradation
> - Clean heat sinks — dust reduces cooling efficiency
> - Log ampere-hours for maintenance scheduling

---

**BLOCK H — Troubleshooting Quick Reference** (right half, X: 12.0" to 23.5")

Y: 27.0" to 32.3"

**Callout container:**
- Element type: Rounded rectangle
- Position: X: 12.0". Y: 27.0"
- Width: 11.5". Height: 5.2"
- Fill: `#1E2435`. Corner radius: 6 pt.
- Left-border accent: `#E05C5C` (Coral)

Callout title:
- Font: Barlow SemiBold, 20 pt, `#E05C5C`
- Text:

> RECTIFIER TROUBLESHOOTING

Table (5 rows):

| Symptom | Likely Cause | Check |
|---|---|---|
| Output drops under load | Failing SCR/diode module | Measure ripple; check individual diodes |
| Hot bus bars | Loose connection | Torque all connections; infrared scan |
| Ammeter reads high but plating thin | Stray current / ground fault | Check tank insulation; isolate buss |
| Erratic current | Loose control wire / failed SCR | Scope the output waveform |
| Burning at HCD only | Excess ripple | Measure ripple %; check filter caps |

Header: Barlow SemiBold, 13 pt, `#F0EDE8`. Data: Inter Regular, 14 pt, `#F0EDE8`. Symptom column: Inter Medium, 14 pt, `#E05C5C`. Alternating rows: `#1E2435` / `#252B3D`.

---

### ZONE 7 — Footer Band

**Dimensions:** Full page width. Y: 32.5" to 36.0" (~3.5" tall).

---

**Footer band background:**
- Element type: Rectangle
- Position: X: 0". Y: 32.5"
- Width: 24.0". Height: 3.5"
- Fill: `#0D1020` (Deep Navy)

**Disclaimer:**
- Element type: Text box
- Position: X: 0.5". Y: 32.8"
- Width: 23.0"
- Font: Inter Regular
- Size: 11 pt
- Color: `#F0EDE8` at 50% opacity
- Alignment: Center
- Text:

> This poster is an educational reference tool. Waveform types, ripple thresholds, and application recommendations are typical industry values. Specific rectifier selection, pulse parameters, and PR settings vary by process, chemistry, and equipment manufacturer. Consult your rectifier supplier and process engineer for application-specific guidance.

**Poster title:**
- Element type: Text box
- Position: X: 0.5". Y: 33.5"
- Font: Barlow SemiBold
- Size: 16 pt
- Color: `#F0EDE8`
- Text:

> Rectifier Fundamentals — DC, Pulse, and Periodic Reverse

**Series name:**
- Element type: Text box
- Position: Centered horizontally. Y: 34.2"
- Font: Inter Regular
- Size: 14 pt
- Color: `#F0EDE8` at 70% opacity
- Alignment: Center
- Text:

> Plating Posters Inc — Metal Finishing Reference Series

**Logo placeholder:**
- Element type: Rectangle (placeholder)
- Position: X: 22.5". Y: 33.3"
- Width: 0.83" (60 pt). Height: 0.42" (30 pt)
- Fill: `#3A4055`
- Text inside: `[LOGO]` — Inter Regular, 10 pt, `#F0EDE8` at 50%

**Version:**
- Element type: Text box
- Position: X: 0.5". Y: 35.0"
- Font: JetBrains Mono Regular
- Size: 11 pt
- Color: `#F0EDE8` at 50% opacity
- Text:

> v1.0 — 2026

---

## Part 5 — Grouping and Naming Convention

| Group Name | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline |
| Zone 2 - Waveform Comparison | Section label, four waveform display panels, characteristics strip |
| Zone 3 - Ripple | Section label, ripple bar gauge, three effects cards |
| Zone 4 - Application Matrix | Section label, process vs. waveform table |
| Zone 5 - Pulse and PR | Section label, PR timing diagram, two benefits callouts |
| Zone 6 - Maintenance | Maintenance checklist, troubleshooting table |
| Zone 7 - Footer | Footer band, disclaimer, poster title, series name, logo placeholder, version |

---

## Part 6 — Light Edition Color Remap Table

Duplicate the completed Dark edition page. Work through this table from top to bottom:

| Dark Hex | Light Hex | Notes |
|----------|-----------|-------|
| `#1A1F2E` | `#F5F4F0` | Background and all BG-colored elements |
| `#F0EDE8` | `#1A1F2E` | All primary text |
| `#1E2435` | `#ECEEF4` | Callout box fills, waveform display backgrounds |
| `#252B3D` | `#E8E8F0` | Alternate row backgrounds, characteristics strip |
| `#0D1020` | `#1A1F2E` | Footer strip background |
| `#E8A020` | `#C8860A` | Amber accent elements |
| `#2EC4B6` | `#1A8C82` | Teal accent elements |
| `#27AE60` | `#1E7A47` | Emerald accent elements |
| `#E05C5C` | `#B83E3E` | Coral accent elements |
| `#3A4055` | `#D0D4DE` | Table headers, dividers |
| `#C8D0D8` | `#C8D0D8` | Bright Silver — **unchanged** |

Waveform stroke colors shift to darkened variants. Verify waveform lines remain clearly visible on the light `#ECEEF4` panel backgrounds.

---

## Part 7 — Export Checklist

Six files per poster:

| File Name | Mode | Quality | Bleed + Marks |
|---|---|---|---|
| `Rectifier Fundamentals — Dark — 24x36 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Rectifier Fundamentals — Dark — 18x24 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Rectifier Fundamentals — Dark — Digital.pdf` | RGB | PDF Standard | No |
| `Rectifier Fundamentals — Light — 24x36 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Rectifier Fundamentals — Light — 18x24 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Rectifier Fundamentals — Light — Digital.pdf` | RGB | PDF Standard | No |

For 18x24" versions: verify all text meets the 14 pt body text minimum floor. The waveform panels (Zone 2) will need careful review at 18x24" to ensure waveform line segments and labels remain legible.

---

## Design Notes

This poster fills a gap that no other poster in the series addresses: the electrical side of electroplating. Most platers think of their rectifier as a black box — turn the dial, read the meter. This poster makes them literate in waveforms, which directly connects to deposit quality issues they deal with every day.

The hero visual (four waveform panels) is designed to be instantly comparative — a shop supervisor can point to Panel 4 (rippled DC) and say "this is what's happening to us" in a way that abstract electrical theory never could. The ripple section (Zone 3) is the poster's strongest practical message — it gives operators a concrete thing to check and a concrete threshold to hold to.

The application matrix (Zone 4) is deliberately conservative — "Standard" for DC in most applications acknowledges that pulse and PR are advanced techniques, not everyday necessities. This prevents the poster from overselling expensive equipment to shops that don't need it.

---

*Alaina — Plating Posters Inc Creative Lead*
*Poster #24 — Rectifier Fundamentals — Construction Workup v1.0*
*2026-04-24*
