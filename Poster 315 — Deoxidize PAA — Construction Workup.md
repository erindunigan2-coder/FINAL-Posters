---
Project: Plating Posters Inc
Poster Number: 315
Title: "Deoxidize -- PAA"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 5: PAA, Section 5.5)"
Technical Source: Desmut/deoxidize stage for PAA. Removes insoluble alloying element residues (smut) from caustic etch. HNO3 for standard alloys; HNO3/HF for copper-bearing alloys. FPL etch combines etch + desmut in one step.
Process Scope: Deoxidize / Desmut -- Stage 4 of PAA sequence
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Anodizing
  - PAA
  - Desmut
  - Deoxidize
  - ConstructionWorkup
  - ClusterAnodPAA
---

# Poster #315 -- Construction Workup
## Deoxidize -- PAA

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 4 of the PAA sequence. The desmut/deoxidize step removes the insoluble smut (copper, silicon, iron, manganese particles) left by the caustic etch. Smut trapped under even a 0.5--1.5 um PAA oxide is immediately visible as discoloration and directly reduces bond strength. If FPL etch was used in Stage 3, this step is already done (FPL combines etch + desmut).

Hero visual: cross-section showing smut layer on aluminum surface and the desmut chemistry dissolving it.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Desmut process hero (Block B):** Schematic showing smut particles being dissolved from the aluminum surface. Built with rectangles and labeled elements.
2. **Chemistry decision panel (Block D):** HNO3 vs. HNO3/HF decision tree based on alloy.
3. **HF safety callout (Block E):** Prominent safety warning for hydrofluoric acid.
4. **Alloy-specific desmut table (Block F):** Which chemistry for which alloy.
5. **FPL exception callout (Block G):** If FPL etch was used, skip this step.

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
  Stage 4 highlighted (Amber)
ZONE 3 -- DESMUT PROCESS HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- CHEMISTRY DECISION + PARAMETERS (14.5"--20.5" / ~6.0")
ZONE 5 -- HF SAFETY + ALTERNATIVES (20.5"--26.5" / ~6.0")
ZONE 6 -- ALLOY TABLE + FAILURE MODES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `DEOXIDIZE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `PAA Desmut -- Stage 4 of 7` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Remove the smut the etch left behind. What the caustic cannot dissolve, the desmut must.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 4 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Etched surface with smut residue  -->  After: Clean, smut-free surface ready for rinse and anodize`

---

### ZONE 3 -- Desmut Process Hero

**Section label:** `THE DESMUT PROCESS` -- Y: 4.4".

**BLOCK B -- Smut Removal Schematic**

Y: 5.0" to 13.5".

**Before panel (left half, X: 1.0", W: 10.5"):**
- Large rounded rect, H: 7.0", fill `#252B3D`
- Title: `BEFORE DESMUT` Barlow SemiBold 16 pt `#E05C5C`
- Aluminum substrate: horizontal rect at bottom, fill `#C8D0D8`
- Smut layer on top: irregular pattern of small colored dots/circles representing:
  - Copper particles: small circles `#E8A020` labeled `Cu`
  - Silicon particles: small circles `#3A4055` labeled `Si`
  - Iron particles: small circles `#E05C5C` labeled `Fe`
  - Manganese particles: small circles `#2EC4B6` labeled `Mn`
- Label: `Insoluble alloying element residues left by caustic etch` Inter Regular 13 pt `#F0EDE8` at 70%

**Arrow between panels:**
- Large right-pointing arrow, `#E8A020`
- Label: `HNO3 (or HNO3/HF) dissolves smut` Barlow SemiBold 14 pt `#E8A020`

**After panel (right half, X: 12.5", W: 10.5"):**
- Large rounded rect, H: 7.0", fill `#252B3D`
- Title: `AFTER DESMUT` Barlow SemiBold 16 pt `#27AE60`
- Aluminum substrate: horizontal rect at bottom, fill `#C8D0D8` -- clean, no particles
- Label: `Clean aluminum surface -- ready for PAA oxide growth` Inter Regular 13 pt `#27AE60`

**Bottom callout (Y: 12.8"):**
- Full-width callout, fill `#1E2435`, left accent `#E8A020` 0.06"
- `What is smut? Insoluble alloying elements (Cu, Si, Fe, Mn) that the alkaline etch cannot dissolve. They remain on the surface as a dark, powdery residue. Under PAA oxide, they block pore formation and reduce bond strength.` Inter Regular 14 pt `#F0EDE8`

**FPL exception badge (top-right of hero zone):**
- Rounded rect pill, fill `#27AE60` at 20%, border 1 pt `#27AE60`
- Text: `If FPL etch was used: SKIP THIS STEP -- FPL combines etch + desmut` Inter Medium 14 pt `#27AE60`

---

### ZONE 4 -- Chemistry Decision + Parameters

**Section label:** `DESMUT CHEMISTRY -- ALLOY DETERMINES THE PATH` -- Y: 14.7".

**Two-column layout (Y: 15.3" to 20.3"):**

**Left -- Standard Desmut: HNO3 (X: 0.5", W: 11.0"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `STANDARD: NITRIC ACID (HNO3)` Barlow SemiBold 18 pt `#E8A020`
- Subtitle: `For 6xxx alloys and low-copper alloys` Inter Regular 14 pt `#F0EDE8` at 60%

| Parameter | Value |
|---|---|
| Chemistry | HNO3 (concentrated = 67--70%) |
| Concentration | 25--50% by volume |
| Temperature | Ambient (room temp) |
| Time | 30--120 seconds |
| Agitation | Mild |

Note: `Nitric acid dissolves the aluminum smut matrix. Effective for alloys without significant copper or silicon content.` Inter Regular 13 pt `#F0EDE8` at 70%

**Right -- Aggressive Desmut: HNO3/HF (X: 12.0", W: 11.5"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E05C5C` 0.06"
- Title: `AGGRESSIVE: MIXED ACID (HNO3/HF)` Barlow SemiBold 18 pt `#E05C5C`
- Subtitle: `For 2xxx (copper) and 7xxx (zinc/copper) alloys` Inter Regular 14 pt `#F0EDE8` at 60%

| Parameter | Value |
|---|---|
| HNO3 | 25--50% by volume |
| HF (40% conc.) | 1--3% by volume |
| Temperature | Ambient |
| Time | 60--180 seconds |
| Agitation | Mild |

Note: `HF attacks metallic copper particles and dissolves silicon. Without HF, residual copper on 2024 causes mottled oxide and bond failure.` Inter Regular 13 pt `#E05C5C`

---

### ZONE 5 -- HF Safety + Alternatives

**Section label:** `HF SAFETY + NON-HF ALTERNATIVES` -- Y: 20.7".

**Two-column layout (Y: 21.3" to 26.3"):**

**Left -- HF Safety (X: 0.5", W: 11.0"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E05C5C` 0.06"
- Title: `HYDROFLUORIC ACID (HF) SAFETY` Barlow SemiBold 22 pt `#E05C5C`

Body (Inter Regular 14 pt `#F0EDE8`, line height 155%):

> HF is extremely hazardous. Unlike other acids, it penetrates skin and causes systemic fluoride poisoning affecting bones and heart.
>
> MANDATORY CONTROLS:
> -- Calcium gluconate gel available at the station
> -- HF-specific training for ALL personnel
> -- Buddy system -- never work alone with HF
> -- Full acid-resistant PPE including face shield
> -- Immediate medical treatment for ANY skin contact
> -- Emergency shower and eyewash within 10 seconds
>
> Skin contact may not cause immediate pain. Delayed symptoms (hours later) mean deeper tissue damage.

Bottom stat: `HF burns are a medical emergency -- treat first, report second` Inter Medium 14 pt `#E05C5C`

**Right -- Non-HF Alternatives (X: 12.0", W: 11.5"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#27AE60` 0.06"
- Title: `NON-HF ALTERNATIVES` Barlow SemiBold 18 pt `#27AE60`

Body (Inter Regular 14 pt `#F0EDE8`, line height 155%):

> **Ferric sulfate-based desmuts** (proprietary, non-HF):
> -- Gaining market share due to HF safety concerns
> -- Work well on 6xxx alloys
> -- May be insufficient for heavy copper smut on 2024
> -- Must be validated for your specific alloy/spec
>
> **Legacy chromic-sulfuric acid deox:**
> -- Na2Cr2O7 30--60 g/L + H2SO4 300--450 g/L
> -- 60--70 C, 5--10 min
> -- Excellent but contains Cr6+
> -- Regulatory pressure eliminating this option

Note: `For PAA on 2024: validate any non-HF desmut against bond test requirements before switching` Inter Medium 13 pt `#E8A020`

---

### ZONE 6 -- Alloy Table + Failure Modes

**Section label:** `ALLOY-SPECIFIC DESMUT + FAILURES` -- Y: 26.7".

**Two-column layout (Y: 27.3" to 32.3"):**

**Left -- Alloy Desmut Guide (X: 0.5", W: 11.0"):**
- Title: `WHICH DESMUT FOR WHICH ALLOY?` Barlow Condensed ExtraBold 22 pt `#F0EDE8`

| Alloy | Recommended Desmut | Time | Notes |
|---|---|---|---|
| 6061 / 6063 | HNO3 25--50% | 30--60 sec | Light smut; standard desmut |
| 5052 | HNO3 25--50% | 30--60 sec | Minimal smut |
| 2024 | HNO3/HF | 60--180 sec | Heavy Cu smut; HF required |
| 7075 | HNO3/HF | 60--180 sec | Cu + Zn smut; aggressive desmut |
| 1100 | HNO3 25% | 15--30 sec | Very light smut; brief dip |

5-row table, alternating fills. Data: JetBrains Mono 12 pt.

**Right -- Failure Modes (X: 12.0", W: 11.5"):**
- Title: `DESMUT FAILURES` Barlow Condensed ExtraBold 22 pt `#F0EDE8`

| Failure | Cause | Bond Impact |
|---|---|---|
| Residual smut | Inadequate chemistry or time | Smut blocks oxide pores; bond failure |
| Mottled oxide | Copper smut on 2024 (no HF used) | Non-uniform bond surface; weak zones |
| Surface pitting | Over-aggressive desmut (HF on thin walls) | Stress concentrators; substrate damage |
| Grain boundary attack | Excessive HF time | Weakened substrate; potential fatigue issue |

4-row table with Coral left accent. Data: Inter Regular 12 pt.

---

### ZONE 7 -- Footer

Standard. Title: `Deoxidize -- Phosphoric Acid Anodizing (PAA)`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; ASTM D3933. Desmut parameters shown are typical industry values. HF handling requires site-specific safety protocols that may exceed the general guidance on this poster. Consult your EHS department.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Deoxidize PAA -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The HF safety callout must be unmissable -- this is one of the most dangerous chemicals in any plating shop. The alloy decision path (HNO3 vs. HNO3/HF) is the key operator decision on this poster. The FPL exception badge reminds operators that if FPL etch was used in Stage 3, the desmut is already done -- preventing redundant processing.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #315 -- Construction Workup v1.0*
*2026-04-26*
