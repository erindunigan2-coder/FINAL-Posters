---
Project: Plating Posters Inc
Poster Number: 394
Title: "Rinse Water Quality & Control -- Conductivity, pH & Water Source"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Chemical Treatment Clusters — Watson Research Brief (CT-8)"
Technical Source: Industry-standard rinse water quality parameters -- conductivity targets by application, pH monitoring for neutralization tanks, city water vs. DI water specifications, and control methods. Per Metal Finishing Guidebook and general industry knowledge.
Process Scope: Rinse water quality and control -- conductivity targets, pH monitoring, water source selection, inline monitoring, and neutralization tank chemistry
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Neutralization
  - RinseSystems
  - WaterQuality
  - Conductivity
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT08
---

# Poster #394 -- Construction Workup
## Rinse Water Quality & Control -- Conductivity, pH & Water Source

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the "recipe and control" poster for the rinse cluster -- except the "recipe" is water quality specifications rather than chemical formulations. Conductivity is the operator's best friend here: a $50 handheld conductivity meter is the cheapest quality tool in the entire plating shop. This poster maps conductivity targets by application (general plating vs. decorative vs. electronics vs. aerospace), explains the relationship between conductivity and contamination, and covers neutralization tank chemistry for the acid-to-alkaline and alkaline-to-acid transitions.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Conductivity target table (Block B -- HERO):** Four application tiers with specific conductivity targets. The defining data on this poster.

2. **Water source comparison (Block C):** City water vs. DI water vs. RO water properties side by side.

3. **Neutralization tank chemistry (Block D):** Four transition scenarios with solution type, concentration, and purpose.

4. **Control methods panel (Block E):** Inline conductivity monitoring, pH measurement, DI system monitoring.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 14.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- CONDUCTIVITY TARGETS + WATER SOURCE (2.9"--14.5" / ~11.6" tall)
  Block B: Conductivity target table (HERO)
  Block C: Water source comparison

ZONE 3 -- NEUTRALIZATION TANK CHEMISTRY (14.5"--22.0" / ~7.5" tall)
  Block D: Four transition scenarios

ZONE 4 -- CONTROL METHODS (22.0"--28.5" / ~6.5" tall)
  Block E: Monitoring methods and automation

ZONE 5 -- KEY PRINCIPLES (28.5"--32.5" / ~4.0" tall)
  Block F: Quick-reference water quality rules

ZONE 6 -- FOOTER BAND (32.5"--36.0")
  Block G: Standard footer
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE WATER QUALITY` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Conductivity Targets, pH Control & Water Source Selection` -- 32 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `A $50 conductivity meter is the cheapest quality insurance in the plating shop. If you are not measuring rinse water, you are guessing -- and contamination does not forgive guesses.` -- 20 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Conductivity Targets + Water Source (HERO)

**Section label:** Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> CONDUCTIVITY TARGETS -- THE NUMBERS THAT MATTER

---

**BLOCK B -- Conductivity Target Table**

Y: 3.8" to 8.5". Full width.

Column widths (23.0" total):
- Application (5.5") | Target Conductivity (5.0") | Rinse Type (5.5") | Water Source (4.0") | Notes (3.0")

Header row: fill `#3A4055`, H: 0.5".

| Application | Target | Rinse Type | Water Source | Notes |
|---|---|---|---|---|
| General industrial plating | < 200 uS/cm | Double counterflow | City water OK | Standard of care |
| Decorative nickel / chrome | < 100 uS/cm | Double or triple counterflow | DI preferred for final | Spots and haze if too high |
| Electronics / connectors | < 20 uS/cm | Triple counterflow + DI | DI required | Chloride and hardness = pitting |
| Aerospace (per processor spec) | < 50 uS/cm | Per specification | DI typically required | Varies by prime; verify spec |

Data: Inter Regular 13 pt. Application names: Barlow SemiBold 14 pt.

Color coding for target:
- < 200: `#27AE60`
- < 100: `#2EC4B6`
- < 50: `#E8A020`
- < 20: `#E05C5C` (most critical)

**Rinse water stage table (Y: 9.0" to 11.5"):**

Section sublabel: `RINSE WATER QUALITY BY STAGE POSITION` Barlow SemiBold 18 pt `#F0EDE8`. Y: 9.0".

| Rinse Type | Water Source | Typical Conductivity | Purpose |
|---|---|---|---|
| First rinse (drag-out) | City water or recirculated | 500-5000 uS/cm | Captures bulk dragout; saves chemistry |
| Intermediate rinse | City water, flowing | 100-500 uS/cm | Removes most carryover |
| Final pre-plating rinse | DI water preferred | < 50 uS/cm | Minimizes contamination entering plating bath |
| Critical pre-plating rinse | DI water required | < 20 uS/cm | Electronics, aerospace, decorative |

---

**BLOCK C -- Water Source Comparison**

Y: 12.0" to 14.3". Three callout boxes side by side.

Each box: Rounded rect, W: 7.33", H: 2.0", fill `#1E2435`, radius 6, top accent 3 pt.

| Box | X | Source | Accent | Key Properties |
|---|---|---|---|---|
| 1 | 0.5" | CITY WATER | `#E8A020` | Conductivity: 200-1000 uS/cm. Hardness: 50-500 ppm CaCO3. Chloride: 10-250 ppm. Silica: 5-50 ppm. Adequate for first and intermediate rinse. |
| 2 | 8.16" | DI WATER | `#27AE60` | Conductivity: 0.055-1.0 uS/cm. Hardness: < 1 ppm. Chloride: < 0.1 ppm. Silica: < 0.01 ppm. Required for final pre-plating and critical rinse. |
| 3 | 15.83" | RO WATER | `#2EC4B6` | Removes 90-99% dissolved solids. Often used as pre-treatment before ion exchange to extend resin life. Not as pure as mixed-bed DI alone. |

Per box:
- Source: Barlow SemiBold 15 pt, accent color
- Properties: Inter Regular 12 pt `#F0EDE8`. Numbers: JetBrains Mono 12 pt.

---

### ZONE 3 -- Neutralization Tank Chemistry

**Section label:** Centered. Y: 14.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> NEUTRALIZATION TANK CHEMISTRY -- FOUR TRANSITIONS

---

**BLOCK D -- Four Transition Scenarios**

Y: 15.4" to 21.8". Four callout boxes stacked in pairs (2x2).

Each box: Rounded rect, W: 11.17", H: 2.9", fill `#1E2435`, radius 6, left accent 0.06".

| Position | Transition | Solution | Concentration | Purpose | Accent |
|---|---|---|---|---|---|
| R1C1 | Alkaline -> Acid | Dilute H2SO4 or HCl | 1-5% (10-50 g/L acid) | Remove alkaline residue from part surface before acid activation | `#E8A020` |
| R1C2 | Acid -> Alkaline | Dilute NaOH or Na2CO3 | 1-3% (10-30 g/L) | Remove acid residue before alkaline plating bath (e.g., alkaline zinc) | `#2EC4B6` |
| R2C1 | Acid -> Acid Plating Bath | Often no neutralization | N/A | Mild acid on surface is compatible with acid plating baths; direct rinse | `#27AE60` |
| R2C2 | Inhibited Acid Dip | Dilute H2SO4 or HCl + wetting agent | 3-10% + inhibitor | Combined neutralization + activation; minimizes base metal attack; 15-60 sec | `#E8A020` |

Per box:
- Transition: Barlow SemiBold 15 pt, accent color
- Solution/concentration: JetBrains Mono 13 pt `#F0EDE8`
- Purpose: Inter Regular 13 pt `#F0EDE8`

**Control callout (Y: 21.3"):**
- Rounded rect, full width, H: 0.4", fill `#E8A020` at 12%, border 1 pt `#E8A020`
- Text: `Neutralization tanks: monitor pH. Acid neutralization: maintain pH 2-3. Alkaline neutralization: maintain pH 9-11.` Inter Medium 13 pt `#E8A020`

---

### ZONE 4 -- Control Methods

**Section label:** Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> MONITORING AND AUTOMATION

---

**BLOCK E -- Four Control Method Cards**

Y: 22.9" to 28.3". Four cards in 2x2 grid. Gap: 0.33".

Each card: Rounded rect, W: 11.17", H: 2.5", fill `#1E2435`, radius 6, left accent 0.06".

| Position | Method | What It Monitors | How It Works | Accent |
|---|---|---|---|---|
| R1C1 | Inline Conductivity Probe | Rinse water contamination level | Continuous reading; alarm or automatic dump valve at setpoint; the most important rinse control tool | `#27AE60` |
| R1C2 | pH Meter / Strips | Neutralization tank effectiveness | Dip strip or handheld meter; verify acid neutralization pH 2-3, alkaline neutralization pH 9-11 | `#E8A020` |
| R2C1 | DI System Resistivity | DI water quality at point of generation | Inline resistivity meter; target 1-18 megohm-cm; alarm on low resistivity (resin exhausted) | `#2EC4B6` |
| R2C2 | Visual Inspection | Foam, cloudiness, oil sheen, color | Free -- requires no instrument; foam = surfactant carryover; cloudiness = precipitation; sheen = oil | `#C8D0D8` |

Per card:
- Method: Barlow SemiBold 15 pt, accent color
- Description: Inter Regular 13 pt `#F0EDE8`

---

### ZONE 5 -- Key Principles

**Section label:** Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

> WATER QUALITY RULES -- QUICK REFERENCE

---

**BLOCK F -- Four Principle Cards**

Y: 29.3" to 32.3". Four cards in a single row.

Each card: Rounded rect, W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06".

| Card | X | Principle | Accent |
|---|---|---|---|
| 1 | 0.5" | Any rinse that feeds directly into a plating tank should use DI water | `#27AE60` |
| 2 | 6.33" | Conductivity monitoring is the cheapest quality tool in the shop -- use it | `#E8A020` |
| 3 | 12.16" | City water hardness (Ca/Mg) forms insoluble soaps in alkaline baths and interferes with plating | `#2EC4B6` |
| 4 | 18.0" | Chloride in city water causes pitting in plating -- DI removes it to < 0.1 ppm | `#E05C5C` |

---

### ZONE 6 -- Footer

Standard. Title: `Rinse Water Quality & Control -- Conductivity, pH & Water Source`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Conductivity targets and water quality parameters shown are typical industry values. Specific requirements vary by plating process, customer specification, and quality standard. Consult your process supplier and applicable specifications for site-specific targets.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Water Quality Control -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The conductivity target table is the hero because it gives operators immediate, actionable numbers. Color-coding the targets by criticality (green for general, coral for electronics-grade) communicates urgency at a glance. The water source comparison boxes distill the city-vs-DI decision into three simple panels -- many operators do not know what DI water actually removes or why it matters. The neutralization chemistry section answers the question "what goes in the dip tank between alkaline and acid?" which is one of the most common setup questions on a plating line.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #394 -- Construction Workup v1.0*
*2026-04-26*
