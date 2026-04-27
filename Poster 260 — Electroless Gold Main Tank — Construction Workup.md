---
Project: Plating Posters Inc
Poster Number: 260
Title: "Electroless Gold -- Main Tank"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters — Watson Research Brief (Process 6: Electroless Gold)"
Technical Source: Industry-standard immersion gold (ENIG/ENEPIG) and autocatalytic gold bath parameters. IPC-4552B (ENIG) and IPC-4556 (ENEPIG). Cyanide-based (KAu(CN)2) and non-cyanide (sulfite-based Na3Au(SO3)2) gold chemistries. Watson domain expertise.
Process Scope: Main tank -- electroless gold plating bath (Stage 5 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ElectrolessGold
  - MainTank
  - ConstructionWorkup
  - Series2
  - ENIG
  - ENEPIG
---

# Poster #260 -- Construction Workup
## Electroless Gold -- Main Tank

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 5 of 8. This is the centerpiece poster of the Electroless Gold cluster -- the gold bath itself. The poster must clearly present TWO completely different gold baths side by side: immersion gold (displacement reaction, self-limiting, ultra-thin) and autocatalytic gold (reducing agent driven, unlimited thickness). These are fundamentally different processes that happen to both deposit gold. The immersion gold bath is the ENIG/ENEPIG workhorse for PCB surface finishing; the autocatalytic gold bath is the specialist for wire bonding, thick gold contacts, and high-reliability electronics.

Design philosophy: dual-bath comparison as the hero, with deposit properties comparison, a black pad deep-dive callout, and a troubleshooting strip. This is the most data-dense poster in the cluster.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Dual-bath comparison hero (Block B):** Two large side-by-side panels -- immersion gold vs. autocatalytic gold.
2. **Deposit properties comparison table (Block D):** Head-to-head comparison of deposit characteristics.
3. **Black pad deep-dive callout (Block E):** The single most feared defect in ENIG -- dedicated panel.
4. **Troubleshooting strip (Block F):** 4 common gold bath problems with one-line fixes.

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
  Stage 5 highlighted (Emerald)
ZONE 3 -- DUAL-BATH COMPARISON HERO (4.2"--15.5" / ~11.3")
ZONE 4 -- DEPOSIT PROPERTIES COMPARISON (15.5"--22.0" / ~6.5")
ZONE 5 -- BLACK PAD DEEP DIVE (22.0"--28.5" / ~6.5")
ZONE 6 -- TROUBLESHOOTING STRIP (28.5"--32.5" / ~4.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `MAIN TANK` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Electroless Gold -- Stage 5 of 8` -- 36 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `Two processes, one metal. Immersion gold is self-limiting displacement. Autocatalytic gold is reducing-agent driven. Know which you are running.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 5 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Rinsed, activated surface  -->  After: Gold-coated surface (0.03-0.1 um immersion; 1-5+ um autocatalytic)`

---

### ZONE 3 -- Dual-Bath Comparison Hero

**Section label:** `TWO GOLD BATHS -- COMPLETELY DIFFERENT PROCESSES` -- Y: 4.4".

**BLOCK B -- Immersion Gold vs. Autocatalytic Gold**

Y: 5.0" to 15.0".

**Left -- Immersion Gold (X: 0.5", Y: 5.0", W: 11.0", H: 9.5"):**
- Rounded rect, fill `#1E2435`, top accent `#E8A020` 4 pt
- Title: `IMMERSION GOLD (ENIG / ENEPIG)` Barlow SemiBold 20 pt `#E8A020`
- Subtitle: `Galvanic Displacement -- NOT Autocatalytic` Barlow Condensed ExtraBold 14 pt `#F0EDE8` at 50%

**Reaction equation:**
- `3 Ni0 + 2 Au3+ --> 3 Ni2+ + 2 Au0` JetBrains Mono 16 pt `#E8A020`
- `Self-limiting: stops when gold covers all nickel` Inter Medium 14 pt `#E8A020`

**Bath composition table:**

| Component | Concentration | Role |
|---|---|---|
| Gold (KAu(CN)2 or Na3Au(SO3)2) | 0.5-2.0 g/L Au | Gold ion source |
| Citric acid / sodium citrate | 10-30 g/L | Complexant + buffer |
| Thallium or proprietary additive | Trace (ppm) | Controls deposition rate |
| pH adjuster (NaOH or citric acid) | As needed | Maintain target pH |

**Operating parameters:**

| Parameter | Value |
|---|---|
| pH | 4.5-6.0 (acid); 7.0-8.0 (neutral formulations) |
| Temperature | 80-90 C (176-194 F) |
| Au concentration | 0.5-2.0 g/L |
| Immersion time | 5-15 minutes |
| Target thickness | 0.03-0.10 um (IPC-4552B: 0.05 um min) |
| Bath type | Cyanide (KAu(CN)2) or non-cyanide (sulfite) |

Data: JetBrains Mono 12 pt `#F0EDE8`. Labels: Inter Medium 12 pt `#F0EDE8` at 60%.

**Right -- Autocatalytic Gold (X: 12.0", Y: 5.0", W: 11.5", H: 9.5"):**
- Rounded rect, fill `#1E2435`, top accent `#27AE60` 4 pt
- Title: `AUTOCATALYTIC GOLD (TRUE ELECTROLESS)` Barlow SemiBold 20 pt `#27AE60`
- Subtitle: `Reducing Agent Driven -- Unlimited Thickness` Barlow Condensed ExtraBold 14 pt `#F0EDE8` at 50%

**Reaction equations (show primary):**
- `Au+ + H2PO2- + H2O --> Au0 + H2PO3- + 2 H+` JetBrains Mono 14 pt `#27AE60`
- `(Hypophosphite-based -- also DMAB and ascorbic acid variants)` Inter Regular 12 pt `#F0EDE8` at 60%

**Bath composition table:**

| Component | Concentration | Role |
|---|---|---|
| Gold (KAu(CN)2 or sulfite complex) | 1-5 g/L Au | Metal ion source |
| Reducing agent (DMAB, hypo, or ascorbic) | 1-10 g/L | Drives autocatalytic reaction |
| KCN or sodium sulfite | 5-15 g/L | Complexant |
| Stabilizer | Proprietary, ppm-level | Prevents decomposition |

**Operating parameters:**

| Parameter | Value |
|---|---|
| pH | 6.0-8.0 (neutral to slightly alkaline) |
| Temperature | 60-80 C (140-176 F) |
| Deposition rate | 1-3 um/hr |
| Typical thickness | 1-5+ um |
| Bath life | 1-3 MTO |

---

### ZONE 4 -- Deposit Properties Comparison

**Section label:** `DEPOSIT PROPERTIES -- HEAD TO HEAD` -- Y: 15.7".

**BLOCK D -- Comparison Table (Y: 16.3" to 21.8")**

Full-width table. Column widths (23.0" total):
- Property (5.0") | Immersion Gold (8.5") | Autocatalytic Gold (9.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.6".

| Property | Immersion Gold | Autocatalytic Gold |
|---|---|---|
| Thickness | 0.03-0.10 um (self-limiting) | 1-5+ um (unlimited) |
| Purity | >99.9% Au | >99% Au (may contain P or B from reducing agent) |
| Solderability | Excellent (gold dissolves into solder) | Excellent |
| Wire bondability | Marginal (too thin for Au wire bonding) | Excellent (0.5-1.5 um min for wire bond) |
| Corrosion resistance | Excellent (noble metal) | Excellent |
| Contact resistance | Very low | Very low |
| Cost per dm2 | Low (ultra-thin film) | High (thick film, concentrated bath) |
| Primary application | PCB surface finish (ENIG/ENEPIG) | Wire bonding pads, connectors, high-reliability electronics |

Data: JetBrains Mono 12 pt `#F0EDE8`. Property labels: Inter Medium 13 pt `#F0EDE8`. Header: Barlow SemiBold 14 pt `#F0EDE8`.

---

### ZONE 5 -- Black Pad Deep Dive

**Section label:** `BLACK PAD -- THE MOST FEARED DEFECT IN ENIG` -- Y: 22.2".

**BLOCK E -- Black Pad Panel (Y: 22.9" to 28.3")**

**Full-width callout (X: 0.5", W: 23.0", H: 5.2"):**
- Rounded rect, fill `#1E2435`, left accent `#E05C5C` 0.06"

**Left half (X: 0.8", W: 10.5"):**
- Title: `WHAT IS BLACK PAD?` Barlow SemiBold 20 pt `#E05C5C`
- Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):
  - `When the immersion gold reaction is too aggressive:`
  - `1. Excessive nickel dissolution at the Ni/Au interface`
  - `2. A phosphorus-enriched "black" layer forms at the interface`
  - `3. This Ni-P enriched layer is brittle and non-wettable`
  - `4. Solder joints formed on black pad surfaces are weak`
  - `5. Joints fail in the field -- catastrophic reliability failure`
- Visual cue: Cross-section diagram (simplified):
  - Top layer: `Au (gold)` -- Amber box
  - Middle layer: `BLACK LAYER (P-rich)` -- Coral box, dashed border
  - Bottom layer: `EN (Ni-P)` -- Emerald box
  - Label: `Excessive Ni corrosion creates P-rich interlayer` Inter Regular 12 pt `#E05C5C`

**Right half (X: 12.0", W: 11.0"):**
- Title: `PREVENTION` Barlow SemiBold 20 pt `#27AE60`
- Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):

| Control | Target |
|---|---|
| Gold concentration | Maintain within spec (0.5-2.0 g/L) |
| Bath pH | Do not let pH drop below spec (increases aggressiveness) |
| Bath temperature | Do not exceed spec (80-90 C) |
| Immersion time | Do not exceed 15 min (longer = more Ni attack) |
| EN quality | EN P% must be in spec (6-9% for Mid-P per IPC-4552B) |
| EN thickness | Minimum 3 um EN before gold |

- Bottom highlight:
  - Rounded rect, W: 10.0", H: 0.6", fill `#E05C5C` at 15%, border 1 pt `#E05C5C`
  - `Black pad is caused by the gold bath, but it is a SYSTEM failure. EN quality, rinse discipline, and gold bath control ALL contribute.` Inter Medium 13 pt `#E05C5C`

---

### ZONE 6 -- Troubleshooting Strip

**Section label:** `QUICK TROUBLESHOOTING -- 4 COMMON GOLD BATH PROBLEMS` -- Y: 28.7".

**BLOCK F -- Four Problem Cards (Y: 29.4" to 32.3")**

Four cards in a single row. Gap: 0.33".

Each card: Rounded rect, W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | NO GOLD DEPOSITION | EN surface oxidized or passivated; bath depleted | Verify EN quality; check Au concentration; reduce transfer time |
| 2 | 6.33" | DARK / HAZY GOLD | Contamination (Ni, hypophosphite drag-in); bath aging | Improve pre-plate rinse; check MTO; carbon treat |
| 3 | 12.16" | EXCESS THICKNESS (IMMERSION) | Gold bath too aggressive (high Au, high temp, low pH) | Reduce Au or temperature; verify pH; check immersion time |
| 4 | 18.0" | BATH DECOMPOSITION (AUTO) | Overheating; low stabilizer; metallic contamination | Check stabilizer; maintain temperature; filter continuously |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 7 -- Footer

Standard footer. Title: `Electroless Gold -- Main Tank`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Process parameters shown are typical industry values for immersion gold and autocatalytic gold baths. Specific formulations, concentrations, and process limits vary by proprietary product. Consult your process supplier for application-specific guidance. Source: General industry knowledge; IPC-4552B; IPC-4556.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Electroless Gold Main Tank -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the most technically dense poster in the Electroless Gold cluster. The dual-bath comparison in Zone 3 is the hero -- it must communicate at a glance that immersion gold and autocatalytic gold are fundamentally different processes. The black pad callout in Zone 5 is the single most important quality concern in ENIG. Every ENIG shop has either experienced black pad or lives in fear of it. The cross-section diagram (Au / black layer / EN) is a classic visual from IPC-4552B failure analysis literature. The troubleshooting strip keeps the problem/cause/fix pattern consistent across all cluster posters. Gold bath economics are extreme -- gold costs $80-100+ per gram -- so bath maintenance and drag-out recovery are not optional, they are survival.

---

*Alaina -- Poster #260 -- Construction Workup v1.0 -- 2026-04-26*
