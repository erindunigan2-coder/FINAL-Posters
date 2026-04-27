---
Project: Plating Posters Inc
Poster Number: 92
Title: "Hard Chrome Main Tank"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-08 technical reference (hard chrome plating)"
  - "Watson Research Brief -- Electroplating Clusters"
Technical Source: Hard chrome plating main tank -- hexavalent CrO3 + H2SO4 (Sargent bath). CrO3 200--300 g/L, CrO3:SO4 ratio 100:1. Temperature 120--145 F, CD 150--400 ASF. Cathode efficiency only 10--18%. Known human carcinogen (OSHA PEL 5 ug/m3 Cr VI). The most chemistry-dangerous poster in the entire series.
Process Scope: Hard chrome plating main tank (Stage 5 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - HardChrome
  - Hexavalent
  - MainTank
  - ConstructionWorkup
  - ClusterEP08
---

# Poster #92 -- Construction Workup
## Hard Chrome Main Tank

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 5 of 8. This is the most hazardous plating bath in the entire poster series. The hard chrome tank contains hexavalent chromium (CrO3) -- a confirmed human carcinogen. Every design decision on this poster must balance technical completeness with safety prominence.

The bath chemistry is deceptively simple: chromic acid + sulfuric acid, maintained at a 100:1 CrO3:SO4 weight ratio. That ratio is THE critical control parameter. The cathode efficiency is brutally low (10--18%) -- most of the electrical energy goes to hydrogen evolution and trivalent chrome formation, not deposition. Despite this inefficiency, hard chrome produces the hardest electroplated coating available (800--1000 HV) with exceptional wear resistance.

Note: Stages 3--5 (reverse etch, polarity reversal, plating) all occur in the same tank. This poster covers the plating phase (Stage 5).

Hero visual: plating tank cross-section with CrO3:SO4 ratio as the central control parameter, conforming lead anodes, and a prominent safety banner.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Plating tank hero (Block B):** Tank cross-section with conforming lead anodes, workpiece, and labeled components.
2. **Bath chemistry table (Block C):** Conventional and high-concentration formulations.
3. **CrO3:SO4 ratio control panel (Block D):** The master control parameter with high/low consequences.
4. **Trivalent chrome (Cr3+) control callout (Block E).**
5. **Defect table (Block F):** 7 common defects.
6. **Safety banner in Zone 1 (Block A2):** Cr(VI) carcinogen warning -- same as Poster #87.
7. **Orientation strip:** Stage 5 highlighted (Emerald).

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.0" / 20.5" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline
  Block A2: Safety banner (Cr VI carcinogen warning)
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 5 highlighted (Emerald)
ZONE 3 -- PLATING TANK HERO + BATH CHEMISTRY (4.2"--14.0" / ~9.8")
  Block B: Tank cross-section
  Block C: Bath chemistry table (conventional + high-conc)
ZONE 4 -- CrO3:SO4 RATIO + Cr3+ CONTROL (14.0"--20.5" / ~6.5")
  Block D: CrO3:SO4 ratio control panel
  Block E: Trivalent chrome control
ZONE 5 -- DEFECTS + CONTAMINATION (20.5"--27.0" / ~6.5")
  Block F: Common defects table
  Block G: Contamination thresholds
ZONE 6 -- ANODE MANAGEMENT + SAFETY (27.0"--32.5" / ~5.5")
  Block H: Conforming anode management
  Block I: Safety and regulatory
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**BLOCK A -- Headline**

- Barlow Condensed ExtraBold, 72 pt, `#F0EDE8`, letter spacing -4. X: 0.5", Y: 0.5".
- Text: `HARD CHROME MAIN TANK`

**BLOCK A -- Subheading**

- Barlow SemiBold, 30 pt, `#27AE60`. X: 0.5", Y: 1.3".
- Text: `Hard Chrome -- Stage 5 of 8 -- Hexavalent Chromium Electrodeposition`

**BLOCK A -- Tagline**

- Barlow SemiBold, 18 pt, `#F0EDE8` at 65%. X: 0.5", Y: 2.0". W: 15.0".
- Text: `CrO3 + H2SO4 at 100:1. 800--1000 HV. 10--18% cathode efficiency. The hardest electroplate -- and the most hazardous chemistry in the shop.`

**BLOCK A2 -- Safety Banner**

- Position: X: 15.5". Y: 1.3". W: 8.0". H: 1.4".
- Rounded rect, fill `#E05C5C` at 15%, border 2 pt `#E05C5C`, radius 6
- Line 1: `HEXAVALENT CHROMIUM (Cr VI)` -- Barlow SemiBold, 16 pt, `#E05C5C`
- Line 2: `KNOWN HUMAN CARCINOGEN` -- Barlow Condensed ExtraBold, 14 pt, `#E05C5C`
- Line 3: `OSHA PEL: 5 ug/m3 | EPA NESHAP 40 CFR 63 Subpart N` -- JetBrains Mono Regular, 10 pt, `#E05C5C` at 80%

---

### ZONE 2 -- Orientation Strip

Stage 5 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Note below strip: `Stages 3--5 occur in the SAME TANK. Reverse etch (anodic) -> polarity reversal -> plating (cathodic).` Inter Medium 13 pt `#E8A020`.

---

### ZONE 3 -- Plating Tank Hero + Bath Chemistry

**Section label:** `THE HARD CHROME PLATING BATH` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Tank Cross-Section Diagram**

Y: 5.0" to 8.5". Full width.

Rounded rect representing tank (W: 23.0", H: 3.0"), fill `#252B3D`, border 2 pt `#27AE60`.

Inside tank:
- Conforming lead anodes (Pb-6%Sn): `Conforming lead alloy anodes -- shaped to match workpiece geometry`
- Workpiece (cathode, center): `Hard chrome deposits here`
- Solution level with fume suppressant layer: `Fume suppressant (PFAS-free fluorosurfactant)`
- Heater: `120--145 F (49--63 C)`
- Note: `NO air agitation -- blows Cr(VI) mist`
- Filtration: `Continuous, 10--25 micron (lead particle capture)`

Labels: JetBrains Mono 12 pt `#F0EDE8`. Component names: Barlow SemiBold 13 pt `#27AE60`.

**BLOCK C -- Bath Chemistry Table**

Y: 9.0" to 13.0".

Section sublabel: `BATH FORMULATION` Barlow SemiBold 18 pt `#27AE60`.

| Component | Conventional (Sargent) | High-Concentration |
|---|---|---|
| Chromic acid (CrO3) | 200--250 g/L (26--33 oz/gal) | 300--400 g/L (40--53 oz/gal) |
| Sulfuric acid (H2SO4) | 2.0--2.5 g/L | 3.0--4.0 g/L |
| CrO3:SO4 ratio (by weight) | 100:1 | 75:1 to 100:1 |
| Trivalent chromium (Cr3+) | 1--3% of CrO3 (2--5 g/L) | 2--5 g/L |

Data: JetBrains Mono 12 pt `#F0EDE8`. Headers: Barlow SemiBold 13 pt on `#3A4055`.

Below table:

Operating parameters summary (rounded rect, fill `#1E2435`, left accent `#27AE60`):
```
Temperature: 120--145 F (49--63 C); typical 130--135 F
Cathode CD: 150--400 ASF (16--43 A/dm2); typical 200--300 ASF
Voltage: 6--12 V
Cathodic efficiency: 10--18%
Plating rate at 200 ASF: ~1.0--1.5 mil/hr (25--38 microns/hr)
Plating rate at 300 ASF: ~1.5--2.2 mil/hr (38--56 microns/hr)
Agitation: Solution flow or mechanical; NEVER air
```
JetBrains Mono 12 pt `#F0EDE8`.

---

### ZONE 4 -- CrO3:SO4 Ratio + Cr3+ Control

**Section label:** `THE MASTER CONTROL PARAMETERS` -- Y: 14.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK D -- CrO3:SO4 Ratio Control Panel**

Y: 14.8" to 18.0".

Rounded rect, fill `#1E2435`, border 2 pt `#E8A020`, W: 23.0".
Title: `CrO3:SO4 RATIO -- THE SINGLE MOST IMPORTANT PARAMETER` Barlow SemiBold 18 pt `#E8A020`

Three horizontal zones within the panel:

- Left zone (too high): `> 125:1 (sulfate too low)` -- fill `#E05C5C` at 10%
  - `Milky deposits, poor coverage, poor hardness` Inter Regular 12 pt `#E05C5C`

- Center zone (optimal): `80:1 to 100:1` -- fill `#27AE60` at 15%, border 1 pt `#27AE60`
  - `OPTIMAL -- good coverage, full hardness, best efficiency` Barlow SemiBold 13 pt `#27AE60`

- Right zone (too low): `< 75:1 (sulfate too high)` -- fill `#E05C5C` at 10%
  - `Poor throwing power, burning, pitting, reduced efficiency` Inter Regular 12 pt `#E05C5C`

Adjustment notes below:
- `Add sulfate: dilute H2SO4` / `Remove sulfate: barium carbonate (BaCO3) -- precipitates BaSO4` JetBrains Mono 11 pt `#F0EDE8`

**BLOCK E -- Trivalent Chrome Control**

Y: 18.3" to 20.3".

Rounded rect, fill `#1E2435`, left accent `#2EC4B6`, W: 23.0".
Title: `TRIVALENT CHROMIUM (Cr3+) CONTROL` Barlow SemiBold 16 pt `#2EC4B6`

Body:
- `Must be present at 1--3% of total CrO3 (typically 2--5 g/L)` JetBrains Mono 12 pt `#F0EDE8`
- `Too low: poor throwing power, burning at HCD`
- `Too high (> 5% of CrO3): dramatically reduced efficiency, dull deposits, reduced hardness`
- `Reduce Cr3+: dilution or electrolytic oxidation with high anode area`
- `Increase Cr3+: add sugar (sucrose) or proprietary reducer`

---

### ZONE 5 -- Defects + Contamination

**Section label:** `COMMON DEFECTS AND CONTAMINATION` -- Y: 20.7". Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`.

**BLOCK F -- Common Defects Table**

Y: 21.3" to 24.5".

| Defect | Cause | Corrective Action |
|---|---|---|
| Burning (brown/black at HCD) | CD too high, temp too low, Cr3+ too high, sulfate too high | Reduce CD; raise temp; reduce Cr3+; check ratio |
| Milky/hazy deposit | CrO3:SO4 too high (low sulfate), low temp | Add H2SO4; raise temp |
| Poor coverage at LCD | Low CrO3, poor ratio, high Cr3+, cold bath | Increase CrO3; correct ratio; reduce Cr3+; raise temp |
| Pitting | Contamination (Fe, Cu), gas pitting | Remove contaminants; use conforming anodes; add fume suppressant |
| Roughness | Lead anode particles, bath contamination | Filter; maintain anodes; check for metallic contaminants |
| Poor adhesion / peeling | Inadequate reverse etch, passive substrate | Extend anodic etch time; check etch current |
| Non-uniform thickness | Anode geometry mismatch, no shields/thieves | Reshape conforming anodes; add shields; adjust racking |

Cards: fill `#1E2435`, alternating `#252B3D`. Defect: `#E05C5C`. Cause: `#F0EDE8`. Fix: `#27AE60`.

**BLOCK G -- Contamination Thresholds**

Y: 24.8" to 26.8".

Section sublabel: `CONTAMINATION LIMITS` Barlow SemiBold 14 pt `#E05C5C`.

| Contaminant | Threshold | Effect | Removal |
|---|---|---|---|
| Iron | > 5--10 g/L | Reduced efficiency, dull deposits | Porous pot or partial dump |
| Copper | > 200 ppm | Dark spots, discoloration | Dummy plate; porous pot |
| Trivalent chrome (excess) | > 5% of CrO3 | Severe efficiency loss | Dilute or electrolyze (high anode area) |
| Chloride | > 200 ppm | Pitting, anode attack | Precipitate with silver or dilute |
| Organic (oil, excess wetting agent) | Any significant | Cr3+ buildup, reduced efficiency | Run bath hot with high anode area |

JetBrains Mono 11 pt `#F0EDE8`.

---

### ZONE 6 -- Anode Management + Safety

**Two-column layout (Y: 27.2" to 32.3"):**

**Left -- Conforming Anode Management (X: 0.5", W: 14.0"):**

Section label: `CONFORMING ANODES` Barlow Condensed ExtraBold 20 pt `#F0EDE8`.

Callout box, fill `#1E2435`, left accent `#E8A020`:
- `Material: Lead alloy (Pb-6%Sn or Pb-7%Sn). Or platinized titanium for special applications.`
- `Shape: CONFORMING -- shaped to mirror workpiece geometry for uniform current distribution.`
- `Anode:cathode ratio: 2:1 to 3:1 (higher than most plating baths).`
- `Maintenance: Inspect for lead sludge buildup. Clean or replace periodically.`
- `Filtration must handle lead particles (10--25 micron media).`
- `Shields and thieves: Used extensively to control HCD/LCD distribution.`

Inter Regular 13 pt `#F0EDE8`, line height 155%.

**Right -- Safety and Regulatory (X: 15.5", W: 8.0"):**

- Rounded rect, fill `#E05C5C` at 15%, border 2 pt `#E05C5C`, radius 8
- Title: `SAFETY AND REGULATORY` Barlow Condensed ExtraBold 18 pt `#E05C5C`
- Body (Inter Regular 12 pt `#F0EDE8`, line height 150%):

> - Cr(VI): IARC Group 1 carcinogen (lung cancer via inhalation)
> - OSHA PEL: 5 ug/m3 (8-hour TWA)
> - EPA: hazardous waste D007
> - Full enclosure or lip exhaust with mist eliminators
> - Fume suppressants mandatory (PFAS-free)
> - P100 respirator or supplied air for maintenance
> - Dedicated chrome room with contained drainage
> - Biological monitoring: urinary chromium
> - Wastewater: Cr6+ reduced to Cr3+ (Na2S2O5 or FeSO4 at pH <3), then precipitate Cr(OH)3 at pH 8--9
> - EPA limit: 0.5 mg/L total Cr daily max

---

### ZONE 7 -- Footer

Standard footer. Title: `Hard Chrome Main Tank`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Hard chrome plating uses hexavalent chromium -- a known human carcinogen regulated under OSHA 29 CFR 1910.1026 and EPA NESHAP 40 CFR 63 Subpart N. Process parameters shown are typical industry values. Consult your process supplier and regulatory authority for application-specific guidance.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table (see Poster #87).
**Export:** Six files -- `Hard Chrome Main Tank -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the densest and most safety-critical main tank poster in the series. The CrO3:SO4 ratio control panel (Block D) is the technical centerpiece -- it must visually communicate that this single ratio controls deposit quality more than any other variable. The three-zone (too high / optimal / too low) visualization is the same pattern used for alloy composition in Poster #52, adapted for ratio control.

The safety banner (Block A2) is carried forward from Poster #87 -- it appears on EVERY poster in the EP-08 cluster. This is not negotiable. Cr(VI) is the most hazardous chemistry in common plating, and every poster that touches it must acknowledge this.

Watson's brief: "CrO3:SO4 ratio is THE critical control parameter in hard chrome." "THIS IS THE MOST HAZARDOUS COMMON PLATING PROCESS."

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #92 -- Construction Workup v1.0*
*2026-04-26*
