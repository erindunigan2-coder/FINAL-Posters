---
Project: Plating Posters Inc
Poster Number: 709
Title: "Application -- Priming"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster 7 technical reference (Industrial Priming Systems) -- Watson Research Brief"
Technical Source: Primer application parameters for zinc-rich (IOZ and OZ), epoxy, and aerospace primers. Covers DFT targets, airless spray settings, mixing and agitation requirements, pot life, and the critical agitation rule for zinc-loaded primers.
Process Scope: Primer application -- Stage 5 of 8
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - IndustrialPriming
  - Application
  - ConstructionWorkup
  - PaintingCoating
  - Cluster7
---

# Poster #709 -- Construction Workup
## Application -- Priming

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 5 of 8. This poster covers the actual application of primer to the prepared substrate. The hero is a head-to-head comparison of IOZ vs. OZ vs. epoxy primer application parameters. The one rule that dominates this stage: continuous agitation. Zinc dust is heavy -- it settles to the bottom of the pot in minutes. Stop stirring and you are spraying clear binder with no zinc. That is an expensive way to achieve zero corrosion protection.

Hero visual: a three-column comparison panel showing IOZ, OZ, and epoxy primer application side by side with spray parameters, DFT targets, and equipment requirements.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Three-column primer comparison hero (Block B):** Three tall panels side by side -- IOZ, OZ, Epoxy -- each with application parameters. Built with rounded rectangles and data rows.
2. **Spray equipment parameters table (Block D):** Airless spray pressure, tip size, gun-to-part distance.
3. **Aerospace primer sidebar (Block E):** Chromated and non-chrome primer DFT and specs.
4. **Agitation callout (Block F):** The "stop stirring = stop protecting" warning.
5. **Pot life comparison strip (Block G):** Visual timeline comparing pot life across primer types.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.0" / 21.0" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 5 highlighted (Amber)
ZONE 3 -- THREE-COLUMN PRIMER APPLICATION HERO (4.2"--15.0" / ~10.8")
ZONE 4 -- SPRAY EQUIPMENT TABLE (15.0"--21.0" / ~6.0")
ZONE 5 -- AEROSPACE PRIMER SIDEBAR + POT LIFE STRIP (21.0"--27.0" / ~6.0")
ZONE 6 -- AGITATION CALLOUT + COMMON MISTAKES (27.0"--32.5" / ~5.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `APPLICATION` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Industrial Priming -- Stage 5 of 8` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Zinc settles. Agitate continuously or spray clear binder with zero corrosion protection. The pot does not stir itself.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 5 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean, profiled, pretreatment-ready substrate  -->  After: Primer film at target DFT`

---

### ZONE 3 -- Three-Column Primer Application Hero

**Section label:** `PRIMER APPLICATION -- THREE SYSTEMS COMPARED` -- Y: 4.4".

**BLOCK B -- Three Primer Columns (Y: 5.0" to 14.5")**

Three tall panels side by side:

**Column 1 -- Inorganic Zinc (IOZ) (X: 0.5", W: 7.33", H: 9.0"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#27AE60`
- Title: `INORGANIC ZINC (IOZ)` Barlow SemiBold 20 pt `#27AE60`
- Subtitle: `The Gold Standard` Inter Regular 14 pt `#F0EDE8` at 50%

Parameters (JetBrains Mono 13 pt `#F0EDE8`, line height 165%):

| Parameter | Value |
|---|---|
| Binder | Ethyl silicate (solvent) or alkali silicate (water) |
| Zinc content (dry film) | 75--85% by weight |
| Zinc dust spec | ASTM D520 Type II (spherical) |
| Target DFT | 2.5--4.0 mils (64--102 um) |
| Coats | 1--2 |
| Method | Airless spray (primary); brush for touch-up only |
| Spray pressure | 2,500--3,500 psi |
| Tip size | 0.017--0.023 inch |
| Pot life | 4--8 hours (zinc slurry) |
| Mixing | CONTINUOUS agitation -- zinc settles in minutes |

Labels: Inter Medium 12 pt `#F0EDE8` at 60%. Values: JetBrains Mono 12 pt `#F0EDE8`.

Bottom highlight:
- Pill-shaped, fill `#27AE60` at 15%, border 1 pt `#27AE60`
- Text: `Maximum galvanic protection -- if applied correctly` Inter Medium 12 pt `#27AE60`

**Column 2 -- Organic Zinc (OZ) (X: 8.33", W: 7.33", H: 9.0"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#E8A020`
- Title: `ORGANIC ZINC (OZ)` Barlow SemiBold 20 pt `#E8A020`
- Subtitle: `The Forgiving Alternative` Inter Regular 14 pt `#F0EDE8` at 50%

| Parameter | Value |
|---|---|
| Binder | Epoxy, polyurethane, or moisture-cure urethane |
| Zinc content (dry film) | 65--80% by weight |
| Zinc dust spec | ASTM D520 Type II |
| Target DFT | 2.0--3.5 mils (51--89 um) |
| Coats | 1--2 |
| Method | Airless, air spray, brush, roll |
| Spray pressure | 2,000--3,000 psi |
| Tip size | 0.017--0.021 inch |
| Pot life | 15 min--8 hr (2K epoxy-zinc); unlimited (1K moisture-cure) |
| Mixing | Continuous agitation -- same zinc settling issue |

Bottom highlight:
- Pill-shaped, fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `Easier application -- brush and roll for field repair` Inter Medium 12 pt `#E8A020`

**Column 3 -- Epoxy Primer (X: 16.17", W: 7.33", H: 9.0"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#2EC4B6`
- Title: `EPOXY PRIMER` Barlow SemiBold 20 pt `#2EC4B6`
- Subtitle: `General Purpose` Inter Regular 14 pt `#F0EDE8` at 50%

| Parameter | Value |
|---|---|
| Binder | Bisphenol A epoxy + amine or polyamide hardener |
| Zinc content | None (barrier protection, not galvanic) |
| Target DFT | 1.0--3.0 mils per coat |
| Coats | 1--2 |
| Method | Airless, air spray, HVLP, brush, roll |
| Spray pressure | 2,000--3,000 psi |
| Tip size | 0.015--0.021 inch |
| Pot life (2K) | 30 min--8 hours |
| Volume solids | 50--80% (high-solids) |
| Mixing | Mix A + B per ratio; no zinc settling concern |

Bottom highlight:
- Pill-shaped, fill `#2EC4B6` at 15%, border 1 pt `#2EC4B6`
- Text: `Broad application range -- lower skill barrier than IOZ` Inter Medium 12 pt `#2EC4B6`

---

### ZONE 4 -- Spray Equipment Table

**Section label:** `AIRLESS SPRAY -- EQUIPMENT PARAMETERS` -- Y: 15.2".

**BLOCK D -- Equipment Table (Y: 15.8" to 20.8")**

| Parameter | IOZ | OZ | Epoxy | Notes |
|---|---|---|---|---|
| Spray pressure (psi) | 2,500--3,500 | 2,000--3,000 | 2,000--3,000 | Higher pressure for IOZ due to zinc loading |
| Tip size (inch) | 0.017--0.023 | 0.017--0.021 | 0.015--0.021 | Larger tips for zinc-loaded primers |
| Gun-to-part distance | 12--18 inches | 10--16 inches | 10--14 inches | IOZ needs more distance for atomization |
| Fan pattern overlap | 50% | 50% | 50% | Standard technique for uniform DFT |
| Stripe coating | Edges, welds, bolts | Edges, welds, bolts | Edges, welds, bolts | Brush-applied stripe coat before spray coat |
| Wet film gauge check | ASTM D4414 | ASTM D4414 | ASTM D4414 | Check WFT during application; calculate DFT from volume solids |

Header: `#3A4055`. Alternating rows `#1E2435` / `#252B3D`. Data: JetBrains Mono 12 pt. Headers: Barlow SemiBold 13 pt `#F0EDE8`.

---

### ZONE 5 -- Aerospace Primer Sidebar + Pot Life Strip

**Two-column layout (Y: 21.2" to 26.8"):**

**Left -- Aerospace Primers (X: 0.5", W: 11.0"):**

Section label: `AEROSPACE PRIMERS -- THIN FILM, HIGH SPEC` Barlow Condensed ExtraBold 22 pt `#2EC4B6`.

| Primer Type | DFT | Key Specification |
|---|---|---|
| Chromated epoxy | 0.6--1.0 mil | MIL-PRF-23377 / BMS 10-11 |
| Non-chrome epoxy | 0.6--1.0 mil | MIL-PRF-85582 / BMS 10-72 |
| Composite primer | 0.3--0.8 mil | Low-density flexible formulation |
| Wash primer | 0.3--0.5 mil | MIL-DTL-15328 (vinyl butyral + phosphoric acid) |

Data: JetBrains Mono 12 pt. Spec codes: `#2EC4B6`.

Note: `Aerospace primer DFT is 3--8x thinner than industrial primer. Precision spray equipment and controlled conditions are mandatory.` Inter Regular 12 pt `#F0EDE8` at 60%.

**Right -- Pot Life Comparison (X: 12.0", W: 11.5"):**

Section label: `POT LIFE -- YOUR WORKING CLOCK` Barlow Condensed ExtraBold 22 pt `#E8A020`.

Four horizontal bars representing pot life at 77 deg F:

| Primer | Pot Life Bar | Duration |
|---|---|---|
| IOZ (ethyl silicate) | Medium bar, `#27AE60` | 4--8 hours |
| OZ (2K epoxy-zinc) | Short bar, `#E8A020` | 15 min--8 hours (varies widely) |
| OZ (1K moisture-cure) | Full bar, `#27AE60` | Unlimited (single component) |
| Epoxy (2K) | Variable bar, `#2EC4B6` | 30 min--8 hours |

Each bar: rounded rect, H: 0.6", fill at 40% of accent color. Duration label: JetBrains Mono 13 pt `#F0EDE8`.

Warning: `Rule of thumb: pot life halves for every 18 deg F (10 deg C) increase in temperature.` Inter Medium 13 pt `#E05C5C`.

---

### ZONE 6 -- Agitation Callout + Common Mistakes

**Two-column layout (Y: 27.2" to 32.3"):**

**Left -- The Agitation Rule (X: 0.5", W: 11.0"):**

Section label: `THE #1 APPLICATION RULE` Barlow Condensed ExtraBold 22 pt `#E05C5C`.

Large callout box, fill `#1E2435`, left accent `#E05C5C`:

Big stat: `AGITATE` Barlow Condensed ExtraBold 60 pt `#E05C5C` (centered)
Subtitle: `Continuously. Without Exception.` Barlow SemiBold 20 pt `#F0EDE8`

Body (Inter Regular 14 pt `#F0EDE8`, line height 165%):
- `Zinc dust density: 7.14 g/cm3 -- it sinks FAST`
- `In a paint pot without agitation, zinc settles to the bottom within minutes`
- `Spraying un-agitated zinc primer = spraying clear binder`
- `Clear binder provides ZERO galvanic protection`
- `Mechanical agitation (air motor or electric paddle) must run continuously during application`

Bottom: `If the agitator stops, stop spraying.` Inter Medium 15 pt `#E05C5C`

**Right -- Common Mistakes (X: 12.0", W: 11.5"):**

Section label: `APPLICATION MISTAKES` Barlow Condensed ExtraBold 22 pt `#E05C5C`.

| Mistake | Consequence |
|---|---|
| No agitation during spray | Clear binder sprayed; zero zinc in film; no galvanic protection |
| Over-application of IOZ (> 5 mils) | Mud cracking during cure -- must strip and reapply |
| Wrong mix ratio (2K primers) | Undercure (too little hardener) or brittleness (too much) |
| Spray in high wind | DFT variation, dry spray, overspray waste |
| Skip stripe coat on edges | Thin film on edges, welds, bolts -- first point of failure |

Each: small card, fill `#1E2435`, left accent `#E05C5C`. Mistake: Barlow SemiBold 14 pt `#E05C5C`. Consequence: Inter Regular 12 pt `#F0EDE8`.

---

### ZONE 7 -- Footer

Standard. Title: `Application -- Priming`. Version `v1.0 -- 2026`.
Disclaimer note: `Source: General industry knowledge; ASTM D520/D521; SSPC-PS 12.01; MIL primer specs; Watson Research Brief.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Application Priming -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster is all about the application parameters that separate a properly applied primer from a "we sprayed something on it" job. The three-column hero makes the IOZ/OZ/Epoxy comparison impossible to miss. The agitation callout gets the big-stat treatment because it is the single most common cause of zinc-rich primer failure in the field -- shops that do not agitate continuously are spraying expensive varnish. The aerospace sidebar keeps the poster relevant for aerospace shops where primer DFT is measured in tenths of a mil.

---

*Alaina -- Poster #709 -- Construction Workup v1.0 -- 2026-04-26*
