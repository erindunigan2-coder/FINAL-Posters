---
title: "Tyler Validation Report — Batch 3"
date: 2026-04-26
author: Tyler (plating-chemist)
scope: Technical accuracy validation of 6 main-tank Construction Workups against Watson Research Briefs
status: Complete
tags:
  - PosterValidation
  - Tyler
  - Series2
---

# Tyler Validation Report -- Batch 3

**Tyler -- Plating Chemist / Analytical Chemistry**
**Plating Posters Inc -- Series 2 Poster Validation**
**2026-04-26**

---

## Summary

Six main-tank Construction Workups were cross-referenced against the corresponding Watson Research Brief sections. Each CW was checked for: bath composition, temperature ranges, current density, pH, anode type, cathode efficiency, plating rate, and safety/regulatory claims.

| # | Poster | Cluster | Verdict |
|---|--------|---------|---------|
| 1 | Poster 52 -- Zinc-Nickel Main Tank | EP-03 | PASS (1 minor note) |
| 2 | Poster 68 -- Nickel Sulfamate Main Tank | EP-05 | PASS (1 minor note) |
| 3 | Poster 92 -- Hard Chrome Main Tank | EP-08 | PASS |
| 4 | Poster 108 -- Copper Alkaline Main Tank | EP-10 | PASS (1 minor note) |
| 5 | Poster 148 -- Tin-Lead Main Tank | EP-15 | FLAG (1 issue) |
| 6 | Poster 164 -- Zinc Phosphate Conversion Stage | CC-02 | FLAG (1 issue) |

**Overall: 4 clean passes, 2 flags. No dangerous errors found. Both flags are conservatively cautious calls -- neither would cause harm, but both should be corrected for accuracy before print.**

---

## 1. Poster 52 -- Zinc-Nickel Main Tank (EP-03)

### Cross-reference: Watson Research Brief, Cluster 2 (lines 253--401)

**Bath Chemistry (CW line 126--133 vs. Watson lines 316--323)**

| Parameter | CW Value | Watson Value | Match? |
|-----------|----------|-------------|--------|
| Zinc (as Zn metal) | 6--12 g/L | 6--12 g/L | YES |
| Nickel (as Ni metal) | 1--3 g/L | 1--3 g/L | YES |
| NaOH | 100--150 g/L | 100--150 g/L | YES |
| Zn:Ni ratio | 4:1 to 8:1 | 4:1 to 8:1 | YES |
| Amine complexing agent | Per supplier TDS | Per supplier TDS | YES |

**Acid Zn-Ni Footnote (CW line 138 vs. Watson lines 327--334)**

| Parameter | CW Value | Watson Value | Match? |
|-----------|----------|-------------|--------|
| Zn | 25--50 g/L | 25--50 g/L | YES |
| Ni | 25--40 g/L | 25--40 g/L | YES |
| NH4Cl or KCl | 100--200 g/L | 100--200 g/L | YES |
| Boric acid | 25--35 g/L | 25--35 g/L | YES |
| pH | 5.5--6.5 | 5.5--6.5 | YES |

**Operating Parameters (CW lines 150--160 vs. Watson lines 338--348)**

| Parameter | CW Value | Watson Value | Match? |
|-----------|----------|-------------|--------|
| Temp (alkaline) | 75--95 F | 75--95 F | YES |
| Temp (acid) | 75--105 F | 75--105 F | YES |
| pH (alkaline) | >13 | >13 | YES |
| pH (acid) | 5.5--6.5 | 5.5--6.5 | YES |
| CD rack (alk) | 10--40 ASF | 10--40 ASF | YES |
| CD barrel (alk) | 5--15 ASF | 5--15 ASF | YES |
| CD rack (acid) | 10--50 ASF | 10--50 ASF | YES |
| CD barrel (acid) | 5--20 ASF | 5--20 ASF | YES |
| Voltage (alk) | 4--12 V | 4--12 V | YES |
| Voltage (acid) | 3--8 V | 3--8 V | YES |
| Cathodic eff (alk) | 40--70% | 40--70% | YES |
| Cathodic eff (acid) | 80--95% | 80--95% | YES |
| Anode (alk) | Pure Zn (no Ni) | Zinc anodes (pure Zn, no Ni) | YES |
| Anode (acid) | Steel or Ni-plated steel (insol) or Zn | Same | YES |
| Plating rate at 20 ASF | ~0.15--0.25 mil/hr | ~0.15--0.25 mil/hr | YES |

**Alloy Composition (CW lines 166--174 vs. Watson lines 350--353)**

| Parameter | CW Value | Watson Value | Match? |
|-----------|----------|-------------|--------|
| Target | 12--16% Ni | 12--16% Ni | YES |
| Low threshold | <10% Ni | <10% Ni | YES |
| High threshold | >18% Ni | >18% Ni | YES |

**Defect Table (CW lines 186--194 vs. Watson lines 366--374)**
All 7 defects match Watson's table exactly.

**Safety (CW lines 234--238)**
- NaOH burn hazard: correct
- Nickel IARC Group 2B (inhalation): NOTE -- Watson does not specify IARC classification in the ZnNi section. Alaina's CW states "IARC Group 2B carcinogen (inhalation)." Technically, IARC classifies nickel compounds as Group 1 (carcinogenic to humans) for inhalation of soluble nickel compounds, and Group 2B for metallic nickel. Since the bath contains soluble nickel salts (NiSO4/NiCl2), the more conservative classification would be Group 1 for the soluble nickel compounds. However, the aerosol exposure from an alkaline bath at 75--95 F is minimal (no mist generation at these temperatures). The CW's "Group 2B" is defensible in context but slightly understates the hazard for the soluble salts.
- Wastewater: Zn at pH 8.5--9.5, Ni at pH 9.0--10.0 -- these are standard precipitation ranges. Correct.

**Verdict: PASS**

> NOTE: CW line 253 states "IARC Group 2B carcinogen (inhalation)" for nickel compounds. The soluble nickel salts in the bath are classified IARC Group 1 for inhalation. Consider changing to "IARC Group 1 (soluble Ni compounds, inhalation)" for maximum accuracy. Not a safety-critical error because the poster already recommends ventilation and PPE.

---

## 2. Poster 68 -- Nickel Sulfamate Main Tank (EP-05)

### Cross-reference: Watson Research Brief, Cluster 4 (lines 609--720)

**Bath Chemistry (CW lines 128--134 vs. Watson lines 650--656)**

| Parameter | CW Value | Watson Value | Match? |
|-----------|----------|-------------|--------|
| Ni sulfamate (electroforming) | 300--450 g/L | 300--650 g/L (low--high) | SEE NOTE |
| Ni sulfamate (gen. engineering) | 450--650 g/L | Same range | YES |
| NiCl2 (electroforming) | 0 g/L | 0 g/L (for zero-stress) | YES |
| NiCl2 (engineering) | 5--30 g/L | 0--30 g/L (low to high) | YES |
| Boric acid (electroforming) | 30--45 g/L | 30--45 g/L | YES |
| Boric acid (engineering) | 37--45 g/L | 37--45 g/L | YES |
| Ni metal (electroforming) | 60--80 g/L | 60 g/L (low) to 110 g/L | YES |
| Ni metal (engineering) | 80--110 g/L | 80--110 g/L | YES |
| Saccharin | 50--200 mg/L | Per supplier TDS | YES (CW more specific) |

NOTE: Watson gives the full range as 300--650 g/L across all applications. The CW splits this into 300--450 for electroforming and 450--650 for engineering. This is a reasonable and pedagogically useful split -- electroforming uses lower concentration for stress reasons. No error.

**Operating Parameters (CW lines 156--167 vs. Watson lines 662--674)**

| Parameter | CW Value | Watson Value | Match? |
|-----------|----------|-------------|--------|
| Temp (electroforming) | 90--110 F | 90--110 F | YES |
| Temp (engineering) | 100--140 F | 100--140 F | YES |
| pH (electroforming) | 3.8--4.2 | 3.8--4.2 | YES |
| pH (engineering) | 3.5--4.5 | 3.5--4.5 | YES |
| CD (electroforming) | 10--40 ASF | 10--40 ASF | YES |
| CD (engineering) | 20--100 ASF | 20--100 ASF | YES |
| Voltage (electroforming) | 4--12 V | 4--12 V | YES |
| Voltage (engineering) | 6--15 V | 6--15 V | YES |
| Cathodic eff | 95--100% | 95--100% | YES |
| Plating rate 40 ASF | ~0.9--1.0 mil/hr | ~0.9--1.0 mil/hr | YES |
| Plating rate 100 ASF | ~2.2--2.5 mil/hr | ~2.2--2.5 mil/hr | YES |

**Hydrolysis Warning (CW line 144 vs. Watson line 658)**
CW: ">160 F (71 C) or pH <3.0" -- exact match to Watson. Correct.
CW: "hydrolyzes to nickel ammonium sulfate IRREVERSIBLY" -- exact match. Correct.

**Stress Control Table (CW lines 176--183 vs. Watson lines 678--686)**
All 7 factors match Watson exactly.

**Defect Table (CW lines 197--204 vs. Watson lines 690--697)**
All 6 defects match Watson exactly.

**Safety (CW lines 253--258)**
- IARC Group 1 (inhalation), Group 2B (metallic Ni): This is technically correct and more precise than the Zn-Ni poster. Soluble nickel compounds via inhalation = Group 1. Metallic nickel = Group 2B. Well stated.
- Wastewater Ni precipitation at pH 9.5--10.5: Correct.
- Discharge limits 0.5--3.4 mg/L: This range spans typical pretreatment standards to daily max depending on category. Acceptable for a poster.

**Anode Management (CW lines 216--221 vs. Watson lines 670)**
- S-Rounds in Ti baskets with bags: matches Watson
- R-Rounds for zero-sulfur: correct additional detail
- Anode:cathode 1:1 to 2:1: matches Watson
- Air agitation avoided: matches Watson

**Tagline (CW line 92): "Near-zero internal stress"**
Watson line 617: "lower internal stress (can approach zero or slightly compressive with stress reducers)." Confirmed.

**Verdict: PASS**

> NOTE: The CW header (line 13) states temperature range as "130--145 F" in the frontmatter, but the operating parameters table correctly shows the full range (90--140 F depending on application). The 130--145 F value in the frontmatter is not technically wrong (it falls within the general engineering range) but it misrepresents the electroforming range. Frontmatter is not printed on the poster, so this is cosmetic only.

---

## 3. Poster 92 -- Hard Chrome Main Tank (EP-08)

### Cross-reference: Watson Research Brief, Cluster 7 (lines 938--1087)

**Bath Chemistry (CW lines 151--157 vs. Watson lines 1001--1007)**

| Parameter | CW Value | Watson Value | Match? |
|-----------|----------|-------------|--------|
| CrO3 (conventional) | 200--250 g/L | 200--250 g/L | YES |
| CrO3 (high-conc) | 300--400 g/L | 300--400 g/L | YES |
| H2SO4 (conventional) | 2.0--2.5 g/L | 2.0--2.5 g/L | YES |
| H2SO4 (high-conc) | 3.0--4.0 g/L | 3.0--4.0 g/L | YES |
| CrO3:SO4 (conventional) | 100:1 | 100:1 | YES |
| CrO3:SO4 (high-conc) | 75:1 to 100:1 | 75:1 to 100:1 | YES |
| Cr3+ | 1--3% of CrO3 (2--5 g/L) | 1--3 g/L (1--3% of CrO3) | YES |

**Operating Parameters (CW lines 163--171 vs. Watson lines 1013--1021)**

| Parameter | CW Value | Watson Value | Match? |
|-----------|----------|-------------|--------|
| Temperature | 120--145 F (typ 130--135) | 120--145 F (typ 130--135) | YES |
| CD | 150--400 ASF (typ 200--300) | 150--400 ASF (typ 200--300) | YES |
| Voltage | 6--12 V | 6--12 V | YES |
| Cathodic eff | 10--18% | 10--18% | YES |
| Plating rate 200 ASF | ~1.0--1.5 mil/hr | ~1.0--1.5 mil/hr | YES |
| Plating rate 300 ASF | ~1.5--2.2 mil/hr | ~1.5--2.2 mil/hr | YES |
| Agitation | Solution flow or mechanical; NEVER air | Same | YES |
| Anode | Pb-6%Sn (or Pb-7%Sn) | Pb-6%Sn or Pb-7%Sn | YES |
| A:C ratio | 2:1 to 3:1 | 2:1 to 3:1 | YES |
| Filtration | 10--25 micron | 10--25 micron | YES |

**CrO3:SO4 Ratio Control (CW lines 189--196 vs. Watson lines 1031--1038)**

| Condition | CW Value | Watson Value | Match? |
|-----------|----------|-------------|--------|
| Ratio too high | >125:1 | >125:1 | YES |
| Optimal | 80:1 to 100:1 | 80:1 to 100:1 | YES |
| Ratio too low | <75:1 | <75:1 | YES |
| Add sulfate | dilute H2SO4 | dilute H2SO4 | YES |
| Remove sulfate | BaCO3 | BaCO3 | YES |

**Cr3+ Control (CW lines 209--213 vs. Watson lines 1040--1045)**
All values match exactly.

**Contamination Thresholds (CW lines 244--249 vs. Watson lines 1061--1067)**
All 5 contaminants, thresholds, and removal methods match exactly.

**Defect Table (CW lines 226--233 vs. Watson lines 1050--1057)**
6 of 7 defects match. CW adds "Non-uniform thickness" which Watson covers under a different defect (poor coverage). The CW version is more specific and useful. Good editorial judgment by Alaina.

**Safety (CW lines 279--288 vs. Watson lines 938, 1072--1077)**
- IARC Group 1 carcinogen: Correct.
- OSHA PEL 5 ug/m3: Correct.
- EPA D007: Correct RCRA waste code for chromium.
- Wastewater: Cr6+ reduced to Cr3+ then precipitate Cr(OH)3 at pH 8--9: Standard two-step treatment. Correct.
- EPA limit 0.5 mg/L total Cr daily max: This is consistent with 40 CFR 433 Metal Finishing categorical limits. Correct.
- OSHA citation 29 CFR 1910.1026: Correct Cr(VI) standard.
- EPA NESHAP 40 CFR 63 Subpart N: Correct for hard chrome. Well done.

**Hardness: 800--1000 HV** (CW line 34, Watson line 942): Match.

**Verdict: PASS**

No flags. This is the cleanest CW in the batch. Every value cross-references perfectly against Watson. The safety and regulatory citations are precise and correct.

---

## 4. Poster 108 -- Copper Alkaline Main Tank (EP-10)

### Cross-reference: Watson Research Brief, Cluster 9 (lines 1262--1389)

**Copper Pyrophosphate Chemistry (CW lines 120--128 vs. Watson lines 1318--1325)**

| Parameter | CW Value | Watson Value | Match? |
|-----------|----------|-------------|--------|
| Cu2P2O7 | 53--84 g/L | 53--84 g/L | YES |
| K4P2O7 | 200--350 g/L | 200--350 g/L | YES |
| NH4OH | 1--5 mL/L | 1--5 mL/L | YES |
| KNO3 | 5--15 g/L | 5--15 g/L | YES |
| Cu metal | 22--34 g/L | 22--34 g/L | YES |
| P2O7:Cu ratio | 7:1 to 8:1 | 7:1 to 8:1 | YES |

**Copper HEDP Chemistry (CW lines 142--148 vs. Watson lines 1329--1335)**

| Parameter | CW Value | Watson Value | Match? |
|-----------|----------|-------------|--------|
| Cu metal | 5--30 g/L | 5--30 g/L | YES |
| HEDP | 50--100 g/L | 50--100 g/L | YES |
| Aux chelant | 10--30 g/L | 10--30 g/L | YES |
| NaOH/KOH | 30--80 g/L | 30--80 g/L | YES |
| Conductive salt | 15--30 g/L | 15--30 g/L | YES |

**Operating Parameters (CW lines 190--200 vs. Watson lines 1339--1348)**

| Parameter | CW (Pyro) | Watson (Pyro) | CW (HEDP) | Watson (HEDP) |
|-----------|-----------|--------------|-----------|--------------|
| Temp | 100--140 F | 100--140 F | 100--160 F | 100--160 F |
| pH | 8.0--9.0 | 8.0--9.0 | 9.0--13.0 | 9.0--13.0 |
| CD | 10--80 ASF | 10--80 ASF | 5--30 ASF | 5--30 ASF |
| Voltage | 3--8 V | 3--8 V | 3--8 V | 3--8 V |
| CE | 70--90% | 70--90% | 30--70% | 30--70% |
| Anode (pyro) | OFHC or phosphorized Cu | Same | -- | -- |
| Anode (HEDP) | -- | -- | OFHC or insol (MMO/Pt-Ti) | Same |

All match.

**Defect Table (CW lines 208--215 vs. Watson lines 1359--1366)**
All 5 defects match Watson.

**Analytical Methods (CW lines 231--238 vs. Watson lines 1350--1355)**
Cu by iodometric or EDTA: match. Free pyrophosphate: match. Hull cell 267 mL, 1--2A, 5--10 min: match.

**Contamination (CW lines 275--280 vs. Watson line 1366)**
- Orthophosphate >100 g/L: Watson confirms this threshold. Match.
- Fe >50 ppm: Watson does not specify Fe threshold explicitly for this bath. This is a reasonable industry value from domain knowledge. Acceptable.

**Safety (CW lines 290--296)**
- No cyanide: Correct -- that is the entire point.
- Copper precipitation at pH 8.5--9.5: Standard. Correct.
- HEDP/pyrophosphate chelation issue: CW correctly notes that chelants keep copper in solution through hydroxide precipitation and may require sulfide precipitation, electrowinning, or ion exchange. Watson line 1388 confirms this exactly.

**Verdict: PASS**

> NOTE: Alaina's CW has a question for Tyler (line 326) about Hull cell parameters for alkaline non-CN copper. I can confirm: 267 mL, 1--2A, 5--10 min at bath temperature is correct for both pyrophosphate and HEDP baths. For pyrophosphate specifically, 2A / 10 min is more common. For HEDP, 1A / 5--10 min is typical due to the lower current density range. The CW's range of "1--2A, 5--10 min" covers both appropriately.

---

## 5. Poster 148 -- Tin-Lead Main Tank (EP-15)

### Cross-reference: Watson Research Brief, Cluster 14 (lines 1965--2105)

**Bath Chemistry (CW lines 157--164, 170--177 vs. Watson lines 2010--2017)**

| Parameter | CW (60/40) | Watson (60/40) | Match? |
|-----------|-----------|----------------|--------|
| Sn2+ | 35--55 g/L | 35--55 g/L | YES |
| Pb2+ | 15--25 g/L | 15--25 g/L | YES |
| Free MSA | 100--200 g/L | 100--200 g/L | YES |
| Antioxidant (HQ) | 1--2 g/L | 1--2 g/L | YES |

| Parameter | CW (90/10) | Watson (90/10) | Match? |
|-----------|-----------|----------------|--------|
| Sn2+ | 50--70 g/L | 50--70 g/L | YES |
| Pb2+ | 5--10 g/L | 5--10 g/L | YES |
| Free MSA | 100--200 g/L | 100--200 g/L | YES |
| Antioxidant (HQ) | 1--2 g/L | 1--2 g/L | YES |

**Operating Parameters (CW lines 127--138 vs. Watson lines 2031--2041)**

| Parameter | CW Value | Watson Value | Match? |
|-----------|----------|-------------|--------|
| Temperature | 75--85 F | 60--100 F (typ 75--85 F) | FLAG |
| CD rack | 15--25 ASF | 10--40 ASF (typ 15--25) | FLAG |
| CD barrel | 5--15 ASF | 5--15 ASF | YES |
| CE | 90--98% | 90--98% | YES |
| A:C ratio | 1:1 to 2:1 | 1:1 to 2:1 | YES |
| Filtration | 5--10 micron | 5--10 micron | YES |
| Anode | Sn-Pb alloy or sep Sn+Pb | Same | YES |
| Agitation | Air (oil-free) or mechanical | Air (oil-free) or mechanical | YES |

**FLAG -- Temperature and CD ranges are narrowed in the CW**

The CW shows the tank parameters as 75--85 F and 15--25 ASF (rack). Watson's research brief gives the full MSA bath range as 60--100 F and 10--40 ASF, with "typical 75--85 F" and "typical 15--25 ASF."

For a main tank poster, showing only the "typical" range without indicating the full operating envelope is misleading. A shop running a higher-speed line at 30 ASF or a cooler bath at 65 F would look at this poster and think they are out of spec. The poster should show the full range with the typical range highlighted, the same way the zinc-nickel poster handles alkaline vs. acid side-by-side.

**Recommendation:** Change the in-tank parameter labels to show the full range:
- Temperature: `60--100 F (16--38 C); typical 75--85 F`
- CD (rack): `10--40 ASF; typical 15--25 ASF`

**Voltage:** CW does not show voltage in the in-tank parameters. Watson gives 1--5 V. Should be added for completeness.

**Defect Table (CW lines 206--213 vs. Watson lines 2059--2066)**

| CW Defect | Watson Match | Match? |
|-----------|-------------|--------|
| Wrong alloy composition | YES | YES |
| Rough/gritty | YES (stannic acid) | YES |
| Dull deposit | YES | YES |
| Pitting | YES | YES |
| Poor solderability | YES | YES |
| Tin pest (alpha tin) | YES (56 F, >3% Pb prevents) | YES |

Watson has 7 defects; CW has 6. CW omits "Sn4+ (stannic) buildup" as a separate defect -- it is folded into "Rough/gritty" which is acceptable.

**Contamination (CW lines 228--233 vs. Watson -- not explicitly in brief)**
Watson does not provide explicit contamination thresholds for tin-lead. The CW's values (Cu >5 ppm, Fe >20 ppm, Cl >10 ppm, Sn4+ >10% of total Sn) are reasonable domain knowledge values. Acceptable.

**Safety / Regulatory (CW line 259)**
CW mentions: "Lead is a restricted substance under EU RoHS and a regulated occupational hazard under OSHA." Watson lines 2088--2104 are more detailed (IARC 2A, OSHA PEL 50 ug/m3, CDC BLL 3.5 ug/dL). The CW disclaimer is brief but accurate. The poster itself would benefit from a dedicated safety section as robust as the hard chrome poster, given that lead is a significant regulated hazard. However, this is a design suggestion, not a technical error.

**Verdict: FLAG**

> FLAG (CW lines 127--131): Temperature shown as 75--85 F and CD shown as 15--25 ASF represent only the "typical" subrange. The full operating range per Watson is 60--100 F and 10--40 ASF (rack). Show the full range with typical highlighted. Also add voltage (1--5 V) to the in-tank parameters.

---

## 6. Poster 164 -- Zinc Phosphate Conversion Stage (CC-02)

### Cross-reference: Watson Research Brief, Cluster 2 (CC brief, lines 194--339)

**Bath Chemistry (CW lines 141--149 vs. Watson lines 304--312)**

| Parameter | CW Value | Watson Value | Match? |
|-----------|----------|-------------|--------|
| Zinc (Zn2+) | 0.8--2.0 g/L (spray) | 0.8--2.0 g/L (typical spray) | YES |
| Phosphoric acid (total PO4) | 10--25 g/L | 10--25 g/L | YES |
| Nickel (Ni2+) | 0.5--1.5 g/L | 0.5--1.5 g/L | YES |
| Manganese (Mn2+) | 0.5--1.5 g/L | 0.5--1.5 g/L | YES |
| Nitrite (NO2-) | 0.05--0.15 g/L | 0.05--0.15 g/L | YES |
| Nitrate (NO3-) | 3--8 g/L | 3--8 g/L | YES |
| Fluoride (F-) | 0.5--2.0 g/L | 0.5--2.0 g/L | YES |

**Operating Parameters (CW lines 107--111, 203--208 vs. Watson lines 316--324)**

| Parameter | CW (Spray) | Watson (Spray) | Match? |
|-----------|-----------|----------------|--------|
| Temperature | 95--130 F | 95--130 F | YES |
| Free acid | 0.5--1.5 pts | 0.5--1.5 pts | YES |
| Total acid | 15--30 pts | 15--30 pts | YES |

| Parameter | CW (Immersion) | Watson (Immersion) | Match? |
|-----------|---------------|---------------------|--------|
| Temperature | 130--200 F | 130--200 F | YES |
| Free acid | 0.8--2.0 pts | 0.8--2.0 pts | YES |
| Total acid | 20--40 pts | 20--40 pts | YES |

**FA:TA Ratio (CW lines 159--163 vs. Watson line 322)**
CW: 1:10 to 1:20. Watson: 1:10 to 1:20. Match.

**pH (CW line 107 vs. Watson lines 323)**
CW: 2.5--3.5. Watson gives spray pH not explicitly but immersion as 2.5--3.5; spray as 2.8--3.5.

**FLAG -- CW pH range includes values below Watson's spray minimum.**

CW line 107 shows `pH: 2.5--3.5` as a single range displayed next to the tank. Watson distinguishes: spray pH 2.8--3.5, immersion pH 2.5--3.5. Since the CW tank diagram shows a general zinc phosphate bath without specifying spray vs. immersion, displaying pH 2.5--3.5 is not wrong -- it covers the full envelope. However, the CW should clarify that 2.5 is only appropriate for immersion; spray baths below 2.8 will produce excessively heavy/powdery coatings and excessive sludge.

**Recommendation:** Either split the pH display by application method (as is done for temperature, free acid, and total acid in the spray vs. immersion table in Zone 5) or add a note: `pH 2.5 for immersion only; spray minimum 2.8.`

**Coating Mechanism (CW lines 117--123 vs. Watson lines 282--296)**
The 4-step mechanism matches Watson:
1. Acid attack on Fe: correct
2. Local pH rise: correct
3. Crystal nucleation on Ti sites: correct
4. Accelerator oxidizes Fe2+ to Fe3+: correct

**Phosphophyllite vs. Hopeite (CW lines 128--129 vs. Watson lines 298--301)**
- Phosphophyllite formula: Zn2Fe(PO4)2.4H2O -- matches Watson
- Hopeite formula: Zn3(PO4)2.4H2O -- matches Watson
- P-ratio >0.5 preferred for automotive OEM: matches Watson

**Coating Weight (CW lines 178--180 vs. Watson lines 329--332)**

| Range | CW Value | Watson Value | Match? |
|-------|----------|-------------|--------|
| Light | 100--200 mg/ft2 | 100--200 mg/ft2 | YES |
| Medium | 200--500 mg/ft2 | 200--500 mg/ft2 | YES |
| Heavy | 500--1000+ mg/ft2 | 500--1000+ mg/ft2 | YES |
| OEM target | 150--350 mg/ft2 | 150--350 mg/ft2 | YES |

**Film Properties (CW lines 183--189 vs. Watson lines 333--338)**

| Property | CW Value | Watson Value | Match? |
|----------|----------|-------------|--------|
| Thickness | 2--25 um | 2--25 um | YES |
| Crystal size (conditioned) | 2--10 um | 2--10 um | YES |
| Color | Medium to dark gray | Medium to dark gray | YES |
| Bare salt spray | 4--48 hr | 4--48 hr | YES |
| With e-coat + topcoat | 500--1500+ hr | 500--1500+ hr | YES |

**Defect Table (CW lines 220--227 vs. Watson -- not in brief section read)**
The 6 defects listed are standard zinc phosphate process knowledge. All technically sound.

**Verdict: FLAG**

> FLAG (CW line 107): pH range shown as 2.5--3.5 without distinguishing spray (2.8--3.5) from immersion (2.5--3.5). This matters because running a spray system at pH 2.5 will produce a heavy, powdery, poorly adherent coating. Add a note or split by application method.

---

## Action Items for Alaina

1. **Poster 52 (Zinc-Nickel):** Consider updating IARC classification for soluble nickel compounds from "Group 2B" to "Group 1" in the safety section. Low priority -- cosmetic accuracy improvement.

2. **Poster 68 (Ni Sulfamate):** Frontmatter temperature range (130--145 F) does not reflect the full electroforming range (90--140 F). No poster impact, but clean up the frontmatter for consistency. Low priority.

3. **Poster 92 (Hard Chrome):** No changes needed. This CW is exemplary.

4. **Poster 108 (Copper Alkaline):** Hull cell parameters confirmed correct. No changes needed.

5. **Poster 148 (Tin-Lead):** MEDIUM PRIORITY. Expand temperature range from 75--85 F to 60--100 F (typical 75--85 F). Expand rack CD from 15--25 ASF to 10--40 ASF (typical 15--25 ASF). Add voltage (1--5 V).

6. **Poster 164 (Zinc Phosphate):** MEDIUM PRIORITY. Add spray vs. immersion distinction for pH (spray 2.8--3.5, immersion 2.5--3.5), or add a clarifying note to the in-tank pH label.

---

## Tyler's Overall Assessment

Alaina's CW quality is excellent. The vast majority of values are copy-perfect against Watson's research brief, which itself carries [VERIFIED] tags on all critical bath chemistry and operating parameter data. The two flags are both "narrowing" errors -- showing a subset of the full range rather than the complete envelope. Neither flag represents a dangerous value (every number in both CWs is within the correct range), but a plater looking at these posters as a reference might incorrectly conclude their own operating conditions are out of spec.

The hard chrome poster (Poster 92) deserves special mention -- every value, every regulatory citation, and every contamination threshold cross-checks perfectly. That poster is ready for production.

---

*Tyler -- Plating Chemist / Analytical Chemistry*
*Validation Report -- Batch 3*
*2026-04-26*
