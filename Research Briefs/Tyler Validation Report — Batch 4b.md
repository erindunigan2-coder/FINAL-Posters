---
title: "Tyler Validation Report — Batch 4b"
date: 2026-04-27T00:00:00
author: Tyler (tyler-plating-chemist)
status: Complete
scope: "Main tank/anodize stage validation for 5 clusters: EL-08 EN-Boron, AN-02 Type III, AN-04 BSAA, AN-05 PAA, AN-06 Bright Anodizing"
tags:
  - PosterValidation
  - TylerReview
  - Batch4b
---

# Tyler Validation Report — Batch 4b

**Tyler — Plating Chemist / Analytical Chemistry**
**Date:** 2026-04-27
**Scope:** Main tank poster validation for 5 clusters against Watson Research Briefs

---

## Summary

| # | Cluster | Poster | Verdict | Flags |
|---|---------|--------|---------|-------|
| 1 | EL-08 EN-Boron | 276 | **FLAG** | 2 flags (deposition rates, boron range in header) |
| 2 | AN-02 Type III Hard Anodize | 292 | **PASS** | 0 flags — anode/cathode correct, all parameters match |
| 3 | AN-04 BSAA | 308 | **FLAG** | 1 flag (H2SO4 concentration in comparison table) |
| 4 | AN-05 PAA | 317 | **FLAG** | 1 critical flag (workpiece labeled CATHODE — must be ANODE) |
| 5 | AN-06 Bright Anodizing | 325 | **PASS** | 0 flags — anode/cathode correct, all parameters match |

**Critical flags: 1** (Poster 317 electrode polarity error)
**Non-critical flags: 3**

---

## Cluster 1 — EL-08 Electroless Nickel-Boron (Poster 276)

**Source Brief:** Electroless Clusters — Watson Research Brief v1.1, Process 8, Poster 6
**CW File:** `Poster 276 — EN Boron Main Tank — Construction Workup.md`

### Deposition Rate Check (Drew's note: Watson corrected to DMAB 10-20, NaBH4 20-30)

The CW shows:
- DMAB deposition rate: **10-20 um/hr** (line 121)
- NaBH4 deposition rate: **20-30 um/hr** (line 165)

Watson's Research Brief (lines 1319-1320) reports:
- DMAB: **8-15 um/hr**
- NaBH4: **15-25 um/hr**

Watson's deposition rate comparison table (line 1502-1503) reports:
- DMAB: **8-15 um/hr**
- NaBH4: **15-25 um/hr**

The CW values (10-20 and 20-30) are the "corrected" values per Drew's note. However, my assessment:

> **FLAG 1 — Deposition Rates (Lines 121, 165)**
>
> The CW values of 10-20 um/hr (DMAB) and 20-30 um/hr (NaBH4) are on the high side compared to most published EN-B literature. The brief's original values of 8-15 um/hr (DMAB) and 15-25 um/hr (NaBH4) are more consistent with my understanding of typical EN-B bath performance. DMAB baths rarely exceed 15 um/hr in production; 20 um/hr would be exceptional. NaBH4 baths can reach 20-25 um/hr in optimized formulations, but 30 um/hr is at the upper extreme.
>
> **Recommendation:** Use 8-15 um/hr for DMAB and 15-25 um/hr for NaBH4. These are the values Watson's brief reports, and they align better with ASTM B841 reference data and published Atotech/MacDermid technical literature. If Watson's correction was based on a specific source, that source should be cited. If it was a general upward adjustment without a specific reference, I recommend reverting to the brief's original values.

### Bath Composition and Parameters — DMAB Side

| Parameter | CW (Poster 276) | Brief (Process 8) | Match? |
|---|---|---|---|
| NiCl2/NiSO4 | 20-30 g/L Ni2+ | 20-30 g/L Ni2+ | YES |
| DMAB | 2-5 g/L | 2-5 g/L | YES |
| EDA | 30-60 g/L | 30-60 g/L | YES |
| pH | 6.0-8.0 | 6.0-8.0 | YES |
| Temperature | 60-75 C | 60-75 C | YES |
| Ni concentration | 4-6 g/L | 4-6 g/L | YES |
| Boron content | 0.5-3 wt% | 0.5-3 wt% | YES |
| Bath life | 3-5 MTO | 3-5 MTO | YES |
| Stabilizer | Thallium/lead acetate 0.5-2 ppm | Thallium/lead acetate 0.5-2 ppm | YES |

### Bath Composition and Parameters — Borohydride Side

| Parameter | CW (Poster 276) | Brief (Process 8) | Match? |
|---|---|---|---|
| NiCl2 | 20-30 g/L Ni2+ | 20-30 g/L Ni2+ | YES |
| NaBH4 | 0.5-1.5 g/L | 0.5-1.5 g/L | YES |
| EDA | 40-80 g/L | 40-80 g/L | YES |
| NaOH | 40-90 g/L | 40-90 g/L | YES |
| pH | 12.0-14.0 | 12.0-14.0 | YES |
| Temperature | 90-95 C | 90-95 C | YES |
| Boron content | 3-8 wt% | 3-8 wt% | YES |
| Bath life | 2-4 MTO | 2-4 MTO | YES |

### Deposit Properties — DMAB

| Property | CW | Brief | Match? |
|---|---|---|---|
| Hardness (as-plated) | 700-800 HV | 700-800 HV | YES |
| Hardness (HT) | 1000-1200 HV | 1000-1200 HV | YES |
| CoF (dry) | 0.08-0.12 | 0.08-0.12 | YES |
| Salt spray (25 um) | 200-500 hrs | 200-500 hrs | YES |

### Deposit Properties — Borohydride

| Property | CW | Brief | Match? |
|---|---|---|---|
| Hardness (as-plated) | 750-850 HV | 750-850 HV | YES |
| Hardness (HT) | 1100-1300 HV | 1100-1300 HV | YES |
| CoF (dry) | 0.05-0.10 | 0.05-0.10 | YES |
| Salt spray (25 um) | 300-600 hrs | 300-600 hrs | YES |

### EN-B vs. EN-P vs. Hard Chrome Comparison Table (Zone 4)

All values match the brief exactly. Confirmed correct.

### Header Tagline Check

> **FLAG 2 — Boron Range in Header (Line 83)**
>
> The orientation strip states: `EN-B coated surface (Ni-B alloy, 0.5-8% B)`. This spans both DMAB (0.5-3%) and borohydride (3-8%), which is technically correct as an overall range. However, the header tagline (line 76) states `700-850 HV as-plated` — this spans both variants combined. This is acceptable for a summary tagline but could imply a single bath achieves that full range. Minor — no change required but worth noting.

### Safety Content

NaBH4 flammability warning present (line 181). Correct and appropriately placed.

### Verdict: FLAG (2 non-critical flags)

---

## Cluster 2 — AN-02 Type III Hard Anodize (Poster 292)

**Source Brief:** Anodizing Clusters — Watson Research Brief, Cluster 2, Section 2.5
**CW File:** `Poster 292 — Hard Anodizing Main Tank Type III — Construction Workup.md`

### CRITICAL CHECK — Electrode Polarity

- **Parts labeled:** `ANODE (+)` (line 106) — **CORRECT**
- **Counter-electrodes labeled:** `CATHODE (-)` (line 112) — **CORRECT**

In anodizing, the workpiece IS the anode. This is correct.

### Bath Parameters

| Parameter | CW (Poster 292) | Brief (Section 2.5) | Match? |
|---|---|---|---|
| Electrolyte | H2SO4 | H2SO4 | YES |
| Concentration | 110-135 g/L (10-12% w/v, 15-18 oz/gal) | 110-135 g/L (10-12% w/v, 15-18 oz/gal) | YES |
| Temperature | 28-36 F (-2 to +2 C) | 28-36 F (-2 to +2 C) | YES |
| Current density | 24-36 ASF | 24-36 ASF | YES |
| Voltage | 40-75+ V | 40-75+ V | YES |
| Time | 60-120 min for 2.0 mil | 60-120 min for 2.0 mil | YES |
| Dissolved Al | < 15 g/L | < 15 g/L | YES |
| Cathode material | Lead or aluminum | Lead or aluminum | YES |

### Current Ramp Protocol

CW ramp sequence (lines 167-170) matches the brief's description (lines 406-411): start at 6-12 ASF, ramp to full CD over 5-15 min, hold at 24-36 ASF. Correct.

### Mixed Acid Variant (Alumilite 225/226)

| Parameter | CW | Brief | Match? |
|---|---|---|---|
| H2SO4 | 12% (132 g/L) | 12% (132 g/L) | YES |
| Oxalic acid | 1% (40-45 g/L) | 1% (40-45 g/L) | YES |
| Temperature | 28-36 F (-2 to +2 C) | 28-36 F (-2 to +2 C) | YES |

### Film Thickness vs. Time

All four thickness targets (1.0, 2.0, 3.0, 4.0 mil) match the brief (lines 424-428). Correct.

### Alloy Thickness Limits

Alloy ratings (6061 Excellent, 5052 Good, 7075 Fair, 2024 Difficult, Cast Not Recommended) match the brief (lines 326-330). Correct.

### Defect Table

All 6 defects (burning, cracking, powdery, non-uniform, delamination, pitting) align with the brief's defect table (lines 435-439) plus additional relevant defects. Correct.

### Verdict: PASS

---

## Cluster 3 — AN-04 BSAA (Poster 308)

**Source Brief:** Anodizing Clusters — Watson Research Brief, Cluster 4, Section 4.5
**CW File:** `Poster 308 — BSAA Anodizing Main Tank — Construction Workup.md`

### CRITICAL CHECK — Electrode Polarity

- **Parts labeled:** `ANODE (+)` (line 106) — **CORRECT**
- **Counter-electrodes labeled:** `CATHODE (-)` (line 111) — **CORRECT**

### Bath Parameters (Main Tank)

| Parameter | CW (Poster 308) | Brief (Section 4.5) | Match? |
|---|---|---|---|
| H2SO4 | 30-50 g/L (3-5% w/v) | 30-50 g/L (3-5% w/v) | YES |
| H3BO3 | 5-10 g/L (0.5-1% w/v) | 5-10 g/L (0.5-1% w/v) | YES |
| Temperature | 70-90 F (21-32 C) | 70-90 F (21-32 C) | YES |
| Voltage | Ramp from ~5V to 15V | Ramp from ~5V to 15V | YES |
| Current density | Max ~10 ASF average | Max ~10 ASF average | YES |
| Time | 20-30 min | 20-30 min | YES |
| Coating weight | 200-700 mg/ft2 | 200-700 mg/ft2 | YES |

### H2SO4 Concentration Check (Drew's note: Watson corrected to 40-100 g/L)

The main tank parameters in the CW use 30-50 g/L (line 131), which matches the brief's primary parameter table (line 668). However:

> **FLAG 3 — H2SO4 in Comparison Table (Line 211)**
>
> In Zone 5, the BSAA vs. Type I chemistry comparison table states: `H2SO4 40-100 g/L + H3BO3 5-10 g/L`. This value (40-100 g/L) does not match the main tank parameter strip in Zone 3 (30-50 g/L, line 131). The brief itself has the same inconsistency — the primary table says 30-50 g/L (line 668) while noting "some sources cite 60-100 g/L."
>
> Watson's correction of "H2SO4 should be 40-100 g/L" appears to have been applied to the comparison table but not to the main tank parameters.
>
> **My assessment:** The range of 40-100 g/L is too broad for a single poster parameter callout. The more useful approach is:
> - **Main tank parameters (Zone 3):** Keep 30-50 g/L as the "BAC 5632 typical" range — this is what Boeing's original process calls for.
> - **Comparison table (Zone 5):** If showing a broader industry range, state it as "30-100 g/L (varies by specification)" with a note that BAC 5632 uses the lower end.
>
> The current state (30-50 in Zone 3, 40-100 in Zone 5) is internally inconsistent within the same poster. Pick one approach and apply it consistently.

### Boric Acid Role Explanation

Zone 4 explanation of boric acid as a buffer that modifies electrolyte behavior without incorporating into the oxide is chemically accurate. Correct.

### Coating Weight Metrics

200-700 mg/ft2 per MIL-A-8625F Type IC. Correct.

### Verdict: FLAG (1 non-critical flag — internal inconsistency in H2SO4 concentration)

---

## Cluster 4 — AN-05 PAA (Poster 317)

**Source Brief:** Anodizing Clusters — Watson Research Brief, Cluster 5, Section 5.5
**CW File:** `Poster 317 — Anodize PAA — Construction Workup.md`

### CRITICAL CHECK — Electrode Polarity

> **FLAG 4 — CRITICAL: Workpiece Labeled as CATHODE (Line 104)**
>
> Line 104 reads: `CATHODE (WORKPIECE)`
>
> **This is WRONG.** In anodizing — ALL anodizing, including PAA — the workpiece is the ANODE. The workpiece is connected to the positive terminal of the DC power supply. The aluminum is oxidized (loses electrons) at the anode, forming aluminum oxide. That is the entire point of the process. The word "anodizing" literally means "making it the anode."
>
> The counter-electrodes (stainless steel or carbon, lines 107-110) are not labeled with a polarity but are described as "counter-electrodes," which is ambiguous but not explicitly wrong. However, the workpiece being called "CATHODE" is a critical factual error that must be corrected before generation.
>
> **Required correction:**
> - Line 104: Change `CATHODE (WORKPIECE)` to `ANODE (WORKPIECE)` or `ANODE (+) — WORKPIECE`
> - Counter-electrodes: Label as `CATHODE (-)` for clarity
>
> This is the same error that was caught and fixed in Poster 301. It must not appear on a printed poster.

### Bath Parameters

| Parameter | CW (Poster 317) | Brief (Section 5.5) | Match? |
|---|---|---|---|
| Electrolyte | H3PO4 100-120 g/L (10-12% w/v) | 100-150 g/L; BAC 5555 ~12% | ACCEPTABLE — CW is tighter range, within brief's bounds |
| Temperature | 20-25 C (68-77 F) | 70-100 F (21-38 C) | CW is tighter — acceptable for BAC 5555 |
| Voltage | 10-15V; BAC 5555: 10V +/-1V | 15-25V | SEE NOTE |
| Current density | 0.5-1.5 A/dm2 (5-15 ASF) | 5-8 ASF | CW is slightly wider but acceptable |
| Time | 20-25 min | 20-25 min | YES |

**Voltage note:** The CW states 10-15V with BAC 5555 at 10V +/-1V (lines 119-120, 165). The brief states 15-25V (line 771). The CW's value is more specific to BAC 5555 — the Boeing spec does call for approximately 10V. The brief's 15-25V range is broader and includes non-BAC specifications. Both are defensible depending on scope. Since this is a PAA poster and BAC 5555 is the dominant specification, the CW's approach of leading with 10-15V and calling out BAC 5555 specifically is actually the better choice. No correction needed.

### Pore Morphology

Whisker height 10-50 nm, open pores, total oxide 0.5-1.5 um. Consistent with published PAA literature (ASTM D3933, BAC 5555). Correct.

### Oxide Thickness

CW: 0.5-1.5 um (line 30, line 168). Brief: 0.01-0.04 mil (0.3-1.0 um) in the overview (line 720), but 0.5-1.5 um is within the broader range seen in practice. Acceptable — the CW's range is reasonable for production PAA.

### Counter-Electrode Material

CW states "stainless steel or carbon" with a note "(NOT aluminum — dissolves in H3PO4)" (lines 109-110). This is correct — aluminum counter-electrodes would dissolve in phosphoric acid and contaminate the bath.

### Bond Strength

CW states "> 40 MPa (6,000 psi)" (line 220). This is consistent with published PAA lap-shear bond strength data for structural adhesive joints. Correct.

### No-Seal Requirement

CW correctly states PAA is never sealed (line 183). Correct.

### Verdict: FLAG (1 CRITICAL flag — electrode polarity error)

---

## Cluster 5 — AN-06 Bright Anodizing (Poster 325)

**Source Brief:** Anodizing Clusters — Watson Research Brief, Cluster 6, Section 6.5
**CW File:** `Poster 325 — Anodize Bright Type II — Construction Workup.md`

### CRITICAL CHECK — Electrode Polarity

- **Parts labeled:** `BRIGHT-DIPPED PARTS (ANODE)` (line 87) — **CORRECT**
- **Counter-electrodes labeled:** `LEAD OR 6063 CATHODE` (line 90) — **CORRECT**

### Bath Parameters

| Parameter | CW (Poster 325) | Brief (Section 6.5 / Cluster 1 Section 1.7) | Match? |
|---|---|---|---|
| Electrolyte | H2SO4 150-200 g/L (15-20%) | 165-225 g/L (15-20% w/v) | CLOSE — see note |
| Temperature | 68-72 F (20-22 C) | 68-72 F (20-22 C) | YES |
| Current density | 12-18 ASF (1.3-2.0 A/dm2) | 12-18 ASF (1.3-2.0 A/dm2) | YES |
| Voltage | 15-21V | 15-21V | YES |
| Time | 15-25 min (thin for clarity) | Per Type II; bright-specific: thin | YES |
| Target thickness | 0.2-0.5 mil (5-12 um) | 0.2-0.5 mil | YES |
| Dissolved Al | < 20 g/L | < 20 g/L (per Type II table, line 235) | YES |

**H2SO4 concentration note:** The CW states 150-200 g/L. The brief's Type II table (line 229) states 165-225 g/L. The CW's lower bound of 150 g/L is slightly below the brief's 165 g/L. In practice, bright anodize shops sometimes run on the slightly dilute side to reduce dissolution rate and preserve clarity, so 150 g/L is defensible. This is a very minor difference and not worth flagging for a poster.

### Bright-Specific Notes

- Coating kept thin for optical clarity: YES, correctly stated (lines 31, 100, 144)
- Temperature control tighter than standard Type II: YES, correctly stated (line 140)
- Clear anodize over bright dip = "bright clear": YES, correctly stated (line 120)

### Thickness vs. Clarity Table

The thickness/clarity relationships in Zone 6 (lines 187-193) are consistent with published bright anodize practice:
- 0.2 mil: excellent clarity — correct
- 0.5 mil: good clarity — correct
- 0.7 mil: slight haze — correct
- 1.0 mil: visible cloudiness — correct

These are accurate characterizations.

### Defect Table

All 6 defects (haze, burning, soft oxide, streaking, pitting, color variation) are relevant and accurate for bright anodize operations. Correct.

### Verdict: PASS

---

## Action Items

### MUST FIX BEFORE GENERATION

1. **Poster 317 (PAA), line 104:** Change `CATHODE (WORKPIECE)` to `ANODE (+) — WORKPIECE`. Label counter-electrodes as `CATHODE (-)`. This is a critical factual error.

### RECOMMENDED CORRECTIONS

2. **Poster 276 (EN-B), lines 121 and 165:** Revert deposition rates to Watson brief values (DMAB: 8-15 um/hr, NaBH4: 15-25 um/hr) unless a specific published source supports the higher values. The CW's current values (10-20 and 20-30) are on the high side of published EN-B data.

3. **Poster 308 (BSAA), lines 131 and 211:** Resolve the internal inconsistency — Zone 3 says H2SO4 30-50 g/L while Zone 5 comparison table says 40-100 g/L. Recommend keeping 30-50 g/L as the BAC 5632 primary range and noting the broader industry range parenthetically in the comparison table if desired.

### NO ACTION NEEDED

4. **Poster 292 (Type III):** All parameters verified. Electrode polarity correct. No flags.
5. **Poster 325 (Bright Anodize):** All parameters verified. Electrode polarity correct. No flags.

---

*Tyler — Plating Chemist*
*Validation Report — Batch 4b*
*2026-04-27*
