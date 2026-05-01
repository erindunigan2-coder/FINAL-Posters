---
Project: Plating Posters Inc
Poster Number: 463
Title: "Electropolishing Stage"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-30T00:00:00
Source: Poster 463 — Electropolishing Stage — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - Electropolishing
  - MainTank
  - SpecialtyAdvanced
  - ClusterSA07
  - v1
---

# Claude Chat Generation Prompt -- Poster #463
## Electropolishing Stage
### Version 1.0 | Dark + Light

*Alaina from CW v1.0 (2026-04-26).*

---

> **IMPORTANT:** Generate as HTML artifact. 24 x 36" portrait. Dark edition first.

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E`, locked palette, 0.5" safe zone. iOS Liquid Glass aesthetic. Fonts: Barlow Condensed 800 (headlines), Barlow 600 (subheads), Inter 400/500 (body), JetBrains Mono 400 (data/params).

---

## Phase 2 -- Header

### Step 1 -- `ELECTROPOLISHING` -- `80` pt `#F0EDE8`. Y: **0.5"**.
### Step 2 -- `The Electropolishing Tank -- Stage 5 of 8 -- PART IS ANODE (+)` -- `32` pt `#27AE60`. Y: **1.4"**.
### Step 3 -- `Controlled anodic dissolution in phosphoric-sulfuric acid. Smoothing, brightening, and passive layer enrichment in one operation.` -- `20` pt at 65%. Y: **2.1"**.

---

## Phase 3 -- Orientation Strip

Poster 5 of 10 highlighted. Stage 5 highlighted (Emerald).

---

## Phase 4 -- EP Tank Cross-Section (HERO)

Y: 4.2" to 14.5".

Section label: `THE ELECTROPOLISHING TANK`

Tank cross-section diagram:
- Tank body: rounded rect with `#C8D0D8` border, `#252B3D` fill (electrolyte)
- **Left + Right: ANODE (+) WORKPIECE** -- vertical rects, Emerald border. Label: `Viscous film layer` on surface.
- **Center: CATHODE (-) Cu or Pb** -- vertical rect, Silver border. Sub-label: `H2 gas evolved here`
- **Rectifier** above tank: `DC RECTIFIER` with (+) wires to anodes, (-) wire to cathode
- Dashed Amber current flow arrows from anode outward to cathode: `Metal ions dissolve from anode surface`

**POLARITY REVERSAL CALLOUT (Coral, prominent):**
`REVERSED POLARITY: The workpiece is the ANODE (+). Metal dissolves FROM the part. This is the opposite of electroplating.`

**Bath parameters inside tank:**

```
H3PO4: ~50% by vol          Time: 5--45 min
H2SO4: ~30% by vol          Agitation: mild (do not disrupt film)
Temp: 65--80 C (150--175 F) Ripple: < 5%
CD: 10--20 A/dm2             Cathode:anode ratio: 1:2 to 1:1
Voltage: 8--14 V
```

---

## Phase 5 -- Electrolyte + Polishing Plateau

Y: 14.5" to 20.5".

Section label: `ELECTROLYTE CHEMISTRY + THE POLISHING PLATEAU`

**Electrolyte by substrate table:**

| Substrate | Electrolyte | Temp | CD | Voltage | Notes |
|---|---|---|---|---|---|
| 300-series SS (304, 316) | H3PO4 50% + H2SO4 30% | 65--80 C | 10--20 A/dm2 | 8--14 V | Standard industrial EP |
| 400-series SS (410, 430) | H3PO4 + H2SO4 + glycerol | 50--80 C | 5--20 A/dm2 | 6--15 V | More sensitive to etching |
| Carbon steel | H3PO4 + H2SO4 | 50--80 C | 10--30 A/dm2 | 8--18 V | Higher CD needed |
| Copper alloys | H3PO4 60--85% (alone) | 20--50 C | 5--30 A/dm2 | 1--6 V | Lower temp, lower voltage |
| Nickel alloys | H2SO4 + citric/glycolic | 50--80 C | 5--15 A/dm2 | 8--18 V | Proprietary blends |

**Three voltage regimes (horizontal segmented bar):**

| Regime | Color | What Happens |
|---|---|---|
| ETCHING | `#E05C5C` | Low voltage: active dissolution, matte surface -- NOT polishing |
| POLISHING PLATEAU | `#27AE60` | Current constant despite voltage increase -- operate HERE |
| GAS EVOLUTION | `#E05C5C` | O2 bubbles: pitting, streaks, gas marks |

Note: `Always run a test coupon to locate the polishing plateau for your specific electrolyte and substrate.`

---

## Phase 6 -- Defects + Surface Finish Results

Y: 20.5" to 32.5".

**6 Common EP Defects (3x2 grid):**

| Defect | Accent | Cause | Fix |
|---|---|---|---|
| PITTING | `#E05C5C` | Above plateau; Cl-; MnS inclusions (303 SS) | Verify voltage; test for Cl-; avoid 303 |
| ORANGE PEEL | `#E8A020` | Below plateau; insufficient time | Increase voltage; extend time |
| STREAKING | `#E8A020` | Non-uniform current; gas entrapment | Reposition parts; tilt for gas escape |
| STAINING | `#E05C5C` | Slow removal; iron contamination; poor rinse | Immediate rinse; maintain purity |
| UNEVEN FINISH | `#2EC4B6` | Poor contact; fixture shielding; spacing | Check contacts; redesign fixture |
| ETCHING (MATTE) | `#E05C5C` | Too hot; too concentrated; excessive current | Check temp; analyze solution; verify plateau |

**Surface Roughness Improvement (Emerald accent):**

| Starting Ra | After EP Ra | Improvement |
|---|---|---|
| 0.8 um (32 uin) | 0.2--0.4 um (8--16 uin) | 50--75% |
| 0.4 um (16 uin) | 0.1--0.2 um (4--8 uin) | 50--75% |
| 0.2 um (8 uin) | 0.05--0.1 um (2--4 uin) | ~50% |

Best achievable: `Ra 0.05 um (2 uin) with excellent starting surface`

**Passive Layer Enrichment (Teal accent):**

```
Cr/Fe surface ratio:
  Mechanically polished: ~0.4
  After electropolishing: 1.0--1.5

EP preferentially dissolves iron, enriching chromium
in the passive oxide layer.

Standards: ASTM B912 | ASME BPE SF4 | SEMI F19
```

---

## Phase 7 -- Footer

Standard. Title: `Electropolishing Stage`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; ASTM B912; ASME BPE; typical H3PO4/H2SO4 electrolyte parameters for stainless steel. Proprietary electrolyte formulations vary.`

---

## Phase 8 -- Review

- [ ] Headline `ELECTROPOLISHING` 80pt
- [ ] Orientation strip with poster 5 of 10, stage 5 highlighted
- [ ] Tank cross-section with reversed polarity clearly labeled
- [ ] Polarity reversal callout (Coral, prominent)
- [ ] Electrolyte by substrate table (5 substrates)
- [ ] Three voltage regimes bar
- [ ] 6-defect grid
- [ ] Ra improvement table + Cr/Fe enrichment
- [ ] Footer with disclaimer and version

---

## Phase 9 -- Light Remap & Export

Standard remap. Verify accent legibility on light background.

Six files: `Electropolishing Stage -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-30 | Initial. |
