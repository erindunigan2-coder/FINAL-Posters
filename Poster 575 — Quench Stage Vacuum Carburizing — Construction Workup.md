---
Project: Plating Posters Inc
Poster Number: 575
Title: "Quench Stage -- Vacuum Carburizing"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 2: Vacuum Carburizing / LPC, Section 2.8)"
Technical Source: HPGQ (high-pressure gas quench) -- N2 and He pressure/H-factor table, oil quench in vacuum option, HPGQ vs. oil comparison, quench severity limitations for thick sections. Per ASM Handbook Vol. 4 and vacuum furnace OEM documentation.
Process Scope: Vacuum carburizing quench stage (Stage 6 of 9)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - VacuumCarburizing
  - LPC
  - Quench
  - HPGQ
  - ConstructionWorkup
  - DiffusionHT
---

# Poster #575 -- Construction Workup
## Quench Stage -- Vacuum Carburizing

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

The quench poster for LPC. High-pressure gas quench (HPGQ) is the default and the signature advantage of vacuum carburizing -- less distortion, no oil mess, no fire risk. But HPGQ has real limitations in quench severity, especially on thick sections in lean alloy steels. This poster covers the HPGQ parameter table (the core data), the oil quench alternative, and an honest assessment of when each method is appropriate.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **HPGQ parameter table (Block B -- HERO):** Gas type, pressure, H-factor, cooling rate -- the essential reference table.
2. **How HPGQ works panel (Block D):** The mechanics of gas quenching in a vacuum vessel.
3. **Oil quench option (Block E):** When and why you still need oil in a vacuum furnace.
4. **Decision matrix strip (Block F):** HPGQ vs. oil -- when to use which.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 6 highlighted (Coral)
ZONE 3 -- HPGQ PARAMETER TABLE HERO (4.2"--15.5" / ~11.3")
  Block B: Gas type / pressure / H-factor table
ZONE 4 -- HOW HPGQ WORKS (15.5"--22.0" / ~6.5")
  Block D: Mechanics of gas quenching
ZONE 5 -- OIL QUENCH OPTION (22.0"--28.5" / ~6.5")
  Block E: When and why oil is still needed
ZONE 6 -- DECISION MATRIX (28.5"--32.5" / ~4.0")
  Block F: HPGQ vs. oil quick-reference
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `QUENCH STAGE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Vacuum Carburizing (LPC) -- Stage 6 of 9` -- 32 pt `#E05C5C` (Coral). Y: 1.4".
**Tagline:** `High-pressure gas quench is the default. Less distortion, no oil, no fire risk. But when section thickness exceeds what gas can handle, oil is still the answer.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 6 highlighted: fill `#E05C5C`, text `#F0EDE8`. Others dimmed.
Below: `Before: Carbon profile complete at temperature  -->  After: Austenite transformed to martensite`

---

### ZONE 3 -- HPGQ Parameter Table (HERO)

**Section label:** `HIGH-PRESSURE GAS QUENCH -- THE ESSENTIAL REFERENCE` -- Y: 4.4". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK B -- Parameter table (Y: 5.0" to 10.5")**

| Gas | Pressure (bar) | H-Factor (approx.) | Cooling Rate | Relative Cost |
|---|---|---|---|---|
| Nitrogen (N2) | 10 | 0.10--0.15 | Slow-moderate | Low |
| Nitrogen (N2) | 20 | 0.15--0.25 | Moderate | Low |
| Helium (He) | 15 | 0.20--0.30 | Moderate-fast | High (5--10x N2) |
| Helium (He) | 20 | 0.30--0.40 | Fast | High |
| He/N2 mix | 20 | 0.25--0.35 | Moderate-fast | Medium |
| Agitated oil (reference) | -- | 0.35--0.80 | Fast-very fast | N/A |

Table: Header `#3A4055`, alternating rows `#252B3D` / `#1E2435`. JetBrains Mono 14 pt. Oil reference row highlighted with left border `#E8A020`.

**Below table -- context callouts (Y: 11.0" to 14.5"):**

Three callout boxes in a row:

| Callout | Title | Content | Accent |
|---|---|---|---|
| Left (W: 7.33") | WHY HELIUM? | He has 5.5x the thermal conductivity of N2. More heat extraction per unit pressure. Worth the cost for high-hardenability demand parts. | `#2EC4B6` |
| Center (W: 7.33") | H-FACTOR MEANING | Grossmann quench severity. Higher = faster cooling = deeper hardening. Oil at 0.50 is roughly 2--3x the severity of N2 at 20 bar. | `#E8A020` |
| Right (W: 7.67") | THE GAP | HPGQ at maximum (He, 20 bar, H=0.40) is still LESS severe than moderate agitated oil (H=0.50). This gap matters for thick sections. | `#E05C5C` |

Each: Rounded rect H: 3.2", fill `#1E2435`, left accent 0.06".

---

### ZONE 4 -- How HPGQ Works

**Section label:** `HOW HIGH-PRESSURE GAS QUENCH WORKS` -- Y: 15.7". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK D -- Two-column layout (Y: 16.3" to 21.8")**

*Left -- Mechanics (X: 0.5", W: 11.0"):*

Rounded rect fill `#1E2435`, left accent `#2EC4B6`.

Title: `THE MECHANICS` Barlow SemiBold 18 pt `#2EC4B6`

Content:
```
1. Carburizing cycle completes at temperature

2. Gas quench initiated by furnace controller
   (all interlocks must verify BEFORE release)

3. High-pressure gas (N2 or He) floods the
   chamber to 10--20 bar in seconds

4. Powerful blower (200+ HP) circulates gas
   through the load at high velocity

5. Heat exchanger cools the recirculating gas

6. Gas extracts heat from parts by forced
   convection -- no liquid contact

7. Parts cool to 150--300 F (66--149 C)

8. Chamber depressurized; parts unloaded
```

*Right -- Advantages (X: 12.0", W: 11.5"):*

Rounded rect fill `#1E2435`, left accent `#27AE60`.

Title: `WHY GAS QUENCH WINS ON DISTORTION` Barlow SemiBold 18 pt `#27AE60`

Content:
```
NO FILM BOILING:
Oil quench has three cooling stages:
vapor blanket -> nucleate boiling -> convection
The vapor blanket is NON-UNIFORM and
causes asymmetric cooling = distortion

Gas quench has ONE cooling mechanism:
forced convection -- UNIFORM around the part

NO LIQUID/VAPOR INTERFACE:
No bubble formation, no surface tension
effects, no drag-out contamination

CONTROLLABLE:
Adjust pressure and blower speed to
tune cooling rate for each application

TYPICAL RESULT:
30--50% less distortion vs. oil quench
(heavily application-dependent)
```

---

### ZONE 5 -- Oil Quench Option

**Section label:** `WHEN YOU STILL NEED OIL` -- Y: 22.2". Barlow Condensed ExtraBold 28 pt `#E8A020`.

**BLOCK E -- Two-column layout (Y: 22.9" to 28.3")**

*Left -- When Oil Is Required (X: 0.5", W: 11.0"):*

Rounded rect fill `#1E2435`, left accent `#E8A020`.

Title: `OIL QUENCH IN VACUUM` Barlow SemiBold 18 pt `#E8A020`

Content:
```
WHEN GAS CANNOT DO THE JOB:

- Thick sections (>1.5" / 38 mm) in
  lean alloy steels (8620, 1020)
  HPGQ may not develop full case hardness

- High hardenability demand
  Where H-factor >0.40 is required

- Legacy specifications
  Some specs mandate oil quench regardless
  of furnace capability

HOW IT WORKS IN VACUUM:
- Integrated oil quench chamber
- Parts transfer from heating chamber
  to oil under vacuum or inert atmosphere
- Oil temperature and agitation same
  parameters as conventional oil quench
- 100--160 F (38--71 C), agitated
```

*Right -- The Trade-Off (X: 12.0", W: 11.5"):*

Rounded rect fill `#1E2435`, left accent `#E05C5C`.

Title: `WHAT YOU LOSE WITH OIL` Barlow SemiBold 18 pt `#E05C5C`

Content:
```
DISTORTION ADVANTAGE: GONE
Oil quench distortion is the same whether
the furnace is vacuum or atmosphere

CLEAN PARTS: GONE
Oil residue requires post-quench wash
(alkaline cleaning step)

FIRE RISK: BACK
Oil quench = oil fire risk = fire
suppression system required

THE BRIGHT SIDE:
- You still get zero IGO (vacuum heating)
- You still get cleaner surface than gas
  carburizing (no scale before quench)
- Higher carburizing temperature still
  applies (shorter cycles)
- LPC + oil quench is still superior to
  gas carburizing + oil quench on most
  quality metrics
```

---

### ZONE 6 -- Decision Matrix

**Section label:** `HPGQ OR OIL? -- QUICK DECISION GUIDE` -- Y: 28.7". Barlow Condensed ExtraBold 24 pt `#F0EDE8`.

**BLOCK F -- Four decision cards (Y: 29.4" to 32.3")**

| Card | X | W | Scenario | Recommendation |
|---|---|---|---|---|
| 1 | 0.5" | 5.5" | `THIN SECTION + HIGH ALLOY` | HPGQ (N2 or He). Full case hardness achievable. Maximum distortion benefit. |
| 2 | 6.33" | 5.5" | `THIN SECTION + LEAN ALLOY` | HPGQ with He at 20 bar. Verify H-factor is sufficient for the steel grade. |
| 3 | 12.16" | 5.5" | `THICK SECTION + HIGH ALLOY` | HPGQ may work. Run trial. If core does not harden, switch to oil. |
| 4 | 18.0" | 5.5" | `THICK SECTION + LEAN ALLOY` | Oil quench. HPGQ will not develop sufficient case hardness. Accept the distortion trade-off. |

Each: Rounded rect H: 2.7", fill `#1E2435`, left accent `#2EC4B6`.
Title: Barlow SemiBold 14 pt `#2EC4B6`.
Details: Inter Regular 12 pt `#F0EDE8`.

---

### ZONE 7 -- Footer

Standard. Title: `Quench Stage -- Vacuum Carburizing (LPC)`. Version `v1.0 -- 2026`.

Disclaimer: `Source: ASM Handbook Vol. 4, AMS 2759/7E, vacuum furnace OEM documentation. H-factor values are approximate and vary with gas purity, nozzle design, and blower capacity. Always verify quench severity on representative test loads.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Quench Stage Vacuum Carburizing -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The HPGQ parameter table is the most important single element -- it's the data that operators and metallurgists need at a glance. The oil reference row at the bottom of the table is crucial context -- it shows where HPGQ stands relative to the method everyone already knows. The decision matrix at the bottom distills the entire poster into four scenarios, which is exactly how a production engineer thinks about the problem.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #575 -- Construction Workup v1.0*
*2026-04-26*
