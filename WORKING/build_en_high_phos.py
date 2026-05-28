#!/usr/bin/env python3
"""Build EN High Phos poster series — 72 files (9 posters × 2 editions × 2 langs × 2 themes)."""
import os, textwrap

POSTERS = [
    ("00", "Electroless Nickel Demystified"),
    ("01", "Process Flow"),
    ("02", "Cleaning"),
    ("03", "Rinse Pre-Activation"),
    ("04", "Activation"),
    ("05", "Critical Rinse"),
    ("06", "EN Bath"),
    ("07", "Final Rinse"),
    ("08", "Post Treatment"),
]

# ── HEADER FUNCTIONS ──────────────────────────────────────────────────
def tech_headers_en(num, title):
    return f"""<div class="poster-header">
    <header class="header-band">
      <div class="header-left">
        <div class="eyebrow"><span>Plating Posters &nbsp;&middot;&nbsp; EN High Phos (10&ndash;13% P) &nbsp;&middot;&nbsp; 7-Stage Process &nbsp;&middot;&nbsp; {title}</span></div>
        <h1 class="headline">ELECTROLESS<br><em>NICKEL</em></h1>
        <h2 class="subhead">High Phosphorus (10&ndash;13% P) &mdash; Maximum Corrosion Resistance, Non-Magnetic</h2>
        <p class="tagline">No current, no anode &mdash; the bath plates itself. High-phos is the corrosion champion of the EN family.</p>
      </div>
      <aside class="glass logo-card">
        <div class="logo-tile"><span>PP</span></div>
        <div class="logo-word"><span class="a">Plating</span> <span class="b">Posters</span></div>
        <div class="logo-inc">www.platingposters.com</div>
      </aside>
    </header>
  </div>"""

def tech_headers_es(num, title):
    return f"""<div class="poster-header">
    <header class="header-band">
      <div class="header-left">
        <div class="eyebrow"><span>Plating Posters &nbsp;&middot;&nbsp; EN Alto F&oacute;sforo (10&ndash;13% P) &nbsp;&middot;&nbsp; Proceso de 7 Etapas &nbsp;&middot;&nbsp; {title}</span></div>
        <h1 class="headline">N&Iacute;QUEL<br><em>QU&Iacute;MICO</em></h1>
        <h2 class="subhead">Alto F&oacute;sforo (10&ndash;13% P) &mdash; M&aacute;xima Resistencia a Corrosi&oacute;n, No Magn&eacute;tico</h2>
        <p class="tagline">Sin corriente, sin &aacute;nodo &mdash; el ba&ntilde;o deposita por s&iacute; solo. Alto f&oacute;sforo es el campe&oacute;n anticorrosi&oacute;n de la familia EN.</p>
      </div>
      <aside class="glass logo-card">
        <div class="logo-tile"><span>PP</span></div>
        <div class="logo-word"><span class="a">Plating</span> <span class="b">Posters</span></div>
        <div class="logo-inc">www.platingposters.com</div>
      </aside>
    </header>
  </div>"""

def sf_headers_en(num, title):
    return f"""<div class="poster-header">
    <div class="header-row">
      <div class="header-left">
        <div class="eyebrow">Plating Posters Inc &mdash; Shop Floor &mdash; EN High Phos Series &mdash; {title}</div>
        <div class="headline">EN HIGH<br><em>PHOS</em></div>
        <div class="subhead">7 Stages From Dirty Part to Finished Deposit</div>
        <div class="tagline">No current, no anode &mdash; the bath plates itself. Follow every stage, every load.</div>
      </div>
      <div class="logo-card">
        <div class="logo-mark"><span>PP</span></div>
        <div class="logo-word"><span class="a">Plating</span> <span class="b">Posters</span></div>
        <div class="logo-url">www.platingposters.com</div>
      </div>
    </div>
  </div>"""

def sf_headers_es(num, title):
    return f"""<div class="poster-header">
    <div class="header-row">
      <div class="header-left">
        <div class="eyebrow">Plating Posters Inc &mdash; Piso de Producci&oacute;n &mdash; Serie EN Alto F&oacute;sforo &mdash; {title}</div>
        <div class="headline">EN ALTO<br><em>P</em></div>
        <div class="subhead">7 Etapas de Pieza Sucia a Dep&oacute;sito Terminado</div>
        <div class="tagline">Sin corriente, sin &aacute;nodo &mdash; el ba&ntilde;o deposita por s&iacute; solo. Siga cada etapa, cada carga.</div>
      </div>
      <div class="logo-card">
        <div class="logo-mark"><span>PP</span></div>
        <div class="logo-word"><span class="a">Plating</span> <span class="b">Posters</span></div>
        <div class="logo-url">www.platingposters.com</div>
      </div>
    </div>
  </div>"""

# ── TECH FOOTER ──────────────────────────────────────────────────────
def tech_footer_en(num, title):
    return f"""<footer class="footer poster-footer">
    <p class="footer-disclaimer">Technical reference only. Verify all parameters against your chemistry supplier&rsquo;s TDS, customer specifications, and applicable regulatory requirements before production use.</p>
    <p class="footer-title">{title} &mdash; EN High Phos Plating Series</p>
    <span class="footer-brand">Plating Posters &middot; Metal Finishing Reference Series &middot; PP-ENhp-{num}-T / v1.0 / 2026</span>
  </footer>"""

def tech_footer_es(num, title):
    return f"""<footer class="footer poster-footer">
    <p class="footer-disclaimer">Referencia t&eacute;cnica solamente. Verifique todos los par&aacute;metros contra la FTS de su proveedor, especificaciones del cliente y requisitos regulatorios antes de usar en producci&oacute;n.</p>
    <p class="footer-title">{title} &mdash; Serie EN Alto F&oacute;sforo</p>
    <span class="footer-brand">Plating Posters &middot; Serie de Referencia de Acabados Met&aacute;licos &middot; PP-ENhp-{num}-T / v1.0 / 2026</span>
  </footer>"""

def sf_footer_en(num, title):
    return f"""<div class="glass footer-panel poster-footer">
    <div class="footer-disclaimer">Operator reference only. Follow your facility SOPs. Report any process deviations to your supervisor.</div>
    <div class="footer-title">{title} &mdash; EN High Phos Plating Series</div>
    <div class="footer-brand">Plating Posters Inc &middot; Shop Floor Reference &middot; PP-ENhp-{num}-SF / v1.0 / 2026</div>
  </div>"""

def sf_footer_es(num, title):
    return f"""<div class="glass footer-panel poster-footer">
    <div class="footer-disclaimer">Referencia para operador solamente. Siga los procedimientos de su &aacute;rea. Reporte cualquier desviaci&oacute;n a su supervisor.</div>
    <div class="footer-title">{title} &mdash; Serie EN Alto F&oacute;sforo</div>
    <div class="footer-brand">Plating Posters Inc &middot; Referencia Piso de Producci&oacute;n &middot; PP-ENhp-{num}-SF / v1.0 / 2026</div>
  </div>"""

# ── POSTER TITLES (ES) ──────────────────────────────────────────────
TITLES_ES = {
    "00": "N&iacute;quel Qu&iacute;mico Desmitificado",
    "01": "Flujo de Proceso",
    "02": "Limpieza",
    "03": "Enjuague Pre-Activaci&oacute;n",
    "04": "Activaci&oacute;n",
    "05": "Enjuague Cr&iacute;tico",
    "06": "Ba&ntilde;o EN",
    "07": "Enjuague Final",
    "08": "Post Tratamiento",
}

# ── BODY CONTENT ─────────────────────────────────────────────────────
TECH_BODY_EN = {}
TECH_BODY_ES = {}
SF_BODY_EN = {}
SF_BODY_ES = {}

# =====================================================================
# POSTER 00 — DEMYSTIFIED
# =====================================================================
TECH_BODY_EN["00"] = """
    <div class="glass rule-card">
      <div class="rule-num">10&ndash;13%</div>
      <div class="rule-body">
        <div class="rule-label">Phosphorus Content &mdash; The Corrosion Champion</div>
        <div class="rule-text">High-phos EN is fully amorphous as-deposited &mdash; no grain boundaries means no preferential corrosion paths. Non-magnetic, uniformly thick on any geometry, and the most chemically resistant deposit in the EN family. Where mid-phos balances everything, high-phos is purpose-built for survival in harsh chemical environments.</div>
      </div>
    </div>

    <!-- PROCESS FLOW SVG -->
    <div class="glass process-flow">
      <svg viewBox="0 0 1100 70" width="100%" height="70" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="80" cy="28" r="20" stroke="var(--amber)" stroke-width="1.8" fill="rgba(232,160,32,.12)"/>
        <text x="80" y="34" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="18">01</text>
        <text x="80" y="60" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11" letter-spacing=".04em" opacity=".62">CLEAN</text>
        <line x1="104" y1="28" x2="140" y2="28" stroke="currentColor" stroke-width="1.4" opacity=".4"/><polygon points="140,24 149,28 140,32" fill="currentColor" opacity=".4"/>
        <circle cx="218" cy="28" r="20" stroke="var(--teal)" stroke-width="1.8" fill="rgba(46,196,182,.12)"/>
        <text x="218" y="34" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="18">02</text>
        <text x="218" y="60" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11" letter-spacing=".04em" opacity=".62">RINSE</text>
        <line x1="242" y1="28" x2="278" y2="28" stroke="currentColor" stroke-width="1.4" opacity=".4"/><polygon points="278,24 287,28 278,32" fill="currentColor" opacity=".4"/>
        <circle cx="356" cy="28" r="20" stroke="var(--amber)" stroke-width="1.8" fill="rgba(232,160,32,.12)"/>
        <text x="356" y="34" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="18">03</text>
        <text x="356" y="60" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11" letter-spacing=".04em" opacity=".62">ACTIVATE</text>
        <line x1="380" y1="28" x2="416" y2="28" stroke="currentColor" stroke-width="1.4" opacity=".4"/><polygon points="416,24 425,28 416,32" fill="currentColor" opacity=".4"/>
        <circle cx="494" cy="28" r="20" stroke="var(--teal)" stroke-width="1.8" fill="rgba(46,196,182,.12)"/>
        <text x="494" y="34" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="18">04</text>
        <text x="494" y="60" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11" letter-spacing=".04em" opacity=".62">RINSE</text>
        <line x1="518" y1="28" x2="554" y2="28" stroke="currentColor" stroke-width="1.4" opacity=".4"/><polygon points="554,24 563,28 554,32" fill="currentColor" opacity=".4"/>
        <circle cx="632" cy="28" r="22" stroke="var(--coral)" stroke-width="2.2" fill="rgba(224,92,92,.12)"/>
        <text x="632" y="34" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="18">05</text>
        <text x="632" y="60" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11" letter-spacing=".04em" opacity=".62">EN BATH</text>
        <line x1="658" y1="28" x2="694" y2="28" stroke="currentColor" stroke-width="1.4" opacity=".4"/><polygon points="694,24 703,28 694,32" fill="currentColor" opacity=".4"/>
        <circle cx="770" cy="28" r="20" stroke="var(--teal)" stroke-width="1.8" fill="rgba(46,196,182,.12)"/>
        <text x="770" y="34" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="18">06</text>
        <text x="770" y="60" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11" letter-spacing=".04em" opacity=".62">RINSE</text>
        <line x1="794" y1="28" x2="830" y2="28" stroke="currentColor" stroke-width="1.4" opacity=".4"/><polygon points="830,24 839,28 830,32" fill="currentColor" opacity=".4"/>
        <circle cx="908" cy="28" r="22" stroke="var(--emerald)" stroke-width="2.2" fill="rgba(39,174,96,.12)"/>
        <text x="908" y="34" text-anchor="middle" fill="var(--emerald)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="18">07</text>
        <text x="908" y="60" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11" letter-spacing=".04em" opacity=".62">POST-TREAT</text>
      </svg>
    </div>

    <!-- FULL PROCESS SEQUENCE -->
    <div>
      <h3 class="section-title">Full Process Sequence <span class="sub">7 stages &mdash; EN high phos</span></h3>
      <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
        <table class="data-table compact">
          <thead><tr><th style="width:28px;">#</th><th>Process</th><th>Temp</th><th>Time</th><th>Key Parameter</th></tr></thead>
          <tbody>
            <tr><td class="mono">01</td><td>Alkaline Soak Clean</td><td class="mono">140&ndash;176&deg;F (60&ndash;80&deg;C)</td><td class="mono">3&ndash;10 min</td><td>Water-break-free surface</td></tr>
            <tr><td class="mono">02</td><td>Cascade Rinse (Pre-Activation)</td><td class="mono">Ambient</td><td class="mono">30&ndash;60 s/stage</td><td>Conductivity &lt;50 &micro;S/cm</td></tr>
            <tr><td class="mono">03</td><td>Acid Activation</td><td class="mono">Ambient</td><td class="mono">30&ndash;120 s</td><td>HCl 10&ndash;20% v/v; or double zincate for Al</td></tr>
            <tr><td class="mono">04</td><td>Critical Rinse (Pre-EN)</td><td class="mono">Ambient</td><td class="mono">30&ndash;60 s</td><td>Conductivity &lt;20 &micro;S/cm; DI water required</td></tr>
            <tr><td class="mono">05</td><td>EN High Phos Bath</td><td class="mono">185&ndash;196&deg;F (85&ndash;91&deg;C)</td><td class="mono">60&ndash;180 min</td><td>pH 4.2&ndash;4.8; Ni&sup2;&#8314; 4.5&ndash;6.5 g/L</td></tr>
            <tr><td class="mono">06</td><td>Final Rinse</td><td class="mono">Cold</td><td class="mono">30&ndash;60 s</td><td>Transfer in &lt;10 sec; DI final stage</td></tr>
            <tr><td class="mono">07</td><td>Post Treatment (Bake/Seal)</td><td class="mono">375&ndash;750&deg;F</td><td class="mono">1&ndash;4+ hr</td><td>Per spec: HE relief, chromate, or sealant</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- AMORPHOUS STRUCTURE SVG -->
    <div class="glass" style="padding:10px 14px;">
      <h3 class="section-title" style="margin-bottom:4px;">Amorphous vs Crystalline Structure <span class="sub">why high phos resists corrosion</span></h3>
      <svg viewBox="0 0 1100 90" width="100%" height="90" fill="none" xmlns="http://www.w3.org/2000/svg">
        <!-- Amorphous side -->
        <rect x="30" y="5" width="480" height="80" rx="8" fill="rgba(46,196,182,.05)" stroke="var(--teal)" stroke-width="1"/>
        <text x="270" y="20" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11" letter-spacing=".06em">HIGH PHOS (10&ndash;13% P) &mdash; AMORPHOUS</text>
        <!-- Random atom positions -->
        <circle cx="80" cy="45" r="4" fill="rgba(46,196,182,.4)"/><circle cx="105" cy="55" r="4" fill="rgba(46,196,182,.4)"/>
        <circle cx="130" cy="40" r="4" fill="rgba(46,196,182,.4)"/><circle cx="155" cy="60" r="4" fill="rgba(46,196,182,.4)"/>
        <circle cx="180" cy="48" r="4" fill="rgba(46,196,182,.4)"/><circle cx="205" cy="38" r="4" fill="rgba(46,196,182,.4)"/>
        <circle cx="230" cy="58" r="4" fill="rgba(46,196,182,.4)"/><circle cx="255" cy="42" r="4" fill="rgba(46,196,182,.4)"/>
        <circle cx="280" cy="55" r="4" fill="rgba(46,196,182,.4)"/><circle cx="305" cy="45" r="4" fill="rgba(46,196,182,.4)"/>
        <circle cx="330" cy="60" r="4" fill="rgba(46,196,182,.4)"/><circle cx="355" cy="38" r="4" fill="rgba(46,196,182,.4)"/>
        <circle cx="380" cy="52" r="4" fill="rgba(46,196,182,.4)"/><circle cx="405" cy="42" r="4" fill="rgba(46,196,182,.4)"/>
        <circle cx="430" cy="55" r="4" fill="rgba(46,196,182,.4)"/><circle cx="455" cy="48" r="4" fill="rgba(46,196,182,.4)"/>
        <text x="270" y="78" text-anchor="middle" fill="var(--teal)" font-family="Inter,sans-serif" font-size="8" font-weight="600">No grain boundaries &rarr; no preferential corrosion paths &rarr; &gt;1000 hr NSS</text>
        <!-- Crystalline side -->
        <rect x="570" y="5" width="480" height="80" rx="8" fill="rgba(224,92,92,.05)" stroke="var(--coral)" stroke-width="1"/>
        <text x="810" y="20" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11" letter-spacing=".06em">LOW/MID PHOS &mdash; MICROCRYSTALLINE</text>
        <!-- Grid atom positions -->
        <circle cx="620" cy="40" r="4" fill="rgba(224,92,92,.4)"/><circle cx="650" cy="40" r="4" fill="rgba(224,92,92,.4)"/>
        <circle cx="680" cy="40" r="4" fill="rgba(224,92,92,.4)"/><circle cx="710" cy="40" r="4" fill="rgba(224,92,92,.4)"/>
        <circle cx="620" cy="60" r="4" fill="rgba(224,92,92,.4)"/><circle cx="650" cy="60" r="4" fill="rgba(224,92,92,.4)"/>
        <circle cx="680" cy="60" r="4" fill="rgba(224,92,92,.4)"/><circle cx="710" cy="60" r="4" fill="rgba(224,92,92,.4)"/>
        <!-- Gap = grain boundary -->
        <line x1="740" y1="30" x2="740" y2="72" stroke="var(--coral)" stroke-width="1.5" stroke-dasharray="3,2"/>
        <text x="740" y="28" text-anchor="middle" fill="var(--coral)" font-family="Inter,sans-serif" font-size="7" font-weight="600">GRAIN BOUNDARY</text>
        <!-- Second grain -->
        <circle cx="770" cy="42" r="4" fill="rgba(224,92,92,.4)"/><circle cx="800" cy="42" r="4" fill="rgba(224,92,92,.4)"/>
        <circle cx="830" cy="42" r="4" fill="rgba(224,92,92,.4)"/><circle cx="860" cy="42" r="4" fill="rgba(224,92,92,.4)"/>
        <circle cx="770" cy="62" r="4" fill="rgba(224,92,92,.4)"/><circle cx="800" cy="62" r="4" fill="rgba(224,92,92,.4)"/>
        <circle cx="830" cy="62" r="4" fill="rgba(224,92,92,.4)"/><circle cx="860" cy="62" r="4" fill="rgba(224,92,92,.4)"/>
        <text x="810" y="78" text-anchor="middle" fill="var(--coral)" font-family="Inter,sans-serif" font-size="8" font-weight="600">Grain boundaries = corrosion highways &rarr; shorter service life</text>
      </svg>
    </div>


    <!-- P% VS PROPERTIES CURVE SVG -->
    <div class="glass" style="padding:10px 14px;">
      <h3 class="section-title" style="margin-bottom:4px;">Phosphorus Content vs Deposit Properties <span class="sub">hardness, corrosion &amp; magnetism across the P% spectrum</span></h3>
      <svg viewBox="0 0 1100 140" width="100%" height="140" fill="none" xmlns="http://www.w3.org/2000/svg">
        <!-- Shaded bands -->
        <rect x="130" y="15" width="143" height="105" rx="4" fill="rgba(224,92,92,.06)"/>
        <text x="201" y="12" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="700" font-size="8" letter-spacing=".05em">LOW PHOS</text>
        <rect x="416" y="15" width="215" height="105" rx="4" fill="rgba(232,160,32,.06)"/>
        <text x="523" y="12" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="700" font-size="8" letter-spacing=".05em">MID PHOS</text>
        <rect x="702" y="15" width="215" height="105" rx="4" fill="rgba(46,196,182,.06)"/>
        <text x="809" y="12" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="700" font-size="8" letter-spacing=".05em">HIGH PHOS</text>
        <!-- Axes -->
        <line x1="58" y1="120" x2="960" y2="120" stroke="var(--muted)" stroke-width="1" opacity=".5"/>
        <line x1="58" y1="15" x2="58" y2="120" stroke="var(--muted)" stroke-width="1" opacity=".5"/>
        <!-- X-axis ticks -->
        <line x1="130" y1="118" x2="130" y2="122" stroke="var(--muted)" stroke-width="1"/><text x="130" y="132" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="8">2%</text>
        <line x1="201" y1="118" x2="201" y2="122" stroke="var(--muted)" stroke-width="1"/><text x="201" y="132" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="8">4%</text>
        <line x1="273" y1="118" x2="273" y2="122" stroke="var(--muted)" stroke-width="1"/><text x="273" y="132" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="8">6%</text>
        <line x1="345" y1="118" x2="345" y2="122" stroke="var(--muted)" stroke-width="1"/><text x="345" y="132" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="8">8%</text>
        <line x1="416" y1="118" x2="416" y2="122" stroke="var(--muted)" stroke-width="1"/><text x="416" y="132" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="8">10%</text>
        <line x1="488" y1="118" x2="488" y2="122" stroke="var(--muted)" stroke-width="1"/><text x="488" y="132" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="8">12%</text>
        <line x1="560" y1="118" x2="560" y2="122" stroke="var(--muted)" stroke-width="1"/><text x="560" y="132" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="8">14%</text>
        <!-- Y-axis label -->
        <text x="20" y="70" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="7" transform="rotate(-90,20,70)">Relative Scale</text>
        <!-- Curve 1: Hardness (coral) -->
        <polyline points="130,25 201,35 273,42 345,50 416,58 488,68 560,78 630,85 702,90 810,95 917,100" stroke="var(--coral)" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
        <!-- Curve 2: Corrosion resistance (teal) -->
        <polyline points="130,110 201,108 273,105 345,102 416,98 488,92 560,85 630,70 702,50 810,30 917,22" stroke="var(--teal)" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
        <!-- Curve 3: Magnetic permeability (amber) -->
        <polyline points="130,28 201,30 273,35 345,42 416,55 488,75 560,95 630,110 702,115 810,117 917,118" stroke="var(--amber)" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
        <!-- Data point dots -->
        <circle cx="130" cy="25" r="3" fill="var(--coral)"/><circle cx="917" cy="100" r="3" fill="var(--coral)"/>
        <circle cx="130" cy="110" r="3" fill="var(--teal)"/><circle cx="917" cy="22" r="3" fill="var(--teal)"/>
        <circle cx="130" cy="28" r="3" fill="var(--amber)"/><circle cx="630" cy="110" r="3" fill="var(--amber)"/>
        <!-- Legend -->
        <rect x="750" y="125" width="210" height="14" rx="3" fill="rgba(0,0,0,.03)"/>
        <line x1="760" y1="132" x2="778" y2="132" stroke="var(--coral)" stroke-width="2"/><text x="782" y="135" fill="var(--coral)" font-family="Inter,sans-serif" font-size="7" font-weight="600">Hardness HV</text>
        <line x1="840" y1="132" x2="858" y2="132" stroke="var(--teal)" stroke-width="2"/><text x="862" y="135" fill="var(--teal)" font-family="Inter,sans-serif" font-size="7" font-weight="600">Corrosion (NSS hr)</text>
        <line x1="935" y1="132" x2="948" y2="132" stroke="var(--amber)" stroke-width="2"/><text x="952" y="135" fill="var(--amber)" font-family="Inter,sans-serif" font-size="7" font-weight="600">&mu;</text>
      </svg>
    </div>

    <!-- BOTTOM GRID -->
    <div class="bottom-grid">
      <div>
        <h3 class="section-title">Why High Phos? <span class="sub">the corrosion champion</span></h3>
        <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
          <table class="data-table bath">
            <thead><tr><th>Property</th><th>High Phos (10&ndash;13% P)</th></tr></thead>
            <tbody>
              <tr><td style="font-weight:600;">Hardness (as-plated)</td><td class="mono">450&ndash;550 HV</td></tr>
              <tr><td style="font-weight:600;">Hardness (baked 400&deg;C/1hr)</td><td class="mono">850&ndash;1000 HV</td></tr>
              <tr><td style="font-weight:600;">Corrosion (salt spray)</td><td class="mono">&gt;1000 hr (25 &micro;m on steel)</td></tr>
              <tr><td style="font-weight:600;">Solderability</td><td>Poor without activation</td></tr>
              <tr><td style="font-weight:600;">Magnetic</td><td>Non-magnetic as-plated (&gt;10.5% P)</td></tr>
              <tr><td style="font-weight:600;">Structure</td><td>Fully amorphous &mdash; no grain boundaries</td></tr>
            </tbody>
          </table>
        </div>
      </div>
      <div>
        <h3 class="section-title">Bath Chemistry <span class="sub">Stage 5</span></h3>
        <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
          <table class="data-table bath">
            <thead><tr><th>Component</th><th>Range</th></tr></thead>
            <tbody>
              <tr><td>Nickel (as Ni&sup2;&#8314;)</td><td class="mono">4.5&ndash;6.5 g/L</td></tr>
              <tr><td>Sodium Hypophosphite</td><td class="mono">25&ndash;40 g/L</td></tr>
              <tr><td>Organic Acids (complexors)</td><td class="mono">Per supplier TDS</td></tr>
              <tr><td>pH</td><td class="mono">4.2&ndash;4.8</td></tr>
              <tr><td>Temperature</td><td class="mono">85&ndash;91&deg;C</td></tr>
              <tr><td>Plating Rate</td><td class="mono">8&ndash;15 &micro;m/hr</td></tr>
              <tr><td>Loading</td><td class="mono">0.5&ndash;1.5 dm&sup2;/L</td></tr>
              <tr><td>Bath Life</td><td class="mono">5&ndash;7 MTO typical</td></tr>
            </tbody>
          </table>
        </div>
        <h3 class="section-title" style="margin-top:10px;">Specifications <span class="sub">common</span></h3>
        <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
          <table class="data-table bath">
            <thead><tr><th>Code</th><th>Scope</th></tr></thead>
            <tbody>
              <tr><td class="mono">ASTM B733</td><td>SC4 (Type V) &mdash; high phos (&ge;10% P)</td></tr>
              <tr><td class="mono">AMS 2404</td><td>Class 1&ndash;4 &mdash; aerospace EN</td></tr>
              <tr><td class="mono">MIL-C-26074</td><td>Class 4 &mdash; high phos military EN</td></tr>
              <tr><td class="mono">ASTM B849</td><td>HE Relief Baking</td></tr>
              <tr><td class="mono">NACE SP0170</td><td>Pipeline / oil &amp; gas coatings</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- TRADEOFFS -->
    <div>
      <h3 class="section-title">High Phos vs Other EN Types <span class="sub">positioning</span></h3>
      <div class="compare-grid">
        <div class="glass compare-card do" style="padding:8px 14px;">
          <h4 style="font-size:18px;margin-bottom:5px;">High Phos Strengths <span class="tag good">Champion</span></h4>
          <ul>
            <li>Best corrosion resistance of any EN formulation</li>
            <li>Non-magnetic &mdash; critical for electronics, HDD, MRI</li>
            <li>Fully amorphous &mdash; no grain boundary attack</li>
          </ul>
        </div>
        <div class="glass compare-card dont" style="padding:8px 14px;">
          <h4 style="font-size:18px;margin-bottom:5px;">When to Choose Differently <span class="tag bad">Limits</span></h4>
          <ul>
            <li>Max hardness needed &rarr; Low Phos (2&ndash;4% P)</li>
            <li>Solderability required &rarr; Mid Phos (6&ndash;9% P)</li>
            <li>Baking destroys amorphous structure &amp; non-magnetic property</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="insight-card">
      <div class="insight-label">The Crystallization Trap</div>
      <div class="insight-text">Heat treating high-phos EN above 260&deg;C crystallizes the deposit into Ni + Ni&#8323;P, dramatically increasing hardness but <strong>destroying</strong> both the amorphous corrosion resistance and the non-magnetic property. If your spec requires corrosion resistance or non-magnetic behavior, do not bake above 260&deg;C. HE bake at 190&deg;C preserves both properties.</div>
    </div>
"""

TECH_BODY_ES["00"] = """
    <div class="glass rule-card">
      <div class="rule-num">10&ndash;13%</div>
      <div class="rule-body">
        <div class="rule-label">Contenido de F&oacute;sforo &mdash; El Campe&oacute;n Anticorrosi&oacute;n</div>
        <div class="rule-text">EN de alto f&oacute;sforo es completamente amorfo tal como se deposita &mdash; sin l&iacute;mites de grano significa sin caminos preferenciales de corrosi&oacute;n. No magn&eacute;tico, espesor uniforme en cualquier geometr&iacute;a, y el dep&oacute;sito m&aacute;s resistente qu&iacute;micamente de la familia EN. Donde el medio f&oacute;sforo equilibra todo, el alto f&oacute;sforo est&aacute; dise&ntilde;ado para sobrevivir en ambientes qu&iacute;micos agresivos.</div>
      </div>
    </div>

    <!-- FLUJO DE PROCESO SVG -->
    <div class="glass process-flow">
      <svg viewBox="0 0 1100 70" width="100%" height="70" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="80" cy="28" r="20" stroke="var(--amber)" stroke-width="1.8" fill="rgba(232,160,32,.12)"/>
        <text x="80" y="34" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="18">01</text>
        <text x="80" y="60" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11" letter-spacing=".04em" opacity=".62">LIMPIAR</text>
        <line x1="104" y1="28" x2="140" y2="28" stroke="currentColor" stroke-width="1.4" opacity=".4"/><polygon points="140,24 149,28 140,32" fill="currentColor" opacity=".4"/>
        <circle cx="218" cy="28" r="20" stroke="var(--teal)" stroke-width="1.8" fill="rgba(46,196,182,.12)"/>
        <text x="218" y="34" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="18">02</text>
        <text x="218" y="60" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11" letter-spacing=".04em" opacity=".62">ENJUAGUE</text>
        <line x1="242" y1="28" x2="278" y2="28" stroke="currentColor" stroke-width="1.4" opacity=".4"/><polygon points="278,24 287,28 278,32" fill="currentColor" opacity=".4"/>
        <circle cx="356" cy="28" r="20" stroke="var(--amber)" stroke-width="1.8" fill="rgba(232,160,32,.12)"/>
        <text x="356" y="34" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="18">03</text>
        <text x="356" y="60" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11" letter-spacing=".04em" opacity=".62">ACTIVAR</text>
        <line x1="380" y1="28" x2="416" y2="28" stroke="currentColor" stroke-width="1.4" opacity=".4"/><polygon points="416,24 425,28 416,32" fill="currentColor" opacity=".4"/>
        <circle cx="494" cy="28" r="20" stroke="var(--teal)" stroke-width="1.8" fill="rgba(46,196,182,.12)"/>
        <text x="494" y="34" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="18">04</text>
        <text x="494" y="60" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11" letter-spacing=".04em" opacity=".62">ENJUAGUE</text>
        <line x1="518" y1="28" x2="554" y2="28" stroke="currentColor" stroke-width="1.4" opacity=".4"/><polygon points="554,24 563,28 554,32" fill="currentColor" opacity=".4"/>
        <circle cx="632" cy="28" r="22" stroke="var(--coral)" stroke-width="2.2" fill="rgba(224,92,92,.12)"/>
        <text x="632" y="34" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="18">05</text>
        <text x="632" y="60" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11" letter-spacing=".04em" opacity=".62">BA&Ntilde;O EN</text>
        <line x1="658" y1="28" x2="694" y2="28" stroke="currentColor" stroke-width="1.4" opacity=".4"/><polygon points="694,24 703,28 694,32" fill="currentColor" opacity=".4"/>
        <circle cx="770" cy="28" r="20" stroke="var(--teal)" stroke-width="1.8" fill="rgba(46,196,182,.12)"/>
        <text x="770" y="34" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="18">06</text>
        <text x="770" y="60" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11" letter-spacing=".04em" opacity=".62">ENJUAGUE</text>
        <line x1="794" y1="28" x2="830" y2="28" stroke="currentColor" stroke-width="1.4" opacity=".4"/><polygon points="830,24 839,28 830,32" fill="currentColor" opacity=".4"/>
        <circle cx="908" cy="28" r="22" stroke="var(--emerald)" stroke-width="2.2" fill="rgba(39,174,96,.12)"/>
        <text x="908" y="34" text-anchor="middle" fill="var(--emerald)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="18">07</text>
        <text x="908" y="60" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11" letter-spacing=".04em" opacity=".62">POST-TRAT</text>
      </svg>
    </div>

    <!-- SECUENCIA COMPLETA -->
    <div>
      <h3 class="section-title">Secuencia Completa de Proceso <span class="sub">7 etapas &mdash; EN alto f&oacute;sforo</span></h3>
      <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
        <table class="data-table compact">
          <thead><tr><th style="width:28px;">#</th><th>Proceso</th><th>Temp</th><th>Tiempo</th><th>Par&aacute;metro Clave</th></tr></thead>
          <tbody>
            <tr><td class="mono">01</td><td>Limpieza Alcalina por Inmersi&oacute;n</td><td class="mono">60&ndash;80&deg;C</td><td class="mono">3&ndash;10 min</td><td>Superficie libre de ruptura de agua</td></tr>
            <tr><td class="mono">02</td><td>Enjuague en Cascada (Pre-Activaci&oacute;n)</td><td class="mono">Ambiente</td><td class="mono">30&ndash;60 s/etapa</td><td>Conductividad &lt;50 &micro;S/cm</td></tr>
            <tr><td class="mono">03</td><td>Activaci&oacute;n &Aacute;cida</td><td class="mono">Ambiente</td><td class="mono">30&ndash;120 s</td><td>HCl 10&ndash;20% v/v; o doble zincado para Al</td></tr>
            <tr><td class="mono">04</td><td>Enjuague Cr&iacute;tico (Pre-EN)</td><td class="mono">Ambiente</td><td class="mono">30&ndash;60 s</td><td>Conductividad &lt;20 &micro;S/cm; agua DI requerida</td></tr>
            <tr><td class="mono">05</td><td>Ba&ntilde;o EN Alto F&oacute;sforo</td><td class="mono">85&ndash;91&deg;C</td><td class="mono">60&ndash;180 min</td><td>pH 4.2&ndash;4.8; Ni&sup2;&#8314; 4.5&ndash;6.5 g/L</td></tr>
            <tr><td class="mono">06</td><td>Enjuague Final</td><td class="mono">Fr&iacute;o</td><td class="mono">30&ndash;60 s</td><td>Transferencia en &lt;10 s; DI en etapa final</td></tr>
            <tr><td class="mono">07</td><td>Post Tratamiento (Horneado/Sellado)</td><td class="mono">190&ndash;400&deg;C</td><td class="mono">1&ndash;4+ hr</td><td>Seg&uacute;n especificaci&oacute;n: alivio HE, cromato o sellador</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- SVG ESTRUCTURA AMORFA -->
    <div class="glass" style="padding:10px 14px;">
      <h3 class="section-title" style="margin-bottom:4px;">Estructura Amorfa vs Cristalina <span class="sub">por qu&eacute; el alto f&oacute;sforo resiste corrosi&oacute;n</span></h3>
      <svg viewBox="0 0 1100 90" width="100%" height="90" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect x="30" y="5" width="480" height="80" rx="8" fill="rgba(46,196,182,.05)" stroke="var(--teal)" stroke-width="1"/>
        <text x="270" y="20" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11" letter-spacing=".06em">ALTO F&Oacute;SFORO (10&ndash;13% P) &mdash; AMORFO</text>
        <circle cx="80" cy="45" r="4" fill="rgba(46,196,182,.4)"/><circle cx="105" cy="55" r="4" fill="rgba(46,196,182,.4)"/>
        <circle cx="130" cy="40" r="4" fill="rgba(46,196,182,.4)"/><circle cx="155" cy="60" r="4" fill="rgba(46,196,182,.4)"/>
        <circle cx="180" cy="48" r="4" fill="rgba(46,196,182,.4)"/><circle cx="205" cy="38" r="4" fill="rgba(46,196,182,.4)"/>
        <circle cx="230" cy="58" r="4" fill="rgba(46,196,182,.4)"/><circle cx="255" cy="42" r="4" fill="rgba(46,196,182,.4)"/>
        <circle cx="280" cy="55" r="4" fill="rgba(46,196,182,.4)"/><circle cx="305" cy="45" r="4" fill="rgba(46,196,182,.4)"/>
        <circle cx="330" cy="60" r="4" fill="rgba(46,196,182,.4)"/><circle cx="355" cy="38" r="4" fill="rgba(46,196,182,.4)"/>
        <circle cx="380" cy="52" r="4" fill="rgba(46,196,182,.4)"/><circle cx="405" cy="42" r="4" fill="rgba(46,196,182,.4)"/>
        <circle cx="430" cy="55" r="4" fill="rgba(46,196,182,.4)"/><circle cx="455" cy="48" r="4" fill="rgba(46,196,182,.4)"/>
        <text x="270" y="78" text-anchor="middle" fill="var(--teal)" font-family="Inter,sans-serif" font-size="8" font-weight="600">Sin l&iacute;mites de grano &rarr; sin caminos preferenciales &rarr; &gt;1000 hr NSS</text>
        <rect x="570" y="5" width="480" height="80" rx="8" fill="rgba(224,92,92,.05)" stroke="var(--coral)" stroke-width="1"/>
        <text x="810" y="20" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11" letter-spacing=".06em">BAJO/MEDIO F&Oacute;SFORO &mdash; MICROCRISTALINO</text>
        <circle cx="620" cy="40" r="4" fill="rgba(224,92,92,.4)"/><circle cx="650" cy="40" r="4" fill="rgba(224,92,92,.4)"/>
        <circle cx="680" cy="40" r="4" fill="rgba(224,92,92,.4)"/><circle cx="710" cy="40" r="4" fill="rgba(224,92,92,.4)"/>
        <circle cx="620" cy="60" r="4" fill="rgba(224,92,92,.4)"/><circle cx="650" cy="60" r="4" fill="rgba(224,92,92,.4)"/>
        <circle cx="680" cy="60" r="4" fill="rgba(224,92,92,.4)"/><circle cx="710" cy="60" r="4" fill="rgba(224,92,92,.4)"/>
        <line x1="740" y1="30" x2="740" y2="72" stroke="var(--coral)" stroke-width="1.5" stroke-dasharray="3,2"/>
        <text x="740" y="28" text-anchor="middle" fill="var(--coral)" font-family="Inter,sans-serif" font-size="7" font-weight="600">L&Iacute;MITE DE GRANO</text>
        <circle cx="770" cy="42" r="4" fill="rgba(224,92,92,.4)"/><circle cx="800" cy="42" r="4" fill="rgba(224,92,92,.4)"/>
        <circle cx="830" cy="42" r="4" fill="rgba(224,92,92,.4)"/><circle cx="860" cy="42" r="4" fill="rgba(224,92,92,.4)"/>
        <circle cx="770" cy="62" r="4" fill="rgba(224,92,92,.4)"/><circle cx="800" cy="62" r="4" fill="rgba(224,92,92,.4)"/>
        <circle cx="830" cy="62" r="4" fill="rgba(224,92,92,.4)"/><circle cx="860" cy="62" r="4" fill="rgba(224,92,92,.4)"/>
        <text x="810" y="78" text-anchor="middle" fill="var(--coral)" font-family="Inter,sans-serif" font-size="8" font-weight="600">L&iacute;mites de grano = autopistas de corrosi&oacute;n &rarr; vida &uacute;til m&aacute;s corta</text>
      </svg>
    </div>

    <!-- CUADR&Iacute;CULA INFERIOR -->

    <!-- SVG CONTENIDO DE F&Oacute;SFORO VS PROPIEDADES -->
    <div class="glass" style="padding:10px 14px;">
      <h3 class="section-title" style="margin-bottom:4px;">Contenido de F&oacute;sforo vs Propiedades del Dep&oacute;sito <span class="sub">dureza, corrosi&oacute;n y magnetismo en el espectro de %P</span></h3>
      <svg viewBox="0 0 1100 140" width="100%" height="140" fill="none" xmlns="http://www.w3.org/2000/svg">
        <!-- Shaded bands -->
        <rect x="130" y="15" width="143" height="105" rx="4" fill="rgba(224,92,92,.06)"/>
        <text x="201" y="12" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="700" font-size="8" letter-spacing=".05em">BAJO F&Oacute;SFORO</text>
        <rect x="416" y="15" width="215" height="105" rx="4" fill="rgba(232,160,32,.06)"/>
        <text x="523" y="12" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="700" font-size="8" letter-spacing=".05em">MEDIO F&Oacute;SFORO</text>
        <rect x="702" y="15" width="215" height="105" rx="4" fill="rgba(46,196,182,.06)"/>
        <text x="809" y="12" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="700" font-size="8" letter-spacing=".05em">ALTO F&Oacute;SFORO</text>
        <!-- Axes -->
        <line x1="58" y1="120" x2="960" y2="120" stroke="var(--muted)" stroke-width="1" opacity=".5"/>
        <line x1="58" y1="15" x2="58" y2="120" stroke="var(--muted)" stroke-width="1" opacity=".5"/>
        <!-- X-axis ticks -->
        <line x1="130" y1="118" x2="130" y2="122" stroke="var(--muted)" stroke-width="1"/><text x="130" y="132" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="8">2%</text>
        <line x1="201" y1="118" x2="201" y2="122" stroke="var(--muted)" stroke-width="1"/><text x="201" y="132" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="8">4%</text>
        <line x1="273" y1="118" x2="273" y2="122" stroke="var(--muted)" stroke-width="1"/><text x="273" y="132" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="8">6%</text>
        <line x1="345" y1="118" x2="345" y2="122" stroke="var(--muted)" stroke-width="1"/><text x="345" y="132" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="8">8%</text>
        <line x1="416" y1="118" x2="416" y2="122" stroke="var(--muted)" stroke-width="1"/><text x="416" y="132" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="8">10%</text>
        <line x1="488" y1="118" x2="488" y2="122" stroke="var(--muted)" stroke-width="1"/><text x="488" y="132" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="8">12%</text>
        <line x1="560" y1="118" x2="560" y2="122" stroke="var(--muted)" stroke-width="1"/><text x="560" y="132" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="8">14%</text>
        <!-- Y-axis label -->
        <text x="20" y="70" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="7" transform="rotate(-90,20,70)">Escala Relativa</text>
        <!-- Curve 1: Dureza (coral) -->
        <polyline points="130,25 201,35 273,42 345,50 416,58 488,68 560,78 630,85 702,90 810,95 917,100" stroke="var(--coral)" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
        <!-- Curve 2: Resistencia a corrosi&oacute;n (teal) -->
        <polyline points="130,110 201,108 273,105 345,102 416,98 488,92 560,85 630,70 702,50 810,30 917,22" stroke="var(--teal)" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
        <!-- Curve 3: Permeabilidad magn&eacute;tica (amber) -->
        <polyline points="130,28 201,30 273,35 345,42 416,55 488,75 560,95 630,110 702,115 810,117 917,118" stroke="var(--amber)" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
        <!-- Data point dots -->
        <circle cx="130" cy="25" r="3" fill="var(--coral)"/><circle cx="917" cy="100" r="3" fill="var(--coral)"/>
        <circle cx="130" cy="110" r="3" fill="var(--teal)"/><circle cx="917" cy="22" r="3" fill="var(--teal)"/>
        <circle cx="130" cy="28" r="3" fill="var(--amber)"/><circle cx="630" cy="110" r="3" fill="var(--amber)"/>
        <!-- Legend -->
        <rect x="740" y="125" width="220" height="14" rx="3" fill="rgba(0,0,0,.03)"/>
        <line x1="750" y1="132" x2="768" y2="132" stroke="var(--coral)" stroke-width="2"/><text x="772" y="135" fill="var(--coral)" font-family="Inter,sans-serif" font-size="7" font-weight="600">Dureza HV</text>
        <line x1="830" y1="132" x2="848" y2="132" stroke="var(--teal)" stroke-width="2"/><text x="852" y="135" fill="var(--teal)" font-family="Inter,sans-serif" font-size="7" font-weight="600">Corrosi&oacute;n (NSS hr)</text>
        <line x1="935" y1="132" x2="948" y2="132" stroke="var(--amber)" stroke-width="2"/><text x="952" y="135" fill="var(--amber)" font-family="Inter,sans-serif" font-size="7" font-weight="600">&mu;</text>
      </svg>
    </div>

    <div class="bottom-grid">
      <div>
        <h3 class="section-title">&iquest;Por Qu&eacute; Alto F&oacute;sforo? <span class="sub">el campe&oacute;n anticorrosi&oacute;n</span></h3>
        <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
          <table class="data-table bath">
            <thead><tr><th>Propiedad</th><th>Alto F&oacute;sforo (10&ndash;13% P)</th></tr></thead>
            <tbody>
              <tr><td style="font-weight:600;">Dureza (tal como se deposita)</td><td class="mono">450&ndash;550 HV</td></tr>
              <tr><td style="font-weight:600;">Dureza (horneado 400&deg;C/1hr)</td><td class="mono">850&ndash;1000 HV</td></tr>
              <tr><td style="font-weight:600;">Corrosi&oacute;n (niebla salina)</td><td class="mono">&gt;1000 hr (25 &micro;m en acero)</td></tr>
              <tr><td style="font-weight:600;">Soldabilidad</td><td>Pobre sin activaci&oacute;n</td></tr>
              <tr><td style="font-weight:600;">Magn&eacute;tico</td><td>No magn&eacute;tico (&gt;10.5% P)</td></tr>
              <tr><td style="font-weight:600;">Estructura</td><td>Completamente amorfo &mdash; sin l&iacute;mites de grano</td></tr>
            </tbody>
          </table>
        </div>
      </div>
      <div>
        <h3 class="section-title">Qu&iacute;mica del Ba&ntilde;o <span class="sub">Etapa 5</span></h3>
        <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
          <table class="data-table bath">
            <thead><tr><th>Componente</th><th>Rango</th></tr></thead>
            <tbody>
              <tr><td>N&iacute;quel (como Ni&sup2;&#8314;)</td><td class="mono">4.5&ndash;6.5 g/L</td></tr>
              <tr><td>Hipofosfito de Sodio</td><td class="mono">25&ndash;40 g/L</td></tr>
              <tr><td>&Aacute;cidos Org&aacute;nicos (complejantes)</td><td class="mono">Seg&uacute;n FTS del proveedor</td></tr>
              <tr><td>pH</td><td class="mono">4.2&ndash;4.8</td></tr>
              <tr><td>Temperatura</td><td class="mono">85&ndash;91&deg;C</td></tr>
              <tr><td>Velocidad de Dep&oacute;sito</td><td class="mono">8&ndash;15 &micro;m/hr</td></tr>
              <tr><td>Carga</td><td class="mono">0.5&ndash;1.5 dm&sup2;/L</td></tr>
              <tr><td>Vida del Ba&ntilde;o</td><td class="mono">5&ndash;7 MTO t&iacute;pico</td></tr>
            </tbody>
          </table>
        </div>
        <h3 class="section-title" style="margin-top:10px;">Especificaciones <span class="sub">comunes</span></h3>
        <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
          <table class="data-table bath">
            <thead><tr><th>C&oacute;digo</th><th>Alcance</th></tr></thead>
            <tbody>
              <tr><td class="mono">ASTM B733</td><td>SC4 (Tipo V) &mdash; alto f&oacute;sforo (&ge;10% P)</td></tr>
              <tr><td class="mono">AMS 2404</td><td>Clase 1&ndash;4 &mdash; EN aeroespacial</td></tr>
              <tr><td class="mono">MIL-C-26074</td><td>Clase 4 &mdash; EN militar alto P</td></tr>
              <tr><td class="mono">ASTM B849</td><td>Horneado Alivio HE</td></tr>
              <tr><td class="mono">NACE SP0170</td><td>Recubrimientos tuber&iacute;as / petr&oacute;leo y gas</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- COMPARACI&Oacute;N -->
    <div>
      <h3 class="section-title">Alto F&oacute;sforo vs Otros Tipos EN <span class="sub">posicionamiento</span></h3>
      <div class="compare-grid">
        <div class="glass compare-card do" style="padding:8px 14px;">
          <h4 style="font-size:18px;margin-bottom:5px;">Fortalezas Alto P <span class="tag good">Campe&oacute;n</span></h4>
          <ul>
            <li>Mejor resistencia a corrosi&oacute;n de toda formulaci&oacute;n EN</li>
            <li>No magn&eacute;tico &mdash; cr&iacute;tico para electr&oacute;nica, HDD, MRI</li>
            <li>Completamente amorfo &mdash; sin ataque intergranular</li>
          </ul>
        </div>
        <div class="glass compare-card dont" style="padding:8px 14px;">
          <h4 style="font-size:18px;margin-bottom:5px;">Cu&aacute;ndo Elegir Diferente <span class="tag bad">L&iacute;mites</span></h4>
          <ul>
            <li>M&aacute;xima dureza necesaria &rarr; Bajo F&oacute;sforo (2&ndash;4% P)</li>
            <li>Soldabilidad requerida &rarr; Medio F&oacute;sforo (6&ndash;9% P)</li>
            <li>Hornear destruye estructura amorfa y propiedad no magn&eacute;tica</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="insight-card">
      <div class="insight-label">La Trampa de la Cristalizaci&oacute;n</div>
      <div class="insight-text">Tratar t&eacute;rmicamente EN de alto f&oacute;sforo por encima de 260&deg;C cristaliza el dep&oacute;sito en Ni + Ni&#8323;P, aumentando dram&aacute;ticamente la dureza pero <strong>destruyendo</strong> tanto la resistencia a corrosi&oacute;n amorfa como la propiedad no magn&eacute;tica. Si su especificaci&oacute;n requiere resistencia a corrosi&oacute;n o comportamiento no magn&eacute;tico, no hornee por encima de 260&deg;C. El horneado de alivio HE a 190&deg;C preserva ambas propiedades.</div>
    </div>
"""

# =====================================================================
# POSTER 00 — SHOP FLOOR
# =====================================================================
SF_BODY_EN["00"] = """
    <div class="glass key-card">
      <div class="key-num">10&ndash;13%</div>
      <div class="key-label">Phosphorus Content &mdash; Maximum Corrosion Resistance</div>
      <div class="key-text">High-phos EN is fully amorphous &mdash; no grain boundaries means no weak points for corrosion to attack. Non-magnetic, uniform thickness everywhere, and the toughest EN deposit against chemical attack. Every prep step matters &mdash; the bath does not forgive contamination.</div>
    </div>

    <!-- SIMPLIFIED PROCESS FLOW -->
    <div class="glass" style="padding:8px 10px;">
      <svg viewBox="0 0 820 55" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block;">
        <rect x="0" y="5" width="90" height="30" rx="5" fill="rgba(46,196,182,.10)" stroke="var(--teal)" stroke-width="1.2"/>
        <text x="45" y="18" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" text-anchor="middle">01 CLEAN</text>
        <text x="45" y="29" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="6.5" text-anchor="middle">60&ndash;80&deg;C</text>
        <line x1="90" y1="20" x2="105" y2="20" stroke="var(--faint)" stroke-width="1"/><polygon points="105,17 110,20 105,23" fill="var(--faint)"/>
        <rect x="112" y="5" width="80" height="30" rx="5" fill="rgba(46,196,182,.10)" stroke="var(--teal)" stroke-width="1.2"/>
        <text x="152" y="18" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" text-anchor="middle">02 RINSE</text>
        <text x="152" y="29" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="6.5" text-anchor="middle">&lt;50 &mu;S</text>
        <line x1="192" y1="20" x2="207" y2="20" stroke="var(--faint)" stroke-width="1"/><polygon points="207,17 212,20 207,23" fill="var(--faint)"/>
        <rect x="214" y="5" width="90" height="30" rx="5" fill="rgba(224,92,92,.10)" stroke="var(--coral)" stroke-width="1.2"/>
        <text x="259" y="18" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" text-anchor="middle">03 ACTIVATE</text>
        <text x="259" y="29" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="6.5" text-anchor="middle">30&ndash;120 s</text>
        <line x1="304" y1="20" x2="319" y2="20" stroke="var(--faint)" stroke-width="1"/><polygon points="319,17 324,20 319,23" fill="var(--faint)"/>
        <rect x="326" y="5" width="80" height="30" rx="5" fill="rgba(46,196,182,.10)" stroke="var(--teal)" stroke-width="1.2"/>
        <text x="366" y="18" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" text-anchor="middle">04 RINSE</text>
        <text x="366" y="29" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="6.5" text-anchor="middle">&lt;20 &mu;S</text>
        <line x1="406" y1="20" x2="421" y2="20" stroke="var(--faint)" stroke-width="1"/><polygon points="421,17 426,20 421,23" fill="var(--faint)"/>
        <rect x="428" y="2" width="105" height="36" rx="5" fill="rgba(224,92,92,.10)" stroke="var(--coral)" stroke-width="1.5"/>
        <text x="480" y="17" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="9" text-anchor="middle">05 EN BATH</text>
        <text x="480" y="30" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="6.5" text-anchor="middle">85&ndash;91&deg;C</text>
        <line x1="533" y1="20" x2="548" y2="20" stroke="var(--faint)" stroke-width="1"/><polygon points="548,17 553,20 548,23" fill="var(--faint)"/>
        <rect x="555" y="5" width="80" height="30" rx="5" fill="rgba(46,196,182,.10)" stroke="var(--teal)" stroke-width="1.2"/>
        <text x="595" y="18" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" text-anchor="middle">06 RINSE</text>
        <text x="595" y="29" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="6.5" text-anchor="middle">&lt;10 s xfer</text>
        <line x1="635" y1="20" x2="650" y2="20" stroke="var(--faint)" stroke-width="1"/><polygon points="650,17 655,20 650,23" fill="var(--faint)"/>
        <rect x="657" y="5" width="100" height="30" rx="5" fill="rgba(39,174,96,.10)" stroke="var(--emerald)" stroke-width="1.2"/>
        <text x="707" y="18" fill="var(--emerald)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" text-anchor="middle">07 POST-TREAT</text>
        <text x="707" y="29" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="6.5" text-anchor="middle">190&ndash;400&deg;C</text>
        <text x="410" y="51" fill="var(--faint)" font-family="Inter,sans-serif" font-size="6.5" font-style="italic" text-anchor="middle">Follow all 7 stages in order &mdash; no skipping</text>
      </svg>
    </div>

    <div class="glass" style="padding:10px 12px;">
      <div class="section-title">Critical Control Points <span style="font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:.10em;color:var(--muted);margin-left:8px;">WATCH THESE 3</span></div>
      <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;">
        <div style="padding:8px 10px;border-radius:8px;background:rgba(232,160,32,.08);border:1px solid rgba(232,160,32,.2);"><div style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:13px;color:var(--amber);letter-spacing:.04em;margin-bottom:3px;">01 &mdash; CLEANING</div><div style="font-size:10.5px;color:var(--muted);line-height:1.35;">EN only deposits on a completely clean surface. Water break test = pass or re-clean.</div></div>
        <div style="padding:8px 10px;border-radius:8px;background:rgba(224,92,92,.08);border:1px solid rgba(224,92,92,.2);"><div style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:13px;color:var(--coral);letter-spacing:.04em;margin-bottom:3px;">05 &mdash; EN BATH</div><div style="font-size:10.5px;color:var(--muted);line-height:1.35;">85&ndash;91&deg;C, pH 4.2&ndash;4.8. Bath can decompose if temp or stabilizer is off.</div></div>
        <div style="padding:8px 10px;border-radius:8px;background:rgba(39,174,96,.08);border:1px solid rgba(39,174,96,.2);"><div style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:13px;color:var(--emerald);letter-spacing:.04em;margin-bottom:3px;">07 &mdash; POST-TREAT</div><div style="font-size:10.5px;color:var(--muted);line-height:1.35;">HE bake for high-strength steel is mandatory within 4 hours. Do NOT bake &gt;260&deg;C if corrosion resistance or non-magnetic property is required.</div></div>
      </div>
    </div>

    <div class="glass" style="padding:10px 12px;">
      <div class="section-title">Process Sequence</div>
      <table class="flow-table">
        <thead><tr><th>#</th><th>Step</th><th>Temp</th><th>Time</th></tr></thead>
        <tbody>
          <tr><td class="mono">01</td><td>Alkaline Soak Clean</td><td class="mono">140&ndash;176&deg;F</td><td class="mono">3&ndash;10 min</td></tr>
          <tr><td class="mono">02</td><td>Cascade Rinse</td><td class="mono">Ambient</td><td class="mono">30&ndash;60 sec/stage</td></tr>
          <tr><td class="mono">03</td><td>Acid Activation</td><td class="mono">Ambient</td><td class="mono">30&ndash;120 sec</td></tr>
          <tr><td class="mono">04</td><td>Critical Rinse</td><td class="mono">Ambient</td><td class="mono">30&ndash;60 sec</td></tr>
          <tr><td class="mono">05</td><td>EN High Phos Bath</td><td class="mono">185&ndash;196&deg;F</td><td class="mono">60&ndash;180 min</td></tr>
          <tr><td class="mono">06</td><td>Final Rinse</td><td class="mono">Cold</td><td class="mono">30&ndash;60 sec</td></tr>
          <tr><td class="mono">07</td><td>Post Treatment (Bake/Seal)</td><td class="mono">375&ndash;750&deg;F</td><td class="mono">1&ndash;4+ hr</td></tr>
        </tbody>
      </table>
    </div>

    <div class="compare-row">
      <div class="compare-card glass do"><div class="compare-head good">&#10003; Do</div><ul class="compare-list"><li>Follow all 7 stages in order, every load</li><li>Water-break test every rack after cleaning</li><li>Transfer promptly &mdash; never let parts dry</li><li>Report any unusual bath behavior immediately</li></ul></div>
      <div class="compare-card glass dont"><div class="compare-head bad">&#10007; Don&rsquo;t</div><ul class="compare-list"><li>Skip any stage &mdash; each one protects the next</li><li>Touch parts with bare hands after cleaning</li><li>Drag acid into the EN bath</li><li>Try to control a decomposing bath &mdash; EVACUATE</li></ul></div>
    </div>

    <div class="glass safety-card">
      <div class="section-title coral">&#9888; Safety &mdash; All Stages</div>
      <div class="safety-text"><strong>Hot alkaline</strong> (Stage 1) &mdash; chemical burns. <strong>Mineral acid</strong> (Stage 3) &mdash; burns, HCl fumes. <strong>EN bath</strong> (Stage 5) &mdash; 85&ndash;91&deg;C hot acidic nickel solution; hydrogen gas generation; skin sensitizer (GHS Cat. 1); soluble nickel compounds are GHS Category 1A carcinogen (IARC Group 1 &mdash; known human carcinogen via inhalation). <strong>Phosphine risk</strong> &mdash; a decomposing bath can release PH&#8323; gas (TLV 0.05 ppm). If unusual odor, turbidity, or temperature spike: EVACUATE immediately. Emergency shower and eyewash within 10 seconds of every station. SDSs accessible. No eating, drinking, or smoking on the line.</div>
    </div>
"""

SF_BODY_ES["00"] = """
    <div class="glass key-card">
      <div class="key-num">10&ndash;13%</div>
      <div class="key-label">Contenido de F&oacute;sforo &mdash; M&aacute;xima Resistencia a Corrosi&oacute;n</div>
      <div class="key-text">EN de alto f&oacute;sforo es completamente amorfo &mdash; sin l&iacute;mites de grano significa sin puntos d&eacute;biles para que la corrosi&oacute;n ataque. No magn&eacute;tico, espesor uniforme en todas partes, y el dep&oacute;sito EN m&aacute;s resistente al ataque qu&iacute;mico. Cada paso de preparaci&oacute;n importa &mdash; el ba&ntilde;o no perdona la contaminaci&oacute;n.</div>
    </div>

    <div class="glass" style="padding:8px 10px;">
      <svg viewBox="0 0 820 55" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block;">
        <rect x="0" y="5" width="90" height="30" rx="5" fill="rgba(46,196,182,.10)" stroke="var(--teal)" stroke-width="1.2"/>
        <text x="45" y="18" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" text-anchor="middle">01 LIMPIAR</text>
        <text x="45" y="29" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="6.5" text-anchor="middle">60&ndash;80&deg;C</text>
        <line x1="90" y1="20" x2="105" y2="20" stroke="var(--faint)" stroke-width="1"/><polygon points="105,17 110,20 105,23" fill="var(--faint)"/>
        <rect x="112" y="5" width="80" height="30" rx="5" fill="rgba(46,196,182,.10)" stroke="var(--teal)" stroke-width="1.2"/>
        <text x="152" y="18" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" text-anchor="middle">02 ENJUAGUE</text>
        <text x="152" y="29" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="6.5" text-anchor="middle">&lt;50 &mu;S</text>
        <line x1="192" y1="20" x2="207" y2="20" stroke="var(--faint)" stroke-width="1"/><polygon points="207,17 212,20 207,23" fill="var(--faint)"/>
        <rect x="214" y="5" width="90" height="30" rx="5" fill="rgba(224,92,92,.10)" stroke="var(--coral)" stroke-width="1.2"/>
        <text x="259" y="18" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" text-anchor="middle">03 ACTIVAR</text>
        <text x="259" y="29" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="6.5" text-anchor="middle">30&ndash;120 s</text>
        <line x1="304" y1="20" x2="319" y2="20" stroke="var(--faint)" stroke-width="1"/><polygon points="319,17 324,20 319,23" fill="var(--faint)"/>
        <rect x="326" y="5" width="80" height="30" rx="5" fill="rgba(46,196,182,.10)" stroke="var(--teal)" stroke-width="1.2"/>
        <text x="366" y="18" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" text-anchor="middle">04 ENJUAGUE</text>
        <text x="366" y="29" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="6.5" text-anchor="middle">&lt;20 &mu;S</text>
        <line x1="406" y1="20" x2="421" y2="20" stroke="var(--faint)" stroke-width="1"/><polygon points="421,17 426,20 421,23" fill="var(--faint)"/>
        <rect x="428" y="2" width="105" height="36" rx="5" fill="rgba(224,92,92,.10)" stroke="var(--coral)" stroke-width="1.5"/>
        <text x="480" y="17" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="9" text-anchor="middle">05 BA&Ntilde;O EN</text>
        <text x="480" y="30" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="6.5" text-anchor="middle">85&ndash;91&deg;C</text>
        <line x1="533" y1="20" x2="548" y2="20" stroke="var(--faint)" stroke-width="1"/><polygon points="548,17 553,20 548,23" fill="var(--faint)"/>
        <rect x="555" y="5" width="80" height="30" rx="5" fill="rgba(46,196,182,.10)" stroke="var(--teal)" stroke-width="1.2"/>
        <text x="595" y="18" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" text-anchor="middle">06 ENJUAGUE</text>
        <text x="595" y="29" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="6.5" text-anchor="middle">&lt;10 s xfer</text>
        <line x1="635" y1="20" x2="650" y2="20" stroke="var(--faint)" stroke-width="1"/><polygon points="650,17 655,20 650,23" fill="var(--faint)"/>
        <rect x="657" y="5" width="100" height="30" rx="5" fill="rgba(39,174,96,.10)" stroke="var(--emerald)" stroke-width="1.2"/>
        <text x="707" y="18" fill="var(--emerald)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" text-anchor="middle">07 POST-TRAT</text>
        <text x="707" y="29" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="6.5" text-anchor="middle">190&ndash;400&deg;C</text>
        <text x="410" y="51" fill="var(--faint)" font-family="Inter,sans-serif" font-size="6.5" font-style="italic" text-anchor="middle">Siga las 7 etapas en orden &mdash; sin omitir ninguna</text>
      </svg>
    </div>

    <div class="glass" style="padding:10px 12px;">
      <div class="section-title">Puntos de Control Cr&iacute;ticos <span style="font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:.10em;color:var(--muted);margin-left:8px;">VIGILE ESTOS 3</span></div>
      <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;">
        <div style="padding:8px 10px;border-radius:8px;background:rgba(232,160,32,.08);border:1px solid rgba(232,160,32,.2);"><div style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:13px;color:var(--amber);letter-spacing:.04em;margin-bottom:3px;">01 &mdash; LIMPIEZA</div><div style="font-size:10.5px;color:var(--muted);line-height:1.35;">EN solo deposita sobre superficie completamente limpia. Prueba de ruptura de agua = pasa o re-limpie.</div></div>
        <div style="padding:8px 10px;border-radius:8px;background:rgba(224,92,92,.08);border:1px solid rgba(224,92,92,.2);"><div style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:13px;color:var(--coral);letter-spacing:.04em;margin-bottom:3px;">05 &mdash; BA&Ntilde;O EN</div><div style="font-size:10.5px;color:var(--muted);line-height:1.35;">85&ndash;91&deg;C, pH 4.2&ndash;4.8. El ba&ntilde;o puede descomponerse si temperatura o estabilizador est&aacute;n fuera de rango.</div></div>
        <div style="padding:8px 10px;border-radius:8px;background:rgba(39,174,96,.08);border:1px solid rgba(39,174,96,.2);"><div style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:13px;color:var(--emerald);letter-spacing:.04em;margin-bottom:3px;">07 &mdash; POST-TRAT</div><div style="font-size:10.5px;color:var(--muted);line-height:1.35;">Horneado HE para acero de alta resistencia es obligatorio dentro de 4 horas. NO hornee &gt;260&deg;C si se requiere resistencia a corrosi&oacute;n o propiedad no magn&eacute;tica.</div></div>
      </div>
    </div>

    <div class="glass" style="padding:10px 12px;">
      <div class="section-title">Secuencia de Proceso</div>
      <table class="flow-table">
        <thead><tr><th>#</th><th>Etapa</th><th>Temp</th><th>Tiempo</th></tr></thead>
        <tbody>
          <tr><td class="mono">01</td><td>Limpieza Alcalina por Inmersi&oacute;n</td><td class="mono">60&ndash;80&deg;C</td><td class="mono">3&ndash;10 min</td></tr>
          <tr><td class="mono">02</td><td>Enjuague en Cascada</td><td class="mono">Ambiente</td><td class="mono">30&ndash;60 s/etapa</td></tr>
          <tr><td class="mono">03</td><td>Activaci&oacute;n &Aacute;cida</td><td class="mono">Ambiente</td><td class="mono">30&ndash;120 s</td></tr>
          <tr><td class="mono">04</td><td>Enjuague Cr&iacute;tico</td><td class="mono">Ambiente</td><td class="mono">30&ndash;60 s</td></tr>
          <tr><td class="mono">05</td><td>Ba&ntilde;o EN Alto F&oacute;sforo</td><td class="mono">85&ndash;91&deg;C</td><td class="mono">60&ndash;180 min</td></tr>
          <tr><td class="mono">06</td><td>Enjuague Final</td><td class="mono">Fr&iacute;o</td><td class="mono">30&ndash;60 s</td></tr>
          <tr><td class="mono">07</td><td>Post Tratamiento (Horneado/Sellado)</td><td class="mono">190&ndash;400&deg;C</td><td class="mono">1&ndash;4+ hr</td></tr>
        </tbody>
      </table>
    </div>

    <div class="compare-row">
      <div class="compare-card glass do"><div class="compare-head good">&#10003; Haga</div><ul class="compare-list"><li>Siga las 7 etapas en orden, cada carga</li><li>Prueba de ruptura de agua en cada rack despu&eacute;s de limpiar</li><li>Transfiera r&aacute;pidamente &mdash; nunca deje secar las piezas</li><li>Reporte cualquier comportamiento inusual del ba&ntilde;o inmediatamente</li></ul></div>
      <div class="compare-card glass dont"><div class="compare-head bad">&#10007; No Haga</div><ul class="compare-list"><li>Omitir ninguna etapa &mdash; cada una protege la siguiente</li><li>Tocar piezas con manos desnudas despu&eacute;s de limpiar</li><li>Arrastrar &aacute;cido al ba&ntilde;o EN</li><li>Intentar controlar un ba&ntilde;o en descomposici&oacute;n &mdash; EVACUE</li></ul></div>
    </div>

    <div class="glass safety-card">
      <div class="section-title coral">&#9888; Seguridad &mdash; Todas las Etapas</div>
      <div class="safety-text"><strong>Alcalino caliente</strong> (Etapa 1) &mdash; quemaduras qu&iacute;micas. <strong>&Aacute;cido mineral</strong> (Etapa 3) &mdash; quemaduras, vapores de HCl. <strong>Ba&ntilde;o EN</strong> (Etapa 5) &mdash; 85&ndash;91&deg;C soluci&oacute;n &aacute;cida caliente de n&iacute;quel; generaci&oacute;n de gas hidr&oacute;geno; sensibilizante cut&aacute;neo (GHS Cat. 1); compuestos solubles de n&iacute;quel son carcin&oacute;geno GHS Categor&iacute;a 1A (IARC Grupo 1 &mdash; carcin&oacute;geno humano conocido por inhalaci&oacute;n). <strong>Riesgo de fosfina</strong> &mdash; un ba&ntilde;o en descomposici&oacute;n puede liberar gas PH&#8323; (TLV 0.05 ppm). Si detecta olor inusual, turbidez o pico de temperatura: EVACUE inmediatamente. Regadera y lavaojos a 10 segundos de cada estaci&oacute;n. FTS accesibles. No comer, beber ni fumar en la l&iacute;nea.</div>
    </div>
"""

# =====================================================================
# POSTER 01 — PROCESS FLOW
# =====================================================================
TECH_BODY_EN["01"] = """
    <!-- EXPANDED PROCESS FLOW SVG — 15+ nodes with rinses -->
    <div class="glass process-flow" style="height:auto;padding:12px 16px;">
      <svg viewBox="0 0 1100 130" width="100%" height="130" fill="none" xmlns="http://www.w3.org/2000/svg">
        <!-- Row 1: Steps 1-8 -->
        <circle cx="60" cy="28" r="18" stroke="var(--amber)" stroke-width="1.6" fill="rgba(232,160,32,.12)"/>
        <text x="60" y="33" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="14">1</text>
        <text x="60" y="55" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" letter-spacing=".04em" opacity=".62">SOAK</text>
        <text x="60" y="63" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" letter-spacing=".04em" opacity=".62">CLEAN</text>
        <line x1="80" y1="28" x2="106" y2="28" stroke="currentColor" stroke-width="1.2" opacity=".35"/><polygon points="106,25 112,28 106,31" fill="currentColor" opacity=".35"/>

        <circle cx="135" cy="28" r="14" stroke="var(--teal)" stroke-width="1.2" fill="rgba(46,196,182,.10)"/>
        <text x="135" y="32" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11">R1</text>
        <text x="135" y="55" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="7" opacity=".5">RINSE</text>
        <line x1="151" y1="28" x2="177" y2="28" stroke="currentColor" stroke-width="1.2" opacity=".35"/><polygon points="177,25 183,28 177,31" fill="currentColor" opacity=".35"/>

        <circle cx="206" cy="28" r="18" stroke="var(--amber)" stroke-width="1.6" fill="rgba(232,160,32,.12)"/>
        <text x="206" y="33" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="14">2</text>
        <text x="206" y="55" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" letter-spacing=".04em" opacity=".62">ELECTRO</text>
        <text x="206" y="63" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" letter-spacing=".04em" opacity=".62">CLEAN</text>
        <line x1="226" y1="28" x2="252" y2="28" stroke="currentColor" stroke-width="1.2" opacity=".35"/><polygon points="252,25 258,28 252,31" fill="currentColor" opacity=".35"/>

        <circle cx="281" cy="28" r="14" stroke="var(--teal)" stroke-width="1.2" fill="rgba(46,196,182,.10)"/>
        <text x="281" y="32" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11">R2</text>
        <text x="281" y="55" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="7" opacity=".5">RINSE</text>
        <line x1="297" y1="28" x2="323" y2="28" stroke="currentColor" stroke-width="1.2" opacity=".35"/><polygon points="323,25 329,28 323,31" fill="currentColor" opacity=".35"/>

        <circle cx="352" cy="28" r="18" stroke="var(--coral)" stroke-width="1.6" fill="rgba(224,92,92,.12)"/>
        <text x="352" y="33" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="14">3</text>
        <text x="352" y="55" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" letter-spacing=".04em" opacity=".62">ACID</text>
        <text x="352" y="63" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" letter-spacing=".04em" opacity=".62">ACTIVATE</text>
        <line x1="372" y1="28" x2="398" y2="28" stroke="currentColor" stroke-width="1.2" opacity=".35"/><polygon points="398,25 404,28 398,31" fill="currentColor" opacity=".35"/>

        <circle cx="427" cy="28" r="14" stroke="var(--teal)" stroke-width="1.2" fill="rgba(46,196,182,.10)"/>
        <text x="427" y="32" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11">R3</text>
        <text x="427" y="55" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="7" opacity=".5">RINSE</text>
        <line x1="443" y1="28" x2="469" y2="28" stroke="currentColor" stroke-width="1.2" opacity=".35"/><polygon points="469,25 475,28 469,31" fill="currentColor" opacity=".35"/>

        <circle cx="498" cy="28" r="14" stroke="var(--teal)" stroke-width="1.2" fill="rgba(46,196,182,.10)"/>
        <text x="498" y="32" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11">R4</text>
        <text x="498" y="55" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="7" opacity=".5">DI</text>
        <line x1="514" y1="28" x2="540" y2="28" stroke="currentColor" stroke-width="1.2" opacity=".35"/><polygon points="540,25 546,28 540,31" fill="currentColor" opacity=".35"/>

        <!-- Row 1 continued: EN Bath (large) -->
        <circle cx="585" cy="28" r="22" stroke="var(--coral)" stroke-width="2.2" fill="rgba(224,92,92,.12)"/>
        <text x="585" y="22" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="10">EN</text>
        <text x="585" y="35" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="14">5</text>
        <text x="585" y="60" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" letter-spacing=".04em" opacity=".62">EN BATH</text>
        <line x1="609" y1="28" x2="635" y2="28" stroke="currentColor" stroke-width="1.2" opacity=".35"/><polygon points="635,25 641,28 635,31" fill="currentColor" opacity=".35"/>

        <circle cx="664" cy="28" r="14" stroke="var(--teal)" stroke-width="1.2" fill="rgba(46,196,182,.10)"/>
        <text x="664" y="32" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11">R5</text>
        <text x="664" y="55" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="7" opacity=".5">RINSE</text>
        <line x1="680" y1="28" x2="706" y2="28" stroke="currentColor" stroke-width="1.2" opacity=".35"/><polygon points="706,25 712,28 706,31" fill="currentColor" opacity=".35"/>

        <circle cx="735" cy="28" r="14" stroke="var(--teal)" stroke-width="1.2" fill="rgba(46,196,182,.10)"/>
        <text x="735" y="32" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11">R6</text>
        <text x="735" y="55" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="7" opacity=".5">DI</text>
        <line x1="751" y1="28" x2="777" y2="28" stroke="currentColor" stroke-width="1.2" opacity=".35"/><polygon points="777,25 783,28 777,31" fill="currentColor" opacity=".35"/>

        <circle cx="812" cy="28" r="18" stroke="var(--emerald)" stroke-width="1.6" fill="rgba(39,174,96,.12)"/>
        <text x="812" y="33" text-anchor="middle" fill="var(--emerald)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="14">6</text>
        <text x="812" y="55" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" letter-spacing=".04em" opacity=".62">DRY</text>
        <line x1="832" y1="28" x2="858" y2="28" stroke="currentColor" stroke-width="1.2" opacity=".35"/><polygon points="858,25 864,28 858,31" fill="currentColor" opacity=".35"/>

        <circle cx="893" cy="28" r="18" stroke="var(--emerald)" stroke-width="1.6" fill="rgba(39,174,96,.12)"/>
        <text x="893" y="33" text-anchor="middle" fill="var(--emerald)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="14">7</text>
        <text x="893" y="55" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" letter-spacing=".04em" opacity=".62">HE BAKE</text>
        <line x1="913" y1="28" x2="939" y2="28" stroke="currentColor" stroke-width="1.2" opacity=".35"/><polygon points="939,25 945,28 939,31" fill="currentColor" opacity=".35"/>

        <circle cx="974" cy="28" r="18" stroke="var(--emerald)" stroke-width="1.6" fill="rgba(39,174,96,.12)"/>
        <text x="974" y="33" text-anchor="middle" fill="var(--emerald)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="14">8</text>
        <text x="974" y="55" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" letter-spacing=".04em" opacity=".62">SEAL /</text>
        <text x="974" y="63" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" letter-spacing=".04em" opacity=".62">CHROMATE</text>

        <!-- Legend -->
        <rect x="30" y="82" width="1040" height="40" rx="6" fill="rgba(255,255,255,.03)" stroke="rgba(255,255,255,.06)" stroke-width=".8"/>
        <circle cx="60" cy="102" r="5" fill="rgba(232,160,32,.3)"/>
        <text x="72" y="106" fill="var(--muted)" font-family="Inter,sans-serif" font-size="8" font-weight="500">Chemical Stage</text>
        <circle cx="180" cy="102" r="5" fill="rgba(46,196,182,.3)"/>
        <text x="192" y="106" fill="var(--muted)" font-family="Inter,sans-serif" font-size="8" font-weight="500">Rinse</text>
        <circle cx="260" cy="102" r="5" fill="rgba(224,92,92,.3)"/>
        <text x="272" y="106" fill="var(--muted)" font-family="Inter,sans-serif" font-size="8" font-weight="500">Critical Process</text>
        <circle cx="390" cy="102" r="5" fill="rgba(39,174,96,.3)"/>
        <text x="402" y="106" fill="var(--muted)" font-family="Inter,sans-serif" font-size="8" font-weight="500">Post-Treatment</text>
        <text x="560" y="106" fill="var(--faint)" font-family="Inter,sans-serif" font-size="8" font-style="italic">Expanded line sequence &mdash; every rinse shown. Actual tank count varies by shop layout.</text>
      </svg>
    </div>

    <!-- DETAILED SEQUENCE TABLE -->
    <div>
      <h3 class="section-title">Expanded Process Sequence <span class="sub">all stages + rinses</span></h3>
      <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
        <table class="data-table compact">
          <thead><tr><th style="width:32px;">Step</th><th>Stage</th><th>Temp</th><th>Time</th><th>Key Control</th></tr></thead>
          <tbody>
            <tr><td class="mono">1</td><td>Alkaline Soak Clean</td><td class="mono">140&ndash;176&deg;F (60&ndash;80&deg;C)</td><td class="mono">3&ndash;10 min</td><td>Water-break-free surface required</td></tr>
            <tr><td class="mono">R1</td><td>Overflow Rinse</td><td class="mono">Ambient</td><td class="mono">30&ndash;60 s</td><td>Remove bulk alkaline; &lt;200 &micro;S/cm</td></tr>
            <tr><td class="mono">2</td><td>Electroclean (cathodic or anodic)</td><td class="mono">140&ndash;160&deg;F (60&ndash;71&deg;C)</td><td class="mono">1&ndash;3 min</td><td>3&ndash;6 V; gas scrubbing action</td></tr>
            <tr><td class="mono">R2</td><td>Cascade Rinse (2 stage)</td><td class="mono">Ambient</td><td class="mono">30&ndash;60 s/stage</td><td>Conductivity &lt;50 &micro;S/cm leaving</td></tr>
            <tr><td class="mono">3</td><td>Acid Activation</td><td class="mono">Ambient</td><td class="mono">30&ndash;120 s</td><td>HCl 10&ndash;20% v/v (steel); HNO&#8323; or double zincate (Al)</td></tr>
            <tr><td class="mono">R3</td><td>Rinse</td><td class="mono">Ambient</td><td class="mono">30 s</td><td>Remove acid drag-out</td></tr>
            <tr><td class="mono">R4</td><td>Critical DI Rinse (Pre-EN)</td><td class="mono">Ambient</td><td class="mono">30&ndash;60 s</td><td>Conductivity &lt;20 &micro;S/cm; DI water only</td></tr>
            <tr><td class="mono">5</td><td style="font-weight:600;">EN High Phos Bath</td><td class="mono">185&ndash;196&deg;F (85&ndash;91&deg;C)</td><td class="mono">60&ndash;180 min</td><td>pH 4.2&ndash;4.8; Ni&sup2;&#8314; 4.5&ndash;6.5 g/L</td></tr>
            <tr><td class="mono">R5</td><td>Drag-Out Recovery Rinse</td><td class="mono">Ambient</td><td class="mono">15&ndash;30 s</td><td>Transfer in &lt;10 sec; captures Ni for return</td></tr>
            <tr><td class="mono">R6</td><td>Final DI Rinse</td><td class="mono">Cold / warm</td><td class="mono">30&ndash;60 s</td><td>Spot-free surface; &lt;10 &micro;S/cm</td></tr>
            <tr><td class="mono">6</td><td>Hot Air Dry</td><td class="mono">150&ndash;180&deg;F (65&ndash;82&deg;C)</td><td class="mono">2&ndash;5 min</td><td>No water spots; blow-off or oven</td></tr>
            <tr><td class="mono">7</td><td>HE Bake (if required)</td><td class="mono">375&deg;F (190&deg;C)</td><td class="mono">4+ hr</td><td>Within 4 hr of plating for high-strength steel</td></tr>
            <tr><td class="mono">8</td><td>Chromate / Sealant (if required)</td><td class="mono">Per spec</td><td class="mono">Per spec</td><td>Additional corrosion protection or cosmetic finish</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- EN FORMULATION COMPARISON -->
    <div>
      <h3 class="section-title">EN Formulation Comparison <span class="sub">low &bull; mid &bull; high phos</span></h3>
      <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
        <table class="data-table compact">
          <thead><tr><th>Property</th><th>Low Phos (2&ndash;4% P)</th><th>Mid Phos (6&ndash;9% P)</th><th style="background:rgba(46,196,182,.12);">High Phos (10&ndash;13% P)</th></tr></thead>
          <tbody>
            <tr><td style="font-weight:600;">Structure</td><td>Microcrystalline</td><td>Mixed amorphous/crystal</td><td style="color:var(--teal);font-weight:600;">Fully amorphous</td></tr>
            <tr><td style="font-weight:600;">Hardness (as-plated)</td><td class="mono">620&ndash;750 HV</td><td class="mono">500&ndash;600 HV</td><td class="mono">450&ndash;550 HV</td></tr>
            <tr><td style="font-weight:600;">Salt Spray (25 &micro;m)</td><td class="mono">200&ndash;500 hr</td><td class="mono">500&ndash;1000 hr</td><td class="mono" style="color:var(--teal);font-weight:600;">&gt;1000 hr</td></tr>
            <tr><td style="font-weight:600;">Magnetic?</td><td>Magnetic</td><td>Weakly magnetic</td><td style="color:var(--teal);font-weight:600;">Non-magnetic</td></tr>
            <tr><td style="font-weight:600;">Solder</td><td>Excellent</td><td>Good</td><td>Poor without activation</td></tr>
            <tr><td style="font-weight:600;">Bath pH</td><td class="mono">4.2&ndash;5.0</td><td class="mono">4.4&ndash;5.0</td><td class="mono">4.2&ndash;4.8</td></tr>
            <tr><td style="font-weight:600;">Bath Temp</td><td class="mono">85&ndash;93&deg;C</td><td class="mono">85&ndash;91&deg;C</td><td class="mono">85&ndash;91&deg;C</td></tr>
            <tr><td style="font-weight:600;">Rate</td><td class="mono">15&ndash;25 &micro;m/hr</td><td class="mono">12&ndash;20 &micro;m/hr</td><td class="mono">8&ndash;15 &micro;m/hr</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- MTO INSIGHT + TROUBLESHOOTING -->
    <div class="bottom-grid">
      <div>
        <h3 class="section-title">Troubleshooting Quick Guide <span class="sub">common failures</span></h3>
        <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
          <table class="data-table compact">
            <thead><tr><th>Symptom</th><th>Likely Root Cause</th><th>Stage</th></tr></thead>
            <tbody>
              <tr><td>Skip plating / bare spots</td><td>Inadequate cleaning or activation</td><td class="mono">1&ndash;3</td></tr>
              <tr><td>Blistering / peeling</td><td>Oxide on surface; over-activation</td><td class="mono">3</td></tr>
              <tr><td>Rough / nodular deposit</td><td>Particles in EN bath; poor filtration</td><td class="mono">5</td></tr>
              <tr><td>Slow plating rate</td><td>Low temp, low Ni, stabilizer excess</td><td class="mono">5</td></tr>
              <tr><td>Pitting</td><td>H&#8322; bubbles sticking; wetting agent low</td><td class="mono">5</td></tr>
              <tr><td>Low phosphorus</td><td>pH too high; Ni too high</td><td class="mono">5</td></tr>
              <tr><td>Plate-out / decomposition</td><td>Temp spike; no stabilizer; contamination</td><td class="mono">5</td></tr>
            </tbody>
          </table>
        </div>
      </div>
      <div>
        <div class="insight-card" style="margin-bottom:8px;">
          <div class="insight-label">Metal Turn-Over (MTO)</div>
          <div class="insight-text">High-phos baths typically run <strong>5&ndash;7 MTO</strong> before performance degrades. Each MTO = the bath has plated out and replenished 100% of its original nickel content. Track MTO by cumulative nickel consumption (kg Ni replenished). Beyond 7 MTO, orthophosphite accumulation slows plating rate and narrows the operating window. Some shops dump-and-rebuild at 5 MTO for consistency.</div>
        </div>
        <div class="insight-card">
          <div class="insight-label">Why Sequence Order Matters</div>
          <div class="insight-text">EN is an autocatalytic reaction &mdash; the deposit catalyzes its own growth. If the surface is not perfectly clean and properly activated, the reaction either does not initiate or initiates unevenly. Every rinse between chemical stages prevents cross-contamination that degrades bath life and deposit quality. Skipping a single rinse can cost an entire bath.</div>
        </div>
      </div>
    </div>

    <div class="safety-card">
      <div class="safety-head">&#9888; Safety &mdash; Full Process Line</div>
      <div class="safety-body"><strong>Alkaline cleaners</strong> (Stages 1&ndash;2): caustic burns, 60&ndash;80&deg;C hot solution. <strong>Acid activation</strong> (Stage 3): HCl fumes, mineral acid burns. <strong>EN bath</strong> (Stage 5): 85&ndash;91&deg;C acidic nickel solution; nickel compounds are GHS Category 1A carcinogen (IARC Group 1 &mdash; known carcinogen by inhalation); skin sensitizer. OSHA PEL: 1 mg/m&sup3; as Ni. <strong>Phosphine risk</strong>: a decomposing bath can release PH&#8323; gas (TLV 0.05 ppm) &mdash; garlic/fish odor = EVACUATE. <strong>Post-treatment</strong> (Stages 7&ndash;8): burn hazard from ovens. Full PPE at every station. Emergency shower and eyewash within 10 seconds.</div>
    </div>
"""

TECH_BODY_ES["01"] = """
    <!-- FLUJO DE PROCESO EXPANDIDO SVG -->
    <div class="glass process-flow" style="height:auto;padding:12px 16px;">
      <svg viewBox="0 0 1100 130" width="100%" height="130" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="60" cy="28" r="18" stroke="var(--amber)" stroke-width="1.6" fill="rgba(232,160,32,.12)"/>
        <text x="60" y="33" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="14">1</text>
        <text x="60" y="55" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" letter-spacing=".04em" opacity=".62">LIMP.</text>
        <text x="60" y="63" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" letter-spacing=".04em" opacity=".62">INMER.</text>
        <line x1="80" y1="28" x2="106" y2="28" stroke="currentColor" stroke-width="1.2" opacity=".35"/><polygon points="106,25 112,28 106,31" fill="currentColor" opacity=".35"/>
        <circle cx="135" cy="28" r="14" stroke="var(--teal)" stroke-width="1.2" fill="rgba(46,196,182,.10)"/>
        <text x="135" y="32" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11">R1</text>
        <text x="135" y="55" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="7" opacity=".5">ENJ.</text>
        <line x1="151" y1="28" x2="177" y2="28" stroke="currentColor" stroke-width="1.2" opacity=".35"/><polygon points="177,25 183,28 177,31" fill="currentColor" opacity=".35"/>
        <circle cx="206" cy="28" r="18" stroke="var(--amber)" stroke-width="1.6" fill="rgba(232,160,32,.12)"/>
        <text x="206" y="33" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="14">2</text>
        <text x="206" y="55" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" letter-spacing=".04em" opacity=".62">ELECTRO</text>
        <text x="206" y="63" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" letter-spacing=".04em" opacity=".62">LIMP.</text>
        <line x1="226" y1="28" x2="252" y2="28" stroke="currentColor" stroke-width="1.2" opacity=".35"/><polygon points="252,25 258,28 252,31" fill="currentColor" opacity=".35"/>
        <circle cx="281" cy="28" r="14" stroke="var(--teal)" stroke-width="1.2" fill="rgba(46,196,182,.10)"/>
        <text x="281" y="32" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11">R2</text>
        <text x="281" y="55" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="7" opacity=".5">ENJ.</text>
        <line x1="297" y1="28" x2="323" y2="28" stroke="currentColor" stroke-width="1.2" opacity=".35"/><polygon points="323,25 329,28 323,31" fill="currentColor" opacity=".35"/>
        <circle cx="352" cy="28" r="18" stroke="var(--coral)" stroke-width="1.6" fill="rgba(224,92,92,.12)"/>
        <text x="352" y="33" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="14">3</text>
        <text x="352" y="55" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" letter-spacing=".04em" opacity=".62">ACTIV.</text>
        <text x="352" y="63" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" letter-spacing=".04em" opacity=".62">&Aacute;CIDA</text>
        <line x1="372" y1="28" x2="398" y2="28" stroke="currentColor" stroke-width="1.2" opacity=".35"/><polygon points="398,25 404,28 398,31" fill="currentColor" opacity=".35"/>
        <circle cx="427" cy="28" r="14" stroke="var(--teal)" stroke-width="1.2" fill="rgba(46,196,182,.10)"/>
        <text x="427" y="32" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11">R3</text>
        <text x="427" y="55" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="7" opacity=".5">ENJ.</text>
        <line x1="443" y1="28" x2="469" y2="28" stroke="currentColor" stroke-width="1.2" opacity=".35"/><polygon points="469,25 475,28 469,31" fill="currentColor" opacity=".35"/>
        <circle cx="498" cy="28" r="14" stroke="var(--teal)" stroke-width="1.2" fill="rgba(46,196,182,.10)"/>
        <text x="498" y="32" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11">R4</text>
        <text x="498" y="55" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="7" opacity=".5">DI</text>
        <line x1="514" y1="28" x2="540" y2="28" stroke="currentColor" stroke-width="1.2" opacity=".35"/><polygon points="540,25 546,28 540,31" fill="currentColor" opacity=".35"/>
        <circle cx="585" cy="28" r="22" stroke="var(--coral)" stroke-width="2.2" fill="rgba(224,92,92,.12)"/>
        <text x="585" y="22" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="10">EN</text>
        <text x="585" y="35" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="14">5</text>
        <text x="585" y="60" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" letter-spacing=".04em" opacity=".62">BA&Ntilde;O EN</text>
        <line x1="609" y1="28" x2="635" y2="28" stroke="currentColor" stroke-width="1.2" opacity=".35"/><polygon points="635,25 641,28 635,31" fill="currentColor" opacity=".35"/>
        <circle cx="664" cy="28" r="14" stroke="var(--teal)" stroke-width="1.2" fill="rgba(46,196,182,.10)"/>
        <text x="664" y="32" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11">R5</text>
        <text x="664" y="55" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="7" opacity=".5">ENJ.</text>
        <line x1="680" y1="28" x2="706" y2="28" stroke="currentColor" stroke-width="1.2" opacity=".35"/><polygon points="706,25 712,28 706,31" fill="currentColor" opacity=".35"/>
        <circle cx="735" cy="28" r="14" stroke="var(--teal)" stroke-width="1.2" fill="rgba(46,196,182,.10)"/>
        <text x="735" y="32" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11">R6</text>
        <text x="735" y="55" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="7" opacity=".5">DI</text>
        <line x1="751" y1="28" x2="777" y2="28" stroke="currentColor" stroke-width="1.2" opacity=".35"/><polygon points="777,25 783,28 777,31" fill="currentColor" opacity=".35"/>
        <circle cx="812" cy="28" r="18" stroke="var(--emerald)" stroke-width="1.6" fill="rgba(39,174,96,.12)"/>
        <text x="812" y="33" text-anchor="middle" fill="var(--emerald)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="14">6</text>
        <text x="812" y="55" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" letter-spacing=".04em" opacity=".62">SECAR</text>
        <line x1="832" y1="28" x2="858" y2="28" stroke="currentColor" stroke-width="1.2" opacity=".35"/><polygon points="858,25 864,28 858,31" fill="currentColor" opacity=".35"/>
        <circle cx="893" cy="28" r="18" stroke="var(--emerald)" stroke-width="1.6" fill="rgba(39,174,96,.12)"/>
        <text x="893" y="33" text-anchor="middle" fill="var(--emerald)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="14">7</text>
        <text x="893" y="55" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" letter-spacing=".04em" opacity=".62">ALIVIO HE</text>
        <line x1="913" y1="28" x2="939" y2="28" stroke="currentColor" stroke-width="1.2" opacity=".35"/><polygon points="939,25 945,28 939,31" fill="currentColor" opacity=".35"/>
        <circle cx="974" cy="28" r="18" stroke="var(--emerald)" stroke-width="1.6" fill="rgba(39,174,96,.12)"/>
        <text x="974" y="33" text-anchor="middle" fill="var(--emerald)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="14">8</text>
        <text x="974" y="55" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" letter-spacing=".04em" opacity=".62">SELLADO /</text>
        <text x="974" y="63" text-anchor="middle" fill="currentColor" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" letter-spacing=".04em" opacity=".62">CROMATO</text>
        <rect x="30" y="82" width="1040" height="40" rx="6" fill="rgba(255,255,255,.03)" stroke="rgba(255,255,255,.06)" stroke-width=".8"/>
        <circle cx="60" cy="102" r="5" fill="rgba(232,160,32,.3)"/>
        <text x="72" y="106" fill="var(--muted)" font-family="Inter,sans-serif" font-size="8" font-weight="500">Etapa Qu&iacute;mica</text>
        <circle cx="190" cy="102" r="5" fill="rgba(46,196,182,.3)"/>
        <text x="202" y="106" fill="var(--muted)" font-family="Inter,sans-serif" font-size="8" font-weight="500">Enjuague</text>
        <circle cx="280" cy="102" r="5" fill="rgba(224,92,92,.3)"/>
        <text x="292" y="106" fill="var(--muted)" font-family="Inter,sans-serif" font-size="8" font-weight="500">Proceso Cr&iacute;tico</text>
        <circle cx="410" cy="102" r="5" fill="rgba(39,174,96,.3)"/>
        <text x="422" y="106" fill="var(--muted)" font-family="Inter,sans-serif" font-size="8" font-weight="500">Post-Tratamiento</text>
        <text x="600" y="106" fill="var(--faint)" font-family="Inter,sans-serif" font-size="8" font-style="italic">Secuencia expandida &mdash; cada enjuague mostrado. N&uacute;mero real de tanques var&iacute;a seg&uacute;n instalaci&oacute;n.</text>
      </svg>
    </div>

    <!-- TABLA DE SECUENCIA DETALLADA -->
    <div>
      <h3 class="section-title">Secuencia de Proceso Expandida <span class="sub">todas las etapas + enjuagues</span></h3>
      <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
        <table class="data-table compact">
          <thead><tr><th style="width:32px;">Paso</th><th>Etapa</th><th>Temp</th><th>Tiempo</th><th>Control Clave</th></tr></thead>
          <tbody>
            <tr><td class="mono">1</td><td>Limpieza Alcalina por Inmersi&oacute;n</td><td class="mono">60&ndash;80&deg;C</td><td class="mono">3&ndash;10 min</td><td>Superficie libre de ruptura de agua</td></tr>
            <tr><td class="mono">R1</td><td>Enjuague por Rebose</td><td class="mono">Ambiente</td><td class="mono">30&ndash;60 s</td><td>Remover alcalino residual; &lt;200 &micro;S/cm</td></tr>
            <tr><td class="mono">2</td><td>Electrolimpieza (cat&oacute;dica o an&oacute;dica)</td><td class="mono">60&ndash;71&deg;C</td><td class="mono">1&ndash;3 min</td><td>3&ndash;6 V; acci&oacute;n de arrastre mec&aacute;nico por gas</td></tr>
            <tr><td class="mono">R2</td><td>Enjuague en Cascada (2 etapas)</td><td class="mono">Ambiente</td><td class="mono">30&ndash;60 s/etapa</td><td>Conductividad &lt;50 &micro;S/cm saliendo</td></tr>
            <tr><td class="mono">3</td><td>Activaci&oacute;n &Aacute;cida</td><td class="mono">Ambiente</td><td class="mono">30&ndash;120 s</td><td>HCl 10&ndash;20% v/v (acero); HNO&#8323; o doble zincado (Al)</td></tr>
            <tr><td class="mono">R3</td><td>Enjuague</td><td class="mono">Ambiente</td><td class="mono">30 s</td><td>Remover arrastre de &aacute;cido</td></tr>
            <tr><td class="mono">R4</td><td>Enjuague DI Cr&iacute;tico (Pre-EN)</td><td class="mono">Ambiente</td><td class="mono">30&ndash;60 s</td><td>Conductividad &lt;20 &micro;S/cm; solo agua DI</td></tr>
            <tr><td class="mono">5</td><td style="font-weight:600;">Ba&ntilde;o EN Alto F&oacute;sforo</td><td class="mono">85&ndash;91&deg;C</td><td class="mono">60&ndash;180 min</td><td>pH 4.2&ndash;4.8; Ni&sup2;&#8314; 4.5&ndash;6.5 g/L</td></tr>
            <tr><td class="mono">R5</td><td>Enjuague de Recuperaci&oacute;n</td><td class="mono">Ambiente</td><td class="mono">15&ndash;30 s</td><td>Transferencia en &lt;10 s; captura Ni para retorno</td></tr>
            <tr><td class="mono">R6</td><td>Enjuague Final DI</td><td class="mono">Fr&iacute;o / tibio</td><td class="mono">30&ndash;60 s</td><td>Superficie sin manchas; &lt;10 &micro;S/cm</td></tr>
            <tr><td class="mono">6</td><td>Secado con Aire Caliente</td><td class="mono">65&ndash;82&deg;C</td><td class="mono">2&ndash;5 min</td><td>Sin manchas de agua; soplado o horno</td></tr>
            <tr><td class="mono">7</td><td>Horneado HE (si se requiere)</td><td class="mono">190&deg;C</td><td class="mono">4+ hr</td><td>Dentro de 4 hr del dep&oacute;sito para acero de alta resistencia</td></tr>
            <tr><td class="mono">8</td><td>Cromato / Sellador (si se requiere)</td><td class="mono">Seg&uacute;n espec.</td><td class="mono">Seg&uacute;n espec.</td><td>Protecci&oacute;n adicional contra corrosi&oacute;n o acabado cosm&eacute;tico</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- COMPARACI&Oacute;N DE FORMULACIONES EN -->
    <div>
      <h3 class="section-title">Comparaci&oacute;n de Formulaciones EN <span class="sub">bajo &bull; medio &bull; alto f&oacute;sforo</span></h3>
      <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
        <table class="data-table compact">
          <thead><tr><th>Propiedad</th><th>Bajo P (2&ndash;4%)</th><th>Medio P (6&ndash;9%)</th><th style="background:rgba(46,196,182,.12);">Alto P (10&ndash;13%)</th></tr></thead>
          <tbody>
            <tr><td style="font-weight:600;">Estructura</td><td>Microcristalino</td><td>Amorfo/cristalino mixto</td><td style="color:var(--teal);font-weight:600;">Completamente amorfo</td></tr>
            <tr><td style="font-weight:600;">Dureza (tal cual)</td><td class="mono">620&ndash;750 HV</td><td class="mono">500&ndash;600 HV</td><td class="mono">450&ndash;550 HV</td></tr>
            <tr><td style="font-weight:600;">Niebla Salina (25 &micro;m)</td><td class="mono">200&ndash;500 hr</td><td class="mono">500&ndash;1000 hr</td><td class="mono" style="color:var(--teal);font-weight:600;">&gt;1000 hr</td></tr>
            <tr><td style="font-weight:600;">&iquest;Magn&eacute;tico?</td><td>Magn&eacute;tico</td><td>D&eacute;bilmente magn&eacute;tico</td><td style="color:var(--teal);font-weight:600;">No magn&eacute;tico</td></tr>
            <tr><td style="font-weight:600;">Soldabilidad</td><td>Excelente</td><td>Buena</td><td>Pobre sin activaci&oacute;n</td></tr>
            <tr><td style="font-weight:600;">pH del Ba&ntilde;o</td><td class="mono">4.2&ndash;5.0</td><td class="mono">4.4&ndash;5.0</td><td class="mono">4.2&ndash;4.8</td></tr>
            <tr><td style="font-weight:600;">Temp del Ba&ntilde;o</td><td class="mono">85&ndash;93&deg;C</td><td class="mono">85&ndash;91&deg;C</td><td class="mono">85&ndash;91&deg;C</td></tr>
            <tr><td style="font-weight:600;">Velocidad</td><td class="mono">15&ndash;25 &micro;m/hr</td><td class="mono">12&ndash;20 &micro;m/hr</td><td class="mono">8&ndash;15 &micro;m/hr</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- MTO + POR QU&Eacute; IMPORTA EL ORDEN -->
    <div class="bottom-grid">
      <div>
        <h3 class="section-title">Gu&iacute;a R&aacute;pida de Soluci&oacute;n de Problemas <span class="sub">fallas comunes</span></h3>
        <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
          <table class="data-table compact">
            <thead><tr><th>S&iacute;ntoma</th><th>Causa Probable</th><th>Etapa</th></tr></thead>
            <tbody>
              <tr><td>Falta de dep&oacute;sito / &aacute;reas desnudas</td><td>Limpieza o activaci&oacute;n inadecuada</td><td class="mono">1&ndash;3</td></tr>
              <tr><td>Ampollas / desprendimiento</td><td>&Oacute;xido en superficie; sobre-activaci&oacute;n</td><td class="mono">3</td></tr>
              <tr><td>Dep&oacute;sito rugoso / nodular</td><td>Part&iacute;culas en ba&ntilde;o EN; filtraci&oacute;n deficiente</td><td class="mono">5</td></tr>
              <tr><td>Velocidad lenta</td><td>Temp baja, Ni bajo, exceso de estabilizador</td><td class="mono">5</td></tr>
              <tr><td>Picaduras</td><td>Burbujas de H&#8322; adheridas; agente humectante bajo</td><td class="mono">5</td></tr>
              <tr><td>F&oacute;sforo bajo</td><td>pH muy alto; Ni muy alto</td><td class="mono">5</td></tr>
              <tr><td>Plate-out / descomposici&oacute;n</td><td>Pico de temp; sin estabilizador; contaminaci&oacute;n</td><td class="mono">5</td></tr>
            </tbody>
          </table>
        </div>
      </div>
      <div>
        <div class="insight-card" style="margin-bottom:8px;">
          <div class="insight-label">Rotaci&oacute;n de Metal (MTO)</div>
          <div class="insight-text">Los ba&ntilde;os de alto f&oacute;sforo t&iacute;picamente funcionan <strong>5&ndash;7 MTO</strong> antes de que el rendimiento se degrade. Cada MTO = el ba&ntilde;o ha depositado y reemplazado 100% de su contenido original de n&iacute;quel. Monitoree MTO por consumo acumulado de n&iacute;quel (kg Ni repuesto). M&aacute;s all&aacute; de 7 MTO, la acumulaci&oacute;n de ortofosfito reduce la velocidad y estrecha la ventana operativa. Algunas instalaciones descartan y reconstruyen a 5 MTO para consistencia.</div>
        </div>
        <div class="insight-card">
          <div class="insight-label">Por Qu&eacute; Importa el Orden de la Secuencia</div>
          <div class="insight-text">EN es una reacci&oacute;n autocatal&iacute;tica &mdash; el dep&oacute;sito cataliza su propio crecimiento. Si la superficie no est&aacute; perfectamente limpia y activada, la reacci&oacute;n no inicia o inicia de forma desigual. Cada enjuague entre etapas qu&iacute;micas previene contaminaci&oacute;n cruzada que degrada la vida del ba&ntilde;o y la calidad del dep&oacute;sito. Omitir un solo enjuague puede costar un ba&ntilde;o entero.</div>
        </div>
      </div>
    </div>

    <div class="safety-card">
      <div class="safety-head">&#9888; Seguridad &mdash; L&iacute;nea de Proceso Completa</div>
      <div class="safety-body"><strong>Limpiadores alcalinos</strong> (Etapas 1&ndash;2): quemaduras c&aacute;usticas, soluci&oacute;n caliente 60&ndash;80&deg;C. <strong>Activaci&oacute;n &aacute;cida</strong> (Etapa 3): vapores de HCl, quemaduras por &aacute;cido mineral. <strong>Ba&ntilde;o EN</strong> (Etapa 5): soluci&oacute;n &aacute;cida de n&iacute;quel a 85&ndash;91&deg;C; compuestos de n&iacute;quel son carcin&oacute;geno GHS Categor&iacute;a 1A (IARC Grupo 1 &mdash; carcin&oacute;geno conocido por inhalaci&oacute;n); sensibilizante cut&aacute;neo. OSHA PEL: 1 mg/m&sup3; como Ni. <strong>Riesgo de fosfina</strong>: un ba&ntilde;o en descomposici&oacute;n puede liberar gas PH&#8323; (TLV 0.05 ppm) &mdash; olor a ajo/pescado = EVACUE. <strong>Post-tratamiento</strong> (Etapas 7&ndash;8): riesgo de quemaduras por hornos. EPP completo en cada estaci&oacute;n. Regadera y lavaojos a 10 segundos.</div>
    </div>
"""

SF_BODY_EN["01"] = """
    <!-- SIMPLIFIED FLOW SVG -->
    <div class="glass" style="padding:8px 10px;">
      <svg viewBox="0 0 820 55" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block;">
        <rect x="0" y="5" width="90" height="30" rx="5" fill="rgba(232,160,32,.10)" stroke="var(--amber)" stroke-width="1.2"/>
        <text x="45" y="18" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" text-anchor="middle">01 CLEAN</text>
        <text x="45" y="29" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="6.5" text-anchor="middle">60&ndash;80&deg;C</text>
        <line x1="90" y1="20" x2="103" y2="20" stroke="var(--faint)" stroke-width="1"/><polygon points="103,17 108,20 103,23" fill="var(--faint)"/>
        <rect x="110" y="5" width="60" height="30" rx="5" fill="rgba(46,196,182,.10)" stroke="var(--teal)" stroke-width="1"/>
        <text x="140" y="23" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="7" text-anchor="middle">RINSE</text>
        <line x1="170" y1="20" x2="183" y2="20" stroke="var(--faint)" stroke-width="1"/><polygon points="183,17 188,20 183,23" fill="var(--faint)"/>
        <rect x="190" y="5" width="90" height="30" rx="5" fill="rgba(224,92,92,.10)" stroke="var(--coral)" stroke-width="1.2"/>
        <text x="235" y="18" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" text-anchor="middle">03 ACTIVATE</text>
        <text x="235" y="29" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="6.5" text-anchor="middle">30&ndash;120 s</text>
        <line x1="280" y1="20" x2="293" y2="20" stroke="var(--faint)" stroke-width="1"/><polygon points="293,17 298,20 293,23" fill="var(--faint)"/>
        <rect x="300" y="5" width="60" height="30" rx="5" fill="rgba(46,196,182,.10)" stroke="var(--teal)" stroke-width="1"/>
        <text x="330" y="18" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="7" text-anchor="middle">RINSE</text>
        <text x="330" y="29" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="6.5" text-anchor="middle">&lt;20 &mu;S</text>
        <line x1="360" y1="20" x2="373" y2="20" stroke="var(--faint)" stroke-width="1"/><polygon points="373,17 378,20 373,23" fill="var(--faint)"/>
        <rect x="380" y="2" width="110" height="36" rx="5" fill="rgba(224,92,92,.10)" stroke="var(--coral)" stroke-width="1.5"/>
        <text x="435" y="17" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="9" text-anchor="middle">05 EN BATH</text>
        <text x="435" y="30" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="6.5" text-anchor="middle">85&ndash;91&deg;C</text>
        <line x1="490" y1="20" x2="503" y2="20" stroke="var(--faint)" stroke-width="1"/><polygon points="503,17 508,20 503,23" fill="var(--faint)"/>
        <rect x="510" y="5" width="60" height="30" rx="5" fill="rgba(46,196,182,.10)" stroke="var(--teal)" stroke-width="1"/>
        <text x="540" y="23" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="7" text-anchor="middle">RINSE</text>
        <line x1="570" y1="20" x2="583" y2="20" stroke="var(--faint)" stroke-width="1"/><polygon points="583,17 588,20 583,23" fill="var(--faint)"/>
        <rect x="590" y="5" width="60" height="30" rx="5" fill="rgba(39,174,96,.10)" stroke="var(--emerald)" stroke-width="1.2"/>
        <text x="620" y="18" fill="var(--emerald)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="7" text-anchor="middle">DRY</text>
        <line x1="650" y1="20" x2="663" y2="20" stroke="var(--faint)" stroke-width="1"/><polygon points="663,17 668,20 663,23" fill="var(--faint)"/>
        <rect x="670" y="5" width="90" height="30" rx="5" fill="rgba(39,174,96,.10)" stroke="var(--emerald)" stroke-width="1.2"/>
        <text x="715" y="18" fill="var(--emerald)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" text-anchor="middle">07 POST-TREAT</text>
        <text x="715" y="29" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="6.5" text-anchor="middle">190&ndash;400&deg;C</text>
        <text x="410" y="51" fill="var(--faint)" font-family="Inter,sans-serif" font-size="6.5" font-style="italic" text-anchor="middle">Follow every stage in order &mdash; no skipping, no shortcuts</text>
      </svg>
    </div>

    <!-- SEQUENCE TABLE -->
    <div class="glass" style="padding:10px 12px;">
      <div class="section-title">Process Sequence</div>
      <table class="flow-table">
        <thead><tr><th>#</th><th>Step</th><th>Temp</th><th>Time</th><th>Watch For</th></tr></thead>
        <tbody>
          <tr><td class="mono">01</td><td>Alkaline Soak Clean</td><td class="mono">140&ndash;176&deg;F</td><td class="mono">3&ndash;10 min</td><td>Water break = re-clean</td></tr>
          <tr><td class="mono">02</td><td>Rinse</td><td class="mono">Ambient</td><td class="mono">30&ndash;60 sec</td><td>Remove alkaline residue</td></tr>
          <tr><td class="mono">03</td><td>Acid Activation</td><td class="mono">Ambient</td><td class="mono">30&ndash;120 sec</td><td>Right acid for substrate</td></tr>
          <tr><td class="mono">04</td><td>Critical Rinse (DI)</td><td class="mono">Ambient</td><td class="mono">30&ndash;60 sec</td><td>&lt;20 &micro;S/cm conductivity</td></tr>
          <tr><td class="mono">05</td><td style="font-weight:600;">EN High Phos Bath</td><td class="mono">185&ndash;196&deg;F</td><td class="mono">60&ndash;180 min</td><td>pH 4.2&ndash;4.8; check temp</td></tr>
          <tr><td class="mono">06</td><td>Final Rinse</td><td class="mono">Cold</td><td class="mono">30&ndash;60 sec</td><td>Transfer fast &mdash; &lt;10 sec</td></tr>
          <tr><td class="mono">07</td><td>Post Treatment</td><td class="mono">375&ndash;750&deg;F</td><td class="mono">1&ndash;4+ hr</td><td>HE bake within 4 hr if needed</td></tr>
        </tbody>
      </table>
    </div>

    <!-- KEY RULES -->
    <div class="glass numbered-list" style="padding:10px 14px;">
      <div class="section-title">Key Rules <span style="font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:.10em;color:var(--muted);margin-left:8px;">FOLLOW EVERY LOAD</span></div>
      <div style="display:flex;flex-direction:column;gap:6px;">
        <div class="list-item"><div class="num">1</div><div class="num-text"><strong>Clean first, clean well.</strong> EN only deposits on perfectly clean surfaces. Water-break test = pass or re-clean.</div></div>
        <div class="list-item"><div class="num">2</div><div class="num-text"><strong>Right acid for the substrate.</strong> Steel gets HCl. Aluminum gets zincate. Copper alloys get mild acid. Wrong acid = failed adhesion.</div></div>
        <div class="list-item"><div class="num">3</div><div class="num-text"><strong>DI rinse before EN.</strong> The last rinse before the EN bath must be DI water &lt;20 &micro;S/cm. Tap water contaminants kill bath life.</div></div>
        <div class="list-item"><div class="num">4</div><div class="num-text"><strong>Never let parts dry between stages.</strong> Dry = oxide = skip plating. Keep parts wet from clean to EN.</div></div>
        <div class="list-item"><div class="num">5</div><div class="num-text"><strong>Transfer fast out of EN.</strong> Pull parts and get to rinse in &lt;10 seconds. Staining and pitting happen on slow transfers.</div></div>
      </div>
    </div>

    <!-- DO / DON'T -->
    <div class="compare-row">
      <div class="compare-card glass do"><div class="compare-head good">&#10003; Do</div><ul class="compare-list"><li>Follow all stages in order, every load</li><li>Water-break test after every clean</li><li>Check conductivity at rinse 04</li><li>Transfer quickly &mdash; never let parts dry</li><li>Report unusual bath color, odor, or temperature</li></ul></div>
      <div class="compare-card glass dont"><div class="compare-head bad">&#10007; Don&rsquo;t</div><ul class="compare-list"><li>Skip cleaning &mdash; EN does not forgive contamination</li><li>Use tap water for the pre-EN rinse</li><li>Touch parts with bare hands after cleaning</li><li>Drag acid into the EN bath</li><li>Try to fix a decomposing bath &mdash; EVACUATE</li></ul></div>
    </div>

    <div class="glass safety-card">
      <div class="section-title coral">&#9888; Safety &mdash; Process Line</div>
      <div class="safety-text"><strong>Hot alkaline cleaners</strong> (Stage 1): chemical burns at 60&ndash;80&deg;C. <strong>Acid</strong> (Stage 3): mineral acid burns, HCl fumes. <strong>EN bath</strong> (Stage 5): 85&ndash;91&deg;C hot acidic nickel; nickel is a GHS Cat. 1A carcinogen (IARC Group 1 &mdash; known) and skin sensitizer. OSHA PEL: 1 mg/m&sup3;. <strong>Phosphine</strong>: decomposing bath can release PH&#8323; (TLV 0.05 ppm). Unusual odor/turbidity = EVACUATE. Emergency shower and eyewash within 10 sec. Full PPE at all stations. No food, drink, or smoking on the line.</div>
    </div>
"""

SF_BODY_ES["01"] = """
    <!-- FLUJO SIMPLIFICADO SVG -->
    <div class="glass" style="padding:8px 10px;">
      <svg viewBox="0 0 820 55" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block;">
        <rect x="0" y="5" width="90" height="30" rx="5" fill="rgba(232,160,32,.10)" stroke="var(--amber)" stroke-width="1.2"/>
        <text x="45" y="18" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" text-anchor="middle">01 LIMPIAR</text>
        <text x="45" y="29" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="6.5" text-anchor="middle">60&ndash;80&deg;C</text>
        <line x1="90" y1="20" x2="103" y2="20" stroke="var(--faint)" stroke-width="1"/><polygon points="103,17 108,20 103,23" fill="var(--faint)"/>
        <rect x="110" y="5" width="60" height="30" rx="5" fill="rgba(46,196,182,.10)" stroke="var(--teal)" stroke-width="1"/>
        <text x="140" y="23" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="7" text-anchor="middle">ENJUAGUE</text>
        <line x1="170" y1="20" x2="183" y2="20" stroke="var(--faint)" stroke-width="1"/><polygon points="183,17 188,20 183,23" fill="var(--faint)"/>
        <rect x="190" y="5" width="90" height="30" rx="5" fill="rgba(224,92,92,.10)" stroke="var(--coral)" stroke-width="1.2"/>
        <text x="235" y="18" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" text-anchor="middle">03 ACTIVAR</text>
        <text x="235" y="29" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="6.5" text-anchor="middle">30&ndash;120 s</text>
        <line x1="280" y1="20" x2="293" y2="20" stroke="var(--faint)" stroke-width="1"/><polygon points="293,17 298,20 293,23" fill="var(--faint)"/>
        <rect x="300" y="5" width="60" height="30" rx="5" fill="rgba(46,196,182,.10)" stroke="var(--teal)" stroke-width="1"/>
        <text x="330" y="18" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="7" text-anchor="middle">ENJUAGUE</text>
        <text x="330" y="29" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="6.5" text-anchor="middle">&lt;20 &mu;S</text>
        <line x1="360" y1="20" x2="373" y2="20" stroke="var(--faint)" stroke-width="1"/><polygon points="373,17 378,20 373,23" fill="var(--faint)"/>
        <rect x="380" y="2" width="110" height="36" rx="5" fill="rgba(224,92,92,.10)" stroke="var(--coral)" stroke-width="1.5"/>
        <text x="435" y="17" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="9" text-anchor="middle">05 BA&Ntilde;O EN</text>
        <text x="435" y="30" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="6.5" text-anchor="middle">85&ndash;91&deg;C</text>
        <line x1="490" y1="20" x2="503" y2="20" stroke="var(--faint)" stroke-width="1"/><polygon points="503,17 508,20 503,23" fill="var(--faint)"/>
        <rect x="510" y="5" width="60" height="30" rx="5" fill="rgba(46,196,182,.10)" stroke="var(--teal)" stroke-width="1"/>
        <text x="540" y="23" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="7" text-anchor="middle">ENJUAGUE</text>
        <line x1="570" y1="20" x2="583" y2="20" stroke="var(--faint)" stroke-width="1"/><polygon points="583,17 588,20 583,23" fill="var(--faint)"/>
        <rect x="590" y="5" width="60" height="30" rx="5" fill="rgba(39,174,96,.10)" stroke="var(--emerald)" stroke-width="1.2"/>
        <text x="620" y="18" fill="var(--emerald)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="7" text-anchor="middle">SECAR</text>
        <line x1="650" y1="20" x2="663" y2="20" stroke="var(--faint)" stroke-width="1"/><polygon points="663,17 668,20 663,23" fill="var(--faint)"/>
        <rect x="670" y="5" width="90" height="30" rx="5" fill="rgba(39,174,96,.10)" stroke="var(--emerald)" stroke-width="1.2"/>
        <text x="715" y="18" fill="var(--emerald)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" text-anchor="middle">07 POST-TRAT</text>
        <text x="715" y="29" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="6.5" text-anchor="middle">190&ndash;400&deg;C</text>
        <text x="410" y="51" fill="var(--faint)" font-family="Inter,sans-serif" font-size="6.5" font-style="italic" text-anchor="middle">Siga todas las etapas en orden &mdash; sin omitir, sin atajos</text>
      </svg>
    </div>

    <!-- TABLA DE SECUENCIA -->
    <div class="glass" style="padding:10px 12px;">
      <div class="section-title">Secuencia de Proceso</div>
      <table class="flow-table">
        <thead><tr><th>#</th><th>Etapa</th><th>Temp</th><th>Tiempo</th><th>Observe</th></tr></thead>
        <tbody>
          <tr><td class="mono">01</td><td>Limpieza Alcalina</td><td class="mono">60&ndash;80&deg;C</td><td class="mono">3&ndash;10 min</td><td>Ruptura de agua = re-limpie</td></tr>
          <tr><td class="mono">02</td><td>Enjuague</td><td class="mono">Ambiente</td><td class="mono">30&ndash;60 s</td><td>Remover residuo alcalino</td></tr>
          <tr><td class="mono">03</td><td>Activaci&oacute;n &Aacute;cida</td><td class="mono">Ambiente</td><td class="mono">30&ndash;120 s</td><td>&Aacute;cido correcto por sustrato</td></tr>
          <tr><td class="mono">04</td><td>Enjuague Cr&iacute;tico (DI)</td><td class="mono">Ambiente</td><td class="mono">30&ndash;60 s</td><td>Conductividad &lt;20 &micro;S/cm</td></tr>
          <tr><td class="mono">05</td><td style="font-weight:600;">Ba&ntilde;o EN Alto P</td><td class="mono">85&ndash;91&deg;C</td><td class="mono">60&ndash;180 min</td><td>pH 4.2&ndash;4.8; revise temp</td></tr>
          <tr><td class="mono">06</td><td>Enjuague Final</td><td class="mono">Fr&iacute;o</td><td class="mono">30&ndash;60 s</td><td>Transfiera r&aacute;pido &mdash; &lt;10 s</td></tr>
          <tr><td class="mono">07</td><td>Post Tratamiento</td><td class="mono">190&ndash;400&deg;C</td><td class="mono">1&ndash;4+ hr</td><td>Alivio HE dentro de 4 hr si aplica</td></tr>
        </tbody>
      </table>
    </div>

    <!-- REGLAS CLAVE -->
    <div class="glass numbered-list" style="padding:10px 14px;">
      <div class="section-title">Reglas Clave <span style="font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:.10em;color:var(--muted);margin-left:8px;">SIGA CADA CARGA</span></div>
      <div style="display:flex;flex-direction:column;gap:6px;">
        <div class="list-item"><div class="num">1</div><div class="num-text"><strong>Limpie primero, limpie bien.</strong> EN solo deposita sobre superficies perfectamente limpias. Prueba de ruptura de agua = pasa o re-limpie.</div></div>
        <div class="list-item"><div class="num">2</div><div class="num-text"><strong>&Aacute;cido correcto para el sustrato.</strong> Acero usa HCl. Aluminio usa zincado. Aleaciones de cobre usan &aacute;cido suave. &Aacute;cido equivocado = falla de adherencia.</div></div>
        <div class="list-item"><div class="num">3</div><div class="num-text"><strong>Enjuague DI antes de EN.</strong> El &uacute;ltimo enjuague antes del ba&ntilde;o EN debe ser agua DI &lt;20 &micro;S/cm. Contaminantes del agua de grifo matan la vida del ba&ntilde;o.</div></div>
        <div class="list-item"><div class="num">4</div><div class="num-text"><strong>Nunca deje secar las piezas entre etapas.</strong> Seco = &oacute;xido = falta de dep&oacute;sito. Mantenga piezas h&uacute;medas desde limpieza hasta EN.</div></div>
        <div class="list-item"><div class="num">5</div><div class="num-text"><strong>Transfiera r&aacute;pido desde el EN.</strong> Saque piezas y ll&eacute;velas al enjuague en &lt;10 segundos. Manchas y picaduras ocurren en transferencias lentas.</div></div>
      </div>
    </div>

    <!-- HAGA / NO HAGA -->
    <div class="compare-row">
      <div class="compare-card glass do"><div class="compare-head good">&#10003; Haga</div><ul class="compare-list"><li>Siga todas las etapas en orden, cada carga</li><li>Prueba de ruptura de agua despu&eacute;s de cada limpieza</li><li>Revise conductividad en enjuague 04</li><li>Transfiera r&aacute;pidamente &mdash; nunca deje secar</li><li>Reporte color, olor o temperatura inusual del ba&ntilde;o</li></ul></div>
      <div class="compare-card glass dont"><div class="compare-head bad">&#10007; No Haga</div><ul class="compare-list"><li>Omitir limpieza &mdash; EN no perdona contaminaci&oacute;n</li><li>Usar agua de grifo para el enjuague pre-EN</li><li>Tocar piezas con manos desnudas despu&eacute;s de limpiar</li><li>Arrastrar &aacute;cido al ba&ntilde;o EN</li><li>Intentar arreglar un ba&ntilde;o en descomposici&oacute;n &mdash; EVACUE</li></ul></div>
    </div>

    <div class="glass safety-card">
      <div class="section-title coral">&#9888; Seguridad &mdash; L&iacute;nea de Proceso</div>
      <div class="safety-text"><strong>Limpiadores alcalinos calientes</strong> (Etapa 1): quemaduras qu&iacute;micas a 60&ndash;80&deg;C. <strong>&Aacute;cido</strong> (Etapa 3): quemaduras por &aacute;cido mineral, vapores de HCl. <strong>Ba&ntilde;o EN</strong> (Etapa 5): soluci&oacute;n &aacute;cida de n&iacute;quel a 85&ndash;91&deg;C; n&iacute;quel es carcin&oacute;geno GHS Cat. 1A (IARC Grupo 1 &mdash; conocido) y sensibilizante cut&aacute;neo. OSHA PEL: 1 mg/m&sup3;. <strong>Fosfina</strong>: ba&ntilde;o en descomposici&oacute;n puede liberar PH&#8323; (TLV 0.05 ppm). Olor/turbidez inusual = EVACUE. Regadera y lavaojos a 10 s. EPP completo en todas las estaciones. No comer, beber ni fumar en la l&iacute;nea.</div>
    </div>
"""

# =====================================================================
# POSTER 02 — CLEANING
# =====================================================================
TECH_BODY_EN["02"] = """
    <div class="glass rule-card">
      <div class="rule-num">01</div>
      <div class="rule-body">
        <div class="rule-label">Stage 1 &mdash; Alkaline Soak Clean</div>
        <div class="rule-text">Electroless nickel is an autocatalytic process &mdash; it only deposits on a catalytically active surface. Any residual oil, oxide, or organic contamination will cause skip plating, blistering, or complete adhesion failure. Cleaning is the single most important stage in the EN line. If the water-break test fails, nothing downstream can fix it.</div>
      </div>
    </div>

    <!-- CLEANING MECHANISMS TABLE -->
    <div>
      <h3 class="section-title">Cleaning Mechanisms <span class="sub">how alkaline cleaners work</span></h3>
      <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
        <table class="data-table compact">
          <thead><tr><th>Mechanism</th><th>Action</th><th>Target Soil</th></tr></thead>
          <tbody>
            <tr><td style="font-weight:600;color:var(--amber);">Saponification</td><td>NaOH/KOH reacts with animal/vegetable fats to form water-soluble soaps</td><td>Natural oils, fingerprints, lard-based lubricants</td></tr>
            <tr><td style="font-weight:600;color:var(--amber);">Emulsification</td><td>Surfactants break petroleum oils into fine droplets suspended in solution</td><td>Mineral oils, cutting fluids, rust preventatives</td></tr>
            <tr><td style="font-weight:600;color:var(--amber);">Deflocculation</td><td>Alkaline dispersants lift solid particles from surface and prevent re-deposition</td><td>Metal fines, carbon residues, polishing compounds</td></tr>
            <tr><td style="font-weight:600;color:var(--amber);">Chelation / Sequestration</td><td>Complexing agents bind Ca&sup2;&#8314;, Mg&sup2;&#8314; ions; prevent hard-water deposits</td><td>Scale, mineral films from hard water</td></tr>
            <tr><td style="font-weight:600;color:var(--amber);">Wetting</td><td>Reduces surface tension so cleaner penetrates recesses and blind holes</td><td>Complex geometries, threaded parts</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- CLEANER CHEMISTRY TABLE -->
    <div class="bottom-grid">
      <div>
        <h3 class="section-title">Typical Alkaline Soak Cleaner <span class="sub">components</span></h3>
        <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
          <table class="data-table bath">
            <thead><tr><th>Component</th><th>Concentration</th><th>Function</th></tr></thead>
            <tbody>
              <tr><td>NaOH / KOH</td><td class="mono">30&ndash;60 g/L</td><td>Primary alkalinity; saponification</td></tr>
              <tr><td>Na&#8322;CO&#8323; (soda ash)</td><td class="mono">15&ndash;30 g/L</td><td>Buffer; mild alkalinity</td></tr>
              <tr><td>Na&#8323;PO&#8324; (TSP)</td><td class="mono">15&ndash;30 g/L</td><td>Emulsification; water softening</td></tr>
              <tr><td>Na&#8322;SiO&#8323; (metasilicate)</td><td class="mono">10&ndash;25 g/L</td><td>Deflocculation; wetting</td></tr>
              <tr><td>Surfactants (nonionics)</td><td class="mono">0.5&ndash;2 g/L</td><td>Emulsification; wetting</td></tr>
              <tr><td>Chelating agents (EDTA/gluconate)</td><td class="mono">2&ndash;8 g/L</td><td>Hard-water sequestration</td></tr>
            </tbody>
          </table>
        </div>
      </div>
      <div>
        <h3 class="section-title">Operating Parameters <span class="sub">Stage 1</span></h3>
        <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
          <table class="data-table bath">
            <thead><tr><th>Parameter</th><th>Range</th></tr></thead>
            <tbody>
              <tr><td>Temperature</td><td class="mono">140&ndash;176&deg;F (60&ndash;80&deg;C)</td></tr>
              <tr><td>Immersion Time</td><td class="mono">3&ndash;10 min</td></tr>
              <tr><td>Concentration</td><td class="mono">4&ndash;8 oz/gal (30&ndash;60 g/L)</td></tr>
              <tr><td>Agitation</td><td>Moderate air or mechanical</td></tr>
              <tr><td>pH</td><td class="mono">12&ndash;14</td></tr>
              <tr><td>Bath Life</td><td>Replace when oil loading exceeds capacity</td></tr>
            </tbody>
          </table>
        </div>
        <h3 class="section-title" style="margin-top:8px;">Contamination Thresholds <span class="sub">dump criteria</span></h3>
        <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
          <table class="data-table bath">
            <thead><tr><th>Contaminant</th><th>Max</th></tr></thead>
            <tbody>
              <tr><td>Total oil load</td><td class="mono">&gt;5 g/L &rarr; dump</td></tr>
              <tr><td>Dissolved metals (Fe, Zn)</td><td class="mono">&gt;2 g/L &rarr; performance loss</td></tr>
              <tr><td>Foam height</td><td>Persistent foam = surfactant imbalance</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- WATER BREAK TEST SVG -->
    <div class="glass" style="padding:10px 14px;">
      <h3 class="section-title" style="margin-bottom:4px;">Water Break Test <span class="sub">pass / fail visual</span></h3>
      <svg viewBox="0 0 1100 80" width="100%" height="80" fill="none" xmlns="http://www.w3.org/2000/svg">
        <!-- PASS side -->
        <rect x="30" y="5" width="490" height="70" rx="8" fill="rgba(39,174,96,.05)" stroke="var(--emerald)" stroke-width="1"/>
        <text x="275" y="18" text-anchor="middle" fill="var(--emerald)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="12" letter-spacing=".06em">&#10003; PASS &mdash; UNIFORM WATER SHEET</text>
        <rect x="80" y="28" width="390" height="12" rx="3" fill="rgba(39,174,96,.15)"/>
        <text x="275" y="37" text-anchor="middle" fill="var(--emerald)" font-family="Inter,sans-serif" font-size="7" font-weight="600">Continuous unbroken film &mdash; no beading, no dry spots</text>
        <line x1="80" y1="44" x2="470" y2="44" stroke="var(--muted)" stroke-width="1.5"/>
        <text x="275" y="57" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="7">SUBSTRATE SURFACE</text>
        <text x="275" y="68" text-anchor="middle" fill="var(--emerald)" font-family="Inter,sans-serif" font-size="8" font-weight="600">Water remains as continuous sheet for &ge;30 seconds &rarr; PROCEED</text>
        <!-- FAIL side -->
        <rect x="560" y="5" width="490" height="70" rx="8" fill="rgba(224,92,92,.05)" stroke="var(--coral)" stroke-width="1"/>
        <text x="805" y="18" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="12" letter-spacing=".06em">&#10007; FAIL &mdash; WATER BEADS / BREAKS</text>
        <!-- Water droplets -->
        <ellipse cx="630" cy="34" rx="12" ry="8" fill="rgba(224,92,92,.2)"/>
        <ellipse cx="700" cy="34" rx="15" ry="8" fill="rgba(224,92,92,.2)"/>
        <ellipse cx="780" cy="34" rx="10" ry="8" fill="rgba(224,92,92,.2)"/>
        <ellipse cx="850" cy="34" rx="18" ry="8" fill="rgba(224,92,92,.2)"/>
        <ellipse cx="940" cy="34" rx="14" ry="8" fill="rgba(224,92,92,.2)"/>
        <!-- Dry gaps -->
        <text x="665" y="37" text-anchor="middle" fill="var(--coral)" font-family="Inter,sans-serif" font-size="6" font-weight="600">DRY</text>
        <text x="815" y="37" text-anchor="middle" fill="var(--coral)" font-family="Inter,sans-serif" font-size="6" font-weight="600">DRY</text>
        <text x="895" y="37" text-anchor="middle" fill="var(--coral)" font-family="Inter,sans-serif" font-size="6" font-weight="600">DRY</text>
        <line x1="610" y1="44" x2="1000" y2="44" stroke="var(--muted)" stroke-width="1.5"/>
        <text x="805" y="57" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="7">SUBSTRATE SURFACE</text>
        <text x="805" y="68" text-anchor="middle" fill="var(--coral)" font-family="Inter,sans-serif" font-size="8" font-weight="600">Water beads or retracts in &lt;30 seconds &rarr; RE-CLEAN</text>
      </svg>
    </div>

    <div class="insight-card">
      <div class="insight-label">Electroclean: When Soak Alone Is Not Enough</div>
      <div class="insight-text">For heavily soiled parts or critical applications, add an electrocleaning step after soak cleaning. Apply 3&ndash;6 V for 1&ndash;3 minutes &mdash; the vigorous hydrogen (cathodic) or oxygen (anodic) evolution physically scrubs the surface. Anodic electroclean is preferred for EN prep because cathodic cleaning can embed hydrogen in high-strength steels (hydrogen embrittlement risk). Follow electroclean with a cascade rinse before acid activation.</div>
    </div>

    <div class="safety-card">
      <div class="safety-head">&#9888; Safety &mdash; Cleaning Stage</div>
      <div class="safety-body"><strong>Hot alkaline solution</strong> at 60&ndash;80&deg;C causes severe chemical burns on contact. NaOH/KOH solutions are corrosive to skin, eyes, and mucous membranes. <strong>Splash hazard</strong> increases with agitation and part immersion. Wear face shield, chemical splash goggles, neoprene or nitrile gloves, and chemical apron. Emergency shower and eyewash within 10 seconds. If contact occurs, flush with water for &ge;15 minutes. Electroclean generates hydrogen gas &mdash; ensure adequate ventilation to prevent accumulation.</div>
    </div>
"""

TECH_BODY_ES["02"] = """
    <div class="glass rule-card">
      <div class="rule-num">01</div>
      <div class="rule-body">
        <div class="rule-label">Etapa 1 &mdash; Limpieza Alcalina por Inmersi&oacute;n</div>
        <div class="rule-text">El n&iacute;quel qu&iacute;mico es un proceso autocatal&iacute;tico &mdash; solo deposita sobre una superficie catal&iacute;ticamente activa. Cualquier aceite residual, &oacute;xido o contaminaci&oacute;n org&aacute;nica causar&aacute; falta de dep&oacute;sito, ampollas o falla completa de adherencia. La limpieza es la etapa m&aacute;s importante en la l&iacute;nea EN. Si la prueba de ruptura de agua falla, nada posterior puede corregirlo.</div>
      </div>
    </div>

    <!-- MECANISMOS DE LIMPIEZA -->
    <div>
      <h3 class="section-title">Mecanismos de Limpieza <span class="sub">c&oacute;mo funcionan los limpiadores alcalinos</span></h3>
      <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
        <table class="data-table compact">
          <thead><tr><th>Mecanismo</th><th>Acci&oacute;n</th><th>Suciedad Objetivo</th></tr></thead>
          <tbody>
            <tr><td style="font-weight:600;color:var(--amber);">Saponificaci&oacute;n</td><td>NaOH/KOH reacciona con grasas animales/vegetales para formar jabones solubles</td><td>Aceites naturales, huellas dactilares, lubricantes base grasa</td></tr>
            <tr><td style="font-weight:600;color:var(--amber);">Emulsificaci&oacute;n</td><td>Surfactantes rompen aceites de petr&oacute;leo en gotas finas suspendidas en soluci&oacute;n</td><td>Aceites minerales, fluidos de corte, antioxidantes</td></tr>
            <tr><td style="font-weight:600;color:var(--amber);">Defloculaci&oacute;n</td><td>Dispersantes alcalinos levantan part&iacute;culas s&oacute;lidas y previenen re-deposici&oacute;n</td><td>Finos met&aacute;licos, residuos de carb&oacute;n, compuestos de pulido</td></tr>
            <tr><td style="font-weight:600;color:var(--amber);">Quelaci&oacute;n / Secuestro</td><td>Agentes complejantes enlazan iones Ca&sup2;&#8314;, Mg&sup2;&#8314;; previenen dep&oacute;sitos de agua dura</td><td>Sarro, pel&iacute;culas minerales de agua dura</td></tr>
            <tr><td style="font-weight:600;color:var(--amber);">Humectaci&oacute;n</td><td>Reduce tensi&oacute;n superficial para que el limpiador penetre cavidades y agujeros ciegos</td><td>Geometr&iacute;as complejas, piezas roscadas</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- QU&Iacute;MICA DEL LIMPIADOR -->
    <div class="bottom-grid">
      <div>
        <h3 class="section-title">Limpiador Alcalino T&iacute;pico <span class="sub">componentes</span></h3>
        <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
          <table class="data-table bath">
            <thead><tr><th>Componente</th><th>Concentraci&oacute;n</th><th>Funci&oacute;n</th></tr></thead>
            <tbody>
              <tr><td>NaOH / KOH</td><td class="mono">30&ndash;60 g/L</td><td>Alcalinidad primaria; saponificaci&oacute;n</td></tr>
              <tr><td>Na&#8322;CO&#8323; (ceniza de soda)</td><td class="mono">15&ndash;30 g/L</td><td>Regulador de pH; alcalinidad suave</td></tr>
              <tr><td>Na&#8323;PO&#8324; (TSP)</td><td class="mono">15&ndash;30 g/L</td><td>Emulsificaci&oacute;n; ablandamiento de agua</td></tr>
              <tr><td>Na&#8322;SiO&#8323; (metasilicato)</td><td class="mono">10&ndash;25 g/L</td><td>Defloculaci&oacute;n; humectaci&oacute;n</td></tr>
              <tr><td>Surfactantes (no i&oacute;nicos)</td><td class="mono">0.5&ndash;2 g/L</td><td>Emulsificaci&oacute;n; humectaci&oacute;n</td></tr>
              <tr><td>Quelantes (EDTA/gluconato)</td><td class="mono">2&ndash;8 g/L</td><td>Secuestro de agua dura</td></tr>
            </tbody>
          </table>
        </div>
      </div>
      <div>
        <h3 class="section-title">Par&aacute;metros de Operaci&oacute;n <span class="sub">Etapa 1</span></h3>
        <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
          <table class="data-table bath">
            <thead><tr><th>Par&aacute;metro</th><th>Rango</th></tr></thead>
            <tbody>
              <tr><td>Temperatura</td><td class="mono">60&ndash;80&deg;C</td></tr>
              <tr><td>Tiempo de Inmersi&oacute;n</td><td class="mono">3&ndash;10 min</td></tr>
              <tr><td>Concentraci&oacute;n</td><td class="mono">30&ndash;60 g/L</td></tr>
              <tr><td>Agitaci&oacute;n</td><td>Moderada con aire o mec&aacute;nica</td></tr>
              <tr><td>pH</td><td class="mono">12&ndash;14</td></tr>
              <tr><td>Vida del Ba&ntilde;o</td><td>Reemplace cuando la carga de aceite exceda capacidad</td></tr>
            </tbody>
          </table>
        </div>
        <h3 class="section-title" style="margin-top:8px;">Umbrales de Contaminaci&oacute;n <span class="sub">criterios de descarte</span></h3>
        <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
          <table class="data-table bath">
            <thead><tr><th>Contaminante</th><th>M&aacute;ximo</th></tr></thead>
            <tbody>
              <tr><td>Carga total de aceite</td><td class="mono">&gt;5 g/L &rarr; descarte</td></tr>
              <tr><td>Metales disueltos (Fe, Zn)</td><td class="mono">&gt;2 g/L &rarr; p&eacute;rdida de rendimiento</td></tr>
              <tr><td>Altura de espuma</td><td>Espuma persistente = desequilibrio de surfactante</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- PRUEBA DE RUPTURA DE AGUA SVG -->
    <div class="glass" style="padding:10px 14px;">
      <h3 class="section-title" style="margin-bottom:4px;">Prueba de Ruptura de Agua <span class="sub">pasa / falla visual</span></h3>
      <svg viewBox="0 0 1100 80" width="100%" height="80" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect x="30" y="5" width="490" height="70" rx="8" fill="rgba(39,174,96,.05)" stroke="var(--emerald)" stroke-width="1"/>
        <text x="275" y="18" text-anchor="middle" fill="var(--emerald)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="12" letter-spacing=".06em">&#10003; PASA &mdash; L&Aacute;MINA DE AGUA UNIFORME</text>
        <rect x="80" y="28" width="390" height="12" rx="3" fill="rgba(39,174,96,.15)"/>
        <text x="275" y="37" text-anchor="middle" fill="var(--emerald)" font-family="Inter,sans-serif" font-size="7" font-weight="600">Pel&iacute;cula continua sin rupturas &mdash; sin gotas, sin &aacute;reas secas</text>
        <line x1="80" y1="44" x2="470" y2="44" stroke="var(--muted)" stroke-width="1.5"/>
        <text x="275" y="57" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="7">SUPERFICIE DEL SUSTRATO</text>
        <text x="275" y="68" text-anchor="middle" fill="var(--emerald)" font-family="Inter,sans-serif" font-size="8" font-weight="600">Agua permanece como l&aacute;mina continua por &ge;30 s &rarr; PROCEDA</text>
        <rect x="560" y="5" width="490" height="70" rx="8" fill="rgba(224,92,92,.05)" stroke="var(--coral)" stroke-width="1"/>
        <text x="805" y="18" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="12" letter-spacing=".06em">&#10007; FALLA &mdash; AGUA SE ROMPE / GOTEA</text>
        <ellipse cx="630" cy="34" rx="12" ry="8" fill="rgba(224,92,92,.2)"/>
        <ellipse cx="700" cy="34" rx="15" ry="8" fill="rgba(224,92,92,.2)"/>
        <ellipse cx="780" cy="34" rx="10" ry="8" fill="rgba(224,92,92,.2)"/>
        <ellipse cx="850" cy="34" rx="18" ry="8" fill="rgba(224,92,92,.2)"/>
        <ellipse cx="940" cy="34" rx="14" ry="8" fill="rgba(224,92,92,.2)"/>
        <text x="665" y="37" text-anchor="middle" fill="var(--coral)" font-family="Inter,sans-serif" font-size="6" font-weight="600">SECO</text>
        <text x="815" y="37" text-anchor="middle" fill="var(--coral)" font-family="Inter,sans-serif" font-size="6" font-weight="600">SECO</text>
        <text x="895" y="37" text-anchor="middle" fill="var(--coral)" font-family="Inter,sans-serif" font-size="6" font-weight="600">SECO</text>
        <line x1="610" y1="44" x2="1000" y2="44" stroke="var(--muted)" stroke-width="1.5"/>
        <text x="805" y="57" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="7">SUPERFICIE DEL SUSTRATO</text>
        <text x="805" y="68" text-anchor="middle" fill="var(--coral)" font-family="Inter,sans-serif" font-size="8" font-weight="600">Agua se rompe o retrae en &lt;30 s &rarr; RE-LIMPIE</text>
      </svg>
    </div>

    <div class="insight-card">
      <div class="insight-label">Electrolimpieza: Cuando la Inmersi&oacute;n No Es Suficiente</div>
      <div class="insight-text">Para piezas muy sucias o aplicaciones cr&iacute;ticas, agregue un paso de electrolimpieza despu&eacute;s de la inmersi&oacute;n. Aplique 3&ndash;6 V por 1&ndash;3 minutos &mdash; la vigorosa evoluci&oacute;n de hidr&oacute;geno (cat&oacute;dica) u ox&iacute;geno (an&oacute;dica) frota f&iacute;sicamente la superficie. La electrolimpieza an&oacute;dica se prefiere para preparaci&oacute;n EN porque la limpieza cat&oacute;dica puede embeber hidr&oacute;geno en aceros de alta resistencia (riesgo de fragilizaci&oacute;n por hidr&oacute;geno). Siga la electrolimpieza con enjuague en cascada antes de la activaci&oacute;n &aacute;cida.</div>
    </div>

    <div class="safety-card">
      <div class="safety-head">&#9888; Seguridad &mdash; Etapa de Limpieza</div>
      <div class="safety-body"><strong>Soluci&oacute;n alcalina caliente</strong> a 60&ndash;80&deg;C causa quemaduras qu&iacute;micas severas al contacto. Soluciones de NaOH/KOH son corrosivas para piel, ojos y mucosas. <strong>Riesgo de salpicaduras</strong> aumenta con agitaci&oacute;n e inmersi&oacute;n de piezas. Use careta, lentes de seguridad contra salpicaduras qu&iacute;micas, guantes de neopreno o nitrilo, y mandil qu&iacute;mico. Regadera y lavaojos a 10 segundos. Si hay contacto, lave con agua por &ge;15 minutos. La electrolimpieza genera gas hidr&oacute;geno &mdash; asegure ventilaci&oacute;n adecuada para prevenir acumulaci&oacute;n.</div>
    </div>
"""

SF_BODY_EN["02"] = """
    <div class="glass key-card">
      <div class="key-num">01</div>
      <div class="key-label">Stage 1 &mdash; Alkaline Soak Clean</div>
      <div class="key-text">EN only deposits on a perfectly clean surface. Cleaning is the most important stage in the entire process. If the water-break test fails, stop and re-clean. Do not proceed to activation with a dirty part.</div>
    </div>

    <!-- PARAMETERS TABLE -->
    <div class="glass" style="padding:10px 12px;">
      <div class="section-title">Cleaner Parameters</div>
      <table class="data-table compact">
        <thead><tr><th>Parameter</th><th>Target</th><th>Note</th></tr></thead>
        <tbody>
          <tr><td>Temperature</td><td class="mono">140&ndash;176&deg;F (60&ndash;80&deg;C)</td><td>Hotter = better cleaning</td></tr>
          <tr><td>Time</td><td class="mono">3&ndash;10 min</td><td>Longer for heavy soils</td></tr>
          <tr><td>Concentration</td><td class="mono">4&ndash;8 oz/gal</td><td>Per supplier recommendation</td></tr>
          <tr><td>Agitation</td><td>Moderate air or mechanical</td><td>Helps remove soils</td></tr>
          <tr><td>Water Break Test</td><td>30 sec unbroken sheet</td><td>Test every rack!</td></tr>
        </tbody>
      </table>
    </div>

    <!-- WATER BREAK VISUAL -->
    <div class="glass" style="padding:10px 12px;">
      <div class="section-title">Water Break Test</div>
      <svg viewBox="0 0 820 60" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block;">
        <rect x="10" y="5" width="370" height="50" rx="6" fill="rgba(39,174,96,.05)" stroke="var(--emerald)" stroke-width="1"/>
        <text x="195" y="17" text-anchor="middle" fill="var(--emerald)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11" letter-spacing=".04em">&#10003; PASS &mdash; UNIFORM SHEET</text>
        <rect x="40" y="24" width="310" height="8" rx="2" fill="rgba(39,174,96,.15)"/>
        <line x1="40" y1="36" x2="350" y2="36" stroke="var(--muted)" stroke-width="1"/>
        <text x="195" y="48" text-anchor="middle" fill="var(--emerald)" font-family="Inter,sans-serif" font-size="7.5" font-weight="600">Continuous water film &ge;30 sec &rarr; proceed</text>
        <rect x="430" y="5" width="370" height="50" rx="6" fill="rgba(224,92,92,.05)" stroke="var(--coral)" stroke-width="1"/>
        <text x="615" y="17" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11" letter-spacing=".04em">&#10007; FAIL &mdash; BEADING / BREAKS</text>
        <ellipse cx="480" cy="28" rx="10" ry="6" fill="rgba(224,92,92,.2)"/>
        <ellipse cx="540" cy="28" rx="14" ry="6" fill="rgba(224,92,92,.2)"/>
        <ellipse cx="620" cy="28" rx="8" ry="6" fill="rgba(224,92,92,.2)"/>
        <ellipse cx="690" cy="28" rx="16" ry="6" fill="rgba(224,92,92,.2)"/>
        <ellipse cx="760" cy="28" rx="12" ry="6" fill="rgba(224,92,92,.2)"/>
        <line x1="460" y1="36" x2="780" y2="36" stroke="var(--muted)" stroke-width="1"/>
        <text x="615" y="48" text-anchor="middle" fill="var(--coral)" font-family="Inter,sans-serif" font-size="7.5" font-weight="600">Water beads or breaks &rarr; RE-CLEAN</text>
      </svg>
    </div>

    <!-- KEY RULES -->
    <div class="glass numbered-list" style="padding:10px 14px;">
      <div class="section-title">Key Rules</div>
      <div style="display:flex;flex-direction:column;gap:6px;">
        <div class="list-item"><div class="num">1</div><div class="num-text"><strong>Water-break test every rack.</strong> Pull the part from rinse, hold vertical &mdash; water must sheet uniformly for 30 sec with no beading.</div></div>
        <div class="list-item"><div class="num">2</div><div class="num-text"><strong>Maintain temp.</strong> Cold cleaner does not clean. Keep 140&ndash;176&deg;F.</div></div>
        <div class="list-item"><div class="num">3</div><div class="num-text"><strong>Replenish regularly.</strong> A dirty cleaner redeposits soil on parts. Top up per supplier schedule.</div></div>
        <div class="list-item"><div class="num">4</div><div class="num-text"><strong>Do not over-soak cast iron or aluminum.</strong> Extended alkaline exposure etches Al and can dissolve castings.</div></div>
      </div>
    </div>

    <!-- DO / DON'T -->
    <div class="compare-row">
      <div class="compare-card glass do"><div class="compare-head good">&#10003; Do</div><ul class="compare-list"><li>Water-break test on every rack</li><li>Keep cleaner at operating temperature</li><li>Agitate parts during immersion</li><li>Replenish cleaner per schedule</li><li>Re-clean any part that fails water break</li></ul></div>
      <div class="compare-card glass dont"><div class="compare-head bad">&#10007; Don&rsquo;t</div><ul class="compare-list"><li>Skip water-break test to save time</li><li>Run cleaner below temperature</li><li>Leave parts soaking overnight (attack risk)</li><li>Drag dirty cleaner into the rinse</li><li>Touch clean parts with bare hands</li></ul></div>
    </div>

    <div class="glass safety-card">
      <div class="section-title coral">&#9888; Safety &mdash; Cleaning</div>
      <div class="safety-text"><strong>Hot alkaline solution</strong> at 140&ndash;176&deg;F causes severe chemical burns. Corrosive to eyes and skin. Always wear face shield, chemical splash goggles, nitrile gloves, and chemical apron. Never add water to concentrated cleaner &mdash; always add cleaner to water. Emergency shower and eyewash within 10 seconds. Flush any contact with water for 15+ minutes. If electroclean is used: hydrogen gas is generated &mdash; no sparks, no open flame.</div>
    </div>
"""

SF_BODY_ES["02"] = """
    <div class="glass key-card">
      <div class="key-num">01</div>
      <div class="key-label">Etapa 1 &mdash; Limpieza Alcalina por Inmersi&oacute;n</div>
      <div class="key-text">EN solo deposita sobre una superficie perfectamente limpia. La limpieza es la etapa m&aacute;s importante de todo el proceso. Si la prueba de ruptura de agua falla, detenga y re-limpie. No proceda a la activaci&oacute;n con una pieza sucia.</div>
    </div>

    <!-- TABLA DE PAR&Aacute;METROS -->
    <div class="glass" style="padding:10px 12px;">
      <div class="section-title">Par&aacute;metros del Limpiador</div>
      <table class="data-table compact">
        <thead><tr><th>Par&aacute;metro</th><th>Objetivo</th><th>Nota</th></tr></thead>
        <tbody>
          <tr><td>Temperatura</td><td class="mono">60&ndash;80&deg;C</td><td>M&aacute;s caliente = mejor limpieza</td></tr>
          <tr><td>Tiempo</td><td class="mono">3&ndash;10 min</td><td>M&aacute;s largo para suciedad pesada</td></tr>
          <tr><td>Concentraci&oacute;n</td><td class="mono">30&ndash;60 g/L</td><td>Seg&uacute;n recomendaci&oacute;n del proveedor</td></tr>
          <tr><td>Agitaci&oacute;n</td><td>Moderada con aire o mec&aacute;nica</td><td>Ayuda a remover suciedad</td></tr>
          <tr><td>Prueba Ruptura de Agua</td><td>30 s l&aacute;mina continua</td><td>&iexcl;Pruebe cada rack!</td></tr>
        </tbody>
      </table>
    </div>

    <!-- VISUAL DE RUPTURA DE AGUA -->
    <div class="glass" style="padding:10px 12px;">
      <div class="section-title">Prueba de Ruptura de Agua</div>
      <svg viewBox="0 0 820 60" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block;">
        <rect x="10" y="5" width="370" height="50" rx="6" fill="rgba(39,174,96,.05)" stroke="var(--emerald)" stroke-width="1"/>
        <text x="195" y="17" text-anchor="middle" fill="var(--emerald)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11" letter-spacing=".04em">&#10003; PASA &mdash; L&Aacute;MINA UNIFORME</text>
        <rect x="40" y="24" width="310" height="8" rx="2" fill="rgba(39,174,96,.15)"/>
        <line x1="40" y1="36" x2="350" y2="36" stroke="var(--muted)" stroke-width="1"/>
        <text x="195" y="48" text-anchor="middle" fill="var(--emerald)" font-family="Inter,sans-serif" font-size="7.5" font-weight="600">Pel&iacute;cula continua de agua &ge;30 s &rarr; proceda</text>
        <rect x="430" y="5" width="370" height="50" rx="6" fill="rgba(224,92,92,.05)" stroke="var(--coral)" stroke-width="1"/>
        <text x="615" y="17" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11" letter-spacing=".04em">&#10007; FALLA &mdash; GOTAS / RUPTURAS</text>
        <ellipse cx="480" cy="28" rx="10" ry="6" fill="rgba(224,92,92,.2)"/>
        <ellipse cx="540" cy="28" rx="14" ry="6" fill="rgba(224,92,92,.2)"/>
        <ellipse cx="620" cy="28" rx="8" ry="6" fill="rgba(224,92,92,.2)"/>
        <ellipse cx="690" cy="28" rx="16" ry="6" fill="rgba(224,92,92,.2)"/>
        <ellipse cx="760" cy="28" rx="12" ry="6" fill="rgba(224,92,92,.2)"/>
        <line x1="460" y1="36" x2="780" y2="36" stroke="var(--muted)" stroke-width="1"/>
        <text x="615" y="48" text-anchor="middle" fill="var(--coral)" font-family="Inter,sans-serif" font-size="7.5" font-weight="600">Agua se gotea o rompe &rarr; RE-LIMPIE</text>
      </svg>
    </div>

    <!-- REGLAS CLAVE -->
    <div class="glass numbered-list" style="padding:10px 14px;">
      <div class="section-title">Reglas Clave</div>
      <div style="display:flex;flex-direction:column;gap:6px;">
        <div class="list-item"><div class="num">1</div><div class="num-text"><strong>Prueba de ruptura de agua en cada rack.</strong> Saque la pieza del enjuague, sostenga vertical &mdash; el agua debe formar l&aacute;mina uniforme por 30 s sin gotas.</div></div>
        <div class="list-item"><div class="num">2</div><div class="num-text"><strong>Mantenga la temperatura.</strong> Limpiador fr&iacute;o no limpia. Mantenga 60&ndash;80&deg;C.</div></div>
        <div class="list-item"><div class="num">3</div><div class="num-text"><strong>Reponga regularmente.</strong> Un limpiador sucio re-deposita suciedad en las piezas. Reponga seg&uacute;n programa del proveedor.</div></div>
        <div class="list-item"><div class="num">4</div><div class="num-text"><strong>No sobre-remoje hierro fundido o aluminio.</strong> La exposici&oacute;n alcalina prolongada ataca Al y puede disolver fundiciones.</div></div>
      </div>
    </div>

    <!-- HAGA / NO HAGA -->
    <div class="compare-row">
      <div class="compare-card glass do"><div class="compare-head good">&#10003; Haga</div><ul class="compare-list"><li>Prueba de ruptura de agua en cada rack</li><li>Mantenga limpiador a temperatura de operaci&oacute;n</li><li>Agite piezas durante inmersi&oacute;n</li><li>Reponga limpiador seg&uacute;n programa</li><li>Re-limpie cualquier pieza que falle ruptura de agua</li></ul></div>
      <div class="compare-card glass dont"><div class="compare-head bad">&#10007; No Haga</div><ul class="compare-list"><li>Omitir prueba de ruptura de agua para ahorrar tiempo</li><li>Operar limpiador bajo temperatura</li><li>Dejar piezas remojando toda la noche (riesgo de ataque)</li><li>Arrastrar limpiador sucio al enjuague</li><li>Tocar piezas limpias con manos desnudas</li></ul></div>
    </div>

    <div class="glass safety-card">
      <div class="section-title coral">&#9888; Seguridad &mdash; Limpieza</div>
      <div class="safety-text"><strong>Soluci&oacute;n alcalina caliente</strong> a 60&ndash;80&deg;C causa quemaduras qu&iacute;micas severas. Corrosivo para ojos y piel. Siempre use careta, lentes de seguridad contra salpicaduras qu&iacute;micas, guantes de nitrilo y mandil qu&iacute;mico. Nunca agregue agua al limpiador concentrado &mdash; siempre agregue limpiador al agua. Regadera y lavaojos a 10 segundos. Lave cualquier contacto con agua por 15+ minutos. Si se usa electrolimpieza: se genera gas hidr&oacute;geno &mdash; sin chispas, sin llama abierta.</div>
    </div>
"""

# =====================================================================
# POSTER 03 — RINSE PRE-ACTIVATION
# =====================================================================
TECH_BODY_EN["03"] = """
    <div class="glass rule-card">
      <div class="rule-num">R</div>
      <div class="rule-body">
        <div class="rule-label">Cascade Rinse &mdash; Between Cleaning and Activation</div>
        <div class="rule-text">Rinsing removes drag-out chemicals from the previous stage before the part enters the next. In EN processing, the rinse between alkaline cleaning and acid activation is critical: alkaline carry-over neutralizes the acid, wastes activation chemistry, and can leave invisible residual films that cause adhesion failures downstream. Counter-flow cascade rinsing reduces water consumption by 90% compared to single-stage overflow while achieving lower conductivity targets.</div>
      </div>
    </div>

    <!-- COUNTER-FLOW RINSE SVG -->
    <div class="glass" style="padding:10px 14px;">
      <h3 class="section-title" style="margin-bottom:4px;">Counter-Flow Cascade Rinse <span class="sub">water flow vs part flow</span></h3>
      <svg viewBox="0 0 1100 120" width="100%" height="120" fill="none" xmlns="http://www.w3.org/2000/svg">
        <!-- Tank 1 (dirtiest) -->
        <rect x="80" y="25" width="200" height="65" rx="6" fill="rgba(224,92,92,.08)" stroke="var(--coral)" stroke-width="1.2"/>
        <text x="180" y="18" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="12" letter-spacing=".06em">RINSE 1 (DIRTIEST)</text>
        <text x="180" y="50" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="9">High conductivity</text>
        <text x="180" y="62" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="9">100&ndash;200 &micro;S/cm</text>
        <text x="180" y="82" text-anchor="middle" fill="var(--coral)" font-family="Inter,sans-serif" font-size="7" font-weight="600">Overflow &rarr; DRAIN</text>
        <!-- Arrow down (drain) -->
        <line x1="180" y1="90" x2="180" y2="105" stroke="var(--coral)" stroke-width="1.2" stroke-dasharray="3,2"/>
        <text x="180" y="115" text-anchor="middle" fill="var(--coral)" font-family="Inter,sans-serif" font-size="7">TO WASTE TREATMENT</text>

        <!-- Tank 2 -->
        <rect x="380" y="25" width="200" height="65" rx="6" fill="rgba(232,160,32,.08)" stroke="var(--amber)" stroke-width="1.2"/>
        <text x="480" y="18" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="12" letter-spacing=".06em">RINSE 2</text>
        <text x="480" y="50" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="9">Medium conductivity</text>
        <text x="480" y="62" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="9">20&ndash;50 &micro;S/cm</text>

        <!-- Tank 3 (cleanest) -->
        <rect x="680" y="25" width="200" height="65" rx="6" fill="rgba(39,174,96,.08)" stroke="var(--emerald)" stroke-width="1.2"/>
        <text x="780" y="18" text-anchor="middle" fill="var(--emerald)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="12" letter-spacing=".06em">RINSE 3 (CLEANEST)</text>
        <text x="780" y="50" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="9">Low conductivity</text>
        <text x="780" y="62" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="9">&lt;50 &micro;S/cm target</text>

        <!-- Part flow arrows (left to right, top) -->
        <line x1="30" y1="40" x2="78" y2="40" stroke="var(--amber)" stroke-width="1.5"/><polygon points="74,37 80,40 74,43" fill="var(--amber)"/>
        <text x="54" y="35" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="9">PARTS &rarr;</text>
        <line x1="282" y1="40" x2="378" y2="40" stroke="var(--amber)" stroke-width="1.5"/><polygon points="374,37 380,40 374,43" fill="var(--amber)"/>
        <line x1="582" y1="40" x2="678" y2="40" stroke="var(--amber)" stroke-width="1.5"/><polygon points="674,37 680,40 674,43" fill="var(--amber)"/>
        <line x1="882" y1="40" x2="960" y2="40" stroke="var(--amber)" stroke-width="1.5"/><polygon points="956,37 962,40 956,43" fill="var(--amber)"/>
        <text x="980" y="37" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="9">TO</text>
        <text x="980" y="47" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="9">ACID</text>

        <!-- Water flow arrows (right to left, bottom) -->
        <line x1="920" y1="75" x2="882" y2="75" stroke="var(--teal)" stroke-width="1.5"/><polygon points="886,72 880,75 886,78" fill="var(--teal)"/>
        <text x="955" y="78" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="9">FRESH</text>
        <text x="955" y="88" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="9">DI</text>
        <line x1="678" y1="75" x2="582" y2="75" stroke="var(--teal)" stroke-width="1.5"/><polygon points="586,72 580,75 586,78" fill="var(--teal)"/>
        <text x="630" y="70" text-anchor="middle" fill="var(--teal)" font-family="Inter,sans-serif" font-size="7" font-weight="600">&larr; WATER FLOW</text>
        <line x1="378" y1="75" x2="282" y2="75" stroke="var(--teal)" stroke-width="1.5"/><polygon points="286,72 280,75 286,78" fill="var(--teal)"/>
      </svg>
    </div>

    <!-- RINSE THEORY TABLE -->
    <div class="bottom-grid">
      <div>
        <h3 class="section-title">Rinse Theory <span class="sub">drag-out / drag-in</span></h3>
        <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
          <table class="data-table compact">
            <thead><tr><th>Concept</th><th>Definition</th><th>Impact</th></tr></thead>
            <tbody>
              <tr><td style="font-weight:600;color:var(--amber);">Drag-Out</td><td>Chemical film carried from a process tank on the part surface and rack</td><td>Determines how much contamination enters the rinse</td></tr>
              <tr><td style="font-weight:600;color:var(--amber);">Drag-In</td><td>Rinse water (with residual contamination) carried into the next process tank</td><td>Contaminates downstream chemistry; shortens bath life</td></tr>
              <tr><td style="font-weight:600;color:var(--amber);">Dilution Ratio</td><td>Volume of rinse water needed to reduce drag-out concentration to target</td><td>Determines rinse stages and water flow rate needed</td></tr>
              <tr><td style="font-weight:600;color:var(--amber);">Drain Time</td><td>Time allowed for part to drip before moving to next tank</td><td>5&ndash;10 sec drain reduces drag-out by 50&ndash;80%</td></tr>
            </tbody>
          </table>
        </div>
      </div>
      <div>
        <h3 class="section-title">Conductivity Targets <span class="sub">this rinse stage</span></h3>
        <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
          <table class="data-table bath">
            <thead><tr><th>Measurement</th><th>Target</th></tr></thead>
            <tbody>
              <tr><td>Rinse 1 (first contact)</td><td class="mono">&lt;200 &micro;S/cm</td></tr>
              <tr><td>Rinse 2 (middle)</td><td class="mono">&lt;100 &micro;S/cm</td></tr>
              <tr><td>Final Rinse (leaving)</td><td class="mono">&lt;50 &micro;S/cm</td></tr>
              <tr><td>Incoming DI water</td><td class="mono">&lt;5 &micro;S/cm</td></tr>
              <tr><td>Measurement point</td><td>Last cascade tank</td></tr>
              <tr><td>Frequency</td><td>Every 2 hours minimum</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- CONTAMINATION EFFECTS -->
    <div>
      <h3 class="section-title">Contamination Effects on Downstream Stages <span class="sub">what happens if rinsing fails</span></h3>
      <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
        <table class="data-table compact">
          <thead><tr><th>Contaminant Carried Forward</th><th>Effect on Activation (Stage 3)</th><th>Effect on EN Bath (Stage 5)</th></tr></thead>
          <tbody>
            <tr><td style="font-weight:600;">Alkaline residue (NaOH)</td><td>Neutralizes acid &rarr; incomplete activation</td><td>Raises pH &rarr; low phosphorus, slow rate</td></tr>
            <tr><td style="font-weight:600;">Silicates</td><td>Invisible film on surface &rarr; skip plating</td><td>Stabilizer poisoning &rarr; slow plating</td></tr>
            <tr><td style="font-weight:600;">Surfactants</td><td>Foaming; wetting interference</td><td>Pitting; stabilizer interaction</td></tr>
            <tr><td style="font-weight:600;">Dissolved metals (Fe, Zn)</td><td>Galvanic displacement in acid</td><td>Immersion deposits; roughness; plate-out risk</td></tr>
            <tr><td style="font-weight:600;">Oil / organic residue</td><td>Passivation of surface</td><td>Skip plating; blistering; decomposition trigger</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="insight-card">
      <div class="insight-label">Water Conservation: Why Counter-Flow Wins</div>
      <div class="insight-text">A single overflow rinse tank achieving a 10,000:1 dilution ratio needs ~10,000 parts of fresh water per part of drag-out. A 3-stage counter-flow cascade achieves the same ratio with only ~22 parts of water per part of drag-out (cube root of 10,000 &asymp; 22). That is a <strong>99.8% reduction in water consumption</strong> for the same rinse quality. Counter-flow also means the cleanest water always contacts the cleanest part last, maximizing effectiveness.</div>
    </div>

    <div class="safety-card">
      <div class="safety-head">&#9888; Safety &mdash; Rinse Stage</div>
      <div class="safety-body">Rinse water may contain <strong>alkaline residues</strong> (pH 10&ndash;12) from drag-out &mdash; treat as mildly corrosive. Wear gloves and splash protection when handling parts or adjusting rinse tanks. <strong>Slip hazard</strong>: wet floors around rinse stations. Maintain anti-slip mats. Rinse overflow goes to waste treatment &mdash; never discharge to storm drain. Conductivity meters should be calibrated weekly to ensure accurate readings.</div>
    </div>
"""

TECH_BODY_ES["03"] = """
    <div class="glass rule-card">
      <div class="rule-num">R</div>
      <div class="rule-body">
        <div class="rule-label">Enjuague en Cascada &mdash; Entre Limpieza y Activaci&oacute;n</div>
        <div class="rule-text">El enjuague remueve qu&iacute;micos de arrastre de la etapa anterior antes de que la pieza entre a la siguiente. En el proceso EN, el enjuague entre limpieza alcalina y activaci&oacute;n &aacute;cida es cr&iacute;tico: el arrastre alcalino neutraliza el &aacute;cido, desperdicia qu&iacute;mica de activaci&oacute;n, y puede dejar pel&iacute;culas residuales invisibles que causan fallas de adherencia. El enjuague en cascada a contraflujo reduce el consumo de agua un 90% comparado con un solo tanque de rebose mientras logra menor conductividad.</div>
      </div>
    </div>

    <!-- SVG ENJUAGUE A CONTRAFLUJO -->
    <div class="glass" style="padding:10px 14px;">
      <h3 class="section-title" style="margin-bottom:4px;">Enjuague en Cascada a Contraflujo <span class="sub">flujo de agua vs flujo de piezas</span></h3>
      <svg viewBox="0 0 1100 120" width="100%" height="120" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect x="80" y="25" width="200" height="65" rx="6" fill="rgba(224,92,92,.08)" stroke="var(--coral)" stroke-width="1.2"/>
        <text x="180" y="18" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="12" letter-spacing=".06em">ENJ. 1 (M&Aacute;S SUCIO)</text>
        <text x="180" y="50" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="9">Alta conductividad</text>
        <text x="180" y="62" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="9">100&ndash;200 &micro;S/cm</text>
        <text x="180" y="82" text-anchor="middle" fill="var(--coral)" font-family="Inter,sans-serif" font-size="7" font-weight="600">Rebose &rarr; DRENAJE</text>
        <line x1="180" y1="90" x2="180" y2="105" stroke="var(--coral)" stroke-width="1.2" stroke-dasharray="3,2"/>
        <text x="180" y="115" text-anchor="middle" fill="var(--coral)" font-family="Inter,sans-serif" font-size="7">A TRATAMIENTO DE RESIDUOS</text>
        <rect x="380" y="25" width="200" height="65" rx="6" fill="rgba(232,160,32,.08)" stroke="var(--amber)" stroke-width="1.2"/>
        <text x="480" y="18" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="12" letter-spacing=".06em">ENJ. 2</text>
        <text x="480" y="50" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="9">Conductividad media</text>
        <text x="480" y="62" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="9">20&ndash;50 &micro;S/cm</text>
        <rect x="680" y="25" width="200" height="65" rx="6" fill="rgba(39,174,96,.08)" stroke="var(--emerald)" stroke-width="1.2"/>
        <text x="780" y="18" text-anchor="middle" fill="var(--emerald)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="12" letter-spacing=".06em">ENJ. 3 (M&Aacute;S LIMPIO)</text>
        <text x="780" y="50" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="9">Baja conductividad</text>
        <text x="780" y="62" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="9">&lt;50 &micro;S/cm objetivo</text>
        <line x1="30" y1="40" x2="78" y2="40" stroke="var(--amber)" stroke-width="1.5"/><polygon points="74,37 80,40 74,43" fill="var(--amber)"/>
        <text x="54" y="35" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="9">PIEZAS &rarr;</text>
        <line x1="282" y1="40" x2="378" y2="40" stroke="var(--amber)" stroke-width="1.5"/><polygon points="374,37 380,40 374,43" fill="var(--amber)"/>
        <line x1="582" y1="40" x2="678" y2="40" stroke="var(--amber)" stroke-width="1.5"/><polygon points="674,37 680,40 674,43" fill="var(--amber)"/>
        <line x1="882" y1="40" x2="960" y2="40" stroke="var(--amber)" stroke-width="1.5"/><polygon points="956,37 962,40 956,43" fill="var(--amber)"/>
        <text x="980" y="37" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="9">A</text>
        <text x="980" y="47" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="9">&Aacute;CIDO</text>
        <line x1="920" y1="75" x2="882" y2="75" stroke="var(--teal)" stroke-width="1.5"/><polygon points="886,72 880,75 886,78" fill="var(--teal)"/>
        <text x="955" y="78" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="9">DI</text>
        <text x="955" y="88" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="9">FRESCA</text>
        <line x1="678" y1="75" x2="582" y2="75" stroke="var(--teal)" stroke-width="1.5"/><polygon points="586,72 580,75 586,78" fill="var(--teal)"/>
        <text x="630" y="70" text-anchor="middle" fill="var(--teal)" font-family="Inter,sans-serif" font-size="7" font-weight="600">&larr; FLUJO DE AGUA</text>
        <line x1="378" y1="75" x2="282" y2="75" stroke="var(--teal)" stroke-width="1.5"/><polygon points="286,72 280,75 286,78" fill="var(--teal)"/>
      </svg>
    </div>

    <!-- TEOR&Iacute;A DE ENJUAGUE -->
    <div class="bottom-grid">
      <div>
        <h3 class="section-title">Teor&iacute;a de Enjuague <span class="sub">arrastre / contaminaci&oacute;n</span></h3>
        <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
          <table class="data-table compact">
            <thead><tr><th>Concepto</th><th>Definici&oacute;n</th><th>Impacto</th></tr></thead>
            <tbody>
              <tr><td style="font-weight:600;color:var(--amber);">Arrastre de Salida</td><td>Pel&iacute;cula qu&iacute;mica que se lleva del tanque de proceso en la superficie y rack</td><td>Determina cu&aacute;nta contaminaci&oacute;n entra al enjuague</td></tr>
              <tr><td style="font-weight:600;color:var(--amber);">Arrastre de Entrada</td><td>Agua de enjuague (con contaminaci&oacute;n residual) que entra al siguiente tanque</td><td>Contamina qu&iacute;mica posterior; acorta vida del ba&ntilde;o</td></tr>
              <tr><td style="font-weight:600;color:var(--amber);">Raz&oacute;n de Diluci&oacute;n</td><td>Volumen de agua necesario para reducir concentraci&oacute;n de arrastre al objetivo</td><td>Determina etapas de enjuague y flujo de agua necesario</td></tr>
              <tr><td style="font-weight:600;color:var(--amber);">Tiempo de Escurrido</td><td>Tiempo para que la pieza gotee antes de mover al siguiente tanque</td><td>5&ndash;10 s de escurrido reduce arrastre un 50&ndash;80%</td></tr>
            </tbody>
          </table>
        </div>
      </div>
      <div>
        <h3 class="section-title">Objetivos de Conductividad <span class="sub">esta etapa</span></h3>
        <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
          <table class="data-table bath">
            <thead><tr><th>Medici&oacute;n</th><th>Objetivo</th></tr></thead>
            <tbody>
              <tr><td>Enjuague 1 (primer contacto)</td><td class="mono">&lt;200 &micro;S/cm</td></tr>
              <tr><td>Enjuague 2 (medio)</td><td class="mono">&lt;100 &micro;S/cm</td></tr>
              <tr><td>Enjuague Final (salida)</td><td class="mono">&lt;50 &micro;S/cm</td></tr>
              <tr><td>Agua DI entrante</td><td class="mono">&lt;5 &micro;S/cm</td></tr>
              <tr><td>Punto de medici&oacute;n</td><td>&Uacute;ltimo tanque de cascada</td></tr>
              <tr><td>Frecuencia</td><td>Cada 2 horas m&iacute;nimo</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- EFECTOS DE CONTAMINACI&Oacute;N -->
    <div>
      <h3 class="section-title">Efectos de Contaminaci&oacute;n en Etapas Posteriores <span class="sub">qu&eacute; pasa si el enjuague falla</span></h3>
      <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
        <table class="data-table compact">
          <thead><tr><th>Contaminante Arrastrado</th><th>Efecto en Activaci&oacute;n (Etapa 3)</th><th>Efecto en Ba&ntilde;o EN (Etapa 5)</th></tr></thead>
          <tbody>
            <tr><td style="font-weight:600;">Residuo alcalino (NaOH)</td><td>Neutraliza &aacute;cido &rarr; activaci&oacute;n incompleta</td><td>Sube pH &rarr; bajo f&oacute;sforo, velocidad lenta</td></tr>
            <tr><td style="font-weight:600;">Silicatos</td><td>Pel&iacute;cula invisible &rarr; falta de dep&oacute;sito</td><td>Envenenamiento de estabilizador &rarr; dep&oacute;sito lento</td></tr>
            <tr><td style="font-weight:600;">Surfactantes</td><td>Espuma; interferencia de humectaci&oacute;n</td><td>Picaduras; interacci&oacute;n con estabilizador</td></tr>
            <tr><td style="font-weight:600;">Metales disueltos (Fe, Zn)</td><td>Desplazamiento galv&aacute;nico en &aacute;cido</td><td>Dep&oacute;sitos por inmersi&oacute;n; rugosidad; riesgo de plate-out</td></tr>
            <tr><td style="font-weight:600;">Aceite / residuo org&aacute;nico</td><td>Pasivaci&oacute;n de superficie</td><td>Falta de dep&oacute;sito; ampollas; disparador de descomposici&oacute;n</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="insight-card">
      <div class="insight-label">Conservaci&oacute;n de Agua: Por Qu&eacute; Gana el Contraflujo</div>
      <div class="insight-text">Un solo tanque de enjuague por rebose que logra una raz&oacute;n de diluci&oacute;n de 10,000:1 necesita ~10,000 partes de agua fresca por parte de arrastre. Una cascada a contraflujo de 3 etapas logra la misma raz&oacute;n con solo ~22 partes de agua por parte de arrastre (ra&iacute;z c&uacute;bica de 10,000 &asymp; 22). Eso es una <strong>reducci&oacute;n del 99.8% en consumo de agua</strong> para la misma calidad de enjuague. El contraflujo tambi&eacute;n significa que el agua m&aacute;s limpia siempre contacta la pieza m&aacute;s limpia al final, maximizando efectividad.</div>
    </div>

    <div class="safety-card">
      <div class="safety-head">&#9888; Seguridad &mdash; Etapa de Enjuague</div>
      <div class="safety-body">El agua de enjuague puede contener <strong>residuos alcalinos</strong> (pH 10&ndash;12) del arrastre &mdash; tratar como ligeramente corrosivo. Use guantes y protecci&oacute;n contra salpicaduras al manejar piezas o ajustar tanques. <strong>Riesgo de resbal&oacute;n</strong>: pisos mojados alrededor de estaciones de enjuague. Mantenga tapetes antideslizantes. El rebose del enjuague va a tratamiento de residuos &mdash; nunca descargue al drenaje pluvial. Los medidores de conductividad deben calibrarse semanalmente para asegurar lecturas precisas.</div>
    </div>
"""

SF_BODY_EN["03"] = """
    <div class="glass key-card">
      <div class="key-num">R</div>
      <div class="key-label">Cascade Rinse &mdash; Between Cleaning and Activation</div>
      <div class="key-text">This rinse removes all cleaning chemical residue before the part enters acid activation. Alkaline carry-over neutralizes the acid and causes adhesion failures in the EN bath. Good rinsing here protects every stage downstream.</div>
    </div>

    <!-- PARAMETERS TABLE -->
    <div class="glass" style="padding:10px 12px;">
      <div class="section-title">Rinse Parameters</div>
      <table class="data-table compact">
        <thead><tr><th>Parameter</th><th>Target</th><th>Why It Matters</th></tr></thead>
        <tbody>
          <tr><td>Configuration</td><td>Counter-flow cascade (2&ndash;3 stages)</td><td>Saves water; better rinse quality</td></tr>
          <tr><td>Water Source</td><td>City water OK at this stage</td><td>DI not required until pre-EN rinse</td></tr>
          <tr><td>Conductivity (last tank)</td><td class="mono">&lt;50 &micro;S/cm</td><td>Confirms alkaline removal</td></tr>
          <tr><td>Time per Stage</td><td class="mono">30&ndash;60 sec</td><td>Agitate parts during rinse</td></tr>
          <tr><td>Temperature</td><td class="mono">Ambient</td><td>Room temp is fine</td></tr>
          <tr><td>Drain Time</td><td class="mono">5&ndash;10 sec over tank</td><td>Reduces drag-out by 50&ndash;80%</td></tr>
        </tbody>
      </table>
    </div>

    <!-- KEY RULES -->
    <div class="glass numbered-list" style="padding:10px 14px;">
      <div class="section-title">Key Rules</div>
      <div style="display:flex;flex-direction:column;gap:6px;">
        <div class="list-item"><div class="num">1</div><div class="num-text"><strong>Check conductivity every 2 hours.</strong> If the last rinse tank reads &gt;50 &micro;S/cm, increase water flow or dump and refill.</div></div>
        <div class="list-item"><div class="num">2</div><div class="num-text"><strong>Let parts drain 5&ndash;10 seconds</strong> over the cleaner tank before transferring to rinse. This cuts drag-out in half.</div></div>
        <div class="list-item"><div class="num">3</div><div class="num-text"><strong>Agitate parts in the rinse.</strong> Stagnant immersion leaves alkaline pockets in recesses and blind holes.</div></div>
        <div class="list-item"><div class="num">4</div><div class="num-text"><strong>Do not skip this stage.</strong> Alkaline residue in the acid activation tank wastes acid, raises pH, and causes skip plating in the EN bath.</div></div>
      </div>
    </div>

    <!-- SIMPLE COUNTER-FLOW VISUAL -->
    <div class="glass" style="padding:10px 12px;">
      <div class="section-title">Counter-Flow Cascade</div>
      <svg viewBox="0 0 820 65" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block;">
        <rect x="30" y="10" width="180" height="35" rx="5" fill="rgba(224,92,92,.08)" stroke="var(--coral)" stroke-width="1"/>
        <text x="120" y="25" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="9">TANK 1 (DIRTIEST)</text>
        <text x="120" y="38" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="7">&lt;200 &micro;S</text>
        <rect x="280" y="10" width="180" height="35" rx="5" fill="rgba(232,160,32,.08)" stroke="var(--amber)" stroke-width="1"/>
        <text x="370" y="25" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="9">TANK 2</text>
        <text x="370" y="38" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="7">&lt;100 &micro;S</text>
        <rect x="530" y="10" width="180" height="35" rx="5" fill="rgba(39,174,96,.08)" stroke="var(--emerald)" stroke-width="1"/>
        <text x="620" y="25" text-anchor="middle" fill="var(--emerald)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="9">TANK 3 (CLEANEST)</text>
        <text x="620" y="38" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="7">&lt;50 &micro;S</text>
        <!-- Part arrows top -->
        <line x1="212" y1="22" x2="278" y2="22" stroke="var(--amber)" stroke-width="1.2"/><polygon points="274,19 280,22 274,25" fill="var(--amber)"/>
        <line x1="462" y1="22" x2="528" y2="22" stroke="var(--amber)" stroke-width="1.2"/><polygon points="524,19 530,22 524,25" fill="var(--amber)"/>
        <text x="245" y="18" text-anchor="middle" fill="var(--amber)" font-family="Inter,sans-serif" font-size="6.5" font-weight="600">PARTS &rarr;</text>
        <!-- Water arrows bottom -->
        <line x1="528" y1="38" x2="462" y2="38" stroke="var(--teal)" stroke-width="1.2"/><polygon points="466,35 460,38 466,41" fill="var(--teal)"/>
        <line x1="278" y1="38" x2="212" y2="38" stroke="var(--teal)" stroke-width="1.2"/><polygon points="216,35 210,38 216,41" fill="var(--teal)"/>
        <text x="495" y="55" text-anchor="middle" fill="var(--teal)" font-family="Inter,sans-serif" font-size="6.5" font-weight="600">&larr; FRESH DI WATER IN</text>
        <text x="245" y="55" text-anchor="middle" fill="var(--coral)" font-family="Inter,sans-serif" font-size="6.5" font-weight="600">OVERFLOW TO DRAIN &rarr;</text>
      </svg>
    </div>

    <div class="insight-card">
      <div class="insight-label">Why Counter-Flow?</div>
      <div class="insight-text">Fresh water enters the cleanest tank and overflows toward the dirtiest. The cleanest water always contacts the cleanest part last. This saves 90%+ of water compared to single-tank overflow while giving you a better rinse. Ask your supervisor about your facility&rsquo;s specific flow rate.</div>
    </div>

    <!-- DO / DON'T -->
    <div class="compare-row">
      <div class="compare-card glass do"><div class="compare-head good">&#10003; Do</div><ul class="compare-list"><li>Check conductivity every 2 hours</li><li>Drain 5&ndash;10 sec over cleaner before moving to rinse</li><li>Agitate parts during rinse</li><li>Keep water flowing &mdash; stagnant rinse = bad rinse</li><li>Report any rinse tank overflow or plumbing issue</li></ul></div>
      <div class="compare-card glass dont"><div class="compare-head bad">&#10007; Don&rsquo;t</div><ul class="compare-list"><li>Skip the rinse &mdash; alkaline carry-over kills the acid bath</li><li>Turn off water flow to &ldquo;save water&rdquo;</li><li>Let parts sit in stagnant rinse</li><li>Ignore high conductivity readings</li><li>Dump rinse water to storm drain</li></ul></div>
    </div>

    <div class="glass safety-card">
      <div class="section-title coral">&#9888; Safety &mdash; Rinse</div>
      <div class="safety-text">Rinse water may contain <strong>alkaline residues</strong> from drag-out &mdash; treat as mildly corrosive. Wear gloves and splash goggles. <strong>Slip hazard</strong>: wet floors are common around rinse stations. Keep anti-slip mats in place. Rinse overflow goes to waste treatment &mdash; never pour anything down an unmarked drain.</div>
    </div>
"""

SF_BODY_ES["03"] = """
    <div class="glass key-card">
      <div class="key-num">R</div>
      <div class="key-label">Enjuague en Cascada &mdash; Entre Limpieza y Activaci&oacute;n</div>
      <div class="key-text">Este enjuague remueve todo residuo del limpiador antes de que la pieza entre a la activaci&oacute;n &aacute;cida. El arrastre alcalino neutraliza el &aacute;cido y causa fallas de adherencia en el ba&ntilde;o EN. Un buen enjuague aqu&iacute; protege cada etapa posterior.</div>
    </div>

    <!-- TABLA DE PAR&Aacute;METROS -->
    <div class="glass" style="padding:10px 12px;">
      <div class="section-title">Par&aacute;metros de Enjuague</div>
      <table class="data-table compact">
        <thead><tr><th>Par&aacute;metro</th><th>Objetivo</th><th>Por Qu&eacute; Importa</th></tr></thead>
        <tbody>
          <tr><td>Configuraci&oacute;n</td><td>Cascada a contraflujo (2&ndash;3 etapas)</td><td>Ahorra agua; mejor calidad de enjuague</td></tr>
          <tr><td>Fuente de Agua</td><td>Agua de ciudad OK en esta etapa</td><td>DI no requerida hasta enjuague pre-EN</td></tr>
          <tr><td>Conductividad (&uacute;ltimo tanque)</td><td class="mono">&lt;50 &micro;S/cm</td><td>Confirma remoci&oacute;n de alcalino</td></tr>
          <tr><td>Tiempo por Etapa</td><td class="mono">30&ndash;60 s</td><td>Agite piezas durante enjuague</td></tr>
          <tr><td>Temperatura</td><td class="mono">Ambiente</td><td>Temperatura ambiente est&aacute; bien</td></tr>
          <tr><td>Tiempo de Escurrido</td><td class="mono">5&ndash;10 s sobre tanque</td><td>Reduce arrastre un 50&ndash;80%</td></tr>
        </tbody>
      </table>
    </div>

    <!-- REGLAS CLAVE -->
    <div class="glass numbered-list" style="padding:10px 14px;">
      <div class="section-title">Reglas Clave</div>
      <div style="display:flex;flex-direction:column;gap:6px;">
        <div class="list-item"><div class="num">1</div><div class="num-text"><strong>Revise conductividad cada 2 horas.</strong> Si el &uacute;ltimo tanque lee &gt;50 &micro;S/cm, aumente el flujo de agua o descarte y rellene.</div></div>
        <div class="list-item"><div class="num">2</div><div class="num-text"><strong>Deje escurrir las piezas 5&ndash;10 segundos</strong> sobre el tanque del limpiador antes de transferir al enjuague. Esto corta el arrastre a la mitad.</div></div>
        <div class="list-item"><div class="num">3</div><div class="num-text"><strong>Agite las piezas en el enjuague.</strong> La inmersi&oacute;n estancada deja bolsas alcalinas en cavidades y agujeros ciegos.</div></div>
        <div class="list-item"><div class="num">4</div><div class="num-text"><strong>No omita esta etapa.</strong> Residuo alcalino en el tanque de activaci&oacute;n desperdicia &aacute;cido, sube pH y causa falta de dep&oacute;sito en el ba&ntilde;o EN.</div></div>
      </div>
    </div>

    <!-- VISUAL SIMPLE DE CONTRAFLUJO -->
    <div class="glass" style="padding:10px 12px;">
      <div class="section-title">Cascada a Contraflujo</div>
      <svg viewBox="0 0 820 65" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block;">
        <rect x="30" y="10" width="180" height="35" rx="5" fill="rgba(224,92,92,.08)" stroke="var(--coral)" stroke-width="1"/>
        <text x="120" y="25" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="9">TANQUE 1 (M&Aacute;S SUCIO)</text>
        <text x="120" y="38" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="7">&lt;200 &micro;S</text>
        <rect x="280" y="10" width="180" height="35" rx="5" fill="rgba(232,160,32,.08)" stroke="var(--amber)" stroke-width="1"/>
        <text x="370" y="25" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="9">TANQUE 2</text>
        <text x="370" y="38" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="7">&lt;100 &micro;S</text>
        <rect x="530" y="10" width="180" height="35" rx="5" fill="rgba(39,174,96,.08)" stroke="var(--emerald)" stroke-width="1"/>
        <text x="620" y="25" text-anchor="middle" fill="var(--emerald)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="9">TANQUE 3 (M&Aacute;S LIMPIO)</text>
        <text x="620" y="38" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="7">&lt;50 &micro;S</text>
        <line x1="212" y1="22" x2="278" y2="22" stroke="var(--amber)" stroke-width="1.2"/><polygon points="274,19 280,22 274,25" fill="var(--amber)"/>
        <line x1="462" y1="22" x2="528" y2="22" stroke="var(--amber)" stroke-width="1.2"/><polygon points="524,19 530,22 524,25" fill="var(--amber)"/>
        <text x="245" y="18" text-anchor="middle" fill="var(--amber)" font-family="Inter,sans-serif" font-size="6.5" font-weight="600">PIEZAS &rarr;</text>
        <line x1="528" y1="38" x2="462" y2="38" stroke="var(--teal)" stroke-width="1.2"/><polygon points="466,35 460,38 466,41" fill="var(--teal)"/>
        <line x1="278" y1="38" x2="212" y2="38" stroke="var(--teal)" stroke-width="1.2"/><polygon points="216,35 210,38 216,41" fill="var(--teal)"/>
        <text x="495" y="55" text-anchor="middle" fill="var(--teal)" font-family="Inter,sans-serif" font-size="6.5" font-weight="600">&larr; AGUA DI FRESCA ENTRA</text>
        <text x="245" y="55" text-anchor="middle" fill="var(--coral)" font-family="Inter,sans-serif" font-size="6.5" font-weight="600">REBOSE A DRENAJE &rarr;</text>
      </svg>
    </div>

    <div class="insight-card">
      <div class="insight-label">&iquest;Por Qu&eacute; Contraflujo?</div>
      <div class="insight-text">El agua fresca entra al tanque m&aacute;s limpio y rebosa hacia el m&aacute;s sucio. El agua m&aacute;s limpia siempre contacta la pieza m&aacute;s limpia al final. Esto ahorra m&aacute;s del 90% del agua comparado con un solo tanque de rebose mientras logra mejor enjuague. Pregunte a su supervisor sobre el flujo espec&iacute;fico de su instalaci&oacute;n.</div>
    </div>

    <!-- HAGA / NO HAGA -->
    <div class="compare-row">
      <div class="compare-card glass do"><div class="compare-head good">&#10003; Haga</div><ul class="compare-list"><li>Revise conductividad cada 2 horas</li><li>Escurra 5&ndash;10 s sobre limpiador antes de mover al enjuague</li><li>Agite piezas durante el enjuague</li><li>Mantenga el agua fluyendo &mdash; enjuague estancado = mal enjuague</li><li>Reporte cualquier rebose o problema de plomer&iacute;a</li></ul></div>
      <div class="compare-card glass dont"><div class="compare-head bad">&#10007; No Haga</div><ul class="compare-list"><li>Omitir el enjuague &mdash; arrastre alcalino mata el ba&ntilde;o &aacute;cido</li><li>Cerrar el flujo de agua para &ldquo;ahorrar agua&rdquo;</li><li>Dejar piezas en enjuague estancado</li><li>Ignorar lecturas altas de conductividad</li><li>Descargar agua de enjuague al drenaje pluvial</li></ul></div>
    </div>

    <div class="glass safety-card">
      <div class="section-title coral">&#9888; Seguridad &mdash; Enjuague</div>
      <div class="safety-text">El agua de enjuague puede contener <strong>residuos alcalinos</strong> del arrastre &mdash; tratar como ligeramente corrosivo. Use guantes y lentes de seguridad contra salpicaduras. <strong>Riesgo de resbal&oacute;n</strong>: pisos mojados son comunes alrededor de las estaciones de enjuague. Mantenga tapetes antideslizantes en su lugar. El rebose del enjuague va a tratamiento de residuos &mdash; nunca vierta nada a un drenaje sin marcar.</div>
    </div>
"""

# =====================================================================
# POSTER 04 — ACTIVATION
# =====================================================================
TECH_BODY_EN["04"] = """
    <div class="glass rule-card">
      <div class="rule-num">03</div>
      <div class="rule-body">
        <div class="rule-label">Stage 3 &mdash; Acid Activation</div>
        <div class="rule-text">Acid activation removes the thin oxide layer that forms on the substrate after cleaning. This exposes fresh, catalytically active metal that initiates the autocatalytic EN reaction. The activation chemistry must match the substrate: steel, aluminum, and copper alloys each require different acids and procedures. Getting activation wrong is the #1 cause of adhesion failures in electroless nickel plating.</div>
      </div>
    </div>

    <!-- ACTIVATION CHEMISTRY TABLE -->
    <div>
      <h3 class="section-title">Activation Chemistry by Acid Type <span class="sub">common options</span></h3>
      <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
        <table class="data-table compact">
          <thead><tr><th>Acid</th><th>Concentration</th><th>Temp</th><th>Time</th><th>Best For</th></tr></thead>
          <tbody>
            <tr><td style="font-weight:600;color:var(--amber);">Hydrochloric (HCl)</td><td class="mono">10&ndash;20% v/v</td><td class="mono">Ambient</td><td class="mono">30&ndash;60 s</td><td>Steel, stainless steel, iron alloys</td></tr>
            <tr><td style="font-weight:600;color:var(--amber);">Sulfuric (H&#8322;SO&#8324;)</td><td class="mono">10&ndash;25% v/v</td><td class="mono">Ambient</td><td class="mono">30&ndash;60 s</td><td>Steel (alternative to HCl); less fume</td></tr>
            <tr><td style="font-weight:600;color:var(--amber);">Nitric (HNO&#8323;)</td><td class="mono">30&ndash;50% v/v</td><td class="mono">Ambient</td><td class="mono">15&ndash;30 s</td><td>Stainless steel (passivation break); copper alloys</td></tr>
            <tr><td style="font-weight:600;color:var(--amber);">Zincate (NaOH + ZnO)</td><td class="mono">Per supplier</td><td class="mono">70&ndash;80&deg;F (21&ndash;27&deg;C)</td><td class="mono">30&ndash;60 s</td><td>Aluminum &amp; aluminum alloys (immersion Zn layer)</td></tr>
            <tr><td style="font-weight:600;color:var(--amber);">Phosphoric (H&#8323;PO&#8324;)</td><td class="mono">5&ndash;15% v/v</td><td class="mono">Ambient</td><td class="mono">30&ndash;60 s</td><td>Mild activation; sensitive substrates</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- SUBSTRATE ROUTING TABLE -->
    <div>
      <h3 class="section-title">Substrate Routing Guide <span class="sub">which path for which metal</span></h3>
      <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
        <table class="data-table compact">
          <thead><tr><th>Substrate</th><th>Activation Sequence</th><th>Critical Notes</th></tr></thead>
          <tbody>
            <tr><td style="font-weight:600;">Carbon Steel</td><td>HCl 10&ndash;20% &rarr; Rinse &rarr; DI Rinse &rarr; EN</td><td>Standard path; watch for flash rust</td></tr>
            <tr><td style="font-weight:600;">Stainless Steel</td><td>HCl 20% or HNO&#8323; 30% &rarr; Rinse &rarr; DI Rinse &rarr; EN (or Wood&rsquo;s Ni strike)</td><td>Must break passive CrO layer; Wood&rsquo;s strike recommended for 300-series</td></tr>
            <tr><td style="font-weight:600;">Aluminum (wrought)</td><td>NaOH etch &rarr; Rinse &rarr; Zincate &rarr; Strip &rarr; Double Zincate &rarr; Rinse &rarr; EN</td><td>Double zincate is mandatory for adhesion; single zincate = peeling risk</td></tr>
            <tr><td style="font-weight:600;">Aluminum (cast)</td><td>NaOH etch &rarr; Desmut (HNO&#8323;+HF) &rarr; Zincate &rarr; Strip &rarr; Double Zincate &rarr; EN</td><td>High-Si castings need HF desmut; use fuming acid caution</td></tr>
            <tr><td style="font-weight:600;">Copper / Brass</td><td>H&#8322;SO&#8324; 10% or HCl 5&ndash;10% &rarr; Rinse &rarr; EN</td><td>Mild acid; avoid over-etch on thin substrates</td></tr>
            <tr><td style="font-weight:600;">High-Strength Steel (&ge;40 HRC)</td><td>HCl 10% (max 120 s) &rarr; Rinse &rarr; EN &rarr; HE Bake within 4 hr</td><td>Minimize acid exposure; hydrogen embrittlement risk; mandatory HE bake per ASTM B849</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- ACTIVATION MECHANISM SVG -->
    <div class="glass" style="padding:10px 14px;">
      <h3 class="section-title" style="margin-bottom:4px;">Activation Mechanism <span class="sub">oxide removal &rarr; catalytic surface</span></h3>
      <svg viewBox="0 0 1100 90" width="100%" height="90" fill="none" xmlns="http://www.w3.org/2000/svg">
        <!-- Before activation -->
        <rect x="30" y="5" width="320" height="80" rx="8" fill="rgba(224,92,92,.05)" stroke="var(--coral)" stroke-width="1"/>
        <text x="190" y="18" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11" letter-spacing=".06em">BEFORE ACTIVATION</text>
        <rect x="60" y="55" width="260" height="14" rx="3" fill="rgba(232,160,32,.12)" stroke="var(--amber)" stroke-width=".8"/>
        <text x="190" y="65" text-anchor="middle" fill="var(--amber)" font-family="Inter,sans-serif" font-size="7" font-weight="600">BASE METAL (Fe / Al / Cu)</text>
        <rect x="60" y="38" width="260" height="14" rx="3" fill="rgba(224,92,92,.2)" stroke="var(--coral)" stroke-width=".8"/>
        <text x="190" y="48" text-anchor="middle" fill="var(--coral)" font-family="Inter,sans-serif" font-size="7" font-weight="600">OXIDE LAYER (passive, non-catalytic)</text>
        <text x="190" y="30" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="7" font-style="italic">EN cannot initiate on oxide &mdash; no catalytic activity</text>

        <!-- Arrow -->
        <line x1="360" y1="45" x2="420" y2="45" stroke="var(--amber)" stroke-width="2"/><polygon points="416,40 425,45 416,50" fill="var(--amber)"/>
        <text x="392" y="38" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="10">ACID</text>

        <!-- After activation -->
        <rect x="430" y="5" width="320" height="80" rx="8" fill="rgba(39,174,96,.05)" stroke="var(--emerald)" stroke-width="1"/>
        <text x="590" y="18" text-anchor="middle" fill="var(--emerald)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11" letter-spacing=".06em">AFTER ACTIVATION</text>
        <rect x="460" y="50" width="260" height="14" rx="3" fill="rgba(232,160,32,.12)" stroke="var(--amber)" stroke-width=".8"/>
        <text x="590" y="60" text-anchor="middle" fill="var(--amber)" font-family="Inter,sans-serif" font-size="7" font-weight="600">CLEAN BASE METAL (catalytically active)</text>
        <text x="590" y="30" text-anchor="middle" fill="var(--emerald)" font-family="Inter,sans-serif" font-size="7" font-weight="600">Oxide dissolved &rarr; fresh metal surface exposed</text>
        <text x="590" y="42" text-anchor="middle" fill="var(--emerald)" font-family="Inter,sans-serif" font-size="7">Fe/Ni/Cu surface catalyzes Ni&sup2;&#8314; reduction by hypophosphite</text>

        <!-- Al zincate path -->
        <rect x="780" y="5" width="280" height="80" rx="8" fill="rgba(46,196,182,.05)" stroke="var(--teal)" stroke-width="1"/>
        <text x="920" y="18" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11" letter-spacing=".06em">ALUMINUM PATH (ZINCATE)</text>
        <rect x="810" y="50" width="220" height="14" rx="3" fill="rgba(232,160,32,.12)" stroke="var(--amber)" stroke-width=".8"/>
        <text x="920" y="60" text-anchor="middle" fill="var(--amber)" font-family="Inter,sans-serif" font-size="7" font-weight="600">ALUMINUM SUBSTRATE</text>
        <rect x="810" y="33" width="220" height="14" rx="3" fill="rgba(46,196,182,.2)" stroke="var(--teal)" stroke-width=".8"/>
        <text x="920" y="43" text-anchor="middle" fill="var(--teal)" font-family="Inter,sans-serif" font-size="7" font-weight="600">IMMERSION ZINC LAYER (catalytic)</text>
        <text x="920" y="30" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="7" font-style="italic">Double zincate: strip first zinc &rarr; reapply for adhesion</text>
      </svg>
    </div>


    <!-- SUBSTRATE ACTIVATION ROUTING FLOWCHART -->
    <div class="glass" style="padding:10px 14px;">
      <h3 class="section-title" style="margin-bottom:4px;">Substrate-Specific Activation Routing <span class="sub">match the acid to the metal</span></h3>
      <svg viewBox="0 0 1100 160" width="100%" height="160" fill="none" xmlns="http://www.w3.org/2000/svg">
        <!-- Start node -->
        <rect x="10" y="55" width="110" height="40" rx="20" fill="rgba(232,160,32,.12)" stroke="var(--amber)" stroke-width="1.5"/>
        <text x="65" y="79" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="13">SUBSTRATE?</text>
        <!-- Branch arrows from start -->
        <line x1="120" y1="60" x2="175" y2="20" stroke="var(--teal)" stroke-width="1.2"/><polygon points="173,16 180,20 173,24" fill="var(--teal)"/>
        <line x1="120" y1="68" x2="175" y2="55" stroke="var(--amber)" stroke-width="1.2"/><polygon points="173,51 180,55 173,59" fill="var(--amber)"/>
        <line x1="120" y1="82" x2="175" y2="100" stroke="var(--coral)" stroke-width="1.2"/><polygon points="173,96 180,100 173,104" fill="var(--coral)"/>
        <line x1="120" y1="90" x2="175" y2="140" stroke="var(--emerald)" stroke-width="1.2"/><polygon points="173,136 180,140 173,144" fill="var(--emerald)"/>
        <!-- Row 1: Carbon Steel (teal) -->
        <rect x="180" y="5" width="120" height="28" rx="6" fill="rgba(46,196,182,.08)" stroke="var(--teal)" stroke-width="1"/>
        <text x="240" y="23" text-anchor="middle" fill="var(--teal)" font-family="Inter,sans-serif" font-size="8" font-weight="700">Carbon Steel</text>
        <line x1="300" y1="19" x2="340" y2="19" stroke="var(--teal)" stroke-width="1"/><polygon points="337,15 344,19 337,23" fill="var(--teal)"/>
        <rect x="345" y="5" width="155" height="28" rx="6" fill="rgba(46,196,182,.05)" stroke="var(--teal)" stroke-width=".8"/>
        <text x="422" y="23" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="7.5" font-weight="600">HCl 10&ndash;20% / 15&ndash;30s</text>
        <line x1="500" y1="19" x2="540" y2="19" stroke="var(--teal)" stroke-width="1"/><polygon points="537,15 544,19 537,23" fill="var(--teal)"/>
        <rect x="545" y="5" width="80" height="28" rx="6" fill="rgba(46,196,182,.05)" stroke="var(--teal)" stroke-width=".8"/>
        <text x="585" y="23" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="7.5" font-weight="600">Rinse</text>
        <line x1="625" y1="19" x2="665" y2="19" stroke="var(--teal)" stroke-width="1"/><polygon points="662,15 669,19 662,23" fill="var(--teal)"/>
        <rect x="670" y="5" width="90" height="28" rx="6" fill="rgba(46,196,182,.15)" stroke="var(--teal)" stroke-width="1.2"/>
        <text x="715" y="23" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-size="10" font-weight="800">EN BATH</text>
        <!-- Row 2: Stainless Steel (amber) -->
        <rect x="180" y="40" width="120" height="28" rx="6" fill="rgba(232,160,32,.08)" stroke="var(--amber)" stroke-width="1"/>
        <text x="240" y="58" text-anchor="middle" fill="var(--amber)" font-family="Inter,sans-serif" font-size="8" font-weight="700">Stainless Steel</text>
        <line x1="300" y1="54" x2="340" y2="54" stroke="var(--amber)" stroke-width="1"/><polygon points="337,50 344,54 337,58" fill="var(--amber)"/>
        <rect x="345" y="40" width="155" height="28" rx="6" fill="rgba(232,160,32,.05)" stroke="var(--amber)" stroke-width=".8"/>
        <text x="422" y="52" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="7" font-weight="600">HCl + HNO&#8323; or</text>
        <text x="422" y="62" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="7" font-weight="600">Wood&rsquo;s Strike</text>
        <line x1="500" y1="54" x2="540" y2="54" stroke="var(--amber)" stroke-width="1"/><polygon points="537,50 544,54 537,58" fill="var(--amber)"/>
        <rect x="545" y="40" width="80" height="28" rx="6" fill="rgba(232,160,32,.05)" stroke="var(--amber)" stroke-width=".8"/>
        <text x="585" y="58" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="7.5" font-weight="600">Rinse</text>
        <line x1="625" y1="54" x2="665" y2="54" stroke="var(--amber)" stroke-width="1"/><polygon points="662,50 669,54 662,58" fill="var(--amber)"/>
        <rect x="670" y="40" width="90" height="28" rx="6" fill="rgba(232,160,32,.15)" stroke="var(--amber)" stroke-width="1.2"/>
        <text x="715" y="58" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-size="10" font-weight="800">EN BATH</text>
        <!-- Row 3: Aluminum (coral) -->
        <rect x="180" y="85" width="120" height="28" rx="6" fill="rgba(224,92,92,.08)" stroke="var(--coral)" stroke-width="1"/>
        <text x="240" y="103" text-anchor="middle" fill="var(--coral)" font-family="Inter,sans-serif" font-size="8" font-weight="700">Aluminum</text>
        <line x1="300" y1="99" x2="340" y2="99" stroke="var(--coral)" stroke-width="1"/><polygon points="337,95 344,99 337,103" fill="var(--coral)"/>
        <rect x="345" y="85" width="90" height="28" rx="6" fill="rgba(224,92,92,.05)" stroke="var(--coral)" stroke-width=".8"/>
        <text x="390" y="103" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="7.5" font-weight="600">Zincate</text>
        <line x1="435" y1="99" x2="465" y2="99" stroke="var(--coral)" stroke-width="1"/><polygon points="462,95 469,99 462,103" fill="var(--coral)"/>
        <rect x="470" y="85" width="70" height="28" rx="6" fill="rgba(224,92,92,.05)" stroke="var(--coral)" stroke-width=".8"/>
        <text x="505" y="103" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="7.5" font-weight="600">Strip</text>
        <line x1="540" y1="99" x2="570" y2="99" stroke="var(--coral)" stroke-width="1"/><polygon points="567,95 574,99 567,103" fill="var(--coral)"/>
        <rect x="575" y="85" width="100" height="28" rx="6" fill="rgba(224,92,92,.05)" stroke="var(--coral)" stroke-width=".8"/>
        <text x="625" y="103" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="7.5" font-weight="600">Re-Zincate</text>
        <line x1="675" y1="99" x2="705" y2="99" stroke="var(--coral)" stroke-width="1"/><polygon points="702,95 709,99 702,103" fill="var(--coral)"/>
        <rect x="710" y="85" width="65" height="28" rx="6" fill="rgba(224,92,92,.05)" stroke="var(--coral)" stroke-width=".8"/>
        <text x="742" y="103" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="7.5" font-weight="600">Rinse</text>
        <line x1="775" y1="99" x2="805" y2="99" stroke="var(--coral)" stroke-width="1"/><polygon points="802,95 809,99 802,103" fill="var(--coral)"/>
        <rect x="810" y="85" width="90" height="28" rx="6" fill="rgba(224,92,92,.15)" stroke="var(--coral)" stroke-width="1.2"/>
        <text x="855" y="103" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-size="10" font-weight="800">EN BATH</text>
        <!-- Loop arrow label -->
        <text x="505" y="80" text-anchor="middle" fill="var(--coral)" font-family="Inter,sans-serif" font-size="6.5" font-style="italic" font-weight="600">double zincate loop</text>
        <!-- Row 4: Copper Alloy (emerald) -->
        <rect x="180" y="125" width="120" height="28" rx="6" fill="rgba(39,174,96,.08)" stroke="var(--emerald)" stroke-width="1"/>
        <text x="240" y="143" text-anchor="middle" fill="var(--emerald)" font-family="Inter,sans-serif" font-size="8" font-weight="700">Copper Alloy</text>
        <line x1="300" y1="139" x2="340" y2="139" stroke="var(--emerald)" stroke-width="1"/><polygon points="337,135 344,139 337,143" fill="var(--emerald)"/>
        <rect x="345" y="125" width="155" height="28" rx="6" fill="rgba(39,174,96,.05)" stroke="var(--emerald)" stroke-width=".8"/>
        <text x="422" y="143" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="7.5" font-weight="600">Mild acid dip (H&#8322;SO&#8324; 5%)</text>
        <line x1="500" y1="139" x2="540" y2="139" stroke="var(--emerald)" stroke-width="1"/><polygon points="537,135 544,139 537,143" fill="var(--emerald)"/>
        <rect x="545" y="125" width="80" height="28" rx="6" fill="rgba(39,174,96,.05)" stroke="var(--emerald)" stroke-width=".8"/>
        <text x="585" y="143" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="7.5" font-weight="600">Rinse</text>
        <line x1="625" y1="139" x2="665" y2="139" stroke="var(--emerald)" stroke-width="1"/><polygon points="662,135 669,139 662,143" fill="var(--emerald)"/>
        <rect x="670" y="125" width="90" height="28" rx="6" fill="rgba(39,174,96,.15)" stroke="var(--emerald)" stroke-width="1.2"/>
        <text x="715" y="143" text-anchor="middle" fill="var(--emerald)" font-family="Barlow Condensed,sans-serif" font-size="10" font-weight="800">EN BATH</text>
      </svg>
    </div>

    <div class="compare-grid">
      <div class="glass compare-card do" style="padding:8px 14px;">
        <h4 style="font-size:18px;margin-bottom:5px;">Proper Activation <span class="tag good">Result</span></h4>
        <ul>
          <li>Uniform matte-gray or bright surface after acid dip</li>
          <li>No rainbow tints, dark spots, or powder residue</li>
          <li>Part goes to rinse immediately &mdash; no air drying</li>
          <li>Excellent EN adhesion (&gt;35 MPa pull test typical)</li>
        </ul>
      </div>
      <div class="glass compare-card dont" style="padding:8px 14px;">
        <h4 style="font-size:18px;margin-bottom:5px;">Over-Activation / Wrong Acid <span class="tag bad">Failure</span></h4>
        <ul>
          <li>Excessive etching roughens surface &rarr; nodular EN deposit</li>
          <li>Flash rust on steel from delayed transfer &rarr; poor adhesion</li>
          <li>Wrong acid on Al (no zincate) &rarr; immediate oxide reform &rarr; peeling EN</li>
          <li>Extended acid time on high-strength steel &rarr; hydrogen embrittlement</li>
        </ul>
      </div>
    </div>

    <div class="insight-card">
      <div class="insight-label">The Double Zincate: Why It Matters for Aluminum</div>
      <div class="insight-text">Aluminum instantly reforms its oxide when exposed to air or water. A single zincate dip deposits a zinc layer over this oxide &mdash; and the EN plates on the zinc. But the bond is only as strong as the oxide beneath it. The double zincate process strips the first zinc layer (which lifts the original oxide with it), then re-applies zinc directly onto fresh aluminum. This produces adhesion values <strong>3&ndash;5&times; higher</strong> than single zincate. For any critical Al application, double zincate is mandatory.</div>
    </div>

    <div class="safety-card">
      <div class="safety-head">&#9888; Safety &mdash; Acid Activation</div>
      <div class="safety-body"><strong>Hydrochloric acid</strong>: corrosive, fuming at concentrations &gt;20%. HCl mist irritates lungs &mdash; TLV-C 2 ppm. <strong>Sulfuric acid</strong>: severely corrosive; exothermic when mixing with water (always add acid to water, never reverse). <strong>Nitric acid</strong>: strong oxidizer; reacts violently with organics; produces NO&#8322; fumes. <strong>Hydrofluoric acid</strong> (Al desmut): extremely dangerous &mdash; penetrates skin and binds calcium in blood; can be fatal even from small skin exposure. HF requires specialized first-aid (calcium gluconate gel). Full PPE including face shield, acid-resistant gloves, and chemical apron at all acid stations. OSHA PEL for HCl: 5 ppm ceiling. Emergency shower and eyewash within 10 seconds.</div>
    </div>
"""

TECH_BODY_ES["04"] = """
    <div class="glass rule-card">
      <div class="rule-num">03</div>
      <div class="rule-body">
        <div class="rule-label">Etapa 3 &mdash; Activaci&oacute;n &Aacute;cida</div>
        <div class="rule-text">La activaci&oacute;n &aacute;cida remueve la capa delgada de &oacute;xido que se forma en el sustrato despu&eacute;s de la limpieza. Esto expone metal fresco y catal&iacute;ticamente activo que inicia la reacci&oacute;n autocatal&iacute;tica del EN. La qu&iacute;mica de activaci&oacute;n debe coincidir con el sustrato: acero, aluminio y aleaciones de cobre requieren diferentes &aacute;cidos y procedimientos. Hacer mal la activaci&oacute;n es la causa #1 de fallas de adherencia en n&iacute;quel qu&iacute;mico.</div>
      </div>
    </div>

    <!-- TABLA DE QU&Iacute;MICA DE ACTIVACI&Oacute;N -->
    <div>
      <h3 class="section-title">Qu&iacute;mica de Activaci&oacute;n por Tipo de &Aacute;cido <span class="sub">opciones comunes</span></h3>
      <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
        <table class="data-table compact">
          <thead><tr><th>&Aacute;cido</th><th>Concentraci&oacute;n</th><th>Temp</th><th>Tiempo</th><th>Mejor Para</th></tr></thead>
          <tbody>
            <tr><td style="font-weight:600;color:var(--amber);">Clorh&iacute;drico (HCl)</td><td class="mono">10&ndash;20% v/v</td><td class="mono">Ambiente</td><td class="mono">30&ndash;60 s</td><td>Acero, acero inoxidable, aleaciones de hierro</td></tr>
            <tr><td style="font-weight:600;color:var(--amber);">Sulf&uacute;rico (H&#8322;SO&#8324;)</td><td class="mono">10&ndash;25% v/v</td><td class="mono">Ambiente</td><td class="mono">30&ndash;60 s</td><td>Acero (alternativa a HCl); menos vapores</td></tr>
            <tr><td style="font-weight:600;color:var(--amber);">N&iacute;trico (HNO&#8323;)</td><td class="mono">30&ndash;50% v/v</td><td class="mono">Ambiente</td><td class="mono">15&ndash;30 s</td><td>Inoxidable (romper pasivaci&oacute;n); aleaciones de cobre</td></tr>
            <tr><td style="font-weight:600;color:var(--amber);">Zincado (NaOH + ZnO)</td><td class="mono">Seg&uacute;n proveedor</td><td class="mono">21&ndash;27&deg;C</td><td class="mono">30&ndash;60 s</td><td>Aluminio y aleaciones de aluminio (capa de Zn por inmersi&oacute;n)</td></tr>
            <tr><td style="font-weight:600;color:var(--amber);">Fosf&oacute;rico (H&#8323;PO&#8324;)</td><td class="mono">5&ndash;15% v/v</td><td class="mono">Ambiente</td><td class="mono">30&ndash;60 s</td><td>Activaci&oacute;n suave; sustratos sensibles</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- GU&Iacute;A DE RUTA POR SUSTRATO -->
    <div>
      <h3 class="section-title">Gu&iacute;a de Ruta por Sustrato <span class="sub">qu&eacute; camino para cada metal</span></h3>
      <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
        <table class="data-table compact">
          <thead><tr><th>Sustrato</th><th>Secuencia de Activaci&oacute;n</th><th>Notas Cr&iacute;ticas</th></tr></thead>
          <tbody>
            <tr><td style="font-weight:600;">Acero al Carb&oacute;n</td><td>HCl 10&ndash;20% &rarr; Enjuague &rarr; Enjuague DI &rarr; EN</td><td>Ruta est&aacute;ndar; cuidado con &oacute;xido r&aacute;pido</td></tr>
            <tr><td style="font-weight:600;">Acero Inoxidable</td><td>HCl 20% o HNO&#8323; 30% &rarr; Enjuague &rarr; DI &rarr; EN (o strike Wood&rsquo;s Ni)</td><td>Debe romper capa pasiva de CrO; strike Wood&rsquo;s recomendado para serie 300</td></tr>
            <tr><td style="font-weight:600;">Aluminio (forjado)</td><td>Ataque NaOH &rarr; Enj. &rarr; Zincado &rarr; Decapar &rarr; Doble Zincado &rarr; Enj. &rarr; EN</td><td>Doble zincado es obligatorio para adherencia; zincado simple = riesgo de desprendimiento</td></tr>
            <tr><td style="font-weight:600;">Aluminio (fundici&oacute;n)</td><td>Ataque NaOH &rarr; Desmut (HNO&#8323;+HF) &rarr; Zincado &rarr; Decapar &rarr; Doble Zincado &rarr; EN</td><td>Fundiciones alto Si necesitan desmut con HF; precauci&oacute;n con &aacute;cido fumante</td></tr>
            <tr><td style="font-weight:600;">Cobre / Lat&oacute;n</td><td>H&#8322;SO&#8324; 10% o HCl 5&ndash;10% &rarr; Enjuague &rarr; EN</td><td>&Aacute;cido suave; evite sobre-ataque en sustratos delgados</td></tr>
            <tr><td style="font-weight:600;">Acero Alta Resistencia (&ge;40 HRC)</td><td>HCl 10% (m&aacute;x 120 s) &rarr; Enj. &rarr; EN &rarr; Alivio HE dentro de 4 hr</td><td>Minimice exposici&oacute;n &aacute;cida; riesgo de fragilizaci&oacute;n por H; horneado HE obligatorio seg&uacute;n ASTM B849</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- SVG MECANISMO DE ACTIVACI&Oacute;N -->
    <div class="glass" style="padding:10px 14px;">
      <h3 class="section-title" style="margin-bottom:4px;">Mecanismo de Activaci&oacute;n <span class="sub">remoci&oacute;n de &oacute;xido &rarr; superficie catal&iacute;tica</span></h3>
      <svg viewBox="0 0 1100 90" width="100%" height="90" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect x="30" y="5" width="320" height="80" rx="8" fill="rgba(224,92,92,.05)" stroke="var(--coral)" stroke-width="1"/>
        <text x="190" y="18" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11" letter-spacing=".06em">ANTES DE ACTIVACI&Oacute;N</text>
        <rect x="60" y="55" width="260" height="14" rx="3" fill="rgba(232,160,32,.12)" stroke="var(--amber)" stroke-width=".8"/>
        <text x="190" y="65" text-anchor="middle" fill="var(--amber)" font-family="Inter,sans-serif" font-size="7" font-weight="600">METAL BASE (Fe / Al / Cu)</text>
        <rect x="60" y="38" width="260" height="14" rx="3" fill="rgba(224,92,92,.2)" stroke="var(--coral)" stroke-width=".8"/>
        <text x="190" y="48" text-anchor="middle" fill="var(--coral)" font-family="Inter,sans-serif" font-size="7" font-weight="600">CAPA DE &Oacute;XIDO (pasiva, no catal&iacute;tica)</text>
        <text x="190" y="30" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="7" font-style="italic">EN no puede iniciar sobre &oacute;xido &mdash; sin actividad catal&iacute;tica</text>
        <line x1="360" y1="45" x2="420" y2="45" stroke="var(--amber)" stroke-width="2"/><polygon points="416,40 425,45 416,50" fill="var(--amber)"/>
        <text x="392" y="38" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="10">&Aacute;CIDO</text>
        <rect x="430" y="5" width="320" height="80" rx="8" fill="rgba(39,174,96,.05)" stroke="var(--emerald)" stroke-width="1"/>
        <text x="590" y="18" text-anchor="middle" fill="var(--emerald)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11" letter-spacing=".06em">DESPU&Eacute;S DE ACTIVACI&Oacute;N</text>
        <rect x="460" y="50" width="260" height="14" rx="3" fill="rgba(232,160,32,.12)" stroke="var(--amber)" stroke-width=".8"/>
        <text x="590" y="60" text-anchor="middle" fill="var(--amber)" font-family="Inter,sans-serif" font-size="7" font-weight="600">METAL LIMPIO (catal&iacute;ticamente activo)</text>
        <text x="590" y="30" text-anchor="middle" fill="var(--emerald)" font-family="Inter,sans-serif" font-size="7" font-weight="600">&Oacute;xido disuelto &rarr; superficie met&aacute;lica fresca expuesta</text>
        <text x="590" y="42" text-anchor="middle" fill="var(--emerald)" font-family="Inter,sans-serif" font-size="7">Superficie Fe/Ni/Cu cataliza reducci&oacute;n Ni&sup2;&#8314; por hipofosfito</text>
        <rect x="780" y="5" width="280" height="80" rx="8" fill="rgba(46,196,182,.05)" stroke="var(--teal)" stroke-width="1"/>
        <text x="920" y="18" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11" letter-spacing=".06em">RUTA ALUMINIO (ZINCADO)</text>
        <rect x="810" y="50" width="220" height="14" rx="3" fill="rgba(232,160,32,.12)" stroke="var(--amber)" stroke-width=".8"/>
        <text x="920" y="60" text-anchor="middle" fill="var(--amber)" font-family="Inter,sans-serif" font-size="7" font-weight="600">SUSTRATO DE ALUMINIO</text>
        <rect x="810" y="33" width="220" height="14" rx="3" fill="rgba(46,196,182,.2)" stroke="var(--teal)" stroke-width=".8"/>
        <text x="920" y="43" text-anchor="middle" fill="var(--teal)" font-family="Inter,sans-serif" font-size="7" font-weight="600">CAPA ZINC POR INMERSI&Oacute;N (catal&iacute;tica)</text>
        <text x="920" y="30" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="7" font-style="italic">Doble zincado: decape primer zinc &rarr; reaplicar para adherencia</text>
      </svg>
    </div>


    <!-- SVG RUTA DE ACTIVACI&Oacute;N POR SUSTRATO -->
    <div class="glass" style="padding:10px 14px;">
      <h3 class="section-title" style="margin-bottom:4px;">Ruta de Activaci&oacute;n por Tipo de Sustrato <span class="sub">el &aacute;cido correcto para cada metal</span></h3>
      <svg viewBox="0 0 1100 160" width="100%" height="160" fill="none" xmlns="http://www.w3.org/2000/svg">
        <!-- Start node -->
        <rect x="10" y="55" width="115" height="40" rx="20" fill="rgba(232,160,32,.12)" stroke="var(--amber)" stroke-width="1.5"/>
        <text x="67" y="79" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="12">SUSTRATO?</text>
        <!-- Branch arrows -->
        <line x1="125" y1="60" x2="175" y2="20" stroke="var(--teal)" stroke-width="1.2"/><polygon points="173,16 180,20 173,24" fill="var(--teal)"/>
        <line x1="125" y1="68" x2="175" y2="55" stroke="var(--amber)" stroke-width="1.2"/><polygon points="173,51 180,55 173,59" fill="var(--amber)"/>
        <line x1="125" y1="82" x2="175" y2="100" stroke="var(--coral)" stroke-width="1.2"/><polygon points="173,96 180,100 173,104" fill="var(--coral)"/>
        <line x1="125" y1="90" x2="175" y2="140" stroke="var(--emerald)" stroke-width="1.2"/><polygon points="173,136 180,140 173,144" fill="var(--emerald)"/>
        <!-- Row 1: Acero al Carbono (teal) -->
        <rect x="180" y="5" width="130" height="28" rx="6" fill="rgba(46,196,182,.08)" stroke="var(--teal)" stroke-width="1"/>
        <text x="245" y="23" text-anchor="middle" fill="var(--teal)" font-family="Inter,sans-serif" font-size="8" font-weight="700">Acero al Carbono</text>
        <line x1="310" y1="19" x2="340" y2="19" stroke="var(--teal)" stroke-width="1"/><polygon points="337,15 344,19 337,23" fill="var(--teal)"/>
        <rect x="345" y="5" width="155" height="28" rx="6" fill="rgba(46,196,182,.05)" stroke="var(--teal)" stroke-width=".8"/>
        <text x="422" y="23" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="7.5" font-weight="600">HCl 10&ndash;20% / 15&ndash;30s</text>
        <line x1="500" y1="19" x2="540" y2="19" stroke="var(--teal)" stroke-width="1"/><polygon points="537,15 544,19 537,23" fill="var(--teal)"/>
        <rect x="545" y="5" width="85" height="28" rx="6" fill="rgba(46,196,182,.05)" stroke="var(--teal)" stroke-width=".8"/>
        <text x="587" y="23" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="7.5" font-weight="600">Enjuague</text>
        <line x1="630" y1="19" x2="665" y2="19" stroke="var(--teal)" stroke-width="1"/><polygon points="662,15 669,19 662,23" fill="var(--teal)"/>
        <rect x="670" y="5" width="100" height="28" rx="6" fill="rgba(46,196,182,.15)" stroke="var(--teal)" stroke-width="1.2"/>
        <text x="720" y="23" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-size="10" font-weight="800">BA&Ntilde;O EN</text>
        <!-- Row 2: Acero Inoxidable (amber) -->
        <rect x="180" y="40" width="130" height="28" rx="6" fill="rgba(232,160,32,.08)" stroke="var(--amber)" stroke-width="1"/>
        <text x="245" y="58" text-anchor="middle" fill="var(--amber)" font-family="Inter,sans-serif" font-size="8" font-weight="700">Acero Inoxidable</text>
        <line x1="310" y1="54" x2="340" y2="54" stroke="var(--amber)" stroke-width="1"/><polygon points="337,50 344,54 337,58" fill="var(--amber)"/>
        <rect x="345" y="40" width="155" height="28" rx="6" fill="rgba(232,160,32,.05)" stroke="var(--amber)" stroke-width=".8"/>
        <text x="422" y="52" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="7" font-weight="600">HCl + HNO&#8323; o</text>
        <text x="422" y="62" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="7" font-weight="600">Strike de Wood</text>
        <line x1="500" y1="54" x2="540" y2="54" stroke="var(--amber)" stroke-width="1"/><polygon points="537,50 544,54 537,58" fill="var(--amber)"/>
        <rect x="545" y="40" width="85" height="28" rx="6" fill="rgba(232,160,32,.05)" stroke="var(--amber)" stroke-width=".8"/>
        <text x="587" y="58" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="7.5" font-weight="600">Enjuague</text>
        <line x1="630" y1="54" x2="665" y2="54" stroke="var(--amber)" stroke-width="1"/><polygon points="662,50 669,54 662,58" fill="var(--amber)"/>
        <rect x="670" y="40" width="100" height="28" rx="6" fill="rgba(232,160,32,.15)" stroke="var(--amber)" stroke-width="1.2"/>
        <text x="720" y="58" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-size="10" font-weight="800">BA&Ntilde;O EN</text>
        <!-- Row 3: Aluminio (coral) -->
        <rect x="180" y="85" width="130" height="28" rx="6" fill="rgba(224,92,92,.08)" stroke="var(--coral)" stroke-width="1"/>
        <text x="245" y="103" text-anchor="middle" fill="var(--coral)" font-family="Inter,sans-serif" font-size="8" font-weight="700">Aluminio</text>
        <line x1="310" y1="99" x2="340" y2="99" stroke="var(--coral)" stroke-width="1"/><polygon points="337,95 344,99 337,103" fill="var(--coral)"/>
        <rect x="345" y="85" width="90" height="28" rx="6" fill="rgba(224,92,92,.05)" stroke="var(--coral)" stroke-width=".8"/>
        <text x="390" y="103" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="7.5" font-weight="600">Zincado</text>
        <line x1="435" y1="99" x2="465" y2="99" stroke="var(--coral)" stroke-width="1"/><polygon points="462,95 469,99 462,103" fill="var(--coral)"/>
        <rect x="470" y="85" width="70" height="28" rx="6" fill="rgba(224,92,92,.05)" stroke="var(--coral)" stroke-width=".8"/>
        <text x="505" y="103" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="7.5" font-weight="600">Decape</text>
        <line x1="540" y1="99" x2="570" y2="99" stroke="var(--coral)" stroke-width="1"/><polygon points="567,95 574,99 567,103" fill="var(--coral)"/>
        <rect x="575" y="85" width="100" height="28" rx="6" fill="rgba(224,92,92,.05)" stroke="var(--coral)" stroke-width=".8"/>
        <text x="625" y="103" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="7.5" font-weight="600">Re-Zincado</text>
        <line x1="675" y1="99" x2="705" y2="99" stroke="var(--coral)" stroke-width="1"/><polygon points="702,95 709,99 702,103" fill="var(--coral)"/>
        <rect x="710" y="85" width="70" height="28" rx="6" fill="rgba(224,92,92,.05)" stroke="var(--coral)" stroke-width=".8"/>
        <text x="745" y="103" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="7.5" font-weight="600">Enjuague</text>
        <line x1="780" y1="99" x2="810" y2="99" stroke="var(--coral)" stroke-width="1"/><polygon points="807,95 814,99 807,103" fill="var(--coral)"/>
        <rect x="815" y="85" width="95" height="28" rx="6" fill="rgba(224,92,92,.15)" stroke="var(--coral)" stroke-width="1.2"/>
        <text x="862" y="103" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-size="10" font-weight="800">BA&Ntilde;O EN</text>
        <!-- Loop label -->
        <text x="505" y="80" text-anchor="middle" fill="var(--coral)" font-family="Inter,sans-serif" font-size="6.5" font-style="italic" font-weight="600">bucle doble zincado</text>
        <!-- Row 4: Aleaci&oacute;n de Cobre (emerald) -->
        <rect x="180" y="125" width="130" height="28" rx="6" fill="rgba(39,174,96,.08)" stroke="var(--emerald)" stroke-width="1"/>
        <text x="245" y="143" text-anchor="middle" fill="var(--emerald)" font-family="Inter,sans-serif" font-size="8" font-weight="700">Aleaci&oacute;n de Cobre</text>
        <line x1="310" y1="139" x2="340" y2="139" stroke="var(--emerald)" stroke-width="1"/><polygon points="337,135 344,139 337,143" fill="var(--emerald)"/>
        <rect x="345" y="125" width="155" height="28" rx="6" fill="rgba(39,174,96,.05)" stroke="var(--emerald)" stroke-width=".8"/>
        <text x="422" y="143" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="7.5" font-weight="600">&Aacute;cido suave (H&#8322;SO&#8324; 5%)</text>
        <line x1="500" y1="139" x2="540" y2="139" stroke="var(--emerald)" stroke-width="1"/><polygon points="537,135 544,139 537,143" fill="var(--emerald)"/>
        <rect x="545" y="125" width="85" height="28" rx="6" fill="rgba(39,174,96,.05)" stroke="var(--emerald)" stroke-width=".8"/>
        <text x="587" y="143" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="7.5" font-weight="600">Enjuague</text>
        <line x1="630" y1="139" x2="665" y2="139" stroke="var(--emerald)" stroke-width="1"/><polygon points="662,135 669,139 662,143" fill="var(--emerald)"/>
        <rect x="670" y="125" width="100" height="28" rx="6" fill="rgba(39,174,96,.15)" stroke="var(--emerald)" stroke-width="1.2"/>
        <text x="720" y="143" text-anchor="middle" fill="var(--emerald)" font-family="Barlow Condensed,sans-serif" font-size="10" font-weight="800">BA&Ntilde;O EN</text>
      </svg>
    </div>

    <div class="compare-grid">
      <div class="glass compare-card do" style="padding:8px 14px;">
        <h4 style="font-size:18px;margin-bottom:5px;">Activaci&oacute;n Correcta <span class="tag good">Resultado</span></h4>
        <ul>
          <li>Superficie uniforme gris mate o brillante despu&eacute;s del &aacute;cido</li>
          <li>Sin tintes arco&iacute;ris, manchas oscuras o residuo en polvo</li>
          <li>Pieza va al enjuague inmediatamente &mdash; sin secar al aire</li>
          <li>Excelente adherencia EN (&gt;35 MPa en prueba de tracci&oacute;n t&iacute;pico)</li>
        </ul>
      </div>
      <div class="glass compare-card dont" style="padding:8px 14px;">
        <h4 style="font-size:18px;margin-bottom:5px;">Sobre-Activaci&oacute;n / &Aacute;cido Incorrecto <span class="tag bad">Falla</span></h4>
        <ul>
          <li>Ataque excesivo vuelve rugosa la superficie &rarr; dep&oacute;sito EN nodular</li>
          <li>&Oacute;xido r&aacute;pido en acero por transferencia tard&iacute;a &rarr; mala adherencia</li>
          <li>&Aacute;cido incorrecto en Al (sin zincado) &rarr; &oacute;xido se reforma &rarr; EN se despega</li>
          <li>Tiempo prolongado en acero alta resistencia &rarr; fragilizaci&oacute;n por hidr&oacute;geno</li>
        </ul>
      </div>
    </div>

    <div class="insight-card">
      <div class="insight-label">El Doble Zincado: Por Qu&eacute; Importa para Aluminio</div>
      <div class="insight-text">El aluminio reforma instant&aacute;neamente su &oacute;xido cuando se expone al aire o agua. Un solo zincado deposita una capa de zinc sobre este &oacute;xido &mdash; y el EN se deposita sobre el zinc. Pero la uni&oacute;n es tan fuerte como el &oacute;xido debajo. El proceso de doble zincado decapa la primera capa de zinc (que levanta el &oacute;xido original con ella), luego re-aplica zinc directamente sobre aluminio fresco. Esto produce valores de adherencia <strong>3&ndash;5&times; mayores</strong> que el zincado simple. Para cualquier aplicaci&oacute;n cr&iacute;tica en Al, el doble zincado es obligatorio.</div>
    </div>

    <div class="safety-card">
      <div class="safety-head">&#9888; Seguridad &mdash; Activaci&oacute;n &Aacute;cida</div>
      <div class="safety-body"><strong>&Aacute;cido clorh&iacute;drico</strong>: corrosivo, emite vapores a concentraciones &gt;20%. Niebla de HCl irrita pulmones &mdash; TLV-C 2 ppm. <strong>&Aacute;cido sulf&uacute;rico</strong>: severamente corrosivo; exot&eacute;rmico al mezclar con agua (siempre agregue &aacute;cido al agua, nunca al rev&eacute;s). <strong>&Aacute;cido n&iacute;trico</strong>: oxidante fuerte; reacciona violentamente con org&aacute;nicos; produce vapores de NO&#8322;. <strong>&Aacute;cido fluorh&iacute;drico</strong> (desmut Al): extremadamente peligroso &mdash; penetra piel y enlaza calcio en sangre; puede ser fatal incluso por peque&ntilde;a exposici&oacute;n cut&aacute;nea. HF requiere primeros auxilios especializados (gel de gluconato de calcio). EPP completo incluyendo careta, guantes resistentes a &aacute;cido y mandil qu&iacute;mico en todas las estaciones de &aacute;cido. OSHA PEL para HCl: 5 ppm techo. Regadera y lavaojos a 10 segundos.</div>
    </div>
"""

SF_BODY_EN["04"] = """
    <div class="glass key-card">
      <div class="key-num">03</div>
      <div class="key-label">Stage 3 &mdash; Acid Activation</div>
      <div class="key-text">Acid removes the thin oxide layer from the part surface so the EN bath can start plating. The right acid for the right metal is critical. Wrong acid = wrong result. If your supervisor says HCl, use HCl. If they say zincate for aluminum, follow the full double zincate procedure.</div>
    </div>

    <!-- PARAMETERS -->
    <div class="glass" style="padding:10px 12px;">
      <div class="section-title">Activation Parameters</div>
      <table class="data-table compact">
        <thead><tr><th>Parameter</th><th>Steel (HCl)</th><th>Aluminum (Zincate)</th></tr></thead>
        <tbody>
          <tr><td>Acid Type</td><td class="mono">HCl 10&ndash;20% v/v</td><td>Zincate solution (per supplier)</td></tr>
          <tr><td>Temperature</td><td class="mono">Ambient</td><td class="mono">70&ndash;80&deg;F</td></tr>
          <tr><td>Time</td><td class="mono">30&ndash;60 sec</td><td class="mono">30&ndash;60 sec per dip</td></tr>
          <tr><td>Surface After</td><td>Uniform matte gray</td><td>Even zinc film, no bare spots</td></tr>
          <tr><td>Next Step</td><td>Rinse &rarr; DI Rinse &rarr; EN</td><td>Strip &rarr; Re-Zincate &rarr; Rinse &rarr; EN</td></tr>
        </tbody>
      </table>
    </div>

    <!-- KEY RULES -->
    <div class="glass numbered-list" style="padding:10px 14px;">
      <div class="section-title">Key Rules</div>
      <div style="display:flex;flex-direction:column;gap:6px;">
        <div class="list-item"><div class="num">1</div><div class="num-text"><strong>Right acid for the metal.</strong> Steel = HCl or H&#8322;SO&#8324;. Stainless = HCl or HNO&#8323;. Aluminum = zincate process. Copper = mild acid. Ask your supervisor if unsure.</div></div>
        <div class="list-item"><div class="num">2</div><div class="num-text"><strong>Do not over-activate.</strong> Stick to the time limits. More acid time &ne; better activation. Excessive acid etches the surface and causes rough EN deposit.</div></div>
        <div class="list-item"><div class="num">3</div><div class="num-text"><strong>Transfer immediately to rinse.</strong> Steel starts rusting within seconds of leaving the acid. Do not let parts air dry between acid and rinse.</div></div>
        <div class="list-item"><div class="num">4</div><div class="num-text"><strong>Aluminum gets double zincate.</strong> Dip in zincate, strip the zinc, then re-dip. Single zincate = peeling risk. This is not optional.</div></div>
        <div class="list-item"><div class="num">5</div><div class="num-text"><strong>High-strength steel: minimize acid time.</strong> Maximum 120 seconds. HE bake is mandatory within 4 hours of plating.</div></div>
      </div>
    </div>

    <div class="insight-card">
      <div class="insight-label">Over-Activation Is Worse Than Under-Activation</div>
      <div class="insight-text">A slightly under-activated part might plate slowly at first, then catch up. An over-activated part has a rough, pitted surface that produces a rough, nodular EN deposit with poor adhesion. When in doubt, start with the minimum time and increase only if needed. For high-strength steel parts, long acid exposure also causes hydrogen embrittlement, which can lead to cracking under load.</div>
    </div>

    <!-- DO / DON'T -->
    <div class="compare-row">
      <div class="compare-card glass do"><div class="compare-head good">&#10003; Do</div><ul class="compare-list"><li>Use the correct acid for the substrate</li><li>Follow time limits exactly</li><li>Transfer to rinse immediately after acid</li><li>Check surface appearance &mdash; uniform matte gray = good</li><li>Double zincate all aluminum parts</li></ul></div>
      <div class="compare-card glass dont"><div class="compare-head bad">&#10007; Don&rsquo;t</div><ul class="compare-list"><li>Leave parts in acid longer than specified</li><li>Let parts air dry between acid and rinse</li><li>Use HCl on aluminum (wrong acid!)</li><li>Mix acids without supervisor approval</li><li>Skip double zincate on aluminum</li></ul></div>
    </div>

    <div class="glass safety-card">
      <div class="section-title coral">&#9888; Safety &mdash; Acid Activation</div>
      <div class="safety-text"><strong>Mineral acids</strong> cause severe chemical burns on contact. <strong>HCl</strong> fumes at &gt;20% concentration &mdash; work with ventilation on. <strong>H&#8322;SO&#8324;</strong>: always add acid to water, never water to acid (violent exothermic reaction). <strong>HF</strong> (aluminum desmut): EXTREMELY DANGEROUS &mdash; penetrates skin, attacks bone. Even small exposure can be fatal. Requires calcium gluconate gel for first aid. Full PPE: face shield, acid-resistant gloves, chemical apron. Emergency shower and eyewash within 10 seconds. If contact: flush with water for 15+ minutes and seek immediate medical attention.</div>
    </div>
"""

SF_BODY_ES["04"] = """
    <div class="glass key-card">
      <div class="key-num">03</div>
      <div class="key-label">Etapa 3 &mdash; Activaci&oacute;n &Aacute;cida</div>
      <div class="key-text">El &aacute;cido remueve la capa delgada de &oacute;xido de la superficie para que el ba&ntilde;o EN pueda iniciar el dep&oacute;sito. El &aacute;cido correcto para el metal correcto es cr&iacute;tico. &Aacute;cido equivocado = resultado equivocado. Si su supervisor dice HCl, use HCl. Si dice zincado para aluminio, siga el procedimiento completo de doble zincado.</div>
    </div>

    <!-- PAR&Aacute;METROS -->
    <div class="glass" style="padding:10px 12px;">
      <div class="section-title">Par&aacute;metros de Activaci&oacute;n</div>
      <table class="data-table compact">
        <thead><tr><th>Par&aacute;metro</th><th>Acero (HCl)</th><th>Aluminio (Zincado)</th></tr></thead>
        <tbody>
          <tr><td>Tipo de &Aacute;cido</td><td class="mono">HCl 10&ndash;20% v/v</td><td>Soluci&oacute;n de zincado (seg&uacute;n proveedor)</td></tr>
          <tr><td>Temperatura</td><td class="mono">Ambiente</td><td class="mono">21&ndash;27&deg;C</td></tr>
          <tr><td>Tiempo</td><td class="mono">30&ndash;60 s</td><td class="mono">30&ndash;60 s por inmersi&oacute;n</td></tr>
          <tr><td>Superficie Despu&eacute;s</td><td>Gris mate uniforme</td><td>Pel&iacute;cula de zinc pareja, sin &aacute;reas desnudas</td></tr>
          <tr><td>Siguiente Paso</td><td>Enj. &rarr; Enj. DI &rarr; EN</td><td>Decapar &rarr; Re-Zincar &rarr; Enj. &rarr; EN</td></tr>
        </tbody>
      </table>
    </div>

    <!-- REGLAS CLAVE -->
    <div class="glass numbered-list" style="padding:10px 14px;">
      <div class="section-title">Reglas Clave</div>
      <div style="display:flex;flex-direction:column;gap:6px;">
        <div class="list-item"><div class="num">1</div><div class="num-text"><strong>&Aacute;cido correcto para el metal.</strong> Acero = HCl o H&#8322;SO&#8324;. Inoxidable = HCl o HNO&#8323;. Aluminio = proceso de zincado. Cobre = &aacute;cido suave. Pregunte a su supervisor si tiene duda.</div></div>
        <div class="list-item"><div class="num">2</div><div class="num-text"><strong>No sobre-active.</strong> Respete los l&iacute;mites de tiempo. M&aacute;s tiempo en &aacute;cido &ne; mejor activaci&oacute;n. El &aacute;cido excesivo ataca la superficie y causa dep&oacute;sito EN rugoso.</div></div>
        <div class="list-item"><div class="num">3</div><div class="num-text"><strong>Transfiera inmediatamente al enjuague.</strong> El acero comienza a oxidarse en segundos al salir del &aacute;cido. No deje secar las piezas entre &aacute;cido y enjuague.</div></div>
        <div class="list-item"><div class="num">4</div><div class="num-text"><strong>Aluminio recibe doble zincado.</strong> Sumerja en zincado, decape el zinc, luego re-sumerja. Zincado simple = riesgo de desprendimiento. Esto no es opcional.</div></div>
        <div class="list-item"><div class="num">5</div><div class="num-text"><strong>Acero alta resistencia: minimice tiempo en &aacute;cido.</strong> M&aacute;ximo 120 segundos. Horneado HE es obligatorio dentro de 4 horas del dep&oacute;sito.</div></div>
      </div>
    </div>

    <div class="insight-card">
      <div class="insight-label">La Sobre-Activaci&oacute;n Es Peor Que la Sub-Activaci&oacute;n</div>
      <div class="insight-text">Una pieza ligeramente sub-activada podr&iacute;a platear lentamente al inicio, luego recuperarse. Una pieza sobre-activada tiene una superficie rugosa y picada que produce un dep&oacute;sito EN rugoso y nodular con mala adherencia. Cuando tenga duda, comience con el tiempo m&iacute;nimo y aumente solo si es necesario. Para piezas de acero de alta resistencia, la exposici&oacute;n prolongada al &aacute;cido tambi&eacute;n causa fragilizaci&oacute;n por hidr&oacute;geno, que puede llevar a agrietamiento bajo carga.</div>
    </div>

    <!-- HAGA / NO HAGA -->
    <div class="compare-row">
      <div class="compare-card glass do"><div class="compare-head good">&#10003; Haga</div><ul class="compare-list"><li>Use el &aacute;cido correcto para el sustrato</li><li>Siga los l&iacute;mites de tiempo exactamente</li><li>Transfiera al enjuague inmediatamente despu&eacute;s del &aacute;cido</li><li>Revise la apariencia &mdash; gris mate uniforme = bien</li><li>Doble zincado en todas las piezas de aluminio</li></ul></div>
      <div class="compare-card glass dont"><div class="compare-head bad">&#10007; No Haga</div><ul class="compare-list"><li>Dejar piezas en &aacute;cido m&aacute;s del tiempo especificado</li><li>Dejar secar piezas al aire entre &aacute;cido y enjuague</li><li>Usar HCl en aluminio (&iexcl;&aacute;cido equivocado!)</li><li>Mezclar &aacute;cidos sin aprobaci&oacute;n del supervisor</li><li>Omitir doble zincado en aluminio</li></ul></div>
    </div>

    <div class="glass safety-card">
      <div class="section-title coral">&#9888; Seguridad &mdash; Activaci&oacute;n &Aacute;cida</div>
      <div class="safety-text"><strong>&Aacute;cidos minerales</strong> causan quemaduras qu&iacute;micas severas al contacto. <strong>HCl</strong> emite vapores a concentraci&oacute;n &gt;20% &mdash; trabaje con ventilaci&oacute;n encendida. <strong>H&#8322;SO&#8324;</strong>: siempre agregue &aacute;cido al agua, nunca agua al &aacute;cido (reacci&oacute;n exot&eacute;rmica violenta). <strong>HF</strong> (desmut aluminio): EXTREMADAMENTE PELIGROSO &mdash; penetra piel, ataca hueso. Incluso peque&ntilde;a exposici&oacute;n puede ser fatal. Requiere gel de gluconato de calcio para primeros auxilios. EPP completo: careta, guantes resistentes a &aacute;cido, mandil qu&iacute;mico. Regadera y lavaojos a 10 segundos. Si hay contacto: lave con agua por 15+ minutos y busque atenci&oacute;n m&eacute;dica inmediata.</div>
    </div>
"""

# =====================================================================
# POSTER 05 — CRITICAL RINSE
# =====================================================================
TECH_BODY_EN["05"] = """
    <div class="glass rule-card">
      <div class="rule-num">&lt;20</div>
      <div class="rule-body">
        <div class="rule-label">Conductivity &lt;20 &micro;S/cm &mdash; DI Water Mandatory</div>
        <div class="rule-text">The rinse between acid activation and the EN bath is the most critical rinse in the entire process. Any acid, chloride, or sulfate dragged into the EN bath destabilizes the autocatalytic reaction, accelerates stabilizer consumption, and can trigger spontaneous decomposition. This rinse must use deionized water and achieve &lt;20 &micro;S/cm before parts enter the EN bath. A failed critical rinse can cost an entire bath.</div>
      </div>
    </div>

    <!-- COUNTER-FLOW CASCADE SVG -->
    <div class="glass" style="padding:10px 14px;">
      <h3 class="section-title" style="margin-bottom:4px;">Counter-Flow Cascade Rinse Design <span class="sub">cleanest water contacts cleanest parts</span></h3>
      <svg viewBox="0 0 1100 140" width="100%" height="140" fill="none" xmlns="http://www.w3.org/2000/svg">
        <!-- Tank 1: Dirty -->
        <rect x="50" y="30" width="200" height="80" rx="8" fill="rgba(224,92,92,.08)" stroke="var(--coral)" stroke-width="1.4"/>
        <text x="150" y="22" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="12" letter-spacing=".06em">STAGE 1 (DIRTIEST)</text>
        <text x="150" y="55" text-anchor="middle" fill="var(--coral)" font-family="JetBrains Mono,monospace" font-size="11" font-weight="500">50&ndash;200 &micro;S/cm</text>
        <text x="150" y="75" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="8">Catches bulk acid drag-in</text>
        <text x="150" y="100" text-anchor="middle" fill="var(--faint)" font-family="Inter,sans-serif" font-size="7">Overflow to drain &darr;</text>
        <!-- Arrow water flow right to left -->
        <line x1="450" y1="120" x2="260" y2="120" stroke="var(--teal)" stroke-width="1.4" stroke-dasharray="4,3"/><polygon points="264,117 255,120 264,123" fill="var(--teal)"/>
        <text x="355" y="135" text-anchor="middle" fill="var(--teal)" font-family="Inter,sans-serif" font-size="7" font-weight="600">WATER FLOWS &larr; (counter to part movement)</text>
        <!-- Tank 2: Mid -->
        <rect x="300" y="30" width="200" height="80" rx="8" fill="rgba(232,160,32,.08)" stroke="var(--amber)" stroke-width="1.4"/>
        <text x="400" y="22" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="12" letter-spacing=".06em">STAGE 2 (MID)</text>
        <text x="400" y="55" text-anchor="middle" fill="var(--amber)" font-family="JetBrains Mono,monospace" font-size="11" font-weight="500">20&ndash;50 &micro;S/cm</text>
        <text x="400" y="75" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="8">Dilution stage</text>
        <!-- Tank 3: DI Final -->
        <rect x="550" y="30" width="200" height="80" rx="8" fill="rgba(46,196,182,.08)" stroke="var(--teal)" stroke-width="1.4"/>
        <text x="650" y="22" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="12" letter-spacing=".06em">STAGE 3 (DI FINAL)</text>
        <text x="650" y="55" text-anchor="middle" fill="var(--teal)" font-family="JetBrains Mono,monospace" font-size="11" font-weight="500">&lt;20 &micro;S/cm</text>
        <text x="650" y="75" text-anchor="middle" fill="var(--teal)" font-family="Inter,sans-serif" font-size="8" font-weight="600">DI water feed &rarr;</text>
        <!-- DI Feed arrow -->
        <line x1="790" y1="70" x2="755" y2="70" stroke="var(--teal)" stroke-width="1.4"/><polygon points="759,67 750,70 759,73" fill="var(--teal)"/>
        <text x="830" y="65" text-anchor="middle" fill="var(--teal)" font-family="JetBrains Mono,monospace" font-size="9" font-weight="500">DI</text>
        <text x="830" y="78" text-anchor="middle" fill="var(--teal)" font-family="JetBrains Mono,monospace" font-size="9" font-weight="500">FEED</text>
        <!-- Part movement arrows -->
        <line x1="100" y1="45" x2="295" y2="45" stroke="var(--amber)" stroke-width="1.2"/><polygon points="291,42 298,45 291,48" fill="var(--amber)"/>
        <line x1="350" y1="45" x2="545" y2="45" stroke="var(--amber)" stroke-width="1.2"/><polygon points="541,42 548,45 541,48" fill="var(--amber)"/>
        <line x1="600" y1="45" x2="780" y2="45" stroke="var(--amber)" stroke-width="1.2"/><polygon points="776,42 783,45 776,48" fill="var(--amber)"/>
        <text x="920" y="50" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11" letter-spacing=".04em">PARTS &rarr;</text>
        <text x="920" y="62" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11" letter-spacing=".04em">TO EN BATH</text>
      </svg>
    </div>

    <!-- CONTAMINATION THRESHOLDS TABLE -->
    <div>
      <h3 class="section-title">Contamination Thresholds &mdash; Critical Rinse Water <span class="sub">maximum allowable in final stage</span></h3>
      <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
        <table class="data-table compact">
          <thead><tr><th>Contaminant</th><th>Max Limit</th><th>Drag-In Source</th><th>Effect on EN Bath</th></tr></thead>
          <tbody>
            <tr><td style="font-weight:600;color:var(--coral);">Chloride (Cl&macr;)</td><td class="mono">&lt;5 ppm</td><td>HCl activation</td><td>Pitting; stabilizer interference; plate-out risk</td></tr>
            <tr><td style="font-weight:600;color:var(--coral);">Sulfate (SO&#8324;&sup2;&macr;)</td><td class="mono">&lt;10 ppm</td><td>H&#8322;SO&#8324; activation</td><td>Deposit stress; dull/dark deposits</td></tr>
            <tr><td style="font-weight:600;color:var(--coral);">Iron (Fe&sup2;&#8314;/Fe&sup3;&#8314;)</td><td class="mono">&lt;2 ppm</td><td>Steel dissolution in acid</td><td>Co-deposits; reduced corrosion resistance</td></tr>
            <tr><td style="font-weight:600;color:var(--coral);">Copper (Cu&sup2;&#8314;)</td><td class="mono">&lt;1 ppm</td><td>Brass/Cu substrate etch</td><td>Immersion copper on parts; catalyzes decomposition</td></tr>
            <tr><td style="font-weight:600;color:var(--coral);">Zinc (Zn&sup2;&#8314;)</td><td class="mono">&lt;2 ppm</td><td>Zincate activation for Al</td><td>Deposit brittleness; reduced phosphorus content</td></tr>
            <tr><td style="font-weight:600;color:var(--coral);">Conductivity</td><td class="mono">&lt;20 &micro;S/cm</td><td>All ionic carryover</td><td>Composite measure of total ionic contamination</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- DRAG-IN VOLUME CALCULATIONS -->
    <div class="bottom-grid">
      <div>
        <h3 class="section-title">Drag-In Volume Calculations <span class="sub">how much acid reaches the EN bath</span></h3>
        <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
          <table class="data-table compact">
            <thead><tr><th>Rinse Method</th><th>Dilution Ratio</th><th>Drag-In Reduction</th><th>Cl&macr; Reaching EN Bath</th></tr></thead>
            <tbody>
              <tr><td style="font-weight:600;">Single Still Rinse</td><td class="mono">1:100</td><td class="mono">99%</td><td class="mono">~500 ppm</td></tr>
              <tr><td style="font-weight:600;">Double Still Rinse</td><td class="mono">1:10,000</td><td class="mono">99.99%</td><td class="mono">~5 ppm</td></tr>
              <tr><td style="font-weight:600;color:var(--teal);">3-Stage Counter-Flow</td><td class="mono">1:1,000,000</td><td class="mono">99.9999%</td><td class="mono">&lt;0.05 ppm</td></tr>
              <tr><td style="font-weight:600;color:var(--teal);">3-Stage + DI Final</td><td class="mono">&gt;1:10,000,000</td><td class="mono">&gt;99.99999%</td><td class="mono">&lt;0.005 ppm</td></tr>
            </tbody>
          </table>
        </div>
        <div class="insight-card" style="margin-top:8px;">
          <div class="insight-label">Drag-In Math</div>
          <div class="insight-text">A typical rack carries 50&ndash;150 mL of drag-out film from the acid tank. In a single still rinse (30 L tank), this means ~5 mL/L acid concentration in the rinse water. Each additional counter-flow stage multiplies the dilution factor by the tank volume ratio. Three stages with DI feed reduce acid carryover by 7+ orders of magnitude &mdash; from harmful to negligible.</div>
        </div>
      </div>
      <div>
        <h3 class="section-title">Rinse Purity Requirements <span class="sub">operating parameters</span></h3>
        <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
          <table class="data-table bath">
            <thead><tr><th>Parameter</th><th>Requirement</th></tr></thead>
            <tbody>
              <tr><td style="font-weight:600;">Water Source</td><td>Deionized (DI) water &mdash; municipal water is NOT acceptable</td></tr>
              <tr><td style="font-weight:600;">Conductivity (final stage)</td><td class="mono">&lt;20 &micro;S/cm</td></tr>
              <tr><td style="font-weight:600;">pH (final stage)</td><td class="mono">5.5&ndash;7.5 (neutral)</td></tr>
              <tr><td style="font-weight:600;">Flow Rate</td><td class="mono">2&ndash;4 L/min per stage</td></tr>
              <tr><td style="font-weight:600;">Cascade Direction</td><td>Counter to part movement (cleanest water last)</td></tr>
              <tr><td style="font-weight:600;">Monitoring</td><td>Inline conductivity meter with alarm at 20 &micro;S/cm</td></tr>
              <tr><td style="font-weight:600;">Immersion Time</td><td class="mono">30&ndash;60 s per stage</td></tr>
              <tr><td style="font-weight:600;">Agitation</td><td>Air or part agitation recommended</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <div class="compare-grid">
      <div class="glass compare-card do" style="padding:8px 14px;">
        <h4 style="font-size:18px;margin-bottom:5px;">Effective Critical Rinse <span class="tag good">Result</span></h4>
        <ul>
          <li>Conductivity &lt;20 &micro;S/cm verified before each load enters EN</li>
          <li>DI water feed is continuous and validated daily</li>
          <li>Cascade flows counter to part direction</li>
          <li>Parts agitated during immersion &mdash; no stagnant zones</li>
        </ul>
      </div>
      <div class="glass compare-card dont" style="padding:8px 14px;">
        <h4 style="font-size:18px;margin-bottom:5px;">Failed Critical Rinse <span class="tag bad">Failure</span></h4>
        <ul>
          <li>Municipal tap water used instead of DI &rarr; Cl&macr;, Ca&sup2;&#8314; contamination</li>
          <li>Conductivity exceeds 50 &micro;S/cm &rarr; accelerated bath degradation</li>
          <li>Parts dragged through air too slowly &rarr; drying and salt crystallization</li>
          <li>Single still rinse with no overflow &rarr; acid builds up rapidly</li>
        </ul>
      </div>
    </div>

    <div class="safety-card">
      <div class="safety-head">&#9888; Safety &mdash; Critical Rinse</div>
      <div class="safety-body">Rinse water in this stage may contain residual <strong>mineral acid</strong> (HCl, H&#8322;SO&#8324;) from the activation step. pH can be 2&ndash;4 in first rinse stages. Treat as acidic until verified. Avoid splashing. Wear acid-resistant gloves and face protection. If acid splash contacts skin, flush immediately with water for 15+ minutes. Emergency shower and eyewash within 10 seconds. Dissolved nickel in downstream rinse water is a <strong>GHS Category 1A carcinogen</strong> &mdash; do not discharge without treatment.</div>
    </div>
"""

TECH_BODY_ES["05"] = """
    <div class="glass rule-card">
      <div class="rule-num">&lt;20</div>
      <div class="rule-body">
        <div class="rule-label">Conductividad &lt;20 &micro;S/cm &mdash; Agua DI Obligatoria</div>
        <div class="rule-text">El enjuague entre la activaci&oacute;n &aacute;cida y el ba&ntilde;o EN es el enjuague m&aacute;s cr&iacute;tico de todo el proceso. Cualquier &aacute;cido, cloruro o sulfato arrastrado al ba&ntilde;o EN desestabiliza la reacci&oacute;n autocatal&iacute;tica, acelera el consumo de estabilizador y puede provocar descomposici&oacute;n espont&aacute;nea. Este enjuague debe usar agua desionizada y alcanzar &lt;20 &micro;S/cm antes de que las piezas entren al ba&ntilde;o EN. Un enjuague cr&iacute;tico fallido puede costar un ba&ntilde;o completo.</div>
      </div>
    </div>

    <!-- SVG CASCADA CONTRA-FLUJO -->
    <div class="glass" style="padding:10px 14px;">
      <h3 class="section-title" style="margin-bottom:4px;">Dise&ntilde;o de Enjuague en Cascada Contra-Flujo <span class="sub">el agua m&aacute;s limpia toca las piezas m&aacute;s limpias</span></h3>
      <svg viewBox="0 0 1100 140" width="100%" height="140" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect x="50" y="30" width="200" height="80" rx="8" fill="rgba(224,92,92,.08)" stroke="var(--coral)" stroke-width="1.4"/>
        <text x="150" y="22" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="12" letter-spacing=".06em">ETAPA 1 (M&Aacute;S SUCIA)</text>
        <text x="150" y="55" text-anchor="middle" fill="var(--coral)" font-family="JetBrains Mono,monospace" font-size="11" font-weight="500">50&ndash;200 &micro;S/cm</text>
        <text x="150" y="75" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="8">Captura arrastre de &aacute;cido</text>
        <text x="150" y="100" text-anchor="middle" fill="var(--faint)" font-family="Inter,sans-serif" font-size="7">Rebose al drenaje &darr;</text>
        <line x1="450" y1="120" x2="260" y2="120" stroke="var(--teal)" stroke-width="1.4" stroke-dasharray="4,3"/><polygon points="264,117 255,120 264,123" fill="var(--teal)"/>
        <text x="355" y="135" text-anchor="middle" fill="var(--teal)" font-family="Inter,sans-serif" font-size="7" font-weight="600">AGUA FLUYE &larr; (contra el movimiento de piezas)</text>
        <rect x="300" y="30" width="200" height="80" rx="8" fill="rgba(232,160,32,.08)" stroke="var(--amber)" stroke-width="1.4"/>
        <text x="400" y="22" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="12" letter-spacing=".06em">ETAPA 2 (MEDIA)</text>
        <text x="400" y="55" text-anchor="middle" fill="var(--amber)" font-family="JetBrains Mono,monospace" font-size="11" font-weight="500">20&ndash;50 &micro;S/cm</text>
        <text x="400" y="75" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="8">Etapa de diluci&oacute;n</text>
        <rect x="550" y="30" width="200" height="80" rx="8" fill="rgba(46,196,182,.08)" stroke="var(--teal)" stroke-width="1.4"/>
        <text x="650" y="22" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="12" letter-spacing=".06em">ETAPA 3 (DI FINAL)</text>
        <text x="650" y="55" text-anchor="middle" fill="var(--teal)" font-family="JetBrains Mono,monospace" font-size="11" font-weight="500">&lt;20 &micro;S/cm</text>
        <text x="650" y="75" text-anchor="middle" fill="var(--teal)" font-family="Inter,sans-serif" font-size="8" font-weight="600">Alimentaci&oacute;n agua DI &rarr;</text>
        <line x1="790" y1="70" x2="755" y2="70" stroke="var(--teal)" stroke-width="1.4"/><polygon points="759,67 750,70 759,73" fill="var(--teal)"/>
        <text x="830" y="65" text-anchor="middle" fill="var(--teal)" font-family="JetBrains Mono,monospace" font-size="9" font-weight="500">DI</text>
        <text x="830" y="78" text-anchor="middle" fill="var(--teal)" font-family="JetBrains Mono,monospace" font-size="9" font-weight="500">ALIM.</text>
        <line x1="100" y1="45" x2="295" y2="45" stroke="var(--amber)" stroke-width="1.2"/><polygon points="291,42 298,45 291,48" fill="var(--amber)"/>
        <line x1="350" y1="45" x2="545" y2="45" stroke="var(--amber)" stroke-width="1.2"/><polygon points="541,42 548,45 541,48" fill="var(--amber)"/>
        <line x1="600" y1="45" x2="780" y2="45" stroke="var(--amber)" stroke-width="1.2"/><polygon points="776,42 783,45 776,48" fill="var(--amber)"/>
        <text x="920" y="50" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11" letter-spacing=".04em">PIEZAS &rarr;</text>
        <text x="920" y="62" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11" letter-spacing=".04em">AL BA&Ntilde;O EN</text>
      </svg>
    </div>

    <!-- TABLA UMBRALES DE CONTAMINACI&Oacute;N -->
    <div>
      <h3 class="section-title">Umbrales de Contaminaci&oacute;n &mdash; Agua de Enjuague Cr&iacute;tico <span class="sub">m&aacute;ximo permitido en etapa final</span></h3>
      <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
        <table class="data-table compact">
          <thead><tr><th>Contaminante</th><th>L&iacute;mite M&aacute;x</th><th>Fuente de Arrastre</th><th>Efecto en Ba&ntilde;o EN</th></tr></thead>
          <tbody>
            <tr><td style="font-weight:600;color:var(--coral);">Cloruro (Cl&macr;)</td><td class="mono">&lt;5 ppm</td><td>Activaci&oacute;n con HCl</td><td>Picaduras; interferencia estabilizador; riesgo de plate-out</td></tr>
            <tr><td style="font-weight:600;color:var(--coral);">Sulfato (SO&#8324;&sup2;&macr;)</td><td class="mono">&lt;10 ppm</td><td>Activaci&oacute;n con H&#8322;SO&#8324;</td><td>Estr&eacute;s en dep&oacute;sito; dep&oacute;sitos opacos/oscuros</td></tr>
            <tr><td style="font-weight:600;color:var(--coral);">Hierro (Fe&sup2;&#8314;/Fe&sup3;&#8314;)</td><td class="mono">&lt;2 ppm</td><td>Disoluci&oacute;n de acero en &aacute;cido</td><td>Co-deposita; reduce resistencia a corrosi&oacute;n</td></tr>
            <tr><td style="font-weight:600;color:var(--coral);">Cobre (Cu&sup2;&#8314;)</td><td class="mono">&lt;1 ppm</td><td>Ataque de sustrato lat&oacute;n/Cu</td><td>Cobre por inmersi&oacute;n en piezas; cataliza descomposici&oacute;n</td></tr>
            <tr><td style="font-weight:600;color:var(--coral);">Zinc (Zn&sup2;&#8314;)</td><td class="mono">&lt;2 ppm</td><td>Activaci&oacute;n por zincado para Al</td><td>Fragilidad del dep&oacute;sito; menor contenido de f&oacute;sforo</td></tr>
            <tr><td style="font-weight:600;color:var(--coral);">Conductividad</td><td class="mono">&lt;20 &micro;S/cm</td><td>Todo arrastre i&oacute;nico</td><td>Medida compuesta de contaminaci&oacute;n i&oacute;nica total</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- C&Aacute;LCULOS DE VOLUMEN DE ARRASTRE -->
    <div class="bottom-grid">
      <div>
        <h3 class="section-title">C&aacute;lculos de Volumen de Arrastre <span class="sub">cu&aacute;nto &aacute;cido llega al ba&ntilde;o EN</span></h3>
        <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
          <table class="data-table compact">
            <thead><tr><th>M&eacute;todo de Enjuague</th><th>Raz&oacute;n de Diluci&oacute;n</th><th>Reducci&oacute;n</th><th>Cl&macr; al Ba&ntilde;o EN</th></tr></thead>
            <tbody>
              <tr><td style="font-weight:600;">Enjuague Est&aacute;tico Simple</td><td class="mono">1:100</td><td class="mono">99%</td><td class="mono">~500 ppm</td></tr>
              <tr><td style="font-weight:600;">Enjuague Est&aacute;tico Doble</td><td class="mono">1:10,000</td><td class="mono">99.99%</td><td class="mono">~5 ppm</td></tr>
              <tr><td style="font-weight:600;color:var(--teal);">Cascada 3 Etapas</td><td class="mono">1:1,000,000</td><td class="mono">99.9999%</td><td class="mono">&lt;0.05 ppm</td></tr>
              <tr><td style="font-weight:600;color:var(--teal);">3 Etapas + DI Final</td><td class="mono">&gt;1:10,000,000</td><td class="mono">&gt;99.99999%</td><td class="mono">&lt;0.005 ppm</td></tr>
            </tbody>
          </table>
        </div>
        <div class="insight-card" style="margin-top:8px;">
          <div class="insight-label">Matem&aacute;ticas del Arrastre</div>
          <div class="insight-text">Un rack t&iacute;pico lleva 50&ndash;150 mL de pel&iacute;cula de arrastre del tanque de &aacute;cido. En un enjuague est&aacute;tico simple (30 L), esto significa ~5 mL/L de concentraci&oacute;n de &aacute;cido. Cada etapa adicional de contra-flujo multiplica el factor de diluci&oacute;n por la raz&oacute;n de volumen del tanque. Tres etapas con alimentaci&oacute;n DI reducen el arrastre de &aacute;cido por 7+ &oacute;rdenes de magnitud.</div>
        </div>
      </div>
      <div>
        <h3 class="section-title">Requisitos de Pureza del Enjuague <span class="sub">par&aacute;metros operativos</span></h3>
        <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
          <table class="data-table bath">
            <thead><tr><th>Par&aacute;metro</th><th>Requisito</th></tr></thead>
            <tbody>
              <tr><td style="font-weight:600;">Fuente de Agua</td><td>Agua desionizada (DI) &mdash; agua municipal NO es aceptable</td></tr>
              <tr><td style="font-weight:600;">Conductividad (etapa final)</td><td class="mono">&lt;20 &micro;S/cm</td></tr>
              <tr><td style="font-weight:600;">pH (etapa final)</td><td class="mono">5.5&ndash;7.5 (neutro)</td></tr>
              <tr><td style="font-weight:600;">Flujo</td><td class="mono">2&ndash;4 L/min por etapa</td></tr>
              <tr><td style="font-weight:600;">Direcci&oacute;n de Cascada</td><td>Contra el movimiento de piezas (agua m&aacute;s limpia al final)</td></tr>
              <tr><td style="font-weight:600;">Monitoreo</td><td>Conduct&iacute;metro en l&iacute;nea con alarma a 20 &micro;S/cm</td></tr>
              <tr><td style="font-weight:600;">Tiempo de Inmersi&oacute;n</td><td class="mono">30&ndash;60 s por etapa</td></tr>
              <tr><td style="font-weight:600;">Agitaci&oacute;n</td><td>Agitaci&oacute;n por aire o movimiento de piezas recomendada</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <div class="compare-grid">
      <div class="glass compare-card do" style="padding:8px 14px;">
        <h4 style="font-size:18px;margin-bottom:5px;">Enjuague Cr&iacute;tico Efectivo <span class="tag good">Resultado</span></h4>
        <ul>
          <li>Conductividad &lt;20 &micro;S/cm verificada antes de cada carga al EN</li>
          <li>Alimentaci&oacute;n de agua DI continua y validada diariamente</li>
          <li>Cascada fluye en contra de la direcci&oacute;n de las piezas</li>
          <li>Piezas agitadas durante inmersi&oacute;n &mdash; sin zonas estancadas</li>
        </ul>
      </div>
      <div class="glass compare-card dont" style="padding:8px 14px;">
        <h4 style="font-size:18px;margin-bottom:5px;">Enjuague Cr&iacute;tico Fallido <span class="tag bad">Falla</span></h4>
        <ul>
          <li>Agua de grifo municipal usada en vez de DI &rarr; contaminaci&oacute;n Cl&macr;, Ca&sup2;&#8314;</li>
          <li>Conductividad excede 50 &micro;S/cm &rarr; degradaci&oacute;n acelerada del ba&ntilde;o</li>
          <li>Piezas arrastradas por aire muy lento &rarr; secado y cristalizaci&oacute;n de sales</li>
          <li>Enjuague est&aacute;tico simple sin rebose &rarr; &aacute;cido se acumula r&aacute;pidamente</li>
        </ul>
      </div>
    </div>

    <div class="safety-card">
      <div class="safety-head">&#9888; Seguridad &mdash; Enjuague Cr&iacute;tico</div>
      <div class="safety-body">El agua de enjuague en esta etapa puede contener <strong>&aacute;cido mineral</strong> residual (HCl, H&#8322;SO&#8324;) del paso de activaci&oacute;n. El pH puede ser 2&ndash;4 en las primeras etapas de enjuague. Trate como &aacute;cido hasta verificar. Evite salpicaduras. Use guantes resistentes a &aacute;cido y protecci&oacute;n facial. Si salpica &aacute;cido en la piel, lave inmediatamente con agua por 15+ minutos. Regadera y lavaojos a 10 segundos. N&iacute;quel disuelto en agua de enjuague aguas abajo es <strong>carcin&oacute;geno GHS Categor&iacute;a 1A</strong> &mdash; no descargue sin tratamiento.</div>
    </div>
"""

SF_BODY_EN["05"] = """
    <div class="glass key-card">
      <div class="key-num">&lt;20</div>
      <div class="key-label">Conductivity &lt;20 &micro;S/cm &mdash; DI Water Only</div>
      <div class="key-text">This rinse protects the EN bath from acid drag-in. Any chloride or sulfate carried over from activation will destabilize the bath and can cause decomposition. Use DI water only. Check conductivity before every load. If over 20 &micro;S/cm, do NOT send parts to the EN bath.</div>
    </div>

    <div class="glass" style="padding:10px 12px;">
      <div class="section-title">Rinse Parameters</div>
      <table class="flow-table">
        <thead><tr><th>Parameter</th><th>Requirement</th></tr></thead>
        <tbody>
          <tr><td>Water Source</td><td class="mono">DI water only &mdash; no tap water</td></tr>
          <tr><td>Conductivity (final stage)</td><td class="mono">&lt;20 &micro;S/cm</td></tr>
          <tr><td>Cascade Stages</td><td class="mono">3 stages minimum (counter-flow)</td></tr>
          <tr><td>Immersion Time</td><td class="mono">30&ndash;60 sec per stage</td></tr>
          <tr><td>Agitation</td><td class="mono">Air or part movement</td></tr>
          <tr><td>Flow Direction</td><td>Counter to part movement (cleanest water last)</td></tr>
        </tbody>
      </table>
    </div>

    <div class="glass" style="padding:10px 12px;">
      <div class="section-title">Key Rules <span style="font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:.10em;color:var(--muted);margin-left:8px;">FOLLOW EVERY LOAD</span></div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;">
        <div style="padding:8px 10px;border-radius:8px;background:rgba(46,196,182,.08);border:1px solid rgba(46,196,182,.2);"><div style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:13px;color:var(--teal);letter-spacing:.04em;margin-bottom:3px;">CHECK CONDUCTIVITY</div><div style="font-size:10.5px;color:var(--muted);line-height:1.35;">Must be &lt;20 &micro;S/cm in the final stage before parts enter the EN bath. If high, increase DI flow or replace water.</div></div>
        <div style="padding:8px 10px;border-radius:8px;background:rgba(232,160,32,.08);border:1px solid rgba(232,160,32,.2);"><div style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:13px;color:var(--amber);letter-spacing:.04em;margin-bottom:3px;">TRANSFER QUICKLY</div><div style="font-size:10.5px;color:var(--muted);line-height:1.35;">Move parts from acid to rinse immediately. Never let parts dry between acid and rinse &mdash; salts crystallize on the surface.</div></div>
        <div style="padding:8px 10px;border-radius:8px;background:rgba(224,92,92,.08);border:1px solid rgba(224,92,92,.2);"><div style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:13px;color:var(--coral);letter-spacing:.04em;margin-bottom:3px;">NO TAP WATER</div><div style="font-size:10.5px;color:var(--muted);line-height:1.35;">Municipal water contains chloride, calcium, and other ions that contaminate the EN bath. DI water only in the final rinse stage.</div></div>
        <div style="padding:8px 10px;border-radius:8px;background:rgba(39,174,96,.08);border:1px solid rgba(39,174,96,.2);"><div style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:13px;color:var(--emerald);letter-spacing:.04em;margin-bottom:3px;">AGITATE PARTS</div><div style="font-size:10.5px;color:var(--muted);line-height:1.35;">Move parts up and down in each stage. Stagnant rinse leaves contamination in recesses and blind holes.</div></div>
      </div>
    </div>

    <div class="compare-row">
      <div class="compare-card glass do"><div class="compare-head good">&#10003; Do</div><ul class="compare-list"><li>Verify conductivity &lt;20 &micro;S/cm before every load</li><li>Use DI water in final rinse stage</li><li>Agitate parts in every rinse tank</li><li>Report if conductivity alarm triggers</li><li>Transfer from acid to rinse within seconds</li></ul></div>
      <div class="compare-card glass dont"><div class="compare-head bad">&#10007; Don&rsquo;t</div><ul class="compare-list"><li>Use tap water in any critical rinse stage</li><li>Skip conductivity checks &mdash; the EN bath pays the price</li><li>Let parts air-dry between acid and rinse</li><li>Bypass the cascade and go straight to the EN bath</li><li>Ignore rising conductivity readings</li></ul></div>
    </div>

    <div class="glass safety-card">
      <div class="section-title coral">&#9888; Safety &mdash; Critical Rinse</div>
      <div class="safety-text">Rinse water may contain residual <strong>mineral acid</strong> from the activation step. pH can be 2&ndash;4 in the first stages. Treat as acidic until verified. Wear acid-resistant gloves and face protection. If acid splash contacts skin, flush with water for 15+ minutes. Emergency shower and eyewash within 10 seconds.</div>
    </div>
"""

SF_BODY_ES["05"] = """
    <div class="glass key-card">
      <div class="key-num">&lt;20</div>
      <div class="key-label">Conductividad &lt;20 &micro;S/cm &mdash; Solo Agua DI</div>
      <div class="key-text">Este enjuague protege al ba&ntilde;o EN del arrastre de &aacute;cido. Cualquier cloruro o sulfato arrastrado de la activaci&oacute;n desestabilizar&aacute; el ba&ntilde;o y puede causar descomposici&oacute;n. Use solo agua DI. Verifique conductividad antes de cada carga. Si est&aacute; por encima de 20 &micro;S/cm, NO env&iacute;e piezas al ba&ntilde;o EN.</div>
    </div>

    <div class="glass" style="padding:10px 12px;">
      <div class="section-title">Par&aacute;metros de Enjuague</div>
      <table class="flow-table">
        <thead><tr><th>Par&aacute;metro</th><th>Requisito</th></tr></thead>
        <tbody>
          <tr><td>Fuente de Agua</td><td class="mono">Solo agua DI &mdash; sin agua de grifo</td></tr>
          <tr><td>Conductividad (etapa final)</td><td class="mono">&lt;20 &micro;S/cm</td></tr>
          <tr><td>Etapas de Cascada</td><td class="mono">3 etapas m&iacute;nimo (contra-flujo)</td></tr>
          <tr><td>Tiempo de Inmersi&oacute;n</td><td class="mono">30&ndash;60 s por etapa</td></tr>
          <tr><td>Agitaci&oacute;n</td><td class="mono">Aire o movimiento de piezas</td></tr>
          <tr><td>Direcci&oacute;n de Flujo</td><td>Contra el movimiento de piezas (agua m&aacute;s limpia al final)</td></tr>
        </tbody>
      </table>
    </div>

    <div class="glass" style="padding:10px 12px;">
      <div class="section-title">Reglas Clave <span style="font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:.10em;color:var(--muted);margin-left:8px;">SIGA EN CADA CARGA</span></div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;">
        <div style="padding:8px 10px;border-radius:8px;background:rgba(46,196,182,.08);border:1px solid rgba(46,196,182,.2);"><div style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:13px;color:var(--teal);letter-spacing:.04em;margin-bottom:3px;">VERIFIQUE CONDUCTIVIDAD</div><div style="font-size:10.5px;color:var(--muted);line-height:1.35;">Debe ser &lt;20 &micro;S/cm en la etapa final antes de que las piezas entren al ba&ntilde;o EN. Si est&aacute; alta, aumente flujo DI o reemplace el agua.</div></div>
        <div style="padding:8px 10px;border-radius:8px;background:rgba(232,160,32,.08);border:1px solid rgba(232,160,32,.2);"><div style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:13px;color:var(--amber);letter-spacing:.04em;margin-bottom:3px;">TRANSFIERA R&Aacute;PIDO</div><div style="font-size:10.5px;color:var(--muted);line-height:1.35;">Mueva piezas del &aacute;cido al enjuague inmediatamente. Nunca deje secar las piezas entre &aacute;cido y enjuague &mdash; las sales cristalizan en la superficie.</div></div>
        <div style="padding:8px 10px;border-radius:8px;background:rgba(224,92,92,.08);border:1px solid rgba(224,92,92,.2);"><div style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:13px;color:var(--coral);letter-spacing:.04em;margin-bottom:3px;">SIN AGUA DE GRIFO</div><div style="font-size:10.5px;color:var(--muted);line-height:1.35;">El agua municipal contiene cloruro, calcio y otros iones que contaminan el ba&ntilde;o EN. Solo agua DI en la etapa final de enjuague.</div></div>
        <div style="padding:8px 10px;border-radius:8px;background:rgba(39,174,96,.08);border:1px solid rgba(39,174,96,.2);"><div style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:13px;color:var(--emerald);letter-spacing:.04em;margin-bottom:3px;">AGITE LAS PIEZAS</div><div style="font-size:10.5px;color:var(--muted);line-height:1.35;">Mueva las piezas arriba y abajo en cada etapa. El enjuague estancado deja contaminaci&oacute;n en cavidades y agujeros ciegos.</div></div>
      </div>
    </div>

    <div class="compare-row">
      <div class="compare-card glass do"><div class="compare-head good">&#10003; Haga</div><ul class="compare-list"><li>Verifique conductividad &lt;20 &micro;S/cm antes de cada carga</li><li>Use agua DI en la etapa final de enjuague</li><li>Agite las piezas en cada tanque de enjuague</li><li>Reporte si la alarma de conductividad se activa</li><li>Transfiera del &aacute;cido al enjuague en segundos</li></ul></div>
      <div class="compare-card glass dont"><div class="compare-head bad">&#10007; No Haga</div><ul class="compare-list"><li>Usar agua de grifo en ninguna etapa de enjuague cr&iacute;tico</li><li>Omitir verificaciones de conductividad &mdash; el ba&ntilde;o EN paga el precio</li><li>Dejar secar piezas al aire entre &aacute;cido y enjuague</li><li>Saltarse la cascada e ir directo al ba&ntilde;o EN</li><li>Ignorar lecturas de conductividad en aumento</li></ul></div>
    </div>

    <div class="glass safety-card">
      <div class="section-title coral">&#9888; Seguridad &mdash; Enjuague Cr&iacute;tico</div>
      <div class="safety-text">El agua de enjuague puede contener <strong>&aacute;cido mineral</strong> residual del paso de activaci&oacute;n. El pH puede ser 2&ndash;4 en las primeras etapas. Trate como &aacute;cido hasta verificar. Use guantes resistentes a &aacute;cido y protecci&oacute;n facial. Si salpica &aacute;cido en la piel, lave con agua por 15+ minutos. Regadera y lavaojos a 10 segundos.</div>
    </div>
"""

# =====================================================================
# POSTER 06 — EN BATH
# =====================================================================
TECH_BODY_EN["06"] = """
    <div class="glass rule-card">
      <div class="rule-num">85&ndash;91&deg;C</div>
      <div class="rule-body">
        <div class="rule-label">Stage 5 &mdash; The EN High Phos Bath</div>
        <div class="rule-text">The heart of the process. Nickel ions are reduced by sodium hypophosphite onto a catalytic surface without external current. The reaction is autocatalytic &mdash; once initiated on a clean surface, the deposit itself catalyzes further deposition. Temperature, pH, nickel concentration, and reducer ratio must all stay within tight windows or the bath can lose rate, produce defects, or decompose catastrophically.</div>
      </div>
    </div>

    <!-- AUTOCATALYTIC REACTION MECHANISM SVG -->
    <div class="glass" style="padding:10px 14px;">
      <h3 class="section-title" style="margin-bottom:4px;">Autocatalytic Reaction Mechanism <span class="sub">simplified</span></h3>
      <svg viewBox="0 0 1100 90" width="100%" height="90" fill="none" xmlns="http://www.w3.org/2000/svg">
        <!-- Reactants -->
        <rect x="30" y="10" width="320" height="70" rx="8" fill="rgba(232,160,32,.06)" stroke="var(--amber)" stroke-width="1"/>
        <text x="190" y="25" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11" letter-spacing=".06em">REACTANTS (IN SOLUTION)</text>
        <text x="190" y="45" text-anchor="middle" fill="var(--text)" font-family="JetBrains Mono,monospace" font-size="13" font-weight="500">Ni&sup2;&#8314; + H&#8322;PO&#8322;&macr; + H&#8322;O</text>
        <text x="190" y="62" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="8">Nickel sulfate + sodium hypophosphite</text>
        <text x="190" y="73" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="8">pH 4.2&ndash;4.8 &bull; 85&ndash;91&deg;C &bull; catalytic surface required</text>
        <!-- Arrow -->
        <line x1="360" y1="45" x2="430" y2="45" stroke="var(--amber)" stroke-width="2"/><polygon points="426,40 435,45 426,50" fill="var(--amber)"/>
        <text x="395" y="38" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="10">CATALYTIC</text>
        <text x="395" y="58" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="10">SURFACE</text>
        <!-- Products -->
        <rect x="440" y="10" width="350" height="70" rx="8" fill="rgba(46,196,182,.06)" stroke="var(--teal)" stroke-width="1"/>
        <text x="615" y="25" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11" letter-spacing=".06em">PRODUCTS (DEPOSITED + GAS)</text>
        <text x="615" y="45" text-anchor="middle" fill="var(--text)" font-family="JetBrains Mono,monospace" font-size="13" font-weight="500">Ni&deg; + P + H&#8322;&uarr; + H&#8314; + HPO&#8323;&sup2;&macr;</text>
        <text x="615" y="62" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="8">Ni-P alloy deposit + hydrogen gas + orthophosphite byproduct</text>
        <text x="615" y="73" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="8">10&ndash;13% P co-deposited &bull; 8&ndash;15 &micro;m/hr &bull; pH drops (acid generated)</text>
        <!-- Feedback loop -->
        <rect x="830" y="10" width="230" height="70" rx="8" fill="rgba(224,92,92,.06)" stroke="var(--coral)" stroke-width="1"/>
        <text x="945" y="25" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11" letter-spacing=".06em">BYPRODUCT BUILDUP</text>
        <text x="945" y="42" text-anchor="middle" fill="var(--text)" font-family="JetBrains Mono,monospace" font-size="11" font-weight="500">HPO&#8323;&sup2;&macr; accumulates</text>
        <text x="945" y="57" text-anchor="middle" fill="var(--coral)" font-family="Inter,sans-serif" font-size="8" font-weight="600">Slows rate at high MTO</text>
        <text x="945" y="70" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="8">Bath life: 5&ndash;7 MTO typical</text>
      </svg>
    </div>

    <!-- OPERATING PARAMETERS TABLE -->
    <div>
      <h3 class="section-title">Operating Parameters <span class="sub">EN high phos bath</span></h3>
      <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
        <table class="data-table compact">
          <thead><tr><th>Parameter</th><th>Range</th><th>Target</th><th>Effect of Deviation</th></tr></thead>
          <tbody>
            <tr><td style="font-weight:600;">Temperature</td><td class="mono">85&ndash;91&deg;C (185&ndash;196&deg;F)</td><td class="mono">88&deg;C</td><td>Low: slow rate. High: decomposition risk</td></tr>
            <tr><td style="font-weight:600;">pH</td><td class="mono">4.2&ndash;4.8</td><td class="mono">4.5</td><td>Low: slow rate, high P%. High: fast rate, low P%, roughness</td></tr>
            <tr><td style="font-weight:600;">Nickel (Ni&sup2;&#8314;)</td><td class="mono">4.5&ndash;6.5 g/L</td><td class="mono">5.5 g/L</td><td>Low: slow rate. High: low P%, possible decomposition</td></tr>
            <tr><td style="font-weight:600;">Hypophosphite (reducer)</td><td class="mono">25&ndash;40 g/L</td><td class="mono">30 g/L</td><td>Low: slow/no plating. High: waste, may destabilize</td></tr>
            <tr><td style="font-weight:600;">Plating Rate</td><td class="mono">8&ndash;15 &micro;m/hr</td><td class="mono">12 &micro;m/hr</td><td>Rate set by T, pH, Ni, stabilizer balance</td></tr>
            <tr><td style="font-weight:600;">Loading</td><td class="mono">0.5&ndash;1.5 dm&sup2;/L</td><td class="mono">1.0 dm&sup2;/L</td><td>Low: stabilizer excess, slow. High: depletion, uneven</td></tr>
            <tr><td style="font-weight:600;">Filtration</td><td class="mono">Continuous, 5&ndash;10 &micro;m</td><td class="mono">5 &micro;m</td><td>Poor filtration &rarr; rough/nodular deposit</td></tr>
            <tr><td style="font-weight:600;">Bath Life (MTO)</td><td class="mono">5&ndash;7 MTO</td><td class="mono">5 MTO rebuild</td><td>Orthophosphite buildup slows rate and narrows window</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- DEPOSIT PROPERTIES TABLE -->
    <div>
      <h3 class="section-title">Deposit Properties &mdash; As-Plated vs Baked <span class="sub">high phos 10&ndash;13% P</span></h3>
      <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
        <table class="data-table compact">
          <thead><tr><th>Property</th><th>As-Plated</th><th>Baked 190&deg;C/4hr (HE)</th><th>Baked 260&deg;C/1hr</th><th>Baked 400&deg;C/1hr</th></tr></thead>
          <tbody>
            <tr><td style="font-weight:600;">Hardness</td><td class="mono">450&ndash;550 HV</td><td class="mono">500&ndash;600 HV</td><td class="mono">600&ndash;750 HV</td><td class="mono">850&ndash;1000 HV</td></tr>
            <tr><td style="font-weight:600;">Structure</td><td>Fully amorphous</td><td>Amorphous</td><td>Transitioning</td><td>Crystalline (Ni + Ni&#8323;P)</td></tr>
            <tr><td style="font-weight:600;">Corrosion (25 &micro;m NSS)</td><td class="mono">&gt;1000 hr</td><td class="mono">&gt;1000 hr</td><td class="mono">500&ndash;800 hr</td><td class="mono">200&ndash;400 hr</td></tr>
            <tr><td style="font-weight:600;">Magnetic</td><td>Non-magnetic</td><td>Non-magnetic</td><td>Weakly magnetic</td><td>Magnetic</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- TROUBLESHOOTING + MTO -->
    <div class="bottom-grid">
      <div>
        <h3 class="section-title">Troubleshooting <span class="sub">common bath issues</span></h3>
        <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
          <table class="data-table compact">
            <thead><tr><th>Symptom</th><th>Likely Root Cause</th><th>Action</th></tr></thead>
            <tbody>
              <tr><td style="font-weight:600;">Low plating rate</td><td>Temp low; Ni low; stabilizer excess; high MTO</td><td>Check T, Ni, MTO; adjust stabilizer</td></tr>
              <tr><td style="font-weight:600;">Pitting</td><td>H&#8322; bubbles adhering; low wetting agent</td><td>Add wetting agent; increase agitation</td></tr>
              <tr><td style="font-weight:600;">Dark/dull deposit</td><td>Metallic contamination (Cu, Zn, Fe, Pb)</td><td>Dummy plate at low current; carbon treat</td></tr>
              <tr><td style="font-weight:600;">High internal stress</td><td>Organic contamination; high MTO; pH drift</td><td>Carbon treat; rebuild bath if MTO &gt;6</td></tr>
              <tr><td style="font-weight:600;">Rough/nodular</td><td>Particulates in bath; poor filtration</td><td>Replace filter cartridges; check 5 &micro;m rating</td></tr>
              <tr><td style="font-weight:600;">Decomposition</td><td>Temp spike &gt;95&deg;C; no stabilizer; heavy contamination</td><td>EVACUATE if uncontrolled. Cool bath. Do NOT add chemistry</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- MTO VS DEPOSIT QUALITY SVG -->
    <div class="glass" style="padding:10px 14px;">
      <h3 class="section-title" style="margin-bottom:4px;">Bath Life vs Deposit Quality <span class="sub">plating rate and orthophosphite over metal turnovers</span></h3>
      <svg viewBox="0 0 1100 130" width="100%" height="130" fill="none" xmlns="http://www.w3.org/2000/svg">
        <!-- Rebuild zone shaded band -->
        <rect x="610" y="10" width="200" height="100" rx="4" fill="rgba(232,160,32,.08)"/>
        <text x="710" y="22" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="700" font-size="9" letter-spacing=".05em">REBUILD ZONE</text>
        <!-- Axes -->
        <line x1="80" y1="110" x2="930" y2="110" stroke="var(--muted)" stroke-width="1" opacity=".5"/>
        <line x1="80" y1="10" x2="80" y2="110" stroke="var(--teal)" stroke-width="1" opacity=".6"/>
        <line x1="930" y1="10" x2="930" y2="110" stroke="var(--coral)" stroke-width="1" opacity=".6"/>
        <!-- X-axis ticks (MTO 0-8) -->
        <line x1="80" y1="108" x2="80" y2="112" stroke="var(--muted)" stroke-width="1"/><text x="80" y="122" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="8">0</text>
        <line x1="186" y1="108" x2="186" y2="112" stroke="var(--muted)" stroke-width="1"/><text x="186" y="122" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="8">1</text>
        <line x1="292" y1="108" x2="292" y2="112" stroke="var(--muted)" stroke-width="1"/><text x="292" y="122" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="8">2</text>
        <line x1="398" y1="108" x2="398" y2="112" stroke="var(--muted)" stroke-width="1"/><text x="398" y="122" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="8">3</text>
        <line x1="504" y1="108" x2="504" y2="112" stroke="var(--muted)" stroke-width="1"/><text x="504" y="122" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="8">4</text>
        <line x1="610" y1="108" x2="610" y2="112" stroke="var(--muted)" stroke-width="1"/><text x="610" y="122" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="8">5</text>
        <line x1="716" y1="108" x2="716" y2="112" stroke="var(--muted)" stroke-width="1"/><text x="716" y="122" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="8">6</text>
        <line x1="822" y1="108" x2="822" y2="112" stroke="var(--muted)" stroke-width="1"/><text x="822" y="122" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="8">7</text>
        <line x1="930" y1="108" x2="930" y2="112" stroke="var(--muted)" stroke-width="1"/><text x="930" y="122" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="8">8</text>
        <!-- X-axis label -->
        <text x="505" y="130" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="8" font-weight="600">Metal Turn-Overs (MTO)</text>
        <!-- Left Y-axis label (teal) -->
        <text x="35" y="60" text-anchor="middle" fill="var(--teal)" font-family="Inter,sans-serif" font-size="7" font-weight="600" transform="rotate(-90,35,60)">Plating Rate (&mu;m/hr)</text>
        <!-- Right Y-axis label (coral) -->
        <text x="975" y="60" text-anchor="middle" fill="var(--coral)" font-family="Inter,sans-serif" font-size="7" font-weight="600" transform="rotate(90,975,60)">Orthophosphite (g/L)</text>
        <!-- Plating rate curve (teal) - descending -->
        <polyline points="80,18 186,22 292,28 398,38 504,50 610,62 716,78 822,90 930,100" stroke="var(--teal)" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
        <!-- Orthophosphite curve (coral) - ascending -->
        <polyline points="80,105 186,100 292,92 398,82 504,68 610,52 716,38 822,25 930,15" stroke="var(--coral)" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
        <!-- Data dots -->
        <circle cx="80" cy="18" r="3" fill="var(--teal)"/><circle cx="930" cy="100" r="3" fill="var(--teal)"/>
        <circle cx="80" cy="105" r="3" fill="var(--coral)"/><circle cx="930" cy="15" r="3" fill="var(--coral)"/>
        <!-- Vertical dashed line at MTO 7 -->
        <line x1="822" y1="10" x2="822" y2="108" stroke="var(--coral)" stroke-width="1.5" stroke-dasharray="5,3"/>
        <text x="822" y="8" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" letter-spacing=".05em">MAX BATH LIFE</text>
        <!-- Legend -->
        <rect x="170" y="12" width="230" height="14" rx="3" fill="rgba(0,0,0,.03)"/>
        <line x1="180" y1="19" x2="198" y2="19" stroke="var(--teal)" stroke-width="2"/><text x="202" y="22" fill="var(--teal)" font-family="Inter,sans-serif" font-size="7" font-weight="600">Plating Rate (&mu;m/hr)</text>
        <line x1="295" y1="19" x2="313" y2="19" stroke="var(--coral)" stroke-width="2"/><text x="317" y="22" fill="var(--coral)" font-family="Inter,sans-serif" font-size="7" font-weight="600">Orthophosphite (g/L)</text>
      </svg>
    </div>

    <div>
        <div class="insight-card" style="margin-bottom:8px;">
          <div class="insight-label">MTO &amp; Bath Life</div>
          <div class="insight-text">Each metal turn-over (MTO) = 100% of the original nickel has been plated out and replenished. High-phos baths typically reach <strong>5&ndash;7 MTO</strong> before orthophosphite (HPO&#8323;&sup2;&macr;) buildup slows rate and narrows the operating window. Track via cumulative nickel consumption (kg Ni replenished). Some shops rebuild at 5 MTO for consistent deposit quality.</div>
        </div>
        <div class="insight-card">
          <div class="insight-label">The Decomposition Cascade</div>
          <div class="insight-text">EN bath decomposition is a runaway exothermic reaction. Warning signs: sudden temperature rise, gas evolution (H&#8322; + PH&#8323;), turbidity, black particles. If a bath begins decomposing: <strong>EVACUATE</strong> the area immediately. Phosphine gas (TLV 0.05 ppm) is toxic and can be lethal. Do NOT attempt to add stabilizer or cool a decomposing bath. Wait for it to exhaust itself. Report to supervisor.</div>
        </div>
      </div>
    </div>

    <!-- DECOMPOSITION CASCADE SVG -->
    <div class="glass" style="padding:10px 14px;">
      <h3 class="section-title" style="margin-bottom:4px;">Bath Decomposition Cascade <span class="sub">warning sequence</span></h3>
      <svg viewBox="0 0 1100 100" width="100%" height="100" fill="none" xmlns="http://www.w3.org/2000/svg">
        <!-- Stage 1: TRIGGER -->
        <rect x="20" y="15" width="220" height="65" rx="8" fill="rgba(232,160,32,.10)" stroke="var(--amber)" stroke-width="1.4"/>
        <text x="130" y="32" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="12" letter-spacing=".06em">TRIGGER</text>
        <text x="130" y="48" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="8" font-weight="500">Stabilizer depleted</text>
        <text x="130" y="59" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="8" font-weight="500">Temp &gt;95&deg;C</text>
        <text x="130" y="70" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="8" font-weight="500">Contamination</text>
        <!-- Arrow 1 -->
        <line x1="245" y1="47" x2="285" y2="47" stroke="var(--amber)" stroke-width="2"/><polygon points="281,43 290,47 281,51" fill="var(--amber)"/>
        <!-- Stage 2: WARNING -->
        <rect x="290" y="15" width="220" height="65" rx="8" fill="rgba(232,160,32,.06)" stroke="var(--amber)" stroke-width="1.2" stroke-dasharray="none"/>
        <rect x="290" y="15" width="220" height="65" rx="8" fill="rgba(224,92,92,.04)" stroke="var(--coral)" stroke-width="0.6"/>
        <text x="400" y="32" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="12" letter-spacing=".06em">WARNING</text>
        <text x="400" y="48" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="8" font-weight="500">Turbidity increasing</text>
        <text x="400" y="59" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="8" font-weight="500">Gas bubbles increase</text>
        <text x="400" y="70" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="8" font-weight="500">Temp climbing</text>
        <!-- Arrow 2 -->
        <line x1="515" y1="47" x2="555" y2="47" stroke="var(--coral)" stroke-width="2"/><polygon points="551,43 560,47 551,51" fill="var(--coral)"/>
        <!-- Stage 3: RUNAWAY -->
        <rect x="560" y="15" width="220" height="65" rx="8" fill="rgba(224,92,92,.12)" stroke="var(--coral)" stroke-width="1.6"/>
        <text x="670" y="32" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="12" letter-spacing=".06em">RUNAWAY</text>
        <text x="670" y="48" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="8" font-weight="600">Exothermic reaction</text>
        <text x="670" y="59" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="8" font-weight="600">PH&#8323; gas release</text>
        <text x="670" y="70" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="8" font-weight="600">Boil-over risk</text>
        <!-- Arrow 3 -->
        <line x1="785" y1="47" x2="825" y2="47" stroke="var(--coral)" stroke-width="2.5"/><polygon points="821,42 832,47 821,52" fill="var(--coral)"/>
        <!-- Stage 4: ACTION -->
        <rect x="835" y="8" width="240" height="80" rx="10" fill="rgba(224,92,92,.18)" stroke="var(--coral)" stroke-width="2.4"/>
        <text x="955" y="40" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="18" letter-spacing=".08em">EVACUATE</text>
        <text x="955" y="58" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="14" letter-spacing=".06em">IMMEDIATELY</text>
        <text x="955" y="76" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="7.5" font-weight="500">Do NOT add chemistry. Report to supervisor.</text>
      </svg>
    </div>

    <div class="safety-card">
      <div class="safety-head">&#9888; Safety &mdash; EN Bath</div>
      <div class="safety-body"><strong>Hot acidic nickel solution</strong> at 85&ndash;91&deg;C &mdash; severe burn hazard. <strong>Nickel compounds</strong> are GHS Category 1A carcinogen (IARC Group 1 &mdash; known human carcinogen by inhalation); skin sensitizer (GHS Cat. 1). OSHA PEL: 1 mg/m&sup3; as Ni. <strong>Hydrogen gas</strong> evolved continuously &mdash; ensure adequate ventilation; no ignition sources. <strong>Phosphine risk</strong>: a decomposing bath releases PH&#8323; gas (TLV 0.05 ppm) &mdash; garlic/fish odor = EVACUATE immediately. Full PPE: face shield, chemical splash goggles, acid-resistant gloves, chemical apron. Emergency shower and eyewash within 10 seconds.</div>
    </div>
"""

TECH_BODY_ES["06"] = """
    <div class="glass rule-card">
      <div class="rule-num">85&ndash;91&deg;C</div>
      <div class="rule-body">
        <div class="rule-label">Etapa 5 &mdash; El Ba&ntilde;o EN de Alto F&oacute;sforo</div>
        <div class="rule-text">El coraz&oacute;n del proceso. Los iones de n&iacute;quel son reducidos por hipofosfito de sodio sobre una superficie catal&iacute;tica sin corriente externa. La reacci&oacute;n es autocatal&iacute;tica &mdash; una vez iniciada sobre una superficie limpia, el dep&oacute;sito mismo cataliza m&aacute;s deposici&oacute;n. Temperatura, pH, concentraci&oacute;n de n&iacute;quel y raz&oacute;n de reductor deben mantenerse dentro de ventanas estrechas o el ba&ntilde;o puede perder velocidad, producir defectos o descomponerse catastr&oacute;ficamente.</div>
      </div>
    </div>

    <!-- SVG MECANISMO DE REACCI&Oacute;N AUTOCATAL&Iacute;TICA -->
    <div class="glass" style="padding:10px 14px;">
      <h3 class="section-title" style="margin-bottom:4px;">Mecanismo de Reacci&oacute;n Autocatal&iacute;tica <span class="sub">simplificado</span></h3>
      <svg viewBox="0 0 1100 90" width="100%" height="90" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect x="30" y="10" width="320" height="70" rx="8" fill="rgba(232,160,32,.06)" stroke="var(--amber)" stroke-width="1"/>
        <text x="190" y="25" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11" letter-spacing=".06em">REACTIVOS (EN SOLUCI&Oacute;N)</text>
        <text x="190" y="45" text-anchor="middle" fill="var(--text)" font-family="JetBrains Mono,monospace" font-size="13" font-weight="500">Ni&sup2;&#8314; + H&#8322;PO&#8322;&macr; + H&#8322;O</text>
        <text x="190" y="62" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="8">Sulfato de n&iacute;quel + hipofosfito de sodio</text>
        <text x="190" y="73" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="8">pH 4.2&ndash;4.8 &bull; 85&ndash;91&deg;C &bull; requiere superficie catal&iacute;tica</text>
        <line x1="360" y1="45" x2="430" y2="45" stroke="var(--amber)" stroke-width="2"/><polygon points="426,40 435,45 426,50" fill="var(--amber)"/>
        <text x="395" y="38" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="10">SUPERFICIE</text>
        <text x="395" y="58" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="10">CATAL&Iacute;TICA</text>
        <rect x="440" y="10" width="350" height="70" rx="8" fill="rgba(46,196,182,.06)" stroke="var(--teal)" stroke-width="1"/>
        <text x="615" y="25" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11" letter-spacing=".06em">PRODUCTOS (DEPOSITADO + GAS)</text>
        <text x="615" y="45" text-anchor="middle" fill="var(--text)" font-family="JetBrains Mono,monospace" font-size="13" font-weight="500">Ni&deg; + P + H&#8322;&uarr; + H&#8314; + HPO&#8323;&sup2;&macr;</text>
        <text x="615" y="62" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="8">Aleaci&oacute;n Ni-P + gas hidr&oacute;geno + subproducto ortofosfito</text>
        <text x="615" y="73" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="8">10&ndash;13% P co-depositado &bull; 8&ndash;15 &micro;m/hr &bull; pH baja (&aacute;cido generado)</text>
        <rect x="830" y="10" width="230" height="70" rx="8" fill="rgba(224,92,92,.06)" stroke="var(--coral)" stroke-width="1"/>
        <text x="945" y="25" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11" letter-spacing=".06em">ACUMULACI&Oacute;N DE SUBPRODUCTO</text>
        <text x="945" y="42" text-anchor="middle" fill="var(--text)" font-family="JetBrains Mono,monospace" font-size="11" font-weight="500">HPO&#8323;&sup2;&macr; se acumula</text>
        <text x="945" y="57" text-anchor="middle" fill="var(--coral)" font-family="Inter,sans-serif" font-size="8" font-weight="600">Reduce velocidad a alto MTO</text>
        <text x="945" y="70" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="8">Vida del ba&ntilde;o: 5&ndash;7 MTO t&iacute;pico</text>
      </svg>
    </div>

    <!-- TABLA PAR&Aacute;METROS OPERATIVOS -->
    <div>
      <h3 class="section-title">Par&aacute;metros Operativos <span class="sub">ba&ntilde;o EN alto f&oacute;sforo</span></h3>
      <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
        <table class="data-table compact">
          <thead><tr><th>Par&aacute;metro</th><th>Rango</th><th>Objetivo</th><th>Efecto de Desviaci&oacute;n</th></tr></thead>
          <tbody>
            <tr><td style="font-weight:600;">Temperatura</td><td class="mono">85&ndash;91&deg;C</td><td class="mono">88&deg;C</td><td>Baja: velocidad lenta. Alta: riesgo de descomposici&oacute;n</td></tr>
            <tr><td style="font-weight:600;">pH</td><td class="mono">4.2&ndash;4.8</td><td class="mono">4.5</td><td>Bajo: velocidad lenta, alto %P. Alto: velocidad r&aacute;pida, bajo %P, rugosidad</td></tr>
            <tr><td style="font-weight:600;">N&iacute;quel (Ni&sup2;&#8314;)</td><td class="mono">4.5&ndash;6.5 g/L</td><td class="mono">5.5 g/L</td><td>Bajo: velocidad lenta. Alto: bajo %P, posible descomposici&oacute;n</td></tr>
            <tr><td style="font-weight:600;">Hipofosfito (reductor)</td><td class="mono">25&ndash;40 g/L</td><td class="mono">30 g/L</td><td>Bajo: sin dep&oacute;sito. Alto: desperdicio, puede desestabilizar</td></tr>
            <tr><td style="font-weight:600;">Velocidad de Dep&oacute;sito</td><td class="mono">8&ndash;15 &micro;m/hr</td><td class="mono">12 &micro;m/hr</td><td>Velocidad definida por T, pH, Ni, balance estabilizador</td></tr>
            <tr><td style="font-weight:600;">Carga</td><td class="mono">0.5&ndash;1.5 dm&sup2;/L</td><td class="mono">1.0 dm&sup2;/L</td><td>Baja: exceso estabilizador, lento. Alta: agotamiento, desigualdad</td></tr>
            <tr><td style="font-weight:600;">Filtraci&oacute;n</td><td class="mono">Continua, 5&ndash;10 &micro;m</td><td class="mono">5 &micro;m</td><td>Pobre filtraci&oacute;n &rarr; dep&oacute;sito rugoso/nodular</td></tr>
            <tr><td style="font-weight:600;">Vida del Ba&ntilde;o (MTO)</td><td class="mono">5&ndash;7 MTO</td><td class="mono">5 MTO reconstruir</td><td>Acumulaci&oacute;n de ortofosfito reduce velocidad y estrecha ventana</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- TABLA PROPIEDADES DEL DEP&Oacute;SITO -->
    <div>
      <h3 class="section-title">Propiedades del Dep&oacute;sito &mdash; Tal como Depositado vs Horneado <span class="sub">alto f&oacute;sforo 10&ndash;13% P</span></h3>
      <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
        <table class="data-table compact">
          <thead><tr><th>Propiedad</th><th>Tal como Dep.</th><th>Horneado 190&deg;C/4hr</th><th>Horneado 260&deg;C/1hr</th><th>Horneado 400&deg;C/1hr</th></tr></thead>
          <tbody>
            <tr><td style="font-weight:600;">Dureza</td><td class="mono">450&ndash;550 HV</td><td class="mono">500&ndash;600 HV</td><td class="mono">600&ndash;750 HV</td><td class="mono">850&ndash;1000 HV</td></tr>
            <tr><td style="font-weight:600;">Estructura</td><td>Completamente amorfo</td><td>Amorfo</td><td>En transici&oacute;n</td><td>Cristalino (Ni + Ni&#8323;P)</td></tr>
            <tr><td style="font-weight:600;">Corrosi&oacute;n (25 &micro;m NSS)</td><td class="mono">&gt;1000 hr</td><td class="mono">&gt;1000 hr</td><td class="mono">500&ndash;800 hr</td><td class="mono">200&ndash;400 hr</td></tr>
            <tr><td style="font-weight:600;">Magn&eacute;tico</td><td>No magn&eacute;tico</td><td>No magn&eacute;tico</td><td>D&eacute;bilmente magn&eacute;tico</td><td>Magn&eacute;tico</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- SOLUCI&Oacute;N DE PROBLEMAS + MTO -->
    <div class="bottom-grid">
      <div>
        <h3 class="section-title">Soluci&oacute;n de Problemas <span class="sub">problemas comunes del ba&ntilde;o</span></h3>
        <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
          <table class="data-table compact">
            <thead><tr><th>S&iacute;ntoma</th><th>Causa Probable</th><th>Acci&oacute;n</th></tr></thead>
            <tbody>
              <tr><td style="font-weight:600;">Velocidad baja</td><td>Temp baja; Ni bajo; exceso estabilizador; alto MTO</td><td>Verificar T, Ni, MTO; ajustar estabilizador</td></tr>
              <tr><td style="font-weight:600;">Picaduras</td><td>Burbujas H&#8322; adheridas; bajo agente humectante</td><td>Agregar humectante; aumentar agitaci&oacute;n</td></tr>
              <tr><td style="font-weight:600;">Dep&oacute;sito oscuro/opaco</td><td>Contaminaci&oacute;n met&aacute;lica (Cu, Zn, Fe, Pb)</td><td>Dep&oacute;sito dummy a baja corriente; tratar con carb&oacute;n</td></tr>
              <tr><td style="font-weight:600;">Alto estr&eacute;s interno</td><td>Contaminaci&oacute;n org&aacute;nica; alto MTO; deriva de pH</td><td>Tratar con carb&oacute;n; reconstruir si MTO &gt;6</td></tr>
              <tr><td style="font-weight:600;">Rugoso/nodular</td><td>Part&iacute;culas en ba&ntilde;o; pobre filtraci&oacute;n</td><td>Reemplazar cartuchos de filtro; verificar 5 &micro;m</td></tr>
              <tr><td style="font-weight:600;">Descomposici&oacute;n</td><td>Pico de temp &gt;95&deg;C; sin estabilizador; contaminaci&oacute;n</td><td>EVACUE si no se controla. Enfr&iacute;e. NO agregue qu&iacute;micos</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- SVG VIDA DEL BA&Ntilde;O VS CALIDAD -->
    <div class="glass" style="padding:10px 14px;">
      <h3 class="section-title" style="margin-bottom:4px;">Vida del Ba&ntilde;o vs Calidad del Dep&oacute;sito <span class="sub">velocidad de deposici&oacute;n y ortofosfito sobre recambios met&aacute;licos</span></h3>
      <svg viewBox="0 0 1100 130" width="100%" height="130" fill="none" xmlns="http://www.w3.org/2000/svg">
        <!-- Rebuild zone -->
        <rect x="610" y="10" width="200" height="100" rx="4" fill="rgba(232,160,32,.08)"/>
        <text x="710" y="22" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="700" font-size="9" letter-spacing=".05em">ZONA DE RECONSTRUCCI&Oacute;N</text>
        <!-- Axes -->
        <line x1="80" y1="110" x2="930" y2="110" stroke="var(--muted)" stroke-width="1" opacity=".5"/>
        <line x1="80" y1="10" x2="80" y2="110" stroke="var(--teal)" stroke-width="1" opacity=".6"/>
        <line x1="930" y1="10" x2="930" y2="110" stroke="var(--coral)" stroke-width="1" opacity=".6"/>
        <!-- X-axis ticks (MTO 0-8) -->
        <line x1="80" y1="108" x2="80" y2="112" stroke="var(--muted)" stroke-width="1"/><text x="80" y="122" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="8">0</text>
        <line x1="186" y1="108" x2="186" y2="112" stroke="var(--muted)" stroke-width="1"/><text x="186" y="122" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="8">1</text>
        <line x1="292" y1="108" x2="292" y2="112" stroke="var(--muted)" stroke-width="1"/><text x="292" y="122" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="8">2</text>
        <line x1="398" y1="108" x2="398" y2="112" stroke="var(--muted)" stroke-width="1"/><text x="398" y="122" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="8">3</text>
        <line x1="504" y1="108" x2="504" y2="112" stroke="var(--muted)" stroke-width="1"/><text x="504" y="122" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="8">4</text>
        <line x1="610" y1="108" x2="610" y2="112" stroke="var(--muted)" stroke-width="1"/><text x="610" y="122" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="8">5</text>
        <line x1="716" y1="108" x2="716" y2="112" stroke="var(--muted)" stroke-width="1"/><text x="716" y="122" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="8">6</text>
        <line x1="822" y1="108" x2="822" y2="112" stroke="var(--muted)" stroke-width="1"/><text x="822" y="122" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="8">7</text>
        <line x1="930" y1="108" x2="930" y2="112" stroke="var(--muted)" stroke-width="1"/><text x="930" y="122" text-anchor="middle" fill="var(--muted)" font-family="JetBrains Mono,monospace" font-size="8">8</text>
        <!-- X-axis label -->
        <text x="505" y="130" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="8" font-weight="600">Recambios Met&aacute;licos (MTO)</text>
        <!-- Left Y-axis label (teal) -->
        <text x="35" y="60" text-anchor="middle" fill="var(--teal)" font-family="Inter,sans-serif" font-size="7" font-weight="600" transform="rotate(-90,35,60)">Vel. Deposici&oacute;n (&mu;m/hr)</text>
        <!-- Right Y-axis label (coral) -->
        <text x="975" y="60" text-anchor="middle" fill="var(--coral)" font-family="Inter,sans-serif" font-size="7" font-weight="600" transform="rotate(90,975,60)">Ortofosfito (g/L)</text>
        <!-- Plating rate curve (teal) -->
        <polyline points="80,18 186,22 292,28 398,38 504,50 610,62 716,78 822,90 930,100" stroke="var(--teal)" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
        <!-- Orthophosphite curve (coral) -->
        <polyline points="80,105 186,100 292,92 398,82 504,68 610,52 716,38 822,25 930,15" stroke="var(--coral)" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
        <!-- Data dots -->
        <circle cx="80" cy="18" r="3" fill="var(--teal)"/><circle cx="930" cy="100" r="3" fill="var(--teal)"/>
        <circle cx="80" cy="105" r="3" fill="var(--coral)"/><circle cx="930" cy="15" r="3" fill="var(--coral)"/>
        <!-- Vertical dashed line at MTO 7 -->
        <line x1="822" y1="10" x2="822" y2="108" stroke="var(--coral)" stroke-width="1.5" stroke-dasharray="5,3"/>
        <text x="822" y="8" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" letter-spacing=".05em">VIDA M&Aacute;X. DEL BA&Ntilde;O</text>
        <!-- Legend -->
        <rect x="170" y="12" width="250" height="14" rx="3" fill="rgba(0,0,0,.03)"/>
        <line x1="180" y1="19" x2="198" y2="19" stroke="var(--teal)" stroke-width="2"/><text x="202" y="22" fill="var(--teal)" font-family="Inter,sans-serif" font-size="7" font-weight="600">Vel. Deposici&oacute;n (&mu;m/hr)</text>
        <line x1="310" y1="19" x2="328" y2="19" stroke="var(--coral)" stroke-width="2"/><text x="332" y="22" fill="var(--coral)" font-family="Inter,sans-serif" font-size="7" font-weight="600">Ortofosfito (g/L)</text>
      </svg>
    </div>

    <div>
        <div class="insight-card" style="margin-bottom:8px;">
          <div class="insight-label">MTO y Vida del Ba&ntilde;o</div>
          <div class="insight-text">Cada recambio met&aacute;lico (MTO) = 100% del n&iacute;quel original ha sido depositado y repuesto. Ba&ntilde;os de alto f&oacute;sforo t&iacute;picamente alcanzan <strong>5&ndash;7 MTO</strong> antes de que la acumulaci&oacute;n de ortofosfito (HPO&#8323;&sup2;&macr;) reduzca la velocidad y estreche la ventana operativa. Rastree v&iacute;a consumo acumulado de n&iacute;quel (kg Ni repuesto).</div>
        </div>
        <div class="insight-card">
          <div class="insight-label">La Cascada de Descomposici&oacute;n</div>
          <div class="insight-text">La descomposici&oacute;n del ba&ntilde;o EN es una reacci&oacute;n exot&eacute;rmica desbocada. Se&ntilde;ales de alerta: aumento s&uacute;bito de temperatura, evoluci&oacute;n de gas (H&#8322; + PH&#8323;), turbidez, part&iacute;culas negras. Si un ba&ntilde;o comienza a descomponerse: <strong>EVACUE</strong> el &aacute;rea inmediatamente. Gas fosfina (TLV 0.05 ppm) es t&oacute;xico y puede ser letal. NO intente agregar estabilizador o enfriar. Reporte a su supervisor.</div>
        </div>
      </div>
    </div>

    <!-- SVG CASCADA DE DESCOMPOSICI&Oacute;N -->
    <div class="glass" style="padding:10px 14px;">
      <h3 class="section-title" style="margin-bottom:4px;">Cascada de Descomposici&oacute;n del Ba&ntilde;o <span class="sub">secuencia de alerta</span></h3>
      <svg viewBox="0 0 1100 100" width="100%" height="100" fill="none" xmlns="http://www.w3.org/2000/svg">
        <!-- Etapa 1: DETONANTE -->
        <rect x="20" y="15" width="220" height="65" rx="8" fill="rgba(232,160,32,.10)" stroke="var(--amber)" stroke-width="1.4"/>
        <text x="130" y="32" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="12" letter-spacing=".06em">DETONANTE</text>
        <text x="130" y="48" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="8" font-weight="500">Estabilizador agotado</text>
        <text x="130" y="59" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="8" font-weight="500">Temp &gt;95&deg;C</text>
        <text x="130" y="70" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="8" font-weight="500">Contaminaci&oacute;n</text>
        <!-- Flecha 1 -->
        <line x1="245" y1="47" x2="285" y2="47" stroke="var(--amber)" stroke-width="2"/><polygon points="281,43 290,47 281,51" fill="var(--amber)"/>
        <!-- Etapa 2: ADVERTENCIA -->
        <rect x="290" y="15" width="220" height="65" rx="8" fill="rgba(232,160,32,.06)" stroke="var(--amber)" stroke-width="1.2"/>
        <rect x="290" y="15" width="220" height="65" rx="8" fill="rgba(224,92,92,.04)" stroke="var(--coral)" stroke-width="0.6"/>
        <text x="400" y="32" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="12" letter-spacing=".06em">ADVERTENCIA</text>
        <text x="400" y="48" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="8" font-weight="500">Turbidez aumentando</text>
        <text x="400" y="59" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="8" font-weight="500">Burbujas de gas aumentan</text>
        <text x="400" y="70" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="8" font-weight="500">Temperatura subiendo</text>
        <!-- Flecha 2 -->
        <line x1="515" y1="47" x2="555" y2="47" stroke="var(--coral)" stroke-width="2"/><polygon points="551,43 560,47 551,51" fill="var(--coral)"/>
        <!-- Etapa 3: DESBOCADA -->
        <rect x="560" y="15" width="220" height="65" rx="8" fill="rgba(224,92,92,.12)" stroke="var(--coral)" stroke-width="1.6"/>
        <text x="670" y="32" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="12" letter-spacing=".06em">DESBOCADA</text>
        <text x="670" y="48" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="8" font-weight="600">Reacci&oacute;n exot&eacute;rmica</text>
        <text x="670" y="59" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="8" font-weight="600">Liberaci&oacute;n gas PH&#8323;</text>
        <text x="670" y="70" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="8" font-weight="600">Riesgo de desbordamiento</text>
        <!-- Flecha 3 -->
        <line x1="785" y1="47" x2="825" y2="47" stroke="var(--coral)" stroke-width="2.5"/><polygon points="821,42 832,47 821,52" fill="var(--coral)"/>
        <!-- Etapa 4: ACCI&Oacute;N -->
        <rect x="835" y="8" width="240" height="80" rx="10" fill="rgba(224,92,92,.18)" stroke="var(--coral)" stroke-width="2.4"/>
        <text x="955" y="40" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="18" letter-spacing=".08em">EVACUE</text>
        <text x="955" y="58" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="14" letter-spacing=".06em">INMEDIATAMENTE</text>
        <text x="955" y="76" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="7.5" font-weight="500">NO agregue qu&iacute;micos. Reporte a su supervisor.</text>
      </svg>
    </div>

    <div class="safety-card">
      <div class="safety-head">&#9888; Seguridad &mdash; Ba&ntilde;o EN</div>
      <div class="safety-body"><strong>Soluci&oacute;n &aacute;cida caliente de n&iacute;quel</strong> a 85&ndash;91&deg;C &mdash; riesgo severo de quemaduras. <strong>Compuestos de n&iacute;quel</strong> son carcin&oacute;geno GHS Categor&iacute;a 1A (IARC Grupo 1 &mdash; carcin&oacute;geno humano conocido por inhalaci&oacute;n); sensibilizante cut&aacute;neo (GHS Cat. 1). OSHA PEL: 1 mg/m&sup3; como Ni. <strong>Gas hidr&oacute;geno</strong> generado continuamente &mdash; asegure ventilaci&oacute;n adecuada; sin fuentes de ignici&oacute;n. <strong>Riesgo de fosfina</strong>: ba&ntilde;o en descomposici&oacute;n libera gas PH&#8323; (TLV 0.05 ppm) &mdash; olor a ajo/pescado = EVACUE inmediatamente. EPP completo: careta, lentes de seguridad contra salpicaduras, guantes resistentes a &aacute;cido, mandil qu&iacute;mico. Regadera y lavaojos a 10 segundos.</div>
    </div>
"""

SF_BODY_EN["06"] = """
    <div class="glass key-card">
      <div class="key-num">85&ndash;91&deg;C</div>
      <div class="key-label">EN Bath Temperature &mdash; The Heart of the Process</div>
      <div class="key-text">The EN bath is where the magic happens. Nickel deposits itself onto the part without external current. Temperature, pH, and nickel level must stay in range. If any parameter drifts too far, the bath can slow down, produce bad deposits, or decompose. Watch the bath closely every load.</div>
    </div>

    <div class="glass" style="padding:10px 12px;">
      <div class="section-title">Key Parameters <span style="font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:.10em;color:var(--muted);margin-left:8px;">CHECK EVERY LOAD</span></div>
      <table class="flow-table">
        <thead><tr><th>Parameter</th><th>Range</th><th>Target</th></tr></thead>
        <tbody>
          <tr><td>Temperature</td><td class="mono">85&ndash;91&deg;C (185&ndash;196&deg;F)</td><td class="mono">88&deg;C</td></tr>
          <tr><td>pH</td><td class="mono">4.2&ndash;4.8</td><td class="mono">4.5</td></tr>
          <tr><td>Nickel (Ni&sup2;&#8314;)</td><td class="mono">4.5&ndash;6.5 g/L</td><td class="mono">5.5 g/L</td></tr>
          <tr><td>Plating Rate</td><td class="mono">8&ndash;15 &micro;m/hr</td><td class="mono">12 &micro;m/hr</td></tr>
          <tr><td>Loading</td><td class="mono">0.5&ndash;1.5 dm&sup2;/L</td><td class="mono">1.0 dm&sup2;/L</td></tr>
          <tr><td>Filtration</td><td class="mono">Continuous, 5 &micro;m</td><td class="mono">Always on</td></tr>
        </tbody>
      </table>
    </div>

    <div class="glass" style="padding:10px 12px;">
      <div class="section-title">Key Rules <span style="font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:.10em;color:var(--muted);margin-left:8px;">CRITICAL</span></div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;">
        <div style="padding:8px 10px;border-radius:8px;background:rgba(224,92,92,.08);border:1px solid rgba(224,92,92,.2);"><div style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:13px;color:var(--coral);letter-spacing:.04em;margin-bottom:3px;">TEMPERATURE</div><div style="font-size:10.5px;color:var(--muted);line-height:1.35;">85&ndash;91&deg;C. Too low = slow plating. Too high = decomposition risk. Never let it exceed 95&deg;C.</div></div>
        <div style="padding:8px 10px;border-radius:8px;background:rgba(232,160,32,.08);border:1px solid rgba(232,160,32,.2);"><div style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:13px;color:var(--amber);letter-spacing:.04em;margin-bottom:3px;">pH CONTROL</div><div style="font-size:10.5px;color:var(--muted);line-height:1.35;">pH 4.2&ndash;4.8. pH drops during plating (acid generated). Add NH&#8324;OH to raise. Never overshoot &mdash; high pH = low phosphorus.</div></div>
        <div style="padding:8px 10px;border-radius:8px;background:rgba(46,196,182,.08);border:1px solid rgba(46,196,182,.2);"><div style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:13px;color:var(--teal);letter-spacing:.04em;margin-bottom:3px;">FILTRATION</div><div style="font-size:10.5px;color:var(--muted);line-height:1.35;">Continuous filtration at 5 &micro;m. Particles in the bath = rough deposit. Check filter pressure daily.</div></div>
        <div style="padding:8px 10px;border-radius:8px;background:rgba(39,174,96,.08);border:1px solid rgba(39,174,96,.2);"><div style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:13px;color:var(--emerald);letter-spacing:.04em;margin-bottom:3px;">LOADING</div><div style="font-size:10.5px;color:var(--muted);line-height:1.35;">0.5&ndash;1.5 dm&sup2;/L. Too few parts = stabilizer excess slows plating. Too many = uneven thickness.</div></div>
      </div>
    </div>

    <div class="insight-card">
      <div class="insight-label">&#9888; Decomposition Warning</div>
      <div class="insight-text">If you see <strong>sudden temperature rise</strong>, <strong>heavy gas bubbling</strong>, <strong>cloudy/dark bath</strong>, or <strong>unusual odor</strong> (garlic/fish): the bath may be decomposing. <strong>EVACUATE</strong> the area immediately. Phosphine gas (PH&#8323;) is released &mdash; toxic at 0.05 ppm. Do NOT try to add chemicals or cool the bath. Report to supervisor. Wait for the bath to exhaust itself.</div>
    </div>

    <!-- DECOMPOSITION CASCADE SVG (SF) -->
    <div class="glass" style="padding:8px 10px;">
      <div class="section-title" style="color:var(--coral);">Decomposition Cascade</div>
      <svg viewBox="0 0 820 70" width="100%" style="height:auto;display:block;" fill="none" xmlns="http://www.w3.org/2000/svg">
        <!-- Stage 1: TRIGGER -->
        <rect x="10" y="8" width="160" height="52" rx="6" fill="rgba(232,160,32,.10)" stroke="var(--amber)" stroke-width="1.2"/>
        <text x="90" y="22" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="10" letter-spacing=".05em">TRIGGER</text>
        <text x="90" y="34" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="7">Stabilizer depleted</text>
        <text x="90" y="44" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="7">Temp &gt;95&deg;C / Contamination</text>
        <!-- Arrow -->
        <line x1="174" y1="34" x2="200" y2="34" stroke="var(--amber)" stroke-width="1.5"/><polygon points="197,31 204,34 197,37" fill="var(--amber)"/>
        <!-- Stage 2: WARNING -->
        <rect x="205" y="8" width="175" height="52" rx="6" fill="rgba(232,160,32,.06)" stroke="var(--amber)" stroke-width="1"/>
        <rect x="205" y="8" width="175" height="52" rx="6" fill="rgba(224,92,92,.04)" stroke="var(--coral)" stroke-width="0.5"/>
        <text x="292" y="22" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="10" letter-spacing=".05em">WARNING</text>
        <text x="292" y="34" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="7">Turbidity / Gas bubbles</text>
        <text x="292" y="44" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="7">Temp climbing</text>
        <!-- Arrow -->
        <line x1="384" y1="34" x2="410" y2="34" stroke="var(--coral)" stroke-width="1.5"/><polygon points="407,31 414,34 407,37" fill="var(--coral)"/>
        <!-- Stage 3: RUNAWAY -->
        <rect x="415" y="8" width="165" height="52" rx="6" fill="rgba(224,92,92,.12)" stroke="var(--coral)" stroke-width="1.4"/>
        <text x="497" y="22" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="10" letter-spacing=".05em">RUNAWAY</text>
        <text x="497" y="34" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="7" font-weight="600">Exothermic / PH&#8323; gas</text>
        <text x="497" y="44" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="7" font-weight="600">Boil-over risk</text>
        <!-- Arrow -->
        <line x1="584" y1="34" x2="615" y2="34" stroke="var(--coral)" stroke-width="2"/><polygon points="612,30 620,34 612,38" fill="var(--coral)"/>
        <!-- Stage 4: ACTION -->
        <rect x="622" y="3" width="188" height="62" rx="8" fill="rgba(224,92,92,.18)" stroke="var(--coral)" stroke-width="2"/>
        <text x="716" y="28" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="14" letter-spacing=".06em">EVACUATE</text>
        <text x="716" y="44" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11" letter-spacing=".05em">IMMEDIATELY</text>
        <text x="716" y="57" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="6.5">Do NOT add chemistry.</text>
      </svg>
    </div>

    <div class="compare-row">
      <div class="compare-card glass do"><div class="compare-head good">&#10003; Do</div><ul class="compare-list"><li>Check temp and pH before every load</li><li>Log all chemistry additions</li><li>Keep filtration running at all times</li><li>Report any unusual bath behavior immediately</li><li>Maintain proper loading ratio</li></ul></div>
      <div class="compare-card glass dont"><div class="compare-head bad">&#10007; Don&rsquo;t</div><ul class="compare-list"><li>Drop parts &mdash; gentle immersion only</li><li>Add chemicals without lab analysis</li><li>Ignore temperature alarms</li><li>Run the bath without filtration</li><li>Attempt to control a decomposing bath</li></ul></div>
    </div>

    <div class="glass safety-card">
      <div class="section-title coral">&#9888; Safety &mdash; EN Bath</div>
      <div class="safety-text"><strong>Hot acidic nickel</strong> at 85&ndash;91&deg;C &mdash; severe burn hazard. <strong>Nickel compounds</strong>: GHS Category 1A carcinogen (IARC Group 1 &mdash; known human carcinogen by inhalation); skin sensitizer. <strong>Hydrogen gas</strong> evolved continuously &mdash; no ignition sources. <strong>Phosphine</strong> (PH&#8323;) from decomposition &mdash; TLV 0.05 ppm &mdash; EVACUATE if unusual odor detected. Full PPE required. Emergency shower and eyewash within 10 seconds.</div>
    </div>
"""

SF_BODY_ES["06"] = """
    <div class="glass key-card">
      <div class="key-num">85&ndash;91&deg;C</div>
      <div class="key-label">Temperatura del Ba&ntilde;o EN &mdash; El Coraz&oacute;n del Proceso</div>
      <div class="key-text">El ba&ntilde;o EN es donde ocurre la magia. El n&iacute;quel se deposita sobre la pieza sin corriente externa. La temperatura, pH y nivel de n&iacute;quel deben mantenerse en rango. Si alg&uacute;n par&aacute;metro se desv&iacute;a demasiado, el ba&ntilde;o puede hacerse lento, producir dep&oacute;sitos malos o descomponerse. Vigile el ba&ntilde;o de cerca cada carga.</div>
    </div>

    <div class="glass" style="padding:10px 12px;">
      <div class="section-title">Par&aacute;metros Clave <span style="font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:.10em;color:var(--muted);margin-left:8px;">VERIFIQUE CADA CARGA</span></div>
      <table class="flow-table">
        <thead><tr><th>Par&aacute;metro</th><th>Rango</th><th>Objetivo</th></tr></thead>
        <tbody>
          <tr><td>Temperatura</td><td class="mono">85&ndash;91&deg;C</td><td class="mono">88&deg;C</td></tr>
          <tr><td>pH</td><td class="mono">4.2&ndash;4.8</td><td class="mono">4.5</td></tr>
          <tr><td>N&iacute;quel (Ni&sup2;&#8314;)</td><td class="mono">4.5&ndash;6.5 g/L</td><td class="mono">5.5 g/L</td></tr>
          <tr><td>Velocidad de Dep&oacute;sito</td><td class="mono">8&ndash;15 &micro;m/hr</td><td class="mono">12 &micro;m/hr</td></tr>
          <tr><td>Carga</td><td class="mono">0.5&ndash;1.5 dm&sup2;/L</td><td class="mono">1.0 dm&sup2;/L</td></tr>
          <tr><td>Filtraci&oacute;n</td><td class="mono">Continua, 5 &micro;m</td><td class="mono">Siempre encendida</td></tr>
        </tbody>
      </table>
    </div>

    <div class="glass" style="padding:10px 12px;">
      <div class="section-title">Reglas Clave <span style="font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:.10em;color:var(--muted);margin-left:8px;">CR&Iacute;TICO</span></div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;">
        <div style="padding:8px 10px;border-radius:8px;background:rgba(224,92,92,.08);border:1px solid rgba(224,92,92,.2);"><div style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:13px;color:var(--coral);letter-spacing:.04em;margin-bottom:3px;">TEMPERATURA</div><div style="font-size:10.5px;color:var(--muted);line-height:1.35;">85&ndash;91&deg;C. Muy baja = deposici&oacute;n lenta. Muy alta = riesgo de descomposici&oacute;n. Nunca permita que exceda 95&deg;C.</div></div>
        <div style="padding:8px 10px;border-radius:8px;background:rgba(232,160,32,.08);border:1px solid rgba(232,160,32,.2);"><div style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:13px;color:var(--amber);letter-spacing:.04em;margin-bottom:3px;">CONTROL DE pH</div><div style="font-size:10.5px;color:var(--muted);line-height:1.35;">pH 4.2&ndash;4.8. El pH baja durante el deposici&oacute;n (&aacute;cido generado). Agregue NH&#8324;OH para subir. Nunca se exceda &mdash; pH alto = bajo f&oacute;sforo.</div></div>
        <div style="padding:8px 10px;border-radius:8px;background:rgba(46,196,182,.08);border:1px solid rgba(46,196,182,.2);"><div style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:13px;color:var(--teal);letter-spacing:.04em;margin-bottom:3px;">FILTRACI&Oacute;N</div><div style="font-size:10.5px;color:var(--muted);line-height:1.35;">Filtraci&oacute;n continua a 5 &micro;m. Part&iacute;culas en el ba&ntilde;o = dep&oacute;sito rugoso. Verifique presi&oacute;n del filtro diariamente.</div></div>
        <div style="padding:8px 10px;border-radius:8px;background:rgba(39,174,96,.08);border:1px solid rgba(39,174,96,.2);"><div style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:13px;color:var(--emerald);letter-spacing:.04em;margin-bottom:3px;">CARGA</div><div style="font-size:10.5px;color:var(--muted);line-height:1.35;">0.5&ndash;1.5 dm&sup2;/L. Muy pocas piezas = exceso de estabilizador ralentiza. Demasiadas = espesor desigual.</div></div>
      </div>
    </div>

    <div class="insight-card">
      <div class="insight-label">&#9888; Advertencia de Descomposici&oacute;n</div>
      <div class="insight-text">Si observa <strong>aumento s&uacute;bito de temperatura</strong>, <strong>burbujeo excesivo de gas</strong>, <strong>ba&ntilde;o turbio/oscuro</strong> u <strong>olor inusual</strong> (ajo/pescado): el ba&ntilde;o puede estar descomponi&eacute;ndose. <strong>EVACUE</strong> el &aacute;rea inmediatamente. Se libera gas fosfina (PH&#8323;) &mdash; t&oacute;xico a 0.05 ppm. NO intente agregar qu&iacute;micos o enfriar el ba&ntilde;o. Reporte a su supervisor. Espere a que el ba&ntilde;o se agote por s&iacute; solo.</div>
    </div>

    <!-- SVG CASCADA DE DESCOMPOSICI&Oacute;N (SF) -->
    <div class="glass" style="padding:8px 10px;">
      <div class="section-title" style="color:var(--coral);">Cascada de Descomposici&oacute;n</div>
      <svg viewBox="0 0 820 70" width="100%" style="height:auto;display:block;" fill="none" xmlns="http://www.w3.org/2000/svg">
        <!-- Etapa 1: DETONANTE -->
        <rect x="10" y="8" width="160" height="52" rx="6" fill="rgba(232,160,32,.10)" stroke="var(--amber)" stroke-width="1.2"/>
        <text x="90" y="22" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="10" letter-spacing=".05em">DETONANTE</text>
        <text x="90" y="34" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="7">Estabilizador agotado</text>
        <text x="90" y="44" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="7">Temp &gt;95&deg;C / Contaminaci&oacute;n</text>
        <!-- Flecha -->
        <line x1="174" y1="34" x2="200" y2="34" stroke="var(--amber)" stroke-width="1.5"/><polygon points="197,31 204,34 197,37" fill="var(--amber)"/>
        <!-- Etapa 2: ADVERTENCIA -->
        <rect x="205" y="8" width="175" height="52" rx="6" fill="rgba(232,160,32,.06)" stroke="var(--amber)" stroke-width="1"/>
        <rect x="205" y="8" width="175" height="52" rx="6" fill="rgba(224,92,92,.04)" stroke="var(--coral)" stroke-width="0.5"/>
        <text x="292" y="22" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="10" letter-spacing=".05em">ADVERTENCIA</text>
        <text x="292" y="34" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="7">Turbidez / Burbujas de gas</text>
        <text x="292" y="44" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="7">Temperatura subiendo</text>
        <!-- Flecha -->
        <line x1="384" y1="34" x2="410" y2="34" stroke="var(--coral)" stroke-width="1.5"/><polygon points="407,31 414,34 407,37" fill="var(--coral)"/>
        <!-- Etapa 3: DESBOCADA -->
        <rect x="415" y="8" width="165" height="52" rx="6" fill="rgba(224,92,92,.12)" stroke="var(--coral)" stroke-width="1.4"/>
        <text x="497" y="22" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="10" letter-spacing=".05em">DESBOCADA</text>
        <text x="497" y="34" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="7" font-weight="600">Exot&eacute;rmica / Gas PH&#8323;</text>
        <text x="497" y="44" text-anchor="middle" fill="var(--text)" font-family="Inter,sans-serif" font-size="7" font-weight="600">Riesgo de desbordamiento</text>
        <!-- Flecha -->
        <line x1="584" y1="34" x2="615" y2="34" stroke="var(--coral)" stroke-width="2"/><polygon points="612,30 620,34 612,38" fill="var(--coral)"/>
        <!-- Etapa 4: ACCI&Oacute;N -->
        <rect x="622" y="3" width="188" height="62" rx="8" fill="rgba(224,92,92,.18)" stroke="var(--coral)" stroke-width="2"/>
        <text x="716" y="28" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="14" letter-spacing=".06em">EVACUE</text>
        <text x="716" y="44" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11" letter-spacing=".05em">INMEDIATAMENTE</text>
        <text x="716" y="57" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="6.5">NO agregue qu&iacute;micos.</text>
      </svg>
    </div>

    <div class="compare-row">
      <div class="compare-card glass do"><div class="compare-head good">&#10003; Haga</div><ul class="compare-list"><li>Verifique temperatura y pH antes de cada carga</li><li>Registre todas las adiciones de qu&iacute;micos</li><li>Mantenga la filtraci&oacute;n funcionando en todo momento</li><li>Reporte cualquier comportamiento inusual del ba&ntilde;o inmediatamente</li><li>Mantenga la proporci&oacute;n de carga adecuada</li></ul></div>
      <div class="compare-card glass dont"><div class="compare-head bad">&#10007; No Haga</div><ul class="compare-list"><li>Dejar caer piezas &mdash; solo inmersi&oacute;n suave</li><li>Agregar qu&iacute;micos sin an&aacute;lisis de laboratorio</li><li>Ignorar alarmas de temperatura</li><li>Operar el ba&ntilde;o sin filtraci&oacute;n</li><li>Intentar controlar un ba&ntilde;o en descomposici&oacute;n</li></ul></div>
    </div>

    <div class="glass safety-card">
      <div class="section-title coral">&#9888; Seguridad &mdash; Ba&ntilde;o EN</div>
      <div class="safety-text"><strong>N&iacute;quel &aacute;cido caliente</strong> a 85&ndash;91&deg;C &mdash; riesgo severo de quemaduras. <strong>Compuestos de n&iacute;quel</strong>: carcin&oacute;geno GHS Categor&iacute;a 1A (IARC Grupo 1 &mdash; carcin&oacute;geno humano conocido por inhalaci&oacute;n); sensibilizante cut&aacute;neo. <strong>Gas hidr&oacute;geno</strong> generado continuamente &mdash; sin fuentes de ignici&oacute;n. <strong>Fosfina</strong> (PH&#8323;) de descomposici&oacute;n &mdash; TLV 0.05 ppm &mdash; EVACUE si detecta olor inusual. EPP completo requerido. Regadera y lavaojos a 10 segundos.</div>
    </div>
"""

# =====================================================================
# POSTER 07 — FINAL RINSE
# =====================================================================
TECH_BODY_EN["07"] = """
    <div class="glass rule-card">
      <div class="rule-num">&lt;10s</div>
      <div class="rule-body">
        <div class="rule-label">Transfer Time &lt;10 Seconds &mdash; Parts to Rinse Immediately</div>
        <div class="rule-text">The final rinse removes residual EN chemistry from the deposit surface before post-treatment. Transfer time is critical: freshly plated EN surfaces oxidize and stain rapidly in air. Parts must move from the EN bath to the first rinse tank within 10 seconds to prevent discoloration, water stains, and rainbow tinting that can compromise adhesion of subsequent coatings or cause cosmetic rejection.</div>
      </div>
    </div>

    <!-- RINSE PARAMETERS TABLE -->
    <div>
      <h3 class="section-title">Rinse Sequence &mdash; After EN Bath <span class="sub">multi-stage recommended</span></h3>
      <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
        <table class="data-table compact">
          <thead><tr><th>Stage</th><th>Type</th><th>Water</th><th>Temp</th><th>Time</th><th>Purpose</th></tr></thead>
          <tbody>
            <tr><td class="mono" style="font-weight:600;color:var(--teal);">R1</td><td>Drag-Out Recovery</td><td>Tap water</td><td class="mono">Ambient</td><td class="mono">15&ndash;30 s</td><td>Capture Ni drag-out for return to bath or waste treatment</td></tr>
            <tr><td class="mono" style="font-weight:600;color:var(--teal);">R2</td><td>Cascade Rinse</td><td>Tap water</td><td class="mono">Ambient</td><td class="mono">30&ndash;60 s</td><td>Bulk removal of residual chemistry</td></tr>
            <tr><td class="mono" style="font-weight:600;color:var(--teal);">R3</td><td>DI Final Rinse</td><td>DI water</td><td class="mono">Cold / warm</td><td class="mono">30&ndash;60 s</td><td>Spot-free surface; prevent mineral deposits; &lt;10 &micro;S/cm</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- WATER QUALITY TABLE -->
    <div>
      <h3 class="section-title">Water Quality Requirements <span class="sub">by rinse stage</span></h3>
      <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
        <table class="data-table compact">
          <thead><tr><th>Parameter</th><th>Drag-Out (R1)</th><th>Cascade (R2)</th><th>DI Final (R3)</th></tr></thead>
          <tbody>
            <tr><td style="font-weight:600;">Conductivity</td><td class="mono">&lt;500 &micro;S/cm</td><td class="mono">&lt;50 &micro;S/cm</td><td class="mono">&lt;10 &micro;S/cm</td></tr>
            <tr><td style="font-weight:600;">Nickel</td><td class="mono">&lt;100 ppm (recover)</td><td class="mono">&lt;5 ppm</td><td class="mono">&lt;0.5 ppm</td></tr>
            <tr><td style="font-weight:600;">pH</td><td class="mono">4&ndash;6</td><td class="mono">5&ndash;7</td><td class="mono">5.5&ndash;7.5</td></tr>
            <tr><td style="font-weight:600;">Water Source</td><td>Municipal OK</td><td>Municipal OK</td><td>DI only</td></tr>
            <tr><td style="font-weight:600;">Dump Frequency</td><td>When Ni &gt;200 ppm</td><td>Weekly or when &gt;50 &micro;S</td><td>Continuous DI feed</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- STAINING PREVENTION + DRYING -->
    <div class="bottom-grid">
      <div>
        <h3 class="section-title">Staining &amp; Oxidation Prevention <span class="sub">protect deposit appearance</span></h3>
        <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
          <table class="data-table compact">
            <thead><tr><th>Issue</th><th>Cause</th><th>Prevention</th></tr></thead>
            <tbody>
              <tr><td style="font-weight:600;">Rainbow tinting</td><td>Air exposure &gt;10 s after EN bath</td><td>Transfer in &lt;10 s; keep wet at all times</td></tr>
              <tr><td style="font-weight:600;">Water spots</td><td>Hard water minerals in final rinse</td><td>DI final stage; blow-off with clean compressed air</td></tr>
              <tr><td style="font-weight:600;">White haze</td><td>Incomplete rinse of EN chemistry</td><td>Adequate cascade time; agitate parts</td></tr>
              <tr><td style="font-weight:600;">Dark staining</td><td>Nickel oxide formation from drying</td><td>Do not air-dry between rinse and post-treatment</td></tr>
              <tr><td style="font-weight:600;">Fingerprints</td><td>Handling with bare hands</td><td>Cotton or nitrile gloves for all handling after EN</td></tr>
            </tbody>
          </table>
        </div>
        <div class="insight-card" style="margin-top:8px;">
          <div class="insight-label">Why DI in the Final Stage</div>
          <div class="insight-text">Municipal water contains dissolved minerals (Ca, Mg, silica) that leave visible spots on the EN surface when parts dry. These spots act as nucleation sites for corrosion and can cause adhesion failure if chromate or sealant is applied over them. A DI final rinse at &lt;10 &micro;S/cm ensures a spot-free surface ready for post-treatment or direct use.</div>
        </div>
      </div>
      <div>
        <h3 class="section-title">Drying Methods <span class="sub">if parts are not going directly to post-treatment</span></h3>
        <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
          <table class="data-table bath">
            <thead><tr><th>Method</th><th>Temp</th><th>Notes</th></tr></thead>
            <tbody>
              <tr><td style="font-weight:600;">Hot Air Blow-Off</td><td class="mono">150&ndash;180&deg;F (65&ndash;82&deg;C)</td><td>Fastest; use filtered, oil-free air; no water spots</td></tr>
              <tr><td style="font-weight:600;">Recirculating Oven</td><td class="mono">150&ndash;200&deg;F (65&ndash;93&deg;C)</td><td>Uniform; good for racks; keep below 260&deg;F if corrosion resistance is required</td></tr>
              <tr><td style="font-weight:600;">Spin Dry (barrel work)</td><td class="mono">Ambient</td><td>For barrel-plated small parts; centrifugal water removal</td></tr>
              <tr><td style="font-weight:600;">Air Dry (ambient)</td><td class="mono">Ambient</td><td>Slowest; highest risk of staining; avoid if possible</td></tr>
            </tbody>
          </table>
        </div>

        <h3 class="section-title" style="margin-top:8px;">Transfer Time Requirements <span class="sub">critical windows</span></h3>
        <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
          <table class="data-table bath">
            <thead><tr><th>Transfer</th><th>Max Time</th><th>Reason</th></tr></thead>
            <tbody>
              <tr><td style="font-weight:600;">EN bath &rarr; Rinse 1</td><td class="mono" style="color:var(--coral);font-weight:600;">&lt;10 sec</td><td>Prevent oxidation/staining</td></tr>
              <tr><td style="font-weight:600;">Rinse &rarr; Rinse</td><td class="mono">&lt;30 sec</td><td>Keep parts wet</td></tr>
              <tr><td style="font-weight:600;">Final rinse &rarr; Dry/Post-treat</td><td class="mono">&lt;60 sec</td><td>Minimize air exposure</td></tr>
              <tr><td style="font-weight:600;">Plating &rarr; HE Bake (high-strength steel)</td><td class="mono" style="color:var(--coral);font-weight:600;">&lt;4 hours</td><td>ASTM B849 mandatory for &ge;40 HRC</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <div class="safety-card">
      <div class="safety-head">&#9888; Safety &mdash; Final Rinse</div>
      <div class="safety-body">Rinse water in the first stage contains <strong>dissolved nickel</strong> (Ni&sup2;&#8314;) at concentrations up to 100+ ppm. Soluble nickel compounds are a <strong>GHS Category 1A carcinogen</strong> (IARC Group 1 &mdash; known human carcinogen by inhalation) and skin sensitizer. Do NOT discharge nickel-bearing rinse water without treatment &mdash; regulatory limits are typically 0.5&ndash;3 ppm Ni. Wear chemical-resistant gloves. Avoid skin contact with rinse water. Emergency shower and eyewash within 10 seconds.</div>
    </div>
"""

TECH_BODY_ES["07"] = """
    <div class="glass rule-card">
      <div class="rule-num">&lt;10s</div>
      <div class="rule-body">
        <div class="rule-label">Tiempo de Transferencia &lt;10 Segundos &mdash; Piezas al Enjuague Inmediatamente</div>
        <div class="rule-text">El enjuague final remueve la qu&iacute;mica residual del EN de la superficie del dep&oacute;sito antes del post-tratamiento. El tiempo de transferencia es cr&iacute;tico: las superficies de EN reci&eacute;n depositadas se oxidan y manchan r&aacute;pidamente al aire. Las piezas deben moverse del ba&ntilde;o EN al primer tanque de enjuague dentro de 10 segundos para prevenir decoloraci&oacute;n, manchas de agua e iridiscencia que pueden comprometer la adherencia de recubrimientos posteriores o causar rechazo cosm&eacute;tico.</div>
      </div>
    </div>

    <!-- TABLA SECUENCIA DE ENJUAGUE -->
    <div>
      <h3 class="section-title">Secuencia de Enjuague &mdash; Despu&eacute;s del Ba&ntilde;o EN <span class="sub">multietapa recomendado</span></h3>
      <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
        <table class="data-table compact">
          <thead><tr><th>Etapa</th><th>Tipo</th><th>Agua</th><th>Temp</th><th>Tiempo</th><th>Prop&oacute;sito</th></tr></thead>
          <tbody>
            <tr><td class="mono" style="font-weight:600;color:var(--teal);">R1</td><td>Recuperaci&oacute;n de Arrastre</td><td>Agua de grifo</td><td class="mono">Ambiente</td><td class="mono">15&ndash;30 s</td><td>Capturar arrastre de Ni para retorno al ba&ntilde;o o tratamiento</td></tr>
            <tr><td class="mono" style="font-weight:600;color:var(--teal);">R2</td><td>Enjuague en Cascada</td><td>Agua de grifo</td><td class="mono">Ambiente</td><td class="mono">30&ndash;60 s</td><td>Remoci&oacute;n gruesa de qu&iacute;mica residual</td></tr>
            <tr><td class="mono" style="font-weight:600;color:var(--teal);">R3</td><td>Enjuague DI Final</td><td>Agua DI</td><td class="mono">Fr&iacute;o / tibio</td><td class="mono">30&ndash;60 s</td><td>Superficie sin manchas; prevenir dep&oacute;sitos minerales; &lt;10 &micro;S/cm</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- TABLA CALIDAD DE AGUA -->
    <div>
      <h3 class="section-title">Requisitos de Calidad de Agua <span class="sub">por etapa de enjuague</span></h3>
      <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
        <table class="data-table compact">
          <thead><tr><th>Par&aacute;metro</th><th>Arrastre (R1)</th><th>Cascada (R2)</th><th>DI Final (R3)</th></tr></thead>
          <tbody>
            <tr><td style="font-weight:600;">Conductividad</td><td class="mono">&lt;500 &micro;S/cm</td><td class="mono">&lt;50 &micro;S/cm</td><td class="mono">&lt;10 &micro;S/cm</td></tr>
            <tr><td style="font-weight:600;">N&iacute;quel</td><td class="mono">&lt;100 ppm (recuperar)</td><td class="mono">&lt;5 ppm</td><td class="mono">&lt;0.5 ppm</td></tr>
            <tr><td style="font-weight:600;">pH</td><td class="mono">4&ndash;6</td><td class="mono">5&ndash;7</td><td class="mono">5.5&ndash;7.5</td></tr>
            <tr><td style="font-weight:600;">Fuente de Agua</td><td>Municipal OK</td><td>Municipal OK</td><td>Solo DI</td></tr>
            <tr><td style="font-weight:600;">Frecuencia de Vaciado</td><td>Cuando Ni &gt;200 ppm</td><td>Semanal o cuando &gt;50 &micro;S</td><td>Alimentaci&oacute;n DI continua</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- PREVENCI&Oacute;N DE MANCHAS + SECADO -->
    <div class="bottom-grid">
      <div>
        <h3 class="section-title">Prevenci&oacute;n de Manchas y Oxidaci&oacute;n <span class="sub">proteger apariencia del dep&oacute;sito</span></h3>
        <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
          <table class="data-table compact">
            <thead><tr><th>Problema</th><th>Causa</th><th>Prevenci&oacute;n</th></tr></thead>
            <tbody>
              <tr><td style="font-weight:600;">Tinte iridiscente</td><td>Exposici&oacute;n al aire &gt;10 s despu&eacute;s del ba&ntilde;o EN</td><td>Transferir en &lt;10 s; mantener mojado en todo momento</td></tr>
              <tr><td style="font-weight:600;">Manchas de agua</td><td>Minerales de agua dura en enjuague final</td><td>Etapa final DI; soplar con aire comprimido limpio</td></tr>
              <tr><td style="font-weight:600;">Neblina blanca</td><td>Enjuague incompleto de qu&iacute;mica EN</td><td>Tiempo adecuado en cascada; agitar piezas</td></tr>
              <tr><td style="font-weight:600;">Manchas oscuras</td><td>Formaci&oacute;n de &oacute;xido de n&iacute;quel por secado</td><td>No secar al aire entre enjuague y post-tratamiento</td></tr>
              <tr><td style="font-weight:600;">Huellas digitales</td><td>Manejo con manos desnudas</td><td>Guantes de algod&oacute;n o nitrilo para todo manejo despu&eacute;s del EN</td></tr>
            </tbody>
          </table>
        </div>
        <div class="insight-card" style="margin-top:8px;">
          <div class="insight-label">Por Qu&eacute; DI en la Etapa Final</div>
          <div class="insight-text">El agua municipal contiene minerales disueltos (Ca, Mg, s&iacute;lice) que dejan manchas visibles en la superficie EN cuando las piezas se secan. Estas manchas act&uacute;an como sitios de nucleaci&oacute;n para corrosi&oacute;n y pueden causar fallas de adherencia si se aplica cromato o sellador sobre ellas. Un enjuague DI final a &lt;10 &micro;S/cm asegura una superficie sin manchas lista para post-tratamiento o uso directo.</div>
        </div>
      </div>
      <div>
        <h3 class="section-title">M&eacute;todos de Secado <span class="sub">si las piezas no van directo a post-tratamiento</span></h3>
        <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
          <table class="data-table bath">
            <thead><tr><th>M&eacute;todo</th><th>Temp</th><th>Notas</th></tr></thead>
            <tbody>
              <tr><td style="font-weight:600;">Soplo de Aire Caliente</td><td class="mono">65&ndash;82&deg;C</td><td>M&aacute;s r&aacute;pido; use aire filtrado, libre de aceite; sin manchas</td></tr>
              <tr><td style="font-weight:600;">Horno de Recirculaci&oacute;n</td><td class="mono">65&ndash;93&deg;C</td><td>Uniforme; bueno para racks; mantenga debajo de 127&deg;C si se requiere resistencia a corrosi&oacute;n</td></tr>
              <tr><td style="font-weight:600;">Secado Centr&iacute;fugo (barril)</td><td class="mono">Ambiente</td><td>Para piezas peque&ntilde;as en barril; remoci&oacute;n centr&iacute;fuga</td></tr>
              <tr><td style="font-weight:600;">Secado al Aire (ambiente)</td><td class="mono">Ambiente</td><td>M&aacute;s lento; mayor riesgo de manchas; evite si es posible</td></tr>
            </tbody>
          </table>
        </div>

        <h3 class="section-title" style="margin-top:8px;">Requisitos de Tiempo de Transferencia <span class="sub">ventanas cr&iacute;ticas</span></h3>
        <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
          <table class="data-table bath">
            <thead><tr><th>Transferencia</th><th>Tiempo M&aacute;x</th><th>Raz&oacute;n</th></tr></thead>
            <tbody>
              <tr><td style="font-weight:600;">Ba&ntilde;o EN &rarr; Enjuague 1</td><td class="mono" style="color:var(--coral);font-weight:600;">&lt;10 s</td><td>Prevenir oxidaci&oacute;n/manchas</td></tr>
              <tr><td style="font-weight:600;">Enjuague &rarr; Enjuague</td><td class="mono">&lt;30 s</td><td>Mantener piezas mojadas</td></tr>
              <tr><td style="font-weight:600;">Enjuague final &rarr; Secado/Post-trat</td><td class="mono">&lt;60 s</td><td>Minimizar exposici&oacute;n al aire</td></tr>
              <tr><td style="font-weight:600;">Dep&oacute;sito &rarr; Horneado HE (acero alta resist.)</td><td class="mono" style="color:var(--coral);font-weight:600;">&lt;4 horas</td><td>ASTM B849 obligatorio para &ge;40 HRC</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <div class="safety-card">
      <div class="safety-head">&#9888; Seguridad &mdash; Enjuague Final</div>
      <div class="safety-body">El agua de enjuague en la primera etapa contiene <strong>n&iacute;quel disuelto</strong> (Ni&sup2;&#8314;) a concentraciones de hasta 100+ ppm. Los compuestos solubles de n&iacute;quel son <strong>carcin&oacute;geno GHS Categor&iacute;a 1A</strong> (IARC Grupo 1 &mdash; carcin&oacute;geno humano conocido por inhalaci&oacute;n) y sensibilizante cut&aacute;neo. NO descargue agua de enjuague con n&iacute;quel sin tratamiento &mdash; l&iacute;mites regulatorios son t&iacute;picamente 0.5&ndash;3 ppm Ni. Use guantes resistentes a qu&iacute;micos. Evite contacto de piel con agua de enjuague. Regadera y lavaojos a 10 segundos.</div>
    </div>
"""

SF_BODY_EN["07"] = """
    <div class="glass key-card">
      <div class="key-num">&lt;10s</div>
      <div class="key-label">Transfer Time &mdash; Parts to Rinse Immediately</div>
      <div class="key-text">After the EN bath, parts must go into the rinse tank within 10 seconds. Freshly plated EN oxidizes and stains fast in air. Keep parts wet at all times. Use DI water in the final rinse stage for a spot-free surface.</div>
    </div>

    <div class="glass" style="padding:10px 12px;">
      <div class="section-title">Rinse Parameters</div>
      <table class="flow-table">
        <thead><tr><th>Stage</th><th>Water</th><th>Time</th><th>Purpose</th></tr></thead>
        <tbody>
          <tr><td class="mono">R1</td><td>Tap water</td><td class="mono">15&ndash;30 sec</td><td>Capture Ni drag-out</td></tr>
          <tr><td class="mono">R2</td><td>Tap water</td><td class="mono">30&ndash;60 sec</td><td>Remove residual chemistry</td></tr>
          <tr><td class="mono">R3</td><td class="mono">DI water</td><td class="mono">30&ndash;60 sec</td><td>Spot-free surface (&lt;10 &micro;S/cm)</td></tr>
        </tbody>
      </table>
    </div>

    <div class="glass" style="padding:10px 12px;">
      <div class="section-title">Key Rules <span style="font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:.10em;color:var(--muted);margin-left:8px;">FOLLOW EVERY LOAD</span></div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;">
        <div style="padding:8px 10px;border-radius:8px;background:rgba(224,92,92,.08);border:1px solid rgba(224,92,92,.2);"><div style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:13px;color:var(--coral);letter-spacing:.04em;margin-bottom:3px;">TRANSFER IN &lt;10 SEC</div><div style="font-size:10.5px;color:var(--muted);line-height:1.35;">Move parts from EN bath to first rinse immediately. Air exposure causes staining and oxidation.</div></div>
        <div style="padding:8px 10px;border-radius:8px;background:rgba(46,196,182,.08);border:1px solid rgba(46,196,182,.2);"><div style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:13px;color:var(--teal);letter-spacing:.04em;margin-bottom:3px;">DI WATER FINAL STAGE</div><div style="font-size:10.5px;color:var(--muted);line-height:1.35;">DI water in the last rinse prevents water spots. Tap water leaves mineral deposits on the surface.</div></div>
        <div style="padding:8px 10px;border-radius:8px;background:rgba(232,160,32,.08);border:1px solid rgba(232,160,32,.2);"><div style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:13px;color:var(--amber);letter-spacing:.04em;margin-bottom:3px;">KEEP PARTS WET</div><div style="font-size:10.5px;color:var(--muted);line-height:1.35;">Never let parts dry between rinse stages. Wet surface = clean surface. Dry surface = stains and oxide.</div></div>
        <div style="padding:8px 10px;border-radius:8px;background:rgba(39,174,96,.08);border:1px solid rgba(39,174,96,.2);"><div style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:13px;color:var(--emerald);letter-spacing:.04em;margin-bottom:3px;">NO BARE HANDS</div><div style="font-size:10.5px;color:var(--muted);line-height:1.35;">Wear cotton or nitrile gloves when handling parts after EN plating. Fingerprints cause corrosion initiation.</div></div>
      </div>
    </div>

    <div class="compare-row">
      <div class="compare-card glass do"><div class="compare-head good">&#10003; Do</div><ul class="compare-list"><li>Transfer from EN bath to rinse in &lt;10 seconds</li><li>Use DI water in the final rinse stage</li><li>Agitate parts in each rinse tank</li><li>Wear gloves when handling plated parts</li><li>Move to post-treatment or drying promptly</li></ul></div>
      <div class="compare-card glass dont"><div class="compare-head bad">&#10007; Don&rsquo;t</div><ul class="compare-list"><li>Let parts sit in air after the EN bath</li><li>Use tap water in the final rinse stage</li><li>Touch plated surfaces with bare hands</li><li>Skip the drag-out recovery rinse</li><li>Stack plated parts wet against each other</li></ul></div>
    </div>

    <div class="insight-card">
      <div class="insight-label">HE Bake Countdown Starts at Plating</div>
      <div class="insight-text">For high-strength steel (&ge;40 HRC), the 4-hour countdown for HE bake starts when parts leave the EN bath, not when they finish rinsing. Every minute spent in rinsing, drying, and handling counts. Plan your post-plating workflow to get parts into the bake oven well within the 4-hour window per ASTM B849.</div>
    </div>

    <div class="glass safety-card">
      <div class="section-title coral">&#9888; Safety &mdash; Final Rinse</div>
      <div class="safety-text">Rinse water contains <strong>dissolved nickel</strong> &mdash; GHS Category 1A carcinogen (IARC Group 1). Wear chemical-resistant gloves. Avoid skin contact. Do not discharge rinse water without treatment. Emergency shower and eyewash within 10 seconds.</div>
    </div>
"""

SF_BODY_ES["07"] = """
    <div class="glass key-card">
      <div class="key-num">&lt;10s</div>
      <div class="key-label">Tiempo de Transferencia &mdash; Piezas al Enjuague Inmediatamente</div>
      <div class="key-text">Despu&eacute;s del ba&ntilde;o EN, las piezas deben ir al tanque de enjuague dentro de 10 segundos. El EN reci&eacute;n depositado se oxida y mancha r&aacute;pido al aire. Mantenga las piezas mojadas en todo momento. Use agua DI en la etapa final de enjuague para una superficie sin manchas.</div>
    </div>

    <div class="glass" style="padding:10px 12px;">
      <div class="section-title">Par&aacute;metros de Enjuague</div>
      <table class="flow-table">
        <thead><tr><th>Etapa</th><th>Agua</th><th>Tiempo</th><th>Prop&oacute;sito</th></tr></thead>
        <tbody>
          <tr><td class="mono">R1</td><td>Agua de grifo</td><td class="mono">15&ndash;30 s</td><td>Capturar arrastre de Ni</td></tr>
          <tr><td class="mono">R2</td><td>Agua de grifo</td><td class="mono">30&ndash;60 s</td><td>Remover qu&iacute;mica residual</td></tr>
          <tr><td class="mono">R3</td><td class="mono">Agua DI</td><td class="mono">30&ndash;60 s</td><td>Superficie sin manchas (&lt;10 &micro;S/cm)</td></tr>
        </tbody>
      </table>
    </div>

    <div class="glass" style="padding:10px 12px;">
      <div class="section-title">Reglas Clave <span style="font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:.10em;color:var(--muted);margin-left:8px;">SIGA EN CADA CARGA</span></div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;">
        <div style="padding:8px 10px;border-radius:8px;background:rgba(224,92,92,.08);border:1px solid rgba(224,92,92,.2);"><div style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:13px;color:var(--coral);letter-spacing:.04em;margin-bottom:3px;">TRANSFIERA EN &lt;10 S</div><div style="font-size:10.5px;color:var(--muted);line-height:1.35;">Mueva piezas del ba&ntilde;o EN al primer enjuague inmediatamente. La exposici&oacute;n al aire causa manchas y oxidaci&oacute;n.</div></div>
        <div style="padding:8px 10px;border-radius:8px;background:rgba(46,196,182,.08);border:1px solid rgba(46,196,182,.2);"><div style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:13px;color:var(--teal);letter-spacing:.04em;margin-bottom:3px;">AGUA DI EN ETAPA FINAL</div><div style="font-size:10.5px;color:var(--muted);line-height:1.35;">Agua DI en el &uacute;ltimo enjuague previene manchas de agua. El agua de grifo deja dep&oacute;sitos minerales en la superficie.</div></div>
        <div style="padding:8px 10px;border-radius:8px;background:rgba(232,160,32,.08);border:1px solid rgba(232,160,32,.2);"><div style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:13px;color:var(--amber);letter-spacing:.04em;margin-bottom:3px;">MANTENGA PIEZAS MOJADAS</div><div style="font-size:10.5px;color:var(--muted);line-height:1.35;">Nunca deje secar las piezas entre etapas de enjuague. Superficie mojada = superficie limpia. Superficie seca = manchas y &oacute;xido.</div></div>
        <div style="padding:8px 10px;border-radius:8px;background:rgba(39,174,96,.08);border:1px solid rgba(39,174,96,.2);"><div style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:13px;color:var(--emerald);letter-spacing:.04em;margin-bottom:3px;">SIN MANOS DESNUDAS</div><div style="font-size:10.5px;color:var(--muted);line-height:1.35;">Use guantes de algod&oacute;n o nitrilo al manejar piezas despu&eacute;s del EN. Las huellas digitales causan inicio de corrosi&oacute;n.</div></div>
      </div>
    </div>

    <div class="compare-row">
      <div class="compare-card glass do"><div class="compare-head good">&#10003; Haga</div><ul class="compare-list"><li>Transfiera del ba&ntilde;o EN al enjuague en &lt;10 segundos</li><li>Use agua DI en la etapa final de enjuague</li><li>Agite las piezas en cada tanque de enjuague</li><li>Use guantes al manejar piezas depositadas</li><li>Pase a post-tratamiento o secado r&aacute;pidamente</li></ul></div>
      <div class="compare-card glass dont"><div class="compare-head bad">&#10007; No Haga</div><ul class="compare-list"><li>Dejar piezas al aire despu&eacute;s del ba&ntilde;o EN</li><li>Usar agua de grifo en la etapa final de enjuague</li><li>Tocar superficies depositadas con manos desnudas</li><li>Omitir el enjuague de recuperaci&oacute;n de arrastre</li><li>Apilar piezas mojadas depositadas una contra otra</li></ul></div>
    </div>

    <div class="insight-card">
      <div class="insight-label">Cuenta Regresiva de Horneado HE Comienza al Depositar</div>
      <div class="insight-text">Para acero de alta resistencia (&ge;40 HRC), la cuenta regresiva de 4 horas para horneado HE comienza cuando las piezas salen del ba&ntilde;o EN, no cuando terminan de enjuagarse. Cada minuto en enjuague, secado y manejo cuenta. Planifique su flujo de trabajo para meter piezas al horno dentro de las 4 horas seg&uacute;n ASTM B849.</div>
    </div>

    <div class="glass safety-card">
      <div class="section-title coral">&#9888; Seguridad &mdash; Enjuague Final</div>
      <div class="safety-text">El agua de enjuague contiene <strong>n&iacute;quel disuelto</strong> &mdash; carcin&oacute;geno GHS Categor&iacute;a 1A (IARC Grupo 1). Use guantes resistentes a qu&iacute;micos. Evite contacto con la piel. No descargue agua de enjuague sin tratamiento. Regadera y lavaojos a 10 segundos.</div>
    </div>
"""

# =====================================================================
# POSTER 08 — POST TREATMENT
# =====================================================================
TECH_BODY_EN["08"] = """
    <div class="glass rule-card">
      <div class="rule-num">&lt;4hr</div>
      <div class="rule-body">
        <div class="rule-label">HE Bake Within 4 Hours for High-Strength Steel</div>
        <div class="rule-text">Post-treatment transforms the as-plated EN deposit. Hydrogen embrittlement (HE) bake is mandatory within 4 hours for high-strength steel (&ge;40 HRC) per ASTM B849. Higher bake temperatures increase hardness but destroy the amorphous structure, corrosion resistance, and non-magnetic property. Chromate conversion or sealant coatings add additional corrosion protection. Choosing the right post-treatment depends on which deposit properties the specification requires.</div>
      </div>
    </div>

    <!-- BAKE SCHEDULE TABLE -->
    <div>
      <h3 class="section-title">Bake Schedule <span class="sub">temperature &times; time &times; purpose</span></h3>
      <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
        <table class="data-table compact">
          <thead><tr><th>Bake Type</th><th>Temp &deg;C (&deg;F)</th><th>Time</th><th>Purpose</th><th>Spec Reference</th></tr></thead>
          <tbody>
            <tr><td style="font-weight:600;color:var(--emerald);">HE Relief</td><td class="mono">190&deg;C (375&deg;F)</td><td class="mono">1&ndash;4+ hr</td><td>Diffuse trapped hydrogen out of steel; mandatory for &ge;40 HRC</td><td class="mono">ASTM B849</td></tr>
            <tr><td style="font-weight:600;color:var(--amber);">Adhesion Bake</td><td class="mono">190&ndash;210&deg;C (375&ndash;410&deg;F)</td><td class="mono">1&ndash;2 hr</td><td>Improve adhesion on steel substrates</td><td class="mono">AMS 2404</td></tr>
            <tr><td style="font-weight:600;color:var(--amber);">Moderate Hardness</td><td class="mono">260&deg;C (500&deg;F)</td><td class="mono">1 hr</td><td>Increase hardness to 600&ndash;750 HV; beginning of crystallization</td><td class="mono">ASTM B733</td></tr>
            <tr><td style="font-weight:600;color:var(--coral);">Full Hardness</td><td class="mono">400&deg;C (750&deg;F)</td><td class="mono">1 hr</td><td>Maximum hardness 850&ndash;1000 HV; fully crystallized</td><td class="mono">ASTM B733</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- DEPOSIT PROPERTIES: AS-PLATED vs BAKE TEMPS -->
    <div>
      <h3 class="section-title">Deposit Properties &mdash; Effect of Bake Temperature <span class="sub">high phos 10&ndash;13% P</span></h3>
      <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
        <table class="data-table compact">
          <thead><tr><th>Property</th><th>As-Plated</th><th>190&deg;C/4hr</th><th>260&deg;C/1hr</th><th>400&deg;C/1hr</th></tr></thead>
          <tbody>
            <tr><td style="font-weight:600;">Hardness</td><td class="mono">450&ndash;550 HV</td><td class="mono">500&ndash;600 HV</td><td class="mono">600&ndash;750 HV</td><td class="mono" style="color:var(--amber);font-weight:600;">850&ndash;1000 HV</td></tr>
            <tr><td style="font-weight:600;">Structure</td><td style="color:var(--teal);">Fully amorphous</td><td style="color:var(--teal);">Amorphous (preserved)</td><td style="color:var(--coral);">Transitioning to crystalline</td><td style="color:var(--coral);">Crystalline (Ni + Ni&#8323;P)</td></tr>
            <tr><td style="font-weight:600;">Corrosion (NSS)</td><td class="mono" style="color:var(--teal);">&gt;1000 hr</td><td class="mono" style="color:var(--teal);">&gt;1000 hr</td><td class="mono" style="color:var(--coral);">500&ndash;800 hr</td><td class="mono" style="color:var(--coral);">200&ndash;400 hr</td></tr>
            <tr><td style="font-weight:600;">Magnetic</td><td style="color:var(--teal);">Non-magnetic</td><td style="color:var(--teal);">Non-magnetic</td><td style="color:var(--coral);">Weakly magnetic</td><td style="color:var(--coral);">Magnetic</td></tr>
            <tr><td style="font-weight:600;">Internal Stress</td><td class="mono">Low compressive</td><td class="mono">Low compressive</td><td class="mono">Near zero</td><td class="mono">Tensile</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- BAKE TEMPERATURE VS PROPERTIES SVG -->
    <div class="glass" style="padding:10px 14px;">
      <h3 class="section-title" style="margin-bottom:4px;">Bake Temperature vs Deposit Properties <span class="sub">hardness &uarr; corrosion &darr; at crystallization threshold</span></h3>
      <svg viewBox="0 0 1100 150" width="100%" height="150" fill="none" xmlns="http://www.w3.org/2000/svg">
        <!-- Magnetic status bar at top -->
        <rect x="120" y="2" width="420" height="16" rx="3" fill="rgba(46,196,182,.12)" stroke="var(--teal)" stroke-width="0.8"/>
        <text x="330" y="13" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" letter-spacing=".06em">MAGNETIC: OFF</text>
        <rect x="540" y="2" width="420" height="16" rx="3" fill="rgba(224,92,92,.12)" stroke="var(--coral)" stroke-width="0.8"/>
        <text x="750" y="13" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" letter-spacing=".06em">MAGNETIC: ON</text>
        <!-- Y-axis labels -->
        <text x="15" y="40" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" letter-spacing=".04em">HV</text>
        <text x="8" y="52" fill="var(--amber)" font-family="JetBrains Mono,monospace" font-size="7">1000</text>
        <text x="12" y="80" fill="var(--amber)" font-family="JetBrains Mono,monospace" font-size="7">650</text>
        <text x="12" y="108" fill="var(--amber)" font-family="JetBrains Mono,monospace" font-size="7">500</text>
        <text x="1075" y="40" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" letter-spacing=".04em">NSS</text>
        <text x="1060" y="52" fill="var(--teal)" font-family="JetBrains Mono,monospace" font-size="7">1000+</text>
        <text x="1060" y="92" fill="var(--teal)" font-family="JetBrains Mono,monospace" font-size="7">500</text>
        <text x="1060" y="120" fill="var(--teal)" font-family="JetBrains Mono,monospace" font-size="7">200</text>
        <!-- X-axis line -->
        <line x1="50" y1="130" x2="1040" y2="130" stroke="var(--faint)" stroke-width="1"/>
        <!-- X-axis labels -->
        <text x="120" y="143" text-anchor="middle" fill="var(--text)" font-family="Barlow Condensed,sans-serif" font-weight="700" font-size="9">As-Plated</text>
        <text x="330" y="143" text-anchor="middle" fill="var(--text)" font-family="Barlow Condensed,sans-serif" font-weight="700" font-size="9">190&deg;C (HE)</text>
        <text x="540" y="143" text-anchor="middle" fill="var(--text)" font-family="Barlow Condensed,sans-serif" font-weight="700" font-size="9">260&deg;C</text>
        <text x="820" y="143" text-anchor="middle" fill="var(--text)" font-family="Barlow Condensed,sans-serif" font-weight="700" font-size="9">400&deg;C (Full)</text>
        <!-- Crystallization threshold line -->
        <line x1="540" y1="22" x2="540" y2="128" stroke="var(--coral)" stroke-width="2" stroke-dasharray="6,3"/>
        <text x="540" y="33" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="9" letter-spacing=".05em">CRYSTALLIZATION THRESHOLD</text>
        <!-- Left label -->
        <text x="225" y="44" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="700" font-size="9" letter-spacing=".04em">AMORPHOUS &mdash; Non-magnetic</text>
        <!-- Right label -->
        <text x="700" y="44" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="700" font-size="9" letter-spacing=".04em">CRYSTALLINE &mdash; Magnetic</text>
        <!-- Hardness curve (amber) - ascending: 500, 500, 650, 950 -->
        <circle cx="120" cy="108" r="4" fill="var(--amber)"/>
        <circle cx="330" cy="108" r="4" fill="var(--amber)"/>
        <circle cx="540" cy="80" r="4" fill="var(--amber)"/>
        <circle cx="820" cy="48" r="5" fill="var(--amber)"/>
        <polyline points="120,108 330,108 540,80 820,48" stroke="var(--amber)" stroke-width="2" fill="none"/>
        <text x="850" y="48" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="9">Hardness</text>
        <!-- Corrosion curve (teal) - descending: 1000+, 1000+, 500, 200 -->
        <circle cx="120" cy="52" r="4" fill="var(--teal)"/>
        <circle cx="330" cy="52" r="4" fill="var(--teal)"/>
        <circle cx="540" cy="92" r="4" fill="var(--teal)"/>
        <circle cx="820" cy="118" r="5" fill="var(--teal)"/>
        <polyline points="120,52 330,52 540,92 820,118" stroke="var(--teal)" stroke-width="2" fill="none"/>
        <text x="850" y="118" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="9">Salt Spray</text>
        <!-- Grid dots for reference -->
        <line x1="120" y1="130" x2="120" y2="126" stroke="var(--faint)" stroke-width="1"/>
        <line x1="330" y1="130" x2="330" y2="126" stroke="var(--faint)" stroke-width="1"/>
        <line x1="540" y1="130" x2="540" y2="126" stroke="var(--faint)" stroke-width="1"/>
        <line x1="820" y1="130" x2="820" y2="126" stroke="var(--faint)" stroke-width="1"/>
      </svg>
    </div>

    <!-- BAKE DECISION FLOWCHART SVG -->
    <div class="glass" style="padding:10px 14px;">
      <h3 class="section-title" style="margin-bottom:4px;">Bake Decision Flowchart <span class="sub">choose the right post-treatment</span></h3>
      <svg viewBox="0 0 1100 120" width="100%" height="120" fill="none" xmlns="http://www.w3.org/2000/svg">
        <!-- Start -->
        <rect x="30" y="15" width="140" height="35" rx="6" fill="rgba(232,160,32,.10)" stroke="var(--amber)" stroke-width="1.4"/>
        <text x="100" y="37" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11">PART PLATED</text>
        <!-- Q1: High-strength steel? -->
        <line x1="170" y1="32" x2="210" y2="32" stroke="var(--amber)" stroke-width="1.2"/><polygon points="206,29 213,32 206,35" fill="var(--amber)"/>
        <rect x="213" y="10" width="170" height="45" rx="6" fill="rgba(46,196,182,.08)" stroke="var(--teal)" stroke-width="1.2"/>
        <text x="298" y="28" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="10">HIGH-STRENGTH STEEL?</text>
        <text x="298" y="42" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="8">(&ge;40 HRC / &ge;180 ksi)</text>
        <!-- YES path -->
        <line x1="298" y1="55" x2="298" y2="75" stroke="var(--emerald)" stroke-width="1.2"/><polygon points="295,72 298,79 301,72" fill="var(--emerald)"/>
        <text x="313" y="68" fill="var(--emerald)" font-family="JetBrains Mono,monospace" font-size="8" font-weight="500">YES</text>
        <rect x="228" y="80" width="140" height="30" rx="6" fill="rgba(39,174,96,.12)" stroke="var(--emerald)" stroke-width="1.4"/>
        <text x="298" y="100" text-anchor="middle" fill="var(--emerald)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">190&deg;C / 4+ HR</text>
        <!-- NO path -->
        <line x1="383" y1="32" x2="430" y2="32" stroke="var(--amber)" stroke-width="1.2"/><polygon points="426,29 433,32 426,35" fill="var(--amber)"/>
        <text x="405" y="27" fill="var(--coral)" font-family="JetBrains Mono,monospace" font-size="8" font-weight="500">NO</text>
        <!-- Q2: Need max hardness? -->
        <rect x="433" y="10" width="160" height="45" rx="6" fill="rgba(46,196,182,.08)" stroke="var(--teal)" stroke-width="1.2"/>
        <text x="513" y="28" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="10">NEED MAX HARDNESS?</text>
        <text x="513" y="42" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="8">(&gt;800 HV wear surface)</text>
        <!-- YES to hardness -->
        <line x1="513" y1="55" x2="513" y2="75" stroke="var(--coral)" stroke-width="1.2"/><polygon points="510,72 513,79 516,72" fill="var(--coral)"/>
        <text x="528" y="68" fill="var(--emerald)" font-family="JetBrains Mono,monospace" font-size="8" font-weight="500">YES</text>
        <rect x="443" y="80" width="140" height="30" rx="6" fill="rgba(224,92,92,.12)" stroke="var(--coral)" stroke-width="1.4"/>
        <text x="513" y="100" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">400&deg;C / 1 HR</text>
        <!-- NO path -->
        <line x1="593" y1="32" x2="640" y2="32" stroke="var(--amber)" stroke-width="1.2"/><polygon points="636,29 643,32 636,35" fill="var(--amber)"/>
        <text x="616" y="27" fill="var(--coral)" font-family="JetBrains Mono,monospace" font-size="8" font-weight="500">NO</text>
        <!-- Q3: Need corrosion + non-mag? -->
        <rect x="643" y="10" width="175" height="45" rx="6" fill="rgba(46,196,182,.08)" stroke="var(--teal)" stroke-width="1.2"/>
        <text x="730" y="28" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="10">NEED CORROSION RES.</text>
        <text x="730" y="42" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="8">or non-magnetic?</text>
        <!-- YES to corrosion -->
        <line x1="730" y1="55" x2="730" y2="75" stroke="var(--teal)" stroke-width="1.2"/><polygon points="727,72 730,79 733,72" fill="var(--teal)"/>
        <text x="745" y="68" fill="var(--emerald)" font-family="JetBrains Mono,monospace" font-size="8" font-weight="500">YES</text>
        <rect x="655" y="80" width="150" height="30" rx="6" fill="rgba(46,196,182,.12)" stroke="var(--teal)" stroke-width="1.4"/>
        <text x="730" y="100" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">DO NOT BAKE &gt;260&deg;C</text>
        <!-- NO path to chromate/sealant -->
        <line x1="818" y1="32" x2="865" y2="32" stroke="var(--amber)" stroke-width="1.2"/><polygon points="861,29 868,32 861,35" fill="var(--amber)"/>
        <text x="841" y="27" fill="var(--coral)" font-family="JetBrains Mono,monospace" font-size="8" font-weight="500">NO</text>
        <rect x="868" y="10" width="180" height="45" rx="6" fill="rgba(39,174,96,.08)" stroke="var(--emerald)" stroke-width="1.2"/>
        <text x="958" y="28" text-anchor="middle" fill="var(--emerald)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="10">CHROMATE / SEALANT</text>
        <text x="958" y="42" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="8">or ship as-plated per spec</text>
      </svg>
    </div>

    <!-- CHROMATE / SEALANT OPTIONS -->
    <div class="bottom-grid">
      <div>
        <h3 class="section-title">Chromate &amp; Sealant Options <span class="sub">supplemental corrosion protection</span></h3>
        <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
          <table class="data-table compact">
            <thead><tr><th>Treatment</th><th>Type</th><th>Benefit</th><th>Notes</th></tr></thead>
            <tbody>
              <tr><td style="font-weight:600;">Hex Chrome (Cr&sup3;&#8314;&amp;Cr&#8310;&#8314;)</td><td>Chromate conversion</td><td>Best corrosion boost; self-healing</td><td>RoHS restricted; declining use</td></tr>
              <tr><td style="font-weight:600;">Trivalent Chrome (Cr&sup3;&#8314;)</td><td>Chromate conversion</td><td>Good corrosion; RoHS compliant</td><td>Does not self-heal; replacing hex</td></tr>
              <tr><td style="font-weight:600;">Silicate Sealant</td><td>Inorganic sealant</td><td>Pore sealing; mild corrosion boost</td><td>Thin coating; does not change appearance</td></tr>
              <tr><td style="font-weight:600;">Organic Topcoat</td><td>Polymer sealant</td><td>Hydrophobic; additional barrier</td><td>May affect dimensions; verify with spec</td></tr>
            </tbody>
          </table>
        </div>
      </div>
      <div>
        <div class="insight-card" style="margin-bottom:8px;">
          <div class="insight-label">The Crystallization Trap</div>
          <div class="insight-text">Baking high-phos EN above 260&deg;C crystallizes the deposit into Ni + Ni&#8323;P precipitates. This dramatically increases hardness (to 850&ndash;1000 HV) but <strong>permanently destroys</strong> both the amorphous corrosion resistance (&gt;1000 hr &rarr; 200&ndash;400 hr NSS) and the non-magnetic property. If your specification requires corrosion resistance or non-magnetic behavior, <strong>do not bake above 260&deg;C</strong>. HE bake at 190&deg;C preserves both.</div>
        </div>
        <div class="insight-card">
          <div class="insight-label">HE Bake Timing</div>
          <div class="insight-text">The 4-hour window for HE bake is measured from the moment parts leave the EN bath, not from when they finish rinsing or drying. For high-strength steel (&ge;40 HRC), hydrogen absorbed during plating must be driven out before it causes cracking. Bake at 190&deg;C (375&deg;F) for at least 1 hour (4+ hours typical for &ge;52 HRC). Failure to bake within the window can result in delayed brittle fracture.</div>
        </div>
      </div>
    </div>

    <div class="safety-card">
      <div class="safety-head">&#9888; Safety &mdash; Post Treatment</div>
      <div class="safety-body"><strong>Bake ovens</strong> at 190&ndash;400&deg;C &mdash; severe burn hazard. Use heat-resistant gloves and tongs. Parts remain hot for minutes after removal. <strong>Chromate solutions</strong>: trivalent chromium is moderately toxic; hexavalent chromium is a GHS Category 1A carcinogen (IARC Group 1). Cr(VI) OSHA PEL: 5 &micro;g/m&sup3;. Full PPE including respiratory protection for hex chrome. Handle chromate-treated parts with gloves. Emergency shower and eyewash within 10 seconds of chromate stations.</div>
    </div>
"""

TECH_BODY_ES["08"] = """
    <div class="glass rule-card">
      <div class="rule-num">&lt;4hr</div>
      <div class="rule-body">
        <div class="rule-label">Horneado HE Dentro de 4 Horas para Acero de Alta Resistencia</div>
        <div class="rule-text">El post-tratamiento transforma el dep&oacute;sito EN tal como se deposit&oacute;. El horneado de alivio de fragilizaci&oacute;n por hidr&oacute;geno (HE) es obligatorio dentro de 4 horas para acero de alta resistencia (&ge;40 HRC) seg&uacute;n ASTM B849. Temperaturas m&aacute;s altas aumentan la dureza pero destruyen la estructura amorfa, la resistencia a corrosi&oacute;n y la propiedad no magn&eacute;tica. Cromato o sellador agregan protecci&oacute;n adicional. Elegir el post-tratamiento correcto depende de qu&eacute; propiedades del dep&oacute;sito requiere la especificaci&oacute;n.</div>
      </div>
    </div>

    <!-- TABLA PROGRAMA DE HORNEADO -->
    <div>
      <h3 class="section-title">Programa de Horneado <span class="sub">temperatura &times; tiempo &times; prop&oacute;sito</span></h3>
      <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
        <table class="data-table compact">
          <thead><tr><th>Tipo de Horneado</th><th>Temp &deg;C (&deg;F)</th><th>Tiempo</th><th>Prop&oacute;sito</th><th>Referencia</th></tr></thead>
          <tbody>
            <tr><td style="font-weight:600;color:var(--emerald);">Alivio HE</td><td class="mono">190&deg;C (375&deg;F)</td><td class="mono">1&ndash;4+ hr</td><td>Difundir hidr&oacute;geno atrapado fuera del acero; obligatorio para &ge;40 HRC</td><td class="mono">ASTM B849</td></tr>
            <tr><td style="font-weight:600;color:var(--amber);">Horneado de Adherencia</td><td class="mono">190&ndash;210&deg;C (375&ndash;410&deg;F)</td><td class="mono">1&ndash;2 hr</td><td>Mejorar adherencia en sustratos de acero</td><td class="mono">AMS 2404</td></tr>
            <tr><td style="font-weight:600;color:var(--amber);">Dureza Moderada</td><td class="mono">260&deg;C (500&deg;F)</td><td class="mono">1 hr</td><td>Aumentar dureza a 600&ndash;750 HV; inicio de cristalizaci&oacute;n</td><td class="mono">ASTM B733</td></tr>
            <tr><td style="font-weight:600;color:var(--coral);">Dureza M&aacute;xima</td><td class="mono">400&deg;C (750&deg;F)</td><td class="mono">1 hr</td><td>Dureza m&aacute;xima 850&ndash;1000 HV; completamente cristalizado</td><td class="mono">ASTM B733</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- TABLA PROPIEDADES DEL DEP&Oacute;SITO -->
    <div>
      <h3 class="section-title">Propiedades del Dep&oacute;sito &mdash; Efecto de Temperatura de Horneado <span class="sub">alto f&oacute;sforo 10&ndash;13% P</span></h3>
      <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
        <table class="data-table compact">
          <thead><tr><th>Propiedad</th><th>Tal como Dep.</th><th>190&deg;C/4hr</th><th>260&deg;C/1hr</th><th>400&deg;C/1hr</th></tr></thead>
          <tbody>
            <tr><td style="font-weight:600;">Dureza</td><td class="mono">450&ndash;550 HV</td><td class="mono">500&ndash;600 HV</td><td class="mono">600&ndash;750 HV</td><td class="mono" style="color:var(--amber);font-weight:600;">850&ndash;1000 HV</td></tr>
            <tr><td style="font-weight:600;">Estructura</td><td style="color:var(--teal);">Completamente amorfo</td><td style="color:var(--teal);">Amorfo (preservado)</td><td style="color:var(--coral);">Transici&oacute;n a cristalino</td><td style="color:var(--coral);">Cristalino (Ni + Ni&#8323;P)</td></tr>
            <tr><td style="font-weight:600;">Corrosi&oacute;n (NSS)</td><td class="mono" style="color:var(--teal);">&gt;1000 hr</td><td class="mono" style="color:var(--teal);">&gt;1000 hr</td><td class="mono" style="color:var(--coral);">500&ndash;800 hr</td><td class="mono" style="color:var(--coral);">200&ndash;400 hr</td></tr>
            <tr><td style="font-weight:600;">Magn&eacute;tico</td><td style="color:var(--teal);">No magn&eacute;tico</td><td style="color:var(--teal);">No magn&eacute;tico</td><td style="color:var(--coral);">D&eacute;bilmente magn&eacute;tico</td><td style="color:var(--coral);">Magn&eacute;tico</td></tr>
            <tr><td style="font-weight:600;">Estr&eacute;s Interno</td><td class="mono">Compresivo bajo</td><td class="mono">Compresivo bajo</td><td class="mono">Cerca de cero</td><td class="mono">Tensil</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- SVG TEMPERATURA DE HORNEADO VS PROPIEDADES -->
    <div class="glass" style="padding:10px 14px;">
      <h3 class="section-title" style="margin-bottom:4px;">Temperatura de Horneado vs Propiedades del Dep&oacute;sito <span class="sub">dureza &uarr; corrosi&oacute;n &darr; en umbral de cristalizaci&oacute;n</span></h3>
      <svg viewBox="0 0 1100 150" width="100%" height="150" fill="none" xmlns="http://www.w3.org/2000/svg">
        <!-- Barra de estado magn&eacute;tico arriba -->
        <rect x="120" y="2" width="420" height="16" rx="3" fill="rgba(46,196,182,.12)" stroke="var(--teal)" stroke-width="0.8"/>
        <text x="330" y="13" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" letter-spacing=".06em">MAGN&Eacute;TICO: NO</text>
        <rect x="540" y="2" width="420" height="16" rx="3" fill="rgba(224,92,92,.12)" stroke="var(--coral)" stroke-width="0.8"/>
        <text x="750" y="13" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" letter-spacing=".06em">MAGN&Eacute;TICO: S&Iacute;</text>
        <!-- Etiquetas eje Y -->
        <text x="15" y="40" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" letter-spacing=".04em">HV</text>
        <text x="8" y="52" fill="var(--amber)" font-family="JetBrains Mono,monospace" font-size="7">1000</text>
        <text x="12" y="80" fill="var(--amber)" font-family="JetBrains Mono,monospace" font-size="7">650</text>
        <text x="12" y="108" fill="var(--amber)" font-family="JetBrains Mono,monospace" font-size="7">500</text>
        <text x="1075" y="40" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="8" letter-spacing=".04em">NSS</text>
        <text x="1060" y="52" fill="var(--teal)" font-family="JetBrains Mono,monospace" font-size="7">1000+</text>
        <text x="1060" y="92" fill="var(--teal)" font-family="JetBrains Mono,monospace" font-size="7">500</text>
        <text x="1060" y="120" fill="var(--teal)" font-family="JetBrains Mono,monospace" font-size="7">200</text>
        <!-- L&iacute;nea eje X -->
        <line x1="50" y1="130" x2="1040" y2="130" stroke="var(--faint)" stroke-width="1"/>
        <!-- Etiquetas eje X -->
        <text x="120" y="143" text-anchor="middle" fill="var(--text)" font-family="Barlow Condensed,sans-serif" font-weight="700" font-size="9">Tal como Dep.</text>
        <text x="330" y="143" text-anchor="middle" fill="var(--text)" font-family="Barlow Condensed,sans-serif" font-weight="700" font-size="9">190&deg;C (HE)</text>
        <text x="540" y="143" text-anchor="middle" fill="var(--text)" font-family="Barlow Condensed,sans-serif" font-weight="700" font-size="9">260&deg;C</text>
        <text x="820" y="143" text-anchor="middle" fill="var(--text)" font-family="Barlow Condensed,sans-serif" font-weight="700" font-size="9">400&deg;C (Completo)</text>
        <!-- L&iacute;nea umbral de cristalizaci&oacute;n -->
        <line x1="540" y1="22" x2="540" y2="128" stroke="var(--coral)" stroke-width="2" stroke-dasharray="6,3"/>
        <text x="540" y="33" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="9" letter-spacing=".05em">UMBRAL DE CRISTALIZACI&Oacute;N</text>
        <!-- Etiqueta izquierda -->
        <text x="225" y="44" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="700" font-size="9" letter-spacing=".04em">AMORFO &mdash; No magn&eacute;tico</text>
        <!-- Etiqueta derecha -->
        <text x="700" y="44" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="700" font-size="9" letter-spacing=".04em">CRISTALINO &mdash; Magn&eacute;tico</text>
        <!-- Curva de dureza (amber) - ascendente: 500, 500, 650, 950 -->
        <circle cx="120" cy="108" r="4" fill="var(--amber)"/>
        <circle cx="330" cy="108" r="4" fill="var(--amber)"/>
        <circle cx="540" cy="80" r="4" fill="var(--amber)"/>
        <circle cx="820" cy="48" r="5" fill="var(--amber)"/>
        <polyline points="120,108 330,108 540,80 820,48" stroke="var(--amber)" stroke-width="2" fill="none"/>
        <text x="850" y="48" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="9">Dureza</text>
        <!-- Curva de corrosi&oacute;n (teal) - descendente: 1000+, 1000+, 500, 200 -->
        <circle cx="120" cy="52" r="4" fill="var(--teal)"/>
        <circle cx="330" cy="52" r="4" fill="var(--teal)"/>
        <circle cx="540" cy="92" r="4" fill="var(--teal)"/>
        <circle cx="820" cy="118" r="5" fill="var(--teal)"/>
        <polyline points="120,52 330,52 540,92 820,118" stroke="var(--teal)" stroke-width="2" fill="none"/>
        <text x="850" y="118" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="9">Niebla Salina</text>
        <!-- Marcas del eje X -->
        <line x1="120" y1="130" x2="120" y2="126" stroke="var(--faint)" stroke-width="1"/>
        <line x1="330" y1="130" x2="330" y2="126" stroke="var(--faint)" stroke-width="1"/>
        <line x1="540" y1="130" x2="540" y2="126" stroke="var(--faint)" stroke-width="1"/>
        <line x1="820" y1="130" x2="820" y2="126" stroke="var(--faint)" stroke-width="1"/>
      </svg>
    </div>

    <!-- SVG DIAGRAMA DE FLUJO DE DECISI&Oacute;N DE HORNEADO -->
    <div class="glass" style="padding:10px 14px;">
      <h3 class="section-title" style="margin-bottom:4px;">Diagrama de Flujo de Decisi&oacute;n de Horneado <span class="sub">elija el post-tratamiento correcto</span></h3>
      <svg viewBox="0 0 1100 120" width="100%" height="120" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect x="30" y="15" width="140" height="35" rx="6" fill="rgba(232,160,32,.10)" stroke="var(--amber)" stroke-width="1.4"/>
        <text x="100" y="37" text-anchor="middle" fill="var(--amber)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="11">PIEZA DEPOSITADA</text>
        <line x1="170" y1="32" x2="210" y2="32" stroke="var(--amber)" stroke-width="1.2"/><polygon points="206,29 213,32 206,35" fill="var(--amber)"/>
        <rect x="213" y="10" width="170" height="45" rx="6" fill="rgba(46,196,182,.08)" stroke="var(--teal)" stroke-width="1.2"/>
        <text x="298" y="28" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="10">&iquest;ACERO ALTA RESIST.?</text>
        <text x="298" y="42" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="8">(&ge;40 HRC / &ge;180 ksi)</text>
        <line x1="298" y1="55" x2="298" y2="75" stroke="var(--emerald)" stroke-width="1.2"/><polygon points="295,72 298,79 301,72" fill="var(--emerald)"/>
        <text x="313" y="68" fill="var(--emerald)" font-family="JetBrains Mono,monospace" font-size="8" font-weight="500">S&Iacute;</text>
        <rect x="228" y="80" width="140" height="30" rx="6" fill="rgba(39,174,96,.12)" stroke="var(--emerald)" stroke-width="1.4"/>
        <text x="298" y="100" text-anchor="middle" fill="var(--emerald)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">190&deg;C / 4+ HR</text>
        <line x1="383" y1="32" x2="430" y2="32" stroke="var(--amber)" stroke-width="1.2"/><polygon points="426,29 433,32 426,35" fill="var(--amber)"/>
        <text x="405" y="27" fill="var(--coral)" font-family="JetBrains Mono,monospace" font-size="8" font-weight="500">NO</text>
        <rect x="433" y="10" width="160" height="45" rx="6" fill="rgba(46,196,182,.08)" stroke="var(--teal)" stroke-width="1.2"/>
        <text x="513" y="28" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="10">&iquest;NECESITA M&Aacute;X DUREZA?</text>
        <text x="513" y="42" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="8">(&gt;800 HV superficie desgaste)</text>
        <line x1="513" y1="55" x2="513" y2="75" stroke="var(--coral)" stroke-width="1.2"/><polygon points="510,72 513,79 516,72" fill="var(--coral)"/>
        <text x="528" y="68" fill="var(--emerald)" font-family="JetBrains Mono,monospace" font-size="8" font-weight="500">S&Iacute;</text>
        <rect x="443" y="80" width="140" height="30" rx="6" fill="rgba(224,92,92,.12)" stroke="var(--coral)" stroke-width="1.4"/>
        <text x="513" y="100" text-anchor="middle" fill="var(--coral)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">400&deg;C / 1 HR</text>
        <line x1="593" y1="32" x2="640" y2="32" stroke="var(--amber)" stroke-width="1.2"/><polygon points="636,29 643,32 636,35" fill="var(--amber)"/>
        <text x="616" y="27" fill="var(--coral)" font-family="JetBrains Mono,monospace" font-size="8" font-weight="500">NO</text>
        <rect x="643" y="10" width="175" height="45" rx="6" fill="rgba(46,196,182,.08)" stroke="var(--teal)" stroke-width="1.2"/>
        <text x="730" y="28" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="10">&iquest;NECESITA RESIST. CORR.?</text>
        <text x="730" y="42" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="8">&iquest;o no magn&eacute;tico?</text>
        <line x1="730" y1="55" x2="730" y2="75" stroke="var(--teal)" stroke-width="1.2"/><polygon points="727,72 730,79 733,72" fill="var(--teal)"/>
        <text x="745" y="68" fill="var(--emerald)" font-family="JetBrains Mono,monospace" font-size="8" font-weight="500">S&Iacute;</text>
        <rect x="655" y="80" width="150" height="30" rx="6" fill="rgba(46,196,182,.12)" stroke="var(--teal)" stroke-width="1.4"/>
        <text x="730" y="100" text-anchor="middle" fill="var(--teal)" font-family="Barlow Condensed,sans-serif" font-weight="900" font-size="11">NO HORNEE &gt;260&deg;C</text>
        <line x1="818" y1="32" x2="865" y2="32" stroke="var(--amber)" stroke-width="1.2"/><polygon points="861,29 868,32 861,35" fill="var(--amber)"/>
        <text x="841" y="27" fill="var(--coral)" font-family="JetBrains Mono,monospace" font-size="8" font-weight="500">NO</text>
        <rect x="868" y="10" width="180" height="45" rx="6" fill="rgba(39,174,96,.08)" stroke="var(--emerald)" stroke-width="1.2"/>
        <text x="958" y="28" text-anchor="middle" fill="var(--emerald)" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="10">CROMATO / SELLADOR</text>
        <text x="958" y="42" text-anchor="middle" fill="var(--muted)" font-family="Inter,sans-serif" font-size="8">o env&iacute;e tal como dep. seg&uacute;n especificaci&oacute;n</text>
      </svg>
    </div>

    <!-- OPCIONES CROMATO / SELLADOR -->
    <div class="bottom-grid">
      <div>
        <h3 class="section-title">Opciones de Cromato y Sellador <span class="sub">protecci&oacute;n anticorrosi&oacute;n suplementaria</span></h3>
        <div class="glass" style="padding:0;overflow:hidden;border-radius:10px;">
          <table class="data-table compact">
            <thead><tr><th>Tratamiento</th><th>Tipo</th><th>Beneficio</th><th>Notas</th></tr></thead>
            <tbody>
              <tr><td style="font-weight:600;">Cromo Hex (Cr&sup3;&#8314;&amp;Cr&#8310;&#8314;)</td><td>Conversi&oacute;n cromato</td><td>Mejor refuerzo anticorrosi&oacute;n; auto-reparable</td><td>Restringido por RoHS; uso en declive</td></tr>
              <tr><td style="font-weight:600;">Cromo Trivalente (Cr&sup3;&#8314;)</td><td>Conversi&oacute;n cromato</td><td>Buena corrosi&oacute;n; cumple RoHS</td><td>No se auto-repara; reemplaza hex</td></tr>
              <tr><td style="font-weight:600;">Sellador de Silicato</td><td>Sellador inorg&aacute;nico</td><td>Sella poros; refuerzo leve corrosi&oacute;n</td><td>Recubrimiento delgado; no cambia apariencia</td></tr>
              <tr><td style="font-weight:600;">Recubrimiento Org&aacute;nico</td><td>Sellador polim&eacute;rico</td><td>Hidrof&oacute;bico; barrera adicional</td><td>Puede afectar dimensiones; verificar con especificaci&oacute;n</td></tr>
            </tbody>
          </table>
        </div>
      </div>
      <div>
        <div class="insight-card" style="margin-bottom:8px;">
          <div class="insight-label">La Trampa de la Cristalizaci&oacute;n</div>
          <div class="insight-text">Hornear EN de alto f&oacute;sforo por encima de 260&deg;C cristaliza el dep&oacute;sito en precipitados Ni + Ni&#8323;P. Esto aumenta dram&aacute;ticamente la dureza (a 850&ndash;1000 HV) pero <strong>destruye permanentemente</strong> tanto la resistencia a corrosi&oacute;n amorfa (&gt;1000 hr &rarr; 200&ndash;400 hr NSS) como la propiedad no magn&eacute;tica. Si su especificaci&oacute;n requiere resistencia a corrosi&oacute;n o comportamiento no magn&eacute;tico, <strong>no hornee por encima de 260&deg;C</strong>. Horneado HE a 190&deg;C preserva ambas.</div>
        </div>
        <div class="insight-card">
          <div class="insight-label">Tiempo de Horneado HE</div>
          <div class="insight-text">La ventana de 4 horas para horneado HE se mide desde el momento en que las piezas salen del ba&ntilde;o EN, no desde cuando terminan de enjuagar o secar. Para acero de alta resistencia (&ge;40 HRC), el hidr&oacute;geno absorbido durante el dep&oacute;sito debe ser expulsado antes de que cause agrietamiento. Hornee a 190&deg;C por al menos 1 hora (4+ horas t&iacute;pico para &ge;52 HRC). No hornear dentro de la ventana puede resultar en fractura fr&aacute;gil retardada.</div>
        </div>
      </div>
    </div>

    <div class="safety-card">
      <div class="safety-head">&#9888; Seguridad &mdash; Post Tratamiento</div>
      <div class="safety-body"><strong>Hornos</strong> a 190&ndash;400&deg;C &mdash; riesgo severo de quemaduras. Use guantes resistentes al calor y pinzas. Las piezas permanecen calientes por minutos despu&eacute;s de retirarlas. <strong>Soluciones de cromato</strong>: cromo trivalente es moderadamente t&oacute;xico; cromo hexavalente es carcin&oacute;geno GHS Categor&iacute;a 1A (IARC Grupo 1). OSHA PEL Cr(VI): 5 &micro;g/m&sup3;. EPP completo incluyendo protecci&oacute;n respiratoria para cromo hex. Maneje piezas tratadas con cromato con guantes. Regadera y lavaojos a 10 segundos de estaciones de cromato.</div>
    </div>
"""

SF_BODY_EN["08"] = """
    <div class="glass key-card">
      <div class="key-num">&lt;4hr</div>
      <div class="key-label">HE Bake Within 4 Hours &mdash; High-Strength Steel</div>
      <div class="key-text">After plating, high-strength steel parts (&ge;40 HRC) must be baked at 190&deg;C (375&deg;F) within 4 hours to prevent hydrogen embrittlement cracking. The clock starts when parts leave the EN bath. Higher bake temperatures increase hardness but destroy corrosion resistance and non-magnetic properties.</div>
    </div>

    <div class="glass" style="padding:10px 12px;">
      <div class="section-title">Bake Schedules</div>
      <table class="flow-table">
        <thead><tr><th>Bake Type</th><th>Temp</th><th>Time</th><th>Purpose</th></tr></thead>
        <tbody>
          <tr><td style="font-weight:600;color:var(--emerald);">HE Relief</td><td class="mono">375&deg;F (190&deg;C)</td><td class="mono">1&ndash;4+ hr</td><td>Remove trapped hydrogen (mandatory for high-strength steel)</td></tr>
          <tr><td style="font-weight:600;">Adhesion Bake</td><td class="mono">375&ndash;410&deg;F</td><td class="mono">1&ndash;2 hr</td><td>Improve deposit adhesion</td></tr>
          <tr><td style="font-weight:600;color:var(--coral);">Full Hardness</td><td class="mono">750&deg;F (400&deg;C)</td><td class="mono">1 hr</td><td>Maximum hardness (850&ndash;1000 HV)</td></tr>
        </tbody>
      </table>
    </div>

    <div class="glass" style="padding:10px 12px;">
      <div class="section-title">Key Rules <span style="font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:.10em;color:var(--muted);margin-left:8px;">CRITICAL</span></div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;">
        <div style="padding:8px 10px;border-radius:8px;background:rgba(39,174,96,.08);border:1px solid rgba(39,174,96,.2);"><div style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:13px;color:var(--emerald);letter-spacing:.04em;margin-bottom:3px;">HE BAKE &lt;4 HOURS</div><div style="font-size:10.5px;color:var(--muted);line-height:1.35;">For high-strength steel (&ge;40 HRC), bake at 375&deg;F (190&deg;C) within 4 hours of plating. The clock starts when parts leave the EN bath.</div></div>
        <div style="padding:8px 10px;border-radius:8px;background:rgba(224,92,92,.08);border:1px solid rgba(224,92,92,.2);"><div style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:13px;color:var(--coral);letter-spacing:.04em;margin-bottom:3px;">CRYSTALLIZATION WARNING</div><div style="font-size:10.5px;color:var(--muted);line-height:1.35;">Baking above 500&deg;F (260&deg;C) destroys corrosion resistance AND non-magnetic properties permanently. Only do this if the spec calls for maximum hardness.</div></div>
        <div style="padding:8px 10px;border-radius:8px;background:rgba(232,160,32,.08);border:1px solid rgba(232,160,32,.2);"><div style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:13px;color:var(--amber);letter-spacing:.04em;margin-bottom:3px;">CHECK SPEC FIRST</div><div style="font-size:10.5px;color:var(--muted);line-height:1.35;">Different specs require different bake temperatures and times. Always verify which bake schedule your customer specification calls for before starting the oven.</div></div>
        <div style="padding:8px 10px;border-radius:8px;background:rgba(46,196,182,.08);border:1px solid rgba(46,196,182,.2);"><div style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:13px;color:var(--teal);letter-spacing:.04em;margin-bottom:3px;">OVEN TEMP VERIFIED</div><div style="font-size:10.5px;color:var(--muted);line-height:1.35;">Verify oven has reached target temperature before loading parts. Log actual temp and time for every bake cycle. Use calibrated pyrometer.</div></div>
      </div>
    </div>

    <div class="compare-row">
      <div class="compare-card glass do"><div class="compare-head good">&#10003; Do</div><ul class="compare-list"><li>Bake high-strength steel within 4 hours of plating</li><li>Verify oven temperature before loading</li><li>Log every bake cycle: temp, time, part numbers</li><li>Use heat-resistant gloves and tongs</li><li>Check spec for required bake schedule</li></ul></div>
      <div class="compare-card glass dont"><div class="compare-head bad">&#10007; Don&rsquo;t</div><ul class="compare-list"><li>Bake above 500&deg;F if corrosion resistance is required</li><li>Exceed the 4-hour window for HE bake</li><li>Load parts into a cold oven and ramp up</li><li>Touch hot parts with bare hands</li><li>Assume all parts get the same bake schedule</li></ul></div>
    </div>

    <div class="insight-card">
      <div class="insight-label">Why 190&deg;C is the Safe Temperature</div>
      <div class="insight-text">At 190&deg;C (375&deg;F), hydrogen diffuses out of the steel and the EN deposit without crystallizing the amorphous structure. Both corrosion resistance (&gt;1000 hr NSS) and non-magnetic properties are fully preserved. Above 260&deg;C, the Ni-P alloy begins to crystallize into Ni + Ni&#8323;P &mdash; and once crystallized, it cannot be reversed.</div>
    </div>

    <div class="glass safety-card">
      <div class="section-title coral">&#9888; Safety &mdash; Post Treatment</div>
      <div class="safety-text"><strong>Bake ovens</strong> at 375&ndash;750&deg;F &mdash; severe burn hazard. Use heat-resistant gloves. Parts stay hot for minutes after removal. <strong>Chromate solutions</strong>: hex chrome (Cr&sup3;&#8314;/Cr&#8310;&#8314;) is a known carcinogen. Full PPE including respiratory protection. Emergency shower and eyewash within 10 seconds.</div>
    </div>
"""

SF_BODY_ES["08"] = """
    <div class="glass key-card">
      <div class="key-num">&lt;4hr</div>
      <div class="key-label">Horneado HE Dentro de 4 Horas &mdash; Acero de Alta Resistencia</div>
      <div class="key-text">Despu&eacute;s del dep&oacute;sito, piezas de acero de alta resistencia (&ge;40 HRC) deben hornearse a 190&deg;C (375&deg;F) dentro de 4 horas para prevenir agrietamiento por fragilizaci&oacute;n por hidr&oacute;geno. El reloj comienza cuando las piezas salen del ba&ntilde;o EN. Temperaturas m&aacute;s altas aumentan dureza pero destruyen resistencia a corrosi&oacute;n y propiedades no magn&eacute;ticas.</div>
    </div>

    <div class="glass" style="padding:10px 12px;">
      <div class="section-title">Programas de Horneado</div>
      <table class="flow-table">
        <thead><tr><th>Tipo de Horneado</th><th>Temp</th><th>Tiempo</th><th>Prop&oacute;sito</th></tr></thead>
        <tbody>
          <tr><td style="font-weight:600;color:var(--emerald);">Alivio HE</td><td class="mono">190&deg;C (375&deg;F)</td><td class="mono">1&ndash;4+ hr</td><td>Remover hidr&oacute;geno atrapado (obligatorio para acero alta resist.)</td></tr>
          <tr><td style="font-weight:600;">Horneado de Adherencia</td><td class="mono">190&ndash;210&deg;C</td><td class="mono">1&ndash;2 hr</td><td>Mejorar adherencia del dep&oacute;sito</td></tr>
          <tr><td style="font-weight:600;color:var(--coral);">Dureza M&aacute;xima</td><td class="mono">400&deg;C (750&deg;F)</td><td class="mono">1 hr</td><td>Dureza m&aacute;xima (850&ndash;1000 HV)</td></tr>
        </tbody>
      </table>
    </div>

    <div class="glass" style="padding:10px 12px;">
      <div class="section-title">Reglas Clave <span style="font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:.10em;color:var(--muted);margin-left:8px;">CR&Iacute;TICO</span></div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;">
        <div style="padding:8px 10px;border-radius:8px;background:rgba(39,174,96,.08);border:1px solid rgba(39,174,96,.2);"><div style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:13px;color:var(--emerald);letter-spacing:.04em;margin-bottom:3px;">HORNEADO HE &lt;4 HORAS</div><div style="font-size:10.5px;color:var(--muted);line-height:1.35;">Para acero de alta resistencia (&ge;40 HRC), hornee a 190&deg;C dentro de 4 horas del dep&oacute;sito. El reloj comienza cuando las piezas salen del ba&ntilde;o EN.</div></div>
        <div style="padding:8px 10px;border-radius:8px;background:rgba(224,92,92,.08);border:1px solid rgba(224,92,92,.2);"><div style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:13px;color:var(--coral);letter-spacing:.04em;margin-bottom:3px;">ADVERTENCIA DE CRISTALIZACI&Oacute;N</div><div style="font-size:10.5px;color:var(--muted);line-height:1.35;">Hornear por encima de 260&deg;C destruye la resistencia a corrosi&oacute;n Y las propiedades no magn&eacute;ticas permanentemente. Solo haga esto si la especificaci&oacute;n requiere dureza m&aacute;xima.</div></div>
        <div style="padding:8px 10px;border-radius:8px;background:rgba(232,160,32,.08);border:1px solid rgba(232,160,32,.2);"><div style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:13px;color:var(--amber);letter-spacing:.04em;margin-bottom:3px;">VERIFIQUE ESPECIFICACI&Oacute;N</div><div style="font-size:10.5px;color:var(--muted);line-height:1.35;">Diferentes especificaciones requieren diferentes temperaturas y tiempos. Siempre verifique qu&eacute; programa de horneado pide la especificaci&oacute;n de su cliente antes de iniciar el horno.</div></div>
        <div style="padding:8px 10px;border-radius:8px;background:rgba(46,196,182,.08);border:1px solid rgba(46,196,182,.2);"><div style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:13px;color:var(--teal);letter-spacing:.04em;margin-bottom:3px;">TEMP DEL HORNO VERIFICADA</div><div style="font-size:10.5px;color:var(--muted);line-height:1.35;">Verifique que el horno alcanz&oacute; la temperatura objetivo antes de cargar piezas. Registre temp real y tiempo para cada ciclo. Use pir&oacute;metro calibrado.</div></div>
      </div>
    </div>

    <div class="compare-row">
      <div class="compare-card glass do"><div class="compare-head good">&#10003; Haga</div><ul class="compare-list"><li>Hornee acero de alta resistencia dentro de 4 horas del dep&oacute;sito</li><li>Verifique temperatura del horno antes de cargar</li><li>Registre cada ciclo de horneado: temp, tiempo, n&uacute;meros de parte</li><li>Use guantes resistentes al calor y pinzas</li><li>Revise la especificaci&oacute;n para el programa de horneado</li></ul></div>
      <div class="compare-card glass dont"><div class="compare-head bad">&#10007; No Haga</div><ul class="compare-list"><li>Hornear por encima de 260&deg;C si se requiere resistencia a corrosi&oacute;n</li><li>Exceder la ventana de 4 horas para horneado HE</li><li>Cargar piezas en un horno fr&iacute;o y subir temperatura</li><li>Tocar piezas calientes con manos desnudas</li><li>Asumir que todas las piezas reciben el mismo programa</li></ul></div>
    </div>

    <div class="insight-card">
      <div class="insight-label">Por Qu&eacute; 190&deg;C es la Temperatura Segura</div>
      <div class="insight-text">A 190&deg;C, el hidr&oacute;geno se difunde fuera del acero y del dep&oacute;sito EN sin cristalizar la estructura amorfa. Tanto la resistencia a corrosi&oacute;n (&gt;1000 hr NSS) como las propiedades no magn&eacute;ticas se preservan completamente. Por encima de 260&deg;C, la aleaci&oacute;n Ni-P comienza a cristalizar en Ni + Ni&#8323;P &mdash; y una vez cristalizada, no se puede revertir.</div>
    </div>

    <div class="glass safety-card">
      <div class="section-title coral">&#9888; Seguridad &mdash; Post Tratamiento</div>
      <div class="safety-text"><strong>Hornos</strong> a 190&ndash;400&deg;C &mdash; riesgo severo de quemaduras. Use guantes resistentes al calor. Las piezas permanecen calientes por minutos despu&eacute;s de retirarlas. <strong>Soluciones de cromato</strong>: cromo hexavalente (Cr&sup3;&#8314;/Cr&#8310;&#8314;) es un carcin&oacute;geno conocido. EPP completo incluyendo protecci&oacute;n respiratoria. Regadera y lavaojos a 10 segundos.</div>
    </div>
"""

# ── TEMPLATES ────────────────────────────────────────────────────────

TECH_TEMPLATE = """<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EN High Phos &mdash; {title} &mdash; Technical | Plating Posters Inc</title>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@800;900&family=Barlow:wght@600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
:root {{
  --bg:#1A1F2E;--navy:#0D1020;--text:#F0EDE8;--muted:rgba(240,237,232,.62);
  --faint:rgba(240,237,232,.38);
  --amber:#E8A020;--teal:#2EC4B6;--emerald:#27AE60;--coral:#E05C5C;
  --slate:#3A4055;--callout:#1E2435;--altrow:#252B3D;
  --glass-bg:rgba(30,36,53,.55);--glass-border:rgba(255,255,255,.12);
  --glass-shadow:inset 0 1px 0 rgba(255,255,255,.14),inset 0 -1px 0 rgba(0,0,0,.2),0 4px 12px rgba(0,0,0,.25);
}}
.poster[data-edition="light"]{{
  --bg:#F5F4F0;--navy:#DDD8CE;--text:#1B2030;--muted:rgba(27,32,48,.66);
  --faint:rgba(27,32,48,.42);
  --amber:#B8770D;--teal:#1A8C82;--emerald:#1E8449;--coral:#B7322F;
  --slate:#C5C0B5;--callout:#ECEAE1;--altrow:#E4E1D6;
  --glass-bg:rgba(255,253,247,.66);--glass-border:rgba(27,32,48,.10);
  --glass-shadow:inset 0 1px 0 rgba(255,255,255,.6),0 4px 12px rgba(27,32,48,.08);
}}
html,body{{margin:0;padding:0;background:#0a0c14;}}
.stage{{width:100vw;min-height:100vh;display:flex;align-items:flex-start;justify-content:center;overflow:visible;padding:12px 0;box-sizing:border-box;}}
.poster-wrap{{transform-origin:center center;}}
.poster{{width:1200px;height:1800px;position:relative;overflow:hidden;background:radial-gradient(1200px 800px at 15% 8%,rgba(46,196,182,.14),transparent 60%),radial-gradient(1000px 700px at 90% 25%,rgba(232,160,32,.12),transparent 55%),radial-gradient(900px 900px at 50% 80%,rgba(224,92,92,.10),transparent 60%),var(--bg);font-family:'Inter',sans-serif;color:var(--text);display:flex;flex-direction:column;padding:32px;box-sizing:border-box;}}
.poster::before{{content:'';position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.025) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.025) 1px,transparent 1px);background-size:50px 50px;mask-image:radial-gradient(ellipse 80% 80% at 50% 50%,black 40%,transparent 100%);-webkit-mask-image:radial-gradient(ellipse 80% 80% at 50% 50%,black 40%,transparent 100%);pointer-events:none;z-index:0;}}
.poster>*{{position:relative;z-index:1;}}
.glass{{background-color:var(--glass-bg);background-image:linear-gradient(145deg,rgba(255,255,255,.055),rgba(255,255,255,.015));border:1px solid var(--glass-border);backdrop-filter:blur(18px) saturate(140%);-webkit-backdrop-filter:blur(18px) saturate(140%);box-shadow:var(--glass-shadow);border-radius:12px;}}
.tack{{position:absolute;width:24px;height:24px;border-radius:50%;border:1.5px solid rgba(232,160,32,.28);z-index:2;pointer-events:none;}}.tack::before,.tack::after{{content:"";position:absolute;background:rgba(232,160,32,.28);}}.tack::before{{left:50%;top:-3px;bottom:-3px;width:1px;transform:translateX(-50%);}}.tack::after{{top:50%;left:-3px;right:-3px;height:1px;transform:translateY(-50%);}}.tack.tl{{top:12px;left:12px;}}.tack.tr{{top:12px;right:12px;}}.tack.bl{{bottom:12px;left:12px;}}.tack.br{{bottom:12px;right:12px;}}
.poster-header{{flex-shrink:0;}}.poster-body{{flex:1;overflow:hidden;display:flex;flex-direction:column;gap:7px;justify-content:space-between;}}.poster-footer{{flex-shrink:0;margin-top:8px;}}
.header-band{{display:flex;align-items:flex-start;justify-content:space-between;gap:16px;margin-bottom:8px;}}.header-left{{flex:1;min-width:0;}}.eyebrow{{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--amber);letter-spacing:.16em;text-transform:uppercase;margin-bottom:4px;display:flex;align-items:center;gap:12px;}}.eyebrow::before{{content:"";display:inline-block;width:30px;height:3px;background:var(--amber);}}.headline{{font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:72px;color:var(--text);line-height:.92;margin:4px 0;letter-spacing:-.01em;text-transform:uppercase;}}.headline em{{font-style:normal;color:var(--amber);}}.subhead{{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:22px;color:var(--teal);margin:0 0 3px;letter-spacing:.02em;text-transform:uppercase;}}.tagline{{font-family:'Inter',sans-serif;font-style:italic;font-size:13px;color:var(--muted);line-height:1.45;max-width:700px;margin:0;}}
.logo-card{{flex-shrink:0;padding:12px 10px;display:flex;flex-direction:column;align-items:center;gap:8px;align-self:flex-start;}}.logo-tile{{width:68px;height:68px;border-radius:12px;background:linear-gradient(135deg,#E8A020,#2EC4B6);display:flex;align-items:center;justify-content:center;box-shadow:inset 0 1px 0 rgba(255,255,255,.4),inset 0 -2px 4px rgba(0,0,0,.15),0 4px 14px rgba(0,0,0,.35);}}.logo-tile span{{font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:26px;color:#1A1F2E;letter-spacing:.02em;line-height:1;}}.logo-word{{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:18px;letter-spacing:.04em;text-transform:uppercase;line-height:1;text-align:center;white-space:nowrap;}}.logo-word .a{{color:var(--text);}}.logo-word .b{{color:var(--amber);}}.logo-inc{{font-family:'JetBrains Mono',monospace;font-size:8.5px;letter-spacing:.05em;text-transform:lowercase;color:var(--muted);margin-top:-2px;}}
.section-title{{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:28px;letter-spacing:.08em;text-transform:uppercase;color:var(--text);margin:0 0 6px;display:flex;align-items:center;gap:8px;}}.section-title::before{{content:"";width:6px;height:6px;background:var(--amber);border-radius:50%;}}.section-title .sub{{font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.14em;color:var(--muted);margin-left:auto;font-weight:500;}}
.rule-card{{display:flex;align-items:center;gap:20px;padding:18px 28px;background:rgba(232,160,32,.07);}}.rule-num{{font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:68px;color:var(--amber);line-height:1;letter-spacing:-.02em;}}.rule-body{{flex:1;}}.rule-label{{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:19px;color:var(--amber);letter-spacing:.08em;text-transform:uppercase;}}.rule-text{{font-family:'Inter',sans-serif;font-size:14px;color:var(--muted);line-height:1.5;margin-top:4px;}}
.data-table{{width:100%;border-collapse:collapse;}}.data-table th{{font-family:'Barlow',sans-serif;font-weight:700;font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--amber);padding:8px 12px;text-align:left;background:rgba(13,16,32,.35);border-bottom:1px solid var(--glass-border);}}.poster[data-edition="light"] .data-table th{{background:rgba(27,32,48,.06);}}.data-table td{{padding:8px 12px;color:var(--text);line-height:1.5;border-bottom:1px solid rgba(255,255,255,.05);font-family:'Inter',sans-serif;font-size:14px;}}.data-table tr:last-child td{{border-bottom:none;}}.data-table tr:nth-child(even) td{{background:rgba(255,255,255,.02);}}.poster[data-edition="light"] .data-table tr:nth-child(even) td{{background:rgba(27,32,48,.025);}}.data-table .mono{{font-family:'JetBrains Mono',monospace;font-size:13px;}}.data-table.compact th{{font-size:12px;padding:7px 10px;}}.data-table.compact td{{padding:6px 10px;font-size:13px;line-height:1.45;}}.data-table.compact .mono{{font-size:12.5px;}}.data-table.bath th{{font-size:12px;padding:6px 8px;}}.data-table.bath td{{padding:5px 8px;font-size:13px;line-height:1.4;}}.data-table.bath .mono{{font-size:12px;}}
.compare-grid{{display:grid;grid-template-columns:1fr 1fr;gap:10px;}}.compare-card{{padding:18px 24px;}}.compare-card h4{{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:21px;color:var(--text);margin:0 0 8px;text-transform:uppercase;letter-spacing:.04em;}}.compare-card h4 .tag{{font-size:12px;padding:2px 8px;border-radius:4px;margin-left:8px;font-family:'JetBrains Mono',monospace;font-weight:500;letter-spacing:.06em;}}.compare-card h4 .tag.good{{background:rgba(39,174,96,.15);color:var(--emerald);}}.compare-card h4 .tag.bad{{background:rgba(224,92,92,.15);color:var(--coral);}}.compare-card ul{{list-style:none;padding:0;margin:0;}}.compare-card li{{font-size:13.5px;line-height:1.5;padding:2px 0;display:flex;gap:8px;align-items:flex-start;}}.compare-card li::before{{content:"";width:5px;height:5px;border-radius:50%;margin-top:7px;flex-shrink:0;}}.compare-card.do li::before{{background:var(--emerald);}}.compare-card.dont li::before{{background:var(--coral);}}
.bottom-grid{{display:grid;grid-template-columns:1.6fr 1fr;gap:10px;}}
.insight-card{{padding:20px 24px;border-left:3px solid var(--teal);background:rgba(46,196,182,.06);border-radius:0 12px 12px 0;}}.insight-label{{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:16px;color:var(--teal);letter-spacing:.08em;text-transform:uppercase;margin-bottom:3px;}}.insight-text{{font-family:'Inter',sans-serif;font-size:14.5px;color:var(--text);line-height:1.5;}}
.safety-card{{padding:18px 24px;background:rgba(224,92,92,.08);border:1px solid rgba(224,92,92,.25);border-radius:12px;}}.safety-head{{font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:20px;color:var(--coral);letter-spacing:.06em;text-transform:uppercase;margin-bottom:5px;}}.safety-body{{font-size:14px;color:var(--text);line-height:1.55;}}.safety-body strong{{font-weight:700;color:var(--coral);}}
.process-flow{{display:flex;align-items:center;justify-content:space-between;padding:10px 16px;height:80px;gap:4px;}}
.footer{{padding:10px 20px;background-color:rgba(13,16,32,.85);background-image:linear-gradient(180deg,rgba(255,255,255,.04),rgba(0,0,0,0));border:1px solid rgba(255,255,255,.10);border-radius:8px;text-align:center;display:flex;flex-direction:column;gap:2px;}}.poster[data-edition="light"] .footer{{background-color:rgba(221,216,206,.95);border-color:rgba(27,32,48,.10);}}.footer-disclaimer{{font-family:'Inter',sans-serif;font-size:9px;line-height:1.35;color:var(--faint);margin:0 auto;max-width:900px;}}.footer-title{{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:13px;color:var(--text);letter-spacing:.04em;text-transform:uppercase;margin:0;}}.footer-brand{{font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--muted);letter-spacing:.12em;text-transform:uppercase;}}
.tweaks{{position:fixed;bottom:16px;right:16px;z-index:100;background:rgba(13,16,32,.92);border:1px solid rgba(255,255,255,.12);border-radius:10px;padding:10px 14px;display:flex;flex-direction:column;gap:8px;font-family:'Inter',sans-serif;font-size:12px;color:#F0EDE8;}}
@media print{{@page{{size:12.5in 18.75in;margin:0;}}html,body{{background:#1A1F2E !important;-webkit-print-color-adjust:exact !important;print-color-adjust:exact !important;}}*{{-webkit-print-color-adjust:exact !important;print-color-adjust:exact !important;}}.stage{{position:static;padding:0;display:block;overflow:visible;}}.poster-wrap{{transform:none !important;width:auto !important;height:auto !important;}}.poster{{box-shadow:none !important;width:1200px !important;height:1800px !important;overflow:hidden !important;}}.glass,.insight-card,.safety-card{{backdrop-filter:none !important;-webkit-backdrop-filter:none !important;}}.tweaks{{display:none !important;}}}}
</style>
</head>
<body>
<div class="stage">
<div class="poster-wrap" id="posterWrap">
<div class="poster" id="poster"{edition_attr}>
  <span class="tack tl" aria-hidden="true"></span><span class="tack tr" aria-hidden="true"></span>
  <span class="tack bl" aria-hidden="true"></span><span class="tack br" aria-hidden="true"></span>
  {header}
  <div class="poster-body">
{body}
  </div>
  {footer}
</div>
</div>
</div>
<div class="tweaks">
  <div style="display:flex;gap:8px;align-items:center;">
    <span style="color:rgba(240,237,232,.5);font-size:11px;letter-spacing:.06em;text-transform:uppercase;">Edition</span>
    <button id="btnDark" style="padding:4px 11px;border-radius:5px;cursor:pointer;font-size:11px;background:{dark_bg};color:{dark_fg};border:1px solid {dark_border};" onclick="setEdition('')">Dark</button>
    <button id="btnLight" style="padding:4px 11px;border-radius:5px;cursor:pointer;font-size:11px;background:{light_bg};color:{light_fg};border:1px solid {light_border};" onclick="setEdition('light')">Light</button>
  </div>
  <button onclick="window.print()" style="padding:4px 11px;border-radius:5px;cursor:pointer;font-size:11px;background:transparent;color:#F0EDE8;border:1px solid rgba(255,255,255,.2);">Print / PDF</button>
</div>
<script>
const posterWrap=document.getElementById('posterWrap');const poster=document.getElementById('poster');function scalePoster(){{const sW=(window.innerWidth-24)/1200;const sH=(window.innerHeight-24)/1800;const s=Math.min(sW,sH);posterWrap.style.transform='scale('+s+')';posterWrap.style.transformOrigin='top center';posterWrap.style.width='1200px';posterWrap.style.height=(1800*s)+'px';}}function setEdition(e){{if(e)poster.dataset.edition=e;else delete poster.dataset.edition;document.getElementById('btnDark').style.background=e?'transparent':'#E8A020';document.getElementById('btnDark').style.color=e?'#F0EDE8':'#1A1F2E';document.getElementById('btnDark').style.borderColor=e?'rgba(255,255,255,.2)':'#E8A020';document.getElementById('btnLight').style.background=e?'#E8A020':'transparent';document.getElementById('btnLight').style.color=e?'#1A1F2E':'#F0EDE8';document.getElementById('btnLight').style.borderColor=e?'#E8A020':'rgba(255,255,255,.2)';}}scalePoster();window.addEventListener('resize',scalePoster);
</script>
</body>
</html>"""

SF_TEMPLATE = """<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EN High Phos &mdash; {title} &mdash; Shop Floor | Plating Posters Inc</title>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@800;900&family=Barlow:wght@600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
:root{{--bg:#1A1F2E;--navy:#0D1020;--text:#F0EDE8;--muted:rgba(240,237,232,.62);--faint:rgba(240,237,232,.38);--amber:#E8A020;--teal:#2EC4B6;--emerald:#27AE60;--coral:#E05C5C;--slate:#3A4055;--glass-bg:rgba(30,36,53,.55);--glass-border:rgba(255,255,255,.12);--glass-shadow:inset 0 1px 0 rgba(255,255,255,.14),inset 0 -1px 0 rgba(0,0,0,.2),0 4px 12px rgba(0,0,0,.25);--tack:24px;}}
body[data-edition="light"]{{--bg:#F5F4F0;--navy:#DDD8CE;--text:#1B2030;--muted:rgba(27,32,48,.78);--amber:#8C5A00;--teal:#0F6B62;--emerald:#15693B;--coral:#9B2825;--faint:rgba(27,32,48,.42);--slate:#C5C0B5;--glass-bg:rgba(255,253,247,.82);--glass-border:rgba(27,32,48,.18);--glass-shadow:inset 0 1px 0 rgba(255,255,255,.6),0 4px 12px rgba(27,32,48,.08);}}body[data-edition="light"] .logo-url{{color:rgba(27,32,48,.62);}}body[data-edition="light"] .logo-word .a{{color:#1B2030;}}
html,body{{margin:0;padding:0;background:#0a0c14;}}.stage{{width:100vw;height:100vh;display:flex;align-items:center;justify-content:center;overflow:hidden;}}.poster-wrap{{transform-origin:center center;}}.poster{{width:900px;height:1200px;position:relative;overflow:hidden;background:radial-gradient(700px 500px at 10% 8%,rgba(46,196,182,.15),transparent 60%),radial-gradient(600px 450px at 92% 20%,rgba(232,160,32,.13),transparent 55%),radial-gradient(550px 500px at 50% 88%,rgba(224,92,92,.10),transparent 60%),var(--bg);font-family:'Inter',sans-serif;color:var(--text);display:flex;flex-direction:column;padding:var(--tack);box-sizing:border-box;}}.poster::before{{content:'';position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.025) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.025) 1px,transparent 1px);background-size:50px 50px;mask-image:radial-gradient(ellipse 80% 80% at 50% 50%,black 40%,transparent 100%);-webkit-mask-image:radial-gradient(ellipse 80% 80% at 50% 50%,black 40%,transparent 100%);pointer-events:none;z-index:0;}}.poster>*{{position:relative;z-index:1;}}
.glass{{background-color:var(--glass-bg);background-image:linear-gradient(145deg,rgba(255,255,255,.055),rgba(255,255,255,.015));border:1px solid var(--glass-border);backdrop-filter:blur(18px) saturate(140%);-webkit-backdrop-filter:blur(18px) saturate(140%);box-shadow:var(--glass-shadow);border-radius:12px;}}
.tack{{position:absolute;width:18px;height:18px;border-radius:50%;border:1.5px solid rgba(232,160,32,.28);z-index:2;pointer-events:none;}}.tack::before,.tack::after{{content:"";position:absolute;background:rgba(232,160,32,.28);}}.tack::before{{left:50%;top:-2px;bottom:-2px;width:1px;transform:translateX(-50%);}}.tack::after{{top:50%;left:-2px;right:-2px;height:1px;transform:translateY(-50%);}}.tack.tl{{top:6px;left:6px;}}.tack.tr{{top:6px;right:6px;}}.tack.bl{{bottom:6px;left:6px;}}.tack.br{{bottom:6px;right:6px;}}
.poster-header{{flex-shrink:0;}}.poster-body{{flex:1;overflow:hidden;display:flex;flex-direction:column;gap:10px;justify-content:space-between;}}.poster-footer{{flex-shrink:0;margin-top:8px;}}
.header-row{{display:flex;align-items:flex-start;justify-content:space-between;gap:14px;margin-bottom:8px;}}.header-left{{flex:1;min-width:0;}}.eyebrow{{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--amber);letter-spacing:.12em;text-transform:uppercase;margin-bottom:4px;}}.headline{{font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:56px;color:var(--text);line-height:.92;letter-spacing:-.01em;margin-bottom:4px;}}.headline em{{font-style:normal;color:var(--amber);}}.subhead{{font-family:'Barlow',sans-serif;font-weight:700;font-size:17px;color:var(--amber);margin-bottom:4px;}}.tagline{{font-family:'Inter',sans-serif;font-weight:500;font-size:11px;color:var(--muted);line-height:1.3;max-width:520px;}}
.logo-card{{flex-shrink:0;display:flex;flex-direction:column;align-items:center;gap:6px;padding:10px 12px;min-width:140px;background-color:var(--glass-bg);background-image:linear-gradient(145deg,rgba(255,255,255,.055),rgba(255,255,255,.015));border:1px solid var(--glass-border);border-radius:12px;backdrop-filter:blur(18px) saturate(140%);-webkit-backdrop-filter:blur(18px) saturate(140%);box-shadow:inset 0 1px 0 rgba(255,255,255,.14),0 4px 12px rgba(0,0,0,.25);}}.logo-mark{{width:60px;height:60px;border-radius:11px;background:linear-gradient(135deg,#E8A020,#2EC4B6);display:flex;align-items:center;justify-content:center;box-shadow:inset 0 1px 0 rgba(255,255,255,.4),inset 0 -2px 4px rgba(0,0,0,.15),0 4px 14px rgba(0,0,0,.35);}}.logo-mark span{{font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:22px;color:#1A1F2E;letter-spacing:.02em;line-height:1;}}.logo-word{{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:16px;letter-spacing:.04em;text-transform:uppercase;line-height:1;text-align:center;white-space:nowrap;}}.logo-word .a{{color:#F0EDE8;}}.logo-word .b{{color:#E8A020;}}.logo-url{{font-family:'JetBrains Mono',monospace;font-size:8px;letter-spacing:.06em;color:rgba(240,237,232,.45);margin-top:-1px;}}
.section-title{{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:16px;letter-spacing:.07em;text-transform:uppercase;color:var(--amber);margin-bottom:6px;}}.section-title.coral{{color:var(--coral);}}
.key-card{{padding:12px 16px;background:rgba(232,160,32,.07);border-radius:12px;}}.key-num{{font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:48px;color:var(--amber);line-height:1;margin-bottom:2px;}}.key-label{{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:16px;color:var(--amber);letter-spacing:.06em;text-transform:uppercase;}}.key-text{{font-family:'Inter',sans-serif;font-size:12px;color:var(--muted);line-height:1.4;margin-top:4px;}}
.flow-table{{width:100%;border-collapse:collapse;}}.flow-table th{{font-family:'Barlow',sans-serif;font-weight:700;font-size:10px;color:var(--amber);letter-spacing:.06em;text-transform:uppercase;padding:5px 8px;text-align:left;border-bottom:1px solid var(--glass-border);}}.flow-table td{{font-family:'Inter',sans-serif;font-weight:500;font-size:11px;color:var(--text);padding:5px 8px;border-bottom:1px solid rgba(255,255,255,.05);line-height:1.3;}}.flow-table td.mono{{font-family:'JetBrains Mono',monospace;font-size:10px;}}.flow-table tr:nth-child(even) td{{background:rgba(255,255,255,.02);}}body[data-edition="light"] .flow-table tr:nth-child(even) td{{background:rgba(27,32,48,.025);}}
.compare-row{{display:flex;gap:10px;}}.compare-card{{flex:1;padding:12px 14px;}}.compare-head{{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:14px;letter-spacing:.06em;text-transform:uppercase;margin-bottom:6px;display:flex;align-items:center;gap:8px;}}.compare-head.good{{color:var(--emerald);}}.compare-head.bad{{color:var(--coral);}}.compare-list{{list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:4px;}}.compare-list li{{font-size:11.5px;line-height:1.4;display:flex;gap:6px;align-items:flex-start;}}.compare-list li::before{{content:"";width:5px;height:5px;border-radius:50%;margin-top:5px;flex-shrink:0;}}.compare-card.do .compare-list li::before{{background:var(--emerald);}}.compare-card.dont .compare-list li::before{{background:var(--coral);}}
.numbered-list{{border-radius:12px;}}.list-item{{display:flex;align-items:flex-start;gap:8px;}}.num{{font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:14px;color:var(--amber);width:18px;text-align:center;flex-shrink:0;}}.num-text{{font-family:'Inter',sans-serif;font-size:12.5px;color:var(--text);line-height:1.4;}}
.insight-card{{padding:10px 14px;border-left:3px solid var(--teal);background:rgba(46,196,182,.06);border-radius:0 12px 12px 0;}}.insight-label{{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:13px;color:var(--teal);letter-spacing:.06em;text-transform:uppercase;margin-bottom:2px;}}.insight-text{{font-family:'Inter',sans-serif;font-size:11.5px;color:var(--text);line-height:1.4;}}
.safety-card{{padding:10px 14px;background:rgba(224,92,92,.06);border-radius:12px;}}.safety-text{{font-family:'Inter',sans-serif;font-weight:500;font-size:11.5px;color:var(--text);line-height:1.45;}}.safety-text strong{{font-weight:700;color:var(--coral);}}
.footer-panel{{padding:8px 18px;text-align:center;border-radius:10px;}}.footer-disclaimer{{font-family:'Inter',sans-serif;font-weight:400;font-size:9px;color:var(--muted);line-height:1.4;margin-bottom:3px;}}.footer-title{{font-family:'Barlow',sans-serif;font-weight:600;font-size:11px;color:var(--text);margin-bottom:2px;}}.footer-brand{{font-family:'JetBrains Mono',monospace;font-size:8.5px;color:var(--muted);}}
.data-table{{width:100%;border-collapse:collapse;}}.data-table th{{font-family:'Barlow',sans-serif;font-weight:700;font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--amber);padding:5px 8px;text-align:left;background:rgba(13,16,32,.35);border-bottom:1px solid var(--glass-border);}}.data-table td{{padding:5px 8px;color:var(--text);line-height:1.4;border-bottom:1px solid rgba(255,255,255,.05);font-family:'Inter',sans-serif;font-size:11.5px;}}.data-table tr:last-child td{{border-bottom:none;}}.data-table .mono{{font-family:'JetBrains Mono',monospace;font-size:10.5px;}}.data-table.compact th{{font-size:10px;padding:4px 7px;}}.data-table.compact td{{padding:4px 7px;font-size:11px;}}.data-table.compact .mono{{font-size:10px;}}
@media print{{@page{{size:9.375in 12.5in;margin:0;}}html,body{{background:#1A1F2E !important;-webkit-print-color-adjust:exact !important;print-color-adjust:exact !important;}}*{{-webkit-print-color-adjust:exact !important;print-color-adjust:exact !important;}}.stage{{position:static;display:block;overflow:visible;}}.poster-wrap{{transform:none !important;width:auto !important;height:auto !important;}}.poster{{box-shadow:none !important;width:900px !important;height:1200px !important;overflow:hidden !important;}}.glass,.safety-card,.compare-card{{backdrop-filter:none !important;-webkit-backdrop-filter:none !important;}}.tweaks{{display:none !important;}}}}
</style>
</head>
<body{edition_attr}>
<div class="stage">
<div class="poster-wrap" id="posterWrap">
<div class="poster" id="poster">
  <span class="tack tl"></span><span class="tack tr"></span><span class="tack bl"></span><span class="tack br"></span>
  {header}
  <div class="poster-body">
{body}
  </div>
  {footer}
</div>
</div>
</div>
<div class="tweaks" style="position:fixed;bottom:16px;right:16px;z-index:100;background:rgba(13,16,32,.92);border:1px solid rgba(255,255,255,.12);border-radius:10px;padding:12px 16px;display:flex;flex-direction:column;gap:8px;font-family:'Inter',sans-serif;font-size:12px;color:#F0EDE8;">
  <div style="display:flex;gap:8px;align-items:center;"><span style="color:rgba(240,237,232,.5);">Edition</span><button id="btnDark" onclick="setEdition('')" style="padding:3px 10px;border-radius:4px;border:1px solid {dark_border};background:{dark_bg};color:{dark_fg};cursor:pointer;font-size:11px;">Dark</button><button id="btnLight" onclick="setEdition('light')" style="padding:3px 10px;border-radius:4px;border:1px solid {light_border};background:{light_bg};color:{light_fg};cursor:pointer;font-size:11px;">Light</button></div>
  <button onclick="window.print()" style="padding:4px 12px;border-radius:4px;border:1px solid rgba(255,255,255,.2);background:transparent;color:#F0EDE8;cursor:pointer;font-size:11px;">Print / PDF</button>
</div>
<script>
const posterWrap=document.getElementById('posterWrap');const poster=document.getElementById('poster');function scalePoster(){{const s=Math.min((window.innerWidth-24)/900,(window.innerHeight-24)/1200);posterWrap.style.transform='scale('+s+')';posterWrap.style.transformOrigin='top center';posterWrap.style.width='900px';posterWrap.style.height=(1200*s)+'px';}}function setEdition(e){{if(e)document.body.dataset.edition=e;else delete document.body.dataset.edition;document.getElementById('btnDark').style.background=e?'transparent':'#E8A020';document.getElementById('btnDark').style.color=e?'#F0EDE8':'#1A1F2E';document.getElementById('btnDark').style.borderColor=e?'rgba(255,255,255,.2)':'#E8A020';document.getElementById('btnLight').style.background=e?'#E8A020':'transparent';document.getElementById('btnLight').style.color=e?'#1A1F2E':'#F0EDE8';document.getElementById('btnLight').style.borderColor=e?'#E8A020':'rgba(255,255,255,.2)';}}scalePoster();window.addEventListener('resize',scalePoster);
</script>
</body>
</html>"""

# ── THEMES ───────────────────────────────────────────────────────────
THEMES = [
    {"name": "Dark", "edition_attr_tech": "", "edition_attr_sf": "",
     "dark_bg": "#E8A020", "dark_fg": "#1A1F2E", "dark_border": "#E8A020",
     "light_bg": "transparent", "light_fg": "#F0EDE8", "light_border": "rgba(255,255,255,.2)"},
    {"name": "Light", "edition_attr_tech": ' data-edition="light"', "edition_attr_sf": ' data-edition="light"',
     "dark_bg": "transparent", "dark_fg": "#F0EDE8", "dark_border": "rgba(255,255,255,.2)",
     "light_bg": "#E8A020", "light_fg": "#1A1F2E", "light_border": "#E8A020"},
]

# ── GENERATOR ────────────────────────────────────────────────────────
def main():
    out_dir = os.path.dirname(os.path.abspath(__file__))
    count = 0
    preview_nums = ["00"]
    for num, title in POSTERS:
        for theme in THEMES:
            for lang_code, lang_label in [("en", "EN"), ("es", "ES")]:
                title_es = TITLES_ES.get(num, title)
                t = title if lang_code == "en" else title_es
                # TECHNICAL
                if lang_code == "en":
                    header = tech_headers_en(num, title)
                    body = TECH_BODY_EN.get(num, "")
                    footer = tech_footer_en(num, title)
                else:
                    header = tech_headers_es(num, title_es)
                    body = TECH_BODY_ES.get(num, "")
                    footer = tech_footer_es(num, title_es)
                html = TECH_TEMPLATE.format(
                    lang=lang_code, title=t, header=header, body=body, footer=footer,
                    edition_attr=theme["edition_attr_tech"],
                    dark_bg=theme["dark_bg"], dark_fg=theme["dark_fg"], dark_border=theme["dark_border"],
                    light_bg=theme["light_bg"], light_fg=theme["light_fg"], light_border=theme["light_border"],
                )
                fname = f"EN High Phos - {num} - TECHNICAL - {title} - {lang_label} - {theme['name']}.html"
                with open(os.path.join(out_dir, fname), "w", encoding="utf-8") as f:
                    f.write(html)
                count += 1

                # SHOP FLOOR
                if lang_code == "en":
                    header = sf_headers_en(num, title)
                    body = SF_BODY_EN.get(num, "")
                    footer = sf_footer_en(num, title)
                else:
                    header = sf_headers_es(num, title_es)
                    body = SF_BODY_ES.get(num, "")
                    footer = sf_footer_es(num, title_es)
                html = SF_TEMPLATE.format(
                    lang=lang_code, title=t, header=header, body=body, footer=footer,
                    edition_attr=theme["edition_attr_sf"],
                    dark_bg=theme["dark_bg"], dark_fg=theme["dark_fg"], dark_border=theme["dark_border"],
                    light_bg=theme["light_bg"], light_fg=theme["light_fg"], light_border=theme["light_border"],
                )
                fname = f"EN High Phos - {num} - SHOP FLOOR - {title} - {lang_label} - {theme['name']}.html"
                with open(os.path.join(out_dir, fname), "w", encoding="utf-8") as f:
                    f.write(html)
                count += 1

    print(f"Generated {count} files in {out_dir}")

if __name__ == "__main__":
    main()
