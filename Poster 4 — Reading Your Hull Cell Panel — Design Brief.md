---
Project: Plating Posters Inc
Poster Number: 4
Title: Reading Your Hull Cell Panel
Status: Design Brief — v1.0 (Approved)
Created: 2026-03-14T00:00:00
Updated: 2026-03-16T00:00:00
Author: Alaina (poster-designer)
Technical Source: Watson — [[Acid Zinc Plating Troubleshooting Guide]] Section 7
Editions: Dark + Light
Process Scope: Acid zinc KCl/NH4Cl only (one process per poster — standing series rule)
Illustration Method: Pure vector from scratch in Affinity Designer
ColorPalette: APPROVED 2026-03-16 — series-wide standard (see Section 4.2)
Typography: APPROVED 2026-03-16 — Option A locked as series-wide standard (see Section 4.3)
tags:
  - PosterDesign
  - HullCell
  - DesignBrief
  - AcidZinc
---

# Design Brief — Poster #4: Reading Your Hull Cell Panel

*Alaina — Plating Posters Inc Creative Lead*
*v1.0 — 2026-03-16 — Color palette and typography APPROVED and locked as series-wide standards.*
*Production layout plan added in Section 5. Watson verification flags consolidated in Section 6.*
*Status: Ready for production — pending Watson confirmations noted in Section 6.*

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| v0.1 | 2026-03-14 | Initial design brief draft |
| v0.2 | 2026-03-14 | Updated with Drew's confirmed decisions: dual editions, one process per poster, pure vector illustration |
| v1.0 | 2026-03-16 | Color palette approved (series standard). Typography Option A approved (series standard). Full production layout plan added (Section 5). Watson verification flags consolidated. |

---

## 1. Poster Purpose

The Hull cell panel is the plating lab's diagnostic instrument. Run one correctly and it tells you — in a visual language — what is wrong with your bath before bad parts make it to the customer. The problem is that panel interpretation is tribal knowledge: experienced techs carry it in their heads, and new techs have no reference except a binder that stays in the supervisor's drawer.

This poster puts that knowledge on the wall above the Hull cell station, in a format that is immediately readable and visually engaging enough to belong in a product line.

**What it must do:**
- Illustrate the current density gradient across a Hull cell panel (HCD → mid-current → LCD)
- Show what each zone looks like under known bath conditions, both good and problematic
- Map visual deposit appearances to their most likely cause and corrective action
- Establish proper Hull cell setup parameters (current, time, cathode prep)
- Be useful to a tech running their first Hull cell and to a chemist confirming a contamination diagnosis

**What it must not do:**
- Cover more than one plating process — scope is acid zinc KCl/NH4Cl only (standing series rule: one process per poster; a separate Nickel Edition would be its own product)
- Replace a vendor's process guide or SDS
- Look like a photocopied spec sheet

---

## 2. Target Audience

**Primary:** Lab technicians, process chemists, QC leads in zinc plating shops — people who run or read Hull cells regularly.

**Secondary:** Shop supervisors and plating managers who need to understand what their tech is telling them when they say "the panel looks burned at the HCD."

**Tertiary:** Trade show and product demonstration context — Drew presenting Plating Posters Inc, with this poster as a sample of the series. It needs to hold up in that setting.

---

## 3. Content Blocks

The following content is drafted and ready for layout. Items marked with a Watson flag are partially drafted and pending confirmation before they should be treated as final. All Watson flags are consolidated in Section 6.

---

### BLOCK A — Headline and Subheading

**Headline:**
Reading Your Hull Cell Panel

**Subheading:**
Diagnose your plating bath before it diagnoses your scrap rate.

**Series tag (footer area):**
Plating Posters Inc — Metal Finishing Reference Series

---

### BLOCK B — What Is a Hull Cell? (Brief Orientation Box)

*Small callout box — 3–5 lines maximum. Orients anyone unfamiliar without slowing down experienced readers.*

> The Hull cell is a 267 mL trapezoidal tank that simultaneously tests a range of current densities on a single cathode panel. The angled cathode panel creates a current density gradient — high at one end, low at the other — so one 5-minute test reveals how your bath performs across the entire operating range.

---

### BLOCK C — Setup Parameters Table

*Reference box, clean tabular format.*

| Parameter | Value |
|-----------|-------|
| Cell volume | 267 mL |
| Cathode material | Cold-rolled steel, cleaned and acid-activated |
| Anode material | SHG zinc (99.99% pure) |
| Test current — rack diagnostic | 2 A (most common) |
| Test current — barrel diagnostic | 1 A |
| Test duration | 5 minutes |
| Agitation | Air agitation — required |
| Temperature | Match actual bath temperature |

**Cathode prep note:**
Degrease with acetone or electrocleaner. Activate in 5–10% HCl for 15–30 seconds. Rinse. Use immediately. Do not touch with bare hands after activation.

*Watson flag — see Section 6, Flag C1: confirm SHG zinc anode specification and cathode prep sequence.*

---

### BLOCK D — The Hull Cell Panel Diagram

*The visual anchor of the poster — the largest single element, occupying the upper-center or full-width upper portion of the layout.*

**What to illustrate:**

A precise, clean technical illustration of a plated Hull cell panel — rectangular, with the following zones clearly labeled along the bottom edge (left-to-right = high-to-low current density convention):

- **HCD Zone** (left / narrow anode end): labeled "High Current Density"
  - Sub-label: ~10–50 A/dm² at 2 A total *(Watson flag C2 — see Section 6)*
- **Mid-Current Zone** (center): labeled "Mid-Current"
  - Sub-label: ~2–10 A/dm² at 2 A total *(Watson flag C2)*
- **LCD Zone** (right / wide end): labeled "Low Current Density"
  - Sub-label: ~0.1–1 A/dm² at 2 A total *(Watson flag C2)*

**Visual treatment of the panel surface:**
Show a "healthy bath" panel as the base reference state: mirror-bright finish transitioning from the HCD zone through mid-current; slight brightness softening at the LCD zone, but still covered and uniform. This is the "good panel" — everything else on the poster is a deviation from it.

Color representation: The zinc deposit surface is represented in silver-white tones (`#C8D0D8` Bright Silver base). Problem zones in the diagnostic table are called out via the approved accent palette.

Zone indicator bands run along the top edge of the panel illustration using `#E8A020` (Amber) at HCD, neutral silver through mid-current, and `#2EC4B6` (Teal) at LCD — subtle gradients, not solid blocks.

---

### BLOCK E — Diagnostic Interpretation Table

*The core reference content. Derived from Watson's Section 7.4 with additional notes from Section 3 (brightener/carrier) and Section 4 (metallic contamination).*

**Table title:** What Your Panel Is Telling You

| Panel Appearance | Most Likely Cause | First Corrective Action |
|------------------|-------------------|------------------------|
| Mirror bright HCD through mid; slight softening at LCD | Good bath | No action needed — archive this panel as your reference |
| Overall semi-bright or matte; burn zone enlarged at HCD | Brightener deficiency | Add brightener in 0.1–0.5 mL/L increments; re-run panel |
| Mirror bright HCD/mid; LCD progressively dull → skip plate | Brightener overload | Carbon treat (5–10 g/L); reconstitute additive system from baseline |
| Pitting across full panel; HCD burning prominent | Carrier (wetting agent) deficiency | Add carrier incrementally; check temperature vs. cloud point first |
| Overall hazy; reduced deposit brightness; foaming in tank | Carrier overload | Check bath temperature; carbon treat if needed |
| Yellow to dark band at HCD; haze across panel; LCD coverage loss | Iron contamination (>50–75 ppm) | H₂O₂ treatment (1–2 mL/L of 30%); raise pH to 5.0–5.5; filter |
| Skip plate in LCD; HCD appears normal; no response to brightener adjustment | Lead or cadmium contamination | Zinc dust treatment; dummy plate; eliminate contamination source |
| Dark or black deposit visible after passivation | Copper contamination (>10 ppm) | Low-CD dummy plate (0.1–0.3 A/dm²); zinc dust treatment |
| LCD dullness; streaking; variable pitting across panel | Organic contamination | Carbon treat; H₂O₂ pre-treatment if severe; reconstitute |
| HCD burning advancing toward mid-current; LCD coverage poor | Low zinc metal concentration | Analyze zinc; add zinc metal source; check anode area |
| Rough, nodular deposit; visible particles in bath | Suspended solids — pH too high or filtration failure | Check pH; inspect filter; clean anode bags |

*Watson flag — see Section 6, Flag C3: confirm contamination thresholds (Fe, Cu, Pb, Cd) and H₂O₂ treatment ratios for acid zinc.*

**Design note:** This table is typeset for readability at 4–6 feet. Alternating row shading. Cause column in `#E8A020` (Amber) header accent. The "good bath" row gets an `#27AE60` (Emerald) left-border accent and a subtle green tint row background. Problem rows flagging contamination get an `#E05C5C` (Coral) left-border accent. See Section 4.6 for full table styling spec.

**Scope note (standing series rule):** This table covers acid zinc KCl/NH4Cl baths only.

---

### BLOCK F — The Isolation Test Protocol

*Procedural callout box — distinct visual treatment, slightly smaller than the main diagnostic table.*

**Callout title:** When the Diagnosis Isn't Clear: The Isolation Protocol

When one corrective action doesn't solve the problem, test one variable at a time using separate aliquots of bath solution:

1. Add a brightener increment to a fresh aliquot — run panel. If HCD/mid-current improves: brightener was low.
2. Add a carrier increment to a fresh aliquot — run panel. If pitting clears: carrier was low.
3. Add boric acid to a fresh aliquot — run panel. If HCD burning reduces: boric acid was low.
4. Adjust pH in a fresh aliquot with HCl or zinc carbonate — run panel. Confirm whether pH was the driver.

**The rule:** Change one variable. Run one panel. Decide. Then move to the next variable.

---

### BLOCK G — Hull Cell as an SPC Tool

*Small callout block — positioned near the footer. Elevates the poster from "how-to" to "professional practice."*

**Callout title:** Make Your Hull Cell a Control Chart

- Run weekly at minimum — or every 500–1000 ampere-hours of production throughput
- Archive every panel with: date, bath analysis results, ampere-hour reading, and all additions made
- Laminate a known-good reference panel and mount it next to this poster
- Visual trends across archived panels reveal bath drift before symptoms appear on production parts

---

### BLOCK H — Footer Content

- Poster title: **Reading Your Hull Cell Panel**
- Series: Plating Posters Inc — Metal Finishing Reference Series
- Disclaimer: *This poster is a diagnostic reference tool. Always consult your process supplier's documentation and applicable safety data sheets. Not a substitute for laboratory analysis.*
- Version and date: v1.0 — 2026
- [Logo placeholder: Plating Posters Inc]

---

## 4. Design Specifications — Affinity Designer

### 4.1 Artboard Dimensions

**Primary format:** 24×36" (609.6 × 914.4 mm)
- Affinity Designer artboard: 7200 × 10800 px at 300 DPI
- Bleed: 0.125" (3.175 mm) all sides
- Safe zone for text/graphics: 0.5" (12.7 mm) inside trim edge

**Secondary format:** 18×24" (457.2 × 609.6 mm)
- Affinity Designer artboard: 5400 × 7200 px at 300 DPI
- Same bleed and safe zone conventions

**Digital export:** PDF (print-quality, CMYK) + PNG (RGB, 150 DPI for screen display)

---

### 4.2 Color Palette — APPROVED 2026-03-16 (Series Standard)

*Approved by Drew 2026-03-16. This palette is now locked as the series-wide standard for all Plating Posters Inc titles.*

#### Dark Edition (Flagship)

| Role | Color Name | Hex | Use |
|------|------------|-----|-----|
| Background | Gunmetal Dark | `#1A1F2E` | Full artboard background; also used as primary text color in Light edition |
| Primary text | Warm White | `#F0EDE8` | All body text, table content, callout text |
| Panel illustration base | Bright Silver | `#C8D0D8` | Hull cell panel surface; zinc deposit representation |
| HCD zone accent | Amber | `#E8A020` | HCD zone band; table section headers; "cause" column accent |
| LCD zone accent | Teal | `#2EC4B6` | LCD zone band; callout box borders and titles |
| Good bath indicator | Emerald | `#27AE60` | "Good bath" table row left-border; positive reference signals |
| Problem indicator | Coral | `#E05C5C` | Contamination problem row left-borders; critical alerts |
| Table rules / dividers | Mid Slate | `#3A4055` | Table row rules, section dividers, subtle structural lines |
| Footer strip | Deep Navy | `#0D1020` | Footer band background |
| Callout box backgrounds | Dark Callout | `#1E2435` | Interior fill of all callout boxes |
| Alternate table rows | Alt Row | `#252B3D` | Even table rows (base rows use `#1A1F2E`) |

**Accessibility:** `#F0EDE8` on `#1A1F2E` = ~13:1 contrast ratio — exceeds WCAG AAA (7:1).

#### Light Edition (Accessible Print)

| Role | Color Name | Hex | Notes |
|------|------------|-----|-------|
| Background | Off-White | `#F5F4F0` | |
| Primary text | Charcoal | `#1A1F2E` | Same hex as Dark BG — intentional inversion |
| Panel illustration base | Bright Silver | `#C8D0D8` | Unchanged — panel is always metallic |
| HCD zone accent | Amber Dark | `#C8860A` | Darkened for contrast on light background |
| LCD zone accent | Teal Dark | `#1A8C82` | Darkened for contrast on light background |
| Good bath indicator | Forest Green | `#1E7A47` | Darkened for contrast |
| Problem indicator | Deep Coral | `#B83E3E` | Darkened for contrast |
| Table rules / dividers | Light Slate | `#D0D4DE` | |
| Footer strip | Charcoal | `#1A1F2E` | |
| Callout box backgrounds | Light Callout | `#ECEEF4` | |
| Alternate table rows | Alt Row Light | `#E8E8F0` | |

**Accessibility:** `#1A1F2E` on `#F5F4F0` = ~15:1 contrast ratio — exceeds WCAG AAA.

**Workflow note:** Design Dark edition as master. Produce Light edition as a duplicate artboard (or duplicate file) using Affinity Designer Global Colors to remap palette values. Do not manually recolor individual elements — the layer naming convention exists precisely so Global Colors can target them cleanly.

**Color mode note:** Work in RGB in Affinity Designer. Export to CMYK only at PDF export time. Verify Amber (`#E8A020`) and Teal (`#2EC4B6`) translate cleanly through CMYK conversion — both are moderately saturated and should convert without significant shift, but proof at print time.

---

### 4.3 Typography — APPROVED 2026-03-16 (Series Standard, Option A)

*Approved by Drew 2026-03-16. Option A is now locked as the series-wide typography standard for all Plating Posters Inc titles.*

| Role | Font | Weight | Notes |
|------|------|--------|-------|
| Poster headlines | Barlow Condensed | ExtraBold | Strong, industrial character; excellent distance readability. Free on Google Fonts. |
| Subheadings / section labels | Barlow | SemiBold | Coherent with headline family. Free on Google Fonts. |
| Body text / diagnostic table | Inter | Regular / Medium | Highly legible at small sizes; excellent for data-dense content. Free on Google Fonts. |
| Data tables / parameters | JetBrains Mono | Regular | Monospace for tabular data reads as precise and technical. Free on Google Fonts / JetBrains. |

**Type scale — 24×36" artboard at 300 DPI:**

| Element | Size | Font | Weight |
|---------|------|------|--------|
| Poster headline | 96–120 pt | Barlow Condensed | ExtraBold |
| Poster subheading | 42–48 pt | Barlow | SemiBold |
| Section subheading | 36–42 pt | Barlow | SemiBold |
| Table header row | 22–24 pt | Barlow / Inter | SemiBold |
| Table body text | 18–20 pt | Inter | Regular |
| Callout box title | 24–28 pt | Barlow | SemiBold |
| Callout box body | 18–20 pt | Inter | Regular |
| Parameter table data | 18–20 pt | JetBrains Mono | Regular |
| Footer series name | 16–18 pt | Barlow | SemiBold |
| Footer disclaimer | 11–12 pt | Inter | Regular / Light |
| Zone sub-labels (diagram) | 16–18 pt | JetBrains Mono | Regular |

**Readability check:** At 20 pt body text on a 24×36" poster at 300 DPI, individual characters are approximately 7mm tall at print. Comfortably legible at 4 feet. The headline and section labels are the primary 3–8 foot read-from-wall elements.

**Scale to 18×24":** Reduce all type sizes proportionally by ~75%. Body text floor: 14 pt minimum.

---

### 4.4 Layout Structure

**Layout type:** Structured editorial — top anchor diagram, lower reference content. Portrait orientation.

**Grid:** 12-column grid, 0.25" gutters, 0.5" margins.

**Vertical proportions — 24×36" artboard:**

```
┌────────────────────────────────────────────────────┐
│  HEADER BAND — 8% of height (~2.9")                │
│  Poster title (Barlow Condensed ExtraBold 96-120pt)│
│  Subheading (Barlow SemiBold 42-48pt)              │
│  Hull Cell orientation box (Block B) — top right   │
├────────────────────────────────────────────────────┤
│  HULL CELL PANEL DIAGRAM — 30% of height (~10.8")  │
│  Full-width illustration; zone bands top edge      │
│  Zone labels + sub-labels at bottom of diagram     │
│  Callout arrows point downward into diagnostic tbl │
├───────────────────────┬────────────────────────────┤
│  DIAGNOSTIC TABLE     │  SETUP PARAMETERS TABLE    │
│  (Block E)            │  (Block C)                 │
│  58% width / cols 1-7 │  38% width / cols 8-12     │
│  37% of height        │  (top-aligned in column)   │
│                       │                            │
│                       │  [space below for Block G] │
│                       │  SPC TOOL CALLOUT (Block G)│
│                       │  (bottom of right column)  │
├───────────────────────┴────────────────────────────┤
│  ISOLATION PROTOCOL CALLOUT (Block F)              │
│  Full width — 12% of height (~4.3")                │
├────────────────────────────────────────────────────┤
│  FOOTER BAND — 6% of height (~2.2")                │
│  Deep Navy strip: series name | disclaimer | logo  │
└────────────────────────────────────────────────────┘
```

**Layout rationale:** The panel diagram anchors the top third — it's the visual magnet that pulls the eye in from across the room. The diagnostic table is the functional workhorse and earns the most real estate. The right column keeps the setup parameters close to the diagram (you look up from the table to the diagram, then right to check parameters). The isolation protocol and SPC callout stay below the fold — important, but secondary to the immediate diagnostic workflow.

---

### 4.5 Affinity Designer Layer Structure

Name layers in this order (bottom to top):

| Layer Name | Contents | Color |
|------------|----------|-------|
| `[BG] Background` | Solid fill rectangle — `#1A1F2E` (Dark) / `#F5F4F0` (Light) covering full artboard + bleed | — |
| `[BG] Footer Strip` | Deep Navy `#0D1020` footer band | — |
| `[BG] Header Band` | Optional subtle tonal differentiation or same as BG | — |
| `[STRUCT] Grid Guides` | Margin, column, and bleed guides (non-printing) | Blue |
| `[STRUCT] Section Rules` | Horizontal rule lines between major sections — `#3A4055` | — |
| `[ILLUS] Hull Cell Panel` | Main panel illustration group — all sub-elements nested inside | Orange |
| `[ILLUS] Zone Bands` | HCD Amber / mid Silver / LCD Teal gradient bands on panel top edge | — |
| `[ILLUS] Zone Labels` | HCD / Mid-Current / LCD zone text labels + sub-labels | — |
| `[ILLUS] Callout Arrows` | Arrows from diagram zones to diagnostic table rows | — |
| `[DATA] Setup Table` | Block C parameters table (JetBrains Mono body) | Green |
| `[DATA] Diagnostic Table` | Block E — What Your Panel Is Telling You | Green |
| `[CALLOUT] What Is a Hull Cell` | Block B orientation box (Teal border, `#1E2435` background) | Teal |
| `[CALLOUT] Isolation Protocol` | Block F callout box | Teal |
| `[CALLOUT] SPC Tool` | Block G callout box | Teal |
| `[TYPE] Headline` | Poster headline (Barlow Condensed ExtraBold) and subheading (Barlow SemiBold) | Red |
| `[TYPE] Section Labels` | All section header text | Red |
| `[TYPE] Body Text` | All body/table text elements not already in data layers | Red |
| `[FOOTER] Footer Content` | Series name, disclaimer, version, logo placeholder | — |
| `[MARKS] Print Marks` | Bleed marks, crop marks — Export Persona only; keep locked during design | Gray |

**Affinity Designer workflow notes:**
- Use Global Colors for the full series palette so that the Light edition can be produced by remapping color swatches rather than touching individual elements
- Use Symbols for repeated elements (callout arrow style, callout box frame) so updates propagate automatically
- Set document color profile to sRGB for design work; convert to CMYK only at export
- Keep `[ILLUS] Hull Cell Panel` as a closed Group — the vector illustration can then be swapped or updated independently without disturbing the surrounding layout
- Configure Export Persona slices before beginning layout: six named slices per the Section 6 file naming convention

---

### 4.6 Visual Element Specifications

**Hull Cell Panel Illustration (pure vector — Affinity Designer from scratch):**
- Style: precise technical illustration — not photorealistic, not cartoonish. The visual language of a high-quality engineering diagram. Flat perspective with subtle dimensional depth suggesting the physical panel.
- The panel: rectangular, slightly wider than tall (Hull cell proportions). Surface base color `#C8D0D8`. Current density gradient visible as a subtle tonal shift left (brighter, more active) to right (more uniform, slightly softer).
- Zone bands: along the top edge only — Amber `#E8A020` at HCD (left), a neutral fade through mid, Teal `#2EC4B6` at LCD (right). Use gradient mesh or overlapping transparent shapes to fade zone transitions — not hard-edged color blocks.
- Panel edge: a 2–3 pt stroke in `#9AA0B0` to define the panel boundary against the dark background.
- Light edition: same vector art; Global Colors remap the zone bands to their darkened equivalents (`#C8860A`, `#1A8C82`). The `#C8D0D8` panel base is unchanged.
- Creation: build in a dedicated Affinity Designer sub-document or as a Symbol, then place into the poster artboard. This allows the illustration to be reused across future Hull cell content.

**Diagnostic Table styling:**
- Row background alternation: `#1A1F2E` (base) / `#252B3D` (alternate)
- "Good bath" row: left border 4 pt in `#27AE60` (Emerald); row background tinted very subtly (apply `#27AE60` at 8% opacity over the row fill)
- Contamination problem rows (iron, lead/cadmium, copper, organic): left border 4 pt in `#E05C5C` (Coral)
- Chemistry-drift rows (brightener, carrier, zinc metal, solids): left border 4 pt in `#E8A020` (Amber)
- Column headers: `#E8A020` (Amber) text on `#3A4055` (Mid Slate) background
- Column width proportions: Panel Appearance 40% / Most Likely Cause 30% / First Corrective Action 30%
- Cell padding: 8 pt top/bottom, 10 pt left/right minimum

**Callout boxes (Blocks B, F, G):**
- Container: rounded rectangle, 8 pt corner radius, 1.5 pt stroke in `#2EC4B6` (Teal Dark edition) / `#1A8C82` (Teal Dark — Light edition)
- Background fill: `#1E2435` (Dark) / `#ECEEF4` (Light)
- Title text: `#2EC4B6` (Teal) in Barlow SemiBold 24–28 pt
- Body text: `#F0EDE8` (Warm White) in Inter Regular 18–20 pt
- Internal padding: 20 pt all sides

**Icons (supporting only — do not substitute for text):**
- Style: single-weight line icons, 1.5 pt stroke, `#F0EDE8` (Warm White — Dark edition)
- Used for: cathode panel indicator, rectifier/power supply, air agitation bubbles, thermometer
- Recommended source: Phosphor Icons (open license, consistent stroke weight) or Material Design Icons (Google, open license)
- Size: 24–32 pt equivalent; always paired with a text label

---

## 5. Production Layout Plan

This section maps every content block to its specific position, palette treatment, and typography application. Use this as the build checklist when opening Affinity Designer.

---

### Zone 1 — Header Band (top 8%)

**What goes here:** Block A (Headline + Subheading) + Block B (Orientation Box, top-right corner)

**Build steps:**
1. Place a rectangle spanning the full artboard width at the header height. Fill: same as background (`#1A1F2E`) — no visible band differentiation unless a very subtle horizontal rule at the bottom of the header feels right during final polish.
2. Typeset headline "Reading Your Hull Cell Panel" in Barlow Condensed ExtraBold, 96–120 pt, `#F0EDE8`. Left-aligned within the safe zone. Tracking: tight (−10 to −20 — Barlow Condensed is built for this).
3. Typeset subheading "Diagnose your plating bath before it diagnoses your scrap rate." in Barlow SemiBold, 42–48 pt, `#E8A020` (Amber). Left-aligned; 6–8 pt below headline baseline.
4. Block B orientation box: build in `[CALLOUT] What Is a Hull Cell` layer. Right-aligned in the header band, vertically centered. Width: ~cols 9–12. Height: fits 3–5 lines at 18–20 pt Inter Regular. Teal border (`#2EC4B6`), dark callout background (`#1E2435`), title "What Is a Hull Cell?" in Teal Barlow SemiBold 24 pt.

**Watson dependency:** None — Block A and B content is finalized.

---

### Zone 2 — Hull Cell Panel Diagram (rows 9–38% of height)

**What goes here:** Block D (Panel Diagram) — full artboard width illustration

**Build steps:**
1. In `[ILLUS] Hull Cell Panel` group: draw the panel rectangle at the target dimensions. A 16:6 width-to-height ratio is a reasonable starting approximation — refine to match actual Hull cell panel geometry.
2. Apply base fill gradient on panel surface: `#C8D0D8` (Bright Silver) lightening slightly toward the left HCD edge (where the deposit would appear more active), gentle tonal shift rightward.
3. In `[ILLUS] Zone Bands` layer: draw three overlapping color band shapes along the top edge of the panel (not the full panel height — keep to roughly 10–15% of the panel height). Use transparent gradient fades at the transitions. Colors: `#E8A020` at left, neutral/transparent in center, `#2EC4B6` at right.
4. In `[ILLUS] Zone Labels` layer: place three label groups below the panel diagram:
   - Left: "HIGH CURRENT DENSITY" (Barlow Condensed ExtraBold, `#E8A020`, 28 pt) with sub-label "~10–50 A/dm² at 2 A" (JetBrains Mono Regular, `#F0EDE8`, 16 pt) — *these values pending Watson Flag C2*
   - Center: "MID-CURRENT" (Barlow Condensed ExtraBold, `#F0EDE8`, 28 pt) with sub-label "~2–10 A/dm² at 2 A" (JetBrains Mono, 16 pt)
   - Right: "LOW CURRENT DENSITY" (Barlow Condensed ExtraBold, `#2EC4B6`, 28 pt) with sub-label "~0.1–1 A/dm² at 2 A" (JetBrains Mono, 16 pt)
5. In `[ILLUS] Callout Arrows` layer: draw three clean leader lines from the HCD, mid-current, and LCD zones of the panel downward toward the diagnostic table. Use rounded arrowheads; line weight 1.5 pt; `#3A4055` (Mid Slate) color so they guide without dominating.

**Watson dependency:** Zone sub-labels (step 4) — Flag C2. Draft these values in the illustration but treat as placeholder until Watson confirms.

---

### Zone 3A — Diagnostic Table, left column (rows 38–75%, cols 1–7)

**What goes here:** Block E (Diagnostic Interpretation Table)

**Build steps:**
1. In `[DATA] Diagnostic Table` layer: build an 11-row table (1 header + 10 data rows) spanning cols 1–7.
2. Table header row: fill `#3A4055` (Mid Slate). Column header text: Barlow SemiBold 22–24 pt, `#E8A020` (Amber). Column labels: "Panel Appearance" / "Most Likely Cause" / "First Corrective Action".
3. Data row backgrounds: alternate `#1A1F2E` (odd) / `#252B3D` (even).
4. "Good bath" row (Row 1): apply `#27AE60` at 8% fill over the row background; add a 4 pt left-border rectangle in `#27AE60`.
5. Contamination rows (iron, Pb/Cd, copper, organic — Rows 6–9): add 4 pt left-border in `#E05C5C` (Coral).
6. Chemistry-drift rows (brightener low, brightener high, carrier low, carrier high, zinc low, solids — Rows 2, 3, 4, 5, 10, 11): add 4 pt left-border in `#E8A020` (Amber).
7. Body text: Inter Regular 18–20 pt, `#F0EDE8` (Warm White). Cell padding: 8 pt vertical, 10 pt horizontal.
8. Section title "WHAT YOUR PANEL IS TELLING YOU" in Barlow SemiBold 28 pt, `#E8A020`, above the table.

**Watson dependency:** Rows 6 (iron threshold), 7 (Pb/Cd), 8 (copper) — Flag C3. Draft from current content; update when Watson confirms.

---

### Zone 3B — Right column (rows 38–75%, cols 8–12)

**What goes here:** Block C (Setup Parameters, top of column) + Block G (SPC Tool callout, bottom of column)

**Block C — Setup Parameters:**
1. In `[DATA] Setup Table` layer: build a 2-column table (Parameter / Value), 8 data rows + 1 header.
2. Header: `#3A4055` background, `#E8A020` text "SETUP PARAMETERS" in Barlow SemiBold 22 pt.
3. Body: JetBrains Mono Regular 18 pt, `#F0EDE8`. Parameter column at 50% width; Value column at 50%.
4. Row alternation: same `#1A1F2E` / `#252B3D` pattern as the diagnostic table — visual consistency.
5. Cathode prep note block: placed directly below the table, Inter Regular 16 pt, `#F0EDE8`, with a top rule line in `#3A4055`.

**Block G — SPC Tool callout:**
1. In `[CALLOUT] SPC Tool` layer: build a rounded rectangle callout box (`#1E2435` fill, `#2EC4B6` border 1.5 pt, 8 pt corners) in the lower portion of the right column — bottom-aligned within Zone 3B.
2. Title "MAKE YOUR HULL CELL A CONTROL CHART" in Barlow SemiBold 20 pt, `#2EC4B6`.
3. Body: Inter Regular 16–18 pt, `#F0EDE8`. Four bullet points from Block G content.

**Watson dependency:** None in this zone.

---

### Zone 4 — Isolation Protocol Callout (rows 75–87%)

**What goes here:** Block F (Isolation Test Protocol) — full width

**Build steps:**
1. In `[CALLOUT] Isolation Protocol` layer: build a full-width rounded rectangle callout box (`#1E2435` fill, `#2EC4B6` border 1.5 pt, 8 pt corners).
2. Title "WHEN THE DIAGNOSIS ISN'T CLEAR: THE ISOLATION PROTOCOL" in Barlow SemiBold 24–28 pt, `#2EC4B6`.
3. Body: numbered list (1–4) in Inter Regular 18 pt, `#F0EDE8`. The four isolation steps from Block F.
4. Closing rule line at the bottom: "THE RULE: Change one variable. Run one panel. Decide. Then move to the next variable." — typeset in Inter Medium 18 pt, `#E8A020` (Amber), with a 2 pt left accent rule in Amber.

**Watson dependency:** None — this block is procedural guidance, not chemistry-specific thresholds.

---

### Zone 5 — Footer Band (bottom 6–7%)

**What goes here:** Block H (Footer Content)

**Build steps:**
1. `[BG] Footer Strip` layer: rectangle spanning full artboard width, `#0D1020` (Deep Navy) fill.
2. Left section: "Reading Your Hull Cell Panel" in Barlow SemiBold 16 pt, `#F0EDE8`.
3. Center: "Plating Posters Inc — Metal Finishing Reference Series" in Inter Regular 14 pt, `#F0EDE8` at 70% opacity.
4. Far right: logo placeholder rectangle, 40×40 px equivalent, `#3A4055` fill with centered text "LOGO" in JetBrains Mono 12 pt.
5. Above footer band, spanning full width: the disclaimer text in Inter Regular 11–12 pt, `#F0EDE8` at 50% opacity. "This poster is a diagnostic reference tool. Always consult your process supplier's documentation and applicable safety data sheets. Not a substitute for laboratory analysis." — center-aligned.
6. Version "v1.0 — 2026" in JetBrains Mono 11 pt, `#F0EDE8` at 50% opacity, bottom-right corner within footer.

**Watson dependency:** None.

---

### Light Edition Conversion Checklist

After the Dark edition master is complete:

1. Duplicate the artboard in Affinity Designer (or File > Save As new file — either method works; artboard duplication within the same file makes side-by-side comparison easier).
2. In the new artboard, open the Global Colors panel (Swatches panel > Global Colors section). Remap each swatch:
   - `#1A1F2E` Background → `#F5F4F0`
   - `#F0EDE8` Warm White → `#1A1F2E`
   - `#1E2435` Dark Callout BG → `#ECEEF4`
   - `#252B3D` Alt Row → `#E8E8F0`
   - `#0D1020` Deep Navy → `#1A1F2E`
   - `#E8A020` Amber → `#C8860A`
   - `#2EC4B6` Teal → `#1A8C82`
   - `#27AE60` Emerald → `#1E7A47`
   - `#E05C5C` Coral → `#B83E3E`
   - `#3A4055` Mid Slate → `#D0D4DE`
   - (Do not remap `#C8D0D8` Bright Silver — the panel illustration stays metallic in both editions)
3. Spot-check: verify all text passes WCAG AA at minimum after remapping; verify the panel illustration's metallic tones still read correctly against the light background.
4. Export Light edition using the same Export Persona slice configuration.

---

## 6. Watson Verification Flags

The following items in this brief are drafted from Watson's Acid Zinc Plating Troubleshooting Guide (v1) and general industry knowledge. They are flagged for Watson's confirmation before the poster is treated as finalized. Content should be built into the layout using these values as placeholders — do not delay production pending Watson's response, but do not release a final PDF until all three flags are cleared.

---

**Flag C1 — Anode specification and cathode prep**

> Watson: Confirm that SHG zinc (99.99% purity) is the correct and standard anode specification for Hull cell testing in an acid zinc KCl/NH4Cl bath. Also confirm the cathode prep sequence: (1) degrease with acetone or electrocleaner; (2) activate in 5–10% HCl for 15–30 seconds; (3) rinse; (4) use immediately, no bare-hand contact after activation. Flag any deviations from standard practice or any acid concentration / time ranges that differ by source.

*Location in poster: Block C (Setup Parameters Table), anode row and cathode prep note.*

---

**Flag C2 — Current density values at HCD and LCD extremes**

> Watson: Confirm the current density values at the HCD and LCD extremes of a standard 267 mL Hull cell operated at 2 A total current, using the Wagner current density scale. The draft values are: HCD ~10–50 A/dm², mid-current ~2–10 A/dm², LCD ~0.1–1 A/dm² at 2 A. Confirm these are accurate for the standard commercial cell geometry. Flag if values vary meaningfully by manufacturer or by the specific Wagner formula variant used. Also confirm the mid-current zone label values.

*Location in poster: Block D (Hull Cell Panel Diagram), zone sub-labels. Also affects Block C if a "current density range" row should be added to the Setup Parameters table.*

---

**Flag C3 — Contamination thresholds and treatment ratios in acid zinc**

> Watson: Confirm the following contamination threshold values and treatment specifications for acid zinc KCl/NH4Cl baths as they appear in Block E:
> - Iron contamination: threshold cited as >50–75 ppm. Confirm. Also confirm: H₂O₂ treatment at 1–2 mL/L of 30% H₂O₂, followed by pH raise to 5.0–5.5 and filtration.
> - Lead / cadmium contamination: confirm that "skip plate in LCD, HCD normal, no response to brightener" is the characteristic symptom signature. Confirm zinc dust treatment as the primary corrective action and note any minimum dummy plate current density or duration.
> - Copper contamination: confirm threshold of >10 ppm and that dark/black deposit after passivation is the characteristic symptom. Confirm low-CD dummy plate at 0.1–0.3 A/dm².
> - Organic contamination: confirm that LCD dullness, streaking, and variable pitting is the characteristic symptom. Confirm carbon treat + H₂O₂ pre-treatment as the standard corrective sequence.
> Flag any values that differ from industry consensus or that Watson has specific published source support for.

*Location in poster: Block E (Diagnostic Interpretation Table), rows 6–9.*

---

## 7. Dual Edition Export Files

Configure these six slices in Affinity Designer's Export Persona before beginning layout:

| Slice Name | Color Mode | Resolution | Bleed/Marks | Size |
|------------|-----------|------------|-------------|------|
| `Hull Cell Panel — Dark — 24x36 — Print` | CMYK | 300 DPI | Yes | 24×36" |
| `Hull Cell Panel — Dark — 18x24 — Print` | CMYK | 300 DPI | Yes | 18×24" |
| `Hull Cell Panel — Dark — Digital` | RGB | 150 DPI screen | No | 24×36" |
| `Hull Cell Panel — Light — 24x36 — Print` | CMYK | 300 DPI | Yes | 24×36" |
| `Hull Cell Panel — Light — 18x24 — Print` | CMYK | 300 DPI | Yes | 18×24" |
| `Hull Cell Panel — Light — Digital` | RGB | 150 DPI screen | No | 24×36" |

Six export files per poster is the series standard. Configure all six as named slices before beginning layout — ten minutes of setup eliminates export friction on every future poster.

---

## 8. Status and Next Steps

- [x] Confirm first poster selection — Hull Cell Panel #4
- [x] Confirm dual editions (Dark + Light) — standing series rule
- [x] Confirm process scope — one process per poster, standing series rule
- [x] Confirm illustration approach — pure vector from scratch in Affinity Designer
- [x] Color palette approved — `#1A1F2E` / `#F0EDE8` / `#E8A020` / `#2EC4B6` / `#27AE60` / `#E05C5C` palette locked as series standard 2026-03-16
- [x] Typography approved — Barlow Condensed ExtraBold / Barlow SemiBold / Inter Regular / JetBrains Mono locked as series standard 2026-03-16
- [x] Production layout plan complete (Section 5)
- [ ] Watson Flag C1 cleared — anode spec and cathode prep confirmation #sand
- [ ] Watson Flag C2 cleared — current density values at HCD/LCD extremes #sand
- [ ] Watson Flag C3 cleared — contamination thresholds and treatment ratios #sand
- [ ] Configure six Export Persona slices in Affinity Designer before beginning layout #sand
- [ ] Drew opens Affinity Designer — builds Dark edition artboard using this brief #gravel
- [ ] Light edition produced as duplicate artboard with Global Color remap #sand
- [ ] All six export files generated and named per Section 7 convention #sand

---

*Alaina — Plating Posters Inc Creative Lead*
*Design Brief v1.0 — 2026-03-16*
*Color palette and typography locked as series-wide standards. Production layout plan complete.*
*Technical content sourced from [[Acid Zinc Plating Troubleshooting Guide]] (Watson, v1, 2026-03-14), Section 7.*
*Three Watson verification flags remain open — see Section 6 before finalizing poster for release.*
