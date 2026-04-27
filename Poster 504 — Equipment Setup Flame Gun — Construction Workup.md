---
Project: Plating Posters Inc
Poster Number: 504
Title: "Equipment Setup -- Flame Gun"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Thermal Spray Clusters -- Watson Research Brief (Cluster 3: Flame Spray)"
Process Scope: Flame spray gun components, gas supply, setup procedure for wire and powder variants
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ThermalSpray
  - FlameSpray
  - Equipment
  - ConstructionWorkup
  - ClusterTS03
---

# Poster #504 -- Construction Workup
## Equipment Setup -- Flame Gun

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Equipment setup for flame spray guns -- both wire and powder variants. The hero visual is a labeled component diagram of both gun types. Key safety emphasis: acetylene is unstable above 15 PSI. This is the most equipment-focused poster in the flame spray cluster.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Gun component diagrams (Block B -- HERO):** Two labeled diagrams side by side -- wire gun and powder gun. Built from rectangles, lines, and text labels.
2. **Gas supply table (Block D):** Pressure settings for O2, C2H2, propane, and compressed air.
3. **Startup checklist (Block E):** Sequential pre-spray checklist.
4. **Safety callout strip (Block F):** Critical safety warnings.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 4 highlighted (Amber)
ZONE 3 -- GUN COMPONENTS / HERO (4.2"--15.5" / ~11.3")
  Block B: Wire gun diagram (left) + Powder gun diagram (right)
  Block C: Component legend
ZONE 4 -- GAS SUPPLY (15.5"--22.0" / ~6.5")
  Block D: Gas pressure table + cylinder safety
ZONE 5 -- STARTUP CHECKLIST (22.0"--28.5" / ~6.5")
  Block E: 8-step pre-spray startup sequence
ZONE 6 -- SAFETY WARNINGS (28.5"--32.5" / ~4.0")
  Block F: 4 critical safety cards
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `EQUIPMENT SETUP` -- 88 pt `#F0EDE8`.
**Subheading:** `Flame Spray Gun -- Wire & Powder Configurations` -- 36 pt `#E8A020` (Amber).
**Tagline:** `Two gun types, one principle: oxy-fuel flame melts feedstock, compressed air propels it. The simplest thermal spray system you can own.` -- 22 pt `#F0EDE8` at 65%.

---

### ZONE 2 -- Orientation Strip

Stage 4 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Gas supply verified, gun assembled --> After: System ready for parameter setup and test fire`

---

### ZONE 3 -- Gun Components (HERO)

**Section label:** `FLAME SPRAY GUN ANATOMY -- WIRE & POWDER` -- Y: 4.4".

**BLOCK B -- Two Gun Diagrams Side by Side**

Y: 5.0" to 13.5".

**Left -- Wire Flame Spray Gun (X: 0.5", W: 11.0"):**

Title: `WIRE FLAME SPRAY GUN` Barlow SemiBold 20 pt `#27AE60`.

Simplified gun schematic (built from rectangles):
- Rectangular body: W: 8.0", H: 3.0", fill `#252B3D`, border 2 pt `#C8D0D8`
- Labeled components with callout lines:

| Component | Position | Label Color |
|---|---|---|
| Oxy-fuel nozzle assembly | Front (left end) | `#E8A020` |
| Mixing chamber + flame cone | Inside front | `#E8A020` |
| Wire feed mechanism | Center top | `#2EC4B6` |
| Wire spool (25--50 lb) | Rear top | `#2EC4B6` |
| Compressed air atomizing cap | Front bottom | `#27AE60` |
| Gas inlets (O2 + C2H2) | Rear bottom | `#E05C5C` |

Labels: Inter Medium 12 pt. Descriptions: Inter Regular 11 pt at 70%.

**Right -- Powder Flame Spray Gun (X: 12.0", W: 11.5"):**

Title: `POWDER FLAME SPRAY GUN` Barlow SemiBold 20 pt `#E8A020`.

| Component | Position | Label Color |
|---|---|---|
| Oxy-fuel nozzle assembly | Front | `#E8A020` |
| Powder injector | Center | `#2EC4B6` |
| Powder hopper (gravity feed) | Top | `#2EC4B6` |
| OR powder feeder (carrier gas) | Alternative top | `#2EC4B6` |
| Gas inlets (O2 + C2H2) | Rear | `#E05C5C` |

**BLOCK C -- Component Legend**

Y: 14.0" to 15.0". Full-width strip, fill `#252B3D`.
- `Amber = Combustion` | `Teal = Feedstock delivery` | `Emerald = Atomization` | `Coral = Gas supply (safety-critical)`

---

### ZONE 4 -- Gas Supply

**Section label:** `GAS SUPPLY -- PRESSURE SETTINGS` -- Y: 15.7".

**BLOCK D -- Gas Pressure Table + Safety Note**

Y: 16.3" to 21.0".

| Gas | Regulated Pressure | Notes |
|---|---|---|
| Oxygen (O2) | 15--40 PSI | Standard welding-grade O2 |
| Acetylene (C2H2) | 10--15 PSI | NEVER exceed 15 PSI -- acetylene is unstable above this pressure |
| Propane (alternative fuel) | 10--20 PSI | Lower flame temperature than acetylene; wider safety margin |
| Compressed air (atomizing) | 40--80 PSI (wire gun) | Oil-free, dry air required |
| Compressed air (carrier) | 20--40 PSI (powder gun) | Entrains powder into flame |

Pressure values: JetBrains Mono 14 pt `#E8A020`. Notes: Inter Regular 13 pt.

Acetylene row: full row highlighted with `#E05C5C` at 15% fill.

Below table -- safety callout:
- Rounded rect, fill `#1E2435`, left accent `#E05C5C`
- `ACETYLENE SAFETY: Flash-back arrestors on BOTH O2 and C2H2 lines. Check with soapy water before every shift. Store acetylene upright. Never use copper fittings on acetylene (forms explosive copper acetylide).` Inter Medium 14 pt `#E05C5C`.

---

### ZONE 5 -- Startup Checklist

**Section label:** `PRE-SPRAY STARTUP CHECKLIST` -- Y: 22.2".

**BLOCK E -- 8-Step Checklist**

Y: 22.8" to 28.3". Two columns of 4 steps each.

| Step | Action | Verify |
|---|---|---|
| 1 | Inspect gun for damage, worn tips, blocked orifices | Replace worn parts before lighting |
| 2 | Connect gas lines; verify flash-back arrestors installed | Both O2 and fuel lines |
| 3 | Open gas cylinders slowly; set regulators to spec | O2 first, then fuel gas |
| 4 | Leak-check all fittings with soapy water | Zero bubbles |
| 5 | Load wire spool or fill powder hopper | Verify correct feedstock material and size |
| 6 | Set atomizing air pressure (wire) or carrier gas (powder) | Per parameter spec |
| 7 | Light flame per OEM procedure; adjust to neutral flame | Neutral = equal inner cones |
| 8 | Test fire on scrap coupon | Verify spray pattern, adhesion, no spitting |

Step numbers: Barlow Condensed ExtraBold 22 pt `#2EC4B6`. Action: Inter Regular 14 pt. Verify: JetBrains Mono 12 pt `#27AE60`.

---

### ZONE 6 -- Safety Warnings

**Section label:** `CRITICAL SAFETY WARNINGS` -- Y: 28.7".

Four cards, W: 5.5", H: 2.5", left accent `#E05C5C`.

| Card | Warning | Detail |
|---|---|---|
| 1 | NEVER EXCEED 15 PSI ON ACETYLENE | Acetylene decomposes explosively above 15 PSI gauge pressure |
| 2 | FLASHBACK ARRESTORS | Required on both O2 and fuel gas lines -- inspect before every shift |
| 3 | VENTILATION | Local exhaust ventilation required; fume extraction active before lighting |
| 4 | FIRE WATCH | Clear area of combustibles within 10 m; fire extinguisher within arm's reach |

---

### ZONE 7 -- Footer

Standard footer. Title: `Equipment Setup -- Flame Gun`. Version `v1.0 -- 2026`.
Disclaimer: `Source: ASM Handbook Vol 5A; equipment OEM documentation; general industry knowledge. Always follow your equipment manufacturer's specific setup procedures.`

---

## Parts 5--7

**Grouping:** 7 zones. **Light Remap:** Standard. **Export:** Six files.

---

*Alaina -- Poster #504 -- Construction Workup v1.0 -- 2026-04-26*
