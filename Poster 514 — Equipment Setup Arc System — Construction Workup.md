---
Project: Plating Posters Inc
Poster Number: 514
Title: "Equipment Setup -- Arc System"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Thermal Spray Clusters -- Watson Research Brief (Cluster 4: Arc Spray)"
Process Scope: Arc spray system components, power supply, wire feeder, air supply, gun anatomy
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ThermalSpray
  - ArcSpray
  - Equipment
  - ConstructionWorkup
  - ClusterTS04
---

# Poster #514 -- Construction Workup
## Equipment Setup -- Arc System

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Equipment setup for twin-wire arc spray systems. The hero visual is a labeled system diagram showing all major components. Arc spray equipment is simpler than plasma or HVOF -- no combustion gases, no plasma-forming gases -- just DC power, compressed air, and wire. The critical emphasis: air quality. Moisture in the air supply is the #1 equipment-related cause of porosity in arc spray coatings.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **System component diagram (Block B -- HERO):** Labeled diagram of the complete arc spray system built from rectangles, lines, and text labels.
2. **Gun anatomy detail (Block C):** Close-up of the arc spray gun with labeled components.
3. **Air supply requirements (Block D):** Pressure, volume, and quality specifications.
4. **Startup checklist (Block E):** Sequential pre-spray checklist.
5. **Safety callout strip (Block F):** Electrical safety warnings.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 4 highlighted (Amber)
ZONE 3 -- SYSTEM COMPONENTS / HERO (4.2"--15.5" / ~11.3")
  Block B: Complete system diagram
  Block C: Gun anatomy detail
ZONE 4 -- AIR SUPPLY (15.5"--22.0" / ~6.5")
  Block D: Air quality and volume specifications
ZONE 5 -- STARTUP CHECKLIST (22.0"--28.5" / ~6.5")
  Block E: 8-step pre-spray startup sequence
ZONE 6 -- SAFETY WARNINGS (28.5"--32.5" / ~4.0")
  Block F: 4 electrical safety cards
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `EQUIPMENT SETUP` -- 88 pt `#F0EDE8`.
**Subheading:** `Arc Spray System -- DC Power, Compressed Air, Twin Wire` -- 36 pt `#E8A020` (Amber).
**Tagline:** `No combustion gases. No plasma. Just electricity, air, and wire. The simplest powered thermal spray system -- but air quality will make or break your coating.` -- 22 pt `#F0EDE8` at 65%.

---

### ZONE 2 -- Orientation Strip

Stage 4 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Masking complete, workpiece positioned --> After: System powered, wire loaded, air verified, ready for parameter setup`

---

### ZONE 3 -- System Components (HERO)

**Section label:** `ARC SPRAY SYSTEM -- COMPLETE SETUP` -- Y: 4.4".

**BLOCK B -- System Component Diagram**

Y: 5.0" to 11.0". Full width.

Simplified system schematic built from rectangles with connecting lines:

| Component | Rect Size | Fill | Label Color | Description |
|---|---|---|---|---|
| DC Power Supply | W: 4.0", H: 2.5" | `#252B3D` | `#E8A020` | Constant-voltage (CV); 18--40 V open circuit; 100--400 A capacity |
| Wire Feeder (dual spool) | W: 3.5", H: 2.0" | `#252B3D` | `#2EC4B6` | Push-type; dual spools; synchronized feed speed |
| Control Unit | W: 3.0", H: 1.5" | `#252B3D` | `#27AE60` | Voltage, amperage, wire speed, air pressure controls |
| Compressed Air Supply | W: 3.5", H: 2.0" | `#252B3D` | `#E05C5C` | 80--120 PSI at 40--80 CFM; oil-free, dry |
| Air Dryer / Filter | W: 2.5", H: 1.5" | `#252B3D` | `#E05C5C` | Coalescing filter + desiccant or refrigerated dryer |
| Arc Spray Gun | W: 3.0", H: 1.5" | `#252B3D` | `#E8A020` | Two wire guides, contact tips, atomizing air cap |

Connecting lines: 2 pt `#C8D0D8` (Bright Silver) with flow direction arrows.
Power cables: dashed lines in `#E8A020`. Air hose: solid lines in `#2EC4B6`. Wire conduit: solid lines in `#27AE60`.

Component labels: Barlow SemiBold 14 pt, label color. Descriptions: Inter Regular 11 pt `#F0EDE8` at 70%.

**BLOCK C -- Gun Anatomy Detail**

Y: 11.5" to 15.0". Centered, W: 16.0".

Title: `ARC SPRAY GUN -- COMPONENT DETAIL` Barlow SemiBold 18 pt `#E8A020`.

Gun schematic (rectangular body with labeled callouts):
- Body: W: 10.0", H: 2.5", fill `#252B3D`, border 2 pt `#C8D0D8`

| Component | Position | Label Color |
|---|---|---|
| Wire guide tubes (2) | Center, entering from rear | `#2EC4B6` |
| Contact tips (2) | Front, where wires converge | `#E8A020` |
| Atomizing air cap | Front, surrounding contact tips | `#27AE60` |
| Insulated nozzle body | Outer shell | `#C8D0D8` |
| Air inlet | Rear bottom | `#E05C5C` |
| Power cable connections (+ and -) | Rear, one per wire | `#E8A020` |

Labels: Inter Medium 12 pt. Descriptions: Inter Regular 11 pt at 70%.

Below diagram:
- `The arc forms between the two wire tips. Compressed air atomizes the molten metal and propels it at the substrate. Each wire is one electrode -- they consume as they spray.` Inter Regular 13 pt `#F0EDE8` at 60%.

---

### ZONE 4 -- Air Supply

**Section label:** `COMPRESSED AIR -- THE CRITICAL UTILITY` -- Y: 15.7".

**BLOCK D -- Air Supply Specifications**

Y: 16.3" to 21.5".

**Left -- Requirements Table (X: 0.5", W: 11.0"):**

| Parameter | Specification |
|---|---|
| Pressure | 80--120 PSI (550--830 kPa) |
| Volume | 40--80 CFM (1,130--2,265 L/min) |
| Oil content | Zero -- oil-free compressor or coalescing filter |
| Moisture | Dew point at least 10 degC below ambient |
| Particulate | <5 microns -- inline filter required |

Values: JetBrains Mono 14 pt `#E8A020`. Parameters: Inter Medium 14 pt.

**Right -- Why Air Quality Matters (X: 12.0", W: 11.5"):**
- Rounded rect, fill `#1E2435`, left accent `#E05C5C`
- Title: `AIR QUALITY = COATING QUALITY` Barlow SemiBold 16 pt `#E05C5C`
- `MOISTURE in air --> porosity in coating (water flash-evaporates on contact with molten metal)`
- `OIL in air --> adhesion failure (oil film at interface prevents bonding)`
- `The air supply is not an afterthought. It is as important as the power supply and wire quality.`
- `Install: refrigerated dryer + coalescing filter + desiccant dryer for best results`
- `Test air quality daily with a white cloth blowdown test (ISO 8573 Class 2 recommended)`

---

### ZONE 5 -- Startup Checklist

**Section label:** `PRE-SPRAY STARTUP CHECKLIST` -- Y: 22.2".

**BLOCK E -- 8-Step Checklist**

Y: 22.8" to 28.3". Two columns of 4 steps each.

| Step | Action | Verify |
|---|---|---|
| 1 | Inspect gun for worn contact tips, damaged wire guides | Replace worn tips -- they cause uneven arc |
| 2 | Load wire spools; thread wire through conduit to gun | Verify correct material and wire diameter (1.6--3.2 mm) |
| 3 | Connect power cables; verify polarity | Each wire = one electrode; polarity per OEM spec |
| 4 | Connect air supply; verify pressure and volume | 80--120 PSI; blowdown test for oil and moisture |
| 5 | Set voltage and wire feed speed on control unit | Per parameter specification for material being sprayed |
| 6 | Test air supply with white cloth blowdown | Zero oil, zero moisture visible on cloth |
| 7 | Strike arc on scrap coupon; verify spray pattern | Uniform fan; no spitting; arc stable |
| 8 | Check wire feed synchronization | Both wires feeding evenly -- uneven feed = asymmetric arc |

Step numbers: Barlow Condensed ExtraBold 22 pt `#2EC4B6`. Action: Inter Regular 14 pt. Verify: JetBrains Mono 12 pt `#27AE60`.

---

### ZONE 6 -- Safety Warnings

**Section label:** `ELECTRICAL SAFETY WARNINGS` -- Y: 28.7".

Four cards, W: 5.5", H: 2.5", left accent `#E05C5C`.

| Card | X | Warning | Detail |
|---|---|---|---|
| 1 | 0.5" | LOCKOUT/TAGOUT BEFORE SERVICE | Never service the gun, contact tips, or wire feeder with the power supply energized. LOTO every time. |
| 2 | 6.33" | INSULATED GLOVES | The gun is live during operation. Welding-grade insulated gloves required. Do not touch wire or contact tips. |
| 3 | 12.16" | CABLE INSPECTION | Inspect all power cables before each shift. Field use causes abrasion damage. Replace frayed or damaged cables immediately. |
| 4 | 18.0" | GFCI PROTECTION | Use ground-fault circuit interrupter (GFCI) on all circuits. Field installations are especially vulnerable to ground faults. |

---

### ZONE 7 -- Footer

Standard footer. Title: `Equipment Setup -- Arc System`. Version `v1.0 -- 2026`.
Disclaimer: `Source: ASM Handbook Vol 5A; equipment OEM documentation; general industry knowledge. Always follow your equipment manufacturer's specific setup procedures and electrical safety requirements.`

---

## Parts 5--7

**Grouping:** 7 zones. **Light Remap:** Standard. **Export:** Six files.

---

*Alaina -- Poster #514 -- Construction Workup v1.0 -- 2026-04-26*
