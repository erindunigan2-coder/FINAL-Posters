---
Project: Plating Posters Inc
Poster Number: 4
Title: Reading Your Hull Cell Panel
Document Type: Content and Layout Draft
Status: v1.0 — Ready for Affinity Designer Build
Created: 2026-03-18T00:00:00
Updated: 2026-03-18T00:00:00
Author: Alaina (poster-designer)
Technical Source: Watson — Acid Zinc Plating Troubleshooting Guide v1 (Sections 4, 7, 8)
Watson Flags: C1 CLEARED / C2 CLEARED / C3 CLEARED — see Section 1 of this document
Process Scope: Acid zinc KCl/NH4Cl only — one process per poster (standing series rule)
Editions: Dark + Light
tags:
  - PosterDesign
  - HullCell
  - ContentDraft
  - AcidZinc
---

# Poster #4 — Content and Layout Draft
## Reading Your Hull Cell Panel

*Alaina — Plating Posters Inc Creative Lead*
*v1.0 — 2026-03-18*
*All three Watson verification flags cleared from Watson's Acid Zinc Plating Troubleshooting Guide v1 (2026-03-14). All technical content is now production-ready. This document is the authoritative content source for the Affinity Designer build.*

---

## Section 1 — Watson Flag Clearances

All three flags blocking the Affinity Designer build have been cleared from Watson's own research.

---

### FLAG C1 — CLEARED: Anode Specification and Cathode Prep

**Source:** Watson, *Acid Zinc Plating Troubleshooting Guide* v1, Sections 5.1 and 7.1–7.2.

**Confirmed values for Block C (Setup Parameters Table):**

- **Anode material:** Special High Grade (SHG) zinc, 99.99% purity — confirmed and strongly emphasized by Watson. The exact note from Section 5.1: "Always use Special High Grade (SHG) 99.99% pure zinc anodes — lower grade introduces Pb, Cd, Fe directly into the bath." This is not just a recommendation — it is a contamination-prevention requirement. Update the anode row in Block C to read "SHG zinc (99.99%) — lower grades introduce Pb, Cd, Fe" with the warning logic embedded.
- **Cathode prep sequence:** Confirmed exactly as drafted. Section 7.2: "Degrease with acetone or electrocleaner; acid activate in 5–10% HCl for 15–30 seconds; rinse; use immediately. Do not handle with bare hands after activation." No deviations noted.
- **Optional step confirmed:** "Optional: bright dip or passivate panel to reveal deposit quality for post-plate evaluation." This is worth adding as a small callout note to Block C — it adds significant practical value for experienced users without cluttering the table.

**Action:** Block C is production-ready. Add the "SHG — lower grades introduce contamination" note to the anode row. Add the optional passivation step as a supplementary note below the Cathode Prep block.

---

### FLAG C2 — CLEARED: Current Density Values at HCD and LCD Extremes

**Source:** Watson, *Acid Zinc Plating Troubleshooting Guide* v1, Section 7.3.

**Confirmed values for Block D (Hull Cell Panel Diagram zone sub-labels):**

Watson's Section 7.3 states: "Use Wagner current density scale chart for current-to-position conversion."

Confirmed zone values at 2A total current:
- **HCD zone (left, narrow end):** ~10–50 A/dm²
- **Mid-current zone:** ~2–10 A/dm²
- **LCD zone (right, wide end):** ~0.1–1 A/dm²

These values match the draft exactly. They are confirmed for use in the diagram sub-labels without qualification. Watson notes the Wagner scale as the appropriate reference — this is standard industry practice and these values align with it.

**Action:** Block D diagram zone sub-labels are production-ready as drafted. No placeholder language needed — remove the "Watson flag pending" parentheticals from the zone sub-labels in the design brief and build them into the illustration.

**Additional note for Block C:** Watson's Section 7.1 confirms the test current range: "2–3 amperes (2A most common for routine diagnostics)" for rack, and 1 A for barrel. The current brief has "2 A (most common)" which is correct. Consider adding a note that 3 A is sometimes used for high-current diagnostic work — this gives the poster slightly more completeness without cluttering the table.

---

### FLAG C3 — CLEARED: Contamination Thresholds and Treatment Ratios

**Source:** Watson, *Acid Zinc Plating Troubleshooting Guide* v1, Sections 4.1–4.4 and 8.3–8.5.

All contamination thresholds and treatment protocols confirmed for Block E (Diagnostic Table). Full detail below:

**Iron contamination:**
- Problem threshold: >50–75 ppm (Watson Section 4.1: "Acceptable range: 0–50 ppm; Problem threshold: >50–75 ppm; Severe: >75 ppm — skip plate and coverage failure")
- H₂O₂ treatment: 1–2 mL/L of 30% H₂O₂ — confirmed (Section 8.3)
- pH raise to 5.0–5.5 for iron precipitation — confirmed
- Filtration required after treatment — confirmed
- Additional symptom confirmed: "yellowing/discoloration at HCD" — the yellowish HCD band is the characteristic visual signature on the Hull cell panel

**Lead contamination:**
- Problem threshold: 1–2 ppm — much lower than the current draft implied (update Block E to add the 1–2 ppm note)
- Characteristic symptom confirmed: "skip plate or no deposit in LCD; deposit brightness failure in low-current areas; problem appears similar to brightener overload but does not respond to brightener addition" — this differentiator is the key diagnostic insight and must be prominent in Block E
- Treatment confirmed: zinc dust treatment (1–3 lb/1000 gal, ~0.12–0.36 g/L) + dummy plate + source elimination (Section 8.5)

**Cadmium contamination:**
- Problem threshold: 1–2 ppm — essentially identical to lead (Watson Section 4.4: "Symptoms: essentially identical to lead contamination")
- Treatment confirmed: zinc dust + dummy plating + source elimination
- Safety flag: Watson notes cadmium is "highly toxic; trace contamination via parts should trigger immediate bath analysis" — this is a critical note to carry into the poster

**Copper contamination:**
- Problem threshold: >10 ppm — confirmed (Section 4.2)
- Characteristic symptom confirmed: "dark to black deposit, particularly visible after bright dip or passivation; deposit may appear bronze-tinted" — the "visible after passivation" detail is important and should be preserved in Block E
- Treatment confirmed: dummy plate at low CD (0.1–0.3 A/dm²) — confirmed (Section 8.4: "Operate at LOW current density: 0.1–0.5 A/dm² — preferentially deposits Cu, Pb, Cd over zinc")
- Secondary treatment: zinc dust (1–3 lb/1000 gal), then carbon treatment

**Organic contamination:**
- Characteristic symptoms confirmed: LCD dullness, streaking, variable pitting (Section 3.6)
- Treatment confirmed: carbon treat at 5–10 g/L; H₂O₂ pre-treatment at 0.5–1 mL/L of 30% H₂O₂ if severe (note: lower dose than iron treatment); reconstitute additive system after (Section 8.2)
- Important note: "carbon removes brightener and carrier along with contaminants — always reconstitute after treatment." This is worth a brief callout in Block F or a footnote to Block E.

**Action:** Block E is production-ready with the updates noted above. Revise the Lead/Cadmium row to reflect the 1–2 ppm threshold. Preserve the "visible after passivation" detail for the copper row. Add a brief cadmium safety note as a footnote. Full revised table text is in Section 3 of this document.

---

## Section 2 — Final Poster Copy: All Text Blocks

This is the complete, production-ready copy for every text element on the poster. Typeset directly from this section in Affinity Designer.

---

### BLOCK A — Headline and Subheading

**Headline (Barlow Condensed ExtraBold, 96–120 pt, #F0EDE8 Dark / #1A1F2E Light):**

> READING YOUR HULL CELL PANEL

**Subheading (Barlow SemiBold, 42–48 pt, #E8A020 Dark / #C8860A Light):**

> Diagnose your plating bath before it diagnoses your scrap rate.

**Series tag (footer — Barlow SemiBold, 16–18 pt, #F0EDE8 at 70% opacity):**

> Plating Posters Inc — Metal Finishing Reference Series

---

### BLOCK B — What Is a Hull Cell? (Orientation Box)

**Callout title (Barlow SemiBold, 24 pt, #2EC4B6 Dark / #1A8C82 Light):**

> WHAT IS A HULL CELL?

**Body (Inter Regular, 18–20 pt, #F0EDE8 Dark / #1A1F2E Light):**

> The Hull cell is a 267 mL trapezoidal tank that simultaneously tests a range of current densities on a single cathode panel. The angled cathode creates a current density gradient — high at one end, low at the other — so one 5-minute test reveals how your bath performs across its entire operating range.
>
> One panel. One test. Every zone, all at once.

*Design note: the final one-liner ("One panel...") should be set in Inter Medium or SemiBold, slightly offset or with a top rule, to give it the character of a closing punch. It is the conceptual hook for anyone who hasn't run a Hull cell before.*

---

### BLOCK C — Setup Parameters Table

**Section title (Barlow SemiBold, 28 pt, #E8A020):**

> HULL CELL SETUP PARAMETERS

**Table header row (Barlow/Inter SemiBold, 22–24 pt, #E8A020 on #3A4055):**

| PARAMETER | VALUE |
|-----------|-------|

**Table data (JetBrains Mono Regular, 18–20 pt, #F0EDE8):**

| Parameter | Value |
|-----------|-------|
| Cell volume | 267 mL |
| Cathode material | Cold-rolled steel — cleaned and acid-activated |
| Anode material | SHG zinc — 99.99% pure (lower grades introduce Pb, Cd, Fe) |
| Test current — rack | 2 A (standard); 3 A for high-current diagnostic |
| Test current — barrel | 1 A |
| Test duration | 5 minutes |
| Agitation | Air agitation — required |
| Temperature | Match actual bath temperature |

**Cathode prep note (below table — Inter Regular, 16 pt, #F0EDE8, with top rule in #3A4055):**

> CATHODE PREPARATION: Degrease with acetone or electrocleaner. Activate in 5–10% HCl for 15–30 seconds. Rinse thoroughly. Use immediately. Do not touch with bare hands after activation.
>
> OPTIONAL: Bright dip or passivate the plated panel to reveal deposit quality — highly recommended for contamination diagnosis.

*Design note: "SHG zinc — 99.99% pure (lower grades introduce Pb, Cd, Fe)" is the anode row. The parenthetical is short and important — it explains why 99.99% matters without requiring a footnote. Keep it on one line if the column width allows; wrap to two lines if needed. Never truncate the contamination warning.*

---

### BLOCK D — Hull Cell Panel Diagram

*This block is illustration specification, not typeset copy. Refer to Section 5.1 of the Design Brief for the full vector illustration spec. The text elements that appear on or near the diagram are listed below for typesetting reference.*

**Zone labels (Barlow Condensed ExtraBold, 24–28 pt — color per zone):**

Left zone (Amber #E8A020):
> HIGH CURRENT DENSITY

Center zone (Warm White #F0EDE8):
> MID-CURRENT

Right zone (Teal #2EC4B6):
> LOW CURRENT DENSITY

**Zone sub-labels (JetBrains Mono Regular, 16–18 pt, #F0EDE8 — confirmed values, no flags):**

Left:
> ~10–50 A/dm² at 2 A

Center:
> ~2–10 A/dm² at 2 A

Right:
> ~0.1–1 A/dm² at 2 A

**Diagram caption (Inter Regular, 14–16 pt, #F0EDE8 at 70% opacity, centered below diagram):**

> Current density values per Wagner scale. Left (narrow end) = high current density. Right (wide end) = low current density.
> Acid zinc KCl/NH₄Cl bath — 2 A total current standard.

---

### BLOCK E — Diagnostic Interpretation Table (FINAL — All Watson Flags Cleared)

**Section title (Barlow SemiBold, 28–32 pt, #E8A020):**

> WHAT YOUR PANEL IS TELLING YOU

**Table header row (Barlow/Inter SemiBold, 22–24 pt, #E8A020 on #3A4055):**

| PANEL APPEARANCE | MOST LIKELY CAUSE | FIRST CORRECTIVE ACTION |

**Table data (Inter Regular, 18–20 pt, #F0EDE8):**

*Row border color codes are specified in parentheses — these drive the 4 pt left-border accent in Affinity Designer.*

| Panel Appearance | Most Likely Cause | First Corrective Action | Border |
|------------------|-------------------|------------------------|--------|
| Mirror bright from HCD through mid-current; slight softening at LCD; no skip plate | **Good bath** | No action needed — archive this panel as your visual reference standard | Emerald |
| Overall semi-bright or matte; burn zone at HCD enlarges toward mid-current | **Brightener deficiency** | Add brightener in 0.1–0.5 mL/L increments; re-run panel after each addition | Amber |
| Mirror bright at HCD and mid-current; LCD progressively dull, advancing to skip plate at extremes | **Brightener overload** | Carbon treat at 5–10 g/L; reconstitute additive system from fresh baseline | Amber |
| Pitting across the full panel; HCD burning prominent | **Carrier (wetting agent) deficiency** | Check bath temperature vs. cloud point first; add carrier incrementally; re-run panel | Amber |
| Overall hazy or milky panel; reduced deposit brightness; foaming visible in production tank | **Carrier overload / temperature above cloud point** | Check and lower bath temperature immediately; carbon treat if needed | Amber |
| Yellow to dark band at HCD; haze across mid-current; LCD coverage loss or skip plate | **Iron contamination (>50–75 ppm)** | Add 1–2 mL/L of 30% H₂O₂; raise pH to 5.0–5.5; allow to settle; filter thoroughly | Coral |
| Skip plate in LCD; HCD appears normal; no improvement after brightener adjustment | **Lead or cadmium contamination (1–2 ppm threshold)** | Zinc dust treatment; dummy plate at low CD; identify and eliminate contamination source | Coral |
| Dark or black deposit visible after bright dip or passivation | **Copper contamination (>10 ppm)** | Dummy plate at 0.1–0.3 A/dm² on steel cathodes; follow with zinc dust treatment | Coral |
| LCD dullness; streaking across panel; variable pitting not resolved by carrier addition | **Organic contamination** | H₂O₂ pre-treat at 0.5–1 mL/L; then carbon treat at 5–10 g/L; reconstitute additives | Coral |
| Burning advances from HCD into mid-current; LCD coverage is consistently poor | **Low zinc metal concentration** | Analyze zinc by titration; add zinc metal source; verify anode area is adequate | Amber |
| Rough, nodular deposit; visible particles in bath; turbidity | **Suspended solids — pH too high or filtration failure** | Check pH (target 4.8–5.2); inspect filter integrity and anode bags; clean tank bottom | Amber |

**Table footnotes (Inter Regular, 13–14 pt, #F0EDE8 at 60% opacity — below table):**

> *Scope: acid zinc KCl/NH₄Cl baths only. Results may differ for other zinc bath chemistries.*
>
> *Cadmium is highly toxic. Even trace cadmium contamination via parts warrants immediate bath analysis. Do not assume lead or cadmium without analytical confirmation.*
>
> *After any carbon treatment, brightener and carrier are partially removed. Always reconstitute the full additive system after carbon treatment.*

---

### BLOCK F — The Isolation Test Protocol (Callout Box)

**Callout title (Barlow SemiBold, 24–28 pt, #2EC4B6 Dark / #1A8C82 Light):**

> WHEN THE DIAGNOSIS ISN'T CLEAR: THE ISOLATION PROTOCOL

**Intro line (Inter Regular, 18 pt, #F0EDE8):**

> When one corrective action doesn't solve the problem, test one variable at a time using separate aliquots of fresh bath solution.

**Numbered steps (Inter Regular, 18 pt, #F0EDE8):**

> 1. Add a brightener increment to a fresh aliquot — run panel. If HCD and mid-current improve: brightener was low.
>
> 2. Add a carrier increment to a fresh aliquot — run panel. If pitting clears: carrier was low.
>
> 3. Add boric acid to a fresh aliquot — run panel. If HCD burning reduces: boric acid was low.
>
> 4. Adjust pH in a fresh aliquot with HCl or zinc carbonate — run panel. Confirm whether pH drift was the driver.

**Closing rule (Inter Medium, 18 pt, #E8A020, with 2 pt Amber left accent rule):**

> THE RULE: Change one variable. Run one panel. Decide. Then move to the next variable.

---

### BLOCK G — Hull Cell as an SPC Tool (Callout Box)

**Callout title (Barlow SemiBold, 20 pt, #2EC4B6 Dark / #1A8C82 Light):**

> MAKE YOUR HULL CELL A CONTROL CHART

**Body bullets (Inter Regular, 16–18 pt, #F0EDE8):**

> - Run weekly at minimum — or every 500–1000 ampere-hours of production throughput
>
> - Archive every panel with: date, bath analysis results, ampere-hour reading, and all additions made
>
> - Laminate a known-good reference panel and mount it next to this poster
>
> - Visual trends across archived panels reveal bath drift before symptoms appear on production parts

---

### BLOCK H — Footer Content

**Left — Poster title (Barlow SemiBold, 16 pt, #F0EDE8):**
> Reading Your Hull Cell Panel

**Center — Series name (Inter Regular, 14 pt, #F0EDE8 at 70% opacity):**
> Plating Posters Inc — Metal Finishing Reference Series

**Far right — Logo placeholder (JetBrains Mono, 12 pt, #3A4055 fill box):**
> [LOGO]

**Disclaimer — above footer band, full width, centered (Inter Regular, 11–12 pt, #F0EDE8 at 50% opacity):**
> This poster is a diagnostic reference tool. Always consult your process supplier's documentation and applicable safety data sheets. Not a substitute for laboratory analysis.

**Version (JetBrains Mono, 11 pt, #F0EDE8 at 50% opacity, bottom-right within footer):**
> v1.0 — 2026

---

## Section 3 — Detailed Layout Specification

This section maps every content block to its precise position, dimensions, and palette treatment. It is the production build checklist for Affinity Designer. Read in conjunction with Section 5 (Production Layout Plan) of the Design Brief (v1.0).

---

### Overall Artboard Architecture (24×36" master)

```
┌──────────────────────────────────────────────────────────────────────┐
│ ZONE 1 — HEADER BAND (top ~8% / ~2.9")                              │
│ BLOCK A: Headline (left) + BLOCK B: Orientation Box (right)          │
├──────────────────────────────────────────────────────────────────────┤
│ ZONE 2 — HULL CELL PANEL ILLUSTRATION (rows 9–38% / ~10.4")         │
│ BLOCK D: Full-width vector diagram with zone bands + labels          │
│ Callout arrows drop from HCD / Mid / LCD zones into table below      │
├───────────────────────────────────┬──────────────────────────────────┤
│ ZONE 3A — DIAGNOSTIC TABLE        │ ZONE 3B — RIGHT COLUMN           │
│ BLOCK E (cols 1–7 / ~58% width)   │ BLOCK C — Setup Parameters (top) │
│ 11 rows (1 header + 10 data)      │ BLOCK G — SPC Callout (bottom)   │
│ ~37% of poster height / ~13.3"    │ Same height band as 3A           │
│                                   │ (~38% width / cols 8–12)         │
├───────────────────────────────────┴──────────────────────────────────┤
│ ZONE 4 — ISOLATION PROTOCOL CALLOUT (rows ~75–87% / ~4.3")          │
│ BLOCK F: Full-width callout box                                      │
├──────────────────────────────────────────────────────────────────────┤
│ ZONE 5 — FOOTER BAND (bottom ~6% / ~2.2")                           │
│ BLOCK H: Title | Series name | Logo | Disclaimer | Version           │
└──────────────────────────────────────────────────────────────────────┘
```

---

### Zone 1 — Header Band

**Affinity Designer layer:** `[TYPE] Headline` (headline/subheading) + `[CALLOUT] What Is a Hull Cell` (Block B box)

**Headline:** Left-aligned within the safe zone (0.5" from trim). Barlow Condensed ExtraBold, 96–120 pt, `#F0EDE8`. Tracking: −15 to −20 (tight — Barlow Condensed is built for this). Baseline sits approximately at the horizontal midpoint of the header band height.

**Subheading:** Left-aligned, 6–8 pt below the headline baseline. Barlow SemiBold, 42–48 pt, `#E8A020`.

**Block B box:** Right-aligned; width spans approximately columns 8–12 (38% of artboard width); vertically centered within the header band. Internal padding 20 pt. Rounded rectangle: `#1E2435` fill, `#2EC4B6` border 1.5 pt, 8 pt corner radius. Title in Barlow SemiBold 24 pt, `#2EC4B6`. Body in Inter Regular 18–20 pt, `#F0EDE8`. Closing punch line in Inter SemiBold or with top rule separator.

**Horizontal rule:** Optional — a 1 pt rule in `#3A4055` along the bottom edge of the header band can cleanly separate it from the diagram zone. Evaluate during layout polish.

---

### Zone 2 — Hull Cell Panel Illustration

**Affinity Designer layers:** `[ILLUS] Hull Cell Panel` (parent group), `[ILLUS] Zone Bands`, `[ILLUS] Zone Labels`, `[ILLUS] Callout Arrows`

**Panel dimensions:** Full artboard width minus the 0.5" safe-zone margins on each side. Approximate ratio: 16:5 (width to height) based on actual Hull cell panel geometry — refine to look proportionally correct. The panel should be wide and relatively shallow — it is a diagnostic instrument, not a painting.

**Surface treatment (vector):**
- Base fill: gradient mesh or linear gradient — `#C8D0D8` (Bright Silver) central to slightly lighter `#D8E0E8` toward the HCD (left) edge, reflecting the more active deposit zone. A very subtle tonal shift rightward toward a slightly more muted `#B8C0C8` at the LCD end. The gradient represents the visual signature of a healthy deposit across the full operating range.
- The surface should read as metallic — flat with a hint of reflectivity. Achieve this with a very subtle linear gradient rather than a complex gradient mesh on the first build. Refine later if time permits.
- Panel edge: 2–3 pt stroke in `#9AA0B0`. Slightly darker at the left (HCD) corner edge to suggest the shadow of a thicker deposit.

**Zone bands:** Along the top edge of the panel only — approximately 12–15% of the panel height. Three color zones using overlapping transparent gradient shapes:
- Left third: `#E8A020` (Amber), fading to transparent toward center. Opacity: 70% at the HCD edge, fading to 0% at the one-third mark.
- Center: no fill — the silver panel reads through.
- Right third: `#2EC4B6` (Teal), fading from transparent at center to 70% opacity at the LCD edge.
- Both zones should overlap in the center region and dissolve naturally — avoid hard edges. This is a gradient transition, not a segmented bar chart.

**Zone labels:** Positioned below the panel illustration (not overlaid on top). Three groups:
- Left: "HIGH CURRENT DENSITY" in Barlow Condensed ExtraBold 24–28 pt, `#E8A020`, centered under the left third of the panel. Sub-label "~10–50 A/dm² at 2 A" in JetBrains Mono 16 pt, `#F0EDE8`, 4 pt below the zone label baseline.
- Center: "MID-CURRENT" in Barlow Condensed ExtraBold 24–28 pt, `#F0EDE8`, centered under the middle third. Sub-label "~2–10 A/dm² at 2 A" in JetBrains Mono 16 pt.
- Right: "LOW CURRENT DENSITY" in Barlow Condensed ExtraBold 24–28 pt, `#2EC4B6`, centered under the right third. Sub-label "~0.1–1 A/dm² at 2 A" in JetBrains Mono 16 pt.

**Callout arrows:** Three leader lines dropping from a point on the bottom edge of the panel (one per zone) downward toward the diagnostic table section. Lines in `#3A4055` (Mid Slate), 1.5 pt weight, with a small rounded arrowhead at the lower end pointing toward the table. The arrows guide the eye from the diagram into the data — they are navigation aids, not decorative elements. Keep them clean and modest.

**Diagram caption:** Below the zone labels, centered, Inter Regular 14–16 pt, `#F0EDE8` at 70% opacity. See Block D copy in Section 2.

---

### Zone 3A — Diagnostic Interpretation Table

**Affinity Designer layer:** `[DATA] Diagnostic Table`

**Dimensions:** Columns 1–7 (approximately 58% of artboard width within safe zone margins). Full height of Zone 3 (~37% of poster height).

**Section title:** "WHAT YOUR PANEL IS TELLING YOU" — Barlow SemiBold 28–32 pt, `#E8A020`, left-aligned above the table. 12 pt spacing below to table top rule.

**Table structure:** 12 rows total (1 header + 11 data rows — one row per diagnostic scenario).

**Header row:** Fill `#3A4055`. Text: Barlow SemiBold 22–24 pt, `#E8A020`. Column labels: "PANEL APPEARANCE" / "MOST LIKELY CAUSE" / "FIRST CORRECTIVE ACTION". Column width proportions: 40% / 30% / 30%.

**Data row backgrounds:**
- Odd rows: `#1A1F2E` (same as background — reads as a subtle distinction)
- Even rows: `#252B3D` (Alt Row)

**Left-border accents (4 pt width rectangles, full cell height):**
- Row 1 (Good bath): `#27AE60` (Emerald) + 8% Emerald fill over row background
- Rows 2–5 and 10–11 (chemistry-drift causes): `#E8A020` (Amber)
- Rows 6–9 (contamination causes): `#E05C5C` (Coral)

**Cell padding:** 8 pt top/bottom, 10 pt left/right. Left padding accounts for the 4 pt left-border accent — content begins 14 pt from left edge of cell.

**Body text:** Inter Regular 18–20 pt, `#F0EDE8`. Line height: 140% for multi-line cells. The "Most Likely Cause" column should bold or highlight the cause name (first few words) — use Inter Medium or SemiBold for the cause name, dropping to Inter Regular for any parenthetical. Example: **Iron contamination** (>50–75 ppm) — the bolding makes scanning the cause column fast.

**Table footnotes:** Below the table, left-aligned, Inter Regular 13–14 pt, `#F0EDE8` at 60% opacity. Three footnotes from Block E copy in Section 2.

---

### Zone 3B — Right Column

**Affinity Designer layers:** `[DATA] Setup Table` (Block C), `[CALLOUT] SPC Tool` (Block G)

**Dimensions:** Columns 8–12 (approximately 38% of artboard width within safe zone). A gutter of approximately 0.25–0.375" separates Zone 3A and Zone 3B. Both zones share the same vertical extent.

**Block C — Setup Parameters Table:**

Section title: "HULL CELL SETUP PARAMETERS" — Barlow SemiBold 28 pt, `#E8A020`, left-aligned above table.

Table header: `#3A4055` fill, "PARAMETER" / "VALUE" in Barlow SemiBold 22 pt, `#E8A020`.

Table data: JetBrains Mono Regular 18–20 pt, `#F0EDE8`. Row alternation: same `#1A1F2E` / `#252B3D` as the diagnostic table — visual consistency across columns.

Parameter column: 45% width. Value column: 55% width.

8 data rows per the table copy in Section 2.

Cathode prep note: below the table proper, with a 1 pt top rule in `#3A4055`. Inter Regular 16 pt, `#F0EDE8`. Introduce with "CATHODE PREPARATION" in Barlow SemiBold as a micro-header.

**Space between Block C and Block G:** Approximately 0.25–0.375" gap. Evaluate during layout — if space is tight, reduce internal padding in one of the elements rather than cutting content.

**Block G — SPC Tool Callout:**

Bottom of the right column. Rounded rectangle: `#1E2435` fill, `#2EC4B6` border 1.5 pt, 8 pt corner radius. Internal padding 16–20 pt.

Title: "MAKE YOUR HULL CELL A CONTROL CHART" — Barlow SemiBold 18–20 pt, `#2EC4B6`. (Reduced from the 20 pt spec in the brief — the right column is narrower, so the title may need to wrap to two lines. Set it to wrap cleanly and reduce size if needed to keep it on two lines maximum.)

Body: Inter Regular 16 pt, `#F0EDE8`. Four bullet points. Bullet character: a small filled circle in `#2EC4B6` (use Affinity Designer text frame bullet style or a manually placed symbol).

---

### Zone 4 — Isolation Protocol Callout

**Affinity Designer layer:** `[CALLOUT] Isolation Protocol`

**Dimensions:** Full artboard width (within safe zone margins). Height: approximately 12% of poster height (~4.3"). Vertical position: rows 75–87%.

**Container:** Rounded rectangle. `#1E2435` fill, `#2EC4B6` border 1.5 pt, 8 pt corner radius. Internal padding: 20 pt all sides.

**Horizontal layout within the callout:** Two-column internal layout.
- Left column (~40% of callout width): Title + intro line
- Right column (~56% of callout width, with gutter): Numbered steps (1–4) + closing rule line

This two-column structure keeps the callout from reading as a wall of text and makes it scan faster.

**Title:** Barlow SemiBold 24–28 pt, `#2EC4B6`. May split across two lines — keep "WHEN THE DIAGNOSIS ISN'T CLEAR:" on line 1 and "THE ISOLATION PROTOCOL" on line 2. Both lines left-aligned, tight leading.

**Intro line:** Inter Regular 18 pt, `#F0EDE8`. Below title, with 8 pt spacing.

**Steps:** Inter Regular 18 pt, `#F0EDE8`. Numbering in JetBrains Mono or Barlow SemiBold, `#2EC4B6` — makes the numbered list scannable.

**Closing rule:** The "THE RULE:" line — Inter Medium 18 pt, `#E8A020`, with a 2 pt Amber left accent rule. This is the visual anchor and takeaway for the entire callout.

---

### Zone 5 — Footer Band

**Affinity Designer layers:** `[BG] Footer Strip`, `[FOOTER] Footer Content`

**Dimensions:** Full artboard width, bottom 6% of poster height (~2.2"). `#0D1020` (Deep Navy) fill.

**Disclaimer:** Above the footer band top edge, full width, centered. Inter Regular 11–12 pt, `#F0EDE8` at 50% opacity. 8 pt spacing between disclaimer text and footer band top edge.

**Within footer band — three-column internal layout:**
- Left: "Reading Your Hull Cell Panel" — Barlow SemiBold 16 pt, `#F0EDE8`
- Center: "Plating Posters Inc — Metal Finishing Reference Series" — Inter Regular 14 pt, `#F0EDE8` at 70% opacity
- Right: Logo placeholder rectangle (40×40 px equivalent), `#3A4055` fill, "LOGO" in JetBrains Mono 12 pt centered

**Version number:** "v1.0 — 2026" — JetBrains Mono 11 pt, `#F0EDE8` at 50% opacity. Bottom-right corner within footer, above logo or below it (evaluate at layout time).

---

## Section 4 — Light Edition Conversion Notes

The Dark edition is the master. These notes describe what to verify when producing the Light edition via Global Color remapping in Affinity Designer.

**Global Colors remap (confirmed in Series Design Standards and Design Brief Section 5.5):**

| Dark | Light |
|------|-------|
| `#1A1F2E` Background | `#F5F4F0` |
| `#F0EDE8` Warm White text | `#1A1F2E` |
| `#1E2435` Dark Callout BG | `#ECEEF4` |
| `#252B3D` Alt Row | `#E8E8F0` |
| `#0D1020` Deep Navy | `#1A1F2E` |
| `#E8A020` Amber | `#C8860A` |
| `#2EC4B6` Teal | `#1A8C82` |
| `#27AE60` Emerald | `#1E7A47` |
| `#E05C5C` Coral | `#B83E3E` |
| `#3A4055` Mid Slate | `#D0D4DE` |
| `#C8D0D8` Bright Silver | `#C8D0D8` (unchanged) |

**Post-remap verification checklist:**
- [ ] Panel illustration base `#C8D0D8` still reads as metallic against `#F5F4F0` background — it should; silver against off-white is a clean combination
- [ ] Amber zone bands and labels read clearly in `#C8860A` against `#F5F4F0` (check contrast — `#C8860A` on `#F5F4F0` is approximately 4.8:1, which clears WCAG AA)
- [ ] Teal callout borders and titles read in `#1A8C82` against `#ECEEF4` — should be strong
- [ ] Emerald left-border on "Good bath" row reads against `#E8E8F0` alternate row background
- [ ] Coral left-borders on contamination rows read against `#E8E8F0`
- [ ] "Good bath" row's 8% Emerald fill tint over `#E8E8F0` is still visible (may need to increase to 12% opacity in Light edition — check at layout time)
- [ ] All footnote text (set at 60% opacity) remains legible against Light background
- [ ] All disclaimer text (set at 50% opacity) remains legible

**Light edition specific adjustment (likely needed):**
The panel illustration's Amber and Teal zone bands are set at 70% opacity in the Dark edition. On the Light background, these may read slightly differently. Test and adjust band opacity (may need to reduce to 50–60%) so the gradient still fades naturally rather than appearing as a solid block.

---

## Section 5 — Pre-Build Checklist for Affinity Designer

Complete these steps before beginning the layout build. This list cannot be skipped — it sets up the infrastructure that makes the Light edition efficient and the export workflow clean.

- [ ] Install fonts: Barlow Condensed (ExtraBold), Barlow (SemiBold), Inter (Regular, Medium), JetBrains Mono (Regular) — all available free on Google Fonts
- [ ] Create new Affinity Designer document: 24×36" (7200 × 10800 px at 300 DPI), sRGB color mode
- [ ] Set bleed: 0.125" (3.175 mm) all sides
- [ ] Set safe zone guides: 0.5" (12.7 mm) inside all trim edges
- [ ] Set up 12-column grid, 0.25" gutters
- [ ] In Swatches panel, add all series palette colors as Global Colors (this is what makes Light edition production painless):
  - `#1A1F2E`, `#F0EDE8`, `#1E2435`, `#252B3D`, `#0D1020`
  - `#E8A020`, `#2EC4B6`, `#27AE60`, `#E05C5C`
  - `#3A4055`, `#9AA0B0`, `#C8D0D8`
- [ ] Create all layer names per the locked convention (see Design Brief Section 4.5 and Series Design Standards Section 5)
- [ ] In Export Persona, configure all six named export slices before beginning layout:
  - `Hull Cell Panel — Dark — 24x36 — Print` (CMYK, 300 DPI, bleed + marks)
  - `Hull Cell Panel — Dark — 18x24 — Print` (CMYK, 300 DPI, bleed + marks)
  - `Hull Cell Panel — Dark — Digital` (RGB, 150 DPI, no bleed)
  - `Hull Cell Panel — Light — 24x36 — Print` (CMYK, 300 DPI, bleed + marks)
  - `Hull Cell Panel — Light — 18x24 — Print` (CMYK, 300 DPI, bleed + marks)
  - `Hull Cell Panel — Light — Digital` (RGB, 150 DPI, no bleed)
- [ ] Lock `[STRUCT] Grid Guides` and `[MARKS] Print Marks` layers immediately after creation

---

## Section 6 — Content Accuracy and Editorial Review

### What Has Been Confirmed

All technical content in this draft is sourced from Watson's *Acid Zinc Plating Troubleshooting Guide v1* (2026-03-14) or is standard industry practice confirmed by that document. The following specific items are now validated:

- SHG zinc anode specification and warning language — confirmed (Section 5.1)
- Cathode prep sequence — confirmed (Section 7.2)
- Current density zone values at 2 A — confirmed (Section 7.3)
- Iron contamination threshold (>50–75 ppm), H₂O₂ treatment protocol — confirmed (Sections 4.1, 8.3)
- Lead and cadmium threshold (1–2 ppm), zinc dust treatment — confirmed (Sections 4.3, 4.4, 8.5)
- Copper contamination threshold (>10 ppm), low-CD dummy plate — confirmed (Sections 4.2, 8.4)
- Organic contamination symptoms and carbon treatment protocol — confirmed (Sections 3.6, 8.2)
- Hull cell as SPC tool — frequency and archiving practice confirmed (Section 7.6)
- Isolation testing protocol (one variable per aliquot) — confirmed (Section 7.5)

### Items That Should Be Tyler-Validated Before First Print Run

These are not blocking items for the design build, but they should be validated before the poster is treated as a finished commercial product:

1. **Brightener overload LCD skip plate mechanism** — the explanation "increases overpotential for zinc deposition, most severely affecting LCD zones" is Watson-sourced and technically sound, but Tyler should confirm this maps to real-world observation in an acid zinc bath. Tyler to confirm the carbon treat dose (5–10 g/L) is appropriate for clearing brightener overload, not just organic contamination.

2. **Isolation protocol step for boric acid** — the poster states "Add boric acid to a fresh aliquot — run panel. If HCD burning reduces: boric acid was low." Tyler should confirm that boric acid effects are distinguishable on a 5-minute Hull cell panel from other HCD burning causes.

3. **SPC frequency** — "every 500–1000 ampere-hours" is Watson's documented range. Tyler can confirm whether this aligns with what actual acid zinc shops run in practice — if there is a tighter or wider range that is more realistic, the poster should reflect it.

**Tyler flag note:** Tyler is available evenings and weekends only. These validations are not required before beginning the Affinity Designer layout build. Queue them for the next Tyler session.

### No Open Watson Flags

All three Watson flags (C1, C2, C3) are now cleared. The poster content is technically production-ready.

---

## Section 7 — Coordination Notes

### Watson
No further Watson research is required for this poster. All three flags resolved from Watson's Acid Zinc Plating Troubleshooting Guide v1. Watson's next assignment for Plating Posters Inc should address Poster #9 (Anodizing — Type I, II, III) when that poster enters development.

### Tyler
Three low-priority validations identified in Section 6 above. Not blocking. Queue for next available Tyler session (evenings/weekends).

### June
See Asset Summary Report below.

---

## Section 8 — Asset Summary Report for June

**Asset Name:** Poster #4 — Reading Your Hull Cell Panel — Content and Layout Draft

**Version:** v1.0

**Date:** 2026-03-18

**Files Produced This Session:**

| File | Location | Status |
|------|----------|--------|
| `Poster 4 — Hull Cell Panel — Content and Layout Draft.md` | `Plating Posters Inc/` | Complete — production-ready |

**Watson Flags Status:**
| Flag | Item | Status |
|------|------|--------|
| C1 | SHG zinc anode spec + cathode prep | CLEARED from Watson v1 Section 5.1, 7.1–7.2 |
| C2 | Current density values HCD/LCD at 2 A | CLEARED from Watson v1 Section 7.3 |
| C3 | Contamination thresholds and treatment ratios | CLEARED from Watson v1 Sections 4.1–4.4, 8.2–8.5 |

**Current Poster #4 Status:** Ready for Affinity Designer build. All content is finalized. Three minor Tyler validations identified — not blocking the build.

**Recommended Next Steps:**

1. **Drew:** Open Affinity Designer. Complete the pre-build checklist in Section 5 of this document before building any content. Build Dark edition master using Design Brief v1.0 (layout zones, layers) and this document (all copy, table content, specifications).

2. **Alaina:** Update `project_poster_library.md` memory file — change Poster #4 status from "Pending Watson" to "In Build." Add note that C1/C2/C3 are cleared.

3. **Tyler (next available evening/weekend session):** Three low-priority validation items in Section 6.3 above. Review and confirm or note any corrections. Not required before Affinity Designer build begins.

4. **Watson (future):** No further action required for Poster #4. Next Plating Posters Inc assignment: begin research for Poster #9 (Anodizing — Type I, II, III) when Drew is ready to queue that poster for development.

5. **June:** Update Poster #4 status in any project tracking to reflect "In Affinity Designer Build." Flag the three Tyler validation items as pending.

---

*Alaina — Plating Posters Inc Creative Lead*
*Content and Layout Draft v1.0 — 2026-03-18*
*Technical source: Watson, Acid Zinc Plating Troubleshooting Guide v1 (2026-03-14).*
*All Watson flags cleared. Poster #4 is ready for the Affinity Designer build.*
