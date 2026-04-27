---
Project: Plating Posters Inc
Poster Number: 61
Title: "Rinse -- Nickel (Watts) -- Post-Plate"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-04 technical reference (Watts nickel)"
  - "Watson Research Brief -- Electroplating Clusters EP-02 through EP-15"
Technical Source: Double counterflow rinse after Watts nickel plating. Removes acidic nickel drag-out and brightener residues before subsequent processing (chrome, gold, lacquer, or anti-tarnish).
Process Scope: Post-plate rinse for Watts nickel plating (Stage 6 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - NickelPlating
  - Watts
  - Rinse
  - PostPlate
  - ConstructionWorkup
  - Series2
  - ClusterEP04
---

# Poster #61 -- Construction Workup
## Rinse -- Nickel (Watts) -- Post-Plate

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 6 of 8. The post-plate rinse removes acidic nickel solution and brightener residues from the freshly plated surface. This rinse is critical because nickel drag-out contaminates whatever comes next -- chrome, gold, passivate, or lacquer. Brightener carry-over is the silent killer of chrome bath life.

Hero visual: double counterflow rinse tank with drag-out recovery concept and path to next process.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Double counterflow rinse hero (Block B):** Two tanks showing counterflow direction and drag-out recovery.
2. **Drag-out recovery callout (Block C):** Why recovering nickel drag-out saves money.
3. **What the next process needs (Block D):** Cleanliness requirements for chrome, gold, lacquer.
4. **Failure modes (Block E):** 4 common problems.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.0" / 21.0" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 6 highlighted (Teal)
ZONE 3 -- COUNTERFLOW RINSE HERO (4.2"--15.0" / ~10.8")
  Block B: Double counterflow tank diagram
  Block C: Drag-out recovery callout
ZONE 4 -- WHAT THE NEXT PROCESS NEEDS (15.0"--21.0" / ~6.0")
  Block D: Requirements by downstream process
ZONE 5 -- NICKEL PASSIVATION + TIMING (21.0"--27.0" / ~6.0")
  Block E: Nickel passivation risk
  Block F: Transfer timing rules
ZONE 6 -- FAILURE MODES + SAFETY (27.0"--32.5" / ~5.5")
  Block G: 4 failure modes
  Block H: Safety
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Nickel (Watts) -- Post-Plate -- Stage 6 of 8` -- 36 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `Nickel drag-out is acidic and loaded with brighteners. Both will poison your next tank if you do not rinse thoroughly.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 6 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Freshly plated nickel, wet with bath solution --> After: Clean nickel surface ready for chrome, gold, or topcoat`

---

### ZONE 3 -- Counterflow Rinse Hero

**Section label:** `THE POST-PLATE RINSE` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Double Counterflow Diagram**

Y: 5.0" to 12.0".

Two tanks side by side:

*Tank 1 -- Drag-Out / Recovery (X: 1.0", W: 10.0", H: 5.5"):*
- Rounded rect, fill `#252B3D`, border 2 pt `#E8A020`
- Label: `TANK 1: DRAG-OUT RECOVERY (OPTIONAL)` Barlow SemiBold 14 pt `#E8A020`
- Parameters (JetBrains Mono 13 pt):
```
Stagnant (no overflow)
Collects concentrated Ni drag-out
Return to plating bath periodically
Saves nickel chemistry costs
```
- Arrow from Tank 1 to Tank 2: `#3A4055`, 2 pt, labeled `Parts move forward`

*Tank 2 -- Final Rinse (X: 13.0", W: 10.0", H: 5.5"):*
- Rounded rect, fill `#252B3D`, border 2 pt `#2EC4B6`
- Label: `TANK 2: FLOWING RINSE` Barlow SemiBold 14 pt `#2EC4B6`
- Parameters (JetBrains Mono 13 pt):
```
Type: Overflow or counterflow
Temperature: Ambient
Conductivity: < 100 microS/cm
Agitation: Rack movement (3--4 dips)
```

Arrow from fresh water inlet to Tank 2: `#2EC4B6`.
Arrow from Tank 2 overflow to Tank 1 (if counterflow): `#3A4055`, labeled `Counterflow direction`.

**BLOCK C -- Drag-Out Recovery**

Y: 12.3" to 14.8". Full-width callout.
- Rounded rect, fill `#1E2435`, left accent `#E8A020`, radius 8

Title: `DRAG-OUT RECOVERY -- SAVE YOUR NICKEL` Barlow SemiBold 18 pt `#E8A020`

Two-column inside:

*Left -- The Math:*
- `Typical drag-out: 0.5--2.0 oz per ft2 of rack surface` JetBrains Mono 13 pt
- `At 60--90 g/L Ni, that is significant metal loss per shift`
- `A drag-out tank captures 70--90% of carried solution`
- `Return it to the plating bath weekly or when volume allows`

*Right -- The Economics:*
- `Nickel sulfate: $2--4/lb` JetBrains Mono 13 pt
- `Nickel chloride: $3--5/lb`
- `Brightener system: expensive`
- `Drag-out recovery pays for itself in weeks on high-volume lines`

---

### ZONE 4 -- What the Next Process Needs

**Section label:** `DOWNSTREAM REQUIREMENTS -- WHAT COMES AFTER NICKEL` -- Y: 15.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK D -- Requirements by Process**

Y: 15.8" to 20.8". Four callout boxes in a 2x2 grid.

| Process | X | Y | W | H | Accent |
|---|---|---|---|---|---|
| Decorative Chrome | 0.5" | 15.8" | 11.0" | 2.3" | `#2EC4B6` |
| Gold Plate | 12.5" | 15.8" | 11.0" | 2.3" | `#E8A020` |
| Lacquer / Anti-Tarnish | 0.5" | 18.4" | 11.0" | 2.3" | `#27AE60` |
| HE Bake (High-Strength Steel) | 12.5" | 18.4" | 11.0" | 2.3" | `#E05C5C` |

*Chrome:*
- Title: `DECORATIVE CHROME` Barlow SemiBold 16 pt `#2EC4B6`
- Body: `Nickel must be active (not passivated). Transfer quickly -- ideally <30 sec from final rinse to chrome immersion. Do not let parts air-dry. Brightener drag-in degrades chrome bath. Thorough rinsing is critical.`

*Gold:*
- Title: `GOLD PLATE` Barlow SemiBold 16 pt `#E8A020`
- Body: `Nickel contamination in gold bath causes dull deposits and co-deposition of nickel. Rinse very thoroughly. DI water for final rinse recommended. Some gold processes require a mild activation dip after nickel rinse.`

*Lacquer:*
- Title: `LACQUER / ANTI-TARNISH` Barlow SemiBold 16 pt `#27AE60`
- Body: `Surface must be completely free of salts and water spots. Final DI rinse essential. Hot-air dry before lacquer application. Any residue under lacquer causes blistering and cosmetic defects.`

*HE Bake:*
- Title: `HE BAKE (HIGH-STRENGTH STEEL)` Barlow SemiBold 16 pt `#E05C5C`
- Body: `Parts requiring HE bake (>31 HRC) must reach the oven within 4 hours of plating (ASTM B850). Rinse, dry, and transfer to bake oven immediately. Do not queue parts at room temperature. 375 +/- 25 F for 3--24 hours.`

---

### ZONE 5 -- Nickel Passivation + Timing

**Two-column layout (Y: 21.2" to 26.8"):**

**Left -- Nickel Passivation Risk (X: 0.5", W: 11.0"):**

- Rounded rect, fill `#E05C5C` at 10%, border 1 pt `#E05C5C`, radius 8
- Title: `NICKEL PASSIVATES IN AIR` Barlow Condensed ExtraBold 20 pt `#E05C5C`
- Body (Inter Medium 14 pt `#F0EDE8`, line height 155%):

> A freshly plated nickel surface begins to passivate (form a thin oxide) within minutes of air exposure. This passive film prevents adhesion of chrome, gold, or other subsequent coatings.
>
> For decorative chrome: move parts from nickel rinse to chrome tank in under 30 seconds. Do not let parts sit in air.
>
> If delay is unavoidable: a mild acid re-activation dip (1--5% H2SO4, 10--30 sec) can restore the surface. But prevention is better than cure.

**Right -- Transfer Timing Rules (X: 12.5", W: 11.0"):**

- Rounded rect, fill `#1E2435`, left accent `#E8A020`
- Title: `TRANSFER TIMING` Barlow SemiBold 18 pt `#E8A020`

| Destination | Max Delay | Notes |
|---|---|---|
| Chrome | < 30 sec | Nickel passivates fast |
| Gold | < 2 min | Less critical but still time-sensitive |
| Lacquer | DI rinse + dry first | Surface must be completely dry |
| HE bake oven | < 4 hours total | Per ASTM B850 |
| Storage (bright Ni final) | Apply anti-tarnish first | Nickel tarnishes in humid air |

---

### ZONE 6 -- Failure Modes + Safety

**Two-column layout (Y: 27.2" to 32.3"):**

**Left -- 4 Failure Modes (X: 0.5", W: 14.0"):**

| Problem | Cause | Downstream Effect |
|---|---|---|
| Brightener carry-over to chrome | Insufficient rinse volume | Chrome bath degradation, dull chrome |
| Nickel salt staining | Parts air-dried with nickel solution | White/green salt deposits under topcoat |
| Passivation before chrome | Delay between rinse and chrome | Chrome peeling, poor adhesion |
| HE bake missed or delayed | Parts queued too long after plating | Hydrogen embrittlement failure in service |

Cards: fill `#1E2435`, left accent `#E05C5C`.

**Right -- Safety (X: 15.5", W: 8.0"):**

> - Nickel drag-out rinse is acidic (pH 3--5). Avoid skin contact.
> - Nickel salts cause dermatitis -- gloves required when handling parts.
> - IARC Group 1 carcinogen (inhalable nickel). Mist extraction at rinse tanks near heated baths.
> - Waste rinse water contains dissolved nickel -- route to treatment, not drain.

---

### ZONE 7 -- Footer

Standard footer. Title: `Rinse -- Nickel (Watts) -- Post-Plate`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Nickel Watts Post-Plate -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This post-plate rinse poster is more complex than the pre-activation and pre-plate rinses because the downstream process matters enormously. The "What Comes After Nickel" grid is the unique value-add -- it transforms a generic rinse poster into a decision support tool. The nickel passivation warning is critical for chrome shops. The drag-out recovery section adds economic context that resonates with shop managers.

---

*Alaina -- Plating Posters Inc Creative Lead*
*Poster #61 -- Construction Workup v1.0*
*2026-04-26*
