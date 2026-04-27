---
Project: Plating Posters Inc
Poster Number: 14
Title: "Safety in the Plating Shop: Chemical Hazard Quick Reference"
Document Type: Construction Workup
Status: v1.0 — Ready for Elara
Created: 2026-04-04T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Poster 14 — Safety in the Plating Shop — Content and Layout Draft.md (v1.0)"
Technical Source: GHS hazard classification standards (OSHA); general industry safety knowledge
Watson Flags: ONE COURTESY FLAG — non-blocking (GHS classifications and first aid protocols)
Process Scope: Safety/compliance reference — cross-process by nature
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow: Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Safety
  - ConstructionWorkup
  - Compliance
---

# Poster # Poster #14 — Construction Workup
## Safety in the Plating Shop: Chemical Hazard Quick Reference

*Alaina — Plating Posters Inc Creative Lead*
*v1.0 — 2026-04-04*

This document is the construction workup for Poster #14. It translates the finalized Content and Layout Draft (v1.0) into specifications directly usable by Elara to engineer a generation prompt for Drew. One Watson courtesy flag is open (GHS classification confirmation) — non-blocking.

> **Workflow update (2026-04-14):** Poster generation now uses claude.ai chat (SVG/HTML visual artifacts) These specs feed the Claude Chat Generation Prompt. If Drew approves the generated output, it proceeds to final production.

**Source of truth for content:** `Poster 14 — Safety in the Plating Shop — Content and Layout Draft.md` — all copy is reproduced here verbatim. If any discrepancy exists, the Content and Layout Draft governs.

---

## Part 1 — Workflow Orientation

### Design Capabilities for This Poster

- Text boxes with precise font, size, weight, color, and spacing control
- Solid-color rectangles and rounded rectangles for panel cards, callout boxes, and accent borders
- Shape rotation for GHS diamond pictograms (rotated squares)
- Icon library search for PPE icons, hazard symbols, and exposure route indicators
- Color fills set to exact hex values
- Background page color set to exact hex
- Export at print-quality PDF (300 DPI equivalent via print export)

### Limitations to Flag for Elara

1. **GHS diamond pictograms:** Built as squares rotated 45 degrees. In the design: add a square shape, rotate 45 degrees, set border to Coral `#E05C5C` (2 pt), fill to `#F0EDE8`. Place a icon inside (search for "skull", "exclamation", "corrosion"). The icon must be centered within the rotated diamond — alignment tools handle this well when both elements are selected and aligned.

2. **3x2 panel grid:** Six identical panel containers in a 3-column, 2-row grid. Build one panel completely, then duplicate 5 times and reposition. Change content in each copy. This is the most efficient approach .

3. **Exposure route icons:** Search icons for "hand" (skin), "lungs" (inhalation), "stomach" or "mouth" (ingestion), "eye" (eyes). If exact matches are unavailable, use simple circles with text labels — the text labels are the primary indicator, icons are reinforcement.

4. **PPE icons:** Search icons for "goggles", "gloves", "apron", "boots". Same fallback as exposure route icons.

5. **GHS color fidelity in Light edition:** The GHS pictogram diamonds must retain their standard GHS colors (red border on white background with dark icon) in BOTH editions. Do NOT remap the GHS pictograms when producing the Light edition. This is a regulatory communication standard.

6. **4 pt / 6 pt left-border accents on panels:** Simulate with a narrow colored rectangle (0.06" for 4 pt, 0.083" for 6 pt) positioned flush against the left edge of each panel.

7. **JetBrains Mono font and print size:** Same as all previous posters — the Pro tier required for font upload; 24x36" custom size at document creation.

8. **Sub/superscript characters:** Chemical formulas use Unicode subscript/superscript characters. These are provided verbatim below — copy-paste exactly. Key characters used: CrO₃, Na₂Cr₂O₇, Cr⁶⁺, H₂SO₄, HNO₃, NaOH, KOH, HCl, HF.

---

## Part 2 — Document Setup Instructions (for Elara's prompt)

### Step 1 — Create the document
- Open the design tool. Create a new custom-size design.
- Width: **24 inches**. Height: **36 inches**.

### Step 2 — Set the background color
- Set the page background color to: **`#1A1F2E`** (Gunmetal Dark)

### Step 3 — Upload fonts (the Pro tier required)
Upload from Google Fonts / JetBrains.org:
- **Barlow Condensed ExtraBold** — all headlines and zone labels
- **Barlow SemiBold** — all subheadings, section labels, callout titles, panel titles
- **Inter Regular** and **Inter Medium** — all body text, hazard descriptions, first aid
- **JetBrains Mono Regular** — chemical examples and formulas

If JetBrains Mono upload fails, substitute **Courier Prime**.

### Step 4 — Set up color palette (save as Brand Colors )

| Color Name | Hex | Primary Use |
|---|---|---|
| Gunmetal Dark | `#1A1F2E` | Background (Dark edition) |
| Warm White | `#F0EDE8` | All primary text; GHS diamond fills |
| Amber | `#E8A020` | Chromic acid mist panel + HCl/H₂SO₄ panel accent |
| Teal | `#2EC4B6` | Strong caustics panel accent; PPE callout |
| Emerald | `#27AE60` | Not primary on this poster (reserve) |
| Coral | `#E05C5C` | Hex chrome + cyanides + HNO₃/HF panel accent; GHS diamond borders; emergency callout |
| Mid Slate | `#3A4055` | Panel internal dividers, icon backgrounds |
| Deep Navy | `#0D1020` | Footer band background |
| Dark Callout | `#1E2435` | Panel card fills, callout box fills |
| Alt Row | `#252B3D` | Not primary on this poster |
| Bright Silver | `#C8D0D8` | Not used on this poster |

### Step 5 — Set ruler guides

**Vertical guides (from left edge):**
- 0.5" — left safe zone margin
- 8.17" — column 1/column 2 boundary
- 15.83" — column 2/column 3 boundary
- 23.5" — right safe zone margin

**Horizontal guides (from top edge):**
- 0.5" — top safe zone margin
- 3.6" — Zone 1/Zone 2 boundary
- 16.0" — Row 1/Row 2 boundary within Zone 2
- 28.1" — Zone 2/Zone 3 boundary
- 32.4" — Zone 3/Zone 4 boundary
- 35.5" — bottom safe zone margin

---

## Part 3 — Layout Zones and Build Order

Build in this sequence. Complete one zone before moving to the next. **Group each zone after completing it.**

```
ZONE 1 — HEADER BAND (0"–3.6")
  Block A: Headline + subheading + tagline (left ~60%)
  Block B: "Every Chemical. Every Time." callout box (right ~40%)

ZONE 2 — CHEMICAL HAZARD GRID (3.6"–28.1" / ~24.5" tall)
  Block C: 3x2 grid of chemical family panels (HERO)
  Row 1 (3.6"–16.0"): Hex Chrome | Cyanides | Chromic Acid Mist
  Row 2 (16.0"–28.1"): HCl/H₂SO₄ | HNO₃/HF | NaOH/KOH

ZONE 3 — UNIVERSAL PPE + EMERGENCY (28.1"–32.4" / ~4.3" tall)
  Block D: Universal PPE baseline (left 50%)
  Block E: Emergency response (right 50%)

ZONE 4 — FOOTER BAND (32.4"–36.0" / ~3.6" tall)
  Block F: Bold disclaimer + poster title + series name + logo + version
```

---

## Part 4 — Zone-by-Zone Build Specifications

### ZONE 1 — Header Band

**Dimensions:** Full page width. Y: 0" to 3.6".
**Background:** Same as page (`#1A1F2E`).

---

**BLOCK A — Headline**

- Element type: Text box
- Position: X: 0.5". Y: 0.5"
- Width: 13.5" (approximately 58% of artboard — leaves room for Block B)
- Font: Barlow Condensed ExtraBold
- Size: 88 pt (slightly smaller than standard 96 pt to fit the longer title)
- Color: `#F0EDE8`
- Letter spacing: Tight (spacing slider: approximately -4)
- Text (all caps):

> SAFETY IN THE PLATING SHOP

**BLOCK A — Subheading**

- Element type: Text box
- Position: X: 0.5". Y: approximately 1.7"
- Width: 13.5"
- Font: Barlow SemiBold
- Size: 36 pt
- Color: `#E8A020` (Amber)
- Text:

> Chemical Hazard Quick Reference

**BLOCK A — Tagline**

- Element type: Text box
- Position: X: 0.5". Y: approximately 2.4"
- Width: 13.5"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8`
- Transparency: 65%
- Text:

> Know what you're working with. Every shift, every day.

---

**BLOCK B — "Every Chemical. Every Time." Callout Box**

Callout container:
- Element type: Rounded rectangle
- Position: X: 14.5". Y: 0.6"
- Width: 9.0". Height: 2.6"
- Fill: `#1E2435` (Dark Callout)
- Border (stroke): 2 pt, `#E05C5C` (Coral)
- Corner radius: 8 pt

Callout title:
- Element type: Text box inside the container
- Position: X: 14.8". Y: 0.85"
- Font: Barlow SemiBold
- Size: 18 pt
- Color: `#E05C5C` (Coral)
- Text:

> EVERY CHEMICAL. EVERY TIME.

Callout body:
- Element type: Text box inside the container
- Position: X: 14.8". Y: 1.3"
- Width: 8.4"
- Font: Inter Regular
- Size: 17 pt
- Color: `#F0EDE8`
- Line height: 140%
- Text:

> Before you handle any chemical, ask three questions: What is it? What does it do to me? What do I do if something goes wrong? This poster helps with all three.

---

### ZONE 2 — Chemical Hazard Grid (HERO)

**Dimensions:** Full page width within margins. Y: 3.6" to 28.1" (~24.5" tall).

**Grid layout:** 3 columns x 2 rows = 6 panels.
- Column width: ~7.3" each (23.0" safe zone / 3 columns, minus 0.2" gutters between columns)
  - Column 1: X: 0.5" to 7.6"
  - Column 2: X: 7.8" to 14.9"
  - Column 3: X: 15.1" to 22.2" ... adjust: let me compute clean: 23.0" total safe zone, 0.2" gutter x 2 = 0.4". Available: 22.6" / 3 = ~7.53" per column.
  - Column 1: X: 0.5" to 8.03"
  - Column 2: X: 8.23" to 15.77"
  - Column 3: X: 15.97" to 23.5"
- Row height: ~12.0" each (24.5" / 2 rows, minus 0.2" gutter = 12.15" per row)
  - Row 1: Y: 3.6" to 15.8"
  - Row 2: Y: 16.0" to 28.1"

**Panel dimensions:** Each panel is approximately 7.53" wide x 12.15" tall.

---

**PANEL TEMPLATE (identical structure for all 6 panels):**

Each panel is a rounded rectangle container with internal elements stacked vertically:

Container:
- Element type: Rounded rectangle
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 8 pt

Left-border accent:
- Element type: Rectangle
- Width: 0.083" (6 pt equivalent)
- Height: matches container height
- Fill: panel-specific accent color (see below)
- Position: Flush against left edge of container

Internal elements (top to bottom, all X positions relative to container left + 0.3" padding):

1. **GHS pictogram diamond** (Y: container top + 0.3")
   - Square shape, rotated 45 degrees
   - Size: 1.0" x 1.0" (before rotation — diamond will measure ~1.4" corner-to-corner)
   - Border: 2 pt, `#E05C5C` (Coral — standard GHS red)
   - Fill: `#F0EDE8` (Warm White — standard GHS white)
   - Interior icon: icon in `#1A1F2E` (Gunmetal Dark — standard GHS black), centered inside diamond
   - Position: Centered horizontally within panel

2. **Chemical family name** (Y: below diamond + 0.3")
   - Font: Barlow Condensed ExtraBold
   - Size: 22 pt
   - Color: panel accent color
   - Alignment: Center

3. **Chemical examples** (Y: below name + 0.15")
   - Font: JetBrains Mono Regular
   - Size: 14 pt
   - Color: `#F0EDE8` at 80% opacity
   - Alignment: Center

4. **Hazard description** (Y: below examples + 0.25")
   - Font: Inter Regular
   - Size: 16 pt
   - Color: `#F0EDE8`
   - Line height: 135%
   - Width: panel width minus 0.6" (0.3" padding each side)

5. **Exposure routes row** (Y: below hazard + 0.3")
   - 3-4 icons in a horizontal row (search: "hand", "lungs", "eye", "stomach")
   - Icon size: 0.4" x 0.4"
   - Default icon color: `#F0EDE8` at 40% opacity (dimmed = not primary route)
   - Highlighted route icon color: panel accent color (full opacity)
   - Labels below each icon: Inter Regular, 10 pt, matching color

6. **PPE requirements** (Y: below routes + 0.25")
   - Font: Inter Regular
   - Size: 14 pt
   - Color: `#2EC4B6` (Teal)
   - Line height: 130%
   - Prefix label: `PPE:` in Barlow SemiBold, 14 pt, `#2EC4B6`

7. **First aid** (Y: below PPE + 0.25")
   - Font: Inter Regular
   - Size: 14 pt
   - Color: `#F0EDE8`
   - Line height: 130%
   - Prefix label: `FIRST AID:` in Barlow SemiBold, 14 pt, `#F0EDE8`
   - Bold/emphasized lines within first aid: Inter Medium, same size, panel accent color

---

**PANEL 1 — HEXAVALENT CHROMIUM** (Row 1, Column 1)
- Position: X: 0.5". Y: 3.6"
- Accent color: `#E05C5C` (Coral)
- GHS icon search: "skull" (skull and crossbones)
- Chemical name: `HEXAVALENT CHROMIUM`
- Examples: `CrO₃ (chromic acid), Na₂Cr₂O₇ (sodium dichromate)`
- Hazard: `Known human carcinogen. Targets lungs, kidneys, liver. Causes severe skin ulceration ("chrome holes"). Corrosive to all tissues on contact.`
- Exposure routes highlighted: **Skin**, **Inhalation**, **Ingestion** — all three
- PPE: `Full-face respirator with P100/OV cartridge. Chemical-resistant gloves (nitrile minimum). Chemical splash goggles. Rubber apron and boots.`
- First aid:
  - `Skin: flush 15+ min with water; seek medical attention for any skin break`
  - `Eyes: flush 15+ min; emergency medical treatment`
  - `Inhalation: move to fresh air; call 911 if breathing difficulty`
  - `Ingestion: do NOT induce vomiting; call Poison Control`

**PANEL 2 — CYANIDES** (Row 1, Column 2)
- Position: X: 8.23". Y: 3.6"
- Accent color: `#E05C5C` (Coral)
- GHS icon search: "skull"
- Chemical name: `CYANIDES`
- Examples: `NaCN, KCN, CuCN (copper cyanide strike baths)`
- Hazard: `Extremely toxic. Fatal by inhalation, skin absorption, or ingestion at very low doses. Releases hydrogen cyanide gas (HCN) on contact with acid — potentially fatal. Never allow cyanide to contact acid.`
- Exposure routes highlighted: **Skin**, **Inhalation**, **Ingestion** — all three
- PPE: `Full-face respirator with cyanide-specific cartridge. Chemical-resistant gloves. Chemical splash goggles. Rubber apron. HCN monitor in work area.`
- First aid:
  - `Skin: flush immediately; remove contaminated clothing`
  - `Inhalation: move to fresh air; call 911; amyl nitrite if available (trained responders only)`
  - `Ingestion: call 911 immediately; do NOT induce vomiting`
  - **Bold emphasis line:** `NEVER mix cyanide solutions with acid — HCN gas is fatal` (Inter Medium, `#E05C5C`)

**PANEL 3 — CHROMIC ACID MIST** (Row 1, Column 3)
- Position: X: 15.97". Y: 3.6"
- Accent color: `#E8A020` (Amber)
- GHS icon search: "exclamation" (exclamation mark)
- Chemical name: `CHROMIC ACID MIST`
- Examples: `Airborne Cr⁶⁺ from chrome plating tank surface — decorative and hard chrome`
- Hazard: `Chrome plating tanks generate hexavalent chromium mist from gas evolution at the anode. Inhaled mist causes nasal septum perforation, lung damage, and increased cancer risk. OSHA PEL: 5 µg/m³ (8-hr TWA).`
- Exposure routes highlighted: **Inhalation** (primary), Skin (secondary — dimmed but not fully off)
- PPE: `Fume suppressant on bath surface (mandatory). Local exhaust ventilation. P100 respirator when near open tanks. Periodic air monitoring per OSHA.`
- First aid:
  - `Inhalation: move to fresh air immediately; medical evaluation`
  - `Skin: flush thoroughly; monitor for irritation or ulceration`
  - `Note: fume suppressants reduce mist but do not eliminate exposure` (Inter Regular, `#F0EDE8` at 70%)

**PANEL 4 — STRONG MINERAL ACIDS** (Row 2, Column 1)
- Position: X: 0.5". Y: 16.0"
- Accent color: `#E8A020` (Amber)
- GHS icon search: "corrosion" (hand/surface being corroded)
- Chemical name: `STRONG MINERAL ACIDS`
- Examples: `HCl (muriatic/hydrochloric), H₂SO₄ (sulfuric) — used in activation, pickling, cleaning`
- Hazard: `Corrosive to skin, eyes, and respiratory tract. HCl fumes irritate lungs at low concentrations. Concentrated H₂SO₄ causes severe thermal and chemical burns. Both react violently with bases.`
- Exposure routes highlighted: **Skin**, **Inhalation**, **Eyes** — all three
- PPE: `Chemical splash goggles (minimum). Face shield for pouring/mixing. Chemical-resistant gloves (butyl or nitrile). Rubber apron. Local ventilation.`
- First aid:
  - `Skin: flush 15+ min; remove contaminated clothing`
  - `Eyes: flush 15+ min with eyewash; emergency medical treatment`
  - `Inhalation: move to fresh air; medical evaluation if symptoms persist`
  - `Spills: neutralize with soda ash or sodium bicarbonate; contain and absorb`

**PANEL 5 — NITRIC / HYDROFLUORIC ACID** (Row 2, Column 2)
- Position: X: 8.23". Y: 16.0"
- Accent color: `#E05C5C` (Coral)
- GHS icon search: "skull"
- Chemical name: `NITRIC / HYDROFLUORIC ACID`
- Examples: `HNO₃ (bright dips, passivation), HF (stainless etch, aluminum desmut blends)`
- Hazard: `HNO₃: strong oxidizer; reacts violently with organics; generates toxic NO₂ fumes. HF: penetrates skin silently; causes deep tissue destruction and hypocalcemia — potentially fatal even from small skin exposures. HF burns may not be painful immediately.`
- Exposure routes highlighted: **Skin** (especially HF), **Inhalation**, **Eyes**
- PPE: `Face shield. HF-specific gloves (neoprene or butyl — NOT nitrile alone). Full chemical suit for HF handling. Calcium gluconate gel must be immediately available where HF is used.`
- First aid:
  - `HF skin exposure: apply calcium gluconate gel immediately; flood with water; call 911`
  - `HNO₃ skin: flush 15+ min; medical attention for any discoloration`
  - `Eyes: flush 15+ min; emergency medical treatment`
  - **Bold emphasis line:** `HF: delayed pain does NOT mean delayed damage — treat immediately` (Inter Medium, `#E05C5C`)

**PANEL 6 — STRONG CAUSTICS** (Row 2, Column 3)
- Position: X: 15.97". Y: 16.0"
- Accent color: `#2EC4B6` (Teal)
- GHS icon search: "corrosion"
- Chemical name: `STRONG CAUSTICS`
- Examples: `NaOH (caustic soda/lye), KOH (potassium hydroxide) — cleaners, etchants, pH adjusters`
- Hazard: `Corrosive to skin and eyes. Causes deep chemical burns that may not be immediately painful (saponifies tissue fats). Eye exposure can cause permanent blindness. Concentrated solutions are extremely slippery — fall hazard.`
- Exposure routes highlighted: **Skin**, **Eyes** (primary) — Inhalation dimmed
- PPE: `Chemical splash goggles (mandatory). Face shield for pouring/mixing. Chemical-resistant gloves (nitrile or butyl). Rubber apron.`
- First aid:
  - `Skin: flush 15+ min; do NOT try to neutralize with acid on skin`
  - `Eyes: flush 15+ min with eyewash; emergency medical treatment — time is critical`
  - `Ingestion: do NOT induce vomiting; call Poison Control`
  - **Bold emphasis line:** `Eye exposure requires immediate, extended flushing — seconds count` (Inter Medium, `#2EC4B6`)

---

### ZONE 3 — Universal PPE + Emergency Response

**Dimensions:** Full page width within margins. Y: 28.1" to 32.4" (~4.3" tall).

---

**BLOCK D — Universal PPE Baseline (Left Half)**

Callout container:
- Element type: Rounded rectangle
- Position: X: 0.5". Y: 28.3"
- Width: 11.2". Height: 3.8"
- Fill: `#1E2435` (Dark Callout)
- Border (stroke): 1.5 pt, `#2EC4B6` (Teal)
- Corner radius: 8 pt

Callout title:
- Element type: Text box
- Position: X: 0.8". Y: 28.55"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#2EC4B6` (Teal)
- Text:

> MINIMUM PPE — EVERY CHEMICAL, EVERY TIME

Icon row:
- Element type: 4 icons in a horizontal row
- Position: X: 1.0" to 10.5". Y: 29.2"
- Icon size: 0.5" x 0.5" (36 pt equivalent)
- Color: `#F0EDE8`
- Spacing: evenly distributed across row

| Icon Search | Label Below Icon |
|---|---|
| "goggles" or "glasses" | Safety goggles |
| "gloves" | Chemical-resistant gloves |
| "apron" or "coat" | Protective apron |
| "boots" or "shoe" | Chemical-resistant footwear |

Labels:
- Font: Inter Regular, 11 pt, `#F0EDE8`
- Alignment: Center under each icon

Body note:
- Element type: Text box
- Position: X: 0.8". Y: 30.5"
- Width: 10.6"
- Font: Inter Regular
- Size: 16 pt
- Color: `#F0EDE8`
- Line height: 135%
- Text:

> This is the baseline. Individual chemicals may require additional PPE (respirators, face shields, full chemical suits). Always check the SDS for the specific product you are handling.

---

**BLOCK E — Emergency Response (Right Half)**

Callout container:
- Element type: Rounded rectangle
- Position: X: 12.0". Y: 28.3"
- Width: 11.5". Height: 3.8"
- Fill: `#1E2435` (Dark Callout)
- Border (stroke): 2 pt, `#E05C5C` (Coral)
- Corner radius: 8 pt

Callout title:
- Element type: Text box
- Position: X: 12.3". Y: 28.55"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#E05C5C` (Coral)
- Text:

> IN ANY EMERGENCY

Numbered steps:
- Element type: Text box
- Position: X: 12.3". Y: 29.1"
- Width: 10.9"
- Font: Inter Medium
- Size: 20 pt
- Color: `#F0EDE8`
- Line height: 155%
- Text:

> 1. REMOVE the person from exposure
> 2. FLUSH affected area with water immediately
> 3. CALL 911 — do not wait for symptoms
> 4. LOCATE the SDS for the specific chemical
> 5. INFORM responders of the chemical name and concentration

Bold footer line:
- Element type: Text box
- Position: Centered horizontally within callout. Y: 31.6"
- Font: Barlow Condensed ExtraBold
- Size: 22 pt
- Color: `#E05C5C` (Coral)
- Alignment: Center
- Text:

> WHEN IN DOUBT, CALL 911 FIRST.

---

### ZONE 4 — Footer Band

**Dimensions:** Full page width. Y: 32.4" to 36.0" (~3.6" tall).

---

**Footer band background:**
- Element type: Rectangle
- Position: X: 0". Y: 32.4"
- Width: 24.0". Height: 3.6"
- Fill: `#0D1020` (Deep Navy)

**BOLD DISCLAIMER (larger than normal — this is a safety poster):**
- Element type: Text box
- Position: X: 0.5". Y: 32.7"
- Width: 23.0"
- Font: Inter Medium
- Size: 14 pt (larger than standard 11 pt disclaimer)
- Color: `#F0EDE8`
- Alignment: Center
- Text (ALL CAPS):

> THIS POSTER IS A HAZARD AWARENESS REFERENCE. IT DOES NOT REPLACE YOUR SAFETY DATA SHEETS (SDS). IN ANY EMERGENCY, CALL 911. CONSULT YOUR SDS FOR COMPLETE HAZARD INFORMATION, EXPOSURE LIMITS, AND FIRST AID PROCEDURES FOR EACH SPECIFIC PRODUCT.

**Poster title:**
- Element type: Text box
- Position: X: 0.5". Y: 33.8"
- Font: Barlow SemiBold
- Size: 16 pt
- Color: `#F0EDE8`
- Text:

> Safety in the Plating Shop: Chemical Hazard Quick Reference

**Series name:**
- Element type: Text box
- Position: Centered horizontally. Y: 34.4"
- Font: Inter Regular
- Size: 14 pt
- Color: `#F0EDE8` at 70% opacity
- Alignment: Center
- Text:

> Plating Posters Inc — Metal Finishing Reference Series

**Logo placeholder:**
- Element type: Rectangle
- Position: X: 22.5". Y: 33.6"
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
| Zone 1 - Header | Headline, subheading, tagline, "Every Chemical" callout box |
| Zone 2 - Hazard Grid | 6 panel groups (each panel should be its own sub-group) |
| Zone 2 - Panel 1 Hex Chrome | GHS diamond, name, examples, hazard, routes, PPE, first aid |
| Zone 2 - Panel 2 Cyanides | (same internal structure) |
| Zone 2 - Panel 3 Chromic Mist | (same internal structure) |
| Zone 2 - Panel 4 Mineral Acids | (same internal structure) |
| Zone 2 - Panel 5 HNO3 HF | (same internal structure) |
| Zone 2 - Panel 6 Caustics | (same internal structure) |
| Zone 3 - PPE + Emergency | PPE callout (left), Emergency callout (right) |
| Zone 4 - Footer | Footer band, bold disclaimer, poster title, series name, logo, version |

Build approach: Build Panel 1 completely, verify it fits within the allocated space, then duplicate 5 times, reposition each copy, and change content. This ensures perfect structural consistency across all 6 panels.

---

## Part 6 — Light Edition Color Remap Table

Duplicate the completed Dark edition page. Work through this table from top to bottom:

| Dark Hex | Light Hex | Notes |
|----------|-----------|-------|
| `#1A1F2E` | `#F5F4F0` | Background and all BG-colored elements |
| `#F0EDE8` | `#1A1F2E` | All primary text |
| `#1E2435` | `#ECEEF4` | Panel card fills, callout box fills |
| `#252B3D` | `#E8E8F0` | Alternate row backgrounds (if used) |
| `#0D1020` | `#1A1F2E` | Footer strip background |
| `#E8A020` | `#C8860A` | Amber accent elements |
| `#2EC4B6` | `#1A8C82` | Teal accent elements |
| `#27AE60` | `#1E7A47` | Emerald accent elements (if used) |
| `#E05C5C` | `#B83E3E` | Coral accent elements |
| `#3A4055` | `#D0D4DE` | Panel dividers, icon backgrounds |
| `#C8D0D8` | `#C8D0D8` | Bright Silver — **unchanged** (not used on this poster) |

**CRITICAL EXCEPTION — GHS Pictogram Diamonds:**
Do NOT remap the GHS pictogram elements. The GHS diamonds must retain their standard colors in both editions:
- Diamond border: `#E05C5C` (Coral) — **unchanged** in Light edition
- Diamond fill: `#F0EDE8` — **unchanged** in Light edition (becomes slightly less contrasty on light background, but the red border maintains visibility)
- Interior icon: `#1A1F2E` — **unchanged** in Light edition

This is a regulatory communication standard. GHS pictograms use red-bordered diamonds on white backgrounds by international convention.

---

## Part 7 — Export Checklist

Six files per poster:

| File Name | Mode | Quality | Bleed + Marks |
|---|---|---|---|
| `Safety Plating Shop — Dark — 24x36 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Safety Plating Shop — Dark — 18x24 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Safety Plating Shop — Dark — Digital.pdf` | RGB | PDF Standard | No |
| `Safety Plating Shop — Light — 24x36 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Safety Plating Shop — Light — 18x24 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Safety Plating Shop — Light — Digital.pdf` | RGB | PDF Standard | No |

For 18x24" versions: duplicate the 24x36" design, use the resize feature, then verify all text meets the 14 pt body text minimum floor. Panel internal text (14-16 pt on 24x36") will need careful verification after resize — some may need to be bumped up to meet the 14 pt floor on the smaller format.

---

*Alaina — Plating Posters Inc Creative Lead*
*Poster #14 — Safety in the Plating Shop — Construction Workup v1.0*
*2026-04-04*
