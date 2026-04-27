---
title: "Zinc Alkaline Cluster EP-01 — Tyler Validation Notes"
date: 2026-04-25T00:00:00
author: Tyler (plating chemist)
scope: Lab/shop-floor validation of Posters 31, 34, 36, 38
status: Complete — ready for Elara corrections
tags:
  - PosterValidation
  - ZincPlating
  - Alkaline
  - ClusterEP01
  - Series2
---

# Zinc Alkaline Cluster EP-01 — Tyler Validation Notes

**Tyler — A Brite Company**
**Date:** 2026-04-25
**Posters reviewed:** #31 (Process Flow), #34 (Activation), #36 (Main Tank), #38 (Post Treatment)

This document is my shop-floor and lab chemistry validation of the four technically densest posters in the EP-01 cluster. Watson is covering the full eight from a research angle. My focus is: would a real alkaline zinc operator look at these posters and trust what they see?

Short answer: Elara did strong work. The overall process knowledge is solid and the flow is correct. I have flagged corrections below — most are refinements, a few are important enough that they would mislead an operator if left as-is.

---

## 1. Zinc Metal and NaOH Concentration Ranges

**Poster #31 (Process Flow) and #36 (Main Tank) both state:**
- Zn: 10--14 g/L (1.3--1.9 oz/gal)
- NaOH: 100--140 g/L (13--19 oz/gal)

### Verdict: Confirmed with a note

The ranges are correct for a generic, supplier-neutral alkaline non-cyanide zinc bath. Most proprietary ANC zinc systems (Enthone Envirozin, MacDermid ZinKlad, Coventya Performa, Atotech Protechsal, and our own A Brite products) fall within or very close to these windows. Some suppliers run zinc as low as 8 g/L or as high as 15 g/L depending on the additive package, but 10--14 g/L is the safe "typical" range for a generic poster.

- Confirmed: Zn 10--14 g/L
- Confirmed: NaOH 100--140 g/L
- Confirmed: oz/gal conversions are correct (1 g/L = 0.1335 oz/gal)

---

## 2. Zn:NaOH Ratio

**Poster #36 states:**
- Optimal range: 1:8 to 1:12
- Optimal marker at 1:10
- Below 1:8 (too much zinc relative to NaOH): rough, burning
- Above 1:14 (too much NaOH relative to zinc): dull, poor coverage

### Verdict: Needs correction — ratio is inverted in presentation

This is the single most important correction in the entire cluster.

The way the ratio is written — "1:8 to 1:12" — reads as Zn:NaOH = 1 part zinc to 8--12 parts NaOH. That numerical statement is actually correct if you divide the g/L values: at 12 g/L Zn and 120 g/L NaOH, the ratio is 1:10. So the numbers themselves check out.

**However, the industry-standard way to express this ratio is NaOH:Zn, not Zn:NaOH.** Every major supplier TDS, every Metal Finishing Guidebook edition, and every NASF reference I have seen expresses the ratio as:

> NaOH-to-Zinc ratio = 8:1 to 12:1 (optimal ~10:1)

The reason is practical: the NaOH number is the bigger number, and operators think "I need 10 parts caustic for every 1 part zinc." Writing it the other way invites confusion on the shop floor.

**Recommended correction for Poster #36:**
- Change the gauge title from `Zn:NaOH (g/L to g/L)` to `NaOH:Zn Ratio (g/L to g/L)`
- Relabel the gauge: `8:1 to 12:1` optimal, marker at `10:1`
- Left red zone: `< 8:1` (too little NaOH — rough, burning)
- Right red zone: `> 14:1` (excess NaOH — dull, poor coverage)
- Update the yellow zone to `12:1 to 14:1`

**Also update Poster #31** wherever the ratio is mentioned — Box 5 says "Zn:NaOH ratio controls deposit quality." Change to "NaOH:Zn ratio controls deposit quality."

The underlying numbers (1:8, 1:10, 1:12) are arithmetically correct. The issue is convention. An operator trained on any major supplier system will expect to see NaOH:Zn, and flipping it will cause hesitation or mistakes on the floor.

---

## 3. Cathode Efficiency

**Poster #36 states:** 70--85%

### Verdict: Confirmed

Alkaline non-cyanide zinc cathode efficiency is typically 60--85%, with most well-maintained baths running 70--85% at normal current densities (10--30 ASF). At very low CD the efficiency drops; at very high CD it also drops due to excessive hydrogen evolution. The 70--85% range stated on the poster is the practical operating window and is correct for a general reference.

If the poster wanted to be more inclusive, 65--85% would capture slightly suboptimal baths, but 70--85% is a defensible "healthy bath" range.

- Confirmed: 70--85% is correct for a well-controlled bath

---

## 4. Activation Stage — Acid Concentrations

**Poster #34 states:**
- HCl: 5--10% v/v
- H2SO4: 2--5% v/v
- Time: 15--60 sec

### Verdict: Needs correction — HCl upper end is aggressive; H2SO4 range needs tightening

**HCl at 10% v/v is on the aggressive side for activation before alkaline zinc.** Most real shops run HCl activation at 10--50% v/v for general descaling and heavy oxide removal, but for activation (light oxide film removal on already-cleaned steel), the common range is:

- HCl: 5--30% v/v is the full published range
- For activation specifically (not pickling): **5--15% v/v** is most common in practice

So 5--10% is actually conservative and safe. I would not call it "too aggressive" — it sits in the gentle end of the range. This is fine for a poster aimed at activation rather than heavy pickling.

**However, the H2SO4 range of 2--5% v/v is too low.** Sulfuric acid activation is typically run at:

- H2SO4: **5--15% v/v** for activation
- Some shops go as high as 25% for heavier oxide

At 2% v/v H2SO4 the acid is barely doing anything. It would take an unacceptably long immersion to remove even a light oxide film.

**Recommended correction for Poster #34:**
- HCl: 5--10% v/v — acceptable as stated (conservative but correct for light activation)
- H2SO4: change from `2--5% v/v` to `5--15% v/v`

**Time range of 15--60 sec:** Correct for activation. For high-strength steel the poster correctly notes limiting to 15--30 sec. Good.

---

## 5. Post-Treatment — Trivalent Chromate Parameters

**Poster #38 states:**
- Tri pH: 3.5--4.5
- Tri temperature: Ambient (65--85 F)
- Tri time: 30--90 sec

### Verdict: Needs minor correction on pH range

The trivalent passivate pH range varies by product type:

- **Trivalent clear/blue:** pH 1.8--2.2 (many products) to pH 3.8--4.2 (some newer formulations)
- **Trivalent thick-film / high-performance:** pH 2.0--3.5
- **Trivalent black:** pH 2.0--3.0 (most products)

A blanket statement of pH 3.5--4.5 for all trivalent passivates is too narrow and too high. Many trivalent passivates run below pH 3.5. The A Brite NZP P1/P2 (trivalent black) runs well below 4.5.

**Recommended correction for Poster #38:**
- Change trivalent pH from `3.5--4.5` to `1.8--4.5` (covers the full range of trivalent products)
- Or, if that range looks too wide for a poster, split it: `Clear/Blue: pH 1.8--2.5` and `Thick-film/Black: pH 2.0--4.5`
- The current range of 3.5--4.5 would cause an operator with a low-pH trivalent product to think something is wrong with their bath

**Temperature:** Ambient to 85 F is correct for most trivalent products. Some can go to 100 F. The poster says "Ambient (65--85 F)" which is fine. No correction needed.

**Time:** 30--90 sec is correct for trivalent. Some products go as short as 20 sec, but 30--90 covers the mainstream.

**Hexavalent parameters are correct:**
- pH 1.5--2.5: Confirmed
- Time 15--30 sec: Confirmed
- Temperature ambient to 100 F: Confirmed

---

## 6. Hexavalent Chromate Time

**Poster #38 states:** Hex time 15--30 sec

### Verdict: Confirmed with a note

15--30 sec is correct for most hex yellow and hex clear chromates. Some hex olive drab / black processes run longer (30--60 sec), but for a general reference 15--30 sec is the right call.

- Confirmed: 15--30 sec for hexavalent

---

## 7. Salt Spray Performance Numbers

**Poster #38 states:**

| Type | Hours to white rust |
|---|---|
| Bare zinc | 12--24 hr |
| Tri clear (no sealer) | 48--72 hr |
| Tri clear + sealer | 96--200 hr |
| Tri black + sealer | 120--240 hr |
| Hex yellow | 96--200 hr |
| Hex yellow + sealer | 200--500 hr |

### Verdict: Confirmed — these are solid general numbers

These are reasonable industry-typical values. Real-world salt spray results vary enormously with zinc thickness, passivate quality, sealer type, substrate prep, and lab technique, but as "typical" ranges for a poster, these are defensible.

One note: bare zinc at 12--24 hr to white rust assumes a relatively thin deposit (5--8 um). Thicker deposits (12--25 um) can go longer even without passivate. But for a general reference, 12--24 hr is fine — it makes the point that passivation is essential.

- Confirmed: all six salt spray ranges are reasonable

---

## 8. Hydrogen Embrittlement — 150 ksi Threshold

**Posters #31, #34, and #38 all reference >150 ksi as the HE risk threshold.**

### Verdict: Needs correction — threshold is too conservative

The commonly cited threshold for hydrogen embrittlement susceptibility in plating specifications is:

- **ASTM B850:** applies to parts with ultimate tensile strength >= 1000 MPa (~145 ksi) or hardness >= 31 HRC
- **ASTM F519:** test method for HE — does not itself define a threshold, but is used to validate processes for HE-susceptible parts
- **AMS 2759/9:** defines HE relief baking requirements
- **ASTM B849:** covers pre-plating stress relief

The practical industry threshold where HE baking becomes mandatory is generally cited as:

> **Hardness >= 31 HRC or tensile strength >= 1000 MPa (~145 ksi)**

Some aerospace specs (BAC, BPS) drop this even lower to 125 ksi / 39 HRC for certain critical applications. Others use 150 ksi as the threshold for extra precautions beyond standard baking.

**The 150 ksi number is not wrong — it is within the range of values used in industry.** But it is slightly high compared to the most commonly cited 145 ksi / 1000 MPa / 31 HRC threshold in ASTM B850.

**Recommended correction:**
- Change `> 150 ksi` to `>= 1000 MPa (~145 ksi) or >= 31 HRC`
- Or for simplicity on a poster: `>= 145 ksi / >= 31 HRC`
- The addition of the HRC value is important because many shops measure hardness, not tensile strength

**Bake parameters on Poster #34 and #38:**
- 375 F: Confirmed (standard per ASTM B850 is 375 +/- 25 F, i.e. 190 +/- 14 C)
- Within 4 hours: Confirmed (some specs say "within 1 hour" for very high strength; 4 hours is the standard ASTM B850 requirement)
- 23 hours minimum: Confirmed (ASTM B850 specifies minimum 23 hours for most applications)
- Reference ASTM B850: Confirmed correct standard

**One additional note for Poster #38:** The workup states "Hydrogen bake (if required): 375 F for 23 hr BEFORE passivation." This is critically important and correctly stated. The bake must happen after plating but before passivation, because baking after passivation degrades the chromate film. Good call by Elara.

---

## 9. Poster #36 — Rectifier Polarity Label

**Poster #36 states:** `+` label on left wire (to anode), `-` label on right wire (to cathode)

### Verdict: Needs correction — polarity is reversed in the label text

The text says "+" goes to the anode and "-" goes to the cathode. The polarity itself is correct — anodes are connected to the positive terminal, cathode (workpiece) to the negative terminal. **However,** the build spec says "+ on left wire (to anode)" and "- on right wire (to cathode)." Looking at the tank cross-section layout, the anodes are on BOTH sides (left at X: 2.5" and right at X: 20.5"), and the cathode is in the CENTER (X: 11.0").

The rectifier is centered above the tank (X: 10.0"). So the wiring should be:
- Left wire from rectifier goes DOWN to cathode (center, directly below) — this should be the **negative (-)** terminal
- Right wire... actually, this layout has the rectifier centered over the cathode, so both positive wires should run outward to the anodes on each side

**Recommended correction:**
- Redraw the rectifier wiring: two "+" wires running from the rectifier outward to the left and right anode banks, and one "-" wire running from the rectifier down to the center cathode
- Or simply label: `(+) to anodes (both sides)` and `(-) to cathode (center)`
- Current description of "left wire to anode, right wire to cathode" is physically confusing given the symmetric tank layout

---

## 10. Poster #36 — Anode Description

**Poster #36 states:** "Zinc balls in Ti baskets"

### Verdict: Confirmed — but could be more inclusive

Zinc balls (or chunks) in titanium baskets is the most common anode setup for ANC zinc. Some shops use:
- Zinc balls in steel baskets (less common, works but Ti is preferred for longevity)
- Zinc slabs (less common in ANC, more common in cyanide zinc)
- Soluble zinc anodes (cast zinc bars)

For a general poster, "Zinc balls in Ti baskets" is the right primary reference. No correction needed, but if space allows, a note that "steel baskets are also used" would be a nice addition.

- Confirmed: Zinc balls in Ti baskets is correct and representative

---

## 11. Poster #36 — Contamination Thresholds

| Contaminant | Poster Value | My Assessment |
|---|---|---|
| Copper > 5 ppm | Confirmed — 5 ppm is a common threshold for Cu in alk zinc |
| Lead > 2 ppm | Confirmed — lead is extremely harmful even at low levels |
| Iron > 25 ppm | Needs correction — should be > 50 ppm; 25 ppm is too tight for most ANC zinc baths |
| Chromium > 1 ppm | Confirmed — Cr is very damaging, 1 ppm is appropriate |
| Organic (oil) visible | Confirmed — any visible organic is a problem |
| Carbonate > 30 g/L | Confirmed — 30 g/L is a common threshold; some baths tolerate up to 50 g/L but problems begin around 30 |

### Iron threshold detail

Most ANC zinc baths tolerate iron up to 25--50 ppm before visible effects appear. The 25 ppm threshold on the poster would trigger unnecessary concern in many healthy baths. A more representative threshold is 50 ppm, with effects becoming noticeable at 25--50 ppm depending on the additive system.

**Recommended correction:**
- Iron: change from `> 25 ppm` to `> 50 ppm`

### Carbonate freeze-out note

The poster says "Freeze-out at < 25 F to remove excess carbonate." This is correct — carbonate crystallizes out when the bath is cooled below approximately -4 C (25 F). However, some references cite the effective freeze-out temperature for sodium carbonate in concentrated NaOH as closer to 0--5 C (32--41 F). The 25 F number is on the aggressive (colder) end.

**Recommended correction:**
- Change `< 25 F` to `< 35 F (2 C)` — this is a more practical and commonly cited temperature for carbonate freeze-out in ANC zinc baths

---

## 12. Poster #31 — Soak Clean Parameters

**Poster #31 states:** 140--160 F, 4--8 oz/gal, 3--10 min

### Verdict: Confirmed

These are standard alkaline soak cleaner parameters. Temperature range is correct (some cleaners go as low as 120 F or as high as 180 F, but 140--160 F is the mainstream). Concentration of 4--8 oz/gal is typical. Time of 3--10 min covers the range from lightly soiled to moderately soiled parts.

- Confirmed: all three parameters are correct

---

## 13. Poster #31 — Dry/Cure Parameters

**Poster #31 states:** 150--170 F, 15--20 min minimum

### Verdict: Confirmed

Standard cure parameters for trivalent passivates. Some sealers and thick-film trivalent products may call for slightly higher temperatures (up to 200 F), but 150--170 F is the safe generic range.

- Confirmed

---

## 14. Poster #34 — Chemical Equation

**Poster #34 states:** Fe2O3 + 6HCl --> 2FeCl3 + 3H2O

### Verdict: Confirmed — balanced and correct

The equation is balanced: 2 Fe, 3 O, 6 H, 6 Cl on each side. This is the simplified dissolution of iron(III) oxide by hydrochloric acid. In reality, the surface oxide on steel is a mix of FeO, Fe2O3, and Fe3O4, and the acid also attacks the base metal to some degree, but for a poster-level explanation this equation is the correct representative reaction.

- Confirmed: equation is balanced and chemically correct

---

## 15. Poster #34 — HCl vs. H2SO4 Comparison Claims

Reviewing each bullet:

| Claim | Verdict |
|---|---|
| HCl: "Most common choice for steel activation" | Confirmed |
| HCl: "Dissolves oxide faster than H2SO4" | Confirmed — HCl is kinetically faster for iron oxide dissolution |
| HCl: "Less risk of hydrogen absorption" | Confirmed — HCl activation generally produces less atomic hydrogen at equivalent oxide removal rates |
| HCl: "Fumes — ventilation required" | Confirmed |
| HCl: "Attacks copper and brass" | Confirmed — important practical note |
| H2SO4: "Lower fuming than HCl" | Confirmed |
| H2SO4: "Slower oxide removal" | Confirmed |
| H2SO4: "Higher risk of hydrogen absorption on steel" | Confirmed |
| H2SO4: "Better for copper substrates" | Confirmed — dilute H2SO4 does not attack copper significantly |
| H2SO4: "More economical in high-volume operations" | Confirmed — H2SO4 is cheaper per unit of acid equivalent |

All ten comparison bullets are accurate.

---

## 16. Poster #38 — Bake Timing vs. Passivation Sequence

**Poster #38 states:** "Hydrogen bake (if required): 375 F for 23 hr BEFORE passivation"

### Verdict: Confirmed — and this is critically correct

This is one of the most important process sequence details in the entire cluster. The hydrogen embrittlement relief bake MUST occur after plating but BEFORE passivation. If you bake after passivation, you destroy the chromate conversion coating (it dehydrates and cracks at 375 F, losing corrosion protection). Elara has this right, and the "BEFORE" is correctly emphasized.

- Confirmed: bake sequence is correct and the emphasis is warranted

---

## 17. Poster #38 — Over-Cure Temperature

**Poster #38 states:** "Over-curing (> 250 F): film degradation — avoid"

### Verdict: Needs minor correction

For trivalent passivates, degradation begins closer to 200--210 F (93--99 C) for extended exposures. At 250 F (121 C), the damage is severe and rapid. The poster says "> 250 F" as the degradation threshold, which could mislead an operator into thinking 200--250 F is safe.

**Recommended correction:**
- Change from `> 250 F` to `> 200 F (93 C)` for trivalent passivates
- Hex chromates are somewhat more heat-resistant (degrade above 250--300 F), so if the poster wants to give a single number that covers both, `> 200 F` is the safer call

---

## Summary of All Flags

### Needs Correction (5 items)

| # | Poster | Issue | Correction |
|---|---|---|---|
| 1 | #31, #36 | Zn:NaOH ratio convention | Change to NaOH:Zn ratio (8:1 to 12:1 optimal, ~10:1). Industry standard is NaOH:Zn, not Zn:NaOH. |
| 2 | #34 | H2SO4 activation concentration | Change from 2--5% v/v to 5--15% v/v. 2% is too dilute for practical activation. |
| 3 | #38 | Trivalent passivate pH range | Change from 3.5--4.5 to 1.8--4.5, or split by product type. Many tri products run below pH 3.5. |
| 4 | #36 | Iron contamination threshold | Change from > 25 ppm to > 50 ppm. 25 ppm is too conservative for most ANC zinc baths. |
| 5 | #38 | Over-cure temperature | Change from > 250 F to > 200 F (93 C). Trivalent passivates degrade below 250 F. |

### Recommended Improvements (3 items)

| # | Poster | Issue | Suggestion |
|---|---|---|---|
| 6 | #31, #34, #38 | HE threshold | Change > 150 ksi to >= 145 ksi / >= 31 HRC. Aligns with ASTM B850 and adds HRC (what shops actually measure). |
| 7 | #36 | Rectifier wiring labels | Redraw to show (+) to both anode banks, (-) to center cathode. Current left/right label is physically confusing for the symmetric layout. |
| 8 | #36 | Carbonate freeze-out temp | Change < 25 F to < 35 F (2 C). More practical and commonly cited. |

### Confirmed Correct (all other items reviewed)

- Zn 10--14 g/L and NaOH 100--140 g/L: Confirmed
- Cathode efficiency 70--85%: Confirmed
- HCl 5--10% v/v for activation: Confirmed (conservative but correct)
- Activation time 15--60 sec: Confirmed
- Hex chromate pH 1.5--2.5: Confirmed
- Hex chromate time 15--30 sec: Confirmed
- All six salt spray performance ranges: Confirmed
- HE bake: 375 F, within 4 hr, 23 hr minimum, ASTM B850: All confirmed
- Bake BEFORE passivation sequence: Confirmed and critically important
- Soak clean 140--160 F, 4--8 oz/gal, 3--10 min: Confirmed
- Dry/cure 150--170 F, 15--20 min: Confirmed
- Fe2O3 + 6HCl equation: Balanced and correct
- All 10 HCl vs. H2SO4 comparison bullets: Confirmed
- All contamination thresholds except iron: Confirmed
- Zinc balls in Ti baskets: Confirmed

---

## Overall Assessment

Elara's chemistry knowledge across these four workups is genuinely impressive for someone working from secondary sources. The process flow is correct, the sequence is right, the safety callouts are appropriate, and the troubleshooting items are real problems that real shops encounter.

The five corrections above are important — especially the ratio convention (#1) and the trivalent pH range (#3), which would cause practical confusion on a shop floor. The remaining three corrections are accuracy refinements that strengthen credibility with experienced platers.

None of the errors are dangerous. No one is going to get hurt or destroy a bath because of what is written here. But a poster hanging on a production floor needs to match what the operators see in their supplier TDS and daily practice, and these corrections bring the content into full alignment.

---

*Tyler — A Brite Company*
*Validation complete — 2026-04-25*
