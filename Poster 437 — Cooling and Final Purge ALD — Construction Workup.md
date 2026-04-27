---
Project: Plating Posters Inc
Poster Number: 437
Title: "Cooling & Final Purge -- ALD"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 4: ALD, Sections 4.7-4.8)"
Technical Source: ALD end-of-run procedure -- extended final purge to remove all precursor residues from reactor and substrate, cooldown under vacuum or inert atmosphere, and safe unloading. ALD films are ultrathin (1-100 nm) so post-deposition handling is about protecting the film from contamination and damage, not managing thermal stress (unlike CVD).
Process Scope: ALD cooling, final purge, and unloading (Stage 9 of 10)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ALD
  - Cooling
  - Purge
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #437 -- Construction Workup
## Cooling & Final Purge -- ALD

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 9 of 10. ALD cycling is complete. The final purge removes residual precursor vapors from the reactor, delivery lines, and substrate surface. Cooling is straightforward compared to CVD -- ALD operates at 150-400 C (vs. CVD's 800-1100 C), so thermal stress is minimal and cooldown times are short. The real concern is precursor residue: TMA, DEZ, and other metalorganic compounds left in the system can react with atmospheric moisture during unloading, contaminating the fresh film or creating safety hazards.

Hero visual: timeline showing the final purge + cooldown sequence from last ALD cycle to safe unloading.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Final purge + cooldown timeline (Block B -- HERO):** Horizontal timeline from last cycle to unloading.
2. **Why the final purge matters (Block C):** Residual precursor risks.
3. **Cooldown protocol (Block D):** Temperature management for different substrate types.
4. **Safe unloading procedure (Block E):** Step-by-step.
5. **Post-deposition handling rules (Block F):** How to protect ultrathin films.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 9 highlighted (Amber)
ZONE 3 -- FINAL PURGE + COOLDOWN TIMELINE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- WHY PURGE MATTERS + COOLDOWN PROTOCOL (14.5"--22.0" / ~7.5")
ZONE 5 -- SAFE UNLOADING + HANDLING RULES (22.0"--28.5" / ~6.5")
ZONE 6 -- COMMON END-OF-RUN PROBLEMS (28.5"--32.5" / ~4.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `COOLING & FINAL PURGE` -- 72 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `ALD -- Stage 9 of 10 -- Clearing Residual Precursors and Safe Unloading` -- 28 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `The last ALD cycle is done. Now purge every trace of precursor from the system before opening to air -- especially if that precursor is pyrophoric.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 9 (`Cooling & Final Purge`): fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Input: ALD cycling complete, film at target thickness (Stage 8) --> Output: Reactor purged, substrate cooled, ready for unloading and characterization`

---

### ZONE 3 -- Final Purge + Cooldown Timeline Hero

**Section label:** `END-OF-RUN SEQUENCE -- FROM LAST CYCLE TO UNLOAD` -- Y: 4.4". Barlow Condensed ExtraBold, 26 pt, `#F0EDE8`.

**BLOCK B -- Horizontal Timeline (Y: 5.0" to 14.0")**

Main panel: Rounded rect, X: 0.5", W: 23.0", fill `#1E2435`, radius 8.

**Timeline base:** Rectangle, X: 1.5", Y: 10.0", W: 20.0", H: 0.08", fill `#C8D0D8`.

**Time labels below timeline:**
- `0 min`, `5 min`, `15 min`, `30 min`, `45 min`, `60 min`
- JetBrains Mono 12 pt `#F0EDE8` at 60%

**Phase bars above timeline:**

| Phase | Color | X Start | Width | Y | Height | Label |
|---|---|---|---|---|---|---|
| Last ALD Cycle | `#E8A020` at 40% | 1.5" | 1.5" | 8.5" | 1.3" | `LAST CYCLE` |
| Extended Purge | `#2EC4B6` | 3.2" | 6.0" | 7.5" | 2.3" | `EXTENDED FINAL PURGE` |
| Heater Off | `#3A4055` | 9.5" | 1.5" | 8.5" | 1.3" | `HEATER OFF` |
| Cooldown | `#27AE60` at 40% | 11.2" | 5.0" | 8.0" | 1.8" | `COOLDOWN` |
| Vent/Unload | `#E8A020` | 16.5" | 3.0" | 8.5" | 1.3" | `VENT & UNLOAD` |

Labels: Barlow SemiBold 14 pt. Details below each bar: Inter Regular 12 pt `#F0EDE8`.

**Detail annotations for each phase (stacked above bars):**

Extended Purge (dominant bar):
```
Carrier gas (N2 or Ar) flows continuously
at high rate (100-500 sccm) for 10-30 min.

PURPOSE:
- Remove residual TMA/H2O from reactor
- Clear delivery lines and valves
- Desorb physisorbed species from film surface
- For TMA: CRITICAL safety step
  (residual TMA + air = fire)
```

Cooldown:
```
Substrate cools from ALD temp (150-350 C)
to < 100 C under flowing inert gas.
Time: 15-30 min (varies by reactor thermal mass).
No thermal stress risk -- ALD films are ultra-thin.
```

Vent/Unload:
```
Reactor vented to atmospheric pressure
with dry N2. Open chamber only after
temperature confirmed < 100 C.
```

**Temperature curve overlay (dashed line):**
- Descending from ALD temp to room temp, overlaid on the timeline
- 2 pt dashed `#E05C5C`
- Key temperature labels: `ALD TEMP`, `< 100 C SAFE`

**Bottom insight (Y: 13.3" to 14.0"):**
- Full-width rounded rect, fill `#252B3D`, left accent `#2EC4B6`
- `The extended purge is NOT optional. Residual TMA in the reactor + atmospheric moisture during unloading = spontaneous combustion. Purge until pressure baseline is clean and stable.` Inter Medium 13 pt `#2EC4B6`

---

### ZONE 4 -- Why Purge Matters + Cooldown Protocol

**Two-column layout (Y: 14.5" to 21.8"):**

**Left -- Why the Final Purge Matters (X: 0.5", W: 11.0")**

**Section label:** `RESIDUAL PRECURSOR RISKS` -- Y: 14.7". Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`.

**BLOCK C -- Risk Panel (Y: 15.3" to 21.5"):**

Rounded rect, fill `#1E2435`, left accent `#E05C5C`.

Three risk cards stacked:

Card 1 -- PYROPHORIC PRECURSORS (TMA, DEZ):
- W: 10.0", H: 1.8", fill `#E05C5C` at 15%, border 1 pt `#E05C5C`
- Title: `FIRE RISK` Barlow SemiBold 14 pt `#E05C5C`
- Body: `TMA and DEZ ignite on contact with air. Any residual vapor in the reactor or delivery lines reacts violently with atmospheric moisture during unloading. Extended purge + N2 vent eliminates this risk.`

Card 2 -- FILM CONTAMINATION:
- W: 10.0", H: 1.5", fill `#252B3D`, left accent `#E8A020`
- Title: `FILM CONTAMINATION` Barlow SemiBold 14 pt `#E8A020`
- Body: `Residual precursor on the film surface reacts with ambient H2O to form an uncontrolled, non-uniform top layer. This changes the film thickness and composition from what was intended.`

Card 3 -- REACTOR CONTAMINATION:
- W: 10.0", H: 1.5", fill `#252B3D`, left accent `#2EC4B6`
- Title: `REACTOR FOULING` Barlow SemiBold 14 pt `#2EC4B6`
- Body: `Residual precursor left in valves and lines reacts over time, clogging delivery paths. TMA residue is especially problematic -- it forms hard Al2O3 deposits inside valves.`

**Right -- Cooldown Protocol (X: 12.0", W: 11.5")**

**Section label:** `COOLDOWN BY SUBSTRATE TYPE` -- Y: 14.7".

**BLOCK D -- Cooldown Table (Y: 15.3" to 21.5"):**

| Substrate | ALD Temp | Cooldown Notes |
|---|---|---|
| Si wafer | 200-350 C | Cool under N2; < 100 C to unload; no thermal stress concern for ALD-thickness films |
| Glass | 200-300 C | Same; avoid thermal shock on thin glass (cool < 5 C/min if glass < 1 mm thick) |
| Polymer (PET, PC) | 80-150 C | Cool gently; polymer softening point is close to ALD temp; maintain vacuum or N2 |
| Metal parts | 150-350 C | No special concern; cool under inert; handle with clean gloves |
| Powders/particles | 150-300 C | Cool in sealed rotary reactor; transfer to inert container before air exposure if pyrophoric precursor residue possible |

Header: Barlow SemiBold 12 pt, fill `#3A4055`. Data: Inter Regular 12 pt `#F0EDE8`.

Below table:
- `ALD films are 1-100 nm thick. Thermal expansion mismatch stress is negligible at these thicknesses -- cooling rate is NOT a concern for the film. It is only a concern for the substrate (fragile glass, temperature-sensitive polymers).` Inter Medium 12 pt `#27AE60`

---

### ZONE 5 -- Safe Unloading + Handling Rules

**Two-column layout (Y: 22.0" to 28.3"):**

**Left -- Safe Unloading Procedure (X: 0.5", W: 11.0")**

**Section label:** `UNLOADING PROCEDURE` -- Y: 22.2". Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`.

**BLOCK E -- Step Sequence (Y: 22.8" to 28.0"):**

Rounded rect, fill `#1E2435`, left accent `#27AE60`.

Numbered steps (Inter Regular 13 pt `#F0EDE8`, line height 160%):
```
1. CONFIRM PURGE COMPLETE
   Pressure baseline clean and stable
   (no residual precursor partial pressure)

2. CONFIRM TEMPERATURE < 100 C
   Read substrate thermocouple directly

3. VENT WITH DRY N2
   Slowly bring reactor to atmospheric
   pressure using filtered, dry N2
   Never vent with compressed air
   (moisture + oil contamination)

4. OPEN CHAMBER
   Wear clean nitrile gloves
   If TMA/DEZ process: verify no smoke
   or odor before reaching in

5. REMOVE SUBSTRATES
   Handle by edges only (wafers)
   Place in clean, closed carrier
   immediately

6. CLOSE CHAMBER
   Re-pump to base pressure or N2 purge
   to keep reactor clean between runs
```

**Right -- Post-Deposition Handling Rules (X: 12.0", W: 11.5")**

**Section label:** `HANDLING ULTRATHIN ALD FILMS` -- Y: 22.2".

**BLOCK F -- Handling Rules (Y: 22.8" to 28.0"):**

Rounded rect, fill `#1E2435`, left accent `#E8A020`.

Five rule cards:

Card 1: `DO NOT TOUCH THE FILM SURFACE` Barlow SemiBold 13 pt `#E8A020`
- `A single fingerprint deposits 1-10 um of organic contamination. The ALD film is 1-100 nm. You would be burying the film under contamination 100x its own thickness.`

Card 2: `STORE IN CLEAN, CLOSED CONTAINERS` Barlow SemiBold 13 pt `#E8A020`
- `Wafer carriers, gel-paks, or N2-purged containers. Ambient dust particles (1-10 um) are giants compared to the film.`

Card 3: `MINIMIZE AIR EXPOSURE TIME` Barlow SemiBold 13 pt `#E8A020`
- `Some ALD films (TiN, ZnO) are sensitive to atmospheric moisture and O2. Characterize within hours if possible.`

Card 4: `HANDLE WAFERS BY EDGES ONLY` Barlow SemiBold 13 pt `#E8A020`
- `Use vacuum wands or edge-grip tweezers. Never contact the coated surface.`

Card 5: `LABEL IMMEDIATELY` Barlow SemiBold 13 pt `#E8A020`
- `Note: film, thickness target, cycle count, date, and reactor ID. Unlabeled samples are worthless.`

Inter Regular 12 pt `#F0EDE8` for body text.

---

### ZONE 6 -- Common End-of-Run Problems

**Section label:** `END-OF-RUN PROBLEMS` -- Y: 28.7".

**Four Problem Cards (Y: 29.3" to 32.0")**

Each card: Rounded rect W: 5.5", H: 2.5", fill `#1E2435`, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | SMOKE ON CHAMBER OPEN | Residual TMA reacting with air | Extend purge time; verify pressure baseline before vent |
| 2 | 6.33" | HAZE ON FILM SURFACE | Residual precursor reacted with ambient H2O | Longer final purge; vent with dry N2 only |
| 3 | 12.16" | THICKNESS ABOVE TARGET | Precursor residue formed extra layer during unloading | Purge completely; unload quickly after venting |
| 4 | 18.0" | PARTICLES ON SURFACE | Chamber wall flaking during vent | Regular reactor cleaning; gentle N2 vent (no pressure surges) |

---

### ZONE 7 -- Footer

Standard. Title: `Cooling & Final Purge -- ALD`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cooling Final Purge ALD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

ALD cooldown is fundamentally different from CVD cooldown -- it is fast, low-risk thermally, and dominated by the precursor purge step rather than temperature management. The hero timeline makes this clear visually: the extended purge bar is the largest element, communicating where the operator should focus. The fingerprint analogy in the handling rules (a fingerprint is 100x thicker than the film) is the kind of concrete comparison that sticks in an operator's mind.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #437 -- Construction Workup v1.0*
*2026-04-26*
