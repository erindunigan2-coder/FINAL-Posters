---
Project: Plating Posters Inc
Document Type: Template — Reusable Production Checklist
Status: Active
Created: 2026-04-03T00:00:00
Author: Alaina (poster-designer)
tags:
  - PosterDesign
  - PlatingPosters
  - Template
  - Checklist
---

# Poster Production Checklist Template

*Copy this checklist into each new poster's working notes when it enters development. Check off each step as it completes. This template captures the full production pipeline established through Posters #4 and #10.*

*Maintained by Alaina — established 2026-04-03.*

---

## How to Use This Template

1. When a new poster is selected for development, copy everything below the "---" line into a new file named: `Poster [#] — [Short Title] — Production Checklist.md`
2. Fill in the poster-specific metadata at the top
3. Work through each stage in order — do not skip ahead
4. Check off each item as it completes; note the date and any blockers
5. Quality gates are marked with a double-check (the step cannot proceed until the gate clears)

---

## Poster Metadata

| Field | Value |
|-------|-------|
| Poster Number | # |
| Working Title | |
| Process Scope | (one process only) |
| Watson Research Brief Required | Yes / No |
| Tyler Validation Required | Yes / No (flag specific items) |
| Date Entered Development | |
| Target Elara Generation Prompt Date | |

---

## Stage 1 — Research and Technical Input

- [ ] **Watson Research Brief received** — file at `Research Briefs/[title].md`
  - Date received: ___
  - Brief version: ___
  - Open Watson flags: ___
- [ ] Drew's Quick Reference Notes consulted for baseline field knowledge
- [ ] Watson troubleshooting guide consulted (if relevant process guide exists in `Knowledge Notes/Troubleshooting/`)
- [ ] All Watson flags resolved — no unconfirmed data remains
  - Flag clearance details documented in Content and Layout Draft, Section 1

**Quality Gate:** All technical data confirmed before proceeding to Stage 2. If Watson flags remain open, do not draft poster content using unconfirmed values — hold or use placeholder language and flag clearly.

*Note: Some posters may not require a Watson Research Brief (e.g., Poster #13 Barrel vs. Rack, Poster #14 Safety). If no brief is needed, note "N/A — chemistry-light poster" and proceed to Stage 2 with vault knowledge sources cited.*

---

## Stage 2 — Content and Layout Draft (Alaina)

- [ ] **Content and Layout Draft produced** — file at `Poster [#] — [Title] — Content and Layout Draft.md`
  - Version: ___
  - Date: ___
- [ ] All poster copy finalized — headlines, subheadings, body text, callout text, table data, diagram labels, footer content
- [ ] Zone map created — all zones defined with approximate height percentages and inch dimensions
- [ ] Every content block specified — font, size, weight, color (Dark and Light hex), position
- [ ] Illustration specifications included — shape descriptions, color fills, build approach
- [ ] Watson flag clearance section complete (Section 1)
- [ ] Design decisions documented with rationale (Section 1)
- [ ] Light edition color remap considerations noted for any non-standard elements
- [ ] Footer content matches series standard — title, series name, disclaimer, logo placeholder, version
- [ ] Disclaimer text appropriate for poster topic

**Quality Gate:** Content and Layout Draft must be internally complete before proceeding. All text on the poster must exist in this document. No "TBD" or placeholder copy in data rows or callout boxes.

### Tyler Validation Checkpoint (if applicable)

- [ ] Tyler validation items identified and flagged
  - Items: ___
- [ ] Tyler session scheduled (evenings/weekends only)
- [ ] Tyler validation received
  - Date: ___
  - Changes required: ___
- [ ] Content and Layout Draft updated with Tyler's input (if any)

*Note: Tyler validation is a checkpoint, not a blocker for the Content and Layout Draft. The draft can proceed in parallel — Tyler's feedback is integrated before the Construction Workup is finalized. For most posters, Tyler validation covers process step accuracy and real-world practicality, not foundational chemistry (that is Watson's domain).*

---

## Stage 3 — Construction Workup (Alaina)

- [ ] **Construction Workup produced** — file at `Poster [#] — [Title] — Construction Workup.md`
  - Version: ___
  - Date: ___
- [ ] Part 1 — Workflow Orientation: capabilities and limitations documented for this poster
- [ ] Part 2 — Document Setup Instructions: page size, background color, font uploads, brand colors, ruler guides
- [ ] Part 3 — Layout Zones and Build Order: complete zone map with inch dimensions
- [ ] Part 4 — Zone-by-Zone Build Specifications: every block fully specified
  - Every text element: font, size, weight, color hex, position, exact copy (verbatim from Content and Layout Draft)
  - Every shape element: type, dimensions, fill color, border/stroke, corner radius, position
  - Every illustration: shape-by-shape construction instructions
- [ ] Part 5 (or 6) — Light Edition Remap Table: complete Dark-to-Light color mapping with any poster-specific overrides noted
- [ ] All copy cross-checked against Content and Layout Draft — verbatim match confirmed
- [ ] Tool limitations documented with workarounds for each

**Quality Gate:** The Construction Workup must contain enough detail that Elara can engineer a generation prompt without referring back to the Content and Layout Draft for any visual specification. Content authority remains with the Draft; visual/build authority lives in the Workup.

---

## Stage 4 — Generation Prompt (Elara)

- [ ] **Generation Prompt engineered by Elara** — file at `Poster [#] — [Title] — Generation Prompt.md`
  - Date: ___
- [ ] Prompt translates Workup into Claude Chat generation instructions
- [ ] All design specifications correct (colors, fonts, sizes, layout)
- [ ] Prompt reviewed against Workup for completeness

---

## Stage 5 — Claude Chat Generation (Drew)

- [ ] Drew generates the 24x36" Dark edition in Claude Chat (SVG/HTML artifact)
- [ ] All fonts specified (Barlow Condensed, Barlow, Inter, JetBrains Mono)
- [ ] All series colors applied
- [ ] Dark edition generation complete — all zones, all blocks
- [ ] Visual review by Drew — does it look right at full zoom?

---

## Stage 6 — Light Edition (Drew)

- [ ] Dark edition design duplicated
- [ ] Color remap completed per remap table in Workup
- [ ] All accent-fill headers checked for WCAG contrast compliance
- [ ] Light edition complete — no Dark-edition colors remaining

---

## Stage 7 — Review and Revision

- [ ] Alaina reviews both editions against Series Design Standards
  - Typography: correct fonts, sizes, weights?
  - Colors: correct hex values, remap accurate?
  - Layout: zones match spec, no elements drifting?
  - Content: all text matches Content and Layout Draft verbatim?
  - Accessibility: contrast ratios verified, no color-only information?
- [ ] Drew reviews for visual quality at simulated wall distance
- [ ] Revision notes compiled (if any)
- [ ] Revisions completed
- [ ] Final review sign-off

---

## Stage 8 — Export

- [ ] Six files exported per Series Design Standards Section 6:
  - [ ] `[Title] — Dark — 24x36 — Print.pdf` (PDF Print, crop marks + bleed)
  - [ ] `[Title] — Dark — 18x24 — Print.pdf` (PDF Print, crop marks + bleed)
  - [ ] `[Title] — Dark — Digital.pdf` (PDF Standard, no marks)
  - [ ] `[Title] — Light — 24x36 — Print.pdf` (PDF Print, crop marks + bleed)
  - [ ] `[Title] — Light — 18x24 — Print.pdf` (PDF Print, crop marks + bleed)
  - [ ] `[Title] — Light — Digital.pdf` (PDF Standard, no marks)
- [ ] 18x24" versions verified: all text meets 14 pt minimum floor
- [ ] File names follow naming convention exactly

---

## Stage 9 — Final Validation and Library Update

- [ ] Both editions validated against full Series Design Standards checklist
- [ ] Master note updated (`Plating Posters Inc/Plating Posters Inc.md`) — poster moved from "In Development" to "Completed"
- [ ] Starter Poster List updated with final status
- [ ] Poster Library memory file updated
- [ ] Asset Summary Report prepared for June

---

## Completion Record

| Field | Value |
|-------|-------|
| Date Completed | |
| Final Version | |
| Generated Artifact Location | |
| Export Files Location | |
| Total Production Time (calendar days) | |
| Notes | |
