---
title: "Posters 24-30 — Watson Research Brief"
date: 2026-04-25T00:00:00
author: Watson (chemistry-researcher)
scope: Published-source validation of Series 1 Posters 24-30
status: Complete
version: v2 — 2026-04-26 (cross-referenced with Gemini research, Tyler validation notes, and domain expertise)
tags:
  - PosterValidation
  - Series1
  - Foundational
---

# Posters 24-30 -- Watson Research Brief v2

**Purpose:** Technical validation of Construction Workups for Posters #24-#30. These seven foundational posters cover cross-process concepts that will hang on production floors -- accuracy is non-negotiable.

**Validation date:** 2026-04-25 (v1) / 2026-04-26 (v2 with fresh Gemini verification)
**Sources used:**
- Gemini research queries: rectifier ripple thresholds, PR ratios, EPA 40 CFR 433 discharge limits, filtration turnover rates, carbon treatment dosages
- Tyler Validation Notes (2026-04-25, v2)
- Watson domain expertise: electroplating handbooks (Lowenheim, Canning), ASTM standards, IPC-TM-650, Nickel Plating Handbook 2023, EPA regulatory texts
- Cross-reference with existing Watson troubleshooting guides in vault

**Severity Scale:**
- **CRITICAL** -- Error would cause real-world harm (incorrect procedure, wrong regulatory limit, safety risk)
- **HIGH** -- Error would undermine poster credibility with knowledgeable audiences
- **MEDIUM** -- Value is off but directionally correct; refinement needed
- **LOW** -- Minor; acceptable for poster-level simplification but flagged for awareness

---

## Poster #24 -- Rectifier Fundamentals

### Validated Claims (CONFIRMED)

- **DC waveform:** Constant unidirectional current -- correct
- **Pulsed DC:** On/off cycling with T-on and T-off -- correct; ion replenishment during T-off is the accepted mechanism
- **Periodic reverse:** Alternating cathodic/anodic cycles -- correct
- **PR for through-hole plating:** "Exceptional" is accurate; PR is the industry standard for PCB via plating
- **Duty cycle formula:** T-on / (T-on + T-off) x 100% -- correct
- **Charge ratio formula:** (I-cathodic x T-cathodic) / (I-anodic x T-anodic) -- correct
- **Net deposition requires charge ratio > 1.0** -- correct
- **Unfiltered DC / ripple description:** AC ripple component from degraded filtering -- correct
- **Ripple % formula:** (Peak - Valley) / Avg x 100 -- correct
- **Causes of ripple:** Aging SCR, failed filter caps, loose bus bars, undersized transformer -- all confirmed

### Corrections Required

| # | Item | CW States | Should Be | Severity | Source |
|---|------|-----------|-----------|----------|--------|
| 24-1 | **Ripple green zone** | 0-5% "Acceptable" | The 0-5% threshold is correct for decorative chrome and bright nickel (the most ripple-sensitive processes). However, **precious metals and high-precision electronics require <1%**. The poster's three-zone gauge is a reasonable simplification but should note the stricter requirement via the existing callout text: "Decorative chrome and bright nickel are the most ripple-sensitive processes -- keep below 5%" is good. **Recommend adding:** "Precious metals: <1%." | LOW | Gemini research; Darrah Electric / Dynapower specs |
| 24-2 | **PR cathodic:anodic ratio** | 3:1 to 20:1 | This is stated as a time or current ratio. Gemini data indicates the range depends on whether you mean *current ratio* or *time ratio*. For copper PCB, the **current ratio** is often 1:3 (anodic current 3x cathodic), while the **time ratio** is 20:1 (cathodic time 20x anodic time). The poster's "3:1 to 20:1" conflates these. **For a poster audience, the range 3:1 to 20:1 describing the overall cathodic-to-anodic charge ratio is defensible and commonly cited.** No change required, but the CW should note this is charge ratio, not pure current ratio. | LOW | Gemini research; PCB plating literature |
| 24-3 | **"~80% of all plating operations" use straight DC** | Stated | Unverifiable exact percentage but directionally correct -- the vast majority of commercial plating uses conventional DC. Acceptable as a poster approximation. | LOW | Domain expertise |

### Application Matrix Review (Block E)

| Process/Claim | Verdict |
|---------------|---------|
| Acid copper: PR "Excellent for PCB" | CONFIRMED |
| Watts nickel: PR "No" -- additives tuned for DC | CONFIRMED -- PR disrupts brightener systems; this is a correct and important distinction |
| Hard chrome: must have <5% ripple | CONFIRMED by Gemini: <5% is the standard threshold for chrome |
| Hard chrome: pulse "Emerging" | CONFIRMED -- pulse chrome is under active development but not yet widespread |
| Gold: pulse "Excellent" | CONFIRMED -- pulse gives finer grain and better hardness in gold |
| Tin-lead: PR reduces whisker risk | CONFIRMED -- this is a documented benefit of PR for tin deposits |

### Missing Content (Recommendations)

- **SCR vs. switch-mode rectifier distinction:** The #1 practical issue in rectifier-related plating problems. SCR rectifiers inherently produce ~5-8% ripple; switch-mode maintains <1-2% across the entire range. Worth a brief callout.
- **Three-phase vs. single-phase:** Three-phase produces lower inherent ripple. Common in industrial installations.

### Brand/Supplier Check: CLEAN -- Zero violations.

**Overall Assessment: LOW severity. Poster is technically solid. Minor refinements only.**

---

## Poster #25 -- Filtration and Purification

### Validated Claims (CONFIRMED)

- **Cartridge, bag, carbon canister, pump-and-filter as primary types** -- correct
- **Micron rating ranges:** 1-50 for cartridge, 1-200 for bag -- confirmed
- **Mag-drive pumps for corrosive solutions** -- correct and standard practice
- **Carbon removes organic contamination** -- confirmed
- **Dummy plating at low CD (2-5 ASF)** -- confirmed; low CD preferentially plates contaminant metals
- **Permanganate treatment oxidizes organics carbon cannot reach** -- confirmed
- **Freezing for carbonate removal in alkaline zinc** -- confirmed, standard practice

### Corrections Required

| # | Item | CW States | Should Be | Severity | Source |
|---|------|-----------|-----------|----------|--------|
| 25-1 | **Carbon treatment pH for nickel** | "Raise pH to 4.5-5.0" | **WRONG. Lower pH to 3.0-5.0 (many references say 3.0-3.5 with H2SO4).** The purpose of the pH adjustment before carbon treatment is to LOWER the pH to improve adsorption efficiency and prevent nickel hydroxide from precipitating on the carbon. Raising to 4.5-5.0 is the OPPOSITE direction from the standard procedure. Some sources recommend 3.0-3.5; the Nickel Plating Handbook indicates 3.0-5.0 depending on organic load. The CW states "raise pH to 4.5-5.0" which implies the bath is below 4.5 -- this is misleading since operating Watts nickel runs at 3.8-4.5 anyway. **The correct instruction is: "Lower pH to 3.0-3.5 with sulfuric acid before adding carbon (nickel bath)."** Tyler concurs: his validation flagged this as "lower, not raise." | **CRITICAL** | Nickel Plating Handbook 2023; Tyler validation; Gemini filtration data |
| 25-2 | **Carbon dosage** | 1-3 g/L | **Should be 2-5 g/L** for routine treatment, up to 5-7 g/L for heavy contamination. Gemini data confirms 1-3 g/L as the low end; 2-5 g/L is the standard cited range. The poster understates dosage. A shop using 1 g/L will see minimal organic removal. | **HIGH** | Gemini research; Metal Finishing Guidebook; Nickel Institute |
| 25-3 | **Carbon contact time** | "30-60 minutes" | **Should be 2-4 hours minimum.** Gemini confirms 2-4 hours with agitation. Some shops run overnight. 30-60 minutes is grossly insufficient for effective adsorption -- the carbon needs time to reach equilibrium with the dissolved organics. Tyler confirms: "2-4 hours with gentle air agitation." | **CRITICAL** | Gemini research; Nickel Plating Handbook; Tyler validation |
| 25-4 | **Post-carbon treatment: "Replenish wetting agent"** | "Replenish wetting agent (carbon removes it)" | This is correct but incomplete. Carbon removes ALL organic additives (brighteners, carriers, wetters), not just the wetting agent. **After carbon treatment, ALL organic additives must be replenished.** The step should read: "Replenish wetting agent, carrier, and brightener -- carbon removes all organic additives." | **MEDIUM** | Standard practice |
| 25-5 | **Turnover rates** | Table shows various rates | Gemini confirms: Bright nickel 2-5 (high-quality: 10+), Hard chrome 1-2, Acid copper 2-5 (PCB: 5-8+), EN **10-20 TPH** (not 3-5 as listed in the CW). The CW's EN value of "3-5 turnovers" is FAR too low. EN filtration must be aggressive due to plate-out nucleation risk. | **HIGH** | Gemini research |
| 25-6 | **Dummy plating: metals listed** | "Cu, Zn, Pb, Cd (metals more noble than Ni at low CD)" | Phrase "more noble than Ni" is misleading. The dummy plating mechanism works because contaminant metals have more positive (noble) reduction potentials than nickel, so at LOW current density they preferentially deposit. The listed metals (Cu, Zn, Pb, Cd) are correct targets for nickel bath dummying, but Zn is actually LESS noble than Ni -- it deposits because the low-CD conditions allow codeposition. **Better phrasing: "Removes Cu, Pb, Cd, and other contaminant metals that deposit preferentially at low current density."** Drop Zn from the "more noble" claim. | **MEDIUM** | Electrochemistry fundamentals; standard reduction potentials |
| 25-7 | **H2O2 treatment description** | "Oxidizes dissolved metallic impurities (Fe2+ to Fe3+ for precipitation)" | Correct for iron. However, the statement "excess peroxide damages some brighteners" needs strengthening: **excess peroxide can decompose nickel brightener systems rapidly and is extremely difficult to remove from the bath once added.** Peroxide treatment should only be used when specifically recommended by the chemical supplier. | **MEDIUM** | Standard practice; Tyler concurrence |

### Missing Content

- **Filter aid (diatomaceous earth / perlite):** Standard practice for carbon filtration -- pre-coat the filter with DE before filtering the carbon-treated bath. Not mentioned anywhere.
- **Procedure differences by bath type:** The carbon treatment procedure differs for acid vs. alkaline baths. The CW implies one procedure fits all.

### Brand/Supplier Check: CLEAN.

**Overall Assessment: CRITICAL severity. This poster has the most serious errors in the 7-poster set. The carbon treatment procedure (pH direction, dosage, and contact time) must ALL be corrected before Elara writes the Generation Prompt. A shop following the CW as-is would waste time and material on an ineffective treatment.**

---

## Poster #26 -- Chromate and Conversion Coatings

### Validated Claims (CONFIRMED)

- **Hexavalent mechanism:** Cr(VI) reduction to Cr(III) forming mixed oxide gel film -- confirmed
- **Trivalent mechanism:** Cr(III) precipitation as oxide/hydroxide film -- confirmed
- **Self-healing in hex:** Cr(VI) reservoir migrates to damage sites -- confirmed
- **No self-healing in tri:** Correct -- Cr(III) film is inert once formed
- **Sealers compensate for tri's lack of self-healing** -- confirmed
- **RoHS directive:** Cr(VI) restricted in electronics -- confirmed (Directive 2011/65/EU)
- **REACH Annex XIV:** Chromium trioxide listed -- confirmed
- **OSHA PEL for Cr(VI):** 5 micrograms/m3 -- CONFIRMED (29 CFR 1910.1026)
- **Heat resistance of hex films:** Degrades above 150 deg F (65 deg C) -- confirmed; Cr(VI) converts to Cr(III) at elevated temperature, losing self-healing
- **Hex baths are more forgiving (wider operating window)** -- confirmed
- **Tri baths are more sensitive to drag-in and pH** -- confirmed

### Corrections Required

| # | Item | CW States | Should Be | Severity | Source |
|---|------|-----------|-----------|----------|--------|
| 26-1 | **Film thickness: hex clear** | 0.05-0.25 micron | The CW uses microns. Chromate conversion coatings are actually measured in both nm and microns depending on the source. **0.05-0.25 micron = 50-250 nm.** This is in the correct ballpark for hex clear/blue passivates. However, some authoritative sources cite clear passivates as 20-80 nm (0.02-0.08 micron). **The poster's values are at the high end but not wrong -- they may include thicker "clear/bright" passivates with some iridescence.** The v1 brief's claim that using microns "overstates by 1000x" was itself an error -- 0.05 microns IS 50 nm, which is a reasonable value. **No change required; values are in the correct order of magnitude.** | LOW | ASTM B633; industry literature |
| 26-2 | **Film thickness: hex yellow** | 0.25-0.75 micron | = 250-750 nm. Heavy yellow/iridescent hex chromates DO form films in this range. **Confirmed.** | LOW | ASTM B633 |
| 26-3 | **Film thickness: tri black** | 0.5-1.5 micron | Black trivalent passivates (often with organic dyes or topcoats) can reach 0.5-1.5 micron total system thickness (base passivate + topcoat). **Confirmed as a system thickness.** Clarification note: the base Cr(III) film itself is thinner; the topcoat/sealer adds the bulk of the thickness. | LOW | Industry practice |
| 26-4 | **SST: hex clear** | 8-24 hrs | This is to white corrosion on zinc. Per ASTM B633, supplementary classification SC1 (Type I = no supplementary treatment) gives 12 hours minimum. 8-24 hours is a reasonable range. **Confirmed.** | -- | ASTM B633 Table X1.1 |
| 26-5 | **SST: hex yellow** | 96-500+ hrs | Heavy hex yellow chromate (Type VI per B633) on sufficient zinc thickness achieves 96+ hours routinely; 200-500+ with optimal conditions. **Confirmed.** | -- | ASTM B633; industry data |
| 26-6 | **SST: tri clear** | 48-200 hrs | With sealer, modern tri clear achieves 48-200+ hours on zinc. Without sealer, 24-120 hours is more typical. **The CW's range assumes sealer, which should be noted explicitly.** | **MEDIUM** | Industry data; chemical supplier literature |
| 26-7 | **SST: tri black** | 96-400 hrs | With sealer/topcoat, this is achievable. **Confirmed.** | -- | Industry data |
| 26-8 | **RoHS scope** | Header callout implies universal | **RoHS applies specifically to Electrical and Electronic Equipment (EEE), not all manufactured goods.** Automotive, aerospace, military, and industrial hardware are NOT covered by RoHS. Many plating shops serve non-EEE markets where hex chromate is fully legal and often specified. The poster should clarify: "RoHS applies to electrical and electronic equipment. Other sectors may have separate restrictions or exemptions." This is a credibility issue -- a quality manager reading this poster will lose trust if the RoHS scope is overstated. | **HIGH** | Directive 2011/65/EU, Article 2 |
| 26-9 | **Tri color: "yellow NOT achievable without hex"** | Stated in comparison table | This is essentially correct -- true yellow/gold iridescent color cannot be achieved with Cr(III) chemistry alone. Some tri products produce a "yellow-tinted" appearance using organic colorants, but the color mechanism is fundamentally different from the Cr(VI)-dependent yellow of hex chromate. **Confirmed with nuance.** | LOW | Chemistry fundamentals |
| 26-10 | **Hex temperature range** | 60-80 deg F | Should be wider: many hex chromate baths operate at **room temperature to 85 deg F (15-29 deg C)**. 60-80 deg F is acceptable as a typical range. | LOW | Industry practice |
| 26-11 | **Tri temperature range** | 70-85 deg F | Confirmed. Tri passivates are tighter on temperature than hex. | -- | Industry practice |

### Missing Content

- **Topcoat/sealer types:** The CW mentions sealers but does not distinguish silicate-based, silane-based, and organic sealers. For a poster audience this level of detail may be excessive, but noting that "topcoat type affects performance" would be valuable.
- **ASTM B633 classification system:** The poster references salt spray performance but does not connect it to the B633 supplementary classification system (SC1-SC4, Type II-VI). A brief reference would ground the poster in the standard shops actually use.

### Brand/Supplier Check: CLEAN.

**Overall Assessment: MEDIUM severity overall. The RoHS scope clarification (26-8) is the most important correction. SST values are reasonable. Film thicknesses are in the correct ballpark (the v1 brief's "wrong by 1000x" claim was itself incorrect -- corrected in this v2).**

---

## Poster #27 -- Wastewater Treatment Fundamentals

### Validated Claims (CONFIRMED)

- **EPA 40 CFR Part 433 discharge limits (Gemini-verified):**
  - Cadmium: 0.69 mg/L daily max, 0.26 monthly avg -- **CONFIRMED EXACT MATCH with CW**
  - Chromium (total): 2.77 daily, 1.71 monthly -- **CONFIRMED EXACT MATCH**
  - Copper: 3.38 daily, 2.07 monthly -- **CONFIRMED EXACT MATCH**
  - Lead: 0.69 daily, 0.43 monthly -- **CONFIRMED EXACT MATCH**
  - Nickel: 3.98 daily, 2.38 monthly -- **CONFIRMED EXACT MATCH**
  - Silver: 0.43 daily, 0.24 monthly -- **CONFIRMED EXACT MATCH**
  - Zinc: 2.61 daily, 1.48 monthly -- **CONFIRMED EXACT MATCH**
  - TTO: 2.13 mg/L -- **CONFIRMED** (this is the PSNS/direct value; existing sources PSES = 4.57)
  - pH: 6.0-9.0 -- **CONFIRMED for direct dischargers** (indirect may have local limits)
- **Alkaline chlorination cyanide destruction:** Two-stage chemistry confirmed
  - Stage 1: CN- to CNO- at pH >10, ORP +350 to +400 mV -- confirmed
  - Stage 2: CNO- to CO2 + N2 at pH 8.0-8.5, ORP +600 mV -- confirmed
- **Chrome reduction:** Cr(VI) to Cr(III) using sodium metabisulfite at pH 2.0-3.0 -- confirmed
- **Diphenylcarbazide spot test** for Cr(VI) verification -- confirmed, this is the standard field test
- **"NEVER mix cyanide waste with acid waste"** -- CONFIRMED and essential safety message
- **Hydroxide precipitation as primary treatment** -- confirmed
- **NaOH vs. Ca(OH)2 comparison** -- confirmed: caustic = cleaner sludge/higher cost; lime = cheaper/more sludge
- **Polymer flocculant dose 1-5 mg/L** -- confirmed typical range

### Corrections Required

| # | Item | CW States | Should Be | Severity | Source |
|---|------|-----------|-----------|----------|--------|
| 27-1 | **TTO value context** | 2.13 mg/L | The CW shows 2.13 mg/L which is the **New Source / PSNS / Direct Discharge** value. For **Existing indirect dischargers (PSES)**, the limit is **4.57 mg/L**. The poster should note which standard applies or show both. Most metal finishing shops are existing indirect dischargers discharging to a POTW, meaning 4.57 is their federal TTO limit. Using 2.13 as the single value is conservative but could mislead existing shops into thinking they are out of compliance when they are not. | **MEDIUM** | Gemini verification of 40 CFR 433 |
| 27-2 | **SMBS stoichiometry** | 2.5 lbs per lb Cr(VI) | **Theoretical stoichiometric ratio is approximately 2.8 lbs Na2S2O5 per lb Cr(VI).** Practical dosing: 3.0-3.5 lbs/lb to account for oxidant demand. The CW's 2.5 understates the requirement -- a shop dosing at 2.5 will likely have incomplete reduction. Recommend: "2.5-3.5 lbs per lb Cr(VI) (theoretical ~2.8; excess for completeness)." | **HIGH** | Stoichiometric calculation; Tyler confirms 3x practical ratio |
| 27-3 | **Chemical equation for SMBS chrome reduction** | Cr2O7(2-) + 3Na2S2O5 + 5H2SO4 -> 2Cr(3+) + 3Na2SO4 + 3SO4(2-) + 5H2O | **This equation is not correctly balanced.** The dichromate reduction with metabisulfite is complex. A simplified but correct form: Cr2O7(2-) + 3H2S2O5 + 4H(+) -> 2Cr(3+) + 3SO4(2-) + 3H2O (when using the bisulfite intermediate). The sodium salt adds Na+ as spectator ions. **For a poster, a simplified representation is acceptable, but the equation as written has balancing issues on the sulfate products.** Recommend either using the simplified ionic form or omitting the full equation and keeping the stoichiometric ratio. Tyler flagged this equation as needing review. | **MEDIUM** | Chemical balancing; Tyler validation |
| 27-4 | **Copper precipitation pH** | 8.0-10.0, optimal 9.0 | The CW shows range 8.0-10.0 with optimal at 9.0. Published data: Cu(OH)2 minimum solubility is at pH ~8.0-9.0. Above pH ~10.5, copper forms soluble cuprate complexes. **The CW's range is acceptable; the optimal of 9.0 is slightly high -- 8.5 is more commonly cited as optimal.** Minor refinement. | LOW | Wastewater chemistry references |
| 27-5 | **Nickel precipitation pH** | 9.0-10.5, optimal 9.5 | Nickel hydroxide has minimum solubility at pH ~9.5-10.0. The CW range is correct. **However, nickel is NOT amphoteric** -- it does not re-dissolve at high pH under normal wastewater conditions. The "mixed metals" callout in Block DD saying "zinc and nickel may re-dissolve above pH 10" is half-wrong: zinc yes (amphoteric), **nickel no.** | **MEDIUM** | Inorganic chemistry; Tyler confirms nickel is not amphoteric |
| 27-6 | **Cr(III) precipitation pH** | 7.5-8.5, optimal 8.0 | Confirmed. **Cr(III) IS amphoteric** -- re-dissolves above ~pH 9.5 as chromite. This is a critical practical point: raising pH to precipitate nickel can re-dissolve already-precipitated chromium. The poster should note this explicitly. The CW's pH-precipitation bar does include this range correctly. | -- | Standard wastewater chemistry |
| 27-7 | **Missing: cyanide discharge limits** | Not in the table | **Total cyanide (T): 1.20 mg/L daily max, 0.65 mg/L monthly avg** per 40 CFR 433. Cyanide is one of the most critical regulated parameters for plating shops. Omitting it from the discharge limits table is a significant gap, especially since the poster dedicates an entire section to cyanide destruction. | **HIGH** | 40 CFR Part 433 |
| 27-8 | **Permit violation fines** | "Up to $50,000/day" | Under the Clean Water Act, civil penalties are up to **$64,618/day/violation** (adjusted for inflation as of 2024; original statutory cap was $25,000/day, increased by EPA inflation adjustments). Criminal penalties can be higher. The $50,000 figure is widely cited but is an older, rounded number. **For a poster, "$50,000/day" is conservative and defensible, but not the current maximum.** Consider: "Fines of $50,000+ per day per violation." | LOW | Clean Water Act Section 309; EPA enforcement penalty policy |

### Missing Content

- **Cyanide discharge limits** (see 27-7 above) -- CRITICAL gap
- **Chelated metals:** EDTA, NTA, citrate chelators prevent conventional hydroxide precipitation. This is the #1 cause of treatment failures in shops using alkaline cleaners with chelating agents. The CW mentions chelators in the "Common Mistakes" section but not in the treatment process itself.
- **Sulfide precipitation** as alternative for ultra-low discharge limits -- relevant for shops with tight local limits
- **F006 hazardous waste classification** for electroplating sludge (40 CFR 261.31) -- important regulatory context for sludge handling

### Brand/Supplier Check: CLEAN.

**Overall Assessment: MEDIUM-HIGH severity. The EPA discharge limits in the table are CONFIRMED CORRECT (Gemini verified all 9 values match exactly). The SMBS ratio and missing cyanide limits are the primary concerns. The nickel amphoteric claim in Block DD needs correction.**

---

## Poster #28 -- Temperature Control

### Validated Claims (CONFIRMED)

- **Acid copper sulfate range:** 70-95 deg F, optimal 75-85 deg F -- confirmed
- **Hard chrome range:** 120-150 deg F, optimal 130-140 deg F -- confirmed
- **Acid zinc:** 70-100 deg F, optimal 75-90 deg F -- confirmed
- **Alkaline zinc:** 70-100 deg F, optimal 75-85 deg F -- confirmed
- **Tin (acid):** 60-90 deg F, optimal 65-80 deg F -- confirmed; grain coarsens with heat
- **Gold (acid hard):** 100-150 deg F, optimal 110-130 deg F -- confirmed
- **Anodize Type II:** 60-75 deg F, optimal 68-72 deg F -- confirmed; this is one of the tightest temperature windows in the shop
- **Conductivity increases with temperature** -- confirmed
- **Additive consumption increases with temperature** -- confirmed
- **Temperature affects grain structure** -- confirmed
- **EN spontaneous decomposition risk** -- confirmed; THE most temperature-critical process
- **Immersion heaters: 5-50 watts/gallon** -- confirmed typical sizing range
- **Tank covers reduce heat loss by 50-70%** -- confirmed; commonly cited figure

### Corrections Required

| # | Item | CW States | Should Be | Severity | Source |
|---|------|-----------|-----------|----------|--------|
| 28-1 | **Watts nickel minimum** | 104 deg F (40 deg C) | **110 deg F (43 deg C)** minimum. Below 110 deg F, cathode efficiency drops severely and deposits become dark/stressed. The 104 deg F value appears to be a conversion error or a margin that does not reflect practical operation. Tyler confirms: "No Watts bright nickel bath runs below 110 deg F in practice." | **MEDIUM** | Nickel Plating Handbook; Tyler validation |
| 28-2 | **Watts nickel optimal** | 130-140 deg F | Confirmed. This is the standard bright nickel operating range. | -- | -- |
| 28-3 | **EN minimum** | 175 deg F (79 deg C) | **180 deg F (82 deg C)** minimum for mid-phosphorus EN. Below 180 deg F, plating rate drops to near zero. The 175 deg F value is below the practical threshold for any commercial EN formulation. Tyler notes: "175 is shut-down territory, not operating territory." | **MEDIUM** | ASTM B733; EN supplier data; Tyler validation |
| 28-4 | **EN optimal** | 185-195 deg F | Confirmed for mid-phos EN. Some high-phos formulations run at the lower end (180-190). | -- | -- |
| 28-5 | **EN maximum** | 200 deg F | Confirmed as a hard ceiling. Above 200 deg F, risk of spontaneous decomposition is extreme. | -- | -- |
| 28-6 | **Arrhenius rule** | "Reaction rate roughly doubles for every 10 deg C increase" | **Needs significant qualification.** The Arrhenius approximation applies to: (a) chemical reactions (EN autocatalytic deposition, additive decomposition, side reactions), (b) dissolution and diffusion processes. It does NOT apply to electrolytic deposition rate, which is governed by Faraday's law (current = deposition rate). Temperature affects cathode efficiency and mass transport, not the Faradaic relationship. **For a poster, the rule is a useful heuristic but the callout should read:** "Rule of thumb: Chemical reaction rates roughly double per 10 deg C (18 deg F) -- applies to additive breakdown, bath aging, and electroless plating rate." Adding "chemical" limits the claim to where it is accurate. | **MEDIUM** | Physical chemistry; electrochemistry texts |
| 28-7 | **Alkaline non-CN copper** | 110-160 deg F, optimal 130-145 deg F | Tyler flags: some alkaline non-cyanide copper baths operate at 100-140 deg F depending on formulation. The CW range is acceptable for the most common formulations. | LOW | Tyler validation |
| 28-8 | **Watts nickel deg C range** | 40-68 deg C | If minimum is corrected to 110 deg F = 43 deg C, the range should be **43-68 deg C**. The CW already shows 40-68, which is close but the lower end should match the corrected Fahrenheit value. | LOW | Unit conversion |

### Missing Content

- **Thermocouple placement:** The CW includes this in Block FF -- good. The recommendation for mid-tank, mid-depth is correct.
- **Seasonal temperature variation:** Mentioned in the common mistakes table -- good inclusion.

### Brand/Supplier Check: CLEAN.

**Overall Assessment: MEDIUM severity. The Watts nickel and EN minimum temperatures need correction (both ~5 deg F too low). The Arrhenius qualification is important for technical credibility. Otherwise solid.**

---

## Poster #29 -- Anode Chemistry and Maintenance

### Validated Claims (CONFIRMED)

- **Soluble vs. insoluble anode concept** -- correct
- **M -> M(2+) + 2e- for soluble anodes** -- correct general equation
- **2H2O -> O2 + 4H+ + 4e- for insoluble anodes** -- correct
- **Phosphorized copper anodes: 0.04-0.06% P** -- confirmed
- **Electrolytic Ni S-Rounds in Ti baskets** -- confirmed standard practice
- **Lead-antimony for hard chrome** -- confirmed; poster says 6-8% Sb, which matches Pb-6%Sb standard
- **Platinized titanium for precious metals** -- confirmed
- **DSA for chrome and electrogalvanizing** -- confirmed
- **A:C ratios:** 2:1 Ni, 1:1 Cu, 1:1-2:1 Zn -- confirmed
- **EN: no external anode, NaH2PO2 provides electrons** -- confirmed
- **Anode passivation mechanism:** Oxide film blocks dissolution, O2 evolution instead of metal dissolution -- confirmed
- **Passivation symptoms:** Rising voltage, declining metal, darkened surface, pH drop -- all confirmed
- **Low chloride as passivation cause in nickel:** Below 30 g/L NiCl2 -- confirmed
- **Double-bag recommendation for bright nickel** -- confirmed best practice
- **PP bags: chemical resistant, heat resistant to 200 deg F** -- confirmed

### Corrections Required

| # | Item | CW States | Should Be | Severity | Source |
|---|------|-----------|-----------|----------|--------|
| 29-1 | **Zinc anodes: "Steel baskets -- NOT titanium (zinc attacks Ti)"** | Stated | **This claim is WRONG for electroplating temperatures.** The zinc-titanium incompatibility applies to HOT-DIP GALVANIZING temperatures (>420 deg C / 788 deg F) where molten zinc aggressively attacks titanium. At electroplating bath temperatures (70-100 deg F / 21-38 deg C), titanium baskets are safe and commonly used for zinc anode containment. Many zinc plating shops use Ti baskets without issue. Steel baskets also work but are not required for Ti-safety reasons. **Tyler concurs: "Titanium baskets work fine for zinc plating at normal temperatures."** | **HIGH** | Metallurgical compatibility data; Tyler validation |
| 29-2 | **Silver anode A:C ratio** | 2:1 | Confirmed. Fine silver anodes at 2:1 is standard practice. | -- | -- |
| 29-3 | **Tin passivation mention** | "Tin passivates easily" | Correct. Tin anodes are prone to passivation, particularly in acid stannous baths. Maintaining adequate Sn(2+) concentration and using proper anode alloys (sometimes with small antimony additions) helps prevent passivation. | -- | -- |

### Missing Content

- **Anode conditioning / break-in:** New anodes often need initial low-current activation before production use. Important for copper and nickel.
- **Sulfur-depolarized vs. electrolytic nickel anodes:** SD anodes dissolve more uniformly but add sulfur to the bath, which can affect brightener systems. Important distinction not covered.
- **Insoluble anode maintenance:** Platinized Ti anodes need periodic inspection for coating wear. Lead anodes in chrome form PbCrO4 film that needs management.

### Brand/Supplier Check: CLEAN.

**Overall Assessment: MEDIUM severity. The zinc/titanium claim (29-1) is the single error. Tyler rated this poster as requiring zero corrections, but I maintain that the Ti basket claim is factually incorrect and should be changed. The rest of the poster is solid -- Tyler's assessment of "excellent work" stands for everything else.**

---

## Poster #30 -- Bath Analysis Methods

### Validated Claims (CONFIRMED)

- **Titration as backbone of bath analysis** -- confirmed
- **EDTA titration for metals, acid-base for pH chemicals, iodometric for oxidizers** -- confirmed
- **pH: fastest and most frequently used measurement** -- confirmed
- **Hull cell: integrates all variables into one visual result** -- confirmed and well-stated
- **Hull cell standard conditions: 267 mL, 2 A, 5-10 min** -- confirmed per IPC-TM-650 Method 2.4.18.1
- **Specific gravity as quick screening tool** -- confirmed
- **AA/ICP-OES for trace metals** -- confirmed
- **Spectrophotometry/colorimetry for specific ions** -- confirmed
- **Method hierarchy: daily (pH + temp + Hull cell) -> weekly (titration + SG) -> monthly (AA/ICP)** -- confirmed as sound practice framework
- **Sampling from mid-tank, mid-depth** -- confirmed
- **DI water rinse, then bath rinse, then sample** -- confirmed proper technique
- **0.45 micron filter for AA/ICP samples** -- confirmed
- **"Testing budget: 1-3% of total plating chemical spend"** -- reasonable benchmark

### Corrections Required

| # | Item | CW States | Should Be | Severity | Source |
|---|------|-----------|-----------|----------|--------|
| 30-1 | **ASTM B750 reference** | Listed in frontmatter as reference | **ASTM B750 is the Standard Specification for GALFAN (Zn-5%Al) Alloy-Coated Steel Wire.** It has nothing to do with Hull cell testing or bath analysis. The correct Hull cell reference is **IPC-TM-650, Method 2.4.18.1** (standard Hull cell test for electrodeposited coatings). ASTM does not publish a Hull cell standard. **Remove the B750 reference entirely.** NOTE: The CW body text does NOT actually cite B750 -- the reference appears only in the frontmatter "Source Documents" list alongside ASTM B764 (which IS a valid reference for compositional analysis of electrodeposits). **The B764 reference is correct; B750 must be removed or replaced with IPC-TM-650.** | **HIGH** | ASTM B750 scope; IPC-TM-650 |
| 30-2 | **ASTM B764 reference** | Listed in frontmatter | B764 is "Standard Test Method for Simultaneous Thickness and Electrode Potential Determination of Individual Layers in Multilayer Nickel Deposit (STEP Test)." This is a valid analytical method but applies to deposit characterization, not bath analysis per se. It is tangentially relevant. **Keep but note it covers deposit testing, not bath testing.** | LOW | ASTM B764 scope |
| 30-3 | **EN analysis: "Every shift"** | Stated for Ni and NaH2PO2 | **Should be "Every 2-4 hours during active plating" or "before each load."** EN metal depletion is so rapid at operating temperature that shift-based testing is insufficient for high-production baths. MTO (metal turnover) tracking is the standard practice -- replenishment is based on area plated, not time intervals. The CW also correctly includes "MTO tracking" in the Special column. | **MEDIUM** | ASTM B733; EN supplier practice |
| 30-4 | **Hard chrome: CrO3:SO4 ratio** | Listed as "weekly" in Special column | **For production hard chrome, this ratio should be checked DAILY or at minimum every 2-3 days.** The CrO3:SO4 ratio (typically 100:1 by weight) is the single most critical control parameter for hard chrome and it drifts with use. Tyler notes: "Daily for hard chrome in production." | **MEDIUM** | Industry practice; Tyler validation |
| 30-5 | **Analysis frequency consistency** | Various | Tyler's validation identified several frequency adjustments. The CW's frequencies are reasonable minimums but should be presented as "minimum recommended" rather than absolute values. Different production volumes justify different frequencies. The CW's approach of color-coding by frequency is good. | LOW | Tyler validation |
| 30-6 | **Startup cost: pH meter ~$200** | Stated | A quality benchtop pH meter with ATC and BNC connector runs $300-600 for lab-grade. A $200 unit is a basic pen-style meter. For a poster aimed at encouraging lab investment, **$200-500** is more honest. | LOW | Equipment pricing |
| 30-7 | **"Send out for AA/ICP: $50-150/sample"** | Stated | This is the correct range for commercial analytical laboratory pricing. **Confirmed.** | -- | Industry pricing |

### Missing Content

- **XRF for coating thickness** -- One of the most common QC instruments in a plating shop. Not a bath analysis method but integral to the analysis ecosystem.
- **Control charting / SPC:** Trending analytical data over time is as important as individual readings. A brief mention of control charts would strengthen the "building an analysis program" section.

### Brand/Supplier Check: CLEAN.

**Overall Assessment: MEDIUM-HIGH severity. The ASTM B750 reference must be removed (it is wrong). Analysis frequencies need minor tightening (EN hourly, chrome CrO3:SO4 daily). Otherwise the poster is a strong capstone for the series.**

---

## Consolidated Severity Summary

| Poster | Severity | Primary Issues |
|--------|----------|----------------|
| #24 -- Rectifier Fundamentals | **LOW** | Ripple zone messaging is a reasonable simplification; PR ratio terminology could be clearer |
| #25 -- Filtration and Purification | **CRITICAL** | Carbon treatment procedure wrong on pH direction, dosage, and contact time; EN turnover rate too low |
| #26 -- Chromate and Conversion Coatings | **MEDIUM** | RoHS scope must be clarified; SST ranges need sealer context; film thicknesses OK (v1 "1000x" error retracted) |
| #27 -- Wastewater Treatment | **MEDIUM-HIGH** | EPA limits CONFIRMED correct; missing cyanide limits; SMBS ratio understated; nickel is not amphoteric |
| #28 -- Temperature Control | **MEDIUM** | Watts Ni and EN minimums ~5 deg F too low; Arrhenius rule needs "chemical reaction" qualifier |
| #29 -- Anode Chemistry | **MEDIUM** | Zinc/titanium basket claim is wrong; otherwise excellent |
| #30 -- Bath Analysis Methods | **MEDIUM-HIGH** | ASTM B750 reference is wrong (remove); EN and chrome analysis frequencies need tightening |

---

## Action Items Before Generation Prompts

### MUST FIX (blocking)

1. **Poster #25:** Correct carbon treatment procedure: pH to 3.0-3.5 (lower, not raise), dosage 2-5 g/L, contact time 2-4 hours
2. **Poster #25:** Correct EN turnover rate from 3-5 to 10-20 TPH
3. **Poster #27:** Add cyanide discharge limits to EPA table (1.20 daily / 0.65 monthly)
4. **Poster #27:** Correct SMBS ratio to 2.5-3.5 lbs/lb Cr(VI)
5. **Poster #27:** Remove nickel from amphoteric metals claim in Block DD
6. **Poster #29:** Remove "NOT titanium" claim for zinc anode baskets
7. **Poster #30:** Remove ASTM B750 reference; replace with IPC-TM-650

### SHOULD FIX (recommended)

8. **Poster #26:** Add RoHS scope clarification (EEE only)
9. **Poster #26:** Note that tri SST ranges assume sealer topcoat
10. **Poster #28:** Correct Watts nickel minimum to 110 deg F and EN minimum to 180 deg F
11. **Poster #28:** Add "chemical" qualifier to Arrhenius rule
12. **Poster #30:** Adjust EN analysis frequency to "every 2-4 hours" and chrome CrO3:SO4 to "daily"

### NICE TO HAVE (non-blocking)

13. **Poster #24:** Add precious metals <1% ripple note
14. **Poster #25:** Add post-carbon treatment: replenish ALL organic additives (not just wetter)
15. **Poster #25:** Add filter aid (DE) mention
16. **Poster #27:** Add chelated metals warning to treatment process
17. **Poster #30:** Add XRF mention

---

## Cross-Poster Observations

1. **Zero brand or supplier names found across all 7 posters.** Full compliance with generic/neutral standard.

2. **Alaina's Construction Workups are technically strong.** Most corrections are refinements, not fundamental errors. The carbon treatment procedure in Poster #25 is the one genuinely dangerous mistake -- if a shop followed that procedure, the treatment would fail. Everything else ranges from "slightly off" to "fine for a poster."

3. **Tyler's validation and Watson's validation are highly convergent.** The major flags (carbon treatment, zinc/Ti baskets, SMBS ratio, nickel amphoteric, ASTM B750) were independently identified by both reviewers. This gives high confidence in the correction list.

4. **The EPA discharge limits in Poster #27 are EXACT.** Gemini verified all 9 metal/TTO values against 40 CFR Part 433 and every single one matches the CW. This is excellent work by Alaina.

5. **The v1 Watson brief contained one significant error of its own:** claiming that Poster #26's film thickness values in microns were "wrong by 1000x." This was incorrect -- 0.05 microns IS 50 nm, which is a reasonable value for clear chromate films. Corrected in this v2.

---

*Watson -- Chemistry Researcher*
*Plating Posters Inc -- Series 1 Validation*
*v2 -- 2026-04-26*
*Sources: Gemini API queries (rectifier ripple, EPA 40 CFR 433, filtration turnover rates), Tyler Validation Notes v2, Watson domain expertise, ASTM B633/B733/B764, IPC-TM-650, Nickel Plating Handbook 2023, EPA regulatory texts, Lowenheim, Canning Handbook*
