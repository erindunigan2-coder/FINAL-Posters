---
Project: Plating Posters Inc
Poster Number: 466
Title: "Drying -- Electropolishing"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters — Watson Research Brief (Cluster 7, Sections 7.6--7.8)"
Technical Source: Post-electropolishing drying methods. Water spots on electropolished surfaces are highly visible defects on mirror-bright surfaces. Covers hot air blow-off, nitrogen purge, vacuum drying, and DI water final rinse requirements.
Process Scope: Electropolishing -- drying (Stage 8a of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Electropolishing
  - Drying
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #466 -- Construction Workup
## Drying -- Electropolishing

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Drying after electropolishing is not just "blow it off and call it done." On a mirror-bright electropolished surface, every water spot, mineral deposit, and fingerprint is visible. This poster covers the methods (hot air, nitrogen, vacuum), the prerequisites (DI water final rinse), and the handling rules (clean gloves, no bare-hand contact) that protect the finish all the way to packaging.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Drying methods comparison (Block B -- HERO):** Three-panel comparison of hot air, nitrogen blow-off, and vacuum/oven drying.
2. **Water quality prerequisite callout (Block C):** Why DI final rinse is mandatory before drying.
3. **Handling rules panel (Block D):** Clean-room-style handling practices for polished surfaces.
4. **Common drying defects (Block F):** Water spots, mineral stains, fingerprints.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE STRIP (2.9"--4.2")
  Stage 8 highlighted (Amber) -- Dry portion
ZONE 3 -- DRYING METHODS HERO (4.2"--14.5" / ~10.3")
  Block B: Three drying method panels
  Block C: DI water prerequisite callout
ZONE 4 -- HANDLING & CONTAMINATION CONTROL (14.5"--22.0" / ~7.5")
  Block D: Clean handling rules
  Block E: Contamination sources table
ZONE 5 -- DRYING DEFECTS (22.0"--28.5" / ~6.5")
  Block F: What goes wrong during drying
ZONE 6 -- PACKAGING NOTES (28.5"--32.5" / ~4.0")
  Block G: Protective packaging for dried EP parts
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `DRYING` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Electropolishing -- Stage 8 (Part 1) -- Water-Spot-Free Drying` -- 36 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `A mirror-bright surface shows everything. Every water spot, every mineral deposit, every fingerprint. Dry right, or dry over.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Sequence Orientation Strip

Stage 8 highlighted: fill `#E8A020`, text `#1A1F2E`. Label: `Dry / Inspect`. Others dimmed.

Below: `Before: Wet, rinsed, passivated surface --> After: Dry, spot-free, ready for inspection and packaging` -- Inter Regular, 13 pt, `#F0EDE8` at 60%.

---

### ZONE 3 -- Drying Methods Hero

**Section label:** `DRYING METHODS` -- Y: 4.4".

---

**BLOCK B -- Three Drying Method Panels (Y: 5.0" to 12.0")**

Three tall panels side by side:

**Panel 1 -- Hot Air (X: 0.5", W: 7.33"):**
- Rounded rect, H: 6.5", fill `#1E2435`, top accent 4 pt `#2EC4B6`
- Title: `HOT AIR BLOW-OFF` Barlow SemiBold 20 pt `#2EC4B6`
- Subtitle: `Most Common Industrial Method` Inter Medium 13 pt `#F0EDE8` at 60%

Parameters (JetBrains Mono 13 pt `#F0EDE8`, line height 155%):
```
Air source: Filtered compressed air
  or dedicated blower
Temperature: 60--100 C (140--212 F)
Filter: 5 um minimum; 0.3 um for
  pharma applications
Oil-free: MANDATORY -- oil mist from
  compressor = contamination
Pressure: 30--60 psi at nozzle
```

Pros/Cons (Inter Regular 12 pt):
```
+ Fast, inexpensive, widely available
+ Effective for most geometries
- Risk of recontamination from dirty air
- Difficult to reach recesses/blind holes
```

**Panel 2 -- Nitrogen Blow-Off (X: 8.33", W: 7.33"):**
- Rounded rect, H: 6.5", fill `#1E2435`, top accent 4 pt `#27AE60`
- Title: `NITROGEN (N2) BLOW-OFF` Barlow SemiBold 20 pt `#27AE60`
- Subtitle: `Pharma / Semiconductor Standard` Inter Medium 13 pt `#F0EDE8` at 60%

Parameters (JetBrains Mono 13 pt `#F0EDE8`, line height 155%):
```
Source: Clean, dry N2 supply
  (point-of-use filtered)
Temperature: Ambient to 60 C
Purity: 99.99% or better
Moisture: < 10 ppm dew point
Particle filter: 0.1--0.3 um
```

Pros/Cons (Inter Regular 12 pt):
```
+ Zero contamination risk (inert, clean)
+ No oxidation during drying
+ Required by many pharma/semi specs
- Higher cost than compressed air
- N2 asphyxiation hazard in enclosed areas
```

**Panel 3 -- Oven / Vacuum Dry (X: 16.16", W: 7.33"):**
- Rounded rect, H: 6.5", fill `#1E2435`, top accent 4 pt `#E8A020`
- Title: `OVEN / VACUUM DRY` Barlow SemiBold 20 pt `#E8A020`
- Subtitle: `Complex Geometries & Recesses` Inter Medium 13 pt `#F0EDE8` at 60%

Parameters (JetBrains Mono 13 pt `#F0EDE8`, line height 155%):
```
Oven temp: 80--120 C (175--250 F)
Time: 15--60 min
Atmosphere: Clean air or N2 purge
Vacuum option: 50--100 mbar, 40--80 C
  (lowers boiling point of water)
```

Pros/Cons (Inter Regular 12 pt):
```
+ Reaches blind holes and recesses
+ Uniform drying -- no flow marks
+ Vacuum reduces temperature needed
- Slower than blow-off methods
- Requires oven/vacuum chamber
- Handling hot parts adds risk
```

---

**BLOCK C -- DI Water Prerequisite (Y: 12.5" to 14.0")**

Rounded rect, X: 0.5", W: 23.0", H: 1.3", fill `#27AE60` at 15%, border 2 pt `#27AE60`.

Title: `PREREQUISITE: DI WATER FINAL RINSE BEFORE DRYING` Barlow SemiBold 16 pt `#27AE60`

Text (Inter Regular 14 pt `#F0EDE8`):

> City water contains dissolved minerals (Ca, Mg, silica) that precipitate as white spots when water evaporates. The ONLY way to prevent mineral water spots is to rinse with DI water (> 1 MOhm-cm) as the final step before drying. This applies to all drying methods. No DI rinse = guaranteed water spots on a mirror surface.

---

### ZONE 4 -- Handling & Contamination Control

**Section label:** `CLEAN HANDLING PRACTICES` -- Y: 14.7".

---

**BLOCK D -- Handling Rules Panel (Y: 15.3" to 19.5")**

Rounded rect, X: 0.5", W: 23.0", H: 4.0", fill `#1E2435`, left accent 0.06" `#E8A020`.

Title: `HANDLING ELECTROPOLISHED SURFACES` Barlow SemiBold 22 pt `#E8A020`

Two-column layout inside:

**Left column (X: 1.0", W: 10.5"):**
Title: `DO` Inter Medium 16 pt `#27AE60`
```
- Wear clean lint-free gloves (nitrile or nylon)
- Handle by edges or non-critical surfaces only
- Use clean, padded fixtures for transport
- Package immediately after drying and inspection
- Store in clean, dry, low-humidity environment
- Use protective film (polyethylene or VCI paper)
```

**Right column (X: 12.5", W: 10.5"):**
Title: `DO NOT` Inter Medium 16 pt `#E05C5C`
```
- Touch with bare hands (fingerprints = acid etch)
- Set on dirty, rough, or metallic surfaces
- Stack parts without separators
- Expose to shop air longer than necessary
- Use shop rags or contaminated cloths
- Allow condensation (move from cold to warm area)
```

Inter Regular 13 pt `#F0EDE8`, line height 160%.

---

**BLOCK E -- Contamination Sources Table (Y: 20.0" to 21.8")**

Table -- columns: Source (5.0") | Contaminant (6.0") | Effect on EP Surface (6.0") | Prevention (6.0")

| Source | Contaminant | Effect | Prevention |
|---|---|---|---|
| Bare hands | Skin oils, NaCl (sweat) | Fingerprints visible; salt causes pitting over time | Lint-free gloves always |
| Compressed air | Oil mist, moisture, particles | Hazy film; particle adhesion | Oil-free compressor; inline filters |
| Shop environment | Airborne dust, grinding swarf | Embedded particles; scratches | Package immediately |
| Packaging material | Sulfur compounds (rubber), PVC offgassing | Tarnishing, discoloration | Use PE film or VCI paper; avoid PVC |

Header: `#3A4055`. Data: Inter Regular 12 pt `#F0EDE8`.

---

### ZONE 5 -- Drying Defects

**Section label:** `DRYING DEFECTS` -- Y: 22.2".

---

**BLOCK F -- Four Defect Cards (Y: 22.9" to 28.0")**

2x2 grid:

| Position | Defect | Accent | Description | Root Cause | Fix |
|---|---|---|---|---|---|
| R1C1 | WATER SPOTS | `#E05C5C` | White circular marks where droplets evaporated | Mineral deposits from non-DI water | DI final rinse; never skip |
| R1C2 | FLOW MARKS | `#E8A020` | Visible streaks following gravity drainage | Uneven air flow; slow drainage | Tilt parts; use uniform air flow |
| R2C1 | HAZE / FILM | `#E8A020` | Dull, milky film across surface | Oil from compressed air; residual rinse chemicals | Oil-free air; verify rinse quality |
| R2C2 | FINGERPRINTS | `#E05C5C` | Visible print marks; may etch over time | Bare-hand contact during handling | Gloves mandatory; re-process if contaminated |

Each card: Rounded rect, W: 11.0", H: 2.3", fill `#1E2435`, left accent 0.06".

Interior per card:
- Defect name: Barlow SemiBold, 16 pt, accent color
- Description: Inter Regular, 12 pt, `#F0EDE8`
- Root Cause: Inter Regular, 12 pt, `#F0EDE8` at 70%
- Fix: Inter Medium, 12 pt, `#27AE60`

---

### ZONE 6 -- Packaging Notes

**Section label:** `PROTECTIVE PACKAGING` -- Y: 28.7".

---

**BLOCK G -- Two-Card Strip (Y: 29.4" to 32.0")**

**Card 1 -- Packaging Materials (X: 0.5", W: 11.0"):**
- Rounded rect, H: 2.3", fill `#1E2435`, left accent `#2EC4B6`
- Title: `RECOMMENDED PACKAGING` Barlow SemiBold 16 pt `#2EC4B6`
- Body (Inter Regular 13 pt `#F0EDE8`):
```
Polyethylene (PE) film or bags
VCI (vapor corrosion inhibitor) paper
Foam separators between stacked parts
Sealed plastic containers for small parts
Custom crates with padded inserts for large parts
```

**Card 2 -- Materials to Avoid (X: 12.5", W: 11.0"):**
- Rounded rect, H: 2.3", fill `#1E2435`, left accent `#E05C5C`
- Title: `PACKAGING TO AVOID` Barlow SemiBold 16 pt `#E05C5C`
- Body (Inter Regular 13 pt `#F0EDE8`):
```
PVC film (offgasses HCl -- causes tarnishing)
Rubber bands or rubber pads (sulfur attack)
Newspaper or printed cardboard (ink transfer)
Bare wood (tannic acid staining)
Metal-on-metal contact (galling, scratching)
```

---

### ZONE 7 -- Footer

Standard. Title: `Drying -- Electropolishing`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; ASME BPE; pharma and semiconductor clean-room drying practices. Specific drying requirements vary by application specification. Consult your quality engineer.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Drying Electropolishing -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster's hero message is "DI rinse before drying is not optional." The three-panel drying method comparison (Block B) gives shops a clear decision framework: hot air for general industrial, N2 for pharma/semi, oven for complex geometries. The handling rules (Zone 4) are equally important -- many shops ruin a perfect EP finish at the handling stage. The packaging notes (Zone 6) extend protection beyond the shop floor.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #466 -- Construction Workup v1.0*
*2026-04-26*
