---
created: 2026-04-03T00:00:00
updated: 2026-04-11
version: v2
poster: "#2 — The Electroplating Process — Step by Step"
tags:
  - Electroplating
  - ProcessOverview
  - PosterResearch
  - ResearchBrief
---

# The Electroplating Process — Alaina Research Brief

**Poster**: #2 — The Electroplating Process -- Step by Step
**Prepared by**: Watson (`watson-chemistry-researcher`)
**Date**: 2026-04-03 (v1); 2026-04-11 (v2)
**Version**: v2 -- publishable quality; collaboration flags resolved; internal annotations removed; sticky facts section added; soluble vs. insoluble anode distinction clarified; product names removed per standing rule; all data cross-verified against 1993 Metal Finishing Guidebook and domain expertise
**Source documents**: 1993 Metal Finishing Guidebook and Directory (vault); Products Finishing (pfonline.com); Drew's Quick Reference Metal Finishing Notes (vault); domain expertise

---

## Why This Poster Matters

This is the "what is electroplating?" poster. It serves two audiences:
1. **New operators and trainees** -- understanding the fundamental mechanism helps them troubleshoot and operate intelligently instead of following rote instructions
2. **Visitors, customers, and executives** -- boardroom-quality visual that explains the core technology in a credible, impressive way

It is the most universal teaching poster in the series.

---

## The Core Concept -- In One Sentence

**Electroplating uses electrical current to drive metal ions from a solution onto a conductive surface, building a thin, adherent metallic coating atom by atom.**

---

## The Four Essential Components

Every electroplating system requires exactly four things:

### 1. The Electrolyte (Plating Solution / Bath)

An aqueous solution containing dissolved metal ions (the metal to be deposited), supporting salts (for conductivity), and additives (for deposit quality). The dissolved metal ions are the raw material for the deposit.

| Process | Metal Ion | Solution Chemistry |
|---|---|---|
| Acid copper | Cu2+ | Copper sulfate + sulfuric acid |
| Watts nickel | Ni2+ | Nickel sulfate + nickel chloride + boric acid |
| Acid zinc | Zn2+ | Zinc chloride + potassium chloride + boric acid |
| Silver | Ag+ | Silver cyanide + potassium cyanide |
| Hard chrome | Cr6+ (as CrO3) | Chromic acid + sulfuric acid catalyst |

### 2. The Cathode (The Part Being Plated)

The workpiece -- connected to the **negative terminal** of the power supply. Metal cations migrate to the cathode surface and gain electrons (are "reduced"), converting from dissolved ions to solid metal:

```
M2+ + 2e- --> M0 (solid metal deposit)
```

**Key concept**: The cathode is where metal **builds up**. "Cathode = Coating."

**Side reaction**: Hydrogen ions compete for electrons, producing hydrogen gas:
```
2H+ + 2e- --> H2 (gas)
```
This wastes current (reduces cathode efficiency) and can cause hydrogen embrittlement in susceptible steels.

### 3. The Anode

The counterelectrode -- connected to the **positive terminal** of the power supply. Two types exist:

**Soluble anodes** -- made of the same metal being plated. They dissolve during plating, replenishing the metal ions consumed at the cathode:
```
M0 (solid anode) --> M2+ + 2e- (dissolves into solution)
```

| Process | Anode Material |
|---|---|
| Acid copper | Phosphorized copper (Cu-P) |
| Watts nickel (bright) | Nickel R-Rounds |
| Watts nickel (semi-bright/sulfamate) | Nickel S-Rounds (sulfur-depolarized) |
| Cyanide copper | Oxygen-free copper (OFHC) |
| Silver | High-purity silver (>99.9%) |
| Tin | Pure tin |

**Insoluble anodes** -- do not dissolve. Current passes through them, but metal ions must be replenished by adding chemicals to the bath:

| Process | Anode Material | Why Insoluble |
|---|---|---|
| Hard chrome | Lead-tin alloy (7% Sn) or lead-antimony | Chromium metal anodes would not dissolve properly in CrO3 |
| Alkaline non-cyanide zinc | Steel plates | Zinc anodes dissolve too fast in alkaline solution; metal added as ZnO |
| Trivalent chrome | Carbon (graphite) | Insoluble by design |

**Key concept**: Soluble anodes keep the bath in balance by replacing what the cathode consumes. Insoluble anodes require the operator to add chemistry manually.

### 4. The Power Supply (Rectifier)

A device that converts AC line power to DC (direct current) at controlled voltage and amperage. Electrons flow from the negative terminal through the external circuit to the cathode, through the electrolyte as ionic current, to the anode, and back to the positive terminal.

**Key controls**:
- **Amperage** -- determines the current density (ASF) and deposition rate
- **Voltage** -- adjusts automatically based on bath resistance; typically 3--12 V for most processes; chrome may require 6--12 V or higher

---

## The Complete Circuit -- How Current Flows

```
RECTIFIER (DC Power Supply)
    |                    |
    | (-)                | (+)
    v                    v
  CATHODE              ANODE
  (Part)               (Metal or insoluble)
    |                    |
    <---- ELECTROLYTE ---->
         (Ion flow)

External circuit: Electrons flow from (-) terminal --> cathode --> through wire --> anode --> (+) terminal
Internal circuit: Cations (M2+) migrate through solution from anode toward cathode
                  Anions (SO42-, Cl-, CN-) migrate toward anode
```

**The flow direction convention**:
- **Electrons** (in the wires): Flow from negative terminal to cathode, and from anode to positive terminal
- **Cations** (M2+, H+ -- positive ions in solution): Migrate **toward the cathode** (attracted to the negative charge)
- **Anions** (SO42-, Cl-, CN- -- negative ions in solution): Migrate **toward the anode** (attracted to the positive charge)

**Poster simplification**: "Metal ions travel through the solution toward the part. When they arrive, they pick up electrons and become solid metal. That's plating."

---

## The Plating Sequence -- From Raw Part to Finished Product

The complete production flow, integrating surface preparation with the plating step:

```
 1. RECEIVE PARTS --> Inspect incoming condition
    |
 2. SOAK CLEAN --> Remove bulk oils and soils
    |
 3. RINSE
    |
 4. ELECTROLYTIC CLEAN --> Final cleaning + surface activation
    |
 5. RINSE
    |
 6. ACID ACTIVATE --> Remove oxides; expose bare metal
    |
 7. RINSE
    |
 8. PLATE --> Electrodeposition of metal coating
    |
 9. RINSE (drag-out recovery)
    |
10. POST-TREATMENT --> Chromate/passivate, sealant, or topcoat
    |
11. RINSE
    |
12. DRY --> Hot air, centrifugal, or oven
    |
13. INSPECT --> Thickness, adhesion, appearance, salt spray
    |
14. SHIP
```

---

## Soluble vs. Insoluble Anodes -- The Two Systems

### Soluble Anode System (e.g., acid copper, nickel, tin)

```
ANODE dissolves --> M2+ enters solution --> M2+ migrates to cathode --> M2+ + 2e- --> M0 (deposit)
```

- The bath is **self-replenishing** -- as fast as the cathode consumes metal, the anode releases it
- Metal concentration stays relatively stable
- Anode maintenance: replace consumed anodes; keep anode bags clean; maintain proper anode area

### Insoluble Anode System (e.g., hard chrome, alkaline zinc)

```
ANODE conducts current only --> Metal ions consumed at cathode --> Bath metal depletes --> Operator adds metal salt
```

- The bath **depletes** with use -- metal concentration drops as parts are plated
- Operator must analyze the bath and add metal salts (CrO3 for chrome, ZnO for alkaline zinc)
- Anode maintenance: inspect for passivation; replace when damaged

---

## Key Process Variables -- What the Operator Controls

| Variable | What It Affects | How It's Controlled |
|---|---|---|
| **Current density (ASF)** | Deposition rate, deposit quality, brightness | Rectifier amperage + part surface area |
| **Temperature** | Deposition rate, conductivity, brightener activity | Heaters, chillers, thermostats |
| **Time** | Deposit thickness | Timer or operator judgment |
| **Agitation** | Mass transport, uniformity, limiting CD | Air sparging, mechanical movement, solution flow |
| **Bath chemistry** | Deposit properties, efficiency, throwing power | Chemical analysis + additions |
| **pH** | Deposit stress, brightness, efficiency | Acid or alkali additions |
| **Filtration** | Deposit smoothness, freedom from particles | Filter pump, carbon treatment |

---

## Common Defects -- Quick Reference

| Defect | Likely Cause | Location on Part |
|---|---|---|
| **Burning** (dark, rough) | Current density too high | Edges, points, corners (HCD zones) |
| **Skip plating** (bare spots) | Current density too low; poor cleaning | Recesses, interior surfaces (LCD zones) |
| **Pitting** | Hydrogen gas adhesion; organic contamination | Random across surface |
| **Peeling** | Poor adhesion; surface preparation failure | Edges or entire surface |
| **Dullness** | Brightener depletion; low temperature; low CD | Uniform across part |
| **Roughness** | Particulates; metallic contamination; anode sludge | Random or follows current flow |
| **Streaking** | Inadequate rinsing; drag-in contamination | Vertical lines following drainage |

---

## Visual / Diagram Opportunities for Poster Design

### 1. The Electroplating Cell Diagram (HERO visual)

A clean, labeled cross-section of a plating tank showing:
- Rectifier at top with (+) and (-) terminals
- Anode on one side (labeled, with dissolution arrows if soluble)
- Cathode (workpiece) on the other side (with M2+ arrows arriving and M0 building up)
- Solution filling the tank (with cation and anion migration arrows)
- Bus bars connecting electrodes to rectifier

**Color coding**:
- Cathode / deposit buildup: Emerald `#27AE60`
- Anode / dissolution: Amber `#E8A020`
- Ion flow arrows: Teal `#2EC4B6`
- Electron flow arrows: Coral `#E05C5C`

### 2. The Production Flow Strip

A horizontal or vertical flow diagram showing the full 14-step sequence from receiving to shipping. Each step is a small icon or labeled box.

### 3. The "Anode Dissolves / Cathode Builds" Side-by-Side

Two magnified cross-sections:
- Left (Anode): Metal atoms leaving the solid surface, becoming M2+ ions in solution
- Right (Cathode): M2+ ions arriving at the surface, gaining electrons, becoming solid atoms
- Caption: "What the anode gives up, the cathode builds."

### 4. The Soluble vs. Insoluble Anode Comparison

Two simple tank diagrams:
- Left: Soluble anode -- anode shrinks over time, metal concentration stays stable
- Right: Insoluble anode -- anode stays the same size, metal concentration drops, operator adds chemistry

### 5. The Four Components Quadrant

A 2x2 grid: Electrolyte | Cathode | Anode | Rectifier -- each with a simple icon and one-line description.

### 6. The Cathode Reaction Close-Up

A magnified view of the cathode surface showing M2+ ions arriving, electrons from the wire, metal atoms joining the growing crystal lattice, and H2 bubbles rising (side reaction).

### 7. The Defect Quick Reference Strip

A horizontal strip at the bottom showing 4--6 defect icons with causes -- burning, skip plating, pitting, peeling. Cross-references Poster #1 (surface prep) and Poster #11 (current density).

---

## Key Data Points for Callouts

**The one-line definition**:
- "Electroplating uses electrical current to deposit a metal coating from solution onto a conductive surface."

**The core reaction**:
- `M2+ + 2e- --> M0`
- "Metal ions + electrons = solid metal"

**The four essentials**:
- `Electrolyte + Cathode + Anode + Rectifier`

**Anode dissolves / Cathode builds**:
- "What the anode gives up, the cathode builds."

**Ion migration direction**:
- Cations --> toward cathode (negative)
- Anions --> toward anode (positive)

**Typical voltage range**:
- Most processes: `3--12 V DC`

**Typical current density range (all processes)**:
- `3--300+ ASF` (zinc barrel on the low end, hard chrome on the high end)

**Process count**:
- Over `30 distinct electroplating processes` are in commercial use worldwide

---

## Poster-Worthy Sticky Facts

1. **"Cathode = Coating"** -- the part is always the cathode (negative). Metal ions in solution are attracted to the negative charge, pick up electrons, and become solid metal. That is the entire basis of electroplating in one sentence.

2. **"What the anode gives up, the cathode builds"** -- in a soluble anode system, the anode dissolves at roughly the same rate that the cathode deposits. The bath is a shuttle service for metal atoms. This is the most elegant concept in plating.

3. **"3 to 300 ASF"** -- the range of current densities across all common processes spans two orders of magnitude. Zinc barrel plating at 3--15 ASF is gentle; hard chrome at 150--300+ ASF is brute force. Same principle, vastly different energy.

4. **"4 things, every time"** -- every electroplating cell in the world requires exactly four components: electrolyte, cathode, anode, and rectifier. A penny in a glass of copper sulfate with a battery qualifies. A 10,000-gallon automatic line qualifies. The physics is identical.

5. **"14 steps from receiving to shipping"** -- electroplating is not just "dipping metal in a tank." The complete production sequence from incoming inspection through cleaning, activation, plating, post-treatment, drying, and final inspection typically involves 14 discrete process steps. Skipping any one of them invites defects.

6. **"Hydrogen: the unwanted guest"** -- at every cathode in every plating bath, hydrogen ions compete with metal ions for electrons. The hydrogen that wins becomes gas bubbles (causing pitting) and dissolved atomic hydrogen (causing embrittlement). Managing this side reaction is a constant challenge.

7. **"Soluble anodes replenish; insoluble anodes deplete"** -- the two anode systems work on opposite principles. Soluble anodes (copper, nickel, tin, silver) self-replenish the bath. Insoluble anodes (chrome, alkaline zinc) require the operator to add metal salts regularly. Know which system your bath uses.

---

*Research Brief v2 authored by Watson (`watson-chemistry-researcher`), 2026-04-11. Sources: 1993 Metal Finishing Guidebook and Directory (vault); Products Finishing (pfonline.com); Drew's Quick Reference Metal Finishing Notes (vault); domain expertise. Ion migration conventions (cations toward cathode, anions toward anode) are fundamental electrochemistry, verified. All voltage, CD, and process parameter ranges are industry-typical -- verify against specific product technical data for production use.*
