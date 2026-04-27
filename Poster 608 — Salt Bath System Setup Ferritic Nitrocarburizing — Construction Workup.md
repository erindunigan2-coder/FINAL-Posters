---
Project: Plating Posters Inc
Poster Number: 608
Title: "Salt Bath / System Setup -- Ferritic Nitrocarburizing (FNC / QPQ)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 6: FNC / QPQ, Section 6.5)"
Technical Source: Salt bath types and compositions -- nitrocarburizing bath (NaCNO/KCNO + carbonate, 1050-1125 F), oxidizing quench bath (NaNO3/NaNO2, 700-800 F), gas FNC alternative (NH3 + CO2), salt bath maintenance (cyanate analysis, cyanide monitoring, sludge removal). Per AMS 2753 and AMS 2755.
Process Scope: Ferritic nitrocarburizing salt bath and system setup (Stage 3 setup)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - FerriticNitrocarburizing
  - FNC
  - QPQ
  - SaltBath
  - SystemSetup
  - ConstructionWorkup
  - DiffusionHT
---

# Poster #608 -- Construction Workup
## Salt Bath / System Setup -- Ferritic Nitrocarburizing (FNC / QPQ)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

The equipment poster for the FNC cluster. A full QPQ installation requires at minimum two salt baths (nitrocarburizing + oxidizing quench), a preheat oven, rinse tanks, and a polishing station. This poster covers the salt bath compositions, the gas FNC alternative, and the critical bath maintenance procedures that keep the process running correctly. The cyanate analysis and cyanide monitoring sections are especially important for regulatory compliance.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Two salt bath cards (Block B -- HERO):** Nitrocarburizing bath and oxidizing quench bath -- compositions, temperatures, and functions.
2. **Gas FNC alternative panel (Block D):** NH3 + CO2 atmosphere approach vs. salt bath.
3. **Bath maintenance procedures (Block E):** Cyanate analysis, cyanide monitoring, sludge removal.
4. **Equipment layout strip (Block F):** Typical QPQ line arrangement.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  System setup context highlighted
ZONE 3 -- SALT BATH SPECIFICATIONS HERO (4.2"--14.5" / ~10.3")
  Block B: Two salt bath cards
ZONE 4 -- GAS FNC ALTERNATIVE (14.5"--22.0" / ~7.5")
  Block D: Gas vs. salt bath comparison
ZONE 5 -- BATH MAINTENANCE (22.0"--28.5" / ~6.5")
  Block E: Maintenance procedures
ZONE 6 -- EQUIPMENT LAYOUT (28.5"--32.5" / ~4.0")
  Block F: Typical QPQ line strip
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `SALT BATH / SYSTEM SETUP` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Ferritic Nitrocarburizing (FNC / QPQ) -- Equipment and Bath Chemistry` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Two molten salt baths, a preheat oven, rinse tanks, and a polishing station. The QPQ line is a multi-station operation where bath chemistry is everything -- cyanate content controls the case, and the oxidizing bath creates the corrosion barrier.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

System setup highlighted: fill `#E8A020`, text `#1A1F2E`.
Below: `Equipment setup for the complete QPQ cycle -- from preheat through final rinse`

---

### ZONE 3 -- Salt Bath Specifications (HERO)

**Section label:** `TWO BATHS, TWO FUNCTIONS -- THE CHEMISTRY OF QPQ` -- Y: 4.4". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK B -- Two Salt Bath Cards (Y: 5.0" to 14.0")**

*Card 1 -- Nitrocarburizing Bath (X: 0.5", W: 11.0", H: 8.5"):*
- Rounded rect fill `#1E2435`, left accent `#27AE60`.
- Title: `NITROCARBURIZING SALT BATH` Barlow SemiBold 20 pt `#27AE60`
- Stat: `THE CORE PROCESS` JetBrains Mono 14 pt `#27AE60`

Content:
```
COMPOSITION:
Alkali cyanate (NaCNO / KCNO)
+ alkali carbonate (Na2CO3 / K2CO3)
Target cyanate content: 35--40% CNO

TEMPERATURE:
1050--1125 F (566--607 C)
Most common: 1075 F (580 C)

FUNCTION:
Cyanate decomposes at the steel surface,
releasing nitrogen AND carbon atoms that
diffuse into the ferrite matrix.

Produces:
- Epsilon iron nitride (Fe2-3N)
  compound zone (0.0004--0.001")
- Nitrogen-enriched diffusion zone
  (0.005--0.025")

IMMERSION TIME:
60--120 minutes (standard)
Up to 240 minutes for deeper case

HEATING:
External electric resistance heaters
or immersed electrodes (depending on
bath size and manufacturer)
```

*Card 2 -- Oxidizing Quench Bath (X: 12.0", W: 11.5", H: 8.5"):*
- Rounded rect fill `#1E2435`, left accent `#E8A020`.
- Title: `OXIDIZING SALT QUENCH BATH` Barlow SemiBold 20 pt `#E8A020`
- Stat: `THE CORROSION BARRIER` JetBrains Mono 14 pt `#E8A020`

Content:
```
COMPOSITION:
Alkali nitrate / nitrite
(NaNO3 / NaNO2)

TEMPERATURE:
700--800 F (371--427 C)

FUNCTION:
Oxidizing salt creates a magnetite
(Fe3O4) layer that fills and seals
the porous compound zone.

This oxide layer is the key to
QPQ corrosion resistance. Without it,
the compound zone alone provides only
moderate corrosion protection.

WITH oxidizing quench (QPQ):
200--500 hours neutral salt spray

WITHOUT oxidizing quench (FNC only):
50--100 hours (estimate, varies)

IMMERSION TIME:
15--30 minutes per quench
(Q1 and Q2 use the SAME bath)

NOTE:
The "quench" is NOT a hardening quench.
No martensite forms. The microstructure
remains ferritic. The term "quench"
refers only to the rapid transfer
and immersion in the lower-temperature
oxidizing bath.
```

---

### ZONE 4 -- Gas FNC Alternative

**Section label:** `GAS FNC -- THE SALT-FREE ALTERNATIVE` -- Y: 14.7". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK D -- Two-column comparison (Y: 15.3" to 21.8")**

*Left -- Gas FNC (X: 0.5", W: 11.0"):*

Rounded rect fill `#1E2435`, left accent `#2EC4B6`.

Title: `GAS FNC (MELONITE / ARCOR)` Barlow SemiBold 18 pt `#2EC4B6`

Content:
```
ATMOSPHERE:
NH3 + CO2 (or endothermic gas + NH3)

TEMPERATURE:
1050--1100 F (566--593 C)

TIME:
60--180 minutes

ADVANTAGES:
+ No molten salt handling
+ No cyanate/cyanide waste stream
+ Cleaner working environment
+ Lower regulatory burden
+ Easier to automate

LIMITATIONS:
- Cannot produce the QPQ oxidizing
  quench in a gas process
- Corrosion resistance without the
  oxidizing quench step is LOWER
  than full QPQ
- Separate oxidizing step can be
  added (steam treatment or liquid)
  but does not match salt QPQ
```

*Right -- Salt Bath FNC (X: 12.0", W: 11.5"):*

Rounded rect fill `#1E2435`, left accent `#E8A020`.

Title: `SALT BATH FNC (TUFFTRIDE / TENIFER)` Barlow SemiBold 18 pt `#E8A020`

Content:
```
ADVANTAGES:
+ Full QPQ cycle available
  (highest corrosion performance)
+ Uniform heat transfer (liquid)
+ Well-established for firearms,
  automotive, and hydraulics
+ Thick compound zone readily achieved

LIMITATIONS:
- Molten salt handling (safety)
- Cyanate salt = regulated waste
- Cyanide byproduct monitoring
- Higher operating cost
- Bath maintenance intensive
- Splash and fume hazards

BOTTOM LINE:
If you need maximum QPQ corrosion
resistance (200--500 hr salt spray),
salt bath is the proven path.
If you need FNC without the salt
hazards, gas FNC is the cleaner option.
```

---

### ZONE 5 -- Bath Maintenance

**Section label:** `BATH MAINTENANCE -- KEEPING THE CHEMISTRY RIGHT` -- Y: 22.2". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK E -- Three maintenance cards (Y: 22.9" to 28.3")**

| Card | X | W | Title | Accent |
|---|---|---|---|---|
| 1 | 0.5" | 7.33" | CYANATE ANALYSIS | `#27AE60` |
| 2 | 8.17" | 7.33" | CYANIDE MONITORING | `#E05C5C` |
| 3 | 15.83" | 7.67" | SLUDGE & DRAGOUT | `#E8A020` |

Each: Rounded rect H: 5.0", fill `#1E2435`, left accent 0.06".

*Card 1 -- Cyanate Analysis:*
- Title: `CYANATE (CNO) ANALYSIS` Barlow SemiBold 18 pt `#27AE60`
- Content:
```
TARGET: 35--40% CNO in primary bath
Frequency: Every shift or per load

METHOD:
Titration (wet chemistry) -- standard
analytical method for cyanate

WHY IT MATTERS:
Cyanate is the active nitrogen/carbon
source. Low cyanate = thin compound
zone = poor hardness and wear
resistance. High cyanate = faster
treatment but may affect bath life.

ACTION:
Replenish salt as cyanate depletes.
Follow bath supplier's regeneration
schedule and replenishment tables.
```

*Card 2 -- Cyanide Monitoring:*
- Title: `CYANIDE (CN) MONITORING` Barlow SemiBold 18 pt `#E05C5C`
- Content:
```
CYANIDE IS A BYPRODUCT:
Bath regeneration and normal operation
produce CN- (cyanide) from CNO-
(cyanate) decomposition.

REGULATORY REQUIREMENT:
Cyanide content must be monitored
and kept below regulatory limits.
Bath regeneration cycle required
when CN exceeds limits.

WASTE DISPOSAL:
Spent salt containing cyanide is
HAZARDOUS WASTE in most jurisdictions.
Proper manifesting, transport, and
disposal required.

NEVER dump salt down a drain.
```

*Card 3 -- Sludge & Dragout:*
- Title: `SLUDGE & DRAGOUT MANAGEMENT` Barlow SemiBold 18 pt `#E8A020`
- Content:
```
SLUDGE:
Iron fines, scale, and oxide debris
accumulate at the bath bottom.
Periodic removal required (ladle or
pump during off-hours).

DRAGOUT:
Salt carried out on parts and fixtures
depletes the bath volume.
Track dragout volume and replenish.

CROSS-CONTAMINATION:
Nitrocarburizing salt dragged into
oxidizing bath (or vice versa) degrades
both baths. Adequate drip time between
transfers. Rinse tank between baths
for critical applications.
```

---

### ZONE 6 -- Equipment Layout

**Section label:** `TYPICAL QPQ LINE LAYOUT` -- Y: 28.7". Barlow Condensed ExtraBold 24 pt `#F0EDE8`.

**BLOCK F -- Five-station strip (Y: 29.4" to 32.3")**

Five stations left to right:

| Station | Label | Accent |
|---|---|---|
| 1 | PREHEAT OVEN (600--700 F) | `#E8A020` |
| 2 | FNC SALT BATH (1050--1075 F) | `#27AE60` |
| 3 | OXIDIZING QUENCH (700--800 F) | `#E8A020` |
| 4 | RINSE TANK (Hot Water) | `#2EC4B6` |
| 5 | POLISH STATION + Q2 RETURN | `#2EC4B6` |

Each: Rounded rect W: 4.4", H: 2.7", fill `#1E2435`, top accent 4 pt.
Arrows between stations: 3 pt `#3A4055`.

Below: `Parts flow left to right. Polish station feeds back to oxidizing quench for Q2. Final rinse after Q2 completes the cycle.` Inter Regular 12 pt `#F0EDE8` at 70%.

---

### ZONE 7 -- Footer

Standard. Title: `Salt Bath / System Setup -- Ferritic Nitrocarburizing (FNC / QPQ)`. Version `v1.0 -- 2026`.

Disclaimer: `Source: AMS 2753, AMS 2755. Salt compositions and maintenance schedules vary by bath supplier (Durferrit, Kolene, etc.). Consult your salt supplier for specific composition targets, replenishment rates, and cyanide disposal requirements.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Salt Bath System Setup Ferritic Nitrocarburizing -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The two salt bath cards are the technical core -- operators need to understand that the nitrocarburizing bath and the oxidizing quench bath are fundamentally different chemistries with different functions. The gas FNC comparison (Zone 4) is commercially important -- many shops are evaluating whether they can get QPQ-equivalent results without molten salt, and the honest answer is "not quite, but close for some applications." The cyanide monitoring card is the regulatory reality check.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #608 -- Construction Workup v1.0*
*2026-04-26*
