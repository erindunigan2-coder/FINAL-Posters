---
Project: Plating Posters Inc
Poster Number: 674
Title: "Cure -- E-Coat"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting & Organic Coating Clusters -- Watson Research Brief (Cluster 3, Section 3.8)"
Technical Source: Cathodic e-coat bake/cure parameters, blocked isocyanate cross-linking chemistry, oven profiling, and undercure detection. Values are typical for automotive cathodic epoxy e-coat systems.
Process Scope: E-coat bake oven cure -- Stage 8 of 9
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ECoating
  - Cure
  - CrossLinking
  - ConstructionWorkup
  - PaintingCoating
  - ClusterPC03
---

# Poster #674 -- Construction Workup
## Cure -- E-Coat

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 8 of 9. The bake oven transforms a wet, gel-like electrodeposited film into a tough, solvent-resistant thermoset primer. The chemistry is elegant: blocked isocyanate cross-linkers unblock at ~300 F, freeing isocyanate groups to react with hydroxyl groups on the epoxy resin backbone. The critical distinction -- oven temperature vs. metal temperature -- catches more people than any other concept in e-coat. The oven is at 375 F; the question is whether the METAL got to 340 F.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cure chemistry diagram (Block B -- HERO):** Visual showing the blocked isocyanate unblocking mechanism and cross-linking reaction. Simplified chemical schematic with temperature milestones.
2. **Oven profile concept (Block C):** Time-temperature chart showing oven air temp vs. metal temp, with the cure window highlighted.
3. **Bake parameter table (Block D):** Compact parameter table.
4. **Undercure vs. overcure comparison (Block E):** Side-by-side callout.
5. **Troubleshooting strip (Block F):** 4 cure problems.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.0" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 8 highlighted (Amber)
ZONE 3 -- CURE CHEMISTRY HERO (4.2"--14.0" / ~9.8")
ZONE 4 -- OVEN PROFILE + PARAMETERS (14.0"--20.5" / ~6.5")
ZONE 5 -- UNDERCURE VS. OVERCURE (20.5"--26.5" / ~6.0")
ZONE 6 -- TROUBLESHOOTING STRIP (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CURE` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `E-Coat Bake Oven -- Blocked Isocyanate Cross-Linking -- Stage 8 of 9` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `The oven says 375 F. Does the metal? Cure is defined by metal temperature -- not oven air temperature. Get this wrong and everything downstream fails.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 8 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Wet gel-like electrodeposited film  -->  After: Tough thermoset primer, MEK rub 100+ double rubs, ready for topcoat`

---

### ZONE 3 -- Cure Chemistry Hero

**Section label:** `BLOCKED ISOCYANATE CROSS-LINKING -- THE CURE REACTION` -- Y: 4.4".

**BLOCK B -- Cure Chemistry Diagram**

Y: 5.0" to 13.5". Full width within margins.

**Three-stage visual (left to right):**

**Stage 1 -- Deposited Film (X: 0.5", W: 7.0", H: 7.5"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#2EC4B6`
- Title: `DEPOSITED FILM` Barlow SemiBold 20 pt `#2EC4B6`
- Subtitle: `Before Oven` 14 pt `#F0EDE8` at 50%

Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):
```
Epoxy-amine resin backbone
  with pendant hydroxyl (-OH) groups

Blocked isocyanate cross-linker:
  Caprolactam-blocked MDI or IPDI

The blocking agent keeps the
isocyanate group dormant at
room temperature.

Film state: wet, gel-like,
water-sensitive, no solvent
resistance.
```

**Arrow to Stage 2:** 3 pt `#E8A020`, right arrowhead. Label: `HEAT` Barlow SemiBold 14 pt `#E8A020`.

**Stage 2 -- Unblocking (X: 8.0", W: 7.5", H: 7.5"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#E8A020`
- Title: `UNBLOCKING` Barlow SemiBold 20 pt `#E8A020`
- Subtitle: `~300 F (149 C)` 14 pt `#E8A020` at 70%

Content:
```
At ~300 F, the blocking agent
volatilizes (evaporates off):

  Blocked-NCO  -->  Free -NCO
                  + Caprolactam (gas)

The freed isocyanate group (-NCO)
is now highly reactive.

IMPORTANT: Caprolactam vapor is
released into the oven atmosphere.
Must be captured by afterburner
(thermal or catalytic oxidizer).

This is the primary VOC emission
source from e-coat operations.
```

JetBrains Mono 12 pt for the reaction equation, `#E8A020`.

**Arrow to Stage 3:** 3 pt `#27AE60`, right arrowhead. Label: `CURE` Barlow SemiBold 14 pt `#27AE60`.

**Stage 3 -- Cross-Linking (X: 16.0", W: 7.5", H: 7.5"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#27AE60`
- Title: `CROSS-LINKING` Barlow SemiBold 20 pt `#27AE60`
- Subtitle: `340--360 F metal temp, 20--30 min` 14 pt `#27AE60` at 70%

Content:
```
Free isocyanate reacts with
hydroxyl groups on epoxy backbone:

  -NCO + -OH  -->  Urethane linkage

Cross-links form a dense,
three-dimensional thermoset network.

Result:
  Tough, solvent-resistant film
  Excellent adhesion to phosphate
  500--1,000+ hr B117 salt spray
  MEK rub: 100+ double rubs

Once cured, the film CANNOT
be remelted or redissolved.
```

JetBrains Mono 12 pt for reaction equation, `#27AE60`.

---

### ZONE 4 -- Oven Profile + Parameters

**Section label:** `OVEN PROFILE -- METAL TEMP IS WHAT MATTERS` -- Y: 14.2".

**Two-column layout (Y: 14.8" to 20.3"):**

**Left -- Oven Profile Concept (X: 0.5", W: 12.0", H: 5.3"):**
- Rounded rect, fill `#1E2435`, left accent 0.06" `#E8A020`
- Title: `TIME-TEMPERATURE PROFILE` Barlow SemiBold 20 pt `#E8A020`

Content: Conceptual description of a time-temperature chart (generation prompt should draw this as a simplified graph):
```
X-axis: Time in oven (0--45 min)
Y-axis: Temperature (ambient--400 F)

Line 1 (dashed, Amber): OVEN AIR TEMP
  Rapidly reaches 350--375 F set point

Line 2 (solid, Teal): METAL TEMP
  Lags behind oven air -- ramp depends
  on part mass and geometry

CURE WINDOW (highlighted zone):
  Metal temp 340--360 F for 20--30 min

A car body may need 30--45 min total
oven time for the metal to reach and
hold cure temperature.
```

Key callout: `Use thermocouple data loggers (Datapaq, ECD) to map actual metal temp vs. time through the oven.` Inter Medium 13 pt `#E8A020`

**Right -- Bake Parameter Table (X: 13.0", W: 10.5", H: 5.3"):**
- Rounded rect, fill `#1E2435`, left accent 0.06" `#27AE60`
- Title: `BAKE PARAMETERS` Barlow SemiBold 20 pt `#27AE60`

**BLOCK D -- Parameter Table**

| Parameter | Value |
|---|---|
| Oven air temperature | 350--375 F (177--191 C) |
| Metal temperature at cure | 340--360 F (171--182 C) |
| Time at metal temp | 20--30 min |
| Total oven time (car body) | 30--45 min (including ramp) |
| Blocking agent unblock temp | ~300 F (149 C) |
| Afterburner required | YES -- blocking agent VOC |
| Oven type | Convection (gas-fired) |
| Energy source | Natural gas (most common) |

JetBrains Mono 13 pt for values. Inter Medium 13 pt for labels.

---

### ZONE 5 -- Undercure vs. Overcure

**Section label:** `UNDERCURE VS. OVERCURE -- BOTH ARE FAILURES` -- Y: 20.7".

**BLOCK E -- Side-by-Side Comparison (Y: 21.3" to 26.3")**

**Left -- Undercure (X: 0.5", W: 11.0", H: 4.8"):**
- Rounded rect, fill `#1E2435`, left accent 0.06" `#E05C5C`
- Title: `UNDERCURE` Barlow SemiBold 20 pt `#E05C5C`
- Subtitle: `Metal temp too low or time too short` 14 pt `#F0EDE8` at 50%

Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):

| Symptom | Detail |
|---|---|
| MEK rub | < 100 double rubs (film dissolves) |
| Solvent resistance | Poor -- topcoat solvents attack primer |
| Adhesion | Reduced -- topcoat delaminates |
| Salt spray | Degraded corrosion protection |
| Visual | May look normal -- HIDDEN failure |

Detection method:
- `MEK double rub test: minimum 100 double rubs for cathodic e-coat. Test EVERY oven zone change.` Inter Medium 13 pt `#E05C5C`

**Right -- Overcure (X: 12.0", W: 11.5", H: 4.8"):**
- Rounded rect, fill `#1E2435`, left accent 0.06" `#E8A020`
- Title: `OVERCURE` Barlow SemiBold 20 pt `#E8A020`
- Subtitle: `Metal temp too high or time excessive` 14 pt `#F0EDE8` at 50%

| Symptom | Detail |
|---|---|
| Yellowing | Epoxy darkens with excess heat |
| Brittleness | Film loses flexibility, cracks on impact |
| Intercoat adhesion | Primer surface too hard for topcoat bite |
| Energy waste | Higher fuel cost for no benefit |
| Visual | Yellow discoloration visible on light colors |

Prevention:
- `Oven profiling with data loggers. Verify metal temp stays within 340--360 F window. Do not exceed 380 F metal.` Inter Medium 13 pt `#E8A020`

---

### ZONE 6 -- Troubleshooting Strip

**Section label:** `CURE PROBLEMS -- 4 COMMON ISSUES` -- Y: 26.7".

**BLOCK F -- Four Problem Cards (Y: 27.3" to 32.3")**

Four cards in a single row. Gap: 0.33".

Each card: Rounded rect W: 5.5", H: 4.5", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | MEK RUB FAILURE | Metal temp below 340 F or time under 20 min | Profile oven with data loggers; increase zone temps or slow conveyor |
| 2 | 6.33" | YELLOWING | Oven too hot or dwell too long (overcure) | Reduce peak metal temp; optimize conveyor speed |
| 3 | 12.16" | POOR TOPCOAT ADHESION | Undercure (soft primer) or overcure (glassy surface) | Verify MEK rub 100+; if overcure, scuff sand before topcoat |
| 4 | 18.0" | AFTERBURNER ALARM | Blocking agent concentration exceeds LEL limit | Check afterburner operation; verify exhaust volume; reduce line speed |

Interior per card:
- Problem: Barlow SemiBold 16 pt `#E05C5C`
- Cause: Inter Regular 13 pt `#F0EDE8`
- Fix: Inter Medium 13 pt `#27AE60`

---

### ZONE 7 -- Footer

Standard. Title: `Cure -- E-Coat`. Version `v1.0 -- 2026`.

Disclaimer note: `Source: General industry knowledge; automotive cathodic e-coat specifications. Cure temperatures are for cathodic epoxy systems. Specific formulations may require different cure windows.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cure E-Coat -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The three-stage cure chemistry visual is the hero -- it tells the story of blocked isocyanate unblocking and cross-linking in a way that even non-chemists can follow. The metal temperature vs. oven temperature distinction is the single most important concept on this poster. The undercure vs. overcure comparison makes the point that both extremes are failures -- and that undercure is the more dangerous because it looks normal until the topcoat goes on.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #674 -- Construction Workup v1.0*
*2026-04-26*
