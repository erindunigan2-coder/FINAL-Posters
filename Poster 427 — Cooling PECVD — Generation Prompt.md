---
Project: Plating Posters Inc
Poster Number: 427
Title: "Cooling -- PECVD"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-28T00:00:00
Source: Poster 427 — Cooling PECVD — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - PECVD
  - PlasmaEnhancedCVD
  - PostProcess
  - ThinFilm
  - ClusterTF03
  - v1
---

# Claude Chat Generation Prompt -- Poster #427
## Cooling -- PECVD
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-28).*

---

> **IMPORTANT:** Generate as SVG or HTML visual artifact. 24 x 36" portrait. Dark edition first.

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E`, locked palette, 0.5" safe zone. iOS Liquid Glass aesthetic. Fonts: Barlow Condensed 800 (headlines), Barlow 600 (subheads), Inter 400/500 (body), JetBrains Mono 400 (data/params).

---

## Phase 2 -- Header

### Step 1 -- `COOLING & UNLOADING` -- `80` pt `#F0EDE8`. Y: **0.5"**.
### Step 2 -- `PECVD -- Stages 7-8 of 10 -- Plasma Off to Part in Hand` -- `32` pt `#C8D0D8`. Y: **1.4"**.
### Step 3 -- `The film is fragile when it is hot. Cool it under vacuum, purge it with inert gas, and do not touch it until it is ready. Patience protects your process.` -- `20` pt at 65%. Y: **2.1"**.

---

## Phase 3 -- Orientation Strip

Poster 9 of 10 highlighted.

---

## Phase 4 -- Post-Deposition Sequence Hero

Y: 5.0" to 14.3".

- Badge: `STEP 1` -- fill `#27AE60`, text `#1A1F2E`
- Title: `Extinguish Plasma` -- Barlow SemiBold, 18 pt, `#F0EDE8`
- Details: `RF power off. Gas flows stop (SiH4, NH3, N2O). Plasma glow extinguishes immediately.` -- Inter Regular, 13 pt, `#F0EDE8`
- Parameter: `RF power: 0 W. All precursor MFCs: closed.` -- JetBrains Mono, 12 pt, `#27AE60`
- Badge: `STEP 2` -- fill `#2EC4B6`, text `#1A1F2E`
- Title: `Inert Gas Purge` -- Barlow SemiBold, 18 pt, `#F0EDE8`
- Details: `Flow N2 or Ar through chamber to sweep out residual process gases and byproducts.` -- Inter Regular, 13 pt, `#F0EDE8`
- Parameter: `N2/Ar flow: 100--500 sccm. Duration: 2--5 min. Pressure: maintained or slowly rising.` -- JetBrains Mono, 12 pt, `#2EC4B6`
- Badge: `STEP 3` -- fill `#C8D0D8`, text `#1A1F2E`
- Title: `Cool Substrate` -- Barlow SemiBold, 18 pt, `#F0EDE8`
- Details: `Heater off or ramped down. Substrate cools under vacuum or continued N2 flow. Monitor temperature.` -- Inter Regular, 13 pt, `#F0EDE8`
- Parameter: `Target: < 80 degC (industrial) or < 50 degC (semiconductor). Time: 15--60 min depending on thermal mass.` -- JetBrains Mono, 12 pt, `#C8D0D8`

---

## Phase 5 -- Why Cooling Matters + Methods


| Method | Description | Speed | Best For |
|---|---|---|---|
| Vacuum Cooldown | Heater off; substrate radiates heat; no convection | Slow (30--60 min) | High-quality films; semiconductor |
| Inert Gas Backfill | N2 or Ar at 1--10 Torr; convective cooling added | Moderate (15--30 min) | Industrial; balance of speed and quality |
| Active Cooling | Helium backside cooling or water-cooled chuck | Fast (5--15 min) | High-throughput production tools |

---

## Phase 6 -- Unloading Protocol + Common Mistakes

Y: 20.2" to 26.3".
Section: `100 degC | Always verify temp < 80 degC on thermocouple before vent command |`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | HOT VENTING | Impatient operator vents at > 100 degC | Always verify temp < 80 degC on thermocouple before vent command |
| 2 | 6.33" | FINGERPRINTS ON FILM | Gloves removed or contaminated during unloading | Fresh gloves every time; handle edges only; if contaminated, film may not be salvageable |
| 3 | 12.16" | PARTICLE BURST ON VENT | Rapid vent dislodges wall particles onto film | Slow vent through filtered N2; never rapid vent |
| 4 | 18.0" | SKIPPING CHAMBER INSPECTION | Assume chamber is clean from last run | Always inspect; buildup is cumulative and invisible until it flakes |

```
1. Wear fresh clean nitrile gloves (no reuse)
2. Handle substrates by edges only -- NEVER touch film surface
3. Transfer to clean container (FOUP, cassette, or lint-free tray)
4. Label with run ID, date, operator, and recipe
5. If inspection is not immediate: store in N2 purged cabinet
6. For semiconductor: return to cleanroom ASAP
```

```
After EVERY unload:
- Look at chamber walls -- any flaking or discoloration?
- Check showerhead -- any clogged holes?
- Inspect O-ring -- any debris or damage?
- Note deposition count since last chamber clean
- If wall buildup is visible: schedule chamber clean BEFORE next production run
```

---

## Phase 7 -- Footer

Standard. Title: `Cooling -- PECVD`. Version `v1.0 -- 2026`.
Disclaimer: `This poster is an educational reference tool. Cooling protocols shown are typical industry values. Specific cooldown times and venting procedures vary by equipment and film type. Consult your equipment manufacturer and process specifications.`

---

## Phase 8 -- Review

- [ ] Headline `COOLING & UNLOADING` 80pt
- [ ] Orientation strip with poster 9 highlighted
- [ ] Footer with disclaimer and version

---

## Phase 9 -- Light Remap & Export

Standard remap. Verify accent legibility on light background.

Six files: `Cooling PECVD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-28 | Initial. |
