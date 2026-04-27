---
Project: Plating Posters Inc
Poster Number: 602
Title: "Post-Treatment -- Plasma Nitriding"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 5)"
  - "Process 4 (Gas Nitriding), Sections 4.7, 4.9"
Process Scope: Post-nitriding treatment options -- compound layer management, lapping, polishing, and any supplementary processing
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - PlasmaNitriding
  - PostTreatment
  - ConstructionWorkup
  - DiffusionHeatTreatment
---

# Poster #602 -- Construction Workup
## Post-Treatment -- Plasma Nitriding

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

After the parts come out of the chamber, the job is not always done. Some specifications require compound layer removal (lapping or grinding the white layer off). Some applications benefit from a controlled oxidation step for corrosion resistance. Some parts go straight to inspection with no post-treatment at all. This poster maps those decision paths.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Post-treatment decision tree (Block B -- HERO):** Flow from "parts unloaded" through decision points to final disposition.
2. **Compound layer management table (Block D):** When to keep, when to remove, when to modify.
3. **Surface treatment options (Block E):** Lapping, polishing, oxidation, coating.
4. **Application examples (Block F):** Real-world use cases mapped to post-treatment choice.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- DECISION TREE HERO (2.9"--15.5")
ZONE 3 -- COMPOUND LAYER MANAGEMENT (15.5"--22.0")
ZONE 4 -- SURFACE OPTIONS + APPLICATIONS (22.0"--32.5")
ZONE 5 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `POST-TREATMENT` -- 88 pt `#F0EDE8`.
**Subheading:** `Plasma Nitriding -- What Happens After the Chamber Door Opens` -- 32 pt `#E8A020` (Amber).
**Tagline:** `Keep the white layer, remove it, or skip it entirely -- plasma nitriding gives you the choice before and after the cycle.` -- 20 pt `#F0EDE8` at 65%.

**Rule card (right):**
- Big number: `3` -- 72 pt `#2EC4B6`
- Label: `Post-treatment paths: keep / remove / none (no white layer)` -- 14 pt `#F0EDE8`

---

### ZONE 2 -- Decision Tree (HERO)

**Section label:** `POST-TREATMENT DECISION TREE` -- Y: 3.1".

**BLOCK B -- Flow Diagram (Y: 3.8" to 15.3")**

Start node:
- Rounded rect, X: 8.5", Y: 4.0", W: 7.0", H: 1.0", fill `#27AE60` at 30%, border 2 pt `#27AE60`
- Text: `PARTS UNLOADED FROM CHAMBER` Barlow SemiBold 16 pt `#27AE60`

Decision 1 (Y: 5.5"):
- Diamond, X: 9.5", W: 5.0", fill `#252B3D`, border 2 pt `#E8A020`
- Text: `COMPOUND LAYER PRESENT?`

Branch YES-LEFT (Y: 7.0"):
- Arrow left to Decision 2

Decision 2 (Y: 7.0", X: 2.0"):
- Diamond, W: 5.0", fill `#252B3D`, border 2 pt `#E8A020`
- Text: `SPEC REQUIRES REMOVAL?`

Branch YES (Y: 9.0", X: 2.0"):
- Action box: `LAP / GRIND WHITE LAYER` fill `#1E2435`, accent `#E05C5C`
- Detail: `Remove 0.0002--0.001 inch compound layer by precision lapping or fine grinding`
- Then: `INSPECT -> SHIP`

Branch NO (Y: 9.0", X: 7.0"):
- Decision 3: `OXIDATION / COATING DESIRED?`
- YES -> `CONTROLLED OXIDATION or COATING` (amber accent)
  - Detail: `Steam oxidation, oil quench (cosmetic black), or post-coat per application`
- NO -> `INSPECT -> SHIP (compound layer retained)` (emerald accent)

Branch NO from Decision 1 (right, Y: 7.0"):
- Action box: `NO COMPOUND LAYER -- DIFFUSION ZONE ONLY`
- Detail: `Process was run at < 10% N2 -- no white layer produced`
- Then: `INSPECT -> SHIP`

All boxes: Rounded rect, W: 7.0", H: 1.5"--2.0", fill `#1E2435`.
Arrows: 3 pt `#3A4055`.
Decision diamonds: border `#E8A020`.

---

### ZONE 3 -- Compound Layer Management

**Section label:** `COMPOUND LAYER -- KEEP, REMOVE, OR PREVENT` -- Y: 15.7".

**BLOCK D -- Three-Column Guide (Y: 16.3" to 21.8")**

| Column | Title | When | How | Accent |
|---|---|---|---|---|
| KEEP | Retain compound layer | Wear applications; corrosion barrier needed; general industrial use | No post-treatment; inspect directly | `#27AE60` |
| REMOVE | Remove compound layer | Fatigue-critical applications (compound layer is brittle under bending fatigue); specs requiring zero white layer (some aerospace) | Precision lapping (< 0.001 inch removal); fine grinding; avoid aggressive stock removal that damages diffusion zone | `#E05C5C` |
| PREVENT | No compound layer produced | Maximum fatigue life applications; process run at < 10% N2 / > 90% H2 | Controlled during nitriding cycle -- NOT a post-treatment; unique to plasma nitriding | `#2EC4B6` |

Each column: Rounded rect, W: 7.33", H: 5.3", fill `#1E2435`, top accent 4 pt in column color.
Title: Barlow SemiBold 20 pt in accent color.
Content: Inter Regular 13 pt `#F0EDE8`.

---

### ZONE 4 -- Surface Options + Applications

**Two-column layout (Y: 22.2" to 32.3")**

**Left -- BLOCK E: Surface Treatment Options (X: 0.5", W: 11.0")**

Section label: `OPTIONAL SURFACE TREATMENTS` -- Barlow Condensed ExtraBold 22 pt.

| Treatment | Purpose | Method | Notes |
|---|---|---|---|
| Precision lapping | Remove compound layer | Fine abrasive lapping; < 0.001 inch removal | Do not damage diffusion zone |
| Fine grinding | Remove compound layer + size correction | Surface grinder with fine wheel | Minimal stock removal |
| Steam oxidation | Corrosion resistance + black finish | Steam at 900--1000 F; 30--60 min | Forms magnetite (Fe3O4) on compound layer |
| Oil blackening | Cosmetic appearance | Hot oil immersion | Less durable than steam oxidation |
| Post-coating | Additional protection | PVD, DLC, or other thin-film coatings over nitrided surface | Duplex treatment -- nitrided substrate + hard coating |

Table: Header `#3A4055`, alternating rows. JetBrains Mono 12 pt for methods, Inter Regular for notes.

**Right -- BLOCK F: Application Examples (X: 12.0", W: 11.5")**

Section label: `REAL-WORLD POST-TREATMENT CHOICES` -- Barlow Condensed ExtraBold 22 pt.

| Application | Post-Treatment | Why |
|---|---|---|
| Automotive crankshaft | Keep compound layer | Wear resistance on journal surfaces |
| Aerospace gear (AMS 2759/10) | Remove white layer by lapping | Fatigue life; spec requires zero compound layer or max 0.0003 inch |
| Injection mold die (H13) | Keep + polish to mirror | Wear + release properties; compound layer aids demolding |
| Austenitic SS medical instrument | None produced (low N2 process) | S-phase only; corrosion resistance preserved; no brittle layer |
| Firearm barrel / slide | Keep + optional oxidation | Wear + corrosion + cosmetic black |
| High-speed tool steel punch (M2) | Keep compound layer | Maximum wear life; fatigue less critical |

Each row: H: 1.3", alternating fills. Application: Inter Medium 13 pt `#F0EDE8`. Post-treatment: JetBrains Mono 12 pt in accent color. Why: Inter Regular 12 pt `#F0EDE8` at 70%.

---

### ZONE 5 -- Footer

Standard footer. Title: `Post-Treatment -- Plasma Nitriding`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 5 zones. **Light Remap:** Standard table. **Export:** Six files.

---

*Alaina -- Poster #602 -- Construction Workup v1.0 -- 2026-04-26*
