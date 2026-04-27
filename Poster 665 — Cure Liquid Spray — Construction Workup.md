---
Project: Plating Posters Inc
Poster Number: 665
Title: "Cure -- Liquid Spray Painting"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting & Organic Coating Clusters — Watson Research Brief, Cluster 2.8"
Technical Source: Cure methods for liquid spray painting -- air dry, force dry, low-temp bake, high-temp bake, 2K chemical cure, and UV cure. Includes pot life management for 2K systems and VOC compliance references.
Process Scope: Cure for liquid spray painting (Stage 7 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - LiquidSprayPainting
  - Cure
  - ConstructionWorkup
  - PaintingClusters
  - ClusterPC02
---

# Poster #665 -- Construction Workup
## Cure -- Liquid Spray Painting

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 7 of 8. Liquid spray painting offers six cure methods -- the widest range of any coating process. From 7-day air-dry alkyds to 10-second UV cure, the cure method defines the production flow. The hero is a six-method comparison table. Pot life management for 2K systems gets its own callout because mixed epoxy or urethane that gels in the pot is the most expensive waste in a paint shop. VOC compliance rounds out the regulatory awareness.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Six cure methods comparison (Block B -- HERO):** Air dry, force dry, low-temp bake, high-temp bake, 2K chemical cure, UV cure.
2. **Pot life management (Block C):** 2K epoxy and 2K urethane pot life windows.
3. **VOC compliance (Block D):** EPA regulations and SCAQMD reference.
4. **Defect grid (Block F):** 6 cure defects.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.5" / 21.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage highlighted: Cure (Amber)
ZONE 3 -- SIX CURE METHODS HERO (4.2"--15.5" / ~11.3")
ZONE 4 -- POT LIFE MANAGEMENT (15.5"--21.5" / ~6.0")
ZONE 5 -- VOC COMPLIANCE (21.5"--26.5" / ~5.0")
ZONE 6 -- DEFECT GRID (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CURE` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Liquid Spray Painting -- Six Methods from Air Dry to UV Cure` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Seven days for an alkyd. Ten seconds for a UV acrylate. The cure method defines the production line -- choose the chemistry that fits your throughput.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage highlighted: Cure -- fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Flashed wet film with solvents partially evaporated --> After: Fully cured, cross-linked or dried film ready for inspection`

---

### ZONE 3 -- Six Cure Methods Hero

**Section label:** `SIX CURE METHODS -- THE WIDEST RANGE IN COATING` -- Y: 4.4".

**BLOCK B -- Six Cards in 3x2 Grid (Y: 5.0" to 15.0")**

**Top Row:**

*Air Dry (X: 0.5", W: 7.33"):*
- Fill: `#1E2435`, top accent `#27AE60`
- Title: `AIR DRY (AMBIENT)` -- Barlow SemiBold, 20 pt, `#27AE60`
- Parameters (JetBrains Mono 12 pt):
```
Temperature: 65--85 F (18--29 C)
Time: 1--7 days to full cure
Systems: Alkyds, latex, moisture-cure PU
```
- Key: `No oven required; simplest setup`
- Limitation: `Longest cure; dust/handling risk during drying`

*Force Dry (X: 8.17", W: 7.33"):*
- Fill: `#1E2435`, top accent `#E8A020`
- Title: `FORCE DRY` -- Barlow SemiBold, 20 pt, `#E8A020`
- Parameters:
```
Temperature: 140--180 F (60--82 C)
Time: 30--60 min
Systems: Alkyds, modified acrylics
```
- Key: `Accelerates air-dry coatings`
- Limitation: `Does not fully cross-link; supplements natural cure`

*Low-Temp Bake (X: 15.83", W: 7.67"):*
- Fill: `#1E2435`, top accent `#2EC4B6`
- Title: `LOW-TEMP BAKE` -- Barlow SemiBold, 20 pt, `#2EC4B6`
- Parameters:
```
Temperature: 200--250 F (93--121 C)
Time: 20--30 min
Systems: Modified alkyds, polyesters
```
- Key: `True bake cure; faster throughput than force dry`

**Bottom Row:**

*High-Temp Bake (X: 0.5", W: 7.33"):*
- Fill: `#1E2435`, top accent `#E8A020`
- Title: `HIGH-TEMP BAKE` -- Barlow SemiBold, 20 pt, `#E8A020`
- Parameters:
```
Temperature: 250--350 F (121--177 C)
Time: 15--30 min
Systems: Thermoset acrylics, baking enamels
```
- Key: `Full thermoset cross-linking; hardest, most durable films`
- Limitation: `Heat-sensitive substrates excluded`

*2K Chemical Cure (X: 8.17", W: 7.33"):*
- Fill: `#1E2435`, top accent `#27AE60`
- Title: `2K CHEMICAL CURE` -- Barlow SemiBold, 20 pt, `#27AE60`
- Parameters:
```
Temperature: Ambient to 140 F
Time: Pot-life dependent (15 min--8 hr)
Systems: 2K epoxy, 2K urethane
```
- Key: `High performance at low temperature`
- Warning (Coral): `Mixed material must be used within pot life or discarded`

*UV Cure (X: 15.83", W: 7.67"):*
- Fill: `#1E2435`, top accent `#2EC4B6`
- Title: `UV CURE` -- Barlow SemiBold, 20 pt, `#2EC4B6`
- Parameters:
```
Temperature: Ambient (UV lamp exposure)
Time: 1--10 sec under lamp
Systems: UV acrylate (wood, plastic, printing)
```
- Key: `Fastest cure in industrial coating`
- Limitation: `Line-of-sight only; shadowed areas do not cure`

---

### ZONE 4 -- Pot Life Management

**Section label:** `POT LIFE -- THE 2K CLOCK IS TICKING` -- Y: 15.7".

**Two-column layout (Y: 16.3" to 21.3"):**

**Left -- Pot Life Table (X: 0.5", W: 11.0"):**

Title: `POT LIFE BY COATING TYPE` -- Barlow SemiBold, 18 pt, `#F0EDE8`

| System | Pot Life at 77 F | Temperature Effect |
|---|---|---|
| 2K Epoxy (polyamide) | 2--4 hours | Halves per 18 F rise |
| 2K Epoxy (amine-adduct) | 30 min--2 hours | Very temperature-sensitive |
| 2K Urethane (aliphatic) | 2--8 hours | Slower reaction than aromatic |
| 2K Urethane (aromatic) | 15 min--2 hours | Fast reaction; short window |

Data: JetBrains Mono 12 pt. Alternating rows: `#1E2435` / `#252B3D`.

**Right -- Pot Life Rules (X: 12.0", W: 11.5"):**

Callout box, fill `#1E2435`, border 2 pt `#E05C5C`.
Title: `POT LIFE RULES -- NO EXCEPTIONS` -- Barlow SemiBold, 20 pt, `#E05C5C`

Rules (Inter Medium 14 pt):
1. `Start the clock when components are mixed -- not when you start spraying`
2. `Mixed material that exceeds pot life = WASTE. Do not spray it.`
3. `Gelled material in the pot clogs spray equipment and produces defects`
4. `Hot weather shortens pot life dramatically -- mix smaller batches`
5. `Never pour unused mixed material back into fresh material`

---

### ZONE 5 -- VOC Compliance

**Section label:** `VOC COMPLIANCE -- KNOW YOUR LIMITS` -- Y: 21.7".

**Single wide callout (Y: 22.3" to 26.3", X: 0.5", W: 23.0"):**

Callout box, fill `#1E2435`, left accent `#E8A020`.
Title: `REGULATORY FRAMEWORK` -- Barlow SemiBold, 20 pt, `#E8A020`

Two-column content inside:

**Left sub-column:**
- `EPA 40 CFR Part 63, Subpart HHHHHH (6H):`
- `  NESHAP for paint stripping / misc surface coating (area sources)`
- `EPA 40 CFR Part 63, Subpart MMMM:`
- `  NESHAP for surface coating of misc metal parts (major sources)`

**Right sub-column:**
- `Typical VOC limits: 2.0--4.2 lb/gal (less water)`
- `SCAQMD Rule 1107 (So. California): strictest in the US`
- `Drives industry toward waterborne and high-solids`
- `HVLP spray required in most jurisdictions for compliance`

Bottom note: `Check your state and local air quality district for specific VOC limits. Federal limits are the floor, not the ceiling.` -- Inter Medium 13 pt `#E05C5C`

---

### ZONE 6 -- Defect Grid

**Section label:** `WHEN CURE GOES WRONG -- 6 DEFECTS` -- Y: 26.7".

**BLOCK F -- 3x2 Grid (Y: 27.3" to 32.3")**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | UNDERCURE (SOFT FILM) | `#E05C5C` | Insufficient time or temperature; expired pot life | Verify oven profile; check mixing ratio |
| R1C2 | OVERCURE (YELLOWING) | `#E8A020` | Excessive time or temperature in bake oven | Profile oven; reduce cycle time |
| R1C3 | SOLVENT POP | `#E05C5C` | Trapped solvent boiling during bake | Force flash before bake; slower oven ramp |
| R2C1 | GELLED MATERIAL | `#E8A020` | 2K material sprayed past pot life | Mix smaller batches; track pot life clock |
| R2C2 | POOR CHEMICAL RESISTANCE | `#E05C5C` | Incorrect mix ratio (off-ratio cure) | Verify A:B ratio by volume or weight per TDS |
| R2C3 | UV SHADOW CURE FAILURE | `#2EC4B6` | UV lamp cannot reach shadowed areas | Reorient parts; supplement with thermal cure |

Each card: Rounded rect W: 7.33", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06" in defect color.

---

### ZONE 7 -- Footer

Standard. Title: `Cure -- Liquid Spray Painting`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; EPA 40 CFR Part 63. Cure schedules and pot life values are product-specific -- consult manufacturer TDS. VOC limits vary by jurisdiction.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cure Liquid Spray -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The six cure methods span the entire industrial range -- from a week of air drying to 10 seconds under a UV lamp. The pot life management section is the practical anchor: 2K systems are the highest-performance liquid coatings, but the clock starts ticking the moment you mix, and mixed material past its pot life is expensive waste. The VOC compliance section connects cure chemistry to regulatory reality -- shops transitioning to waterborne or high-solids are doing so because of these rules.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #665 -- Construction Workup v1.0*
*2026-04-26*
