# Tyler Validation Report — Electroplating Main Tank Posters

**Validated:** 2026-04-26
**Validator:** Tyler (plating chemist)
**Scope:** Nine Main Tank Construction Workup files across the electroplating poster clusters
**Method:** Each CW was read in full and all stated technical parameters were checked against standard industry references (Metal Finishing Guidebook, Modern Electroplating, ASM Handbook Vol. 5, Nickel Institute publications, ASTM standards, and direct field experience).

---

## Poster 44 — Zinc Plating (Acid) Main Tank

**Status:** PASS

**Parameters reviewed:**

| Parameter | CW Value | Industry Standard | Verdict |
|---|---|---|---|
| Zn metal | 25--35 g/L | 20--40 g/L typical KCl type | OK |
| KCl | 180--200 g/L | 150--230 g/L | OK |
| Boric acid | 25--30 g/L | 20--35 g/L | OK |
| pH | 5.0--5.4 (optimal); 4.8--5.8 (range) | 4.8--5.8 typical; 5.0--5.4 optimal | OK |
| Temperature | 70--85 F (21--29 C) | 70--90 F | OK |
| CD (rack) | 20--40 ASF | 10--40 ASF | OK |
| CD (barrel) | 5--12 ASF | 3--15 ASF | OK |
| Cathode efficiency | 95--98% | 95--98% | OK |
| Anodes | SHG zinc balls in Ti baskets, 99.99% purity | Correct | OK |
| A:C ratio | 1:1 to 2:1 | Standard | OK |
| Anode bags | 1--2 um PP | Correct | OK |

**Contamination thresholds:** Iron >50 ppm, Cu >5 ppm, Pb >2 ppm, Cr >1 ppm -- all consistent with published data.

**Notes:** Solid workup. The KCl vs. NH4Cl distinction is well handled. The carbonate "N/A" row in the contamination table is a smart educational callout. No issues found.

---

## Poster 60 — Nickel Plating (Watts) Main Tank

**Status:** FLAG (minor)

**Parameters reviewed:**

| Parameter | CW Value | Industry Standard | Verdict |
|---|---|---|---|
| NiSO4 (as salt) | 270--330 g/L | 240--340 g/L | OK |
| NiCl2 (as salt) | 37--55 g/L | 30--60 g/L | OK |
| Boric acid | 37--45 g/L | 30--45 g/L | OK |
| Ni metal (total) | 60--90 g/L | 55--90 g/L | OK |
| pH | 3.8--4.2 (optimal) | 3.8--4.2 typical bright Watts | OK |
| Temperature | 130--150 F (54--66 C) | 130--160 F | OK |
| CD (rack) | 30--50 ASF | 20--50 ASF | OK |
| CD (barrel) | 8--15 ASF | 5--15 ASF | OK |
| Cathode efficiency | 92--98% | 93--97% typical | OK |
| Anodes | Ni S-rounds, 99.9%+, in Ti baskets, double-bagged | Correct | OK |
| A:C ratio | 1:1 to 2:1 | Standard | OK |

**Issues found:**

1. **[FLAG — Minor] NiCl2 Ni content description:** The CW states NiCl2-6H2O is "~25% Ni by weight." The actual nickel content of NiCl2-6H2O (MW = 237.7 g/mol, Ni = 58.7 g/mol) is 24.7%, so "~25%" is acceptable. No correction needed — this is just a note for completeness.

2. **[FLAG — Minor] NiSO4 Ni content description:** States "~22% Ni by weight." NiSO4-6H2O (MW = 262.8 g/mol) contains 22.3% Ni. Acceptable.

3. **[FLAG — Minor] Hull cell temperature:** States "140 F." This is correct for a Watts bath Hull cell — the test should be run at bath temperature.

**Contamination thresholds:** Cu >5 ppm, Zn >10 ppm, Fe >25 ppm, Cr(VI) >1 ppm, Pb >1 ppm — all consistent with Nickel Institute and industry data.

**Notes:** Very solid workup. The boric acid solubility note (39 g/L at 68 F, 54 g/L at 140 F) is accurate and a strong educational addition. The low-pH dummying protocol (pH 3.0, 2--5 ASF) is correct. All flags are informational only — no corrections needed.

---

## Poster 76 — Nickel-Cobalt Plating Main Tank

**Status:** FLAG (review recommended)

**Parameters reviewed:**

| Parameter | CW Value | Industry Standard | Verdict |
|---|---|---|---|
| Ni sulfamate (as salt) | 300--400 g/L | 300--450 g/L | OK |
| CoSO4-7H2O | 10--60 g/L | 5--60 g/L typical (highly variable by spec) | OK |
| Boric acid | 30--45 g/L | 30--45 g/L | OK |
| NiCl2 | 5--15 g/L (0--15 listed in component box) | 0--15 g/L | OK |
| pH | 3.5--4.5 | 3.5--4.5 typical sulfamate NiCo | OK |
| Temperature | 120--140 F (49--60 C) | 110--150 F | OK |
| CD | 20--60 ASF (rack) | 20--80 ASF | OK |
| Cathode efficiency | 90--98% | 90--98% | OK |
| Anodes | Ni S-rounds in Ti baskets, no cobalt anodes | Correct | OK |
| A:C ratio | 1:1 to 2:1 | Standard | OK |
| Deposit Co content | 15--35% by weight | 10--40% per application | OK |
| Hardness (as-plated) | 400--500 HV | 350--550 HV typical | OK |
| Hardness (heat-treated) | 600--700 HV (in frontmatter) | 550--750 HV | OK |

**Issues found:**

1. **[FLAG — Medium confidence] Cobalt deposit percentage and anomalous codeposition claim:** The CW states "A bath with 10% Co (by metal weight) can produce a deposit with 20--30% Co." This is directionally correct — anomalous codeposition of iron-group metals (Fe, Co, Ni) is a well-documented phenomenon. The degree of anomaly depends heavily on bath conditions. The specific numbers (10% bath -> 20--30% deposit) are plausible but should be understood as illustrative, not universal. The general principle is correct. **No correction needed, but recommend adding a qualifier like "under typical conditions" to the callout.**

2. **[FLAG — Low priority] Alloy control gauge — CD and temperature effects:** The CW states that higher CD increases Co% and higher temperature decreases Co%. This is CORRECT for anomalous codeposition in the Ni-Co system. Higher current density (closer to mass-transport limiting conditions) favors the less-noble metal (Co). Higher temperature increases diffusion rates and reduces the anomalous effect. The science is sound.

3. **[FLAG — Minor] OSHA PEL for cobalt:** The CW states "0.02 mg/m3 TWA." The current OSHA PEL for cobalt metal dust and fume is 0.1 mg/m3 (8-hr TWA). However, ACGIH TLV is 0.02 mg/m3. **The CW appears to be citing the ACGIH TLV, not the OSHA PEL.** This should be corrected to either: (a) state the correct OSHA PEL of 0.1 mg/m3, or (b) clarify that 0.02 mg/m3 is the ACGIH TLV, not the OSHA PEL. **Recommend correction before Generation Prompt.**

4. **[FLAG — Informational] IARC classification for cobalt compounds:** CW states "IARC Group 2B: Possibly carcinogenic to humans." This is correct for cobalt and cobalt compounds (IARC Monograph 86, 2006). Cobalt metal with tungsten carbide is Group 2A, but cobalt sulfate and other soluble compounds are Group 2B. Correct as stated.

**Notes:** Strong workup overall. The anomalous codeposition explanation is well done and accurate. The "no cobalt anodes" callout is critical and correct — cobalt is replenished only by chemical addition. The OSHA PEL error (Flag 3) should be corrected before the Generation Prompt is written.

---

## Poster 84 — Chrome Plating (Decorative) Main Tank

**Status:** FLAG (review recommended)

**Parameters reviewed — Trivalent (Cr III):**

| Parameter | CW Value | Industry Standard | Verdict |
|---|---|---|---|
| Cr3+ | 4--8 g/L | 3--10 g/L | OK |
| pH | 2.5--4.0 | 2.5--4.0 | OK |
| Temperature | 80--120 F (27--49 C) | 80--120 F | OK |
| CD | 50--200 ASF | 50--200 ASF | OK |
| Cathode efficiency | 15--30% | 10--30% | OK |
| Deposit thickness | 0.15--0.50 um | 0.1--0.5 um | OK |
| Anodes | Graphite or MMO on Ti | Correct | OK |

**Parameters reviewed — Hexavalent (Cr VI):**

| Parameter | CW Value | Industry Standard | Verdict |
|---|---|---|---|
| CrO3 | 200--400 g/L | 200--400 g/L (250 g/L typical for decorative) | OK |
| CrO3:SO4 ratio | 100:1 | 100:1 classic ratio | OK |
| Sulfate (SO4) | 2.0--4.0 g/L | 2.0--4.0 g/L at 200--400 g/L CrO3 | OK |
| Temperature | 95--120 F (35--49 C) | 95--115 F typical decorative | OK |
| CD | 100--300 ASF | 100--300 ASF | OK |
| Cathode efficiency | 10--18% | 8--18% | OK |
| Deposit thickness | 0.25--0.75 um | 0.2--0.8 um | OK |
| Cr3+ limit | < 10--15 g/L | < 2--3% of total Cr is optimal | See flag |
| Anodes | Lead or Pb-Sn (93:7) | Correct | OK |
| PbO2 film maintenance | Called out | Correct | OK |

**Issues found:**

1. **[FLAG — Medium] Hex chrome Cr3+ limit stated as "< 10--15 g/L":** At 250 g/L CrO3, the Cr content is approximately 130 g/L (Cr = 52/100 of CrO3). 10--15 g/L Cr3+ would be 7.7--11.5% of total chromium. Industry best practice is to keep Cr3+ below 2--3% of total chromium content (i.e., below about 2.6--3.9 g/L at 250 g/L CrO3). At 400 g/L CrO3, 10--15 g/L Cr3+ would be about 4.8--7.2% of total Cr, which is already problematic. **The stated range of 10--15 g/L is on the high side and represents the upper limit where problems become severe, not the operating target.** Recommend revising to: "Cr3+ monitoring: keep < 2--3% of total Cr (typically < 3--5 g/L). Above 10 g/L: serious bath performance degradation." **Confidence: High.**

2. **[FLAG — Minor] Hex temperature upper limit 120 F:** Most decorative hex chrome references cite 105--115 F as the optimal range for decorative work, with 120 F being the absolute upper boundary before you start losing bright range. The CW range of 95--120 F is acceptable but the optimal of 105--115 F should be emphasized. Already stated in the CW. No correction needed.

3. **[FLAG — Informational] CrO3:SO4 ratio:** The classic 100:1 ratio is correctly stated. Some modern baths use mixed catalyst (sulfate + fluoride) systems at different ratios, but for a general educational poster, 100:1 is the right number. Correct.

4. **[FLAG — Informational] Lead anode alloy:** Stated as Pb-Sn 93:7. The standard composition is 93% Pb / 7% Sn (sometimes cited as 6--8% Sn). Correct.

**Notes:** Good dual-chemistry presentation. The bright range chart concept is excellent — this is the single most important diagnostic tool for chrome plating. The Cr3+ limit flag (Issue 1) should be addressed before the Generation Prompt to avoid giving the impression that 10--15 g/L Cr3+ is acceptable operation.

---

## Poster 100 — Copper Plating (Acid) Main Tank

**Status:** PASS

**Parameters reviewed:**

| Parameter | CW Value | Industry Standard | Verdict |
|---|---|---|---|
| CuSO4-5H2O | 180--250 g/L | 180--260 g/L | OK |
| Cu metal | 45--65 g/L | 45--75 g/L | OK |
| H2SO4 | 45--100 g/L | 30--100 g/L (wide range by application) | OK |
| Cl- | 30--80 ppm (optimal 40--60) | 30--80 ppm typical | OK |
| Temperature | 70--80 F (21--27 C) | 68--85 F | OK |
| CD (rack) | 20--40 ASF | 15--40 ASF | OK |
| Cathode efficiency | ~100% | 97--100% | OK |
| Anodes | Phosphorized Cu (0.04--0.06% P) in Ti baskets | Correct (0.04--0.065% P standard) | OK |
| Anode bags | PP, 1--2 um | Correct | OK |
| A:C ratio | 1:1 to 2:1 | Standard | OK |
| pH | Not measured (strongly acidic) | Correct | OK |

**Contamination thresholds and defects:** All consistent with published data.

**Notes:** Excellent workup. The phosphorized anode callout with the Cu+ disproportionation explanation is technically correct and critically important. The chloride gauge (30--80 ppm window) is accurate. The brightener system description (carrier/suppressor = PEG-type, brightener/accelerator = SPS-type, leveler = N-containing) correctly identifies the three-component organic additive system used in modern acid copper. This poster is ready for Generation Prompt as-is.

---

## Poster 116 — Tin Plating Main Tank

**Status:** PASS

**Parameters reviewed — Acid Sulfate:**

| Parameter | CW Value | Industry Standard | Verdict |
|---|---|---|---|
| SnSO4 | 30--80 g/L | 30--80 g/L | OK |
| Sn2+ | 15--45 g/L (optimal 20--30) | 15--40 g/L | OK |
| H2SO4 | 100--200 g/L (optimal 130--170) | 100--200 g/L | OK |
| Temperature | 60--85 F (16--29 C) | 60--85 F | OK |
| CD (rack, sulfate) | 10--30 ASF | 10--30 ASF | OK |
| Cathode efficiency (sulfate) | 85--95% | 85--95% | OK |

**Parameters reviewed — MSA:**

| Parameter | CW Value | Industry Standard | Verdict |
|---|---|---|---|
| Stannous methanesulfonate | 40--100 g/L | 40--100 g/L | OK |
| Sn2+ (MSA) | 20--55 g/L (optimal 30--40) | 20--55 g/L | OK |
| Free MSA | 100--250 g/L (optimal 150--200) | 100--250 g/L | OK |
| CD (rack, MSA) | 10--100 ASF | 10--100+ ASF (MSA allows very high speed) | OK |
| Cathode efficiency (MSA) | 90--99% | 90--99% | OK |

**Common parameters:**

| Parameter | CW Value | Industry Standard | Verdict |
|---|---|---|---|
| Anodes | Pure tin 99.9%+, bars or balls in Ti baskets | Correct | OK |
| Anode bags | PP, required | Correct | OK |
| No air agitation | Prominently called out | Correct — critical | OK |
| A:C ratio | 1:1 to 2:1 | Standard | OK |

**Contamination thresholds:** Fe >20 ppm, Cu >5 ppm, Pb >2 ppm, Cl- >10 ppm (sulfate bath), Sn4+ >10% of total — all consistent with published data.

**Notes:** Very well done. The dual-bath presentation (sulfate vs. MSA) is well structured. The "NO AIR AGITATION" callout is the most important safety/process message on the poster and is correctly emphasized. The Sn2+/Sn4+ oxidation gauge is an excellent educational tool. The tin whiskers defect entry correctly cross-references mitigation (Ni underplate, reflow, Bi alloying). No corrections needed.

---

## Poster 124 — Gold Plating Main Tank

**Status:** FLAG (review recommended)

**Parameters reviewed:**

| Parameter | CW Value | Industry Standard | Verdict |
|---|---|---|---|
| Au | 8--12 g/L | 4--16 g/L (8--12 typical for acid hard gold) | OK |
| Hardener (Co or Ni) | 1.0--2.0 g/L | 0.1--0.3% in deposit; bath conc varies widely | See flag |
| Citric acid/citrate buffer | 80--120 g/L | 60--120 g/L | OK |
| pH | 4.0--4.5 | 3.5--5.0 (4.0--4.5 typical for citrate-based) | OK |
| Temperature | 100--120 F (38--49 C) | 90--130 F (100--120 typical) | OK |
| CD (rack) | 5--10 ASF | 3--10 ASF | OK |
| CD (barrel) | 1--3 ASF | 0.5--3 ASF | OK |
| Cathode efficiency | 30--50% | 25--50% | OK |
| Anodes | Platinized titanium (Pt/Ti), insoluble | Correct | OK |
| A:C ratio | 1:1 to 3:1 | Up to 3:1 or higher | OK |
| Hardness | 130--200 HK | 130--200 HK (acid hard gold with Co) | OK |

**Issues found:**

1. **[FLAG — Medium] Hardener concentration "1.0--2.0 g/L" needs clarification:** The CW states the hardener (Co or Ni) concentration is 1.0--2.0 g/L. For cobalt-hardened acid gold baths, typical cobalt concentrations in the bath solution range from roughly 0.5--2.0 g/L as cobalt metal, depending on the proprietary system. The stated range is within the broad industry window. However, the deposit cobalt content is typically 0.1--0.3% by weight (for Type III hard gold per ASTM B488), which is a very different number from the bath concentration. **Recommend adding a note distinguishing bath Co concentration from deposit Co content to avoid confusion.** The bath numbers as stated are plausible. **Confidence: Medium — this varies significantly by proprietary system.**

2. **[FLAG — Informational] Gold theoretical consumption:** The CW states "12.25 g Au / 1000 amp-min." Let me verify: Faraday's law for Au+ (MW = 197.0, n = 1, F = 96485 C/mol): mass = (I x t x MW) / (n x F). For 1000 amp-min = 60000 A-s: mass = (60000 x 197.0) / (1 x 96485) = 122.5 g at 100% efficiency. At 100% efficiency this would be 122.5 g per 1000 amp-min, or 12.25 g per 100 amp-min. **The CW states "12.25 g Au / 1000 amp-min" but the correct value at 100% efficiency is 12.25 g / 100 amp-min (or 122.5 g / 1000 amp-min).** However, at the stated 30--50% cathode efficiency, actual consumption would be about 3.7--6.1 g per 100 amp-min, or 37--61 g per 1000 amp-min. **This appears to be a decimal place error. Recommend verifying and correcting. Confidence: High.**

3. **[FLAG — Low priority] Chloride threshold "> 1 ppm — attacks gold complex — catastrophic":** This is correct for cyanide-based gold baths where chloride can decompose the gold cyanide complex. For some acid gold citrate systems, chloride tolerance can be slightly higher (up to ~5 ppm depending on formulation), but calling it catastrophic at >1 ppm is defensible as a conservative general guideline. No correction needed.

**Notes:** Good workup overall. The "GOLD ADDED BY CHEMICAL ADDITION" callout is critical and correct. The gold tracking/accountability section is a strong practical addition. **The theoretical consumption figure (Flag 2) should be corrected before the Generation Prompt — this is a math error that a knowledgeable reader would catch immediately.**

---

## Poster 132 — Silver Plating (Cyanide) Main Tank

**Status:** FLAG (minor)

**Parameters reviewed — Strike Bath:**

| Parameter | CW Value | Industry Standard | Verdict |
|---|---|---|---|
| Ag (as metal) | 1--6 g/L (target 3--5) | 1--6 g/L | OK |
| Free KCN | 75--120 g/L (target 90--100) | 60--120 g/L | OK |
| Temperature | 70--80 F | 65--85 F | OK |
| CD | 10--20 ASF (target) | 5--30 ASF | OK |
| Time | 15--30 sec | 10--60 sec | OK |
| CN:Ag ratio | ~20:1 to 30:1 (stated) | High ratio, typically 15:1 to 30:1 | OK |

**Parameters reviewed — Plate Bath:**

| Parameter | CW Value | Industry Standard | Verdict |
|---|---|---|---|
| Ag (as metal) | 30--50 g/L (target 35--45) | 25--50 g/L | OK |
| Free KCN | 75--150 g/L (target 100--120) | 30--150 g/L (varies widely) | OK |
| K2CO3 | < 75 g/L | < 75--100 g/L | OK |
| Temperature | 75--85 F (target) | 70--90 F | OK |
| CD (rack) | 8--15 ASF | 5--20 ASF | OK |
| CD (barrel) | 2--4 ASF | 1--5 ASF | OK |
| Cathode efficiency | 95--100% | 95--100% | OK |
| Anodes | Pure silver 99.9%+, in bags | Correct | OK |
| A:C ratio | 1:1 to 2:1 | Standard | OK |

**Issues found:**

1. **[FLAG — Minor] Free cyanide ratio not explicitly specified as a number for the plate bath:** The CW correctly identifies free cyanide as "THE MASTER CONTROL" and includes a gauge, but the gauge shows qualitative zones (low/optimal/high) without specifying the actual CN:Ag ratio target for the plate bath. Industry standard for the plate bath is approximately 2:1 to 4:1 (free KCN : Ag metal, by weight). For example, at 40 g/L Ag and 120 g/L free KCN, the ratio is 3:1. **Recommend adding the explicit ratio range (2:1 to 4:1 by weight) to the gauge or composition table. This is the single most referenced control parameter in silver plating.** Confidence: High.

2. **[FLAG — Informational] Strike CN:Ag ratio stated as "~20:1 to 30:1":** At 3 g/L Ag and 90 g/L KCN, the ratio is 30:1. At 5 g/L Ag and 75 g/L KCN, the ratio is 15:1. The stated range is consistent with the parameter ranges given. OK.

3. **[FLAG — Informational] Brightener system:** The CW describes antimony-based grain refiners and selenium co-brighteners. This is correct for conventional bright silver plating. The note about bright silver having lower conductivity than matte silver for RF applications is accurate and a strong practical detail.

**Contamination thresholds:** Sulfide (trace), Fe >5 ppm, K2CO3 >75 g/L, Cu >10 ppm — all consistent with published data. Sulfide sensitivity correctly emphasized.

**Notes:** Very well-constructed dual-bath poster. The strike-then-plate workflow is clearly presented. The main recommendation is to add the explicit free CN:Ag ratio number (Flag 1) — operators need that specific number on the wall.

---

## Poster 140 — Cadmium Plating (Cyanide) Main Tank

**Status:** PASS

**Parameters reviewed:**

| Parameter | CW Value | Industry Standard | Verdict |
|---|---|---|---|
| Cd metal | 18--35 g/L (target 22--27) | 15--35 g/L | OK |
| CdO | 20--40 g/L | 20--45 g/L | OK |
| Total NaCN | 90--150 g/L | 90--150 g/L | OK |
| Free NaCN | 15--45 g/L (target 20--30) | 12--45 g/L | OK |
| NaOH | 15--30 g/L (target 20) | 15--37 g/L | OK |
| Temperature | 75--90 F (24--32 C) | 70--90 F | OK |
| CD (rack) | 10--25 ASF | 5--30 ASF | OK |
| CD (barrel) | 3--8 ASF | 2--10 ASF | OK |
| Cathode efficiency | 85--95% | 85--95% | OK |
| Anodes | Pure cadmium 99.95%+, bars or balls | Correct | OK |
| A:C ratio | 1:1 to 2:1 | Standard | OK |

**Acid chloride alternative:**

| Parameter | CW Value | Industry Standard | Verdict |
|---|---|---|---|
| CdCl2 | 25--40 g/L | 20--45 g/L | OK |
| NH4Cl | 150--225 g/L | 150--230 g/L | OK |
| pH | 3.5--5.5 | 3.5--5.5 | OK |
| Temperature | 65--90 F | 65--90 F | OK |
| CD | 10--40 ASF | 10--40 ASF | OK |

**Contamination thresholds:** Cu >5 ppm, Pb >2 ppm, Fe >50 ppm, Cr >1 ppm, carbonate >30 g/L — all consistent with published data.

**Notes:** Very well done. The dual-hazard emphasis (cyanide + carcinogen) is essential and correctly prominent. Leading with HE failure in the defect grid is the right call — hydrogen embrittlement bake failures are the #1 reject in aerospace cadmium plating. The AMS 2759/9 reference for bake requirements is correct. The acid chloride alternative panel provides useful context. No corrections needed.

---

## Summary

| Poster | Process | Status | Action Required Before GP |
|---|---|---|---|
| 44 | Zinc Acid | PASS | None |
| 60 | Nickel Watts | PASS (minor flags, informational only) | None |
| 76 | Nickel-Cobalt | FLAG | Correct OSHA PEL vs. ACGIH TLV (Flag 3) |
| 84 | Chrome Decorative | FLAG | Revise Cr3+ limit guidance (Flag 1) |
| 100 | Copper Acid | PASS | None |
| 116 | Tin | PASS | None |
| 124 | Gold | FLAG | Correct gold consumption figure (Flag 2); clarify hardener bath vs. deposit concentration (Flag 1) |
| 132 | Silver | FLAG (minor) | Add explicit free CN:Ag ratio number to plate bath (Flag 1) |
| 140 | Cadmium | PASS | None |

### Priority Corrections (must fix before Generation Prompt)

1. **Poster 124 (Gold) — Theoretical gold consumption figure:** "12.25 g Au / 1000 amp-min" appears to be off by a factor of 10. Correct value at 100% efficiency is ~12.25 g / 100 amp-min or ~122.5 g / 1000 amp-min. This is a math error visible to any plater who tracks gold.

2. **Poster 84 (Chrome) — Cr3+ limit in hex bath:** Stated as "< 10--15 g/L" which represents severe degradation, not a control target. Revise to indicate that < 3--5 g/L is the operating target and > 10 g/L is the crisis threshold.

3. **Poster 76 (Nickel-Cobalt) — OSHA PEL for cobalt:** Stated as 0.02 mg/m3 which is the ACGIH TLV, not the OSHA PEL (0.1 mg/m3). Either correct the label or cite both.

### Recommended Additions (improve quality, not blocking)

4. **Poster 132 (Silver) — Free CN:Ag ratio for plate bath:** Add explicit ratio (2:1 to 4:1 by weight) — this is the number every silver plater looks for.

5. **Poster 124 (Gold) — Hardener bath vs. deposit clarification:** Distinguish 1.0--2.0 g/L Co in bath from 0.1--0.3% Co in deposit.

---

*Tyler — Plating Chemist*
*Validation completed 2026-04-26*
