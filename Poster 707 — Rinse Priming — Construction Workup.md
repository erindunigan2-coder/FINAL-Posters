---
Project: Plating Posters Inc
Poster Number: 707
Title: "Rinse -- Priming"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster 7 technical reference (Industrial Priming Systems) -- Watson Research Brief"
Technical Source: Rinse and dry requirements in the industrial priming sequence. Covers the unique aspect that zinc-rich and epoxy primers on steel require NO aqueous rinse -- the blast-cleaned surface must stay dry. Aerospace primers on aluminum DO require rinse/dry after conversion coating. Blast-to-prime time window is the critical parameter.
Process Scope: Rinse / dry for industrial priming -- Stage 4 context (time window management)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - IndustrialPriming
  - Rinse
  - ConstructionWorkup
  - PaintingCoating
  - Cluster7
---

# Poster #707 -- Construction Workup
## Rinse -- Priming

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This poster addresses the "rinse" stage in the industrial priming context -- which is fundamentally different from plating or wet coating processes. For zinc-rich and epoxy primers on steel, there is NO aqueous rinse step. The blast-cleaned steel surface must stay dry. The critical parameter is the blast-to-prime time window: how long you have before flash rust makes your surface prep worthless.

For aerospace primers on aluminum, rinse and dry after conversion coating IS required -- this poster covers that too.

Hero visual: a countdown timer concept showing the blast-to-prime window closing as humidity rises.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Blast-to-prime countdown hero (Block B):** Large visual showing a timeline from blast completion to primer application with humidity-dependent windows. Built with horizontal bar segments and time markers.
2. **"No Rinse" emphasis panel (Block D):** Bold callout explaining why steel priming skips aqueous rinse.
3. **Humidity vs. time table (Block E):** How RH affects the working window.
4. **Aerospace rinse panel (Block F):** The exception -- rinse and dry after conversion coating on aluminum.
5. **Dew point monitoring (Block G):** Surface temp vs. dew point rule.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.0" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  "Rinse" position highlighted -- with "N/A for steel" annotation
ZONE 3 -- BLAST-TO-PRIME COUNTDOWN HERO (4.2"--14.0" / ~9.8")
ZONE 4 -- NO RINSE RULE + HUMIDITY TABLE (14.0"--20.5" / ~6.5")
ZONE 5 -- DEW POINT MONITORING (20.5"--26.5" / ~6.0")
ZONE 6 -- AEROSPACE EXCEPTION + FLASH RUST DIAGNOSIS (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE / DRY` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Industrial Priming -- The Blast-to-Prime Window` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `No water touches blasted steel. Your enemy is time and humidity -- the clock starts the moment the blast stops.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

"Rinse" position shown with Teal outline but interior marked `N/A (STEEL)` in `#F0EDE8` at 40%. Aerospace variant noted as exception.

---

### ZONE 3 -- Blast-to-Prime Countdown Hero

**Section label:** `THE BLAST-TO-PRIME WINDOW -- YOUR CLOCK IS TICKING` -- Y: 4.4".

**BLOCK B -- Countdown Timeline (Y: 5.0" to 13.5")**

Large horizontal timeline bar spanning full width:

**Timeline bar:** Rounded rect, X: 0.5", Y: 7.0", W: 23.0", H: 1.5"

Three segments colored by risk:
- `0--4 hours` fill `#27AE60` at 50% -- `SAFE ZONE` Barlow SemiBold 16 pt `#27AE60`
- `4--8 hours` fill `#E8A020` at 40% -- `CAUTION ZONE` Barlow SemiBold 16 pt `#E8A020`
- `8+ hours` fill `#E05C5C` at 40% -- `RE-BLAST ZONE` Barlow SemiBold 16 pt `#E05C5C`

**Humidity modifier callouts (above timeline):**
- Arrow at 1-2 hr: `> 80% RH: window closes HERE` Inter Medium 14 pt `#E05C5C`
- Arrow at 4 hr: `50-80% RH: prime by 4 hours` Inter Medium 14 pt `#E8A020`
- Arrow at 8 hr: `< 50% RH: 8 hours maximum` Inter Medium 14 pt `#27AE60`

**Below timeline -- three condition panels (Y: 9.5" to 13.0"):**

Three callout boxes side by side:

| Panel | X | W | Accent | Condition | Guidance |
|---|---|---|---|---|---|
| Ideal | 0.5" | 7.33" | `#27AE60` | `< 50% RH, dry climate` | `8 hr window. Prime same shift. Best practice: 4 hr max.` |
| Typical | 8.0" | 7.33" | `#E8A020` | `50-80% RH, temperate` | `4 hr window. Plan blast and prime in one sequence.` |
| Critical | 15.5" | 8.0" | `#E05C5C` | `> 80% RH, coastal/marine` | `1-2 hr window. Blast small areas, prime immediately. Dehumidify enclosure if possible.` |

Each: rounded rect, fill `#1E2435`, left accent 0.06".
Condition: Barlow SemiBold 16 pt in accent color. Guidance: Inter Regular 13 pt `#F0EDE8`.

---

### ZONE 4 -- No Rinse Rule + Humidity Table

**Two-column layout (Y: 14.2" to 20.3"):**

**Left -- The No-Rinse Rule (X: 0.5", W: 11.0"):**

Section label: `WHY NO WATER RINSE ON STEEL` Barlow Condensed ExtraBold 22 pt `#E8A020`.

Large callout box, fill `#1E2435`, left accent `#E8A020`:
- `Zinc-rich and epoxy primers are applied directly to dry, blast-cleaned steel.`
- `Water on a blasted steel surface causes immediate flash rust.`
- `Flash rust creates a weak oxide layer between the primer and the steel.`
- `For IOZ primers, this breaks the galvanic circuit -- defeating the purpose of the primer entirely.`
- `The blast profile IS the surface preparation. No chemical step follows.`
- Inter Regular 14 pt `#F0EDE8`, line height 165%

Bottom emphasis: `RULE: Blast -> Blow-Down -> Prime. No water. No rinse. No exceptions (on steel).` Inter Medium 15 pt `#E8A020`

**Right -- Humidity Effects Table (X: 12.0", W: 11.5"):**

Section label: `HUMIDITY AND FLASH RUST` Barlow Condensed ExtraBold 22 pt `#E05C5C`.

| RH Range | Flash Rust Onset | Practical Window | Action |
|---|---|---|---|
| < 40% | 8--12+ hours | Full shift | Standard workflow |
| 40--60% | 4--8 hours | Half shift | Plan efficiently |
| 60--80% | 2--4 hours | 2 hours safe | Blast small areas |
| > 80% | 30 min--2 hr | Minimal | Dehumidify or tent |
| Rain / dew | Immediate | Zero | Do not blast |

Data: JetBrains Mono 12 pt. "Rain / dew" row: fill `#E05C5C` at 20%.

---

### ZONE 5 -- Dew Point Monitoring

**Section label:** `DEW POINT -- THE 5 DEG F RULE` -- Y: 20.7".

**Full-width callout (Y: 21.3" to 26.3"):**

Large centered callout, fill `#1E2435`, left accent `#E8A020`:

Big stat number: `5 deg F` Barlow Condensed ExtraBold 72 pt `#E8A020` (centered)
Subtitle: `Minimum surface temperature above dew point` Barlow SemiBold 22 pt `#F0EDE8`

Explanation (Inter Regular 14 pt `#F0EDE8`, centered, line height 165%):
- `Surface temperature must be at least 5 deg F (3 deg C) above the dew point at all times during application and cure.`
- `If surface temp drops to dew point, invisible moisture condenses on the coating surface.`
- `On uncured primer: causes amine blush (epoxy) or cure inhibition (IOZ).`
- `On blasted steel: causes flash rust before primer is applied.`

Measurement method:
- `Sling psychrometer + surface thermometer per ASTM E337` JetBrains Mono 13 pt `#2EC4B6`
- `Digital dew point meter (faster, more convenient)` JetBrains Mono 13 pt `#2EC4B6`

Bottom note: `Check and record dew point at start of each shift and whenever conditions change. Log in coating inspection report.` Inter Medium 13 pt `#E8A020`.

---

### ZONE 6 -- Aerospace Exception + Flash Rust Diagnosis

**Two-column layout (Y: 26.7" to 32.3"):**

**Left -- Aerospace Exception (X: 0.5", W: 11.0"):**

Section label: `EXCEPTION: AEROSPACE PRIMERS ON ALUMINUM` Barlow Condensed ExtraBold 20 pt `#2EC4B6`.

Callout, fill `#1E2435`, left accent `#2EC4B6`:
- `Aerospace primers on aluminum DO include rinse and dry steps:`
- `1. Alkaline clean -> rinse`
- `2. Deoxidize / etch -> rinse`
- `3. Conversion coating (chromate or TCP) -> rinse`
- `4. Dry thoroughly (forced air or oven)`
- `5. Apply primer within 24 hours of conversion coating`
- `Rinse water quality: DI or RO water; conductivity < 50 uS/cm for final rinse`
- Inter Regular 13 pt `#F0EDE8`

Note: `The rinse/dry cycle for aerospace aluminum follows the conversion coating process -- not the priming process. The primer is applied to a dry, conversion-coated surface.` Inter Regular 12 pt `#F0EDE8` at 60%.

**Right -- Flash Rust Grading (X: 12.0", W: 11.5"):**

Section label: `FLASH RUST -- WHEN IS IT TOO LATE?` Barlow Condensed ExtraBold 20 pt `#E05C5C`.

| Grade | Appearance | Action |
|---|---|---|
| None | Bright steel, metallic sheen | Prime immediately -- ideal |
| Light (L) | Faint yellow-orange tint | Most primers accept light flash rust; check TDS |
| Medium (M) | Visible orange-brown staining | Re-blast recommended; some tolerant primers accept |
| Heavy (H) | Dense rust, loose particles | Must re-blast to spec before priming |

Grades: Barlow SemiBold 14 pt in `#27AE60` (None), `#E8A020` (L), `#E05C5C` (M, H).

Reference: `ASTM D7087 and SSPC-VIS 4 / SSPC-VIS 5 for flash rust grading` JetBrains Mono 11 pt `#F0EDE8` at 50%.

---

### ZONE 7 -- Footer

Standard. Title: `Rinse -- Priming`. Version `v1.0 -- 2026`.
Disclaimer note: `Source: General industry knowledge; SSPC standards; ASTM E337; Watson Research Brief.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Priming -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster flips the usual "rinse" poster on its head -- the entire point is that you do NOT rinse blasted steel. The blast-to-prime countdown hero makes the time pressure viscerally obvious. The dew point "5 deg F rule" is the single most important environmental check in protective coatings work, and it deserves the big-stat treatment. The aerospace exception panel prevents the poster from being misleading for shops that prime aluminum.

---

*Alaina -- Poster #707 -- Construction Workup v1.0 -- 2026-04-26*
