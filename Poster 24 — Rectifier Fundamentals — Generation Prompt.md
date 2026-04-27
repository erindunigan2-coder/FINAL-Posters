---
Project: Plating Posters Inc
Poster Number: 24
Title: "Rectifier Fundamentals -- DC, Pulse, and Periodic Reverse"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-25T00:00:00
Source: Poster 24 -- Rectifier Fundamentals -- Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - Rectifier
  - PulsePlating
  - PeriodicReverse
  - Waveforms
  - v1
---

# Claude Chat Generation Prompt -- Poster #24
## Rectifier Fundamentals -- DC, Pulse, and Periodic Reverse
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-25).*

---

> **IMPORTANT:** Generate as a single self-contained HTML file. 1200x1800 CSS px, wrapped in a `.stage` flex container that scales to fit the browser via `transform: scale()`. Dark edition first. Must implement the full iOS 18 Liquid Glass aesthetic from the canonical design file. Must include all print CSS rules, tweaks panel, and dark/light toggle. Reference: `Plating Posters Inc/Claude Design Output/Plating Posters - Series Design Prompt.md`.

---

## Phase 0 -- Series Design System

This poster MUST conform to the Plating Posters Inc Series Design Prompt in its entirety. Key requirements:

- **Output:** single self-contained HTML file, 1200x1800 CSS px
- **Aesthetic:** industrial-technical meets iOS 18 Liquid Glass -- frosted glass cards, ambient color orbs, faint grid texture
- **Palette:** Gunmetal Dark `#1A1F2E`, Warm White `#F0EDE8`, Amber `#E8A020`, Teal `#2EC4B6`, Emerald `#27AE60`, Coral `#E05C5C`, Mid Slate `#3A4055`, Deep Navy `#0D1020`, Dark Callout `#1E2435`, Alt Row `#252B3D`, Silver `#C8D0D8`
- **Fonts (Google Fonts CDN):** Barlow Condensed 800/900 (headlines), Barlow 600/700 (step names, emphasis), Inter 400/500/600 (body), JetBrains Mono 400/500 (specs, data)
- **Glass surfaces:** `background-color: rgba(30,36,53,.55)` solid fallback + translucent gradient + `backdrop-filter: blur(18px) saturate(140%)` + standard inset highlights and ambient shadow. Border-radius 12-18px.
- **Background:** three ambient color orbs (teal, amber, coral) via radial-gradient, plus faint 50x50px grid with radial mask
- **Print CSS:** `@page { size: 12.5in 18.75in; margin: 0; }`. All glass surfaces have solid background-color fallbacks. NEVER use `color-mix()`. NEVER use `opacity` on absolutely-positioned pseudo-elements. Strip backdrop-filter at print time.
- **Tweaks panel:** floating bottom-right, outside poster stage. Dark/Light toggle, Grid lines toggle, Print button.
- **Light edition:** via `body[data-edition="light"]` CSS overrides (NOT a separate file)
- **Scaling:** `.stage` flex container wraps fixed 1200x1800 poster; scales on resize via JS `transform: scale()`

---

## Phase 1 -- Foundation

Standard: 1200x1800 CSS px, `#1A1F2E` background, locked palette, 25px safe-zone padding. Three ambient orbs. Faint grid overlay.

---

## Phase 2 -- Header (Zone 1)

### Step 1 -- `RECTIFIER FUNDAMENTALS` -- Barlow Condensed 900, ~96px, `#F0EDE8`, tight tracking.
### Step 2 -- `DC, Pulse, and Periodic Reverse -- The Power Behind Every Plated Part` -- Barlow 700, ~30px, `#E8A020`.
### Step 3 -- `Your rectifier is not just a power supply -- it shapes every atom that lands on the cathode.` -- Inter 400, ~18px, `#F0EDE8` at 65% opacity.

---

## Phase 3 -- Waveform Comparison Panel (Zone 2 -- HERO)

Section label: `THE FOUR WAVEFORMS YOU NEED TO KNOW` -- Barlow Condensed 800, 28px, centered.

### Step 4 -- Four glass cards side by side

Each card: glass surface, colored top accent strip.

| Card | Accent | Title | Waveform |
|---|---|---|---|
| 1 | `#27AE60` Emerald | STRAIGHT DC | Flat horizontal line at ~70% height |
| 2 | `#E8A020` Amber | PULSED DC | Square wave -- alternating high (70%) / zero segments, 4-5 cycles |
| 3 | `#2EC4B6` Teal | PERIODIC REVERSE | Rectangles above (cathodic, teal) and below (anodic, coral) baseline. Cathodic wider/taller |
| 4 | `#E05C5C` Coral | UNFILTERED DC (RIPPLE) | Zigzag line oscillating around 70% height |

**Waveform diagrams:** Built from inline SVG paths inside each card. Baseline: silver dashed line. Waveform stroke: 3px, accent color. Labels in JetBrains Mono 10-11px.

**Card descriptions (Inter 400, ~13px):**
1. `Steady, uninterrupted current flow. The standard for most plating baths. Simple, reliable, and well-understood.`
2. `Current pulses on and off. During T-off, ions replenish at the cathode surface. Finer grain, better throwing power.`
3. `Current reverses polarity. Anodic pulse selectively dissolves HCD buildup, leveling the deposit. Exceptional for through-hole plating.`
4. `What happens when filtering capacitors or SCRs degrade. The AC ripple component causes uneven deposition -- roughness, burning, and poor coverage.`

**Key stats (JetBrains Mono, ~11px, accent color):**
1. `Used in: ~80% of all plating operations`
2. `Duty cycle: T-on / (T-on + T-off) x 100%`
3. `Cathodic:Anodic ratio typically 3:1 to 20:1`
4. `Ripple % = (Peak - Valley) / Avg x 100`

### Step 5 -- Characteristics strip below cards

Four columns aligned under each card. Glass surface, accent-colored header.

| Column | Grain Size | Throwing Power | Equipment Cost |
|---|---|---|---|
| Straight DC | Standard | Standard | Lowest |
| Pulsed DC | Finer | Improved | Moderate |
| Periodic Reverse | Finest | Best | Highest |
| Unfiltered DC | Coarse/uneven | Degraded | N/A (fault) |

JetBrains Mono 11px for values, Inter Medium 11px at 60% for labels.

---

## Phase 4 -- Ripple: The Hidden Enemy (Zone 3)

Section label: `RIPPLE -- THE HIDDEN ENEMY OF DEPOSIT QUALITY` -- Barlow Condensed 800, 28px, centered.

### Step 6 -- Ripple percentage bar gauge

Full-width horizontal bar with three proportional colored segments:

| Segment | Width | Fill | Label | Range |
|---|---|---|---|---|
| Green | 40% | `#27AE60` at 30% | ACCEPTABLE | 0-5% ripple |
| Yellow | 30% | `#E8A020` at 30% | CAUTION | 5-10% ripple |
| Red | 30% | `#E05C5C` at 30% | DANGER | >10% ripple |

Key callout below: `Decorative chrome and bright nickel are the most ripple-sensitive processes -- keep below 5%. Chrome and bright Ni: target <3%.` -- Inter Medium, coral.

### Step 7 -- Three ripple effects cards

| Card | Accent | Title | Content |
|---|---|---|---|
| 1 | `#27AE60` | WHAT CAUSES RIPPLE | Aging SCR components / Failed filter capacitors / Loose bus bar connections / Undersized transformer for load |
| 2 | `#E8A020` | WHAT RIPPLE DOES | Roughness and nodular deposits / Burning at HCD areas / Reduced brightness in Ni / Poor adhesion on thin deposits / Inconsistent thickness |
| 3 | `#E05C5C` | HOW TO CHECK | Oscilloscope across output terminals / Compare peak-to-peak vs. DC average / Check under FULL LOAD -- not idle / Measure at rectifier AND at tank |

Glass cards with 4px left-border accent. Barlow 600 18px titles, Inter 400 14px body.

---

## Phase 5 -- Application Selection Matrix (Zone 4)

Section label: `CHOOSING THE RIGHT WAVEFORM` -- Barlow Condensed 800, 28px, centered.

### Step 8 -- Process vs. waveform table

Glass table. Header row: Mid Slate. Alternating rows: Dark Callout / Alt Row.

| Process | DC | Pulse | PR | Notes |
|---|---|---|---|---|
| Acid copper | Standard | Good | Excellent for PCB | PR eliminates dog-boning on through-holes |
| Watts nickel (bright) | Standard | Rarely | No | Additives tuned for DC; PR disrupts brightener system |
| Hard chrome | Standard | Emerging | No | Must have <5% ripple; pulse may improve microcrack density |
| Zinc (acid/alk) | Standard | Good | Good | Pulse improves LCD coverage in barrel |
| Gold (hard) | Standard | Excellent | Good | Pulse gives finer grain, better hardness |
| Tin-lead / Tin | Standard | Good | Good | PR reduces whisker risk in some alloys |
| Copper sulfate (dec) | Standard | Good | Rarely | Pulse improves leveling |

Color coding: `Standard` = Emerald, `Good` = Amber, `Excellent` = Teal, `Rarely` / `No` / `Emerging` = Coral.

---

## Phase 6 -- Pulse and PR Deep Dive (Zone 5)

Section label: `PULSE AND PERIODIC REVERSE -- THE DETAILS` -- Barlow Condensed 800, 28px, centered.

### Step 9 -- PR timing diagram (left half)

Large glass panel. Single PR cycle with labeled components:

- Baseline: silver dashed horizontal line at vertical center (`0 A`)
- Cathodic pulse: teal rectangle above baseline (~60% diagram width, ~40% height). Label: `CATHODIC (FORWARD)`. Current: `I-cathodic`. Time: `T-cathodic` with double-headed arrow.
- Anodic pulse: coral rectangle below baseline (~20% width, ~25% height). Label: `ANODIC (REVERSE)`. Time: `T-anodic`.

Below diagram (JetBrains Mono 12px):
- `Duty cycle = T-cathodic / (T-cathodic + T-anodic)`
- `Charge ratio = (I-cathodic x T-cathodic) / (I-anodic x T-anodic)`
- `Net deposition requires charge ratio > 1.0`

### Step 10 -- Benefits callouts (right half)

Two stacked glass cards:

**Top -- PULSE PLATING BENEFITS** (amber left border):
- Finer grain structure -- harder, denser deposits
- Better throwing power -- improved LCD coverage
- Reduced hydrogen embrittlement risk
- Lower internal stress in many systems
- Can plate at higher peak CD than DC average would allow

**Bottom -- PERIODIC REVERSE BENEFITS** (teal left border):
- Levels HCD/LCD distribution -- the reverse pulse "shaves the peaks"
- Eliminates dog-boning on PCB through-holes
- Reduces nodule formation in hard chrome
- Enables plating into deep recesses and blind holes
- Can replace or supplement thieves in some applications

---

## Phase 7 -- Maintenance and Troubleshooting (Zone 6)

### Step 11 -- Preventive maintenance checklist (left half)

Emerald-bordered glass card. Title: `PREVENTIVE MAINTENANCE CHECKLIST`.

Bullet list (Inter 400, 14px):
- Check bus bar connections for heat/discoloration (monthly)
- Measure output ripple under full load (quarterly)
- Inspect cooling fans and air filters (monthly)
- Verify ammeter/voltmeter calibration (annually)
- Check anode and cathode connections for corrosion
- Inspect SCR/diode modules -- replace at first sign of degradation
- Clean heat sinks -- dust reduces cooling efficiency
- Log ampere-hours for maintenance scheduling

### Step 12 -- Troubleshooting table (right half)

Coral-bordered glass card. Title: `RECTIFIER TROUBLESHOOTING`.

| Symptom | Likely Cause | Check |
|---|---|---|
| Output drops under load | Failing SCR/diode module | Measure ripple; check individual diodes |
| Hot bus bars | Loose connection | Torque all connections; infrared scan |
| Ammeter reads high but plating thin | Stray current / ground fault | Check tank insulation; isolate buss |
| Erratic current | Loose control wire / failed SCR | Scope the output waveform |
| Burning at HCD only | Excess ripple | Measure ripple %; check filter caps |

Header: Barlow 600, 12px. Data: Inter 400, 12px. Symptom column: coral. Alternating rows.

---

## Phase 8 -- Footer (Zone 7)

Standard footer. Dark navy `#0D1020` full-bleed band. Three blocks:

1. **Disclaimer:** `This poster is an educational reference tool. Waveform types, ripple thresholds, and application recommendations are typical industry values. Specific rectifier selection, pulse parameters, and PR settings vary by process, chemistry, and equipment manufacturer. Consult your rectifier supplier and process engineer for application-specific guidance.`
2. **Brand line:** `Rectifier Fundamentals -- DC, Pulse, and Periodic Reverse` | `Plating Posters Inc -- Metal Finishing Reference Series` | PP gradient logo square (36px)
3. **Version:** `v1.0 -- 2026 | Poster #24 -- Rectifier Fundamentals | Plating Posters Inc` -- JetBrains Mono 11px at 50%.

---

## Phase 9 -- Light Remap

Standard remap via `body[data-edition="light"]` overrides:

| Dark | Light | Notes |
|---|---|---|
| `#1A1F2E` | `#F5F4F0` | Background |
| `#F0EDE8` | `#1A1F2E` | Primary text |
| `#1E2435` | `#ECEEF4` | Callout fills |
| `#252B3D` | `#E8E8F0` | Alt rows |
| `#0D1020` | `#1A1F2E` | Footer |
| `#E8A020` | `#C8860A` | Amber |
| `#2EC4B6` | `#1A8C82` | Teal |
| `#27AE60` | `#1E7A47` | Emerald |
| `#E05C5C` | `#B83E3E` | Coral |
| `#3A4055` | `#D0D4DE` | Slate |
| `#C8D0D8` | `#C8D0D8` | Silver -- unchanged |

Verify waveform strokes remain visible on light callout backgrounds.

---

## Phase 10 -- Review Checklist

- [ ] Headline `RECTIFIER FUNDAMENTALS` ~96px Barlow Condensed 900
- [ ] Subhead in amber, tagline at 65% opacity
- [ ] Four waveform cards with SVG diagrams (DC, Pulse, PR, Ripple)
- [ ] Characteristics strip below (grain size / throwing power / cost)
- [ ] Ripple bar gauge: green / yellow / red with percentage ranges
- [ ] Three ripple effects cards (causes / effects / how to check)
- [ ] Application matrix: 7 processes x 4 columns, color-coded
- [ ] PR timing diagram with labeled cathodic/anodic pulses
- [ ] Two benefits callouts (pulse + PR)
- [ ] Maintenance checklist (8 items, emerald)
- [ ] Troubleshooting table (5 rows, coral)
- [ ] Footer with disclaimer, brand, version
- [ ] Dark/Light toggle functional
- [ ] Print CSS with solid fallbacks
- [ ] Tweaks panel (edition toggle, grid lines, print)
- [ ] No brand or supplier names anywhere in content
- [ ] All glass surfaces have solid background-color fallback

---

## Phase 11 -- Export

Six files:
- `Rectifier Fundamentals -- Dark -- 24x36 -- Print.pdf`
- `Rectifier Fundamentals -- Dark -- 18x24 -- Print.pdf`
- `Rectifier Fundamentals -- Dark -- Digital.pdf`
- `Rectifier Fundamentals -- Light -- 24x36 -- Print.pdf`
- `Rectifier Fundamentals -- Light -- 18x24 -- Print.pdf`
- `Rectifier Fundamentals -- Light -- Digital.pdf`

---

| v1.0 | 2026-04-25 | Initial. |
