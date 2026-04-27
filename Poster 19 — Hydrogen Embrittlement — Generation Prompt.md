---
Project: Plating Posters Inc
Poster Number: 19
Title: "Hydrogen Embrittlement — The Invisible Threat"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-20T00:00:00
Source: Poster 19 — Hydrogen Embrittlement — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - HydrogenEmbrittlement
  - HighStrengthSteel
  - Baking
  - v1
---

# Claude Chat Generation Prompt — Poster #19
## Hydrogen Embrittlement — The Invisible Threat
### Version 1.0 | Dark Edition (Primary) + Light Edition (Remap)

*Originally engineered by Elara from Alaina's Construction Workup v1.0. Adapted for Claude chat visual generation (2026-04-20). All technical content production-ready.*

---

**Workflow: Claude Chat Visual Generation**

> **IMPORTANT:** This poster is to be generated as a visual artifact in claude.ai chat (SVG or HTML recommended). Do NOT use any external design tools. Generate the poster visually in the chat as a complete SVG or HTML artifact.

**Instructions for Claude:**

- Generate this poster as a **complete visual artifact** — either SVG or HTML with inline CSS.
- The poster is **24 x 36 inches** (portrait orientation). Design at this aspect ratio.
- Produce the **Dark edition first**. Light edition remap table provided at the end.
- Follow all specifications exactly. Every hex code, font, and size is intentional.
- Prioritize **readability at distance** — 3-8 feet on a shop wall.

---

## Phase 1 — Design Foundation

### Artboard
- **Size:** 24 x 36 inches (portrait)
- **Background color (Dark edition):** `#1A1F2E` (Gunmetal Dark)

### Typography
| Role | Font | Weight | Notes |
|------|------|--------|-------|
| Headlines | Barlow Condensed | ExtraBold (800) | All caps, letter-spacing -4 |
| Subheadings | Barlow | SemiBold (600) | Title case |
| Body text | Inter | Regular (400) / Medium (500) | Sentence case |
| Data/formulas | JetBrains Mono | Regular (400) | Monospace for Rc values, ASTM numbers |

### Brand Colors (Dark Edition)

| Name | Hex | Role |
|------|-----|------|
| Gunmetal Dark | `#1A1F2E` | Background |
| Warm White | `#F0EDE8` | Body text |
| Amber | `#E8A020` | Danger zone (Rc 36-43), bake-required warnings |
| Teal | `#2EC4B6` | Bake parameters, callout borders |
| Emerald | `#27AE60` | Safe zone (Rc < 35), "not susceptible" indicators |
| Coral | `#E05C5C` | Prohibited zone (Rc > 43), critical warnings, susceptible materials |
| Mid Slate | `#3A4055` | Scale body, dividers, table headers |
| Deep Navy | `#0D1020` | Footer band |
| Dark Callout | `#1E2435` | Card fills |
| Alt Row | `#252B3D` | Alternate row backgrounds |
| Bright Silver | `#C8D0D8` | Steel substrate icon fills |

### Layout Safe Zones
- **0.5" margin** on all sides

---

## Phase 2 — Zone 1: Header Band

### Step 6 — Headline
- Text: `HYDROGEN EMBRITTLEMENT`
- Font: Barlow Condensed ExtraBold, `88` pt, `#F0EDE8`, letter spacing `-4`. X: **0.5"**, Y: **0.5"**.

### Step 7 — Subheading
- Text: `The Invisible Threat`
- Font: Barlow SemiBold, `40` pt, `#E05C5C` (Coral). X: **0.5"**, Y: **1.5"**.

### Step 8 — Tagline
- Text: `Parts pass every visual inspection — and then break catastrophically in service.`
- Font: Barlow SemiBold, `22` pt, `#F0EDE8` at 65%. X: **0.5"**, Y: **2.2"**.

---

## Phase 3 — Zone 2: Hardness Scale + Bake Parameters

Y: 2.9" to 22.5" (~19.6" tall). Two-column layout.

### Step 9 — Section label (left column)
- Text: `SUSCEPTIBILITY ZONES`
- Font: Barlow Condensed ExtraBold, `24` pt, `#F0EDE8`, Center. X: **0.5"**, Width: **10.5"**, Y: **3.1"**.

### Step 10 — Sub-label
- Text: `Rockwell C hardness — also approx. tensile strength (psi)`
- Font: Inter Regular, `14` pt, `#F0EDE8` at 60%, Center. X: **0.5"**, Width: **10.5"**, Y: **3.7"**.

### Step 11 — Rockwell C Hardness Scale (HERO)

The scale runs from Rc 25 (bottom, safe) to Rc 50 (top, prohibited). Total scale height: ~17.5". Y range: 4.3" (top, Rc 50) to 21.8" (bottom, Rc 25). X: **4.0"**, W: **3.5"**.

**11a — Scale body container:**
- Rectangle, X: **4.0"**, Y: **4.3"**, W: `3.5"`, H: `17.5"`, fill `#3A4055`, border 2 pt `#F0EDE8`.

**11b — Three colored zones (overlaid on scale body):**

1. **Prohibited zone (Rc 43-50, top):**
   - Rectangle, X: **4.0"**, Y: **4.3"**, W: `3.5"`, H: `4.9"`, fill `#E05C5C` (Coral).

2. **Danger zone (Rc 36-43):**
   - Rectangle, X: **4.0"**, Y: **9.2"**, W: `3.5"`, H: `4.9"`, fill `#E8A020` (Amber).

3. **Safe zone (Rc 25-35):**
   - Rectangle, X: **4.0"**, Y: **14.1"**, W: `3.5"`, H: `7.7"`, fill `#27AE60` (Emerald).

**11c — Threshold lines:**
- **Rc 43 line:** Line from X: **3.7"** to **7.8"**, Y: **9.2"**, stroke 3 pt, `#F0EDE8`.
- **Rc 35 line:** Line from X: **3.7"** to **7.8"**, Y: **14.8"**, stroke 3 pt, `#F0EDE8`.

**11d — Scale tick marks and Rc labels (left side, X: 3.0" to 3.9"):**

JetBrains Mono Regular, `16` pt, `#F0EDE8`. Small horizontal tick at each value.

| Rc Value | Y Position | Label Style |
|---|---|---|
| 50 | 4.3" | `Rc 50` — standard |
| 43 | 9.2" | `Rc 43` — Coral, bold |
| 40 | 11.0" | `Rc 40` — standard |
| 36 | 13.7" | `Rc 36` — Amber, bold |
| 35 | 14.8" | `Rc 35` — Emerald, bold — THRESHOLD |
| 30 | 17.6" | `Rc 30` — standard |
| 25 | 21.8" | `Rc 25` — standard |

**11e — Tensile strength sub-labels (right side, X: 7.8" to 10.5"):**

JetBrains Mono Regular, `13` pt, `#F0EDE8` at 70%.

- Y: 4.3": `~250,000 psi`
- Y: 9.2": `~210,000 psi`
- Y: 14.8": `~170,000 psi (threshold)`
- Y: 21.8": `~120,000 psi`

**11f — Zone labels (centered inside each zone):**

1. **Prohibited zone label (~Y 6.7"):**
   - Barlow Condensed ExtraBold, `22` pt, `#F0EDE8`, centered.
   - Line 1: `PROHIBITED`
   - Line 2: `(some processes not allowed)`
   - Sub-line: Inter Regular, `12` pt: `Use mechanical Zn or non-electrolytic methods`

2. **Danger zone label (~Y 11.6"):**
   - Barlow Condensed ExtraBold, `22` pt, `#1A1F2E` (dark text on amber).
   - `BAKING MANDATORY`
   - Sub-line: Inter Medium, `12` pt, `#1A1F2E`: `Bake within spec window after plating`

3. **Safe zone label (~Y 18.0"):**
   - Barlow Condensed ExtraBold, `22` pt, `#1A1F2E`.
   - `LOW RISK`
   - Sub-line: Inter Medium, `12` pt, `#1A1F2E`: `Below the susceptibility threshold`

### Step 12 — Mechanism Callout (right column, Block C)

Y: 3.1" to 8.0".

**12a — Container:**
- Rounded rectangle, X: **12.0"**, Y: **3.1"**, W: `11.5"`, H: `4.9"`, fill `#1E2435`, radius `8`.
- Left accent: `0.06"` x `4.9"`, fill `#E05C5C` (Coral).

**12b — Title:** `HOW IT HAPPENS` — Barlow SemiBold, `22` pt, `#E05C5C`. X: **12.3"**, Y: **3.3"**.

**12c — Body (4 numbered steps):**
- Font: Inter Regular, `16` pt, `#F0EDE8`, line height 150%. X: **12.3"**, Y: **3.9"**, Width: `11.0"`.
- Text:
  1. Hydrogen is generated at the cathode during plating (or pickling, or cleaning).
  2. Atomic hydrogen diffuses INTO the steel — much faster than it can escape.
  3. Hydrogen concentrates at stress points, crack tips, and inclusions.
  4. Under load, the embrittled steel fractures suddenly — often hours or days later.

### Step 13 — Bake Parameter Cards (right column, Block D)

Y: 8.4" to 22.0". Four cards stacked vertically.

**Card template (used for all four):**
- Rounded rectangle, X: **12.0"**, W: `11.5"`, H: `3.0"`, fill `#1E2435`, radius `6`.
- Left accent: `0.06"` x `3.0"`, fill `#2EC4B6` (Teal).
- Title: Barlow SemiBold, `20` pt, `#2EC4B6`, X: **12.3"**, top of card + 0.2".
- Big number: Barlow Condensed ExtraBold, `60` pt, `#F0EDE8`, X: **12.3"**, below title.
- Unit/sub-text: JetBrains Mono Regular, `16` pt, `#F0EDE8` at 70%, beside or below number.
- Caption: Inter Regular, `13` pt, `#F0EDE8` at 75%, italic, bottom of card.

**Card 1 — Temperature** (Y: **8.4"**)
- Title: `BAKE TEMPERATURE`
- Big number: `375 °F`
- Sub-text: `± 25 °F`
- Caption: `Standard for cadmium and most plated high-strength steel.`

**Card 2 — Time** (Y: **11.7"**)
- Title: `BAKE TIME`
- Big number: `23 hours`
- Sub-text: `minimum (Cd plate, ASTM B766)`
- Caption: `Other deposits: 3–24 hours per spec. Always check the relevant standard.`

**Card 3 — Bake Window** (Y: **15.0"**)
- Title: `BAKE START WINDOW`
- Big number: `1–4 hours`
- Sub-text: `after plating (per spec)`
- Caption: `Delay = hydrogen migrates deeper. Start the oven within the spec window.`

**Card 4 — Sequence Rule** (Y: **18.3"**)
- Title: `SEQUENCE RULE`
- Big number: `BAKE FIRST`
- Sub-text: `THEN chromate`
- Caption: `Chromate conversion ALWAYS follows baking — never precedes it.`

### Step 14 — Group all of Zone 2

---

## Phase 4 — Zone 3: Susceptible Materials

Y: 22.5" to 28.5" (~6.0" tall).

### Step 15 — Section label
- Text: `WHAT'S AT RISK`
- Font: Barlow Condensed ExtraBold, `28` pt, `#F0EDE8`, Center. Y: **22.7"**.

### Step 16 — Two-column callout (Block E)

**16a — Left column — Susceptible:**

Container:
- Rounded rectangle, X: **0.5"**, Y: **23.4"**, W: `11.2"`, H: `4.6"`, fill `#1E2435`, radius `6`.
- Left accent: `0.06"` x `4.6"`, fill `#E05C5C`.

Title: `SUSCEPTIBLE — BAKE REQUIRED` — Barlow SemiBold, `22` pt, `#E05C5C`. X: **0.8"**, Y: **23.6"**.

Bullet list — Inter Regular, `18` pt, `#F0EDE8`, line height 150%. X: **0.8"**, Y: **24.2"**, Width: `10.6"`:
- Martensitic stainless steels (400-series at high hardness)
- Precipitation-hardening (PH) stainless steels
- High-strength low-alloy carbon steels (4140, 4340, 8620 above Rc 35)
- High-strength fasteners (Grade 8, A574, MS21250)
- Spring steels and music wire
- Quenched and tempered tool steels

**16b — Right column — Not susceptible:**

Container:
- Rounded rectangle, X: **12.0"**, Y: **23.4"**, W: `11.5"`, H: `4.6"`, fill `#1E2435`, radius `6`.
- Left accent: `0.06"` x `4.6"`, fill `#27AE60`.

Title: `NOT SUSCEPTIBLE — NO BAKE NEEDED` — Barlow SemiBold, `22` pt, `#27AE60`. X: **12.3"**, Y: **23.6"**.

Bullet list — Inter Regular, `18` pt, `#F0EDE8`, line height 150%. X: **12.3"**, Y: **24.2"**, Width: `10.9"`:
- Austenitic stainless steels (300-series, FCC structure)
- Copper and copper alloys (brass, bronze)
- Aluminum and aluminum alloys
- Nickel and nickel alloys (in most service conditions)
- Low-strength carbon steels (below Rc 35 / 170,000 psi)
- Magnesium

### Step 17 — Group all of Zone 3

---

## Phase 5 — Zone 4: Verification Tests

Y: 28.5" to 32.5" (~4.0" tall).

### Step 18 — Verification callout (Block F)

**18a — Container:**
- Rounded rectangle, X: **0.5"**, Y: **28.7"**, W: `23.0"`, H: `3.6"`, fill `#1E2435`, radius `8`.
- Left accent: `0.06"` x `3.6"`, fill `#E8A020` (Amber).

**18b — Title:** `PROCESS VERIFICATION TESTS` — Barlow SemiBold, `22` pt, `#E8A020`. X: **0.8"**, Y: **28.9"**.

**18c — Two-column body:**

Left half (X: **0.8"** to **11.5"**):
- Font: Inter Regular, `16` pt, `#F0EDE8`, line height 145%. X: **0.8"**, Y: **29.5"**, Width: `10.5"`.
- Text:

> **ASTM F519 — Static Load Test**
> Notched-bar specimens loaded to 75% of notched fracture strength for **200 hours**. Used to qualify the plating process before production. The reference test for aerospace and DOD specs.

Right half (X: **12.5"** to **23.5"**):
- Font: Inter Regular, `16` pt, `#F0EDE8`, line height 145%. X: **12.5"**, Y: **29.5"**, Width: `10.5"`.
- Text:

> **ASTM F1940 — Step Load Test**
> Faster method (< 24 hours). Specimens are loaded in increasing steps until failure. Used for production lot verification when speed matters more than absolute correlation to F519.

**18d — Bottom warning bar:**
- Font: Inter Medium, `14` pt, `#E05C5C`, Center. X: **0.8"**, Y: **31.7"**, Width: `22.4"`.
- Text: `Verification tests qualify the PROCESS — they do not catch a single bad part. Process control is the only protection.`

### Step 19 — Group all of Zone 4

---

## Phase 6 — Zone 5: Footer Band

### Step 20 — Footer band
- Rectangle. W: `24.0"`. H: `3.5"`. Fill: `#0D1020`. X: **0"**, Y: **32.5"**.

### Step 21 — Disclaimer
- Text: `Bake parameters shown are typical for cadmium plate per ASTM B766. Other deposits and end-use specifications (NADCAP, AMS-2759, MIL-STD) may require different temperatures, times, or windows. Always follow the controlling specification for your part.`
- Font: Inter Regular, `11` pt, `#F0EDE8` at 50%, Center. X: **0.5"**, Y: **32.8"**.

### Step 22 — Poster title
- Text: `Hydrogen Embrittlement — The Invisible Threat`
- Font: Barlow SemiBold, `16` pt, `#F0EDE8`. X: **0.5"**, Y: **33.5"**.

### Step 23 — Series name, logo, version
- Series: `Plating Posters Inc — Metal Finishing Reference Series` — Inter Regular, `14` pt, `#F0EDE8` at 70%, Center. Y: **34.2"**.
- Logo: Rectangle `0.83"` x `0.42"`, fill `#3A4055`. Text: `[LOGO]`. X: **22.5"**, Y: **33.3"**.
- Version: `v1.0 — 2026` — JetBrains Mono Regular, `11` pt, `#F0EDE8` at 50%. X: **0.5"**, Y: **35.0"**.

---

## Phase 7 — Final Review Checklist

- [ ] Headline: `HYDROGEN EMBRITTLEMENT` at 88 pt
- [ ] Rockwell C hardness scale present with three colored zones (Emerald safe, Amber danger, Coral prohibited)
- [ ] Threshold lines at Rc 35 and Rc 43 with tick marks at Rc 25, 30, 35, 36, 40, 43, 50
- [ ] Tensile strength sub-labels on right side of scale
- [ ] Zone labels centered inside each colored zone with dark text on Amber/Emerald
- [ ] Mechanism callout: 4 numbered steps explaining how HE happens
- [ ] Four bake parameter cards: Temperature (375 °F), Time (23 hours), Window (1-4 hours), Sequence (Bake First)
- [ ] Two-column susceptible vs. not susceptible materials callout
- [ ] Verification tests: ASTM F519 and F1940 with bottom warning bar
- [ ] All text within safe zone; footer complete

---

## Phase 8 — Light Edition: Remap

| Change From | Change To |
|---|---|
| `#1A1F2E` | `#F5F4F0` |
| `#F0EDE8` | `#1A1F2E` |
| `#1E2435` | `#ECEEF4` |
| `#252B3D` | `#E8E8F0` |
| `#0D1020` | `#1A1F2E` |
| `#E8A020` | `#C8860A` |
| `#2EC4B6` | `#1A8C82` |
| `#27AE60` | `#1E7A47` |
| `#E05C5C` | `#B83E3E` |
| `#3A4055` | `#D0D4DE` |
| `#C8D0D8` | `#C8D0D8` |

**Light edition override:** In the Dark edition, the Amber zone uses dark text (`#1A1F2E`) on Amber fill. In the Light edition, the darkened Amber (`#C8860A`) may not contrast well with `#1A1F2E` text — verify and switch to `#F5F4F0` text if needed. Same check for Emerald zone label.

---

## Phase 9 — Export

### Export file checklist
- [ ] `Hydrogen Embrittlement — Dark — 24x36 — Print.pdf`
- [ ] `Hydrogen Embrittlement — Dark — 18x24 — Print.pdf`
- [ ] `Hydrogen Embrittlement — Dark — Digital.pdf`
- [ ] `Hydrogen Embrittlement — Light — 24x36 — Print.pdf`
- [ ] `Hydrogen Embrittlement — Light — 18x24 — Print.pdf`
- [ ] `Hydrogen Embrittlement — Light — Digital.pdf`

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | 2026-04-20 | Initial build prompt. Engineered by Elara from Alaina's Construction Workup v1.0. |
