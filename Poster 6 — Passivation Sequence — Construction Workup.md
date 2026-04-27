---
Project: Plating Posters Inc
Poster Number: 6
Title: "The Passivation Sequence: From Plated Part to Protected Part"
Document Type: Construction Workup
Status: v1.0 — Ready for Elara
Created: 2026-04-04T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Poster 6 — Passivation Sequence — Content and Layout Draft.md (v1.0)"
Technical Source: Watson — Passivation Sequence Research Brief v1 (2026-04-03)
Watson Flags: THREE — salt spray ranges, drying temp limits, hex self-healing (all Drew, non-blocking)
Process Scope: Passivation (chromate conversion) on zinc-plated parts
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow: Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Passivation
  - ChromateConversion
  - ConstructionWorkup
---

# Poster # Poster #6 — Construction Workup
## The Passivation Sequence: From Plated Part to Protected Part

*Alaina — Plating Posters Inc Creative Lead*
*v1.0 — 2026-04-04*

This document is the construction workup for Poster #6. Three Watson flags remain open but are non-blocking.

> **Workflow update (2026-04-14):** Poster generation now uses claude.ai chat (SVG/HTML visual artifacts) These specs feed the Claude Chat Generation Prompt. If Drew approves the generated output, it proceeds to final production.

**Source of truth for content:** `Poster 6 — Passivation Sequence — Content and Layout Draft.md` — all copy is reproduced here verbatim. If any discrepancy exists, the Content and Layout Draft governs.

---

## Part 1 — Workflow Orientation

### Design Capabilities for This Poster

- Text boxes with precise font, size, weight, color, and spacing control
- Solid-color rectangles and rounded rectangles for color panels, table rows, callout boxes, process flow boxes, and compliance badges
- Line elements with arrowheads for the process flow connectors
- Gradient-style color fills for passivation color bars (approximate with solid colors — see note below)
- Export at print-quality PDF (300 DPI equivalent)

### Limitations to Flag for Elara

1. **Passivation color bars on the spectrum panels:** The Content Draft specifies gradient fills for the top color bars on each panel (e.g., light blue to lighter blue). The tool supports gradients on shapes, but subtle gradients can be difficult to control precisely. **Recommendation:** Use flat solid fills at the midpoint color for each bar. The color impression is the goal, not photographic accuracy. Flat fills are cleaner at print scale.

2. **Process flow strip (Zone 2):** 7 boxes connected by arrows. Straightforward in the design — use rounded rectangles and line elements with arrowheads. The `PASSIVATE` box gets a distinct Amber border to highlight it as the focus step.

3. **Color spectrum panels (8 total — 4 trivalent, 4 hexavalent):** Each panel is a rounded rectangle with a colored top bar and text content. Build each as a sub-group. The top color bars represent actual passivation appearance colors — these are NOT series palette colors and must be entered as the specific hex values provided below.

4. **Top color bars exempt from Light edition remap.** The color bars on the spectrum panels represent real-world passivation colors. In the Light edition, these bars keep their original colors while all structural elements remap per the standard table.

5. **4 pt left-border accents and callout boxes:** Standard technique from previous posters.

6. **Global Colors / swatch remap for Light edition:** Manual recolor per Part 6.

7. **JetBrains Mono:** Ensure font is available. Substitute Courier Prime if unavailable.

8. **Print size — 24x36".** 18x24" by duplicate and resize.

9. **Sub/superscript:** Copy-paste Unicode (Cr³⁺, Cr⁶⁺, Fe³⁺, Zn²⁺, Cu²⁺, CrO₃, etc.).

---

## Part 2 — Document Setup Instructions (for Elara's prompt)

### Step 1 — Create the document
- Width: **24 inches**. Height: **36 inches**.

### Step 2 — Set the background color
- **`#1A1F2E`** (Gunmetal Dark)

### Step 3 — Upload fonts (the Pro tier required)
- **Barlow Condensed ExtraBold** — headlines, zone labels
- **Barlow SemiBold** — subheadings, callout titles
- **Inter Regular** and **Inter Medium** — body text, table data
- **JetBrains Mono Regular** — salt spray values, parameter data

### Step 4 — Set up color palette

| Color Name | Hex | Primary Use |
|---|---|---|
| Gunmetal Dark | `#1A1F2E` | Background |
| Warm White | `#F0EDE8` | Primary text |
| Amber | `#E8A020` | Subheading, passivate box highlight, Drew's notes |
| Teal | `#2EC4B6` | Callout borders, rinse labels |
| Emerald | `#27AE60` | Trivalent row labels, RoHS badge |
| Coral | `#E05C5C` | Hexavalent row labels, restricted badge |
| Mid Slate | `#3A4055` | Table headers, flow arrows, box borders |
| Deep Navy | `#0D1020` | Footer band |
| Dark Callout | `#1E2435` | Callout fills, panel fills, flow strip BG |
| Alt Row | `#252B3D` | Flow boxes, alternating rows |

**Additional passivation color hex values (NOT series palette — appearance colors only):**
| Color | Hex | Use |
|-------|-----|-----|
| Clear/Blue (tri) | `#B0D0E8` | Top bar — trivalent clear/blue panel |
| Yellow (tri) | `#D4A830` | Top bar — trivalent yellow panel |
| Black (tri/hex) | `#1A1A1A` | Top bar — black panels |
| Thick Film (tri) | `#4A5568` | Top bar — thick film panel |
| Clear/Blue (hex) | `#A8C8E0` | Top bar — hex clear/blue panel |
| Yellow (hex) | `#C89820` | Top bar — hex yellow panel |
| Olive Drab | `#5A6644` | Top bar — hex OD panel |

### Step 5 — Set ruler guides

**Vertical guides:**
- 0.5" — left safe zone
- 23.5" — right safe zone

**Horizontal guides:**
- 0.5" — top safe zone
- 2.9" — Zone 1/Zone 2 boundary
- 6.5" — Zone 2/Zone 3 boundary
- 18.0" — Zone 3/Zone 4 boundary
- 23.8" — Zone 4/Zone 5 boundary
- 30.6" — Zone 5/Zone 6 boundary
- 32.4" — Zone 6/Zone 7 boundary
- 35.5" — bottom safe zone

---

## Part 3 — Layout Zones and Build Order

```
ZONE 1 — HEADER BAND (0"–2.9")
  Block A: Headline + subheading + tagline (left ~55%)
  Block B: "Why Passivate?" callout (right ~45%)

ZONE 2 — POST-PLATING FLOW (2.9"–6.5" / ~3.6" tall)
  Block C: 7-step horizontal process flow strip

ZONE 3 — COLOR SPECTRUM (HERO) (6.5"–18.0" / ~11.5" tall)
  Block D: Two rows of 4 color panels — Trivalent top, Hexavalent bottom

ZONE 4 — OPERATING PARAMETERS (18.0"–23.8" / ~5.8" tall)
  Block E: Trivalent params (left) | Hexavalent params (right)

ZONE 5 — CONTAMINATION + CARE (23.8"–30.6" / ~6.8" tall)
  Block F: Contamination thresholds table (left 55%)
  Block G: Post-passivation care callouts (right 45%)

ZONE 6 — SELF-HEALING + COMPLIANCE (30.6"–32.4" / ~1.8" tall)
  Block H: Self-healing note (left) + RoHS badges (right)

ZONE 7 — FOOTER BAND (32.4"–36.0" / ~3.6" tall)
  Block I: Disclaimer + poster title + series name + logo + version
```

---

## Part 4 — Zone-by-Zone Build Specifications

### ZONE 1 — Header Band

**Dimensions:** Full width. Y: 0" to 2.9".

---

**BLOCK A — Headline**
- Position: X: 0.5". Y: 0.5". Width: 12.5"
- Font: Barlow Condensed ExtraBold, 88 pt. Color: `#F0EDE8`. Letter spacing: -4
- Text:

> THE PASSIVATION SEQUENCE

**BLOCK A — Subheading**
- Position: X: 0.5". Y: 1.5"
- Font: Barlow SemiBold, 36 pt. Color: `#E8A020`
- Text:

> From Plated Part to Protected Part

**BLOCK A — Tagline**
- Position: X: 0.5". Y: 2.1"
- Font: Barlow SemiBold, 22 pt. Color: `#F0EDE8` at 65%
- Text:

> The step that determines whether your parts pass salt spray.

---

**BLOCK B — "Why Passivate?" Callout**

*Container:*
- Position: X: 13.25". Y: 0.5". Width: 10.25". Height: 2.2"
- Fill: `#1E2435`. Border: 1.5 pt, `#2EC4B6`. Corner radius: 8 pt

*Title:*
- X: 13.55". Y: 0.7". Barlow SemiBold, 18 pt. Color: `#2EC4B6`
- Text:

> WHY PASSIVATE?

*Body:*
- X: 13.55". Y: 1.05". Width: 9.65"
- Inter Regular, 16 pt. Color: `#F0EDE8`. Line height: 140%
- Text:

> Bare zinc corrodes to white rust within hours. The passivation step forms a chromium-zinc barrier film that extends corrosion life by 10x to 100x — turning hours of protection into hundreds.

*Key fact:*
- X: 13.55". Y: 2.0". Inter Medium, 16 pt. Color: `#2EC4B6`
- Text:

> This is a chemical conversion — not plating. No current required.

---

### ZONE 2 — Post-Plating Process Flow

**Dimensions:** Full width. Y: 2.9" to 6.5" (3.6" tall).

---

**BLOCK C — Process Flow Strip**

**Background band:**
- Rectangle. X: 0". Y: 2.9". Width: 24.0". Height: 3.6". Fill: `#1E2435`

**7 process boxes + 6 connecting arrows:**

Box dimensions: each 2.6" wide x 1.3" tall. Corner radius: 4 pt.
Box fill: `#252B3D`. Box border: 1 pt, `#3A4055`.
Arrows: line elements, 2 pt, `#3A4055`, with arrowheads, spanning the 0.3" gap between boxes.

**Box positions (Y: 4.0" for all, centered vertically in the strip):**
- Box 1: X: 0.6"
- Box 2: X: 3.5"
- Box 3: X: 6.4"
- Box 4: X: 9.3"
- Box 5: X: 12.2" — **special border: 2 pt, `#E8A020` (Amber)**
- Box 6: X: 15.1"
- Box 7: X: 18.0"

**Box labels (centered in each box, Barlow SemiBold, 14 pt, `#F0EDE8`):**
1. `ZINC PLATE`
2. `RINSE`
3. `BRIGHT DIP`
4. `RINSE`
5. `PASSIVATE`
6. `RINSE`
7. `DRY`

**Sub-labels for specific boxes (below box name, Inter Regular, 11 pt):**
- Box 3 sub: `(optional)` — color: `#E8A020`
- Box 6 sub: `(gentle)` — color: `#2EC4B6`

**Strip footnote:**
- Position: X: 0.5". Y: 5.6"
- Inter Regular, 13 pt. Color: `#F0EDE8` at 60%
- Text:

> Optional sealant/topcoat step omitted for clarity — see operating parameters.

---

### ZONE 3 — Color Spectrum (HERO)

**Dimensions:** Full width. Y: 6.5" to 18.0" (11.5" tall).

---

**BLOCK D — Color Spectrum Panels**

**Section label:**
- Position: X: centered. Y: 6.7"
- Barlow Condensed ExtraBold, 28 pt. Color: `#F0EDE8`. Alignment: Center
- Text:

> THE COLOR SPECTRUM — PROTECTION BY PASSIVATION TYPE

---

**ROW 1 — TRIVALENT (Y: 7.3" to 12.3" — 5.0" tall)**

**Row label:**
- Position: X: 0.5". Y: 7.3"
- Barlow SemiBold, 20 pt. Color: `#27AE60`
- Text:

> TRIVALENT (Cr³⁺) — RoHS COMPLIANT

**Panel dimensions:** Each 5.5" wide x 4.2" tall, separated by 0.2" gutters.
- Panel 1: X: 0.5". Y: 7.8"
- Panel 2: X: 6.2". Y: 7.8"
- Panel 3: X: 11.9". Y: 7.8"
- Panel 4: X: 17.6". Y: 7.8"

**Panel template (repeat for all 4):**

*Panel body:*
- Rounded rectangle. Width: 5.5". Height: 4.2"
- Fill: `#1E2435`. Corner radius: 6 pt

*Top color bar:*
- Rectangle. Flush with panel top. Width: 5.5". Height: 0.6"
- Fill: passivation color hex (see below)
- Corner radius: top-left and top-right match panel (6 pt)

*Title:*
- Centered in panel, Y: panel top + 0.8"
- Barlow Condensed ExtraBold, 18 pt. Color: `#F0EDE8`

*Film label:*
- Centered. Y: panel top + 1.2"
- Inter Regular, 14 pt. Color: `#F0EDE8` at 70%

*White rust hours:*
- Centered. Y: panel top + 1.7"
- JetBrains Mono, 16 pt. Color: `#E8A020`
- Format: `White rust: XX-XX hrs`

*Red rust hours:*
- Centered. Y: panel top + 2.1"
- JetBrains Mono, 16 pt. Color: `#E05C5C`
- Format: `Red rust: XX-XX hrs`

*Note:*
- Centered. Y: panel top + 2.7". Width: 5.0"
- Inter Regular, 12 pt. Color: `#F0EDE8` at 70%. Alignment: Center

---

**Trivalent panel data:**

| Panel | Top Bar Color | Title | Film | White Rust | Red Rust | Note |
|-------|--------------|-------|------|------------|----------|------|
| 1 | `#B0D0E8` | CLEAR / BLUE | Thinnest | 24-72 hrs | 72-200 hrs | Most common; cosmetically bright |
| 2 | `#D4A830` | YELLOW (IRIDESCENT) | Medium | 72-120 hrs | 200-400 hrs | Proprietary formulations; mimics hex yellow |
| 3 | `#1A1A1A` | BLACK | Medium-heavy | 72-120 hrs | 200-400 hrs | A Brite: BriteGuard NZP P1 / NZP P2 |
| 4 | `#4A5568` | THICK FILM / HIGH-PERF | Heaviest | 120-200 hrs | 400-720+ hrs | Latest generation — approaching hex yellow |

---

**ROW 2 — HEXAVALENT (Y: 12.6" to 17.6" — 5.0" tall)**

**Row label:**
- Position: X: 0.5". Y: 12.6"
- Barlow SemiBold, 20 pt. Color: `#E05C5C`
- Text:

> HEXAVALENT (Cr⁶⁺) — RESTRICTED (RoHS/REACH/ELV)

**Panel positions (same widths and gutters as Row 1):**
- Panel 1: X: 0.5". Y: 13.1"
- Panel 2: X: 6.2". Y: 13.1"
- Panel 3: X: 11.9". Y: 13.1"
- Panel 4: X: 17.6". Y: 13.1"

**Hexavalent panel data:**

| Panel | Top Bar Color | Title | White Rust | Red Rust | Note |
|-------|--------------|-------|------------|----------|------|
| 1 | `#A8C8E0` | CLEAR / BLUE | 12-24 hrs | 72-150 hrs | (none) |
| 2 | `#C89820` | YELLOW / IRIDESCENT | 96-200 hrs | 200-500 hrs | The industry workhorse for decades |
| 3 | `#1A1A1A` | BLACK | 72-120 hrs | 200-400 hrs | (none) |
| 4 | `#5A6644` | OLIVE DRAB (OD) | 200-500 hrs | 500-1000+ hrs | Military/defense; MIL-DTL-5541; heaviest hex film |

---

### ZONE 4 — Operating Parameters

**Dimensions:** Full width. Y: 18.0" to 23.8" (5.8" tall).

---

**BLOCK E — Two-Column Parameter Tables**

**Left column — Trivalent:** X: 0.5". Width: 11.2".
**Right column — Hexavalent:** X: 12.3". Width: 11.2".

---

**Left — Trivalent:**

*Title:*
- X: 0.5". Y: 18.2". Barlow SemiBold, 20 pt. Color: `#27AE60`
- Text:

> TRIVALENT OPERATING PARAMETERS

*Table header:*
- Rectangle. X: 0.5". Y: 18.7". Width: 11.2". Height: 0.45". Fill: `#3A4055`
- Col 1: `Parameter` — Barlow SemiBold, 16 pt. X: 0.7"
- Col 2: `Range` — Barlow SemiBold, 16 pt. X: 4.5"

*Data rows (6 rows, 0.55" each, alternating):*

| Row | Y | Fill | Parameter | Range |
|-----|---|------|-----------|-------|
| 1 | 19.15" | `#1A1F2E` | Chemistry | Cr³⁺ sulfate or chloride based |
| 2 | 19.70" | `#252B3D` | pH | 1.5-2.5 (up to 3.0 for thicker films) |
| 3 | 20.25" | `#1A1F2E` | Temperature | 70-140 deg F (21-60 deg C) |
| 4 | 20.80" | `#252B3D` | Immersion | 30-90 sec (clear); 60-180 sec (thick) |
| 5 | 21.35" | `#1A1F2E` | Agitation | Gentle — avoid turbulence |
| 6 | 21.90" | `#252B3D` | Max dry temp | < 150 deg F (65 deg C) |

Parameter: Inter Medium, 16 pt, `#F0EDE8`. Range: Inter Regular, 15 pt, `#F0EDE8`.

*Drew's note:*
- X: 0.5". Y: 22.6"
- Inter Regular, 13 pt. Color: `#E8A020`
- Text:

> Raising pH to 2.5 allows thicker film build — part stays longer without zinc degradation.

---

**Right — Hexavalent:**

*Title:*
- X: 12.3". Y: 18.2". Barlow SemiBold, 20 pt. Color: `#E05C5C`
- Text:

> HEXAVALENT OPERATING PARAMETERS

*Table header:*
- Rectangle. X: 12.3". Y: 18.7". Width: 11.2". Height: 0.45". Fill: `#3A4055`

*Data rows (6 rows, same structure):*

| Row | Y | Fill | Parameter | Range |
|-----|---|------|-----------|-------|
| 1 | 19.15" | `#1A1F2E` | Chemistry | CrO₃-based (dichromate, chromic acid) |
| 2 | 19.70" | `#252B3D` | pH | 1.0-2.0 (clear); 0.5-1.5 (yellow) |
| 3 | 20.25" | `#1A1F2E` | Temperature | 70-100 deg F (21-38 deg C) |
| 4 | 20.80" | `#252B3D` | Immersion | 5-30 sec (clear); 15-60 sec (yellow); 30-120 sec (OD) |
| 5 | 21.35" | `#1A1F2E` | Agitation | Gentle rack movement |
| 6 | 21.90" | `#252B3D` | Max dry temp | < 300 deg F (150 deg C) |

---

### ZONE 5 — Contamination + Care

**Dimensions:** Full width. Y: 23.8" to 30.6" (6.8" tall).

---

**BLOCK F — Contamination Thresholds (left 55%)**

**Position:** X: 0.5". Y: 23.8". Width: 12.5".

*Section label:*
- X: 0.5". Y: 24.0". Barlow Condensed ExtraBold, 22 pt. Color: `#F0EDE8`
- Text:

> WHAT KILLS THE PASSIVATION BATH

*Table header:*
- Rectangle. X: 0.5". Y: 24.5". Width: 12.5". Height: 0.45". Fill: `#3A4055`
- Col headers: `Contaminant` (X: 0.7"), `Source` (X: 3.0"), `Threshold` (X: 6.2"), `Effect` (X: 8.5")
- Barlow SemiBold, 16 pt. Color: `#F0EDE8`

*Data rows (5 rows, 0.6" each, alternating):*

| Row | Y | Fill | Contaminant | Source | Threshold | Effect |
|-----|---|------|-------------|--------|-----------|--------|
| 1 | 24.95" | `#1A1F2E` | Iron (Fe³⁺) | Steel racks, parts | >100-150 ppm | Yellow/brown discoloration |
| 2 | 25.55" | `#252B3D` | Zinc (Zn²⁺) | Drag-in from plating | High levels | Film discoloration |
| 3 | 26.15" | `#1A1F2E` | Copper (Cu²⁺) | Drag-in, rack corrosion | >30 ppm | Darkens film |
| 4 | 26.75" | `#252B3D` | Organics | Brightener drag-in | Variable | Spotty passivation |
| 5 | 27.35" | `#1A1F2E` | Chloride | Acid zinc KCl drag-in | Variable | Accelerates zinc attack |

Contaminant: Inter Medium, 16 pt, `#F0EDE8`. Other cols: Inter Regular, 15 pt, `#F0EDE8`.

*Prevention callout:*
- X: 0.5". Y: 28.1". Width: 12.5"
- Inter Medium, 15 pt. Color: `#E8A020`
- Text:

> Drag-in is the #1 source of passivation bath contamination. Rinse thoroughly between plating and passivation.

---

**BLOCK G — Post-Passivation Care (right 45%)**

**Position:** X: 13.5". Y: 23.8". Width: 10.0".

---

**Rinse Warning callout:**

*Container:*
- Rounded rectangle. X: 13.5". Y: 24.2". Width: 10.0". Height: 2.4"
- Fill: `#1E2435`. Border: 1.5 pt, `#2EC4B6`. Corner radius: 6 pt

*Title:*
- X: 13.8". Y: 24.4". Barlow SemiBold, 16 pt. Color: `#2EC4B6`
- Text:

> RINSE AFTER PASSIVATION

*Body:*
- X: 13.8". Y: 24.8". Width: 9.4"
- Inter Regular, 14 pt. Color: `#F0EDE8`. Line height: 140%
- Text:

> Use cold to warm water — NOT hot. Minimal agitation. Brief immersion. Aggressive rinsing or hot water damages the freshly formed film.

---

**Drying Warning callout:**

*Container:*
- Rounded rectangle. X: 13.5". Y: 26.9". Width: 10.0". Height: 2.6"
- Fill: `#1E2435`. Border: 1.5 pt, `#E8A020`. Corner radius: 6 pt

*Title:*
- X: 13.8". Y: 27.1". Barlow SemiBold, 16 pt. Color: `#E8A020`
- Text:

> DRYING TEMPERATURE

*Body:*
- X: 13.8". Y: 27.5". Width: 9.4"
- Inter Regular, 14 pt. Color: `#F0EDE8`. Line height: 140%
- Text:

> Trivalent: below 150 deg F (65 deg C). Hexavalent: below 300 deg F (150 deg C). Excessive heat destroys corrosion resistance.

---

### ZONE 6 — Self-Healing + Compliance

**Dimensions:** Full width. Y: 30.6" to 32.4" (1.8" tall).

---

**BLOCK H — Self-Healing Note (left ~60%)**

- Position: X: 0.5". Y: 30.8". Width: 13.5"
- Inter Regular, 14 pt. Color: `#F0EDE8`. Line height: 140%
- Text (bold the opening phrase via separate text box or bold formatting):

> Self-healing (hexavalent only): Hex passivation films contain soluble Cr⁶⁺ that migrates to scratches and re-passivates exposed zinc. Trivalent films do not self-heal — once damaged, the barrier is compromised.

*"Self-healing (hexavalent only):"* — use Inter Medium for this opening phrase, then Inter Regular for the rest. Or use a single text box with the tool's inline bold.

---

**BLOCK H — Compliance Badges (right ~40%)**

**Badge 1 — Trivalent (Emerald):**
- Rounded rectangle. X: 14.5". Y: 30.7". Width: 4.2". Height: 0.65"
- Fill: `#1E2435`. Border: 2 pt, `#27AE60`. Corner radius: 4 pt
- Text (centered): `TRIVALENT — RoHS/REACH COMPLIANT`
- Inter Medium, 12 pt. Color: `#27AE60`

**Badge 2 — Hexavalent (Coral):**
- Rounded rectangle. X: 19.0". Y: 30.7". Width: 4.5". Height: 0.65"
- Fill: `#1E2435`. Border: 2 pt, `#E05C5C`. Corner radius: 4 pt
- Text (centered): `HEXAVALENT — RESTRICTED SUBSTANCE`
- Inter Medium, 12 pt. Color: `#E05C5C`

---

### ZONE 7 — Footer Band

**Dimensions:** Full width. Y: 32.4" to 36.0" (3.6" tall).

**Footer band background:**
- Rectangle. X: 0". Y: 32.4". Width: 24.0". Height: 3.6". Fill: `#0D1020`

**Disclaimer:**
- X: 0.5". Y: 32.8". Width: 23.0"
- Inter Regular, 11 pt. Color: `#F0EDE8` at 50%. Alignment: Center
- Text:

> This poster presents general passivation guidelines. Salt spray performance varies by vendor formulation, zinc thickness, and sealant use. Consult your process supplier for product-specific data. This poster does not replace your SDS.

**Poster title:**
- X: 0.5". Y: 33.5". Barlow SemiBold, 16 pt. Color: `#F0EDE8`
- Text: `The Passivation Sequence: From Plated Part to Protected Part`

**Series name:**
- X: 0.5". Y: 34.0". Inter Regular, 13 pt. Color: `#F0EDE8` at 60%
- Text: `Plating Posters Inc — Metal Finishing Reference Series`

**Version:**
- X: 0.5". Y: 34.4". Inter Regular, 11 pt. Color: `#F0EDE8` at 40%
- Text: `v1.0 — 2026`

**Logo placeholder:**
- X: 21.0". Y: 33.5". Width: 2.5". Height: 1.5"
- Barlow SemiBold, 14 pt. Color: `#F0EDE8` at 30%. Alignment: Center. Text: `[LOGO]`

---

## Part 5 — Grouping and Layer Order

| Group Name | Contains | Lock? |
|-----------|----------|-------|
| Zone 1 — Header | Blocks A + B | Yes |
| Zone 2 — Flow Strip | Block C (background + 7 boxes + 6 arrows + footnote) | Yes |
| Zone 3 — Color Spectrum | Block D — 8 panel sub-groups + row labels | Yes |
| Zone 4 — Parameters | Block E (two column tables) | Yes |
| Zone 5 — Contamination | Blocks F + G | Yes |
| Zone 6 — Compliance | Block H (note + 2 badges) | Yes |
| Zone 7 — Footer | Block I | Yes |

**Sub-grouping for Zone 3:** Group each of the 8 panels as individual sub-groups (panel body + color bar + all text). Then group each row (4 panels + row label). Then group both rows as the full zone.

---

## Part 6 — Light Edition Remap Table

| Element / Role | Dark Edition | Light Edition |
|---|---|---|
| Page background | `#1A1F2E` | `#F0EDE8` |
| Primary text | `#F0EDE8` | `#1A1F2E` |
| Amber accent | `#E8A020` | `#B87A10` |
| Teal accent | `#2EC4B6` | `#1E9A8F` |
| Emerald accent | `#27AE60` | `#1D8A4A` |
| Coral accent | `#E05C5C` | `#C43C3C` |
| Mid Slate fills | `#3A4055` | `#D0D4DC` |
| Deep Navy footer | `#0D1020` | `#E2E0DB` |
| Dark Callout fills | `#1E2435` | `#E8E5E0` |
| Alt Row fills | `#252B3D` | `#F5F3EF` |

**CRITICAL OVERRIDE — Passivation color bars:**
The top color bars on all 8 spectrum panels (`#B0D0E8`, `#D4A830`, `#1A1A1A`, `#4A5568`, `#A8C8E0`, `#C89820`, `#5A6644`) are NOT remapped. These represent actual passivation appearance colors and must remain unchanged in the Light edition. Only the panel bodies, text, borders, and structural elements remap.

**Note on black panel bars:** The `#1A1A1A` bars will appear very dark on the light background — this is intentional and correct (black passivation IS black).

---

## Part 7 — Export Checklist

| Export | Size | Edition | Format | Filename |
|--------|------|---------|--------|----------|
| 1 | 24x36" | Dark | PDF Print | `Poster-06-Passivation-Sequence-24x36-Dark.pdf` |
| 2 | 24x36" | Light | PDF Print | `Poster-06-Passivation-Sequence-24x36-Light.pdf` |
| 3 | 18x24" | Dark | PDF Print | `Poster-06-Passivation-Sequence-18x24-Dark.pdf` |
| 4 | 18x24" | Light | PDF Print | `Poster-06-Passivation-Sequence-18x24-Light.pdf` |
| 5 | 24x36" | Dark | PNG | `Poster-06-Passivation-Sequence-24x36-Dark.png` |
| 6 | 24x36" | Light | PNG | `Poster-06-Passivation-Sequence-24x36-Light.png` |

---

*Alaina — Plating Posters Inc Creative Lead*
*Poster #6 — The Passivation Sequence — Construction Workup v1.0*
*2026-04-04*
