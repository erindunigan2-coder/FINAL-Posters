---
Project: Plating Posters Inc
Poster Number: 262
Title: "Post Treatment -- Electroless Gold"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters — Watson Research Brief (Process 6: Electroless Gold)"
Process Scope: Post treatment for electroless gold (Stage 7 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ElectrolessGold
  - PostTreatment
  - ConstructionWorkup
  - Series2
  - ENIG
  - ENEPIG
---

# Poster #262 -- Construction Workup
## Post Treatment -- Electroless Gold

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 7 of 8. Post treatment for electroless gold is the simplest stage in the cluster for ENIG users and the most nuanced for autocatalytic gold wire bonding applications. For ENIG/ENEPIG, there is NO heat treatment -- the gold surface is ready for soldering as-plated. Oven dry at 60-80 C, then store in nitrogen or vacuum-sealed packaging. For autocatalytic gold used in wire bonding, thermal annealing at 150-200 C may be required to optimize grain structure for thermosonic wire bonding.

Hero visual: two-path post-treatment decision -- ENIG (dry and store) vs. autocatalytic (optional anneal for wire bonding).

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Two-path decision hero (Block B):** ENIG (no heat treatment -- dry and store) vs. autocatalytic (optional anneal).
2. **Storage and handling requirements (Block D):** Nitrogen storage, vacuum sealing, contamination prevention.
3. **Wire bonding optimization callout (Block E):** Thermal annealing parameters for autocatalytic gold.
4. **Quality verification strip (Block F):** Final inspection checks for gold-plated surfaces.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 7 highlighted (Amber)
ZONE 3 -- TWO-PATH POST-TREATMENT HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- STORAGE AND HANDLING (14.5"--20.5" / ~6.0")
ZONE 5 -- WIRE BONDING OPTIMIZATION (20.5"--26.5" / ~6.0")
ZONE 6 -- QUALITY VERIFICATION (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `POST TREATMENT` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Electroless Gold -- Stage 7 of 8` -- 36 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `ENIG gold is ready to solder as-plated -- no heat treatment. Autocatalytic gold for wire bonding may need a gentle anneal.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 7 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Rinsed gold surface  -->  After: Dried, packaged surface ready for assembly or storage`

---

### ZONE 3 -- Two-Path Post-Treatment Hero

**Section label:** `POST-TREATMENT DEPENDS ON YOUR GOLD PROCESS` -- Y: 4.4".

**BLOCK B -- Two-Path Decision Diagram**

Y: 5.0" to 14.0".

**Root node (top center):**
- Rounded rect, X: 5.0", Y: 5.0", W: 14.0", H: 1.5", fill `#E8A020` at 20%, border 2 pt `#E8A020`
- Text: `WHICH GOLD PROCESS DID YOU RUN?` Barlow Condensed ExtraBold 22 pt `#E8A020`

**Left -- ENIG / ENEPIG (X: 0.5", Y: 7.5", W: 11.0", H: 6.0"):**
- Rounded rect, fill `#1E2435`, top accent `#E8A020` 4 pt
- Title: `ENIG / ENEPIG` Barlow SemiBold 20 pt `#E8A020`
- Large text: `NO HEAT TREATMENT` Barlow Condensed ExtraBold 28 pt `#27AE60`
- Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):
  - `The gold surface is solderable and bondable as-plated`
  - `No thermal processing is required or recommended`
  - `Heat treatment would risk oxidizing the underlying EN layer at the Au/Ni interface`
- Steps:
  - `1. Oven dry: 60-80 C forced air or air knife` JetBrains Mono 13 pt `#F0EDE8`
  - `2. Visual inspection under magnification` JetBrains Mono 13 pt `#F0EDE8`
  - `3. Package in N2 atmosphere or vacuum-sealed bags` JetBrains Mono 13 pt `#F0EDE8`
  - `4. Store in clean, dry, temperature-controlled environment` JetBrains Mono 13 pt `#F0EDE8`
- Bottom note: `Do NOT heat treat between EN and gold in ENIG -- this is a critical process rule` Inter Medium 13 pt `#E05C5C`

**Right -- Autocatalytic Gold (X: 12.5", Y: 7.5", W: 11.0", H: 6.0"):**
- Rounded rect, fill `#1E2435`, top accent `#27AE60` 4 pt
- Title: `AUTOCATALYTIC GOLD` Barlow SemiBold 20 pt `#27AE60`
- Content:
  - `Standard applications: dry and store (same as ENIG)` Inter Regular 14 pt `#F0EDE8`
  - `Wire bonding applications: optional thermal anneal` Inter Medium 14 pt `#E8A020`

**Anneal parameters table:**

| Parameter | Value |
|---|---|
| Temperature | 150-200 C (300-390 F) |
| Time | 30-60 minutes |
| Atmosphere | Air or N2 (inert preferred) |
| Purpose | Optimize grain structure for thermosonic wire bonding |
| Gold thickness for wire bond | 0.5-1.5 um minimum |
| When required | Per wire bonding specification; not all applications need it |

Data: JetBrains Mono 12 pt `#F0EDE8`.

- Bottom note: `Anneal is optional and application-specific. Most autocatalytic gold does NOT require heat treatment.` Inter Medium 13 pt `#27AE60`

---

### ZONE 4 -- Storage and Handling

**Section label:** `STORAGE AND HANDLING -- PROTECTING THE GOLD SURFACE` -- Y: 14.7".

**BLOCK D -- Four Handling Boxes (Y: 15.3" to 20.3")**

2x2 grid:

**Box 1 -- Drying (X: 0.5", Y: 15.3", W: 11.0", H: 2.3"):**
- Rounded rect, fill `#1E2435`, left accent `#2EC4B6` 0.06"
- Title: `DRYING` Barlow SemiBold 16 pt `#2EC4B6`
- `Forced air (air knife) + oven at 60-80 C` JetBrains Mono 13 pt `#F0EDE8`
- `Remove all moisture before packaging` Inter Regular 13 pt `#F0EDE8`
- `Do not exceed 100 C -- no benefit, risk of oxidation at interfaces` Inter Medium 12 pt `#E05C5C`

**Box 2 -- Nitrogen Storage (X: 12.0", Y: 15.3", W: 11.5", H: 2.3"):**
- Rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `NITROGEN / VACUUM STORAGE` Barlow SemiBold 16 pt `#E8A020`
- `Store in nitrogen atmosphere or vacuum-sealed bags` JetBrains Mono 13 pt `#F0EDE8`
- `Prevents surface contamination from sulfides, chlorides, organics` Inter Regular 13 pt `#F0EDE8`
- `Critical for ENIG PCBs awaiting assembly -- shelf life is finite` Inter Medium 12 pt `#E8A020`

**Box 3 -- Handling (X: 0.5", Y: 17.8", W: 11.0", H: 2.3"):**
- Rounded rect, fill `#1E2435`, left accent `#E05C5C` 0.06"
- Title: `HANDLING PRECAUTIONS` Barlow SemiBold 16 pt `#E05C5C`
- `NEVER touch gold surfaces with bare hands` Inter Medium 14 pt `#E05C5C`
- `Fingerprint oils cause solderability failures` Inter Regular 13 pt `#F0EDE8`
- `Wear clean lint-free nitrile gloves for all handling` Inter Regular 13 pt `#F0EDE8`
- `Use edge handling or vacuum pickup for PCBs` Inter Regular 13 pt `#F0EDE8`

**Box 4 -- Shelf Life (X: 12.0", Y: 17.8", W: 11.5", H: 2.3"):**
- Rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `SHELF LIFE CONSIDERATIONS` Barlow SemiBold 16 pt `#E8A020`
- `ENIG shelf life: 6-12 months if properly stored` JetBrains Mono 13 pt `#F0EDE8`
- `Solderability degrades with time even under N2` Inter Regular 13 pt `#F0EDE8`
- `Verify solderability before assembly if storage exceeds 6 months` Inter Medium 13 pt `#E8A020`
- `Wire bond gold: test within specification window before use` Inter Regular 13 pt `#F0EDE8`

---

### ZONE 5 -- Wire Bonding Optimization

**Section label:** `WIRE BONDING -- GOLD SURFACE REQUIREMENTS` -- Y: 20.7".

**BLOCK E -- Two Panels (Y: 21.3" to 26.3")**

**Left -- Wire Bond Gold Requirements (X: 0.5", W: 11.0", H: 4.8"):**
- Rounded rect, fill `#1E2435`, left accent `#27AE60` 0.06"
- Title: `AUTOCATALYTIC GOLD FOR WIRE BONDING` Barlow SemiBold 18 pt `#27AE60`
- Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):

| Requirement | Value |
|---|---|
| Minimum gold thickness | 0.5-1.5 um (application-specific) |
| Surface roughness | Ra <0.1 um (smooth for bond formation) |
| Gold purity | >99% (P or B from reducing agent may be present) |
| Contamination | Zero organics, zero sulfides, zero chlorides |
| Grain structure | Fine-grained preferred for thermosonic bonding |
| Anneal (if required) | 150-200 C, 30-60 min, N2 atmosphere |

**Right -- Why ENIG Cannot Wire Bond (X: 12.0", W: 11.5", H: 4.8"):**
- Rounded rect, fill `#1E2435`, left accent `#E05C5C` 0.06"
- Title: `WHY ENIG GOLD CANNOT WIRE BOND` Barlow SemiBold 18 pt `#E05C5C`
- Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):
  - `ENIG immersion gold is only 0.03-0.10 um thick`
  - `Wire bonding requires 0.5-1.5+ um of gold`
  - `During thermosonic bonding, the gold wire must alloy with the pad gold`
  - `At 0.03-0.10 um, the wire bonds directly to the Ni-P underlayer`
  - `Result: brittle Ni-Au intermetallic + P-enriched interface = weak bond`
  - `For wire bonding, you MUST use autocatalytic gold (or electrolytic gold)` Inter Medium 14 pt `#E8A020`

- Bottom highlight:
  - Rounded rect, W: 10.5", H: 0.6", fill `#E05C5C` at 15%, border 1 pt `#E05C5C`
  - `ENIG is for soldering. Autocatalytic gold is for wire bonding. Do not confuse the two.` Inter Medium 13 pt `#E05C5C`

---

### ZONE 6 -- Quality Verification

**Section label:** `FINAL QUALITY CHECKS -- GOLD SURFACE` -- Y: 26.7".

**BLOCK F -- Four Check Cards (Y: 27.3" to 32.3")**

Four cards in a single row. Gap: 0.33".

Each card: Rounded rect, W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#27AE60`.

| Card | X | Check | Method | Accept/Reject |
|---|---|---|---|---|
| 1 | 0.5" | GOLD THICKNESS | XRF measurement (non-destructive) | ENIG: 0.05-0.10 um; Auto: per spec |
| 2 | 6.33" | VISUAL INSPECTION | 10-40x magnification; uniform gold color | Reject: haze, dark spots, skip, discoloration |
| 3 | 12.16" | SOLDERABILITY | Solder float test or wetting balance | Accept: >95% wetting within 3 seconds |
| 4 | 18.0" | WIRE BOND (AUTO ONLY) | Pull test per MIL-STD-883 or IPC J-STD-002 | Accept: minimum pull force per spec |

Interior per card:
- Check name: Barlow SemiBold, 16 pt, `#27AE60`
- Method: Inter Regular, 13 pt, `#F0EDE8`
- Accept/Reject: Inter Medium, 13 pt, `#F0EDE8`

---

### ZONE 7 -- Footer

Standard footer. Title: `Post Treatment -- Electroless Gold`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Process parameters shown are typical industry values for electroless gold post-treatment, storage, and quality verification. Specific requirements vary by application specification, customer requirements, and governing standards. Consult your process supplier and applicable IPC/MIL standards. Source: General industry knowledge; IPC-4552B; IPC-4556.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Post Treatment Electroless Gold -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster closes the Electroless Gold cluster. The two-path decision in Zone 3 mirrors the structure from Poster #258 (activation) -- reinforcing the ENIG vs. autocatalytic dichotomy one final time. The "NO HEAT TREATMENT" callout for ENIG is large and bold because the single most common mistake operators make is heat-treating between EN and gold in an ENIG line, which oxidizes the EN surface and destroys the gold interface. The wire bonding section in Zone 5 clearly explains why ENIG gold is too thin for wire bonding -- this is a frequently misunderstood topic in the industry. The quality verification strip in Zone 6 replaces the usual troubleshooting strip with a more appropriate final-inspection focus, since post-treatment for gold is primarily about handling, storage, and verification rather than troubleshooting process defects.

---

*Alaina -- Poster #262 -- Construction Workup v1.0 -- 2026-04-26*
