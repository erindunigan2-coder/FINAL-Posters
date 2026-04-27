---
Project: Plating Posters Inc
Poster Number: 386
Title: "Safety & PPE -- Ultrasonic Cleaning"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster CT-7 technical reference (ultrasonic cleaning)"
  - "Chemical Treatment Clusters — Watson Research Brief"
Process Scope: Ultrasonic cleaning -- safety hazards and personal protective equipment
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - UltrasonicCleaning
  - Safety
  - PPE
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT07
---

# Poster #386 -- Construction Workup
## Safety & PPE -- Ultrasonic Cleaning

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Ultrasonic cleaning has a unique hazard profile that most operators underestimate. The #1 rule: NEVER immerse bare hands in an operating ultrasonic tank. Cavitation will damage tissue. Beyond that, the noise, chemical mist, and hot solution hazards demand specific PPE. This poster makes the hazards visible and the PPE requirements unmistakable.

Hero visual: a large PPE figure with callout lines to each piece of required equipment, paired with a hazard matrix showing the five primary risks.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **PPE figure (Block B -- HERO):** Silhouette figure with callout lines to hearing protection, goggles, chemical-resistant gloves, apron, and closed-toe shoes. Built with rectangles and lines -- no raster images.
2. **Hazard matrix (Block D):** Five-row table of hazards, sources, and controls.
3. **"Never Do" warning strip (Block E):** Coral-tinted danger callouts for the most critical prohibitions.
4. **Chemical-specific cross-reference (Block F):** Reminder that chemical hazards depend on the cleaning solution -- refer to alkaline or solvent cluster posters.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts per series design system.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 16.0" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 2-position: "Safety applies to ALL stages"
ZONE 3 -- PPE FIGURE HERO (4.2"--16.0" / ~11.8")
ZONE 4 -- HAZARD MATRIX (16.0"--22.0" / ~6.0")
ZONE 5 -- "NEVER DO" WARNING STRIP (22.0"--28.5" / ~6.5")
ZONE 6 -- CHEMICAL CROSS-REFERENCE + NOISE DATA (28.5"--32.5" / ~4.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `SAFETY & PPE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Ultrasonic Cleaning -- Hazards You Cannot See or Hear` -- 36 pt `#E05C5C` (Coral). Y: 1.5".
**Tagline:** `Cavitation cleans parts brilliantly. It also damages skin, generates aerosol, and produces noise above 90 dBA. Respect the tank.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Y: 2.9" to 4.2". Full-width bar: `#252B3D`.

- Text centered: `SAFETY APPLIES TO ALL 6 STAGES -- THESE RULES ARE NON-NEGOTIABLE` Barlow Condensed ExtraBold 20 pt `#E05C5C`
- Below: `Refer to your facility SDS for solution-specific hazard information` Inter Regular 14 pt `#F0EDE8` at 60%

---

### ZONE 3 -- PPE Figure Hero

**Section label:** `REQUIRED PERSONAL PROTECTIVE EQUIPMENT` -- Y: 4.4".

**BLOCK B -- PPE Figure with Callouts**

Y: 5.0" to 15.8".

**Central figure:**
- Simplified operator silhouette built from rectangles (head circle, torso rect, arm rects, leg rects)
- Position: centered horizontally, X: ~10.0", Y: 5.5"
- Fill: `#3A4055`, border 2 pt `#C8D0D8`
- Height: ~9.0"

**Five PPE callout boxes** positioned around the figure, connected by 2 pt `#C8D0D8` lines:

| PPE Item | Position | Accent | Content |
|---|---|---|---|
| HEARING PROTECTION | Upper-left (X: 0.5", Y: 5.5") | `#E05C5C` | `Earplugs minimum; muffs for extended exposure. Ultrasonic tanks produce > 90 dBA harmonics. Tank covers reduce airborne noise significantly.` |
| SAFETY GLASSES / GOGGLES | Upper-right (X: 16.0", Y: 5.5") | `#E8A020` | `Chemical splash and aerosol protection. Cavitation at liquid surface creates fine mist. Goggles preferred when tank is open.` |
| CHEMICAL-RESISTANT GLOVES | Mid-left (X: 0.5", Y: 9.5") | `#E05C5C` | `Matched to cleaning solution -- nitrile for most alkaline; check SDS. CRITICAL: Gloves for handling parts and baskets -- NEVER for reaching into an operating tank.` |
| CHEMICAL APRON | Mid-right (X: 16.0", Y: 9.5") | `#2EC4B6` | `Protection from splash during loading/unloading. Standard chemical-resistant apron appropriate to the cleaning solution.` |
| CLOSED-TOE SHOES | Bottom-center (X: 8.0", Y: 13.5") | `#2EC4B6` | `Chemical-resistant footwear. Hot alkaline solution splashes are common during basket transfer.` |

Each callout box:
- Rounded rect, W: 7.0", H: 2.5", fill `#1E2435`, left accent 0.06" in accent color, radius 6
- PPE name: Barlow SemiBold, 18 pt, accent color
- Description: Inter Regular, 13 pt, `#F0EDE8`

---

### ZONE 4 -- Hazard Matrix

**Section label:** `ULTRASONIC-SPECIFIC HAZARDS` -- Y: 16.2".

**BLOCK D -- Five-Row Hazard Table**

Y: 16.8" to 21.8". Column widths (23.0" total):
- Hazard (4.0") | Source (6.0") | Risk Level (3.0") | Control (10.0")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

| Hazard | Source | Risk | Control |
|---|---|---|---|
| Noise (airborne) | Transducers at 20--40 kHz produce harmonics > 90 dBA | HIGH | Hearing protection; tank covers; limit exposure time |
| Chemical mist/aerosol | Cavitation at liquid surface atomizes solution | MODERATE | Tank covers; local exhaust ventilation for volatile/hazardous chemicals |
| Burns (hot solution) | Operating temp 120--150 F (50--65 C) | MODERATE | Gloves; avoid reaching into tank; proper basket handling |
| Cavitation tissue damage | Direct skin contact with operating ultrasonic liquid | SEVERE | NEVER immerse hands in operating tank |
| Ergonomic strain | Repetitive loading/unloading of baskets | LOW--MOD | Proper work height; mechanical assist for heavy loads |

Risk level color coding:
- SEVERE: `#E05C5C` bold
- HIGH: `#E05C5C`
- MODERATE: `#E8A020`
- LOW--MOD: `#2EC4B6`

Data: Inter Regular, 13 pt. Hazard names: Barlow SemiBold 14 pt.

---

### ZONE 5 -- "Never Do" Warning Strip

**Section label:** `ABSOLUTE PROHIBITIONS` -- Y: 22.2". `#E05C5C`.

**BLOCK E -- Three Warning Cards**

Y: 22.8" to 28.3". Three large cards in a single row.

Each card: Rounded rect, W: 7.33", H: 5.3", fill `#E05C5C` at 10%, border 2 pt `#E05C5C`, radius 8.

| Card | X | Prohibition | Explanation |
|---|---|---|---|
| 1 | 0.5" | NEVER IMMERSE BARE HANDS | Cavitation damages tissue on contact -- pain, redness, cellular damage. This is not optional safety advice. It is a hard biological limit. Use baskets, fixtures, or tongs exclusively. |
| 2 | 8.17" | NEVER OPERATE WITHOUT COVER (when possible) | Open tanks generate airborne ultrasonic noise and chemical aerosol. Covers reduce noise by 10--15 dB and virtually eliminate mist. |
| 3 | 15.83" | NEVER MIX INCOMPATIBLE SOLUTIONS | If switching from alkaline to acid (or vice versa) in the same tank, drain, rinse, and neutralize completely. Residual alkaline + fresh acid = violent reaction. |

Interior per card:
- Triangle warning icon: built from three lines, 0.5" tall, stroke 3 pt `#E05C5C`, positioned top-center
- Prohibition: Barlow Condensed ExtraBold, 22 pt, `#E05C5C`
- Explanation: Inter Regular, 14 pt, `#F0EDE8`

---

### ZONE 6 -- Chemical Cross-Reference + Noise

**Two-column layout (Y: 28.7" to 32.3"):**

**Left -- Chemical Cross-Reference (X: 0.5", W: 11.0"):**

Rounded rect, fill `#1E2435`, left accent `#E8A020`.

- Title: `CHEMICAL HAZARDS DEPEND ON YOUR SOLUTION` Barlow SemiBold 18 pt `#E8A020`
- Body (Inter Regular 14 pt `#F0EDE8`):
  - `Alkaline cleaner? --> Refer to Alkaline Cleaning Safety poster`
  - `Solvent-based? --> Refer to Solvent Degreasing Safety poster`
  - `Always check the SDS for YOUR specific product`
  - `PPE must match the chemical, not just the ultrasonic process`

**Right -- Noise Reference (X: 12.0", W: 11.5"):**

Rounded rect, fill `#1E2435`, left accent `#2EC4B6`.

- Title: `NOISE EXPOSURE REFERENCE` Barlow SemiBold 18 pt `#2EC4B6`
- Data (JetBrains Mono 13 pt `#F0EDE8`):
  - `85 dBA -- hearing protection recommended`
  - `90 dBA -- hearing protection REQUIRED (OSHA)`
  - `Typical open ultrasonic tank: 85--100+ dBA`
  - `With cover: reduces 10--15 dB`
  - `Measure YOUR tank -- don't guess`

---

### ZONE 7 -- Footer

Standard. Title: `Safety & PPE -- Ultrasonic Cleaning`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Safety requirements shown are general industry guidelines. Consult your facility safety officer, equipment manufacturer SDS, and applicable OSHA standards for site-specific requirements.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Safety PPE Ultrasonic -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The single most important message on this poster: NEVER put your hands in an operating ultrasonic tank. This must be the visually dominant element. The hearing protection requirement is the second most commonly overlooked hazard -- most operators don't realize how loud these tanks are, especially at 20-40 kHz where harmonics fall in the audible range.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #386 -- Construction Workup v1.0*
*2026-04-26*
