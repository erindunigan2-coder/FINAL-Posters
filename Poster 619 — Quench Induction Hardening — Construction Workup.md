---
Project: Plating Posters Inc
Poster Number: 619
Title: "Quench -- Induction Hardening"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion Heat Treatment Clusters -- Watson Research Brief (Process 7, Section 7.7)"
Technical Source: Induction hardening quench parameters -- polymer (PAG) quenchant concentration, spray pressure, flow rate, quench delay, and the unique aspects of integral spray quench systems. No oil quench in induction -- polymer/water spray is standard.
Process Scope: Induction hardening -- quench
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - InductionHardening
  - Quench
  - ConstructionWorkup
  - ClusterHT07
---

# Poster #619 -- Construction Workup
## Quench -- Induction Hardening

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Induction quenching is fundamentally different from furnace quenching. There is no quench tank. The quench is a precision spray system built into the inductor coil itself -- quenchant follows the heat by fractions of a second. The quench delay (time between power-off and quenchant contact) is measured in tenths of seconds, and getting it wrong means the heat soaks into the core and ruins the case/core differential that makes surface hardening valuable.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Quench system diagram (Block B -- HERO):** Three quench configurations: integral spray, following spray (scan), and immersion.
2. **Quenchant concentration table (Block D):** PAG polymer concentration vs. quench severity.
3. **Quench delay callout (Block E):** Why delay matters and acceptable ranges.
4. **Quench defects strip (Block F):** Four common quench-related defects with fixes.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 7 highlighted (Teal)
ZONE 3 -- QUENCH SYSTEM CONFIGURATIONS / HERO (4.2"--14.5" / ~10.3")
  Block B: Three quench configuration panels
  Block C: "No Oil Tank" advantage callout
ZONE 4 -- QUENCHANT PARAMETERS (14.5"--22.0" / ~7.5")
  Block D: PAG concentration vs. severity table + reservoir parameters
ZONE 5 -- QUENCH DELAY + DEFECTS (22.0"--32.5" / ~10.5")
  Block E: Quench delay panel
  Block F: Quench defect strip
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `QUENCH` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Induction Hardening -- Stage 7 of 9` -- 36 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `Spray quench, not tank quench. The quenchant follows the heat by fractions of a second -- precision cooling for precision heating.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 7 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Surface at 1500--1700 F (austenitized)  -->  After: Surface transformed to martensite`

---

### ZONE 3 -- Quench System Configurations (HERO)

**Section label:** `THREE QUENCH CONFIGURATIONS` -- Y: 4.4".

**BLOCK B -- Three Configuration Panels**

Y: 5.0" to 12.0". Three panels side by side.

Each panel: Rounded rect W: 7.33", H: 6.5", fill `#1E2435`, radius 8, top accent 4 pt.

| Panel | X | Config | Accent | Description | When Used |
|---|---|---|---|---|---|
| 1 | 0.5" | INTEGRAL SPRAY | `#2EC4B6` | Quench orifices built into the inductor coil body. Quenchant sprays from the coil itself immediately after power-off. Quench delay: 0.1--0.5 sec. | Single-shot hardening; most common configuration; shafts, bearing seats, cam lobes |
| 2 | 8.17" | FOLLOWING SPRAY (SCAN) | `#E8A020` | Separate spray ring mounted below the coil. As the coil scans along the part, the spray ring follows, quenching each section immediately after heating. Quench delay: effectively 0 (continuous). | Progressive scan hardening; long shafts, rolls, bars |
| 3 | 15.83" | IMMERSION QUENCH | `#27AE60` | Part dropped or lowered into a quench tank after heating. Less precise than spray. Used when spray is impractical. Quench delay: 1--3 sec (transfer time). | Large parts; parts requiring full-body quench; some spin hardening setups |

Panel interior:
- Config name: Barlow SemiBold 20 pt, accent color
- Diagram placeholder: Rounded rect 6.0" x 2.5", fill `#252B3D`, center text `[Configuration diagram]`
- Description: Inter Regular 13 pt `#F0EDE8`
- When used: Inter Medium 12 pt, accent color

**BLOCK C -- No Oil Tank Advantage**

Y: 12.3" to 14.3". Full-width callout.
- Rounded rect W: 23.0", H: 1.8", fill `#1E2435`, left accent 0.06" `#27AE60`
- Title: `NO OIL QUENCH TANK` -- Barlow SemiBold 18 pt `#27AE60`
- Text: `Induction hardening uses water-based polymer (PAG) spray -- not oil. This eliminates: oil fires, smoke and fumes, oil disposal costs, oil maintenance (viscosity, flash point, water content monitoring). The safety and environmental advantages are significant.` -- Inter Medium 14 pt `#F0EDE8`

---

### ZONE 4 -- Quenchant Parameters

**Section label:** `QUENCHANT CONCENTRATION & SYSTEM PARAMETERS` -- Y: 14.7".

**BLOCK D -- Two-panel layout**

**Left -- Concentration vs. Severity (X: 0.5", W: 11.0"):**

Table (Y: 15.5" to 19.5"):

| PAG Concentration | Quench Severity | Equivalent | Use |
|---|---|---|---|
| 0% (water only) | Maximum (severe) | Water quench | Rarely used -- cracking risk |
| 5% PAG | High | Fast oil equivalent | High-carbon steels; deep case |
| 10% PAG | Moderate-high | Standard | Most common production setting |
| 15% PAG | Moderate | Mild oil equivalent | Crack-sensitive parts |
| 20% PAG | Mild | Slow oil equivalent | Thin sections; complex geometry |

Header: fill `#3A4055`. Data rows: alternating `#1E2435` / `#252B3D`, H: 0.7".
Data: JetBrains Mono Regular 12 pt `#F0EDE8`.

Bottom note: `Increasing PAG concentration SLOWS the quench. Use higher concentration to reduce cracking risk on complex geometries.` Inter Medium 13 pt `#2EC4B6`

**Right -- System Parameters (X: 12.0", W: 11.5"):**

- Rounded rect H: 6.0", fill `#1E2435`, left accent 0.06" `#2EC4B6`

| Parameter | Value |
|---|---|
| Spray pressure | 20--60 psi |
| Flow rate | Sufficient to cover heated zone within 1 sec |
| Reservoir temperature | 70--110 F (21--43 C) |
| Concentration check | Refractometer -- weekly minimum |
| pH | 8.5--9.5 (maintain with biocide) |
| Filtration | Required -- scale and debris clog spray orifices |
| Biological control | Biocide addition per supplier; bacteria degrade PAG |

Parameter: Inter Medium 13 pt `#F0EDE8`. Value: JetBrains Mono Regular 12 pt `#F0EDE8`.

---

### ZONE 5 -- Quench Delay + Defects

**Two-column layout (Y: 22.2" to 32.3"):**

**Left -- Quench Delay (X: 0.5", W: 11.0"):**

Section label: `QUENCH DELAY -- THE CRITICAL FRACTION OF A SECOND` Barlow Condensed ExtraBold 24 pt.

- Rounded rect H: 9.5", fill `#1E2435`, left accent 0.06" `#E05C5C`

Content (Inter Regular 14 pt `#F0EDE8`, line height 160%):
```
WHAT IS QUENCH DELAY?
The time between power-off (end of heating)
and first quenchant contact with the part.

WHY IT MATTERS:
During the delay, heat conducts from the hot
surface INWARD toward the core. A delay of
even 1-2 seconds can:
  - Deepen the austenitized zone beyond spec
  - Heat the core (loss of tough core)
  - Cause through-hardening on thin sections

ACCEPTABLE RANGES:
  Integral spray:    0.1--0.5 sec
  Following spray:   ~0 sec (continuous)
  Immersion:         1--3 sec (transfer time)

RULE: Minimize quench delay to the shortest
time your system can achieve. If delay exceeds
2 seconds, consider redesigning the quench
delivery.
```

Data: JetBrains Mono Regular 14 pt `#E05C5C`. Body: Inter Regular 13 pt `#F0EDE8`.

**Right -- Quench Defects (X: 12.0", W: 11.5"):**

Section label: `QUENCH-RELATED DEFECTS` Barlow Condensed ExtraBold 24 pt `#E05C5C`.

Four stacked cards (H: 2.1" each), fill `#1E2435`, left accent 0.06" `#E05C5C`.

| Card | Problem | Cause | Fix |
|---|---|---|---|
| 1 | QUENCH CRACKING | Quench too severe (low PAG %); sharp corners; residual stress from prior machining | Increase PAG concentration; radius all transitions; stress relieve before hardening |
| 2 | SOFT SPOTS (QUENCH) | Non-uniform spray coverage; clogged orifices; part not rotating | Clean orifices; verify spray pattern; ensure rotation |
| 3 | THROUGH-HARDENED | Quench delay too long; heat soaked to core before quenchant arrived | Reduce delay; verify spray activation timing |
| 4 | DISTORTION | Asymmetric quench pattern; one side quenched before the other | Balance spray around circumference; verify orifice flow |

Problem: Barlow SemiBold 14 pt `#E05C5C`. Cause: Inter Regular 12 pt `#F0EDE8`. Fix: Inter Medium 12 pt `#27AE60`.

---

### ZONE 6 -- Footer

Standard footer. Title: `Quench -- Induction Hardening`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Quench parameters are application-specific. PAG concentration, spray pressure, and delay settings must be validated for each part geometry and steel grade. Consult your quenchant supplier and equipment manufacturer. Source: General industry knowledge; ASM Handbook Vol. 4.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Quench Induction Hardening -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The "no oil" message is a genuine differentiator for induction shops and deserves prominent placement. Operators who have worked around quench oil fires appreciate the safety advantage immediately. The quench delay concept is uniquely important for induction -- furnace quenching does not have this concern because the entire part is at temperature. In induction, only the surface is hot, and every tenth of a second of delay bleeds heat into the core. The PAG concentration table is the daily-use quick reference on this poster.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #619 -- Construction Workup v1.0*
*2026-04-26*
