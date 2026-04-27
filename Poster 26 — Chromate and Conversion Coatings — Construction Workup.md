---
Project: Plating Posters Inc
Poster Number: 26
Title: "Chromate and Conversion Coatings — Hex, Tri, and Beyond"
Document Type: Construction Workup
Status: v1.0 — Ready for Elara
Created: 2026-04-24T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - General industry knowledge (chromate conversion coatings, trivalent chrome passivation, RoHS directive)
Technical Source: General industry knowledge — hexavalent vs. trivalent chromate chemistry, conversion coating mechanisms, RoHS/REACH regulatory context, color standards, salt spray performance comparisons. ASTM B633, MIL-DTL-5541, ASTM B201 reference.
Watson Flags: THREE OPEN — (1) Confirm current RoHS exemption status for hex chrome on zinc plating (as of 2026 regulatory landscape). (2) Verify trivalent chromate salt spray performance ranges (96-200 hrs for clear on zinc) against latest industry data — performance has been closing the gap with hex. (3) Confirm the film thickness ranges for hex clear (0.05-0.25 micron) vs. hex yellow (0.25-0.75 micron) vs. tri clear vs. tri black against ASTM B633 Table 2. All non-blocking but highly important — regulatory accuracy is critical for this poster.
Tyler Flags: ONE OPEN — (1) Validate the "self-healing" property description for hex chrome films and confirm the mechanism (Cr6+ reservoir migrates to scratch site) is accurately simplified for a poster audience. Non-blocking.
Process Scope: Chromate and passivate conversion coatings applied over zinc, zinc alloy, cadmium, and aluminum substrates
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow: Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ChromateConversion
  - Trivalent
  - Hexavalent
  - RoHS
  - Passivation
  - ConstructionWorkup
---

# Poster #26 — Construction Workup
## Chromate and Conversion Coatings — Hex, Tri, and Beyond

*Alaina — Plating Posters Inc Creative Lead*
*v1.0 — 2026-04-24*

This document is the construction workup for Poster #26. It covers the post-plating conversion coating step that determines whether a zinc or zinc alloy deposit actually protects the base metal in service. This is one of the most commercially relevant topics in the series — the hex-to-tri transition is reshaping the entire zinc plating industry, and shops need a clear reference on what the options are, how they compare, and what the regulations require.

> **Workflow note:** Poster generation uses claude.ai chat (SVG/HTML visual artifacts). These specs feed the Claude Chat Generation Prompt engineered by Elara.

**What makes this poster valuable:** The hex chrome question comes up in every zinc plating shop, every week. Customers ask "do you run trivalent?" Specs call for yellow chromate, but RoHS says no hex chrome. This poster puts the comparison on the wall — chemistry, performance, regulatory status, and appearance — so the answer is always within arm's reach.

**Who it's for:** Process engineers, quality managers, sales staff who need to discuss chromate options with customers, and operators who apply chromates daily. Also valuable for purchasing managers evaluating tri-chrome vendor claims.

**Relationship to existing posters:** Builds directly on Poster #6 (Passivation Sequence) — that poster covers the process flow; this one goes deep on the conversion coating step specifically. Also connects to Poster #3 (Zinc Plating) as the natural "what happens next" after zinc deposition.

---

## Part 1 — Workflow Orientation

### Design Capabilities for This Poster

- Text boxes with precise font, size, weight, color, and spacing control
- Solid-color rectangles and rounded rectangles for comparison tables, callout boxes, and color swatch representations
- Simple shapes for cross-section diagram (layered rectangles representing substrate, zinc, conversion coating)
- Color fills set to exact hex values
- Background page color set to exact hex
- Export at print-quality PDF (300 DPI equivalent via print export)

### Limitations to Flag for Elara

1. **Coating cross-section diagram (Block B — HERO):** Three layered rectangles (substrate, zinc plate, conversion coating) shown side by side for hex clear, hex yellow, tri clear, and tri black. The conversion coating layer uses the closest available fill color to represent the actual coating appearance (clear/iridescent, yellow/gold, blue-tinted clear, black). Simple layered-rectangle construction.

2. **Color appearance swatches (Block C):** Small rectangles filled with approximate color representations of each coating type. Since actual chromate colors are iridescent/translucent, use solid fills that suggest the color: clear = very pale blue-green, yellow = golden amber, olive drab = olive green, black = near-black. These are representative, not photographic.

3. **Hex vs. Tri comparison table (Block D):** The central reference table. Wide format, 7 columns. Same construction as Poster #22's six-method table.

4. **Regulatory timeline (Block F):** A simple horizontal timeline with date markers. Built from a horizontal line with vertical tick marks and text labels.

5. **4 pt left-border accents on callout boxes.** Standard.

6. **Print size — 24x36".** Standard.

---

## Part 2 — Document Setup Instructions (for Elara's prompt)

### Step 1-3 — Standard (24x36", `#1A1F2E` background, standard font stack)

### Step 4 — Set up color palette

| Color Name | Hex | Primary Use |
|---|---|---|
| Gunmetal Dark | `#1A1F2E` | Background (Dark edition) |
| Warm White | `#F0EDE8` | All primary text (Dark edition) |
| Amber | `#E8A020` | Hex chrome indicators, yellow chromate swatch, caution/regulatory |
| Teal | `#2EC4B6` | Tri chrome indicators, clear chromate swatch, modern/compliant |
| Emerald | `#27AE60` | RoHS compliant badges, best practice, performance data |
| Coral | `#E05C5C` | Hex chrome warning, RoHS non-compliant badge, health hazard |
| Mid Slate | `#3A4055` | Table headers, cross-section outlines, dividers |
| Deep Navy | `#0D1020` | Footer band background |
| Dark Callout | `#1E2435` | Callout box fills, cross-section backgrounds |
| Alt Row | `#252B3D` | Alternating table rows |
| Bright Silver | `#C8D0D8` | Zinc layer representation, neutral elements |
| Olive Drab | `#6B702A` | Olive drab chromate swatch (approximate) |

### Step 5 — Set ruler guides

**Horizontal guides:**
- 0.5" — top safe zone
- 3.2" — Zone 1/Zone 2 boundary
- 10.0" — Zone 2/Zone 3 boundary
- 13.0" — Zone 3/Zone 4 boundary
- 22.0" — Zone 4/Zone 5 boundary
- 27.0" — Zone 5/Zone 6 boundary
- 32.5" — Zone 6/Zone 7 boundary
- 35.5" — bottom safe zone

---

## Part 3 — Layout Zones and Build Order

```
ZONE 1 — HEADER BAND (0"–3.2")
  Block A: Headline + subheading + regulatory hero callout

ZONE 2 — COATING CROSS-SECTIONS AND COLOR GUIDE (3.2"–10.0" / ~6.8" tall)
  Block B: Four coating cross-section diagrams (HERO)
  Block C: Color appearance guide strip with swatches

ZONE 3 — THE MECHANISM (10.0"–13.0" / ~3.0" tall)
  Block CC: How conversion coatings work — simplified chemistry explanation

ZONE 4 — HEX VS. TRI COMPARISON TABLE (13.0"–22.0" / ~9.0" tall)
  Block D: Comprehensive comparison table

ZONE 5 — SELF-HEALING AND THE PERFORMANCE GAP (22.0"–27.0" / ~5.0" tall)
  Block E: Self-healing explanation (left half)
  Block F: Regulatory timeline (right half)

ZONE 6 — APPLICATION BEST PRACTICES (27.0"–32.5" / ~5.5" tall)
  Block G: Process control callout (left half)
  Block H: Common failures and causes (right half)

ZONE 7 — FOOTER BAND (32.5"–36.0" / ~3.5" tall)
  Block J: Standard footer
```

---

## Part 4 — Zone-by-Zone Build Specifications

### ZONE 1 — Header Band

**Dimensions:** Full page width. Y: 0" to 3.2".

---

**BLOCK A — Headline**

- Font: Barlow Condensed ExtraBold, 78 pt, `#F0EDE8`
- Letter spacing: -4
- Text (all caps):

> CHROMATE AND CONVERSION COATINGS

**BLOCK A — Subheading**

- Font: Barlow SemiBold, 34 pt, `#E8A020` (Amber)
- Text:

> Hexavalent, Trivalent, and Beyond — The Final Line of Defense

**BLOCK A — Regulatory Hero Callout**

- Element type: Rounded rectangle
- Position: X: 0.5". Y: 2.2"
- Width: 23.0". Height: 0.8"
- Fill: `#E05C5C` at 12%
- Border: 2 pt, `#E05C5C`
- Corner radius: 6 pt
- Text (centered): Barlow Condensed ExtraBold, 24 pt, `#E05C5C`

> HEXAVALENT CHROMIUM IS A KNOWN CARCINOGEN — REGULATORY RESTRICTIONS ARE INCREASING WORLDWIDE

---

### ZONE 2 — Coating Cross-Sections and Color Guide (HERO)

**Dimensions:** Y: 3.2" to 10.0" (~6.8" tall).

---

**Section label:**
- Centered. Y: 3.4"
- Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text:

> THE COATING TYPES AT A GLANCE

---

**BLOCK B — Four Coating Cross-Section Diagrams**

Y: 4.0" to 8.5" (~4.5" tall). Four cards evenly spaced.

Each card: Width: 5.5". Height: 4.3". Fill: `#1E2435`. Corner radius: 6 pt. Border: 2 pt.

| Card | X | Border | Title | Type |
|---|---|---|---|---|
| 1 | 0.5" | `#E8A020` | HEX CLEAR / BLUE | Hexavalent clear |
| 2 | 6.25" | `#E8A020` | HEX YELLOW / IRIDESCENT | Hexavalent yellow |
| 3 | 12.0" | `#2EC4B6` | TRI CLEAR | Trivalent clear |
| 4 | 17.75" | `#2EC4B6` | TRI BLACK | Trivalent black |

**Inside each card:**

Title: Barlow Condensed ExtraBold, 20 pt, border color.

Cross-section diagram (centered, 4.0" wide x 1.5" tall):
Three horizontal layers stacked:
- Bottom layer: `#3A4055` (substrate steel) — Rectangle, 4.0" x 0.4". Label: `SUBSTRATE`
- Middle layer: `#C8D0D8` (zinc plate) — Rectangle, 4.0" x 0.4". Label: `ZINC`
- Top layer: Conversion coating — Rectangle, 4.0" x 0.15"-0.3" (varies by type). Label: coating type name.

Conversion coating layer fills and heights:

| Type | Fill | Height | Film Thickness |
|---|---|---|---|
| Hex clear | `#B8D8E8` at 50% (pale blue) | 0.15" | `0.05–0.25 micron` |
| Hex yellow | `#E8A020` at 60% (golden) | 0.25" | `0.25–0.75 micron` |
| Tri clear | `#D0E8E4` at 50% (pale teal) | 0.15" | `0.05–0.25 micron` |
| Tri black | `#2A2A2A` at 80% (near black) | 0.20" | `0.5–1.5 micron` |

Below cross-section — key data:
- Font: JetBrains Mono Regular, 12 pt, `#F0EDE8`

*Card 1 — Hex Clear:*
> Film: 0.05–0.25 micron
> SST: 8–24 hrs (clear)
> RoHS: NON-COMPLIANT

*Card 2 — Hex Yellow:*
> Film: 0.25–0.75 micron
> SST: 96–500+ hrs
> RoHS: NON-COMPLIANT

*Card 3 — Tri Clear:*
> Film: 0.05–0.25 micron
> SST: 24–96 hrs (no sealer) / 96–200+ hrs (with sealer)
> RoHS: COMPLIANT

*Card 4 — Tri Black:*
> Film: 0.5–1.5 micron
> SST: 96–400 hrs
> RoHS: COMPLIANT

RoHS status: `NON-COMPLIANT` in `#E05C5C`, `COMPLIANT` in `#27AE60`.

---

**BLOCK C — Color Appearance Guide Strip**

Y: 8.8" to 9.8" (~1.0" tall).

A horizontal strip with 6 color swatches representing common chromate appearances:

- Element type: Rounded rectangle (overall container)
- Width: 23.0". Height: 0.8". Fill: `#252B3D`. Corner radius: 4 pt.

Six swatches evenly spaced inside (each ~3.5" wide):

| Swatch | Fill Color (approximate) | Label |
|---|---|---|
| Clear (hex) | `#D0DFE8` | `Clear / Blue-bright` |
| Yellow (hex) | `#D4A830` | `Yellow / Iridescent` |
| Olive drab (hex) | `#6B702A` | `Olive Drab (mil-spec)` |
| Clear (tri) | `#C8E0D8` | `Tri Clear` |
| Black (tri) | `#282828` | `Tri Black` |
| Topcoat/sealer | `#A0B0C0` | `+ Sealer / Topcoat` |

Each swatch: Small rectangle (0.6" x 0.5") with the fill color, label to the right in Inter Regular, 12 pt, `#F0EDE8`.

---

### ZONE 3 — The Mechanism

**Dimensions:** Y: 10.0" to 13.0" (~3.0" tall).

---

**Section label:**
- Centered. Y: 10.2"
- Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`
- Text:

> HOW CONVERSION COATINGS WORK

---

**BLOCK CC — Mechanism Explanation**

Two side-by-side callout boxes:

**Left — Hexavalent Process:**
- X: 0.5". Width: 11.0". Height: 2.2". Fill: `#1E2435`. Left-border: `#E8A020`.
- Title: `HEXAVALENT MECHANISM` — Barlow SemiBold, 18 pt, `#E8A020`
- Body (Inter Regular, 15 pt, `#F0EDE8`):

> Zinc dissolves into the acidic chromate solution. Cr⁶⁺ is reduced to Cr³⁺ at the surface, forming a mixed Cr⁶⁺/Cr³⁺ oxide gel film. The residual Cr⁶⁺ in the film provides "self-healing" — if the film is scratched, soluble Cr⁶⁺ migrates to the damaged area and re-forms the barrier.

**Right — Trivalent Process:**
- X: 12.0". Width: 11.5". Height: 2.2". Fill: `#1E2435`. Left-border: `#2EC4B6`.
- Title: `TRIVALENT MECHANISM` — Barlow SemiBold, 18 pt, `#2EC4B6`
- Body:

> Similar acid dissolution of zinc surface. Cr³⁺ precipitates as a chromium (III) oxide/hydroxide film. No Cr⁶⁺ present at any stage — fully RoHS compliant. No self-healing mechanism. Performance enhanced by topcoat sealers (silicate, silane, or organic-based) that add a secondary barrier layer.

---

### ZONE 4 — Hex vs. Tri Comparison Table

**Dimensions:** Y: 13.0" to 22.0" (~9.0" tall).

---

**Section label:**
- Centered. Y: 13.2"
- Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text:

> HEAD-TO-HEAD — HEXAVALENT VS. TRIVALENT

---

**BLOCK D — Comparison Table**

Y: 13.8" to 21.8" (~8.0" tall).

Table with 2 main columns (Hexavalent, Trivalent) plus a Property label column:

Column widths: Property (5.0"), Hexavalent (9.0"), Trivalent (9.0"). Total: 23.0".

Header row: Fill `#3A4055`. Labels: `Property` | `HEXAVALENT (Cr⁶⁺)` | `TRIVALENT (Cr³⁺)`. Hex header subtly tinted `#E8A020` at 15%; Tri header tinted `#2EC4B6` at 15%.

| Property | Hexavalent | Trivalent |
|---|---|---|
| Active chemistry | Cr⁶⁺ (chromic acid based) | Cr³⁺ (chromium chloride or sulfate based) |
| RoHS status | Non-compliant for electrical/electronic equipment (EEE). Military, aerospace, and industrial sectors may have exemptions — verify applicable regulations. | Fully compliant with RoHS (EEE applications). |
| Self-healing | Yes — Cr⁶⁺ reservoir migrates to damage sites | No — film is inert once formed |
| Color options | Clear, yellow/iridescent, olive drab, black | Clear, light blue, black (yellow NOT achievable without hex) |
| Salt spray (clear on zinc) | 8-24 hours | Without sealer: 24-96 hrs. With sealer: 96-200+ hrs. |
| Salt spray (yellow/high-perf on zinc) | 96-500+ hours | N/A — no true yellow; black tri: 96-400 hrs |
| Film thickness | 0.05-0.75 micron (varies by type) | 0.05-1.5 micron (varies by type) |
| Topcoat/sealer | Optional (improves already-good base performance) | Often required to match hex yellow performance |
| Heat resistance | Degrades above 150°F (65°C) — Cr⁶⁺ converts to Cr³⁺ | More heat-stable — no Cr⁶⁺ to reduce |
| Torque tension | Well-characterized, predictable | Can vary — test with fastener coatings |
| Bath life | Long — very forgiving, self-replenishing Cr⁶⁺ | Shorter — more sensitive to metallic drag-in, pH drift |
| Process control | Moderate — wide operating window | Tighter — pH, temperature, immersion time all critical |
| Health hazard | Carcinogen (OSHA PEL: 5 microg/m³) | Low hazard — irritant, not carcinogen |

Data font: Inter Regular, 14 pt, `#F0EDE8`. Property labels: Inter Medium, 14 pt, `#F0EDE8`. Alternating rows: `#1E2435` / `#252B3D`. RoHS status row: "Non-compliant" in `#E05C5C`, "Fully compliant" in `#27AE60`.

---

### ZONE 5 — Self-Healing and the Performance Gap

**Dimensions:** Y: 22.0" to 27.0" (~5.0" tall).

---

**BLOCK E — Self-Healing Explanation** (left half, X: 0.5" to 11.5")

Y: 22.0" to 26.8"

Callout container: Width: 11.0". Height: 4.6". Fill: `#1E2435`. Corner radius: 6 pt. Left-border: `#E8A020`.

Title: `THE SELF-HEALING ADVANTAGE (AND WHY IT MATTERS LESS THAN IT USED TO)` — Barlow SemiBold, 16 pt, `#E8A020`

Body (Inter Regular, 15 pt, `#F0EDE8`, line height 145%):

> Hex chrome films contain a reservoir of soluble Cr⁶⁺. When the film is scratched or abraded, Cr⁶⁺ migrates to the damaged site and re-oxidizes to form new barrier. This is genuine self-healing — no other conversion coating does this.
>
> But modern trivalent systems with topcoat sealers have closed the gap significantly. The sealer provides a secondary physical barrier that compensates for the lack of chemical self-healing. Many automotive and electronics OEMs have successfully transitioned to tri + sealer with no field performance loss.

Key callout (JetBrains Mono Regular, 13 pt, `#E8A020`):

> Self-healing is real but not magic — it does not survive extreme abrasion or high-temperature baking

---

**BLOCK F — Regulatory Timeline** (right half, X: 12.0" to 23.5")

Y: 22.0" to 26.8"

Callout container: Width: 11.5". Height: 4.6". Fill: `#1E2435`. Corner radius: 6 pt. Left-border: `#E05C5C`.

Title: `REGULATORY TIMELINE` — Barlow SemiBold, 18 pt, `#E05C5C`

A vertical timeline with key dates:

Timeline backbone: Vertical line, 1 pt, `#3A4055`, centered in the box. Date markers as small circles (`#E05C5C`, 8 pt diameter) with text to the right.

| Date | Event |
|---|---|
| 2003 | EU RoHS Directive adopted — Cr⁶⁺ restricted in electronics |
| 2006 | RoHS enforcement begins — 1000 ppm max Cr⁶⁺ |
| 2007 | EU REACH regulation — Cr⁶⁺ on SVHC candidate list |
| 2013 | Cr⁶⁺ added to REACH Annex XIV (authorization required) |
| 2017 | REACH authorization sunset for many Cr⁶⁺ uses |
| 2024+ | Ongoing exemption reviews; automotive and aerospace still use hex under exemptions |

Date: JetBrains Mono Regular, 13 pt, `#E05C5C`.
Event text: Inter Regular, 13 pt, `#F0EDE8`.

Bottom callout: Inter Medium, 14 pt, `#27AE60`:

> The trend is clear: the window for hex chrome is closing. Build your tri capability now.

---

### ZONE 6 — Application Best Practices

**Dimensions:** Y: 27.0" to 32.5" (~5.5" tall).

---

**BLOCK G — Process Control** (left half, X: 0.5" to 11.5")

Y: 27.0" to 32.3"

Callout container: Width: 11.0". Height: 5.0". Fill: `#1E2435`. Corner radius: 6 pt. Left-border: `#27AE60`.

Title: `CRITICAL PROCESS CONTROLS` — Barlow SemiBold, 20 pt, `#27AE60`

Bullets (Inter Regular, 15 pt, `#F0EDE8`, line height 145%):

> - **pH** — Most critical for trivalent. Maintain within +/- 0.2 of target. Out-of-range pH = poor film formation or excessive coating.
> - **Temperature** — Hex: 60-80°F (wide). Tri: tighter — typically 70-85°F. Too hot = patchy film.
> - **Immersion time** — Hex: 15-60 sec (forgiving). Tri: 30-90 sec (timing matters more).
> - **Drag-in** — Rinse thoroughly before chromating. Nickel or iron drag-in poisons tri baths rapidly.
> - **Agitation** — Gentle rack or barrel agitation. Avoid air agitation in hex (Cr⁶⁺ mist hazard).
> - **Drying** — Do not force-dry above 150°F for hex films. Tri films more tolerant but check supplier spec.

---

**BLOCK H — Common Failures and Causes** (right half, X: 12.0" to 23.5")

Y: 27.0" to 32.3"

Callout container: Width: 11.5". Height: 5.0". Fill: `#1E2435`. Corner radius: 6 pt. Left-border: `#E05C5C`.

Title: `WHAT GOES WRONG` — Barlow SemiBold, 20 pt, `#E05C5C`

Table (6 rows):

| Failure | Cause | Fix |
|---|---|---|
| Patchy / uneven film | Poor rinsing before chromate; zinc surface passivated | Improve rinse; reduce transfer time from zinc to chromate |
| Film too thin (poor SST) | Low concentration, low immersion time, bath temperature too low | Analyze and replenish; extend dip time; check heater |
| Iridescent / rainbow (on clear) | Film too thick — over-immersion or over-concentration | Reduce dip time or dilute bath |
| Powdery / chalky film | Bath pH too high (alkaline); heavy zinc drag-in | Adjust pH; improve pre-chromate rinse |
| Color inconsistency | Temperature variation; uneven agitation; bath aging | Stabilize temp; check barrel rotation; schedule bath maintenance |
| White rust in SST too early | Inadequate film + no sealer; poor rinsing before drying | Optimize chromate parameters; add sealer topcoat |

Header: Barlow SemiBold, 13 pt, `#F0EDE8` on `#3A4055`. Data: Inter Regular, 13 pt, `#F0EDE8`. Failure column: Inter Medium, 13 pt, `#E05C5C`. Alternating rows.

---

### ZONE 7 — Footer Band

Standard footer per series convention.

**Disclaimer:**
> This poster is an educational reference tool. Chromate types, performance data, and regulatory information are typical industry values as of 2026. Conversion coating performance varies by zinc deposit type, bath chemistry, and application conditions. RoHS and REACH regulations are subject to revision — verify current exemption status with your regulatory compliance team. Consult your chemical supplier for application-specific guidance.

**Poster title:** Chromate and Conversion Coatings — Hex, Tri, and Beyond

**Version:** v1.0 — 2026

---

## Part 5 — Grouping and Naming Convention

| Group Name | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, regulatory hero callout |
| Zone 2 - Coating Types | Section label, four cross-section cards, color appearance strip |
| Zone 3 - Mechanism | Section label, hex and tri mechanism callouts |
| Zone 4 - Comparison Table | Section label, comprehensive hex vs. tri table |
| Zone 5 - Self-Healing and Regulation | Self-healing explanation, regulatory timeline |
| Zone 6 - Best Practices | Process control callout, common failures table |
| Zone 7 - Footer | Standard footer elements |

---

## Part 6 — Light Edition Color Remap Table

| Dark Hex | Light Hex | Notes |
|----------|-----------|-------|
| `#1A1F2E` | `#F5F4F0` | Background and all BG-colored elements |
| `#F0EDE8` | `#1A1F2E` | All primary text |
| `#1E2435` | `#ECEEF4` | Callout box fills, card backgrounds |
| `#252B3D` | `#E8E8F0` | Alternate row backgrounds, color guide strip |
| `#0D1020` | `#1A1F2E` | Footer strip background |
| `#E8A020` | `#C8860A` | Amber accent elements |
| `#2EC4B6` | `#1A8C82` | Teal accent elements |
| `#27AE60` | `#1E7A47` | Emerald accent elements |
| `#E05C5C` | `#B83E3E` | Coral accent elements |
| `#3A4055` | `#D0D4DE` | Table headers, dividers |
| `#C8D0D8` | `#C8D0D8` | Bright Silver — **unchanged** |
| `#6B702A` | `#6B702A` | Olive Drab swatch — **unchanged** (represents actual coating color) |

Color appearance swatches (Block C): Retain approximate real-world colors on both editions — these represent physical coating appearances, not design accents.

---

## Part 7 — Export Checklist

Standard six files (Dark/Light x 24x36/18x24/Digital).

File name prefix: `Chromate and Conversion Coatings`

The hex vs. tri comparison table (Zone 4) is the most space-intensive element — verify text remains legible at 18x24" resize.

---

## Design Notes

This poster is the most regulatory-sensitive in the series. The Watson flags on RoHS/REACH status are important — regulatory landscapes shift, and the poster's credibility depends on getting this right. The disclaimer is deliberately strong, and the regulatory timeline is dated to allow readers to assess currency.

The hex chrome carcinogen callout in the header is intentionally prominent. This poster does not shy away from the health reality — that honesty builds credibility. But it also does not demonize hex chrome; the comparison table is fair, acknowledging that hex yellow still outperforms tri in some applications. The poster's message is nuanced: "know what you're working with, understand the alternatives, and plan your transition."

The self-healing explanation (Zone 5) addresses the single strongest technical argument for hex chrome. By explaining both the mechanism AND its limitations, the poster equips readers to have informed conversations rather than falling back on "hex is better because self-healing."

---

*Alaina — Plating Posters Inc Creative Lead*
*Poster #26 — Chromate and Conversion Coatings — Construction Workup v1.0*
*2026-04-24*
