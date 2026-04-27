---
Project: Plating Posters Inc
Poster Number: 62
Title: "Post Treatment -- Nickel (Watts)"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-04 technical reference (Watts nickel)"
  - "Watson Research Brief -- Electroplating Clusters EP-02 through EP-15"
Technical Source: Post-treatment options for Watts nickel plating. Covers chrome topcoat, gold topcoat, lacquer/anti-tarnish, duplex/triplex nickel systems, and hydrogen embrittlement baking.
Process Scope: Post-treatment for Watts nickel plating (Stage 7-8 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - NickelPlating
  - Watts
  - PostTreatment
  - ConstructionWorkup
  - Series2
  - ClusterEP04
---

# Poster #62 -- Construction Workup
## Post Treatment -- Nickel (Watts)

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 7-8 of 8. Nickel is rarely a final finish on its own -- it almost always receives a topcoat. This poster covers the four main post-treatment paths: decorative chrome (the most common), gold, lacquer/anti-tarnish, and the duplex/triplex nickel system. It also covers HE baking for high-strength steel. This poster is a decision map: which topcoat for which application?

Hero visual: a branching path diagram showing the four post-treatment options diverging from the nickel-plated part.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Branching path hero (Block B):** Central "nickel-plated part" node with four branches to chrome, gold, lacquer, and duplex/triplex. Built with rectangles and arrows.
2. **Duplex/triplex nickel callout (Block C):** Cross-section diagram showing multi-layer nickel systems.
3. **HE bake parameters panel (Block D):** Prominent callout for high-strength steel.
4. **Topcoat selection table (Block E):** Application x topcoat matrix.
5. **Failure modes strip (Block F):** 4 post-treatment failures.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.5" / 21.5" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stages 7-8 highlighted (Amber)
ZONE 3 -- BRANCHING PATH HERO (4.2"--15.5" / ~11.3")
  Block B: Four post-treatment paths
  Block C: Duplex/triplex nickel cross-section
ZONE 4 -- HE BAKE + TOPCOAT SELECTION (15.5"--21.5" / ~6.0")
  Block D: HE bake parameters
  Block E: Topcoat selection table
ZONE 5 -- DUPLEX/TRIPLEX DETAIL + SPECIFICATIONS (21.5"--27.0" / ~5.5")
  Block F: Multi-layer nickel system detail
  Block G: Relevant specs and standards
ZONE 6 -- FAILURE MODES + SAFETY (27.0"--32.5" / ~5.5")
  Block H: 4 post-treatment failures
  Block I: Safety
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `POST TREATMENT` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Nickel (Watts) -- Stages 7--8 of 8` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Nickel is rarely the last layer. Chrome, gold, lacquer, or more nickel -- pick the right topcoat for the job.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stages 7--8 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Freshly plated, rinsed nickel surface --> After: Finished part with topcoat, ready for inspection`

---

### ZONE 3 -- Branching Path Hero

**Section label:** `FOUR PATHS FROM NICKEL` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Branching Diagram**

Y: 5.0" to 13.0".

Central node (X: 9.0", Y: 5.2", W: 6.0", H: 1.5"):
- Rounded rect, fill `#27AE60` at 30%, border 2 pt `#27AE60`, radius 8
- Text: `WATTS NICKEL DEPOSIT` Barlow SemiBold 20 pt `#27AE60`
- Subtext: `Semi-bright or bright` Inter Regular 13 pt `#F0EDE8` at 60%

Four branch nodes below, connected by arrows:

| Path | X | Y | W | H | Accent | Title |
|---|---|---|---|---|---|---|
| Chrome | 0.5" | 7.5" | 5.5" | 4.5" | `#2EC4B6` | DECORATIVE CHROME |
| Gold | 6.5" | 7.5" | 5.0" | 4.5" | `#E8A020` | GOLD PLATE |
| Lacquer | 12.0" | 7.5" | 5.5" | 4.5" | `#27AE60` | LACQUER / ANTI-TARNISH |
| Duplex/Triplex | 18.0" | 7.5" | 5.5" | 4.5" | `#C8D0D8` | MULTI-LAYER NICKEL |

Each box: Rounded rect, fill `#1E2435`, left accent 0.06".

*Chrome box:*
- `Decorative Cr over bright Ni` Barlow SemiBold 14 pt `#2EC4B6`
- `0.25--0.75 microns Cr thickness`
- `150--200 ASF, 105--115 F`
- `Blue-white mirror finish`
- `THE most common nickel topcoat`
- `Move from Ni to Cr in <30 sec`

*Gold box:*
- `Gold over Ni undercoat` Barlow SemiBold 14 pt `#E8A020`
- `Electronics, connectors, jewelry`
- `Hard gold: 50--200 microinch`
- `Decorative gold: flash to 10 microinch`
- `Ni provides barrier + leveling`

*Lacquer box:*
- `Clear or tinted lacquer` Barlow SemiBold 14 pt `#27AE60`
- `Anti-tarnish protection`
- `Spray, dip, or electrophoretic`
- `Satin/matte Ni -- often used as-is for hardware`
- `DI rinse + full dry before lacquer`

*Duplex/Triplex box:*
- `Multi-layer Ni system` Barlow SemiBold 14 pt `#C8D0D8`
- `Semi-bright + bright Ni layers`
- `Corrosion potential difference = sacrificial protection`
- `Then chrome on top`
- `Automotive bumpers, exterior trim`

**BLOCK C -- Duplex/Triplex Cross-Section (Y: 13.2" to 15.3")**

Full-width callout showing stacked layers:

Horizontal bar diagram showing deposit cross-section (bottom to top):
- `SUBSTRATE (Steel)` -- fill `#3A4055`, H: 0.4"
- `SEMI-BRIGHT Ni (15--25 microns)` -- fill `#27AE60` at 30%, H: 0.35"
- `HIGH-S STRIKE (0.5--1.0 micron) [triplex only]` -- fill `#E8A020` at 30%, H: 0.15"
- `BRIGHT Ni (5--15 microns)` -- fill `#27AE60` at 50%, H: 0.3"
- `CHROME (0.25--0.75 microns)` -- fill `#2EC4B6` at 40%, H: 0.1"

Labels: JetBrains Mono 12 pt. Arrow between semi-bright and bright: `Potential difference drives sacrificial corrosion of bright Ni before semi-bright` Inter Medium 12 pt `#E8A020`.

---

### ZONE 4 -- HE Bake + Topcoat Selection

**Two-column layout (Y: 15.7" to 21.3"):**

**Left -- HE Bake (X: 0.5", W: 11.0"):**

- Rounded rect, fill `#E05C5C` at 12%, border 2 pt `#E05C5C`, radius 8
- Title: `HYDROGEN EMBRITTLEMENT BAKE` Barlow Condensed ExtraBold 22 pt `#E05C5C`

| Parameter | Value |
|---|---|
| Temperature | 375 +/- 25 F (190 +/- 14 C) |
| Time | 3--24 hours (specification-dependent) |
| Time to oven | Within 4 hours of plating (ASTM B850) |
| Applies to | Steel >31 HRC or >1000 MPa UTS |
| Surface-hardened parts | Bake based on case hardness, not core |

JetBrains Mono 14 pt for values. Inter Medium 13 pt for labels.

Bottom warning: `HE failure is delayed and catastrophic. Parts pass inspection, go into service, and fail without warning. Baking is not optional for high-strength steel.` Inter Medium 13 pt `#E05C5C`.

**Right -- Topcoat Selection Table (X: 12.5", W: 11.0"):**

| Application | Recommended Topcoat | Notes |
|---|---|---|
| Decorative trim | Chrome over bright Ni | Standard automotive/appliance |
| Automotive bumpers | Chrome over duplex/triplex Ni | Maximum corrosion resistance |
| Electronics connectors | Gold over Ni | Contact resistance, corrosion |
| Architectural hardware | Satin Ni + lacquer | Or satin Ni as-is |
| Industrial wear | Bright Ni alone (sometimes) | Add anti-tarnish if cosmetic |
| Aerospace | Per specification | Often bare Ni or chrome per AMS |

---

### ZONE 5 -- Duplex/Triplex Detail + Specifications

**Two-column layout (Y: 21.7" to 26.8"):**

**Left -- Multi-Layer Nickel (X: 0.5", W: 11.0"):**

- Rounded rect, fill `#1E2435`, left accent `#C8D0D8`
- Title: `DUPLEX AND TRIPLEX NICKEL SYSTEMS` Barlow SemiBold 18 pt `#C8D0D8`

| System | Structure | Purpose |
|---|---|---|
| Duplex | Semi-bright Ni + Bright Ni | Potential difference drives sacrificial protection |
| Triplex | Semi-bright + High-S strike + Bright Ni | Enhanced corrosion resistance |

Body: `The semi-bright layer contains no sulfur (no secondary brightener). The bright layer contains sulfur from Class II brightener decomposition. This sulfur difference creates a 100--150 mV potential difference that causes the bright layer to corrode sacrificially, protecting the semi-bright undercoat and substrate. The high-S strike in triplex systems creates an additional potential step that further improves performance.` Inter Regular 13 pt `#F0EDE8`.

**Right -- Specifications (X: 12.5", W: 11.0"):**

- Rounded rect, fill `#1E2435`, left accent `#2EC4B6`
- Title: `RELEVANT SPECIFICATIONS` Barlow SemiBold 18 pt `#2EC4B6`

| Spec | Coverage |
|---|---|
| ASTM B689 | Electroplated Engineering Nickel Coatings |
| ASTM B456 | Electrodeposited Coatings of Nickel Plus Chromium |
| AMS 2403 | Nickel Plating (General Purpose) |
| AMS 2424 | Nickel Plating (Low Stress, High Ductility) |
| ASTM B850 | Post-Coating Treatments -- HE Relief |
| AMS 2759/9 | HE Relief Baking |

JetBrains Mono 12 pt for spec codes. Inter Regular 12 pt for descriptions.

---

### ZONE 6 -- Failure Modes + Safety

**Two-column layout (Y: 27.2" to 32.3"):**

**Left -- 4 Post-Treatment Failures (X: 0.5", W: 14.0"):**

| Failure | Root Cause | Effect |
|---|---|---|
| Chrome peeling from nickel | Nickel passivated before chrome (delay, air exposure) | Chrome flakes off in sheets |
| Tarnished nickel (no topcoat) | Exposed bright Ni in humid environment | Yellow/brown discoloration |
| Lacquer blistering | Salt residue under lacquer from poor rinsing | Cosmetic defect, customer rejection |
| HE field failure | Bake missed, insufficient time, or delayed beyond 4 hr | Catastrophic brittle fracture in service |

Cards: fill `#1E2435`, left accent `#E05C5C`.

**Right -- Safety (X: 15.5", W: 8.0"):**

> - Chrome plating (hexavalent): OSHA PEL 5 microg/m3. Known carcinogen. Full ventilation and mist suppression required.
> - HE bake ovens: burn hazard. PPE for oven operations.
> - Lacquer solvents: flammable. Ventilation and fire suppression required.
> - Nickel dermatitis: continued risk when handling plated parts.

---

### ZONE 7 -- Footer

Standard footer. Title: `Post Treatment -- Nickel (Watts)`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Post Treatment Nickel Watts -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster is the "what happens after nickel?" decision guide. The branching path hero makes the four options immediately clear. The duplex/triplex cross-section is a visual that shops rarely see explained well -- the potential difference concept is the key insight and should be visually prominent. The HE bake callout is deliberately alarming because HE failures kill people. The specification table is a daily reference for quality engineers. This poster bookends the Watts cluster with Poster #55 (process flow) and gives the complete picture.

---

*Alaina -- Plating Posters Inc Creative Lead*
*Poster #62 -- Construction Workup v1.0*
*2026-04-26*
