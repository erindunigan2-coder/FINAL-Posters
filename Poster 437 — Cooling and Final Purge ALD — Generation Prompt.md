---
Project: Plating Posters Inc
Poster Number: 437
Title: "Cooling & Final Purge -- ALD"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-28T00:00:00
Source: Poster 437 — Cooling and Final Purge ALD — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - ALD
  - AtomicLayerDeposition
  - PostProcess
  - ThinFilm
  - ClusterTF04
  - v1
---

# Claude Chat Generation Prompt -- Poster #437
## Cooling & Final Purge -- ALD
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-28).*

---

> **IMPORTANT:** Generate as SVG or HTML visual artifact. 24 x 36" portrait. Dark edition first.

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E`, locked palette, 0.5" safe zone. iOS Liquid Glass aesthetic. Fonts: Barlow Condensed 800 (headlines), Barlow 600 (subheads), Inter 400/500 (body), JetBrains Mono 400 (data/params).

---

## Phase 2 -- Header

### Step 1 -- `COOLING & FINAL PURGE` -- `72` pt `#F0EDE8`. Y: **0.5"**.
### Step 2 -- `ALD -- Stage 9 of 10 -- Clearing Residual Precursors and Safe Unloading` -- `32` pt `#E8A020`. Y: **1.4"**.
### Step 3 -- `The last ALD cycle is done. Now purge every trace of precursor from the system before opening to air -- especially if that precursor is pyrophoric.` -- `20` pt at 65%. Y: **2.1"**.

---

## Phase 3 -- Orientation Strip

Poster 9 of 10 highlighted.

---

## Phase 4 -- Final Purge + Cooldown Timeline Hero

Y: 5.0" to 14.0".

| Phase | Color | X Start | Width | Y | Height | Label |
|---|---|---|---|---|---|---|
| Last ALD Cycle | `#E8A020` at 40% | 1.5" | 1.5" | 8.5" | 1.3" | `LAST CYCLE` |
| Extended Purge | `#2EC4B6` | 3.2" | 6.0" | 7.5" | 2.3" | `EXTENDED FINAL PURGE` |
| Heater Off | `#3A4055` | 9.5" | 1.5" | 8.5" | 1.3" | `HEATER OFF` |
| Cooldown | `#27AE60` at 40% | 11.2" | 5.0" | 8.0" | 1.8" | `COOLDOWN` |
| Vent/Unload | `#E8A020` | 16.5" | 3.0" | 8.5" | 1.3" | `VENT & UNLOAD` |

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

```
Substrate cools from ALD temp (150-350 C)
to < 100 C under flowing inert gas.
Time: 15-30 min (varies by reactor thermal mass).
No thermal stress risk -- ALD films are ultra-thin.
```

```
Reactor vented to atmospheric pressure
with dry N2. Open chamber only after
temperature confirmed < 100 C.
```

---

## Phase 5 -- Why Purge Matters + Cooldown Protocol

Y: 14.5" to 21.8".

| Substrate | ALD Temp | Cooldown Notes |
|---|---|---|
| Si wafer | 200-350 C | Cool under N2; < 100 C to unload; no thermal stress concern for ALD-thickness films |
| Glass | 200-300 C | Same; avoid thermal shock on thin glass (cool < 5 C/min if glass < 1 mm thick) |
| Polymer (PET, PC) | 80-150 C | Cool gently; polymer softening point is close to ALD temp; maintain vacuum or N2 |
| Metal parts | 150-350 C | No special concern; cool under inert; handle with clean gloves |
| Powders/particles | 150-300 C | Cool in sealed rotary reactor; transfer to inert container before air exposure if pyrophoric precursor residue possible |

Callout: `TMA and DEZ ignite on contact with air. Any residual vapor in the reactor or delivery lines reacts violently with atmospheric moisture during unloading. Extended purge + N2 vent eliminates this risk.`

Callout: `Residual precursor on the film surface reacts with ambient H2O to form an uncontrolled, non-uniform top layer. This changes the film thickness and composition from what was intended.`

Callout: `Residual precursor left in valves and lines reacts over time, clogging delivery paths. TMA residue is especially problematic -- it forms hard Al2O3 deposits inside valves.`

---

## Phase 6 -- Safe Unloading + Handling Rules

Y: 22.0" to 28.3".

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

---

## Phase 7 -- Common End-of-Run Problems

Y: 29.3" to 32.0".

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | SMOKE ON CHAMBER OPEN | Residual TMA reacting with air | Extend purge time; verify pressure baseline before vent |
| 2 | 6.33" | HAZE ON FILM SURFACE | Residual precursor reacted with ambient H2O | Longer final purge; vent with dry N2 only |
| 3 | 12.16" | THICKNESS ABOVE TARGET | Precursor residue formed extra layer during unloading | Purge completely; unload quickly after venting |
| 4 | 18.0" | PARTICLES ON SURFACE | Chamber wall flaking during vent | Regular reactor cleaning; gentle N2 vent (no pressure surges) |

---

## Phase 8 -- Footer

Standard. Title: `Cooling & Final Purge -- ALD`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge. Consult your process supplier for application-specific guidance.`

---

## Phase 9 -- Review

- [ ] Headline `COOLING & FINAL PURGE` 72pt
- [ ] Orientation strip with poster 9 highlighted
- [ ] Footer with disclaimer and version

---

## Phase 10 -- Light Remap & Export

Standard remap. Verify accent legibility on light background.

Six files: `Cooling & Final Purge ALD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-28 | Initial. |
