---
Project: Plating Posters Inc
Poster Number: 22
Title: "Corrosion Testing at a Glance — Salt Spray, CASS, Humidity, and Beyond"
Document Type: Construction Workup
Status: v1.0 — Ready for Elara
Created: 2026-04-11T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Watson — New Poster Concepts from CEF — 2026-04-06.md (Concept 20)"
Technical Source: Watson research brief (ASTM B117, B368, B287, B380, D2247, B605 test methods; salt spray cabinet operation; solution compositions; panel angle requirements)
Watson Flags: TWO OPEN — (1) Verify Corrodkote (ASTM B380) slurry composition details (salts and kaolin clay proportions) against current ASTM revision. (2) Confirm SO2 test (ASTM B605) is still an active standard and not withdrawn. Both non-blocking; values presented as reference-grade with ASTM numbers for user verification.
Tyler Flags: NONE
Process Scope: Accelerated corrosion test methods for evaluating plated coatings (universal — applies to every plated finish)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow: Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - CorrosionTesting
  - SaltSpray
  - CASS
  - QualityControl
  - ConstructionWorkup
---

# Poster # Poster #22 — Construction Workup
## Corrosion Testing at a Glance — Salt Spray, CASS, Humidity, and Beyond

*Alaina — Plating Posters Inc Creative Lead*
*v1.0 — 2026-04-11*

This document is the construction workup for Poster #22. It translates Watson's research concept into a full design specification usable by Elara to engineer a generation prompt for Drew. Two Watson flags remain open — both non-blocking.

> **Workflow update (2026-04-14):** Poster generation now uses claude.ai chat (SVG/HTML visual artifacts) These specs feed the Claude Chat Generation Prompt. If Drew approves the generated output, it proceeds to final production.

**Content source:** Watson — New Poster Concepts from CEF — 2026-04-06.md (Concept 20 — Corrosion Testing at a Glance).

---

## Part 1 — Workflow Orientation

### Design Capabilities for This Poster

- Text boxes with precise font, size, weight, color, and spacing control
- Solid-color rectangles and rounded rectangles for the six-method comparison table, callout boxes, and accent borders
- Simple shapes for the salt spray cabinet cross-section (rectangles, angled lines, circles for collection cups)
- Color fills set to exact hex values
- Background page color set to exact hex
- Icon library search for laboratory, test tube, shield, corrosion icons
- Export at print-quality PDF (300 DPI equivalent via print export)

### Limitations to Flag for Elara

1. **Salt spray cabinet cross-section (Block B — HERO):** Built from rectangles (cabinet body, door), angled lines (panel rack at 15-30 degrees), small circles (collection cups), and a dashed area representing fog distribution. This is a simplified schematic, not a photorealistic illustration. Straightforward in the design but requires careful element positioning.

2. **Six-method comparison table (Block D):** Six columns, 6-7 rows. This is a wide table. At 24" poster width with 0.5" margins on each side, each column gets approximately 3.67" — tight but workable with 14 pt body text. Font size may need to drop to 13 pt in table cells. Elara should test readability.

3. **4 pt left-border accents on callout boxes:** Same technique as all previous posters.

4. **Global Colors / swatch remap for Light edition:** Manual recolor per remap table.

5. **JetBrains Mono font:** Ensure font is available. Fallback: Courier Prime.

6. **Print size — 24x36":** Set to exactly 24 inches wide by 36 inches tall at document creation.

7. **Sub/superscript characters:** Unicode characters provided for CuCl₂, NaCl, SO₂ notation.

---

## Part 2 — Document Setup Instructions (for Elara's prompt)

### Step 1 — Create the document
- Open the design tool. Create a new custom-size design.
- Width: **24 inches**. Height: **36 inches**.

### Step 2 — Set the background color
- Set the page background color to: **`#1A1F2E`** (Gunmetal Dark)

### Step 3 — Upload fonts (the Pro tier required)
Upload from Google Fonts / JetBrains.org (if not already uploaded from previous posters):
- **Barlow Condensed ExtraBold** — all headlines and section labels
- **Barlow SemiBold** — all subheadings, callout titles
- **Inter Regular** and **Inter Medium** — all body text and table data
- **JetBrains Mono Regular** — all parameter data, ASTM numbers, and version number

If JetBrains Mono upload fails, substitute **Courier Prime**.

### Step 4 — Set up color palette (save as Brand Colors )

| Color Name | Hex | Primary Use |
|---|---|---|
| Gunmetal Dark | `#1A1F2E` | Background (Dark edition) |
| Warm White | `#F0EDE8` | All primary text (Dark edition) |
| Amber | `#E8A020` | ASTM standard numbers, key data callouts, warning elements |
| Teal | `#2EC4B6` | Test solution details, pH values, cabinet diagram accents |
| Emerald | `#27AE60` | Best practice callouts, proper procedure indicators |
| Coral | `#E05C5C` | Hero callout (misconception warning), critical limitations |
| Mid Slate | `#3A4055` | Table headers, divider lines, cabinet outline |
| Deep Navy | `#0D1020` | Footer band background |
| Dark Callout | `#1E2435` | Callout box fills, cabinet interior |
| Alt Row | `#252B3D` | Alternating table rows |
| Bright Silver | `#C8D0D8` | Test panel shapes in cabinet diagram |

### Step 5 — Set ruler guides

**Vertical guides (from left edge):**
- 0.5" — left safe zone margin
- 23.5" — right safe zone margin

**Horizontal guides (from top edge):**
- 0.5" — top safe zone margin
- 3.4" — Zone 1/Zone 2 boundary
- 10.0" — Zone 2/Zone 3 boundary
- 12.5" — Zone 3/Zone 4 boundary
- 27.5" — Zone 4/Zone 5 boundary
- 32.5" — Zone 5/Zone 6 boundary
- 35.5" — bottom safe zone margin

---

## Part 3 — Layout Zones and Build Order

Build in this sequence. Each zone is a discrete group of elements. Complete one zone before moving to the next. **Group each zone (Ctrl+G / Cmd+G) after completing it.**

```
ZONE 1 — HEADER BAND (0"–3.4")
  Block A: Headline + subheading + HERO CALLOUT (the misconception warning)

ZONE 2 — SALT SPRAY CABINET CROSS-SECTION (3.4"–10.0" / ~6.6" tall)
  Block B: Simplified cabinet schematic (HERO illustration)
  Block C: Key operation callouts (panel angle, collection cups, fog distribution)

ZONE 3 — SOLUTION COMPARISON STRIP (10.0"–12.5" / ~2.5" tall)
  Block CC: Three key solution formulations side by side (B117, B368, B287)

ZONE 4 — SIX-METHOD COMPARISON TABLE (12.5"–27.5" / ~15.0" tall)
  Block D: Six-column comparison table (B117, B368, B287, B380, D2247, B605)

ZONE 5 — BEST PRACTICES + LIMITATIONS (27.5"–32.5" / ~5.0" tall)
  Block E: Proper operation best practices (left half)
  Block F: Limitations and misconceptions (right half)

ZONE 6 — FOOTER BAND (32.5"–36.0" / ~3.5" tall)
  Block G: Disclaimer + poster title + series name + logo placeholder + version
```

---

## Part 4 — Zone-by-Zone Build Specifications

### ZONE 1 — Header Band

**Dimensions:** Full page width. Y: 0" to 3.4".
**Background:** Same as page (`#1A1F2E`) — no separate fill needed.

---

**BLOCK A — Headline**

- Element type: Text box
- Position: X: 0.5" (left safe zone). Y: 0.5" (top safe zone)
- Width: 23.0" (full safe zone width)
- Font: Barlow Condensed ExtraBold
- Size: 84 pt
- Color: `#F0EDE8`
- Letter spacing: Tight (spacing slider: approximately -4)
- Text (all caps):

> CORROSION TESTING AT A GLANCE

**BLOCK A — Subheading**

- Element type: Text box
- Position: X: 0.5". Y: immediately below headline baseline + 6 pt gap (approximately Y: 1.5")
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 36 pt
- Color: `#2EC4B6` (Teal)
- Text:

> Salt Spray, CASS, Humidity, and Beyond

**BLOCK A — Hero Callout (Misconception Warning)**

This is the poster's single most important message — positioned prominently in the header band.

- Element type: Rounded rectangle
- Position: X: 0.5". Y: 2.2"
- Width: 23.0". Height: 1.0"
- Fill: `#E05C5C` (Coral) at 15% opacity
- Border: 2 pt, `#E05C5C`
- Corner radius: 6 pt

Text inside:
- Font: Barlow Condensed ExtraBold, 28 pt, `#E05C5C`
- Alignment: Center
- Text:

> SALT SPRAY TESTING IS A RELATIVE COMPARISON TOOL — NOT A PREDICTOR OF SERVICE LIFE

---

### ZONE 2 — Salt Spray Cabinet Cross-Section (HERO)

**Dimensions:** Full page width within margins. Y: 3.4" to 10.0" (~6.6" tall).

---

**Section label:**
- Element type: Text box
- Position: Centered horizontally. Y: 3.6"
- Font: Barlow Condensed ExtraBold
- Size: 28 pt
- Color: `#F0EDE8`
- Alignment: Center
- Text:

> INSIDE THE SALT SPRAY CABINET

---

**BLOCK B — Cabinet Cross-Section Schematic**

Y: 4.3" to 9.5" (~5.2" available).

This is a simplified cross-section showing the key operational features of a salt spray (fog) cabinet. Built entirely from geometric shapes.

**Cabinet body (outer shell):**
- Element type: Rectangle
- Position: X: 3.0". Y: 4.5"
- Width: 18.0". Height: 4.5"
- Fill: `#1E2435` (Dark Callout — represents cabinet interior)
- Border: 3 pt, `#3A4055` (Mid Slate)
- Corner radius: 4 pt (top corners only if possible; otherwise square is fine)

**Cabinet lid (top, slightly angled to prevent drip-back):**
- Element type: Line (slight angle) or thin rectangle
- Position: Spans full cabinet width at top, with a slight pitch
- Stroke: 3 pt, `#3A4055`
- Label above lid: `Lid angled to prevent condensate dripping on panels` — Inter Regular, 12 pt, `#F0EDE8` at 60%

**Fog zone (interior fill representing mist):**
- Element type: Rectangle
- Position: Inside cabinet body, offset 0.3" from all interior walls
- Width: 17.4". Height: 3.2"
- Fill: `#2EC4B6` at 8% opacity (very faint teal haze — represents salt fog)
- No border

**Atomizer nozzle (center-bottom of cabinet):**
- Element type: Small triangle or inverted teardrop shape
- Position: Bottom-center of cabinet interior. X: 12.0". Y: 8.5"
- Fill: `#E8A020` (Amber)
- Size: 0.4" wide, 0.3" tall
- Label: `Atomizer nozzle` — Inter Regular, 11 pt, `#E8A020`

**Fog spray lines (emanating from atomizer):**
- Element type: 3-5 thin dashed lines radiating upward from the nozzle in a fan pattern
- Stroke: 1 pt dashed, `#2EC4B6` at 40%
- Length: 2.0" each, spreading from center

**Test panels (3 angled panels inside cabinet):**
- Element type: Thin rectangles (0.15" wide, 2.5" tall), angled at approximately 20 degrees from vertical
- Position: Evenly spaced inside the cabinet (X: 6.0", 10.0", 14.0")
- Fill: `#C8D0D8` (Bright Silver)
- Each panel sits on a small support line at the bottom

**Panel angle callout:**
- Element type: Arc or angle indicator between one panel and vertical
- Label: `15–30° from vertical` — JetBrains Mono Regular, 14 pt, `#E8A020`
- Position: Adjacent to the rightmost panel

**Collection cups (bottom of cabinet, below panels):**
- Element type: 2 small circle shapes
- Diameter: 0.4"
- Fill: `#2EC4B6` at 30%
- Border: 1 pt, `#2EC4B6`
- Position: Bottom of cabinet interior, between panels. X: 8.0" and 12.0". Y: 8.6"
- Label: `Collection cups — verify 1.0–2.0 mL/hr/80 cm² fog rate` — JetBrains Mono Regular, 11 pt, `#2EC4B6`

**Temperature callout (right side of cabinet):**
- Element type: Text box with Teal left-border accent
- Position: X: 21.5". Y: 6.0"
- Font: JetBrains Mono Regular, 14 pt, `#F0EDE8`
- Text:

> 95 +/- 3°F
> (35 +/- 1.7°C)

Label above: `Cabinet temp:` — Barlow SemiBold, 12 pt, `#2EC4B6`

---

**BLOCK C — Key Operation Notes** (below cabinet, Y: 9.2" to 9.8")

Three inline callouts spaced across the width:

| Callout | X | Color | Text |
|---|---|---|---|
| Left | 0.5" | `#E8A020` | `Maintain unobstructed fog circulation — panels must not touch or shield each other` |
| Center | 8.5" | `#2EC4B6` | `Solution: 5 parts NaCl to 95 parts DI water (by weight) for B117` |
| Right | 16.5" | `#27AE60` | `Log exposure hours and check daily — interruptions must be recorded` |

Each: Inter Medium, 14 pt, respective color. Width: ~7.0" each.

---

### ZONE 3 — Solution Comparison Strip

**Dimensions:** Full page width within margins. Y: 10.0" to 12.5" (~2.5" tall).

---

**Section label:**
- Element type: Text box
- Position: Centered horizontally. Y: 10.2"
- Font: Barlow Condensed ExtraBold
- Size: 24 pt
- Color: `#F0EDE8`
- Alignment: Center
- Text:

> TEST SOLUTIONS — THE KEY DIFFERENCES

---

**BLOCK CC — Three Solution Cards**

Y: 10.8" to 12.3". Three cards side by side, each 7.33" wide with 0.17" gaps.

**Card 1 — B117 (Neutral Salt Spray):**
- Element type: Rounded rectangle
- Position: X: 0.5". Y: 10.8"
- Width: 7.2". Height: 1.4"
- Fill: `#1E2435`. Corner radius: 4 pt.
- Left-border accent: 0.06" wide, `#2EC4B6` (Teal)
- Title: `B117 — Neutral Salt Spray` — Barlow SemiBold, 16 pt, `#2EC4B6`
- Body: `5% NaCl  |  pH 6.5–7.2  |  35°C` — JetBrains Mono Regular, 14 pt, `#F0EDE8`

**Card 2 — B368 (CASS):**
- Element type: Rounded rectangle
- Position: X: 8.0". Y: 10.8"
- Width: 7.2". Height: 1.4"
- Fill: `#1E2435`. Corner radius: 4 pt.
- Left-border accent: 0.06" wide, `#E8A020` (Amber)
- Title: `B368 — CASS (Copper-Accel.)` — Barlow SemiBold, 16 pt, `#E8A020`
- Body: `5% NaCl + 0.25 g/L CuCl₂  |  pH 3.1–3.3  |  49°C` — JetBrains Mono Regular, 13 pt, `#F0EDE8`

**Card 3 — B287 (Acetic Acid Salt Spray):**
- Element type: Rounded rectangle
- Position: X: 15.5". Y: 10.8"
- Width: 7.5". Height: 1.4"
- Fill: `#1E2435`. Corner radius: 4 pt.
- Left-border accent: 0.06" wide, `#E05C5C` (Coral)
- Title: `B287 — Acetic Acid Salt Spray` — Barlow SemiBold, 16 pt, `#E05C5C`
- Body: `5% NaCl + acetic acid  |  pH 3.1–3.3  |  35°C` — JetBrains Mono Regular, 13 pt, `#F0EDE8`

---

### ZONE 4 — Six-Method Comparison Table

**Dimensions:** Full page width within margins. Y: 12.5" to 27.5" (~15.0" tall).

---

**Section label:**
- Element type: Text box
- Position: Centered horizontally. Y: 12.7"
- Font: Barlow Condensed ExtraBold
- Size: 28 pt
- Color: `#F0EDE8`
- Alignment: Center
- Text:

> THE SIX MAJOR TEST METHODS

---

**BLOCK D — Comparison Table**

Y: 13.4" to 27.0" (~13.6" available).

This is a six-column table with a header row and 7 data rows. Total width: 23.0" (within safe zone). Column widths vary for readability:

| Column | Test | Width | X Position |
|---|---|---|---|
| 1 | B117 (NSS) | 4.0" | 0.5" |
| 2 | B368 (CASS) | 4.0" | 4.5" |
| 3 | B287 (ASS) | 3.8" | 8.5" |
| 4 | B380 (Corrodkote) | 3.8" | 12.3" |
| 5 | D2247 (Humidity) | 3.7" | 16.1" |
| 6 | B605 (SO₂) | 3.4" | 19.8" |

**Column headers (row 0):**

Each column header:
- Element type: Rectangle
- Height: 0.8"
- Fill: `#3A4055` (Mid Slate)
- Text inside: Barlow Condensed ExtraBold, 16 pt, `#F0EDE8`
- Y: 13.4"

Header labels:
- Col 1: `B117` (line break) `Neutral Salt Spray`
- Col 2: `B368` (line break) `CASS`
- Col 3: `B287` (line break) `Acetic Acid SS`
- Col 4: `B380` (line break) `Corrodkote`
- Col 5: `D2247` (line break) `Humidity`
- Col 6: `B605` (line break) `SO₂`

**Row labels and data** (rows 1-7, built as alternating-color rectangles with text overlays):

Row height: 1.7" each (to accommodate wrapped text in narrow columns). Alternating fills: `#1E2435` (odd rows) and `#252B3D` (even rows).

Each row spans full table width. Row label at far left as a vertical header or integrated into the first cell. Use Inter Regular 14 pt for data cells, Inter Medium 13 pt `#F0EDE8` at 60% for row labels.

**Row 1 — Environment / Solution:**
- Label: `Solution`
- B117: `5% NaCl in DI water`
- B368: `5% NaCl + 0.25 g/L CuCl₂ + acetic acid`
- B287: `5% NaCl + acetic acid (glacial)`
- B380: `Slurry of salts + kaolin clay, applied and dried`
- D2247: `100% relative humidity, no salt`
- B605: `SO₂ gas environment`

**Row 2 — pH:**
- Label: `pH`
- B117: `6.5–7.2`
- B368: `3.1–3.3`
- B287: `3.1–3.3`
- B380: `N/A (dry slurry)`
- D2247: `N/A`
- B605: `Varies`

**Row 3 — Temperature:**
- Label: `Temp`
- B117: `95°F (35°C)`
- B368: `120°F (49°C)`
- B287: `95°F (35°C)`
- B380: `95°F (35°C)`
- D2247: `100°F (38°C)`
- B605: `77°F (25°C)`

**Row 4 — Typical Duration:**
- Label: `Duration`
- B117: `24–2,000+ hrs` (use Amber `#E8A020` for the number)
- B368: `6–240 hrs`
- B287: `24–1,000 hrs`
- B380: `20 hrs (standard)`
- D2247: `24–1,000 hrs`
- B605: `24–500 hrs`

**Row 5 — What It Simulates:**
- Label: `Simulates`
- B117: `General marine / industrial corrosion`
- B368: `Accelerated decorative Ni-Cr degradation`
- B287: `Acidic industrial atmosphere`
- B380: `Multi-salt mixed environment`
- D2247: `Tropical / high-humidity storage`
- B605: `Industrial acid rain / sulfur atmosphere`

**Row 6 — Best For / Specified By:**
- Label: `Best For`
- B117: `Zinc, zinc alloy, cadmium coatings; general screening`
- B368: `Decorative nickel-chrome (automotive, hardware)`
- B287: `Anodized aluminum, conversion coatings`
- B380: `Multi-layer systems, referee test`
- D2247: `Paint adhesion, organic coatings, corrosion resistance`
- B605: `Copper, silver deposits, electronic contacts`

**Row 7 — Destructive?:**
- Label: `Destructive?`
- All: `Yes — panels consumed` — Inter Regular, 14 pt, `#E05C5C` (Coral)

---

### ZONE 5 — Best Practices + Limitations

**Dimensions:** Full page width within margins. Y: 27.5" to 32.5" (~5.0" tall).

---

**BLOCK E — Proper Operation** (left half, X: 0.5" to 11.5")

Y: 27.7" to 32.3"

**Callout container:**
- Element type: Rounded rectangle
- Position: X: 0.5". Y: 27.7"
- Width: 11.0". Height: 4.5"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 6 pt

Left-border accent:
- Element type: Rectangle
- Position: X: 0.5". Y: 27.7"
- Width: 0.06". Height: 4.5"
- Fill: `#27AE60` (Emerald)

Callout title:
- Element type: Text box
- Position: X: 0.8". Y: 27.9"
- Font: Barlow SemiBold, 20 pt, `#27AE60`
- Text:

> GETTING RELIABLE RESULTS

Bullet list:
- Element type: Text box
- Position: X: 0.8". Y: 28.5"
- Width: 10.4"
- Font: Inter Regular, 16 pt, `#F0EDE8`
- Line height: 150%
- Text:

> - Prepare solution fresh each batch — NaCl purity matters
> - Verify pH of collected fog, not just the reservoir
> - Maintain panel angle at 15–30° from vertical — do not stack
> - Record exposure hours and any interruptions (power loss, door opened)
> - Clean cabinet and replace solution on schedule
> - Run control panels alongside test panels for baseline comparison
> - Report results as "hours to first appearance of base metal corrosion" — not just white/red rust

---

**BLOCK F — Limitations and Common Misconceptions** (right half, X: 12.0" to 23.5")

Y: 27.7" to 32.3"

**Callout container:**
- Element type: Rounded rectangle
- Position: X: 12.0". Y: 27.7"
- Width: 11.5". Height: 4.5"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 6 pt

Left-border accent:
- Element type: Rectangle
- Position: X: 12.0". Y: 27.7"
- Width: 0.06". Height: 4.5"
- Fill: `#E05C5C` (Coral)

Callout title:
- Element type: Text box
- Position: X: 12.3". Y: 27.9"
- Font: Barlow SemiBold, 20 pt, `#E05C5C`
- Text:

> WHAT SALT SPRAY CANNOT TELL YOU

Bullet list:
- Element type: Text box
- Position: X: 12.3". Y: 28.5"
- Width: 10.9"
- Font: Inter Regular, 16 pt, `#F0EDE8`
- Line height: 150%
- Text:

> - More hours in salt spray DOES NOT equal more years in service
> - Salt spray does not replicate real-world corrosion mechanisms (UV, thermal cycling, mechanical wear, crevice corrosion)
> - Results are only valid for comparing coatings tested under identical conditions in the same cabinet
> - Different test methods are NOT interchangeable — 24 hrs CASS is not equivalent to 24 hrs B117
> - Salt spray is an accelerated screening tool, not a life prediction model
> - Field failures have occurred on parts that passed extended salt spray testing

**Key fact callout (bottom of box):**
- Element type: Text box
- Position: X: 12.3". Y: 31.4"
- Width: 10.9"
- Font: JetBrains Mono Regular, 13 pt, `#E8A020` (Amber)
- Text:

> CASS is 6-8x more aggressive than B117 — 16 hrs CASS roughly equals 96-128 hrs NSS for decorative Ni-Cr

---

### ZONE 6 — Footer Band

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

> This poster is an educational reference tool. Test parameters, durations, and solution compositions are typical industry values per the referenced ASTM standards. Always verify against the current edition of each ASTM specification. Consult your quality engineer for application-specific test selection and acceptance criteria.

**Poster title:**
- Element type: Text box
- Position: X: 0.5". Y: 33.5"
- Font: Barlow SemiBold
- Size: 16 pt
- Color: `#F0EDE8`
- Text:

> Corrosion Testing at a Glance — Salt Spray, CASS, Humidity, and Beyond

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

After building each zone, select all elements within that zone and group them (Ctrl+G / Cmd+G). Name each group:

| Group Name | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, hero misconception callout |
| Zone 2 - Cabinet Cross-Section | Section label, cabinet schematic, panels, nozzle, fog, collection cups, callouts |
| Zone 3 - Solution Comparison | Section label, three solution cards |
| Zone 4 - Six-Method Table | Section label, six-column comparison table with headers and 7 data rows |
| Zone 5 - Best Practices and Limitations | Proper operation callout, misconceptions callout |
| Zone 6 - Footer | Footer band, disclaimer, poster title, series name, logo placeholder, version |

After grouping, lock each completed zone (right-click > Lock) before proceeding to the next.

---

## Part 6 — Light Edition Color Remap Table

Duplicate the completed Dark edition page. Work through this table from top to bottom:

| Dark Hex | Light Hex | Notes |
|----------|-----------|-------|
| `#1A1F2E` | `#F5F4F0` | Background and all BG-colored elements |
| `#F0EDE8` | `#1A1F2E` | All primary text |
| `#1E2435` | `#ECEEF4` | Callout box fills, cabinet interior |
| `#252B3D` | `#E8E8F0` | Alternate row backgrounds |
| `#0D1020` | `#1A1F2E` | Footer strip background |
| `#E8A020` | `#C8860A` | Amber accent elements |
| `#2EC4B6` | `#1A8C82` | Teal accent elements |
| `#27AE60` | `#1E7A47` | Emerald accent elements |
| `#E05C5C` | `#B83E3E` | Coral accent elements (including hero callout border and fill) |
| `#3A4055` | `#D0D4DE` | Table headers, cabinet outline, dividers |
| `#C8D0D8` | `#C8D0D8` | Bright Silver — **unchanged** |

Hero callout (Coral): In Light edition, the fill background changes from `#E05C5C` at 15% to `#B83E3E` at 10% — verify the Coral border and text remain legible on the light background.

---

## Part 7 — Export Checklist

Six files per poster:

| File Name | Mode | Quality | Bleed + Marks |
|---|---|---|---|
| `Corrosion Testing at a Glance — Dark — 24x36 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Corrosion Testing at a Glance — Dark — 18x24 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Corrosion Testing at a Glance — Dark — Digital.pdf` | RGB | PDF Standard | No |
| `Corrosion Testing at a Glance — Light — 24x36 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Corrosion Testing at a Glance — Light — 18x24 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Corrosion Testing at a Glance — Light — Digital.pdf` | RGB | PDF Standard | No |

For 18x24" versions: duplicate the 24x36" design, use the resize feature, then verify all text meets the 14 pt body text minimum floor. The six-column table in Zone 4 will be tight at 18x24" — Elara should flag if font size drops below 12 pt after resize.

---

*Alaina — Plating Posters Inc Creative Lead*
*Poster #22 — Corrosion Testing at a Glance — Construction Workup v1.0*
*2026-04-11*
