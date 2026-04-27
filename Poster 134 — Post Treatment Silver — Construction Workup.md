---
Project: Plating Posters Inc
Poster Number: 134
Title: "Post Treatment -- Silver"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Process Scope: Post-treatment for cyanide silver plating (Stage 8 of 8) -- anti-tarnish
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - SilverPlating
  - Cyanide
  - PostTreatment
  - ConstructionWorkup
  - ClusterEP13
---

# Poster #134 -- Construction Workup
## Post Treatment -- Silver

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 8 of 8. Silver tarnishes. It is the #1 post-plating failure mode. Hydrogen sulfide (H2S) and sulfur dioxide (SO2) in the atmosphere react with silver to form black silver sulfide (Ag2S). Anti-tarnish treatment is standard for almost all silver-plated parts. The choice of treatment depends on application: electrical contacts need thin chemical barriers; decorative items get lacquer; functional parts get proprietary protectors.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Anti-tarnish treatment comparison (Block B -- HERO):** Four treatment methods compared side-by-side with application guidance.
2. **Tarnish mechanism diagram (Block D):** How H2S attacks silver.
3. **Application-specific routing (Block E):** Decision tree -- electronics vs. decorative vs. functional.
4. **Lacquer and coating options (Block F):** When to lacquer and when not to.
5. **CYANIDE SAFETY badge:** Header zone (included on all cluster posters even though this stage does not involve cyanide directly).

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
  Stage 8 highlighted (Amber)
ZONE 3 -- ANTI-TARNISH COMPARISON HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- TARNISH MECHANISM (14.5"--20.5" / ~6.0")
ZONE 5 -- APPLICATION ROUTING (20.5"--26.5" / ~6.0")
ZONE 6 -- STORAGE + HANDLING (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `POST TREATMENT` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Silver Plating -- Anti-Tarnish -- Stage 8 of 8` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Silver tarnishes. That is not a defect -- it is chemistry. Anti-tarnish treatment is not optional.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".
**CYANIDE SAFETY badge:** Same spec as Poster #127.

---

### ZONE 2 -- Orientation Strip

Stage 8 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Bright silver surface vulnerable to atmospheric attack  -->  After: Protected silver ready for service`

---

### ZONE 3 -- Anti-Tarnish Comparison Hero

**Section label:** `ANTI-TARNISH TREATMENT OPTIONS` -- Y: 4.4".

**BLOCK B -- Four Treatment Panels (Y: 5.0" to 14.0")**

Four panels in a 2x2 grid:

**Panel 1 -- Chromate Dip (X: 0.5", Y: 5.0", W: 11.0", H: 4.0"):**
- Fill `#1E2435`, left accent `#E8A020`
- Title: `CHROMATE-BASED ANTI-TARNISH` Barlow SemiBold 18 pt `#E8A020`
- Parameters: `Dilute chromate solution` / `5--15 sec immersion` / `Ambient temperature`
- Effectiveness: `Good -- traditional standard`
- Limitation: `Hexavalent chromium -- RoHS restricted`
- `Used in legacy aerospace/military specs where chromate is permitted`
- Status badge: `RoHS RESTRICTED` in Coral box

**Panel 2 -- BTA Dip (X: 12.0", Y: 5.0", W: 11.5", H: 4.0"):**
- Fill `#1E2435`, left accent `#2EC4B6`
- Title: `BENZOTRIAZOLE (BTA) DIP` Barlow SemiBold 18 pt `#2EC4B6`
- Parameters: `0.1--1% BTA in water` / `30--60 sec immersion` / `Ambient`
- Effectiveness: `Moderate -- invisible organic barrier`
- Limitation: `Less durable than chromate; may need renewal`
- `RoHS-compliant. Common for electronics.`

**Panel 3 -- Proprietary Protector (X: 0.5", Y: 9.5", W: 11.0", H: 4.0"):**
- Fill `#1E2435`, left accent `#27AE60`
- Title: `PROPRIETARY SILVER PROTECTOR` Barlow SemiBold 18 pt `#27AE60`
- Parameters: `Organic polymer coating` / `Immersion or spray application` / `Per TDS`
- Effectiveness: `Good -- most common modern approach`
- Limitation: `Cost varies; must verify contact resistance for electrical parts`
- `RoHS-compliant. Recommended default for new installations.`

**Panel 4 -- Lacquer (X: 12.0", Y: 9.5", W: 11.5", H: 4.0"):**
- Fill `#1E2435`, left accent `#C8D0D8`
- Title: `CLEAR LACQUER` Barlow SemiBold 18 pt `#C8D0D8`
- Parameters: `Clear coat (spray or dip)` / `Air dry or bake` / `1--5 microns thick`
- Effectiveness: `Excellent -- complete barrier`
- Limitation: `Increases contact resistance significantly. NOT for electrical contacts.`
- `Decorative tableware, jewelry, display items.`

---

### ZONE 4 -- Tarnish Mechanism

**Section label:** `HOW SILVER TARNISHES` -- Y: 14.7".

**BLOCK D -- Mechanism Panel (Y: 15.3" to 20.3")**

**Left -- Chemical Reaction (X: 0.5", W: 11.0"):**
- Rounded rect, H: 4.5", fill `#1E2435`, left accent `#E05C5C`
- Title: `THE REACTION` Barlow SemiBold 18 pt `#E05C5C`
- `2 Ag + H2S --> Ag2S + H2` JetBrains Mono 18 pt `#E05C5C`
- `Silver sulfide (Ag2S) is BLACK`
- `H2S sources: industrial atmosphere, rubber (vulcanized), eggs, human skin oils, sulfur-containing packaging`
- `SO2 also attacks silver in humid conditions`
- `Rate accelerated by: humidity, heat, and UV light`

**Right -- Prevention Strategy (X: 12.0", W: 11.5"):**
- Rounded rect, H: 4.5", fill `#1E2435`, left accent `#27AE60`
- Title: `PREVENTION STRATEGY` Barlow SemiBold 18 pt `#27AE60`
- Bullet list:
```
1. Anti-tarnish chemical treatment (always)
2. Store in sulfur-free packaging
3. Avoid rubber bands, cardboard with sulfur
4. Desiccant packs reduce humidity
5. Anti-tarnish paper wraps (intercept technology)
6. Controlled atmosphere storage for long-term
```

---

### ZONE 5 -- Application Routing

**Section label:** `CHOOSE BY APPLICATION` -- Y: 20.7".

**BLOCK E -- Three-Column Decision Guide (Y: 21.3" to 26.3")**

| Application | Treatment | Why |
|---|---|---|
| **Electrical Contacts / RF** | BTA or thin proprietary | Contact resistance must stay low; no lacquer |
| **Connectors / Terminals** | BTA or proprietary | Balance between tarnish protection and electrical function |
| **Decorative (Tableware)** | Lacquer | Maximum protection; appearance is primary concern |
| **Aerospace Fasteners** | Per spec (often chromate) | Anti-galling is primary purpose of silver; tarnish is secondary |
| **Waveguides / Microwave** | Matte silver + thin protector | Maximum conductivity; no brightener co-deposits |
| **General Industrial** | Proprietary protector | Best balance of cost, protection, and compliance |

Standard table. "Treatment" column in `#27AE60`. "Application" column in Barlow SemiBold.

**Note for electrical contacts:** `Anti-tarnish treatment must NOT significantly increase contact resistance. Verify with a milliohm meter before and after treatment. Maximum acceptable increase: per customer specification.` Inter Medium 13 pt `#E8A020`

---

### ZONE 6 -- Storage and Handling

**Section label:** `STORAGE AND HANDLING` -- Y: 26.7".

**BLOCK F -- Four Cards (Y: 27.3" to 32.3")**

| Card | Topic | Detail |
|---|---|---|
| 1 | PACKAGING | Sulfur-free bags or anti-tarnish paper. NEVER use rubber bands. Avoid uncoated cardboard. |
| 2 | ENVIRONMENT | <60% RH ideal. Avoid proximity to rubber, eggs, or sulfur-bearing chemicals. |
| 3 | HANDLING | Cotton or nitrile gloves only. Skin oils accelerate tarnish. Fingerprints are permanent under tarnish film. |
| 4 | INSPECTION | Visual check for tarnish before shipment. Any yellow/brown haze = tarnish beginning. Re-treat or reject. |

Cards use Amber accent `#E8A020` (informational, not error).

---

### ZONE 7 -- Footer

Standard. Title: `Post Treatment -- Silver`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Post Treatment Silver -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Tarnish is silver's nemesis and the most common customer complaint. The four treatment options are the hero -- operators need to know which treatment matches which application. The chromate option carries a RoHS badge because shops must understand the regulatory landscape. The packaging/handling zone is practical and immediately actionable. Silver-plated parts stored improperly will tarnish regardless of how well the anti-tarnish treatment was applied.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #134 -- Construction Workup v1.0*
*2026-04-26*
