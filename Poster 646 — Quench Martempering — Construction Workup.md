---
Project: Plating Posters Inc
Poster Number: 646
Title: "Quench -- Martempering"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion Heat Treatment Clusters -- Watson Research Brief (Process 10, Section 10.7)"
Technical Source: Martempering quench -- the interrupted quench concept. Rapid cooling from austenitizing to salt/oil bath is the quench. The isothermal hold is equalization. The air cool is where martensite forms. This poster clarifies the three phases that operators commonly confuse, and distinguishes martempering from austempering at the quench level.
Process Scope: Martempering -- quench stage
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Martempering
  - Quench
  - InterruptedQuench
  - ConstructionWorkup
  - ClusterHT10
---

# Poster #646 -- Construction Workup
## Quench -- Martempering

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

The martempering quench is the most misunderstood step in the process. Operators hear "quench into salt" and think the salt bath IS the quench. It is -- partly. The rapid cooling from austenitizing temperature to the salt bath temperature is the quench phase. But the hold in the salt is equalization, not transformation. And the martensite formation happens after the part leaves the salt, during air cooling. Three distinct phases, one continuous operation, and the terminology trips up even experienced heat treaters. This poster untangles it.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Three-phase quench breakdown (Block B -- HERO):** Visual separating the quench into its three distinct phases with what happens metallurgically in each.
2. **Martempering vs. austempering quench comparison (Block C):** Side-by-side showing the critical difference -- equalization vs. transformation.
3. **Quench media options (Block D):** Salt bath and hot oil specifications with trade-offs.
4. **Transfer and hold timing rules (Block E):** Critical timing callouts.

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
  Stage 7 highlighted (Coral)
ZONE 3 -- THREE-PHASE BREAKDOWN / HERO (4.2"--14.5" / ~10.3")
  Block B: Three-phase quench diagram
  Block C: Martempering vs. austempering comparison
ZONE 4 -- QUENCH MEDIA OPTIONS (14.5"--22.0" / ~7.5")
  Block D: Salt vs. hot oil side-by-side
ZONE 5 -- TIMING RULES (22.0"--28.5" / ~6.5")
  Block E: Critical timing callouts
ZONE 6 -- FOOTER BAND (28.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `QUENCH` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Martempering -- Stage 7 of 9` -- 36 pt `#E05C5C` (Coral). Y: 1.5".
**Tagline:** `The interrupted quench: rapid cool to the salt bath, equalize, then air cool. Three phases. One operation. Martensite forms AFTER the bath -- not in it.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 7 highlighted: fill `#E05C5C`, text `#F0EDE8`. Others dimmed.
Below: `Before: Austenitized at 1475--1600 F  -->  After: Equalized at Ms, removed, martensite forming during air cool`

---

### ZONE 3 -- Three-Phase Breakdown (HERO)

**Section label:** `THREE PHASES OF THE INTERRUPTED QUENCH` -- Y: 4.4".

**BLOCK B -- Three-Phase Quench Diagram**

Y: 5.0" to 10.0". Three panels, left to right, connected by arrows.

Each panel: Rounded rect W: 7.3", H: 4.5", fill `#1E2435`, radius 8, top accent 4 pt.

| Phase | X | Accent | Title | What Happens | Temperature | Duration |
|---|---|---|---|---|---|---|
| 1 | 0.5" | `#E05C5C` | RAPID COOL (THE QUENCH) | Part plunges from austenitizing temp to salt bath temp. This IS the quench -- rapid heat extraction. Must pass the pearlite nose on the TTT curve. | 1475--1600 F down to 350--600 F | Seconds (immersion) |
| 2 | 8.3" | `#27AE60` | EQUALIZATION (THE HOLD) | Surface and core temperatures equalize at the salt bath temperature. NO transformation occurs. Austenite is stable above Ms. The uniform temperature is the entire point. | Held at just above Ms (350--600 F) | 5--15 min |
| 3 | 16.0" | `#2EC4B6` | AIR COOL (THE TRANSFORMATION) | Part removed from bath and cooled in still air. Surface and core pass through Ms together. Martensite forms uniformly. Minimal thermal gradient = minimal distortion. | Ms to room temperature | 15--60 min |

Panel interior:
- Phase badge: Rounded rect 1.2" x 0.35", fill accent color, text `PHASE [N]` Barlow Condensed ExtraBold 13 pt `#1A1F2E`
- Title: Barlow Condensed ExtraBold, 18 pt, accent color
- What happens: Inter Regular, 12 pt, `#F0EDE8`, line height 150%
- Temperature: JetBrains Mono Regular, 13 pt, `#F0EDE8`
- Duration: JetBrains Mono Regular, 12 pt, accent color

Arrows: 3 pt `#3A4055`, filled arrowhead right.

**BLOCK C -- Martempering vs. Austempering Quench Comparison**

Y: 10.5" to 14.3". Two side-by-side panels.

**Left -- Martempering Quench (X: 0.5", W: 11.0"):**

Rounded rect, H: 3.5", fill `#1E2435`, left accent 0.06" `#27AE60`, radius 6.

Title: `MARTEMPERING` -- Barlow SemiBold, 18 pt, `#27AE60`

Content (Inter Medium 13 pt `#F0EDE8`):
```
Salt bath purpose:  EQUALIZATION ONLY
Hold time:          5--15 minutes
Transformation:     AFTER removal (air cool)
Final structure:    Martensite (requires temper)
Salt bath temp:     Just above Ms
```

Key data: JetBrains Mono Regular 13 pt `#27AE60`.

**Right -- Austempering Quench (X: 12.0", W: 11.5"):**

Rounded rect, H: 3.5", fill `#1E2435`, left accent 0.06" `#E8A020`, radius 6.

Title: `AUSTEMPERING` -- Barlow SemiBold, 18 pt, `#E8A020`

Content (Inter Medium 13 pt `#F0EDE8`):
```
Salt bath purpose:  FULL TRANSFORMATION
Hold time:          30--120 minutes
Transformation:     IN the salt bath
Final structure:    Bainite (no temper needed)
Salt bath temp:     In bainite range (400--750 F)
```

Key data: JetBrains Mono Regular 13 pt `#E8A020`.

Bottom callout spanning both panels (Y: 13.5"):
- Rounded rect W: 23.0", H: 0.6", fill `#E05C5C` at 12%, border 1 pt `#E05C5C`
- Text: `CRITICAL DISTINCTION: If you hold martempering parts too long in salt, bainite starts to form. That's austempering -- and it's the wrong microstructure for martempering.` -- Inter Medium 14 pt `#E05C5C`

---

### ZONE 4 -- Quench Media Options

**Section label:** `QUENCH MEDIA -- SALT vs. HOT OIL` -- Y: 14.7".

**BLOCK D -- Side-by-Side Media Specs**

Y: 15.3" to 21.8". Two side-by-side tables.

**Left -- Salt Bath (X: 0.5", W: 11.0"):**

Title: `MOLTEN SALT` -- Barlow SemiBold, 18 pt, `#E8A020`

| Parameter | Value |
|---|---|
| Composition | 50/50 NaNO2/KNO3 (typical) |
| Operating range | 350--600 F (177--316 C) |
| H-Factor (agitated) | 0.30--0.50 |
| Temp uniformity | +/-5 F (+/-3 C) |
| Agitation | Required (propeller or pump) |
| Advantages | Wider temp range; higher H-factor; better uniformity |
| Disadvantages | Corrosive; salt cleanup; oxidizer hazard; moisture explosion risk |

**Right -- Hot Oil (X: 12.0", W: 11.5"):**

Title: `MARQUENCH OIL` -- Barlow SemiBold, 18 pt, `#2EC4B6`

| Parameter | Value |
|---|---|
| Composition | Proprietary petroleum base |
| Operating range | 250--400 F (121--204 C) |
| H-Factor (agitated) | 0.20--0.35 |
| Temp uniformity | +/-10 F typical |
| Agitation | Required (propeller) |
| Advantages | Lower cost; no corrosion; easier cleanup; no explosion risk |
| Disadvantages | Narrower range; lower H-factor; fire risk; less uniform |

Header rows: fill `#3A4055`. Data rows: alternating `#1E2435` / `#252B3D`, H: 0.45".
Data: JetBrains Mono Regular 11 pt `#F0EDE8`. Parameter: Inter Medium 12 pt.

---

### ZONE 5 -- Timing Rules

**Section label:** `CRITICAL TIMING RULES` -- Y: 22.2".

**BLOCK E -- Three Timing Callouts**

Y: 22.9" to 28.3". Three full-width callout panels stacked.

Each panel: Rounded rect W: 23.0", H: 1.6", fill `#1E2435`, radius 6.

| Panel | Y | Accent | Rule | Detail |
|---|---|---|---|---|
| 1 | 22.9" | `#E05C5C` | TRANSFER: < 15 SECONDS | From furnace door open to part fully immersed in salt/oil. Automated transfer (conveyor, robot) preferred. Manual transfer acceptable only if consistently achievable. If transfer exceeds 15 sec, pearlite nucleates at the nose of the TTT curve = soft spots = reject. |
| 2 | 24.8" | `#27AE60` | EQUALIZATION HOLD: 5--15 MINUTES | Hold until surface and core are at the same temperature. Longer hold risks bainite formation. For thin sections (< 0.5 in), 5 minutes is sufficient. For heavy sections (> 2 in), up to 15 minutes. Load thermocouple verification recommended. |
| 3 | 26.7" | `#2EC4B6` | AIR COOL: STILL AIR ONLY | Do NOT fan cool or water quench after salt bath removal. The entire point of martempering is uniform transformation. Forced cooling reintroduces the thermal gradient that the equalization step eliminated. Still air to room temperature. |

Panel interior:
- Rule: Barlow Condensed ExtraBold, 22 pt, accent color. Left-aligned within panel.
- Detail: Inter Regular, 13 pt, `#F0EDE8`. Below rule text.

---

### ZONE 6 -- Footer

Standard footer. Title: `Quench -- Martempering`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Transfer times, hold durations, and salt bath temperatures vary by steel grade, section thickness, and equipment. Ms temperatures are approximate. Consult steel supplier data and applicable AMS 2759 specifications. Source: General industry knowledge; ASM Handbook Vol. 4.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Quench Martempering -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The three-phase breakdown is the educational centerpiece. Most operators think of "quench" as one event, but in martempering it's three distinct metallurgical events packed into one continuous operation. The comparison with austempering in Block C is essential -- the difference between "equalize and leave" (martempering) vs. "hold until transformed" (austempering) is the single most important concept in this cluster. The timing rules in Zone 5 are deliberately oversized with strong accent colors because every one of them is a hard pass/fail boundary.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #646 -- Construction Workup v1.0*
*2026-04-26*
