---
Project: Plating Posters Inc
Poster Number: 372
Title: "Safety & PPE -- Descaling Operations"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster CT-5 technical reference (descaling / heavy oxide removal)"
Technical Source: OSHA 29 CFR 1910.95 (noise), 29 CFR 1910.1025 (lead), SSPC/NACE blast safety standards. Covers mechanical and chemical descaling hazards.
Process Scope: Descaling safety -- mechanical blasting hazards, chemical descaling hazards, PPE requirements
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Descaling
  - Safety
  - PPE
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT05
---

# Poster #372 -- Construction Workup
## Safety & PPE -- Descaling Operations

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Descaling is one of the highest-hazard operations in a finishing shop. Between airborne particulate from blasting, noise exposure above 85 dBA, molten salt at 400-500 C, and strong oxidizer chemistry, there is a lot that can go wrong. This poster splits the hazard landscape into two clear domains: mechanical and chemical. Every hazard gets a control measure. Every PPE item gets a context.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Dual hazard domain layout (Block B -- HERO):** Two side-by-side panels -- left for mechanical hazards, right for chemical hazards. Each panel is a callout box with hazard rows inside.

2. **PPE visual grid (Block D):** Six PPE items in a 3x2 grid, each with an icon placeholder, item name, and context note.

3. **Emergency procedures callout (Block E):** Coral-tinted callout box with first-aid procedures.

4. **OSHA reference strip (Block F):** Key regulatory citations in a horizontal strip.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 16.5" / 22.5" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- DUAL HAZARD PANELS / HERO (2.9"--16.5" / ~13.6" tall)
  Block B: Left -- Mechanical Descaling Hazards (5 rows)
  Block C: Right -- Chemical Descaling Hazards (4 rows)

ZONE 3 -- PPE REQUIREMENTS GRID (16.5"--22.5" / ~6.0" tall)
  Block D: 3x2 PPE grid (6 items)

ZONE 4 -- EMERGENCY PROCEDURES (22.5"--28.5" / ~6.0" tall)
  Block E: Emergency callout (skin, eye, spill, thermal burn)

ZONE 5 -- OSHA / REGULATORY STRIP (28.5"--32.5" / ~4.0" tall)
  Block F: Key OSHA citations and prohibited media note

ZONE 6 -- FOOTER BAND (32.5"--36.0")
  Block G: Standard footer
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `DESCALING SAFETY` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Safety & PPE -- Mechanical and Chemical Descaling Operations` -- 32 pt `#E05C5C` (Coral). Y: 1.5".
**Tagline:** `Airborne dust, molten salt, strong oxidizers, and noise above 100 dBA. Descaling demands respect -- suit up or sit out.` -- 20 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Dual Hazard Panels (HERO)

**Section label:** Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> KNOW YOUR HAZARDS -- TWO DOMAINS

---

**BLOCK B -- Mechanical Descaling Hazards (Left Panel)**

Rounded rect, X: 0.5", Y: 3.8", W: 11.0", H: 12.2", fill `#1E2435`, radius 8.
Left accent: 0.06" `#2EC4B6`.
Title: `MECHANICAL DESCALING` -- Barlow SemiBold, 22 pt, `#2EC4B6`.

Five hazard rows inside (each row H: 2.0", alternating `#1E2435` / `#252B3D`):

| Row | Hazard | Source | Control |
|---|---|---|---|
| 1 | Airborne Particulate | Blasting, tumbling, grinding -- metal dust, abrasive dust, oxide dust | Enclosed cabinet or room; HEPA dust collection; P100 respirator minimum |
| 2 | Noise (> 85 dBA) | Blast equipment, tumbling barrels | Hearing protection required (OSHA 29 CFR 1910.95); earplugs + muffs for > 100 dBA |
| 3 | Silicosis Risk | Silica sand media -- PROHIBITED in many jurisdictions | Use non-silica media only: steel shot, steel grit, aluminum oxide, garnet, glass bead |
| 4 | Projectile Hazard | High-velocity abrasive particles | Full-body protection; face shield; blast suit for open blasting |
| 5 | Lead / Heavy Metal Dust | Blasting painted or coated parts; lead alloy castings | OSHA lead standard (29 CFR 1910.1025); air monitoring; medical surveillance |

Per row:
- Hazard: Barlow SemiBold, 15 pt, `#E05C5C`
- Source: Inter Regular, 12 pt, `#F0EDE8` at 80%
- Control: Inter Medium, 12 pt, `#27AE60`

---

**BLOCK C -- Chemical Descaling Hazards (Right Panel)**

Rounded rect, X: 12.0", Y: 3.8", W: 11.5", H: 12.2", fill `#1E2435`, radius 8.
Left accent: 0.06" `#E8A020`.
Title: `CHEMICAL DESCALING` -- Barlow SemiBold, 22 pt, `#E8A020`.

Four hazard rows inside:

| Row | Hazard | Source | Control |
|---|---|---|---|
| 1 | Alkaline Permanganate | KMnO4 is a strong oxidizer; NaOH caustic burns; skin staining from permanganate | Chemical splash goggles + face shield; neoprene gloves; chemical apron |
| 2 | Molten Salt (400--500 C) | Extreme thermal burn risk; fume generation; water contact = violent steam explosion | Face shield + heat-resistant suit; fume extraction; NEVER introduce wet parts |
| 3 | Acid Pickle Hazards | HCl and H2SO4 fumes; skin/eye burns; hydrogen embrittlement on high-strength steel | Ventilation; splash goggles; nitrile or neoprene gloves; see Cluster 3/4 posters |
| 4 | Temperature Hazard | Chemical baths at 80--95 C (175--205 F) for alkaline permanganate | Thermal-resistant gloves; long-handled tongs; steam/mist inhalation protection |

Per row: same styling as Block B.

---

### ZONE 3 -- PPE Requirements Grid

**Section label:** Centered. Y: 16.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> REQUIRED PPE -- DESCALING OPERATIONS

---

**BLOCK D -- 3x2 PPE Grid**

Y: 17.4" to 22.3". Six cards in 3 columns x 2 rows. Gap: 0.33".

Each card: Rounded rect, W: 7.33", H: 2.2", fill `#1E2435`, radius 6, top accent 3 pt `#E05C5C`.

| Position | Item | Context |
|---|---|---|
| R1C1 | Blast Hood / Face Shield | With neck protection for open blasting |
| R1C2 | Respiratory Protection | P100 minimum (cabinet); supplied air (open blast) |
| R1C3 | Hearing Protection | Earplugs + muffs combined for > 100 dBA environments |
| R2C1 | Blast Suit (Leather/Canvas) | Full-body coverage for open blasting operations |
| R2C2 | Chemical Splash Goggles | For all chemical descaling; face shield when charging |
| R2C3 | Chemical-Resistant Gloves | Neoprene or nitrile (15 mil min); heat-resistant for molten salt |

Per card:
- Item: Barlow SemiBold, 16 pt, `#F0EDE8`
- Context: Inter Regular, 13 pt, `#F0EDE8` at 70%
- Icon placeholder: 0.5" x 0.5" circle, fill `#3A4055`, centered left inside card

---

### ZONE 4 -- Emergency Procedures

**Section label:** Centered. Y: 22.7". Barlow Condensed ExtraBold, 28 pt, `#E05C5C`.

> EMERGENCY PROCEDURES

---

**BLOCK E -- Emergency Callout Box**

Rounded rect, X: 0.5", Y: 23.4", W: 23.0", H: 4.8", fill `#1E2435`, radius 8.
Left accent: 0.06" `#E05C5C`.
Border: 1 pt `#E05C5C` at 40%.

Four columns inside:

| Column | Emergency | Action |
|---|---|---|
| 1 | SKIN CONTACT (Chemical) | Flush immediately with water for 15+ minutes. Do NOT neutralize with acid. |
| 2 | EYE CONTACT | Flush with eyewash for 15+ minutes. Seek immediate medical attention. |
| 3 | THERMAL BURN (Molten Salt) | Cool with water. Do NOT apply ice. Cover with sterile dressing. Seek medical attention. |
| 4 | SPILL (Permanganate/Acid) | Contain with absorbent. Neutralize residual with dilute acid (permanganate) or soda ash (acid). |

Per column:
- Emergency type: Barlow SemiBold, 15 pt, `#E05C5C`
- Action: Inter Regular, 13 pt, `#F0EDE8`

---

### ZONE 5 -- OSHA / Regulatory Strip

**Section label:** Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

> KEY REGULATORY REFERENCES

---

**BLOCK F -- Regulatory Cards**

Y: 29.4" to 32.3". Three cards in a single row.

Each card: Rounded rect, W: 7.33", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E8A020`.

| Card | X | Reference | Detail |
|---|---|---|---|
| 1 | 0.5" | OSHA 29 CFR 1910.95 | Noise: hearing conservation program required at 85 dBA TWA. Blast operations routinely exceed 100 dBA. |
| 2 | 8.16" | OSHA 29 CFR 1910.1025 | Lead: applies when blasting lead-painted or lead-alloy parts. Air monitoring + medical surveillance. |
| 3 | 15.83" | SILICA SAND: PROHIBITED | Silica sand blasting banned in many jurisdictions due to silicosis risk. Use steel, garnet, aluminum oxide, or glass bead. |

Per card:
- Reference: JetBrains Mono Regular, 14 pt, `#E8A020`
- Detail: Inter Regular, 13 pt, `#F0EDE8`

---

### ZONE 6 -- Footer

Standard. Title: `Safety & PPE -- Descaling Operations`. Version `v1.0 -- 2026`.

Disclaimer: `Source: OSHA standards; SSPC safety guidelines; general industry knowledge. This poster is an educational reference tool -- consult your facility safety officer and applicable regulations for site-specific requirements.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Safety PPE Descaling -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Descaling safety is uniquely split between mechanical and chemical hazards -- most plating safety posters only deal with chemical risks. The mechanical side (noise, dust, projectiles) is an entirely different world. The molten salt hazard at 400-500 C deserves special visual weight -- this is "touch it and you're in the burn unit" territory. The silica sand prohibition callout must be prominent because some shops still have legacy sandblast equipment.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #372 -- Construction Workup v1.0*
*2026-04-26*
