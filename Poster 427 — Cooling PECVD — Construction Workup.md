---
Project: Plating Posters Inc
Poster Number: 427
Title: "Cooling -- PECVD"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 3: PECVD, Sections 3.7, 3.8)"
Technical Source: PECVD post-deposition cooling, purge, vent, and unloading protocols. Cooling under vacuum or inert atmosphere prevents oxidation of freshly deposited films. Venting a hot substrate to atmosphere causes surface oxidation, discoloration, and potential thermal stress cracking.
Process Scope: PECVD plasma shutdown, chamber purge, substrate cooling, venting, and unloading
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - PECVD
  - Cooling
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #427 -- Construction Workup
## Cooling -- PECVD

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stages 7 and 8 of the PECVD sequence combined -- cooling, purge, vent, and unloading. This poster covers everything between "plasma off" and "part in your hand." The core message: patience. Venting a hot substrate to air ruins the film you just spent an hour depositing. The rule card stat is the magic number: cool to below 80 degC before you vent.

Silver dominates -- this is a post-process/handling stage.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Post-deposition sequence flow (Block B -- HERO):** Vertical timeline from plasma off through purge, cool, vent, and unload.
2. **Why cooling matters (Block C):** Oxidation, thermal stress, and film integrity callouts.
3. **Cooling methods comparison (Block D):** Vacuum cooldown vs. inert gas backfill vs. active cooling.
4. **Unloading protocol (Block E):** Clean handling, chamber inspection, and contamination prevention.
5. **Common mistakes (Block F):** 4-card strip of cooling/unloading errors.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.0" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stages 7-8 highlighted (Silver)
ZONE 3 -- POST-DEPOSITION SEQUENCE HERO (4.2"--14.5" / ~10.3")
  Block B: Timeline from plasma off to unload
ZONE 4 -- WHY COOLING MATTERS + METHODS (14.5"--20.0" / ~5.5")
  Block C: Oxidation and thermal stress
  Block D: Cooling methods comparison
ZONE 5 -- UNLOADING PROTOCOL + COMMON MISTAKES (20.0"--32.5" / ~12.5")
  Block E: Unloading and handling
  Block F: Common mistakes strip
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `COOLING & UNLOADING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `PECVD -- Stages 7-8 of 10 -- Plasma Off to Part in Hand` -- 28 pt `#C8D0D8` (Silver). Y: 1.4".
**Tagline:** `The film is fragile when it is hot. Cool it under vacuum, purge it with inert gas, and do not touch it until it is ready. Patience protects your process.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

**Rule Card (top right):**
- Rounded rect, X: 17.0", Y: 0.5", W: 6.5", H: 2.2", fill `#1E2435`, border 1 pt `#C8D0D8`
- Big number: `< 80` -- Barlow Condensed ExtraBold, 64 pt, `#C8D0D8`
- Label: `degC BEFORE VENT` -- JetBrains Mono Regular, 14 pt, `#F0EDE8` at 70%
- Sub-label: `Cool to below 80 degC before opening to air` -- Inter Regular, 12 pt, `#F0EDE8` at 50%

---

### ZONE 2 -- Orientation Strip

Stages 7 (`Cooling`) and 8 (`Unloading`): fill `#C8D0D8`, text `#1A1F2E`. Others dimmed.
Below: `Input: Deposited film at process temperature  -->  Output: Cooled, unloaded parts ready for inspection`

---

### ZONE 3 -- Post-Deposition Sequence Hero

**Section label:** `FROM PLASMA OFF TO PART IN HAND` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Post-Deposition Timeline**

Y: 5.0" to 14.3". Full width.

Five sequential steps in a vertical flow, full width. Each step is a rounded rect, W: 23.0", H: 1.5", with left accent and connecting arrows.

**Step 1: PLASMA OFF**
- Fill `#1E2435`, left accent 4 pt `#27AE60`
- Badge: `STEP 1` -- fill `#27AE60`, text `#1A1F2E`
- Title: `Extinguish Plasma` -- Barlow SemiBold, 18 pt, `#F0EDE8`
- Details: `RF power off. Gas flows stop (SiH4, NH3, N2O). Plasma glow extinguishes immediately.` -- Inter Regular, 13 pt, `#F0EDE8`
- Parameter: `RF power: 0 W. All precursor MFCs: closed.` -- JetBrains Mono, 12 pt, `#27AE60`

**Step 2: PURGE**
- Fill `#1E2435`, left accent 4 pt `#2EC4B6`
- Badge: `STEP 2` -- fill `#2EC4B6`, text `#1A1F2E`
- Title: `Inert Gas Purge` -- Barlow SemiBold, 18 pt, `#F0EDE8`
- Details: `Flow N2 or Ar through chamber to sweep out residual process gases and byproducts.` -- Inter Regular, 13 pt, `#F0EDE8`
- Parameter: `N2/Ar flow: 100--500 sccm. Duration: 2--5 min. Pressure: maintained or slowly rising.` -- JetBrains Mono, 12 pt, `#2EC4B6`

**Step 3: COOL**
- Fill `#1E2435`, left accent 4 pt `#C8D0D8`
- Badge: `STEP 3` -- fill `#C8D0D8`, text `#1A1F2E`
- Title: `Cool Substrate` -- Barlow SemiBold, 18 pt, `#F0EDE8`
- Details: `Heater off or ramped down. Substrate cools under vacuum or continued N2 flow. Monitor temperature.` -- Inter Regular, 13 pt, `#F0EDE8`
- Parameter: `Target: < 80 degC (industrial) or < 50 degC (semiconductor). Time: 15--60 min depending on thermal mass.` -- JetBrains Mono, 12 pt, `#C8D0D8`

**Step 4: VENT**
- Fill `#1E2435`, left accent 4 pt `#E8A020`
- Badge: `STEP 4` -- fill `#E8A020`, text `#1A1F2E`
- Title: `Vent Chamber to Atmosphere` -- Barlow SemiBold, 18 pt, `#F0EDE8`
- Details: `Backfill with dry N2 (preferred) or filtered dry air. Slow vent rate to avoid particle disturbance.` -- Inter Regular, 13 pt, `#F0EDE8`
- Parameter: `Vent through filtered N2 line. Vent time: 2--5 min. Wait until pressure equalizes.` -- JetBrains Mono, 12 pt, `#E8A020`

**Step 5: UNLOAD**
- Fill `#1E2435`, left accent 4 pt `#E8A020`
- Badge: `STEP 5` -- fill `#E8A020`, text `#1A1F2E`
- Title: `Open Chamber and Remove Parts` -- Barlow SemiBold, 18 pt, `#F0EDE8`
- Details: `Wear clean nitrile gloves. Handle by edges only. Transfer to clean container immediately.` -- Inter Regular, 13 pt, `#F0EDE8`
- Parameter: `Inspect chamber interior. Note any wall buildup or flaking for next maintenance cycle.` -- JetBrains Mono, 12 pt, `#E8A020`

Arrows between steps: 3 pt `#3A4055`, down, centered.

---

### ZONE 4 -- Why Cooling Matters + Methods

**BLOCK C -- Why Cooling Matters (Left, X: 0.5", W: 11.0")**

Section label: `WHY YOU MUST COOL BEFORE VENTING` -- Y: 14.7". Barlow Condensed ExtraBold, 22 pt, `#E05C5C`.

Three callout rows:

Row 1 -- Oxidation:
- Left accent `#E05C5C`
- `HOT FILM + AIR = SURFACE OXIDATION` -- Barlow SemiBold, 16 pt, `#E05C5C`
- `A freshly deposited SiNx film at 350 degC exposed to air forms an unwanted SiO2 surface layer. This changes optical properties (refractive index) and electrical properties (charge density). For solar cells, this ruins passivation quality.` -- Inter Regular, 12 pt, `#F0EDE8`

Row 2 -- Thermal Stress:
- Left accent `#E8A020`
- `RAPID COOLING = THERMAL STRESS = CRACKING` -- Barlow SemiBold, 16 pt, `#E8A020`
- `Film and substrate have different thermal expansion coefficients. Rapid cooling creates differential contraction, generating stress that can crack the film or cause delamination.` -- Inter Regular, 12 pt, `#F0EDE8`

Row 3 -- Contamination:
- Left accent `#2EC4B6`
- `HOT SURFACES ATTRACT PARTICLES` -- Barlow SemiBold, 16 pt, `#2EC4B6`
- `Thermophoretic forces drive particles away from hot surfaces during deposition. When the surface cools, this protection disappears. Particles settle on the film during cooldown -- minimize time spent at intermediate temperatures.` -- Inter Regular, 12 pt, `#F0EDE8`

**BLOCK D -- Cooling Methods (Right, X: 12.0", W: 11.5")**

Section label: `COOLING METHODS COMPARED` -- Y: 14.7".

Three method cards:

| Method | Description | Speed | Best For |
|---|---|---|---|
| Vacuum Cooldown | Heater off; substrate radiates heat; no convection | Slow (30--60 min) | High-quality films; semiconductor |
| Inert Gas Backfill | N2 or Ar at 1--10 Torr; convective cooling added | Moderate (15--30 min) | Industrial; balance of speed and quality |
| Active Cooling | Helium backside cooling or water-cooled chuck | Fast (5--15 min) | High-throughput production tools |

Note: `Helium backside cooling works by flooding the gap between substrate and chuck with He gas (excellent thermal conductor). Requires electrostatic or mechanical clamping.` -- Inter Regular, 12 pt, `#F0EDE8` at 70%

---

### ZONE 5 -- Unloading Protocol + Common Mistakes

**BLOCK E -- Unloading Protocol (Y: 20.2" to 26.3")**

Section label: `UNLOADING -- CLEAN HANDLING IS NOT OPTIONAL` -- Barlow Condensed ExtraBold, 22 pt, `#E8A020`. Y: 20.4".

Two-column layout:

Left -- Handling Rules (X: 0.5", W: 11.0"):
Callout panel, fill `#1E2435`, left accent `#E8A020`.

Numbered checklist:
```
1. Wear fresh clean nitrile gloves (no reuse)
2. Handle substrates by edges only -- NEVER touch film surface
3. Transfer to clean container (FOUP, cassette, or lint-free tray)
4. Label with run ID, date, operator, and recipe
5. If inspection is not immediate: store in N2 purged cabinet
6. For semiconductor: return to cleanroom ASAP
```

Right -- Chamber Inspection (X: 12.0", W: 11.5"):
Callout panel, fill `#1E2435`, left accent `#2EC4B6`.

```
After EVERY unload:
- Look at chamber walls -- any flaking or discoloration?
- Check showerhead -- any clogged holes?
- Inspect O-ring -- any debris or damage?
- Note deposition count since last chamber clean
- If wall buildup is visible: schedule chamber clean BEFORE next production run
```

Bottom note: `A 5-minute chamber inspection after every run prevents hours of rework from particle-contaminated films.` -- Inter Medium, 13 pt, `#2EC4B6`

**BLOCK F -- Common Cooling/Unloading Mistakes (Y: 27.0" to 32.3")**

Section label: `MISTAKES THAT RUIN PERFECTLY GOOD FILMS` -- Barlow Condensed ExtraBold, 22 pt, `#E05C5C`. Y: 27.2".

Four cards in single row:

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | HOT VENTING | Impatient operator vents at > 100 degC | Always verify temp < 80 degC on thermocouple before vent command |
| 2 | 6.33" | FINGERPRINTS ON FILM | Gloves removed or contaminated during unloading | Fresh gloves every time; handle edges only; if contaminated, film may not be salvageable |
| 3 | 12.16" | PARTICLE BURST ON VENT | Rapid vent dislodges wall particles onto film | Slow vent through filtered N2; never rapid vent |
| 4 | 18.0" | SKIPPING CHAMBER INSPECTION | Assume chamber is clean from last run | Always inspect; buildup is cumulative and invisible until it flakes |

Card format: Rounded rect, W: 5.5", H: 4.8", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 12 pt, `#F0EDE8`
- Fix: Inter Medium, 12 pt, `#27AE60`

---

### ZONE 6 -- Footer

Standard. Title: `Cooling & Unloading -- PECVD`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Cooling protocols shown are typical industry values. Specific cooldown times and venting procedures vary by equipment and film type. Consult your equipment manufacturer and process specifications.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cooling PECVD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster combines PECVD stages 7 (Cooling) and 8 (Unloading) because they are a continuous workflow -- you do not cool a substrate and then walk away; cooling flows directly into venting and unloading. The vertical timeline hero is the natural layout: top to bottom mirrors the real-world sequence. The "< 80 degC" rule card is the one number an operator needs to remember from this poster.

The "why cooling matters" section is where the science lives -- thermal stress, oxidation, and particle dynamics are genuinely interesting and non-obvious to someone coming from a wet chemistry background.

---

*Alaina -- Poster #427 -- Construction Workup v1.0 -- 2026-04-26*
