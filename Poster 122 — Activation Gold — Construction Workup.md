---
Project: Plating Posters Inc
Poster Number: 122
Title: "Activation -- Gold"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Process Scope: Acid activation for gold plating (Stage 3 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - GoldPlating
  - Activation
  - ConstructionWorkup
  - Series2
  - ClusterEP12
---

# Poster #122 -- Construction Workup
## Activation -- Gold

*Alaina -- Plating Posters Inc*
*v1.0 -- 2026-04-26*

Stage 3 of 8. Activation for gold plating removes the thin oxide film from the nickel underplate surface. The parameters are mild -- sulfuric acid, ambient temperature, short immersion. But the rules are absolute: NEVER use hydrochloric acid. Chloride contamination in a gold bath is catastrophic. This poster exists to drill that rule into every operator on the line.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Activation mechanism diagram (Block B -- HERO):** Same three-panel before/during/after concept as Poster #114 (Tin) but focused on nickel oxide removal.
2. **The chloride rule callout (Block D):** The dominant visual -- a large, unmissable warning panel about HCl.
3. **Activation parameters (Block E):** Simple table -- gold activation is straightforward.
4. **Gold strike option (Block F):** When and why a gold strike is used before the main bath.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 3 highlighted (Amber)
ZONE 3 -- ACTIVATION MECHANISM HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- THE CHLORIDE RULE (14.5"--20.5" / ~6.0")
ZONE 5 -- ACTIVATION PARAMETERS (20.5"--26.5" / ~6.0")
ZONE 6 -- GOLD STRIKE OPTION (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ACTIVATION` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Gold Plating -- Stage 3 of 8` -- 36 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `Remove the nickel oxide. Sulfuric acid only. If you touch HCl, you will contaminate the most expensive bath in the shop.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 3 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Nickel underplate with oxide film  -->  After: Oxide-free nickel ready for gold deposition`

---

### ZONE 3 -- Activation Mechanism Hero

**Section label:** `HOW ACTIVATION WORKS ON NICKEL` -- Y: 4.4".

**BLOCK B -- Three-Panel Surface Cross-Section**

Y: 5.0" to 14.0". Same concept as Poster #114 (Tin) but showing nickel oxide removal.

Panel 1 -- `BEFORE`:
- Nickel layer (bottom), fill `#2EC4B6` at 30%
- Nickel oxide layer (top), fill `#E05C5C` at 40%, labeled `NiO OXIDE FILM`
- `Oxide blocks gold adhesion` Inter Regular 13 pt `#E05C5C`

Panel 2 -- `DURING`:
- Nickel oxide partially dissolved
- Acid arrows: `H2SO4` labels
- `NiO + H2SO4 -> NiSO4 + H2O` JetBrains Mono 13 pt `#E8A020`
- `Acid dissolves oxide` Inter Regular 13 pt `#E8A020`

Panel 3 -- `AFTER`:
- Clean nickel surface, bright
- `Active nickel surface` Inter Regular 13 pt `#27AE60`
- `Ready for gold deposition` Inter Medium 13 pt `#27AE60`

**Key parameters (Y: 13.0"):**
- `5--10% H2SO4 | Ambient | 15--30 sec` JetBrains Mono 16 pt `#E8A020`

---

### ZONE 4 -- The Chloride Rule

**Section label:** `THE #1 RULE IN GOLD ACTIVATION` -- Y: 14.7".

**BLOCK D -- Chloride Warning Panel**

Y: 15.3" to 20.0". Full-width panel -- this is the visual centerpiece.

- Rounded rect, X: 0.5", W: 23.0", H: 4.5", fill `#E05C5C` at 12%, border 3 pt `#E05C5C`, radius 8
- Title: `NEVER USE HYDROCHLORIC ACID (HCl) FOR GOLD ACTIVATION` Barlow Condensed ExtraBold 28 pt `#E05C5C`

**Three-column content inside:**

| Column | Header | Content |
|---|---|---|
| Left | `THE RULE` | Sulfuric acid (H2SO4) only for gold activation. No exceptions. No "just this once." Chloride ions are poison to gold baths. |
| Center | `THE CHEMISTRY` | Cl- ions complex with Au+ to form soluble AuCl, depleting gold from solution. Chloride attacks the gold cyanide complex. Even 1 ppm Cl- is detectable in the deposit. |
| Right | `THE COST` | A single chloride contamination event can require partial or complete bath replacement. At $200--800/gal in gold content, one mistake = $1,000+ loss. |

Column headers: Barlow SemiBold 16 pt, each in `#E05C5C`.
Content: Inter Regular 14 pt `#F0EDE8`, line height 155%.

Bottom warning: `Post this rule at the activation tank. Tape it to the wall. Tattoo it on your foreman's arm if necessary. No HCl. Ever.` Inter Medium 14 pt `#E05C5C`

---

### ZONE 5 -- Activation Parameters

**Section label:** `ACTIVATION PARAMETERS BY SUBSTRATE` -- Y: 20.7".

**BLOCK E -- Parameter Table**

Y: 21.3" to 26.0".

| Substrate | Acid | Concentration | Temp | Time | Notes |
|---|---|---|---|---|---|
| Nickel underplate (standard) | H2SO4 | 5--10% v/v | Ambient | 15--30 sec | Most common |
| Kovar / alloy 42 | Proprietary or H2SO4 | Per supplier | Ambient | 15--30 sec | Specialty substrates |
| Copper (rare -- direct gold) | H2SO4 | 5--10% v/v | Ambient | 15--30 sec | Ni underplate preferred |

Header: `#3A4055`. Alternating rows: `#1E2435` / `#252B3D`.

**Note below:**
- `Activation for gold is simple. The chemistry is mild. The rule is absolute. Get the acid right and the rest follows.` Inter Medium 13 pt `#27AE60`

---

### ZONE 6 -- Gold Strike Option

**Section label:** `GOLD STRIKE -- WHEN AND WHY` -- Y: 26.7".

**BLOCK F -- Gold Strike Panel**

Y: 27.3" to 32.0". Two-column layout.

**Left -- When to Use a Strike:**
- Rounded rect, X: 0.5", W: 11.0", H: 4.5", fill `#1E2435`, left accent `#E8A020`
- Title: `WHEN A GOLD STRIKE IS NEEDED` Barlow SemiBold 18 pt `#E8A020`

Content:
- `Difficult substrates (Kovar, alloy 42, tungsten)`
- `Long time gap between activation and gold plate`
- `Rework or replating over existing gold`
- `Adhesion failures on standard activation`
- `Some specifications require it (MIL-G-45204)`

**Right -- Strike Parameters:**
- Rounded rect, X: 12.0", W: 11.5", H: 4.5", fill `#1E2435`, left accent `#27AE60`
- Title: `GOLD STRIKE PARAMETERS` Barlow SemiBold 18 pt `#27AE60`

| Parameter | Range |
|---|---|
| Gold concentration | 1--4 g/L |
| pH | 3.5--5.0 |
| Temperature | 90--120 F (32--49 C) |
| Current density | 3--10 ASF |
| Time | 15--60 sec |
| Purpose | Thin flash for adhesion |

Note: `The strike is a thin adhesion layer -- not a structural deposit. If your standard process has good adhesion, a strike may not be needed. Consult your supplier TDS.` Inter Medium 12 pt `#F0EDE8` at 70%

---

### ZONE 7 -- Footer

Standard. Title: `Activation -- Gold`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Activation Gold -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The chloride warning panel dominates this poster by design. It is the single most important message in gold activation -- arguably the most important safety-of-chemistry message in the entire gold cluster. The panel is intentionally oversized relative to the simple activation parameters because the rule matters more than the numbers. The gold strike section is included because it is a common "Stage 3.5" in gold plating that operators encounter but may not fully understand.

---

*Alaina -- Plating Posters Inc*
*Poster #122 -- Construction Workup v1.0*
*2026-04-26*
