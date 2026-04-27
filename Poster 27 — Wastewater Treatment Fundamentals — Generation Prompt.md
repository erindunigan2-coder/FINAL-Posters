---
Project: Plating Posters Inc
Poster Number: 27
Title: "Wastewater Treatment Fundamentals -- From Rinse Tank to Discharge"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-25T00:00:00
Source: Poster 27 -- Wastewater Treatment Fundamentals -- Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - WastewaterTreatment
  - EnvironmentalCompliance
  - HydroxidePrecipitation
  - CyanideDestruction
  - v1
---

# Claude Chat Generation Prompt -- Poster #27
## Wastewater Treatment Fundamentals -- From Rinse Tank to Discharge
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-25).*

---

> **IMPORTANT:** Generate as HTML visual artifact. 24 x 36" portrait. Dark edition first. This poster is content-dense with a large process flow diagram, pH precipitation chart, and two special waste stream procedures. NO specific mg/L discharge limits -- the poster directs operators to their individual permit instead.

---

## Phase 0 -- Design System Reference

Follow `Plating Posters - Series Design Prompt.md` exactly. Key reminders:

- Stage: 1200x1800 CSS px, scaled via `transform: scale()`
- Glass surfaces: `rgba(30,36,53,.55)` solid fallback + gradient + border + `backdrop-filter`. NEVER `color-mix()`.
- Three ambient orbs + faint grid background
- Print CSS: `@page { size: 12.5in 18.75in; margin: 0; }`
- Tweaks panel: Dark/Light + Grid + Print, floating bottom-right
- Light edition via `body[data-edition="light"]` overrides
- Fonts CDN: Barlow Condensed 800/900, Barlow 600/700, Inter 400/500/600, JetBrains Mono 400/500

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E` background, locked palette, 0.5" (25px) safe zone. Full palette:

| Token | Hex | Use |
|---|---|---|
| `--bg` | `#1A1F2E` | Background |
| `--text` | `#F0EDE8` | Primary text |
| `--amber` | `#E8A020` | pH values, chrome reduction, caution |
| `--teal` | `#2EC4B6` | Flow indicators, treatment stages |
| `--emerald` | `#27AE60` | Compliant discharge, best practices |
| `--coral` | `#E05C5C` | Violations, cyanide hazard, warnings |
| `--slate` | `#3A4055` | Table headers, tank outlines |
| `--navy` | `#0D1020` | Footer |
| `--callout` | `#1E2435` | Card fills |
| `--altrow` | `#252B3D` | Alt rows, pH scale bar |
| `--silver` | `#C8D0D8` | Flow arrows, neutral |

---

## Phase 2 -- Header (Zone 1)

### Step 1 -- Headline
`WASTEWATER TREATMENT FUNDAMENTALS` -- Barlow Condensed 800, large (~80px), `#F0EDE8`. Y: **0.5"**.

### Step 2 -- Subheading
`From Rinse Tank to Discharge -- Every Drop Is Regulated` -- Barlow 600, 28px, `#2EC4B6`. Y: **1.4"**.

### Step 3 -- Compliance Callout Banner
Full-width coral-tinted glass banner spanning the poster width (inside safe zone). Coral border, coral-tinted fill (`rgba(224,92,92,.12)`).
Text (centered): Barlow Condensed 800, ~18px, `#E05C5C`:
`PERMIT VIOLATIONS CARRY SIGNIFICANT FINES AND CRIMINAL LIABILITY -- ALWAYS OPERATE TO YOUR DISCHARGE PERMIT`

---

## Phase 3 -- Treatment System Flow Diagram (Zone 2 -- HERO)

Y: ~170px to ~700px. Section label: `THE TREATMENT PROCESS -- STEP BY STEP`.

### Step 4 -- Process Flow Schematic

Build from labeled glass rectangles connected by arrow elements. Two rows forming an L/U shape:

**Row 1 (left to right):**
1. `EQUALIZATION TANK` -- slate border. Description: `Mix all waste streams. Equalize flow rate and chemistry.`
2. `pH ADJUSTMENT` -- amber border. Description: `Raise pH with NaOH or Ca(OH)2 to precipitation target.`
3. `COAGULANT / FLOCCULANT` -- teal border. Description: `Add polymer flocculant. Gentle mixing to form settable floc.`

Arrow connecting Row 1 to Row 2 (down-right turn).

**Row 2 (right to left -- reversed flow):**
4. `CLARIFIER` -- emerald border. Description: `Gravity separation. Clear water rises; sludge settles.`
5. `FILTER PRESS` -- amber border. Description: `Dewater sludge for disposal. Filtrate returns to system.`
6. `FINAL pH CHECK` -- emerald border. Description: `Verify pH 6.0-9.0 before release.`
7. `DISCHARGE` -- emerald fill at 20%, emerald border. Description: `To POTW or direct discharge per permit.`

**Sludge output:** Arrow pointing down from Filter Press. Label: `SLUDGE TO HAZARDOUS WASTE DISPOSAL` in coral.

Flow arrows: silver (`#C8D0D8`), 2px stroke.

### Step 5 -- Stage Chemistry Note Cards

Three compact glass cards below the flow diagram:

| Card | Accent | Title | Content |
|---|---|---|---|
| 1 | `#E8A020` | `pH ADJUSTMENT` | `NaOH or Ca(OH)2. Caustic = cleaner sludge, higher cost. Lime = cheaper, more sludge.` |
| 2 | `#2EC4B6` | `FLOCCULATION` | `Anionic polymer 1-5 mg/L. Overdosing breaks floc. Gentle mixing.` |
| 3 | `#27AE60` | `CLARIFICATION` | `30-60 min retention. Lamellar plates reduce footprint. Turbidity <25 NTU target.` |

---

## Phase 4 -- The pH Sweet Spot (Zone 3)

Y: ~700px to ~930px. Section label: `THE pH SWEET SPOT -- WHERE METALS FALL OUT OF SOLUTION`.

### Step 6 -- pH Precipitation Scale

A horizontal bar representing pH 6.0 to 11.0 (`#252B3D` fill). Colored horizontal zone bars stacked above showing each metal's precipitation range:

| Metal | Color | pH Range | Optimal |
|---|---|---|---|
| Cr3+ | `#2EC4B6` | 7.5-8.5 | 8.0 |
| Cu2+ | `#E8A020` | 8.0-10.0 | 8.5 |
| Zn2+ | `#C8D0D8` | 8.0-9.5 | 9.0 |
| Ni2+ | `#27AE60` | 9.0-10.5 | 9.5 |
| Cd2+ | `#E05C5C` | 9.0-11.0 | 10.0 |
| Fe2+/3+ | `#E8A020` at 60% | 7.0-9.0 | 8.0 |

Each bar at 25% opacity of its color. Optimal pH marked with a vertical line/dot at full color. pH labels along the bottom in JetBrains Mono.

### Step 7 -- Mixed Metals Callout

Amber-tinted callout strip below the pH chart. JetBrains Mono, amber text:
`Mixed metals bath? Target pH 8.5-9.5 for best overall precipitation -- but zinc re-dissolves above pH 10 (amphoteric behavior). Chromium (III) also re-dissolves above ~pH 9.5 as chromite -- raising pH for nickel can re-dissolve already-precipitated chrome.`

---

## Phase 5 -- Special Waste Streams (Zone 4)

Y: ~930px to ~1250px. Section label: `SPECIAL WASTE STREAMS -- TREAT SEPARATELY BEFORE MIXING`.

### Step 8 -- Cyanide Destruction (left half)

Coral-bordered glass card.
Title: `ALKALINE CHLORINATION -- CYANIDE DESTRUCTION` in coral.

**Stage 1** (coral badge):
- `CN- + OCl- -> CNO- + Cl-`
- pH > 10 (CRITICAL -- do not let pH drop during Stage 1)
- ORP target: +350 to +400 mV
- Contact time: 15-30 minutes minimum

**Stage 2** (coral badge):
- `2CNO- + 3OCl- -> 2CO2 + N2 + 3Cl-`
- LOWER pH to 8.0-8.5 (Stage 2 does NOT work above pH 10)
- ORP target: +600 mV
- Contact time: 30-60 minutes

Warning callout (coral): `NEVER mix cyanide waste with acid waste -- generates HCN gas (lethal)`

### Step 9 -- Chrome Reduction (right half)

Amber-bordered glass card.
Title: `CHROME REDUCTION -- Cr6+ TO Cr3+` in amber.

- Step 1: Lower pH to 2.0-3.0 with H2SO4
- Step 2: Add sodium metabisulfite. ORP target: +250 to +300 mV
- Step 3: Contact time: 20-30 minutes
- Step 4: Verify complete reduction (diphenylcarbazide spot test -- no purple = complete)
- Step 5: Raise pH to 8.0-8.5 for Cr(OH)3 precipitation

Simplified reaction: `Cr6+ reduced to Cr3+ by sodium metabisulfite under acidic conditions`
Key ratio (JetBrains Mono, amber): `2.5-3.0 lbs sodium metabisulfite per lb of Cr6+ (theoretical ~2.8 lbs; add 10-20% excess)`

---

## Phase 6 -- Discharge Compliance (Zone 5)

Y: ~1250px to ~1430px. Section label: `DISCHARGE COMPLIANCE -- KNOW YOUR PERMIT`.

**CRITICAL: NO specific mg/L discharge limit values anywhere in this zone. No EPA 40 CFR Part 433 numbers. Direct to permit.**

### Step 10 -- Jurisdictional Disclaimer Panel (left, wider)

Amber-bordered glass card.
Title: `DISCHARGE LIMITS VARY -- DO NOT RELY ON A POSTER FOR COMPLIANCE` in amber.

Body text:
- Federal: EPA categorical pretreatment standards set minimum national thresholds
- State: State environmental agencies may impose stricter requirements
- Local POTW: Your Publicly Owned Treatment Works sets the permit limits you actually operate under -- and these are often tighter than federal standards
- Limits change over time as regulations are updated
- The values in your facility's individual discharge permit are the only numbers that matter legally. Always operate to permit -- not to any published reference, table, or poster.

### Step 11 -- Where to Find Your Limits (right, narrower)

Coral-bordered glass card.
Title: `WHERE TO FIND YOUR LIMITS` in coral.

Numbered list:
1. Your discharge permit -- issued by your POTW or state agency. Keep a copy in the treatment room.
2. Your state environmental agency -- publishes current categorical standards
3. Your POTW's industrial pretreatment coordinator -- call them directly
4. Your environmental consultant or attorney -- for compliance questions

Bottom: `If you don't have a current copy of your permit on the wall -- get one today.`

---

## Phase 7 -- Operator Best Practices (Zone 6)

Y: ~1430px to ~1620px. Two-column layout.

### Step 12 -- Daily Operator Checklist (left)

Emerald-bordered glass card.
Title: `DAILY OPERATOR CHECKLIST` in emerald.

8 bullets:
1. Check and record influent pH before treatment begins
2. Verify chemical feed systems are functioning (pumps, lines, tanks)
3. Test effluent pH -- must be 6.0-9.0 before discharge
4. Check clarifier for sludge blanket level -- pump sludge before overflow
5. Sample and test effluent for metals per permit schedule
6. Record all chemical additions, pH readings, and flow rates
7. Inspect filter press -- dewater when press is full; weigh and log sludge
8. Report any spill, upset, or unusual discharge IMMEDIATELY

### Step 13 -- Common Mistakes (right)

Coral-bordered glass card.
Title: `THE MISTAKES THAT CAUSE VIOLATIONS` in coral.

7 bullets:
1. Treating all waste streams in one batch without segregating cyanide and chrome
2. Not adjusting pH before polymer addition (floc won't form at wrong pH)
3. Overdosing polymer (breaks floc -- effluent goes cloudy)
4. Discharging without final pH check (most common violation)
5. Poor recordkeeping -- if you didn't write it down, it didn't happen
6. Running out of treatment chemicals on Friday and "catching up" Monday
7. Ignoring chelated metals -- EDTA and NTA chelators prevent precipitation at normal pH

Key callout (JetBrains Mono, coral):
`The EPA does not accept "the treatment system was down" as an excuse for non-compliant discharge.`

---

## Phase 8 -- Footer (Zone 7)

Standard series footer. Dark navy glass, full-bleed.

**Disclaimer:** `This poster is an educational reference tool covering treatment process fundamentals. No specific discharge limits are shown -- discharge limits vary by jurisdiction, are set by your individual discharge permit, and change over time. Always operate in accordance with your facility's specific discharge permit and applicable federal, state, and local regulations. Consult your environmental engineer and local regulatory authority for application-specific requirements.`

**Brand line:** `Wastewater Treatment Fundamentals -- From Rinse Tank to Discharge`

**Meta:** `v1.0 -- 2026 | Poster #27 -- Wastewater Treatment Fundamentals | Plating Posters Inc`

---

## Phase 9 -- Review Checklist

- [ ] Headline `WASTEWATER TREATMENT FUNDAMENTALS` large, warm white
- [ ] Subheading in teal
- [ ] Full-width coral compliance callout banner
- [ ] 7-stage process flow diagram (two rows, L/U shape) with descriptions
- [ ] Sludge output arrow in coral from filter press
- [ ] Three stage chemistry note cards (pH Adjustment, Flocculation, Clarification)
- [ ] pH precipitation scale bar (6 metals, optimal markers)
- [ ] Mixed metals / amphoteric behavior callout in amber
- [ ] Cyanide destruction two-stage procedure (coral card)
- [ ] Chrome reduction 5-step procedure (amber card)
- [ ] HCN warning callout
- [ ] Metabisulfite ratio in JetBrains Mono
- [ ] Discharge compliance section with NO mg/L values
- [ ] Jurisdictional disclaimer panel (amber)
- [ ] Where to find your limits panel (coral)
- [ ] 8-bullet daily operator checklist (emerald)
- [ ] 7-bullet common mistakes (coral)
- [ ] EPA excuse callout in JetBrains Mono
- [ ] Footer with disclaimer, brand, meta
- [ ] Light edition remap functional via tweaks panel
- [ ] Print CSS correct (@page 12.5in x 18.75in)
- [ ] No `color-mix()` used anywhere

---

## Phase 10 -- Light Remap & Export

Standard remap via `body[data-edition="light"]`:

| Dark | Light | Element |
|------|-------|---------|
| `#1A1F2E` | `#F5F4F0` | Background |
| `#F0EDE8` | `#1A1F2E` | Primary text |
| `#1E2435` | `#ECEEF4` | Card fills |
| `#252B3D` | `#E8E8F0` | Alt rows / pH bar |
| `#0D1020` | `#1A1F2E` | Footer |
| `#E8A020` | `#C8860A` | Amber |
| `#2EC4B6` | `#1A8C82` | Teal |
| `#27AE60` | `#1E7A47` | Emerald |
| `#E05C5C` | `#B83E3E` | Coral |
| `#3A4055` | `#D0D4DE` | Headers/dividers |
| `#C8D0D8` | `#C8D0D8` | Silver (unchanged) |

Six export files: `Wastewater Treatment Fundamentals -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-25 | Initial. |
