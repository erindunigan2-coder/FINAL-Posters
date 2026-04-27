---
Project: Plating Posters Inc
Poster Number: 379
Title: "Safety & PPE -- Solvent Cleaning Operations"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Chemical Treatment Clusters — Watson Research Brief (CT-6)"
Technical Source: OSHA 29 CFR 1910.1000 (air contaminants), NESHAP 40 CFR Part 63 Subpart T, NFPA 30 (flammable liquids). Covers halogenated and non-halogenated solvent hazards, including carcinogenicity (TCE IARC Group 1), flammability, and CNS depression.
Process Scope: Solvent cleaning safety -- chemical hazards by solvent category, PPE requirements, emergency response, ventilation
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - SolventCleaning
  - Safety
  - PPE
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT06
---

# Poster #379 -- Construction Workup
## Safety & PPE -- Solvent Cleaning Operations

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Solvent cleaning safety is a two-headed beast. Halogenated solvents will not catch fire, but they will quietly destroy your liver and kidneys -- TCE is a known carcinogen. Non-halogenated solvents are less toxic but will absolutely catch fire -- acetone has a flash point of 0 deg F. This poster splits the hazard landscape cleanly into halogenated and non-halogenated domains, then maps PPE, emergency response, and ventilation requirements for each.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Dual hazard domain layout (Block B -- HERO):** Two side-by-side panels -- left for halogenated solvent hazards, right for non-halogenated solvent hazards. Each panel is a callout box with hazard rows inside.

2. **PPE requirements grid (Block D):** Five PPE items in a row with solvent-specific notes.

3. **Emergency procedures callout (Block E):** Coral-tinted callout with four emergency scenarios.

4. **OSHA PEL reference strip (Block F):** Key PELs and TLVs for common solvents.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 16.0" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- DUAL HAZARD PANELS / HERO (2.9"--16.0" / ~13.1" tall)
  Block B: Left -- Halogenated Solvent Hazards (4 rows)
  Block C: Right -- Non-Halogenated Solvent Hazards (4 rows)

ZONE 3 -- PPE REQUIREMENTS (16.0"--22.0" / ~6.0" tall)
  Block D: PPE grid (5 items)

ZONE 4 -- EMERGENCY PROCEDURES (22.0"--28.5" / ~6.5" tall)
  Block E: Emergency callout (inhalation, skin, ingestion, fire)

ZONE 5 -- OSHA / PEL REFERENCE (28.5"--32.5" / ~4.0" tall)
  Block F: PEL and TLV table for common solvents

ZONE 6 -- FOOTER BAND (32.5"--36.0")
  Block G: Standard footer
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `SOLVENT SAFETY` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Safety & PPE -- Halogenated and Non-Halogenated Solvent Cleaning` -- 32 pt `#E05C5C` (Coral). Y: 1.5".
**Tagline:** `Two categories, two threat profiles. One will poison you quietly. The other will burn the building down. Know the difference and suit up accordingly.` -- 20 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Dual Hazard Panels (HERO)

**Section label:** Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> TWO SOLVENT CATEGORIES -- TWO HAZARD PROFILES

---

**BLOCK B -- Halogenated Solvent Hazards (Left Panel)**

Rounded rect, X: 0.5", Y: 3.8", W: 11.0", H: 11.7", fill `#1E2435`, radius 8.
Left accent: 0.06" `#E05C5C`.
Title: `HALOGENATED (CHLORINATED)` -- Barlow SemiBold, 22 pt, `#E05C5C`.
Subtitle: `TCE, PERC, Methylene Chloride, nPB, trans-DCE` -- JetBrains Mono 13 pt `#F0EDE8` at 70%.

Four hazard rows inside (each row H: 2.4", alternating `#1E2435` / `#252B3D`):

| Row | Hazard | Detail | Control |
|---|---|---|---|
| 1 | Liver / Kidney Toxicity | Chronic exposure damages liver and kidneys; TCE is a known carcinogen (IARC Group 1); PERC is a probable carcinogen | Enclosed vapor degreasing; continuous air monitoring; medical surveillance |
| 2 | CNS Depression | Acute overexposure causes dizziness, confusion, unconsciousness; "solvent drunk" | Ventilation; buddy system; never work alone in enclosed areas |
| 3 | Decomposition Products | Heat or UV breaks down chlorinated solvents into phosgene and HCl gas -- both lethal | Never smoke near solvents; no open flame; no welding nearby; maintain stabilizer |
| 4 | Reproductive Toxicity | nPB (1-bromopropane) linked to reproductive harm and peripheral neuropathy | ACGIH TLV 0.1 ppm (proposed); use alternatives where possible |

Per row:
- Hazard: Barlow SemiBold, 15 pt, `#E05C5C`
- Detail: Inter Regular, 12 pt, `#F0EDE8` at 80%
- Control: Inter Medium, 12 pt, `#27AE60`

---

**BLOCK C -- Non-Halogenated Solvent Hazards (Right Panel)**

Rounded rect, X: 12.0", Y: 3.8", W: 11.5", H: 11.7", fill `#1E2435`, radius 8.
Left accent: 0.06" `#E8A020`.
Title: `NON-HALOGENATED (FLAMMABLE)` -- Barlow SemiBold, 22 pt, `#E8A020`.
Subtitle: `Mineral Spirits, Naphtha, Toluene, Acetone, IPA` -- JetBrains Mono 13 pt `#F0EDE8` at 70%.

Four hazard rows inside:

| Row | Hazard | Detail | Control |
|---|---|---|---|
| 1 | Fire / Explosion | Flash points vary widely: acetone 0 deg F (-18 C), mineral spirits 105-145 deg F (40-63 C); vapor heavier than air accumulates in low areas | Explosion-proof electrical; no ignition sources; bonding and grounding; LEL monitoring |
| 2 | CNS Effects | Acute: headache, dizziness, nausea; chronic: toluene causes permanent neurological damage | Ventilation below PEL; organic vapor respirator if ventilation insufficient |
| 3 | Skin Defatting | Prolonged contact strips natural oils; causes dermatitis, cracking, and secondary infection risk | Solvent-resistant gloves (nitrile for most); minimize skin contact; barrier cream |
| 4 | Respiratory Irritation | Vapors irritate mucous membranes and respiratory tract; some solvents are sensitizers | Local exhaust ventilation; organic vapor cartridge; supplied air for confined spaces |

Per row: same styling as Block B.

---

### ZONE 3 -- PPE Requirements

**Section label:** Centered. Y: 16.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> REQUIRED PPE -- SOLVENT CLEANING OPERATIONS

---

**BLOCK D -- PPE Grid**

Y: 16.9" to 21.8". Five cards in a single row. Gap: 0.25".

Each card: Rounded rect, W: 4.4", H: 4.5", fill `#1E2435`, radius 6, top accent 3 pt `#E05C5C`.

| Position | Item | Halogenated Note | Non-Halogenated Note |
|---|---|---|---|
| 1 | Chemical Splash Goggles | Required for liquid contact | Required for liquid contact |
| 2 | Gloves | Butyl rubber (best for chlorinated) | Nitrile (good for most; check SDS) |
| 3 | Respiratory Protection | Organic vapor cartridge minimum; supplied air for enclosed spaces | Organic vapor cartridge; supplied air for confined space entry |
| 4 | Body Protection | Standard work clothing; chemical suit for spill response | Anti-static clothing; no synthetic fabrics (static ignition risk) |
| 5 | Eye / Face | Safety glasses for vapor-only; full goggles + face shield for splash | Same as halogenated |

Per card:
- Item: Barlow SemiBold, 15 pt, `#F0EDE8`
- Halogenated: Inter Regular, 12 pt, `#E05C5C`
- Non-Halogenated: Inter Regular, 12 pt, `#E8A020`
- Icon placeholder: 0.5" x 0.5" circle, fill `#3A4055`, centered top inside card

---

### ZONE 4 -- Emergency Procedures

**Section label:** Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#E05C5C`.

> EMERGENCY PROCEDURES

---

**BLOCK E -- Emergency Callout Box**

Rounded rect, X: 0.5", Y: 22.9", W: 23.0", H: 5.3", fill `#1E2435`, radius 8.
Left accent: 0.06" `#E05C5C`.
Border: 1 pt `#E05C5C` at 40%.

Four columns inside:

| Column | Emergency | Action |
|---|---|---|
| 1 | INHALATION | Move to fresh air immediately. Administer oxygen if available. Monitor for delayed pulmonary effects. Call 911 for unconscious or confused worker. |
| 2 | SKIN CONTACT | Remove contaminated clothing. Wash with SOAP and water -- not more solvent. Do not use solvent to clean skin. |
| 3 | INGESTION | Do NOT induce vomiting -- aspiration of hydrocarbon solvents into lungs is life-threatening. Give water to dilute. Immediate medical attention. |
| 4 | FIRE (Non-Halogenated) | CO2 or dry chemical extinguisher. Do NOT use water on solvent fires (spreads the burning liquid). Evacuate if fire exceeds initial stage. |

Per column:
- Emergency type: Barlow SemiBold, 15 pt, `#E05C5C`
- Action: Inter Regular, 13 pt, `#F0EDE8`

---

### ZONE 5 -- OSHA / PEL Reference

**Section label:** Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

> EXPOSURE LIMITS -- KNOW YOUR NUMBERS

---

**BLOCK F -- PEL/TLV Table**

Y: 29.3" to 32.3". Column widths (23.0" total):
- Solvent (5.0") | OSHA PEL (5.0") | ACGIH TLV (5.0") | Flash Point (4.0") | Key Note (4.0")

Header row: fill `#3A4055`, H: 0.4".

| Solvent | OSHA PEL | ACGIH TLV | Flash Point | Key Note |
|---|---|---|---|---|
| TCE | 100 ppm TWA | 10 ppm TWA | Non-flammable | Known carcinogen (IARC Group 1) |
| PERC | 100 ppm TWA | 25 ppm TWA | Non-flammable | Probable carcinogen |
| Mineral Spirits | 500 ppm TWA | 100 ppm TWA | 105-145 deg F | Most common non-halogenated |
| Acetone | 1000 ppm TWA | 250 ppm TWA | 0 deg F (-18 C) | Extremely flammable |
| nPB | No OSHA PEL (2025) | 0.1 ppm (proposed) | Non-flammable | Neurotoxic; reproductive toxin |

Data: Inter Regular 12 pt. Solvent names: Barlow SemiBold 13 pt. Flash point for flammable solvents in `#E8A020`. "Non-flammable" in `#2EC4B6`.

---

### ZONE 6 -- Footer

Standard. Title: `Safety & PPE -- Solvent Cleaning Operations`. Version `v1.0 -- 2026`.

Disclaimer: `Source: OSHA 29 CFR 1910; ACGIH TLV documentation; NFPA 30; general industry knowledge. PELs and TLVs are subject to change -- always reference current OSHA and ACGIH guidance. This poster is an educational reference tool.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Safety PPE Solvent Cleaning -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Solvent safety is uniquely polarized -- halogenated solvents are toxic but non-flammable, while non-halogenated solvents are less toxic but flammable. The dual-panel hero layout makes this contrast visceral and immediate. The PEL/TLV table is essential because many operators do not realize that OSHA and ACGIH limits can differ by 10x (TCE: 100 vs. 10 ppm). The fire emergency column must be prominent -- never use water on a solvent fire is a life-saving message.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #379 -- Construction Workup v1.0*
*2026-04-26*
