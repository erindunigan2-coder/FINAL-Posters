---
Project: Plating Posters Inc
Poster Number: 611
Title: "Q-P-Q Oxidizing Quench -- Ferritic Nitrocarburizing"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 6: FNC / Q-P-Q, Section 6.7)"
Technical Source: Q-P-Q oxidizing quench -- NOT a hardening quench but an oxidizing immersion in NaNO3/NaNO2 salt at 700-800 F. Creates magnetite (Fe3O4) that seals compound zone pores. Polish step between Q1 and Q2. Corrosion resistance: 200-500 hours neutral salt spray on low-carbon steel (ASTM B117). Per AMS 2755.
Process Scope: Q-P-Q oxidizing quench, polish, and second quench (Stages 4, 6, and 7 of 9)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - FerriticNitrocarburizing
  - FNC
  - Q-P-Q
  - OxidizingQuench
  - ConstructionWorkup
  - DiffusionHT
---

# Poster #611 -- Construction Workup
## Q-P-Q Oxidizing Quench -- Ferritic Nitrocarburizing

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This poster covers the "Q-P-Q" in Q-P-Q -- the Quench-Polish-Quench sequence that transforms FNC from a hardness treatment into a corrosion powerhouse. The "quench" is NOT a hardening quench -- no martensite forms. It's an immersion in oxidizing salt that creates a magnetite (Fe3O4) layer, sealing the porous compound zone. The polish step smooths the surface and exposes fresh compound zone for the second oxidizing treatment. The result: 200-500 hours of salt spray resistance on low-carbon steel -- an order of magnitude better than hard chrome plate.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Q-P-Q three-step hero (Block B):** Visual showing the three Q-P-Q steps and what each accomplishes.
2. **Corrosion resistance comparison (Block D):** Q-P-Q vs. hard chrome vs. FNC-only vs. untreated.
3. **Polish specification panel (Block E):** Ra targets, methods, and why polish quality matters.
4. **The magnetite mechanism callout (Block F):** How Fe3O4 seals the compound zone pores.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stages 4, 6, and 7 highlighted
ZONE 3 -- Q-P-Q THREE-STEP HERO (4.2"--15.5" / ~11.3")
  Block B: Q1 -> Polish -> Q2 with annotations
ZONE 4 -- CORROSION RESISTANCE COMPARISON (15.5"--22.0" / ~6.5")
  Block D: Salt spray comparison table
ZONE 5 -- POLISH + MAGNETITE MECHANISM (22.0"--32.5" / ~10.5")
  Block E: Polish specs (left)
  Block F: Magnetite mechanism (right)
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `Q-P-Q OXIDIZING QUENCH` -- 80 pt `#F0EDE8`.
**Subheading:** `Quench -- Polish -- Quench: The Corrosion Resistance Sequence` -- 30 pt `#E8A020` (Amber).
**Tagline:** `This is NOT a hardening quench. No martensite. No phase change. The Q-P-Q "quench" is an oxidizing immersion that creates a magnetite seal over the compound zone -- and it is the reason FNC/Q-P-Q outperforms hard chrome in salt spray testing.` -- 20 pt `#F0EDE8` at 65%.

**Rule card (right):**
- Big number: `200-500` -- 60 pt `#27AE60`
- Label: `hours ASTM B117 salt spray on Q-P-Q-treated 1018 steel` -- 14 pt `#F0EDE8`

---

### ZONE 2 -- Orientation Strip

Stages 4, 6, 7 highlighted in Amber. Others dimmed.
Below: `Before: Compound zone formed (porous)  -->  After: Compound zone sealed with magnetite, polished, re-sealed`

---

### ZONE 3 -- Q-P-Q Three-Step Hero

**Section label:** `THE Q-P-Q SEQUENCE -- THREE STEPS TO EXCEPTIONAL CORROSION RESISTANCE` -- Y: 4.4". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK B -- Three large step cards (Y: 5.0" to 14.5")**

| Card | X | W | Step | Accent |
|---|---|---|---|---|
| Q1 | 0.5" | 7.33" | FIRST OXIDIZING QUENCH | `#E8A020` |
| P | 8.17" | 7.33" | POLISH | `#2EC4B6` |
| Q2 | 15.83" | 7.67" | SECOND OXIDIZING QUENCH | `#E8A020` |

Each: Rounded rect H: 9.0", fill `#1E2435`, top accent 4 pt.
Arrows between cards: 3 pt `#3A4055`.

*Card Q1 -- First Oxidizing Quench:*
- Badge: `Q1` Barlow SemiBold 24 pt `#E8A020`
- Title: `FIRST OXIDIZING QUENCH` Barlow SemiBold 18 pt `#E8A020`
- Parameters:
```
Bath: NaNO3 / NaNO2 (oxidizing salt)
Temperature: 700--800 F (371--427 C)
Time: 15--30 minutes
```
JetBrains Mono 13 pt.

- What happens:
```
1. Part transferred directly from
   FNC salt bath (1075 F) into
   oxidizing salt (700--800 F)

2. Oxidizing salt reacts with the
   porous epsilon compound zone

3. Iron in the compound zone oxidizes
   to MAGNETITE (Fe3O4) -- a hard,
   adherent, black oxide

4. Magnetite fills the pores of the
   compound zone, creating a SEALED
   surface layer

5. Result: dramatic improvement in
   corrosion resistance

APPEARANCE AFTER Q1:
Black, slightly rough surface
(compound zone texture + oxide)
```
Inter Regular 13 pt `#F0EDE8`.

*Card P -- Polish:*
- Badge: `P` Barlow SemiBold 24 pt `#2EC4B6`
- Title: `POLISH` Barlow SemiBold 18 pt `#2EC4B6`
- Parameters:
```
Method: Buffing, lapping, or
centerless grinding
Target: Ra 8--16 micro-inch
Temperature: Ambient
```

- What happens:
```
1. Mechanical polishing smooths
   the post-Q1 surface

2. Removes the outermost rough
   oxide layer

3. EXPOSES fresh compound zone
   surface below the initial oxide

4. This fresh surface will receive
   the SECOND oxidizing treatment (Q2)
   for enhanced protection

5. Polish quality directly affects
   final corrosion performance --
   poor polish = poor Q2 adhesion

CRITICAL:
Polish removes material -- but only
the outermost surface. The compound
zone must remain intact. Do NOT
grind through the compound zone.
```

*Card Q2 -- Second Oxidizing Quench:*
- Badge: `Q2` Barlow SemiBold 24 pt `#E8A020`
- Title: `SECOND OXIDIZING QUENCH` Barlow SemiBold 18 pt `#E8A020`
- Parameters:
```
Bath: SAME oxidizing salt as Q1
Temperature: 700--800 F (371--427 C)
Time: 15--30 minutes
```

- What happens:
```
1. Polished part re-immersed in
   oxidizing salt bath

2. Fresh compound zone surface
   (exposed by polish) receives
   a new magnetite layer

3. This second oxide layer is formed
   on a smooth, clean surface =
   BETTER adhesion and coverage

4. Combined Q1 + Polish + Q2 produces
   a multi-layer corrosion barrier:
   - Oxide-sealed pores (from Q1)
   - Smooth polished interface
   - Fresh oxide layer (from Q2)

FINAL APPEARANCE:
Uniform matte black finish
Professional, consistent appearance
```

---

### ZONE 4 -- Corrosion Resistance Comparison

**Section label:** `CORROSION RESISTANCE -- Q-P-Q vs. THE COMPETITION` -- Y: 15.7". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK D -- Comparison Table (Y: 16.3" to 21.8")**

| Treatment | Substrate | Salt Spray (ASTM B117) | Appearance | Hex Cr? |
|---|---|---|---|---|
| Q-P-Q (full Q-P-Q) | 1018 steel | 200--500 hours | Matte black | No |
| FNC only (no Q-P-Q) | 1018 steel | 50--100 hours (est.) | Gray | No |
| Hard chrome plate | Steel | 24--96 hours (typical) | Bright metallic | YES (Cr6+) |
| Black oxide | Steel | 1--4 hours | Black | No |
| Zinc plate (clear) | Steel | 8--24 hours | Silver | No |
| Untreated 1018 | -- | 2--8 hours | Bare steel | N/A |

Table: Header `#3A4055`, alternating rows. Q-P-Q row highlighted with left border `#27AE60`.

Below table:
- `Q-P-Q outperforms hard chrome by 2--10x in salt spray testing AND eliminates hexavalent chromium exposure.` Inter Medium 16 pt `#27AE60`
- `This is why Q-P-Q is positioned as a hard chrome REPLACEMENT for hydraulic cylinders, gun barrels, and shafts.` Inter Regular 13 pt `#F0EDE8` at 70%

---

### ZONE 5 -- Polish + Magnetite Mechanism

**BLOCK E -- Polish Specification (X: 0.5", W: 11.0", Y: 22.2" to 32.3")**

Rounded rect fill `#1E2435`, left accent `#2EC4B6`.

Title: `POLISH SPECIFICATION AND METHODS` Barlow SemiBold 18 pt `#2EC4B6`

Content:
```
TARGET SURFACE FINISH:
Ra 8--16 micro-inch (0.2--0.4 um)

METHODS:
- Mechanical buffing (most common)
- Centerless grinding (cylindrical parts)
- Lapping (flat surfaces)
- Vibratory finishing (small parts)

CRITICAL RULES:
1. Do NOT remove the compound zone
   Polish removes only the outermost
   oxide + roughness -- the epsilon
   layer must remain intact

2. Polish quality = corrosion quality
   A rough polish leaves pits and
   scratches that the Q2 oxide cannot
   fully seal

3. Verify Ra with profilometer
   Visual inspection alone is not
   sufficient for quality-critical parts

4. Clean after polish -- remove
   polishing compound residue before
   Q2 immersion

COMMON MISTAKES:
- Over-polishing (grinding through
  the compound zone)
- Under-polishing (rough surface
  reduces Q2 effectiveness)
- Contamination from polishing media
  carried into Q2 bath
```

**BLOCK F -- Magnetite Mechanism (X: 12.0", W: 11.5", Y: 22.2" to 32.3")**

Rounded rect fill `#1E2435`, left accent `#E8A020`.

Title: `THE MAGNETITE MECHANISM -- HOW OXIDE CREATES CORROSION RESISTANCE` Barlow SemiBold 18 pt `#E8A020`

Content:
```
THE COMPOUND ZONE IS POROUS:
Epsilon iron nitride (Fe2-3N) formed
during FNC contains micro-pores.
These pores are a weakness --
corrosive media can penetrate
through pores to the base metal.

THE OXIDIZING QUENCH SOLUTION:
NaNO3/NaNO2 salt at 700--800 F
oxidizes the iron in the pore walls,
forming MAGNETITE (Fe3O4).

Magnetite is:
- Hard (580--630 HV)
- Adherent (bonds chemically)
- Black (gives Q-P-Q its appearance)
- Corrosion-resistant (stable oxide)
- Space-filling (plugs the pores)

THE RESULT:
A compound zone that is no longer
porous but sealed -- the magnetite
acts as a gasket, preventing
corrosive media from reaching
the substrate.

WHY TWO QUENCHES?
Q1 fills the initial pores.
Polish exposes fresh surface.
Q2 seals the polished surface.
Two layers > one layer.

WHY Q-P-Q BEATS HARD CHROME:
Chrome plate is subject to
micro-cracking under stress.
Cracks allow corrosion attack.
Q-P-Q has no cracks -- the oxide-
sealed compound zone is continuous.
```

---

### ZONE 6 -- Footer

Standard. Title: `Q-P-Q Oxidizing Quench -- Ferritic Nitrocarburizing`. Version `v1.0 -- 2026`.

Disclaimer: `Source: AMS 2755, ASTM B117. Salt spray values are typical for Q-P-Q-treated low-carbon steel. Actual corrosion resistance varies by substrate, bath condition, polish quality, and test conditions. Q-P-Q corrosion resistance of 200-500 hours reflects the Watson-verified range for this treatment.`

---

## Parts 5--7

**Grouping:** 6 zones. **Light Remap:** Standard table. **Export:** Six files.

---

## Design Notes

The three-step hero (Q1 -> P -> Q2) is the visual structure that makes Q-P-Q intuitive. Each card tells the story of what happens at that stage AND why it matters. The corrosion comparison table is the commercial argument -- showing Q-P-Q at 200-500 hours alongside hard chrome at 24-96 hours is the data point that sells this process. The magnetite mechanism panel connects the metallurgy to the performance in plain language -- "the oxide plugs the pores" is a mental model that any operator can carry.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #611 -- Construction Workup v1.0*
*2026-04-26*
