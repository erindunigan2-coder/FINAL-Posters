# Plating Posters Inc

The largest educational poster library for the metal finishing industry. **721 unique posters** (English) across 9 major process categories — with Spanish editions planned to double that total. Each poster is a boardroom-quality technical reference designed for plating shops, labs, and training programs.

## Scope

| Category | Clusters | Posters | Poster Range |
|---|---|---|---|
| Electroplating | 15 | 112 | 39-150 |
| Conversion Coating | 8 | 64 | 151-214 |
| Electroless Plating | 8 | 64 | 215-278 |
| Anodizing | 8 | 64 | 279-342 |
| Chemical Treatment | 8 | 56 | 343-398 |
| Specialty & Advanced | 8 | 80 | 399-478 |
| Thermal Spray | 8 | 80 | 479-558 |
| Diffusion & Heat Treatment | 10 | 90 | 559-648 |
| Painting & Coating | 8 | 73 | 649-721 |
| Series 1 (Conceptual) | — | 38 | 1-38 |
| **Total** | **81** | **721** | |

Each cluster covers one plating/coating process end-to-end — from cleaning and activation through plating, rinsing, and post-treatment. Every poster in a cluster is a standalone reference for that specific stage.

## Repository Structure

```
/                           Root — Construction Workups (CW) and Generation Prompts (GP)
/Claude Design Output/      Design system spec + rendered HTML posters
/Research Briefs/           Watson technical research briefs (source data for all posters)
/Additional Poster Ideas/   Category-level poster idea lists
/Archive/                   Superseded versions
```

## File Types

- **Construction Workup (CW):** Content planning document specifying poster layout, zone content, typography, technical data, and visual element descriptions. One per poster. This is the blueprint.
- **Generation Prompt (GP):** Engineered Claude prompt that transforms a CW into the final HTML poster artifact. One per poster.
- **Research Brief:** Technical reference document per process category, sourced from industry literature (Metal Finishing Guidebook, ASTM standards, NASF/AES publications, supplier TDS). 12 briefs covering all 9 categories.
- **HTML Poster:** The final rendered poster output — self-contained HTML with print CSS.

## Design System

The canonical design spec is at:
`Claude Design Output/Plating Posters - Series Design Prompt.md`

All posters use:
- **Format:** HTML output, iOS 18 Liquid Glass aesthetic, 6-zone layout, print CSS
- **Palette:** Gunmetal Dark `#1A1F2E`, Amber `#E8A020`, Teal `#2EC4B6`, Emerald `#27AE60`, Coral `#E05C5C`
- **Typography:** Barlow Condensed ExtraBold (headers) / Inter (body) / JetBrains Mono (data)
- **Editions:** Dark (flagship) + Light (accessible print)
- **Sizes:** 24x36" (print), 18x24" (compact), Digital

## Building Posters

To generate an HTML poster from this repo:
1. Read the **Construction Workup** for the poster number
2. Read the **Generation Prompt** for the poster number
3. Read the **Series Design Prompt** from `Claude Design Output/`
4. Feed the Generation Prompt to Claude — it produces the final HTML artifact

## Pipeline

```
Watson (research) --> Tyler (validation) --> Alaina (CW) --> Elara (GP) --> Claude Design (HTML)
```

## Current Status

- **Construction Workups:** 642 / 721 (79 in progress)
- **Generation Prompts:** 38 / 721
- **Rendered HTML:** 7 (Posters 24-30)
- **Research Briefs:** 12 / 12 (complete)
- **Tyler Validation:** 19+ clusters verified

---

*Plating Posters Inc — Drew Adkins*
*Educational posters for the metal finishing industry*
*2026*
