---
Project: Plating Posters Inc
Poster Number: 135
Title: "Cadmium Plating (Cyanide) -- Process Flow"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-14 technical reference (cyanide cadmium)"
Technical Source: Industry-standard cyanide cadmium plating process. Covers the complete 8-stage sequence from cleaning through hydrogen embrittlement bake. Values are typical ranges for aerospace-grade cyanide cadmium baths per AMS-QQ-P-416.
Process Scope: Cyanide cadmium plating -- complete process flow (8 stages)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - CadmiumPlating
  - Cyanide
  - ProcessFlow
  - ConstructionWorkup
  - ClusterEP14
---

# Poster #135 -- Construction Workup
## Cadmium Plating (Cyanide) -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Cluster overview poster for EP-14: Cadmium Plating (Cyanide). This is one of the most regulated processes in the plating industry. Cadmium is a known human carcinogen (IARC Group 1), RoHS restricted, REACH restricted, and subject to the lowest OSHA PEL of any common plating metal (5 ug/m3). It is still used in aerospace under AMS-QQ-P-416 for high-strength steel fasteners, connectors, and landing gear where no substitute exists.

This poster carries TWO prominent safety/regulatory badges: a CYANIDE SAFETY badge and a RESTRICTED SUBSTANCE badge. Both appear in the header zone. The hydrogen embrittlement bake (Stage 8) is life-safety critical -- delayed or omitted baking has caused fatal aircraft component failures.

---

## Part 1 -- Workflow Orientation

### Design Capabilities for This Poster

- Text boxes with precise font, size, weight, color, and spacing control
- Solid-color rectangles and rounded rectangles for flow boxes, callout panels, table rows, and accent borders
- Arrow/line elements connecting flow boxes in sequence
- Color fills set to exact hex values
- Background page color set to exact hex
- Export at print-quality PDF (300 DPI equivalent via print export)

### Limitations to Flag

1. **Process flow diagram (Block B -- HERO):** Eight rounded rectangles in a U-flow. Stage 8 (HE Bake) gets a double-border Coral treatment to emphasize its life-safety criticality.
2. **Parameter summary table (Block D):** 8-row table.
3. **Regulatory status panel (Block E):** Full-width panel listing OSHA, EPA, IARC, RoHS, REACH restrictions.
4. **Troubleshooting quick-hit strip (Block F):** 4 common problems.
5. **CYANIDE SAFETY badge + RESTRICTED SUBSTANCE badge:** Both in header zone.

---

## Part 2 -- Document Setup Instructions

### Step 1 -- Create the document
- Width: **24 inches**. Height: **36 inches**.

### Step 2 -- Set the background color
- **`#1A1F2E`** (Gunmetal Dark)

### Step 3 -- Upload fonts
Standard locked font set.

### Step 4 -- Set up color palette
Standard locked palette.

### Step 5 -- Set ruler guides
Standard guides: 0.5" / 2.9" / 15.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline + DUAL SAFETY BADGES

ZONE 2 -- PROCESS FLOW DIAGRAM / HERO (2.9"--15.5" / ~12.6" tall)
  Block B: Eight-stage U-flow diagram (2 rows of 4)
  Block C: Stage legend strip (color key)

ZONE 3 -- PARAMETER SUMMARY TABLE (15.5"--22.0" / ~6.5" tall)
  Block D: 8-row parameter table

ZONE 4 -- REGULATORY STATUS (22.0"--28.5" / ~6.5" tall)
  Block E: Full regulatory panel (OSHA, EPA, IARC, RoHS, REACH)

ZONE 5 -- TROUBLESHOOTING QUICK HITS (28.5"--32.5" / ~4.0" tall)
  Block F: 4-problem strip

ZONE 6 -- FOOTER BAND (32.5"--36.0" / ~3.5" tall)
  Block G: Disclaimer + poster title + series name + logo + version
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Dimensions:** Full page width. Y: 0" to 2.9".

**BLOCK A -- Headline**
- X: 0.5". Y: 0.5". Width: 12.0" (room for two badges)
- Font: Barlow Condensed ExtraBold, 80 pt (reduced from 88 to fit)
- Color: `#F0EDE8`
- Text: `CADMIUM PLATING`

**Subheading:**
- Y: 1.4". Width: 12.0"
- Barlow SemiBold, 32 pt, `#27AE60`
- Text: `Complete Process Flow -- 8 Stages from Cleaning to HE Bake`

**Tagline:**
- Y: 2.1". Width: 12.0"
- Barlow SemiBold, 20 pt, `#F0EDE8` at 65%
- Text: `Aerospace-grade corrosion protection for high-strength steel. Severely restricted. Used only where no alternative exists.`

**CYANIDE SAFETY BADGE (top right):**
- Rounded rect, X: 13.0", Y: 0.5", W: 5.0", H: 1.0"
- Fill: `#E05C5C` at 15%, border 2 pt `#E05C5C`, radius 6
- `CYANIDE PROCESS -- SAFETY CRITICAL` Barlow SemiBold 14 pt `#E05C5C`
- `NEVER mix with acid` Inter Medium 11 pt `#F0EDE8` at 80%

**RESTRICTED SUBSTANCE BADGE (below cyanide badge):**
- Rounded rect, X: 13.0", Y: 1.7", W: 10.5", H: 1.0"
- Fill: `#E05C5C` at 20%, border 2 pt `#E05C5C`, radius 6
- `RESTRICTED SUBSTANCE -- CADMIUM` Barlow Condensed ExtraBold 16 pt `#E05C5C`
- `IARC Group 1 Carcinogen | RoHS Restricted | REACH SVHC | OSHA PEL 5 ug/m3` JetBrains Mono 10 pt `#F0EDE8` at 80%

---

### ZONE 2 -- Process Flow Diagram (HERO)

**Section label:** `THE COMPLETE PROCESS -- STAGE BY STAGE` -- Y: 3.1".

**BLOCK B -- Eight-Stage U-Flow Diagram**

Y: 3.8" to 14.0". Same U-flow layout as Poster #127.

**Top Row (Y: 3.8" to 8.3") -- Stages 1-4:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Soak Clean / Electroclean | Box 1 | 0.5" | `#2EC4B6` (Teal) | Cleaning |
| 2. Rinse (Pre-Act) | Box 2 | 6.0" | `#2EC4B6` (Teal) | Rinse |
| 3. Acid Activation | Box 3 | 11.5" | `#E8A020` (Amber) | Activation |
| 4. Rinse (Pre-Plate) | Box 4 | 17.0" | `#2EC4B6` (Teal) | Rinse |

**Bottom Row (Y: 9.5" to 14.0") -- Stages 5-8:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 5. Cadmium Plate | Box 5 | 17.0" | `#27AE60` (Emerald) | Plating |
| 6. Rinse (Post-Plate) | Box 6 | 11.5" | `#2EC4B6` (Teal) | Rinse |
| 7. Chromate Conversion | Box 7 | 6.0" | `#E8A020` (Amber) | Post-Treatment |
| 8. HE Bake | Box 8 | 0.5" | `#E05C5C` (Coral) | CRITICAL |

**Inside each flow box:**

*Box 1 -- Cleaning:*
- Badge: `STAGE 1`, fill `#2EC4B6`
- Name: `Clean / Electroclean`
- Parameters: `Vapor degrease or soak clean` / `Electroclean anodic 3--5 min` / `Minimize H2 exposure`
- Purpose: `Remove oils; prepare high-strength steel`
- Check: `Short electroclean time -- minimize hydrogen charging`

*Box 2 -- Rinse:*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Activation`
- Parameters: `Ambient` / `Flowing`
- Purpose: `Remove cleaner carry-over`
- Check: `Standard`

*Box 3 -- Acid Activation:*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Acid Activation`
- Parameters: `HCl 10--20% v/v` / `Ambient, 15--30 sec MAX`
- Purpose: `Remove surface oxides`
- Check: `MINIMIZE TIME -- H-embrittlement risk on high-strength steel` (`#E05C5C`)

*Box 4 -- Rinse:*
- Badge: `STAGE 4`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Plate`
- Parameters: `Ambient` / `Flowing`
- Purpose: `Remove acid before cyanide bath`
- Check: `SAFETY: Acid to cyanide = HCN gas` (`#E05C5C`)

*Box 5 -- Cadmium Plate:*
- Badge: `STAGE 5`, fill `#27AE60`
- Name: `Cadmium Plate` / Subtitle: `Main Tank`
- Parameters: `Cd: 18--35 g/L` / `NaCN: 90--150 g/L` / `75--90 F (24--32 C)` / `10--25 ASF (rack)`
- Purpose: `Electrodeposit cadmium onto substrate`
- Check: `Free NaCN: 15--45 g/L`

*Box 6 -- Rinse:*
- Badge: `STAGE 6`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Post-Plate`
- Parameters: `Double counterflow` / `Cd waste segregation`
- Purpose: `Remove CN drag-out; capture Cd for treatment`
- Check: `Cd rinse water is hazardous waste` (`#E05C5C`)

*Box 7 -- Chromate Conversion:*
- Badge: `STAGE 7`, fill `#E8A020`
- Name: `Chromate Conversion`
- Parameters: `Type I (Clear): 48--96 hr WSS` / `Type II (Gold): 96--200 hr WSS` / `Type III (OD): 200--400 hr WSS`
- Purpose: `Enhance corrosion resistance`
- Check: `Almost always hexavalent chromate (no trivalent Cd passivation market)`

*Box 8 -- HE Bake (LIFE-SAFETY CRITICAL):*
- Badge: `STAGE 8`, fill `#E05C5C`
- Name: `HYDROGEN EMBRITTLEMENT BAKE`
- Parameters: `375 +/- 25 F (190 +/- 14 C)` / `12--24 hr (per AMS 2759/9)` / `WITHIN 1 HOUR OF PLATING`
- Purpose: `Drive out absorbed hydrogen from steel`
- Check: `NOT OPTIONAL. Delayed bake has caused fatal aircraft failures.` (`#E05C5C`)
- Special: Double border 3 pt `#E05C5C` on this box

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.3". Standard format.

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Cleaning & Rinse` |
| `#E8A020` (Amber) | `Activation & Post-Treatment` |
| `#27AE60` (Emerald) | `Plating (Main Tank)` |
| `#E05C5C` (Coral) | `CRITICAL Safety / HE Bake` |

---

### ZONE 3 -- Parameter Summary Table

**Section label:** `AT-A-GLANCE PARAMETERS` -- Y: 15.7".

**BLOCK D -- 8-Row Parameter Table**

| Stage | Chemistry | Temp | Time | CD | Key Control |
|---|---|---|---|---|---|
| 1. Clean | Alk cleaner + electroclean | 140--160 F | 3--5 min EC | 20--50 ASF | Minimize H2 |
| 2. Rinse | Water | Ambient | 30--60 sec | -- | Standard |
| 3. Activation | HCl 10--20% | Ambient | 15--30 sec MAX | -- | Minimize time |
| 4. Rinse | Water | Ambient | 30--60 sec | -- | No acid to CN |
| 5. Cd Plate | Cd 18--35 g/L, NaCN 90--150 | 75--90 F | Per spec | 10--25 ASF | Free NaCN |
| 6. Rinse | Water (Cd segregated) | Ambient | 30--60 sec | -- | Haz waste |
| 7. Chromate | Hex chromate per type | Per type | Per type | -- | SST hours |
| 8. HE Bake | N/A (oven) | 375 F | 12--24 hr | -- | WITHIN 1 HR |

---

### ZONE 4 -- Regulatory Status

**Section label:** `REGULATORY STATUS -- CADMIUM IS SEVERELY RESTRICTED` -- Y: 22.2".

**BLOCK E -- Full-Width Regulatory Panel (Y: 22.9" to 28.3")**

- Rounded rect, X: 0.5", W: 23.0", H: 5.2", fill `#E05C5C` at 10%, border 2 pt `#E05C5C`, radius 8

**Left column (X: 1.0", W: 7.0"):**
- Title: `HEALTH HAZARDS` Barlow Condensed ExtraBold 20 pt `#E05C5C`
- `IARC: Group 1 -- Known human carcinogen (lung cancer)` Inter Medium 13 pt `#F0EDE8`
- `Target organs: Lungs, kidneys, bones`
- `Exposure routes: Inhalation (primary), ingestion`
- `OSHA PEL: 5 ug/m3 (8-hr TWA)`
- `Action level: 2.5 ug/m3`
- `Mandatory: Blood and urine Cd monitoring for all exposed workers`

**Center column (X: 8.5", W: 7.0"):**
- Title: `REGULATORY RESTRICTIONS` Barlow Condensed ExtraBold 20 pt `#E8A020`
- `RoHS: BANNED in electronics (0.01% max -- lowest threshold of any RoHS substance)`
- `REACH: SVHC candidate list -- authorization required in EU`
- `EPA: Clean Water Act priority pollutant (0.1 mg/L monthly avg discharge)`
- `29 CFR 1910.1027: Full Cd standard -- medical surveillance, exposure monitoring, training`

**Right column (X: 16.0", W: 7.5"):**
- Title: `WHERE STILL PERMITTED` Barlow Condensed ExtraBold 20 pt `#27AE60`
- `Aerospace: AMS-QQ-P-416 (active spec)`
- `Military: Legacy programs referencing QQ-P-416`
- `Nuclear: Certain shielding applications`
- `No new installations being built`
- `Existing shops operate under stringent EPA/OSHA permits`
- Note: `If zinc or zinc-nickel can meet the specification, they MUST be used instead of cadmium.`

---

### ZONE 5 -- Troubleshooting Quick Hits

**Section label:** `QUICK TROUBLESHOOTING -- 4 COMMON PROBLEMS` -- Y: 28.7".

**BLOCK F -- Four Problem Cards**

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | HE FAILURE | Delayed or insufficient bake | Bake within 1 hr; verify time/temp per AMS 2759/9 |
| 2 | 6.33" | DARK DEPOSIT | Organic contamination, metallic impurities | Carbon treat; dummy plate |
| 3 | 12.16" | POOR ADHESION | Surface contamination, inadequate activation | Improve cleaning; verify activation |
| 4 | 18.0" | THIN LCD COVERAGE | Low cadmium metal, poor throwing power | Add CdO; check NaCN level |

Standard card style.

---

### ZONE 6 -- Footer Band

Standard footer. Title: `Cadmium Plating (Cyanide) -- Process Flow`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Cadmium plating is restricted to authorized applications under aerospace, military, and nuclear exemptions. Cadmium is classified as a known human carcinogen. All cadmium operations require engineering controls, medical surveillance, and regulatory compliance. Consult your EHS officer and process supplier. Source: General industry knowledge; AMS-QQ-P-416; OSHA 29 CFR 1910.1027.`

---

## Part 5 -- Grouping and Naming Convention

| Group Name | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline, cyanide badge, restricted substance badge |
| Zone 2 - Process Flow | Section label, eight flow boxes, arrows, legend strip |
| Zone 3 - Parameter Table | Section label, 8-row table |
| Zone 4 - Regulatory | Section label, three-column regulatory panel |
| Zone 5 - Troubleshooting | Section label, four problem cards |
| Zone 6 - Footer | Footer band, disclaimer, title, series, logo, version |

---

## Part 6 -- Light Edition Color Remap Table

Standard remap table (same as Poster #127).

---

## Part 7 -- Export Checklist

| File Name | Mode | Quality | Bleed |
|---|---|---|---|
| `Cadmium Plating Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Cadmium Plating Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Cadmium Plating Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Cadmium Plating Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Cadmium Plating Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Cadmium Plating Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This poster carries the heaviest regulatory burden of any poster in the series. The dual badges (cyanide + restricted substance) must be impossible to miss. The HE Bake box (Stage 8) is highlighted in Coral with a double border -- this is a life-safety item. The regulatory panel in Zone 4 replaces the usual comparison callout because the regulatory story IS the story for cadmium. Educational, not alarmist -- cadmium plating is a legal, necessary process in aerospace, but everyone touching it must understand the restrictions.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #135 -- Construction Workup v1.0*
*2026-04-26*
