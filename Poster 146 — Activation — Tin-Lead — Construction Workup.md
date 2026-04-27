---
Project: Plating Posters Inc
Poster Number: 146
Title: "Activation -- Tin-Lead"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Process Scope: Acid activation for tin-lead plating (Stage 3 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - TinLeadPlating
  - Activation
  - ConstructionWorkup
  - Series2
  - ClusterEP15
---

# Poster #146 -- Construction Workup
## Activation -- Tin-Lead

*Alaina -- Plating Posters Inc*
*v1.0 -- 2026-04-26*

Stage 3 of 8. Activation removes surface oxides and exposes clean, active metal for tin-lead deposition. The key difference from pure tin activation: tin-lead baths historically used fluoboric acid (HBF4) activation, and modern MSA-based lines use MSA itself for activation. Using the same acid family for activation and plating eliminates cross-contamination risk entirely. This poster covers substrate-specific activation for copper, nickel-plated surfaces, and the chemistry behind oxide removal.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Activation mechanism diagram (Block B -- HERO):** Cross-section of a substrate surface showing oxide layer dissolving in acid, exposing clean metal beneath. Built with layered rectangles and annotation arrows.
2. **Substrate-specific activation table (Block D):** Parameters by substrate (copper/brass, nickel-plated).
3. **Over-activation vs. under-activation callout (Block E):** Side-by-side showing what both look like.
4. **Acid selection callout (Block F):** MSA vs. fluoboric acid vs. sulfuric acid -- which to use and why acid family matching matters.

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
  Stage 3 highlighted (Amber)
ZONE 3 -- ACTIVATION MECHANISM HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- SUBSTRATE ACTIVATION TABLE (14.5"--20.5" / ~6.0")
ZONE 5 -- OVER VS. UNDER ACTIVATION (20.5"--26.5" / ~6.0")
ZONE 6 -- ACID SELECTION (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ACTIVATION` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Tin-Lead Plating -- Stage 3 of 8` -- 36 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `Strip the oxide. Expose the copper. Use the same acid family as your plating bath -- or pay for the cross-contamination.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 3 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean surface with oxide film  -->  After: Oxide-free metal ready for solder deposition`

---

### ZONE 3 -- Activation Mechanism Hero

**Section label:** `HOW ACID ACTIVATION WORKS` -- Y: 4.4".

**BLOCK B -- Surface Cross-Section Diagram**

Y: 5.0" to 14.0".

**Diagram concept:** Three-panel sequence showing:

Panel 1 (left third) -- `BEFORE`:
- Substrate layer (bottom): rounded rect, fill `#C8D0D8`, labeled `COPPER / BRASS`
- Oxide layer (top): rounded rect, fill `#E05C5C` at 40%, labeled `COPPER OXIDE (Cu2O)`
- Annotation: `Surface oxides block solder adhesion` Inter Regular 13 pt `#E05C5C`

Panel 2 (center third) -- `DURING`:
- Substrate layer: same
- Oxide layer: partially dissolved, gaps showing
- Acid arrows pointing down at oxide: `MSA` labels, stroke 2 pt `#E8A020`
- Chemical equation: `Cu2O + 2CH3SO3H -> 2Cu(CH3SO3) + H2O` JetBrains Mono 12 pt `#E8A020`
- Annotation: `MSA dissolves oxide layer` Inter Regular 13 pt `#E8A020`

Panel 3 (right third) -- `AFTER`:
- Substrate layer: exposed, bright
- No oxide layer
- Fill `#27AE60` at 20% glow on surface
- Annotation: `Clean, active copper surface` Inter Regular 13 pt `#27AE60`
- `Ready for Sn-Pb deposition` Inter Medium 13 pt `#27AE60`

Each panel: Rounded rect frame, W: 7.0", H: 8.0", fill `#1E2435`, radius 6.
Panel labels: Barlow Condensed ExtraBold 22 pt, centered.
Arrow connectors between panels: 3 pt `#3A4055`, right-pointing.

**Key parameters below diagram (Y: 13.0"):**
- `Typical: 5--10% MSA or HBF4 | Ambient | 15--30 sec` JetBrains Mono 16 pt `#E8A020`

---

### ZONE 4 -- Substrate Activation Table

**Section label:** `ACTIVATION BY SUBSTRATE` -- Y: 14.7".

**BLOCK D -- Substrate Table**

Y: 15.3" to 20.0".

| Substrate | Acid | Concentration | Temp | Time | Notes |
|---|---|---|---|---|---|
| Copper / Brass | MSA | 5--10% v/v | Ambient | 15--30 sec | Preferred for MSA plating bath |
| Copper / Brass | HBF4 | 5--10% v/v | Ambient | 15--30 sec | Legacy fluoborate bath lines |
| Nickel-plated | MSA or H2SO4 | 5% v/v | Ambient | 10--15 sec | Light touch -- protect Ni layer |
| Steel (with Cu strike) | H2SO4 | 5--15% v/v | Ambient | 15--60 sec | Rare -- steel gets Cu strike first |

Header: `#3A4055`. Alternating rows: `#1E2435` / `#252B3D`.

**Note below table:**
- `Match your activation acid to your plating bath acid. MSA bath = MSA activation. Fluoborate bath = fluoboric activation. This eliminates cross-contamination risk and simplifies waste treatment.` Inter Medium 13 pt `#E8A020`

---

### ZONE 5 -- Over vs. Under Activation

**Section label:** `GET IT RIGHT -- OVER VS. UNDER` -- Y: 20.7".

**BLOCK E -- Two-Panel Comparison**

Y: 21.3" to 26.0".

**Left -- Under-Activation:**
- Rounded rect, X: 0.5", W: 11.0", H: 4.5", fill `#1E2435`, left accent `#E05C5C`
- Title: `UNDER-ACTIVATED` Barlow SemiBold 18 pt `#E05C5C`

Symptoms:
- `Oxide film remains on copper surface`
- `Solder plates over oxide -- poor adhesion`
- `Blistering during reflow (solder melts, oxide does not bond)`
- `Solderability test failure -- cold solder joints`
- `Peel test failure on connectors`

Visual cue: `Looks OK wet -- fails at reflow` Inter Medium 13 pt `#E05C5C`

**Right -- Over-Activation:**
- Rounded rect, X: 12.0", W: 11.5", H: 4.5", fill `#1E2435`, left accent `#E8A020`
- Title: `OVER-ACTIVATED` Barlow SemiBold 18 pt `#E8A020`

Symptoms:
- `Copper surface etched -- roughened, pink or matte`
- `Grainy, rough solder deposit`
- `Dissolved copper drag-in contaminates tin-lead bath`
- `Copper immersion deposit possible (dark spots)`
- `Dimensional loss on precision connector pins`

Visual cue: `Visible etch on copper = too long or too strong` Inter Medium 13 pt `#E8A020`

**Center divider verdict:**
- `The window is narrow: 15--30 seconds in 5--10% acid. Set a timer. Every time.` Inter Medium 14 pt `#27AE60`

---

### ZONE 6 -- Acid Selection

**Section label:** `CHOOSE YOUR ACTIVATION ACID` -- Y: 26.7".

**BLOCK F -- Three Acid Options**

Y: 27.3" to 32.0". Three side-by-side callout boxes.

**Left -- MSA (Methanesulfonic Acid):**
- Rounded rect, X: 0.5", W: 7.33", H: 4.5", fill `#1E2435`, left accent `#27AE60`
- Title: `MSA` Barlow SemiBold 18 pt `#27AE60`
- `The modern choice`
- `Matches MSA plating bath`
- `Biodegradable -- simple waste treatment`
- `No fluoride issues`
- `Zero cross-contamination risk with MSA bath`
- Verdict: `USE THIS for MSA solder lines` Inter Medium 13 pt `#27AE60`

**Center -- Fluoboric Acid (HBF4):**
- Rounded rect, X: 8.16", W: 7.33", H: 4.5", fill `#1E2435`, left accent `#E8A020`
- Title: `FLUOBORIC ACID` Barlow SemiBold 18 pt `#E8A020`
- `Legacy choice -- matches fluoborate bath`
- `Effective oxide removal`
- `Fluoride in wastewater -- treatment required`
- `Being phased out with fluoborate baths`
- Verdict: `Legacy lines only` Inter Medium 13 pt `#E8A020`

**Right -- Sulfuric Acid (H2SO4):**
- Rounded rect, X: 15.83", W: 7.67", H: 4.5", fill `#1E2435`, left accent `#2EC4B6`
- Title: `SULFURIC ACID` Barlow SemiBold 18 pt `#2EC4B6`
- `Universal acid -- works on all substrates`
- `Risk: sulfate drag-in may affect MSA bath`
- `Acceptable for nickel-plated parts (light activation)`
- `Lowest cost option`
- Verdict: `OK for Ni-plated; avoid for Cu into MSA bath` Inter Medium 13 pt `#2EC4B6`

---

### ZONE 7 -- Footer

Standard. Title: `Activation -- Tin-Lead`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Activation Tin-Lead -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The three-panel before/during/after hero works as well here as in the tin cluster. The acid selection zone (Zone 6) is the unique value-add for tin-lead: acid family matching is not emphasized in most plating references but is critical for bath longevity. MSA activation into an MSA bath is the cleanest path. The chemical equation in Panel 2 shows MSA dissolving copper oxide specifically -- the dominant substrate reaction in tin-lead plating. Over-activation is especially dangerous here because dissolved copper ions dragged into the tin-lead bath cause immersion deposits and dark spots.

---

*Alaina -- Plating Posters Inc*
*Poster #146 -- Construction Workup v1.0*
*2026-04-26*
