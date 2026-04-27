---
Project: Plating Posters Inc
Poster Number: 351
Title: "Safety & PPE -- Electrocleaning"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Chemical Treatment Clusters -- Watson Research Brief (CT-2.2)"
Technical Source: Industry-standard safety and PPE requirements for electrolytic cleaning operations. Covers caustic chemical hazards, electrical hazards, hydrogen gas explosion risk, OSHA PELs, and emergency procedures.
Process Scope: Safety and PPE for electrocleaning operations
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Electrocleaning
  - Safety
  - PPE
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT02
---

# Poster #351 -- Construction Workup
## Safety & PPE -- Electrocleaning

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Poster 2 of 7 in the CT-02 cluster. This is the safety poster for electrocleaning -- and it has teeth. Electrocleaning adds two hazards that soak cleaning does not have: live electrical connections (rectifier bus bars) and hydrogen gas generation during cathodic operation. The hero visual is a PPE diagram with electrical safety callouts integrated. The hydrogen gas hazard panel is the unique feature of this poster versus the alkaline cleaning safety poster (344). Emergency procedures cover chemical, electrical, AND gas hazards.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **PPE diagram with electrical callouts (Block B -- HERO):** Silhouette figure with standard chemical PPE plus insulated gloves and face shield for bus bar work.
2. **Triple hazard table (Block D):** Chemical, electrical, and gas hazards in one table.
3. **Emergency procedure cards (Block E):** Four cards covering chemical burn, electrical shock, hydrogen explosion prevention, and eye contact.
4. **Hydrogen gas warning panel (Block F):** Dedicated panel for hydrogen accumulation and ventilation.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 21.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Poster 2 of 7 highlighted (Coral -- safety context)
ZONE 3 -- PPE EQUIPMENT DIAGRAM / HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- TRIPLE HAZARD TABLE (14.5"--21.0" / ~6.5")
ZONE 5 -- EMERGENCY PROCEDURES (21.0"--28.5" / ~7.5")
ZONE 6 -- HYDROGEN GAS + VENTILATION (28.5"--32.5" / ~4.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `SAFETY & PPE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Electrocleaning -- Chemistry, Electricity, and Hydrogen Walk Into a Tank` -- 32 pt `#E05C5C` (Coral). Y: 1.4".
**Tagline:** `Three hazard categories in one process. Know the risks, wear the gear, go home safe.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Y: 2.9" to 4.2". Seven small boxes representing the 7-poster sequence. Box 2 (Safety & PPE) highlighted: fill `#E05C5C`, text `#1A1F2E`. Others dimmed `#3A4055`.

Below strip: `Electrocleaning Cluster -- Poster 2 of 7` Inter Medium 14 pt `#F0EDE8` at 60%.

---

### ZONE 3 -- PPE Equipment Diagram (HERO)

**Section label:** `REQUIRED PERSONAL PROTECTIVE EQUIPMENT` -- Y: 4.4". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK B -- PPE Diagram**

Y: 5.0" to 14.0". Central silhouette figure with callout lines to PPE items.

**Center figure:** Simplified body outline using rectangles. X: 9.5", W: 5.0", H: 8.0". Fill `#252B3D`, border 1 pt `#3A4055`.

**PPE Callouts (arranged around figure with leader lines):**

| PPE Item | Position | Accent | Details |
|---|---|---|---|
| Chemical Splash Goggles + Face Shield | Upper right | `#E05C5C` | Face shield required near energized bus bars. Goggles sealed against splash. Both required simultaneously during bus bar work. |
| Insulated Gloves | Upper left | `#E8A020` | Electrically insulated gloves rated for low-voltage DC when handling bus bars or adjusting rack contacts. Chemical-resistant rubber or neoprene for routine tank work. |
| Chemical-Resistant Apron | Right center | `#E8A020` | Full-length PVC or rubber apron. Same as soak cleaning -- caustic solution at operating concentration. |
| Non-Conductive Boots | Lower right | `#2EC4B6` | Chemical-resistant AND non-conductive soles. Electrocleaning requires footwear rated for both hazards. |
| Long Sleeves | Lower left | `#2EC4B6` | No exposed skin near hot caustic solution or energized bus bars. |
| Hearing Protection | Lower center | `#3A4055` | Not required for standard electrocleaning. Flag only if ultrasonic agitation or high-volume gas evolution is present. |

Each callout:
- Leader line: 2 pt stroke in accent color
- Callout box: Rounded rect, W: 4.5", H: 1.3", fill `#1E2435`, left accent 0.06"
- Item name: Barlow SemiBold 16 pt, accent color
- Detail: Inter Regular 12 pt `#F0EDE8`

---

### ZONE 4 -- Triple Hazard Table

**Section label:** `THREE HAZARD CATEGORIES -- KNOW ALL OF THEM` -- Y: 14.7". Barlow Condensed ExtraBold 28 pt.

**BLOCK D -- Hazard Table**

Y: 15.4" to 20.8". Column widths (23.0" total):
- Hazard Category (4.5") | Source (5.5") | Risk (6.0") | Key Precaution (7.0")

Header row: Rectangle fill `#E05C5C` at 30%, H: 0.5". Barlow SemiBold 14 pt `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 1.2".

| Category | Source | Risk | Key Precaution |
|---|---|---|---|
| Chemical (Caustic) | NaOH solution at 3-8 oz/gal; 140-180 F operating temp | Severe skin and eye burns; alkaline mist inhalation | Full PPE; eyewash/shower within 10 seconds (OSHA 29 CFR 1910.151) |
| Electrical | Rectifier output 6-12 V DC; hundreds of amperes at bus bars | Shock, arc flash at loose connections, burns | De-energize before adjusting racks; insulated gloves; LOTO per 29 CFR 1910.147 |
| Hydrogen Gas | Cathodic cleaning generates H2 at workpiece; LEL 4%, UEL 75% | Explosion if H2 accumulates in enclosed space; flammable gas | Continuous ventilation; no sealed covers; No Smoking; explosion-proof electrical per NEC Art. 500 |

Data: Inter Regular 13 pt `#F0EDE8`. Category names: Barlow SemiBold 14 pt, color-coded:
- Chemical: `#E8A020`
- Electrical: `#E05C5C`
- Hydrogen: `#2EC4B6`

---

### ZONE 5 -- Emergency Procedures

**Section label:** `EMERGENCY RESPONSE -- THREE SCENARIOS` -- Y: 21.2". Barlow Condensed ExtraBold 28 pt.

**BLOCK E -- Four Emergency Cards**

Y: 21.9" to 28.3". 2x2 grid.

| Card | Position | Title | Steps |
|---|---|---|---|
| Caustic Burn (Skin) | R1C1 (X: 0.5", Y: 21.9") | CAUSTIC SKIN CONTACT | 1. Flush immediately with large volumes of water. 2. Continue flushing minimum 15 minutes. 3. Do NOT neutralize with acid. 4. Remove contaminated clothing while flushing. 5. Seek medical attention. |
| Eye Contact | R1C2 (X: 12.0", Y: 21.9") | EYE CONTACT | 1. Flush with eyewash station minimum 15 minutes. 2. Hold eyelids open during flush. 3. Alkaline burns cause LIQUEFACTIVE NECROSIS -- damage worsens over time. 4. Seek IMMEDIATE medical attention. |
| Electrical Incident | R2C1 (X: 0.5", Y: 25.3") | ELECTRICAL SHOCK / ARC FLASH | 1. De-energize rectifier IMMEDIATELY (emergency stop). 2. Do NOT touch victim if still in contact with live circuit. 3. Call emergency services. 4. Administer first aid/CPR if trained. 5. Report per OSHA 29 CFR 1904. |
| Hydrogen Accumulation | R2C2 (X: 12.0", Y: 25.3") | HYDROGEN GAS ALARM | 1. Evacuate immediate area. 2. Eliminate ignition sources (no switches, no sparks). 3. Increase ventilation (open doors, activate fans). 4. Do NOT de-energize rectifier if switch could spark -- use remote disconnect. 5. Monitor with combustible gas detector before re-entry. |

Each card: Rounded rect W: 11.0", H: 3.0", fill `#1E2435`, radius 6.
- Top accent: 4 pt `#E05C5C`
- Title: Barlow SemiBold 18 pt `#E05C5C`
- Steps: Inter Regular 12 pt `#F0EDE8`, numbered, line height 145%

---

### ZONE 6 -- Hydrogen Gas + Ventilation

**Two-column layout (Y: 28.7" to 32.3"):**

**Left -- Hydrogen Hazard (X: 0.5", W: 11.0"):**
- Rounded rect H: 3.3", fill `#E05C5C` at 15%, border 1 pt `#E05C5C`
- Title: `HYDROGEN GAS -- THE INVISIBLE HAZARD` Barlow SemiBold 20 pt `#E05C5C`
- Body: Inter Regular 14 pt `#F0EDE8`:
```
Cathodic cleaning generates H2 at the workpiece
H2 is colorless, odorless, lighter than air
LEL: 4% in air -- UEL: 75% in air
Accumulates under covers, hoods, and ceilings
One spark = explosion
```
- Highlight: `NEVER seal or cover an electrocleaner tank during operation` Inter Medium 13 pt `#E8A020`

**Right -- Ventilation (X: 12.0", W: 11.5"):**
- Rounded rect H: 3.3", fill `#2EC4B6` at 15%, border 1 pt `#2EC4B6`
- Title: `VENTILATION REQUIREMENTS` Barlow SemiBold 20 pt `#2EC4B6`
- Body:
```
Local exhaust at tank lip: 100-150 FPM minimum
Continuous operation during electrocleaning
Explosion-proof electrical in tank area (NEC Art. 500)
Tank covers must allow gas venting
Post "No Smoking / No Open Flame" signs
```

---

### ZONE 7 -- Footer

Standard. Title: `Safety & PPE -- Electrocleaning`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry safety practices; OSHA 29 CFR 1910 (electrical, respiratory, eyewash); NEC Article 500 (hazardous locations); NFPA 497. Consult your facility safety officer for site-specific requirements.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Safety PPE Electrocleaning -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This safety poster is more complex than CT-01's version (344) because electrocleaning introduces two additional hazard categories that soak cleaning does not have. The triple hazard table is the unique feature -- it forces the viewer to recognize that this is not "just another caustic tank." The hydrogen gas panel must be visually aggressive -- this is the hazard that kills people in plating shops. The electrical emergency card is new territory for this series and must be crystal clear: do NOT touch a person in contact with live circuit.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #351 -- Construction Workup v1.0*
*2026-04-26*
