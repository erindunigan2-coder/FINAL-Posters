#!/usr/bin/env python3
"""Build 8 Anodizing Demystified posters x 4 variants = 32 files."""

import os

OUT = os.path.dirname(os.path.abspath(__file__))

# -- CSS (shared across all posters) -----------------------------------------
CSS = r""":root {
  --bg:#1A1F2E;--navy:#0D1020;--text:#F0EDE8;--muted:rgba(240,237,232,.62);
  --faint:rgba(240,237,232,.38);
  --amber:#E8A020;--teal:#2EC4B6;--emerald:#27AE60;--coral:#E05C5C;
  --slate:#3A4055;--callout:#1E2435;--altrow:#252B3D;
  --glass-bg:rgba(30,36,53,.55);--glass-border:rgba(255,255,255,.12);
  --glass-shadow:inset 0 1px 0 rgba(255,255,255,.14),inset 0 -1px 0 rgba(0,0,0,.2),0 4px 12px rgba(0,0,0,.25);
}
.poster[data-edition="light"]{
  --bg:#F5F4F0;--navy:#DDD8CE;--text:#1B2030;--muted:rgba(27,32,48,.66);
  --faint:rgba(27,32,48,.42);
  --amber:#B8770D;--teal:#1A8C82;--emerald:#1E8449;--coral:#B7322F;
  --slate:#C5C0B5;--callout:#ECEAE1;--altrow:#E4E1D6;
  --glass-bg:rgba(255,253,247,.66);--glass-border:rgba(27,32,48,.10);
  --glass-shadow:inset 0 1px 0 rgba(255,255,255,.6),0 4px 12px rgba(27,32,48,.08);
}
html,body{margin:0;padding:0;background:#0a0c14;}
.stage{width:100vw;min-height:100vh;display:flex;align-items:flex-start;justify-content:center;overflow:visible;padding:12px 0;box-sizing:border-box;}
.poster-wrap{transform-origin:center center;}
.poster{width:1200px;height:1800px;position:relative;overflow:hidden;background:radial-gradient(1200px 800px at 15% 8%,rgba(46,196,182,.14),transparent 60%),radial-gradient(1000px 700px at 90% 25%,rgba(232,160,32,.12),transparent 55%),radial-gradient(900px 900px at 50% 80%,rgba(224,92,92,.10),transparent 60%),var(--bg);font-family:'Inter',sans-serif;color:var(--text);display:flex;flex-direction:column;padding:28px;box-sizing:border-box;}
.poster::before{content:'';position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.025) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.025) 1px,transparent 1px);background-size:50px 50px;mask-image:radial-gradient(ellipse 80% 80% at 50% 50%,black 40%,transparent 100%);-webkit-mask-image:radial-gradient(ellipse 80% 80% at 50% 50%,black 40%,transparent 100%);pointer-events:none;z-index:0;}
.poster>*{position:relative;z-index:1;}
.glass{background-color:var(--glass-bg);background-image:linear-gradient(145deg,rgba(255,255,255,.055),rgba(255,255,255,.015));border:1px solid var(--glass-border);backdrop-filter:blur(18px) saturate(140%);-webkit-backdrop-filter:blur(18px) saturate(140%);box-shadow:var(--glass-shadow);border-radius:12px;}
.tack{position:absolute;width:24px;height:24px;border-radius:50%;border:1.5px solid rgba(232,160,32,.28);z-index:2;pointer-events:none;}.tack::before,.tack::after{content:"";position:absolute;background:rgba(232,160,32,.28);}.tack::before{left:50%;top:-3px;bottom:-3px;width:1px;transform:translateX(-50%);}.tack::after{top:50%;left:-3px;right:-3px;height:1px;transform:translateY(-50%);}.tack.tl{top:12px;left:12px;}.tack.tr{top:12px;right:12px;}.tack.bl{bottom:12px;left:12px;}.tack.br{bottom:12px;right:12px;}
.poster-header{flex-shrink:0;}.poster-body{flex:1;overflow:hidden;display:flex;flex-direction:column;gap:4px;justify-content:space-between;}.poster-footer{flex-shrink:0;margin-top:4px;}
.header-band{display:flex;align-items:flex-start;justify-content:space-between;gap:16px;margin-bottom:4px;}.header-left{flex:1;min-width:0;}.eyebrow{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--amber);letter-spacing:.16em;text-transform:uppercase;margin-bottom:4px;display:flex;align-items:center;gap:12px;}.eyebrow::before{content:"";display:inline-block;width:30px;height:3px;background:var(--amber);}.headline{font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:58px;color:var(--text);line-height:.92;margin:4px 0;letter-spacing:-.01em;text-transform:uppercase;}.headline em{font-style:normal;color:var(--amber);}.subhead{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:19px;color:var(--teal);margin:0 0 3px;letter-spacing:.02em;text-transform:uppercase;}.tagline{font-family:'Inter',sans-serif;font-style:italic;font-size:13px;color:var(--muted);line-height:1.45;max-width:700px;margin:0;}
.logo-card{flex-shrink:0;padding:12px 10px;display:flex;flex-direction:column;align-items:center;gap:8px;align-self:flex-start;}.logo-tile{width:68px;height:68px;border-radius:12px;background:linear-gradient(135deg,#E8A020,#2EC4B6);display:flex;align-items:center;justify-content:center;box-shadow:inset 0 1px 0 rgba(255,255,255,.4),inset 0 -2px 4px rgba(0,0,0,.15),0 4px 14px rgba(0,0,0,.35);}.logo-tile span{font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:26px;color:#1A1F2E;letter-spacing:.02em;line-height:1;}.logo-word{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:18px;letter-spacing:.04em;text-transform:uppercase;line-height:1;text-align:center;white-space:nowrap;}.logo-word .a{color:var(--text);}.logo-word .b{color:var(--amber);}.logo-inc{font-family:'JetBrains Mono',monospace;font-size:8.5px;letter-spacing:.05em;text-transform:lowercase;color:var(--muted);margin-top:-2px;}
.section-title{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:24px;letter-spacing:.08em;text-transform:uppercase;color:var(--text);margin:0 0 3px;display:flex;align-items:center;gap:8px;}.section-title::before{content:"";width:6px;height:6px;background:var(--amber);border-radius:50%;}.section-title .sub{font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.14em;color:var(--muted);margin-left:auto;font-weight:500;}
.rule-card{display:flex;align-items:center;gap:16px;padding:8px 18px;background:rgba(232,160,32,.07);}.rule-num{font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:44px;color:var(--amber);line-height:1;letter-spacing:-.02em;}.rule-body{flex:1;}.rule-label{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:19px;color:var(--amber);letter-spacing:.08em;text-transform:uppercase;}.rule-text{font-family:'Inter',sans-serif;font-size:12.5px;color:var(--muted);line-height:1.5;margin-top:4px;}
.data-table{width:100%;border-collapse:collapse;}.data-table th{font-family:'Barlow',sans-serif;font-weight:700;font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--amber);padding:6px 10px;text-align:left;background:rgba(13,16,32,.35);border-bottom:1px solid var(--glass-border);}.poster[data-edition="light"] .data-table th{background:rgba(27,32,48,.06);}.data-table td{padding:6px 10px;color:var(--text);line-height:1.5;border-bottom:1px solid rgba(255,255,255,.05);font-family:'Inter',sans-serif;font-size:14px;}.data-table tr:last-child td{border-bottom:none;}.data-table tr:nth-child(even) td{background:rgba(255,255,255,.02);}.poster[data-edition="light"] .data-table tr:nth-child(even) td{background:rgba(27,32,48,.025);}.data-table .mono{font-family:'JetBrains Mono',monospace;font-size:13px;}.data-table.compact th{font-size:11px;padding:5px 9px;}.data-table.compact td{padding:4px 9px;font-size:12px;line-height:1.45;}.data-table.compact .mono{font-size:12.5px;}.data-table.bath th{font-size:12px;padding:7px 10px;}.data-table.bath td{padding:6px 10px;font-size:13px;line-height:1.4;}.data-table.bath .mono{font-size:12px;}
.bottom-grid .data-table.bath td{padding:6px 10px;}.bottom-grid .data-table.bath th{padding:7px 10px;}
.compare-grid{display:grid;grid-template-columns:1fr 1fr;gap:6px;}.compare-card{padding:10px 16px;}.compare-card h4{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:18px;color:var(--text);margin:0 0 8px;text-transform:uppercase;letter-spacing:.04em;}.compare-card h4 .tag{font-size:12px;padding:2px 8px;border-radius:4px;margin-left:8px;font-family:'JetBrains Mono',monospace;font-weight:500;letter-spacing:.06em;}.compare-card h4 .tag.good{background:rgba(39,174,96,.15);color:var(--emerald);}.compare-card h4 .tag.bad{background:rgba(224,92,92,.15);color:var(--coral);}.compare-card ul{list-style:none;padding:0;margin:0;}.compare-card li{font-size:12.5px;line-height:1.5;padding:2px 0;display:flex;gap:8px;align-items:flex-start;}.compare-card li::before{content:"";width:5px;height:5px;border-radius:50%;margin-top:7px;flex-shrink:0;}.compare-card.do li::before{background:var(--emerald);}.compare-card.dont li::before{background:var(--coral);}
.bottom-grid{display:grid;grid-template-columns:1.6fr 1fr;gap:8px;}
.insight-card{padding:10px 16px;border-left:3px solid var(--teal);background:rgba(46,196,182,.06);border-radius:0 12px 12px 0;}.insight-label{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:16px;color:var(--teal);letter-spacing:.08em;text-transform:uppercase;margin-bottom:3px;}.insight-text{font-family:'Inter',sans-serif;font-size:13px;color:var(--text);line-height:1.5;}
.safety-card{padding:12px 18px;background:rgba(224,92,92,.08);border:1px solid rgba(224,92,92,.25);border-radius:12px;}.safety-head{font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:20px;color:var(--coral);letter-spacing:.06em;text-transform:uppercase;margin-bottom:5px;}.safety-body{font-size:14px;color:var(--text);line-height:1.55;}.safety-body strong{font-weight:700;color:var(--coral);}
.footer{padding:10px 20px;background-color:rgba(13,16,32,.85);background-image:linear-gradient(180deg,rgba(255,255,255,.04),rgba(0,0,0,0));border:1px solid rgba(255,255,255,.10);border-radius:8px;text-align:center;display:flex;flex-direction:column;gap:2px;}.poster[data-edition="light"] .footer{background-color:rgba(221,216,206,.95);border-color:rgba(27,32,48,.10);}.footer-disclaimer{font-family:'Inter',sans-serif;font-size:9px;line-height:1.35;color:var(--faint);margin:0 auto;max-width:900px;}.footer-title{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:13px;color:var(--text);letter-spacing:.04em;text-transform:uppercase;margin:0;}.footer-brand{font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--muted);letter-spacing:.12em;text-transform:uppercase;}
.tweaks{position:fixed;bottom:16px;right:16px;z-index:100;background:rgba(13,16,32,.92);border:1px solid rgba(255,255,255,.12);border-radius:10px;padding:10px 14px;display:flex;flex-direction:column;gap:8px;font-family:'Inter',sans-serif;font-size:12px;color:#F0EDE8;}
@media print{@page{size:12.5in 18.75in;margin:0;}html,body{background:#1A1F2E !important;-webkit-print-color-adjust:exact !important;print-color-adjust:exact !important;}*{-webkit-print-color-adjust:exact !important;print-color-adjust:exact !important;}.stage{position:static;padding:0;display:block;overflow:visible;}.poster-wrap{transform:none !important;width:auto !important;height:auto !important;}.poster{box-shadow:none !important;width:1200px !important;height:1800px !important;overflow:hidden !important;}.glass,.insight-card,.safety-card{backdrop-filter:none !important;-webkit-backdrop-filter:none !important;}.tweaks{display:none !important;}}"""

JS = r"""const posterWrap=document.getElementById('posterWrap');const poster=document.getElementById('poster');
function scalePoster(){const sW=(window.innerWidth-24)/1200;const sH=(window.innerHeight-24)/1800;const s=Math.min(sW,sH);posterWrap.style.transform='scale('+s+')';posterWrap.style.transformOrigin='top center';posterWrap.style.width='1200px';posterWrap.style.height=(1800*s)+'px';}
function setEdition(e){if(e)poster.dataset.edition=e;else delete poster.dataset.edition;['Dark','Light'].forEach(function(n){var b=document.getElementById('btn'+n);var active=(n.toLowerCase()===e)||(n==='Dark'&&!e);b.style.background=active?'#E8A020':'transparent';b.style.color=active?'#1A1F2E':'#F0EDE8';b.style.borderColor=active?'#E8A020':'rgba(255,255,255,.2)';})}
scalePoster();window.addEventListener('resize',scalePoster);"""


# -- POSTER DEFINITIONS -------------------------------------------------------

POSTERS = {
    # ======================================================================
    # 1. SULFURIC ACID ANODIZING (TYPE II)
    # ======================================================================
    "type_ii": {
        "prefix": "Type II",
        "footer_code": "PP-TypeII-00-T",
        "en": {
            "eyebrow": "Plating Posters &middot; Anodizing &middot; Sulfuric Acid Type II &middot; Overview",
            "headline": "SULFURIC ACID<br><em>ANODIZING</em>",
            "subhead": "Type II &mdash; The Workhorse of Aluminum Surface Finishing",
            "tagline": "The most widely used anodizing process worldwide &mdash; sulfuric acid Type II builds a porous alumina oxide layer that accepts dyes, resists corrosion, and provides moderate wear protection on virtually any aluminum alloy.",
            "rule_num": "5&ndash;25",
            "rule_label": "Typical Oxide Thickness (&micro;m) &mdash; Sulfuric Acid Type II Anodize",
            "rule_text": "Type II sulfuric acid anodizing converts the aluminum surface into a hard, porous aluminum oxide (Al&#8322;O&#8323;) layer 5&ndash;25 &micro;m thick. The regular pore structure readily absorbs organic and inorganic dyes before sealing locks in color and corrosion resistance for decades of service.",
            "process_title": "Typical Process Sequence <span class=\"sub\">rack line</span>",
            "process_rows": [
                ("01", "Alkaline Clean / Degrease", "130&ndash;160&deg;F", "3&ndash;5 min", "Remove oils, fingerprints, shop soils"),
                ("02", "Rinse", "Ambient", "30&ndash;60 s", "Overflow; prevent alkaline drag-in"),
                ("03", "Alkaline Etch (optional)", "130&ndash;150&deg;F", "1&ndash;5 min", "NaOH 40&ndash;60 g/L &mdash; matte finish"),
                ("04", "Rinse", "Ambient", "30&ndash;60 s", "Remove etch residue"),
                ("05", "Desmut / Deoxidize", "Ambient", "1&ndash;3 min", "HNO&#8323; + HF or proprietary &mdash; remove smut"),
                ("06", "Rinse", "Ambient", "30&ndash;60 s", "Prevent acid drag-in to anodize tank"),
                ("07", "Sulfuric Acid Anodize", "68&ndash;72&deg;F", "20&ndash;60 min", "15&ndash;18% H&#8322;SO&#8324;; 12&ndash;18 ASF"),
                ("08", "Rinse", "Ambient", "1&ndash;2 min", "Multi-stage counterflow rinse"),
                ("09", "Dye (optional)", "130&ndash;140&deg;F", "5&ndash;15 min", "Organic or inorganic dye immersion"),
                ("10", "Seal", "200&ndash;210&deg;F", "15&ndash;30 min", "Hot DI water, nickel acetate, or mid-temp"),
            ],
            "insight_label": "Why Type II Anodizing Is the Industry Standard",
            "insight_text": "Sulfuric acid anodizing dominates because it strikes the ideal balance of cost, performance, and versatility. The porous oxide layer grows at roughly 1 &micro;m per 3 minutes under standard conditions, giving operators precise thickness control. Approximately two-thirds of the coating grows into the substrate and one-third builds outward, so dimensional change is modest. The hexagonal pore structure is ideal for dye absorption, and sealing in hot water or nickel acetate hydrates the alumina to close pores permanently. A properly sealed Type II coating passes 336+ hours of salt spray and resists UV fading for decades outdoors.",
            "svg": """<svg viewBox="0 0 1060 80" width="100%" height="65" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="10" y="8" width="95" height="38" rx="7" fill="rgba(46,196,182,.10)" stroke="var(--teal)" stroke-width="1.5"/>
    <text x="57" y="24" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">CLEAN</text>
    <text x="57" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">Alk Degrease</text>
    <line x1="109" y1="27" x2="133" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="133,24 139,27 133,30" fill="currentColor" opacity=".3"/>
    <rect x="143" y="8" width="80" height="38" rx="7" fill="rgba(224,92,92,.10)" stroke="var(--coral)" stroke-width="1.2"/>
    <text x="183" y="24" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">ETCH</text>
    <text x="183" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">NaOH Matte</text>
    <line x1="227" y1="27" x2="251" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="251,24 257,27 251,30" fill="currentColor" opacity=".3"/>
    <rect x="261" y="8" width="95" height="38" rx="7" fill="rgba(120,120,140,.08)" stroke="var(--muted)" stroke-width="1"/>
    <text x="308" y="24" text-anchor="middle" fill="var(--muted)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">DESMUT</text>
    <text x="308" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">HNO&#8323; Deox</text>
    <line x1="360" y1="27" x2="384" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="384,24 390,27 384,30" fill="currentColor" opacity=".3"/>
    <rect x="394" y="4" width="160" height="46" rx="8" fill="rgba(232,160,32,.12)" stroke="var(--amber)" stroke-width="2"/>
    <text x="474" y="22" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="13">TYPE II ANODIZE</text>
    <text x="474" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8.5" opacity=".6">H&#8322;SO&#8324; 15&ndash;18% &bull; 68&ndash;72&deg;F</text>
    <text x="474" y="70" text-anchor="middle" fill="var(--amber)" font-family="JetBrains Mono,monospace" font-size="8" opacity=".7">KEY STAGE</text>
    <line x1="558" y1="27" x2="582" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="582,24 588,27 582,30" fill="currentColor" opacity=".3"/>
    <rect x="592" y="8" width="80" height="38" rx="7" fill="rgba(39,174,96,.10)" stroke="var(--emerald)" stroke-width="1.2"/>
    <text x="632" y="24" text-anchor="middle" fill="var(--emerald)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">DYE</text>
    <text x="632" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">Color Immerse</text>
    <line x1="676" y1="27" x2="700" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="700,24 706,27 700,30" fill="currentColor" opacity=".3"/>
    <rect x="710" y="8" width="115" height="38" rx="7" fill="rgba(232,160,32,.08)" stroke="var(--amber)" stroke-width="1" stroke-dasharray="5,3"/>
    <text x="767" y="24" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">SEAL</text>
    <text x="767" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">Hot DI / NiAc</text>
    <line x1="10" y1="58" x2="830" y2="58" stroke="currentColor" stroke-width="1.5" opacity=".12" stroke-dasharray="8,4"/>
    <text x="855" y="62" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" opacity=".35" letter-spacing=".06em">LINE</text>
</svg>""",
            "svg_title": "Type II Anodize Process Flow <span class=\"sub\">rack line</span>",
            "app_title": "Application Guide <span class=\"sub\">by alloy series</span>",
            "app_headers": ("Alloy Series", "Typical Use", "Oxide Quality", "Dye Uptake"),
            "app_rows": [
                ("1xxx / 5xxx", "Architectural, marine", "Excellent &mdash; clear, dense", "Excellent"),
                ("6xxx (6061/6063)", "Structural, extrusion", "Very good &mdash; slight haze", "Very good"),
                ("2xxx (2024)", "Aerospace", "Fair &mdash; Cu causes color", "Moderate"),
                ("7xxx (7075)", "Aerospace, high-strength", "Fair &mdash; Zn affects clarity", "Moderate"),
            ],
            "dyk_text": "The pore structure of Type II anodic oxide is remarkably regular &mdash; a self-organizing hexagonal array with pore diameters of <strong style=\"color:var(--amber);\">10&ndash;30 nm</strong>. Each pore sits at the center of a hexagonal cell roughly 50&ndash;100 nm across. This nano-architecture is so uniform that anodic alumina is actually used as a <strong style=\"color:var(--amber);\">template for nanotechnology</strong> research &mdash; scientists use it to grow nanowires, nanotubes, and quantum dots. The same structure that makes Type II coatings excellent at absorbing dye molecules also makes them scientifically fascinating.",
            "bath_title": "Bath Chemistry <span class=\"sub\">sulfuric acid</span>",
            "bath_rows": [
                ("Sulfuric Acid", "15&ndash;18 wt%"),
                ("Dissolved Al", "&lt;20 g/L"),
                ("Temperature", "68&ndash;72&deg;F"),
                ("Voltage", "14&ndash;18 V"),
                ("Current Density", "12&ndash;18 ASF"),
                ("Agitation", "Air or mech."),
            ],
            "spec_title": "Specifications <span class=\"sub\">common</span>",
            "spec_rows": [
                ("MIL-A-8625 Type II", "Sulfuric anodize"),
                ("AMS 2471", "Type II anodize"),
                ("ASTM B580", "Anodic coatings"),
                ("ISO 7599", "Al anodizing"),
            ],
            "compare_title": "Type II vs Type III <span class=\"sub\">when to choose each</span>",
            "do_title": "Type II <span class=\"tag good\">Choose When</span>",
            "do_items": [
                "Corrosion resistance is the primary goal",
                "Color dyeing or decorative finish needed",
                "Tight tolerances (less dimensional growth)",
                "Cost-effective, high-throughput production",
                "Wide range of alloys acceptable",
            ],
            "dont_title": "Type III <span class=\"tag bad\">Choose Instead</span>",
            "dont_items": [
                "Maximum wear and abrasion resistance",
                "Thicker coatings needed (&gt;25 &micro;m)",
                "High hardness required (60&ndash;70 Rc equiv.)",
                "Electrical insulation properties needed",
                "Operating temp above 350&deg;F",
            ],
            "footer_title": "Sulfuric Acid Anodizing (Type II) Demystified &mdash; Anodizing Series",
            "footer_disclaimer": "Technical reference only. Verify all parameters against your chemistry supplier&rsquo;s TDS, customer specifications, and applicable regulatory requirements before production use.",
        },
        "es": {
            "eyebrow": "Plating Posters &middot; Anodizado &middot; &Aacute;cido Sulf&uacute;rico Tipo II &middot; Descripci&oacute;n",
            "headline": "&Aacute;CIDO SULF&Uacute;RICO<br><em>ANODIZADO</em>",
            "subhead": "Tipo II &mdash; El Caballo de Batalla del Acabado de Aluminio",
            "tagline": "El proceso de anodizado m&aacute;s utilizado en el mundo &mdash; el &aacute;cido sulf&uacute;rico Tipo II genera una capa porosa de al&uacute;mina que acepta tintes, resiste la corrosi&oacute;n y proporciona protecci&oacute;n moderada contra el desgaste.",
            "rule_num": "5&ndash;25",
            "rule_label": "Espesor T&iacute;pico del &Oacute;xido (&micro;m) &mdash; Anodizado Tipo II con &Aacute;cido Sulf&uacute;rico",
            "rule_text": "El anodizado Tipo II convierte la superficie del aluminio en una capa dura y porosa de &oacute;xido de aluminio (Al&#8322;O&#8323;) de 5&ndash;25 &micro;m. La estructura regular de poros absorbe tintes org&aacute;nicos e inorg&aacute;nicos antes de que el sellado fije el color y la resistencia a la corrosi&oacute;n.",
            "process_title": "Secuencia T&iacute;pica del Proceso <span class=\"sub\">l&iacute;nea de bastidor</span>",
            "process_rows": [
                ("01", "Limpieza / Desengrase Alcalino", "54&ndash;71&deg;C", "3&ndash;5 min", "Eliminar aceites y suciedad"),
                ("02", "Enjuague", "Ambiente", "30&ndash;60 s", "Rebose; prevenir arrastre alcalino"),
                ("03", "Ataque Alcalino (opcional)", "54&ndash;66&deg;C", "1&ndash;5 min", "NaOH 40&ndash;60 g/L &mdash; acabado mate"),
                ("04", "Enjuague", "Ambiente", "30&ndash;60 s", "Eliminar residuos del ataque"),
                ("05", "Desmanchar / Desoxidar", "Ambiente", "1&ndash;3 min", "HNO&#8323; + HF o propietario"),
                ("06", "Enjuague", "Ambiente", "30&ndash;60 s", "Prevenir arrastre al tanque de anodizado"),
                ("07", "Anodizado con &Aacute;cido Sulf&uacute;rico", "20&ndash;22&deg;C", "20&ndash;60 min", "15&ndash;18% H&#8322;SO&#8324;; 1.3&ndash;1.9 A/dm&sup2;"),
                ("08", "Enjuague", "Ambiente", "1&ndash;2 min", "Enjuague contracorriente multi-etapa"),
                ("09", "Tinte (opcional)", "54&ndash;60&deg;C", "5&ndash;15 min", "Inmersi&oacute;n en tinte org&aacute;nico o inorg&aacute;nico"),
                ("10", "Sellado", "93&ndash;99&deg;C", "15&ndash;30 min", "Agua DI caliente, acetato de n&iacute;quel, o temp. media"),
            ],
            "insight_label": "Por Qu&eacute; el Tipo II Es el Est&aacute;ndar de la Industria",
            "insight_text": "El anodizado con &aacute;cido sulf&uacute;rico domina porque logra el equilibrio ideal entre costo, rendimiento y versatilidad. La capa de &oacute;xido poroso crece aproximadamente 1 &micro;m cada 3 minutos, dando control preciso del espesor. Aproximadamente dos tercios del recubrimiento crecen hacia el sustrato y un tercio hacia afuera, por lo que el cambio dimensional es modesto. La estructura de poros hexagonales es ideal para absorci&oacute;n de tintes, y el sellado en agua caliente o acetato de n&iacute;quel hidrata la al&uacute;mina para cerrar los poros permanentemente.",
            "svg_title": "Flujo del Proceso de Anodizado Tipo II <span class=\"sub\">l&iacute;nea de bastidor</span>",
            "app_title": "Gu&iacute;a de Aplicaci&oacute;n <span class=\"sub\">por serie de aleaci&oacute;n</span>",
            "app_headers": ("Serie de Aleaci&oacute;n", "Uso T&iacute;pico", "Calidad del &Oacute;xido", "Absorci&oacute;n de Tinte"),
            "app_rows": [
                ("1xxx / 5xxx", "Arquitectura, marino", "Excelente &mdash; claro, denso", "Excelente"),
                ("6xxx (6061/6063)", "Estructural, extrusi&oacute;n", "Muy buena &mdash; leve opacidad", "Muy buena"),
                ("2xxx (2024)", "Aeroespacial", "Regular &mdash; Cu causa color", "Moderada"),
                ("7xxx (7075)", "Aeroespacial, alta resist.", "Regular &mdash; Zn afecta claridad", "Moderada"),
            ],
            "dyk_text": "La estructura de poros del &oacute;xido an&oacute;dico Tipo II es notablemente regular &mdash; un arreglo hexagonal autoorganizado con di&aacute;metros de poro de <strong style=\"color:var(--amber);\">10&ndash;30 nm</strong>. Cada poro se ubica en el centro de una celda hexagonal de 50&ndash;100 nm. Esta nano-arquitectura es tan uniforme que la al&uacute;mina an&oacute;dica se usa como <strong style=\"color:var(--amber);\">plantilla para nanotecnolog&iacute;a</strong> &mdash; para cultivar nanohilos, nanotubos y puntos cu&aacute;nticos.",
            "bath_title": "Qu&iacute;mica del Ba&ntilde;o <span class=\"sub\">&aacute;cido sulf&uacute;rico</span>",
            "bath_rows": [
                ("&Aacute;cido Sulf&uacute;rico", "15&ndash;18% en peso"),
                ("Al Disuelto", "&lt;20 g/L"),
                ("Temperatura", "20&ndash;22&deg;C"),
                ("Voltaje", "14&ndash;18 V"),
                ("Densidad de Corriente", "1.3&ndash;1.9 A/dm&sup2;"),
                ("Agitaci&oacute;n", "Aire o mec&aacute;nica"),
            ],
            "spec_title": "Especificaciones <span class=\"sub\">comunes</span>",
            "spec_rows": [
                ("MIL-A-8625 Tipo II", "Anodizado sulf&uacute;rico"),
                ("AMS 2471", "Anodizado Tipo II"),
                ("ASTM B580", "Recubrimientos an&oacute;dicos"),
                ("ISO 7599", "Anodizado de Al"),
            ],
            "compare_title": "Tipo II vs Tipo III <span class=\"sub\">cu&aacute;ndo elegir cada uno</span>",
            "do_title": "Tipo II <span class=\"tag good\">Elegir Cuando</span>",
            "do_items": [
                "La resistencia a la corrosi&oacute;n es la meta principal",
                "Se necesita te&ntilde;ido de color o acabado decorativo",
                "Tolerancias estrechas (menos crecimiento dimensional)",
                "Producci&oacute;n econ&oacute;mica y de alto volumen",
                "Amplia gama de aleaciones aceptable",
            ],
            "dont_title": "Tipo III <span class=\"tag bad\">Elegir En Su Lugar</span>",
            "dont_items": [
                "M&aacute;xima resistencia al desgaste y abrasi&oacute;n",
                "Se necesitan recubrimientos m&aacute;s gruesos (&gt;25 &micro;m)",
                "Se requiere alta dureza (equiv. 60&ndash;70 Rc)",
                "Se necesitan propiedades de aislamiento el&eacute;ctrico",
                "Temperatura de operaci&oacute;n superior a 175&deg;C",
            ],
            "footer_title": "Anodizado con &Aacute;cido Sulf&uacute;rico (Tipo II) Desmitificado &mdash; Serie de Anodizado",
            "footer_disclaimer": "Referencia t&eacute;cnica solamente. Verifique todos los par&aacute;metros contra la TDS de su proveedor, especificaciones del cliente y requisitos regulatorios aplicables antes del uso en producci&oacute;n.",
        },
    },

    # ======================================================================
    # 2. HARDCOAT ANODIZING (TYPE III)
    # ======================================================================
    "hardcoat": {
        "prefix": "Hardcoat",
        "footer_code": "PP-Hardcoat-00-T",
        "en": {
            "eyebrow": "Plating Posters &middot; Anodizing &middot; Hardcoat Type III &middot; Overview",
            "headline": "HARDCOAT<br><em>ANODIZING</em>",
            "subhead": "Type III &mdash; Extreme Wear Resistance from Aluminum Oxide",
            "tagline": "Cold electrolyte, high current density, and extended time produce a dense oxide coating 25&ndash;100 &micro;m thick with hardness rivaling case-hardened steel &mdash; the gold standard for wear-critical aluminum components.",
            "rule_num": "25&ndash;75",
            "rule_label": "Typical Oxide Thickness (&micro;m) &mdash; Hardcoat Type III Anodize",
            "rule_text": "Hardcoat anodizing grows a dense, hard aluminum oxide layer at near-freezing electrolyte temperatures. At 25&ndash;75 &micro;m (up to 100+ on some alloys), the coating reaches 60&ndash;70 Rc equivalent hardness &mdash; harder than many tool steels. Roughly half the coating grows inward, so dimensional change per side is ~50% of total thickness.",
            "process_title": "Typical Process Sequence <span class=\"sub\">rack line</span>",
            "process_rows": [
                ("01", "Alkaline Clean / Degrease", "130&ndash;160&deg;F", "3&ndash;5 min", "Remove oils, soils, and shop debris"),
                ("02", "Rinse", "Ambient", "30&ndash;60 s", "Overflow; prevent drag-in"),
                ("03", "Alkaline Etch (light)", "130&ndash;150&deg;F", "30&ndash;90 s", "Brief etch; avoid excess metal removal"),
                ("04", "Rinse", "Ambient", "30&ndash;60 s", "Remove etch residue"),
                ("05", "Desmut / Deoxidize", "Ambient", "1&ndash;3 min", "HNO&#8323; + HF &mdash; critical for uniform oxide"),
                ("06", "Rinse", "Ambient", "30&ndash;60 s", "Clean surface for anodize"),
                ("07", "Hardcoat Anodize", "28&ndash;36&deg;F", "60&ndash;120 min", "H&#8322;SO&#8324; 12&ndash;15%; 24&ndash;36 ASF; ramp start"),
                ("08", "Rinse (cold)", "Ambient", "1&ndash;2 min", "Multi-stage; avoid thermal shock"),
                ("09", "Mid-Temp Seal or PTFE", "170&ndash;190&deg;F", "20&ndash;30 min", "Nickel fluoride or PTFE co-deposit"),
                ("10", "Dry / Inspect", "Ambient", "As req.", "Thickness, hardness, and seal QC"),
            ],
            "insight_label": "Why Hardcoat Outperforms Conventional Anodize",
            "insight_text": "The secret to hardcoat is temperature. At 28&ndash;36&deg;F, the sulfuric acid dissolves the oxide far more slowly than at 68&deg;F, so the coating grows thicker and denser before dissolution catches up. Higher current density (24&ndash;36 ASF vs 12&ndash;18 for Type II) drives faster growth, and the cold bath keeps the oxide from becoming soft or powdery. The result is an oxide layer 3&ndash;5&times; thicker than Type II with significantly higher hardness. This makes hardcoat the preferred surface treatment for hydraulic cylinders, pistons, valve bodies, and any aluminum part subject to sliding wear or abrasion.",
            "svg": """<svg viewBox="0 0 1060 80" width="100%" height="65" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="10" y="8" width="95" height="38" rx="7" fill="rgba(46,196,182,.10)" stroke="var(--teal)" stroke-width="1.5"/>
    <text x="57" y="24" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">CLEAN</text>
    <text x="57" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">Alk Degrease</text>
    <line x1="109" y1="27" x2="133" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="133,24 139,27 133,30" fill="currentColor" opacity=".3"/>
    <rect x="143" y="8" width="80" height="38" rx="7" fill="rgba(224,92,92,.10)" stroke="var(--coral)" stroke-width="1.2"/>
    <text x="183" y="24" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">ETCH</text>
    <text x="183" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">Light NaOH</text>
    <line x1="227" y1="27" x2="251" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="251,24 257,27 251,30" fill="currentColor" opacity=".3"/>
    <rect x="261" y="8" width="95" height="38" rx="7" fill="rgba(120,120,140,.08)" stroke="var(--muted)" stroke-width="1"/>
    <text x="308" y="24" text-anchor="middle" fill="var(--muted)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">DESMUT</text>
    <text x="308" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">HNO&#8323; Deox</text>
    <line x1="360" y1="27" x2="384" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="384,24 390,27 384,30" fill="currentColor" opacity=".3"/>
    <rect x="394" y="4" width="175" height="46" rx="8" fill="rgba(232,160,32,.12)" stroke="var(--amber)" stroke-width="2"/>
    <text x="481" y="22" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="13">HARDCOAT ANODIZE</text>
    <text x="481" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8.5" opacity=".6">28&ndash;36&deg;F &bull; 24&ndash;36 ASF &bull; 1&ndash;2 hr</text>
    <text x="481" y="70" text-anchor="middle" fill="var(--amber)" font-family="JetBrains Mono,monospace" font-size="8" opacity=".7">KEY STAGE</text>
    <line x1="573" y1="27" x2="597" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="597,24 603,27 597,30" fill="currentColor" opacity=".3"/>
    <rect x="607" y="8" width="100" height="38" rx="7" fill="rgba(120,120,140,.08)" stroke="var(--muted)" stroke-width="1"/>
    <text x="657" y="24" text-anchor="middle" fill="var(--muted)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">RINSE</text>
    <text x="657" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">Cold Multi-Stage</text>
    <line x1="711" y1="27" x2="735" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="735,24 741,27 735,30" fill="currentColor" opacity=".3"/>
    <rect x="745" y="8" width="115" height="38" rx="7" fill="rgba(232,160,32,.08)" stroke="var(--amber)" stroke-width="1" stroke-dasharray="5,3"/>
    <text x="802" y="24" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">SEAL / PTFE</text>
    <text x="802" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">Mid-Temp or PTFE</text>
    <line x1="10" y1="58" x2="863" y2="58" stroke="currentColor" stroke-width="1.5" opacity=".12" stroke-dasharray="8,4"/>
    <text x="888" y="62" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" opacity=".35" letter-spacing=".06em">LINE</text>
</svg>""",
            "svg_title": "Hardcoat Anodize Process Flow <span class=\"sub\">rack line</span>",
            "app_title": "Application Guide <span class=\"sub\">by thickness</span>",
            "app_headers": ("Thickness", "Hardness (Rc)", "Wear Rate", "Common Use"),
            "app_rows": [
                ("25&ndash;40 &micro;m", "55&ndash;60", "Low", "General wear, valve bodies"),
                ("40&ndash;65 &micro;m", "60&ndash;65", "Very low", "Hydraulic cylinders, pistons"),
                ("65&ndash;100 &micro;m", "65&ndash;70", "Minimal", "Extreme abrasion, mil-spec"),
                ("+PTFE sealed", "55&ndash;65", "Lowest (dry lube)", "Sliding contact, low friction"),
            ],
            "dyk_text": "Hardcoat anodizing requires <strong style=\"color:var(--amber);\">refrigeration equipment</strong> capable of holding the electrolyte at 28&ndash;36&deg;F while dissipating the substantial heat generated by 24&ndash;36 ASF current flow. A typical 500-gallon hardcoat tank may require <strong style=\"color:var(--amber);\">15&ndash;25 tons of refrigeration</strong> capacity. This energy cost is why hardcoat is 3&ndash;5&times; more expensive per square foot than Type II, but for wear-critical applications the performance justifies the investment many times over.",
            "bath_title": "Bath Chemistry <span class=\"sub\">sulfuric acid</span>",
            "bath_rows": [
                ("Sulfuric Acid", "12&ndash;15 wt%"),
                ("Dissolved Al", "&lt;15 g/L"),
                ("Temperature", "28&ndash;36&deg;F"),
                ("Voltage", "25&ndash;100 V (ramp)"),
                ("Current Density", "24&ndash;36 ASF"),
                ("Agitation", "Vigorous air"),
            ],
            "spec_title": "Specifications <span class=\"sub\">common</span>",
            "spec_rows": [
                ("MIL-A-8625 Type III", "Hardcoat anodize"),
                ("AMS 2469", "Hardcoat anodize"),
                ("ASTM B580 Type A", "Hard anodic coating"),
                ("AMS-A-8625 Cl 1/2", "Undyed / dyed"),
            ],
            "compare_title": "Type III Hardcoat vs Hard Chrome <span class=\"sub\">surface hardening</span>",
            "do_title": "Hardcoat Anodize <span class=\"tag good\">Choose When</span>",
            "do_items": [
                "Substrate is aluminum (native oxide growth)",
                "Uniform coverage on complex geometries",
                "Electrical insulation also needed",
                "No environmental issues (no Cr(VI))",
                "Integral bond &mdash; cannot delaminate",
            ],
            "dont_title": "Hard Chrome <span class=\"tag bad\">Choose Instead</span>",
            "dont_items": [
                "Substrate is steel, copper, or other metal",
                "Surface must be repaired / rebuilt",
                "Higher hardness needed (68&ndash;72 Rc)",
                "Thicker coatings (&gt;100 &micro;m practical)",
                "Lower coefficient of friction required",
            ],
            "footer_title": "Hardcoat Anodizing (Type III) Demystified &mdash; Anodizing Series",
            "footer_disclaimer": "Technical reference only. Verify all parameters against your chemistry supplier&rsquo;s TDS, customer specifications, and applicable regulatory requirements before production use.",
        },
        "es": {
            "eyebrow": "Plating Posters &middot; Anodizado &middot; Hardcoat Tipo III &middot; Descripci&oacute;n",
            "headline": "ANODIZADO<br><em>HARDCOAT</em>",
            "subhead": "Tipo III &mdash; Resistencia Extrema al Desgaste con &Oacute;xido de Aluminio",
            "tagline": "Electrolito fr&iacute;o, alta densidad de corriente y tiempo extendido producen una capa densa de 25&ndash;100 &micro;m con dureza comparable al acero endurecido &mdash; el est&aacute;ndar dorado para componentes de aluminio cr&iacute;ticos.",
            "rule_num": "25&ndash;75",
            "rule_label": "Espesor T&iacute;pico del &Oacute;xido (&micro;m) &mdash; Hardcoat Tipo III",
            "rule_text": "El anodizado hardcoat genera una capa densa de &oacute;xido de aluminio a temperaturas de electrolito cercanas al punto de congelaci&oacute;n. A 25&ndash;75 &micro;m (hasta 100+ en algunas aleaciones), el recubrimiento alcanza dureza equivalente a 60&ndash;70 Rc. Aproximadamente la mitad crece hacia adentro del sustrato.",
            "process_title": "Secuencia T&iacute;pica del Proceso <span class=\"sub\">l&iacute;nea de bastidor</span>",
            "process_rows": [
                ("01", "Limpieza / Desengrase Alcalino", "54&ndash;71&deg;C", "3&ndash;5 min", "Eliminar aceites y residuos"),
                ("02", "Enjuague", "Ambiente", "30&ndash;60 s", "Rebose; prevenir arrastre"),
                ("03", "Ataque Alcalino (ligero)", "54&ndash;66&deg;C", "30&ndash;90 s", "Ataque breve; evitar exceso de remoci&oacute;n"),
                ("04", "Enjuague", "Ambiente", "30&ndash;60 s", "Eliminar residuos del ataque"),
                ("05", "Desmanchar / Desoxidar", "Ambiente", "1&ndash;3 min", "HNO&#8323; + HF &mdash; cr&iacute;tico para &oacute;xido uniforme"),
                ("06", "Enjuague", "Ambiente", "30&ndash;60 s", "Superficie limpia para anodizado"),
                ("07", "Anodizado Hardcoat", "&minus;2 a 2&deg;C", "60&ndash;120 min", "H&#8322;SO&#8324; 12&ndash;15%; 2.6&ndash;3.9 A/dm&sup2;; rampa"),
                ("08", "Enjuague (fr&iacute;o)", "Ambiente", "1&ndash;2 min", "Multi-etapa; evitar choque t&eacute;rmico"),
                ("09", "Sellado Temp. Media o PTFE", "77&ndash;88&deg;C", "20&ndash;30 min", "Fluoruro de n&iacute;quel o co-dep&oacute;sito de PTFE"),
                ("10", "Secado / Inspecci&oacute;n", "Ambiente", "Seg&uacute;n req.", "Espesor, dureza y control de sellado"),
            ],
            "insight_label": "Por Qu&eacute; el Hardcoat Supera al Anodizado Convencional",
            "insight_text": "El secreto del hardcoat es la temperatura. A &minus;2 a 2&deg;C, el &aacute;cido sulf&uacute;rico disuelve el &oacute;xido mucho m&aacute;s lentamente que a 20&deg;C, por lo que la capa crece m&aacute;s gruesa y densa antes de que la disoluci&oacute;n la alcance. Mayor densidad de corriente impulsa un crecimiento m&aacute;s r&aacute;pido, y el ba&ntilde;o fr&iacute;o evita que el &oacute;xido se vuelva suave o polvoriento. El resultado es 3&ndash;5 veces m&aacute;s grueso que el Tipo II con dureza significativamente mayor.",
            "svg_title": "Flujo del Proceso de Hardcoat <span class=\"sub\">l&iacute;nea de bastidor</span>",
            "app_title": "Gu&iacute;a de Aplicaci&oacute;n <span class=\"sub\">por espesor</span>",
            "app_headers": ("Espesor", "Dureza (Rc)", "Desgaste", "Uso Com&uacute;n"),
            "app_rows": [
                ("25&ndash;40 &micro;m", "55&ndash;60", "Bajo", "Desgaste gral., v&aacute;lvulas"),
                ("40&ndash;65 &micro;m", "60&ndash;65", "Muy bajo", "Cilindros hidr&aacute;ulicos, pistones"),
                ("65&ndash;100 &micro;m", "65&ndash;70", "M&iacute;nimo", "Abrasi&oacute;n extrema, mil-spec"),
                ("+PTFE sellado", "55&ndash;65", "M&iacute;nimo (lubric. seco)", "Contacto deslizante, baja fricci&oacute;n"),
            ],
            "dyk_text": "El anodizado hardcoat requiere <strong style=\"color:var(--amber);\">equipo de refrigeraci&oacute;n</strong> capaz de mantener el electrolito a &minus;2 a 2&deg;C mientras disipa el calor generado por corrientes de 2.6&ndash;3.9 A/dm&sup2;. Un tanque t&iacute;pico de 2000 litros puede requerir <strong style=\"color:var(--amber);\">15&ndash;25 toneladas de refrigeraci&oacute;n</strong>. Este costo energ&eacute;tico hace que el hardcoat sea 3&ndash;5 veces m&aacute;s caro por metro cuadrado que el Tipo II, pero para aplicaciones cr&iacute;ticas el rendimiento lo justifica ampliamente.",
            "bath_title": "Qu&iacute;mica del Ba&ntilde;o <span class=\"sub\">&aacute;cido sulf&uacute;rico</span>",
            "bath_rows": [
                ("&Aacute;cido Sulf&uacute;rico", "12&ndash;15% en peso"),
                ("Al Disuelto", "&lt;15 g/L"),
                ("Temperatura", "&minus;2 a 2&deg;C"),
                ("Voltaje", "25&ndash;100 V (rampa)"),
                ("Densidad de Corriente", "2.6&ndash;3.9 A/dm&sup2;"),
                ("Agitaci&oacute;n", "Aire vigoroso"),
            ],
            "spec_title": "Especificaciones <span class=\"sub\">comunes</span>",
            "spec_rows": [
                ("MIL-A-8625 Tipo III", "Anodizado hardcoat"),
                ("AMS 2469", "Anodizado hardcoat"),
                ("ASTM B580 Tipo A", "Recubrimiento an&oacute;dico duro"),
                ("AMS-A-8625 Cl 1/2", "Sin te&ntilde;ir / te&ntilde;ido"),
            ],
            "compare_title": "Hardcoat Tipo III vs Cromo Duro <span class=\"sub\">endurecimiento superficial</span>",
            "do_title": "Hardcoat <span class=\"tag good\">Elegir Cuando</span>",
            "do_items": [
                "El sustrato es aluminio (crecimiento de &oacute;xido nativo)",
                "Cobertura uniforme en geometr&iacute;as complejas",
                "Tambi&eacute;n se necesita aislamiento el&eacute;ctrico",
                "Sin problemas ambientales (sin Cr(VI))",
                "Uni&oacute;n integral &mdash; no puede delaminar",
            ],
            "dont_title": "Cromo Duro <span class=\"tag bad\">Elegir En Su Lugar</span>",
            "dont_items": [
                "El sustrato es acero, cobre u otro metal",
                "La superficie debe repararse / reconstruirse",
                "Se necesita mayor dureza (68&ndash;72 Rc)",
                "Recubrimientos m&aacute;s gruesos (&gt;100 &micro;m pr&aacute;cticos)",
                "Se requiere menor coeficiente de fricci&oacute;n",
            ],
            "footer_title": "Anodizado Hardcoat (Tipo III) Desmitificado &mdash; Serie de Anodizado",
            "footer_disclaimer": "Referencia t&eacute;cnica solamente. Verifique todos los par&aacute;metros contra la TDS de su proveedor, especificaciones del cliente y requisitos regulatorios aplicables antes del uso en producci&oacute;n.",
        },
    },

    # ======================================================================
    # 3. CHROMIC ACID ANODIZING (TYPE I)
    # ======================================================================
    "type_i": {
        "prefix": "Type I",
        "footer_code": "PP-TypeI-00-T",
        "en": {
            "eyebrow": "Plating Posters &middot; Anodizing &middot; Chromic Acid Type I &middot; Overview",
            "headline": "CHROMIC ACID<br><em>ANODIZING</em>",
            "subhead": "Type I &mdash; Thin Oxide, Maximum Fatigue Life",
            "tagline": "The original aerospace anodizing process &mdash; a thin, non-porous chromic acid oxide preserves fatigue strength while providing corrosion protection and an excellent primer adhesion surface for paint systems.",
            "rule_num": "1&ndash;8",
            "rule_label": "Typical Oxide Thickness (&micro;m) &mdash; Chromic Acid Type I Anodize",
            "rule_text": "Chromic acid anodizing produces the thinnest oxide of all anodize types (1&ndash;8 &micro;m). The coating is soft, opaque gray, and relatively non-porous compared to sulfuric. Its key advantage is minimal fatigue strength reduction (&lt;5%), making it the choice for fatigue-critical aerospace structures.",
            "process_title": "Typical Process Sequence <span class=\"sub\">rack line</span>",
            "process_rows": [
                ("01", "Alkaline Clean / Degrease", "130&ndash;160&deg;F", "3&ndash;5 min", "Remove oils, sealants, shop soils"),
                ("02", "Rinse", "Ambient", "30&ndash;60 s", "Overflow counterflow rinse"),
                ("03", "Alkaline Etch (optional)", "130&ndash;150&deg;F", "1&ndash;3 min", "Light etch only &mdash; preserve dims"),
                ("04", "Rinse", "Ambient", "30&ndash;60 s", "Remove etch residue"),
                ("05", "Desmut / Deoxidize", "Ambient", "1&ndash;3 min", "HNO&#8323; or Cr-free deox"),
                ("06", "Rinse", "Ambient", "30&ndash;60 s", "Critical &mdash; no chloride drag-in"),
                ("07", "Chromic Acid Anodize", "95&ndash;100&deg;F", "30&ndash;60 min", "CrO&#8323; 30&ndash;100 g/L; 40 V ramp cycle"),
                ("08", "Rinse", "Ambient", "1&ndash;2 min", "Multi-stage; recover Cr(VI)"),
                ("09", "Seal (optional)", "200&ndash;210&deg;F", "15&ndash;20 min", "Hot DI water or dichromate seal"),
                ("10", "Dry / Prime", "Ambient", "As req.", "Apply primer within 24&ndash;72 hrs"),
            ],
            "insight_label": "Why Type I Preserves Fatigue Life",
            "insight_text": "Fatigue cracks initiate at surface stress risers. Thick, brittle oxide layers (Type II, III) create micro-cracks under cyclic loading that propagate into the aluminum substrate. Type I&rsquo;s thin, relatively soft oxide minimizes this effect &mdash; fatigue strength reduction is typically &lt;5% vs 15&ndash;25% for Type II and 25&ndash;40% for Type III. This is why Type I remains specified on fatigue-critical airframe structures like wing skins, fuselage panels, and pressure bulkheads despite the environmental pressure to replace hexavalent chromium.",
            "svg": """<svg viewBox="0 0 1060 80" width="100%" height="65" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="10" y="8" width="95" height="38" rx="7" fill="rgba(46,196,182,.10)" stroke="var(--teal)" stroke-width="1.5"/>
    <text x="57" y="24" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">CLEAN</text>
    <text x="57" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">Alk Degrease</text>
    <line x1="109" y1="27" x2="133" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="133,24 139,27 133,30" fill="currentColor" opacity=".3"/>
    <rect x="143" y="8" width="95" height="38" rx="7" fill="rgba(120,120,140,.08)" stroke="var(--muted)" stroke-width="1"/>
    <text x="190" y="24" text-anchor="middle" fill="var(--muted)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">DESMUT</text>
    <text x="190" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">HNO&#8323; Deox</text>
    <line x1="242" y1="27" x2="266" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="266,24 272,27 266,30" fill="currentColor" opacity=".3"/>
    <rect x="276" y="4" width="190" height="46" rx="8" fill="rgba(232,160,32,.12)" stroke="var(--amber)" stroke-width="2"/>
    <text x="371" y="22" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="13">CHROMIC ANODIZE</text>
    <text x="371" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8.5" opacity=".6">CrO&#8323; 30&ndash;100 g/L &bull; 40 V ramp</text>
    <text x="371" y="70" text-anchor="middle" fill="var(--amber)" font-family="JetBrains Mono,monospace" font-size="8" opacity=".7">KEY STAGE</text>
    <line x1="470" y1="27" x2="494" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="494,24 500,27 494,30" fill="currentColor" opacity=".3"/>
    <rect x="504" y="8" width="80" height="38" rx="7" fill="rgba(120,120,140,.08)" stroke="var(--muted)" stroke-width="1"/>
    <text x="544" y="24" text-anchor="middle" fill="var(--muted)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">RINSE</text>
    <text x="544" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">Cr Recovery</text>
    <line x1="588" y1="27" x2="612" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="612,24 618,27 612,30" fill="currentColor" opacity=".3"/>
    <rect x="622" y="8" width="100" height="38" rx="7" fill="rgba(39,174,96,.10)" stroke="var(--emerald)" stroke-width="1.2"/>
    <text x="672" y="24" text-anchor="middle" fill="var(--emerald)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">SEAL</text>
    <text x="672" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">Hot DI Water</text>
    <line x1="726" y1="27" x2="750" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="750,24 756,27 750,30" fill="currentColor" opacity=".3"/>
    <rect x="760" y="8" width="100" height="38" rx="7" fill="rgba(232,160,32,.08)" stroke="var(--amber)" stroke-width="1" stroke-dasharray="5,3"/>
    <text x="810" y="24" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">PRIME</text>
    <text x="810" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">Within 72 hrs</text>
    <line x1="10" y1="58" x2="863" y2="58" stroke="currentColor" stroke-width="1.5" opacity=".12" stroke-dasharray="8,4"/>
    <text x="888" y="62" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" opacity=".35" letter-spacing=".06em">LINE</text>
</svg>""",
            "svg_title": "Chromic Acid Anodize Process Flow <span class=\"sub\">rack line</span>",
            "app_title": "Application Guide <span class=\"sub\">aerospace uses</span>",
            "app_headers": ("Application", "Alloy", "Thickness", "Fatigue Loss"),
            "app_rows": [
                ("Wing skins", "2024-T3", "2&ndash;5 &micro;m", "&lt;5%"),
                ("Fuselage panels", "7075-T6", "2&ndash;5 &micro;m", "&lt;5%"),
                ("Hydraulic fittings", "6061-T6", "3&ndash;8 &micro;m", "&lt;8%"),
                ("Pressure bulkheads", "2024-T3", "1&ndash;3 &micro;m", "&lt;3%"),
            ],
            "dyk_text": "The chromic acid anodize process uses a distinctive <strong style=\"color:var(--amber);\">voltage ramp cycle</strong> rather than constant current: voltage is slowly increased from 0 to 40 V over 10 minutes, held at 40 V for 20&ndash;35 minutes, then optionally stepped to 50 V for a final 5 minutes. This ramp prevents <strong style=\"color:var(--amber);\">burning</strong> of high-copper alloys like 2024, which are extremely sensitive to localized heating. The opaque gray color of chromic anodize also serves as a built-in defect detector &mdash; cracks and lap joints appear as dark lines, making visual QC straightforward.",
            "bath_title": "Bath Chemistry <span class=\"sub\">chromic acid</span>",
            "bath_rows": [
                ("Chromic Acid (CrO&#8323;)", "30&ndash;100 g/L"),
                ("Chloride", "&lt;0.02 g/L"),
                ("Sulfate", "&lt;0.05 g/L"),
                ("Temperature", "95&ndash;100&deg;F"),
                ("Voltage", "0&rarr;40 V ramp"),
                ("Time at 40 V", "20&ndash;35 min"),
            ],
            "spec_title": "Specifications <span class=\"sub\">common</span>",
            "spec_rows": [
                ("MIL-A-8625 Type I", "Chromic anodize"),
                ("AMS 2470", "Type I anodize"),
                ("MIL-A-8625 Type IB", "Low-voltage CAA"),
                ("BAC 5019", "Boeing chromic anod."),
            ],
            "compare_title": "Type I vs Type II <span class=\"sub\">when fatigue matters</span>",
            "do_title": "Type I (Chromic) <span class=\"tag good\">Choose When</span>",
            "do_items": [
                "Fatigue-critical aerospace structures",
                "Minimal dimensional change required",
                "Paint adhesion base (primer within 72 hrs)",
                "Crack detection visual inspection needed",
                "High-Cu alloys (2024, 7075)",
            ],
            "dont_title": "Type II (Sulfuric) <span class=\"tag bad\">Choose Instead</span>",
            "dont_items": [
                "Decorative color dyeing needed",
                "Maximum corrosion resistance (undyed)",
                "Thicker oxide for standalone protection",
                "Environmental restrictions on Cr(VI)",
                "Cost-sensitive, high-volume production",
            ],
            "footer_title": "Chromic Acid Anodizing (Type I) Demystified &mdash; Anodizing Series",
            "footer_disclaimer": "Technical reference only. Verify all parameters against your chemistry supplier&rsquo;s TDS, customer specifications, and applicable regulatory requirements before production use.",
        },
        "es": {
            "eyebrow": "Plating Posters &middot; Anodizado &middot; &Aacute;cido Cr&oacute;mico Tipo I &middot; Descripci&oacute;n",
            "headline": "&Aacute;CIDO CR&Oacute;MICO<br><em>ANODIZADO</em>",
            "subhead": "Tipo I &mdash; &Oacute;xido Delgado, M&aacute;xima Vida a la Fatiga",
            "tagline": "El proceso original de anodizado aeroespacial &mdash; un &oacute;xido delgado y no poroso preserva la resistencia a la fatiga mientras proporciona protecci&oacute;n anticorrosiva y excelente adherencia para sistemas de pintura.",
            "rule_num": "1&ndash;8",
            "rule_label": "Espesor T&iacute;pico del &Oacute;xido (&micro;m) &mdash; Anodizado Tipo I con &Aacute;cido Cr&oacute;mico",
            "rule_text": "El anodizado con &aacute;cido cr&oacute;mico produce el &oacute;xido m&aacute;s delgado de todos los tipos (1&ndash;8 &micro;m). La capa es suave, gris opaca y relativamente no porosa. Su ventaja clave es la m&iacute;nima reducci&oacute;n de resistencia a la fatiga (&lt;5%), convirti&eacute;ndolo en la opci&oacute;n para estructuras aeroespaciales cr&iacute;ticas.",
            "process_title": "Secuencia T&iacute;pica del Proceso <span class=\"sub\">l&iacute;nea de bastidor</span>",
            "process_rows": [
                ("01", "Limpieza / Desengrase Alcalino", "54&ndash;71&deg;C", "3&ndash;5 min", "Eliminar aceites, selladores, suciedad"),
                ("02", "Enjuague", "Ambiente", "30&ndash;60 s", "Enjuague contracorriente"),
                ("03", "Ataque Alcalino (opcional)", "54&ndash;66&deg;C", "1&ndash;3 min", "Ataque ligero &mdash; preservar dimensiones"),
                ("04", "Enjuague", "Ambiente", "30&ndash;60 s", "Eliminar residuos del ataque"),
                ("05", "Desmanchar / Desoxidar", "Ambiente", "1&ndash;3 min", "HNO&#8323; o desoxidante sin Cr"),
                ("06", "Enjuague", "Ambiente", "30&ndash;60 s", "Cr&iacute;tico &mdash; sin arrastre de cloruros"),
                ("07", "Anodizado con &Aacute;cido Cr&oacute;mico", "35&ndash;38&deg;C", "30&ndash;60 min", "CrO&#8323; 30&ndash;100 g/L; rampa de 40 V"),
                ("08", "Enjuague", "Ambiente", "1&ndash;2 min", "Multi-etapa; recuperar Cr(VI)"),
                ("09", "Sellado (opcional)", "93&ndash;99&deg;C", "15&ndash;20 min", "Agua DI caliente o sello de dicromato"),
                ("10", "Secado / Imprimaci&oacute;n", "Ambiente", "Seg&uacute;n req.", "Aplicar imprimador dentro de 24&ndash;72 hrs"),
            ],
            "insight_label": "Por Qu&eacute; el Tipo I Preserva la Vida a la Fatiga",
            "insight_text": "Las grietas por fatiga se inician en concentradores de esfuerzo superficiales. Las capas gruesas y fr&aacute;giles (Tipo II, III) crean micro-grietas bajo carga c&iacute;clica que se propagan al sustrato. El &oacute;xido delgado y suave del Tipo I minimiza este efecto &mdash; la reducci&oacute;n de resistencia a la fatiga es t&iacute;picamente &lt;5% versus 15&ndash;25% para Tipo II y 25&ndash;40% para Tipo III. Por esto el Tipo I sigue especific&aacute;ndose en estructuras de fuselaje cr&iacute;ticas a pesar de la presi&oacute;n ambiental para reemplazar el cromo hexavalente.",
            "svg_title": "Flujo del Proceso de Anodizado Cr&oacute;mico <span class=\"sub\">l&iacute;nea de bastidor</span>",
            "app_title": "Gu&iacute;a de Aplicaci&oacute;n <span class=\"sub\">usos aeroespaciales</span>",
            "app_headers": ("Aplicaci&oacute;n", "Aleaci&oacute;n", "Espesor", "P&eacute;rdida Fatiga"),
            "app_rows": [
                ("Pieles de ala", "2024-T3", "2&ndash;5 &micro;m", "&lt;5%"),
                ("Paneles de fuselaje", "7075-T6", "2&ndash;5 &micro;m", "&lt;5%"),
                ("Accesorios hidr&aacute;ulicos", "6061-T6", "3&ndash;8 &micro;m", "&lt;8%"),
                ("Mamparos de presi&oacute;n", "2024-T3", "1&ndash;3 &micro;m", "&lt;3%"),
            ],
            "dyk_text": "El anodizado con &aacute;cido cr&oacute;mico usa un <strong style=\"color:var(--amber);\">ciclo de rampa de voltaje</strong> distintivo: el voltaje se incrementa lentamente de 0 a 40 V en 10 minutos, se mantiene a 40 V durante 20&ndash;35 minutos, y opcionalmente se sube a 50 V por 5 minutos finales. Esta rampa previene el <strong style=\"color:var(--amber);\">quemado</strong> de aleaciones con alto cobre como 2024. El color gris opaco del anodizado cr&oacute;mico tambi&eacute;n sirve como detector de defectos &mdash; las grietas aparecen como l&iacute;neas oscuras, facilitando la inspecci&oacute;n visual.",
            "bath_title": "Qu&iacute;mica del Ba&ntilde;o <span class=\"sub\">&aacute;cido cr&oacute;mico</span>",
            "bath_rows": [
                ("&Aacute;cido Cr&oacute;mico (CrO&#8323;)", "30&ndash;100 g/L"),
                ("Cloruro", "&lt;0.02 g/L"),
                ("Sulfato", "&lt;0.05 g/L"),
                ("Temperatura", "35&ndash;38&deg;C"),
                ("Voltaje", "0&rarr;40 V rampa"),
                ("Tiempo a 40 V", "20&ndash;35 min"),
            ],
            "spec_title": "Especificaciones <span class=\"sub\">comunes</span>",
            "spec_rows": [
                ("MIL-A-8625 Tipo I", "Anodizado cr&oacute;mico"),
                ("AMS 2470", "Anodizado Tipo I"),
                ("MIL-A-8625 Tipo IB", "CAA bajo voltaje"),
                ("BAC 5019", "Anod. cr&oacute;mico Boeing"),
            ],
            "compare_title": "Tipo I vs Tipo II <span class=\"sub\">cuando la fatiga importa</span>",
            "do_title": "Tipo I (Cr&oacute;mico) <span class=\"tag good\">Elegir Cuando</span>",
            "do_items": [
                "Estructuras aeroespaciales cr&iacute;ticas a fatiga",
                "Se requiere cambio dimensional m&iacute;nimo",
                "Base de adherencia para pintura (imprimar en 72 hrs)",
                "Se necesita inspecci&oacute;n visual de grietas",
                "Aleaciones con alto Cu (2024, 7075)",
            ],
            "dont_title": "Tipo II (Sulf&uacute;rico) <span class=\"tag bad\">Elegir En Su Lugar</span>",
            "dont_items": [
                "Se necesita te&ntilde;ido decorativo de color",
                "M&aacute;xima resistencia a la corrosi&oacute;n (sin te&ntilde;ir)",
                "&Oacute;xido m&aacute;s grueso para protecci&oacute;n aut&oacute;noma",
                "Restricciones ambientales sobre Cr(VI)",
                "Producci&oacute;n de alto volumen sensible al costo",
            ],
            "footer_title": "Anodizado con &Aacute;cido Cr&oacute;mico (Tipo I) Desmitificado &mdash; Serie de Anodizado",
            "footer_disclaimer": "Referencia t&eacute;cnica solamente. Verifique todos los par&aacute;metros contra la TDS de su proveedor, especificaciones del cliente y requisitos regulatorios aplicables antes del uso en producci&oacute;n.",
        },
    },

    # ======================================================================
    # 4. BORIC-SULFURIC ACID ANODIZING (BSAA)
    # ======================================================================
    "bsaa": {
        "prefix": "BSAA",
        "footer_code": "PP-BSAA-00-T",
        "en": {
            "eyebrow": "Plating Posters &middot; Anodizing &middot; BSAA &middot; Overview",
            "headline": "BORIC-SULFURIC<br><em>ACID ANODIZING</em>",
            "subhead": "BSAA &mdash; The Chromium-Free Replacement for Type I",
            "tagline": "Developed to eliminate hexavalent chromium from aerospace anodizing &mdash; BSAA produces a thin, fatigue-friendly oxide comparable to chromic acid without the carcinogenic and environmental hazards of Cr(VI).",
            "rule_num": "2&ndash;8",
            "rule_label": "Typical Oxide Thickness (&micro;m) &mdash; Boric-Sulfuric Acid Anodize",
            "rule_text": "BSAA produces a thin oxide layer (2&ndash;8 &micro;m) with fatigue and corrosion properties closely matching chromic acid (Type I). The dilute sulfuric acid grows the oxide while boric acid buffers pH at the oxide&ndash;electrolyte interface, controlling dissolution and producing a denser, less porous layer than standard Type II.",
            "process_title": "Typical Process Sequence <span class=\"sub\">rack line</span>",
            "process_rows": [
                ("01", "Alkaline Clean / Degrease", "130&ndash;160&deg;F", "3&ndash;5 min", "Remove oils, soils, and residues"),
                ("02", "Rinse", "Ambient", "30&ndash;60 s", "Overflow counterflow rinse"),
                ("03", "Alkaline Etch (optional)", "130&ndash;150&deg;F", "1&ndash;3 min", "Light etch; NaOH 40&ndash;60 g/L"),
                ("04", "Rinse", "Ambient", "30&ndash;60 s", "Remove etch residue"),
                ("05", "Desmut / Deoxidize", "Ambient", "1&ndash;3 min", "Cr-free deoxidizer; HNO&#8323;/HF blend"),
                ("06", "Rinse", "Ambient", "30&ndash;60 s", "Prevent contamination of BSAA tank"),
                ("07", "BSAA Anodize", "77&ndash;80&deg;F", "20&ndash;25 min", "H&#8322;SO&#8324; 5 g/L + H&#8323;BO&#8323; 7 g/L; 15 V"),
                ("08", "Rinse", "Ambient", "1&ndash;2 min", "Multi-stage counterflow"),
                ("09", "Seal (non-Cr)", "190&ndash;210&deg;F", "15&ndash;20 min", "Hot DI water or dilute NiAc seal"),
                ("10", "Dry / Prime", "Ambient", "As req.", "Apply primer within 72 hrs"),
            ],
            "insight_label": "Why BSAA Is Replacing Chromic Acid Anodize",
            "insight_text": "REACH regulations in Europe and growing EPA restrictions in the US are phasing out hexavalent chromium from surface finishing. BSAA was developed by Boeing and validated across major OEMs as a drop-in replacement for Type I chromic acid anodize. The dilute sulfuric acid concentration (5 g/L vs 150&ndash;180 g/L for Type II) combined with boric acid buffering produces an oxide that closely mimics CAA in thickness, fatigue performance, and paint adhesion &mdash; without generating hazardous Cr(VI) waste. BSAA is now qualified under MIL-A-8625 Type IC and has been adopted by Boeing (BAC 5632), Airbus, and most Tier 1 aerospace suppliers.",
            "svg": """<svg viewBox="0 0 1060 80" width="100%" height="65" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="10" y="8" width="95" height="38" rx="7" fill="rgba(46,196,182,.10)" stroke="var(--teal)" stroke-width="1.5"/>
    <text x="57" y="24" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">CLEAN</text>
    <text x="57" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">Alk Degrease</text>
    <line x1="109" y1="27" x2="133" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="133,24 139,27 133,30" fill="currentColor" opacity=".3"/>
    <rect x="143" y="8" width="95" height="38" rx="7" fill="rgba(120,120,140,.08)" stroke="var(--muted)" stroke-width="1"/>
    <text x="190" y="24" text-anchor="middle" fill="var(--muted)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">DESMUT</text>
    <text x="190" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">Cr-Free Deox</text>
    <line x1="242" y1="27" x2="266" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="266,24 272,27 266,30" fill="currentColor" opacity=".3"/>
    <rect x="276" y="4" width="175" height="46" rx="8" fill="rgba(232,160,32,.12)" stroke="var(--amber)" stroke-width="2"/>
    <text x="363" y="22" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="13">BSAA ANODIZE</text>
    <text x="363" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8.5" opacity=".6">H&#8322;SO&#8324; + H&#8323;BO&#8323; &bull; 15 V &bull; 77&deg;F</text>
    <text x="363" y="70" text-anchor="middle" fill="var(--amber)" font-family="JetBrains Mono,monospace" font-size="8" opacity=".7">KEY STAGE</text>
    <line x1="455" y1="27" x2="479" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="479,24 485,27 479,30" fill="currentColor" opacity=".3"/>
    <rect x="489" y="8" width="80" height="38" rx="7" fill="rgba(120,120,140,.08)" stroke="var(--muted)" stroke-width="1"/>
    <text x="529" y="24" text-anchor="middle" fill="var(--muted)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">RINSE</text>
    <text x="529" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">Multi-Stage</text>
    <line x1="573" y1="27" x2="597" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="597,24 603,27 597,30" fill="currentColor" opacity=".3"/>
    <rect x="607" y="8" width="100" height="38" rx="7" fill="rgba(39,174,96,.10)" stroke="var(--emerald)" stroke-width="1.2"/>
    <text x="657" y="24" text-anchor="middle" fill="var(--emerald)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">SEAL</text>
    <text x="657" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">Hot DI / NiAc</text>
    <line x1="711" y1="27" x2="735" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="735,24 741,27 735,30" fill="currentColor" opacity=".3"/>
    <rect x="745" y="8" width="100" height="38" rx="7" fill="rgba(232,160,32,.08)" stroke="var(--amber)" stroke-width="1" stroke-dasharray="5,3"/>
    <text x="795" y="24" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">PRIME</text>
    <text x="795" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">Within 72 hrs</text>
    <line x1="10" y1="58" x2="848" y2="58" stroke="currentColor" stroke-width="1.5" opacity=".12" stroke-dasharray="8,4"/>
    <text x="873" y="62" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" opacity=".35" letter-spacing=".06em">LINE</text>
</svg>""",
            "svg_title": "BSAA Process Flow <span class=\"sub\">rack line</span>",
            "app_title": "Application Guide <span class=\"sub\">vs chromic acid</span>",
            "app_headers": ("Property", "BSAA", "Type I (CAA)", "Verdict"),
            "app_rows": [
                ("Fatigue loss", "&lt;5&ndash;8%", "&lt;5%", "Comparable"),
                ("Paint adhesion", "Excellent", "Excellent", "Equivalent"),
                ("Corrosion (SST hrs)", "336&ndash;500+", "336&ndash;500+", "Equivalent"),
                ("Hex chrome waste", "None", "High", "BSAA wins"),
            ],
            "dyk_text": "The boric acid in BSAA isn&rsquo;t there to grow oxide &mdash; it acts as a <strong style=\"color:var(--amber);\">pH buffer</strong> at the oxide&ndash;electrolyte interface. During anodizing, the local pH at the pore base drops as aluminum ions dissolve, which accelerates oxide dissolution and makes pores wider. Boric acid neutralizes this pH drop, keeping dissolution in check and producing <strong style=\"color:var(--amber);\">smaller, denser pores</strong> similar to chromic acid &mdash; despite using sulfuric acid as the primary electrolyte. This buffering trick is what lets BSAA match Type I fatigue performance.",
            "bath_title": "Bath Chemistry <span class=\"sub\">boric-sulfuric</span>",
            "bath_rows": [
                ("Sulfuric Acid", "4&ndash;6 g/L"),
                ("Boric Acid", "6&ndash;8 g/L"),
                ("Dissolved Al", "&lt;5 g/L"),
                ("Temperature", "77&ndash;80&deg;F"),
                ("Voltage", "15 V (constant)"),
                ("Time", "20&ndash;25 min"),
            ],
            "spec_title": "Specifications <span class=\"sub\">common</span>",
            "spec_rows": [
                ("MIL-A-8625 Type IC", "BSAA anodize"),
                ("BAC 5632", "Boeing BSAA"),
                ("AIMS 03-04-022", "Airbus BSAA"),
                ("AMS 2468", "BSAA (pending)"),
            ],
            "compare_title": "BSAA vs Chromic Acid (Type I) <span class=\"sub\">the transition</span>",
            "do_title": "BSAA <span class=\"tag good\">Choose When</span>",
            "do_items": [
                "Replacing Type I for environmental compliance",
                "REACH/EPA chromium restrictions apply",
                "Fatigue-critical parts (equivalent performance)",
                "New programs with Cr(VI)-free mandate",
                "Lower waste treatment cost desired",
            ],
            "dont_title": "Type I (CAA) <span class=\"tag bad\">Choose Instead</span>",
            "dont_items": [
                "Legacy spec requires Type I specifically",
                "Customer has not qualified BSAA yet",
                "Existing Cr(VI) line with no transition plan",
                "Alloy-specific qualification not completed",
                "Repair/overhaul of heritage aircraft parts",
            ],
            "footer_title": "Boric-Sulfuric Acid Anodizing (BSAA) Demystified &mdash; Anodizing Series",
            "footer_disclaimer": "Technical reference only. Verify all parameters against your chemistry supplier&rsquo;s TDS, customer specifications, and applicable regulatory requirements before production use.",
        },
        "es": {
            "eyebrow": "Plating Posters &middot; Anodizado &middot; BSAA &middot; Descripci&oacute;n",
            "headline": "ANODIZADO<br><em>B&Oacute;RICO-SULF&Uacute;RICO</em>",
            "subhead": "BSAA &mdash; El Reemplazo Libre de Cromo para el Tipo I",
            "tagline": "Desarrollado para eliminar el cromo hexavalente del anodizado aeroespacial &mdash; el BSAA produce un &oacute;xido delgado comparable al &aacute;cido cr&oacute;mico sin los riesgos carcinog&eacute;nicos y ambientales del Cr(VI).",
            "rule_num": "2&ndash;8",
            "rule_label": "Espesor T&iacute;pico del &Oacute;xido (&micro;m) &mdash; Anodizado B&oacute;rico-Sulf&uacute;rico",
            "rule_text": "El BSAA produce una capa delgada de &oacute;xido (2&ndash;8 &micro;m) con propiedades de fatiga y corrosi&oacute;n similares al &aacute;cido cr&oacute;mico (Tipo I). El &aacute;cido sulf&uacute;rico diluido genera el &oacute;xido mientras el &aacute;cido b&oacute;rico regula el pH en la interfaz, controlando la disoluci&oacute;n y produciendo una capa m&aacute;s densa.",
            "process_title": "Secuencia T&iacute;pica del Proceso <span class=\"sub\">l&iacute;nea de bastidor</span>",
            "process_rows": [
                ("01", "Limpieza / Desengrase Alcalino", "54&ndash;71&deg;C", "3&ndash;5 min", "Eliminar aceites y residuos"),
                ("02", "Enjuague", "Ambiente", "30&ndash;60 s", "Enjuague contracorriente"),
                ("03", "Ataque Alcalino (opcional)", "54&ndash;66&deg;C", "1&ndash;3 min", "Ataque ligero; NaOH 40&ndash;60 g/L"),
                ("04", "Enjuague", "Ambiente", "30&ndash;60 s", "Eliminar residuos del ataque"),
                ("05", "Desmanchar / Desoxidar", "Ambiente", "1&ndash;3 min", "Desoxidante sin Cr; mezcla HNO&#8323;/HF"),
                ("06", "Enjuague", "Ambiente", "30&ndash;60 s", "Prevenir contaminaci&oacute;n del tanque BSAA"),
                ("07", "Anodizado BSAA", "25&ndash;27&deg;C", "20&ndash;25 min", "H&#8322;SO&#8324; 5 g/L + H&#8323;BO&#8323; 7 g/L; 15 V"),
                ("08", "Enjuague", "Ambiente", "1&ndash;2 min", "Contracorriente multi-etapa"),
                ("09", "Sellado (sin Cr)", "88&ndash;99&deg;C", "15&ndash;20 min", "Agua DI caliente o NiAc diluido"),
                ("10", "Secado / Imprimaci&oacute;n", "Ambiente", "Seg&uacute;n req.", "Aplicar imprimador dentro de 72 hrs"),
            ],
            "insight_label": "Por Qu&eacute; el BSAA Est&aacute; Reemplazando al Anodizado Cr&oacute;mico",
            "insight_text": "Las regulaciones REACH en Europa y las restricciones de la EPA en EE.UU. est&aacute;n eliminando el cromo hexavalente del acabado de superficies. El BSAA fue desarrollado por Boeing y validado en las principales OEM como reemplazo directo del Tipo I. La baja concentraci&oacute;n de &aacute;cido sulf&uacute;rico (5 g/L vs 150&ndash;180 g/L del Tipo II) combinada con el amortiguamiento del &aacute;cido b&oacute;rico produce un &oacute;xido similar al CAA en espesor, rendimiento a fatiga y adherencia de pintura &mdash; sin generar residuos peligrosos de Cr(VI).",
            "svg_title": "Flujo del Proceso BSAA <span class=\"sub\">l&iacute;nea de bastidor</span>",
            "app_title": "Gu&iacute;a de Aplicaci&oacute;n <span class=\"sub\">vs &aacute;cido cr&oacute;mico</span>",
            "app_headers": ("Propiedad", "BSAA", "Tipo I (CAA)", "Resultado"),
            "app_rows": [
                ("P&eacute;rdida por fatiga", "&lt;5&ndash;8%", "&lt;5%", "Comparable"),
                ("Adherencia de pintura", "Excelente", "Excelente", "Equivalente"),
                ("Corrosi&oacute;n (hrs SST)", "336&ndash;500+", "336&ndash;500+", "Equivalente"),
                ("Residuos de Cr hex.", "Ninguno", "Alto", "BSAA gana"),
            ],
            "dyk_text": "El &aacute;cido b&oacute;rico en el BSAA no genera &oacute;xido &mdash; act&uacute;a como <strong style=\"color:var(--amber);\">amortiguador de pH</strong> en la interfaz &oacute;xido-electrolito. Durante el anodizado, el pH local en la base del poro baja mientras los iones de aluminio se disuelven, acelerando la disoluci&oacute;n. El &aacute;cido b&oacute;rico neutraliza esta ca&iacute;da, produciendo <strong style=\"color:var(--amber);\">poros m&aacute;s peque&ntilde;os y densos</strong> similares al &aacute;cido cr&oacute;mico &mdash; a pesar de usar &aacute;cido sulf&uacute;rico como electrolito principal.",
            "bath_title": "Qu&iacute;mica del Ba&ntilde;o <span class=\"sub\">b&oacute;rico-sulf&uacute;rico</span>",
            "bath_rows": [
                ("&Aacute;cido Sulf&uacute;rico", "4&ndash;6 g/L"),
                ("&Aacute;cido B&oacute;rico", "6&ndash;8 g/L"),
                ("Al Disuelto", "&lt;5 g/L"),
                ("Temperatura", "25&ndash;27&deg;C"),
                ("Voltaje", "15 V (constante)"),
                ("Tiempo", "20&ndash;25 min"),
            ],
            "spec_title": "Especificaciones <span class=\"sub\">comunes</span>",
            "spec_rows": [
                ("MIL-A-8625 Tipo IC", "Anodizado BSAA"),
                ("BAC 5632", "BSAA de Boeing"),
                ("AIMS 03-04-022", "BSAA de Airbus"),
                ("AMS 2468", "BSAA (pendiente)"),
            ],
            "compare_title": "BSAA vs &Aacute;cido Cr&oacute;mico (Tipo I) <span class=\"sub\">la transici&oacute;n</span>",
            "do_title": "BSAA <span class=\"tag good\">Elegir Cuando</span>",
            "do_items": [
                "Reemplazar Tipo I por cumplimiento ambiental",
                "Aplican restricciones REACH/EPA de cromo",
                "Piezas cr&iacute;ticas a fatiga (rendimiento equivalente)",
                "Programas nuevos con mandato libre de Cr(VI)",
                "Se desea menor costo de tratamiento de residuos",
            ],
            "dont_title": "Tipo I (CAA) <span class=\"tag bad\">Elegir En Su Lugar</span>",
            "dont_items": [
                "La especificaci&oacute;n legada requiere Tipo I espec&iacute;ficamente",
                "El cliente a&uacute;n no ha calificado BSAA",
                "L&iacute;nea existente de Cr(VI) sin plan de transici&oacute;n",
                "Calificaci&oacute;n por aleaci&oacute;n no completada",
                "Reparaci&oacute;n de piezas de aeronaves legadas",
            ],
            "footer_title": "Anodizado B&oacute;rico-Sulf&uacute;rico (BSAA) Desmitificado &mdash; Serie de Anodizado",
            "footer_disclaimer": "Referencia t&eacute;cnica solamente. Verifique todos los par&aacute;metros contra la TDS de su proveedor, especificaciones del cliente y requisitos regulatorios aplicables antes del uso en producci&oacute;n.",
        },
    },

    # ======================================================================
    # 5. PHOSPHORIC ACID ANODIZING (PAA)
    # ======================================================================
    "paa": {
        "prefix": "PAA",
        "footer_code": "PP-PAA-00-T",
        "en": {
            "eyebrow": "Plating Posters &middot; Anodizing &middot; PAA &middot; Overview",
            "headline": "PHOSPHORIC ACID<br><em>ANODIZING</em>",
            "subhead": "PAA &mdash; The Adhesive Bonding Surface Treatment",
            "tagline": "The only anodize process designed specifically for structural adhesive bonding &mdash; PAA creates a whisker-like porous oxide that mechanical interlocking with adhesive primers achieves peel strengths conventional surfaces cannot match.",
            "rule_num": "0.1&ndash;0.5",
            "rule_label": "Typical Oxide Thickness (&micro;m) &mdash; Phosphoric Acid Anodize",
            "rule_text": "PAA produces the thinnest, most open oxide of any anodize process (0.1&ndash;0.5 &micro;m). Unlike other anodize types, PAA is never sealed &mdash; the open, whisker-like pore structure is the entire point. Adhesive primer wicks into the pores and cures in place, creating a mechanical interlock that resists peel and cleavage forces in bonded airframe assemblies.",
            "process_title": "Typical Process Sequence <span class=\"sub\">bonding line</span>",
            "process_rows": [
                ("01", "Alkaline Clean / Degrease", "130&ndash;160&deg;F", "3&ndash;5 min", "Remove oils, mold release agents"),
                ("02", "Rinse", "Ambient", "30&ndash;60 s", "Overflow counterflow"),
                ("03", "FPL Etch (or P2 Etch)", "150&ndash;160&deg;F", "10&ndash;12 min", "Na&#8322;Cr&#8322;O&#8327; / H&#8322;SO&#8324; or Cr-free P2"),
                ("04", "Rinse", "Ambient", "30&ndash;60 s", "Multiple immersion rinses"),
                ("05", "Desmut (if needed)", "Ambient", "30&ndash;60 s", "Alloy-dependent; remove Cu/Si smut"),
                ("06", "Rinse", "Ambient", "30&ndash;60 s", "Critical cleanliness for bonding"),
                ("07", "Phosphoric Acid Anodize", "73&ndash;80&deg;F", "20&ndash;25 min", "H&#8323;PO&#8324; 5&ndash;12 wt%; 10&ndash;20 V"),
                ("08", "Rinse", "Ambient", "1&ndash;2 min", "DI water; no seal applied"),
                ("09", "Dry (forced air)", "140&ndash;160&deg;F", "5&ndash;10 min", "Immediate dry; prevent hydration"),
                ("10", "Prime", "Ambient", "Within 72 hrs", "Apply bonding primer (BR 127, etc.)"),
            ],
            "insight_label": "Why PAA Creates the Best Bonding Surface",
            "insight_text": "The phosphoric acid electrolyte preferentially dissolves the barrier layer at the pore base while growing new oxide at the metal/oxide interface. This produces an oxide with uniquely open, funnel-shaped pores and finger-like whiskers at the surface. When adhesive primer is applied, it flows into these features and cures around them, creating a mechanical interlock far superior to the smooth, sealed surface of Type II. Boeing testing showed PAA-bonded joints retain &gt;90% of initial peel strength after 14 years of outdoor exposure, compared to &lt;50% for FPL-etch-only bonds.",
            "svg": """<svg viewBox="0 0 1060 80" width="100%" height="65" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="10" y="8" width="95" height="38" rx="7" fill="rgba(46,196,182,.10)" stroke="var(--teal)" stroke-width="1.5"/>
    <text x="57" y="24" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">CLEAN</text>
    <text x="57" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">Alk Degrease</text>
    <line x1="109" y1="27" x2="133" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="133,24 139,27 133,30" fill="currentColor" opacity=".3"/>
    <rect x="143" y="8" width="95" height="38" rx="7" fill="rgba(224,92,92,.10)" stroke="var(--coral)" stroke-width="1.2"/>
    <text x="190" y="24" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">FPL ETCH</text>
    <text x="190" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">Chromate or P2</text>
    <line x1="242" y1="27" x2="266" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="266,24 272,27 266,30" fill="currentColor" opacity=".3"/>
    <rect x="276" y="4" width="170" height="46" rx="8" fill="rgba(232,160,32,.12)" stroke="var(--amber)" stroke-width="2"/>
    <text x="361" y="22" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="13">PAA ANODIZE</text>
    <text x="361" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8.5" opacity=".6">H&#8323;PO&#8324; 5&ndash;12% &bull; 10&ndash;20 V</text>
    <text x="361" y="70" text-anchor="middle" fill="var(--amber)" font-family="JetBrains Mono,monospace" font-size="8" opacity=".7">KEY STAGE</text>
    <line x1="450" y1="27" x2="474" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="474,24 480,27 474,30" fill="currentColor" opacity=".3"/>
    <rect x="484" y="8" width="80" height="38" rx="7" fill="rgba(120,120,140,.08)" stroke="var(--muted)" stroke-width="1"/>
    <text x="524" y="24" text-anchor="middle" fill="var(--muted)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">RINSE</text>
    <text x="524" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">DI Water</text>
    <line x1="568" y1="27" x2="592" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="592,24 598,27 592,30" fill="currentColor" opacity=".3"/>
    <rect x="602" y="8" width="95" height="38" rx="7" fill="rgba(39,174,96,.10)" stroke="var(--emerald)" stroke-width="1.2"/>
    <text x="649" y="24" text-anchor="middle" fill="var(--emerald)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">DRY</text>
    <text x="649" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">Forced Air</text>
    <line x1="701" y1="27" x2="725" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="725,24 731,27 725,30" fill="currentColor" opacity=".3"/>
    <rect x="735" y="8" width="120" height="38" rx="7" fill="rgba(232,160,32,.08)" stroke="var(--amber)" stroke-width="1" stroke-dasharray="5,3"/>
    <text x="795" y="24" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">PRIME</text>
    <text x="795" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">BR 127 &lt;72 hrs</text>
    <line x1="10" y1="58" x2="858" y2="58" stroke="currentColor" stroke-width="1.5" opacity=".12" stroke-dasharray="8,4"/>
    <text x="883" y="62" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" opacity=".35" letter-spacing=".06em">LINE</text>
</svg>""",
            "svg_title": "PAA Process Flow <span class=\"sub\">bonding line</span>",
            "app_title": "Application Guide <span class=\"sub\">bonding performance</span>",
            "app_headers": ("Surface Prep", "Peel (lb/in)", "Wedge Crack", "Durability"),
            "app_rows": [
                ("PAA + BR 127", "50&ndash;80+", "Cohesive", "Excellent &mdash; 14+ yr proven"),
                ("FPL Etch + primer", "30&ndash;50", "Mixed mode", "Good &mdash; degradation over time"),
                ("Abrade + primer", "20&ndash;35", "Adhesive", "Fair &mdash; moisture-sensitive"),
                ("Grit blast + primer", "25&ndash;40", "Mixed mode", "Moderate"),
            ],
            "dyk_text": "PAA was invented by Boeing in the 1970s (U.S. Patent 4,085,012) specifically to improve the durability of adhesively bonded aluminum airframe structures. The <strong style=\"color:var(--amber);\">wedge crack extension test</strong> (ASTM D3762) is the gold standard for evaluating PAA surfaces &mdash; a bonded specimen is loaded, exposed to 140&deg;F / 95% RH for 14&ndash;28 days, and crack growth is measured. A properly PAA-treated surface shows <strong style=\"color:var(--amber);\">cohesive failure</strong> (adhesive fails, not the interface), proving the bond is stronger than the adhesive itself.",
            "bath_title": "Bath Chemistry <span class=\"sub\">phosphoric acid</span>",
            "bath_rows": [
                ("Phosphoric Acid", "5&ndash;12 wt%"),
                ("Dissolved Al", "&lt;5 g/L"),
                ("Temperature", "73&ndash;80&deg;F"),
                ("Voltage", "10&ndash;20 V"),
                ("Current Density", "4&ndash;10 ASF"),
                ("Time", "20&ndash;25 min"),
            ],
            "spec_title": "Specifications <span class=\"sub\">common</span>",
            "spec_rows": [
                ("ASTM D3933", "PAA surface prep"),
                ("BAC 5555", "Boeing PAA"),
                ("ASTM D3762", "Wedge crack test"),
                ("MIL-A-8625 Type II*", "*with PAA note"),
            ],
            "compare_title": "PAA vs FPL Etch <span class=\"sub\">for structural bonding</span>",
            "do_title": "PAA <span class=\"tag good\">Choose When</span>",
            "do_items": [
                "Structural adhesive bonding (primary)",
                "Long-term bond durability required",
                "Hot-wet environmental exposure expected",
                "Boeing or Airbus bonding spec required",
                "Fatigue-critical bonded assemblies",
            ],
            "dont_title": "FPL Etch Alone <span class=\"tag bad\">May Suffice When</span>",
            "dont_items": [
                "Non-structural or secondary bonding only",
                "Short service life or benign environment",
                "Field repair with no anodize capability",
                "Cost-constrained, non-critical joints",
                "Small repair patches (manual application)",
            ],
            "footer_title": "Phosphoric Acid Anodizing (PAA) Demystified &mdash; Anodizing Series",
            "footer_disclaimer": "Technical reference only. Verify all parameters against your chemistry supplier&rsquo;s TDS, customer specifications, and applicable regulatory requirements before production use.",
        },
        "es": {
            "eyebrow": "Plating Posters &middot; Anodizado &middot; PAA &middot; Descripci&oacute;n",
            "headline": "&Aacute;CIDO FOSF&Oacute;RICO<br><em>ANODIZADO</em>",
            "subhead": "PAA &mdash; El Tratamiento Superficial para Uni&oacute;n Adhesiva",
            "tagline": "El &uacute;nico proceso de anodizado dise&ntilde;ado espec&iacute;ficamente para uni&oacute;n adhesiva estructural &mdash; el PAA crea un &oacute;xido poroso que logra resistencias al despegue imposibles con superficies convencionales.",
            "rule_num": "0.1&ndash;0.5",
            "rule_label": "Espesor T&iacute;pico del &Oacute;xido (&micro;m) &mdash; Anodizado con &Aacute;cido Fosf&oacute;rico",
            "rule_text": "El PAA produce el &oacute;xido m&aacute;s delgado y abierto de cualquier anodizado (0.1&ndash;0.5 &micro;m). A diferencia de otros tipos, el PAA nunca se sella &mdash; la estructura abierta de poros es el objetivo. El imprimador adhesivo penetra los poros y cura in situ, creando un interlock mec&aacute;nico que resiste fuerzas de pelado.",
            "process_title": "Secuencia T&iacute;pica del Proceso <span class=\"sub\">l&iacute;nea de uni&oacute;n</span>",
            "process_rows": [
                ("01", "Limpieza / Desengrase Alcalino", "54&ndash;71&deg;C", "3&ndash;5 min", "Eliminar aceites y agentes desmoldantes"),
                ("02", "Enjuague", "Ambiente", "30&ndash;60 s", "Contracorriente con rebose"),
                ("03", "Ataque FPL (o P2)", "66&ndash;71&deg;C", "10&ndash;12 min", "Na&#8322;Cr&#8322;O&#8327; / H&#8322;SO&#8324; o P2 sin Cr"),
                ("04", "Enjuague", "Ambiente", "30&ndash;60 s", "M&uacute;ltiples enjuagues por inmersi&oacute;n"),
                ("05", "Desmanchar (si es necesario)", "Ambiente", "30&ndash;60 s", "Seg&uacute;n aleaci&oacute;n; eliminar Cu/Si"),
                ("06", "Enjuague", "Ambiente", "30&ndash;60 s", "Limpieza cr&iacute;tica para uni&oacute;n"),
                ("07", "Anodizado con &Aacute;cido Fosf&oacute;rico", "23&ndash;27&deg;C", "20&ndash;25 min", "H&#8323;PO&#8324; 5&ndash;12%; 10&ndash;20 V"),
                ("08", "Enjuague", "Ambiente", "1&ndash;2 min", "Agua DI; sin sellado"),
                ("09", "Secado (aire forzado)", "60&ndash;71&deg;C", "5&ndash;10 min", "Secado inmediato; evitar hidrataci&oacute;n"),
                ("10", "Imprimaci&oacute;n", "Ambiente", "Dentro de 72 hrs", "Aplicar imprimador de uni&oacute;n (BR 127, etc.)"),
            ],
            "insight_label": "Por Qu&eacute; el PAA Crea la Mejor Superficie para Uni&oacute;n",
            "insight_text": "El electrolito de &aacute;cido fosf&oacute;rico disuelve preferencialmente la capa barrera en la base del poro mientras genera nuevo &oacute;xido en la interfaz metal/&oacute;xido. Esto produce un &oacute;xido con poros abiertos en forma de embudo y estructuras digitiformes en la superficie. Cuando se aplica el imprimador, fluye dentro de estas estructuras y cura alrededor de ellas, creando un interlock mec&aacute;nico superior. Pruebas de Boeing mostraron que juntas con PAA retienen &gt;90% de su resistencia al pelado despu&eacute;s de 14 a&ntilde;os de exposici&oacute;n al exterior.",
            "svg_title": "Flujo del Proceso PAA <span class=\"sub\">l&iacute;nea de uni&oacute;n</span>",
            "app_title": "Gu&iacute;a de Aplicaci&oacute;n <span class=\"sub\">rendimiento de uni&oacute;n</span>",
            "app_headers": ("Prep. Superficial", "Pelado (lb/in)", "Grieta Cu&ntilde;a", "Durabilidad"),
            "app_rows": [
                ("PAA + BR 127", "50&ndash;80+", "Cohesiva", "Excelente &mdash; 14+ a&ntilde;os"),
                ("Ataque FPL + imprim.", "30&ndash;50", "Modo mixto", "Buena &mdash; degradaci&oacute;n con tiempo"),
                ("Abrasi&oacute;n + imprim.", "20&ndash;35", "Adhesiva", "Regular &mdash; sensible a humedad"),
                ("Granallado + imprim.", "25&ndash;40", "Modo mixto", "Moderada"),
            ],
            "dyk_text": "El PAA fue inventado por Boeing en los 1970s (Patente U.S. 4,085,012) espec&iacute;ficamente para mejorar la durabilidad de estructuras de aluminio unidas adhesivamente. La <strong style=\"color:var(--amber);\">prueba de extensi&oacute;n de grieta por cu&ntilde;a</strong> (ASTM D3762) es el est&aacute;ndar dorado &mdash; un esp&eacute;cimen se carga, expone a 60&deg;C / 95% HR durante 14&ndash;28 d&iacute;as, y se mide el crecimiento de grieta. Una superficie tratada correctamente con PAA muestra <strong style=\"color:var(--amber);\">falla cohesiva</strong> (falla el adhesivo, no la interfaz).",
            "bath_title": "Qu&iacute;mica del Ba&ntilde;o <span class=\"sub\">&aacute;cido fosf&oacute;rico</span>",
            "bath_rows": [
                ("&Aacute;cido Fosf&oacute;rico", "5&ndash;12% en peso"),
                ("Al Disuelto", "&lt;5 g/L"),
                ("Temperatura", "23&ndash;27&deg;C"),
                ("Voltaje", "10&ndash;20 V"),
                ("Densidad de Corriente", "0.4&ndash;1.1 A/dm&sup2;"),
                ("Tiempo", "20&ndash;25 min"),
            ],
            "spec_title": "Especificaciones <span class=\"sub\">comunes</span>",
            "spec_rows": [
                ("ASTM D3933", "Prep. superficial PAA"),
                ("BAC 5555", "PAA de Boeing"),
                ("ASTM D3762", "Prueba de grieta cu&ntilde;a"),
                ("MIL-A-8625 Tipo II*", "*con nota PAA"),
            ],
            "compare_title": "PAA vs Ataque FPL <span class=\"sub\">para uni&oacute;n estructural</span>",
            "do_title": "PAA <span class=\"tag good\">Elegir Cuando</span>",
            "do_items": [
                "Uni&oacute;n adhesiva estructural (primaria)",
                "Se requiere durabilidad a largo plazo",
                "Exposici&oacute;n a ambiente caliente-h&uacute;medo esperada",
                "Especificaci&oacute;n de Boeing o Airbus requerida",
                "Ensambles unidos cr&iacute;ticos a fatiga",
            ],
            "dont_title": "Ataque FPL Solo <span class=\"tag bad\">Puede Bastar Cuando</span>",
            "dont_items": [
                "Uni&oacute;n no estructural o secundaria solamente",
                "Vida de servicio corta o ambiente benigno",
                "Reparaci&oacute;n en campo sin capacidad de anodizado",
                "Juntas no cr&iacute;ticas con restricci&oacute;n de costo",
                "Parches peque&ntilde;os de reparaci&oacute;n (aplicaci&oacute;n manual)",
            ],
            "footer_title": "Anodizado con &Aacute;cido Fosf&oacute;rico (PAA) Desmitificado &mdash; Serie de Anodizado",
            "footer_disclaimer": "Referencia t&eacute;cnica solamente. Verifique todos los par&aacute;metros contra la TDS de su proveedor, especificaciones del cliente y requisitos regulatorios aplicables antes del uso en producci&oacute;n.",
        },
    },

    # ======================================================================
    # 6. BRIGHT ANODIZING
    # ======================================================================
    "bright": {
        "prefix": "Bright Anod",
        "footer_code": "PP-BrtAnod-00-T",
        "en": {
            "eyebrow": "Plating Posters &middot; Anodizing &middot; Bright Anodizing &middot; Overview",
            "headline": "BRIGHT<br><em>ANODIZING</em>",
            "subhead": "Chemical Brightening + Type II &mdash; Mirror-Like Aluminum Finishes",
            "tagline": "A multi-step process combining chemical or electrochemical brightening with standard sulfuric acid anodizing to produce highly reflective, mirror-finish aluminum surfaces for architectural, automotive, and decorative applications.",
            "rule_num": "5&ndash;20",
            "rule_label": "Typical Oxide Thickness (&micro;m) &mdash; Bright Anodize (Type II on Brightened Surface)",
            "rule_text": "Bright anodizing is standard Type II sulfuric acid anodize performed on a chemically or electrochemically brightened surface. The brightening step smooths micro-roughness to achieve &gt;80% specular reflectance; the subsequent anodize protects this surface while maintaining clarity. Oxide thickness of 5&ndash;20 &micro;m is typical, with thinner coatings preserving more reflectivity.",
            "process_title": "Typical Process Sequence <span class=\"sub\">bright dip line</span>",
            "process_rows": [
                ("01", "Alkaline Clean / Degrease", "130&ndash;160&deg;F", "3&ndash;5 min", "Remove oils; avoid scratching"),
                ("02", "Rinse", "Ambient", "30&ndash;60 s", "Overflow; prevent drag-in"),
                ("03", "Alkaline Etch (very light)", "130&ndash;140&deg;F", "15&ndash;60 s", "Minimal metal removal; preserve finish"),
                ("04", "Rinse", "Ambient", "30&ndash;60 s", "Remove etch residue"),
                ("05", "Bright Dip / Electropolish", "180&ndash;220&deg;F", "30&ndash;120 s", "H&#8323;PO&#8324; / HNO&#8323; blend; or anodic EP"),
                ("06", "Rinse (multi-stage)", "Ambient", "1&ndash;2 min", "Remove acid; prevent staining"),
                ("07", "Desmut (if needed)", "Ambient", "15&ndash;30 s", "Light HNO&#8323; for Cu-bearing alloys"),
                ("08", "Sulfuric Acid Anodize", "68&ndash;72&deg;F", "20&ndash;40 min", "Standard Type II; lower CD for clarity"),
                ("09", "Clear or Light Dye (opt.)", "130&ndash;140&deg;F", "2&ndash;10 min", "Gold, champagne, or clear seal only"),
                ("10", "Seal", "200&ndash;210&deg;F", "15&ndash;30 min", "Hot DI water or NiAc seal"),
            ],
            "insight_label": "How Bright Dipping Creates Mirror Surfaces",
            "insight_text": "Chemical brightening works by preferential dissolution of micro-peaks on the aluminum surface. The concentrated phosphoric-nitric acid blend creates a viscous boundary layer over valleys while peaks protrude into fresh acid and dissolve faster. This levels the surface roughness from Ra ~0.5 &micro;m down to Ra &lt;0.05 &micro;m, producing specular reflectance above 80%. Electrochemical brightening (electropolishing) uses a similar principle with anodic current in phosphoric acid, giving even finer control. The subsequent clear anodize must be carefully controlled &mdash; too thick and the oxide scatters light, reducing reflectivity.",
            "svg": """<svg viewBox="0 0 1060 80" width="100%" height="65" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="10" y="8" width="95" height="38" rx="7" fill="rgba(46,196,182,.10)" stroke="var(--teal)" stroke-width="1.5"/>
    <text x="57" y="24" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">CLEAN</text>
    <text x="57" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">Gentle Degrease</text>
    <line x1="109" y1="27" x2="133" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="133,24 139,27 133,30" fill="currentColor" opacity=".3"/>
    <rect x="143" y="4" width="140" height="46" rx="8" fill="rgba(232,160,32,.12)" stroke="var(--amber)" stroke-width="2"/>
    <text x="213" y="22" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="13">BRIGHT DIP</text>
    <text x="213" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8.5" opacity=".6">H&#8323;PO&#8324;/HNO&#8323; &bull; 200&deg;F</text>
    <text x="213" y="70" text-anchor="middle" fill="var(--amber)" font-family="JetBrains Mono,monospace" font-size="8" opacity=".7">KEY STAGE 1</text>
    <line x1="287" y1="27" x2="311" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="311,24 317,27 311,30" fill="currentColor" opacity=".3"/>
    <rect x="321" y="8" width="80" height="38" rx="7" fill="rgba(120,120,140,.08)" stroke="var(--muted)" stroke-width="1"/>
    <text x="361" y="24" text-anchor="middle" fill="var(--muted)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">RINSE</text>
    <text x="361" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">Multi-Stage</text>
    <line x1="405" y1="27" x2="429" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="429,24 435,27 429,30" fill="currentColor" opacity=".3"/>
    <rect x="439" y="4" width="160" height="46" rx="8" fill="rgba(39,174,96,.12)" stroke="var(--emerald)" stroke-width="2"/>
    <text x="519" y="22" text-anchor="middle" fill="var(--emerald)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="13">TYPE II ANODIZE</text>
    <text x="519" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8.5" opacity=".6">H&#8322;SO&#8324; 15% &bull; 68&ndash;72&deg;F</text>
    <text x="519" y="70" text-anchor="middle" fill="var(--emerald)" font-family="JetBrains Mono,monospace" font-size="8" opacity=".7">KEY STAGE 2</text>
    <line x1="603" y1="27" x2="627" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="627,24 633,27 627,30" fill="currentColor" opacity=".3"/>
    <rect x="637" y="8" width="80" height="38" rx="7" fill="rgba(120,120,140,.08)" stroke="var(--muted)" stroke-width="1"/>
    <text x="677" y="24" text-anchor="middle" fill="var(--muted)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">DYE</text>
    <text x="677" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">Optional Light</text>
    <line x1="721" y1="27" x2="745" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="745,24 751,27 745,30" fill="currentColor" opacity=".3"/>
    <rect x="755" y="8" width="100" height="38" rx="7" fill="rgba(232,160,32,.08)" stroke="var(--amber)" stroke-width="1" stroke-dasharray="5,3"/>
    <text x="805" y="24" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">SEAL</text>
    <text x="805" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">Hot DI / NiAc</text>
    <line x1="10" y1="58" x2="858" y2="58" stroke="currentColor" stroke-width="1.5" opacity=".12" stroke-dasharray="8,4"/>
    <text x="883" y="62" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" opacity=".35" letter-spacing=".06em">LINE</text>
</svg>""",
            "svg_title": "Bright Anodize Process Flow <span class=\"sub\">bright dip line</span>",
            "app_title": "Application Guide <span class=\"sub\">by alloy</span>",
            "app_headers": ("Alloy", "Bright Result", "Reflectance", "Common Use"),
            "app_rows": [
                ("5657 (bright)", "&gt;85% specular", "Excellent", "Automotive trim, reflectors"),
                ("6463 (bright)", "80&ndash;85% specular", "Very good", "Architectural extrusions"),
                ("1100 / 3003", "75&ndash;82% specular", "Good", "Lighting, nameplates"),
                ("6061", "65&ndash;75% specular", "Moderate", "Industrial decorative"),
            ],
            "dyk_text": "The best alloys for bright anodizing are specifically designed for it. <strong style=\"color:var(--amber);\">Alloy 5657</strong> (Al-0.8Mg) and <strong style=\"color:var(--amber);\">6463</strong> (Al-Mg-Si) have tightly controlled impurity limits &mdash; iron and silicon are held below 0.08% and 0.04% respectively because these elements form intermetallic particles that scatter light and create dark spots during brightening. Standard alloys like 6061 (0.7% Fe + Si allowed) simply cannot achieve the same mirror-like reflectance no matter how perfect the processing is.",
            "bath_title": "Bright Dip Chemistry <span class=\"sub\">chemical</span>",
            "bath_rows": [
                ("Phosphoric Acid", "75&ndash;85 vol%"),
                ("Nitric Acid", "3&ndash;5 vol%"),
                ("Dissolved Al", "15&ndash;40 g/L"),
                ("Temperature", "190&ndash;220&deg;F"),
                ("Immersion Time", "30&ndash;120 s"),
                ("Agitation", "None or gentle"),
            ],
            "spec_title": "Specifications <span class=\"sub\">common</span>",
            "spec_rows": [
                ("ASTM B580", "Anodic coatings"),
                ("AAMA 611", "Bright anodize (arch.)"),
                ("ASTM D523", "Specular gloss"),
                ("ASTM E430", "Specular reflectance"),
            ],
            "compare_title": "Bright Anodize vs Standard Type II <span class=\"sub\">finish quality</span>",
            "do_title": "Bright Anodize <span class=\"tag good\">Choose When</span>",
            "do_items": [
                "Mirror-like reflective finish required",
                "Decorative or architectural application",
                "High-purity alloy (5657, 6463) available",
                "Reflector, lighting, or trim application",
                "Premium appearance is the primary goal",
            ],
            "dont_title": "Standard Type II <span class=\"tag bad\">Choose Instead</span>",
            "dont_items": [
                "Matte or satin finish preferred",
                "Standard alloys (6061, 7075) must be used",
                "Cost is the primary concern",
                "Opaque dye colors needed (dark black, etc.)",
                "Functional corrosion protection only",
            ],
            "footer_title": "Bright Anodizing Demystified &mdash; Anodizing Series",
            "footer_disclaimer": "Technical reference only. Verify all parameters against your chemistry supplier&rsquo;s TDS, customer specifications, and applicable regulatory requirements before production use.",
        },
        "es": {
            "eyebrow": "Plating Posters &middot; Anodizado &middot; Anodizado Brillante &middot; Descripci&oacute;n",
            "headline": "ANODIZADO<br><em>BRILLANTE</em>",
            "subhead": "Abrillantado Qu&iacute;mico + Tipo II &mdash; Acabados Espejo en Aluminio",
            "tagline": "Un proceso multi-etapa que combina abrillantado qu&iacute;mico o electroqu&iacute;mico con anodizado est&aacute;ndar de &aacute;cido sulf&uacute;rico para producir superficies altamente reflectivas para aplicaciones arquitect&oacute;nicas, automotrices y decorativas.",
            "rule_num": "5&ndash;20",
            "rule_label": "Espesor T&iacute;pico del &Oacute;xido (&micro;m) &mdash; Anodizado Brillante (Tipo II sobre Superficie Abrillantada)",
            "rule_text": "El anodizado brillante es un Tipo II est&aacute;ndar sobre una superficie abrillantada qu&iacute;mica o electroqu&iacute;micamente. El abrillantado suaviza la micro-rugosidad para lograr &gt;80% de reflectancia especular; el anodizado subsecuente protege esta superficie manteniendo la claridad.",
            "process_title": "Secuencia T&iacute;pica del Proceso <span class=\"sub\">l&iacute;nea de abrillantado</span>",
            "process_rows": [
                ("01", "Limpieza / Desengrase Alcalino", "54&ndash;71&deg;C", "3&ndash;5 min", "Eliminar aceites; evitar rayado"),
                ("02", "Enjuague", "Ambiente", "30&ndash;60 s", "Rebose; prevenir arrastre"),
                ("03", "Ataque Alcalino (muy ligero)", "54&ndash;60&deg;C", "15&ndash;60 s", "M&iacute;nima remoci&oacute;n; preservar acabado"),
                ("04", "Enjuague", "Ambiente", "30&ndash;60 s", "Eliminar residuos del ataque"),
                ("05", "Ba&ntilde;o Brillante / Electropulido", "82&ndash;104&deg;C", "30&ndash;120 s", "Mezcla H&#8323;PO&#8324;/HNO&#8323;; o EP an&oacute;dico"),
                ("06", "Enjuague (multi-etapa)", "Ambiente", "1&ndash;2 min", "Eliminar &aacute;cido; prevenir manchas"),
                ("07", "Desmanchar (si es necesario)", "Ambiente", "15&ndash;30 s", "HNO&#8323; ligero para aleaciones con Cu"),
                ("08", "Anodizado con &Aacute;cido Sulf&uacute;rico", "20&ndash;22&deg;C", "20&ndash;40 min", "Tipo II est&aacute;ndar; menor DC para claridad"),
                ("09", "Tinte Claro o Ligero (opc.)", "54&ndash;60&deg;C", "2&ndash;10 min", "Dorado, champa&ntilde;a, o solo sellado"),
                ("10", "Sellado", "93&ndash;99&deg;C", "15&ndash;30 min", "Agua DI caliente o sello NiAc"),
            ],
            "insight_label": "C&oacute;mo el Ba&ntilde;o Brillante Crea Superficies Espejo",
            "insight_text": "El abrillantado qu&iacute;mico funciona por disoluci&oacute;n preferencial de los micro-picos. La mezcla concentrada de &aacute;cido fosf&oacute;rico-n&iacute;trico crea una capa l&iacute;mite viscosa sobre los valles mientras los picos sobresalen hacia &aacute;cido fresco y se disuelven m&aacute;s r&aacute;pido. Esto nivela la rugosidad de Ra ~0.5 &micro;m a Ra &lt;0.05 &micro;m, produciendo reflectancia especular superior al 80%. El anodizado transparente subsecuente debe controlarse cuidadosamente &mdash; si es muy grueso, el &oacute;xido dispersa la luz y reduce la reflectividad.",
            "svg_title": "Flujo del Proceso de Anodizado Brillante <span class=\"sub\">l&iacute;nea de abrillantado</span>",
            "app_title": "Gu&iacute;a de Aplicaci&oacute;n <span class=\"sub\">por aleaci&oacute;n</span>",
            "app_headers": ("Aleaci&oacute;n", "Resultado Brillante", "Reflectancia", "Uso Com&uacute;n"),
            "app_rows": [
                ("5657 (brillante)", "&gt;85% especular", "Excelente", "Molduras automotrices, reflectores"),
                ("6463 (brillante)", "80&ndash;85% especular", "Muy buena", "Extrusiones arquitect&oacute;nicas"),
                ("1100 / 3003", "75&ndash;82% especular", "Buena", "Iluminaci&oacute;n, placas"),
                ("6061", "65&ndash;75% especular", "Moderada", "Decorativo industrial"),
            ],
            "dyk_text": "Las mejores aleaciones para anodizado brillante est&aacute;n dise&ntilde;adas espec&iacute;ficamente para ello. La <strong style=\"color:var(--amber);\">aleaci&oacute;n 5657</strong> (Al-0.8Mg) y la <strong style=\"color:var(--amber);\">6463</strong> (Al-Mg-Si) tienen l&iacute;mites de impurezas estrictamente controlados &mdash; hierro y silicio se mantienen por debajo de 0.08% y 0.04% porque forman part&iacute;culas intermet&aacute;licas que dispersan la luz. Aleaciones est&aacute;ndar como 6061 simplemente no pueden lograr la misma reflectancia espejo.",
            "bath_title": "Qu&iacute;mica del Ba&ntilde;o Brillante <span class=\"sub\">qu&iacute;mico</span>",
            "bath_rows": [
                ("&Aacute;cido Fosf&oacute;rico", "75&ndash;85 vol%"),
                ("&Aacute;cido N&iacute;trico", "3&ndash;5 vol%"),
                ("Al Disuelto", "15&ndash;40 g/L"),
                ("Temperatura", "88&ndash;104&deg;C"),
                ("Tiempo Inmersi&oacute;n", "30&ndash;120 s"),
                ("Agitaci&oacute;n", "Ninguna o suave"),
            ],
            "spec_title": "Especificaciones <span class=\"sub\">comunes</span>",
            "spec_rows": [
                ("ASTM B580", "Recubrimientos an&oacute;dicos"),
                ("AAMA 611", "Anod. brillante (arq.)"),
                ("ASTM D523", "Brillo especular"),
                ("ASTM E430", "Reflectancia especular"),
            ],
            "compare_title": "Anod. Brillante vs Tipo II Est&aacute;ndar <span class=\"sub\">calidad de acabado</span>",
            "do_title": "Anodizado Brillante <span class=\"tag good\">Elegir Cuando</span>",
            "do_items": [
                "Se requiere acabado reflectivo tipo espejo",
                "Aplicaci&oacute;n decorativa o arquitect&oacute;nica",
                "Aleaci&oacute;n de alta pureza disponible (5657, 6463)",
                "Aplicaci&oacute;n de reflector, iluminaci&oacute;n o moldura",
                "La apariencia premium es el objetivo principal",
            ],
            "dont_title": "Tipo II Est&aacute;ndar <span class=\"tag bad\">Elegir En Su Lugar</span>",
            "dont_items": [
                "Se prefiere acabado mate o sat&iacute;n",
                "Se deben usar aleaciones est&aacute;ndar (6061, 7075)",
                "El costo es la preocupaci&oacute;n principal",
                "Se necesitan colores de tinte opacos (negro, etc.)",
                "Solo protecci&oacute;n funcional contra corrosi&oacute;n",
            ],
            "footer_title": "Anodizado Brillante Desmitificado &mdash; Serie de Anodizado",
            "footer_disclaimer": "Referencia t&eacute;cnica solamente. Verifique todos los par&aacute;metros contra la TDS de su proveedor, especificaciones del cliente y requisitos regulatorios aplicables antes del uso en producci&oacute;n.",
        },
    },

    # ======================================================================
    # 7. INTEGRAL COLOR ANODIZING
    # ======================================================================
    "integral_color": {
        "prefix": "Integ Color",
        "footer_code": "PP-IntColor-00-T",
        "en": {
            "eyebrow": "Plating Posters &middot; Anodizing &middot; Integral Color &middot; Overview",
            "headline": "INTEGRAL COLOR<br><em>ANODIZING</em>",
            "subhead": "Organic Acid Electrolytes &mdash; Permanent, UV-Stable Color from the Oxide Itself",
            "tagline": "Color generated within the anodic oxide by the electrolyte and alloy chemistry &mdash; not by dyes. Integral color produces bronze, gold, and dark brown/black finishes that are completely UV-stable and will not fade over decades of outdoor exposure.",
            "rule_num": "25&ndash;50",
            "rule_label": "Typical Oxide Thickness (&micro;m) &mdash; Integral Color Anodize",
            "rule_text": "Integral color anodizing uses organic acid electrolytes (oxalic, sulfosalicylic, or mixed organic/sulfuric) to grow thick oxide layers that incorporate color-producing compounds directly into the oxide structure. At 25&ndash;50 &micro;m, the color is part of the coating itself &mdash; it cannot fade, scratch off, or bleed out like organic dyes.",
            "process_title": "Typical Process Sequence <span class=\"sub\">rack line</span>",
            "process_rows": [
                ("01", "Alkaline Clean / Degrease", "130&ndash;160&deg;F", "3&ndash;5 min", "Remove oils and soils"),
                ("02", "Rinse", "Ambient", "30&ndash;60 s", "Overflow counterflow"),
                ("03", "Alkaline Etch (controlled)", "130&ndash;150&deg;F", "2&ndash;5 min", "Uniform surface; NaOH 40&ndash;60 g/L"),
                ("04", "Rinse", "Ambient", "30&ndash;60 s", "Remove etch residue"),
                ("05", "Desmut / Deoxidize", "Ambient", "1&ndash;3 min", "HNO&#8323; + HF deoxidize"),
                ("06", "Rinse", "Ambient", "30&ndash;60 s", "Clean surface for anodize"),
                ("07", "Integral Color Anodize", "68&ndash;80&deg;F", "30&ndash;90 min", "Organic acid blend; 50&ndash;80 V; AC/DC"),
                ("08", "Rinse", "Ambient", "1&ndash;2 min", "Multi-stage counterflow"),
                ("09", "Seal", "200&ndash;210&deg;F", "20&ndash;30 min", "Hot DI water or NiAc seal"),
                ("10", "Inspect / QC", "Ambient", "As req.", "Color match, thickness, seal QC"),
            ],
            "insight_label": "How Integral Color Creates Permanent Color",
            "insight_text": "In conventional dyeing, color molecules sit inside open pores and can be degraded by UV light over time. Integral color works differently &mdash; the organic acid electrolyte (oxalic acid, sulfosalicylic acid, or proprietary blends) decomposes during anodizing and deposits carbon-rich compounds directly into the growing oxide lattice. These compounds absorb light at specific wavelengths, creating bronze, gold, or dark brown colors that are embedded in the crystal structure itself. Because the color is part of the oxide &mdash; not adsorbed on pore walls &mdash; it is completely immune to UV degradation, making integral color the gold standard for architectural facades.",
            "svg": """<svg viewBox="0 0 1060 80" width="100%" height="65" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="10" y="8" width="95" height="38" rx="7" fill="rgba(46,196,182,.10)" stroke="var(--teal)" stroke-width="1.5"/>
    <text x="57" y="24" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">CLEAN</text>
    <text x="57" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">Alk Degrease</text>
    <line x1="109" y1="27" x2="133" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="133,24 139,27 133,30" fill="currentColor" opacity=".3"/>
    <rect x="143" y="8" width="80" height="38" rx="7" fill="rgba(224,92,92,.10)" stroke="var(--coral)" stroke-width="1.2"/>
    <text x="183" y="24" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">ETCH</text>
    <text x="183" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">NaOH Uniform</text>
    <line x1="227" y1="27" x2="251" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="251,24 257,27 251,30" fill="currentColor" opacity=".3"/>
    <rect x="261" y="8" width="95" height="38" rx="7" fill="rgba(120,120,140,.08)" stroke="var(--muted)" stroke-width="1"/>
    <text x="308" y="24" text-anchor="middle" fill="var(--muted)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">DESMUT</text>
    <text x="308" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">HNO&#8323; Deox</text>
    <line x1="360" y1="27" x2="384" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="384,24 390,27 384,30" fill="currentColor" opacity=".3"/>
    <rect x="394" y="4" width="200" height="46" rx="8" fill="rgba(232,160,32,.12)" stroke="var(--amber)" stroke-width="2"/>
    <text x="494" y="22" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="13">INTEGRAL COLOR ANODIZE</text>
    <text x="494" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8.5" opacity=".6">Organic Acid &bull; 50&ndash;80 V &bull; AC/DC</text>
    <text x="494" y="70" text-anchor="middle" fill="var(--amber)" font-family="JetBrains Mono,monospace" font-size="8" opacity=".7">KEY STAGE</text>
    <line x1="598" y1="27" x2="622" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="622,24 628,27 622,30" fill="currentColor" opacity=".3"/>
    <rect x="632" y="8" width="80" height="38" rx="7" fill="rgba(120,120,140,.08)" stroke="var(--muted)" stroke-width="1"/>
    <text x="672" y="24" text-anchor="middle" fill="var(--muted)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">RINSE</text>
    <text x="672" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">Multi-Stage</text>
    <line x1="716" y1="27" x2="740" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="740,24 746,27 740,30" fill="currentColor" opacity=".3"/>
    <rect x="750" y="8" width="100" height="38" rx="7" fill="rgba(232,160,32,.08)" stroke="var(--amber)" stroke-width="1" stroke-dasharray="5,3"/>
    <text x="800" y="24" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">SEAL</text>
    <text x="800" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">Hot DI / NiAc</text>
    <line x1="10" y1="58" x2="853" y2="58" stroke="currentColor" stroke-width="1.5" opacity=".12" stroke-dasharray="8,4"/>
    <text x="878" y="62" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" opacity=".35" letter-spacing=".06em">LINE</text>
</svg>""",
            "svg_title": "Integral Color Anodize Process Flow <span class=\"sub\">rack line</span>",
            "app_title": "Application Guide <span class=\"sub\">color range</span>",
            "app_headers": ("Color", "Thickness", "UV Stability", "Common Use"),
            "app_rows": [
                ("Light Bronze", "25&ndash;30 &micro;m", "Excellent (20+ yr)", "Architectural curtain walls"),
                ("Medium Bronze", "30&ndash;40 &micro;m", "Excellent (20+ yr)", "Window frames, storefronts"),
                ("Dark Bronze", "35&ndash;45 &micro;m", "Excellent (20+ yr)", "Building columns, mullions"),
                ("Black / Charcoal", "40&ndash;50 &micro;m", "Excellent (20+ yr)", "Premium facades, accents"),
            ],
            "dyk_text": "Integral color anodizing requires <strong style=\"color:var(--amber);\">very high voltage</strong> (50&ndash;80 V) compared to standard Type II (14&ndash;18 V), and often uses AC/DC or pulsed current. The high voltage is needed to drive the organic acid decomposition products into the oxide. Power consumption is 3&ndash;5&times; higher than Type II, and the thick oxide layer means <strong style=\"color:var(--amber);\">significant dimensional change</strong> (~12&ndash;25 &micro;m per side). This is why integral color is primarily used on architectural extrusions where precise dimensions are less critical than permanent color.",
            "bath_title": "Bath Chemistry <span class=\"sub\">organic acid</span>",
            "bath_rows": [
                ("Electrolyte", "Proprietary organic blend"),
                ("Sulfuric Acid", "0&ndash;5% (some formulas)"),
                ("Oxalic Acid", "3&ndash;10% (typical)"),
                ("Temperature", "68&ndash;80&deg;F"),
                ("Voltage", "50&ndash;80 V (AC/DC)"),
                ("Time", "30&ndash;90 min"),
            ],
            "spec_title": "Specifications <span class=\"sub\">common</span>",
            "spec_rows": [
                ("AAMA 612", "Class I integral color"),
                ("ASTM B580", "Anodic coatings"),
                ("Qualanod", "European quality label"),
                ("ASTM D2244", "Color difference"),
            ],
            "compare_title": "Integral Color vs Dyed Anodize <span class=\"sub\">color permanence</span>",
            "do_title": "Integral Color <span class=\"tag good\">Choose When</span>",
            "do_items": [
                "Maximum UV stability required (20+ years)",
                "Architectural facade or outdoor signage",
                "Bronze/gold/brown/black color range fits",
                "No organic dye degradation acceptable",
                "Premium long-life appearance required",
            ],
            "dont_title": "Dyed Type II <span class=\"tag bad\">Choose Instead</span>",
            "dont_items": [
                "Bright colors needed (red, blue, green, etc.)",
                "Tight dimensional tolerances required",
                "Lower cost per piece is priority",
                "Standard alloys without color matching issues",
                "Indoor use (UV exposure not a concern)",
            ],
            "footer_title": "Integral Color Anodizing Demystified &mdash; Anodizing Series",
            "footer_disclaimer": "Technical reference only. Verify all parameters against your chemistry supplier&rsquo;s TDS, customer specifications, and applicable regulatory requirements before production use.",
        },
        "es": {
            "eyebrow": "Plating Posters &middot; Anodizado &middot; Color Integral &middot; Descripci&oacute;n",
            "headline": "ANODIZADO DE<br><em>COLOR INTEGRAL</em>",
            "subhead": "Electrolitos de &Aacute;cido Org&aacute;nico &mdash; Color Permanente y Estable al UV del Propio &Oacute;xido",
            "tagline": "Color generado dentro del &oacute;xido an&oacute;dico por el electrolito y la qu&iacute;mica de la aleaci&oacute;n &mdash; no por tintes. Produce acabados bronce, dorado y marr&oacute;n/negro completamente estables al UV que no se desvanecen en d&eacute;cadas de exposici&oacute;n exterior.",
            "rule_num": "25&ndash;50",
            "rule_label": "Espesor T&iacute;pico del &Oacute;xido (&micro;m) &mdash; Anodizado de Color Integral",
            "rule_text": "El anodizado de color integral usa electrolitos de &aacute;cido org&aacute;nico (ox&aacute;lico, sulfosalic&iacute;lico, o mezclas org&aacute;nicas/sulf&uacute;ricas) para generar capas gruesas de &oacute;xido que incorporan compuestos productores de color directamente en la estructura. A 25&ndash;50 &micro;m, el color es parte del recubrimiento &mdash; no puede desvanecerse ni desprenderse.",
            "process_title": "Secuencia T&iacute;pica del Proceso <span class=\"sub\">l&iacute;nea de bastidor</span>",
            "process_rows": [
                ("01", "Limpieza / Desengrase Alcalino", "54&ndash;71&deg;C", "3&ndash;5 min", "Eliminar aceites y suciedad"),
                ("02", "Enjuague", "Ambiente", "30&ndash;60 s", "Contracorriente con rebose"),
                ("03", "Ataque Alcalino (controlado)", "54&ndash;66&deg;C", "2&ndash;5 min", "Superficie uniforme; NaOH 40&ndash;60 g/L"),
                ("04", "Enjuague", "Ambiente", "30&ndash;60 s", "Eliminar residuos del ataque"),
                ("05", "Desmanchar / Desoxidar", "Ambiente", "1&ndash;3 min", "Desoxidar con HNO&#8323; + HF"),
                ("06", "Enjuague", "Ambiente", "30&ndash;60 s", "Superficie limpia para anodizado"),
                ("07", "Anodizado de Color Integral", "20&ndash;27&deg;C", "30&ndash;90 min", "Mezcla &aacute;cida org&aacute;nica; 50&ndash;80 V; AC/DC"),
                ("08", "Enjuague", "Ambiente", "1&ndash;2 min", "Contracorriente multi-etapa"),
                ("09", "Sellado", "93&ndash;99&deg;C", "20&ndash;30 min", "Agua DI caliente o sello NiAc"),
                ("10", "Inspecci&oacute;n / QC", "Ambiente", "Seg&uacute;n req.", "Igualaci&oacute;n de color, espesor, QC de sellado"),
            ],
            "insight_label": "C&oacute;mo el Color Integral Crea Color Permanente",
            "insight_text": "En el te&ntilde;ido convencional, las mol&eacute;culas de color se alojan en poros abiertos y pueden degradarse con UV. El color integral funciona diferente &mdash; el electrolito de &aacute;cido org&aacute;nico se descompone durante el anodizado y deposita compuestos ricos en carbono directamente en la red cristalina del &oacute;xido. Estos compuestos absorben luz a longitudes de onda espec&iacute;ficas, creando colores bronce, dorado o marr&oacute;n oscuro incrustados en la estructura cristalina. Como el color es parte del &oacute;xido, es completamente inmune a la degradaci&oacute;n UV.",
            "svg_title": "Flujo del Proceso de Color Integral <span class=\"sub\">l&iacute;nea de bastidor</span>",
            "app_title": "Gu&iacute;a de Aplicaci&oacute;n <span class=\"sub\">rango de color</span>",
            "app_headers": ("Color", "Espesor", "Estabilidad UV", "Uso Com&uacute;n"),
            "app_rows": [
                ("Bronce Claro", "25&ndash;30 &micro;m", "Excelente (20+ a&ntilde;os)", "Muros cortina arquitect&oacute;nicos"),
                ("Bronce Medio", "30&ndash;40 &micro;m", "Excelente (20+ a&ntilde;os)", "Marcos de ventana, vitrinas"),
                ("Bronce Oscuro", "35&ndash;45 &micro;m", "Excelente (20+ a&ntilde;os)", "Columnas, montantes"),
                ("Negro / Carb&oacute;n", "40&ndash;50 &micro;m", "Excelente (20+ a&ntilde;os)", "Fachadas premium, acentos"),
            ],
            "dyk_text": "El anodizado de color integral requiere <strong style=\"color:var(--amber);\">voltaje muy alto</strong> (50&ndash;80 V) comparado con el Tipo II est&aacute;ndar (14&ndash;18 V), y frecuentemente usa corriente AC/DC o pulsada. El alto voltaje es necesario para impulsar los productos de descomposici&oacute;n del &aacute;cido org&aacute;nico hacia el &oacute;xido. El consumo de energ&iacute;a es 3&ndash;5 veces mayor que el Tipo II, y la capa gruesa significa un <strong style=\"color:var(--amber);\">cambio dimensional significativo</strong> (~12&ndash;25 &micro;m por lado).",
            "bath_title": "Qu&iacute;mica del Ba&ntilde;o <span class=\"sub\">&aacute;cido org&aacute;nico</span>",
            "bath_rows": [
                ("Electrolito", "Mezcla org&aacute;nica propietaria"),
                ("&Aacute;cido Sulf&uacute;rico", "0&ndash;5% (algunas f&oacute;rmulas)"),
                ("&Aacute;cido Ox&aacute;lico", "3&ndash;10% (t&iacute;pico)"),
                ("Temperatura", "20&ndash;27&deg;C"),
                ("Voltaje", "50&ndash;80 V (AC/DC)"),
                ("Tiempo", "30&ndash;90 min"),
            ],
            "spec_title": "Especificaciones <span class=\"sub\">comunes</span>",
            "spec_rows": [
                ("AAMA 612", "Clase I color integral"),
                ("ASTM B580", "Recubrimientos an&oacute;dicos"),
                ("Qualanod", "Sello de calidad europeo"),
                ("ASTM D2244", "Diferencia de color"),
            ],
            "compare_title": "Color Integral vs Anodizado Te&ntilde;ido <span class=\"sub\">permanencia del color</span>",
            "do_title": "Color Integral <span class=\"tag good\">Elegir Cuando</span>",
            "do_items": [
                "M&aacute;xima estabilidad UV requerida (20+ a&ntilde;os)",
                "Fachada arquitect&oacute;nica o se&ntilde;alizaci&oacute;n exterior",
                "El rango bronce/dorado/marr&oacute;n/negro es adecuado",
                "Degradaci&oacute;n de tintes org&aacute;nicos inaceptable",
                "Apariencia premium de larga vida requerida",
            ],
            "dont_title": "Tipo II Te&ntilde;ido <span class=\"tag bad\">Elegir En Su Lugar</span>",
            "dont_items": [
                "Se necesitan colores brillantes (rojo, azul, verde)",
                "Se requieren tolerancias dimensionales estrechas",
                "Menor costo por pieza es prioridad",
                "Aleaciones est&aacute;ndar sin problemas de igualaci&oacute;n",
                "Uso interior (exposici&oacute;n UV no es preocupaci&oacute;n)",
            ],
            "footer_title": "Anodizado de Color Integral Desmitificado &mdash; Serie de Anodizado",
            "footer_disclaimer": "Referencia t&eacute;cnica solamente. Verifique todos los par&aacute;metros contra la TDS de su proveedor, especificaciones del cliente y requisitos regulatorios aplicables antes del uso en producci&oacute;n.",
        },
    },

    # ======================================================================
    # 8. TWO-STEP (ELECTROLYTIC) COLOR ANODIZING
    # ======================================================================
    "two_step": {
        "prefix": "2-Step Color",
        "footer_code": "PP-2Step-00-T",
        "en": {
            "eyebrow": "Plating Posters &middot; Anodizing &middot; Two-Step Electrolytic Color &middot; Overview",
            "headline": "TWO-STEP<br><em>COLOR ANODIZING</em>",
            "subhead": "Electrolytic Metal Salt Deposition &mdash; UV-Stable Architectural Color",
            "tagline": "A two-stage process: standard sulfuric acid anodize first, then AC or DC electrolytic deposition of metal salts (tin, cobalt, nickel) into the pore bases to produce a bronze-to-black color range that is completely UV-stable for exterior architectural use.",
            "rule_num": "15&ndash;25",
            "rule_label": "Typical Oxide Thickness (&micro;m) &mdash; Two-Step Electrolytic Color Anodize",
            "rule_text": "The first step grows a standard Type II oxide layer (15&ndash;25 &micro;m). The second step deposits metal (Sn, Co, or Ni) into the pore bases using AC or pulsed DC current. Color depth is controlled by deposition time &mdash; from champagne (30 s) through medium bronze (2&ndash;4 min) to black (8&ndash;12 min). The metal sits at the bottom of the pores, protected by the oxide above.",
            "process_title": "Typical Process Sequence <span class=\"sub\">two-step line</span>",
            "process_rows": [
                ("01", "Alkaline Clean / Degrease", "130&ndash;160&deg;F", "3&ndash;5 min", "Remove oils and soils"),
                ("02", "Rinse", "Ambient", "30&ndash;60 s", "Overflow counterflow"),
                ("03", "Alkaline Etch", "130&ndash;150&deg;F", "2&ndash;5 min", "Uniform matte; NaOH 40&ndash;60 g/L"),
                ("04", "Rinse", "Ambient", "30&ndash;60 s", "Remove etch residue"),
                ("05", "Desmut / Deoxidize", "Ambient", "1&ndash;3 min", "HNO&#8323; deoxidize"),
                ("06", "Sulfuric Acid Anodize", "68&ndash;72&deg;F", "30&ndash;50 min", "Type II; 15&ndash;25 &micro;m; 12&ndash;18 ASF"),
                ("07", "Rinse", "Ambient", "1&ndash;2 min", "Multi-stage; no seal before color"),
                ("08", "Electrolytic Color", "Ambient", "0.5&ndash;12 min", "SnSO&#8324; or CoSO&#8324; bath; 12&ndash;18 VAC"),
                ("09", "Rinse", "Ambient", "30&ndash;60 s", "Remove excess electrolyte"),
                ("10", "Seal", "200&ndash;210&deg;F", "20&ndash;30 min", "Hot DI water or NiAc seal"),
            ],
            "insight_label": "Why Two-Step Color Is the Architectural Standard",
            "insight_text": "Two-step electrolytic coloring combines the best of both worlds: the well-proven, economical sulfuric acid anodize line (Step 1) with a short electrolytic coloring bath (Step 2). Unlike integral color, which requires expensive organic acid electrolytes and very high voltage, two-step uses a simple metal salt solution at low voltage (12&ndash;18 VAC). The metal deposits only at the pore bases where the barrier layer is thinnest, creating color from the bottom up. Because the metal is protected under 15&ndash;25 &micro;m of clear oxide, it is completely shielded from UV and weathering, providing the same 20+ year color stability as integral color at significantly lower cost.",
            "svg": """<svg viewBox="0 0 1060 80" width="100%" height="65" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="10" y="8" width="95" height="38" rx="7" fill="rgba(46,196,182,.10)" stroke="var(--teal)" stroke-width="1.5"/>
    <text x="57" y="24" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">CLEAN</text>
    <text x="57" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">Alk + Etch</text>
    <line x1="109" y1="27" x2="133" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="133,24 139,27 133,30" fill="currentColor" opacity=".3"/>
    <rect x="143" y="8" width="95" height="38" rx="7" fill="rgba(120,120,140,.08)" stroke="var(--muted)" stroke-width="1"/>
    <text x="190" y="24" text-anchor="middle" fill="var(--muted)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">DESMUT</text>
    <text x="190" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">HNO&#8323; Deox</text>
    <line x1="242" y1="27" x2="266" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="266,24 272,27 266,30" fill="currentColor" opacity=".3"/>
    <rect x="276" y="4" width="155" height="46" rx="8" fill="rgba(232,160,32,.12)" stroke="var(--amber)" stroke-width="2"/>
    <text x="353" y="22" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="12">STEP 1: ANODIZE</text>
    <text x="353" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8.5" opacity=".6">H&#8322;SO&#8324; Type II &bull; 15&ndash;25 &micro;m</text>
    <text x="353" y="70" text-anchor="middle" fill="var(--amber)" font-family="JetBrains Mono,monospace" font-size="8" opacity=".7">OXIDE GROWTH</text>
    <line x1="435" y1="27" x2="459" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="459,24 465,27 459,30" fill="currentColor" opacity=".3"/>
    <rect x="469" y="8" width="80" height="38" rx="7" fill="rgba(120,120,140,.08)" stroke="var(--muted)" stroke-width="1"/>
    <text x="509" y="24" text-anchor="middle" fill="var(--muted)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">RINSE</text>
    <text x="509" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">No Seal Yet</text>
    <line x1="553" y1="27" x2="577" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="577,24 583,27 577,30" fill="currentColor" opacity=".3"/>
    <rect x="587" y="4" width="165" height="46" rx="8" fill="rgba(39,174,96,.12)" stroke="var(--emerald)" stroke-width="2"/>
    <text x="669" y="22" text-anchor="middle" fill="var(--emerald)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="12">STEP 2: COLOR</text>
    <text x="669" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8.5" opacity=".6">Sn/Co salt &bull; AC 12&ndash;18 V</text>
    <text x="669" y="70" text-anchor="middle" fill="var(--emerald)" font-family="JetBrains Mono,monospace" font-size="8" opacity=".7">METAL DEPOSITION</text>
    <line x1="756" y1="27" x2="780" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="780,24 786,27 780,30" fill="currentColor" opacity=".3"/>
    <rect x="790" y="8" width="100" height="38" rx="7" fill="rgba(232,160,32,.08)" stroke="var(--amber)" stroke-width="1" stroke-dasharray="5,3"/>
    <text x="840" y="24" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">SEAL</text>
    <text x="840" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">Hot DI / NiAc</text>
    <line x1="10" y1="58" x2="893" y2="58" stroke="currentColor" stroke-width="1.5" opacity=".12" stroke-dasharray="8,4"/>
    <text x="918" y="62" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" opacity=".35" letter-spacing=".06em">LINE</text>
</svg>""",
            "svg_title": "Two-Step Color Anodize Flow <span class=\"sub\">two-step line</span>",
            "app_title": "Application Guide <span class=\"sub\">color by time</span>",
            "app_headers": ("Color", "Color Time", "Metal Salt", "UV Stability"),
            "app_rows": [
                ("Champagne / Light", "30&ndash;60 s", "Tin or Cobalt", "Excellent &mdash; 20+ yr"),
                ("Medium Bronze", "2&ndash;4 min", "Tin or Cobalt", "Excellent &mdash; 20+ yr"),
                ("Dark Bronze", "5&ndash;8 min", "Tin or Cobalt", "Excellent &mdash; 20+ yr"),
                ("Black", "8&ndash;12 min", "Tin + Cobalt or Nickel", "Excellent &mdash; 20+ yr"),
            ],
            "dyk_text": "The most widely used two-step process is <strong style=\"color:var(--amber);\">Sandalor</strong> (Clariant), which uses stannous sulfate (tin) as the coloring salt. The AC current causes tin to deposit preferentially at the pore base during the cathodic half-cycle, while the anodic half-cycle prevents over-deposition. Color is controlled purely by time &mdash; the bath chemistry, voltage, and temperature stay constant. This makes two-step coloring remarkably <strong style=\"color:var(--amber);\">reproducible</strong> &mdash; a facility can match colors batch-to-batch simply by controlling immersion time to &plusmn;5 seconds.",
            "bath_title": "Color Bath Chemistry <span class=\"sub\">step 2</span>",
            "bath_rows": [
                ("Stannous Sulfate", "10&ndash;25 g/L"),
                ("Sulfuric Acid", "15&ndash;25 g/L"),
                ("Stabilizer", "Per supplier TDS"),
                ("Temperature", "68&ndash;77&deg;F"),
                ("Voltage", "12&ndash;18 VAC"),
                ("Time", "0.5&ndash;12 min"),
            ],
            "spec_title": "Specifications <span class=\"sub\">common</span>",
            "spec_rows": [
                ("AAMA 611", "Class I colored anodize"),
                ("ASTM B580", "Anodic coatings"),
                ("Qualanod", "European quality label"),
                ("ASTM D2244", "Color difference"),
            ],
            "compare_title": "Two-Step Color vs Organic Dye <span class=\"sub\">color method</span>",
            "do_title": "Two-Step (Electrolytic) <span class=\"tag good\">Choose When</span>",
            "do_items": [
                "Exterior architectural use (UV exposure)",
                "Bronze/brown/black color range needed",
                "20+ year color warranty required",
                "Batch-to-batch color consistency critical",
                "Existing Type II line can add step 2",
            ],
            "dont_title": "Organic Dye <span class=\"tag bad\">Choose Instead</span>",
            "dont_items": [
                "Bright colors needed (red, blue, green, etc.)",
                "Indoor application (no UV concern)",
                "Single-piece or prototype production",
                "Custom color matching (Pantone, RAL)",
                "Lower capital investment preferred",
            ],
            "footer_title": "Two-Step (Electrolytic) Color Anodizing Demystified &mdash; Anodizing Series",
            "footer_disclaimer": "Technical reference only. Verify all parameters against your chemistry supplier&rsquo;s TDS, customer specifications, and applicable regulatory requirements before production use.",
        },
        "es": {
            "eyebrow": "Plating Posters &middot; Anodizado &middot; Color Electrol&iacute;tico de Dos Pasos &middot; Descripci&oacute;n",
            "headline": "ANODIZADO COLOR<br><em>DOS PASOS</em>",
            "subhead": "Deposici&oacute;n Electrol&iacute;tica de Sales Met&aacute;licas &mdash; Color Arquitect&oacute;nico Estable al UV",
            "tagline": "Un proceso de dos etapas: primero anodizado est&aacute;ndar con &aacute;cido sulf&uacute;rico, luego deposici&oacute;n electrol&iacute;tica AC o DC de sales met&aacute;licas (esta&ntilde;o, cobalto, n&iacute;quel) en las bases de los poros para producir un rango de color bronce a negro completamente estable al UV.",
            "rule_num": "15&ndash;25",
            "rule_label": "Espesor T&iacute;pico del &Oacute;xido (&micro;m) &mdash; Anodizado Color Electrol&iacute;tico de Dos Pasos",
            "rule_text": "El primer paso genera una capa est&aacute;ndar Tipo II (15&ndash;25 &micro;m). El segundo deposita metal (Sn, Co o Ni) en las bases de los poros usando corriente AC o DC pulsada. La profundidad del color se controla por tiempo de deposici&oacute;n &mdash; desde champa&ntilde;a (30 s) hasta bronce medio (2&ndash;4 min) y negro (8&ndash;12 min).",
            "process_title": "Secuencia T&iacute;pica del Proceso <span class=\"sub\">l&iacute;nea de dos pasos</span>",
            "process_rows": [
                ("01", "Limpieza / Desengrase Alcalino", "54&ndash;71&deg;C", "3&ndash;5 min", "Eliminar aceites y suciedad"),
                ("02", "Enjuague", "Ambiente", "30&ndash;60 s", "Contracorriente con rebose"),
                ("03", "Ataque Alcalino", "54&ndash;66&deg;C", "2&ndash;5 min", "Mate uniforme; NaOH 40&ndash;60 g/L"),
                ("04", "Enjuague", "Ambiente", "30&ndash;60 s", "Eliminar residuos del ataque"),
                ("05", "Desmanchar / Desoxidar", "Ambiente", "1&ndash;3 min", "Desoxidar con HNO&#8323;"),
                ("06", "Anodizado con &Aacute;cido Sulf&uacute;rico", "20&ndash;22&deg;C", "30&ndash;50 min", "Tipo II; 15&ndash;25 &micro;m; 1.3&ndash;1.9 A/dm&sup2;"),
                ("07", "Enjuague", "Ambiente", "1&ndash;2 min", "Multi-etapa; sin sellar antes del color"),
                ("08", "Color Electrol&iacute;tico", "Ambiente", "0.5&ndash;12 min", "Ba&ntilde;o SnSO&#8324; o CoSO&#8324;; 12&ndash;18 VAC"),
                ("09", "Enjuague", "Ambiente", "30&ndash;60 s", "Eliminar exceso de electrolito"),
                ("10", "Sellado", "93&ndash;99&deg;C", "20&ndash;30 min", "Agua DI caliente o sello NiAc"),
            ],
            "insight_label": "Por Qu&eacute; el Color de Dos Pasos Es el Est&aacute;ndar Arquitect&oacute;nico",
            "insight_text": "El coloreado electrol&iacute;tico de dos pasos combina lo mejor de ambos mundos: la l&iacute;nea econ&oacute;mica y probada de anodizado sulf&uacute;rico (Paso 1) con un breve ba&ntilde;o de coloraci&oacute;n electrol&iacute;tica (Paso 2). A diferencia del color integral, que requiere electrolitos org&aacute;nicos costosos y voltaje muy alto, el de dos pasos usa una soluci&oacute;n simple de sales met&aacute;licas a bajo voltaje (12&ndash;18 VAC). El metal se deposita solo en las bases de los poros donde la capa barrera es m&aacute;s delgada, creando color de abajo hacia arriba. Protegido bajo 15&ndash;25 &micro;m de &oacute;xido transparente, ofrece la misma estabilidad de color de 20+ a&ntilde;os que el color integral a menor costo.",
            "svg_title": "Flujo del Proceso de Color de Dos Pasos <span class=\"sub\">l&iacute;nea de dos pasos</span>",
            "app_title": "Gu&iacute;a de Aplicaci&oacute;n <span class=\"sub\">color por tiempo</span>",
            "app_headers": ("Color", "Tiempo Color", "Sal Met&aacute;lica", "Estabilidad UV"),
            "app_rows": [
                ("Champa&ntilde;a / Claro", "30&ndash;60 s", "Esta&ntilde;o o Cobalto", "Excelente &mdash; 20+ a&ntilde;os"),
                ("Bronce Medio", "2&ndash;4 min", "Esta&ntilde;o o Cobalto", "Excelente &mdash; 20+ a&ntilde;os"),
                ("Bronce Oscuro", "5&ndash;8 min", "Esta&ntilde;o o Cobalto", "Excelente &mdash; 20+ a&ntilde;os"),
                ("Negro", "8&ndash;12 min", "Esta&ntilde;o + Cobalto o N&iacute;quel", "Excelente &mdash; 20+ a&ntilde;os"),
            ],
            "dyk_text": "El proceso de dos pasos m&aacute;s utilizado es <strong style=\"color:var(--amber);\">Sandalor</strong> (Clariant), que usa sulfato estannoso (esta&ntilde;o) como sal colorante. La corriente AC hace que el esta&ntilde;o se deposite preferencialmente en la base del poro durante el semiciclo cat&oacute;dico, mientras el semiciclo an&oacute;dico previene sobre-deposici&oacute;n. El color se controla puramente por tiempo &mdash; la qu&iacute;mica, voltaje y temperatura permanecen constantes. Esto hace que el coloreado sea notablemente <strong style=\"color:var(--amber);\">reproducible</strong> &mdash; igualando colores lote a lote controlando el tiempo a &plusmn;5 segundos.",
            "bath_title": "Qu&iacute;mica del Ba&ntilde;o de Color <span class=\"sub\">paso 2</span>",
            "bath_rows": [
                ("Sulfato Estannoso", "10&ndash;25 g/L"),
                ("&Aacute;cido Sulf&uacute;rico", "15&ndash;25 g/L"),
                ("Estabilizador", "Seg&uacute;n TDS del proveedor"),
                ("Temperatura", "20&ndash;25&deg;C"),
                ("Voltaje", "12&ndash;18 VAC"),
                ("Tiempo", "0.5&ndash;12 min"),
            ],
            "spec_title": "Especificaciones <span class=\"sub\">comunes</span>",
            "spec_rows": [
                ("AAMA 611", "Clase I anodizado coloreado"),
                ("ASTM B580", "Recubrimientos an&oacute;dicos"),
                ("Qualanod", "Sello de calidad europeo"),
                ("ASTM D2244", "Diferencia de color"),
            ],
            "compare_title": "Color Dos Pasos vs Tinte Org&aacute;nico <span class=\"sub\">m&eacute;todo de color</span>",
            "do_title": "Dos Pasos (Electrol&iacute;tico) <span class=\"tag good\">Elegir Cuando</span>",
            "do_items": [
                "Uso arquitect&oacute;nico exterior (exposici&oacute;n UV)",
                "Rango de color bronce/marr&oacute;n/negro necesario",
                "Se requiere garant&iacute;a de color de 20+ a&ntilde;os",
                "Consistencia de color lote a lote es cr&iacute;tica",
                "L&iacute;nea Tipo II existente puede agregar paso 2",
            ],
            "dont_title": "Tinte Org&aacute;nico <span class=\"tag bad\">Elegir En Su Lugar</span>",
            "dont_items": [
                "Se necesitan colores brillantes (rojo, azul, verde)",
                "Aplicaci&oacute;n interior (sin preocupaci&oacute;n UV)",
                "Producci&oacute;n de pieza &uacute;nica o prototipo",
                "Igualaci&oacute;n de color personalizado (Pantone, RAL)",
                "Se prefiere menor inversi&oacute;n de capital",
            ],
            "footer_title": "Anodizado Color Electrol&iacute;tico de Dos Pasos Desmitificado &mdash; Serie de Anodizado",
            "footer_disclaimer": "Referencia t&eacute;cnica solamente. Verifique todos los par&aacute;metros contra la TDS de su proveedor, especificaciones del cliente y requisitos regulatorios aplicables antes del uso en producci&oacute;n.",
        },
    },
}


# -- HTML TEMPLATE ------------------------------------------------------------

def build_html(poster_key, lang, edition):
    """Return complete HTML string for one poster variant."""
    p = POSTERS[poster_key]
    d = p[lang]
    is_light = (edition == "light")
    edition_attr = ' data-edition="light"' if is_light else ''
    html_lang = "es" if lang == "es" else "en"

    # Build process sequence rows
    proc_rows = ""
    for num, stage, temp, time, param in d["process_rows"]:
        proc_rows += f'            <tr><td class="mono">{num}</td><td>{stage}</td><td class="mono">{temp}</td><td class="mono">{time}</td><td>{param}</td></tr>\n'

    # Build application guide rows
    app_rows = ""
    for row in d["app_rows"]:
        cells = "".join(f'<td class="mono">{c}</td>' if i > 0 else f'<td>{c}</td>' for i, c in enumerate(row))
        app_rows += f"              <tr>{cells}</tr>\n"

    # Build app table headers
    app_th = "".join(f"<th>{h}</th>" for h in d["app_headers"])

    # Build bath chemistry rows
    bath_rows = ""
    for param, val in d["bath_rows"]:
        bath_rows += f'              <tr><td>{param}</td><td class="mono">{val}</td></tr>\n'

    # Build spec rows
    spec_rows = ""
    for code, scope in d["spec_rows"]:
        spec_rows += f'              <tr><td class="mono">{code}</td><td>{scope}</td></tr>\n'

    # Build compare lists
    do_items = "".join(f"            <li>{item}</li>\n" for item in d["do_items"])
    dont_items = "".join(f"            <li>{item}</li>\n" for item in d["dont_items"])

    # DYK label
    dyk_label = "&iquest;Sab&iacute;a Usted?" if lang == "es" else "Did You Know?"

    # SVG: use EN version for both languages
    svg_content = POSTERS[poster_key]["en"]["svg"]

    return f"""<!DOCTYPE html>
<html lang="{html_lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{p['prefix']} &mdash; {d['footer_title'].split(' &mdash; ')[0]} &mdash; Technical | Plating Posters Inc</title>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@800;900&family=Barlow:wght@600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
{CSS}
</style>
</head>
<body>
<div class="stage">
<div class="poster-wrap" id="posterWrap">
<div class="poster" id="poster"{edition_attr}>
  <span class="tack tl" aria-hidden="true"></span><span class="tack tr" aria-hidden="true"></span>
  <span class="tack bl" aria-hidden="true"></span><span class="tack br" aria-hidden="true"></span>
  <div class="poster-header">
    <header class="header-band">
      <div class="header-left">
        <div class="eyebrow"><span>{d['eyebrow']}</span></div>
        <h1 class="headline">{d['headline']}</h1>
        <h2 class="subhead">{d['subhead']}</h2>
        <p class="tagline">{d['tagline']}</p>
      </div>
      <aside class="glass logo-card">
        <div class="logo-tile"><span>PP</span></div>
        <div class="logo-word"><span class="a">Plating</span> <span class="b">Posters</span></div>
        <div class="logo-inc">www.platingposters.com</div>
      </aside>
    </header>
  </div>
  <div class="poster-body">
    <div class="glass rule-card">
      <div class="rule-num">{d['rule_num']}</div>
      <div class="rule-body">
        <div class="rule-label">{d['rule_label']}</div>
        <div class="rule-text">{d['rule_text']}</div>
      </div>
    </div>

    <div>
      <h3 class="section-title">{d['process_title']}</h3>
      <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
        <table class="data-table compact">
          <thead><tr><th style="width:28px;">#</th><th>{'Etapa' if lang == 'es' else 'Stage'}</th><th>Temp</th><th>{'Tiempo' if lang == 'es' else 'Time'}</th><th>{'Par&aacute;metro Clave' if lang == 'es' else 'Key Parameter'}</th></tr></thead>
          <tbody>
{proc_rows}          </tbody>
        </table>
      </div>
    </div>

    <div class="insight-card">
      <div class="insight-label">{d['insight_label']}</div>
      <div class="insight-text">{d['insight_text']}</div>
    </div>

    <div class="glass" style="padding:8px 16px;">
      <h3 class="section-title" style="margin-bottom:4px;">{d['svg_title']}</h3>
      {svg_content}
    </div>

    <div class="bottom-grid">
      <div>
        <h3 class="section-title">{d['app_title']}</h3>
        <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
          <table class="data-table bath">
            <thead><tr>{app_th}</tr></thead>
            <tbody>
{app_rows}            </tbody>
          </table>
        </div>

        <div class="glass" style="padding:10px 16px;border-left:3px solid var(--amber);margin-top:8px;">
  <div style="font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:16px;color:var(--amber);letter-spacing:.08em;text-transform:uppercase;margin-bottom:3px;">{dyk_label}</div>
      <div style="font-family:'Inter',sans-serif;font-size:12.5px;color:var(--text);line-height:1.5;">{d['dyk_text']}</div>
</div>
      </div>
      <div>
        <h3 class="section-title">{d['bath_title']}</h3>
        <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
          <table class="data-table bath">
            <thead><tr><th>{'Par&aacute;metro' if lang == 'es' else 'Parameter'}</th><th>{'Rango' if lang == 'es' else 'Range'}</th></tr></thead>
            <tbody>
{bath_rows}            </tbody>
          </table>
        </div>
        <h3 class="section-title" style="margin-top:10px;">{d['spec_title']}</h3>
        <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
          <table class="data-table bath">
            <thead><tr><th>{'C&oacute;digo' if lang == 'es' else 'Code'}</th><th>{'Alcance' if lang == 'es' else 'Scope'}</th></tr></thead>
            <tbody>
{spec_rows}            </tbody>
          </table>
        </div>
      </div>
    </div>

    <div>
      <h3 class="section-title">{d['compare_title']}</h3>
      <div class="compare-grid">
        <div class="glass compare-card do" style="padding:8px 14px;">
          <h4 style="font-size:18px;margin-bottom:5px;">{d['do_title']}</h4>
          <ul>
{do_items}          </ul>
        </div>
        <div class="glass compare-card dont" style="padding:8px 14px;">
          <h4 style="font-size:18px;margin-bottom:5px;">{d['dont_title']}</h4>
          <ul>
{dont_items}          </ul>
        </div>
      </div>
    </div>
  </div>
  <footer class="footer poster-footer">
    <p class="footer-disclaimer">{d['footer_disclaimer']}</p>
    <p class="footer-title">{d['footer_title']}</p>
    <span class="footer-brand">Plating Posters &middot; Metal Finishing Reference Series &middot; {p['footer_code']} / v1.0 / 2026</span>
  </footer>
</div>
</div>
</div>
<div class="tweaks">
  <div style="display:flex;gap:6px;align-items:center;">
    <span style="color:rgba(240,237,232,.5);font-size:11px;letter-spacing:.06em;text-transform:uppercase;">Edition</span>
    <button id="btnDark" style="padding:4px 10px;border-radius:5px;cursor:pointer;font-size:11px;background:{'transparent' if is_light else '#E8A020'};color:{'#F0EDE8' if is_light else '#1A1F2E'};border:1px solid {'rgba(255,255,255,.2)' if is_light else '#E8A020'};" onclick="setEdition('')">Dark</button>
    <button id="btnLight" style="padding:4px 10px;border-radius:5px;cursor:pointer;font-size:11px;background:{'#E8A020' if is_light else 'transparent'};color:{'#1A1F2E' if is_light else '#F0EDE8'};border:1px solid {'#E8A020' if is_light else 'rgba(255,255,255,.2)'};" onclick="setEdition('light')">Light</button>
  </div>
  <button onclick="window.print()" style="padding:4px 11px;border-radius:5px;cursor:pointer;font-size:11px;background:transparent;color:#F0EDE8;border:1px solid rgba(255,255,255,.2);">Print / PDF</button>
</div>
<script>
{JS}
</script>
</body>
</html>"""


# -- FILE NAME MAP ------------------------------------------------------------

TITLE_MAP = {
    "type_ii":        "Sulfuric Acid Anodizing (Type II) Demystified",
    "hardcoat":       "Hardcoat Anodizing (Type III) Demystified",
    "type_i":         "Chromic Acid Anodizing (Type I) Demystified",
    "bsaa":           "Boric-Sulfuric Acid Anodizing (BSAA) Demystified",
    "paa":            "Phosphoric Acid Anodizing (PAA) Demystified",
    "bright":         "Bright Anodizing Demystified",
    "integral_color": "Integral Color Anodizing Demystified",
    "two_step":       "Two-Step Electrolytic Color Anodizing Demystified",
}

TITLE_MAP_ES = {
    "type_ii":        "Anodizado con Acido Sulfurico (Tipo II) Desmitificado",
    "hardcoat":       "Anodizado Hardcoat (Tipo III) Desmitificado",
    "type_i":         "Anodizado con Acido Cromico (Tipo I) Desmitificado",
    "bsaa":           "Anodizado Borico-Sulfurico (BSAA) Desmitificado",
    "paa":            "Anodizado con Acido Fosforico (PAA) Desmitificado",
    "bright":         "Anodizado Brillante Desmitificado",
    "integral_color": "Anodizado Color Integral Desmitificado",
    "two_step":       "Anodizado Color Electrolitico Dos Pasos Desmitificado",
}


# -- GENERATE -----------------------------------------------------------------

def main():
    count = 0
    for key, p in POSTERS.items():
        prefix = p["prefix"]
        for lang in ("en", "es"):
            for edition in ("dark", "light"):
                lang_label = "EN" if lang == "en" else "ES"
                edition_label = "Dark" if edition == "dark" else "Light"
                title = TITLE_MAP[key] if lang == "en" else TITLE_MAP_ES[key]
                fname = f"{prefix} - 00 - TECHNICAL - {title} - {lang_label} - {edition_label}.html"
                fpath = os.path.join(OUT, fname)
                html = build_html(key, lang, edition)
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(html)
                count += 1
                print(f"  [{count:02d}] {fname}")
    print(f"\nDone -- {count} files written to {OUT}")


if __name__ == "__main__":
    main()
