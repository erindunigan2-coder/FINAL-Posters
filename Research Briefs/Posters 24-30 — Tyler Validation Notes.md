---
title: "Posters 24-30 — Tyler Validation Notes"
date: 2026-04-25T00:00:00
author: Tyler (plating chemist)
scope: Shop-floor validation of Series 1 Posters 24-30
status: Complete
tags:
  - PosterValidation
  - Series1
  - Foundational
---

# Posters 24-30 — Tyler Validation Notes

**Reviewer:** Tyler | **Date:** 2026-04-25 | **Status:** Complete — v2 (thorough re-review)

These notes validate the technical content of Construction Workups for Posters #24 through #30 from a practicing lab chemist and shop-floor perspective. Every factual claim, parameter value, and process description has been evaluated. Findings are categorized as **Confirmed**, **Correction Needed**, or **Recommended Improvement**. Items requiring Watson source-verification are flagged separately.

Overall assessment: Alaina's workups are technically strong across the board. The corrections below are refinements, not overhauls. Poster #29 (Anode Chemistry) requires zero corrections. The most correction-intensive posters are #25 (carbon treatment procedure), #27 (precipitation pH and equation), and #30 (analysis frequency table).

Zero brand or supplier names found in any poster. All content is appropriately generic.

---

## Poster #24 -- Rectifier Fundamentals

### Confirmed

- Pulsed DC description: ion replenishment during T-off, finer grain, improved throwing power -- all correct and well stated.
- Periodic Reverse description: selective dissolution of HCD buildup is the accepted mechanism. "Exceptional for through-hole plating" is accurate (PR is the standard for PCB via plating).
- Unfiltered DC / ripple description: failed filter capacitors and degraded SCRs are the two most common causes of excessive ripple. Correct.
- Cathodic:Anodic ratio "typically 3:1 to 20:1" -- correct. Acid copper PCB work commonly runs 5:1 to 15:1; gold can run higher. The 3:1 to 20:1 envelope covers practical spread.
- Ripple formula: Ripple % = (Peak - Valley) / Avg x 100 -- correct (standard peak-to-peak ripple percentage).
- Duty cycle formula for pulse plating -- correct.
- PR charge ratio formula and "net deposition requires charge ratio > 1.0" -- correct.
- Application matrix: Watts nickel PR "No" with note about brightener system disruption -- correct. Bright nickel brightener systems are formulated for DC; PR would strip brightener selectively.
- Troubleshooting: "Ammeter reads high but plating thin -- stray current / ground fault" -- correct. One of the most misdiagnosed problems in plating.
- Maintenance: "Measure output ripple under full load (quarterly)" -- correct. Ripple at idle tells you nothing useful.
- Pulse plating benefits list (finer grain, better throwing power, reduced H embrittlement risk, lower internal stress, higher peak CD) -- all correct.
- PR benefits list (levels HCD/LCD, eliminates dog-boning, reduces nodules in hard chrome, deep recesses, can supplement thieves) -- all correct.
- "Ripple causes roughness in chrome" (Tyler flag from Alaina): Confirmed as a fair simplification. Ripple in chrome causes roughness, burning, and hazy deposits depending on magnitude and CD. For a poster audience, this is adequate.

### Corrections Needed

1. **Straight DC description -- "Constant voltage and current"**
   - **Problem:** A rectifier operates in either constant current OR constant voltage mode, not both simultaneously. In electroplating, we almost always run constant current (amperage control).
   - **Correction:** Change to: "Steady, uninterrupted current flow. The standard power mode for most plating baths. Simple, reliable, and well-understood."
   - **Priority:** Medium

2. **Ripple threshold zones -- Green 0-5%, Yellow 5-15%, Red >15%**
   - **Problem:** The yellow and red thresholds are too generous. At 15% ripple, most baths are already producing defects. Industry consensus for chrome and bright nickel is below 5%, with many specifications calling for less than 3%.
   - **Correction:** Green: 0-5% (add note "Chrome and bright Ni: target less than 3%"). Yellow: 5-10%. Red: greater than 10%.
   - **Priority:** High

3. **Hard chrome pulse -- "Pulse improves microcracking"**
   - **Problem:** Pulse chrome remains genuinely experimental in most production shops as of 2026. The microcracking claim applies to certain proprietary pulse-chrome processes but is not a general statement.
   - **Correction:** Soften to: "may improve microcrack density in specialized processes." Leave "Emerging" rating unchanged.
   - **Priority:** Low

### Recommended Improvements

- The characteristics strip listing "Grain size: Standard / Finer / Finest / Coarse" for each waveform is a good comparative framework but could mislead operators into thinking pulse always produces finer grain than DC. Add a qualifier: "relative to DC at equivalent average current density."

### Items for Watson

- **Tin whisker / PR claim** ("PR reduces whisker risk in some alloys"): This is an area of active research. Some published work supports it via stress reduction, but I would not state it as settled fact. Watson should source-check against current literature. If unsourced, soften to "may help reduce whisker risk -- under investigation."

---

## Poster #25 -- Filtration and Purification

### Confirmed

- Turnover rates: Watts nickel min 3 target 5, hard chrome min 2 target 3, EN min 3 target 5, gold/precious min 3 target 5 -- all correct per standard supplier recommendations and the Nickel Plating Handbook.
- Filter media descriptions: depth vs. pleated cartridge distinction, bag filter 1-200 micron range, carbon canister for organic removal -- all correct.
- Micron rating strip: 1 micron for fine Ni/Cr, 5 micron standard, 10-25 micron for acid copper/barrel, >25 for coarse pre-filtration -- correct.
- Sizing formula: GPM = Tank volume (gal) x turnovers/hr / 60 -- dimensionally consistent and correct.
- Dummy plating parameters: 2-5 ASF, corrugated mild steel cathode, 4-24 hours -- standard practice.
- "Filter media must be compatible with cyanide" for gold/precious -- important and correct (PP is standard for cyanide baths).
- Permanganate treatment description -- correct.
- Hydrogen peroxide treatment for Fe2+ to Fe3+ -- correct.
- Freezing for carbonate removal in alkaline zinc -- correct.
- Maintenance: "Do NOT run on a calendar -- run on pressure differential" -- excellent advice, correct.

### Corrections Needed

4. **Carbon treatment pH for nickel -- "Raise pH to 4.5-5.0"**
   - **Problem:** The effective range for carbon adsorption of organic breakdown products in Watts nickel is pH 5.0-5.5. At pH 4.5, carbon is measurably less effective.
   - **Correction:** Change to "Raise pH to 5.0-5.5 (nickel) or per supplier guidance."
   - **Priority:** High

5. **Carbon contact time -- "Stir thoroughly for 30-60 minutes"**
   - **Problem:** 30 minutes is often insufficient for heavy organic loading. Standard practice is 1-2 hours of contact time with agitation. Some shops run overnight.
   - **Correction:** Change to "Stir thoroughly for 1-2 hours minimum."
   - **Priority:** High

6. **Don't list -- "Don't leave carbon in solution longer than 1 hour"**
   - **Problem:** This contradicts the contact time recommendation (which already says 30-60 min) and is factually wrong. Carbon can remain in solution for several hours without harm. The real risk is returning the bath to service with unfiltered carbon particles, which cause severe roughness.
   - **Correction:** Rewrite to: "Don't return bath to service without removing ALL carbon by filtration."
   - **Priority:** High

### Recommended Improvements

- The "Removes: Cu, Zn, Pb, Cd (metals more noble than Ni at low CD)" note for dummy plating uses "more noble" as a simplification. Technically, it is the relative deposition potentials at low overpotential that matter, not electrochemical nobility per se. For the poster audience this is close enough -- no change needed, just noting the nuance.
- Consider adding "Electrodialysis" as a maintenance note for the advanced purification section: "requires operator training and membrane maintenance -- not a set-and-forget system."

---

## Poster #26 -- Chromate and Conversion Coatings

This poster received the most scrutiny given the Drew/Watson flag on trivalent/hexavalent accuracy.

### Confirmed

- Hex clear film thickness 0.05-0.25 micron -- correct per ASTM B633.
- Hex yellow film thickness 0.25-0.75 micron -- correct.
- Tri clear film thickness 0.05-0.25 micron -- correct.
- Tri black film thickness 0.5-1.5 micron -- correct.
- Hex clear SST 8-24 hours -- correct for Type II per ASTM B633.
- Hex yellow SST 96-500+ hours -- correct. 500+ achievable with thick yellow + sealer on quality zinc deposits.
- Tri black SST 96-400 hours -- correct as overall range.
- Self-healing mechanism: Cr6+ reservoir migrates to scratch site and re-forms barrier -- correct. This is the accepted mechanism.
- "Self-healing does not survive extreme abrasion or high-temperature baking" -- correct. Baking above 150 F converts soluble Cr(VI) to insoluble Cr(III), destroying the self-healing reservoir.
- Hex temperature 60-80 F wide window, Tri 70-85 F tighter -- correct.
- Hex immersion 15-60 sec, Tri 30-90 sec -- correct as generic ranges.
- Tri pH must be controlled within +/- 0.2 of target -- correct. This is one of the most important practical differences.
- "Hex degrades above 150 F (65 C)" -- correct. Standard industry threshold. This is why hydrogen embrittlement bake-out (375 F typical) far exceeds chromate degradation temperature.
- "Tri more heat-stable -- no Cr6+ to reduce" -- correct. Already in Cr(III) oxide state.
- Hexavalent mechanism description (Cr6+ reduced to Cr3+ at surface, mixed oxide gel film) -- correct.
- Trivalent mechanism description (Cr3+ precipitates as oxide/hydroxide film, no Cr6+ at any stage) -- correct.
- "Yellow NOT achievable without hex" -- correct. No trivalent chemistry produces a true yellow/iridescent appearance equivalent to hex yellow.
- OSHA PEL for Cr6+: 5 microg/m3 -- correct.
- RoHS/REACH timeline dates (2003, 2006, 2007, 2013, 2017, 2024+) -- all correct. Watson should still verify current exemption status as of 2026 per his own flag.
- "Avoid air agitation in hex (Cr6+ mist hazard)" -- correct and important safety note.
- "Nickel or iron drag-in poisons tri baths rapidly" -- correct.
- Common failures table (patchy film, film too thin, rainbow on clear, powdery film, color inconsistency, early white rust) -- all causes and fixes are accurate.

### Corrections Needed

7. **Tri clear SST -- "48-200 hrs"**
   - **Problem:** This range conflates with-sealer and without-sealer performance. Without sealer, tri clear on zinc typically achieves 24-96 hours to white rust. With sealer, 96-200+ hours.
   - **Correction:** Split into two lines: "Without sealer: 24-96 hrs. With sealer: 96-200+ hrs."
   - **Priority:** Medium

### Recommended Improvements

- In the comparison table, under "Torque tension": "Can vary -- test with fastener coatings" is accurate but could be strengthened. Torque-tension variability with trivalent chromates is a known issue in the fastener industry. Consider adding: "Tri passivates with sealers can shift torque-tension coefficients by 10-20% -- always re-qualify."
- The "Bath life" row ("Tri: shorter -- more sensitive to metallic drag-in, pH drift") is correct. Consider adding that tri baths are also more sensitive to zinc drag-in concentration than hex baths.

### Items for Watson

- Verify current RoHS/REACH Cr6+ exemption status for plating applications as of 2026 (Watson flag #1 already open).

---

## Poster #27 -- Wastewater Treatment Fundamentals

This poster falls mostly outside my core lab chemistry scope. However, the chemistry sections are within my competence.

### Confirmed

- Cyanide destruction Stage 1: CN- + OCl- -> CNO- + Cl- at pH > 10 -- correct. pH > 10 is critical because below pH 10, chlorine gas can evolve, and at low pH, HCN gas (lethal at 50 ppm) is generated.
- Cyanide destruction Stage 2: 2CNO- + 3OCl- -> 2CO2 + N2 + 3Cl- at pH 8.0-8.5 -- correct. The pH drop for Stage 2 is essential and often missed by operators.
- "NEVER mix cyanide waste with acid waste -- generates HCN gas (lethal)" -- correct. Cannot be overstated. Appropriately prominent.
- Chrome reduction procedure: lower pH to 2.0-3.0 with H2SO4, add sodium metabisulfite -- correct.
- Diphenylcarbazide spot test for Cr6+ verification -- correct.
- Cr3+ precipitation pH 7.5-8.5, optimal 8.0 -- correct.
- Ni2+ precipitation pH 9.0-10.5, optimal 9.5 -- correct.
- Fe2+/3+ precipitation pH 7.0-9.0, optimal 8.0 -- correct.
- Cd2+ precipitation pH 9.0-11.0, optimal 10.0 -- correct.
- Cu2+ precipitation range 8.0-10.0 -- acceptable as a broad window (see correction below for optimal value).
- Treatment process flow (equalization -> pH adjustment -> coagulant/flocculant -> clarifier -> filter press -> final pH check -> discharge) -- correct sequence.
- Polymer dosing "1-5 mg/L typical" and "overdosing breaks floc apart" -- correct.
- "Sludge to hazardous waste disposal" -- correct. F006 listed hazardous waste under RCRA.
- "NaOH = cleaner sludge, higher chemical cost. Lime = cheaper, more sludge volume" -- correct.
- Retention time 30-60 minutes minimum for clarifier -- correct.
- Final discharge pH 6.0-9.0 -- correct per 40 CFR 433.
- All operator best practices and common mistakes lists -- accurate and practical.

### Corrections Needed

8. **Copper precipitation optimal pH -- listed as 9.0**
   - **Problem:** Copper hydroxide minimum solubility is closer to pH 8.5-9.0. The optimal should be 8.5 rather than 9.0 for the typical case.
   - **Correction:** Change optimal to 8.5.
   - **Priority:** Low (the difference is small, but correctness matters for a reference poster)

9. **Zinc precipitation optimal pH -- listed as 9.5, range 8.5-10.5**
   - **Problem:** Zinc hydroxide is amphoteric and begins to re-dissolve above approximately pH 10. At pH 9.5, zinc is at the edge in some systems. The practical minimum solubility for zinc is approximately pH 8.5-9.0.
   - **Correction:** Change optimal to 9.0. Narrow the range to 8.0-9.5. The upper bound of 10.5 is dangerously high for zinc -- it will re-dissolve.
   - **Priority:** Medium

10. **Amphoteric callout -- "zinc and nickel may re-dissolve above pH 10"**
    - **Problem:** Nickel hydroxide is not truly amphoteric in the classical sense at practical concentrations. It does not readily re-dissolve in excess NaOH. Zinc is the textbook example.
    - **Correction:** Change to: "zinc re-dissolves above pH 10 (amphoteric behavior)." Drop nickel from this specific claim.
    - **Priority:** Medium

11. **Chrome reduction balanced equation**
    - **Problem:** The equation as written (Cr2O7(2-) + 3Na2S2O5 + 5H2SO4 -> 2Cr(3+) + 3Na2SO4 + 3SO4(2-) + 5H2O) does not balance cleanly. The sulfur and oxygen atom counts need verification.
    - **Correction:** Flag for Watson to balance properly before committing to a poster.
    - **Priority:** Medium

12. **Metabisulfite dosage -- "2.5 lbs per lb of Cr6+"**
    - **Problem:** The stoichiometric requirement is approximately 2.8-3.0 lbs metabisulfite per lb Cr6+. The 2.5 figure may be an underestimate. Practical dosing should include excess (typically 10-20% above stoichiometric).
    - **Correction:** Watson should verify. If 2.5 is the theoretical minimum, change to: "2.5-3.0 lbs sodium metabisulfite per lb Cr6+ (add 10-20% excess for complete reduction)."
    - **Priority:** Medium

### Recommended Improvements

- Consider adding a note about chelated metals to the precipitation pH section: "EDTA, NTA, and citrate chelators prevent normal hydroxide precipitation. Chelated metals require specialized treatment (higher pH, oxidation of chelator, or ion exchange)." The common mistakes section mentions chelators but the pH reference section does not.

### Items for Watson

- Verify all EPA 40 CFR Part 433 discharge limit values against current regulation (Watson flag already open).
- Balance the chrome reduction equation properly.
- Verify the metabisulfite dosage ratio (theoretical vs. practical).

---

## Poster #28 -- Temperature Control

### Confirmed

- Acid copper sulfate 70-95 F, optimal 75-85 F -- correct.
- Watts nickel (bright) 104-155 F, optimal 130-140 F -- correct (54-60 C standard).
- Hard chrome 120-150 F, optimal 130-140 F -- correct.
- Alkaline non-CN copper 110-160 F, optimal 130-145 F -- correct.
- Tin (acid) 60-90 F, optimal 65-80 F -- correct. Grain coarsening above 90 F is real.
- Anodize Type II 60-75 F, optimal 68-72 F -- correct. Temperature control is critical.
- Acid zinc (chloride) 70-100 F, optimal 75-90 F -- correct.
- Alkaline zinc (non-CN) 70-100 F, optimal 75-85 F -- correct.
- Gold (acid hard) 100-150 F, optimal 110-130 F -- correct as generic range.
- Arrhenius rule of thumb ("roughly doubles per 10 C") -- correct as standard teaching approximation. Actual factor varies 1.5x-3x per 10 C depending on reaction.
- Brightener consumption "approximately 2x per 10 C rise" for Watts nickel (Tyler flag from Alaina) -- acceptable. Directionally correct and consistent with the Arrhenius approximation. The word "approximately" provides adequate qualification.
- Immersion heaters 5-50 watts/gallon -- correct.
- Mag-drive pumps standard for corrosive solutions -- correct.
- Thermocouple placement mid-tank, mid-depth -- correct.
- EN decomposition risk above 200 F -- correct. Plate-out on tank walls, heaters, everything.
- "Tank covers reduce heat loss by 50-70%" -- correct as a general estimate.
- Conductivity-voltage relationship: "10 C rise can drop cell voltage by 0.5-1.0V in Watts nickel" -- reasonable order-of-magnitude estimate.

### Corrections Needed

13. **EN optimal upper temperature -- listed as 195 F**
    - **Problem:** 195 F (91 C) is at the upper edge of safe operation for most mid-phosphorus EN formulations. The optimal range should cap at 190-192 F.
    - **Correction:** Change to "optimal 185-190 F" (85-88 C). Keep max at 200 F but note that 195+ F approaches the decomposition threshold.
    - **Priority:** High (safety-critical -- EN decomposition is one of the most expensive single-event failures in a plating shop)

### Recommended Improvements

- The six-property effects matrix Row 4 says throwing power "Generally improved" at higher temperature. This is true for most systems but is an oversimplification. For some baths (particularly acid zinc), throwing power can degrade at elevated temperature as the cathode efficiency curve shifts. Consider adding "varies by system" or "most baths" as a qualifier.
- Row 6 (Brightness) correctly notes the peak-then-decline behavior. No change needed.

---

## Poster #29 -- Anode Chemistry and Maintenance

### Confirmed

- Soluble anode half-reaction M -> M2+ + 2e- -- correct as generic representation. 2+ is the most common oxidation state for major plating metals.
- Insoluble anode half-reaction 2H2O -> O2 + 4H+ + 4e- -- correct. The H+ generation explains why insoluble-anode baths drift acidic.
- "Produces sludge/fines -- MUST use anode bags" -- correct and appropriately emphatic.
- "Bath chemistry requires more active management" for insoluble anodes -- correct.
- Watts nickel: electrolytic Ni S-Rounds in Ti baskets + PP bags, A:C 2:1 -- all correct.
- Acid copper: OFHC copper (P-deoxidized), 0.04-0.06% P, A:C 1:1 -- correct. P content is critical.
- Alkaline zinc: SHG zinc in steel baskets, NOT titanium -- correct. Zinc alloys with titanium.
- Hard chrome: lead-antimony 6-8% Sb or DSA -- correct.
- Silver (cyanide): fine silver 99.9% bars, A:C 2:1, anode bags critical -- all correct.
- Tin: passivates easily, maintain adequate Sn2+ -- correct.
- Electroless nickel: no external anode, chemical reduction -- correct.
- Passivation symptoms: rising voltage, declining metal concentration, surface filming, pH drop -- all correct.
- Passivation causes: low chloride, excessive anode CD, contaminated surface, wrong composition, stagnant solution -- all correct.
- Chloride threshold for nickel: 30 g/L NiCl2 -- defensible as an alarm threshold. Some formulations recommend 40-50 g/L NiCl2 minimum, but passivation can begin below 30 g/L.
- Carbonyl vs. electrolytic nickel distinction -- correct. Carbonyl rounds can passivate more readily.
- Recovery: acid-dip (10% HCl for nickel anodes), inspect, verify chloride before re-install -- all correct.
- Anode bag materials: PP heat-resistant to 200 F, polyester less heat-resistant, cotton/Dynel being phased out -- all correct.
- Double-bag for bright nickel -- correct best practice.
- Rinse new bags in DI water to remove sizing compounds -- correct.
- Replace all bags simultaneously -- correct (prevents uneven flow distribution).
- Weekly bag inspection -- appropriate for production lines.
- Troubleshooting table: all symptom-cause-fix relationships are accurate.
- "pH dropping unexpectedly -- passivated anodes (O2 evolution generates acid)" -- correct and often overlooked.
- DSA description (mixed metal oxide coatings, longer life, no lead contamination) -- correct.

### Corrections Needed

None. This poster is technically excellent throughout.

### Recommended Improvements

- In the anode type gallery, Card 4 lists platinized titanium as "Used in: Precious metals, EN." For EN, this is slightly misleading -- EN does not use anodes. Platinized titanium is used as a current-carrying element in some electrolytic precious metal processes. Consider changing to "Used in: Precious metals, rhodium, ruthenium."
- The passivation prevention note "Ensure solution circulation reaches anode surface" could be strengthened: "Air or solution agitation near anodes is as important as agitation near parts."

---

## Poster #30 -- Bath Analysis Methods

This poster directly overlaps my core expertise. Both Tyler flags were open.

### Confirmed

- Hull cell conditions: 267 mL, 2 A, 5-10 min, bath temperature -- correct. 267 mL is the standard volume (produces 1 mL/cm2 at standard panel geometry). Bath temperature (not room temp) is correct.
- Cathode material varies by process: brass for acid copper and zinc, steel for nickel and chrome -- correct.
- Titration description ("EDTA for metals, acid-base for pH chemicals, iodometric for oxidizers") -- correct summary of the three major categories.
- AA/ICP as "gold standard for contaminant detection" -- correct.
- Specific gravity "quick, non-destructive" -- correct.
- Method hierarchy: daily pH + temp + Hull cell; weekly titration + SG; monthly AA/ICP -- correct as a general framework.
- Watts nickel metal analysis weekly (NiSO4, NiCl2, H3BO3) -- correct for a well-controlled bath.
- Watts nickel Hull cell every shift -- correct.
- Watts nickel contaminants monthly AA (Cu, Zn, Fe, Pb) -- correct.
- Watts nickel surface tension weekly -- correct.
- Hard chrome metal weekly (CrO3, SO4) -- correct. CrO3:SO4 ratio (100:1) is the critical parameter.
- EN metal analysis every shift -- correct. EN is the most analysis-intensive bath.
- EN temperature continuous -- correct, with alarm.
- EN MTO tracking -- correct and essential.
- Gold metal daily -- correct (gold is expensive and concentration directly affects deposition rate).
- Silver free cyanide ratio critical -- correct.
- Sampling: mid-tank mid-depth, clean dedicated labware, rinse protocol, filter 0.45 micron for AA/ICP, unfiltered for titration, label immediately -- all correct.
- Common errors: stale pH cal, wrong indicator, contaminated glassware, ignoring temperature correction, surface sampling, rushing Hull cell -- all accurate and practical.
- Startup cost estimates (pH meter ~$200, Hull cell ~$300, titration kit ~$500, hydrometer ~$50, thermometer ~$75) -- correct as ballpark figures.
- "Testing budget target: 1-3% of total plating chemical spend" -- reasonable industry guideline.

### Corrections Needed

14. **Acid copper -- "pH: Daily"**
    - **Problem:** Acid copper sulfate baths do not have a meaningful pH control point. The bath is strongly acidic (H2SO4-based). What matters is free sulfuric acid content, measured by titration.
    - **Correction:** Change column entry from "pH -- Daily" to "Free acid (titration) -- Weekly."
    - **Priority:** High (this would mislead a lab tech into pH-metering acid copper, which is not how it is done)

15. **Watts nickel pH frequency -- "Daily"**
    - **Problem:** In a production nickel bath, pH can drift significantly during a single shift under heavy loading. Daily is not frequent enough for a busy line.
    - **Correction:** Change to "Every shift" or "2x/day minimum."
    - **Priority:** Medium

16. **Hull cell amperage -- only "2 A" stated**
    - **Problem:** Some processes use different amperage. Decorative chrome is commonly run at 3 A or 5 A. Alkaline zinc is sometimes run at 1 A.
    - **Correction:** Add a note: "2 A is standard for most baths. Some processes use different amperage -- consult your chemical supplier's test procedure."
    - **Priority:** Low

17. **Hard chrome Hull cell frequency -- "Weekly"**
    - **Problem:** Hull cell testing for hard chrome is not universally practiced because the deposit appearance is less informative than for nickel or zinc. Some shops rely on chemistry and test coupons instead.
    - **Correction:** Change to "Weekly or as needed."
    - **Priority:** Low

### Recommended Improvements

- The acid zinc row lists "Baume (daily)" under Special Tests. Baume is a measure of specific gravity. Since SG is already listed as a weekly column, the Baume entry is redundant unless the intent is to emphasize that acid zinc benefits from more frequent SG checks. Clarify: either move to the SG column with "Daily" frequency, or relabel as "Baume / SG (daily) -- acid zinc benefits from daily monitoring."
- The spectrophotometry card description is accurate but could note that UV-Vis spectrophotometry is also used for additive analysis (CVS -- Cyclic Voltammetric Stripping for acid copper brightener) in advanced labs. This is a nice-to-have, not critical.
- The alkaline zinc row lists "Carbonate (monthly)" under Special Tests. This is correct and important. Consider adding the method: "carbonate by titration (BaCl2 precipitation method)" so the lab tech knows what to look up.

---

## Master Correction Summary

### Corrections Required (by priority)

| # | Poster | Item | Current | Should Be | Priority |
|---|--------|------|---------|-----------|----------|
| 1 | #24 | Straight DC description | "Constant voltage and current" | "Steady, uninterrupted current flow" | Medium |
| 2 | #24 | Ripple thresholds | Green 0-5%, Yellow 5-15%, Red >15% | Green 0-5% (note <3% for chrome/Ni), Yellow 5-10%, Red >10% | High |
| 3 | #24 | Hard chrome pulse claim | "improves microcracking" | "may improve microcrack density in specialized processes" | Low |
| 4 | #25 | Carbon treatment pH (nickel) | "Raise pH to 4.5-5.0" | "Raise pH to 5.0-5.5" | High |
| 5 | #25 | Carbon contact time | "30-60 minutes" | "1-2 hours minimum" | High |
| 6 | #25 | Don't: carbon time limit | "Don't leave carbon longer than 1 hour" | "Don't return bath to service without removing ALL carbon by filtration" | High |
| 7 | #26 | Tri clear SST | "48-200 hrs" (conflated) | "Without sealer: 24-96 hrs. With sealer: 96-200+ hrs" | Medium |
| 8 | #27 | Copper precipitation optimal | 9.0 | 8.5 | Low |
| 9 | #27 | Zinc precipitation range/optimal | 8.5-10.5, optimal 9.5 | 8.0-9.5, optimal 9.0 | Medium |
| 10 | #27 | Amphoteric callout | "zinc and nickel may re-dissolve" | "zinc re-dissolves above pH 10" (drop nickel) | Medium |
| 11 | #27 | Chrome reduction equation | May not balance | Watson to verify and correct | Medium |
| 12 | #27 | Metabisulfite dosage | "2.5 lbs per lb Cr6+" | Verify; likely "2.5-3.0 lbs + 10-20% excess" | Medium |
| 13 | #28 | EN optimal upper temp | 195 F | 190 F (85-88 C safe optimal ceiling) | High |
| 14 | #30 | Acid copper "pH" column | "pH -- Daily" | "Free acid (titration) -- Weekly" | High |
| 15 | #30 | Nickel pH frequency | "Daily" | "Every shift" | Medium |
| 16 | #30 | Hull cell amperage note | 2 A only | Add note: some processes use different amperage | Low |
| 17 | #30 | Chrome Hull cell frequency | "Weekly" | "Weekly or as needed" | Low |

**Count:** 17 corrections across 7 posters. 5 High priority, 7 Medium, 5 Low.

### Items for Watson Source-Check

| # | Poster | Item | Question |
|---|--------|------|----------|
| 1 | #24 | Tin whisker / PR claim | Is PR plating a validated whisker mitigation strategy? Source needed. |
| 2 | #24 | Hard chrome pulse microcracking | Verify "improves microcracking" is sourced or soften language. |
| 3 | #26 | RoHS/REACH Cr6+ exemptions | Current exemption status as of 2026 for plating applications. |
| 4 | #27 | Chrome reduction equation | Balance the dichromate + metabisulfite equation properly. |
| 5 | #27 | Metabisulfite dosage | 2.5 lbs/lb: is this theoretical minimum or practical dose? |
| 6 | #27 | EPA discharge limits | Verify all values against current 40 CFR Part 433 tables. |

### Posters Requiring Zero Corrections

- **Poster #29 (Anode Chemistry and Maintenance)** -- technically excellent throughout. No corrections needed.

### Poster Quality Rankings

1. **#29 Anode Chemistry** -- Excellent. Zero corrections.
2. **#26 Chromate and Conversion** -- Very strong. One correction (SST split).
3. **#28 Temperature Control** -- Very strong. One correction (EN temp).
4. **#24 Rectifier Fundamentals** -- Strong. Three corrections.
5. **#30 Bath Analysis Methods** -- Strong. Four corrections (important since lab techs reference daily).
6. **#25 Filtration and Purification** -- Strong. Three corrections (all in carbon treatment section).
7. **#27 Wastewater Treatment** -- Good. Five corrections/verifications (precipitation pH, equation, dosage).

---

*Tyler -- Plating Chemist Agent*
*Validation completed 2026-04-25*
*v2 -- Full re-review with expanded confirmations and refined corrections*
