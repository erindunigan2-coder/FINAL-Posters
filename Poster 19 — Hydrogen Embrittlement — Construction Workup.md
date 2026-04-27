---
Project: Plating Posters Inc
Poster Number: 19
Title: "Hydrogen Embrittlement — The Invisible Threat"
Document Type: Construction Workup
Status: v1.0 — Ready for Elara
Created: 2026-04-06T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Tyler — New Poster Concepts from CEF — 2026-04-06.md (Concept 19)"
Technical Source: Tyler research brief (Rc thresholds, bake parameters, ASTM B766/F519/F1940, susceptible materials)
Watson Flags: ONE OPEN — Confirm bake time/temperature for non-cadmium deposits per relevant ASTM specifications (current revisions). Tyler used cadmium-specific values from B766; other deposits may differ. Non-blocking; cadmium values clearly attributed.
Tyler Flags: NONE — content drawn directly from Tyler's brief.
Process Scope: Hydrogen embrittlement relief (high-strength steel plating)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow: Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - HydrogenEmbrittlement
  - HighStrengthSteel
  - Baking
  - ConstructionWorkup
---

# Poster # Poster #19 — Construction Workup
## Hydrogen Embrittlement — The Invisible Threat

*Alaina — Plating Posters Inc Creative Lead*
*v1.0 — 2026-04-06*

This document is the construction workup for Poster #19. The hero element is a vertical Rockwell C hardness scale showing the susceptibility threshold (Rc 35), the danger zone (Rc 36–43), and the prohibition zone (above Rc 43). The poster is aimed at aerospace fastener shops, military hardware platers, and any shop running high-strength steel. One Watson flag remains open (non-cadmium bake parameters) — non-blocking; cadmium values are clearly attributed to ASTM B766.

> **Workflow update (2026-04-14):** Poster generation now uses claude.ai chat (SVG/HTML visual artifacts) These specs feed the Claude Chat Generation Prompt. If Drew approves the generated output, it proceeds to final production.

**Content source:** Tyler — New Poster Concepts from CEF — 2026-04-06.md (Concept 19).

---

## Part 1 — Workflow Orientation

### Design Capabilities for This Poster

- Text boxes with precise font, size, weight, color, and spacing control
- Solid-color rectangles for the hardness scale, callout boxes, and parameter cards
- Rounded rectangles for callout boxes and the bake parameter "stack"
- Line elements with arrowheads for hardness threshold indicators
- Color fills set to exact hex values
- Background page color set to exact hex
- Icon library search for warning, oven, fastener icons
- Export at print-quality PDF (300 DPI equivalent via print export)

### Limitations to Flag for Elara

1. **Vertical Rockwell C hardness scale (Block B — HERO):** Built as a tall vertical rectangle (the scale body) divided into three colored zones — Emerald (safe), Amber (danger/baking required), Coral (prohibited). Tick marks and labels for Rc 25, 30, 35, 36, 40, 43, 50. Threshold lines (red horizontal rules) at Rc 35 and Rc 43. Straightforward .

2. **Bake parameter card stack (Block D):** Four parameter cards stacked vertically — Temperature, Time, Bake Window, Sequence Rule. Each card uses the same template. Build one, duplicate three times.

3. **4 pt left-border accents on callout boxes:** Same technique as all previous posters.

4. **Susceptible materials list (Block E):** Two-column callout — left column "Susceptible," right column "Not susceptible." Built as standard two-column callout with bullet lists.

5. **Global Colors / swatch remap for Light edition:** Manual recolor required.

6. **JetBrains Mono font:** The generation tool may not include JetBrains Mono natively. Ensure font is available. Substitute Courier Prime if unavailable.

7. **Print size — 24x36":** Set to exactly 24 inches wide by 36 inches tall.

---

## Part 2 — Document Setup Instructions

### Step 1 — Create the document
- Width: **24 inches**. Height: **36 inches**.

### Step 2 — Set the background color
- Page background: **`#1A1F2E`** (Gunmetal Dark)

### Step 3 — Upload fonts (the Pro tier required)
- Barlow Condensed ExtraBold, Barlow SemiBold, Inter Regular/Medium, JetBrains Mono Regular

### Step 4 — Set up color palette (save as Brand Colors)

| Color Name | Hex | Primary Use |
|---|---|---|
| Gunmetal Dark | `#1A1F2E` | Background |
| Warm White | `#F0EDE8` | Primary text |
| Amber | `#E8A020` | Danger zone (Rc 36-43), bake-required warnings |
| Teal | `#2EC4B6` | Bake parameters, callout borders |
| Emerald | `#27AE60` | Safe zone (Rc < 35), "not susceptible" indicators |
| Coral | `#E05C5C` | Prohibited zone (Rc > 43), critical warnings, susceptible materials |
| Mid Slate | `#3A4055` | Scale body, dividers, table headers |
| Deep Navy | `#0D1020` | Footer band background |
| Dark Callout | `#1E2435` | Callout fills |
| Alt Row | `#252B3D` | Alternate row backgrounds |
| Bright Silver | `#C8D0D8` | Steel substrate icon fills |

### Step 5 — Set ruler guides

**Vertical guides:**
- 0.5" — left safe zone
- 11.5" — Zone 2 left/right column split
- 23.5" — right safe zone

**Horizontal guides:**
- 0.5" — top safe zone
- 2.9" — Zone 1/Zone 2 boundary
- 22.5" — Zone 2/Zone 3 boundary
- 28.5" — Zone 3/Zone 4 boundary
- 32.5" — Zone 4/Zone 5 boundary
- 35.5" — bottom safe zone margin

---

## Part 3 — Layout Zones and Build Order

```
ZONE 1 — HEADER BAND (0"–2.9")
  Block A: Headline + subheading + tagline

ZONE 2 — HARDNESS SCALE + BAKE PARAMETERS (2.9"–22.5" / ~19.6" tall)
  LEFT COLUMN (X: 0.5"–11.0"): Rockwell C hardness scale (HERO)
  RIGHT COLUMN (X: 12.0"–23.5"):
    Block C: "How it happens" mechanism callout
    Block D: Four bake parameter cards (Temperature, Time, Window, Sequence)

ZONE 3 — SUSCEPTIBLE MATERIALS (22.5"–28.5" / ~6.0" tall)
  Block E: Two-column susceptible vs. not susceptible callout

ZONE 4 — VERIFICATION TESTS (28.5"–32.5" / ~4.0" tall)
  Block F: Full-width callout — ASTM F519 and F1940 tests

ZONE 5 — FOOTER BAND (32.5"–36.0" / ~3.5" tall)
  Block G: Disclaimer + poster title + series name + logo placeholder + version
```

---

## Part 4 — Zone-by-Zone Build Specifications

### ZONE 1 — Header Band

**Dimensions:** Y: 0" to 2.9".

**BLOCK A — Headline**
- Position: X: 0.5". Y: 0.5". Width: 23.0"
- Font: Barlow Condensed ExtraBold, 88 pt, `#F0EDE8`
- Letter spacing: -4
- Text:

> HYDROGEN EMBRITTLEMENT

**BLOCK A — Subheading**
- Position: X: 0.5". Y: 1.5". Width: 23.0"
- Font: Barlow SemiBold, 40 pt, `#E05C5C` (Coral)
- Text:

> The Invisible Threat

**BLOCK A — Tagline**
- Position: X: 0.5". Y: 2.2". Width: 23.0"
- Font: Barlow SemiBold, 22 pt, `#F0EDE8` at 65%
- Text:

> Parts pass every visual inspection — and then break catastrophically in service.

---

### ZONE 2 — Hardness Scale + Bake Parameters

**Dimensions:** Y: 2.9" to 22.5" (~19.6" tall). Two-column layout.

---

#### LEFT COLUMN — Rockwell C Hardness Scale (HERO)

X: 0.5" to 11.0". Y: 3.1" to 22.0".

**Section label:**
- Position: X: 0.5". Y: 3.1". Width: 10.5"
- Font: Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`
- Alignment: Center
- Text:

> SUSCEPTIBILITY ZONES

**Sub-label:**
- Position: X: 0.5". Y: 3.7". Width: 10.5"
- Font: Inter Regular, 14 pt, `#F0EDE8` at 60%
- Alignment: Center
- Text:

> Rockwell C hardness — also approx. tensile strength (psi)

---

**BLOCK B — Hardness Scale**

The scale runs from Rc 25 (bottom, safe) to Rc 50 (top, prohibited). Total scale height: ~17.5". Y range: 4.3" (top, Rc 50) to 21.8" (bottom, Rc 25).

**Scale body container:**
- Element type: Rectangle
- Position: X: 4.0". Y: 4.3"
- Width: 3.5". Height: 17.5"
- Fill: `#3A4055` (will be overlaid with three colored zones)
- Border: 2 pt, `#F0EDE8`

**Three colored zones (overlaid on scale body):**

1. **Prohibited zone (Rc 43–50, top):**
   - Rectangle, X: 4.0", Y: 4.3", W: 3.5", H: 4.9" (representing Rc 43-50)
   - Fill: `#E05C5C` (Coral)

2. **Danger zone (Rc 36–43):**
   - Rectangle, X: 4.0", Y: 9.2", W: 3.5", H: 4.9" (representing Rc 36-43)
   - Fill: `#E8A020` (Amber)

3. **Safe zone (Rc 25–35):**
   - Rectangle, X: 4.0", Y: 14.1", W: 3.5", H: 7.7" (representing Rc 25-35)
   - Fill: `#27AE60` (Emerald)

**Threshold lines (horizontal rules across the scale):**

- **Rc 43 line** (between Amber and Coral): Line, X: 3.7" to 7.8", Y: 9.2", stroke 3 pt, `#F0EDE8`
- **Rc 35 line** (between Emerald and Amber): Line, X: 3.7" to 7.8", Y: 14.8", stroke 3 pt, `#F0EDE8`

**Scale tick marks and Rc labels (left side of scale, X: 3.0" to 3.9"):**

For each tick: small horizontal line + JetBrains Mono Regular 16 pt label, `#F0EDE8`.

| Rc Value | Y Position | Label |
|---|---|---|
| 50 | 4.3" | `Rc 50` |
| 43 | 9.2" | `Rc 43` (Coral, bold) |
| 40 | 11.0" | `Rc 40` |
| 36 | 13.7" | `Rc 36` (Amber, bold) |
| 35 | 14.8" | `Rc 35` (Emerald, bold) — THRESHOLD |
| 30 | 17.6" | `Rc 30` |
| 25 | 21.8" | `Rc 25` |

**Tensile strength sub-labels (right side of scale, X: 7.8" to 10.5"):**

For each major threshold: JetBrains Mono Regular 13 pt, `#F0EDE8` at 70%.

- Y: 4.3": `~250,000 psi`
- Y: 9.2": `~210,000 psi`
- Y: 14.8": `~170,000 psi (threshold)`
- Y: 21.8": `~120,000 psi`

**Zone labels (large text, centered inside each zone):**

1. **Prohibited zone label (centered in Coral zone, ~Y 6.7"):**
   - Text box, Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`, centered
   - Two lines:
   - `PROHIBITED`
   - `(some processes not allowed)`
   - Sub-line: Inter Regular 12 pt: `Use mechanical Zn or non-electrolytic methods`

2. **Danger zone label (centered in Amber zone, ~Y 11.6"):**
   - Text box, Barlow Condensed ExtraBold, 22 pt, `#1A1F2E` (dark text on amber)
   - `BAKING MANDATORY`
   - Sub-line: Inter Medium 12 pt, `#1A1F2E`: `Bake within spec window after plating`

3. **Safe zone label (centered in Emerald zone, ~Y 18.0"):**
   - Text box, Barlow Condensed ExtraBold, 22 pt, `#1A1F2E`
   - `LOW RISK`
   - Sub-line: Inter Medium 12 pt, `#1A1F2E`: `Below the susceptibility threshold`

---

#### RIGHT COLUMN — Mechanism + Bake Parameters

X: 12.0" to 23.5". Y: 3.1" to 22.0".

---

**BLOCK C — Mechanism Callout**

Y: 3.1" to 8.0"

**Container:**
- Rounded rectangle, X: 12.0", Y: 3.1", W: 11.5", H: 4.9", fill `#1E2435`, radius 8 pt
- Left accent: 0.06" x 4.9", fill `#E05C5C` (Coral)

**Title:**
- Position: X: 12.3". Y: 3.3"
- Font: Barlow SemiBold, 22 pt, `#E05C5C`
- Text:

> HOW IT HAPPENS

**Body (4 numbered steps):**
- Position: X: 12.3". Y: 3.9"
- Width: 11.0"
- Font: Inter Regular, 16 pt, `#F0EDE8`
- Line height: 150%
- Text (use numbered list):

> 1. Hydrogen is generated at the cathode during plating (or pickling, or cleaning).
> 2. Atomic hydrogen diffuses INTO the steel — much faster than it can escape.
> 3. Hydrogen concentrates at stress points, crack tips, and inclusions.
> 4. Under load, the embrittled steel fractures suddenly — often hours or days later.

---

**BLOCK D — Bake Parameter Cards**

Y: 8.4" to 22.0". Four cards stacked vertically, each ~3.3" tall.

**Card template (used for all four):**
- Rounded rectangle, X: 12.0", W: 11.5", H: 3.0", fill `#1E2435`, radius 6 pt
- Left accent: 0.06" x 3.0", fill `#2EC4B6` (Teal)
- Title: Barlow SemiBold, 20 pt, `#2EC4B6`, X: 12.3", top of card + 0.2"
- Big number: Barlow Condensed ExtraBold, 60 pt, `#F0EDE8`, X: 12.3", below title
- Unit/sub-text: JetBrains Mono Regular, 16 pt, `#F0EDE8` at 70%, beside or below number
- Caption: Inter Regular, 13 pt, `#F0EDE8` at 75%, italic, bottom of card

---

**Card 1 — Temperature** (Y: 8.4")
- Title: `BAKE TEMPERATURE`
- Big number: `375 °F`
- Sub-text: `± 25 °F` (positioned beside the big number)
- Caption: `Standard for cadmium and most plated high-strength steel.`

**Card 2 — Time** (Y: 11.7")
- Title: `BAKE TIME`
- Big number: `23 hours`
- Sub-text: `minimum (Cd plate, ASTM B766)`
- Caption: `Other deposits: 3–24 hours per spec. Always check the relevant standard.`

**Card 3 — Bake Window** (Y: 15.0")
- Title: `BAKE START WINDOW`
- Big number: `1–4 hours`
- Sub-text: `after plating (per spec)`
- Caption: `Delay = hydrogen migrates deeper. Start the oven within the spec window.`

**Card 4 — Sequence Rule** (Y: 18.3")
- Title: `SEQUENCE RULE`
- Big number: `BAKE FIRST`
- Sub-text: `THEN chromate`
- Caption: `Chromate conversion ALWAYS follows baking — never precedes it.`

---

### ZONE 3 — Susceptible Materials

**Dimensions:** Y: 22.5" to 28.5" (~6.0" tall).

---

**Section label:**
- Position: Centered horizontally. Y: 22.7"
- Font: Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Alignment: Center
- Text:

> WHAT'S AT RISK

---

**BLOCK E — Two-Column Callout**

Y: 23.4" to 28.0"

**Left column — Susceptible:**

Container:
- Rounded rectangle, X: 0.5", Y: 23.4", W: 11.2", H: 4.6", fill `#1E2435`, radius 6 pt
- Left accent: 0.06" x 4.6", fill `#E05C5C`

Title:
- Position: X: 0.8". Y: 23.6"
- Font: Barlow SemiBold, 22 pt, `#E05C5C`
- Text:

> SUSCEPTIBLE — BAKE REQUIRED

Bullet list:
- Position: X: 0.8". Y: 24.2". Width: 10.6"
- Font: Inter Regular, 18 pt, `#F0EDE8`
- Line height: 150%
- Text:

> - Martensitic stainless steels (400-series at high hardness)
> - Precipitation-hardening (PH) stainless steels
> - High-strength low-alloy carbon steels (4140, 4340, 8620 above Rc 35)
> - High-strength fasteners (Grade 8, A574, MS21250)
> - Spring steels and music wire
> - Quenched and tempered tool steels

---

**Right column — Not susceptible:**

Container:
- Rounded rectangle, X: 12.0", Y: 23.4", W: 11.5", H: 4.6", fill `#1E2435`, radius 6 pt
- Left accent: 0.06" x 4.6", fill `#27AE60`

Title:
- Position: X: 12.3". Y: 23.6"
- Font: Barlow SemiBold, 22 pt, `#27AE60`
- Text:

> NOT SUSCEPTIBLE — NO BAKE NEEDED

Bullet list:
- Position: X: 12.3". Y: 24.2". Width: 10.9"
- Font: Inter Regular, 18 pt, `#F0EDE8`
- Line height: 150%
- Text:

> - Austenitic stainless steels (300-series, FCC structure)
> - Copper and copper alloys (brass, bronze)
> - Aluminum and aluminum alloys
> - Nickel and nickel alloys (in most service conditions)
> - Low-strength carbon steels (below Rc 35 / 170,000 psi)
> - Magnesium

---

### ZONE 4 — Verification Tests

**Dimensions:** Y: 28.5" to 32.5" (~4.0" tall).

---

**BLOCK F — Full-Width ASTM Verification Callout**

**Container:**
- Rounded rectangle, X: 0.5", Y: 28.7", W: 23.0", H: 3.6", fill `#1E2435`, radius 8 pt
- Left accent: 0.06" x 3.6", fill `#E8A020` (Amber)

**Title:**
- Position: X: 0.8". Y: 28.9"
- Font: Barlow SemiBold, 22 pt, `#E8A020`
- Text:

> PROCESS VERIFICATION TESTS

**Two-column body:**

Left half (X: 0.8" to 11.5"):
- Position: X: 0.8". Y: 29.5". Width: 10.5"
- Font: Inter Regular, 16 pt, `#F0EDE8`. Line height 145%.
- Text:

> **ASTM F519 — Static Load Test**
> Notched-bar specimens loaded to 75% of notched fracture strength for **200 hours**. Used to qualify the plating process before production. The reference test for aerospace and DOD specs.

Right half (X: 12.5" to 23.5"):
- Position: X: 12.5". Y: 29.5". Width: 10.5"
- Font: Inter Regular, 16 pt, `#F0EDE8`. Line height 145%.
- Text:

> **ASTM F1940 — Step Load Test**
> Faster method (< 24 hours). Specimens are loaded in increasing steps until failure. Used for production lot verification when speed matters more than absolute correlation to F519.

**Bottom warning bar:**
- Position: X: 0.8". Y: 31.7". Width: 22.4"
- Font: Inter Medium, 14 pt, `#E05C5C`
- Alignment: Center
- Text:

> Verification tests qualify the PROCESS — they do not catch a single bad part. Process control is the only protection.

---

### ZONE 5 — Footer Band

**Dimensions:** Y: 32.5" to 36.0".

**Footer band background:**
- Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:**
- Position: X: 0.5". Y: 32.8". Width: 23.0"
- Font: Inter Regular, 11 pt, `#F0EDE8` at 50%, center
- Text:

> Bake parameters shown are typical for cadmium plate per ASTM B766. Other deposits and end-use specifications (NADCAP, AMS-2759, MIL-STD) may require different temperatures, times, or windows. Always follow the controlling specification for your part.

**Poster title:**
- Position: X: 0.5". Y: 33.5"
- Font: Barlow SemiBold, 16 pt, `#F0EDE8`
- Text:

> Hydrogen Embrittlement — The Invisible Threat

**Series name:**
- Position: Centered. Y: 34.2"
- Font: Inter Regular, 14 pt, `#F0EDE8` at 70%, center
- Text:

> Plating Posters Inc — Metal Finishing Reference Series

**Logo placeholder:**
- Position: X: 22.5". Y: 33.3". W: 0.83", H: 0.42", fill `#3A4055`
- Text inside: `[LOGO]` — 10 pt, `#F0EDE8` at 50%

**Version:**
- Position: X: 0.5". Y: 35.0"
- Font: JetBrains Mono Regular, 11 pt, `#F0EDE8` at 50%
- Text:

> v1.0 — 2026

---

## Part 5 — Grouping and Naming Convention

| Group Name | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline |
| Zone 2 - Hardness Scale | Section label, sub-label, scale body, three zones, threshold lines, tick marks, labels, zone labels |
| Zone 2 - Mechanism | Block C: how-it-happens callout |
| Zone 2 - Bake Parameters | Four parameter cards |
| Zone 3 - Susceptible Materials | Section label, two callouts |
| Zone 4 - Verification Tests | Block F: ASTM F519/F1940 callout with warning bar |
| Zone 5 - Footer | Footer band, disclaimer, poster title, series name, logo placeholder, version |

**Tip:** Build Bake Parameter Card 1 fully, then duplicate three times. Each card uses the same template — only the title, big number, sub-text, and caption change.

---

## Part 6 — Light Edition Color Remap Table

| Dark Hex | Light Hex | Notes |
|----------|-----------|-------|
| `#1A1F2E` | `#F5F4F0` | Background |
| `#F0EDE8` | `#1A1F2E` | All primary text |
| `#1E2435` | `#ECEEF4` | Callout fills, parameter card fills |
| `#252B3D` | `#E8E8F0` | Alternate backgrounds |
| `#0D1020` | `#1A1F2E` | Footer strip |
| `#E8A020` | `#C8860A` | Amber zone and accents |
| `#2EC4B6` | `#1A8C82` | Teal accents |
| `#27AE60` | `#1E7A47` | Emerald zone and accents |
| `#E05C5C` | `#B83E3E` | Coral zone and accents |
| `#3A4055` | `#D0D4DE` | Scale body, dividers |
| `#C8D0D8` | `#C8D0D8` | Bright Silver — **unchanged** |

**Light edition override (Amber zone label):** In the Dark edition, the Amber zone uses dark text (`#1A1F2E`) on Amber fill. In the Light edition, the darkened Amber (`#C8860A`) may not contrast well with `#1A1F2E` text — verify and switch to `#F5F4F0` text if needed. Same check for Emerald zone label.

---

## Part 7 — Export Checklist

| File Name | Mode | Quality | Bleed + Marks |
|---|---|---|---|
| `Hydrogen Embrittlement — Dark — 24x36 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Hydrogen Embrittlement — Dark — 18x24 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Hydrogen Embrittlement — Dark — Digital.pdf` | RGB | PDF Standard | No |
| `Hydrogen Embrittlement — Light — 24x36 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Hydrogen Embrittlement — Light — 18x24 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Hydrogen Embrittlement — Light — Digital.pdf` | RGB | PDF Standard | No |

---

*Alaina — Plating Posters Inc Creative Lead*
*Poster #19 — Hydrogen Embrittlement — Construction Workup v1.0*
*2026-04-06*
