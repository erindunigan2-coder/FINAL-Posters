---
Project: Plating Posters Inc
Poster Number: 454
Title: "Beam Setup -- Ion Implantation"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters — Watson Research Brief (Cluster 6: Ion Implantation, Sections 6.1, 6.5)"
Process Scope: Ion source startup, mass analysis, and beam establishment for ion implantation
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - IonImplantation
  - BeamSetup
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #454 -- Construction Workup
## Beam Setup -- Ion Implantation

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This poster covers the heart of the ion implanter: generating the ion beam, separating the desired species by mass, and establishing a stable, pure, calibrated beam ready for implantation. The hero visual is a beam-line architecture diagram showing the path from ion source to process chamber. The mass analyzer magnet is the critical component -- it is what makes ion implantation a precision process rather than a shotgun blast of random ions. This poster is the most "machine-focused" in the cluster.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Beam-line architecture hero (Block B):** Horizontal schematic showing ion source -> extraction -> mass analyzer -> acceleration -> scanning -> process chamber. Built with labeled rectangles and connecting arrows.
2. **Ion source types (Block D):** Freeman, Bernas, and IHC source comparison.
3. **Mass analyzer function (Block E):** How the analyzing magnet separates species.
4. **Beam quality checks (Block F):** Verification steps before implantation begins.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 15.0" / 21.0" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- BEAM-LINE ARCHITECTURE HERO (2.9"--15.0" / ~12.1")
  Block B: Full implanter beam-line schematic
ZONE 3 -- ION SOURCE TYPES (15.0"--21.0" / ~6.0")
  Block D: Source comparison table
ZONE 4 -- MASS ANALYZER FUNCTION (21.0"--27.0" / ~6.0")
  Block E: How mass separation works
ZONE 5 -- BEAM QUALITY CHECKS (27.0"--32.5" / ~5.5")
  Block F: Pre-implant verification checklist
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `BEAM SETUP` -- 88 pt `#F0EDE8`.
**Subheading:** `Ion Implantation -- Source Ignition, Mass Analysis & Beam Establishment` -- 32 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `The mass analyzer is the brain of the implanter. It selects exactly the ion species you need from a plasma soup of everything in the source. Without it, you are implanting garbage.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Beam-Line Architecture Hero

**Section label:** `INSIDE THE IMPLANTER -- FROM SOURCE TO SUBSTRATE` -- Y: 3.1".

**BLOCK B -- Beam-Line Schematic**

Y: 3.8" to 14.8".

**Full-width horizontal schematic (X: 0.5", W: 23.0"):**

Rounded rect container, H: 10.5", fill `#1E2435`.

**Seven components in sequence, left to right:**

| Component | X | W | H | Fill | Accent | Label |
|---|---|---|---|---|---|---|
| 1. Ion Source | 0.8" | 2.5" | 3.0" | `#3A4055` | `#E05C5C` | `ION SOURCE` / `Gas in -> Plasma` |
| 2. Extraction | 3.6" | 1.5" | 2.5" | `#3A4055` | `#E8A020` | `EXTRACTION` / `10--80 kV` |
| 3. Mass Analyzer | 5.4" | 4.0" | 4.0" | `#3A4055` | `#E8A020` | `ANALYZING MAGNET` / `90 deg bend` / `Mass separation` |
| 4. Resolving Slit | 9.7" | 0.5" | 2.5" | `#E8A020` | -- | `SLIT` / `Selects species` |
| 5. Acceleration | 10.5" | 2.5" | 2.5" | `#3A4055` | `#27AE60` | `ACCELERATION` / `or DECEL stage` |
| 6. Beam Scanning | 13.3" | 3.5" | 3.0" | `#3A4055` | `#2EC4B6` | `BEAM SCANNER` / `X-Y electrostatic` / `or hybrid scan` |
| 7. Process Chamber | 17.1" | 5.5" | 4.5" | `#3A4055` | `#27AE60` | `PROCESS CHAMBER` / `Wafer/part + Faraday` |

Each component: Rounded rect, fill as specified, border 1 pt accent color.
Labels: Barlow SemiBold 12 pt accent color (component name); JetBrains Mono 10 pt `#F0EDE8` (specs).

**Connecting arrows between components:**
- Stroke 3 pt `#27AE60`, arrowhead filled right.
- Label along beam path: `ION BEAM` Barlow SemiBold 14 pt `#27AE60`, centered above arrow line.

**Annotations (below main schematic, Y: 10.0" to 14.5"):**

Four annotation callout boxes:

| Callout | X | W | Content | Accent |
|---|---|---|---|---|
| Source detail | 0.8" | 5.5" | Gas feed (BF3, AsH3, PH3, N2) or solid vaporizer -> plasma chamber. Arc discharge ionizes gas. Ions extracted by high-voltage electrode. | `#E05C5C` |
| Magnet detail | 6.8" | 5.5" | Magnetic field bends ion trajectories. Lighter ions bend more; heavier ions bend less. Only the selected mass-to-charge ratio passes through the resolving slit. Example: separates B-11 from B-10, BF2+ from BF+. | `#E8A020` |
| Scan detail | 12.8" | 5.0" | Electrostatic plates deflect beam in X and Y. Scan frequency: 100--1000 Hz. Ensures uniform dose across entire wafer/part surface. Some systems use hybrid: electrostatic X-scan + mechanical Y-scan (wafer translation). | `#2EC4B6` |
| Faraday detail | 18.3" | 5.0" | Faraday cage/cup surrounds the substrate. Measures total ion current reaching the wafer. Dose = (current x time) / (charge x area). Accuracy: +/- 1--2%. This is the dose control system. | `#27AE60` |

Each: Rounded rect, H: 3.5", fill `#1E2435`, top accent 3 pt.
Content: Inter Regular, 12 pt, `#F0EDE8`.

---

### ZONE 3 -- Ion Source Types

**Section label:** `ION SOURCE TYPES` -- Y: 15.2".

**BLOCK D -- Source Comparison Table**

Y: 15.8" to 20.8".

| Source Type | Mechanism | Feed Materials | Beam Current | Best For |
|---|---|---|---|---|
| Freeman | Hot-cathode arc discharge; linear extraction slit | BF3, AsH3, PH3, N2 (gas); solid vaporizer for In, Sb | 0.1--10 mA | Medium-current implants; versatile |
| Bernas | Hot-cathode arc with reflex geometry; higher ionization efficiency | Same as Freeman | 1--30 mA | High-current implants; high-dose applications |
| IHC (Indirectly Heated Cathode) | Cathode heated indirectly; longer lifetime; higher electron density | Same + Ge, C (cluster ions) | 5--50+ mA | High-current, high-throughput production |
| RF / Microwave | Electrodeless plasma; no filament consumption | All gases | 0.01--1 mA | Low-current, high-energy implants; MeV systems |

Header: Barlow SemiBold, 13 pt, `#F0EDE8`, fill `#3A4055`.
Data: alternating `#1E2435` / `#252B3D`. Inter Regular 13 pt `#F0EDE8`. Beam current: JetBrains Mono 12 pt `#E8A020`.

---

### ZONE 4 -- Mass Analyzer Function

**Section label:** `THE ANALYZING MAGNET -- PRECISION ION SELECTION` -- Y: 21.2".

**BLOCK E -- Mass Separation Explanation**

Y: 21.8" to 26.8". Three cards in a row.

| Card | X | W | Title | Accent | Content |
|---|---|---|---|---|---|
| 1 | 0.5" | 7.33" | THE PHYSICS | `#E8A020` | A charged particle moving through a magnetic field follows a curved path. The radius of curvature depends on the particle's mass, charge, and velocity: r = mv/qB. Heavier ions curve less. Lighter ions curve more. At a fixed B field and extraction voltage, each mass follows a unique radius. |
| 2 | 8.16" | 7.33" | THE RESOLVING SLIT | `#2EC4B6` | After the magnet, only ions with the correct curvature radius pass through a narrow slit. All other species hit the slit walls and are blocked. Mass resolution: M/deltaM = 50--200 typical. This separates B-11 from B-10 (mass 11 vs. 10), and P-31 from Si-30 (mass 31 vs. 30). |
| 3 | 15.83" | 7.33" | WHY IT MATTERS | `#27AE60` | Without mass separation, a BF3 source produces B+, BF+, BF2+, F+, and BF3+ ions -- all at different masses and energies. Implanting the wrong species gives wrong depth profile, wrong dose, wrong electrical properties. The mass analyzer ensures only the intended ion reaches the substrate. |

Each card: Rounded rect, H: 4.8", fill `#1E2435`, radius 6, left accent 0.06".
Title: Barlow SemiBold, 18 pt, accent color.
Content: Inter Regular, 14 pt, `#F0EDE8`.

---

### ZONE 5 -- Beam Quality Checks

**Section label:** `PRE-IMPLANT BEAM VERIFICATION` -- Y: 27.2".

**BLOCK F -- Verification Checklist**

Y: 27.8" to 32.3". Six checklist items in a 3x2 grid.

| Position | Check | Accent | Specification | If Failed |
|---|---|---|---|---|
| R1C1 | Beam species | `#E8A020` | Mass spectrum shows only target species at resolving slit | Re-tune magnet; check source gas; verify slit position |
| R1C2 | Beam energy | `#E8A020` | Verified by analyzing magnet field + extraction voltage | Recalibrate; check power supply setpoints |
| R1C3 | Beam current | `#27AE60` | Faraday cup reads target current (+/- 5%) | Adjust source parameters; check extraction; clean source |
| R2C1 | Dose uniformity | `#27AE60` | Multi-point Faraday scan: +/- 1--2% across wafer area | Adjust scan waveform; check scan amplitudes |
| R2C2 | Beam profile | `#2EC4B6` | Beam shape centered; no asymmetry or halo | Re-steer beam; check for aperture obstruction |
| R2C3 | Charge neutralization | `#2EC4B6` | Electron flood gun active (for insulating substrates) | Verify flood gun emission; check filament |

Each item: Rounded rect, W: 7.33", H: 2.0", fill `#1E2435`, left accent 0.06".
Check: Barlow SemiBold, 14 pt, accent color.
Specification: JetBrains Mono 11 pt `#F0EDE8`.
If Failed: Inter Regular, 11 pt, `#E05C5C`.

---

### ZONE 6 -- Footer

Standard. Title: `Beam Setup -- Ion Implantation`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Beam Setup Ion Implantation -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The beam-line schematic hero (Zone 2) is the most technically complex visual in the Ion Implantation cluster. It must communicate the elegance of the beam-line concept: a focused stream of precisely selected ions, accelerated to exact energy, scanned uniformly across the substrate. The mass analyzer explanation (Zone 4) is where this poster earns its educational value -- most people outside semiconductor manufacturing have never heard of an analyzing magnet. The analogy to a prism separating light by wavelength works well if verbally described, but the poster uses the physics directly: r = mv/qB.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #454 -- Construction Workup v1.0*
*2026-04-26*
