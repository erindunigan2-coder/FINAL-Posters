---
Project: Plating Posters Inc
Poster Number: 628
Title: "Quench -- Flame Hardening"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion Heat Treatment Clusters -- Watson Research Brief (Process 8, Section 8.7)"
Technical Source: Flame hardening quench methods -- water spray (progressive), immersion (spot/spin), and self-quench (mass quench). Spray-follow distance, quench delay timing, and the unique option of using the cold core as a heat sink on large parts. Unlike induction (polymer spray standard), flame hardening uses plain water almost exclusively.
Process Scope: Flame hardening -- quench stage
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - FlameHardening
  - Quench
  - ConstructionWorkup
  - ClusterHT08
---

# Poster #628 -- Construction Workup
## Quench -- Flame Hardening

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

The flame hardening quench is beautifully simple: water. No polymer concentration to maintain, no oil viscosity to monitor, no salt bath temperature to control. A spray nozzle follows the flame at a fixed distance, and the martensite transformation happens right behind the torch. For spot and spin methods, the whole part goes into a tank. And on truly massive parts, the cold core itself acts as the quench -- mass quench, no external coolant needed. This poster covers all three methods and quantifies the critical spray-follow distance.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Three quench methods hero (Block B -- HERO):** Three side-by-side method panels with parameters and best-for guidance.
2. **Spray-follow distance diagram (Block C):** Visual showing flame-to-spray gap with dimensional callout.
3. **Quench severity comparison table (Block D):** Flame hardening quench media vs. induction and conventional.
4. **Quench defect quick-hit strip (Block E):** Common quench-related failures.

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
ZONE 3 -- THREE QUENCH METHODS / HERO (4.2"--14.5" / ~10.3")
  Block B: Three method panels
  Block C: Spray-follow distance diagram
ZONE 4 -- QUENCH SEVERITY COMPARISON (14.5"--22.0" / ~7.5")
  Block D: Comparison table
ZONE 5 -- QUENCH DEFECTS (22.0"--28.5" / ~6.5")
  Block E: Four defect cards
ZONE 6 -- FOOTER BAND (28.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `QUENCH` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Flame Hardening -- Stage 7 of 9` -- 36 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `Water spray follows the flame. Immersion catches the rest. On massive parts, the cold core does the work. No polymer. No oil. Just water.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 7 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Surface austenitized at 1500--1650 F  -->  After: Martensite formed, surface hardened, ready for temper`

---

### ZONE 3 -- Three Quench Methods (HERO)

**Section label:** `THREE QUENCH METHODS` -- Y: 4.4".

**BLOCK B -- Three Method Panels**

Y: 5.0" to 11.5". Three side-by-side panels.

Each panel: Rounded rect W: 7.3", H: 6.0", fill `#1E2435`, radius 8, top accent 4 pt.

| Pos | Method | X | Accent | Parameters | Best For |
|---|---|---|---|---|---|
| Left | SPRAY FOLLOW (PROGRESSIVE) | 0.5" | `#2EC4B6` | Water spray nozzle follows flame at 0.5--2.0 in (13--51 mm) behind; quench begins immediately after austenitization; spray pressure 20--60 psi; water flow 2--10 GPM per nozzle | Long surfaces: ways, rails, shafts; most common production method; most repeatable |
| Center | IMMERSION | 8.3" | `#E8A020` | Part immersed in water tank after heating; water at 60--80 F (16--27 C); agitation recommended; used for spot and spin methods | Small to medium parts; spot hardening; spin-hardened cylinders |
| Right | SELF-QUENCH (MASS QUENCH) | 16.0" | `#27AE60` | No external quenchant; cold core acts as heat sink; heat conducts inward from hot surface to cold interior; limited to very large parts with thin case relative to mass | Very large parts (rolls, dies); field repairs where water supply is limited; case depth < 10% of section thickness |

Panel interior:
- Method: Barlow Condensed ExtraBold, 20 pt, accent color
- Parameters: JetBrains Mono Regular, 12 pt, `#F0EDE8`, line height 155%
- Best for: Inter Medium, 13 pt, accent color

**BLOCK C -- Spray-Follow Distance Diagram**

Y: 12.0" to 14.3". Full-width panel.

- Rounded rect W: 23.0", H: 2.0", fill `#1E2435`, radius 6

Visual concept: horizontal bar representing a part surface. Left section colored `#E8A020` (flame zone), center section colored gradient from `#E8A020` to `#2EC4B6` (transition), right section colored `#2EC4B6` (quenched zone).

Labels (JetBrains Mono Regular, 13 pt):
- Above flame zone: `FLAME` in `#E8A020`
- Above transition: `0.5--2.0 in GAP` in `#F0EDE8`
- Above quench zone: `SPRAY` in `#2EC4B6`
- Below center: `Traverse direction -->` in `#F0EDE8` at 50%

Key insight callout (Y: 13.5"):
- Rounded rect W: 23.0", H: 0.6", fill `#1E2435`, left accent 0.06" `#E05C5C`
- Text: `CRITICAL: If spray-follow distance is too large, the surface air-cools below Ac3 before quench and won't fully transform. Too close, and steam blanket forms against the hot surface.` Inter Medium, 13 pt, `#E05C5C`

---

### ZONE 4 -- Quench Severity Comparison

**Section label:** `QUENCH SEVERITY -- FLAME HARDENING IN CONTEXT` -- Y: 14.7".

**BLOCK D -- Comparison Table**

Y: 15.3" to 21.8". Column widths (23.0" total):
- Method (6.0") | Medium (5.0") | Typical H-Factor (3.5") | Notes (8.5")

Header row: fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

| Method | Medium | H-Factor | Notes |
|---|---|---|---|
| Flame -- spray follow | Water spray | 0.50--1.0 | Depends on spray pressure, distance, water flow |
| Flame -- immersion | Still water | 1.0 | Standard immersion quench |
| Flame -- immersion | Agitated water | 1.0--1.5 | Agitation increases severity |
| Flame -- self-quench | Mass (no medium) | 0.02--0.10 | Depends on part mass vs. case volume |
| Induction -- spray | Polymer (5--15% PAG) | 0.30--0.50 | Lower severity than water; less distortion risk |
| Conventional | Oil (agitated) | 0.35--0.80 | Standard furnace quench |
| Conventional | Water (agitated) | 1.0--1.5 | Most severe conventional quench |

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.55".
Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Method: Inter Medium, 13 pt.

Highlight rows for flame methods with left accent `#2EC4B6`.

**Note below table:**
- `Flame hardening typically uses water (H = 0.5--1.5) -- more severe than induction's polymer spray (H = 0.3--0.5). This is acceptable because flame-hardened parts are usually large with robust sections that tolerate the thermal shock.` -- Inter Regular, 12 pt, `#F0EDE8` at 70%

---

### ZONE 5 -- Quench Defects

**Section label:** `QUENCH-RELATED DEFECTS` -- Y: 22.2".

**BLOCK E -- Four Defect Cards**

Y: 22.9" to 28.3". Four cards in a row. Gap: 0.25".

Each card: Rounded rect, W: 5.5", H: 5.0", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Defect | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | CRACKING | Quench too severe for section thickness; water too cold; no preheat on complex geometry | Reduce spray pressure; preheat part to 300--400 F; increase spray-follow distance |
| 2 | 6.25" | SOFT SPOTS | Spray-follow distance too large; delayed quench; steam blanket (vapor lock) | Reduce gap to 0.5--1.0 in; increase water flow; verify spray coverage |
| 3 | 12.0" | DISTORTION | Asymmetric quench; one-sided spray; part not supported during quench | Balance spray from multiple nozzles; support part against deflection |
| 4 | 17.75" | INCOMPLETE HARDENING | Self-quench on part too small (insufficient mass); case too deep relative to section | Switch to spray or immersion quench; reduce case depth target |

Interior per card:
- Defect: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer

Standard footer. Title: `Quench -- Flame Hardening`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Quench parameters are application-specific. H-factors are approximate ranges from Grossmann data. Spray pressure, flow rate, and follow distance vary by equipment and part geometry. Source: General industry knowledge; ASM Handbook Vol. 4.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Quench Flame Hardening -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The spray-follow distance diagram in Block C is the most operator-actionable element on this poster. It turns an abstract concept ("quench immediately after heating") into a measurable dimension (0.5--2.0 inches). The self-quench method is the most exotic -- using the part's own thermal mass as the quenchant -- and will be new information to many operators. The H-factor comparison table puts flame hardening quench severity in context against induction and conventional methods, answering "why water instead of polymer?" (because flame parts are big enough to take it).

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #628 -- Construction Workup v1.0*
*2026-04-26*
