---
Project: Plating Posters Inc
Poster Number: 198
Title: "Aluminum Conversion Coating -- Dry / Seal"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Conversion Coating Clusters — Watson Research Brief (CC-06 Section 6.8)"
Technical Source: Drying and post-treatment/seal stage for Ti/Zr and non-chromate aluminum conversion coatings. Covers air dry, low-temperature oven cure, thermal cure requirements for hybrid silane/Zr systems, supplementary sealers, and standards.
Process Scope: Aluminum conversion coating -- Stage 7 dry / seal (post-treatment)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ConversionCoating
  - AluminumConversion
  - DryingSeal
  - PostTreatment
  - ConstructionWorkup
  - ClusterCC06
---

# Poster #198 -- Construction Workup
## Aluminum Conversion Coating -- Dry / Seal

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the final stage poster for CC-06. For pure Zr coatings, drying is straightforward -- air dry or low-temperature oven. But for hybrid Zr/silane systems (increasingly common), a thermal cure is REQUIRED to crosslink the organic component. The poster must make this distinction clear: check your supplier's TDS. Over-cure degrades the film. Under-cure leaves the organic component unreacted.

The poster also covers supplementary sealers (silane topcoats, organic polymers) and the standards landscape, which for Zr coatings is notably sparse compared to chromate -- no dedicated MIL-SPEC exists as of 2026.

---

## Part 1 -- Workflow Orientation

### Design Capabilities for This Poster

- Text boxes with precise font, size, weight, color, and spacing control
- Solid-color rectangles and rounded rectangles for flow boxes, callout panels, table rows, and accent borders
- Arrow/line elements connecting flow boxes in sequence
- Color fills set to exact hex values
- Background page color set to exact hex
- Export at print-quality PDF (300 DPI equivalent via print export)

### Limitations to Flag

1. **Stage detail panel (Block B -- HERO):** Three drying/seal pathways (air dry, oven cure, thermal cure for hybrids).
2. **Thermal cure decision tree (Block C):** Is your coating a hybrid? -> YES = thermal cure required -> Check supplier TDS for temp/time.
3. **Supplementary sealers panel (Block D).**
4. **Standards and specifications table (Block E).**
5. **Troubleshooting strip (Block F).**

---

## Part 2 -- Document Setup Instructions

Standard: 24x36", `#1A1F2E`, locked palette and fonts. Standard guides.

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- DRY / SEAL STAGE DETAIL / HERO (2.9"--15.5" / ~12.6" tall)
  Block B: Three drying pathways (air dry / oven / thermal cure)
  Block C: Thermal cure decision tree

ZONE 3 -- SUPPLEMENTARY SEALERS (15.5"--22.0" / ~6.5" tall)
  Block D: Sealer options and when to use them

ZONE 4 -- STANDARDS AND SPECIFICATIONS (22.0"--28.5" / ~6.5" tall)
  Block E: Standards table + spec landscape callout

ZONE 5 -- TROUBLESHOOTING QUICK HITS (28.5"--32.5" / ~4.0" tall)
  Block F: 4-problem strip

ZONE 6 -- FOOTER BAND (32.5"--36.0" / ~3.5" tall)
  Block G: Disclaimer + footer
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**BLOCK A -- Headline**
- Font: Barlow Condensed ExtraBold, 76 pt, `#F0EDE8`, letter spacing -4
- Text: `ALUMINUM CONVERSION COATING`
- X: 0.5", Y: 0.5", W: 23.0"

**BLOCK A -- Subheading**
- Font: Barlow SemiBold, 36 pt, `#E8A020` (Amber)
- Text: `Stage 7 -- Dry / Seal`
- Y: 1.5"

**BLOCK A -- Tagline**
- Font: Barlow SemiBold, 20 pt, `#F0EDE8` at 65%
- Text: `Air dry, oven cure, or thermal crosslink -- the right answer depends on your coating chemistry. Check your supplier TDS.`
- Y: 2.2"

---

### ZONE 2 -- Dry / Seal Stage Detail (HERO)

**Section label:**
- Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `DRY / SEAL -- THREE PATHWAYS`

---

**BLOCK B -- Three Drying Pathways**

Y: 3.8" to 10.5". Three side-by-side panels.

| Pathway | X | W | Accent | Key Data |
|---|---|---|---|---|
| Air Dry | 0.5" | 7.33" | `#2EC4B6` | Ambient temp, forced air OK, 15--30 min until dry. Simplest option. For pure Zr (inorganic) coatings only. No crosslinking needed. |
| Low-Temp Oven | 8.08" | 7.33" | `#E8A020` | 180--250 F (82--121 C), 5--15 min. Faster drying. Standard for production lines. Acceptable for most Zr formulations. |
| Thermal Cure (Hybrids) | 15.67" | 7.83" | `#27AE60` | 200--350 F (93--177 C), 5--15 min. REQUIRED for silane/Zr hybrid coatings. Crosslinks the organic component. Temperature and time per supplier TDS. |

Each panel: Rounded rect, H: 6.5", fill `#1E2435`, radius 6, top accent 4 pt.

Interior per panel:
- Pathway name: Barlow SemiBold, 18 pt, in accent color
- Parameters: JetBrains Mono 13 pt `#F0EDE8`
- When to use: Inter Regular 13 pt `#F0EDE8`
- Caution: Inter Medium 13 pt `#E05C5C` (where applicable)

**Air Dry panel:**
```
Temperature:   Ambient
Method:        Room temp or forced air (filtered)
Time:          15--30 min until touch-dry
When:          Pure Zr (inorganic) formulations
Caution:       Slow; dust contamination risk
```

**Low-Temp Oven panel:**
```
Temperature:   180--250 F (82--121 C)
Method:        Convection oven
Time:          5--15 min
When:          Production lines needing throughput
Caution:       Do NOT exceed 250 F for pure Zr coatings
               -- over-cure degrades the film
```

**Thermal Cure (Hybrids) panel:**
```
Temperature:   200--350 F (93--177 C) -- PER SUPPLIER TDS
Method:        Convection oven with calibrated thermocouples
Time:          5--15 min at metal temp (not air temp)
When:          Silane/Zr hybrid coatings (e.g., oxsilan)
CRITICAL:      Under-cure = uncrosslinked organic = poor adhesion
               Over-cure = degraded film = poor corrosion protection
               Follow supplier cure window EXACTLY
```

---

**BLOCK C -- Thermal Cure Decision Tree**

Y: 11.0" to 15.0". Single wide panel.

Rounded rect, X: 0.5", Y: 11.0", W: 23.0", H: 3.8", fill `#1E2435`, radius 8, left accent 0.06" `#E8A020`.

Title: `DO YOU NEED A THERMAL CURE?` -- Barlow SemiBold, 20 pt, `#E8A020`

Decision flow (Inter Medium 14 pt `#F0EDE8`):

```
Is your Ti/Zr coating a HYBRID (silane + inorganic)?

  YES --> Thermal cure is REQUIRED
          - Check supplier TDS for exact temp and time
          - Measure METAL temperature, not oven air temperature
          - Typical: 200--350 F for 5--15 min
          - Cure window is narrow -- calibrate your oven

  NO (pure inorganic Zr) --> Air dry or low-temp oven is sufficient
          - No crosslinking needed
          - 180--250 F for 5--15 min (oven) or ambient (air dry)
          - Do not exceed 250 F -- degrades inorganic film

  NOT SURE? --> Check your supplier TDS
          - If the TDS specifies a "cure temperature," it is a hybrid
          - If the TDS says only "dry," it is pure inorganic
```

---

### ZONE 3 -- Supplementary Sealers

**Section label:**
- Centered. Y: 15.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `SUPPLEMENTARY SEALERS -- DO YOU NEED ONE?`

**BLOCK D -- Sealer Options Panel**

Y: 16.3" to 21.8". Three-column layout.

| Sealer Type | X | W | Accent | Key Data |
|---|---|---|---|---|
| Silane/Siloxane | 0.5" | 7.33" | `#27AE60` | Most common supplement. Hydrophobic barrier. Can extend bare SST from 24--72 hr to 200+ hr. Applied by dip or spray, ambient. |
| Organic Polymer | 8.08" | 7.33" | `#2EC4B6` | Waterborne or solvent-borne. Thicker film (1--5 um). Excellent paint base. May need thermal cure. |
| None Required | 15.67" | 7.83" | `#E8A020` | Many modern Zr systems are designed as COMPLETE single-stage treatments. The coating + hybrid organic = sealer built in. Check supplier TDS. |

Each panel: Rounded rect, H: 5.0", fill `#1E2435`, radius 6, top accent 4 pt.

Interior per panel:
- Sealer name: Barlow SemiBold 16 pt in accent color
- Description: Inter Regular 13 pt `#F0EDE8`
- Application: JetBrains Mono 12 pt `#F0EDE8`
- When to use: Inter Medium 12 pt in accent color

---

### ZONE 4 -- Standards and Specifications

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `STANDARDS AND SPECIFICATIONS`

**BLOCK E -- Standards Table + Landscape Callout**

Y: 22.9" to 28.3".

**Standards Table (left, W: 14.0"):**
- Rounded rect, X: 0.5", Y: 22.9", W: 14.0", H: 5.0", fill `#1E2435`, radius 8

| Standard | Scope |
|---|---|
| SAE ARP 5903 | Evaluation of non-chromate conversion coatings (test methods, NOT specification) |
| ASTM D5894 | Cyclic salt spray / UV testing (often used for non-chrome evaluation) |
| ASTM B921 | Non-hexavalent chromium conversion coatings on aluminum (covers Zr) |
| Automotive OEM specs | GM, Ford, Toyota -- each has proprietary approval for specific Zr products |
| No dedicated MIL-SPEC | As of 2026, no MIL-DTL or MIL-PRF exists for Zr conversion coatings |

Data: JetBrains Mono 12 pt. Standard names: Inter Medium 13 pt.

**Spec Landscape Callout (right, W: 8.5"):**
- Rounded rect, X: 14.75", Y: 22.9", W: 8.75", H: 5.0", fill `#1E2435`, left accent `#E8A020`
- Title: `THE STANDARDS GAP` -- Barlow SemiBold, 18 pt, `#E8A020`

Content (Inter Regular 13 pt `#F0EDE8`):
```
Zr conversion coatings are commercially
mature but specification-immature.

No MIL-SPEC means each customer, OEM,
or prime contractor must individually
qualify the coating + supplier.

This is changing. The aerospace industry
is actively developing specifications to
formalize what automotive has already
adopted at scale.

Until then: qualify to your customer's
requirements and the supplier's TDS.
```

---

### ZONE 5 -- Troubleshooting Quick Hits

**Section label:**
- Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`
- Text: `QUICK TROUBLESHOOTING -- 4 COMMON PROBLEMS`

**BLOCK F -- Four Problem Cards**

Y: 29.4" to 32.3". Same construction as Poster #191.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | POOR PAINT ADHESION | Hybrid coating under-cured; organic not crosslinked | Verify oven temp at PART surface; extend cure time |
| 2 | 6.33" | COATING DEGRADATION | Over-cure; oven too hot; dwell time too long | Reduce oven temp; calibrate thermocouples; follow TDS |
| 3 | 12.16" | BLISTERING UNDER PAINT | Moisture trapped under paint; incomplete drying | Extend dry time; verify parts are fully dry before paint |
| 4 | 18.0" | PREMATURE CORROSION | No sealer on bare Zr; thin coating; specification not met | Add supplementary sealer; verify XRF coating weight |

---

### ZONE 6 -- Footer Band

Standard footer. Title: `Aluminum Conversion Coating -- Dry / Seal`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Parameters shown are typical for drying and sealing stages in Ti/Zr and non-chromate conversion coating systems. Cure temperatures and times vary significantly by supplier formulation. Consult your process supplier's TDS for application-specific guidance.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Al Conversion Dry Seal -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The three-pathway layout in Zone 2 is designed to prevent the most common mistake: treating all Zr coatings the same in the oven. The decision tree makes it binary -- hybrid = thermal cure required, pure inorganic = air dry or low-temp oven. The supplementary sealer section addresses the growing number of "all-in-one" hybrid Zr/silane products that build the sealer INTO the coating chemistry.

The standards gap callout is unique to this cluster -- no other conversion coating process in the series lacks a dedicated MIL-SPEC. This is important context for aerospace shops evaluating Zr as a chromate replacement.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #198 -- Construction Workup v1.0*
*2026-04-26*
