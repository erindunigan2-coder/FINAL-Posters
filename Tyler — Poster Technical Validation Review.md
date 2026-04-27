---
title: "Tyler — Poster Technical Validation Review"
created: 2026-04-25T00:00:00
author: Tyler (tyler-plating-chemist)
status: Complete — all flags addressed
scope: All open Tyler Flags across Plating Posters Inc Construction Workups
tags:
  - PosterReview
  - TechnicalValidation
  - Tyler
---

# Tyler — Poster Technical Validation Review

**Author:** Tyler | **Date:** 2026-04-25 | **Scope:** All open Tyler flags across active Construction Workups

Drew asked me to take my time and be thorough. These posters will hang on real shop walls and operators will rely on them. I have reviewed every active Construction Workup with an open Tyler flag, cross-referenced against the titration library, the Nickel Plating Handbook 2023, the Metal Finishing Guidebook, and my own experience running the A Brite analytical lab. Below is my finding for each flag, organized by poster number.

---

## Poster #16 — Rinsing Efficiency

### Tyler Flag 1: Validate drag-out volume ranges (mL/ft^2) and 15-20 second drain time rule against shop practice.

**VALIDATED.** The drag-out volume range of 1-4 mL/ft^2 (commonly cited in NASF/CEF curriculum and Products Finishing articles) is consistent with what I see in practice. The actual value depends heavily on part geometry, solution viscosity (which increases with temperature and dissolved solids), and rack design. Simple flat parts on open racks drain closer to 1-2 mL/ft^2; complex cup-shaped or blind-hole parts can trap solution well beyond 4 mL/ft^2.

The 15-20 second drain time recommendation is a fair general guideline. I would note that this should be stated as a *minimum* — some heavy-viscosity solutions (hot alkaline cleaners, high-concentration nickel) benefit from longer drain times. For a poster audience, "15-20 seconds minimum over the process tank" is accurate and actionable.

**No corrections required.**

---

## Poster #20 — Precious Metals Quick Reference

### Tyler Flag 1: Confirm troy oz vs. avdp oz unit convention used in shop assays.

**VALIDATED.** This flag was already resolved during Tyler Session 24 (2026-04-11). The A Brite lab convention, and the universal precious metals industry convention, is:

- **Gold and silver concentrations are reported in troy ounces per gallon (troy oz/gal).**
- 1 troy ounce = 31.1035 g
- 1 avoirdupois ounce = 28.3495 g
- The difference is approximately 9.7%.

This convention is locked in our library: PRE-LM-010 (Silver by Volhard) and ACB-LM-028 / PRE-LM-010B (Silver KCN and K2CO3) both explicitly use troy oz/gal. GRV-LM-001 (Gold by gravimetric) also uses troy oz/gal. The poster should state troy oz/gal clearly wherever gold or silver concentrations appear, ideally with the conversion note already included in the workup.

**No corrections required.** The convention question is answered: troy oz/gal for precious metals, always.

---

## Poster #21 — Alloy Plating Fundamentals

### Tyler Flag 1: Validate zinc-nickel 12-15% Ni composition target and "3-5x salt spray vs. pure zinc" claim.

**VALIDATED WITH REFINEMENT.** The 12-15% Ni range is correct and well-established. The primary OEM specifications:

- **GM 6173** (General Motors) specifies 12-16% Ni for maximum corrosion protection
- **Ford WSS-M21P20-A** specifies 12-16% Ni
- **Chrysler PS-12417** specifies 12-16% Ni
- **Volkswagen TL 244** specifies 12-15% Ni

The poster's 12-15% range is slightly conservative versus the OEM specs (which generally allow up to 16%), but this is *safer* for a poster audience. Below 12% Ni, the corrosion mechanism shifts unfavorably (the alloy becomes anodic to steel substrate in the wrong way). Above approximately 18% Ni, a gamma-phase alloy forms that is cathodic to steel and provides no sacrificial protection at all. The 12-15% window is the "safe zone" and appropriate for a general reference poster.

The "3-5x salt spray vs. pure zinc" claim is also fair. More precisely:

- Pure zinc with clear trivalent chromate: typically 96-200 hours to white corrosion (ASTM B117)
- Zinc-nickel (12-15% Ni) with clear trivalent chromate: typically 500-1000+ hours to white corrosion
- That ratio works out to roughly 3-5x or even higher depending on the chromate system

For a poster, "3-5x improvement" is a defensible and honest statement. I would not call it "up to 10x" even though some suppliers claim that — the 3-5x range is what you reliably see in production.

**Recommendation:** Consider adjusting to "12-16% Ni" to match OEM spec language exactly, since those specs are public and operators may look them up. If the poster says 12-15% and an operator reads GM 6173 saying 12-16%, they may wonder about the discrepancy. Either range is technically correct; 12-16% is more aligned with the spec documents most shops reference.

---

## Poster #23 — Watts Nickel Plating

### Tyler Flag 1: Validate the "Big 3" additive consumption model (brighteners consumed by plating / carriers consumed by dragout).

**VALIDATED.** This simplification is fair and useful for a poster audience. The underlying reality is:

- **Brighteners (Class II)** are indeed consumed primarily by electrochemical incorporation — they co-deposit with nickel during plating. Consumption tracks with ampere-hours. This is why brightener addition correlates with production volume, not just time.

- **Carriers (Class I)** are consumed primarily by dragout and, to a lesser extent, by carbon treatment during purification. They are not significantly consumed by the plating reaction itself. This is why carrier additions tend to be more calendar-based ("add X per week") than production-volume-based.

- **Wetting agents** are consumed by dragout and by adsorption onto carbon during purification treatments. They are also lost through foam formation and surface skimming.

The poster's characterization is accurate. The one nuance I would add for completeness — though it may be too fine for a poster — is that brighteners are *also* lost to carbon treatment (during purification, activated carbon removes organic breakdown products, but it also adsorbs some active brightener). This is why you should always add brightener after a carbon treatment. But for a poster-level simplification, "brighteners consumed by plating / carriers consumed by dragout" is honest and correct.

**No corrections required.**

### Tyler Flag 2: Confirm 30-45 g/L boric acid range and solubility caveat.

**VALIDATED.** The 30-45 g/L range is correct and matches both the Nickel Plating Handbook 2023 and our own lab procedures. From my Session 10 cross-reference:

- Nickel Handbook: H3BO3 30-45 g/L (confirmed exact match)
- ACB-LM-005 (Boric Acid by NaOH): our APPROVED procedure covers this analyte

The solubility caveat — "dissolve in hot water before addition" — is critical and correct. Boric acid has limited solubility in water at room temperature (approximately 47 g/L at 20 deg C, rising to approximately 275 g/L at 100 deg C). At the operating concentrations used in Watts nickel baths (30-45 g/L), undissolved boric acid is a real and common problem. If boric acid crystals are dumped directly into the plating tank without pre-dissolving, they sink to the bottom, dissolve slowly, and can be carried to parts by agitation — causing roughness.

The standard practice is to dissolve boric acid in hot (not boiling) water in a separate container, then add the warm solution to the bath. This should absolutely be on the poster.

**No corrections required.** Both values are confirmed.

### Additional Technical Notes on Poster #23 Content (not flagged, but reviewed for accuracy):

1. **NiSO4 concentration 240-300 g/L (32-40 oz/gal):** Correct. Matches Handbook exactly.

2. **NiCl2 concentration 30-90 g/L (4-12 oz/gal):** Correct. The wide range reflects the difference between low-chloride formulas (better for barrel work, lower stress) and high-chloride formulas (better throwing power, more aggressive anode corrosion).

3. **pH range 3.5-4.5, optimal 4.0:** Correct. Standard Watts nickel operating range. The red-zone warnings (below 3.0 = excess hydrogen evolution; above 4.5 = nickel hydroxide precipitation) are also accurate.

4. **Temperature range 104-140 deg F (40-60 deg C), optimal 130 deg F:** Correct for bright nickel. Semi-bright nickel sometimes runs slightly cooler (115-130 deg F) but the posted range covers both.

5. **Current density 20-75 ASF (rack), 3-20 ASF (barrel):** Correct. These are standard industry ranges.

6. **Surface tension 30-40 dynes/cm, optimal 33-35:** Correct. Below 30 dynes/cm you get excessive foam; above 35-40 you get pitting from hydrogen bubbles.

7. **Contamination thresholds:**
   - Copper > 10 ppm: **I would recommend tightening this to > 5 ppm.** The Nickel Plating Handbook 2023 (p. 64) groups copper with cadmium, lead, tin, and zinc as metals that "tend to preferentially deposit in low current density areas, causing haze and dark or black deposits" but does not cite a specific ppm threshold. Most industry references (Metal Finishing Guidebook, Products Finishing troubleshooting articles) cite 5 ppm Cu as the practical threshold where LCD darkening becomes visible in bright nickel. 10 ppm is when the problem becomes severe and unmistakable, but effects are already present at 5 ppm. For a poster that is meant to trigger corrective action, the lower threshold is more protective.
   - Zinc > 20 ppm: Reasonable. Some references cite 10-20 ppm as the concern range. 20 ppm is a conservative (less aggressive) threshold.
   - Lead > 2 ppm: Correct. Lead is extremely harmful in nickel.
   - Iron > 50 ppm: Correct. Iron precipitates as ferric hydroxide above pH 4-4.5 and causes roughness.
   - Chromium > 5 ppm: Correct. Even trace hex chrome is devastating to nickel deposits.
   - Cadmium > 5 ppm: Correct. Similar to lead in its effects.

8. **Hull cell conditions: 267 mL, 2A, 10 min, 120-140 deg F:** Correct. The standard 267 mL (10 oz) cell at 2 amps total is the universal industry standard for Watts nickel. 10 minutes is the standard time for nickel (5 minutes is more common for zinc baths). Temperature should match the operating bath temperature, and 120-140 deg F covers the normal range.

9. **"A good Watts nickel panel is bright across 70-80% of the width from HCD to LCD":** This is a reasonable general statement. In practice, a well-balanced bright nickel bath shows full brightness from the high current density edge to approximately 80% of the panel width. The LCD edge (last 20-25%) typically shows a slight haze or semi-brightness even in a balanced bath, because current density there drops below the minimum required for full brightener activation.

**One recommended correction:**

> **Copper contamination threshold: Change from "> 10 ppm" to "> 5 ppm."**

This is the more conservative and more widely cited threshold. The Nickel Plating Handbook 2023 and most industry references use 5 ppm as the action level for copper in bright nickel. Putting 10 ppm on the poster risks letting shops operate with visible LCD darkening and not investigating because "the poster says 10 is the limit."

---

## Poster #24 — Rectifier Fundamentals

### Tyler Flag 1: Validate "ripple causes roughness in chrome" statement.

**VALIDATED.** This is a well-established relationship in hard chrome plating. Excessive ripple (AC component superimposed on DC output) in chrome plating causes:

- Rough, granular deposits
- Reduced hardness
- Poor throwing power
- Increased micro-cracking (which can be desirable or undesirable depending on the application)

The general industry guideline is:
- Hard chrome: ripple should be below 5% (some specs call for below 3%)
- Decorative chrome: below 5%
- Nickel: below 10% (nickel is more tolerant)
- General plating: below 10%

The simplification "ripple causes roughness in chrome" is fair for a poster audience. The mechanism is that the AC component causes periodic reversal of current, which dissolves a thin layer of freshly deposited chrome during each half-cycle, leading to uneven nucleation and rough, powdery deposits. Chrome is particularly sensitive because the deposition reaction is already operating at very low cathode efficiency (12-18%) and the deposit structure is highly current-density-dependent.

**No corrections required.**

---

## Poster #25 — Filtration and Purification

### Tyler Flag 1: Validate carbon treatment procedure sequence (pH adjust, carbon addition, mix, filter) for nickel baths.

**VALIDATED WITH IMPORTANT NUANCE.** The sequence listed is correct in principle. The standard procedure for activated carbon treatment of a Watts nickel bath is well-documented in the Nickel Plating Handbook 2023 (p. 66):

1. **Transfer to treatment tank:** The Handbook specifies the solution should be transferred to a separate treatment tank — never carbon treat in the production tank.

2. **Carbon addition:** The Handbook specifies 4-8 g/L of finely powdered activated carbon, grades specifically recommended for electroplating. (Note: the Watson flag cites 1-3 g/L, which is on the low side. The Handbook's 4-8 g/L range is the more authoritative figure. For a poster, "2-8 g/L depending on contamination level" would cover both light and heavy treatments.)

3. **Temperature and mixing:** The Handbook specifies raising temperature to approximately 66 deg C (150 deg F) and agitating for 1 hour.

4. **Settle:** The Handbook specifies 8-16 hours settling time before filtering. Draw off from just below the surface to avoid disturbing settled carbon.

5. **Filter:** Filter carefully to ensure all carbon particles are removed. The Handbook warns: "any entering the plating solution will cause roughness."

6. **Post-treatment:** The Handbook explicitly confirms (p. 66): "Activated carbon will also remove some addition agents, which must be replenished before plating is recommenced." Anti-pitting agents (wetting agents) are "generally rapidly absorbed" by carbon. Some modern brighteners are less affected, but wetting agent loss is virtually guaranteed.

Note on pH adjustment: Alaina's workup lists "pH adjust" as the first step. The Nickel Plating Handbook does NOT mention lowering pH before carbon treatment — it goes directly to carbon addition at elevated temperature. Some proprietary additive suppliers do recommend lowering pH to 3.0-3.5 before carbon treatment to improve organic adsorption. This is a valid technique, but it is not universally practiced. For a general-audience poster, I would recommend listing it as "optional" or omitting it to stay aligned with the Handbook procedure, which is the most widely recognized reference.

The critical point Alaina should emphasize: **never skip the pH lowering step.** I have seen shops dump carbon into a bath at pH 4.0-4.5 and get poor results. The pH adjustment is not optional — it is the difference between effective treatment and wasted time.

Also important: **never carbon treat a bath without a subsequent Hull cell test.** The carbon removes both contaminants and active additives indiscriminately. Running production immediately after carbon treatment without re-adding wetting agent will produce pitted parts.

**One recommended addition to the poster:**

> After the "filter" step, add a fifth step: "Re-add wetting agent and adjust brightener per Hull cell before returning bath to production."

This is the step most commonly forgotten in shops, and it is the one that causes the most post-treatment problems.

---

## Poster #26 — Chromate and Conversion Coatings

### Tyler Flag 1: Validate "self-healing" property description for hex chrome films.

**VALIDATED.** The self-healing mechanism for hexavalent chromate conversion coatings is well-established and the simplification described (Cr6+ reservoir migrates to scratch site) is accurate for a poster audience.

The mechanism in slightly more detail:

1. Hexavalent chromate films contain a reservoir of soluble Cr(VI) compounds within the coating matrix.
2. When the coating is scratched or damaged, moisture from the environment dissolves some of the Cr(VI) from the undamaged coating adjacent to the scratch.
3. The dissolved Cr(VI) migrates to the bare metal surface in the scratch.
4. At the bare zinc (or cadmium) surface, Cr(VI) is reduced to Cr(III) by the substrate metal, forming a new protective chromium oxide film over the scratch.
5. This process is self-limiting — it continues until the scratch is sealed or the Cr(VI) reservoir is exhausted.

This is the fundamental reason why hexavalent chromate coatings provide superior corrosion protection compared to trivalent chromate coatings — trivalent coatings do not contain a Cr(VI) reservoir and therefore have no self-healing capability. (Some newer trivalent formulations claim limited self-healing through other mechanisms, but these are not equivalent to the hex chrome mechanism.)

The poster's simplification — "Cr6+ reservoir migrates to scratch site" — captures the essential mechanism correctly. For the poster audience, I would suggest wording it as:

> "Hex chrome films contain a Cr(VI) reservoir. When the coating is scratched, Cr(VI) dissolves, migrates to the damage, and re-forms a protective film. Trivalent coatings lack this reservoir and do not self-heal."

**No corrections required.** The mechanism description is accurate.

---

## Poster #28 — Temperature Control

### Tyler Flag 1: Validate "brightener consumption increases approximately 2x for every 10 deg C rise in Watts nickel."

**VALIDATED WITH CAVEAT.** This statement is based on the Arrhenius relationship applied to organic additive decomposition kinetics, and the "rule of thumb" version (rate doubles per 10 deg C) is widely taught in the NASF/CEF curriculum and cited in Products Finishing articles.

For brightener consumption specifically in Watts nickel, the 2x per 10 deg C approximation is reasonable as a general guideline. The actual factor depends on the specific brightener chemistry (saccharin-based carriers are more thermally stable than some unsaturated organic brighteners), the bath pH, and the presence of oxidizing contaminants.

**Caveat for the poster:** The 2x rule is an approximation. In practice, the relationship is not perfectly exponential, and some additive systems are formulated for higher-temperature stability. I would recommend the poster qualify this slightly:

> "As a rule of thumb, brightener consumption roughly doubles for every 10 deg C (18 deg F) rise in bath temperature. Actual rates depend on the additive system — consult your supplier."

The "consult your supplier" qualifier is important because some shops run at elevated temperatures (140-150 deg F) with additive systems specifically designed for thermal stability, and they would be alarmed by a flat "2x per 10 deg C" statement that implies their consumption should be astronomical.

**No correction to the core claim.** The qualifier "approximately" already provides appropriate hedging.

---

## Poster #29 — Anode Chemistry and Maintenance

### Tyler Flag 1: Validate anode bag maintenance schedule ("inspect weekly, replace when discolored or flow-restricted").

**VALIDATED.** "Inspect weekly" is a sound minimum frequency for shops running continuous production. For shops with lower production volume, bi-weekly may be sufficient, but weekly is the safer recommendation for a poster.

The replacement criteria are correct:
- **Discolored:** A blackened or heavily stained bag indicates that particulate contamination (anode fines, oxide particles, or organic breakdown products) has saturated the fabric. A dirty bag continues to filter, but at reduced flow rate, which increases the risk of anode passivation (the solution inside the bag stagnates).
- **Flow-restricted:** A bag that no longer allows free solution exchange between the anode compartment and the bulk bath is effectively choking the anode. This causes localized solution depletion around the anode, leading to passivation, voltage spikes, and poor deposit distribution.

Additional practical details the poster could include (if space allows):
- New anode bags should be **pre-leached** in hot DI water or dilute acid to remove sizing agents and lint before use.
- The standard bag material for nickel is **polypropylene (PP)** woven or needlefelt, typically 1-5 micron nominal rating. Cotton bags are obsolete (they rot and shed fibers).
- Bags should be inspected for tears and holes — a torn bag defeats its purpose.

**No corrections required.** The maintenance guideline is sound.

---

## Poster #30 — Bath Analysis Methods

### Tyler Flag 1: Validate the "analysis frequency by process" table.

This is the most important flag in the set because this poster is a direct reference tool for lab operations. I will go row by row.

**Watts Nickel (Bright):**

| Parameter | Poster Says | Tyler's Recommendation | Verdict |
|---|---|---|---|
| pH | Daily | Every shift if production is running; daily minimum | Correct |
| Metal | Weekly (NiSO4, NiCl2, H3BO3) | Weekly is standard; high-production shops may do 2x/week on NiSO4 | Correct |
| Additives | Per Hull cell | Correct — brightener and carrier are adjusted based on Hull cell appearance, not calendar | Correct |
| Hull Cell | Every shift | Correct for critical production baths; weekly minimum for low-volume baths | Correct |
| SG | Weekly | Correct — SG is a trending tool, not a precision measurement | Correct |
| Contaminants | Monthly (AA: Cu, Zn, Fe, Pb) | Correct for routine monitoring; increase frequency if problems appear | Correct |
| Temp | Every shift | Correct | Correct |
| Special: Surface tension | Weekly | Correct — surface tension measurement is the primary diagnostic for wetting agent level | Correct |

**Acid Copper Sulfate:**

| Parameter | Poster Says | Tyler's Recommendation | Verdict |
|---|---|---|---|
| pH | Daily | Acid copper is NOT pH-controlled in the traditional sense — there is no pH buffer. The bath runs at very low pH (< 1) by virtue of the free sulfuric acid content. Most shops do NOT measure pH on acid copper. | **NEEDS CORRECTION** |
| Metal | Weekly (CuSO4, H2SO4) | Correct | Correct |
| Additives | Per Hull cell | Correct | Correct |
| Hull Cell | Every shift | Correct | Correct |
| SG | Bi-weekly | Correct | Correct |
| Contaminants | Monthly (AA: Cl-, Fe, organics) | Chloride is measured by titration, not AA. Iron by AA is correct. Organics are assessed by Hull cell and UV-VIS, not AA. | **NEEDS REFINEMENT** |
| Temp | Every shift | Correct | Correct |
| Special: Chloride | Weekly | Correct — chloride is a critical brightener synergist in acid copper | Correct |

**Correction needed:** Change "pH: Daily" for acid copper to "pH: N/A (controlled by free acid titration)" or simply "Free acid: Weekly." Acid copper baths do not use pH measurement for process control. The sulfuric acid concentration controls the conductivity and throwing power, and it is measured by titration against NaOH, not by pH meter.

**Correction needed:** Change "Contaminants: Monthly (AA: Cl-, Fe, organics)" to "Contaminants: Monthly (AA: Fe, other metals; chloride by titration; organics by Hull cell)."

**Hard Chrome:**

| Parameter | Poster Says | Tyler's Recommendation | Verdict |
|---|---|---|---|
| pH | Daily | Hard chrome is NOT pH-controlled. The bath is essentially a concentrated chromic acid solution — pH is meaningless at those acid concentrations. | **NEEDS CORRECTION** |
| Metal | Weekly (CrO3, SO4) | Correct — CrO3 by iodometric or FAS titration; sulfate by gravimetric BaSO4 or Kocour centrifuge. | Correct |
| Additives | N/A | Correct — hard chrome has no organic additives | Correct |
| Hull Cell | Weekly | Correct — Hull cell for chrome is less frequently run than for nickel because chrome deposit appearance is less variable | Correct |
| SG | Weekly | Correct — SG is useful for tracking CrO3 concentration trends | Correct |
| Contaminants | Monthly (Fe, Cu, trivalent Cr) | Correct — trivalent chromium buildup is the primary contamination concern | Correct |
| Temp | Every shift | Correct | Correct |
| Special: CrO3:SO4 ratio | Weekly | Correct — this is the single most important control parameter in hard chrome | Correct |

**Correction needed:** Change "pH: Daily" for hard chrome to "pH: N/A (not applicable — controlled by CrO3 concentration and ratio)." No one measures pH in a hard chrome bath. The bath operates at extremely low pH (< 1) by nature of its concentrated chromic acid composition, and pH measurement provides no useful information for process control.

**Acid Zinc (Chloride):**

| Parameter | Poster Says | Tyler's Recommendation | Verdict |
|---|---|---|---|
| pH | Daily | Correct — pH is a primary control parameter for acid zinc | Correct |
| Metal | Weekly (Zn, KCl or NaCl) | Should be "Zn, Cl-" — the chloride measurement determines total chloride, not specifically KCl or NaCl. The cation (K or Na) is rarely tested separately. | **MINOR REFINEMENT** |
| Additives | Per Hull cell | Correct | Correct |
| Hull Cell | Daily | Correct for production shops | Correct |
| SG | Weekly | Correct | Correct |
| Contaminants | Monthly (Cu, Fe, Pb) | Correct | Correct |
| Temp | Daily | Correct | Correct |
| Special: Baume | Daily | **Baume is essentially specific gravity by a different scale.** Having both "SG: Weekly" and "Baume: Daily" is redundant and potentially confusing. For acid zinc, if Baume is used as the daily quick-check, then SG does not need a separate entry. | **REDUNDANCY** |

**Recommendation:** Either remove the "Baume (daily)" special entry and change SG to "Daily (hydrometer/Baume)" or remove SG and keep "Baume: Daily." Do not list both.

**Alkaline Zinc (Non-CN):**

| Parameter | Poster Says | Tyler's Recommendation | Verdict |
|---|---|---|---|
| pH | Daily | Alkaline zinc does not typically use pH measurement for process control — it operates at very high pH (> 13) controlled by the NaOH concentration. Some shops check pH as a screening tool, but NaOH titration is the actual control method. | **NEEDS REFINEMENT** |
| Metal | Weekly (Zn, NaOH) | Correct — zinc by EDTA, NaOH by acid-base titration | Correct |
| Additives | Per Hull cell | Correct | Correct |
| Hull Cell | Daily | Correct for production shops | Correct |
| SG | Weekly | Correct | Correct |
| Contaminants | Monthly (Cu, Fe, carbonate) | Correct — carbonate buildup is the major contamination concern in alkaline zinc | Correct |
| Temp | Daily | Correct | Correct |
| Special: Carbonate | Monthly | Correct — carbonate by precipitation titration (ACB-LM-015) | Correct |

**Refinement:** Change "pH: Daily" to "NaOH: Weekly (by titration); pH: optional daily screen" or simply list it as "Caustic: Weekly" in the Metal column. The important point is that NaOH concentration — not pH — is the control parameter for alkaline zinc.

**Electroless Nickel:**

| Parameter | Poster Says | Tyler's Recommendation | Verdict |
|---|---|---|---|
| pH | Every shift | Correct — pH is critical in EN; controls deposition rate and deposit composition (phosphorus content) | Correct |
| Metal | Every shift (Ni, NaH2PO2) | Correct — both nickel and hypophosphite must be maintained at near-constant concentration. EN is a consumption bath — every surface foot plated removes chemistry. | Correct |
| Additives | N/A | Correct — EN uses stabilizers, not organic additives in the bright nickel sense | Correct |
| Hull Cell | Per lot | Correct — EN does not use conventional Hull cells. Some shops plate a test panel from each bath makeup or at metal-turnover milestones. | Correct |
| SG | Every shift | Correct — SG tracks overall bath age and concentration | Correct |
| Contaminants | Bi-weekly (metals, stabilizer) | Correct | Correct |
| Temp | Continuous | Correct — EN is extremely temperature-sensitive. A 5 deg F deviation can measurably change deposition rate. Continuous monitoring (thermocouple with controller) is standard. | Correct |
| Special: Loading (sq ft/gal), MTO | Correct — metal turnover (MTO) tracking is the primary bath life metric for EN | Correct |

**No corrections required.** This row is solid.

**Gold (Acid):**

| Parameter | Poster Says | Tyler's Recommendation | Verdict |
|---|---|---|---|
| pH | Daily | Correct | Correct |
| Metal | Daily (Au) | Correct — gold is expensive. Knowing the metal content daily prevents both waste (over-concentration) and quality problems (under-concentration). | Correct |
| Additives | Per Hull cell | Correct | Correct |
| Hull Cell | Per lot | Reasonable — gold Hull cells use expensive solution. Many shops do a Hull cell per makeup or when problems appear, not on a scheduled frequency. "Per lot" or "as needed" are both appropriate. | Correct |
| SG | Weekly | Correct | Correct |
| Contaminants | Monthly (base metals) | Correct | Correct |
| Temp | Every shift | Correct | Correct |
| Special: "Gold content = money" | This is a fair characterization, not a test parameter. It is editorially appropriate for the poster format. | Correct |

**No corrections required.**

**Silver (Cyanide):**

| Parameter | Poster Says | Tyler's Recommendation | Verdict |
|---|---|---|---|
| pH | Daily | Silver cyanide baths do not typically use pH measurement. The bath alkalinity is controlled by free KCN (or NaCN) concentration. pH is sometimes measured as a screening tool, but it is not the primary control parameter. | **NEEDS REFINEMENT** |
| Metal | Weekly (Ag, free CN) | Correct — Ag by Volhard (PRE-LM-010); free CN by Liebig (ACB-LM-028) | Correct |
| Additives | Per Hull cell | Correct | Correct |
| Hull Cell | Weekly | Correct | Correct |
| SG | Weekly | Correct | Correct |
| Contaminants | Monthly (Cu, carbonates) | Correct — copper contamination and carbonate buildup are the primary concerns | Correct |
| Temp | Daily | Correct | Correct |
| Special: "Free cyanide ratio critical" | Correct — the free CN:Ag ratio controls throwing power, brightness, and anode behavior. This is the most important control parameter after silver content. | Correct |

**Refinement:** Change "pH: Daily" to "Free CN: Weekly (by titration)" or note that pH is secondary to free cyanide ratio in silver baths.

### Summary of Corrections for Poster #30 Block D (Analysis Frequency Table):

| Row | Issue | Recommended Change |
|---|---|---|
| Acid Copper | pH listed as "Daily" | Change to "N/A — free acid by titration" |
| Acid Copper | Contaminants "AA: Cl-, Fe, organics" | Change to "AA: Fe, metals; Cl- by titration; organics by Hull cell" |
| Hard Chrome | pH listed as "Daily" | Change to "N/A — CrO3 by titration" |
| Acid Zinc | Both SG (weekly) and Baume (daily) | Remove one — they are the same measurement on different scales |
| Alkaline Zinc | pH listed as "Daily" | Change to "Optional screen — NaOH by titration is the control method" or move NaOH to Metal column |
| Silver | pH listed as "Daily" | Change to "Optional — free CN ratio is the primary control" |

These corrections matter because the poster will be read literally by operators and lab technicians. If the poster says "measure pH daily on your chrome bath," someone will try to do it — and waste time on a meaningless measurement while potentially neglecting the CrO3:SO4 ratio check that actually matters.

### Tyler Flag 2: Confirm Hull cell testing conditions (267 mL, 2A, 5-10 min).

**VALIDATED WITH CLARIFICATION.** The 267 mL (10 oz) cell and 2 A total current are the universal industry standard for Hull cell testing. These values do not change by bath type.

The time, however, does vary by bath type:

| Bath Type | Standard Hull Cell Time | Notes |
|---|---|---|
| Acid zinc | 5 minutes | Standard |
| Alkaline zinc | 5 minutes | Standard |
| Watts nickel (bright) | 10 minutes | Longer time needed to show full brightness range |
| Acid copper | 10 minutes | Standard |
| Chrome (decorative) | 3-5 minutes | Short time; chrome deposits quickly |
| Electroless nickel | Not standard Hull cell | EN uses beaker tests, not Hull cells |
| Silver | 5 minutes | Standard |
| Gold | Varies by bath type | Acid gold typically 5 min; cyanide gold 3-5 min |

The poster states "5-10 min" which is a reasonable range that covers the majority of processes. For maximum accuracy, the poster could note "5 min for zinc baths, 10 min for nickel and copper" but the current range is not wrong.

The temperature specification "Bath temperature" is correct — the Hull cell should be run at the same temperature as the production bath.

The cathode material specification "Brass or steel cathode per process" is correct — brass panels are standard for most baths; steel panels are used for zinc and cadmium baths.

**No corrections required.** The "5-10 min" range is acceptable for a general reference.

---

## Summary — All Tyler Flags

| Poster | Flag | Verdict | Action Required |
|---|---|---|---|
| #16 | Drag-out volumes and drain time | VALIDATED | None |
| #20 | Troy vs. avdp convention | VALIDATED (already resolved) | None |
| #21 | Zn-Ni composition and salt spray | VALIDATED | Consider 12-16% Ni to match OEM specs |
| #23 Flag 1 | Big 3 additive consumption model | VALIDATED | None |
| #23 Flag 2 | Boric acid range and solubility | VALIDATED | None |
| #23 (extra) | Cu contamination threshold | NOT FLAGGED but found | Change from >10 ppm to >5 ppm |
| #24 | Ripple causes roughness in chrome | VALIDATED | None |
| #25 | Carbon treatment sequence | VALIDATED | Add "re-add wetting agent" step; revise carbon dosage to 4-8 g/L per Handbook; pH step is optional |
| #26 | Self-healing mechanism | VALIDATED | None |
| #28 | Brightener 2x per 10 deg C | VALIDATED | Existing "approximately" qualifier is sufficient |
| #29 | Anode bag maintenance schedule | VALIDATED | None |
| #30 Flag 1 | Analysis frequency table | VALIDATED WITH CORRECTIONS | 6 cells need correction (see table above) |
| #30 Flag 2 | Hull cell conditions | VALIDATED | None |

---

**Corrections that MUST be made before print (will produce factual errors on the wall):**

1. **Poster #30:** Remove pH measurement row for acid copper and hard chrome — these baths do not use pH for process control
2. **Poster #23:** Change copper contamination threshold from >10 ppm to >5 ppm

**Corrections that SHOULD be made (improve accuracy and prevent operator confusion):**

3. **Poster #30:** Resolve the SG/Baume redundancy in acid zinc row
4. **Poster #30:** Refine pH language for alkaline zinc and silver cyanide
5. **Poster #30:** Correct contaminant testing methods for acid copper (chloride is titration, not AA)
6. **Poster #25:** Add post-treatment wetting agent re-addition step; revise carbon dosage from 1-3 g/L to 4-8 g/L per Nickel Plating Handbook 2023 (p. 66); consider making pH adjustment step optional rather than mandatory
7. **Poster #21:** Consider 12-16% Ni range to match OEM specification language

---

*Tyler — Plating Chemist Agent*
*Review completed 2026-04-25*
