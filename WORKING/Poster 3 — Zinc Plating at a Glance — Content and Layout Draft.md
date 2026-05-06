---
Project: Plating Posters Inc
Poster Number: 3
Title: "Zinc Plating at a Glance: Acid Chloride vs. Alkaline Non-Cyanide"
Document Type: Content and Layout Draft
Status: v1.0 — Ready for Canva Construction Workup
Created: 2026-04-04T00:00:00
Author: Alaina (poster-designer)
Technical Source: Watson — Zinc Plating at a Glance Research Brief v1 (2026-04-04)
Watson Flags: THREE — throwing power ratios (Tyler), NZP P1/P2 compatibility (Tyler), KCl vs NH4Cl emphasis (Drew) — all non-blocking
Process Scope: Zinc plating — acid chloride and alkaline non-cyanide (two sub-processes, one metal, one poster)
Editions: Dark + Light
tags:
  - PosterDesign
  - ZincPlating
  - AcidZinc
  - AlkalineZinc
  - ContentDraft
---

# Poster #3 — Content and Layout Draft
## Zinc Plating at a Glance: Acid Chloride vs. Alkaline Non-Cyanide

*Alaina — Plating Posters Inc Creative Lead*
*v1.0 — 2026-04-04*
*Content sourced from Watson's Zinc Plating at a Glance Research Brief v1. This poster gives process engineers and operators a single wall reference comparing the two dominant zinc plating systems — side by side, honest about tradeoffs.*

---

## Section 1 — Watson Flag Status and Design Decisions

**Status: THREE FLAGS — non-blocking.**

**Flag 1 (Tyler):** Throwing power thickness ratios — 3:1-5:1 for acid vs. 1.5:1-2:1 for alkaline on equivalent geometry. Watson sources these from industry literature. Tyler may have Hull cell comparison data to validate or refine.

**Flag 2 (Tyler):** BriteGuard NZP P1/P2 performance equivalence on both acid and alkaline zinc deposits. Poster states "both zinc types accept all passivation chemistries" — Tyler should confirm NZP specifically.

**Flag 3 (Drew):** KCl vs. NH4Cl emphasis — should the poster emphasize one sub-type, or treat them equally? Current draft treats KCl as the modern default with NH4Cl mentioned as an alternative. Confirm this reflects A Brite's customer base.

**Design decisions:**

- **HERO: the master comparison table.** This is a true head-to-head comparison poster. The table IS the product — two columns, every meaningful parameter, side by side. Amber for acid zinc (warm = acidic pH). Teal for alkaline zinc (cool = caustic pH). The color assignment is chemically intuitive and immediately separates the two systems visually.

- **Throwing power illustration.** The single most powerful visual for explaining why these two processes exist. Same part geometry, different thickness distribution. Acid zinc: thick at edges, thin in recesses. Alkaline zinc: more uniform. Built from layered rectangles in Canva — no external illustration needed.

- **Cathode efficiency concept panel.** The flat-line (acid) vs. declining-curve (alkaline) CE relationship is the scientific explanation behind throwing power. Including this elevates the poster from "what" to "why."

- **Decision guide.** Closes the poster with "when to choose which" — the question every engineer asks. Six criteria per system, presented as a compact two-column checklist.

- **One poster, two sub-processes?** This qualifies under the "one process per poster" rule because both are zinc plating systems producing the same functional coating. The comparison IS the value proposition. Splitting them into two posters would eliminate the head-to-head comparison that makes this content useful.

---

## Section 2 — Layout Zone Map

```
+------------------------------------------------------------------------+
| ZONE 1 — HEADER BAND (~0-8% / 2.9")                                    |
| BLOCK A: Headline + subheading + tagline (left ~55%)                    |
| BLOCK B: "Same Goal, Different Path" callout (right ~45%)               |
+------------------------------------------------------------------------+
| ZONE 2 — MASTER COMPARISON TABLE (HERO) (~8-50% / 15.1")              |
| BLOCK C: Two-column comparison — Acid Chloride | Alkaline NC            |
| 16 parameter rows + column headers                                       |
+------------------------------------------------------------------------+
| ZONE 3 — THROWING POWER + CE CONCEPT (~50-68% / 6.5")                 |
| BLOCK D: Throwing power illustration (left 55%)                          |
| BLOCK E: Cathode efficiency concept (right 45%)                          |
+------------------------------------------------------------------------+
| ZONE 4 — DECISION GUIDE + PASSIVATION (~68-82% / 5.0")                |
| BLOCK F: "When to choose which" (left 55%)                              |
| BLOCK G: Passivation compatibility strip (right 45%)                     |
+------------------------------------------------------------------------+
| ZONE 5 — SPECS + COMMON PROBLEMS (~82-90% / 2.9")                     |
| BLOCK H: ASTM B633 service conditions (left 50%)                        |
| BLOCK I: Top failure modes (right 50%)                                   |
+------------------------------------------------------------------------+
| ZONE 6 — FOOTER BAND (~90-100% / 3.6")                                 |
| BLOCK J: Disclaimer + Series + Logo + Version                            |
+------------------------------------------------------------------------+
```

**Zone height summary:**
| Zone | Content | % Height | Approx Inches |
|------|---------|----------|---------------|
| 1 — Header | Headline + callout | 8% | 2.9" |
| 2 — Comparison Table | HERO data block | 42% | 15.1" |
| 3 — Throwing Power | Illustration + CE concept | 18% | 6.5" |
| 4 — Decision Guide | Checklist + passivation | 14% | 5.0" |
| 5 — Specs + Problems | B633 + failure modes | 8% | 2.9" |
| 6 — Footer | Disclaimer + metadata | 10% | 3.6" |
| **Total** | | **100%** | **36.0"** |

---

## Section 3 — Content Blocks

---

### BLOCK A — Headline and Subheading

**Headline (Barlow Condensed ExtraBold, 88 pt, `#F0EDE8`):**

> ZINC PLATING AT A GLANCE

**Subheading (Barlow SemiBold, 36 pt, `#E8A020`):**

> Acid Chloride vs. Alkaline Non-Cyanide

**Tagline (Barlow SemiBold, 22 pt, `#F0EDE8` at 65% opacity):**

> Same goal. Different chemistry. Know the difference.

---

### BLOCK B — "Same Goal, Different Path" Callout (Header Right)

**Callout box:** fill `#1E2435`, border `#2EC4B6` Teal 1.5 pt, corner radius 8 pt

**Title (Barlow SemiBold, 18 pt, `#2EC4B6`):**

> WHY TWO SYSTEMS?

**Body (Inter Regular, 16 pt, `#F0EDE8`):**

> Both produce sacrificial zinc coatings that protect steel from corrosion. Acid zinc is fast and bright. Alkaline zinc throws better and bends without cracking. The right choice depends on your part and your spec.

**A Brite products (JetBrains Mono Regular, 14 pt, `#E8A020`):**

> Acid:     Brite-Zinc 404
> Alkaline: Brite-Zinc 421

---

### BLOCK C — Master Comparison Table (HERO — Zone 2)

**Section label (Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`, centered):**

> HEAD-TO-HEAD: EVERY PARAMETER THAT MATTERS

**Table structure:** Two data columns with a shared parameter label column on the left. Amber column header for acid, Teal column header for alkaline.

**Column structure (3 columns):**
1. **Parameter** (~28%) — Inter Medium, 16 pt, `#F0EDE8`
2. **Acid Chloride** (~36%) — accent `#E8A020` Amber column header
3. **Alkaline Non-Cyanide** (~36%) — accent `#2EC4B6` Teal column header

Column header row: Amber fill for acid column, Teal fill for alkaline column. Parameter column: `#3A4055` Mid Slate fill. Text: Barlow SemiBold 18 pt. Acid/Alkaline headers use `#1A1F2E` dark text on accent fill.

**Data rows (alternating `#1A1F2E` / `#252B3D`):**

| Parameter | Acid Chloride | Alkaline Non-Cyanide |
|-----------|---------------|----------------------|
| Primary salt | KCl 180-250 g/L | NaOH 100-140 g/L |
| Zinc metal | 15-30 g/L (2.0-4.0 oz/gal) | 8-15 g/L (1.1-2.0 oz/gal) |
| pH | 4.5-5.5 (target 4.8-5.2) | 13-14 |
| Temperature | 20-30 C (68-86 F) | 22-30 C (72-86 F) |
| Rack CD | 2-5 A/dm² (19-46 ASF) | 1-4 A/dm² (9-37 ASF) |
| Barrel CD | 0.3-1.5 A/dm² (3-14 ASF) | 0.3-1.5 A/dm² (3-14 ASF) |
| Cathode efficiency | 95-98% | 60-80% |
| Throwing power | Moderate | Excellent |
| Anode type | Soluble zinc (SHG 99.99%) | Insoluble mild steel |
| A:C ratio | 2:1 | 2:1 rack / 2.5:1 barrel |
| Buffer | Boric acid (25-45 g/L) | NaOH (inherent stability) |
| Critical ratio | Zn:boric acid balance | NaOH:Zn 9:1-12:1 |
| Deposit appearance | Bright to semi-bright | Semi-bright to matte |
| Deposit ductility | Good | Excellent |
| Iron limit | <50 ppm (action at 25) | <20 ppm (action at 10) |
| Copper limit | <10 ppm (action at 5) | <5 ppm (action at 2) |

Font for data cells: Inter Regular 16 pt for text values, JetBrains Mono Regular 16 pt for numerical values. Color: `#F0EDE8`.

**Table footnote (Inter Regular, 13 pt, `#F0EDE8` at 60%):**

> *Ranges are for normal production plating. NH₄Cl systems: similar parameters with additional buffering capacity and ammonia-bearing wastewater. Consult your product TDS for formulation-specific operating ranges.*

---

### BLOCK D — Throwing Power Illustration (Zone 3 — Left)

**Section label (Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`):**

> THROWING POWER — THE KEY DIFFERENCE

**Illustration:** Two copies of the same part cross-section (a U-channel or deep recess shape), side by side.

**Left part — Acid Zinc:**
- Part outline: `#3A4055` Mid Slate, 2 pt
- Deposit layer: `#C8D0D8` Bright Silver
- Thick deposit at edges/HCD areas (0.15" wide), thin deposit in recess/LCD area (0.03" wide)
- Label above: `ACID CHLORIDE` — Barlow SemiBold, 14 pt, `#E8A020`
- Annotation arrows: `Thick edges` (pointing to HCD), `Thin recess` (pointing to LCD)
- Thickness ratio label: `3:1 to 5:1 variation` — JetBrains Mono, 12 pt, `#E8A020`

**Right part — Alkaline Zinc:**
- Same part outline
- Deposit layer: `#C8D0D8` Bright Silver
- More uniform deposit (0.10" at edges, 0.07" in recess)
- Label above: `ALKALINE NC` — Barlow SemiBold, 14 pt, `#2EC4B6`
- Annotation: `Uniform coverage` (spanning full recess)
- Thickness ratio label: `1.5:1 to 2:1 variation` — JetBrains Mono, 12 pt, `#2EC4B6`

**Caption (Inter Medium, 15 pt, `#F0EDE8`):**

> Same part. Same thickness spec. Different distribution. Alkaline zinc throws better because its cathode efficiency varies with current density.

---

### BLOCK E — Cathode Efficiency Concept (Zone 3 — Right)

**Section label (Barlow Condensed ExtraBold, 20 pt, `#F0EDE8`):**

> WHY ALKALINE ZINC THROWS BETTER

**Conceptual graph:** A simplified CE vs. CD plot built from Canva shapes.

- X-axis: `Current Density (ASF)` — JetBrains Mono, 12 pt
- Y-axis: `Cathode Efficiency (%)` — JetBrains Mono, 12 pt
- Acid zinc line: flat horizontal line near 95-98%, `#E8A020` Amber, 3 pt
  - Label: `Acid: 95-98% — flat`
- Alkaline zinc line: declining curve from ~80% (low CD) to ~60% (high CD), `#2EC4B6` Teal, 3 pt
  - Label: `Alkaline: 80% → 60% — drops with CD`

Build the "curve" as 3-4 connected line segments (Canva line tool). The visual does not need to be mathematically precise — it needs to clearly communicate that acid CE is flat and alkaline CE declines.

**Key insight (Inter Medium, 14 pt, `#2EC4B6`):**

> Variable efficiency = self-leveling. LCD areas plate more efficiently than HCD areas, naturally redistributing metal toward recesses.

---

### BLOCK F — "When to Choose Which" Decision Guide (Zone 4 — Left)

**Section label (Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`):**

> WHEN TO CHOOSE WHICH

**Two sub-columns inside a callout box:**

Callout box: fill `#1E2435`, corner radius 8 pt

**Left sub-column — CHOOSE ACID**
- Title: Barlow SemiBold, 16 pt, `#E8A020`
- Text: `CHOOSE ACID WHEN:`
- Bullet list (Inter Regular, 14 pt, `#F0EDE8`):
  - Simple geometry (flat, cylindrical)
  - High throughput required
  - Bright appearance matters
  - Barrel plating small parts
  - New installation (easier operation)
  - Ammonia-free wastewater needed (KCl)

**Right sub-column — CHOOSE ALKALINE**
- Title: Barlow SemiBold, 16 pt, `#2EC4B6`
- Text: `CHOOSE ALKALINE WHEN:`
- Bullet list (Inter Regular, 14 pt, `#F0EDE8`):
  - Complex geometry (recesses, threads, tubes)
  - Tight thickness tolerance required
  - Paint/powder coat adhesion critical
  - High-strength steel (reduced H₂ risk)
  - Uniform passivate color needed
  - Customer spec requires it

Center divider: vertical line, `#3A4055` Mid Slate, 1 pt.

**Closing (Inter Medium, 14 pt, `#F0EDE8` at 70%):**

> Neither is universally better. The right choice depends on the part and the spec.

---

### BLOCK G — Passivation Compatibility (Zone 4 — Right)

**Section label (Barlow Condensed ExtraBold, 20 pt, `#F0EDE8`):**

> PASSIVATION COMPATIBILITY

**Passivation table (compact):**

| Passivation | Salt Spray (white) | RoHS |
|-------------|-------------------|------|
| Clear/blue trivalent | 72-120 hrs | Yes |
| Yellow trivalent | 120-200 hrs | Yes |
| Black trivalent | 72-120 hrs | Yes |
| Yellow hex (legacy) | 96-240 hrs | No |
| Olive drab hex | 200+ hrs | No |

Font: Inter Regular, 13 pt, `#F0EDE8`. RoHS column: Emerald for Yes, Coral for No.

**Key note (Inter Medium, 14 pt, `#27AE60`):**

> Both acid and alkaline zinc accept all passivation types. BriteGuard NZP P1/P2 works on both.

---

### BLOCK H — ASTM B633 Service Conditions (Zone 5 — Left)

**Compact table:**

| SC | Environment | Min Thickness |
|----|-------------|---------------|
| SC1 | Indoor, dry | 5 um (0.2 mil) |
| SC2 | Moderate | 8 um (0.3 mil) |
| SC3 | Severe, outdoor | 12 um (0.5 mil) |
| SC4 | Very severe | 25 um (1.0 mil) |

Font: Inter Regular, 13 pt. Header: Barlow SemiBold, 14 pt, `#E8A020`.

**Label:** `ASTM B633 — SERVICE CONDITIONS` — Barlow SemiBold, 16 pt, `#F0EDE8`

---

### BLOCK I — Top Failure Modes (Zone 5 — Right)

**Section label (Barlow SemiBold, 16 pt, `#E05C5C`):**

> COMMON PROBLEMS — QUICK REFERENCE

**Compact table (3 columns):**

| Problem | Acid Cause | Alkaline Cause |
|---------|-----------|----------------|
| Burning | Low Zn; low boric acid | Low Zn; low NaOH:Zn ratio |
| Pitting | Low carrier; organics | Low carrier; H₂ adhesion |
| Roughness | pH >5.5; anode bag damage | High carbonate; poor filtration |
| Dullness | High temp; low brightener | Brightener deficient; organics |

Font: Inter Regular, 12 pt, `#F0EDE8`. Left-border accents: `#E05C5C` Coral.

---

### BLOCK J — Footer Content

Standard footer per series convention.

**Band fill:** `#0D1020` Deep Navy

**Disclaimer:** `This poster presents industry-typical operating parameters for acid chloride and alkaline non-cyanide zinc plating. Specific ranges vary by vendor formulation — always consult your product TDS. Analysis by titration is the authoritative method for confirming bath composition.`

**Poster title:** `Zinc Plating at a Glance: Acid Chloride vs. Alkaline Non-Cyanide`
**Series name:** `Plating Posters Inc — Metal Finishing Reference Series`
**Version:** `v1.0 — 2026`
**Logo:** `[LOGO]`

---

## Section 4 — Light Edition Notes

Standard remap table applies. The two-column comparison table uses Amber and Teal as column header fills — keep column header text as `#F0EDE8` (Warm White) in both editions to ensure contrast on the darkened accent fills. Apply the Light edition override per Design Standards Section 3.

The throwing power illustration uses `#C8D0D8` Bright Silver for the deposit layer — unchanged in Light edition.

The CE concept graph lines (Amber and Teal) remap to their darkened Light equivalents. Verify the graph lines remain clearly distinguishable against the Light background.

---

## Section 5 — Collaboration Flags

**Watson:** Research complete. No additional research needed.

**Tyler (OPEN):** Validate throwing power thickness ratios (3:1-5:1 acid vs. 1.5:1-2:1 alkaline). Confirm NZP P1/P2 equivalence on both zinc types.

**Drew (OPEN):** KCl vs. NH4Cl emphasis — should KCl be presented as the default?

---

*Alaina — Plating Posters Inc Creative Lead*
*Poster #3 — Zinc Plating at a Glance — Content and Layout Draft v1.0*
*2026-04-04*
