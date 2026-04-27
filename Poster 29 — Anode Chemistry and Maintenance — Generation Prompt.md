---
Project: Plating Posters Inc
Poster Number: 29
Title: "Anode Chemistry and Maintenance -- Soluble, Insoluble, and Everything Between"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-25T00:00:00
Source: Poster 29 -- Anode Chemistry and Maintenance -- Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - AnodeChemistry
  - AnodeMaintenance
  - SolubleAnode
  - InsolubleAnode
  - v1
---

# Claude Chat Generation Prompt -- Poster #29
## Anode Chemistry and Maintenance -- Soluble, Insoluble, and Everything Between
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-25).*

---

> **IMPORTANT:** Generate as HTML visual artifact. 24 x 36" portrait. Dark edition first. This poster has seven zones -- header, hero comparison, process table, passivation, anode bags, troubleshooting, footer.

---

## Elara Notes

> **DREW REVIEW NEEDED:** Watson disputes the CW's statement that alkaline zinc uses steel baskets and NOT titanium -- Watson claims Ti baskets are safe at plating temps. Tyler confirmed steel/NOT titanium as correct. The HTML poster shows steel baskets per Tyler's confirmation. Awaiting Drew's final adjudication before locking this detail.

> **Watson Flags (non-blocking):** (1) Confirm dissolution efficiency ranges for electrolytic Ni S-Rounds (95-100%) vs. carbonyl nickel. (2) Verify A:C ratios (2:1 nickel, 1:1 copper, etc.) against standard references.

> **Tyler Flag (non-blocking):** Validate anode bag maintenance schedule and inspection criteria against shop experience.

---

## Phase 0 -- Design System Reference

Refer to: `Plating Posters - Series Design Prompt.md` for all visual identity, glass surfaces, layout system, print CSS, and tweaks panel specs. This poster follows the canonical design system exactly.

Standard: 24x36", `#1A1F2E`, locked palette, 0.5" safe zone. 1200x1800 CSS px in `.stage` scaled via `transform:scale()`.

---

## Phase 1 -- Header (Zone 1)

### Step 1 -- Eyebrow
`POSTER #29` -- JetBrains Mono 500, 13pt, `#E8A020`, with amber left bar.

### Step 2 -- Headline
`ANODE CHEMISTRY AND MAINTENANCE` -- Barlow Condensed 800, 72pt, `#F0EDE8`. One word italicized and amber: `ANODE` as `<em>` in `#E8A020`.

### Step 3 -- Subheading
`Soluble, Insoluble, and Everything Between` -- Barlow 600, 30pt, `#E8A020`. Y below headline.

### Step 4 -- Tagline
`When the deposit goes wrong, check the anodes before you blame the bath.` -- Inter 400 italic, 16pt, `#F0EDE8` at 65%.

### Step 5 -- Rule Card (right)
Coral-tinted glass card. Big stat: `7` -- Barlow Condensed 900, 78pt, `#E05C5C`. Label: `ANODE-RELATED DEFECTS DIAGNOSED BELOW` -- Inter 500, 13pt, `#F0EDE8` at 70%.

---

## Phase 2 -- Soluble vs. Insoluble Hero (Zone 2)

Section label: `THE TWO FAMILIES OF ANODES` -- Barlow Condensed 800, 28pt, `#F0EDE8`, centered. Sublabel: `Every anode is one or the other -- know the difference` -- Inter 400, 13pt, `#F0EDE8` at 55%.

### Step 6 -- Soluble Anode Panel (left)

Glass card, amber-tinted border (2pt `#E8A020`), fill `rgba(30,36,53,.55)`.

Title: `SOLUBLE ANODES` -- Barlow Condensed 800, 26pt, `#E8A020`.
Subtitle: `The anode dissolves to replenish metal in the bath` -- Inter 400, 14pt, `#F0EDE8` at 60%.

Half-reaction (centered): `M --> M2+ + 2e-` -- JetBrains Mono 500, 18pt, `#E8A020`. Use superscript for `2+` and `-`.

Bullet list (Inter 400, 13pt, `#F0EDE8`, 140% line height):
- Anode metal dissolves during plating -- replenishes bath concentration
- Metal balance: dissolution rate ideally matches deposition rate
- Produces sludge/fines -- MUST use anode bags
- Purity matters -- impurities dissolve into the bath
- Requires chloride (in nickel) to prevent passivation

### Step 7 -- Insoluble Anode Panel (right)

Glass card, teal-tinted border (2pt `#2EC4B6`), fill `rgba(30,36,53,.55)`.

Title: `INSOLUBLE ANODES` -- Barlow Condensed 800, 26pt, `#2EC4B6`.
Subtitle: `The anode conducts current but does not dissolve` -- Inter 400, 14pt, `#F0EDE8` at 60%.

Half-reaction (centered): `2H2O --> O2 + 4H+ + 4e-` -- JetBrains Mono 500, 16pt, `#2EC4B6`. Use subscript for `2` in H2O and superscript for `+` and `-`.

Bullet list (Inter 400, 13pt, `#F0EDE8`, 140% line height):
- Anode does NOT dissolve -- no sludge, no anode bags needed
- Metal replenished by chemical addition (salts) or proprietary replenishers
- Bath chemistry requires more active management (metal level drops during plating)
- Generates O2 and acid at the anode -- must account for pH drift
- Longer life but higher initial cost

### Step 8 -- Anode Type Gallery

Six small glass cards in a single row below the two panels.

| Card | Accent | Type Name | Shape | Used In |
|---|---|---|---|---|
| 1 | `#E8A020` | SOLID BARS / SLABS | Tall rectangle | Zinc, copper, tin |
| 2 | `#E8A020` | S-ROUNDS / CHIPS | Circles in basket | Nickel (in Ti baskets) |
| 3 | `#E8A020` | CAST / ROLLED SHEET | Wide thin rectangle | Copper, tin |
| 4 | `#2EC4B6` | PLATINIZED TITANIUM | Rect with bright border | Precious metals, EN |
| 5 | `#2EC4B6` | DSA (MIXED OXIDE) | Rect with stripe pattern | Hard chrome, electrogalvanizing |
| 6 | `#2EC4B6` | LEAD / LEAD ALLOY | Solid dark rectangle | Hard chrome (traditional) |

Card title: Barlow 600, 12pt, accent color. "Used in" line: Inter 400, 11pt, `#F0EDE8` at 55%.

---

## Phase 3 -- Process-to-Anode Table (Zone 3)

Section label: `WHICH ANODE FOR WHICH PROCESS?` -- Barlow Condensed 800, 28pt, `#F0EDE8`, centered. Sublabel: `9 processes, 9 anode specifications` -- Inter 400, 13pt, `#F0EDE8` at 55%.

### Step 9 -- Process Table

Glass table, full width. Headers: `Process` | `Anode Type` | `Material` | `A:C Ratio` | `Key Notes`.

| Process | Type | Material | A:C | Notes |
|---|---|---|---|---|
| Watts nickel (bright) | Soluble | Electrolytic Ni S-Rounds in Ti baskets + PP bags | 2:1 | Chloride prevents passivation; S-Rounds dissolve evenly |
| Acid copper sulfate | Soluble | OFHC copper (P-deoxidized, 0.04-0.06% P) | 1:1 | P content controls dissolution rate |
| Acid zinc (chloride) | Soluble | SHG zinc slabs | 1:1 to 2:1 | Zinc dissolves readily; watch sludge buildup |
| Alkaline zinc (non-CN) | Soluble | SHG zinc in steel baskets | 1:1 | Steel baskets -- NOT titanium (zinc attacks Ti) |
| Hard chrome | Insoluble | Lead-antimony (6-8% Sb) or DSA | N/A | Chromic acid replenished by chemical addition |
| Gold (acid) | Insoluble | Platinized titanium | Per spec | Gold replenished by gold salt addition |
| Silver (cyanide) | Soluble | Fine silver (99.9%) bars | 2:1 | Anode bags critical -- silver sludge is expensive |
| Tin (acid) | Soluble | Pure tin bars or balls | 1:1 to 2:1 | Tin passivates easily -- maintain Sn2+ |
| Electroless nickel | N/A | None (chemical reduction -- no external anode) | N/A | Reducing agent (NaH2PO2) provides electrons |

"Soluble" in `#E8A020`. "Insoluble" in `#2EC4B6`. "N/A" in `#C8D0D8` at 50%. A:C ratios in JetBrains Mono 400, `#27AE60`. Alternating row tints.

---

## Phase 4 -- Anode Passivation (Zone 4)

Section label: `ANODE PASSIVATION -- THE SILENT BATH KILLER` -- Barlow Condensed 800, 26pt, `#F0EDE8`, centered. Sublabel: `It looks like a chemistry problem. It's an electrode problem.` -- Inter 400, 13pt, `#F0EDE8` at 55%.

### Step 10 -- What Happens and Why (left panel)

Glass card, coral left border (4pt `#E05C5C`).

Title: `WHAT HAPPENS AND WHY` -- Barlow 700, 18pt, `#E05C5C`.

Body (Inter 400, 13pt, `#F0EDE8`, 145% line height):
> A passive anode develops an oxide film that blocks metal dissolution. Current still flows -- but it goes to oxygen evolution instead of metal dissolution. The bath slowly starves of metal ions while the operator sees normal amperage on the meter.

**Symptoms** (Inter 500, `#E05C5C` label):
- Rising bath voltage (same amps, higher volts)
- Declining metal concentration despite normal plating load
- Darkening or filming on anode surface
- Gray or black sludge on anode surface
- pH drop (acid generation from O2 evolution)

**Causes** (JetBrains Mono 400, 12pt, `#E05C5C`):
- Low chloride (nickel) -- below 30 g/L NiCl2
- Excessive current density on anode (too small anode area)
- Contaminated anode surface (oil, grease, oxide)
- Wrong anode composition (carbonyl vs. electrolytic matters)
- Stagnant solution at anode surface (poor agitation)

### Step 11 -- Prevention and Recovery (right panel)

Glass card, emerald left border (4pt `#27AE60`).

Title: `PREVENTION AND RECOVERY` -- Barlow 700, 18pt, `#27AE60`.

**Prevention** (Inter 400, 13pt, `#F0EDE8`, 145% line height):
- Maintain chloride at or above minimum (nickel: 30+ g/L NiCl2)
- Size anodes to maintain proper A:C ratio -- never run undersized
- Use correct anode composition for the bath
- Ensure solution circulation reaches anode surface
- Keep anodes clean -- remove buildup during scheduled maintenance

**Recovery** (Inter 400, 13pt, `#F0EDE8`, 145% line height):
- Remove anodes from tank
- Scrub or acid-dip to remove oxide/film (10% HCl for nickel anodes)
- Inspect for unusual corrosion patterns -- pitting means impure anode
- Verify chloride level before re-installing
- Consider activating anodes in a "break-in" period at low current

Key callout (pill banner, amber glass):
`Prevention is cheaper than recovery -- a $5 chloride addition prevents a $500 bath adjustment`

---

## Phase 5 -- Anode Bags (Zone 5)

Section label: `ANODE BAGS -- YOUR FIRST LINE OF FILTRATION` -- Barlow Condensed 800, 24pt, `#F0EDE8`, centered. Sublabel: `The cheapest component that causes the most expensive defects when neglected` -- Inter 400, 13pt, `#F0EDE8` at 55%.

### Step 12 -- Bag Materials Table (left panel)

Glass card, teal left border (4pt `#2EC4B6`).

Title: `ANODE BAG MATERIALS` -- Barlow 700, 16pt, `#2EC4B6`.

| Material | Used For | Micron | Notes |
|---|---|---|---|
| Polypropylene (PP) | Nickel, copper, general | 1-10 um | Most common; chemical-resistant; heat-resistant to 200 F |
| Polyester (PE) | General, lower-temp baths | 1-10 um | Less heat-resistant than PP; good for acid zinc |
| Cotton / Dynel | Traditional; being phased out | Variable | Can shed fibers -- not for critical applications |
| Nylon | Acid baths | 5-25 um | Good strength; not suitable for strong alkali |

Key callout below table (JetBrains Mono 400, 12pt, `#2EC4B6`):
`Double-bag anodes in bright nickel -- the inner bag catches fines, the outer catches what the inner misses`

### Step 13 -- Maintenance Schedule (right panel)

Glass card, amber left border (4pt `#E8A020`).

Title: `ANODE BAG MAINTENANCE` -- Barlow 700, 16pt, `#E8A020`.

**Daily:**
- Visual check -- bags submerged, no tears, no collapse

**Weekly:**
- Remove and inspect for discoloration, holes, or clogging
- Check for sludge buildup inside bags -- if heavy, clean or replace
- Verify bag is not restricting solution flow around anode

**Monthly or as needed:**
- Replace bags showing discoloration, reduced porosity, or physical damage
- Rinse new bags in DI water before use (removes sizing compounds)
- Replace ALL bags at the same time -- mixing old and new changes flow distribution

Warning callout (coral glass): `If you see black or gray particles on plated parts, check anode bags FIRST.`

---

## Phase 6 -- Troubleshooting (Zone 6)

Section label: `ANODE-RELATED DEFECTS -- DIAGNOSIS TABLE` -- Barlow Condensed 800, 26pt, `#F0EDE8`, centered. Sublabel: `7 symptoms, 7 anode causes -- check here before you blame the chemistry` -- Inter 400, 13pt, `#F0EDE8` at 55%.

### Step 14 -- Defect Diagnosis Table

Glass table, full width. Headers: `Symptom` | `Anode Cause` | `Check` | `Fix`.

| Symptom | Anode Cause | Check | Fix |
|---|---|---|---|
| Rough deposits / particles | Torn anode bags; anode sludge in bath | Inspect bags; check bath clarity | Replace bags; filter bath; clean anodes |
| Thin deposits / slow plating | Passivated anodes; insufficient anode area | Check voltage (rising?); check metal level | Activate anodes; add anode area; replenish chloride |
| Uneven thickness | Poor anode placement; mismatched A:C ratio | Compare HCD/LCD; check anode positioning | Reposition anodes; adjust A:C ratio |
| High voltage / high power | Passivated anodes; poor connection | Check bus bar contacts; check anode surface | Clean contacts; de-passivate anodes |
| Dark deposits at LCD | Anode impurities dissolving into bath | Analyze bath for contaminants; check purity cert | Dummy plate; switch to higher-purity anodes |
| pH dropping unexpectedly | Passivated anodes (O2 evolution generates acid) | Check dissolution rate vs. deposition rate | De-passivate; correct metal balance |
| Anode sludge excessive | Wrong composition; CD too high on anode | Check anode spec sheet; check A:C ratio | Use correct anode type; increase anode area |

Symptom column: Inter 500, `#E05C5C`. Alternating row tints.

---

## Phase 7 -- Footer

Standard footer per design system.

Disclaimer: `This poster is an educational reference tool. Anode types, compositions, and maintenance procedures are typical industry values. Specific anode requirements vary by bath chemistry, proprietary formulation, and application. Consult your anode supplier and process chemical supplier for application-specific guidance.`

Title: `Anode Chemistry and Maintenance -- Soluble, Insoluble, and Everything Between`
Version: `v1.0 -- 2026`
Poster: `#29`

---

## Phase 8 -- Light Remap & Export

Standard remap via `body[data-edition="light"]`. Six files: `Anode Chemistry and Maintenance -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Phase 9 -- Review Checklist

- [ ] Headline `ANODE CHEMISTRY AND MAINTENANCE` with `ANODE` in amber italic
- [ ] Rule card: big `7` with defect count label
- [ ] Soluble panel: amber border, half-reaction `M --> M2+ + 2e-`, 5 bullets
- [ ] Insoluble panel: teal border, half-reaction `2H2O --> O2 + 4H+ + 4e-`, 5 bullets
- [ ] 6-card anode type gallery row
- [ ] 9-row process-to-anode table with colored type labels and JetBrains Mono A:C ratios
- [ ] Alkaline zinc row shows steel baskets, NOT titanium
- [ ] Passivation left panel: symptoms + causes (coral)
- [ ] Prevention/recovery right panel (emerald) + amber pill callout
- [ ] Anode bag materials table (4 materials) + double-bag callout
- [ ] Maintenance schedule: daily/weekly/monthly + coral warning
- [ ] 7-row troubleshooting table with coral symptom column
- [ ] pH drop row explicitly links to passivated anode O2 evolution
- [ ] Footer with disclaimer, title, version, poster number
- [ ] Tweaks panel: Dark/Light + Grid + Print
- [ ] Print CSS: `@page { size: 12.5in 18.75in; margin:0; }`
- [ ] No brand names, no supplier names, no product codes
- [ ] Zero `color-mix()` -- all colors pre-mixed to hex
- [ ] Zero `opacity` on pseudo-elements -- alpha baked into color
- [ ] All glass surfaces have solid `background-color` fallback

---

| v1.0 | 2026-04-25 | Initial from CW v1.0. |
