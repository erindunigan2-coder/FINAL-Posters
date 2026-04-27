---
Project: Plating Posters Inc
Poster Number: 376
Title: "Secondary Treatment -- Vibratory, Wire Brush & Laser Descaling"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster CT-5 technical reference (descaling / heavy oxide removal)"
Technical Source: Vibratory finishing, wire brushing / power tool cleaning, and laser descaling as secondary or alternative descaling methods. SSPC-SP 3 reference.
Process Scope: Secondary descaling treatments -- vibratory finishing (tumble), power tool cleaning, and emerging laser descaling
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Descaling
  - SecondaryTreatment
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT05
---

# Poster #376 -- Construction Workup
## Secondary Treatment -- Vibratory, Wire Brush & Laser Descaling

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Beyond blast cleaning and chemical descaling, three secondary methods round out the descaling toolkit: vibratory finishing (tumble descaling), power tool cleaning (wire brush, grinding), and laser descaling (the emerging technology). This poster covers when and why each is used, their limitations relative to primary methods, and whether they are sufficient for plating preparation.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Three-method comparison (Block B -- HERO):** Three tall panels -- Vibratory Finishing, Power Tool Cleaning, Laser Descaling. Similar to Poster #374's three-column approach.

2. **When-to-use decision matrix (Block D):** A compact table showing when each secondary method is appropriate and when it is not.

3. **Comparison vs. primary methods callout (Block E):** A clear statement that secondary methods are generally NOT equivalent to blast cleaning for plating.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 16.5" / 23.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- THREE SECONDARY METHODS / HERO (2.9"--16.5" / ~13.6" tall)
  Block B: Vibratory | Power Tool | Laser -- three columns

ZONE 3 -- WHEN TO USE MATRIX (16.5"--23.0" / ~6.5" tall)
  Block D: Decision matrix table

ZONE 4 -- vs. PRIMARY METHODS (23.0"--28.5" / ~5.5" tall)
  Block E: Comparison callout + limitations

ZONE 5 -- KEY TAKEAWAYS STRIP (28.5"--32.5" / ~4.0" tall)
  Block F: Four takeaway cards

ZONE 6 -- FOOTER BAND (32.5"--36.0")
  Block G: Standard footer
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `SECONDARY TREATMENT` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Vibratory Finishing, Wire Brush & Laser Descaling` -- 32 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `When blast cleaning is not an option -- or when you need to deburr and descale in one step. Know what these methods can and cannot do.` -- 20 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Three Secondary Methods (HERO)

**Section label:** Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> THREE SECONDARY DESCALING METHODS

---

**BLOCK B -- Three Columns**

Y: 3.8" to 16.0". Three side-by-side callout boxes.

| Column | X | W | Accent | Title |
|---|---|---|---|---|
| Vibratory Finishing | 0.5" | 7.33" | `#2EC4B6` | VIBRATORY FINISHING |
| Power Tool Cleaning | 8.17" | 7.33" | `#E8A020` | POWER TOOL CLEANING |
| Laser Descaling | 15.83" | 7.67" | `#27AE60` | LASER DESCALING |

Each box: Rounded rect, H: 12.0", fill `#1E2435`, radius 8, left accent 0.06".

---

*Column 1 -- Vibratory Finishing:*

Title: Barlow SemiBold, 20 pt, `#2EC4B6`.
Subtitle: `Tumble Descaling` -- 14 pt `#F0EDE8` at 50%.

Parameters (JetBrains Mono 13 pt):
```
Media: ceramic (aggressive) or
       plastic (gentle)
Compound: alkaline, pH 8--10
Water: recirculating
Time: 30 min -- 4 hours
```

How it works (Inter Regular 13 pt `#F0EDE8`):
`Parts and abrasive media tumble together in a vibratory bowl or trough. Media impacts part surface, removing scale and burrs simultaneously. Cleaning compound keeps parts clean and prevents redeposition.`

Best for (Inter Medium 13 pt `#27AE60`):
`Complex geometry where blast cannot reach. Deburring + light descaling in one step. Small to medium parts in volume.`

Limitation (Inter Regular 12 pt `#E05C5C`):
`Slow for heavy scale. Media selection must match part geometry -- oversized media skips recesses, undersized media lodges in holes.`

SSPC equivalent: `Not classified under SSPC standards. Effective for light oxide removal only.` Inter Regular 11 pt `#F0EDE8` at 60%.

---

*Column 2 -- Power Tool Cleaning:*

Title: Barlow SemiBold, 20 pt, `#E8A020`.
Subtitle: `Wire Brush, Grinding, Sanding` -- 14 pt `#F0EDE8` at 50%.

Parameters:
```
Methods: rotary wire brush, angle
grinder, flap disc, orbital sander
SSPC-SP 3: Power Tool Cleaning
SSPC-SP 11: Power Tool Cleaning
to Bare Metal (with rotary impact)
```

How it works:
`Manual or power-driven abrasive or wire tools remove loose scale, rust, and paint. Does not achieve uniform surface profile like blast cleaning.`

Best for:
`Touch-up of small areas. Non-critical applications where blast cleaning is impractical. Weld preparation.`

Limitation:
`NOT equivalent to blast cleaning for plating preparation. Leaves residual tight oxide in pits and low areas. SSPC-SP 3 allows tight scale to remain.`

WARNING callout (inside panel):
- Rounded rect, fill `#E05C5C` at 12%, border 1 pt `#E05C5C`
- `SP-3 is generally INSUFFICIENT for plating prep. If spec requires SP-5 or SP-10, power tools alone will not meet it.` -- Inter Medium 12 pt `#E05C5C`

---

*Column 3 -- Laser Descaling:*

Title: Barlow SemiBold, 20 pt, `#27AE60`.
Subtitle: `Emerging Technology` -- 14 pt `#F0EDE8` at 50%.

Parameters:
```
Method: pulsed laser ablation
Media: NONE (no abrasive)
Chemicals: NONE
Dust: minimal (fume extraction
      still required)
Speed: slow for production volume
Cost: HIGH (equipment $100K+)
```

How it works:
`Pulsed laser energy vaporizes oxide layers on metal surface. Precise, localized, no mechanical or chemical contact with substrate. Zero media consumption.`

Best for:
`Aerospace and precision applications. Where zero media embedment is required. Delicate or thin substrates. R&D and specialty shops.`

Limitation:
`Currently expensive and slow for high-volume production. Line-of-sight only (like blast). Equipment cost limits adoption to high-value applications.`

FUTURE callout:
- Rounded rect, fill `#27AE60` at 12%, border 1 pt `#27AE60`
- `Watch this space. Laser descaling costs are falling and speeds are increasing. May become mainstream for precision surface prep within 10 years.` -- Inter Medium 12 pt `#27AE60`

---

### ZONE 3 -- When-to-Use Decision Matrix

**Section label:** Centered. Y: 16.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> WHEN TO USE SECONDARY METHODS

---

**BLOCK D -- Decision Matrix Table**

Y: 17.4" to 22.8".

Column widths: Scenario (7.0") | Vibratory (5.0") | Power Tool (5.0") | Laser (6.0")

Header: `#3A4055` fill.

| Scenario | Vibratory | Power Tool | Laser |
|---|---|---|---|
| Heavy mill scale on flat steel | NOT recommended | NOT recommended | Possible but slow |
| Light oxide on complex geometry | EXCELLENT -- primary choice | Partial (accessible areas only) | Good but expensive |
| Deburring + descaling in one step | EXCELLENT | Good for edges only | Not applicable |
| Touch-up of small blast-missed areas | Possible if parts fit bowl | GOOD -- primary choice | Good for spot treatment |
| Plating preparation (SP-5 / SP-10 required) | NOT sufficient alone | NOT sufficient (SP-3 only) | Possible -- verify profile |
| Aerospace / precision parts | Good with plastic media | NOT recommended (surface damage risk) | EXCELLENT -- primary choice |

Data: Inter Regular 12 pt. "EXCELLENT" and "GOOD" in `#27AE60`. "NOT" items in `#E05C5C`. "Possible" in `#E8A020`.

---

### ZONE 4 -- vs. Primary Methods

**Section label:** Centered. Y: 23.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> SECONDARY vs. PRIMARY -- KNOW THE LIMITS

---

**BLOCK E -- Comparison Callout**

Y: 23.9" to 28.3". Full-width callout.

Rounded rect, X: 0.5", W: 23.0", H: 4.0", fill `#1E2435`, radius 8, left accent 0.06" `#E05C5C`, border 1 pt `#E05C5C` at 30%.

Title: `THE BOTTOM LINE` -- Barlow Condensed ExtraBold, 22 pt, `#E05C5C`.

Two-column content:

Left column:
- `FOR PLATING PREPARATION:` -- Barlow SemiBold 16 pt `#F0EDE8`
- `Blast cleaning (SP-5 or SP-10) remains the standard. No secondary method alone meets typical plating specifications for heavy scale removal.` -- Inter Regular 14 pt `#F0EDE8`

Right column:
- `SECONDARY METHODS ARE BEST AS:` -- Barlow SemiBold 16 pt `#F0EDE8`
- `Supplements to primary blast/chemical descaling` -- Inter Regular 14 pt `#27AE60`
- `Solutions for complex geometry that blast cannot reach` -- Inter Regular 14 pt `#27AE60`
- `Combined deburring + light descaling operations` -- Inter Regular 14 pt `#27AE60`
- `Spot touch-up of blast-missed areas` -- Inter Regular 14 pt `#27AE60`

---

### ZONE 5 -- Key Takeaways Strip

**Section label:** Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

> KEY TAKEAWAYS

**BLOCK F -- Four Cards**

Y: 29.4" to 32.3".

| Card | X | Takeaway | Detail |
|---|---|---|---|
| 1 | 0.5" | VIBRATORY = COMPLEX PARTS | Reaches where blast cannot. Size media to part geometry. |
| 2 | 6.33" | SP-3 IS NOT SP-10 | Power tools remove loose scale. Tight oxide remains. Not for plating prep. |
| 3 | 12.16" | LASER = THE FUTURE | Zero media, zero chemicals. Currently limited by cost and speed. |
| 4 | 18.0" | SUPPLEMENT, DON'T REPLACE | Use secondary methods alongside primary descaling, not instead of. |

Per card: Rounded rect W: 5.5", H: 2.7", fill `#1E2435`, left accent 0.06" `#2EC4B6`.
Takeaway: Barlow SemiBold 15 pt `#2EC4B6`. Detail: Inter Regular 13 pt `#F0EDE8`.

---

### ZONE 6 -- Footer

Standard. Title: `Secondary Treatment -- Vibratory, Wire Brush & Laser Descaling`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Secondary Treatment Descaling -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster serves a crucial function: it prevents shops from over-relying on secondary methods when primary blast cleaning is what the spec actually requires. The decision matrix in Zone 3 is the key practical tool -- a supervisor can look at their scenario and immediately see whether vibratory, power tools, or laser is appropriate. The laser descaling section acknowledges the emerging technology without overpromising -- it is real, it is growing, but it is not yet practical for most shops.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #376 -- Construction Workup v1.0*
*2026-04-26*
