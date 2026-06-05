#!/usr/bin/env python3
"""Build 4 Electroplating Demystified posters × 4 variants = 16 files."""

import os

OUT = os.path.dirname(os.path.abspath(__file__))

# ── CSS (shared across all posters) ──────────────────────────────────────────
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
.header-band{display:flex;align-items:flex-start;justify-content:space-between;gap:16px;margin-bottom:4px;}.header-left{flex:1;min-width:0;}.eyebrow{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--amber);letter-spacing:.16em;text-transform:uppercase;margin-bottom:4px;display:flex;align-items:center;gap:12px;}.eyebrow::before{content:"";display:inline-block;width:30px;height:3px;background:var(--amber);}.headline{font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:72px;color:var(--text);line-height:.92;margin:4px 0;letter-spacing:-.01em;text-transform:uppercase;}.headline em{font-style:normal;color:var(--amber);}.subhead{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:22px;color:var(--teal);margin:0 0 3px;letter-spacing:.02em;text-transform:uppercase;}.tagline{font-family:'Inter',sans-serif;font-style:italic;font-size:13px;color:var(--muted);line-height:1.45;max-width:700px;margin:0;}
.logo-card{flex-shrink:0;padding:12px 10px;display:flex;flex-direction:column;align-items:center;gap:8px;align-self:flex-start;}.logo-tile{width:68px;height:68px;border-radius:12px;background:linear-gradient(135deg,#E8A020,#2EC4B6);display:flex;align-items:center;justify-content:center;box-shadow:inset 0 1px 0 rgba(255,255,255,.4),inset 0 -2px 4px rgba(0,0,0,.15),0 4px 14px rgba(0,0,0,.35);}.logo-tile span{font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:26px;color:#1A1F2E;letter-spacing:.02em;line-height:1;}.logo-word{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:18px;letter-spacing:.04em;text-transform:uppercase;line-height:1;text-align:center;white-space:nowrap;}.logo-word .a{color:var(--text);}.logo-word .b{color:var(--amber);}.logo-inc{font-family:'JetBrains Mono',monospace;font-size:8.5px;letter-spacing:.05em;text-transform:lowercase;color:var(--muted);margin-top:-2px;}
.section-title{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:28px;letter-spacing:.08em;text-transform:uppercase;color:var(--text);margin:0 0 3px;display:flex;align-items:center;gap:8px;}.section-title::before{content:"";width:6px;height:6px;background:var(--amber);border-radius:50%;}.section-title .sub{font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.14em;color:var(--muted);margin-left:auto;font-weight:500;}
.rule-card{display:flex;align-items:center;gap:20px;padding:12px 22px;background:rgba(232,160,32,.07);}.rule-num{font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:56px;color:var(--amber);line-height:1;letter-spacing:-.02em;}.rule-body{flex:1;}.rule-label{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:19px;color:var(--amber);letter-spacing:.08em;text-transform:uppercase;}.rule-text{font-family:'Inter',sans-serif;font-size:14px;color:var(--muted);line-height:1.5;margin-top:4px;}
.data-table{width:100%;border-collapse:collapse;}.data-table th{font-family:'Barlow',sans-serif;font-weight:700;font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--amber);padding:6px 10px;text-align:left;background:rgba(13,16,32,.35);border-bottom:1px solid var(--glass-border);}.poster[data-edition="light"] .data-table th{background:rgba(27,32,48,.06);}.data-table td{padding:6px 10px;color:var(--text);line-height:1.5;border-bottom:1px solid rgba(255,255,255,.05);font-family:'Inter',sans-serif;font-size:14px;}.data-table tr:last-child td{border-bottom:none;}.data-table tr:nth-child(even) td{background:rgba(255,255,255,.02);}.poster[data-edition="light"] .data-table tr:nth-child(even) td{background:rgba(27,32,48,.025);}.data-table .mono{font-family:'JetBrains Mono',monospace;font-size:13px;}.data-table.compact th{font-size:12px;padding:7px 10px;}.data-table.compact td{padding:6px 10px;font-size:13px;line-height:1.45;}.data-table.compact .mono{font-size:12.5px;}.data-table.bath th{font-size:12px;padding:6px 8px;}.data-table.bath td{padding:5px 8px;font-size:13px;line-height:1.4;}.data-table.bath .mono{font-size:12px;}
.compare-grid{display:grid;grid-template-columns:1fr 1fr;gap:6px;}.compare-card{padding:10px 16px;}.compare-card h4{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:21px;color:var(--text);margin:0 0 8px;text-transform:uppercase;letter-spacing:.04em;}.compare-card h4 .tag{font-size:12px;padding:2px 8px;border-radius:4px;margin-left:8px;font-family:'JetBrains Mono',monospace;font-weight:500;letter-spacing:.06em;}.compare-card h4 .tag.good{background:rgba(39,174,96,.15);color:var(--emerald);}.compare-card h4 .tag.bad{background:rgba(224,92,92,.15);color:var(--coral);}.compare-card ul{list-style:none;padding:0;margin:0;}.compare-card li{font-size:13.5px;line-height:1.5;padding:2px 0;display:flex;gap:8px;align-items:flex-start;}.compare-card li::before{content:"";width:5px;height:5px;border-radius:50%;margin-top:7px;flex-shrink:0;}.compare-card.do li::before{background:var(--emerald);}.compare-card.dont li::before{background:var(--coral);}
.bottom-grid{display:grid;grid-template-columns:1.6fr 1fr;gap:6px;}
.insight-card{padding:14px 18px;border-left:3px solid var(--teal);background:rgba(46,196,182,.06);border-radius:0 12px 12px 0;}.insight-label{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:16px;color:var(--teal);letter-spacing:.08em;text-transform:uppercase;margin-bottom:3px;}.insight-text{font-family:'Inter',sans-serif;font-size:14.5px;color:var(--text);line-height:1.5;}
.safety-card{padding:12px 18px;background:rgba(224,92,92,.08);border:1px solid rgba(224,92,92,.25);border-radius:12px;}.safety-head{font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:20px;color:var(--coral);letter-spacing:.06em;text-transform:uppercase;margin-bottom:5px;}.safety-body{font-size:14px;color:var(--text);line-height:1.55;}.safety-body strong{font-weight:700;color:var(--coral);}
.footer{padding:10px 20px;background-color:rgba(13,16,32,.85);background-image:linear-gradient(180deg,rgba(255,255,255,.04),rgba(0,0,0,0));border:1px solid rgba(255,255,255,.10);border-radius:8px;text-align:center;display:flex;flex-direction:column;gap:2px;}.poster[data-edition="light"] .footer{background-color:rgba(221,216,206,.95);border-color:rgba(27,32,48,.10);}.footer-disclaimer{font-family:'Inter',sans-serif;font-size:9px;line-height:1.35;color:var(--faint);margin:0 auto;max-width:900px;}.footer-title{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:13px;color:var(--text);letter-spacing:.04em;text-transform:uppercase;margin:0;}.footer-brand{font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--muted);letter-spacing:.12em;text-transform:uppercase;}
.tweaks{position:fixed;bottom:16px;right:16px;z-index:100;background:rgba(13,16,32,.92);border:1px solid rgba(255,255,255,.12);border-radius:10px;padding:10px 14px;display:flex;flex-direction:column;gap:8px;font-family:'Inter',sans-serif;font-size:12px;color:#F0EDE8;}
@media print{@page{size:12.5in 18.75in;margin:0;}html,body{background:#1A1F2E !important;-webkit-print-color-adjust:exact !important;print-color-adjust:exact !important;}*{-webkit-print-color-adjust:exact !important;print-color-adjust:exact !important;}.stage{position:static;padding:0;display:block;overflow:visible;}.poster-wrap{transform:none !important;width:auto !important;height:auto !important;}.poster{box-shadow:none !important;width:1200px !important;height:1800px !important;overflow:hidden !important;}.glass,.insight-card,.safety-card{backdrop-filter:none !important;-webkit-backdrop-filter:none !important;}.tweaks{display:none !important;}}"""

JS = r"""const posterWrap=document.getElementById('posterWrap');const poster=document.getElementById('poster');
function scalePoster(){const sW=(window.innerWidth-24)/1200;const sH=(window.innerHeight-24)/1800;const s=Math.min(sW,sH);posterWrap.style.transform='scale('+s+')';posterWrap.style.transformOrigin='top center';posterWrap.style.width='1200px';posterWrap.style.height=(1800*s)+'px';}
function setEdition(e){if(e)poster.dataset.edition=e;else delete poster.dataset.edition;['Dark','Light'].forEach(function(n){var b=document.getElementById('btn'+n);var active=(n.toLowerCase()===e)||(n==='Dark'&&!e);b.style.background=active?'#E8A020':'transparent';b.style.color=active?'#1A1F2E':'#F0EDE8';b.style.borderColor=active?'#E8A020':'rgba(255,255,255,.2)';})}
scalePoster();window.addEventListener('resize',scalePoster);"""


# ── POSTER DEFINITIONS ───────────────────────────────────────────────────────

POSTERS = {
    # ======================================================================
    # ZINC ALKALINE
    # ======================================================================
    "zinc_alk": {
        "prefix": "Zinc Alk",
        "footer_code": "PP-ZnAlk-00-T",
        "en": {
            "eyebrow": "Plating Posters &middot; Electroplating &middot; Zinc Alkaline &middot; Overview",
            "headline": "ALKALINE<br><em>ZINC PLATING</em>",
            "subhead": "Non-Cyanide Electrodeposition &mdash; The Corrosion Protection Workhorse",
            "tagline": "The dominant zinc process for rack and barrel work &mdash; uniform throwing power, no cyanide, and simple trivalent passivation deliver reliable corrosion protection at scale.",
            "rule_num": "8&ndash;25",
            "rule_label": "Typical Deposit Thickness (&micro;m) &mdash; Rack &amp; Barrel Alkaline Zinc",
            "rule_text": "Alkaline non-cyanide zinc produces a matte-to-bright deposit with excellent throwing power into recesses and barrel loads. At 8&ndash;25 &micro;m with trivalent passivation, alkaline zinc routinely delivers 120&ndash;500+ hours of white corrosion in salt spray depending on thickness and sealant.",
            "process_title": "Typical Process Sequence <span class=\"sub\">rack or barrel</span>",
            "process_rows": [
                ("01", "Alkaline Soak Clean", "140&ndash;180&deg;F", "3&ndash;5 min", "Remove oils, soils, and shop dirt"),
                ("02", "Electroclean (Anodic)", "140&ndash;180&deg;F", "1&ndash;3 min", "Final degrease; anodic avoids hydrogen"),
                ("03", "Rinse", "Ambient", "30&ndash;60 s", "Overflow; conductivity &lt;200 &micro;S"),
                ("04", "Acid Activate", "Ambient", "15&ndash;30 s", "10&ndash;15% HCl &mdash; remove oxides, smut"),
                ("05", "Rinse", "Ambient", "30&ndash;60 s", "Prevent acid drag-in to plating bath"),
                ("06", "Alkaline Zinc Plate", "70&ndash;90&deg;F", "15&ndash;45 min", "NaOH 120&ndash;150 g/L; Zn 8&ndash;15 g/L"),
                ("07", "Drag-Out Rinse", "Ambient", "30 s", "Recover chemistry; extend bath life"),
                ("08", "Acid Dip / Bright Dip", "Ambient", "5&ndash;15 s", "0.25&ndash;0.5% HNO&#8323; activation"),
                ("09", "Trivalent Passivate", "70&ndash;90&deg;F", "30&ndash;90 s", "Cr(III) conversion; clear, blue, or yellow"),
                ("10", "Seal / Dry", "150&ndash;200&deg;F", "5&ndash;10 min", "Optional topcoat sealer; oven dry"),
            ],
            "insight_label": "Why Alkaline Zinc Dominates Industrial Finishing",
            "insight_text": "Alkaline zinc plating replaced toxic cyanide zinc in most facilities by the 1990s while keeping its best trait: outstanding throwing power. The high-pH bath (NaOH-based) distributes zinc uniformly into deep recesses, threads, and barrel loads where acid zinc struggles. It generates less hydrogen embrittlement risk than acid baths, making it preferred for hardened fasteners (Class 10.9+). Combined with trivalent passivation and a topcoat sealer, alkaline zinc is the go-to corrosion barrier for automotive fasteners, brackets, stampings, and general industrial hardware.",
            "svg": """<svg viewBox="0 0 1060 80" width="100%" height="75" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="10" y="8" width="95" height="38" rx="7" fill="rgba(46,196,182,.10)" stroke="var(--teal)" stroke-width="1.5"/>
    <text x="57" y="24" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">CLEAN</text>
    <text x="57" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">Soak + E-Clean</text>
    <line x1="109" y1="27" x2="133" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="133,24 139,27 133,30" fill="currentColor" opacity=".3"/>
    <rect x="143" y="8" width="80" height="38" rx="7" fill="rgba(120,120,140,.08)" stroke="var(--muted)" stroke-width="1"/>
    <text x="183" y="24" text-anchor="middle" fill="var(--muted)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">RINSE</text>
    <text x="183" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">Overflow</text>
    <line x1="227" y1="27" x2="251" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="251,24 257,27 251,30" fill="currentColor" opacity=".3"/>
    <rect x="261" y="8" width="95" height="38" rx="7" fill="rgba(224,92,92,.10)" stroke="var(--coral)" stroke-width="1.2"/>
    <text x="308" y="24" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">ACTIVATE</text>
    <text x="308" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">HCl Dip</text>
    <line x1="360" y1="27" x2="384" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="384,24 390,27 384,30" fill="currentColor" opacity=".3"/>
    <rect x="394" y="4" width="160" height="46" rx="8" fill="rgba(232,160,32,.12)" stroke="var(--amber)" stroke-width="2"/>
    <text x="474" y="22" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="13">ALK ZINC PLATE</text>
    <text x="474" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8.5" opacity=".6">NaOH 120&ndash;150 g/L &bull; 70&ndash;90&deg;F</text>
    <text x="474" y="70" text-anchor="middle" fill="var(--amber)" font-family="JetBrains Mono,monospace" font-size="8" opacity=".7">KEY STAGE</text>
    <line x1="558" y1="27" x2="582" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="582,24 588,27 582,30" fill="currentColor" opacity=".3"/>
    <rect x="592" y="8" width="80" height="38" rx="7" fill="rgba(120,120,140,.08)" stroke="var(--muted)" stroke-width="1"/>
    <text x="632" y="24" text-anchor="middle" fill="var(--muted)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">RINSE</text>
    <text x="632" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">Drag-Out</text>
    <line x1="676" y1="27" x2="700" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="700,24 706,27 700,30" fill="currentColor" opacity=".3"/>
    <rect x="710" y="8" width="115" height="38" rx="7" fill="rgba(39,174,96,.10)" stroke="var(--emerald)" stroke-width="1.2"/>
    <text x="767" y="24" text-anchor="middle" fill="var(--emerald)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">PASSIVATE</text>
    <text x="767" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">Cr(III) Trivalent</text>
    <line x1="829" y1="27" x2="853" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="853,24 859,27 853,30" fill="currentColor" opacity=".3"/>
    <rect x="863" y="8" width="100" height="38" rx="7" fill="rgba(232,160,32,.08)" stroke="var(--amber)" stroke-width="1" stroke-dasharray="5,3"/>
    <text x="913" y="24" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">SEAL / DRY</text>
    <text x="913" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">Topcoat + Oven</text>
    <line x1="10" y1="58" x2="963" y2="58" stroke="currentColor" stroke-width="1.5" opacity=".12" stroke-dasharray="8,4"/>
    <text x="985" y="62" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" opacity=".35" letter-spacing=".06em">LINE</text>
</svg>""",
            "svg_title": "Alkaline Zinc Process Flow <span class=\"sub\">rack / barrel line</span>",
            "app_title": "Application Guide <span class=\"sub\">salt spray hours</span>",
            "app_headers": ("Passivation", "Thickness", "White Rust (hrs)", "Red Rust (hrs)"),
            "app_rows": [
                ("Clear Trivalent", "8&ndash;12 &micro;m", "72&ndash;120", "150&ndash;250"),
                ("Blue Trivalent", "8&ndash;12 &micro;m", "96&ndash;168", "200&ndash;350"),
                ("Yellow/Iridescent Tri", "10&ndash;15 &micro;m", "120&ndash;250", "350&ndash;500"),
                ("Tri + Topcoat Sealer", "12&ndash;25 &micro;m", "200&ndash;500+", "500&ndash;1000+"),
            ],
            "dyk_text": "Alkaline zinc plating was developed in the 1960s as a direct replacement for toxic cyanide zinc baths. The breakthrough was using <strong style=\"color:var(--amber);\">sodium hydroxide</strong> as the complexing agent instead of sodium cyanide, achieving nearly identical throwing power with dramatically lower toxicity. Today, alkaline non-cyanide zinc accounts for over <strong style=\"color:var(--amber);\">60% of all zinc plating</strong> in North America. The process is so forgiving that many job shops run the same bath chemistry for decades with only minor adjustments, making it one of the most &ldquo;set-and-forget&rdquo; plating processes in the industry.",
            "bath_title": "Bath Chemistry <span class=\"sub\">non-cyanide</span>",
            "bath_rows": [
                ("Zinc Metal", "8&ndash;15 g/L"),
                ("Sodium Hydroxide", "120&ndash;150 g/L"),
                ("Brightener", "Per supplier TDS"),
                ("Temperature", "70&ndash;90&deg;F"),
                ("Cathode CD", "10&ndash;40 ASF"),
                ("pH", "&gt;13 (inherent)"),
            ],
            "spec_title": "Specifications <span class=\"sub\">common</span>",
            "spec_rows": [
                ("ASTM B633", "Zinc on iron/steel"),
                ("AMS 2402", "Zinc plating"),
                ("MIL-DTL-12706", "Military zinc plating"),
                ("ISO 2081", "Zinc coatings"),
            ],
            "compare_title": "Alkaline Zinc vs Acid Zinc <span class=\"sub\">when to use each</span>",
            "do_title": "Alkaline Zinc <span class=\"tag good\">Choose When</span>",
            "do_items": [
                "Deep recesses, threads, barrel loads",
                "Hardened steel (reduced HE risk)",
                "Thick deposits needed (&gt;12 &micro;m)",
                "Broad current density tolerance",
                "Simple waste treatment required",
            ],
            "dont_title": "Acid Zinc <span class=\"tag bad\">Choose Instead</span>",
            "dont_items": [
                "Bright decorative finish required",
                "Die castings or zinc substrates",
                "Thinner deposits with high leveling",
                "Faster plating speed needed",
                "Room-temperature operation preferred",
            ],
            "footer_title": "Alkaline Zinc Plating Demystified &mdash; Electroplating Series",
            "footer_disclaimer": "Technical reference only. Verify all parameters against your chemistry supplier&rsquo;s TDS, customer specifications, and applicable regulatory requirements before production use.",
        },
        "es": {
            "eyebrow": "Plating Posters &middot; Electrodeposici&oacute;n &middot; Zinc Alcalino &middot; Descripci&oacute;n",
            "headline": "ZINC<br><em>ALCALINO</em>",
            "subhead": "Electrodeposici&oacute;n Sin Cianuro &mdash; El Caballo de Batalla Anticorrosivo",
            "tagline": "El proceso de zinc dominante para bastidor y tambor &mdash; poder de penetraci&oacute;n uniforme, sin cianuro, y pasivaci&oacute;n trivalente simple ofrecen protecci&oacute;n confiable a escala.",
            "rule_num": "8&ndash;25",
            "rule_label": "Espesor T&iacute;pico del Dep&oacute;sito (&micro;m) &mdash; Zinc Alcalino en Bastidor y Tambor",
            "rule_text": "El zinc alcalino no cianurado produce un dep&oacute;sito mate a brillante con excelente poder de penetraci&oacute;n. A 8&ndash;25 &micro;m con pasivaci&oacute;n trivalente, el zinc alcalino entrega 120&ndash;500+ horas de corrosi&oacute;n blanca en c&aacute;mara salina seg&uacute;n espesor y sellador.",
            "process_title": "Secuencia T&iacute;pica del Proceso <span class=\"sub\">bastidor o tambor</span>",
            "process_rows": [
                ("01", "Limpieza Alcalina por Inmersi&oacute;n", "60&ndash;82&deg;C", "3&ndash;5 min", "Eliminar aceites, suciedad de taller"),
                ("02", "Electrolimpieza (An&oacute;dica)", "60&ndash;82&deg;C", "1&ndash;3 min", "Desengrase final; an&oacute;dica evita hidr&oacute;geno"),
                ("03", "Enjuague", "Ambiente", "30&ndash;60 s", "Rebose; conductividad &lt;200 &micro;S"),
                ("04", "Activaci&oacute;n &Aacute;cida", "Ambiente", "15&ndash;30 s", "10&ndash;15% HCl &mdash; eliminar &oacute;xidos"),
                ("05", "Enjuague", "Ambiente", "30&ndash;60 s", "Prevenir arrastre de &aacute;cido al ba&ntilde;o"),
                ("06", "Zincado Alcalino", "21&ndash;32&deg;C", "15&ndash;45 min", "NaOH 120&ndash;150 g/L; Zn 8&ndash;15 g/L"),
                ("07", "Enjuague de Arrastre", "Ambiente", "30 s", "Recuperar qu&iacute;mica; extender vida del ba&ntilde;o"),
                ("08", "Inmers. &Aacute;cida / Abrillantado", "Ambiente", "5&ndash;15 s", "0.25&ndash;0.5% HNO&#8323; activaci&oacute;n"),
                ("09", "Pasivado Trivalente", "21&ndash;32&deg;C", "30&ndash;90 s", "Cr(III); transparente, azul o amarillo"),
                ("10", "Sellado / Secado", "66&ndash;93&deg;C", "5&ndash;10 min", "Sellador superior opcional; secado en horno"),
            ],
            "insight_label": "Por Qu&eacute; el Zinc Alcalino Domina el Acabado Industrial",
            "insight_text": "El zinc alcalino reemplaz&oacute; al t&oacute;xico zinc cianurado en la mayor&iacute;a de las instalaciones para los a&ntilde;os 90 conservando su mejor cualidad: excelente poder de penetraci&oacute;n. El ba&ntilde;o de alto pH distribuye zinc uniformemente en cavidades profundas, roscas y cargas de tambor. Genera menor riesgo de fragilizaci&oacute;n por hidr&oacute;geno que los ba&ntilde;os &aacute;cidos, haci&eacute;ndolo preferido para torniller&iacute;a endurecida. Combinado con pasivaci&oacute;n trivalente y sellador, el zinc alcalino es la barrera anticorrosiva principal para la industria automotriz y ferreter&iacute;a general.",
            "svg_title": "Flujo del Proceso de Zinc Alcalino <span class=\"sub\">l&iacute;nea bastidor / tambor</span>",
            "app_title": "Gu&iacute;a de Aplicaci&oacute;n <span class=\"sub\">horas en c&aacute;mara salina</span>",
            "app_headers": ("Pasivaci&oacute;n", "Espesor", "Corrosi&oacute;n Blanca", "Corrosi&oacute;n Roja"),
            "app_rows": [
                ("Trivalente Transparente", "8&ndash;12 &micro;m", "72&ndash;120", "150&ndash;250"),
                ("Trivalente Azul", "8&ndash;12 &micro;m", "96&ndash;168", "200&ndash;350"),
                ("Tri Amarillo/Iridiscente", "10&ndash;15 &micro;m", "120&ndash;250", "350&ndash;500"),
                ("Tri + Sellador Superior", "12&ndash;25 &micro;m", "200&ndash;500+", "500&ndash;1000+"),
            ],
            "dyk_text": "El zincado alcalino fue desarrollado en los a&ntilde;os 60 como reemplazo directo de los ba&ntilde;os t&oacute;xicos de zinc cianurado. El avance fue usar <strong style=\"color:var(--amber);\">hidr&oacute;xido de sodio</strong> como agente complejante en lugar de cianuro de sodio, logrando poder de penetraci&oacute;n casi id&eacute;ntico con toxicidad dram&aacute;ticamente menor. Hoy el zinc alcalino no cianurado representa m&aacute;s del <strong style=\"color:var(--amber);\">60% de todo el zincado</strong> en Norteam&eacute;rica. El proceso es tan tolerante que muchos talleres operan la misma qu&iacute;mica durante d&eacute;cadas con ajustes m&iacute;nimos.",
            "bath_title": "Qu&iacute;mica del Ba&ntilde;o <span class=\"sub\">sin cianuro</span>",
            "bath_rows": [
                ("Metal de Zinc", "8&ndash;15 g/L"),
                ("Hidr&oacute;xido de Sodio", "120&ndash;150 g/L"),
                ("Abrillantador", "Seg&uacute;n TDS del proveedor"),
                ("Temperatura", "21&ndash;32&deg;C"),
                ("DC C&aacute;todo", "1&ndash;4 A/dm&sup2;"),
                ("pH", "&gt;13 (inherente)"),
            ],
            "spec_title": "Especificaciones <span class=\"sub\">comunes</span>",
            "spec_rows": [
                ("ASTM B633", "Zinc sobre hierro/acero"),
                ("AMS 2402", "Zincado electrol&iacute;tico"),
                ("MIL-DTL-12706", "Zincado militar"),
                ("ISO 2081", "Recubrimientos de zinc"),
            ],
            "compare_title": "Zinc Alcalino vs Zinc &Aacute;cido <span class=\"sub\">cu&aacute;ndo usar cada uno</span>",
            "do_title": "Zinc Alcalino <span class=\"tag good\">Elegir Cuando</span>",
            "do_items": [
                "Cavidades profundas, roscas, tambor",
                "Acero endurecido (menor riesgo de HE)",
                "Dep&oacute;sitos gruesos (&gt;12 &micro;m)",
                "Amplia tolerancia de densidad de corriente",
                "Tratamiento de residuos simple",
            ],
            "dont_title": "Zinc &Aacute;cido <span class=\"tag bad\">Elegir En Su Lugar</span>",
            "dont_items": [
                "Acabado decorativo brillante requerido",
                "Fundiciones a presi&oacute;n o sustratos de zinc",
                "Dep&oacute;sitos delgados con alto nivelado",
                "Mayor velocidad de deposici&oacute;n",
                "Operaci&oacute;n a temperatura ambiente",
            ],
            "footer_title": "Zinc Alcalino Desmitificado &mdash; Serie de Electrodeposici&oacute;n",
            "footer_disclaimer": "Referencia t&eacute;cnica solamente. Verifique todos los par&aacute;metros contra la TDS de su proveedor, especificaciones del cliente y requisitos regulatorios aplicables antes del uso en producci&oacute;n.",
        },
    },

    # ======================================================================
    # ACID ZINC
    # ======================================================================
    "acid_zinc": {
        "prefix": "Acid Zinc",
        "footer_code": "PP-AcZn-00-T",
        "en": {
            "eyebrow": "Plating Posters &middot; Electroplating &middot; Acid Zinc &middot; Overview",
            "headline": "ACID<br><em>ZINC PLATING</em>",
            "subhead": "High-Brightness Electrodeposition &mdash; Superior Leveling &amp; Speed",
            "tagline": "The bright zinc process for decorative and functional applications &mdash; excellent leveling, fast deposition, and room-temperature operation on a wide range of substrates.",
            "rule_num": "5&ndash;15",
            "rule_label": "Typical Deposit Thickness (&micro;m) &mdash; Bright Acid Zinc",
            "rule_text": "Acid zinc (ammonium chloride or potassium chloride based) delivers bright, leveled deposits directly from the bath. The lower thickness range versus alkaline zinc is typical because the bright, dense deposit and efficient passivation provide excellent corrosion protection per micrometer of coating.",
            "process_title": "Typical Process Sequence <span class=\"sub\">rack or barrel</span>",
            "process_rows": [
                ("01", "Alkaline Soak Clean", "140&ndash;180&deg;F", "3&ndash;5 min", "Remove oils and shop soils"),
                ("02", "Electroclean", "140&ndash;180&deg;F", "1&ndash;3 min", "Cathodic or anodic per substrate"),
                ("03", "Rinse", "Ambient", "30&ndash;60 s", "Overflow rinse"),
                ("04", "Acid Activate", "Ambient", "10&ndash;30 s", "5&ndash;10% HCl &mdash; remove oxides"),
                ("05", "Rinse", "Ambient", "30&ndash;60 s", "Prevent drag-in contamination"),
                ("06", "Acid Zinc Plate", "70&ndash;85&deg;F", "10&ndash;30 min", "pH 4.8&ndash;5.8; Zn 15&ndash;45 g/L"),
                ("07", "Drag-Out / Rinse", "Ambient", "30 s", "Recover chemistry"),
                ("08", "Trivalent Passivate", "70&ndash;90&deg;F", "30&ndash;90 s", "Cr(III) clear, blue, or iridescent"),
                ("09", "Rinse", "Ambient", "30 s", "Remove passivation residue"),
                ("10", "Topcoat Seal / Dry", "150&ndash;200&deg;F", "5&ndash;10 min", "Optional sealer; oven dry"),
            ],
            "insight_label": "Why Acid Zinc for Decorative &amp; High-Speed Work",
            "insight_text": "Acid zinc excels where brightness and leveling matter. The chloride-based electrolyte plates at higher current efficiencies (95&ndash;99%) than alkaline baths, enabling faster deposition. The deposit&rsquo;s fine grain structure produces a mirror-bright finish directly from the bath without post-polishing. Acid zinc also plates well on die castings and zinc alloy substrates where alkaline baths can cause preferential attack. The trade-off: reduced throwing power means acid zinc struggles in deep recesses and barrel work compared to alkaline processes.",
            "svg": """<svg viewBox="0 0 1060 80" width="100%" height="75" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="10" y="8" width="95" height="38" rx="7" fill="rgba(46,196,182,.10)" stroke="var(--teal)" stroke-width="1.5"/>
    <text x="57" y="24" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">CLEAN</text>
    <text x="57" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">Soak + E-Clean</text>
    <line x1="109" y1="27" x2="133" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="133,24 139,27 133,30" fill="currentColor" opacity=".3"/>
    <rect x="143" y="8" width="80" height="38" rx="7" fill="rgba(120,120,140,.08)" stroke="var(--muted)" stroke-width="1"/>
    <text x="183" y="24" text-anchor="middle" fill="var(--muted)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">RINSE</text>
    <text x="183" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">Overflow</text>
    <line x1="227" y1="27" x2="251" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="251,24 257,27 251,30" fill="currentColor" opacity=".3"/>
    <rect x="261" y="8" width="95" height="38" rx="7" fill="rgba(224,92,92,.10)" stroke="var(--coral)" stroke-width="1.2"/>
    <text x="308" y="24" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">ACTIVATE</text>
    <text x="308" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">HCl Dip</text>
    <line x1="360" y1="27" x2="384" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="384,24 390,27 384,30" fill="currentColor" opacity=".3"/>
    <rect x="394" y="4" width="160" height="46" rx="8" fill="rgba(232,160,32,.12)" stroke="var(--amber)" stroke-width="2"/>
    <text x="474" y="22" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="13">ACID ZINC PLATE</text>
    <text x="474" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8.5" opacity=".6">pH 4.8&ndash;5.8 &bull; 70&ndash;85&deg;F</text>
    <text x="474" y="70" text-anchor="middle" fill="var(--amber)" font-family="JetBrains Mono,monospace" font-size="8" opacity=".7">KEY STAGE</text>
    <line x1="558" y1="27" x2="582" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="582,24 588,27 582,30" fill="currentColor" opacity=".3"/>
    <rect x="592" y="8" width="80" height="38" rx="7" fill="rgba(120,120,140,.08)" stroke="var(--muted)" stroke-width="1"/>
    <text x="632" y="24" text-anchor="middle" fill="var(--muted)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">RINSE</text>
    <text x="632" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">Drag-Out</text>
    <line x1="676" y1="27" x2="700" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="700,24 706,27 700,30" fill="currentColor" opacity=".3"/>
    <rect x="710" y="8" width="115" height="38" rx="7" fill="rgba(39,174,96,.10)" stroke="var(--emerald)" stroke-width="1.2"/>
    <text x="767" y="24" text-anchor="middle" fill="var(--emerald)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">PASSIVATE</text>
    <text x="767" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">Cr(III) Trivalent</text>
    <line x1="829" y1="27" x2="853" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="853,24 859,27 853,30" fill="currentColor" opacity=".3"/>
    <rect x="863" y="8" width="100" height="38" rx="7" fill="rgba(232,160,32,.08)" stroke="var(--amber)" stroke-width="1" stroke-dasharray="5,3"/>
    <text x="913" y="24" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">SEAL / DRY</text>
    <text x="913" y="38" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">Topcoat + Oven</text>
    <line x1="10" y1="58" x2="963" y2="58" stroke="currentColor" stroke-width="1.5" opacity=".12" stroke-dasharray="8,4"/>
    <text x="985" y="62" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" opacity=".35" letter-spacing=".06em">LINE</text>
</svg>""",
            "svg_title": "Acid Zinc Process Flow <span class=\"sub\">rack / barrel line</span>",
            "app_title": "Application Guide <span class=\"sub\">finish brightness</span>",
            "app_headers": ("Substrate", "Thickness", "Finish", "Notes"),
            "app_rows": [
                ("Mild Steel", "5&ndash;12 &micro;m", "Mirror-bright", "Standard rack &amp; barrel work"),
                ("Die Castings", "5&ndash;10 &micro;m", "Bright leveled", "Acid preferred over alkaline"),
                ("Spring Steel", "8&ndash;12 &micro;m", "Semi-bright", "HE bake required for high-strength"),
                ("Stampings", "5&ndash;8 &micro;m", "Bright", "High-speed barrel; fast plating"),
            ],
            "dyk_text": "Acid zinc baths achieve current efficiencies of <strong style=\"color:var(--amber);\">95&ndash;99%</strong> compared to only 60&ndash;80% for alkaline zinc, meaning nearly all the electricity goes into depositing zinc rather than generating hydrogen gas. This makes acid zinc significantly faster and more energy-efficient. The potassium chloride formulation (KCl) has largely replaced the older ammonium chloride (NH&#8324;Cl) version because it eliminates ammonia fumes and simplifies waste treatment. Modern acid zinc brightener systems can produce deposits so leveled that they rival the appearance of decorative nickel-chrome finishes at a fraction of the cost.",
            "bath_title": "Bath Chemistry <span class=\"sub\">KCl type</span>",
            "bath_rows": [
                ("Zinc Metal", "15&ndash;45 g/L"),
                ("Potassium Chloride", "180&ndash;220 g/L"),
                ("Boric Acid", "20&ndash;30 g/L"),
                ("pH", "4.8&ndash;5.8"),
                ("Temperature", "70&ndash;85&deg;F"),
                ("Cathode CD", "10&ndash;60 ASF"),
            ],
            "spec_title": "Specifications <span class=\"sub\">common</span>",
            "spec_rows": [
                ("ASTM B633", "Zinc on iron/steel"),
                ("AMS 2402", "Zinc plating"),
                ("GM 6193", "GM zinc plating std"),
                ("ISO 2081", "Zinc coatings"),
            ],
            "compare_title": "Acid Zinc vs Alkaline Zinc <span class=\"sub\">when to use each</span>",
            "do_title": "Acid Zinc <span class=\"tag good\">Choose When</span>",
            "do_items": [
                "Bright decorative finish required",
                "Die castings and zinc alloy substrates",
                "High plating speed / efficiency",
                "Excellent leveling over polished parts",
                "Room-temperature operation",
            ],
            "dont_title": "Alkaline Zinc <span class=\"tag bad\">Choose Instead</span>",
            "dont_items": [
                "Deep recesses, complex barrel loads",
                "High-strength steel (lower HE risk)",
                "Thick deposits &gt;12 &micro;m needed",
                "Wider current density range",
                "Simpler waste treatment",
            ],
            "footer_title": "Acid Zinc Plating Demystified &mdash; Electroplating Series",
            "footer_disclaimer": "Technical reference only. Verify all parameters against your chemistry supplier&rsquo;s TDS, customer specifications, and applicable regulatory requirements before production use.",
        },
        "es": {
            "eyebrow": "Plating Posters &middot; Electrodeposici&oacute;n &middot; Zinc &Aacute;cido &middot; Descripci&oacute;n",
            "headline": "ZINC<br><em>&Aacute;CIDO</em>",
            "subhead": "Electrodeposici&oacute;n de Alto Brillo &mdash; Nivelado y Velocidad Superiores",
            "tagline": "El proceso de zinc brillante para aplicaciones decorativas y funcionales &mdash; excelente nivelado, deposici&oacute;n r&aacute;pida y operaci&oacute;n a temperatura ambiente.",
            "rule_num": "5&ndash;15",
            "rule_label": "Espesor T&iacute;pico del Dep&oacute;sito (&micro;m) &mdash; Zinc &Aacute;cido Brillante",
            "rule_text": "El zinc &aacute;cido (base cloruro de potasio o amonio) entrega dep&oacute;sitos brillantes y nivelados directamente del ba&ntilde;o. El rango inferior de espesor versus zinc alcalino es t&iacute;pico porque el dep&oacute;sito denso y brillante proporciona excelente protecci&oacute;n por micr&oacute;metro de recubrimiento.",
            "process_title": "Secuencia T&iacute;pica del Proceso <span class=\"sub\">bastidor o tambor</span>",
            "process_rows": [
                ("01", "Limpieza Alcalina por Inmersi&oacute;n", "60&ndash;82&deg;C", "3&ndash;5 min", "Eliminar aceites y suciedad"),
                ("02", "Electrolimpieza", "60&ndash;82&deg;C", "1&ndash;3 min", "Cat&oacute;dica o an&oacute;dica seg&uacute;n sustrato"),
                ("03", "Enjuague", "Ambiente", "30&ndash;60 s", "Enjuague con rebose"),
                ("04", "Activaci&oacute;n &Aacute;cida", "Ambiente", "10&ndash;30 s", "5&ndash;10% HCl &mdash; eliminar &oacute;xidos"),
                ("05", "Enjuague", "Ambiente", "30&ndash;60 s", "Prevenir contaminaci&oacute;n por arrastre"),
                ("06", "Zincado &Aacute;cido", "21&ndash;29&deg;C", "10&ndash;30 min", "pH 4.8&ndash;5.8; Zn 15&ndash;45 g/L"),
                ("07", "Arrastre / Enjuague", "Ambiente", "30 s", "Recuperar qu&iacute;mica"),
                ("08", "Pasivado Trivalente", "21&ndash;32&deg;C", "30&ndash;90 s", "Cr(III) transparente, azul o iridiscente"),
                ("09", "Enjuague", "Ambiente", "30 s", "Eliminar residuos de pasivaci&oacute;n"),
                ("10", "Sellado / Secado", "66&ndash;93&deg;C", "5&ndash;10 min", "Sellador opcional; secado en horno"),
            ],
            "insight_label": "Por Qu&eacute; Zinc &Aacute;cido para Trabajo Decorativo y de Alta Velocidad",
            "insight_text": "El zinc &aacute;cido sobresale donde importan el brillo y el nivelado. El electrolito a base de cloruro deposita con eficiencias de corriente superiores (95&ndash;99%) que los ba&ntilde;os alcalinos, permitiendo deposici&oacute;n m&aacute;s r&aacute;pida. La estructura de grano fino produce un acabado brillante espejo directamente del ba&ntilde;o sin pulido posterior. El zinc &aacute;cido tambi&eacute;n deposita bien sobre fundiciones a presi&oacute;n donde los ba&ntilde;os alcalinos pueden causar ataque preferencial. La desventaja: menor poder de penetraci&oacute;n en cavidades profundas.",
            "svg_title": "Flujo del Proceso de Zinc &Aacute;cido <span class=\"sub\">l&iacute;nea bastidor / tambor</span>",
            "app_title": "Gu&iacute;a de Aplicaci&oacute;n <span class=\"sub\">brillo del acabado</span>",
            "app_headers": ("Sustrato", "Espesor", "Acabado", "Notas"),
            "app_rows": [
                ("Acero Dulce", "5&ndash;12 &micro;m", "Espejo brillante", "Trabajo est&aacute;ndar bastidor y tambor"),
                ("Fundiciones", "5&ndash;10 &micro;m", "Brillante nivelado", "&Aacute;cido preferido sobre alcalino"),
                ("Acero de Resorte", "8&ndash;12 &micro;m", "Semi-brillante", "Horneo HE requerido para alta resistencia"),
                ("Estampados", "5&ndash;8 &micro;m", "Brillante", "Tambor alta velocidad; deposici&oacute;n r&aacute;pida"),
            ],
            "dyk_text": "Los ba&ntilde;os de zinc &aacute;cido alcanzan eficiencias de corriente del <strong style=\"color:var(--amber);\">95&ndash;99%</strong> comparado con solo 60&ndash;80% del zinc alcalino, lo que significa que casi toda la electricidad se usa para depositar zinc en vez de generar hidr&oacute;geno. La formulaci&oacute;n de cloruro de potasio (KCl) ha reemplazado en gran medida al antiguo cloruro de amonio (NH&#8324;Cl) porque elimina vapores de amoniaco y simplifica el tratamiento de residuos. Los sistemas modernos de abrillantadores producen dep&oacute;sitos tan nivelados que rivalizan con el acabado de n&iacute;quel-cromo decorativo a una fracci&oacute;n del costo.",
            "bath_title": "Qu&iacute;mica del Ba&ntilde;o <span class=\"sub\">tipo KCl</span>",
            "bath_rows": [
                ("Metal de Zinc", "15&ndash;45 g/L"),
                ("Cloruro de Potasio", "180&ndash;220 g/L"),
                ("&Aacute;cido B&oacute;rico", "20&ndash;30 g/L"),
                ("pH", "4.8&ndash;5.8"),
                ("Temperatura", "21&ndash;29&deg;C"),
                ("DC C&aacute;todo", "1&ndash;6 A/dm&sup2;"),
            ],
            "spec_title": "Especificaciones <span class=\"sub\">comunes</span>",
            "spec_rows": [
                ("ASTM B633", "Zinc sobre hierro/acero"),
                ("AMS 2402", "Zincado electrol&iacute;tico"),
                ("GM 6193", "Est&aacute;ndar zinc de GM"),
                ("ISO 2081", "Recubrimientos de zinc"),
            ],
            "compare_title": "Zinc &Aacute;cido vs Zinc Alcalino <span class=\"sub\">cu&aacute;ndo usar cada uno</span>",
            "do_title": "Zinc &Aacute;cido <span class=\"tag good\">Elegir Cuando</span>",
            "do_items": [
                "Acabado decorativo brillante requerido",
                "Fundiciones a presi&oacute;n y sustratos de zinc",
                "Alta velocidad / eficiencia de deposici&oacute;n",
                "Excelente nivelado sobre piezas pulidas",
                "Operaci&oacute;n a temperatura ambiente",
            ],
            "dont_title": "Zinc Alcalino <span class=\"tag bad\">Elegir En Su Lugar</span>",
            "dont_items": [
                "Cavidades profundas, cargas de tambor",
                "Acero de alta resistencia (menor riesgo HE)",
                "Dep&oacute;sitos gruesos &gt;12 &micro;m",
                "Rango m&aacute;s amplio de densidad de corriente",
                "Tratamiento de residuos m&aacute;s simple",
            ],
            "footer_title": "Zinc &Aacute;cido Desmitificado &mdash; Serie de Electrodeposici&oacute;n",
            "footer_disclaimer": "Referencia t&eacute;cnica solamente. Verifique todos los par&aacute;metros contra la TDS de su proveedor, especificaciones del cliente y requisitos regulatorios aplicables antes del uso en producci&oacute;n.",
        },
    },

    # ======================================================================
    # ZINC-NICKEL
    # ======================================================================
    "znni": {
        "prefix": "ZnNi",
        "footer_code": "PP-ZnNi-00-T",
        "en": {
            "eyebrow": "Plating Posters &middot; Electroplating &middot; Zinc-Nickel &middot; Overview",
            "headline": "ZINC-NICKEL<br><em>PLATING</em>",
            "subhead": "High-Performance Alloy Electrodeposition &mdash; Ultimate Corrosion Protection",
            "tagline": "The premium zinc alloy coating for automotive, aerospace, and defense &mdash; 12&ndash;15% nickel delivers 3&ndash;5&times; the corrosion life of pure zinc at equivalent thickness.",
            "rule_num": "12&ndash;15%",
            "rule_label": "Nickel Content in Deposit &mdash; Critical Alloy Composition",
            "rule_text": "The magic window for zinc-nickel is 12&ndash;15% nickel by weight. Below 10% Ni, you lose the corrosion benefit. Above 18% Ni, the deposit becomes brittle and passivation adhesion degrades. Within the 12&ndash;15% band, the gamma-phase ZnNi intermetallic forms, delivering extraordinary corrosion resistance that satisfies automotive OEM salt-spray requirements.",
            "process_title": "Typical Process Sequence <span class=\"sub\">rack or barrel</span>",
            "process_rows": [
                ("01", "Alkaline Soak Clean", "140&ndash;180&deg;F", "3&ndash;5 min", "Remove oils, soils, drawing compounds"),
                ("02", "Electroclean (Anodic)", "140&ndash;180&deg;F", "1&ndash;3 min", "Anodic preferred for steel"),
                ("03", "Rinse", "Ambient", "30&ndash;60 s", "Overflow; conductivity &lt;200 &micro;S"),
                ("04", "Acid Activate", "Ambient", "15&ndash;30 s", "10&ndash;15% HCl &mdash; remove oxides"),
                ("05", "Rinse", "Ambient", "30&ndash;60 s", "Prevent drag-in"),
                ("06", "Zinc-Nickel Plate", "75&ndash;95&deg;F", "20&ndash;60 min", "Alloy control: 12&ndash;15% Ni target"),
                ("07", "Drag-Out / Rinse", "Ambient", "30&ndash;60 s", "Recover chemistry"),
                ("08", "Trivalent Passivate", "70&ndash;100&deg;F", "45&ndash;120 s", "Thick-film Cr(III) passivation"),
                ("09", "Topcoat Sealer", "Ambient", "30&ndash;60 s", "Organic or inorganic topcoat"),
                ("10", "HE Bake (if req&rsquo;d)", "375&deg;F", "4&ndash;24 hr", "Per spec; within 4 hrs of plating"),
            ],
            "insight_label": "Why ZnNi Is the Automotive &amp; Aerospace Standard",
            "insight_text": "Zinc-nickel has become the premium corrosion protection standard because its gamma-phase intermetallic corrodes 3&ndash;5&times; slower than pure zinc. A 10 &micro;m ZnNi deposit with trivalent passivation and sealer routinely delivers 720&ndash;1,000+ hours to red rust in salt spray. The alloy also offers a higher service temperature ceiling (~250&deg;C vs ~120&deg;C for pure zinc) before the passivation degrades. Every major automotive OEM now specifies zinc-nickel for underbody fasteners, brake components, and structural brackets.",
            "svg": """<svg viewBox="0 0 1060 80" width="100%" height="75" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="5" y="8" width="85" height="38" rx="7" fill="rgba(46,196,182,.10)" stroke="var(--teal)" stroke-width="1.5"/>
    <text x="47" y="24" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="10">CLEAN</text>
    <text x="47" y="37" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="7.5" opacity=".6">Soak+E-Clean</text>
    <line x1="94" y1="27" x2="112" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="112,24 117,27 112,30" fill="currentColor" opacity=".3"/>
    <rect x="121" y="8" width="70" height="38" rx="7" fill="rgba(120,120,140,.08)" stroke="var(--muted)" stroke-width="1"/>
    <text x="156" y="24" text-anchor="middle" fill="var(--muted)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="10">RINSE</text>
    <line x1="195" y1="27" x2="213" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="213,24 218,27 213,30" fill="currentColor" opacity=".3"/>
    <rect x="222" y="8" width="85" height="38" rx="7" fill="rgba(224,92,92,.10)" stroke="var(--coral)" stroke-width="1.2"/>
    <text x="264" y="24" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="10">ACTIVATE</text>
    <text x="264" y="37" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="7.5" opacity=".6">HCl Dip</text>
    <line x1="311" y1="27" x2="329" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="329,24 334,27 329,30" fill="currentColor" opacity=".3"/>
    <rect x="338" y="4" width="155" height="46" rx="8" fill="rgba(232,160,32,.12)" stroke="var(--amber)" stroke-width="2"/>
    <text x="415" y="22" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="12">ZnNi PLATE</text>
    <text x="415" y="37" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">12&ndash;15% Ni &bull; 75&ndash;95&deg;F</text>
    <text x="415" y="70" text-anchor="middle" fill="var(--amber)" font-family="JetBrains Mono,monospace" font-size="8" opacity=".7">KEY STAGE</text>
    <line x1="497" y1="27" x2="515" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="515,24 520,27 515,30" fill="currentColor" opacity=".3"/>
    <rect x="524" y="8" width="70" height="38" rx="7" fill="rgba(120,120,140,.08)" stroke="var(--muted)" stroke-width="1"/>
    <text x="559" y="24" text-anchor="middle" fill="var(--muted)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="10">RINSE</text>
    <line x1="598" y1="27" x2="616" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="616,24 621,27 616,30" fill="currentColor" opacity=".3"/>
    <rect x="625" y="8" width="100" height="38" rx="7" fill="rgba(39,174,96,.10)" stroke="var(--emerald)" stroke-width="1.2"/>
    <text x="675" y="24" text-anchor="middle" fill="var(--emerald)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="10">PASSIVATE</text>
    <text x="675" y="37" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="7.5" opacity=".6">Thick Cr(III)</text>
    <line x1="729" y1="27" x2="747" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="747,24 752,27 747,30" fill="currentColor" opacity=".3"/>
    <rect x="756" y="8" width="80" height="38" rx="7" fill="rgba(46,196,182,.08)" stroke="var(--teal)" stroke-width="1" stroke-dasharray="5,3"/>
    <text x="796" y="24" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="10">SEALER</text>
    <text x="796" y="37" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="7.5" opacity=".6">Topcoat</text>
    <line x1="840" y1="27" x2="858" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="858,24 863,27 858,30" fill="currentColor" opacity=".3"/>
    <rect x="867" y="8" width="95" height="38" rx="7" fill="rgba(224,92,92,.08)" stroke="var(--coral)" stroke-width="1" stroke-dasharray="5,3"/>
    <text x="914" y="24" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="10">HE BAKE</text>
    <text x="914" y="37" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="7.5" opacity=".6">375&deg;F / 4&ndash;24h</text>
    <line x1="5" y1="58" x2="962" y2="58" stroke="currentColor" stroke-width="1.5" opacity=".12" stroke-dasharray="8,4"/>
    <text x="985" y="62" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" opacity=".35" letter-spacing=".06em">LINE</text>
</svg>""",
            "svg_title": "Zinc-Nickel Process Flow <span class=\"sub\">rack / barrel line</span>",
            "app_title": "Application Guide <span class=\"sub\">salt spray hours</span>",
            "app_headers": ("System", "Thickness", "White Rust (hrs)", "Red Rust (hrs)"),
            "app_rows": [
                ("ZnNi + Clear Tri", "8&ndash;10 &micro;m", "200&ndash;400", "500&ndash;720"),
                ("ZnNi + Black Tri", "8&ndash;10 &micro;m", "200&ndash;400", "500&ndash;720"),
                ("ZnNi + Tri + Sealer", "10&ndash;15 &micro;m", "400&ndash;720", "720&ndash;1000+"),
                ("ZnNi + Tri + Seal (thick)", "15&ndash;20 &micro;m", "720&ndash;1000+", "1500+"),
            ],
            "dyk_text": "Zinc-nickel alloy plating was developed in the 1980s for the European automotive industry when OEMs demanded coatings that could survive <strong style=\"color:var(--amber);\">1,000+ hours of salt spray</strong> without red corrosion. The secret is the <strong style=\"color:var(--amber);\">gamma-phase</strong> (&gamma;) intermetallic compound that forms at 12&ndash;15% nickel: it has a more noble corrosion potential than pure zinc, so it corrodes more slowly while still sacrificially protecting the steel substrate. Today, every major automotive specification worldwide (VW TL 244, GM GMW 3359, Toyota TSH 6650) includes zinc-nickel as the preferred fastener coating.",
            "bath_title": "Bath Chemistry <span class=\"sub\">acid or alkaline</span>",
            "bath_rows": [
                ("Zinc Metal", "6&ndash;30 g/L"),
                ("Nickel Metal", "1&ndash;8 g/L"),
                ("Chloride / NaOH", "Per bath type"),
                ("pH (Acid)", "5.5&ndash;6.5"),
                ("pH (Alkaline)", "&gt;13"),
                ("Cathode CD", "5&ndash;50 ASF"),
            ],
            "spec_title": "Specifications <span class=\"sub\">common</span>",
            "spec_rows": [
                ("ASTM B841", "ZnNi on iron/steel"),
                ("AMS 2417", "Aerospace ZnNi"),
                ("VW TL 244", "VW/Audi ZnNi std"),
                ("GM GMW 3359", "GM fastener spec"),
            ],
            "compare_title": "Acid ZnNi vs Alkaline ZnNi <span class=\"sub\">when to use each</span>",
            "do_title": "Acid ZnNi <span class=\"tag good\">Choose When</span>",
            "do_items": [
                "Bright or semi-bright finish needed",
                "Die castings or mixed substrates",
                "Higher plating speed priority",
                "Better leveling on flat parts",
                "Lower operating temperature",
            ],
            "dont_title": "Alkaline ZnNi <span class=\"tag bad\">Choose Instead</span>",
            "dont_items": [
                "Deep recesses or barrel work",
                "Superior alloy uniformity (12&ndash;15% Ni)",
                "High-strength steel (lower HE risk)",
                "Complex geometries",
                "Tighter alloy composition control",
            ],
            "footer_title": "Zinc-Nickel Plating Demystified &mdash; Electroplating Series",
            "footer_disclaimer": "Technical reference only. Verify all parameters against your chemistry supplier&rsquo;s TDS, customer specifications, and applicable regulatory requirements before production use.",
        },
        "es": {
            "eyebrow": "Plating Posters &middot; Electrodeposici&oacute;n &middot; Zinc-N&iacute;quel &middot; Descripci&oacute;n",
            "headline": "ZINC-N&Iacute;QUEL<br><em>ELECTROL&Iacute;TICO</em>",
            "subhead": "Aleaci&oacute;n de Alto Rendimiento &mdash; Protecci&oacute;n Anticorrosiva Superior",
            "tagline": "El recubrimiento premium de aleaci&oacute;n de zinc para automotriz, aeroespacial y defensa &mdash; 12&ndash;15% n&iacute;quel entrega 3&ndash;5&times; la vida anticorrosiva del zinc puro.",
            "rule_num": "12&ndash;15%",
            "rule_label": "Contenido de N&iacute;quel en el Dep&oacute;sito &mdash; Composici&oacute;n Cr&iacute;tica",
            "rule_text": "La ventana m&aacute;gica para zinc-n&iacute;quel es 12&ndash;15% de n&iacute;quel en peso. Por debajo del 10% se pierde el beneficio anticorrosivo. Por encima del 18%, el dep&oacute;sito se vuelve fr&aacute;gil. Dentro de la banda del 12&ndash;15%, se forma el intermet&aacute;lico fase gamma ZnNi, entregando resistencia a la corrosi&oacute;n extraordinaria.",
            "process_title": "Secuencia T&iacute;pica del Proceso <span class=\"sub\">bastidor o tambor</span>",
            "process_rows": [
                ("01", "Limpieza Alcalina por Inmersi&oacute;n", "60&ndash;82&deg;C", "3&ndash;5 min", "Eliminar aceites y compuestos de embutici&oacute;n"),
                ("02", "Electrolimpieza (An&oacute;dica)", "60&ndash;82&deg;C", "1&ndash;3 min", "An&oacute;dica preferida para acero"),
                ("03", "Enjuague", "Ambiente", "30&ndash;60 s", "Rebose; conductividad &lt;200 &micro;S"),
                ("04", "Activaci&oacute;n &Aacute;cida", "Ambiente", "15&ndash;30 s", "10&ndash;15% HCl &mdash; eliminar &oacute;xidos"),
                ("05", "Enjuague", "Ambiente", "30&ndash;60 s", "Prevenir arrastre"),
                ("06", "Zinc-N&iacute;quel Electrol&iacute;tico", "24&ndash;35&deg;C", "20&ndash;60 min", "Control de aleaci&oacute;n: 12&ndash;15% Ni objetivo"),
                ("07", "Arrastre / Enjuague", "Ambiente", "30&ndash;60 s", "Recuperar qu&iacute;mica"),
                ("08", "Pasivado Trivalente", "21&ndash;38&deg;C", "45&ndash;120 s", "Pasivaci&oacute;n Cr(III) de pel&iacute;cula gruesa"),
                ("09", "Sellador Superior", "Ambiente", "30&ndash;60 s", "Sellador org&aacute;nico o inorg&aacute;nico"),
                ("10", "Horneo HE (si req.)", "191&deg;C", "4&ndash;24 hr", "Seg&uacute;n spec; dentro de 4 hrs del dep&oacute;sito"),
            ],
            "insight_label": "Por Qu&eacute; ZnNi Es el Est&aacute;ndar Automotriz y Aeroespacial",
            "insight_text": "El zinc-n&iacute;quel se ha convertido en el est&aacute;ndar premium porque su intermet&aacute;lico fase gamma se corroe 3&ndash;5&times; m&aacute;s lento que el zinc puro. Un dep&oacute;sito de 10 &micro;m con pasivaci&oacute;n trivalente y sellador entrega 720&ndash;1,000+ horas hasta corrosi&oacute;n roja en c&aacute;mara salina. La aleaci&oacute;n tambi&eacute;n ofrece mayor temperatura de servicio (~250&deg;C vs ~120&deg;C del zinc puro). Todo OEM automotriz importante especifica zinc-n&iacute;quel para componentes cr&iacute;ticos.",
            "svg_title": "Flujo del Proceso Zinc-N&iacute;quel <span class=\"sub\">l&iacute;nea bastidor / tambor</span>",
            "app_title": "Gu&iacute;a de Aplicaci&oacute;n <span class=\"sub\">horas en c&aacute;mara salina</span>",
            "app_headers": ("Sistema", "Espesor", "Corrosi&oacute;n Blanca", "Corrosi&oacute;n Roja"),
            "app_rows": [
                ("ZnNi + Tri Transparente", "8&ndash;10 &micro;m", "200&ndash;400", "500&ndash;720"),
                ("ZnNi + Tri Negro", "8&ndash;10 &micro;m", "200&ndash;400", "500&ndash;720"),
                ("ZnNi + Tri + Sellador", "10&ndash;15 &micro;m", "400&ndash;720", "720&ndash;1000+"),
                ("ZnNi + Tri + Sell. (grueso)", "15&ndash;20 &micro;m", "720&ndash;1000+", "1500+"),
            ],
            "dyk_text": "El zinc-n&iacute;quel fue desarrollado en los a&ntilde;os 80 para la industria automotriz europea cuando los OEM exigieron recubrimientos capaces de sobrevivir <strong style=\"color:var(--amber);\">1,000+ horas de c&aacute;mara salina</strong> sin corrosi&oacute;n roja. El secreto es el compuesto intermet&aacute;lico <strong style=\"color:var(--amber);\">fase gamma</strong> (&gamma;) que se forma al 12&ndash;15% de n&iacute;quel: tiene un potencial de corrosi&oacute;n m&aacute;s noble que el zinc puro pero a&uacute;n protege sacrificialmente al acero. Hoy, cada especificaci&oacute;n automotriz importante (VW TL 244, GM GMW 3359, Toyota TSH 6650) incluye zinc-n&iacute;quel como recubrimiento preferido.",
            "bath_title": "Qu&iacute;mica del Ba&ntilde;o <span class=\"sub\">&aacute;cido o alcalino</span>",
            "bath_rows": [
                ("Metal de Zinc", "6&ndash;30 g/L"),
                ("Metal de N&iacute;quel", "1&ndash;8 g/L"),
                ("Cloruro / NaOH", "Seg&uacute;n tipo de ba&ntilde;o"),
                ("pH (&Aacute;cido)", "5.5&ndash;6.5"),
                ("pH (Alcalino)", "&gt;13"),
                ("DC C&aacute;todo", "0.5&ndash;5 A/dm&sup2;"),
            ],
            "spec_title": "Especificaciones <span class=\"sub\">comunes</span>",
            "spec_rows": [
                ("ASTM B841", "ZnNi sobre hierro/acero"),
                ("AMS 2417", "ZnNi aeroespacial"),
                ("VW TL 244", "Est&aacute;ndar ZnNi de VW"),
                ("GM GMW 3359", "Spec torniller&iacute;a GM"),
            ],
            "compare_title": "ZnNi &Aacute;cido vs ZnNi Alcalino <span class=\"sub\">cu&aacute;ndo usar cada uno</span>",
            "do_title": "ZnNi &Aacute;cido <span class=\"tag good\">Elegir Cuando</span>",
            "do_items": [
                "Acabado brillante o semi-brillante",
                "Fundiciones o sustratos mixtos",
                "Prioridad en velocidad de deposici&oacute;n",
                "Mejor nivelado en piezas planas",
                "Menor temperatura de operaci&oacute;n",
            ],
            "dont_title": "ZnNi Alcalino <span class=\"tag bad\">Elegir En Su Lugar</span>",
            "dont_items": [
                "Cavidades profundas o trabajo en tambor",
                "Uniformidad superior de aleaci&oacute;n (12&ndash;15% Ni)",
                "Acero de alta resistencia (menor riesgo HE)",
                "Geometr&iacute;as complejas",
                "Control m&aacute;s estricto de composici&oacute;n",
            ],
            "footer_title": "Zinc-N&iacute;quel Desmitificado &mdash; Serie de Electrodeposici&oacute;n",
            "footer_disclaimer": "Referencia t&eacute;cnica solamente. Verifique todos los par&aacute;metros contra la TDS de su proveedor, especificaciones del cliente y requisitos regulatorios aplicables antes del uso en producci&oacute;n.",
        },
    },

    # ======================================================================
    # BRIGHT NICKEL
    # ======================================================================
    "bright_nickel": {
        "prefix": "Bright Nickel",
        "footer_code": "PP-BrNi-00-T",
        "en": {
            "eyebrow": "Plating Posters &middot; Electroplating &middot; Bright Nickel &middot; Overview",
            "headline": "BRIGHT<br><em>NICKEL</em>",
            "subhead": "Decorative Watts-Type Electroplating &mdash; Brilliance &amp; Corrosion Resistance",
            "tagline": "The mirror-finish workhorse of decorative plating &mdash; leveling brighteners produce a brilliant deposit that underpins chrome, serves as the primary corrosion barrier, and defines the appearance of premium finished goods.",
            "rule_num": "10&ndash;40",
            "rule_label": "Typical Deposit Thickness (&micro;m) &mdash; Bright Nickel (Decorative)",
            "rule_text": "Bright nickel is the thick, leveled layer that provides the bulk of corrosion protection in the nickel-chrome system. At 10&ndash;40 &micro;m, it delivers the mirror finish and mechanical barrier that thin decorative chrome (0.25&ndash;0.75 &micro;m) alone cannot. Automotive trim typically specifies 20&ndash;40 &micro;m of bright nickel under chrome for CASS and Corrodkote performance.",
            "process_title": "Typical Process Sequence <span class=\"sub\">rack line</span>",
            "process_rows": [
                ("01", "Alkaline Soak Clean", "140&ndash;180&deg;F", "3&ndash;5 min", "Remove oils, polishing compounds"),
                ("02", "Electroclean (Anodic)", "140&ndash;180&deg;F", "1&ndash;3 min", "Final degrease; reverse current"),
                ("03", "Rinse", "Ambient", "30&ndash;60 s", "Overflow rinse"),
                ("04", "Acid Activate", "Ambient", "15&ndash;30 s", "10&ndash;20% HCl &mdash; remove oxides"),
                ("05", "Rinse", "Ambient", "30&ndash;60 s", "Prevent acid drag-in"),
                ("06", "Nickel Strike (optional)", "Ambient", "1&ndash;3 min", "Wood&rsquo;s strike for passive metals"),
                ("07", "Bright Nickel Plate", "130&ndash;150&deg;F", "15&ndash;40 min", "NiSO&#8324; 250&ndash;300 g/L; brighteners"),
                ("08", "Rinse", "Ambient", "30&ndash;60 s", "Prevent drag-out to chrome"),
                ("09", "Dec Chrome (optional)", "95&ndash;115&deg;F", "3&ndash;8 min", "Cr(III) or Cr(VI) decorative flash"),
                ("10", "Rinse / Dry", "Ambient", "1&ndash;2 min", "Multi-stage rinse; air dry"),
            ],
            "insight_label": "Why Bright Nickel Is the Heart of Decorative Finishing",
            "insight_text": "In any nickel-chrome plating system, bright nickel is the primary corrosion barrier &mdash; not chrome. Decorative chrome is only 0.25&ndash;0.75 &micro;m thick and exists for appearance and hardness, while bright nickel at 10&ndash;40 &micro;m does the actual corrosion protection work. Brightener additives (Class I carriers + Class II levelers) produce the mirror finish by preferentially depositing into micro-valleys, creating a leveled surface. In duplex or triplex systems, a semi-bright undercoat is used beneath bright nickel to create a potential difference that forces corrosion laterally, dramatically extending coating life.",
            "svg": """<svg viewBox="0 0 1060 80" width="100%" height="75" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="5" y="8" width="85" height="38" rx="7" fill="rgba(46,196,182,.10)" stroke="var(--teal)" stroke-width="1.5"/>
    <text x="47" y="24" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="10">CLEAN</text>
    <text x="47" y="37" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="7.5" opacity=".6">Soak+E-Clean</text>
    <line x1="94" y1="27" x2="112" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="112,24 117,27 112,30" fill="currentColor" opacity=".3"/>
    <rect x="121" y="8" width="70" height="38" rx="7" fill="rgba(120,120,140,.08)" stroke="var(--muted)" stroke-width="1"/>
    <text x="156" y="24" text-anchor="middle" fill="var(--muted)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="10">RINSE</text>
    <line x1="195" y1="27" x2="213" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="213,24 218,27 213,30" fill="currentColor" opacity=".3"/>
    <rect x="222" y="8" width="85" height="38" rx="7" fill="rgba(224,92,92,.10)" stroke="var(--coral)" stroke-width="1.2"/>
    <text x="264" y="24" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="10">ACTIVATE</text>
    <text x="264" y="37" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="7.5" opacity=".6">HCl Dip</text>
    <line x1="311" y1="27" x2="329" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="329,24 334,27 329,30" fill="currentColor" opacity=".3"/>
    <rect x="338" y="8" width="90" height="38" rx="7" fill="rgba(46,196,182,.08)" stroke="var(--teal)" stroke-width="1" stroke-dasharray="5,3"/>
    <text x="383" y="24" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="10">Ni STRIKE</text>
    <text x="383" y="37" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="7.5" opacity=".6">Optional</text>
    <line x1="432" y1="27" x2="450" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="450,24 455,27 450,30" fill="currentColor" opacity=".3"/>
    <rect x="459" y="4" width="155" height="46" rx="8" fill="rgba(232,160,32,.12)" stroke="var(--amber)" stroke-width="2"/>
    <text x="536" y="22" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="12">BRIGHT Ni</text>
    <text x="536" y="37" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="8" opacity=".6">Watts &bull; 130&ndash;150&deg;F</text>
    <text x="536" y="70" text-anchor="middle" fill="var(--amber)" font-family="JetBrains Mono,monospace" font-size="8" opacity=".7">KEY STAGE</text>
    <line x1="618" y1="27" x2="636" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="636,24 641,27 636,30" fill="currentColor" opacity=".3"/>
    <rect x="645" y="8" width="70" height="38" rx="7" fill="rgba(120,120,140,.08)" stroke="var(--muted)" stroke-width="1"/>
    <text x="680" y="24" text-anchor="middle" fill="var(--muted)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="10">RINSE</text>
    <line x1="719" y1="27" x2="737" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="737,24 742,27 737,30" fill="currentColor" opacity=".3"/>
    <rect x="746" y="8" width="110" height="38" rx="7" fill="rgba(144,96,200,.12)" stroke="#9060C8" stroke-width="1.2" stroke-dasharray="5,3"/>
    <text x="801" y="24" text-anchor="middle" fill="#9060C8" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="10">DEC CHROME</text>
    <text x="801" y="37" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="7.5" opacity=".6">Optional Flash</text>
    <line x1="860" y1="27" x2="878" y2="27" stroke="currentColor" stroke-width="1" opacity=".3"/><polygon points="878,24 883,27 878,30" fill="currentColor" opacity=".3"/>
    <rect x="887" y="8" width="75" height="38" rx="7" fill="rgba(232,160,32,.08)" stroke="var(--amber)" stroke-width="1" stroke-dasharray="5,3"/>
    <text x="924" y="24" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="10">DRY</text>
    <text x="924" y="37" text-anchor="middle" fill="currentColor" font-family="Inter,sans-serif" font-weight="500" font-size="7.5" opacity=".6">Air / Oven</text>
    <line x1="5" y1="58" x2="962" y2="58" stroke="currentColor" stroke-width="1.5" opacity=".12" stroke-dasharray="8,4"/>
    <text x="985" y="62" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" opacity=".35" letter-spacing=".06em">LINE</text>
</svg>""",
            "svg_title": "Bright Nickel Process Flow <span class=\"sub\">rack plating line</span>",
            "app_title": "Application Guide <span class=\"sub\">system type</span>",
            "app_headers": ("System", "Bright Ni", "Total Ni", "CASS (hrs)"),
            "app_rows": [
                ("Single-layer Bright", "15&ndash;25 &micro;m", "15&ndash;25 &micro;m", "8&ndash;16"),
                ("Duplex (SB + Bright)", "15&ndash;25 &micro;m", "25&ndash;40 &micro;m", "22&ndash;44"),
                ("Triplex (SB + HB + Bright)", "10&ndash;20 &micro;m", "30&ndash;50 &micro;m", "44&ndash;64+"),
                ("Bright Ni (no chrome)", "20&ndash;40 &micro;m", "20&ndash;40 &micro;m", "N/A &mdash; ASTM B117"),
            ],
            "dyk_text": "The &ldquo;bright&rdquo; in bright nickel comes from organic brightener additives, not from the nickel itself. <strong style=\"color:var(--amber);\">Class I carriers</strong> (like naphthalene sulfonates) reduce surface tension and refine grain, while <strong style=\"color:var(--amber);\">Class II levelers</strong> (like coumarin or propargyl-based compounds) preferentially plate into micro-valleys to create the mirror finish. Without brighteners, a Watts nickel bath produces a matte, slightly yellowish deposit. The sulfur co-deposited from Class II brighteners (0.04&ndash;0.1% S) is actually what creates the electrochemical potential difference that makes duplex nickel corrosion protection work.",
            "bath_title": "Bath Chemistry <span class=\"sub\">Watts type</span>",
            "bath_rows": [
                ("Nickel Sulfate", "250&ndash;300 g/L"),
                ("Nickel Chloride", "40&ndash;60 g/L"),
                ("Boric Acid", "35&ndash;45 g/L"),
                ("pH", "3.5&ndash;4.5"),
                ("Temperature", "130&ndash;150&deg;F"),
                ("Cathode CD", "20&ndash;60 ASF"),
            ],
            "spec_title": "Specifications <span class=\"sub\">common</span>",
            "spec_rows": [
                ("ASTM B456", "Ni-Cr on steel/Cu/Zn"),
                ("AMS 2403", "Nickel plating"),
                ("GM 4394M", "GM decorative Ni-Cr"),
                ("ISO 1456", "Ni coatings"),
            ],
            "compare_title": "Bright Nickel vs Semi-Bright Nickel <span class=\"sub\">key differences</span>",
            "do_title": "Bright Nickel <span class=\"tag good\">Key Traits</span>",
            "do_items": [
                "Mirror-bright finish; high leveling",
                "Contains sulfur (0.04&ndash;0.1% S)",
                "More active corrosion potential",
                "Used as outer Ni layer in duplex",
                "Excellent appearance without polishing",
            ],
            "dont_title": "Semi-Bright Nickel <span class=\"tag bad\">Key Traits</span>",
            "dont_items": [
                "Satin-bright finish; columnar grain",
                "Sulfur-free (&lt;0.005% S)",
                "More noble potential than bright Ni",
                "Used as inner Ni layer in duplex",
                "Better ductility; lower internal stress",
            ],
            "footer_title": "Bright Nickel Plating Demystified &mdash; Electroplating Series",
            "footer_disclaimer": "Technical reference only. Verify all parameters against your chemistry supplier&rsquo;s TDS, customer specifications, and applicable regulatory requirements before production use.",
        },
        "es": {
            "eyebrow": "Plating Posters &middot; Electrodeposici&oacute;n &middot; N&iacute;quel Brillante &middot; Descripci&oacute;n",
            "headline": "N&Iacute;QUEL<br><em>BRILLANTE</em>",
            "subhead": "Electrodeposici&oacute;n Decorativa Tipo Watts &mdash; Brillo y Resistencia a la Corrosi&oacute;n",
            "tagline": "El caballo de batalla del acabado espejo decorativo &mdash; los abrillantadores niveladores producen un dep&oacute;sito brillante que sustenta al cromo y define la apariencia de productos premium.",
            "rule_num": "10&ndash;40",
            "rule_label": "Espesor T&iacute;pico del Dep&oacute;sito (&micro;m) &mdash; N&iacute;quel Brillante (Decorativo)",
            "rule_text": "El n&iacute;quel brillante es la capa gruesa y nivelada que proporciona la mayor parte de la protecci&oacute;n anticorrosiva en el sistema n&iacute;quel-cromo. A 10&ndash;40 &micro;m, entrega el acabado espejo y la barrera mec&aacute;nica que el cromo decorativo delgado (0.25&ndash;0.75 &micro;m) por s&iacute; solo no puede brindar.",
            "process_title": "Secuencia T&iacute;pica del Proceso <span class=\"sub\">l&iacute;nea de bastidor</span>",
            "process_rows": [
                ("01", "Limpieza Alcalina por Inmersi&oacute;n", "60&ndash;82&deg;C", "3&ndash;5 min", "Eliminar aceites y compuestos de pulido"),
                ("02", "Electrolimpieza (An&oacute;dica)", "60&ndash;82&deg;C", "1&ndash;3 min", "Desengrase final; corriente inversa"),
                ("03", "Enjuague", "Ambiente", "30&ndash;60 s", "Enjuague con rebose"),
                ("04", "Activaci&oacute;n &Aacute;cida", "Ambiente", "15&ndash;30 s", "10&ndash;20% HCl &mdash; eliminar &oacute;xidos"),
                ("05", "Enjuague", "Ambiente", "30&ndash;60 s", "Prevenir arrastre de &aacute;cido"),
                ("06", "Strike de N&iacute;quel (opcional)", "Ambiente", "1&ndash;3 min", "Strike Wood para metales pasivos"),
                ("07", "N&iacute;quel Brillante", "54&ndash;66&deg;C", "15&ndash;40 min", "NiSO&#8324; 250&ndash;300 g/L; abrillantadores"),
                ("08", "Enjuague", "Ambiente", "30&ndash;60 s", "Prevenir arrastre al cromo"),
                ("09", "Cromo Decorativo (opcional)", "35&ndash;46&deg;C", "3&ndash;8 min", "Cr(III) o Cr(VI) flash decorativo"),
                ("10", "Enjuague / Secado", "Ambiente", "1&ndash;2 min", "Enjuague multi-etapa; secado al aire"),
            ],
            "insight_label": "Por Qu&eacute; el N&iacute;quel Brillante Es el Coraz&oacute;n del Acabado Decorativo",
            "insight_text": "En cualquier sistema de n&iacute;quel-cromo, el n&iacute;quel brillante es la barrera anticorrosiva principal &mdash; no el cromo. El cromo decorativo solo tiene 0.25&ndash;0.75 &micro;m y existe por apariencia y dureza, mientras que el n&iacute;quel brillante a 10&ndash;40 &micro;m realiza el trabajo real de protecci&oacute;n. Los aditivos abrillantadores producen el acabado espejo depositando preferencialmente en micro-valles. En sistemas duplex o triplex, una capa semi-brillante debajo crea una diferencia de potencial que dirige la corrosi&oacute;n lateralmente.",
            "svg_title": "Flujo del Proceso de N&iacute;quel Brillante <span class=\"sub\">l&iacute;nea de bastidor</span>",
            "app_title": "Gu&iacute;a de Aplicaci&oacute;n <span class=\"sub\">tipo de sistema</span>",
            "app_headers": ("Sistema", "Ni Brillante", "Ni Total", "CASS (hrs)"),
            "app_rows": [
                ("Capa &Uacute;nica Brillante", "15&ndash;25 &micro;m", "15&ndash;25 &micro;m", "8&ndash;16"),
                ("Duplex (SB + Brillante)", "15&ndash;25 &micro;m", "25&ndash;40 &micro;m", "22&ndash;44"),
                ("Triplex (SB + HB + Brill.)", "10&ndash;20 &micro;m", "30&ndash;50 &micro;m", "44&ndash;64+"),
                ("Ni Brillante (sin cromo)", "20&ndash;40 &micro;m", "20&ndash;40 &micro;m", "N/A &mdash; ASTM B117"),
            ],
            "dyk_text": "El &ldquo;brillante&rdquo; del n&iacute;quel brillante proviene de aditivos org&aacute;nicos, no del n&iacute;quel mismo. Los <strong style=\"color:var(--amber);\">portadores Clase I</strong> (como sulfonatos de naftaleno) reducen la tensi&oacute;n superficial y refinan el grano, mientras los <strong style=\"color:var(--amber);\">niveladores Clase II</strong> (como cumarina o compuestos proparg&iacute;licos) depositan preferencialmente en micro-valles para crear el acabado espejo. El azufre co-depositado de los abrillantadores Clase II (0.04&ndash;0.1% S) es lo que crea la diferencia de potencial electroqu&iacute;mica que hace funcionar la protecci&oacute;n del n&iacute;quel duplex.",
            "bath_title": "Qu&iacute;mica del Ba&ntilde;o <span class=\"sub\">tipo Watts</span>",
            "bath_rows": [
                ("Sulfato de N&iacute;quel", "250&ndash;300 g/L"),
                ("Cloruro de N&iacute;quel", "40&ndash;60 g/L"),
                ("&Aacute;cido B&oacute;rico", "35&ndash;45 g/L"),
                ("pH", "3.5&ndash;4.5"),
                ("Temperatura", "54&ndash;66&deg;C"),
                ("DC C&aacute;todo", "2&ndash;6 A/dm&sup2;"),
            ],
            "spec_title": "Especificaciones <span class=\"sub\">comunes</span>",
            "spec_rows": [
                ("ASTM B456", "Ni-Cr sobre acero/Cu/Zn"),
                ("AMS 2403", "Niquelado electrol&iacute;tico"),
                ("GM 4394M", "Ni-Cr decorativo de GM"),
                ("ISO 1456", "Recubrimientos de Ni"),
            ],
            "compare_title": "Ni Brillante vs Ni Semi-Brillante <span class=\"sub\">diferencias clave</span>",
            "do_title": "N&iacute;quel Brillante <span class=\"tag good\">Caracter&iacute;sticas</span>",
            "do_items": [
                "Acabado espejo brillante; alto nivelado",
                "Contiene azufre (0.04&ndash;0.1% S)",
                "Potencial de corrosi&oacute;n m&aacute;s activo",
                "Capa exterior de Ni en sistema duplex",
                "Excelente apariencia sin pulido",
            ],
            "dont_title": "N&iacute;quel Semi-Brillante <span class=\"tag bad\">Caracter&iacute;sticas</span>",
            "dont_items": [
                "Acabado sat&iacute;n-brillante; grano columnar",
                "Libre de azufre (&lt;0.005% S)",
                "Potencial m&aacute;s noble que Ni brillante",
                "Capa interior de Ni en sistema duplex",
                "Mejor ductilidad; menor estr&eacute;s interno",
            ],
            "footer_title": "N&iacute;quel Brillante Desmitificado &mdash; Serie de Electrodeposici&oacute;n",
            "footer_disclaimer": "Referencia t&eacute;cnica solamente. Verifique todos los par&aacute;metros contra la TDS de su proveedor, especificaciones del cliente y requisitos regulatorios aplicables antes del uso en producci&oacute;n.",
        },
    },
}


# ── HTML TEMPLATE ────────────────────────────────────────────────────────────

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

    # SVG: use EN version for both languages (diagram labels are fine in EN)
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


# ── FILE NAME MAP ────────────────────────────────────────────────────────────

TITLE_MAP = {
    "zinc_alk":      "Alkaline Zinc Plating Demystified",
    "acid_zinc":     "Acid Zinc Plating Demystified",
    "znni":          "Zinc-Nickel Plating Demystified",
    "bright_nickel": "Bright Nickel Plating Demystified",
}

TITLE_MAP_ES = {
    "zinc_alk":      "Zinc Alcalino Desmitificado",
    "acid_zinc":     "Zinc Acido Desmitificado",
    "znni":          "Zinc-Niquel Desmitificado",
    "bright_nickel": "Niquel Brillante Desmitificado",
}


# ── GENERATE ─────────────────────────────────────────────────────────────────

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
    print(f"\nDone — {count} files written to {OUT}")


if __name__ == "__main__":
    main()
