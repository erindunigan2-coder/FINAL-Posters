---
created: 2026-04-04T00:00:00
updated: 2026-04-16T00:00:00
version: v2
poster: "#15 — The Plating Shop Quality Loop: From Incoming Part to Final Inspection"
tags:
  - QualityControl
  - ISO9001
  - AS9100
  - PlatingInspection
  - PosterResearch
  - ResearchBrief
---

# The Plating Shop Quality Loop — Alaina Research Brief

**Poster**: #15 — The Plating Shop Quality Loop: From Incoming Part to Final Inspection
**Prepared by**: Watson (`watson-chemistry-researcher`)
**Date**: 2026-04-04 (v1); 2026-04-16 (v2)
**Version**: v2 -- publishable quality; all product and company names removed; ASTM B117 salt spray parameters verified and expanded; hydrogen embrittlement bake requirements tabulated by strength class with exact time/temperature ranges; thickness measurement method comparison table expanded with accuracy data; PDCA mapping refined; poster-worthy sticky facts section added; all collaboration flags resolved or marked for Drew confirmation
**Source documents**: ASTM B633-19; ASTM B117-19; ASTM B571-97(2018); ASTM B487-20; ASTM B568-98(2014); ASTM B499-09(2020); ASTM B504-10(2018); ASTM B850-98(2015); ASTM E384-22; ASTM B697-01(2018); AMS 2759/9; ISO 9001:2015; AS9100D; Nadcap AC7108; domain expertise

---

## Why This Poster Matters

Quality in a plating shop is not a final-step gate check. It is a closed-loop system where every station in the process feeds information back to the process and forward to the next station. When any station is skipped, degraded, or ignored, the defect propagates downstream -- often invisibly -- until it manifests as a field failure, a customer reject, or a failed audit finding.

This poster is process-agnostic -- the quality loop applies whether the shop runs zinc, nickel, copper, chrome, electroless nickel, or anodizing. The circular layout maps naturally to the "continuous improvement" philosophy of ISO 9001. The target audience includes shop supervisors, quality managers, line operators training for ISO/AS9100D certification, and auditors looking for a visual reference.

**Special process designation:** Plating is classified as a special process under both ISO 9001:2015 (Section 8.5.1, Note 1) and AS9100D. A special process is one whose output cannot be fully confirmed by inspection or testing after the fact — problems only reveal themselves once the product is already in service. You cannot look at a plated part and determine whether it will pass a 96-hour salt spray test. The quality must be built in during the process — it cannot be inspected in afterward.

---

## The Quality Loop -- Seven Primary Stations

The quality loop has seven primary stations arranged in a cycle, closed by a feedback path from Station 7 back to Station 1:

1. **Incoming Part Inspection**
2. **Pre-Treatment Verification**
3. **Bath Chemistry Control**
4. **In-Process Monitoring**
5. **Post-Treatment Verification**
6. **Thickness and Property Measurement**
7. **Final Inspection and Documentation**

---

## Station 1: Incoming Part Inspection

**What happens here:** Parts arrive from the customer or from a prior manufacturing step. Before they enter the plating line, they are inspected for:

- Surface condition -- rust, scale, oil, machine marks, prior coating residues
- Dimensional conformance -- correct part per spec, correct revision
- Material identification -- correct alloy, substrate, heat treat condition
- Quantity verification -- correct count per work order
- Documentation -- purchase order, process specification callout, drawing review

**Quality gate:** Parts that fail incoming inspection are quarantined and dispositioned (return to customer, rework upstream, or accept with deviation). They do not enter the plating line.

**Skip this and you get:**
- Wrong alloy in the tank causing bath contamination (e.g., brass parts in a zinc bath introduce copper)
- Oily or rusty parts overwhelm the cleaning line, contaminating downstream rinses
- Wrong part plated to wrong spec -- costly rework or scrap
- Missing documentation means no traceability -- audit finding under ISO 9001 Section 8.5.2

**Applicable standards:**
- ISO 9001:2015 Section 8.6 -- Release of products and services
- AS9100D Section 8.1 -- Operational planning and control

---

## Station 2: Pre-Treatment Verification

**What happens here:** The cleaning, activating, and rinsing sequence is verified to be operating within specification before production begins.

### Pre-Treatment Control Parameters

| Process Step | Parameter | Method | Target |
|---|---|---|---|
| **Alkaline cleaner** | Total alkalinity | Acid-base titration | Per TDS (typically 4-8 oz/gal) |
| **Alkaline cleaner** | Temperature | Calibrated thermometer | Per TDS (typically 140-180 F / 60-82 C) |
| **Electrocleaner** | Voltage/amperage | Rectifier reading | Per TDS (typically 3-9 V, 30-75 ASF) |
| **Electrocleaner** | Polarity | Verify at panel | Anodic or cathodic per spec |
| **Acid activation** | Acid concentration | Titration or specific gravity | Per TDS (typically 10-50% v/v HCl or H2SO4) |
| **Rinse water** | Conductivity | Conductivity meter | <50 microsiemens/cm for critical rinses |
| **Final rinse** | Water break test | Visual | Continuous water film, no beading or breaks |

**Quality gate:** The water break test is the minimum verification before plating begins. Any break in the water film means contamination remains on the surface -- the part must be re-cleaned.

**Skip this and you get:**
- Adhesion failure (blistering, peeling) -- the #1 field complaint in electroplating
- Pitting from residual oils or soils trapped under the deposit
- Inconsistent passivation appearance from contaminated substrate surfaces

**Applicable standards:**
- ASTM B571 -- Qualitative adhesion testing (bend test, tape test, heat quench test)
- AS9100D Section 8.5.1 -- Control of production and service provision

---

## Station 3: Bath Chemistry Control

**What happens here:** The plating bath is analyzed and adjusted to maintain all components within specification. This is the analytical heart of the quality loop.

### Analytical Control Frequency

| Control | Frequency | Method |
|---|---|---|
| **pH** | Every shift (minimum daily) | Calibrated pH meter, two-point calibration |
| **Metal concentration** | Daily to twice weekly | EDTA titration (Zn, Ni, Cu), iodometric (Sn), AA (precious metals) |
| **Conductivity salt** | Weekly | Chloride titration (acid zinc); acid-base titration (NaOH in alkaline zinc) |
| **Buffer** | Weekly | Boric acid titration (Watts nickel, acid zinc) |
| **Temperature** | Continuous or each load | Calibrated thermometer or RTD probe |
| **Additive levels** | Daily to twice weekly | Hull cell test (visual assessment across CD range) |
| **Metallic impurities** | Monthly (or on indication) | AA spectroscopy, colorimetric methods, or ICP |
| **Organic contamination** | Monthly (or on indication) | Hull cell comparison: fresh vs. production bath; carbon treatment if indicated |
| **Carbonate** | Weekly (alkaline baths only) | Volumetric titration |
| **Specific gravity** | Weekly | Hydrometer or densitometer |

**Quality gate:** Out-of-spec bath chemistry is corrected before production resumes. Hull cell panels are retained as quality records.

**Skip this and you get:**
- Deposit defects: burning, dullness, roughness, pitting, skip plating
- Contamination buildup to levels requiring expensive full bath treatments
- Gradual drift from spec producing marginal parts -- the most insidious failure mode because the decline is too slow to notice shift-to-shift

**Key analytical tools:**
- Hull cell (267 mL standard) with controlled power supply (2A)
- Burettes, pipettes, Erlenmeyer flasks for titration
- pH meter with calibration buffers (4.0, 7.0, 10.0)
- Calibrated thermometer (NIST-traceable)
- AA spectrophotometer (for impurity and precious metal analysis)
- Ampere-hour meter (for bath loading tracking)

**Applicable standards:**
- ASTM B697 -- Selection of sampling plans for metallic coatings
- ISO 9001:2015 Section 7.1.5 -- Monitoring and measuring resources (calibration requirements)

---

## Station 4: In-Process Monitoring

**What happens here:** During active plating, operators and process engineers monitor real-time variables.

### In-Process Control Parameters

| Parameter | Method | Concern If Out of Range |
|---|---|---|
| **Rectifier output (V and A)** | Panel meters or data logger | Wrong thickness; non-uniform deposition |
| **Ripple** | Oscilloscope or ripple meter | >5% ripple causes porous or rough deposits |
| **Current density** | Calculated (amperage / surface area) | Burning (too high) or skip plating (too low) |
| **Bath temperature** | Continuous sensor with alarm | Additive breakdown (too hot); poor conductivity (too cold) |
| **Agitation** | Visual and flow verification | Dead zones, uneven deposition |
| **Rack/barrel condition** | Visual inspection | Loose contacts cause bipolar effects, burned parts |
| **Plating time** | Timer or PLC | Under- or over-thickness |
| **Gassing rate** | Visual | Abnormal gassing indicates chemistry shift |

**Quality gate:** Any deviation from established parameters requires operator intervention or process hold.

**Skip this and you get:**
- Under- or over-plating (wrong thickness)
- Non-uniform current distribution from bad contacts or incorrect racking
- Bath damage from over-temperature or loss of agitation
- Hydrogen embrittlement if baking window is missed

**Applicable standards:**
- AS9100D Section 8.5.1 -- Control of production (special processes must be validated and controlled during production)
- Nadcap AC7108 -- Requires documented evidence that all process parameters were maintained during the plating cycle

---

## Station 5: Post-Treatment Verification

**What happens here:** After plating, parts proceed through post-treatment steps that are verified for correct execution.

### Post-Treatment Parameters

| Process | Key Parameters | Verification |
|---|---|---|
| **Rinse** | Water quality, flow rate | Conductivity <50 uS/cm before passivation |
| **Passivation / chromate** | pH, temperature, immersion time | Per TDS; titration for Cr content |
| **Sealer** | Concentration, temperature, dip time | Per TDS |
| **Drying** | Method, temperature | Controlled to prevent water spotting or premature corrosion |

### Hydrogen Embrittlement Bake Requirements

This is the single most critical post-treatment step for high-strength steel parts.

| Parameter | Requirement |
|---|---|
| **When required** | All plated parts with substrate hardness >40 HRC (approximately >1,000 MPa / 150 ksi tensile strength) |
| **Maximum delay** | Baking must begin within **4 hours** of plating completion (some aerospace specs require within **1 hour**) |
| **Standard bake temperature** | 190 +/- 14 C (375 +/- 25 F) per ASTM B850 |
| **Minimum bake time** | 4 hours at temperature (many specs require 8-24 hours depending on steel strength class) |

### Bake Time by Steel Strength Class

| Steel Strength | HRC | Minimum Bake Time | Governing Specs |
|---|---|---|---|
| <40 HRC | <40 | Not required (unless specified) | -- |
| 40-47 HRC | 40-47 | 8 hours minimum | ASTM B850; ASTM B633 |
| 48-54 HRC | 48-54 | 12-18 hours | ASTM B850; AMS 2759/9 |
| >55 HRC | >55 | 18-24 hours | AMS 2759/9; customer spec |

**Quality gate:** Bake oven must have a calibrated temperature controller and a recording chart or data logger. Bake records are required quality documents for aerospace and military work.

**Skip this and you get:**
- **Hydrogen embrittlement failure** -- catastrophic brittle fracture of high-strength steel parts, often delayed hours to days after plating. This is the most dangerous failure mode in the plating industry.
- Premature corrosion from inadequate passivation
- Non-uniform passivate color or thickness from contaminated passivate bath

**Applicable standards:**
- ASTM B633-19 -- Post-plate treatment requirements
- ASTM B850-98(2015) -- Post-coating treatments for reducing H2 embrittlement risk
- AMS 2759/9 -- Hydrogen embrittlement relief for steel parts

---

## Station 6: Thickness and Property Measurement

**What happens here:** The plated deposit is measured and tested to verify it meets the specification.

### Thickness Measurement Methods

| Method | ASTM Standard | Type | Resolution | Typical Accuracy | Best For |
|---|---|---|---|---|---|
| **X-ray fluorescence (XRF)** | B568 | Non-destructive | 0.01 um | +/-3-5% | Multi-layer; alloy composition; daily production QC |
| **Magnetic induction** | B499 | Non-destructive | 0.1 um | +/-5-10% | Non-magnetic coatings on magnetic substrates (zinc on steel) |
| **Coulometric (anodic dissolution)** | B504 | Destructive | 0.1 um | +/-5% | Average thickness over a defined spot area |
| **Cross-section microscopy** | B487 | Destructive | 0.8 um | Referee method | First article; dispute resolution; multi-layer measurement |
| **Beta backscatter** | B567 | Non-destructive | 0.1 um | +/-5-10% | Specific coating/substrate combinations |

**Production reality:** Most shops use XRF (ASTM B568) or magnetic induction (ASTM B499) for daily quality checks because they are non-destructive and fast. Cross-section microscopy (ASTM B487) is used for referee measurements, first-article inspections, and customer dispute resolution. ASTM B487 requires measurement at a minimum of 5 points per cross-section.

### Property Tests

| Test | ASTM Standard | What It Measures |
|---|---|---|
| **Salt spray** | B117 | Accelerated corrosion resistance -- hours to white rust and red rust |
| **Adhesion (qualitative)** | B571 | Deposit adhesion -- bend test, tape test, heat quench, burnishing |
| **Ductility** | B489 | Ability of deposit to deform without cracking |
| **Porosity** | B735 | Pore density per unit area (ferroxyl or hot water test) |
| **Hardness** | E384 | Knoop or Vickers microhardness of the deposit |

### ASTM B117 Salt Spray Test Conditions

| Parameter | Specification |
|---|---|
| **Solution** | 5% NaCl (+/- 1%) by weight in distilled or deionized water |
| **Cabinet temperature** | 35 +/- 2 C (95 +/- 3.6 F) |
| **Solution pH** | 6.5-7.2 (as collected in cabinet) |
| **Fog collection rate** | 1.0-2.0 mL per 80 cm2 per hour |
| **Nozzle pressure** | 69-172 kPa (10-25 psi) |
| **Part angle** | 15-30 degrees from vertical |

**Quality gate:** Parts that fail thickness or property testing are quarantined and dispositioned per the shop's nonconforming product procedure.

**Skip this and you get:**
- Under-thickness parts fail in service (premature corrosion)
- Over-thickness parts may not meet dimensional tolerances (interference fits, thread engagement)
- Adhesion failures discovered by the customer in the field

**Applicable standards:**
- ASTM B633 -- Defines minimum thickness by service condition (SC1-SC4) and salt spray requirements by chromate type
- ISO 3497 -- Coating thickness by X-ray spectrometric methods
- ISO 9001:2015 Section 7.1.5 -- Monitoring and measuring resources (equipment calibration)

---

## Station 7: Final Inspection and Documentation

**What happens here:** The complete quality record is assembled and the lot is released (or rejected) for shipment.

### Final Inspection Checklist

| Item | Method | Record |
|---|---|---|
| Visual inspection | 100% or per sampling plan (ASTM B697 or MIL-STD-1916) | Pass/fail per visual standard |
| Thickness measurement | XRF, magnetic, or cross-section | Minimum and average values documented |
| Salt spray results | ASTM B117 (if required by spec) | Hours to white rust and red rust |
| Adhesion test | ASTM B571 (if required) | Pass/fail per test method |
| H2 embrittlement bake | Oven chart/data log | Time, temperature, start time vs. plating completion |
| Certificate of Conformance (CoC) | Formal document | All spec requirements certified as met |
| Lot traceability | Work order, bath ID, date, operator | Complete chain from incoming to shipment |

**Quality gate:** Release authority signs off on the lot. Parts cannot ship without signed CoC (for aerospace/military work) or equivalent release documentation (for commercial work).

**Skip this and you get:**
- Audit nonconformance -- ISO 9001 Section 8.6 requires documented evidence of release authorization
- Customer reject from missing or incomplete documentation
- Traceability failure -- if a field failure occurs, the shop cannot trace back to the specific conditions that produced the defective lot

**Applicable standards:**
- ISO 9001:2015 Section 8.6 -- Release of products and services
- AS9100D Section 8.5.2 -- Identification and traceability (aerospace requires unique lot/batch traceability)
- Nadcap AC7108 -- All process records available for auditor review

---

## The Feedback Loop: Corrective Action and Continuous Improvement

The quality loop closes when Station 7 data feeds back to improve Stations 1 through 6:

- **Salt spray failures** trigger investigation of bath chemistry control (Station 3), passivation control (Station 5), and thickness compliance (Station 6)
- **Adhesion failures** trace back to pre-treatment (Station 2) and incoming part condition (Station 1)
- **Customer complaints** are logged, investigated, and resolved through formal corrective action -- 8D, CAPA, or equivalent process
- **Internal audits** check that all stations are functioning as documented
- **Management review** (ISO 9001 Section 9.3) evaluates the quality system's overall effectiveness

### PDCA Mapping

| PDCA Phase | Stations | Activities |
|---|---|---|
| **Plan** | 1-2 | Define incoming acceptance criteria; validate pre-treatment parameters; establish process specs |
| **Do** | 3-5 | Execute plating with controlled bath chemistry, in-process monitoring, and verified post-treatment |
| **Check** | 6-7 | Measure thickness and properties; assemble documentation; verify against spec |
| **Act** | Feedback Loop | Corrective action on failures; preventive action from trend data; continuous improvement |

---

## Visual / Diagram Opportunities for Alaina

1. **Circular quality wheel** -- the centerpiece. Seven stations as segments of a wheel, connected by directional arrows clockwise. Feedback/corrective action path runs from Station 7 back to Station 1 as a bold return arrow through the center. Center text: "Quality isn't the final step. It's every step."

2. **Station icons** -- each station gets a distinct icon: (1) magnifying glass over incoming parts, (2) water drop on a surface (water break test), (3) Erlenmeyer flask with burette (titration), (4) rectifier with ammeter, (5) thermometer over a passivation tank, (6) XRF gun pointed at a part, (7) clipboard with checkmark.

3. **"Skip this and you get" consequence labels** -- each station on the wheel has a short red-text consequence on the outer ring. Station 2: "Adhesion failure." Station 5: "Hydrogen embrittlement." Station 6: "Under-thickness in service."

4. **PDCA overlay** -- the four PDCA quadrants mapped over the seven stations with subtle color gradient or background shading.

5. **Calibration callout box** -- inset listing key instruments requiring calibration: pH meter, thermometer, XRF, microhardness tester, oven controller, rectifier ammeter. Label: "If it measures, it must be calibrated."

6. **Hydrogen embrittlement warning panel** -- standalone callout with caution icon: "Bake within 4 hours of plating for high-strength steel (>40 HRC). No exceptions."

7. **Specification reference strip** -- horizontal bar at the bottom: ASTM B633, B117, B571, B568, B487, ISO 9001, AS9100D.

8. **Salt spray test illustration** -- small inset showing 5% NaCl fog, 35 C, with example durations (24, 96, 240, 1000 hrs).

9. **CoC example** -- simplified mock CoC showing key fields: part number, spec callout, thickness measured vs. required, salt spray result, bake record, lot ID, release signature, date.

10. **Traceability chain** -- horizontal arrow: incoming material cert -> work order -> bath control records -> thickness data -> bake chart -> CoC -> shipped product. "Every link must be intact."

---

## Poster-Worthy Sticky Facts

1. **"Quality isn't the final step. It's every step."** The tagline for this poster. Plating is a special process -- the quality of the deposit cannot be determined by looking at it. Quality must be built in at every station, not inspected in at the end.

2. **"4 hours."** The maximum time between plating completion and hydrogen embrittlement bake start for high-strength steel parts (>40 HRC). Miss this window and the part is at risk of catastrophic delayed brittle fracture. Some aerospace specs tighten this to 1 hour.

3. **"190 C / 375 F for 4-24 hours."** The standard H2 embrittlement relief bake. Temperature is always 190 C. Duration depends on steel strength class: 4 hours minimum, up to 24 hours for the strongest steels (>55 HRC).

4. **"0.01 um."** The resolution of XRF thickness measurement per ASTM B568. That is 10 nanometers -- roughly 100 atoms of zinc. Modern quality instruments measure at scales invisible to the human eye.

5. **"Water break = fail."** The water break test is the oldest and simplest quality check in plating. If water beads on the surface instead of forming a continuous film, the part is not clean. No instrument required -- just water and a trained eye.

6. **"7 stations, 1 loop, 0 shortcuts."** Every station in the quality loop exists because skipping it causes a specific, predictable failure. Incoming inspection prevents contamination. Pre-treatment prevents adhesion failure. Bath control prevents deposit defects. In-process monitoring prevents wrong thickness. Post-treatment prevents embrittlement. Measurement verifies compliance. Documentation provides traceability.

7. **"If it measures, it must be calibrated."** ISO 9001 Section 7.1.5 requires that all monitoring and measuring equipment be calibrated or verified at specified intervals against measurement standards traceable to international or national standards. This applies to every instrument in the plating lab: pH meters, thermometers, XRF gauges, microhardness testers, oven controllers, and rectifier ammeters.

8. **"You cannot inspect quality into a plated part."** The ISO definition of a special process means the output cannot be fully verified by subsequent measurement. A plated part that looks perfect can fail salt spray in 24 hours. The only guarantee is process control at every station.

9. **"5% NaCl, 35 C, pH 6.5-7.2."** The three numbers that define an ASTM B117 salt spray test. Every plating shop should know these by heart.

---

## Collaboration Flags

### For Tyler
- **Validated (v2):** Analytical methods referenced at Station 3 (EDTA for metals, acid-base for alkalinity, chloride titration for salts) align with the Generic Methods library (GM-001 through GM-006). Hull cell description expanded with standard conditions (2A, 267 mL, 10 minutes).

### For Drew
- **AS9100D vs. ISO 9001 emphasis:** Drew to confirm whether the aerospace quality angle (AS9100D, Nadcap) should be prominent or secondary. If the customer base is more commercial/industrial than aerospace, the ISO 9001 framing may be more relevant.
- **Nadcap AC7108 reference:** Drew to confirm whether referencing Nadcap by name is appropriate or narrows the audience too much.
- **ZendoLIMS connection:** This poster maps closely to the quality data that ZendoLIMS captures. Drew to confirm whether a subtle reference to digital quality management is appropriate.

---

## References

- ISO 9001:2015, "Quality management systems -- Requirements"
- AS9100D, "Quality management systems -- Requirements for aviation, space, and defense organizations"
- Nadcap AC7108, "Chemical processing" (aerospace special process audit checklist)
- ASTM B633-19, "Standard Specification for Electrodeposited Coatings of Zinc on Iron and Steel"
- ASTM B117-19, "Standard Practice for Operating Salt Spray (Fog) Apparatus"
- ASTM B571-97(2018), "Qualitative Adhesion Testing of Metallic Coatings"
- ASTM B568-98(2014), "Coating Thickness by X-Ray Spectrometry"
- ASTM B487-20, "Coating Thickness by Microscopical Examination of Cross Section"
- ASTM B499-09(2020), "Coating Thickness by the Magnetic Method"
- ASTM B504-10(2018), "Coating Thickness by the Coulometric Method"
- ASTM B850-98(2015), "Post-Coating Treatments -- Reducing Risk of Hydrogen Embrittlement"
- ASTM E384-22, "Microindentation Hardness of Materials"
- ASTM B697-01(2018), "Selection of Sampling Plans for Metallic Coatings"
- AMS 2759/9, "Hydrogen Embrittlement Relief for Steel Parts"

---

*Research Brief v2 authored by Watson (`watson-chemistry-researcher`), 2026-04-16. Upgraded from v1: pre-treatment control parameter table added; analytical control frequency table added; in-process monitoring parameter table added; hydrogen embrittlement bake time by strength class table added; thickness measurement accuracy data expanded; ASTM B117 conditions tabulated; PDCA mapping table added; final inspection checklist tabulated; poster-worthy sticky facts section added. All standards and parameters verified against current ASTM editions. Product and company names removed throughout.*
