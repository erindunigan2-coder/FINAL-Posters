---
Project: Plating Posters Inc
Poster Number: 587
Title: "Gas Nitriding -- Safety & PPE"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 4: Gas Nitriding, Section 4.2)"
Technical Source: Safety and personal protective equipment requirements for gas nitriding operations. Ammonia (NH3) is the primary hazard -- OSHA PEL 50 ppm TWA, IDLH 300 ppm. Hydrogen from dissociated ammonia creates fire/explosion risk. All values per OSHA 29 CFR 1910 and NFPA standards.
Process Scope: Gas nitriding -- safety and PPE (Stage 2 deep-dive)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - GasNitriding
  - Safety
  - PPE
  - ConstructionWorkup
  - DiffusionHeatTreatment
---

# Poster #587 -- Construction Workup
## Gas Nitriding -- Safety & PPE

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This poster covers every safety hazard and PPE requirement for gas nitriding operations. The primary hazard is anhydrous ammonia -- toxic, corrosive, and lighter than air. Secondary hazard is hydrogen from ammonia dissociation -- flammable and explosive. This poster hangs next to the furnace so operators see it every shift.

Design philosophy: high-contrast safety-first layout. Coral and Amber dominate over Emerald and Teal. Hazard panels are large and unmissable. PPE checklist is scannable at 6 feet. Emergency response procedures are in a highlighted callout box.

---

## Part 1 -- Workflow Orientation

### Design Capabilities for This Poster

- Text boxes with precise font, size, weight, color, and spacing control
- Solid-color rectangles and rounded rectangles for hazard panels, PPE checklist boxes, and accent borders
- Color fills set to exact hex values
- Background page color set to exact hex
- Export at print-quality PDF (300 DPI equivalent via print export)

### Limitations to Flag

1. **Hazard panels (Block B -- HERO):** Four large hazard cards arranged in a 2x2 grid covering ammonia toxicity, hydrogen flammability, burn risk, and cylinder handling.

2. **PPE checklist (Block D):** Vertical checklist of required protective equipment with icons described in text.

3. **Emergency response callout (Block E):** Full-width highlighted panel with ammonia release and hydrogen accumulation procedures.

4. **Exposure limits table (Block C):** Compact reference table for OSHA/NIOSH limits.

5. **4 pt left-border accents on callout boxes.**

6. **Global Colors / swatch remap for Light edition.**

7. **Print size -- 24x36".**

---

## Part 2 -- Document Setup Instructions

### Step 1 -- Create the document
- Width: **24 inches**. Height: **36 inches**.

### Step 2 -- Set the background color
- **`#1A1F2E`** (Gunmetal Dark)

### Step 3 -- Upload fonts
- **Barlow Condensed ExtraBold** -- all headlines and section labels
- **Barlow SemiBold** -- all subheadings, callout titles
- **Inter Regular** and **Inter Medium** -- all body text, table data, and descriptions
- **JetBrains Mono Regular** -- all parameter data, chemical formulas, concentration ranges, version number

If JetBrains Mono upload fails, substitute **Courier Prime**.

### Step 4 -- Set up color palette

| Color Name | Hex | Primary Use |
|---|---|---|
| Gunmetal Dark | `#1A1F2E` | Background (Dark edition) |
| Warm White | `#F0EDE8` | All primary text (Dark edition) |
| Amber | `#E8A020` | Warning headers, caution highlights |
| Teal | `#2EC4B6` | PPE items, positive safety actions |
| Emerald | `#27AE60` | Correct procedures, safe conditions |
| Coral | `#E05C5C` | Hazards, danger callouts, exposure limits |
| Mid Slate | `#3A4055` | Table headers, dividers |
| Deep Navy | `#0D1020` | Footer band background |
| Dark Callout | `#1E2435` | Hazard card fills, PPE box fills |
| Alt Row | `#252B3D` | Alternating table rows |
| Bright Silver | `#C8D0D8` | Neutral metallic accents |

### Step 5 -- Set ruler guides

**Vertical guides (from left edge):**
- 0.5" -- left safe zone margin
- 23.5" -- right safe zone margin

**Horizontal guides (from top edge):**
- 0.5" -- top safe zone margin
- 2.9" -- Zone 1/Zone 2 boundary
- 14.5" -- Zone 2/Zone 3 boundary
- 18.0" -- Zone 3/Zone 4 boundary
- 25.5" -- Zone 4/Zone 5 boundary
- 32.5" -- Zone 5/Zone 6 boundary
- 35.5" -- bottom safe zone margin

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- HAZARD PANELS / HERO (2.9"--14.5" / ~11.6" tall)
  Block B: Four hazard cards (2x2 grid)

ZONE 3 -- EXPOSURE LIMITS TABLE (14.5"--18.0" / ~3.5" tall)
  Block C: Ammonia and hydrogen exposure limits reference table

ZONE 4 -- PPE CHECKLIST (18.0"--25.5" / ~7.5" tall)
  Block D: Required PPE items with descriptions

ZONE 5 -- EMERGENCY RESPONSE (25.5"--32.5" / ~7.0" tall)
  Block E: Ammonia release and hydrogen accumulation response procedures

ZONE 6 -- FOOTER BAND (32.5"--36.0" / ~3.5" tall)
  Block F: Disclaimer + poster title + series name + logo placeholder + version
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Dimensions:** Full page width. Y: 0" to 2.9".
**Background:** Same as page (`#1A1F2E`) -- no separate fill needed.

---

**BLOCK A -- Headline**

- Element type: Text box
- Position: X: 0.5". Y: 0.5"
- Width: 23.0"
- Font: Barlow Condensed ExtraBold
- Size: 88 pt
- Color: `#F0EDE8`
- Letter spacing: -4
- Text (all caps):

> GAS NITRIDING

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 36 pt
- Color: `#E05C5C` (Coral -- safety poster)
- Text:

> Safety & PPE -- Ammonia Hazards, Hydrogen Risk, Burn Protection

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 20 pt
- Color: `#F0EDE8` at 65%
- Text:

> Anhydrous ammonia is the primary process gas. It is toxic, corrosive, and lighter than air. Know the hazards. Wear the gear. Follow the procedures.

---

### ZONE 2 -- Hazard Panels (HERO)

**Dimensions:** Full page width within margins. Y: 2.9" to 14.5" (~11.6" tall).

---

**Section label:**
- Centered horizontally. Y: 3.1"
- Font: Barlow Condensed ExtraBold, 28 pt, `#E05C5C`, Center
- Text:

> KNOW YOUR HAZARDS

---

**BLOCK B -- Four Hazard Cards (2x2 Grid)**

Y: 3.8" to 14.3". Two columns, two rows. Gap: 0.4".

Each card: Rounded rect, W: 11.1", H: 4.9", fill `#1E2435`, radius 8, top accent 4 pt.

**Row 1 (Y: 3.8" to 8.7"):**

*Card 1 -- Ammonia Toxicity (X: 0.5"):*
- Top accent: `#E05C5C` (Coral)
- Title: `AMMONIA (NH3) -- TOXIC & CORROSIVE` -- Barlow SemiBold, 22 pt, `#E05C5C`

Content (Inter Regular, 14 pt, `#F0EDE8`, line height 170%):
```
OSHA PEL: 50 ppm TWA (8-hour average)
IDLH: 300 ppm (immediately dangerous to life)
Detectable by smell at 5--25 ppm
Causes severe respiratory irritation and chemical burns
Corrosive to eyes, skin, and mucous membranes
LIGHTER THAN AIR -- accumulates at CEILING height
```

Key data callout (JetBrains Mono, 13 pt, `#E05C5C`):
```
NH3 detection system REQUIRED at all nitriding installations
Ventilate from TOP of building (NH3 rises)
```

*Card 2 -- Hydrogen Flammability (X: 11.9"):*
- Top accent: `#E8A020` (Amber)
- Title: `HYDROGEN (H2) -- FLAMMABLE & EXPLOSIVE` -- Barlow SemiBold, 22 pt, `#E8A020`

Content:
```
Dissociated ammonia leaving furnace contains H2
H2 LEL: 4% in air (wide flammability range to 75%)
H2 flame is nearly invisible in daylight
Burn-off pilot at exhaust is MANDATORY
Pilot failure = H2 accumulation = explosion risk
```

Key data callout (JetBrains Mono, 13 pt, `#E8A020`):
```
BURN-OFF PILOT MUST BE LIT whenever NH3 is flowing
Verify pilot before every cycle start
```

**Row 2 (Y: 9.3" to 14.2"):**

*Card 3 -- Thermal / Burn Hazards (X: 0.5"):*
- Top accent: `#E8A020` (Amber)
- Title: `THERMAL HAZARDS -- FURNACE BURNS` -- Barlow SemiBold, 22 pt, `#E8A020`

Content:
```
Furnace operating temperature: 925--1050 F (496--566 C)
Lower than carburizing -- but still causes severe burns
Parts remain hot during 40--90 hour cycles
Loading/unloading requires full thermal PPE
Retort and fixtures are at furnace temperature
```

Key data callout (JetBrains Mono, 13 pt, `#E8A020`):
```
Lower temp than carburizing ≠ safe to handle
Full PPE for every load/unload operation
```

*Card 4 -- Ammonia Cylinder Handling (X: 11.9"):*
- Top accent: `#E05C5C` (Coral)
- Title: `CYLINDER HANDLING -- ANHYDROUS NH3` -- Barlow SemiBold, 22 pt, `#E05C5C`

Content:
```
Store cylinders UPRIGHT with protective caps
Keep away from heat sources and direct sunlight
Never use copper fittings (NH3 corrodes copper/brass)
Chain cylinders to prevent falling
Verify regulator is rated for ammonia service
OSHA 29 CFR 1910.111 applies to NH3 storage
```

Key data callout (JetBrains Mono, 13 pt, `#E05C5C`):
```
Emergency eyewash/shower within 10 seconds
of ammonia use area (OSHA 29 CFR 1910.151)
```

---

### ZONE 3 -- Exposure Limits Table

**Dimensions:** Y: 14.5" to 18.0" (~3.5" tall).

---

**Section label:**
- Centered. Y: 14.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`

> AMMONIA EXPOSURE LIMITS -- QUICK REFERENCE

---

**BLOCK C -- Exposure Limits Table**

Y: 15.3" to 17.8". Column widths (23.0" total):
- Standard (4.0") | Limit Type (5.0") | Value (3.5") | Action Required (10.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.5".

| Standard | Limit Type | Value | Action Required |
|---|---|---|---|
| OSHA PEL | TWA (8 hr) | 50 ppm | Maximum allowable average exposure |
| OSHA STEL | Short-term (15 min) | 35 ppm | Maximum 15-min peak |
| NIOSH REL | TWA (10 hr) | 25 ppm | Recommended limit (more conservative) |
| NIOSH | IDLH | 300 ppm | Immediately dangerous -- evacuate; SCBA required |
| Odor threshold | Detection | 5--25 ppm | If you smell it, levels may already exceed REL |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Limit values: `#E05C5C` for emphasis.

---

### ZONE 4 -- PPE Checklist

**Dimensions:** Y: 18.0" to 25.5" (~7.5" tall).

---

**Section label:**
- Centered. Y: 18.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> REQUIRED PERSONAL PROTECTIVE EQUIPMENT

---

**BLOCK D -- PPE Items**

Y: 18.9" to 25.3". Two columns of PPE items.

Each item: Rounded rect, W: 11.0", H: 1.9", fill `#1E2435`, radius 6, left accent 4 pt `#2EC4B6`.

**Left Column (X: 0.5"):**

*Item 1 (Y: 18.9"):*
- Title: `AMMONIA-RATED RESPIRATOR` -- Barlow SemiBold, 18 pt, `#2EC4B6`
- Detail: `Full-face respirator with NIOSH-approved chemical cartridge for NH3. Required when levels may exceed PEL.` -- Inter Regular, 13 pt, `#F0EDE8`
- Note: `Emergency SCBA accessible within 30 seconds` -- Inter Medium, 12 pt, `#E05C5C`

*Item 2 (Y: 21.0"):*
- Title: `CHEMICAL SPLASH GOGGLES` -- Barlow SemiBold, 18 pt, `#2EC4B6`
- Detail: `Required when connecting/disconnecting ammonia cylinders or making any ammonia system connection.` -- Inter Regular, 13 pt, `#F0EDE8`
- Note: `Standard safety glasses NOT sufficient for NH3 splash` -- Inter Medium, 12 pt, `#E8A020`

*Item 3 (Y: 23.1"):*
- Title: `RUBBER OR NITRILE GLOVES` -- Barlow SemiBold, 18 pt, `#2EC4B6`
- Detail: `Chemical-resistant gloves for ammonia handling. Leather NOT suitable -- NH3 penetrates leather.` -- Inter Regular, 13 pt, `#F0EDE8`

**Right Column (X: 12.5"):**

*Item 4 (Y: 18.9"):*
- Title: `HEAT-RESISTANT PPE` -- Barlow SemiBold, 18 pt, `#2EC4B6`
- Detail: `Standard furnace loading PPE: heat gloves, face shield, FRC clothing. Lower temp than carburizing but still required.` -- Inter Regular, 13 pt, `#F0EDE8`

*Item 5 (Y: 21.0"):*
- Title: `EMERGENCY SCBA` -- Barlow SemiBold, 18 pt, `#2EC4B6`
- Detail: `Self-contained breathing apparatus accessible within 30 seconds of any ammonia use area for emergency response.` -- Inter Regular, 13 pt, `#F0EDE8`
- Note: `Required by facility emergency response plan` -- Inter Medium, 12 pt, `#E05C5C`

*Item 6 (Y: 23.1"):*
- Title: `STANDARD INDUSTRIAL PPE` -- Barlow SemiBold, 18 pt, `#2EC4B6`
- Detail: `Steel-toed boots, safety glasses with side shields, hearing protection near vacuum pumps.` -- Inter Regular, 13 pt, `#F0EDE8`

---

### ZONE 5 -- Emergency Response

**Dimensions:** Y: 25.5" to 32.5" (~7.0" tall).

---

**Section label:**
- Centered. Y: 25.7". Barlow Condensed ExtraBold, 28 pt, `#E05C5C`

> EMERGENCY RESPONSE PROCEDURES

---

**BLOCK E -- Two Emergency Panels**

Y: 26.4" to 32.3". Two panels side by side.

**Left -- Ammonia Release (X: 0.5", W: 11.0"):**
- Rounded rect, H: 5.7", fill `#1E2435`, radius 8
- Top accent: 4 pt `#E05C5C`
- Title: `AMMONIA RELEASE` -- Barlow SemiBold, 22 pt, `#E05C5C`

Steps (Inter Regular, 14 pt, `#F0EDE8`, line height 180%):
```
1. EVACUATE the area immediately
2. Approach from UPWIND only
3. Use water FOG (NOT solid stream) to knock down vapor cloud
4. Do NOT re-enter without SCBA
5. NH3 is lighter than air -- it RISES
6. Ventilate from the TOP of the building
7. Call emergency response / hazmat team
```

Highlighted note (Inter Medium, 13 pt, `#E05C5C`):
```
NH3 at 300 ppm is IDLH -- do NOT attempt rescue
without full SCBA and buddy system
```

**Right -- Hydrogen Accumulation (X: 12.5", W: 11.0"):**
- Rounded rect, H: 5.7", fill `#1E2435`, radius 8
- Top accent: 4 pt `#E8A020`
- Title: `HYDROGEN ACCUMULATION` -- Barlow SemiBold, 22 pt, `#E8A020`

Steps (Inter Regular, 14 pt, `#F0EDE8`, line height 180%):
```
1. If burn-off pilot fails during cycle:
2. SHUT OFF ammonia supply immediately
3. Purge furnace with nitrogen (N2)
4. Ventilate the area
5. Do NOT relight pilot until H2 is cleared
6. Verify < 1% H2 before relighting
7. Inspect pilot system before resuming operation
```

Highlighted note (Inter Medium, 13 pt, `#E8A020`):
```
H2 flame is nearly INVISIBLE in daylight
Use flame detector or paper test -- never assume
```

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Safety requirements shown follow OSHA 29 CFR 1910 general industry standards and NFPA guidelines. Facility-specific safety programs, local regulations, and equipment manufacturer requirements may impose additional or more stringent requirements. Consult your safety officer and applicable regulations.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Gas Nitriding -- Safety & PPE

**Series name:** Inter Regular, 14 pt, `#F0EDE8` at 70%, Center. Y: 34.2"

> Plating Posters Inc -- Metal Finishing Reference Series

**Logo placeholder:** Rectangle, X: 22.5", Y: 33.3", W: 0.83", H: 0.42", fill `#3A4055`. Text: `[LOGO]` -- Inter Regular, 10 pt, `#F0EDE8` at 50%

**Version:** JetBrains Mono Regular, 11 pt, `#F0EDE8` at 50%. X: 0.5", Y: 35.0"

> v1.0 -- 2026

---

## Part 5 -- Grouping and Naming Convention

| Group Name | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline |
| Zone 2 - Hazard Panels | Section label, four hazard cards |
| Zone 3 - Exposure Limits | Section label, limits table |
| Zone 4 - PPE Checklist | Section label, six PPE items |
| Zone 5 - Emergency Response | Section label, two emergency panels |
| Zone 6 - Footer | Footer band, disclaimer, title, series, logo, version |

---

## Part 6 -- Light Edition Color Remap Table

| Dark Hex | Light Hex | Notes |
|----------|-----------|-------|
| `#1A1F2E` | `#F5F4F0` | Background and all BG-colored elements |
| `#F0EDE8` | `#1A1F2E` | All primary text |
| `#1E2435` | `#ECEEF4` | Callout/hazard card fills |
| `#252B3D` | `#E8E8F0` | Alternate rows |
| `#0D1020` | `#1A1F2E` | Footer background |
| `#E8A020` | `#C8860A` | Amber accents |
| `#2EC4B6` | `#1A8C82` | Teal accents |
| `#27AE60` | `#1E7A47` | Emerald accents |
| `#E05C5C` | `#B83E3E` | Coral accents |
| `#3A4055` | `#D0D4DE` | Table headers, dividers |
| `#C8D0D8` | `#C8D0D8` | Bright Silver -- **unchanged** |

---

## Part 7 -- Export Checklist

| File Name | Mode | Quality | Bleed |
|---|---|---|---|
| `Gas Nitriding Safety PPE -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Nitriding Safety PPE -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Nitriding Safety PPE -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Gas Nitriding Safety PPE -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Nitriding Safety PPE -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Nitriding Safety PPE -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

Safety posters demand maximum contrast and immediate readability. Coral dominates -- it signals danger without ambiguity. The ammonia exposure limits table is the single most referenced data on this poster; operators will check it mid-shift.

The "hydrogen flame is invisible" fact is genuinely dangerous and not widely known. Give it maximum emphasis. The emergency response procedures are formatted as numbered steps because in an actual emergency, sequence matters.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #587 -- Construction Workup v1.0*
*2026-04-26*
