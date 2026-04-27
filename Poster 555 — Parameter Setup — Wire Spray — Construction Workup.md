---
Project: Plating Posters Inc
Poster Number: 555
Title: "Parameter Setup -- Wire Combustion Spray"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 8: Wire Combustion Spray)"
Technical Source: Wire combustion spray parameters -- O2 20--40 PSI, acetylene 10--15 PSI, compressed air 40--80 PSI, wire feed 1--8 m/min, flame temp ~3100 degC (oxy-acet) or ~2800 degC (oxy-propane), particle velocity 80--200 m/s, standoff 150--250 mm, deposition rate 2--8 kg/hr, deposition efficiency 50--70%.
Process Scope: Wire combustion spray parameter setup and process variable control
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ThermalSpray
  - WireCombustionSpray
  - Parameters
  - ConstructionWorkup
  - ClusterTS08
---

# Poster #555 -- Construction Workup
## Parameter Setup -- Wire Combustion Spray

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Wire combustion spray parameters are simpler than any other thermal spray process. Three gas pressures (O2, fuel, air), wire feed rate, and standoff distance. That's the core of it. The flame type (neutral, oxidizing, reducing) is set by the O2-to-fuel ratio -- neutral is the default for most materials. The "how the operator handles the gun" factors (traverse speed, spray angle, crossing pattern) matter as much as the mechanical parameters because this is a manual process.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- PARAMETER TABLE / HERO (2.9"--15.5")
  Block B: Full parameter table
  Block C: Flame type guide (neutral, oxidizing, reducing)
ZONE 3 -- WIRE MATERIAL PARAMETERS (15.5"--22.0")
  Block D: Material-specific parameter adjustments (zinc, aluminum, steel, bronze)
ZONE 4 -- MANUAL TECHNIQUE PARAMETERS (22.0"--28.5")
  Block E: Operator-controlled variables (traverse, angle, pattern)
  Block F: Preheat procedure
ZONE 5 -- PARAMETER PROBLEMS (28.5"--32.5")
  Block G: 4 parameter problem cards
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `PARAMETER SETUP` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Wire Combustion Spray -- Gas, Wire, Air & Manual Technique` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Three pressures. One wire feed rate. One standoff distance. The rest is operator skill. Wire spray parameters are simple -- but getting them right separates a good coating from a reject.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Parameter Table (HERO)

**Section label:** `WIRE COMBUSTION SPRAY OPERATING PARAMETERS` -- Y: 3.1".

**BLOCK B -- Full Parameter Table**

Y: 3.8" to 11.0". Column widths (23.0" total):
- Parameter (5.5") | Range (5.5") | Notes (12.0")

| Parameter | Range | Notes |
|---|---|---|
| Oxygen pressure | 20--40 PSI | Adjust for neutral or slightly oxidizing flame |
| Fuel pressure (acetylene) | 10--15 PSI | Neutral flame preferred; NEVER exceed 15 PSI |
| Fuel pressure (propane) | 10--20 PSI | Alternative; lower flame temp (~2800 degC) |
| Compressed air pressure | 40--80 PSI | Atomizing air; higher = finer droplets, more overspray |
| Wire feed rate | 1--8 m/min | Material and wire diameter dependent |
| Flame temperature | ~3100 degC (oxy-acet); ~2800 degC (oxy-propane) | Oxy-acetylene is standard |
| Particle velocity | 80--200 m/s | Lower end of thermal spray range; air blast dependent |
| Standoff distance | 150--250 mm (6--10 inches) | Manual control; maintain consistent |
| Spray angle | 60--90 degrees | Perpendicular preferred |
| Deposition rate | 2--8 kg/hr | Wire material and diameter dependent |
| Deposition efficiency | 50--70% | Remainder is overspray |

Data: JetBrains Mono 12 pt. Header: Barlow SemiBold 14 pt.

**BLOCK C -- Flame Type Guide**

Y: 11.5" to 15.3". Three side-by-side panels.

| Flame Type | X | W | O2/Fuel Ratio | Appearance | Use |
|---|---|---|---|---|---|
| Neutral | 0.5" | 7.33" | Balanced (1:1 volume acet) | Clear inner cone; no feather | DEFAULT -- zinc, aluminum, most materials |
| Oxidizing | 8.0" | 7.33" | Excess O2 | Short, pointed inner cone; hissing | Some bronzes; avoid for zinc |
| Reducing | 15.5" | 8.0" | Excess fuel | Long, feathery inner cone | Some specialty alloys; rarely used |

Each panel: Rounded rect, fill `#1E2435`.
- Neutral: left accent `#27AE60`. `RECOMMENDED DEFAULT` badge.
- Oxidizing: left accent `#E8A020`.
- Reducing: left accent `#2EC4B6`.

Note: `Start neutral. Adjust only if specification or wire manufacturer recommends otherwise.` Inter Medium 14 pt `#27AE60`.

---

### ZONE 3 -- Wire Material Parameters

**Section label:** `MATERIAL-SPECIFIC PARAMETER ADJUSTMENTS` -- Y: 15.7".

**BLOCK D -- Material Parameter Table**

| Wire Material | Diameter | Feed Rate | O2/Fuel | Air | Standoff | Notes |
|---|---|---|---|---|---|---|
| Zinc (99.0%+) | 1.6--3.2 mm | 2--6 m/min | Neutral | 50--70 PSI | 150--250 mm | Low melting point (420 degC); easy to spray; fume control critical |
| Aluminum (1100/99.0%) | 1.6--3.2 mm | 2--6 m/min | Neutral | 50--70 PSI | 150--250 mm | Higher melting point (660 degC); denser than zinc coating |
| Zn-Al 85/15 | 1.6--3.2 mm | 2--5 m/min | Neutral | 50--70 PSI | 150--200 mm | Best combination of cathodic protection and sealer adhesion |
| Carbon steel | 1.6--3.2 mm | 3--8 m/min | Neutral to slightly ox. | 60--80 PSI | 150--250 mm | Dimensional restoration; higher feed rate |
| Stainless steel | 1.6--3.2 mm | 3--8 m/min | Neutral | 60--80 PSI | 150--250 mm | Corrosion-resistant overlay |
| Bronze | 1.6--3.2 mm | 2--6 m/min | Slightly oxidizing | 50--70 PSI | 150--250 mm | Bearing surfaces; journal repairs |

Data: JetBrains Mono 11 pt.

Note: `Zinc and aluminum are the primary wire spray materials (>80% of all wire combustion spray volume). The rest are specialty applications.` Inter Medium 13 pt `#E8A020`.

---

### ZONE 4 -- Manual Technique Parameters

**Section label:** `OPERATOR-CONTROLLED VARIABLES` -- Y: 22.2".

**Left -- BLOCK E: Traverse & Angle (X: 0.5", W: 11.0"):**

Rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06".

Title: `MANUAL TECHNIQUE` Barlow SemiBold 20 pt `#E8A020`.

| Variable | Guidance |
|---|---|
| Traverse speed | Steady, consistent speed; 200--600 mm/s typical |
| Spray pattern | Crossing passes at 60--90 deg to each other |
| Overlap | 50% overlap between passes for uniform thickness |
| Spray angle | 75--90 deg to surface; below 45 deg causes porosity |
| Number of passes | Build to specification thickness in multiple thin passes |
| Standoff consistency | Maintain 150--250 mm -- arm distance, not wrist |

Note: `This is a manual skill. Consistent traverse speed and standoff are the hardest things to maintain. New operators should practice on scrap before production work.` Inter Medium 13 pt `#2EC4B6`.

**Right -- BLOCK F: Preheat Procedure (X: 12.0", W: 11.5"):**

Rounded rect, fill `#1E2435`, left accent `#27AE60` 0.06".

Title: `SUBSTRATE PREHEAT` Barlow SemiBold 20 pt `#27AE60`.

- `Preheat substrate to 80--120 degC using flame gun (no wire feed)`
- `Purpose: drives off moisture; improves first-pass adhesion`
- `Use temperature-indicating crayons or IR thermometer to verify`
- `Do NOT overheat -- aluminum substrates max 120--150 degC`
- `Preheat immediately before spraying -- do not allow cool-down`

Callout: `Preheat is optional for some specifications but ALWAYS improves bond quality. Make it standard practice.` JetBrains Mono 13 pt `#27AE60`.

---

### ZONE 5 -- Parameter Problems

**Section label:** `PARAMETER PROBLEMS -- 4 COMMON ISSUES` -- Y: 28.7".

**BLOCK G -- Four Problem Cards**

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | WIRE NOT MELTING FULLY | Flame too lean; wire feed too fast; wrong flame type | Enrich flame; reduce wire feed; verify neutral flame |
| 2 | 6.33" | EXCESSIVE SPATTER | Wire feed too fast for flame capacity; air too high | Reduce wire feed; balance air pressure; check for wire kinks |
| 3 | 12.16" | OXIDIZED COATING | Oxidizing flame; standoff too far; too many passes | Adjust to neutral flame; reduce standoff; use fewer, thicker passes |
| 4 | 18.0" | INCONSISTENT THICKNESS | Varying traverse speed; changing standoff | Practice consistent technique; use guide rails if available |

---

### ZONE 6 -- Footer

Standard. Title: `Parameter Setup -- Wire Combustion Spray`. Version `v1.0 -- 2026`.

Disclaimer: `Parameters shown are representative ranges for wire combustion spray. Specific values vary by wire material, diameter, gun model, and specification requirements. Consult your equipment manufacturer and applicable standards (AWS C2.18).`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Parameter Setup Wire Spray -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

*Alaina -- Poster #555 -- Construction Workup v1.0 -- 2026-04-26*
