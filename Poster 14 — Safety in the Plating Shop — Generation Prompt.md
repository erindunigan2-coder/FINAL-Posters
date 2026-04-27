---
Project: Plating Posters Inc
Poster Number: 14
Title: "Safety in the Plating Shop: Chemical Hazard Quick Reference"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-04T00:00:00
Source: Poster 14 — Safety in the Plating Shop — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - Safety
  - Compliance
  - v1
---

# Claude Chat Generation Prompt — Poster #14
## Safety in the Plating Shop: Chemical Hazard Quick Reference
### Version 1.0 | Dark Edition (Primary) + Light Edition (Remap)

*Originally engineered by Elara from Alaina's Construction Workup. Adapted for Claude chat visual generation (2026-04-14). All technical content production-ready.*

---

**Workflow: Claude Chat Visual Generation**

> **IMPORTANT:** This poster is to be generated as a visual artifact in claude.ai chat (SVG or HTML recommended). Do NOT use any external design tools. Generate the poster visually in the chat as a complete SVG or HTML artifact.

**Instructions for Claude:**

- Generate this poster as a **complete visual artifact** — either SVG or HTML with inline CSS. The output should be a finished, print-ready poster design.
- The poster is **24 x 36 inches** (portrait orientation). Design at this aspect ratio.
- Produce the **Dark edition first** (dark background). The Light edition remap table is provided at the end.
- Follow the design specifications in each Phase below. They describe WHAT to render — layout zones, text content, colors, typography, and visual elements.
- Every color is specified as a hex code. Every font, size, and weight is specified. Follow them exactly.
- Chemical formulas use Unicode subscript/superscript characters. Reproduce them exactly as written in this document.
- Prioritize **readability at distance** — this poster will be read from 3-8 feet away on a shop wall.

---

## Phase 1 — Design Foundation

### Artboard
- **Size:** 24 x 36 inches (portrait)
- **Background color (Dark edition):** `#1A1F2E` (Gunmetal Dark)

### Typography
| Role | Font | Weight | Notes |
|------|------|--------|-------|
| Headlines | Barlow Condensed | ExtraBold (800) | All caps, tight letter-spacing (-4) |
| Subheadings | Barlow | SemiBold (600) | Title case |
| Body text | Inter | Regular (400) / Medium (500) | Sentence case |
| Data/formulas | JetBrains Mono | Regular (400) | Monospace for technical values |

### Brand Colors (Dark Edition)

| Name | Hex | Role |
|------|-----|------|
| Gunmetal Dark | `#1A1F2E` | Background |
| Warm White | `#F0EDE8` | Body text |
| Amber | `#E8A020` | Accent, subheadings |
| Teal | `#2EC4B6` | Callout borders, secondary accent |
| Emerald | `#27AE60` | Positive/success accent |
| Coral | `#E05C5C` | Warning/alert accent |
| Mid Slate | `#3A4055` | Dividers, table headers |
| Deep Navy | `#0D1020` | Footer band |
| Dark Callout | `#1E2435` | Card/callout box fills |
| Alt Row | `#252B3D` | Alternating row backgrounds |

### Layout Safe Zones
- **0.5" margin** on all sides (safe zone for print trimming)
- All content must stay within the 23" x 35" live area

---

## Phase 2 — Zone 1: Header Band

This zone occupies the top 3.6 inches. Headline + subheading + tagline on the left (~60%), "Every Chemical. Every Time." callout on the right (~40%).

### Step 6 — Place the headline
1. Add a heading text element: Type: `SAFETY IN THE PLATING SHOP`
2. Set properties:
   - **Font**: Barlow Condensed ExtraBold
   - **Size**: `88` (slightly smaller than standard 96 to fit the longer title)
   - **Color**: `F0EDE8`
   - **Letter spacing**: `-4`
   - **Alignment**: Left
3. Position: left edge at 0.5 inches, top edge at 0.5 inches. Width: `13.5"`.

### Step 7 — Place the subheading
1. Add text: `Chemical Hazard Quick Reference`
2. Font: Barlow SemiBold, Size: `36`, Color: `E8A020` (Amber), Alignment: Left
3. Position: X: **0.5"**, Y: approximately **1.7"**.

### Step 8 — Place the tagline
1. Add text: `Know what you're working with. Every shift, every day.`
2. Font: Barlow SemiBold, Size: `22`, Color: `F0EDE8`, Transparency: **65%**
3. Position: X: **0.5"**, Y: approximately **2.4"**.

### Step 9 — Build "Every Chemical. Every Time." callout

**9a — Container:**
1. Add rounded rectangle. Width: `9.0"`. Height: `2.6"`. Fill: `1E2435`. Border: 2 pt, `E05C5C` (Coral). Corner radius: `8`.
2. Position: X: **14.5"**, Y: **0.6"**.

**9b — Title:**
1. Add text: `EVERY CHEMICAL. EVERY TIME.`
2. Font: Barlow SemiBold, Size: `18`, Color: `E05C5C` (Coral)
3. Position: X: **14.8"**, Y: **0.85"**.

**9c — Body:**
1. Add text. Copy-paste:
   `Before you handle any chemical, ask three questions: What is it? What does it do to me? What do I do if something goes wrong? This poster helps with all three.`
2. Font: Inter Regular, Size: `17`, Color: `F0EDE8`, Line height: `1.4`
3. Position: X: **14.8"**, Y: **1.3"**. Width: `8.4"`.

**9d — Group the callout.**

### Step 10 — Group all of Zone 1
Select headline, subheading, tagline, and callout group. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 3 — Zone 2: Chemical Hazard Grid (Hero)

This zone occupies Y: 3.6" to 28.1" (~24.5 inches tall). 3 columns x 2 rows = 6 chemical family panels.

**Grid layout:**
- Column 1: X: **0.5"** to **8.03"** (7.53" wide)
- Column 2: X: **8.23"** to **15.77"** (7.53" wide)
- Column 3: X: **15.97"** to **23.5"** (7.53" wide)
- Row 1: Y: **3.6"** to **15.8"** (12.2" tall)
- Row 2: Y: **16.0"** to **28.1"** (12.1" tall)

### Step 11 — Build Panel 1 (Template): HEXAVALENT CHROMIUM

This is the template panel. Build it completely, then duplicate 5 times.

**11a — Panel container:**
1. Add rounded rectangle. Width: `7.53"`. Height: `12.15"`. Fill: `1E2435` (Dark Callout). Corner radius: `8`.
2. Position: X: **0.5"**, Y: **3.6"**.

**11b — Left-border accent:**
1. Add narrow rectangle. Width: `0.083"` (6 pt). Height: `12.15"`. Fill: `E05C5C` (Coral).
2. Position: flush against left edge (X: **0.5"**, Y: **3.6"**).

**11c — GHS diamond pictogram:**
1. Add a **square** shape.
2. Width: `1.0"`. Height: `1.0"`.
3. Fill: `F0EDE8` (Warm White). Border: 2 pt, `E05C5C` (Coral).
4. **Rotate 45 degrees:** With the square selected, find the rotation handle (circular arrow above the element). Drag it to rotate exactly 45 degrees. Or look for the rotation field in the position toolbar and type `45`.
5. Position: centered horizontally within the panel, Y: approximately **4.0"** (0.3" below panel top).
6. **Icon inside diamond:** Click **Elements** > search `skull`. Place a skull icon (skull and crossbones) inside the diamond.
   - Icon size: approximately `0.5"` x `0.5"`. Color: `1A1F2E` (Gunmetal Dark).
   - Center the icon within the rotated diamond using alignment tools (select both elements > Align > Center).
   - If exact skull icon is not available, use any hazard-related icon or skip — the text label below carries the data.

**11d — Chemical family name:**
1. Add text: `HEXAVALENT CHROMIUM`
2. Font: Barlow Condensed ExtraBold, Size: `22`, Color: `E05C5C` (Coral), Alignment: Center
3. Position: centered within panel, Y: approximately **5.5"** (below the diamond).

**11e — Chemical examples:**
1. Add text. Copy-paste: `CrO₃ (chromic acid), Na₂Cr₂O₇ (sodium dichromate)`
2. Font: JetBrains Mono Regular, Size: `14`, Color: `F0EDE8`, Transparency: **80%**, Alignment: Center
3. Position: centered within panel, Y: approximately **6.0"**.

**11f — Hazard description:**
1. Add text. Copy-paste:
   `Known human carcinogen. Targets lungs, kidneys, liver. Causes severe skin ulceration ("chrome holes"). Corrosive to all tissues on contact.`
2. Font: Inter Regular, Size: `16`, Color: `F0EDE8`, Line height: `1.35`
3. Position: X: panel left + 0.3" padding. Width: panel width minus 0.6". Y: approximately **6.5"**.

**11g — Exposure routes row:**
1. Use icons for: "hand" (Skin), "lungs" (Inhalation), "eye" (Eyes), "stomach" (Ingestion).
2. Place 4 icons in a horizontal row inside the panel. Icon size: `0.4"` x `0.4"`.
3. For **highlighted routes** (Skin, Inhalation, Ingestion on this panel): set icon color to `E05C5C` (Coral — panel accent).
4. For **non-primary route** (Eyes on this panel): set icon color to `F0EDE8` at 40% opacity (dimmed).
5. Add labels below each icon: `Skin`, `Inhalation`, `Eyes`, `Ingestion` — Inter Regular, `10` pt. Highlighted labels: accent color. Dimmed labels: `F0EDE8` at 40%.
6. Y: approximately **8.3"**.

**If icons are unavailable:** Use small circles with text labels. The text labels are the primary indicator.

**11h — PPE requirements:**
1. Add text. First line: `PPE:` in Barlow SemiBold, `14` pt, `2EC4B6` (Teal).
2. Body: Copy-paste:
   `Full-face respirator with P100/OV cartridge. Chemical-resistant gloves (nitrile minimum). Chemical splash goggles. Rubber apron and boots.`
3. Font: Inter Regular, Size: `14`, Color: `2EC4B6` (Teal), Line height: `1.3`
4. Y: approximately **9.3"**.

**11i — First aid:**
1. Add text. First line: `FIRST AID:` in Barlow SemiBold, `14` pt, `F0EDE8`.
2. Body: Copy-paste (as bullet list):
   ```
   Skin: flush 15+ min with water; seek medical attention for any skin break
   Eyes: flush 15+ min; emergency medical treatment
   Inhalation: move to fresh air; call 911 if breathing difficulty
   Ingestion: do NOT induce vomiting; call Poison Control
   ```
3. Font: Inter Regular, Size: `14`, Color: `F0EDE8`, Line height: `1.3`
4. Y: approximately **10.5"**.

**11j — Group the entire panel:**
Select the container, accent bar, GHS diamond + icon, family name, examples, hazard description, exposure route icons + labels, PPE text, and first aid text. Press **Ctrl+G**. Name: "Zone 2 - Panel 1 Hex Chrome".

### Step 12 — Duplicate and modify for Panels 2-6

Duplicate the Panel 1 group 5 times. Reposition each copy per the grid layout. Ungroup each temporarily, change all content, and re-group.

---

**Panel 2 — CYANIDES** (Row 1, Column 2: X: **8.23"**, Y: **3.6"**)

- **Accent color**: `#E05C5C` (Coral)
- **GHS icon**: skull (same as Panel 1)
- **Name**: `CYANIDES`
- **Examples**: `NaCN, KCN, CuCN (copper cyanide strike baths)`
- **Hazard**: `Extremely toxic. Fatal by inhalation, skin absorption, or ingestion at very low doses. Releases hydrogen cyanide gas (HCN) on contact with acid — potentially fatal. Never allow cyanide to contact acid.`
- **Routes highlighted**: Skin, Inhalation, Ingestion (all three)
- **PPE**: `Full-face respirator with cyanide-specific cartridge. Chemical-resistant gloves. Chemical splash goggles. Rubber apron. HCN monitor in work area.`
- **First aid**:
  ```
  Skin: flush immediately; remove contaminated clothing
  Inhalation: move to fresh air; call 911; amyl nitrite if available (trained responders only)
  Ingestion: call 911 immediately; do NOT induce vomiting
  ```
- **Bold emphasis line** (add at end of first aid section):
  `NEVER mix cyanide solutions with acid — HCN gas is fatal`
  Font: Inter Medium, Size: `14`, Color: `E05C5C` (Coral)

---

**Panel 3 — CHROMIC ACID MIST** (Row 1, Column 3: X: **15.97"**, Y: **3.6"**)

- **Accent color**: `#E8A020` (Amber)
- **GHS icon**: exclamation mark (search "exclamation")
- **Name**: `CHROMIC ACID MIST`
- **Examples**: Copy-paste: `Airborne Cr⁶⁺ from chrome plating tank surface — decorative and hard chrome`
- **Hazard**: Copy-paste: `Chrome plating tanks generate hexavalent chromium mist from gas evolution at the anode. Inhaled mist causes nasal septum perforation, lung damage, and increased cancer risk. OSHA PEL: 5 µg/m³ (8-hr TWA).`
- **Routes highlighted**: **Inhalation** (primary full accent). Skin (secondary — dimmed but not fully off, ~60% opacity).
- **PPE**: `Fume suppressant on bath surface (mandatory). Local exhaust ventilation. P100 respirator when near open tanks. Periodic air monitoring per OSHA.`
- **First aid**:
  ```
  Inhalation: move to fresh air immediately; medical evaluation
  Skin: flush thoroughly; monitor for irritation or ulceration
  Note: fume suppressants reduce mist but do not eliminate exposure
  ```
  (Final "Note:" line: Inter Regular, `F0EDE8` at 70%)

---

**Panel 4 — STRONG MINERAL ACIDS** (Row 2, Column 1: X: **0.5"**, Y: **16.0"**)

- **Accent color**: `#E8A020` (Amber)
- **GHS icon**: corrosion (search "corrosion" — hand/surface being corroded)
- **Name**: `STRONG MINERAL ACIDS`
- **Examples**: Copy-paste: `HCl (muriatic/hydrochloric), H₂SO₄ (sulfuric) — used in activation, pickling, cleaning`
- **Hazard**: Copy-paste: `Corrosive to skin, eyes, and respiratory tract. HCl fumes irritate lungs at low concentrations. Concentrated H₂SO₄ causes severe thermal and chemical burns. Both react violently with bases.`
- **Routes highlighted**: Skin, Inhalation, Eyes (all three)
- **PPE**: `Chemical splash goggles (minimum). Face shield for pouring/mixing. Chemical-resistant gloves (butyl or nitrile). Rubber apron. Local ventilation.`
- **First aid**:
  ```
  Skin: flush 15+ min; remove contaminated clothing
  Eyes: flush 15+ min with eyewash; emergency medical treatment
  Inhalation: move to fresh air; medical evaluation if symptoms persist
  Spills: neutralize with soda ash or sodium bicarbonate; contain and absorb
  ```

---

**Panel 5 — NITRIC / HYDROFLUORIC ACID** (Row 2, Column 2: X: **8.23"**, Y: **16.0"**)

- **Accent color**: `#E05C5C` (Coral)
- **GHS icon**: skull
- **Name**: `NITRIC / HYDROFLUORIC ACID`
- **Examples**: Copy-paste: `HNO₃ (bright dips, passivation), HF (stainless etch, aluminum desmut blends)`
- **Hazard**: Copy-paste: `HNO₃: strong oxidizer; reacts violently with organics; generates toxic NO₂ fumes. HF: penetrates skin silently; causes deep tissue destruction and hypocalcemia — potentially fatal even from small skin exposures. HF burns may not be painful immediately.`
- **Routes highlighted**: Skin (especially HF), Inhalation, Eyes
- **PPE**: `Face shield. HF-specific gloves (neoprene or butyl — NOT nitrile alone). Full chemical suit for HF handling. Calcium gluconate gel must be immediately available where HF is used.`
- **First aid**:
  ```
  HF skin exposure: apply calcium gluconate gel immediately; flood with water; call 911
  HNO₃ skin: flush 15+ min; medical attention for any discoloration
  Eyes: flush 15+ min; emergency medical treatment
  ```
- **Bold emphasis line**:
  `HF: delayed pain does NOT mean delayed damage — treat immediately`
  Font: Inter Medium, `14` pt, `E05C5C`

---

**Panel 6 — STRONG CAUSTICS** (Row 2, Column 3: X: **15.97"**, Y: **16.0"**)

- **Accent color**: `#2EC4B6` (Teal)
- **GHS icon**: corrosion
- **Name**: `STRONG CAUSTICS`
- **Examples**: Copy-paste: `NaOH (caustic soda/lye), KOH (potassium hydroxide) — cleaners, etchants, pH adjusters`
- **Hazard**: `Corrosive to skin and eyes. Causes deep chemical burns that may not be immediately painful (saponifies tissue fats). Eye exposure can cause permanent blindness. Concentrated solutions are extremely slippery — fall hazard.`
- **Routes highlighted**: Skin, Eyes (primary). Inhalation dimmed.
- **PPE**: `Chemical splash goggles (mandatory). Face shield for pouring/mixing. Chemical-resistant gloves (nitrile or butyl). Rubber apron.`
- **First aid**:
  ```
  Skin: flush 15+ min; do NOT try to neutralize with acid on skin
  Eyes: flush 15+ min with eyewash; emergency medical treatment — time is critical
  Ingestion: do NOT induce vomiting; call Poison Control
  ```
- **Bold emphasis line**:
  `Eye exposure requires immediate, extended flushing — seconds count`
  Font: Inter Medium, `14` pt, `2EC4B6` (Teal)

---

### Step 13 — Group all of Zone 2
Select all 6 panel groups. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 4 — Zone 3: Universal PPE + Emergency Response

This zone occupies Y: 28.1" to 32.4" (~4.3 inches tall). Two side-by-side callout boxes.

### Step 14 — Block D: Universal PPE Baseline (left half)

**14a — Container:**
1. Add rounded rectangle. Width: `11.2"`. Height: `3.8"`. Fill: `1E2435`. Border: 1.5 pt, `2EC4B6` (Teal). Corner radius: `8`.
2. Position: X: **0.5"**, Y: **28.3"**.

**14b — Title:**
1. Add text: `MINIMUM PPE — EVERY CHEMICAL, EVERY TIME`
2. Font: Barlow SemiBold, Size: `22`, Color: `2EC4B6`
3. Position: X: **0.8"**, Y: **28.55"**.

**14c — PPE icon row:**
1. Use icons for: "goggles", "gloves", "apron" (or "coat"), "boots" (or "shoe").
2. Place 4 icons in a horizontal row. Icon size: `0.5"` x `0.5"`. Color: `F0EDE8`.
3. Position: evenly distributed, X: **1.0"** to **10.5"**, Y: **29.2"**.
4. Add labels below each icon:
   - `Safety goggles` | `Chemical-resistant gloves` | `Protective apron` | `Chemical-resistant footwear`
   - Font: Inter Regular, `11` pt, `F0EDE8`, Alignment: Center under each icon.

**If icons unavailable:** Use small circles with text labels.

**14d — Body note:**
1. Add text. Copy-paste:
   `This is the baseline. Individual chemicals may require additional PPE (respirators, face shields, full chemical suits). Always check the SDS for the specific product you are handling.`
2. Font: Inter Regular, Size: `16`, Color: `F0EDE8`, Line height: `1.35`
3. Position: X: **0.8"**, Y: **30.5"**. Width: `10.6"`.

### Step 15 — Block E: Emergency Response (right half)

**15a — Container:**
1. Rounded rectangle. Width: `11.5"`. Height: `3.8"`. Fill: `1E2435`. Border: 2 pt, `E05C5C` (Coral). Corner radius: `8`.
2. Position: X: **12.0"**, Y: **28.3"**.

**15b — Title:**
1. Add text: `IN ANY EMERGENCY`
2. Font: Barlow SemiBold, Size: `22`, Color: `E05C5C` (Coral)
3. Position: X: **12.3"**, Y: **28.55"**.

**15c — Numbered steps:**
1. Add text. Copy-paste:
   ```
   1. REMOVE the person from exposure
   2. FLUSH affected area with water immediately
   3. CALL 911 — do not wait for symptoms
   4. LOCATE the SDS for the specific chemical
   5. INFORM responders of the chemical name and concentration
   ```
2. Font: Inter Medium, Size: `20`, Color: `F0EDE8`, Line height: `1.55`
3. Position: X: **12.3"**, Y: **29.1"**. Width: `10.9"`.

**15d — Bold footer line:**
1. Add text: `WHEN IN DOUBT, CALL 911 FIRST.`
2. Font: Barlow Condensed ExtraBold, Size: `22`, Color: `E05C5C` (Coral), Alignment: Center
3. Position: centered within the callout, Y: approximately **31.6"**.

### Step 16 — Group all of Zone 3
Select both callout groups. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 5 — Zone 4: Footer Band

### Step 17 — Footer band background
1. Add rectangle. Width: `24.0"`. Height: `3.6"`. Fill: `0D1020`.
2. Position: X: **0"**, Y: **32.4"**.

### Step 18 — BOLD DISCLAIMER (larger than standard — safety poster)
1. Add text. Copy-paste (ALL CAPS):
   `THIS POSTER IS A HAZARD AWARENESS REFERENCE. IT DOES NOT REPLACE YOUR SAFETY DATA SHEETS (SDS). IN ANY EMERGENCY, CALL 911. CONSULT YOUR SDS FOR COMPLETE HAZARD INFORMATION, EXPOSURE LIMITS, AND FIRST AID PROCEDURES FOR EACH SPECIFIC PRODUCT.`
2. Font: Inter Medium, Size: `14` (larger than standard 11 pt), Color: `F0EDE8`, Alignment: Center
3. Position: X: **0.5"**, Y: **32.7"**. Width: `23.0"`.

### Step 19 — Poster title
1. Add text: `Safety in the Plating Shop: Chemical Hazard Quick Reference`
2. Font: Barlow SemiBold, Size: `16`, Color: `F0EDE8`
3. Position: X: **0.5"**, Y: **33.8"**.

### Step 20 — Series name
1. Add text: `Plating Posters Inc — Metal Finishing Reference Series`
2. Font: Inter Regular, Size: `14`, Color: `F0EDE8`, Transparency: **70%**, Alignment: Center
3. Position: centered horizontally, Y: **34.4"**.

### Step 21 — Logo placeholder
1. Add rectangle. Width: `0.83"`. Height: `0.42"`. Fill: `3A4055`.
2. Position: X: **22.5"**, Y: **33.6"**.
3. Add text: `[LOGO]` — Inter Regular, `10` pt, `F0EDE8`, Transparency: **50%**.

### Step 22 — Version
1. Add text: `v1.0 — 2026`
2. Font: JetBrains Mono Regular, Size: `11`, Color: `F0EDE8`, Transparency: **50%**
3. Position: X: **0.5"**, Y: **35.0"**.

### Step 23 — Group all of Zone 4
Select footer rectangle, disclaimer, poster title, series name, logo, version. Press **Ctrl+G**.

---

## Phase 6 — Final Review Checklist

### Text verification
- [ ] Headline reads: `SAFETY IN THE PLATING SHOP` at 88 pt
- [ ] Subheading: `Chemical Hazard Quick Reference` in Amber
- [ ] All 6 panels present in 3x2 grid
- [ ] Panel 1: Hexavalent Chromium (Coral accent)
- [ ] Panel 2: Cyanides (Coral accent) — includes bold "NEVER mix" warning
- [ ] Panel 3: Chromic Acid Mist (Amber accent)
- [ ] Panel 4: Strong Mineral Acids (Amber accent)
- [ ] Panel 5: Nitric/Hydrofluoric Acid (Coral accent) — includes bold "HF delayed pain" warning
- [ ] Panel 6: Strong Caustics (Teal accent) — includes bold "Eye exposure" warning
- [ ] Each panel has: GHS diamond, name, examples, hazard, exposure routes, PPE, first aid
- [ ] PPE callout: 4 icons with labels
- [ ] Emergency callout: 5 numbered steps + bold "CALL 911 FIRST" line
- [ ] Bold disclaimer in ALL CAPS at 14 pt (larger than standard)
- [ ] All Unicode characters display correctly

### Color verification
- [ ] Background is `#1A1F2E`
- [ ] GHS diamonds: `#F0EDE8` fill, `#E05C5C` border (standard GHS colors)
- [ ] Panels 1, 2, 5 use Coral accent
- [ ] Panels 3, 4 use Amber accent
- [ ] Panel 6 uses Teal accent
- [ ] PPE callout border is Teal; Emergency border is Coral
- [ ] Footer band is `#0D1020`

### Layout verification
- [ ] 6 panels in 3x2 grid with consistent spacing
- [ ] All panel internal elements vertically consistent
- [ ] PPE and Emergency callouts side by side with no overlap
- [ ] All text within 0.5-inch safe zone

---

## Phase 7 — Light Edition: Remap Instructions

### Step 24 — Duplicate the page
1. **...** menu on page thumbnail > **Duplicate page**. Switch to Page 2.

### Step 25 — Change the background
Change from `1A1F2E` to `F5F4F0` (Off-White).

### Step 26 — Remap all elements

| Element Type | Change From | Change To |
|---|---|---|
| **Background** | `#1A1F2E` | `#F5F4F0` |
| **All body text** | `#F0EDE8` | `#1A1F2E` |
| **Panel card fills** | `#1E2435` | `#ECEEF4` |
| **Footer band** | `#0D1020` | `#1A1F2E` |
| **Amber elements** | `#E8A020` | `#C8860A` |
| **Teal elements** | `#2EC4B6` | `#1A8C82` |
| **Coral elements** | `#E05C5C` | `#B83E3E` |
| **Mid Slate elements** | `#3A4055` | `#D0D4DE` |

### CRITICAL EXCEPTION — GHS Pictogram Diamonds

**Do NOT remap the GHS pictogram elements.** The GHS diamonds must retain their standard colors in BOTH editions:
- Diamond border: `#E05C5C` (Coral) — **unchanged** in Light edition
- Diamond fill: `#F0EDE8` — **unchanged** in Light edition
- Interior icon: `#1A1F2E` — **unchanged** in Light edition

This is a regulatory communication standard. GHS pictograms use red-bordered diamonds on white backgrounds by international convention.

### Step 27 — Post-remap adjustments
1. **Tagline at 65%**: If too faint, increase to **75-80%**.
2. **Chemical examples at 80%**: If too faint, increase to **90%**.
3. **Dimmed exposure route icons at 40%**: If invisible on light background, increase to **55%**.
4. **Disclaimer at standard opacity**: Since this is larger text (14 pt), it should remain readable. Verify.
5. **PPE icon labels**: Verify readable on light background.

### Post-remap verification checklist
- [ ] GHS diamonds retain standard colors (red border, white fill, dark icon)
- [ ] All body text passes WCAG AA
- [ ] Bold warning lines in each panel are clearly visible
- [ ] Exposure route icons visible (both highlighted and dimmed)
- [ ] Emergency numbered steps readable

---

## Phase 8 — Export Instructions

### Step 28 — Export Dark edition (Page 1)

**28a — Print PDF, 24x36":**
1. **Share** > **Download** > **PDF Print**. Check **Crop marks and bleed**. Page 1.
2. Rename: `Safety Plating Shop — Dark — 24x36 — Print.pdf`

**28b — Digital PDF:**
1. **PDF Standard**. Uncheck crop marks. Page 1.
2. Rename: `Safety Plating Shop — Dark — Digital.pdf`

**28c — Print PDF, 18x24":**
1. **Resize** > **18 x 24 inches** > **Copy & resize**.
2. **Important:** Verify all panel text meets 14 pt minimum. Panel body text (14-16 pt on 24x36") will scale to approximately 10.5-12 pt at 75%. You may need to increase panel body text to 15-16 pt on the 18x24" version.
3. Export PDF Print. Rename: `Safety Plating Shop — Dark — 18x24 — Print.pdf`

### Step 29 — Export Light edition (Page 2)

Repeat with these filenames:
- `Safety Plating Shop — Light — 24x36 — Print.pdf`
- `Safety Plating Shop — Light — Digital.pdf`
- `Safety Plating Shop — Light — 18x24 — Print.pdf`

### Export file checklist
- [ ] `Safety Plating Shop — Dark — 24x36 — Print.pdf`
- [ ] `Safety Plating Shop — Dark — 18x24 — Print.pdf`
- [ ] `Safety Plating Shop — Dark — Digital.pdf`
- [ ] `Safety Plating Shop — Light — 24x36 — Print.pdf`
- [ ] `Safety Plating Shop — Light — 18x24 — Print.pdf`
- [ ] `Safety Plating Shop — Light — Digital.pdf`

---

## Quick Reference — All Hex Codes Used

| Code | Name | Used For |
|---|---|---|
| `#1A1F2E` | Gunmetal Dark | Background (Dark), GHS icon fill, body text (Light) |
| `#F0EDE8` | Warm White | Body text (Dark), GHS diamond fill |
| `#E8A020` | Amber | Panels 3 + 4 accent |
| `#2EC4B6` | Teal | Panel 6 accent, PPE callout border |
| `#E05C5C` | Coral | Panels 1 + 2 + 5 accent, GHS diamond borders, Emergency callout |
| `#3A4055` | Mid Slate | Panel dividers, icon backgrounds |
| `#0D1020` | Deep Navy | Footer band |
| `#1E2435` | Dark Callout | Panel fills, callout fills |
| `#F5F4F0` | Off-White | Background (Light edition) |
| `#ECEEF4` | Light Callout | Panel fills (Light edition) |
| `#C8860A` | Amber Dark | Amber elements (Light edition) |
| `#1A8C82` | Teal Dark | Teal elements (Light edition) |
| `#B83E3E` | Deep Coral | Coral elements (Light edition) |
| `#D0D4DE` | Light Slate | Dividers (Light edition) |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | 2026-04-04 | Initial build prompt (Claude Chat generation). Engineered by Elara from Alaina's Construction Workup v1.0. One Watson courtesy flag open (GHS classifications) — non-blocking. |
