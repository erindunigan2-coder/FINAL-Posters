---
Project: Plating Posters Inc
Poster Number: 393
Title: "Safety & PPE -- Neutralization & Rinse Systems"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Chemical Treatment Clusters — Watson Research Brief (CT-8)"
Technical Source: OSHA 29 CFR 1910 standards, cyanide-acid segregation requirements (HCN generation), dilute acid/alkali hazards, Cr(VI) mist exposure at chrome rinse stations. Values per EPA 40 CFR, OSHA standards, and general industry knowledge.
Process Scope: Neutralization and rinse system safety -- dilute acid/alkali hazards, cyanide segregation (HCN), cross-contamination awareness, PPE, emergency response
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Neutralization
  - RinseSystems
  - Safety
  - PPE
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT08
---

# Poster #393 -- Construction Workup
## Safety & PPE -- Neutralization & Rinse Systems

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Rinse tanks are "low hazard" on paper -- dilute solutions, ambient temperature, no exotic chemistry. But there is one scenario that kills people: mixing acid and cyanide rinse water generates hydrogen cyanide gas (HCN), which is lethal at 300 ppm. This poster makes that hazard impossible to miss while also covering the more routine hazards of dilute acid/alkali neutralization tanks and hexavalent chromium mist at chrome rinse stations.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Cyanide-acid segregation hero (Block B -- HERO):** The single most critical safety message in this cluster -- acid + cyanide = HCN gas. Visually dominant, impossible to miss.

2. **Routine hazard panel (Block C):** Dilute acid/alkali, Cr(VI) mist, and cross-contamination risks.

3. **PPE grid (Block D):** Minimal PPE for routine rinse, escalated PPE for neutralization and chrome-adjacent stations.

4. **Emergency procedures callout (Block E):** HCN exposure, acid/alkali splash, Cr(VI) exposure.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 14.0" / 21.5" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- CYANIDE-ACID SEGREGATION HERO (2.9"--14.0" / ~11.1" tall)
  Block B: HCN generation warning (HERO)
  Block C: Routine hazard panels

ZONE 3 -- PPE REQUIREMENTS (14.0"--21.5" / ~7.5" tall)
  Block D: PPE grid by station type

ZONE 4 -- EMERGENCY PROCEDURES (21.5"--28.5" / ~7.0" tall)
  Block E: Emergency callout (HCN, acid/alkali, Cr(VI))

ZONE 5 -- OSHA / REGULATORY STRIP (28.5"--32.5" / ~4.0" tall)
  Block F: Key OSHA citations

ZONE 6 -- FOOTER BAND (32.5"--36.0")
  Block G: Standard footer
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE & NEUTRALIZATION SAFETY` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Safety & PPE -- From Dilute Solutions to Lethal Gas in One Wrong Connection` -- 32 pt `#E05C5C` (Coral). Y: 1.5".
**Tagline:** `Rinse tanks look harmless. Most are. But one cross-connection between acid and cyanide drains generates hydrogen cyanide gas -- and HCN kills at 300 ppm. Segregation is non-negotiable.` -- 20 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Cyanide-Acid Segregation Hero

**Section label:** Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#E05C5C`.

> LIFE SAFETY: CYANIDE + ACID = HCN GAS

---

**BLOCK B -- HCN Warning Hero**

Y: 3.8" to 9.5". Full width.

Rounded rect, X: 0.5", W: 23.0", H: 5.5", fill `#E05C5C` at 10%, radius 8.
Border: 3 pt `#E05C5C`.
Left accent: 0.10" `#E05C5C`.

**Interior:**

- Title: `NEVER MIX ACID AND CYANIDE WASTE STREAMS` Barlow Condensed ExtraBold 32 pt `#E05C5C`

- Chemical equation: JetBrains Mono 20 pt `#F0EDE8`:
```
CN- + H+  -->  HCN (gas)
```

- Subtitle: `Hydrogen cyanide (HCN) is lethal at approximately 300 ppm in air` Inter Medium 16 pt `#E05C5C`

- Body: Inter Regular 14 pt `#F0EDE8`:
```
Plating shops with BOTH cyanide and acid processes MUST have:
  - Separate drain systems for cyanide and acid rinse water
  - Separate collection sumps
  - Physical barriers preventing cross-connection
  - Signage at every drain identifying the waste stream

Cyanide waste must be treated (alkaline chlorination or
other approved method) BEFORE combining with acid streams.

This is not a guideline. This is a life safety requirement.
```

- Callout at bottom: Inter Medium 14 pt `#E8A020`:
```
EPA requires cyanide-bearing waste to be segregated and treated
before mixing with any acidic waste stream.
```

---

**BLOCK C -- Routine Hazard Panels**

Y: 10.0" to 13.8". Three callout boxes side by side.

Each box: Rounded rect, W: 7.33", H: 3.5", fill `#1E2435`, radius 6, left accent 0.06".

| Box | X | Hazard | Detail | Accent |
|---|---|---|---|---|
| 1 | 0.5" | Dilute Acid/Alkali | Neutralization tanks: 1-5% H2SO4, HCl, or NaOH. Mild skin irritant. Eye splash is still serious -- pH extremes damage corneal tissue rapidly. Always wear goggles when making additions. | `#E8A020` |
| 2 | 8.16" | Cr(VI) Mist | Rinse tanks adjacent to chrome plating or chromic acid carry hexavalent chromium mist. Cr(VI) is a known carcinogen. Ventilation required at chrome rinse stations. | `#E05C5C` |
| 3 | 15.83" | Cross-Contamination | Dragout from one process into another via shared rinse water. Can introduce metals, acids, or alkali into incompatible baths. Use dedicated rinse tanks between incompatible processes. | `#2EC4B6` |

Per box:
- Hazard: Barlow SemiBold 16 pt, accent color
- Detail: Inter Regular 13 pt `#F0EDE8`

---

### ZONE 3 -- PPE Requirements

**Section label:** Centered. Y: 14.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> PPE BY STATION TYPE

---

**BLOCK D -- PPE Grid**

Y: 14.9" to 21.3". Three columns representing station types, each with PPE rows.

Column headers (Barlow SemiBold 18 pt):

| Column | X | W | Station Type | Accent |
|---|---|---|---|---|
| 1 | 0.5" | 7.33" | ROUTINE RINSE TANKS | `#2EC4B6` |
| 2 | 8.16" | 7.33" | NEUTRALIZATION TANKS | `#E8A020` |
| 3 | 15.83" | 7.33" | CHROME-ADJACENT RINSE | `#E05C5C` |

Each column: Rounded rect, H: 5.8", fill `#1E2435`, radius 6, top accent 4 pt.

**Column 1 -- Routine Rinse:**
```
Eyes: Safety glasses (minimum)
Gloves: Nitrile or rubber (standard)
Apron: Standard PVC or rubber
Respiratory: Not required
Notes: Low-hazard dilute solutions
```

**Column 2 -- Neutralization:**
```
Eyes: Chemical splash goggles
Gloves: Rubber, chemical-resistant
Apron: Standard PVC or rubber
Respiratory: Not required (unless adding acid)
Notes: Goggles when making chemical additions
```

**Column 3 -- Chrome-Adjacent:**
```
Eyes: Chemical splash goggles
Gloves: Rubber, chemical-resistant
Apron: Full splash apron
Respiratory: P100 if Cr(VI) mist present
Notes: Ventilation at tank lip is primary control
```

Per row: Inter Regular 13 pt `#F0EDE8`. Station type in accent color. PPE item labels: Barlow SemiBold 13 pt `#F0EDE8`.

---

### ZONE 4 -- Emergency Procedures

**Section label:** Centered. Y: 21.7". Barlow Condensed ExtraBold, 28 pt, `#E05C5C`.

> EMERGENCY PROCEDURES

---

**BLOCK E -- Emergency Callout Box**

Rounded rect, X: 0.5", Y: 22.4", W: 23.0", H: 5.8", fill `#1E2435`, radius 8.
Left accent: 0.06" `#E05C5C`.
Border: 1 pt `#E05C5C` at 40%.

Three columns inside:

| Column | Emergency | Action |
|---|---|---|
| 1 | HCN EXPOSURE | Evacuate area IMMEDIATELY. Move upwind. Call 911. Administer amyl nitrite inhalant if available (per facility protocol). Do NOT re-enter without supplied-air respirator. HCN is immediately dangerous to life at 50 ppm. |
| 2 | ACID / ALKALI SPLASH | Skin: flush with water 15+ min. Eyes: eyewash 15+ min; seek immediate medical attention. When making neutralization tank additions, ALWAYS add chemical to water, never water to acid. |
| 3 | Cr(VI) EXPOSURE | Skin: wash immediately; Cr(VI) causes contact dermatitis and ulceration. Inhalation: move to fresh air; Cr(VI) is a lung carcinogen. Report any chrome-colored stain on skin to supervisor. |

Per column:
- Emergency type: Barlow SemiBold, 16 pt, `#E05C5C`
- Action: Inter Regular, 13 pt, `#F0EDE8`

---

### ZONE 5 -- OSHA / Regulatory Strip

**Section label:** Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

> KEY REGULATORY REFERENCES

---

**BLOCK F -- Regulatory Cards**

Y: 29.3" to 32.3". Three cards in a row.

Each card: Rounded rect, W: 7.33", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E8A020`.

| Card | X | Reference | Detail |
|---|---|---|---|
| 1 | 0.5" | OSHA 29 CFR 1910.1000 | Air contaminants: HCN PEL = 10 ppm ceiling (skin notation). Cr(VI) PEL = 5 ug/m3 (action level 2.5 ug/m3). |
| 2 | 8.16" | OSHA 29 CFR 1910.151 | Eyewash and safety shower within 10 seconds travel time of all chemical-handling areas. |
| 3 | 15.83" | EPA 40 CFR 261 / 403 | Cyanide waste: segregate and treat before discharge. Pretreatment standards for metal finishing. pH 6.0-9.0 discharge. |

Per card:
- Reference: JetBrains Mono Regular, 14 pt, `#E8A020`
- Detail: Inter Regular, 13 pt, `#F0EDE8`

---

### ZONE 6 -- Footer

Standard. Title: `Safety & PPE -- Neutralization & Rinse Systems`. Version `v1.0 -- 2026`.

Disclaimer: `Source: OSHA standards; EPA regulations; general industry knowledge. This poster is an educational reference tool. Cyanide-acid segregation is a life safety requirement -- consult your facility safety officer and applicable regulations. HCN exposure limits and emergency response protocols must be site-specific per your facility EAP.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Safety PPE Neutralization Rinse -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The HCN warning hero dominates Zone 2 for a reason: this is the single most lethal scenario in routine plating shop operations. The triple-thickness border and oversized type make it impossible to skip. The routine hazard panel below it provides contrast -- most rinse operations are genuinely low-hazard, and the poster should communicate that balance honestly. The chrome-adjacent PPE column reflects a real-world scenario many shops face: the rinse tank next to the chrome tank carries Cr(VI) mist that the operator at that station inhales daily.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #393 -- Construction Workup v1.0*
*2026-04-26*
