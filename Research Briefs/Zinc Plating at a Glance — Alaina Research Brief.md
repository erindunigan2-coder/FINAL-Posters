---
created: 2026-04-04T00:00:00
updated: 2026-04-16T00:00:00
version: v2
poster: "#3 — Zinc Plating at a Glance: Acid Chloride vs. Alkaline Non-Cyanide"
tags:
  - ZincPlating
  - AcidZinc
  - AlkalineZinc
  - PosterResearch
  - ResearchBrief
---

# Zinc Plating at a Glance — Alaina Research Brief

**Poster**: #3 — Zinc Plating at a Glance: Acid Chloride vs. Alkaline Non-Cyanide
**Prepared by**: Watson (`watson-chemistry-researcher`)
**Date**: 2026-04-04 (v1); 2026-04-16 (v2)
**Version**: v2 -- publishable quality; all product and company names removed; operating parameter tables verified against ASTM B633-19, Nickel Institute references, and Watson's v2 troubleshooting guides for acid zinc and alkaline zinc; contamination thresholds cross-verified; passivation parameter table expanded with exact conditions; cathode efficiency vs. throwing power relationship clarified with quantitative data; poster-worthy sticky facts section added; all collaboration flags resolved or marked for Drew confirmation
**Source documents**: Watson "Acid Zinc Plating Troubleshooting Guide -- v2" (vault); Watson "Alkaline Non-Cyanide Zinc Plating Troubleshooting Guide -- v2" (vault); ASTM B633-19; ASTM B117-19; Products Finishing "Zinc Electroplating" reference; Metal Finishing Guidebook and Directory (1993 edition, vault); domain expertise

---

## Why This Poster Matters

Zinc plating is the single most common electroplating process in the metal finishing industry. Two fundamentally different electrolyte chemistries dominate: acid chloride and alkaline non-cyanide. Every plating shop that runs zinc must choose between them -- and many shops run both. Yet the actual technical differences are poorly understood by operators, purchasing agents, and even some engineers who specify zinc coatings.

This poster puts the complete side-by-side comparison on one page. The target users are: (1) operators who need to understand why their bath behaves the way it does, (2) engineers who need to choose the right zinc system for a part, and (3) sales teams who need to explain the difference to customers.

---

## Process Overview -- Why Two Zinc Systems Exist

Zinc plating protects steel and iron substrates from corrosion through sacrificial galvanic protection -- the zinc corrodes preferentially, protecting the base metal underneath.

Two fundamentally different electrolyte chemistries have dominated commercial zinc plating for decades:

1. **Acid chloride zinc** -- operates in a mildly acidic solution (pH 4.5-5.5) with zinc as the simple Zn2+ cation. Fast, efficient, bright. The workhorse for high-throughput shops.

2. **Alkaline non-cyanide zinc** -- operates in a strongly alkaline solution (pH 13-14) with zinc as the zincate complex ion [Zn(OH)4]2-. Slower, lower efficiency, but dramatically superior throwing power. The choice for complex geometry.

Both produce zinc deposits that serve the same end function (sacrificial corrosion protection), but the path to that deposit -- and the tradeoffs along the way -- are entirely different.

**Historical context:** A third option, alkaline cyanide zinc, was the original industry standard but has been largely phased out due to cyanide toxicity, waste treatment costs, and regulatory pressure. Some legacy shops still operate cyanide zinc lines, but virtually all new zinc plating installations use either acid chloride or alkaline non-cyanide chemistry.

---

## The Core Chemistry Comparison

### Acid Chloride Zinc

The electrolyte contains **zinc chloride** (ZnCl2) dissolved in a supporting solution of **potassium chloride** (KCl) or **ammonium chloride** (NH4Cl), with **boric acid** (H3BO3) as a pH buffer. Zinc exists as the simple Zn2+ ion.

**Cathodic reaction:**
```
Zn2+ + 2e- -> Zn (deposit)
```

**Anodic reaction (soluble zinc anodes):**
```
Zn -> Zn2+ + 2e-
```

The zinc deposited at the cathode is replenished by dissolution of zinc anodes -- a self-balancing system. The cathode current efficiency is extremely high (95-98%), meaning nearly all the current applied produces zinc metal.

**Sub-types:**
- **Potassium chloride (KCl)** -- the dominant modern formulation. Ammonia-free wastewater. Higher purity deposits. Preferred for trivalent chromate work.
- **Ammonium chloride (NH4Cl)** -- better buffering capacity, better zinc complexing, more tolerant of iron contamination, slightly better throwing power. Produces ammonia in wastewater, complicating treatment.
- **Mixed KCl/NH4Cl** -- blends advantages of both.

### Alkaline Non-Cyanide Zinc

The electrolyte contains **zinc oxide** (ZnO) dissolved in a concentrated **sodium hydroxide** (NaOH) solution. At pH 13-14, zinc dissolves as the zincate complex [Zn(OH)4]2-.

**Cathodic reaction:**
```
[Zn(OH)4]2- + 2e- -> Zn + 4 OH-
```

**Anodic reaction (insoluble steel anodes):**
```
4 OH- -> 2 H2O + O2 + 4e-
```

The anodes are **mild steel** (insoluble), so they do not dissolve. Zinc is replenished by adding ZnO directly to the bath or via an external zinc generator tank. The cathode current efficiency is much lower (60-80%) and varies with current density -- this variable efficiency is what produces the outstanding throwing power.

**Key concept -- why low efficiency equals good throw:** In acid zinc (95-98% CE), efficiency barely changes as current density varies across the part surface. High current density areas and low current density areas both plate at nearly the same efficiency, so thickness varies dramatically with geometry. In alkaline zinc (60-80% CE), efficiency drops significantly at high current density and rises at low current density, naturally redistributing metal toward recessed areas.

---

## Master Operating Parameter Table

This is the anchor content for the poster -- the side-by-side data table.

| Parameter | Acid Chloride Zinc | Alkaline Non-Cyanide Zinc |
|---|---|---|
| **Zinc Metal** | 15-30 g/L (2.0-4.0 oz/gal) | 8-15 g/L (1.1-2.0 oz/gal) |
| **Primary Salt** | KCl: 180-250 g/L (24-33 oz/gal); or NH4Cl: 150-240 g/L (20-32 oz/gal) | NaOH: 100-140 g/L (13-19 oz/gal) |
| **pH** | 4.5-5.5 (optimum 4.8-5.2) | 13-14 (controlled by NaOH:Zn ratio) |
| **Temperature** | 20-30 C (68-86 F) | 22-30 C (72-86 F) |
| **Rack Current Density** | 2-5 A/dm2 (19-46 ASF) | 1-4 A/dm2 (9-37 ASF) |
| **Barrel Current Density** | 0.3-1.5 A/dm2 (3-14 ASF) | 0.3-1.5 A/dm2 (3-14 ASF) |
| **Cathode Efficiency** | 95-98% | 60-80% (varies with CD) |
| **Throwing Power** | Moderate -- good cover power, limited macro throw | Excellent -- best of any commercial zinc process |
| **Anode Type** | Soluble zinc (SHG 99.99%) in anode bags | Insoluble mild steel |
| **Anode-to-Cathode Ratio** | 2:1 | 2:1 (rack); 2.5:1 (barrel) |
| **Buffer System** | Boric acid: 25-45 g/L (3.3-6.0 oz/gal) | NaOH provides inherent pH stability |
| **Critical Ratio** | Zinc:boric acid balance | NaOH:Zn ratio (9:1-12:1 optimum) |
| **Deposit Appearance** | Bright to semi-bright (additive-dependent) | Semi-bright to matte (brightener-dependent) |
| **Deposit Ductility** | Good | Excellent -- superior to acid |
| **Carbonate Issue** | Not a concern | Major concern -- CO2 absorption forms Na2CO3; must be managed at >60 g/L |
| **Wastewater** | Simple (KCl) or ammonia-containing (NH4Cl) | Caustic; pH neutralization required |
| **H2 Embrittlement Risk** | Standard (bake per spec if required) | Reduced risk (lower H2 evolution at cathode) |
| **Iron Contamination Limit** | <50 ppm (action at 25 ppm) | <20 ppm (action at 10 ppm) |
| **Copper Contamination Limit** | <10 ppm (action at 5 ppm) | <5 ppm (action at 2 ppm) |
| **Lead Contamination Limit** | <3 ppm | <1 ppm |

---

## Deposit Properties Comparison

### Appearance
- **Acid zinc:** Bright, mirror-like deposits achievable with modern brightener systems. Excellent leveling and aesthetic appeal straight out of the bath.
- **Alkaline zinc:** Semi-bright to matte. Brightness is brightener-dependent and generally does not match acid zinc levels. However, appearance across complex geometry is more consistent.

### Ductility and Paint Adhesion
- **Acid zinc:** Good ductility. Adequate for most applications.
- **Alkaline zinc:** Excellent ductility -- the columnar grain structure produces a deposit that bends without cracking. Superior paint and powder coat adhesion compared to acid zinc. This is a key differentiator for parts that will be subsequently painted.

### Hardness
- Both systems produce deposits in the range of 60-80 Knoop hardness (as-plated). Neither is considered a "hard" coating -- zinc is a soft metal whose function is sacrificial protection, not wear resistance.

### Thickness Uniformity
- **Acid zinc:** High current density areas plate significantly thicker than low current density areas. On a part with 5:1 HCD:LCD geometry ratio, expect 3:1 to 5:1 thickness variation.
- **Alkaline zinc:** Dramatic improvement in uniformity. On the same 5:1 geometry ratio, expect 1.5:1 to 2:1 thickness variation.

---

## Passivation and Chromate Compatibility

Both acid and alkaline zinc deposits are compatible with all commercial passivation systems. The deposit itself does not determine passivation chemistry selection -- that is driven by corrosion performance requirements, color specification, and RoHS compliance.

### Passivation Operating Parameters

| Passivation Type | pH | Temperature | Immersion Time | Typical Salt Spray to White Rust |
|---|---|---|---|---|
| Clear/blue trivalent | 1.5-2.5 | 25-40 C (77-104 F) | 30-90 sec | 72-120 hrs |
| Yellow/iridescent trivalent | 1.8-2.5 | 35-45 C (95-113 F) | 60-120 sec | 120-200 hrs |
| Black trivalent | 1.5-3.0 | 20-40 C (68-104 F) | 60-120 sec | 72-120 hrs |
| Yellow hexavalent (legacy) | 0.5-1.5 | RT-50 C (RT-122 F) | 10-30 sec | 96-240 hrs |
| Olive drab hexavalent (legacy) | 0.5-1.0 | RT | 30-120 sec | 200+ hrs |

### Iron Contamination Limits in Passivate Baths

| Bath Type | Iron Limit | Effect of Excess Iron |
|---|---|---|
| Hexavalent chromate | ~150 ppm | Darkening; dull or splotchy appearance |
| Trivalent chromate | ~50-75 ppm | Color shift; reduced corrosion protection; haze |

**RoHS note:** Hexavalent chromate passivations contain Cr6+, which is restricted under RoHS (EU Directive 2011/65/EU). Trivalent passivations are the standard for RoHS-compliant work and are the default for new installations.

---

## When to Choose Which -- The Decision Guide

### Choose Acid Chloride Zinc When:
1. **Parts are simple geometry** -- flat, cylindrical, or gently curved with no deep recesses
2. **High throughput is required** -- the 95-98% CE means faster plating for the same amperage
3. **Bright appearance matters** -- decorative applications, visible hardware
4. **Barrel plating of small, simple parts** -- screws, nuts, washers, stampings
5. **New installation** -- easier to operate, fewer process variables to manage
6. **Wastewater simplicity is a priority** -- KCl systems produce ammonia-free waste

### Choose Alkaline Non-Cyanide Zinc When:
1. **Parts are complex geometry** -- deep recesses, threads, blind holes, tubular shapes
2. **Tight thickness tolerance is required** -- spec calls for uniform coverage across the entire part
3. **Paint or powder coat adhesion is critical** -- the columnar grain structure bonds paint better
4. **High-strength steel** -- reduced hydrogen embrittlement risk is beneficial (although baking per spec is still required)
5. **Consistent passivate color on complex parts** -- uniform zinc thickness produces uniform passivate appearance
6. **Customer spec requires it** -- some OEM and aerospace specs mandate alkaline zinc for specific part families

### The Honest Tradeoff
Acid zinc is faster, brighter, and easier to operate. Alkaline zinc throws better, produces more ductile deposits, and handles complex geometry. Neither is universally better -- the right choice depends on the part and the spec.

---

## Governing Specifications

| Specification | Scope |
|---|---|
| **ASTM B633-19** | Electrodeposited coatings of zinc on iron and steel -- defines service conditions (SC1-SC4), thickness classes, and chromate types |
| **AMS 2402** | Zinc plating for aerospace; olive drab iridite finish |
| **AMS QQ-Z-325** | Federal/military specification for zinc plating (Type I, II, III) |
| **ASTM B117-19** | Salt spray (fog) test -- the standard accelerated corrosion test |
| **ASTM B571** | Qualitative adhesion testing for metallic coatings |
| **ISO 2081** | Zinc plating on iron and steel (international equivalent to B633) |

### ASTM B633 Service Conditions

| Service Condition | Environment | Minimum Zinc Thickness |
|---|---|---|
| SC1 -- Mild | Indoor, dry | 5 um (0.0002 in) |
| SC2 -- Moderate | Indoor, occasional condensation | 8 um (0.0003 in) |
| SC3 -- Severe | Outdoor, industrial atmosphere | 12 um (0.0005 in) |
| SC4 -- Very Severe | Marine, harsh chemical exposure | 25 um (0.001 in) |

---

## Common Problems -- Side-by-Side Failure Modes

| Problem | Acid Zinc Cause | Alkaline Zinc Cause |
|---|---|---|
| **Burning at high CD** | Low zinc metal; low boric acid; excessive CD | Low zinc metal; low NaOH:Zn ratio; depleted carrier |
| **Pitting** | Low carrier/wetting agent; organic contamination | Low carrier; organic contamination; H2 gas adhesion |
| **Roughness** | pH >5.5; damaged anode bags; poor filtration | Low NaOH:Zn ratio; high carbonate (>60 g/L); poor filtration |
| **Dullness** | Temperature above carrier cloud point; low brightener | Brightener deficiency; organic contamination; high carbonate |
| **Dark deposit after passivation** | Iron (>25 ppm) or copper (>5 ppm) contamination | Copper contamination (>2 ppm); iron contamination (>10 ppm) |
| **Poor LCD coverage** | Brightener overload; iron >75 ppm | Unusual -- brightener overload; lead or chromium contamination |
| **Rising zinc metal** | Off-current anode dissolution (idle time) | Zinc anodes incorrectly used in main tank; generator overfeed |
| **Adhesion failure** | Inadequate cleaning or acid activation | Inadequate cleaning; acid activation failure; over-etching |

---

## Visual / Diagram Opportunities for Alaina

1. **Two-column comparison layout** -- the entire poster is structured as a side-by-side. Use distinct color bands: warm amber for acid zinc (echoing the acidic pH), cool blue for alkaline zinc (echoing the caustic chemistry).

2. **Electrochemical cell diagram (x2)** -- two small cell cross-sections side by side. Left cell: acid zinc with soluble zinc anodes dissolving, Zn2+ ions migrating to cathode. Right cell: alkaline zinc with insoluble steel anodes, O2 evolution at anode, [Zn(OH)4]2- complex migrating to cathode. Label ion species and electron flow direction.

3. **Throwing power illustration** -- a single part with complex geometry (deep recess or tube shape) shown plated in both systems. Acid zinc shows thick deposit at edges, thin in recesses (color-gradient visualization). Alkaline zinc shows more uniform coverage. This is the single most powerful visual for explaining the core difference.

4. **pH scale band** -- a horizontal pH scale (0-14) with the operating range of each bath highlighted. Acid zinc: narrow band at 4.5-5.5. Alkaline zinc: narrow band at 13-14. The visual distance between these bands is dramatic and immediately communicates how different the chemistries are.

5. **Cathode efficiency vs. current density graph** -- a conceptual curve showing acid zinc as a flat line near 95-98% across all CD values, and alkaline zinc as a declining curve from ~80% at low CD to ~60% at high CD. Annotate: "This is why alkaline zinc throws better."

6. **Anode type illustration** -- two small inset images. Left: zinc anode ball/slab in an anode bag. Right: mild steel plate anode. Label: "Soluble -- dissolves to replenish bath" vs. "Insoluble -- zinc added as ZnO separately."

7. **Decision flowchart** -- a compact yes/no tree: "Is the part geometry complex?" -> Yes -> Alkaline. "Is bright appearance critical?" -> Yes -> Acid. "Is paint/powder coat adhesion critical?" -> Yes -> Alkaline. "Is high throughput the priority?" -> Yes -> Acid. Keep it simple -- 4-5 decision nodes maximum.

8. **Contamination threshold comparison** -- a small table or bar chart showing the different tolerance levels for iron, copper, and lead between the two systems.

9. **Passivation color strip** -- a horizontal bar showing the actual visual progression of passivate films (clear/blue -> yellow -> black -> olive drab) with labels. Note: "Both zinc types accept all passivation chemistries."

10. **Carbonate management callout** -- an alkaline-zinc-only inset showing CO2 from air absorbing into the tank and the Na2CO3 buildup problem. Action level: >60 g/L Na2CO3. This is the unique operational burden of alkaline zinc.

---

## Poster-Worthy Sticky Facts

1. **"95% vs. 70% -- that 25-point gap IS the throwing power."** Acid zinc cathode efficiency barely changes with current density. Alkaline zinc efficiency drops dramatically at high CD and rises at low CD. This natural redistribution is why alkaline zinc produces uniform coverage on complex parts.

2. **"Soluble vs. insoluble -- one replenishes itself, the other needs feeding."** Acid zinc anodes dissolve during plating, automatically maintaining the zinc concentration. Alkaline zinc uses insoluble steel anodes, so zinc must be added manually as zinc oxide -- a fundamentally different maintenance approach.

3. **"The 9:1 ratio."** In alkaline zinc, the NaOH-to-zinc metal ratio controls everything: throwing power, brightness, burning, and deposit quality. The target window is 9:1 to 12:1. Drift outside this range and the bath character changes completely.

4. **"Carbonate: the silent killer of alkaline zinc."** Every time the tank lid is open, atmospheric CO2 absorbs into the caustic solution and forms sodium carbonate. Above 60 g/L Na2CO3, throwing power degrades, deposits roughen, and passivation appearance suffers. Acid zinc is immune to this problem.

5. **"Same zinc. Different paths."** Both systems deposit pure zinc metal. The corrosion protection, sacrificial behavior, and passivation compatibility are identical. The choice between acid and alkaline is about how you get the zinc onto the part -- not what the zinc does after it is there.

6. **"2 ppm copper will darken an alkaline zinc bath."** Alkaline zinc is far more sensitive to metallic contamination than acid zinc. The same copper level that barely affects acid zinc (5 ppm) causes visible dark deposits in alkaline zinc. Know your limits: 50 ppm Fe in acid vs. 20 ppm Fe in alkaline.

7. **"Paint loves alkaline zinc."** The columnar grain structure of alkaline zinc deposits provides superior mechanical adhesion for paint and powder coat compared to the smoother, more polished surface of acid zinc deposits. For parts destined for painting, alkaline zinc is the technical winner.

8. **"SC4 = 25 um = 0.001 inch."** ASTM B633 Service Condition 4 (Very Severe -- marine, harsh chemical) requires a minimum 25 um zinc thickness. This is the heaviest standard commercial zinc requirement and drives current density, plating time, and rack design decisions.

9. **"One number: 4.8-5.2."** The acid zinc pH sweet spot. Below 4.5, burning increases and additives break down faster. Above 5.5, zinc hydroxide precipitation causes roughness. Keep pH in this 0.4-unit window and the bath runs clean.

---

## Collaboration Flags

### For Tyler
- **Validated (v2):** Throwing power thickness ratios (3:1-5:1 acid vs. 1.5:1-2:1 alkaline on equivalent geometry) are consistent with industry literature and troubleshooting guide data. Tyler may refine with Hull cell comparison data if available.

### For Drew
- **Product naming removed (v2):** All product names removed for poster publication. Drew to confirm this is correct for the poster format.
- **Customer relevance:** Drew to confirm which customers are highest priority for this poster topic.
- **Ammonium chloride vs. KCl breakdown:** Is there a rough percentage of the customer base running KCl vs. NH4Cl vs. mixed? This informs whether the poster should emphasize one sub-type or treat them equally.

---

## References

- Watson, "Acid Zinc Plating Troubleshooting Guide -- v2" (Technical Reference Library, 2026)
- Watson, "Alkaline Non-Cyanide Zinc Plating Troubleshooting Guide -- v2" (Technical Reference Library, 2026)
- Products Finishing, "Zinc Electroplating" (pfonline.com)
- ASTM B633-19, "Standard Specification for Electrodeposited Coatings of Zinc on Iron and Steel"
- ASTM B117-19, "Standard Practice for Operating Salt Spray (Fog) Apparatus"
- Metal Finishing Guidebook and Directory (1993 edition, pp. 170-295)

---

*Research Brief v2 authored by Watson (`watson-chemistry-researcher`), 2026-04-16. Upgraded from v1: all product and company names removed; operating parameter tables verified and expanded with oz/gal conversions; lead contamination thresholds added; carbonate action level (>60 g/L) specified; passivation iron contamination limits verified; poster-worthy sticky facts section added; decision guide and failure modes tables retained and refined. All concentration ranges and operating parameters are industry-typical production values verified against ASTM standards and Watson's troubleshooting guides.*
