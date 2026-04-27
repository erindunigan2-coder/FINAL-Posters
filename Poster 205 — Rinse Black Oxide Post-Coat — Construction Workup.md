---
Project: Plating Posters Inc
Poster Number: 205
Title: "Rinse -- Black Oxide -- Post-Coat"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Process Scope: Post-oxide rinse stages (cold + hot) for hot alkaline black oxide on steel (Stages 6--7 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - BlackOxide
  - Rinse
  - ConstructionWorkup
  - Series2
  - ClusterCC07
---

# Poster #205 -- Construction Workup
## Rinse -- Black Oxide -- Post-Coat

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stages 6 and 7 of 8. Black oxide uses a two-stage rinse after the conversion bath: cold rinse first (removes bulk caustic), then hot rinse (further cleans and preheats parts for the oil dip). This poster covers both stages because they work as a pair. The optional chromate dip in the hot rinse is noted but flagged for Cr(VI) regulatory concerns.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Two-tank hero (Block B):** Cold rinse tank and hot rinse tank side by side with arrow connecting them.
2. **Thermal shock advisory (Block D):** 285 F parts into cold water.
3. **Optional chromate dip (Block E):** Benefits vs. regulatory burden.
4. **Transition to oil seal (Block F):** Why hot rinse preheats parts for the oil stage.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stages 6+7 highlighted (Teal)
ZONE 3 -- TWO-TANK RINSE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- THERMAL SHOCK + VENTILATION (14.5"--20.5" / ~6.0")
ZONE 5 -- OPTIONAL CHROMATE DIP (20.5"--26.5" / ~6.0")
ZONE 6 -- TRANSITION TO OIL SEAL (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Black Oxide -- Post-Coat Rinse -- Stages 6 & 7 of 8` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Cold rinse strips the caustic. Hot rinse preheats for oil. Two stages, one goal: get the parts clean and ready to seal.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stages 6 and 7 highlighted: both fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Fresh magnetite coating carrying hot caustic --> After: Clean, preheated black parts ready for oil seal`

---

### ZONE 3 -- Two-Tank Rinse Hero

**Section label:** `TWO-STAGE RINSE -- COLD THEN HOT` -- Y: 4.4".

**BLOCK B -- Two Tanks Side by Side**

Y: 5.0" to 14.0".

**Tank 1 -- Cold Rinse (left, X: 1.0", W: 10.0"):**
- Rounded rect, Y: 5.5", H: 7.0", fill `#252B3D`, border 3 pt `#2EC4B6`
- Label above: `STAGE 6 -- COLD RINSE` Barlow SemiBold 16 pt `#2EC4B6`
- Temperature: `Ambient` JetBrains Mono 16 pt `#F0EDE8`
- Time: `1--2 min immersion` JetBrains Mono 14 pt `#F0EDE8`
- Purpose bullets:
  - `Removes bulk caustic (600--900 g/L NaOH)` Inter Regular 13 pt `#F0EDE8`
  - `Removes dissolved salts and iron compounds` Inter Regular 13 pt `#F0EDE8`
  - `Thermal shock: 285 F parts into cold water` Inter Regular 13 pt `#F0EDE8`
- Steam cloud at surface: wavy lines, `#F0EDE8` at 20%
- Warning note: `Expect steam -- parts are ~285 F. Ventilation required.` Inter Medium 12 pt `#E8A020`

**Arrow between tanks:**
- Stroke 3 pt `#3A4055`, right-pointing, Y: 9.0"

**Tank 2 -- Hot Rinse (right, X: 13.0", W: 10.0"):**
- Rounded rect, Y: 5.5", H: 7.0", fill `#252B3D`, border 3 pt `#E8A020`
- Label above: `STAGE 7 -- HOT RINSE` Barlow SemiBold 16 pt `#E8A020`
- Temperature: `180--200 F (82--93 C)` JetBrains Mono 16 pt `#E8A020`
- Time: `1--2 min` JetBrains Mono 14 pt `#F0EDE8`
- Purpose bullets:
  - `Further removes caustic residue` Inter Regular 13 pt `#F0EDE8`
  - `Heats parts for efficient oil dip` Inter Regular 13 pt `#F0EDE8`
  - `Hot part + hot oil = best penetration into magnetite pores` Inter Regular 13 pt `#F0EDE8`
- Optional note: `Some shops add chromate to this stage (see Zone 5)` Inter Regular 12 pt `#F0EDE8` at 60%

**Bottom callout (Y: 13.5"):**
- `Cold rinse = bulk caustic removal. Hot rinse = final clean + preheat. Together they bridge the 285 F oxide bath to the oil seal.` Inter Medium 14 pt `#2EC4B6`

---

### ZONE 4 -- Thermal Shock + Ventilation

**Section label:** `THERMAL SHOCK AND VENTILATION` -- Y: 14.7".

**Two-panel layout (Y: 15.3" to 20.3"):**

**Left -- Thermal Shock (X: 0.5", W: 11.0"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E8A020`
- Title: `THERMAL SHOCK CONSIDERATIONS` Barlow SemiBold 18 pt `#E8A020`
- Content:
```
Parts emerge from black oxide at ~285 F
and go directly into ambient cold water.

Temperature drop: ~220 F (122 C) in
seconds.

Effects:
- Immediate steam generation
- Potential for warping on thin-wall parts
- Cracking risk on brittle/cast iron parts

For critical parts: consider gradual cooling
(warm rinse first, then cold) or simply
extend time in Stage 7 hot rinse.
```

**Right -- Ventilation (X: 12.0", W: 11.5"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E05C5C`
- Title: `VENTILATION REQUIREMENTS` Barlow SemiBold 18 pt `#E05C5C`
- Content:
```
Cold rinse generates a visible steam cloud
when 285 F parts are immersed.

This steam carries traces of caustic mist.

REQUIRED: Exhaust ventilation at cold
rinse tank lip (slot exhaust or canopy
hood).

PPE: Face shield, chemical gloves,
chemical apron.

Lower parts slowly into the rinse --
do not drop. Dropping splashes hot
caustic-contaminated water.
```

---

### ZONE 5 -- Optional Chromate Dip

**Section label:** `OPTIONAL: CHROMATE DIP IN HOT RINSE` -- Y: 20.7".

**Two-column comparison (Y: 21.3" to 26.3"):**

**Left -- Benefits (X: 0.5", W: 11.0"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#27AE60`
- Title: `WHY ADD CHROMATE?` Barlow SemiBold 18 pt `#27AE60`
```
Some operations add 0.5--2 oz/gal
CrO3 (chromic acid) to the hot rinse.

Benefits:
- 2--5x improvement in bare corrosion
  resistance
- Passivates any exposed iron in
  coating imperfections
- Slightly improves oil adhesion

When it makes sense:
- Military/defense specifications
- Extended storage without oiling
- Parts going into humid environments
```

**Right -- Regulatory Burden (X: 12.0", W: 11.5"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E05C5C`
- Title: `THE Cr(VI) PROBLEM` Barlow SemiBold 18 pt `#E05C5C`
```
Hexavalent chromium (Cr6+) is a known
human carcinogen.

Adding CrO3 to your rinse triggers:
- OSHA PEL: 5 ug/m3 (extremely low)
- EPA reporting requirements
- EU REACH authorization (if exporting)
- RoHS non-compliance
- Hazardous waste disposal for rinse

Most modern shops are eliminating
Cr(VI) from all stages. The corrosion
improvement often does not justify the
regulatory cost.

ALTERNATIVE: Oil seal alone provides
adequate protection for most applications.
```

---

### ZONE 6 -- Transition to Oil Seal

**Section label:** `PREPARING FOR THE OIL SEAL` -- Y: 26.7".

**Single wide callout (Y: 27.3" to 32.3"):**

Rounded rect, full width (23.0"), H: 4.8", fill `#1E2435`, left accent `#27AE60`.

**Title:** `WHY THE HOT RINSE MATTERS FOR OIL PENETRATION` Barlow SemiBold 18 pt `#27AE60`

**Content (two columns inside):**

Left:
```
The magnetite coating (Fe3O4) is
microporous -- it has millions of
tiny pores that must be filled with
oil for corrosion protection.

Hot part (180--200 F) + hot oil
(150--180 F) = best penetration.

The oil displaces water from the
pores and fills them. This is the
actual corrosion barrier.
```

Right:
```
If parts cool before oil dip:
- Water trapped in pores
- Oil sits on surface, does not
  penetrate
- Corrosion starts from within
  the coating

RULE: Parts go from hot rinse
directly into oil with NO delay.
Do not air-dry between rinse and
oil.
```

---

### ZONE 7 -- Footer

Standard. Title: `Rinse -- Black Oxide -- Post-Coat`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Black Oxide Post-Coat -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Combining Stages 6 and 7 into one poster is the right call -- they function as a pair and neither has enough individual content for a full poster. The two-tank hero visual makes the sequence unmistakable. The chromate dip section is a balanced treatment -- benefits acknowledged but regulatory burden clearly presented. The "hot part + hot oil = best penetration" explanation is the scientific underpinning that makes this poster more than just "rinse your parts." Magnetite micropore filling is the real story of black oxide corrosion protection.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #205 -- Construction Workup v1.0*
*2026-04-26*
