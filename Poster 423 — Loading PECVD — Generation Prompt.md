---
Project: Plating Posters Inc
Poster Number: 423
Title: "Loading -- PECVD"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-28T00:00:00
Source: Poster 423 — Loading PECVD — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - PECVD
  - PlasmaEnhancedCVD
  - Loading
  - ThinFilm
  - ClusterTF03
  - v1
---

# Claude Chat Generation Prompt -- Poster #423
## Loading -- PECVD
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-28).*

---

> **IMPORTANT:** Generate as SVG or HTML visual artifact. 24 x 36" portrait. Dark edition first.

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E`, locked palette, 0.5" safe zone. iOS Liquid Glass aesthetic. Fonts: Barlow Condensed 800 (headlines), Barlow 600 (subheads), Inter 400/500 (body), JetBrains Mono 400 (data/params).

---

## Phase 2 -- Header

### Step 1 -- `LOADING` -- `88` pt `#F0EDE8`. Y: **0.5"**.
### Step 2 -- `PECVD -- Stage 3 of 10 -- Fixturing, Chamber Closure, and Pump-Down` -- `32` pt `#C8D0D8`. Y: **1.4"**.
### Step 3 -- `The electrode gap sets the plasma. The pump-down sets the purity. Get both right before you strike a glow.` -- `20` pt at 65%. Y: **2.1"**.

---

## Phase 3 -- Orientation Strip

Poster 5 of 10 highlighted.

---

## Phase 4 -- Chamber Cross-Section Hero

Y: 5.0" to 14.3".

- Rect, X: 4.0", Y: 6.0", W: 16.0", H: 0.8", fill `#3A4055`, border 1 pt `#C8D0D8`
- Label above: `TOP ELECTRODE (SHOWERHEAD)` Barlow SemiBold, 14 pt, `#C8D0D8`
- Small circles (gas holes) in row across bottom of electrode: 8 circles, 0.2" dia, fill `#1A1F2E`
- Label: `Gas inlet -- uniform distribution` Inter Regular, 11 pt, `#F0EDE8` at 60%
- Rect, X: 4.0", Y: 11.0", W: 16.0", H: 0.8", fill `#3A4055`, border 1 pt `#E8A020`
- Label below: `BOTTOM ELECTRODE (SUBSTRATE HOLDER)` Barlow SemiBold, 14 pt, `#E8A020`
- Sub-label: `Temperature-controlled; RF or DC biased` Inter Regular, 11 pt, `#F0EDE8` at 60%
- Rect, X: 6.0", Y: 10.5", W: 12.0", H: 0.4", fill `#2EC4B6` at 40%, border 2 pt `#2EC4B6`
- Label: `SUBSTRATE` Barlow SemiBold, 12 pt, `#2EC4B6`
- Double-headed arrow between bottom of top electrode and top of substrate
- Label: `GAP: 10--50 mm` JetBrains Mono Regular, 16 pt, `#E8A020`
- Note: `Smaller gap = higher power density. Larger gap = more uniform but lower rate.` Inter Regular, 12 pt, `#F0EDE8` at 70%
- Line from external label to bottom electrode
- Label: `RF POWER (13.56 MHz)` JetBrains Mono, 12 pt, `#E8A020`

---

## Phase 5 -- Loading Sequence + Pump-Down

Section: `1 Torr | 2--5 min | Rotary vane or scroll pump |`.

| Phase | Pressure | Time | Action |
|---|---|---|---|
| Roughing | Atm -> 1 Torr | 2--5 min | Rotary vane or scroll pump |
| Crossover | 1 Torr -> 50 mTorr | 5--15 min | Roots blower engages |
| Base vacuum | < 50 mTorr | 10--30 min | Turbo (if equipped) for final pump |
| Leak check | Rate of rise < 5 mTorr/min | 2 min | Isolate pump; watch pressure gauge |
| Bake-out (optional) | At base vacuum | 15--30 min | Heat substrate to process temp; outgas |

---

## Phase 6 -- Electrode Gap + Common Mistakes

Y: 22.2" to 27.0".
Section: `300 mm) depositions`.

| Application | Gap | Substrate Size |
|---|---|---|
| Semiconductor (wafer) | 15--25 mm | 200--300 mm |
| Solar cell (panel) | 20--40 mm | 300+ mm |
| DLC on parts | 20--30 mm | Variable |
| Barrier coating (roll-to-roll) | 10--20 mm | Web width |

| Card | Problem | Cause | Fix |
|---|---|---|---|
| 1 | POOR THERMAL CONTACT | Substrate not flat on electrode; air gap | Use thermal paste, clamping ring, or He backside cooling |
| 2 | FINGERPRINTS ON SUBSTRATE | Handling after final clean | ALWAYS wear clean nitrile gloves during loading |
| 3 | O-RING SEAL FAILURE | Dirty, cracked, or misaligned O-ring | Inspect and lube O-rings per schedule; replace annually |
| 4 | SLOW PUMP-DOWN | Virtual leak from trapped gas or outgassing | Check for blind holes, trapped volumes; bake if needed |

```
Smaller gap (10--20 mm):
  Higher power density at substrate
  Faster deposition rate
  Less uniform across large areas
  Risk of arcing if too small

Larger gap (30--50 mm):
  Better uniformity across substrate
  Lower deposition rate
  More gas-phase reactions (particles!)
  Standard for large-area (>300 mm) depositions
```

---

## Phase 7 -- Footer

Standard. Title: `Loading -- PECVD`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge. Consult your process supplier for application-specific guidance.`

---

## Phase 8 -- Review

- [ ] Headline `LOADING` 88pt
- [ ] Orientation strip with poster 5 highlighted
- [ ] Footer with disclaimer and version

---

## Phase 9 -- Light Remap & Export

Standard remap. Verify accent legibility on light background.

Six files: `Loading PECVD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-28 | Initial. |
