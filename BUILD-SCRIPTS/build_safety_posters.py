#!/usr/bin/env python3
"""
Build Safety Poster Series — 18 topics × 4 variants = 72 files
Format: SHOP FLOOR only (900×1200px), EN+ES, Dark+Light
Palette: Coral #E05C5C as primary accent (hazard theme)
Rodrigo's prior corrections pre-baked (contra el viento, lentes, vía de exposición, etc.)
"""
import os, html

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ─── 18 SAFETY TOPICS ───────────────────────────────────────────────────────
TOPICS = [
  {
    "num": "01", "code": "SAF-01",
    "en": {
      "headline": "CYANIDE<br><em>SAFETY</em>",
      "subhead": "Never Add Acid to Cyanide",
      "tagline": "One wrong chemical addition can release deadly hydrogen cyanide gas in seconds.",
      "hazard_signal": "DANGER",
      "hazard_chemical": "Hydrogen Cyanide (HCN) Gas — Sodium/Potassium Cyanide Solutions",
      "hazard_limits": "OSHA PEL: 10 ppm (ceiling) · IDLH: 50 ppm · Odor threshold: 1–5 ppm (bitter almond — unreliable)",
      "danger_title": "The Danger",
      "danger_chips": ["Acid contacts cyanide solution", "HCN gas released instantly", "Inhalation within breathing zone", "Rapid loss of consciousness", "Death in minutes at high concentrations"],
      "danger_caption": "HCN blocks cellular oxygen uptake. You may not smell it before it kills you.",
      "protect_title": "Protect Yourself",
      "protect_steps": [
        "<strong>Never add acid</strong> to any cyanide-bearing tank. Verify labels before every addition.",
        "<strong>Full-face respirator</strong> with combination OV/HCN cartridge when handling cyanide solutions.",
        "<strong>Chemical splash goggles</strong> and face shield for all transfers and tank-side work.",
        "<strong>Cyanide antidote kit</strong> must be stationed within 30 seconds of the cyanide line.",
        "<strong>Buddy system</strong> — never work alone at cyanide tanks. Two-person minimum, always."
      ],
      "never_title": "Never Do This",
      "never_rows": [
        ["Add acid to a cyanide tank", "Produces lethal HCN gas instantly"],
        ["Work alone at cyanide stations", "No one to call for help if you collapse"],
        ["Eat, drink, or smoke near cyanide", "Ingestion of residue is fatal"],
        ["Dispose of cyanide in acid waste", "Generates HCN in the waste system"]
      ],
      "exposed_title": "If Exposed — Act Now",
      "exposed_steps": [
        "Move victim to fresh air immediately — upwind, not downwind.",
        "Call 911 and your facility emergency team.",
        "Administer cyanide antidote kit if trained and authorized.",
        "Begin rescue breathing if victim is not breathing (use barrier device — no mouth-to-mouth).",
        "Remove contaminated clothing; flush skin with water for 15+ minutes."
      ],
      "symptoms": "Headache, dizziness, confusion, gasping, seizures, cherry-red skin, collapse."
    },
    "es": {
      "headline": "SEGURIDAD CON<br><em>CIANURO</em>",
      "subhead": "Nunca Agregue Ácido al Cianuro",
      "tagline": "Una adición química incorrecta puede liberar gas de cianuro de hidrógeno mortal en segundos.",
      "hazard_signal": "PELIGRO",
      "hazard_chemical": "Gas de Cianuro de Hidrógeno (HCN) — Soluciones de Cianuro de Sodio/Potasio",
      "hazard_limits": "OSHA PEL: 10 ppm (techo) · IDLH: 50 ppm · Umbral de olor: 1–5 ppm (almendra amarga — no confiable)",
      "danger_title": "El Peligro",
      "danger_chips": ["El ácido contacta la solución de cianuro", "Gas HCN se libera instantáneamente", "Inhalación en la zona de respiración", "Pérdida rápida del conocimiento", "Muerte en minutos a altas concentraciones"],
      "danger_caption": "El HCN bloquea la absorción celular de oxígeno. Puede que no lo huela antes de que lo mate.",
      "protect_title": "Protéjase",
      "protect_steps": [
        "<strong>Nunca agregue ácido</strong> a ningún tanque que contenga cianuro. Verifique etiquetas antes de cada adición.",
        "<strong>Respirador de cara completa</strong> con cartucho combinado OV/HCN al manejar soluciones de cianuro.",
        "<strong>Lentes antisalpicaduras</strong> y careta protectora para todas las transferencias y trabajo en tanques.",
        "<strong>Kit de antídoto de cianuro</strong> debe estar a menos de 30 segundos de la línea de cianuro.",
        "<strong>Sistema de compañero</strong> — nunca trabaje solo en tanques de cianuro. Mínimo dos personas, siempre."
      ],
      "never_title": "Nunca Haga Esto",
      "never_rows": [
        ["Agregar ácido a un tanque de cianuro", "Produce gas HCN letal al instante"],
        ["Trabajar solo en estaciones de cianuro", "Nadie para pedir ayuda si colapsa"],
        ["Comer, beber o fumar cerca del cianuro", "La ingestión de residuos es fatal"],
        ["Desechar cianuro en residuos ácidos", "Genera HCN en el sistema de residuos"]
      ],
      "exposed_title": "Si Hay Exposición — Actúe Ahora",
      "exposed_steps": [
        "Mueva a la víctima al aire fresco inmediatamente — contra el viento, no a favor.",
        "Llame al 911 y a su equipo de emergencia de la instalación.",
        "Administre el kit de antídoto de cianuro si está capacitado y autorizado.",
        "Inicie respiración de rescate si la víctima no respira (use dispositivo barrera — no boca a boca).",
        "Retire la ropa contaminada; enjuague la piel con agua por 15+ minutos."
      ],
      "symptoms": "Dolor de cabeza, mareo, confusión, jadeo, convulsiones, piel rojo cereza, colapso."
    }
  },
  {
    "num": "02", "code": "SAF-02",
    "en": {
      "headline": "HEXAVALENT<br><em>CHROMIUM</em>",
      "subhead": "Protect Your Lungs",
      "tagline": "Cr(VI) mist is an OSHA-regulated carcinogen. Every breath at the chrome tank matters.",
      "hazard_signal": "DANGER",
      "hazard_chemical": "Hexavalent Chromium Cr(VI) — Chromic Acid Mist and Dust",
      "hazard_limits": "OSHA PEL: 5 µg/m³ (8-hr TWA) · Action Level: 2.5 µg/m³ · IDLH: 15 mg/m³ as Cr(VI)",
      "danger_title": "The Danger",
      "danger_chips": ["Chromic acid mist generated at tank surface", "Inhalation into lungs", "Cr(VI) penetrates lung tissue", "DNA damage and mutation", "Lung cancer after chronic exposure"],
      "danger_caption": "Cr(VI) is a confirmed human carcinogen. Damage is cumulative and irreversible.",
      "protect_title": "Protect Yourself",
      "protect_steps": [
        "<strong>Local exhaust ventilation</strong> must be running before you approach the chrome tank. Verify airflow.",
        "<strong>Half-face respirator minimum</strong> with P100 or OV/P100 cartridges. Full-face if mist is visible.",
        "<strong>Chemical splash goggles</strong> and face shield at all times near the tank.",
        "<strong>Disposable coveralls or chemical apron</strong> — Cr(VI) on clothing goes home with you.",
        "<strong>Wash hands and face</strong> before eating, drinking, or leaving the plating area. Use designated wash stations."
      ],
      "never_title": "Never Do This",
      "never_rows": [
        ["Work at the chrome tank without ventilation", "Mist concentration spikes in seconds"],
        ["Eat or drink in the chrome plating area", "Ingestion of Cr(VI) residue from surfaces"],
        ["Dry-sweep chrome dust or spills", "Aerosolizes carcinogenic particles"],
        ["Ignore skin ulcers or nasal irritation", "Early signs of chromium exposure damage"]
      ],
      "exposed_title": "If Exposed — Act Now",
      "exposed_steps": [
        "Move to fresh air immediately if you feel throat or chest irritation.",
        "Flush skin contact with water for 15+ minutes — Cr(VI) causes chrome ulcers.",
        "Flush eyes with eyewash for 15 minutes if mist contacts eyes.",
        "Report exposure to your supervisor and occupational health immediately.",
        "Seek medical evaluation — document for your chromium medical surveillance record."
      ],
      "symptoms": "Nasal irritation, nosebleeds, skin ulcers, cough, wheezing, shortness of breath."
    },
    "es": {
      "headline": "CROMO<br><em>HEXAVALENTE</em>",
      "subhead": "Proteja Sus Pulmones",
      "tagline": "La niebla de Cr(VI) es un carcinógeno regulado por OSHA. Cada respiración en el tanque de cromo importa.",
      "hazard_signal": "PELIGRO",
      "hazard_chemical": "Cromo Hexavalente Cr(VI) — Niebla y Polvo de Ácido Crómico",
      "hazard_limits": "OSHA PEL: 5 µg/m³ (TWA 8 hrs) · Nivel de Acción: 2.5 µg/m³ · IDLH: 15 mg/m³ como Cr(VI)",
      "danger_title": "El Peligro",
      "danger_chips": ["Niebla de ácido crómico generada en la superficie del tanque", "Inhalación hacia los pulmones", "Cr(VI) penetra el tejido pulmonar", "Daño al ADN y mutación", "Cáncer de pulmón tras exposición crónica"],
      "danger_caption": "El Cr(VI) es un carcinógeno humano confirmado. El daño es acumulativo e irreversible.",
      "protect_title": "Protéjase",
      "protect_steps": [
        "<strong>Ventilación de extracción local</strong> debe estar funcionando antes de acercarse al tanque de cromo. Verifique el flujo de aire.",
        "<strong>Respirador de media cara mínimo</strong> con cartuchos P100 u OV/P100. Cara completa si la niebla es visible.",
        "<strong>Lentes antisalpicaduras</strong> y careta protectora en todo momento cerca del tanque.",
        "<strong>Overoles desechables o mandil químico</strong> — el Cr(VI) en la ropa se va a casa con usted.",
        "<strong>Lave manos y cara</strong> antes de comer, beber o salir del área de recubrimiento. Use estaciones de lavado designadas."
      ],
      "never_title": "Nunca Haga Esto",
      "never_rows": [
        ["Trabajar en el tanque de cromo sin ventilación", "La concentración de niebla se eleva en segundos"],
        ["Comer o beber en el área de cromado", "Ingestión de residuos de Cr(VI) de superficies"],
        ["Barrer en seco polvo o derrames de cromo", "Aerosoliza partículas carcinógenas"],
        ["Ignorar úlceras en la piel o irritación nasal", "Señales tempranas de daño por exposición al cromo"]
      ],
      "exposed_title": "Si Hay Exposición — Actúe Ahora",
      "exposed_steps": [
        "Muévase al aire fresco inmediatamente si siente irritación en garganta o pecho.",
        "Enjuague el contacto con la piel con agua por 15+ minutos — el Cr(VI) causa úlceras de cromo.",
        "Enjuague los ojos con lavaojos por 15 minutos si la niebla contacta los ojos.",
        "Reporte la exposición a su supervisor y salud ocupacional inmediatamente.",
        "Busque evaluación médica — documente para su registro de vigilancia médica de cromo."
      ],
      "symptoms": "Irritación nasal, sangrado nasal, úlceras en la piel, tos, sibilancias, dificultad para respirar."
    }
  },
  {
    "num": "03", "code": "SAF-03",
    "en": {
      "headline": "ACID TANK<br><em>BURNS</em>",
      "subhead": "Skin and Eye Protection",
      "tagline": "Acid splashes happen fast. The right PPE is the difference between a near-miss and a burn ward visit.",
      "hazard_signal": "DANGER",
      "hazard_chemical": "Sulfuric, Hydrochloric, Nitric, Phosphoric, and Chromic Acids",
      "hazard_limits": "pH < 2 typical · HCl OSHA PEL: 5 ppm ceiling · H₂SO₄ PEL: 1 mg/m³ · HNO₃ PEL: 2 ppm",
      "danger_title": "The Danger",
      "danger_chips": ["Acid splashes during transfer or agitation", "Contact with skin or eyes", "Chemical burn begins immediately", "Tissue destruction deepens with time", "Permanent scarring or vision loss"],
      "danger_caption": "Acid burns continue destroying tissue until the acid is physically flushed away. Seconds matter.",
      "protect_title": "Protect Yourself",
      "protect_steps": [
        "<strong>Chemical splash goggles</strong> — mandatory at all acid tanks. Safety glasses are NOT sufficient.",
        "<strong>Face shield</strong> over goggles for any pouring, transfer, or agitation work.",
        "<strong>Acid-resistant gloves</strong> (butyl or neoprene) — check for pinholes before every use.",
        "<strong>Chemical apron</strong> over long sleeves. No exposed skin between gloves and sleeves.",
        "<strong>Know your eyewash location</strong> — you must reach it in under 10 seconds from any acid station."
      ],
      "never_title": "Never Do This",
      "never_rows": [
        ["Add water to concentrated acid", "Violent exothermic reaction — boiling and spattering"],
        ["Wear contact lenses at acid tanks", "Acid trapped under lenses causes severe corneal damage"],
        ["Use compressed air to agitate acid baths", "Creates aerosol mist that bypasses PPE"],
        ["Reach into a tank without draining first", "Full-arm immersion burns are catastrophic"]
      ],
      "exposed_title": "If Exposed — Act Now",
      "exposed_steps": [
        "Flush skin immediately with water for 20+ minutes — do not stop early.",
        "For eye contact: eyewash station for 15–20 minutes, hold eyelids open.",
        "Remove all contaminated clothing while flushing — acid soaks through fabric.",
        "Call 911 for large-area burns, facial burns, or any eye contact.",
        "Do NOT apply neutralizers, creams, or ointments — water only."
      ],
      "symptoms": "Redness, blistering, white or charred skin, severe pain, eye clouding or vision loss."
    },
    "es": {
      "headline": "QUEMADURAS<br><em>POR ÁCIDO</em>",
      "subhead": "Protección de Piel y Ojos",
      "tagline": "Las salpicaduras de ácido ocurren rápido. El EPP correcto es la diferencia entre un casi-accidente y una quemadura grave.",
      "hazard_signal": "PELIGRO",
      "hazard_chemical": "Ácidos Sulfúrico, Clorhídrico, Nítrico, Fosfórico y Crómico",
      "hazard_limits": "pH < 2 típico · HCl OSHA PEL: 5 ppm techo · H₂SO₄ PEL: 1 mg/m³ · HNO₃ PEL: 2 ppm",
      "danger_title": "El Peligro",
      "danger_chips": ["Salpicadura de ácido durante transferencia o agitación", "Contacto con piel u ojos", "La quemadura química comienza inmediatamente", "La destrucción del tejido se profundiza con el tiempo", "Cicatrices permanentes o pérdida de visión"],
      "danger_caption": "Las quemaduras por ácido continúan destruyendo tejido hasta que el ácido se enjuaga físicamente. Los segundos importan.",
      "protect_title": "Protéjase",
      "protect_steps": [
        "<strong>Lentes antisalpicaduras químicas</strong> — obligatorios en todos los tanques de ácido. Los lentes de seguridad NO son suficientes.",
        "<strong>Careta protectora</strong> sobre los lentes para cualquier vertido, transferencia o agitación.",
        "<strong>Guantes resistentes a ácido</strong> (butilo o neopreno) — revise agujeros antes de cada uso.",
        "<strong>Mandil químico</strong> sobre mangas largas. Sin piel expuesta entre guantes y mangas.",
        "<strong>Conozca la ubicación del lavaojos</strong> — debe llegar en menos de 10 segundos desde cualquier estación de ácido."
      ],
      "never_title": "Nunca Haga Esto",
      "never_rows": [
        ["Agregar agua al ácido concentrado", "Reacción exotérmica violenta — ebullición y salpicadura"],
        ["Usar lentes de contacto en tanques de ácido", "Ácido atrapado bajo los lentes causa daño corneal severo"],
        ["Usar aire comprimido para agitar baños de ácido", "Crea niebla de aerosol que evade el EPP"],
        ["Meter la mano en un tanque sin drenar primero", "Quemaduras por inmersión de brazo completo son catastróficas"]
      ],
      "exposed_title": "Si Hay Exposición — Actúe Ahora",
      "exposed_steps": [
        "Enjuague la piel inmediatamente con agua por 20+ minutos — no se detenga antes.",
        "Para contacto con ojos: lavaojos por 15–20 minutos, mantenga los párpados abiertos.",
        "Retire toda la ropa contaminada mientras enjuaga — el ácido penetra la tela.",
        "Llame al 911 para quemaduras de área grande, quemaduras faciales o cualquier contacto con ojos.",
        "NO aplique neutralizadores, cremas ni ungüentos — solo agua."
      ],
      "symptoms": "Enrojecimiento, ampollas, piel blanca o carbonizada, dolor severo, opacidad ocular o pérdida de visión."
    }
  },
  {
    "num": "04", "code": "SAF-04",
    "en": {
      "headline": "EMERGENCY<br><em>EYEWASH</em>",
      "subhead": "Act in Seconds",
      "tagline": "Chemical eye injuries are time-critical. The first 10 seconds determine whether you keep your sight.",
      "hazard_signal": "DANGER",
      "hazard_chemical": "All Plating Chemicals — Acids, Caustics, Chromates, Cyanides",
      "hazard_limits": "ANSI Z358.1: Eyewash within 10 sec travel · 0.4 GPM for 15 min · Weekly activation test required",
      "danger_title": "The Danger",
      "danger_chips": ["Chemical splash reaches eyes", "Burns cornea and conjunctiva on contact", "Penetration deepens every second", "Scar tissue forms in minutes", "Permanent vision loss if untreated"],
      "danger_caption": "Alkaline chemicals (NaOH, KOH) are worse than acids for eyes — they penetrate deeper and faster.",
      "protect_title": "Protect Yourself",
      "protect_steps": [
        "<strong>Know every eyewash location</strong> on your line. Walk the route blindfolded — you may need to.",
        "<strong>Test weekly</strong> — eyewash stations must flush clean water. Report any non-functional unit immediately.",
        "<strong>Keep paths clear</strong> — no carts, pallets, or hoses blocking access to any eyewash.",
        "<strong>Wear splash goggles</strong> at every chemical station — not safety glasses, goggles.",
        "<strong>Practice the motion</strong> — push the lever, lean in, hold lids open. Do it until it's muscle memory."
      ],
      "never_title": "Never Do This",
      "never_rows": [
        ["Rub your eyes after chemical contact", "Drives the chemical deeper into tissue"],
        ["Delay flushing to 'check what it was'", "Every second of delay increases damage"],
        ["Use a sink or water bottle instead", "Insufficient flow and no lid-hold capability"],
        ["Stop flushing before 15 minutes", "Chemical continues burning beneath the surface"]
      ],
      "exposed_title": "If Exposed — Act Now",
      "exposed_steps": [
        "Get to the nearest eyewash IMMEDIATELY — seconds count.",
        "Push the activation lever and lean into the stream, eyes open.",
        "Hold eyelids open with your fingers — the reflex to close them is strong.",
        "Flush for a FULL 15 minutes minimum. Have someone time you.",
        "Call 911 during flushing — do NOT stop flushing to make the call yourself."
      ],
      "symptoms": "Burning pain, tearing, redness, blurred vision, swelling, inability to open eyes."
    },
    "es": {
      "headline": "LAVAOJOS DE<br><em>EMERGENCIA</em>",
      "subhead": "Actúe en Segundos",
      "tagline": "Las lesiones químicas en los ojos son urgentes. Los primeros 10 segundos determinan si conserva su vista.",
      "hazard_signal": "PELIGRO",
      "hazard_chemical": "Todos los Químicos de Recubrimiento — Ácidos, Cáusticos, Cromatos, Cianuros",
      "hazard_limits": "ANSI Z358.1: Lavaojos a 10 seg de distancia · 0.4 GPM por 15 min · Prueba semanal requerida",
      "danger_title": "El Peligro",
      "danger_chips": ["Salpicadura química alcanza los ojos", "Quema córnea y conjuntiva al contacto", "La penetración se profundiza cada segundo", "Tejido cicatricial se forma en minutos", "Pérdida permanente de visión si no se trata"],
      "danger_caption": "Los químicos alcalinos (NaOH, KOH) son peores que los ácidos para los ojos — penetran más profundo y más rápido.",
      "protect_title": "Protéjase",
      "protect_steps": [
        "<strong>Conozca cada ubicación de lavaojos</strong> en su línea. Camine la ruta con los ojos cerrados — puede que lo necesite.",
        "<strong>Pruebe semanalmente</strong> — las estaciones de lavaojos deben fluir agua limpia. Reporte cualquier unidad que no funcione.",
        "<strong>Mantenga los caminos despejados</strong> — sin carritos, tarimas o mangueras bloqueando acceso a lavaojos.",
        "<strong>Use lentes antisalpicaduras</strong> en cada estación química — no lentes de seguridad, lentes antisalpicaduras.",
        "<strong>Practique el movimiento</strong> — empuje la palanca, inclínese, mantenga los párpados abiertos. Hágalo hasta que sea memoria muscular."
      ],
      "never_title": "Nunca Haga Esto",
      "never_rows": [
        ["Frotar los ojos después del contacto químico", "Lleva el químico más profundo en el tejido"],
        ["Retrasar el enjuague para 'ver qué era'", "Cada segundo de retraso aumenta el daño"],
        ["Usar un fregadero o botella de agua", "Flujo insuficiente y sin capacidad para sostener párpados"],
        ["Dejar de enjuagar antes de 15 minutos", "El químico continúa quemando bajo la superficie"]
      ],
      "exposed_title": "Si Hay Exposición — Actúe Ahora",
      "exposed_steps": [
        "Llegue al lavaojos más cercano INMEDIATAMENTE — los segundos cuentan.",
        "Empuje la palanca de activación e inclínese hacia el chorro, ojos abiertos.",
        "Mantenga los párpados abiertos con los dedos — el reflejo de cerrarlos es fuerte.",
        "Enjuague por un MÍNIMO de 15 minutos completos. Que alguien tome el tiempo.",
        "Llame al 911 durante el enjuague — NO deje de enjuagar para hacer la llamada usted mismo."
      ],
      "symptoms": "Dolor ardiente, lagrimeo, enrojecimiento, visión borrosa, hinchazón, incapacidad de abrir los ojos."
    }
  },
  {
    "num": "05", "code": "SAF-05",
    "en": {
      "headline": "CYANIDE<br><em>WASTE</em>",
      "subhead": "Segregation and Disposal",
      "tagline": "Cyanide waste mixed with acid waste produces lethal HCN gas. Segregation is non-negotiable.",
      "hazard_signal": "DANGER",
      "hazard_chemical": "Cyanide Waste Streams — Rinse Water, Dragout, Spent Solutions",
      "hazard_limits": "OSHA PEL HCN: 10 ppm ceiling · EPA RCRA P-listed waste · DOT Hazard Class 6.1 (Poison)",
      "danger_title": "The Danger",
      "danger_chips": ["Cyanide waste enters acid drain", "pH drops below 10", "HCN gas evolves from solution", "Gas fills confined drain space", "Lethal exposure to workers nearby"],
      "danger_caption": "Even dilute cyanide rinse water can generate deadly HCN if it contacts acid waste.",
      "protect_title": "Protect Yourself",
      "protect_steps": [
        "<strong>Segregate all cyanide waste</strong> into dedicated, labeled containers. Never mix with acid waste streams.",
        "<strong>Maintain pH above 11</strong> in all cyanide waste tanks. Test pH at every shift start.",
        "<strong>Label everything</strong> — pipes, drums, tanks, drains. Color-code cyanide lines distinctly.",
        "<strong>Full-face respirator</strong> with HCN/OV cartridge when handling concentrated cyanide waste.",
        "<strong>Emergency HCN monitor</strong> — fixed monitors at cyanide waste treatment area with audible alarm."
      ],
      "never_title": "Never Do This",
      "never_rows": [
        ["Pour cyanide waste into acid drains", "Generates lethal HCN gas in pipes"],
        ["Mix cyanide and acid waste containers", "Same reaction — different container"],
        ["Treat cyanide waste without pH check", "Acidic conditions release HCN during treatment"],
        ["Store cyanide waste in unlabeled drums", "Next person may add acid waste to the drum"]
      ],
      "exposed_title": "If Exposed — Act Now",
      "exposed_steps": [
        "Evacuate the area upwind immediately — do not attempt rescue without SCBA.",
        "Call 911 and facility emergency response team.",
        "If exposed to HCN gas, move to fresh air — upwind of the source.",
        "Administer cyanide antidote kit if trained. Begin rescue breathing with barrier device.",
        "Ventilate the area with forced air before re-entry."
      ],
      "symptoms": "Bitter almond odor (unreliable), headache, dizziness, rapid breathing, confusion, collapse."
    },
    "es": {
      "headline": "RESIDUOS DE<br><em>CIANURO</em>",
      "subhead": "Segregación y Eliminación",
      "tagline": "Residuos de cianuro mezclados con residuos ácidos producen gas HCN letal. La segregación no es negociable.",
      "hazard_signal": "PELIGRO",
      "hazard_chemical": "Corrientes de Residuos de Cianuro — Agua de Enjuague, Arrastre, Soluciones Agotadas",
      "hazard_limits": "OSHA PEL HCN: 10 ppm techo · EPA RCRA residuo lista P · DOT Clase 6.1 (Veneno)",
      "danger_title": "El Peligro",
      "danger_chips": ["Residuo de cianuro entra al drenaje ácido", "El pH baja de 10", "Gas HCN se libera de la solución", "El gas llena el espacio confinado del drenaje", "Exposición letal a trabajadores cercanos"],
      "danger_caption": "Incluso agua de enjuague diluida de cianuro puede generar HCN mortal si contacta residuos ácidos.",
      "protect_title": "Protéjase",
      "protect_steps": [
        "<strong>Segregue todos los residuos de cianuro</strong> en contenedores dedicados y etiquetados. Nunca mezcle con corrientes de residuos ácidos.",
        "<strong>Mantenga el pH arriba de 11</strong> en todos los tanques de residuos de cianuro. Pruebe el pH al inicio de cada turno.",
        "<strong>Etiquete todo</strong> — tuberías, tambores, tanques, drenajes. Codifique por color las líneas de cianuro de forma distintiva.",
        "<strong>Respirador de cara completa</strong> con cartucho HCN/OV al manejar residuos concentrados de cianuro.",
        "<strong>Monitor de HCN de emergencia</strong> — monitores fijos en el área de tratamiento de residuos de cianuro con alarma audible."
      ],
      "never_title": "Nunca Haga Esto",
      "never_rows": [
        ["Verter residuos de cianuro en drenajes ácidos", "Genera gas HCN letal en las tuberías"],
        ["Mezclar contenedores de residuos de cianuro y ácido", "Misma reacción — diferente contenedor"],
        ["Tratar residuos de cianuro sin verificar pH", "Condiciones ácidas liberan HCN durante el tratamiento"],
        ["Almacenar residuos de cianuro en tambores sin etiqueta", "La siguiente persona puede agregar residuos ácidos al tambor"]
      ],
      "exposed_title": "Si Hay Exposición — Actúe Ahora",
      "exposed_steps": [
        "Evacúe el área contra el viento inmediatamente — no intente rescatar sin SCBA.",
        "Llame al 911 y al equipo de respuesta de emergencia de la instalación.",
        "Si se expuso a gas HCN, muévase al aire fresco — contra el viento de la fuente.",
        "Administre kit de antídoto de cianuro si está capacitado. Inicie respiración de rescate con dispositivo barrera.",
        "Ventile el área con aire forzado antes de reingresar."
      ],
      "symptoms": "Olor a almendra amarga (no confiable), dolor de cabeza, mareo, respiración rápida, confusión, colapso."
    }
  },
  {
    "num": "06", "code": "SAF-06",
    "en": {
      "headline": "CADMIUM<br><em>PLATING</em>",
      "subhead": "Zero Tolerance Exposure",
      "tagline": "Cadmium is a confirmed carcinogen and kidney toxin. There is no safe level of chronic exposure.",
      "hazard_signal": "DANGER",
      "hazard_chemical": "Cadmium Compounds — Cadmium Cyanide, Cadmium Oxide Fumes, Cadmium Dust",
      "hazard_limits": "OSHA PEL: 5 µg/m³ (8-hr TWA) · Action Level: 2.5 µg/m³ · IDLH: 9 mg/m³ (as Cd)",
      "danger_title": "The Danger",
      "danger_chips": ["Cadmium mist or dust generated during plating", "Inhalation or skin absorption", "Cadmium accumulates in kidneys", "Kidney damage and lung disease develop", "Cancer risk after chronic exposure"],
      "danger_caption": "Cadmium stays in the body for decades. A half-life of 10–30 years means today's exposure is tomorrow's disease.",
      "protect_title": "Protect Yourself",
      "protect_steps": [
        "<strong>Enclosed ventilation system</strong> required on all cadmium plating tanks. Verify airflow before starting.",
        "<strong>Full-face PAPR</strong> with P100 HEPA filters for all cadmium tank work.",
        "<strong>Disposable coveralls</strong> — do NOT take work clothing home. Change in designated areas.",
        "<strong>Medical surveillance</strong> — cadmium blood and urine tests as required by OSHA Cadmium Standard (1910.1027).",
        "<strong>Shower before leaving</strong> the cadmium work area. Use separate locker for street clothes."
      ],
      "never_title": "Never Do This",
      "never_rows": [
        ["Take cadmium work clothes home", "Exposes family members to cadmium dust"],
        ["Eat, drink, or smoke in cadmium areas", "Ingestion of cadmium residue from hands/surfaces"],
        ["Dry-sand or grind cadmium plating", "Generates respirable cadmium dust"],
        ["Skip medical surveillance tests", "Kidney damage is silent until it's severe"]
      ],
      "exposed_title": "If Exposed — Act Now",
      "exposed_steps": [
        "Move to fresh air if you inhale cadmium fumes or dust.",
        "Remove contaminated clothing immediately and bag it for proper disposal.",
        "Wash exposed skin thoroughly with soap and water.",
        "Report to occupational health — request cadmium blood/urine levels.",
        "Seek emergency medical care for cadmium fume inhalation (flu-like symptoms within hours)."
      ],
      "symptoms": "Metal fume fever (chills, fever, cough), chest tightness, nausea, kidney pain after chronic exposure."
    },
    "es": {
      "headline": "RECUBRIMIENTO<br><em>CON CADMIO</em>",
      "subhead": "Tolerancia Cero a la Exposición",
      "tagline": "El cadmio es un carcinógeno confirmado y tóxico renal. No existe nivel seguro de exposición crónica.",
      "hazard_signal": "PELIGRO",
      "hazard_chemical": "Compuestos de Cadmio — Cianuro de Cadmio, Humos de Óxido de Cadmio, Polvo de Cadmio",
      "hazard_limits": "OSHA PEL: 5 µg/m³ (TWA 8 hrs) · Nivel de Acción: 2.5 µg/m³ · IDLH: 9 mg/m³ (como Cd)",
      "danger_title": "El Peligro",
      "danger_chips": ["Niebla o polvo de cadmio generado durante el recubrimiento", "Inhalación o absorción cutánea", "El cadmio se acumula en los riñones", "Se desarrolla daño renal y enfermedad pulmonar", "Riesgo de cáncer tras exposición crónica"],
      "danger_caption": "El cadmio permanece en el cuerpo por décadas. Una vida media de 10–30 años significa que la exposición de hoy es la enfermedad de mañana.",
      "protect_title": "Protéjase",
      "protect_steps": [
        "<strong>Sistema de ventilación cerrado</strong> requerido en todos los tanques de cadmio. Verifique el flujo de aire antes de comenzar.",
        "<strong>PAPR de cara completa</strong> con filtros HEPA P100 para todo trabajo en tanques de cadmio.",
        "<strong>Overoles desechables</strong> — NO lleve la ropa de trabajo a casa. Cámbiese en áreas designadas.",
        "<strong>Vigilancia médica</strong> — pruebas de cadmio en sangre y orina según lo requiere el Estándar de Cadmio de OSHA (1910.1027).",
        "<strong>Dúchese antes de salir</strong> del área de trabajo con cadmio. Use casillero separado para ropa de calle."
      ],
      "never_title": "Nunca Haga Esto",
      "never_rows": [
        ["Llevar la ropa de trabajo con cadmio a casa", "Expone a familiares al polvo de cadmio"],
        ["Comer, beber o fumar en áreas de cadmio", "Ingestión de residuos de cadmio de manos/superficies"],
        ["Lijar o esmerilar en seco recubrimiento de cadmio", "Genera polvo de cadmio respirable"],
        ["Omitir las pruebas de vigilancia médica", "El daño renal es silencioso hasta que es severo"]
      ],
      "exposed_title": "Si Hay Exposición — Actúe Ahora",
      "exposed_steps": [
        "Muévase al aire fresco si inhala humos o polvo de cadmio.",
        "Retire la ropa contaminada inmediatamente y empáquela para eliminación adecuada.",
        "Lave la piel expuesta completamente con jabón y agua.",
        "Repórtese a salud ocupacional — solicite niveles de cadmio en sangre/orina.",
        "Busque atención médica de emergencia por inhalación de humos de cadmio (síntomas gripales en horas)."
      ],
      "symptoms": "Fiebre por humos metálicos (escalofríos, fiebre, tos), opresión en el pecho, náusea, dolor renal tras exposición crónica."
    }
  },
  {
    "num": "07", "code": "SAF-07",
    "en": {
      "headline": "NICKEL<br><em>DERMATITIS</em>",
      "subhead": "Skin Protection at the Nickel Line",
      "tagline": "Nickel allergy is the #1 occupational skin disease in plating. Once sensitized, it does not go away.",
      "hazard_signal": "WARNING",
      "hazard_chemical": "Nickel Sulfate, Nickel Chloride, Nickel Sulfamate — All Nickel Plating Solutions",
      "hazard_limits": "OSHA PEL Ni compounds: 1 mg/m³ · ACGIH TLV: 0.1 mg/m³ (inhalable) · IARC Group 1 carcinogen (Ni compounds)",
      "danger_title": "The Danger",
      "danger_chips": ["Nickel solution contacts bare skin", "Skin becomes sensitized over time", "Immune system overreacts to nickel", "Allergic contact dermatitis develops", "Permanent sensitivity — no cure"],
      "danger_caption": "Nickel sensitization is permanent. Once your immune system reacts, even trace contact triggers dermatitis.",
      "protect_title": "Protect Yourself",
      "protect_steps": [
        "<strong>Nitrile or neoprene gloves</strong> at all nickel tanks — never bare hands. Check for tears before each use.",
        "<strong>Long sleeves under apron</strong> — nickel solution on forearms is the most common sensitization route.",
        "<strong>Barrier cream</strong> on exposed skin as a secondary defense. Not a substitute for gloves.",
        "<strong>Wash immediately</strong> if nickel solution contacts skin. Don't wait until break time.",
        "<strong>Report early symptoms</strong> — redness, itching, or rash near hands/wrists. Early detection protects your career."
      ],
      "never_title": "Never Do This",
      "never_rows": [
        ["Handle nickel parts or solutions bare-handed", "Direct route to sensitization"],
        ["Ignore rash or itching near hands/wrists", "Early symptoms become chronic dermatitis"],
        ["Reuse torn or degraded gloves", "Solution seeps through — worse than no gloves"],
        ["Assume 'I'm not allergic yet' means safe", "Sensitization threshold varies — it can happen any day"]
      ],
      "exposed_title": "If Exposed — Act Now",
      "exposed_steps": [
        "Wash affected skin immediately with mild soap and cool water.",
        "Remove contaminated clothing and gloves — bag for laundering.",
        "Apply unscented moisturizer to clean, dry skin if irritation persists.",
        "Report to your supervisor and occupational health for documentation.",
        "See a dermatologist if rash appears or worsens within 24–72 hours."
      ],
      "symptoms": "Redness, itching, small blisters, dry cracked skin, rash on hands/wrists/forearms."
    },
    "es": {
      "headline": "DERMATITIS<br><em>POR NÍQUEL</em>",
      "subhead": "Protección de Piel en la Línea de Níquel",
      "tagline": "La alergia al níquel es la enfermedad ocupacional de piel #1 en recubrimiento. Una vez sensibilizado, no desaparece.",
      "hazard_signal": "ADVERTENCIA",
      "hazard_chemical": "Sulfato de Níquel, Cloruro de Níquel, Sulfamato de Níquel — Todas las Soluciones de Níquel",
      "hazard_limits": "OSHA PEL compuestos Ni: 1 mg/m³ · ACGIH TLV: 0.1 mg/m³ (inhalable) · IARC Grupo 1 carcinógeno (compuestos Ni)",
      "danger_title": "El Peligro",
      "danger_chips": ["Solución de níquel contacta la piel desnuda", "La piel se sensibiliza con el tiempo", "El sistema inmune reacciona exageradamente al níquel", "Se desarrolla dermatitis de contacto alérgica", "Sensibilidad permanente — sin cura"],
      "danger_caption": "La sensibilización al níquel es permanente. Una vez que su sistema inmune reacciona, hasta el contacto mínimo provoca dermatitis.",
      "protect_title": "Protéjase",
      "protect_steps": [
        "<strong>Guantes de nitrilo o neopreno</strong> en todos los tanques de níquel — nunca manos desnudas. Revise roturas antes de cada uso.",
        "<strong>Mangas largas bajo el mandil</strong> — solución de níquel en los antebrazos es la vía de sensibilización más común.",
        "<strong>Crema barrera</strong> en piel expuesta como defensa secundaria. No sustituye los guantes.",
        "<strong>Lave inmediatamente</strong> si la solución de níquel contacta la piel. No espere hasta el descanso.",
        "<strong>Reporte síntomas tempranos</strong> — enrojecimiento, comezón o sarpullido cerca de manos/muñecas. La detección temprana protege su carrera."
      ],
      "never_title": "Nunca Haga Esto",
      "never_rows": [
        ["Manejar partes o soluciones de níquel con manos desnudas", "Vía directa a la sensibilización"],
        ["Ignorar sarpullido o comezón cerca de manos/muñecas", "Los síntomas tempranos se vuelven dermatitis crónica"],
        ["Reutilizar guantes rotos o degradados", "La solución se filtra — peor que sin guantes"],
        ["Asumir 'aún no soy alérgico' significa seguro", "El umbral de sensibilización varía — puede ocurrir cualquier día"]
      ],
      "exposed_title": "Si Hay Exposición — Actúe Ahora",
      "exposed_steps": [
        "Lave la piel afectada inmediatamente con jabón suave y agua fría.",
        "Retire la ropa y guantes contaminados — empaque para lavado.",
        "Aplique humectante sin fragancia en la piel limpia y seca si la irritación persiste.",
        "Reporte a su supervisor y salud ocupacional para documentación.",
        "Vea a un dermatólogo si aparece sarpullido o empeora dentro de 24–72 horas."
      ],
      "symptoms": "Enrojecimiento, comezón, pequeñas ampollas, piel seca y agrietada, sarpullido en manos/muñecas/antebrazos."
    }
  },
  {
    "num": "08", "code": "SAF-08",
    "en": {
      "headline": "ALKALINE<br><em>CLEANER BURNS</em>",
      "subhead": "Not Just Soap and Water",
      "tagline": "Alkaline cleaners dissolve grease — and skin. Caustic burns are sneaky: less pain at first, worse damage underneath.",
      "hazard_signal": "DANGER",
      "hazard_chemical": "Sodium Hydroxide (NaOH), Potassium Hydroxide (KOH), Alkaline Cleaner Concentrates",
      "hazard_limits": "NaOH OSHA PEL: 2 mg/m³ ceiling · pH 12–14 in use · IDLH: 10 mg/m³",
      "danger_title": "The Danger",
      "danger_chips": ["Caustic solution contacts skin or eyes", "Saponifies (dissolves) skin oils and proteins", "Burn feels minor initially", "Tissue destruction continues beneath surface", "Deep burns worse than acid without proper flushing"],
      "danger_caption": "Caustic burns are deceptive — they feel like mild irritation while destroying tissue underneath. Flush long and hard.",
      "protect_title": "Protect Yourself",
      "protect_steps": [
        "<strong>Chemical splash goggles</strong> mandatory at all alkaline cleaning tanks. Caustic eye burns are the worst.",
        "<strong>Neoprene or PVC gloves</strong> — caustic eats through latex. Gauntlet-length for tank work.",
        "<strong>Chemical apron</strong> and long sleeves. Solution splashes farther than you think during loading.",
        "<strong>Face shield</strong> over goggles when adding concentrate or working above tank level.",
        "<strong>Test water quality</strong> — if your skin feels slippery after contact, you're dissolving. Flush immediately."
      ],
      "never_title": "Never Do This",
      "never_rows": [
        ["Dismiss caustic contact as 'just soap'", "Caustic burns destroy deeper tissue than acids"],
        ["Use latex gloves for caustic solutions", "NaOH degrades latex quickly — breakthrough in minutes"],
        ["Lean over open alkaline tanks", "Mist and steam carry caustic to face and eyes"],
        ["Delay flushing 'because it doesn't hurt yet'", "Pain delay is the danger — tissue is already damaged"]
      ],
      "exposed_title": "If Exposed — Act Now",
      "exposed_steps": [
        "Flush skin with water for 20–60 MINUTES. Caustic burns require much longer flushing than acid burns.",
        "For eye contact: eyewash for 20+ minutes minimum. Caustic eye damage is devastating.",
        "Remove all contaminated clothing during flushing — caustic soaks through fabric.",
        "If skin still feels slippery after flushing, continue flushing — caustic remains.",
        "Seek medical attention for ALL caustic eye contact and any burn larger than your palm."
      ],
      "symptoms": "Slippery feel on skin, redness, painless white patches (deep burn), eye clouding, severe delayed pain."
    },
    "es": {
      "headline": "QUEMADURAS POR<br><em>LIMPIADOR ALCALINO</em>",
      "subhead": "No Es Solo Jabón y Agua",
      "tagline": "Los limpiadores alcalinos disuelven grasa — y piel. Las quemaduras cáusticas son engañosas: menos dolor al inicio, peor daño debajo.",
      "hazard_signal": "PELIGRO",
      "hazard_chemical": "Hidróxido de Sodio (NaOH), Hidróxido de Potasio (KOH), Concentrados de Limpiador Alcalino",
      "hazard_limits": "NaOH OSHA PEL: 2 mg/m³ techo · pH 12–14 en uso · IDLH: 10 mg/m³",
      "danger_title": "El Peligro",
      "danger_chips": ["Solución cáustica contacta piel u ojos", "Saponifica (disuelve) aceites y proteínas de la piel", "La quemadura se siente menor al inicio", "La destrucción del tejido continúa bajo la superficie", "Quemaduras profundas peores que ácido sin enjuague adecuado"],
      "danger_caption": "Las quemaduras cáusticas son engañosas — se sienten como irritación leve mientras destruyen el tejido debajo. Enjuague largo e intenso.",
      "protect_title": "Protéjase",
      "protect_steps": [
        "<strong>Lentes antisalpicaduras</strong> obligatorios en todos los tanques de limpieza alcalina. Las quemaduras oculares cáusticas son las peores.",
        "<strong>Guantes de neopreno o PVC</strong> — el cáustico penetra el látex. Largo de guantelete para trabajo en tanques.",
        "<strong>Mandil químico</strong> y mangas largas. La solución salpica más lejos de lo que cree durante la carga.",
        "<strong>Careta protectora</strong> sobre lentes al agregar concentrado o trabajar sobre el nivel del tanque.",
        "<strong>Pruebe la calidad del agua</strong> — si su piel se siente resbalosa después del contacto, se está disolviendo. Enjuague inmediatamente."
      ],
      "never_title": "Nunca Haga Esto",
      "never_rows": [
        ["Desestimar contacto cáustico como 'solo jabón'", "Quemaduras cáusticas destruyen tejido más profundo que ácidos"],
        ["Usar guantes de látex para soluciones cáusticas", "El NaOH degrada el látex rápidamente — penetración en minutos"],
        ["Inclinarse sobre tanques alcalinos abiertos", "La niebla y el vapor llevan cáustico a cara y ojos"],
        ["Retrasar el enjuague 'porque aún no duele'", "El retraso del dolor es el peligro — el tejido ya está dañado"]
      ],
      "exposed_title": "Si Hay Exposición — Actúe Ahora",
      "exposed_steps": [
        "Enjuague la piel con agua por 20–60 MINUTOS. Las quemaduras cáusticas requieren mucho más enjuague que las de ácido.",
        "Para contacto con ojos: lavaojos por 20+ minutos mínimo. El daño ocular cáustico es devastador.",
        "Retire toda la ropa contaminada durante el enjuague — el cáustico penetra la tela.",
        "Si la piel aún se siente resbalosa después del enjuague, continúe enjuagando — queda cáustico.",
        "Busque atención médica para TODO contacto cáustico con ojos y cualquier quemadura mayor que su palma."
      ],
      "symptoms": "Sensación resbalosa en la piel, enrojecimiento, parches blancos sin dolor (quemadura profunda), opacidad ocular, dolor severo tardío."
    }
  },
  {
    "num": "09", "code": "SAF-09",
    "en": {
      "headline": "NITRIC ACID<br><em>AND NOx</em>",
      "subhead": "The Invisible Danger",
      "tagline": "Nitric acid releases toxic NOx fumes that can kill hours after exposure — even if you feel fine at first.",
      "hazard_signal": "DANGER",
      "hazard_chemical": "Nitric Acid (HNO₃) — Nitrogen Dioxide (NO₂) and Nitric Oxide (NO) Fumes",
      "hazard_limits": "HNO₃ OSHA PEL: 2 ppm · NO₂ PEL: 5 ppm ceiling · IDLH NO₂: 20 ppm · NOx is immediately dangerous",
      "danger_title": "The Danger",
      "danger_chips": ["Nitric acid reacts with metals", "Brown/orange NOx fumes released", "Inhalation feels mild at first", "Delayed pulmonary edema (4–24 hours)", "Lungs fill with fluid — death possible"],
      "danger_caption": "NOx damage is DELAYED. You may feel fine for hours, then develop fatal pulmonary edema. Always seek medical evaluation.",
      "protect_title": "Protect Yourself",
      "protect_steps": [
        "<strong>Work only in ventilated areas</strong> — LEV or fume hood required for all nitric acid work.",
        "<strong>Full-face respirator</strong> with acid gas/P100 cartridge. Half-face minimum.",
        "<strong>Chemical splash goggles</strong> and face shield. Nitric acid causes severe eye burns.",
        "<strong>Acid-resistant gloves</strong> (nitrile or butyl). Nitric acid destroys most common glove materials fast.",
        "<strong>Know the color</strong> — brown or orange fumes mean NOx. Evacuate immediately if ventilation fails."
      ],
      "never_title": "Never Do This",
      "never_rows": [
        ["Mix nitric acid with organics or solvents", "Violent reaction — fire or explosion risk"],
        ["Assume 'I feel fine' after NOx exposure", "Delayed pulmonary edema kills 4–24 hours later"],
        ["Work with nitric acid without ventilation", "NOx accumulates in breathing zone rapidly"],
        ["Store nitric acid near bases or organics", "Incompatible storage leads to violent reactions"]
      ],
      "exposed_title": "If Exposed — Act Now",
      "exposed_steps": [
        "Move to fresh air immediately. Even brief NOx inhalation needs medical evaluation.",
        "Call 911 and inform them: nitric acid / NOx exposure — delayed pulmonary edema risk.",
        "REST completely — physical exertion worsens delayed lung damage.",
        "Seek medical evaluation even if asymptomatic. 24-hour observation minimum.",
        "Flush any skin/eye contact with water for 15+ minutes."
      ],
      "symptoms": "Mild cough/irritation initially, then 4–24 hr later: cough, chest tightness, frothy sputum, difficulty breathing."
    },
    "es": {
      "headline": "ÁCIDO NÍTRICO<br><em>Y NOx</em>",
      "subhead": "El Peligro Invisible",
      "tagline": "El ácido nítrico libera humos tóxicos de NOx que pueden matar horas después de la exposición — aunque se sienta bien al inicio.",
      "hazard_signal": "PELIGRO",
      "hazard_chemical": "Ácido Nítrico (HNO₃) — Dióxido de Nitrógeno (NO₂) y Óxido Nítrico (NO)",
      "hazard_limits": "HNO₃ OSHA PEL: 2 ppm · NO₂ PEL: 5 ppm techo · IDLH NO₂: 20 ppm · NOx es inmediatamente peligroso",
      "danger_title": "El Peligro",
      "danger_chips": ["El ácido nítrico reacciona con metales", "Humos de NOx café/naranja se liberan", "La inhalación se siente leve al inicio", "Edema pulmonar tardío (4–24 horas)", "Los pulmones se llenan de líquido — muerte posible"],
      "danger_caption": "El daño por NOx es TARDÍO. Puede sentirse bien por horas, luego desarrollar edema pulmonar fatal. Siempre busque evaluación médica.",
      "protect_title": "Protéjase",
      "protect_steps": [
        "<strong>Trabaje solo en áreas ventiladas</strong> — LEV o campana de humos requerida para todo trabajo con ácido nítrico.",
        "<strong>Respirador de cara completa</strong> con cartucho de gas ácido/P100. Media cara como mínimo.",
        "<strong>Lentes antisalpicaduras</strong> y careta protectora. El ácido nítrico causa quemaduras oculares severas.",
        "<strong>Guantes resistentes a ácido</strong> (nitrilo o butilo). El ácido nítrico destruye la mayoría de guantes comunes rápidamente.",
        "<strong>Conozca el color</strong> — humos cafés o naranjas significan NOx. Evacúe inmediatamente si falla la ventilación."
      ],
      "never_title": "Nunca Haga Esto",
      "never_rows": [
        ["Mezclar ácido nítrico con orgánicos o solventes", "Reacción violenta — riesgo de incendio o explosión"],
        ["Asumir 'me siento bien' después de exposición a NOx", "El edema pulmonar tardío mata 4–24 horas después"],
        ["Trabajar con ácido nítrico sin ventilación", "El NOx se acumula en la zona de respiración rápidamente"],
        ["Almacenar ácido nítrico cerca de bases u orgánicos", "Almacenamiento incompatible lleva a reacciones violentas"]
      ],
      "exposed_title": "Si Hay Exposición — Actúe Ahora",
      "exposed_steps": [
        "Muévase al aire fresco inmediatamente. Incluso inhalación breve de NOx necesita evaluación médica.",
        "Llame al 911 e informe: exposición a ácido nítrico / NOx — riesgo de edema pulmonar tardío.",
        "DESCANSE completamente — el esfuerzo físico empeora el daño pulmonar tardío.",
        "Busque evaluación médica aunque no tenga síntomas. Observación mínima de 24 horas.",
        "Enjuague cualquier contacto con piel/ojos con agua por 15+ minutos."
      ],
      "symptoms": "Tos/irritación leve al inicio, luego 4–24 hrs después: tos, opresión en el pecho, esputo espumoso, dificultad para respirar."
    }
  },
  {
    "num": "10", "code": "SAF-10",
    "en": {
      "headline": "H.E. BAKING<br><em>OVEN SAFETY</em>",
      "subhead": "Hydrogen Embrittlement Baking",
      "tagline": "Baking ovens run at 375–400 °F for hours. Burns, fires, and ventilation failures are real risks.",
      "hazard_signal": "WARNING",
      "hazard_chemical": "High Temperature — Residual Plating Chemistry on Parts — Hydrogen Gas Offgassing",
      "hazard_limits": "Oven temp 375–400 °F (190–205 °C) · Contact burn in < 1 sec above 160 °F · H₂ LEL: 4% in air",
      "danger_title": "The Danger",
      "danger_chips": ["Oven operates at 375–400 °F continuously", "Contact with hot surfaces or racks", "Chemical residue vaporizes in heat", "Hydrogen offgasses from plated parts", "Fire risk if combustibles enter oven"],
      "danger_caption": "Parts, racks, and oven walls cause instant burns at operating temperature. Never rush loading or unloading.",
      "protect_title": "Protect Yourself",
      "protect_steps": [
        "<strong>Heat-resistant gloves</strong> rated for 400 °F minimum when loading/unloading the oven.",
        "<strong>Face shield</strong> when opening the oven door — heat blast and chemical vapors exit fast.",
        "<strong>Long sleeves</strong> and closed-toe boots. No synthetic fabrics near the oven — they melt.",
        "<strong>Verify ventilation</strong> is running before starting the bake cycle. H₂ offgassing needs dilution.",
        "<strong>Never leave combustibles</strong> on top of or inside the oven — rags, gloves, or packaging."
      ],
      "never_title": "Never Do This",
      "never_rows": [
        ["Touch racks or parts without heat gloves", "Instant contact burn at oven temperatures"],
        ["Place wet or dripping parts in the oven", "Water flash-steams — spatters hot chemistry"],
        ["Block oven ventilation openings", "H₂ accumulation creates explosion risk"],
        ["Exceed the bake time 'just to be safe'", "Over-baking can temper and weaken parts"]
      ],
      "exposed_title": "If Exposed — Act Now",
      "exposed_steps": [
        "For thermal burns: cool with running water for 10+ minutes. Do NOT use ice.",
        "Remove clothing from burn area unless it's stuck to the skin.",
        "Cover burn with clean, dry dressing. Do not apply ointments.",
        "For chemical vapor inhalation from oven: move to fresh air, seek medical evaluation.",
        "Call 911 for burns larger than your hand, facial burns, or any breathing difficulty."
      ],
      "symptoms": "Red or blistered skin, white/charred tissue (deep burn), cough from chemical vapors, dizziness."
    },
    "es": {
      "headline": "HORNEADO H.E.<br><em>SEGURIDAD DEL HORNO</em>",
      "subhead": "Horneado para Eliminación de Hidrógeno",
      "tagline": "Los hornos operan a 190–205 °C por horas. Quemaduras, incendios y fallas de ventilación son riesgos reales.",
      "hazard_signal": "ADVERTENCIA",
      "hazard_chemical": "Alta Temperatura — Química Residual de Recubrimiento en Piezas — Desgasificación de Hidrógeno",
      "hazard_limits": "Temp. del horno 190–205 °C · Quemadura por contacto en < 1 seg arriba de 71 °C · H₂ LEL: 4% en aire",
      "danger_title": "El Peligro",
      "danger_chips": ["El horno opera a 190–205 °C continuamente", "Contacto con superficies o racks calientes", "Residuos químicos se vaporizan con el calor", "Hidrógeno se desgasifica de las piezas recubiertas", "Riesgo de incendio si entran combustibles al horno"],
      "danger_caption": "Las piezas, racks y paredes del horno causan quemaduras instantáneas a la temperatura de operación. Nunca apresure la carga o descarga.",
      "protect_title": "Protéjase",
      "protect_steps": [
        "<strong>Guantes resistentes al calor</strong> clasificados para 205 °C mínimo al cargar/descargar el horno.",
        "<strong>Careta protectora</strong> al abrir la puerta del horno — el golpe de calor y vapores químicos salen rápido.",
        "<strong>Mangas largas</strong> y botas cerradas. Sin telas sintéticas cerca del horno — se derriten.",
        "<strong>Verifique la ventilación</strong> antes de iniciar el ciclo de horneado. La desgasificación de H₂ necesita dilución.",
        "<strong>Nunca deje combustibles</strong> encima o dentro del horno — trapos, guantes o empaque."
      ],
      "never_title": "Nunca Haga Esto",
      "never_rows": [
        ["Tocar racks o piezas sin guantes térmicos", "Quemadura por contacto instantánea a temperaturas del horno"],
        ["Colocar piezas mojadas o goteando en el horno", "El agua se evapora violentamente — salpica química caliente"],
        ["Bloquear las aberturas de ventilación del horno", "La acumulación de H₂ crea riesgo de explosión"],
        ["Exceder el tiempo de horneado 'para estar seguro'", "El sobre-horneado puede templar y debilitar las piezas"]
      ],
      "exposed_title": "Si Hay Exposición — Actúe Ahora",
      "exposed_steps": [
        "Para quemaduras térmicas: enfríe con agua corriente por 10+ minutos. NO use hielo.",
        "Retire la ropa del área quemada a menos que esté pegada a la piel.",
        "Cubra la quemadura con vendaje limpio y seco. No aplique ungüentos.",
        "Para inhalación de vapores químicos del horno: muévase al aire fresco, busque evaluación médica.",
        "Llame al 911 para quemaduras mayores que su mano, quemaduras faciales o cualquier dificultad para respirar."
      ],
      "symptoms": "Piel roja o con ampollas, tejido blanco/carbonizado (quemadura profunda), tos por vapores químicos, mareo."
    }
  },
  {
    "num": "11", "code": "SAF-11",
    "en": {
      "headline": "ANODIZE LINE<br><em>HAZARDS</em>",
      "subhead": "Sulfuric Acid and Electrical Hazards",
      "tagline": "The anodize line combines concentrated acid with high-current DC power. Respect both or pay the price.",
      "hazard_signal": "DANGER",
      "hazard_chemical": "Sulfuric Acid (H₂SO₄), Chromic Acid, Caustic Etch (NaOH), DC Electrical Current",
      "hazard_limits": "H₂SO₄ PEL: 1 mg/m³ · NaOH PEL: 2 mg/m³ ceiling · Anodize voltage: 12–100 V DC · Current: 100–10,000 A",
      "danger_title": "The Danger",
      "danger_chips": ["Sulfuric acid splash or mist", "Caustic etch burns from NaOH tanks", "DC arc flash at bus bar connections", "Electrical shock from wet contacts", "Hydrogen gas evolution at cathode"],
      "danger_caption": "Wet hands + DC current + acid = the most dangerous combination in the plating shop.",
      "protect_title": "Protect Yourself",
      "protect_steps": [
        "<strong>Chemical splash goggles + face shield</strong> for all acid and etch tank work.",
        "<strong>Acid-resistant gloves</strong> with gauntlet cuffs. Check for holes every time.",
        "<strong>Rubber-soled boots</strong> — wet floors conduct electricity. Never work in wet shoes.",
        "<strong>Lockout/tagout</strong> the rectifier before touching bus bars, connections, or racks in the tank.",
        "<strong>Ventilation verified</strong> — sulfuric acid mist and hydrogen gas must be exhausted continuously."
      ],
      "never_title": "Never Do This",
      "never_rows": [
        ["Touch bus bars or contacts without LOTO", "DC arc flash at high amperage causes severe burns"],
        ["Work at the anodize tank in wet clothing", "Wet fabric conducts electricity across your body"],
        ["Lean over the acid tank while current is on", "Acid mist + electrical hazard together"],
        ["Ignore hydrogen gas bubbling", "H₂ accumulation creates explosion risk in enclosed areas"]
      ],
      "exposed_title": "If Exposed — Act Now",
      "exposed_steps": [
        "For acid splash: flush with water for 20+ minutes immediately.",
        "For electrical shock: do NOT touch the victim if still in contact — de-energize first.",
        "Call 911 for any electrical shock, arc flash burn, or large-area acid burn.",
        "For H₂SO₄ eye contact: eyewash for 15–20 minutes, hold lids open.",
        "Monitor for delayed symptoms — acid mist inhalation can cause respiratory distress hours later."
      ],
      "symptoms": "Acid burns, muscle contractions (electrical), arc flash blindness, breathing difficulty, hydrogen explosion risk."
    },
    "es": {
      "headline": "LÍNEA DE<br><em>ANODIZADO</em>",
      "subhead": "Ácido Sulfúrico y Riesgos Eléctricos",
      "tagline": "La línea de anodizado combina ácido concentrado con corriente DC de alta potencia. Respete ambos o pague el precio.",
      "hazard_signal": "PELIGRO",
      "hazard_chemical": "Ácido Sulfúrico (H₂SO₄), Ácido Crómico, Ataque Cáustico (NaOH), Corriente Eléctrica DC",
      "hazard_limits": "H₂SO₄ PEL: 1 mg/m³ · NaOH PEL: 2 mg/m³ techo · Voltaje anodizado: 12–100 V DC · Corriente: 100–10,000 A",
      "danger_title": "El Peligro",
      "danger_chips": ["Salpicadura o niebla de ácido sulfúrico", "Quemaduras por ataque cáustico de tanques de NaOH", "Arco eléctrico DC en conexiones de barras", "Choque eléctrico por contactos mojados", "Evolución de gas hidrógeno en el cátodo"],
      "danger_caption": "Manos mojadas + corriente DC + ácido = la combinación más peligrosa en el taller de recubrimiento.",
      "protect_title": "Protéjase",
      "protect_steps": [
        "<strong>Lentes antisalpicaduras + careta protectora</strong> para todo trabajo en tanques de ácido y ataque.",
        "<strong>Guantes resistentes a ácido</strong> con puños de guantelete. Revise agujeros cada vez.",
        "<strong>Botas con suela de hule</strong> — los pisos mojados conducen electricidad. Nunca trabaje con zapatos mojados.",
        "<strong>Bloqueo/etiquetado</strong> del rectificador antes de tocar barras, conexiones o racks en el tanque.",
        "<strong>Ventilación verificada</strong> — la niebla de ácido sulfúrico y el gas hidrógeno deben extraerse continuamente."
      ],
      "never_title": "Nunca Haga Esto",
      "never_rows": [
        ["Tocar barras o contactos sin LOTO", "Arco eléctrico DC a alto amperaje causa quemaduras severas"],
        ["Trabajar en el tanque de anodizado con ropa mojada", "La tela mojada conduce electricidad a través de su cuerpo"],
        ["Inclinarse sobre el tanque de ácido con corriente encendida", "Niebla de ácido + riesgo eléctrico juntos"],
        ["Ignorar el burbujeo de gas hidrógeno", "La acumulación de H₂ crea riesgo de explosión en áreas cerradas"]
      ],
      "exposed_title": "Si Hay Exposición — Actúe Ahora",
      "exposed_steps": [
        "Para salpicadura de ácido: enjuague con agua por 20+ minutos inmediatamente.",
        "Para choque eléctrico: NO toque a la víctima si aún está en contacto — desenergice primero.",
        "Llame al 911 para cualquier choque eléctrico, quemadura por arco eléctrico o quemadura de ácido de área grande.",
        "Para contacto de H₂SO₄ con ojos: lavaojos por 15–20 minutos, mantenga los párpados abiertos.",
        "Monitoree síntomas tardíos — la inhalación de niebla de ácido puede causar dificultad respiratoria horas después."
      ],
      "symptoms": "Quemaduras por ácido, contracciones musculares (eléctricas), ceguera por arco, dificultad para respirar, riesgo de explosión de hidrógeno."
    }
  },
  {
    "num": "12", "code": "SAF-12",
    "en": {
      "headline": "ELECTRO-<br><em>POLISHING</em>",
      "subhead": "Concentrated Acid Mixtures",
      "tagline": "Electropolishing uses hot phosphoric-sulfuric acid at high current. The combination demands maximum respect.",
      "hazard_signal": "DANGER",
      "hazard_chemical": "Phosphoric Acid (H₃PO₄) + Sulfuric Acid (H₂SO₄) Mixture — 140–180 °F Operating Temp",
      "hazard_limits": "H₃PO₄ PEL: 1 mg/m³ · H₂SO₄ PEL: 1 mg/m³ · Operating temp: 140–180 °F · Voltage: 6–18 V DC",
      "danger_title": "The Danger",
      "danger_chips": ["Hot acid mixture splashes during loading", "Acid mist from gas evolution at surface", "DC electrical hazard in wet environment", "Concentrated acid on skin = instant burn", "Metal fumes from dissolving substrate"],
      "danger_caption": "This bath is hot, concentrated, and electrically energized. A single splash combines thermal, chemical, and toxic hazards.",
      "protect_title": "Protect Yourself",
      "protect_steps": [
        "<strong>Full-face shield + chemical goggles</strong> — mandatory for all tank-side work. Hot acid spatters on loading.",
        "<strong>Heavy neoprene gloves</strong> — gauntlet length, rated for hot acid. Check integrity every use.",
        "<strong>Chemical apron + long sleeves</strong>. Tuck sleeves into gloves — no gaps.",
        "<strong>Rubber-soled boots</strong> — acid spills + DC current + wet floor = electrocution risk.",
        "<strong>Ventilation running</strong> before you approach. Hot acid generates more mist than cold acid."
      ],
      "never_title": "Never Do This",
      "never_rows": [
        ["Load parts too fast into hot acid", "Rapid immersion causes violent spattering"],
        ["Add water to hot concentrated acid", "Steam explosion — acid throws across the room"],
        ["Work without verifying LOTO on rectifier", "Energized bus bars + wet hands = shock"],
        ["Ignore rising bath temperature", "Runaway heat = boiling acid and mist explosion"]
      ],
      "exposed_title": "If Exposed — Act Now",
      "exposed_steps": [
        "Flush acid contact with water for 20+ minutes — the burn is both thermal and chemical.",
        "For eye contact: eyewash for 20 minutes minimum. Hot acid eye burns require specialist care.",
        "Remove all contaminated clothing while flushing. Hot acid soaks through instantly.",
        "For electrical shock: de-energize before touching victim. Call 911.",
        "Seek medical evaluation for all exposures — hot acid burns are deeper than they appear."
      ],
      "symptoms": "Immediate burning pain, blistering, white/gray tissue, acid mist cough, electrical tingling."
    },
    "es": {
      "headline": "ELECTRO-<br><em>PULIDO</em>",
      "subhead": "Mezclas de Ácido Concentrado",
      "tagline": "El electropulido usa ácido fosfórico-sulfúrico caliente a alta corriente. La combinación exige máximo respeto.",
      "hazard_signal": "PELIGRO",
      "hazard_chemical": "Ácido Fosfórico (H₃PO₄) + Ácido Sulfúrico (H₂SO₄) — Temp. de Operación 60–82 °C",
      "hazard_limits": "H₃PO₄ PEL: 1 mg/m³ · H₂SO₄ PEL: 1 mg/m³ · Temp. operación: 60–82 °C · Voltaje: 6–18 V DC",
      "danger_title": "El Peligro",
      "danger_chips": ["Mezcla de ácido caliente salpica durante la carga", "Niebla de ácido por evolución de gas en la superficie", "Riesgo eléctrico DC en ambiente mojado", "Ácido concentrado en piel = quemadura instantánea", "Humos metálicos por disolución del sustrato"],
      "danger_caption": "Este baño es caliente, concentrado y electrificado. Una sola salpicadura combina riesgos térmicos, químicos y tóxicos.",
      "protect_title": "Protéjase",
      "protect_steps": [
        "<strong>Careta completa + lentes antisalpicaduras</strong> — obligatorios para todo trabajo junto al tanque. El ácido caliente salpica al cargar.",
        "<strong>Guantes gruesos de neopreno</strong> — largo de guantelete, clasificados para ácido caliente. Verifique integridad cada uso.",
        "<strong>Mandil químico + mangas largas</strong>. Meta las mangas dentro de los guantes — sin espacios.",
        "<strong>Botas con suela de hule</strong> — derrames de ácido + corriente DC + piso mojado = riesgo de electrocución.",
        "<strong>Ventilación funcionando</strong> antes de acercarse. El ácido caliente genera más niebla que el ácido frío."
      ],
      "never_title": "Nunca Haga Esto",
      "never_rows": [
        ["Cargar piezas demasiado rápido en ácido caliente", "La inmersión rápida causa salpicadura violenta"],
        ["Agregar agua al ácido concentrado caliente", "Explosión de vapor — el ácido se lanza por el cuarto"],
        ["Trabajar sin verificar LOTO en el rectificador", "Barras energizadas + manos mojadas = choque"],
        ["Ignorar el aumento de temperatura del baño", "Calor descontrolado = ácido hirviendo y explosión de niebla"]
      ],
      "exposed_title": "Si Hay Exposición — Actúe Ahora",
      "exposed_steps": [
        "Enjuague el contacto con ácido con agua por 20+ minutos — la quemadura es térmica y química.",
        "Para contacto con ojos: lavaojos por 20 minutos mínimo. Quemaduras oculares por ácido caliente requieren atención especializada.",
        "Retire toda la ropa contaminada mientras enjuaga. El ácido caliente penetra instantáneamente.",
        "Para choque eléctrico: desenergice antes de tocar a la víctima. Llame al 911.",
        "Busque evaluación médica para todas las exposiciones — las quemaduras por ácido caliente son más profundas de lo que parecen."
      ],
      "symptoms": "Dolor ardiente inmediato, ampollas, tejido blanco/gris, tos por niebla de ácido, hormigueo eléctrico."
    }
  },
  {
    "num": "13", "code": "SAF-13",
    "en": {
      "headline": "CHEMICAL<br><em>MIXING</em>",
      "subhead": "Order of Addition Matters",
      "tagline": "Adding chemicals in the wrong order causes violent reactions. Read the SDS, follow the procedure, every time.",
      "hazard_signal": "DANGER",
      "hazard_chemical": "All Plating Chemicals — Acids, Bases, Oxidizers, Cyanides, Concentrates",
      "hazard_limits": "Varies by chemical · Exothermic reactions can exceed 200 °F instantly · Splash radius: up to 10+ feet",
      "danger_title": "The Danger",
      "danger_chips": ["Wrong chemical added to tank", "Exothermic reaction begins", "Boiling, spattering, gas evolution", "Acid + cyanide = HCN gas", "Acid + water (reversed) = steam explosion"],
      "danger_caption": "Always add concentrate to water, never water to concentrate. Always add acid to cyanide destroyer, never cyanide to acid.",
      "protect_title": "Protect Yourself",
      "protect_steps": [
        "<strong>Read the SDS and mixing procedure</strong> before every chemical addition. No exceptions.",
        "<strong>Add slowly</strong> — pour concentrate into water/solution in small increments with stirring.",
        "<strong>Full PPE</strong> — goggles, face shield, chemical gloves, apron for all chemical additions.",
        "<strong>Two-person verification</strong> for critical additions (cyanide, chromic acid, concentrated acids).",
        "<strong>Keep incompatibles separated</strong> — acids away from cyanides, oxidizers away from organics."
      ],
      "never_title": "Never Do This",
      "never_rows": [
        ["Add water to concentrated acid", "Violent boiling — acid spatters everywhere"],
        ["Mix chemicals without reading the SDS", "Unknown reactions can be explosive or toxic"],
        ["Rush a chemical addition", "Speed = splash = injury"],
        ["Add acid to cyanide solutions", "Produces lethal HCN gas immediately"]
      ],
      "exposed_title": "If Exposed — Act Now",
      "exposed_steps": [
        "If a violent reaction starts: evacuate the area immediately. Do NOT try to stop it.",
        "Pull the fire alarm if the reaction produces fire, smoke, or toxic fumes.",
        "Move upwind of any gas or vapor release — against the wind, not with it.",
        "Flush any chemical splash with water for 20+ minutes.",
        "Call 911 and provide the chemical names involved in the reaction."
      ],
      "symptoms": "Burns (thermal + chemical), toxic gas inhalation, eye injuries, respiratory distress."
    },
    "es": {
      "headline": "MEZCLA DE<br><em>QUÍMICOS</em>",
      "subhead": "El Orden de Adición Importa",
      "tagline": "Agregar químicos en el orden incorrecto causa reacciones violentas. Lea la HDS, siga el procedimiento, siempre.",
      "hazard_signal": "PELIGRO",
      "hazard_chemical": "Todos los Químicos de Recubrimiento — Ácidos, Bases, Oxidantes, Cianuros, Concentrados",
      "hazard_limits": "Varía por químico · Reacciones exotérmicas pueden exceder 93 °C instantáneamente · Radio de salpicadura: hasta 3+ metros",
      "danger_title": "El Peligro",
      "danger_chips": ["Químico incorrecto agregado al tanque", "La reacción exotérmica comienza", "Ebullición, salpicadura, evolución de gas", "Ácido + cianuro = gas HCN", "Ácido + agua (invertido) = explosión de vapor"],
      "danger_caption": "Siempre agregue concentrado al agua, nunca agua al concentrado. Siempre agregue ácido al destructor de cianuro, nunca cianuro al ácido.",
      "protect_title": "Protéjase",
      "protect_steps": [
        "<strong>Lea la HDS y el procedimiento de mezcla</strong> antes de cada adición química. Sin excepciones.",
        "<strong>Agregue lentamente</strong> — vierta concentrado en agua/solución en pequeños incrementos con agitación.",
        "<strong>EPP completo</strong> — lentes, careta, guantes químicos, mandil para todas las adiciones químicas.",
        "<strong>Verificación de dos personas</strong> para adiciones críticas (cianuro, ácido crómico, ácidos concentrados).",
        "<strong>Mantenga los incompatibles separados</strong> — ácidos lejos de cianuros, oxidantes lejos de orgánicos."
      ],
      "never_title": "Nunca Haga Esto",
      "never_rows": [
        ["Agregar agua al ácido concentrado", "Ebullición violenta — ácido salpica por todos lados"],
        ["Mezclar químicos sin leer la HDS", "Reacciones desconocidas pueden ser explosivas o tóxicas"],
        ["Apresurarse en una adición química", "Velocidad = salpicadura = lesión"],
        ["Agregar ácido a soluciones de cianuro", "Produce gas HCN letal inmediatamente"]
      ],
      "exposed_title": "Si Hay Exposición — Actúe Ahora",
      "exposed_steps": [
        "Si una reacción violenta comienza: evacúe el área inmediatamente. NO intente detenerla.",
        "Active la alarma de incendio si la reacción produce fuego, humo o humos tóxicos.",
        "Muévase contra el viento de cualquier liberación de gas o vapor — contra el viento, no a favor.",
        "Enjuague cualquier salpicadura química con agua por 20+ minutos.",
        "Llame al 911 y proporcione los nombres de los químicos involucrados en la reacción."
      ],
      "symptoms": "Quemaduras (térmicas + químicas), inhalación de gas tóxico, lesiones oculares, dificultad respiratoria."
    }
  },
  {
    "num": "14", "code": "SAF-14",
    "en": {
      "headline": "CONFINED<br><em>SPACE</em>",
      "subhead": "Tank Entry and Cleaning",
      "tagline": "Plating tanks are permit-required confined spaces. Entry without the right procedure kills experienced workers.",
      "hazard_signal": "DANGER",
      "hazard_chemical": "Residual Chemicals — Toxic Atmospheres — Oxygen Deficiency — Engulfment",
      "hazard_limits": "O₂ safe range: 19.5–23.5% · H₂S IDLH: 100 ppm · HCN IDLH: 50 ppm · Permit required per OSHA 1910.146",
      "danger_title": "The Danger",
      "danger_chips": ["Worker enters tank for cleaning/maintenance", "Residual chemicals produce toxic vapor", "Oxygen displaced by inert gas or reactions", "Worker loses consciousness in seconds", "Would-be rescuer enters and also dies"],
      "danger_caption": "60% of confined space deaths are would-be rescuers. Never enter to save someone without proper equipment and training.",
      "protect_title": "Protect Yourself",
      "protect_steps": [
        "<strong>Never enter without a permit</strong> — signed by the entry supervisor with atmospheric testing documented.",
        "<strong>Test the atmosphere</strong> — O₂, LEL, and toxics BEFORE entry and continuously during work.",
        "<strong>Attendant posted outside</strong> at all times. They do NOT enter the space for any reason.",
        "<strong>Rescue plan and equipment</strong> ready before anyone enters — retrieval harness, tripod, SCBA.",
        "<strong>Ventilate continuously</strong> — forced-air ventilation running throughout the entry."
      ],
      "never_title": "Never Do This",
      "never_rows": [
        ["Enter a tank without a permit and gas test", "Invisible toxic or oxygen-deficient atmosphere"],
        ["Enter to rescue without SCBA and harness", "You become the second victim in seconds"],
        ["Assume a tank is safe because it's been drained", "Residual sludge generates toxic gas"],
        ["Leave the entry point unattended", "No one to call for help if you're overcome"]
      ],
      "exposed_title": "If Exposed — Act Now",
      "exposed_steps": [
        "DO NOT enter the space to rescue — call trained rescue team or 911 immediately.",
        "If you can, retrieve the victim using the harness/retrieval system from outside.",
        "Alert everyone in the area — activate the facility emergency alarm.",
        "If the victim is out: move to fresh air, begin CPR if not breathing.",
        "Provide rescuers with chemical information about what was in the tank."
      ],
      "symptoms": "Confusion, loss of consciousness (seconds), difficulty breathing, collapse, no warning with O₂ deficiency."
    },
    "es": {
      "headline": "ESPACIO<br><em>CONFINADO</em>",
      "subhead": "Entrada a Tanques y Limpieza",
      "tagline": "Los tanques de recubrimiento son espacios confinados que requieren permiso. Entrar sin el procedimiento correcto mata a trabajadores experimentados.",
      "hazard_signal": "PELIGRO",
      "hazard_chemical": "Químicos Residuales — Atmósferas Tóxicas — Deficiencia de Oxígeno — Atrapamiento",
      "hazard_limits": "O₂ rango seguro: 19.5–23.5% · H₂S IDLH: 100 ppm · HCN IDLH: 50 ppm · Permiso requerido per OSHA 1910.146",
      "danger_title": "El Peligro",
      "danger_chips": ["Trabajador entra al tanque para limpieza/mantenimiento", "Químicos residuales producen vapor tóxico", "Oxígeno desplazado por gas inerte o reacciones", "Trabajador pierde el conocimiento en segundos", "Rescatista potencial entra y también muere"],
      "danger_caption": "El 60% de las muertes en espacios confinados son rescatistas potenciales. Nunca entre a rescatar sin equipo y capacitación adecuados.",
      "protect_title": "Protéjase",
      "protect_steps": [
        "<strong>Nunca entre sin permiso</strong> — firmado por el supervisor de entrada con pruebas atmosféricas documentadas.",
        "<strong>Pruebe la atmósfera</strong> — O₂, LEL y tóxicos ANTES de entrar y continuamente durante el trabajo.",
        "<strong>Vigía apostado afuera</strong> en todo momento. NO entra al espacio por ninguna razón.",
        "<strong>Plan de rescate y equipo</strong> listos antes de que alguien entre — arnés de recuperación, trípode, SCBA.",
        "<strong>Ventile continuamente</strong> — ventilación forzada funcionando durante toda la entrada."
      ],
      "never_title": "Nunca Haga Esto",
      "never_rows": [
        ["Entrar a un tanque sin permiso y prueba de gas", "Atmósfera tóxica o deficiente de oxígeno invisible"],
        ["Entrar a rescatar sin SCBA y arnés", "Usted se convierte en la segunda víctima en segundos"],
        ["Asumir que un tanque es seguro porque se drenó", "El lodo residual genera gas tóxico"],
        ["Dejar el punto de entrada sin vigilancia", "Nadie para pedir ayuda si usted es vencido"]
      ],
      "exposed_title": "Si Hay Exposición — Actúe Ahora",
      "exposed_steps": [
        "NO entre al espacio a rescatar — llame al equipo de rescate capacitado o al 911 inmediatamente.",
        "Si puede, recupere a la víctima usando el sistema de arnés/recuperación desde afuera.",
        "Alerte a todos en el área — active la alarma de emergencia de la instalación.",
        "Si la víctima está afuera: mueva al aire fresco, inicie RCP si no respira.",
        "Proporcione a los rescatistas información química sobre lo que estaba en el tanque."
      ],
      "symptoms": "Confusión, pérdida del conocimiento (segundos), dificultad para respirar, colapso, sin advertencia con deficiencia de O₂."
    }
  },
  {
    "num": "15", "code": "SAF-15",
    "en": {
      "headline": "ELECTRICAL<br><em>SAFETY</em>",
      "subhead": "Rectifiers and Bus Bars",
      "tagline": "Plating rectifiers deliver thousands of amps at low voltage. Enough to vaporize a wrench and blind you permanently.",
      "hazard_signal": "DANGER",
      "hazard_chemical": "DC Electrical Energy — Arc Flash — Molten Metal Spray from Bus Bar Faults",
      "hazard_limits": "Typical: 6–18 V DC at 500–10,000 A · Arc flash energy: up to 40 cal/cm² · Bus bar temp: 150+ °F normal",
      "danger_title": "The Danger",
      "danger_chips": ["Metal tool bridges bus bar terminals", "Massive short-circuit current flows", "Arc flash: 35,000 °F plasma ball", "Molten copper spray in all directions", "Blast pressure throws worker backwards"],
      "danger_caption": "Low voltage does NOT mean low danger. At 5,000 amps, a dropped wrench becomes a bomb.",
      "protect_title": "Protect Yourself",
      "protect_steps": [
        "<strong>Lockout/tagout</strong> before any work on rectifiers, bus bars, or connections. No exceptions.",
        "<strong>Insulated tools only</strong> when working near energized bus bars. No bare metal tools.",
        "<strong>Remove all jewelry</strong> — rings, watches, chains conduct current and cause severe burns.",
        "<strong>Arc-flash rated PPE</strong> if you must work near energized equipment — per NFPA 70E.",
        "<strong>Dry hands, dry floors</strong> — water + electricity = path through your body."
      ],
      "never_title": "Never Do This",
      "never_rows": [
        ["Use metal tools near energized bus bars", "Tool bridges terminals = instant arc flash"],
        ["Wear jewelry near rectifiers", "Ring welds to bus bar — finger amputation"],
        ["Bypass safety interlocks on rectifiers", "Interlocks exist because people died without them"],
        ["Work on wet bus bars without LOTO", "Water creates conductive path at lethal amperage"]
      ],
      "exposed_title": "If Exposed — Act Now",
      "exposed_steps": [
        "De-energize the circuit BEFORE touching the victim — you'll become the second casualty.",
        "Call 911 immediately for any arc flash or electrical contact injury.",
        "If victim is not breathing, begin CPR. Electrical shock can stop the heart.",
        "Cool arc flash burns with water — do NOT remove stuck clothing.",
        "Preserve the scene for investigation — do not reset the rectifier until cleared."
      ],
      "symptoms": "Burns (entry/exit wounds), cardiac arrhythmia, muscle spasms, arc flash blindness, hearing loss from blast."
    },
    "es": {
      "headline": "SEGURIDAD<br><em>ELÉCTRICA</em>",
      "subhead": "Rectificadores y Barras de Bus",
      "tagline": "Los rectificadores entregan miles de amperios a bajo voltaje. Suficiente para vaporizar una herramienta y cegarlo permanentemente.",
      "hazard_signal": "PELIGRO",
      "hazard_chemical": "Energía Eléctrica DC — Arco Eléctrico — Rociado de Metal Fundido por Fallas en Barras",
      "hazard_limits": "Típico: 6–18 V DC a 500–10,000 A · Energía de arco: hasta 40 cal/cm² · Temp. barra: 65+ °C normal",
      "danger_title": "El Peligro",
      "danger_chips": ["Herramienta metálica puentea terminales de barra", "Corriente masiva de cortocircuito fluye", "Arco eléctrico: bola de plasma a 19,000 °C", "Rociado de cobre fundido en todas direcciones", "Presión de la explosión lanza al trabajador hacia atrás"],
      "danger_caption": "Bajo voltaje NO significa bajo peligro. A 5,000 amperios, una llave caída se convierte en una bomba.",
      "protect_title": "Protéjase",
      "protect_steps": [
        "<strong>Bloqueo/etiquetado</strong> antes de cualquier trabajo en rectificadores, barras o conexiones. Sin excepciones.",
        "<strong>Solo herramientas aisladas</strong> al trabajar cerca de barras energizadas. Sin herramientas de metal desnudo.",
        "<strong>Retire toda la joyería</strong> — anillos, relojes, cadenas conducen corriente y causan quemaduras severas.",
        "<strong>EPP clasificado para arco eléctrico</strong> si debe trabajar cerca de equipo energizado — según NFPA 70E.",
        "<strong>Manos secas, pisos secos</strong> — agua + electricidad = camino a través de su cuerpo."
      ],
      "never_title": "Nunca Haga Esto",
      "never_rows": [
        ["Usar herramientas metálicas cerca de barras energizadas", "Herramienta puentea terminales = arco instantáneo"],
        ["Usar joyería cerca de rectificadores", "Anillo se suelda a la barra — amputación de dedo"],
        ["Puentear los enclavamientos de seguridad en rectificadores", "Los enclavamientos existen porque personas murieron sin ellos"],
        ["Trabajar en barras mojadas sin LOTO", "El agua crea camino conductivo a amperaje letal"]
      ],
      "exposed_title": "Si Hay Exposición — Actúe Ahora",
      "exposed_steps": [
        "Desenergice el circuito ANTES de tocar a la víctima — usted será la segunda víctima.",
        "Llame al 911 inmediatamente para cualquier arco eléctrico o lesión por contacto eléctrico.",
        "Si la víctima no respira, inicie RCP. El choque eléctrico puede detener el corazón.",
        "Enfríe las quemaduras por arco con agua — NO retire ropa adherida.",
        "Preserve la escena para investigación — no reinicie el rectificador hasta que se autorice."
      ],
      "symptoms": "Quemaduras (heridas de entrada/salida), arritmia cardíaca, espasmos musculares, ceguera por arco, pérdida de audición por la explosión."
    }
  },
  {
    "num": "16", "code": "SAF-16",
    "en": {
      "headline": "VENTILATION<br><em>FAILURE</em>",
      "subhead": "What to Do When the Air Stops",
      "tagline": "When ventilation fails on a chemical line, toxic concentrations can reach dangerous levels in minutes.",
      "hazard_signal": "DANGER",
      "hazard_chemical": "All Tank Chemistries — Acid Mist, Alkaline Mist, Cyanide Vapor, Chrome Mist, NOx",
      "hazard_limits": "Varies by tank — multiple PELs exceeded simultaneously · HCN, Cr(VI), NOx can reach IDLH in minutes",
      "danger_title": "The Danger",
      "danger_chips": ["Exhaust fan or ductwork fails", "Chemical mist/vapor stops being removed", "Breathing zone concentration rises rapidly", "Multiple chemicals accumulate simultaneously", "Workers may not notice until symptomatic"],
      "danger_caption": "Chemical mist is often invisible. By the time you smell or feel it, you've already been overexposed.",
      "protect_title": "Protect Yourself",
      "protect_steps": [
        "<strong>Know the alarm</strong> — learn what ventilation failure sounds and looks like on your line.",
        "<strong>Check airflow indicators</strong> at the start of every shift — flags, manometers, or smoke tubes.",
        "<strong>Stop work immediately</strong> if ventilation fails. Do not continue 'just to finish this load.'",
        "<strong>Evacuate the area</strong> upwind. Do not re-enter until ventilation is restored and verified.",
        "<strong>Report immediately</strong> — ventilation failure is an emergency, not a maintenance request."
      ],
      "never_title": "Never Do This",
      "never_rows": [
        ["Keep working 'until the load is done'", "Toxic concentration rises every second without exhaust"],
        ["Assume a fan restart fixes the problem", "Ductwork blockage or damper failure may persist"],
        ["Prop open doors as a substitute for LEV", "Cross-drafts spread contamination, don't remove it"],
        ["Ignore reduced airflow or unusual smells", "Early signs of ventilation degradation before full failure"]
      ],
      "exposed_title": "If Exposed — Act Now",
      "exposed_steps": [
        "Evacuate the plating area immediately — move upwind and to fresh air.",
        "Alert all workers in the area — activate emergency notification.",
        "Report symptoms to your supervisor and seek medical evaluation.",
        "Do NOT re-enter until maintenance confirms ventilation is restored and air monitoring clears.",
        "For NOx or cyanide line failures: 24-hour medical observation even if asymptomatic."
      ],
      "symptoms": "Eye/throat irritation, headache, cough, metallic taste, dizziness, nausea, difficulty breathing."
    },
    "es": {
      "headline": "FALLA DE<br><em>VENTILACIÓN</em>",
      "subhead": "Qué Hacer Cuando el Aire Se Detiene",
      "tagline": "Cuando la ventilación falla en una línea química, las concentraciones tóxicas pueden alcanzar niveles peligrosos en minutos.",
      "hazard_signal": "PELIGRO",
      "hazard_chemical": "Todas las Químicas de Tanques — Niebla Ácida, Niebla Alcalina, Vapor de Cianuro, Niebla de Cromo, NOx",
      "hazard_limits": "Varía por tanque — múltiples PEL excedidos simultáneamente · HCN, Cr(VI), NOx pueden alcanzar IDLH en minutos",
      "danger_title": "El Peligro",
      "danger_chips": ["Ventilador de extracción o ducto falla", "La niebla/vapor químico deja de removerse", "La concentración en zona de respiración sube rápidamente", "Múltiples químicos se acumulan simultáneamente", "Los trabajadores pueden no notarlo hasta tener síntomas"],
      "danger_caption": "La niebla química es frecuentemente invisible. Para cuando la huele o la siente, ya ha sido sobreexpuesto.",
      "protect_title": "Protéjase",
      "protect_steps": [
        "<strong>Conozca la alarma</strong> — aprenda cómo suena y se ve la falla de ventilación en su línea.",
        "<strong>Verifique indicadores de flujo</strong> al inicio de cada turno — banderas, manómetros o tubos de humo.",
        "<strong>Detenga el trabajo inmediatamente</strong> si falla la ventilación. No continúe 'solo para terminar esta carga.'",
        "<strong>Evacúe el área</strong> contra el viento. No reingrese hasta que la ventilación sea restaurada y verificada.",
        "<strong>Reporte inmediatamente</strong> — la falla de ventilación es una emergencia, no una solicitud de mantenimiento."
      ],
      "never_title": "Nunca Haga Esto",
      "never_rows": [
        ["Seguir trabajando 'hasta terminar la carga'", "La concentración tóxica sube cada segundo sin extracción"],
        ["Asumir que reiniciar el ventilador arregla el problema", "Bloqueo de ducto o falla de compuerta puede persistir"],
        ["Abrir puertas como sustituto del LEV", "Las corrientes cruzadas esparcen contaminación, no la remueven"],
        ["Ignorar flujo de aire reducido u olores inusuales", "Señales tempranas de degradación antes de la falla total"]
      ],
      "exposed_title": "Si Hay Exposición — Actúe Ahora",
      "exposed_steps": [
        "Evacúe el área de recubrimiento inmediatamente — muévase contra el viento y al aire fresco.",
        "Alerte a todos los trabajadores en el área — active la notificación de emergencia.",
        "Reporte síntomas a su supervisor y busque evaluación médica.",
        "NO reingrese hasta que mantenimiento confirme que la ventilación está restaurada y el monitoreo de aire despeje.",
        "Para fallas en línea de NOx o cianuro: observación médica de 24 horas aunque no tenga síntomas."
      ],
      "symptoms": "Irritación de ojos/garganta, dolor de cabeza, tos, sabor metálico, mareo, náusea, dificultad para respirar."
    }
  },
  {
    "num": "17", "code": "SAF-17",
    "en": {
      "headline": "SPILL<br><em>RESPONSE</em>",
      "subhead": "Know Your Chemical, Know Your Kit",
      "tagline": "Every chemical spill is different. The wrong cleanup makes it worse. Match the response to the hazard.",
      "hazard_signal": "DANGER",
      "hazard_chemical": "All Plating Chemicals — Acids, Bases, Cyanides, Chromates, Solvents",
      "hazard_limits": "Varies by chemical · Cyanide + acid = HCN gas · Chromate spills = RCRA hazardous waste · Reportable quantities apply",
      "danger_title": "The Danger",
      "danger_chips": ["Chemical container tips, line leaks, or tank overflow", "Spill spreads across floor", "Incompatible chemicals mix in drain", "Toxic gas released from reaction", "Slip/fall into pooled chemical"],
      "danger_caption": "A spill on a wet plating floor reaches the drain in seconds. Know what's in that drain before it gets there.",
      "protect_title": "Protect Yourself",
      "protect_steps": [
        "<strong>Identify the chemical first</strong> — read the label or SDS before touching anything.",
        "<strong>Use the correct spill kit</strong> — acid, caustic, and cyanide spills need different absorbents.",
        "<strong>Full PPE</strong> for cleanup — goggles, face shield, chemical gloves, apron, boots.",
        "<strong>Contain first, clean second</strong> — dam the spill to stop it spreading to drains or other chemicals.",
        "<strong>Report every spill</strong> — even small ones. Spill logs protect you and your facility."
      ],
      "never_title": "Never Do This",
      "never_rows": [
        ["Hose a chemical spill into the floor drain", "Sends untreated hazardous waste into the system"],
        ["Use the wrong neutralizer", "Acid neutralizer on cyanide = HCN gas"],
        ["Clean up Cr(VI) spills without hazmat PPE", "Chromate dust is carcinogenic"],
        ["Ignore a 'small' drip or leak", "Small leaks become big spills — and chronic exposures"]
      ],
      "exposed_title": "If Exposed — Act Now",
      "exposed_steps": [
        "If you slip or fall into a spill: get out, strip contaminated clothing, flush skin 20+ minutes.",
        "If gas is evolving from the spill: evacuate upwind immediately — do NOT attempt cleanup.",
        "Call your spill response team. For large spills, call 911 and your environmental coordinator.",
        "Block drains downstream of the spill to prevent environmental release.",
        "Document everything: chemical, quantity, time, response actions, and who was exposed."
      ],
      "symptoms": "Chemical burns, slip injuries, toxic inhalation (chemical-dependent), eye irritation."
    },
    "es": {
      "headline": "RESPUESTA A<br><em>DERRAMES</em>",
      "subhead": "Conozca Su Químico, Conozca Su Kit",
      "tagline": "Cada derrame químico es diferente. La limpieza incorrecta lo empeora. Ajuste la respuesta al peligro.",
      "hazard_signal": "PELIGRO",
      "hazard_chemical": "Todos los Químicos de Recubrimiento — Ácidos, Bases, Cianuros, Cromatos, Solventes",
      "hazard_limits": "Varía por químico · Cianuro + ácido = gas HCN · Derrames de cromato = residuo peligroso RCRA · Cantidades reportables aplican",
      "danger_title": "El Peligro",
      "danger_chips": ["Contenedor se voltea, línea gotea o tanque se desborda", "El derrame se esparce por el piso", "Químicos incompatibles se mezclan en el drenaje", "Gas tóxico liberado por la reacción", "Resbalón/caída en químico acumulado"],
      "danger_caption": "Un derrame en un piso mojado de recubrimiento llega al drenaje en segundos. Sepa qué hay en ese drenaje antes de que llegue.",
      "protect_title": "Protéjase",
      "protect_steps": [
        "<strong>Identifique el químico primero</strong> — lea la etiqueta o HDS antes de tocar nada.",
        "<strong>Use el kit de derrames correcto</strong> — derrames de ácido, cáustico y cianuro necesitan absorbentes diferentes.",
        "<strong>EPP completo</strong> para limpieza — lentes, careta, guantes químicos, mandil, botas.",
        "<strong>Contenga primero, limpie después</strong> — represar el derrame para evitar que llegue a drenajes u otros químicos.",
        "<strong>Reporte cada derrame</strong> — incluso los pequeños. Los registros de derrames lo protegen a usted y a su instalación."
      ],
      "never_title": "Nunca Haga Esto",
      "never_rows": [
        ["Enjuagar un derrame químico al drenaje del piso", "Envía residuos peligrosos sin tratar al sistema"],
        ["Usar el neutralizador incorrecto", "Neutralizador de ácido sobre cianuro = gas HCN"],
        ["Limpiar derrames de Cr(VI) sin EPP de materiales peligrosos", "El polvo de cromato es carcinógeno"],
        ["Ignorar un goteo o fuga 'pequeño'", "Las fugas pequeñas se vuelven derrames grandes — y exposiciones crónicas"]
      ],
      "exposed_title": "Si Hay Exposición — Actúe Ahora",
      "exposed_steps": [
        "Si resbala o cae en un derrame: salga, retire la ropa contaminada, enjuague la piel 20+ minutos.",
        "Si hay gas emanando del derrame: evacúe contra el viento inmediatamente — NO intente limpiar.",
        "Llame a su equipo de respuesta a derrames. Para derrames grandes, llame al 911 y su coordinador ambiental.",
        "Bloquee los drenajes aguas abajo del derrame para prevenir liberación ambiental.",
        "Documente todo: químico, cantidad, hora, acciones de respuesta y quién fue expuesto."
      ],
      "symptoms": "Quemaduras químicas, lesiones por resbalón, inhalación tóxica (depende del químico), irritación ocular."
    }
  },
  {
    "num": "18", "code": "SAF-18",
    "en": {
      "headline": "COMPRESSED<br><em>GAS</em>",
      "subhead": "Nitrogen, Air, and Hydrogen Safety",
      "tagline": "A ruptured cylinder is a missile. Hydrogen is invisible and explosive. Nitrogen displaces oxygen without warning.",
      "hazard_signal": "DANGER",
      "hazard_chemical": "Compressed Nitrogen (N₂), Hydrogen (H₂), Compressed Air — High-Pressure Cylinders",
      "hazard_limits": "Cylinder pressure: 2,000–2,400 psi · H₂ LEL: 4% in air · N₂: simple asphyxiant — no warning properties",
      "danger_title": "The Danger",
      "danger_chips": ["Cylinder valve damage or failure", "High-pressure gas release", "Cylinder becomes uncontrolled projectile", "H₂ accumulation reaches explosive range", "N₂ displaces O₂ in enclosed space"],
      "danger_caption": "Nitrogen is odorless and colorless. It kills by silently replacing the oxygen you breathe. You get no warning.",
      "protect_title": "Protect Yourself",
      "protect_steps": [
        "<strong>Chain or strap all cylinders</strong> upright to a wall, rack, or cart. Never leave them free-standing.",
        "<strong>Valve caps on</strong> during storage and transport. The valve is the most vulnerable point.",
        "<strong>Never use damaged regulators</strong> — replace immediately. Leaking regulators create fire/explosion risk.",
        "<strong>H₂ detection</strong> — ensure monitors are in place where hydrogen is used or stored.",
        "<strong>Ventilate enclosed areas</strong> where N₂ is used — oxygen monitors required per OSHA."
      ],
      "never_title": "Never Do This",
      "never_rows": [
        ["Leave cylinders unsecured", "Tipped cylinder + broken valve = 2,000 psi rocket"],
        ["Use hydrogen near ignition sources", "H₂ ignites at 4% in air — invisible flame"],
        ["Enter N₂-purged space without O₂ monitor", "Unconsciousness in one breath at < 6% O₂"],
        ["Use compressed gas to blow off clothing", "Gas injection under skin requires surgical removal"]
      ],
      "exposed_title": "If Exposed — Act Now",
      "exposed_steps": [
        "For N₂ displacement: move victim to fresh air immediately. Begin CPR if not breathing.",
        "For H₂ leak: evacuate, eliminate ignition sources, ventilate from a safe distance.",
        "For cylinder rupture: evacuate the area — do NOT approach until gas is fully vented.",
        "Call 911 for any gas release in an enclosed space or any H₂ ignition event.",
        "For high-pressure gas injection injury: seek emergency surgery — this is a medical emergency."
      ],
      "symptoms": "N₂ asphyxiation: sudden collapse, no warning. H₂ fire: invisible flame, radiant heat burns. Gas injection: swelling, extreme pain."
    },
    "es": {
      "headline": "GAS<br><em>COMPRIMIDO</em>",
      "subhead": "Seguridad con Nitrógeno, Aire e Hidrógeno",
      "tagline": "Un cilindro roto es un misil. El hidrógeno es invisible y explosivo. El nitrógeno desplaza el oxígeno sin advertencia.",
      "hazard_signal": "PELIGRO",
      "hazard_chemical": "Nitrógeno Comprimido (N₂), Hidrógeno (H₂), Aire Comprimido — Cilindros de Alta Presión",
      "hazard_limits": "Presión del cilindro: 2,000–2,400 psi · H₂ LEL: 4% en aire · N₂: asfixiante simple — sin propiedades de advertencia",
      "danger_title": "El Peligro",
      "danger_chips": ["Daño o falla de válvula del cilindro", "Liberación de gas a alta presión", "El cilindro se convierte en proyectil descontrolado", "Acumulación de H₂ alcanza rango explosivo", "N₂ desplaza O₂ en espacio cerrado"],
      "danger_caption": "El nitrógeno es inodoro e incoloro. Mata al reemplazar silenciosamente el oxígeno que respira. No recibe advertencia.",
      "protect_title": "Protéjase",
      "protect_steps": [
        "<strong>Encadene o asegure todos los cilindros</strong> verticalmente a una pared, rack o carro. Nunca los deje sueltos.",
        "<strong>Tapas de válvula puestas</strong> durante almacenamiento y transporte. La válvula es el punto más vulnerable.",
        "<strong>Nunca use reguladores dañados</strong> — reemplace inmediatamente. Reguladores con fugas crean riesgo de incendio/explosión.",
        "<strong>Detección de H₂</strong> — asegure que haya monitores donde se usa o almacena hidrógeno.",
        "<strong>Ventile áreas cerradas</strong> donde se usa N₂ — monitores de oxígeno requeridos según OSHA."
      ],
      "never_title": "Nunca Haga Esto",
      "never_rows": [
        ["Dejar cilindros sin asegurar", "Cilindro volcado + válvula rota = cohete de 2,000 psi"],
        ["Usar hidrógeno cerca de fuentes de ignición", "H₂ se enciende al 4% en aire — llama invisible"],
        ["Entrar a espacio purgado con N₂ sin monitor de O₂", "Pérdida del conocimiento en una respiración a < 6% O₂"],
        ["Usar gas comprimido para soplar la ropa", "Inyección de gas bajo la piel requiere cirugía"]
      ],
      "exposed_title": "Si Hay Exposición — Actúe Ahora",
      "exposed_steps": [
        "Para desplazamiento de N₂: mueva a la víctima al aire fresco inmediatamente. Inicie RCP si no respira.",
        "Para fuga de H₂: evacúe, elimine fuentes de ignición, ventile desde distancia segura.",
        "Para ruptura de cilindro: evacúe el área — NO se acerque hasta que el gas se ventile completamente.",
        "Llame al 911 para cualquier liberación de gas en espacio cerrado o cualquier evento de ignición de H₂.",
        "Para lesión por inyección de gas a alta presión: busque cirugía de emergencia — es una emergencia médica."
      ],
      "symptoms": "Asfixia por N₂: colapso repentino, sin advertencia. Fuego de H₂: llama invisible, quemaduras por calor radiante. Inyección de gas: hinchazón, dolor extremo."
    }
  },
]

# ─── HTML TEMPLATE ────────────────────────────────────────────────────────────
def build_html(topic, lang, edition):
    """Build one poster HTML file."""
    d = topic[lang]
    num = topic["num"]
    code = topic["code"]
    is_light = edition == "light"
    is_es = lang == "es"

    # Edition body attribute
    body_attr = ' data-edition="light"' if is_light else ''

    # Eyebrow
    if is_es:
        eyebrow = f"Plating Posters Inc &mdash; Piso de Producción &mdash; Serie de Seguridad &mdash; {num}"
    else:
        eyebrow = f"Plating Posters Inc &mdash; Shop Floor &mdash; Safety Series &mdash; {num}"

    # Signal word color
    signal_color = "#E05C5C"  # coral for DANGER/PELIGRO
    if d["hazard_signal"] in ("WARNING", "ADVERTENCIA"):
        signal_color = "#E8A020"  # amber for WARNING

    # Hazard banner
    hazard_banner = f"""
    <div class="glass" style="padding:10px 14px;background:rgba(224,92,92,.10);border:1px solid rgba(224,92,92,.25);">
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:6px;">
        <span style="font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:22px;color:{signal_color};letter-spacing:.04em;">&#9888; {d['hazard_signal']}</span>
      </div>
      <div style="font-family:'Inter',sans-serif;font-weight:600;font-size:12px;color:var(--text);line-height:1.35;margin-bottom:4px;">{d['hazard_chemical']}</div>
      <div style="font-family:'JetBrains Mono',monospace;font-size:9.5px;color:var(--muted);line-height:1.4;">{d['hazard_limits']}</div>
    </div>"""

    # Danger zone — pathway chips
    chips_html = "".join(
        f'<span style="display:inline-block;padding:3px 8px;border-radius:6px;background:rgba(224,92,92,.08);border:1px solid rgba(224,92,92,.18);font-size:10px;color:var(--coral);font-weight:600;white-space:nowrap;">{c}</span>'
        for c in d["danger_chips"]
    )
    # Add arrows between chips
    chips_with_arrows = ""
    for i, c in enumerate(d["danger_chips"]):
        if i > 0:
            chips_with_arrows += '<span style="color:var(--coral);font-size:12px;margin:0 2px;">&rarr;</span>'
        chips_with_arrows += f'<span style="display:inline-block;padding:3px 8px;border-radius:6px;background:rgba(224,92,92,.08);border:1px solid rgba(224,92,92,.18);font-size:10px;color:var(--coral);font-weight:600;">{c}</span>'

    danger_zone = f"""
    <div class="glass" style="padding:10px 14px;">
      <div class="section-title" style="color:var(--coral);">{d['danger_title']}</div>
      <div style="display:flex;flex-wrap:wrap;align-items:center;gap:4px;margin-bottom:6px;">
        {chips_with_arrows}
      </div>
      <div style="font-family:'Inter',sans-serif;font-size:11px;color:var(--muted);line-height:1.4;font-style:italic;">{d['danger_caption']}</div>
    </div>"""

    # Protect zone — 5 numbered steps
    protect_items = ""
    for i, step in enumerate(d["protect_steps"], 1):
        protect_items += f"""
        <div style="display:flex;gap:8px;align-items:flex-start;">
          <div style="flex-shrink:0;width:22px;height:22px;border-radius:50%;background:rgba(39,174,96,.12);border:1px solid rgba(39,174,96,.3);display:flex;align-items:center;justify-content:center;font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:11px;color:var(--emerald);">{i}</div>
          <div style="font-family:'Inter',sans-serif;font-size:11px;color:var(--text);line-height:1.4;">{step}</div>
        </div>"""

    protect_zone = f"""
    <div class="glass" style="padding:10px 14px;">
      <div class="section-title" style="color:var(--emerald);">{d['protect_title']}</div>
      <div style="display:flex;flex-direction:column;gap:5px;">
        {protect_items}
      </div>
    </div>"""

    # Never zone — 4-row prohibition table
    never_rows = ""
    for action, reason in d["never_rows"]:
        never_rows += f"""
          <tr><td style="font-weight:600;color:var(--coral);">{action}</td><td class="muted">{reason}</td></tr>"""

    never_zone = f"""
    <div class="glass" style="padding:10px 14px;">
      <div class="section-title" style="color:var(--coral);">{d['never_title']}</div>
      <table class="flow-table">
        <thead><tr><th style="color:var(--coral);">&#10007; {"Acción" if is_es else "Action"}</th><th style="color:var(--coral);">{"Por Qué" if is_es else "Why"}</th></tr></thead>
        <tbody>{never_rows}
        </tbody>
      </table>
    </div>"""

    # Exposed zone — 5 response items + symptoms
    exposed_items = ""
    for i, step in enumerate(d["exposed_steps"], 1):
        exposed_items += f"""
        <div style="display:flex;gap:8px;align-items:flex-start;">
          <div style="flex-shrink:0;width:22px;height:22px;border-radius:50%;background:rgba(232,160,32,.12);border:1px solid rgba(232,160,32,.3);display:flex;align-items:center;justify-content:center;font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:11px;color:var(--amber);">{i}</div>
          <div style="font-family:'Inter',sans-serif;font-size:11px;color:var(--text);line-height:1.4;">{step}</div>
        </div>"""

    symptoms_label = "Síntomas:" if is_es else "Symptoms:"
    exposed_zone = f"""
    <div class="glass" style="padding:10px 14px;">
      <div class="section-title" style="color:var(--amber);">{d['exposed_title']}</div>
      <div style="display:flex;flex-direction:column;gap:4px;margin-bottom:6px;">
        {exposed_items}
      </div>
      <div style="padding:6px 10px;border-radius:8px;background:rgba(224,92,92,.06);border:1px solid rgba(224,92,92,.18);font-family:'Inter',sans-serif;font-size:10.5px;color:var(--muted);line-height:1.4;"><strong style="color:var(--coral);">{symptoms_label}</strong> {d['symptoms']}</div>
    </div>"""

    # Footer
    if is_es:
        footer_disclaimer = "Solo referencia para el operador. Siga los POE de su instalación. Reporte cualquier desviación a su supervisor."
        footer_title = f"{d['subhead']} &mdash; Serie de Seguridad en el Recubrimiento"
        footer_brand = f"Plating Posters Inc &middot; Referencia de Piso de Producción &middot; PP-{code}-SF / v1.0 / Jun 2026"
    else:
        footer_disclaimer = "Operator reference only. Follow your facility SOPs. Report any process deviations to your supervisor."
        footer_title = f"{d['subhead']} &mdash; Plating Safety Series"
        footer_brand = f"Plating Posters Inc &middot; Shop Floor Reference &middot; PP-{code}-SF / v1.0 / Jun 2026"

    # Topic name for file title
    topic_name = d['subhead']

    return f"""<!DOCTYPE html>
<html lang="{'es' if is_es else 'en'}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{topic_name} &mdash; Safety Series &mdash; Shop Floor | Plating Posters Inc</title>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@800;900&family=Barlow:wght@600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
:root{{--bg:#1A1F2E;--navy:#0D1020;--text:#F0EDE8;--muted:rgba(240,237,232,.62);--faint:rgba(240,237,232,.38);--amber:#E8A020;--teal:#2EC4B6;--emerald:#27AE60;--coral:#E05C5C;--slate:#3A4055;--glass-bg:rgba(30,36,53,.55);--glass-border:rgba(255,255,255,.12);--glass-shadow:inset 0 1px 0 rgba(255,255,255,.14),inset 0 -1px 0 rgba(0,0,0,.2),0 4px 12px rgba(0,0,0,.25);--tack:24px;}}
body[data-edition="light"]{{--bg:#F5F4F0;--navy:#DDD8CE;--text:#1B2030;--muted:rgba(27,32,48,.78);--amber:#8C5A00;--teal:#0F6B62;--emerald:#15693B;--coral:#9B2825;--faint:rgba(27,32,48,.42);--slate:#C5C0B5;--glass-bg:rgba(255,253,247,.82);--glass-border:rgba(27,32,48,.18);--glass-shadow:inset 0 1px 0 rgba(255,255,255,.6),0 4px 12px rgba(27,32,48,.08);}}
body[data-edition="light"] .logo-url{{color:rgba(27,32,48,.62);}}body[data-edition="light"] .logo-word .a{{color:#1B2030;}}
html,body{{margin:0;padding:0;background:#0a0c14;}}.stage{{width:100vw;height:100vh;display:flex;align-items:center;justify-content:center;overflow:hidden;}}.poster-wrap{{transform-origin:center center;}}.poster{{width:900px;height:1200px;position:relative;overflow:hidden;background:radial-gradient(700px 500px at 10% 8%,rgba(224,92,92,.15),transparent 60%),radial-gradient(600px 450px at 92% 20%,rgba(232,160,32,.13),transparent 55%),radial-gradient(550px 500px at 50% 88%,rgba(224,92,92,.10),transparent 60%),var(--bg);font-family:'Inter',sans-serif;color:var(--text);display:flex;flex-direction:column;padding:var(--tack);box-sizing:border-box;}}.poster::before{{content:'';position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.025) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.025) 1px,transparent 1px);background-size:50px 50px;mask-image:radial-gradient(ellipse 80% 80% at 50% 50%,black 40%,transparent 100%);-webkit-mask-image:radial-gradient(ellipse 80% 80% at 50% 50%,black 40%,transparent 100%);pointer-events:none;z-index:0;}}.poster>*{{position:relative;z-index:1;}}
.glass{{background-color:var(--glass-bg);background-image:linear-gradient(145deg,rgba(255,255,255,.055),rgba(255,255,255,.015));border:1px solid var(--glass-border);backdrop-filter:blur(18px) saturate(140%);-webkit-backdrop-filter:blur(18px) saturate(140%);box-shadow:var(--glass-shadow);border-radius:12px;}}
.tack{{position:absolute;width:18px;height:18px;border-radius:50%;border:1.5px solid rgba(224,92,92,.28);z-index:2;pointer-events:none;}}.tack::before,.tack::after{{content:"";position:absolute;background:rgba(224,92,92,.28);}}.tack::before{{left:50%;top:-2px;bottom:-2px;width:1px;transform:translateX(-50%);}}.tack::after{{top:50%;left:-2px;right:-2px;height:1px;transform:translateY(-50%);}}.tack.tl{{top:6px;left:6px;}}.tack.tr{{top:6px;right:6px;}}.tack.bl{{bottom:6px;left:6px;}}.tack.br{{bottom:6px;right:6px;}}
.poster-header{{flex-shrink:0;}}.poster-body{{flex:1;overflow:hidden;display:flex;flex-direction:column;gap:8px;justify-content:space-between;}}.poster-footer{{flex-shrink:0;margin-top:6px;}}
.header-row{{display:flex;align-items:flex-start;justify-content:space-between;gap:14px;margin-bottom:6px;}}.header-left{{flex:1;min-width:0;}}.eyebrow{{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--coral);letter-spacing:.12em;text-transform:uppercase;margin-bottom:4px;}}.headline{{font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:52px;color:var(--text);line-height:.92;letter-spacing:-.01em;margin-bottom:4px;}}.headline em{{font-style:normal;color:var(--coral);}}.subhead{{font-family:'Barlow',sans-serif;font-weight:700;font-size:17px;color:var(--coral);margin-bottom:4px;}}.tagline{{font-family:'Inter',sans-serif;font-weight:500;font-size:11px;color:var(--muted);line-height:1.3;max-width:520px;}}
.logo-card{{flex-shrink:0;display:flex;flex-direction:column;align-items:center;gap:6px;padding:10px 12px;min-width:140px;background-color:var(--glass-bg);background-image:linear-gradient(145deg,rgba(255,255,255,.055),rgba(255,255,255,.015));border:1px solid var(--glass-border);border-radius:12px;backdrop-filter:blur(18px) saturate(140%);-webkit-backdrop-filter:blur(18px) saturate(140%);box-shadow:inset 0 1px 0 rgba(255,255,255,.14),0 4px 12px rgba(0,0,0,.25);}}.logo-mark{{width:60px;height:60px;border-radius:11px;background:linear-gradient(135deg,#E05C5C,#E8A020);display:flex;align-items:center;justify-content:center;box-shadow:inset 0 1px 0 rgba(255,255,255,.4),inset 0 -2px 4px rgba(0,0,0,.15),0 4px 14px rgba(0,0,0,.35);}}.logo-mark span{{font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:22px;color:#1A1F2E;letter-spacing:.02em;line-height:1;}}.logo-word{{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:16px;letter-spacing:.04em;text-transform:uppercase;line-height:1;text-align:center;white-space:nowrap;}}.logo-word .a{{color:#F0EDE8;}}.logo-word .b{{color:#E05C5C;}}.logo-url{{font-family:'JetBrains Mono',monospace;font-size:8px;letter-spacing:.06em;color:rgba(240,237,232,.45);margin-top:-1px;}}
.section-title{{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:15px;letter-spacing:.07em;text-transform:uppercase;margin-bottom:5px;}}
.flow-table{{width:100%;border-collapse:collapse;}}.flow-table th{{font-family:'Barlow',sans-serif;font-weight:700;font-size:10px;letter-spacing:.06em;text-transform:uppercase;padding:4px 8px;text-align:left;border-bottom:1px solid var(--glass-border);}}.flow-table td{{font-family:'Inter',sans-serif;font-weight:500;font-size:11px;color:var(--text);padding:4px 8px;border-bottom:1px solid rgba(255,255,255,.05);line-height:1.3;}}.flow-table td.muted{{color:var(--muted);}}.flow-table tr:nth-child(even) td{{background:rgba(255,255,255,.02);}}body[data-edition="light"] .flow-table tr:nth-child(even) td{{background:rgba(27,32,48,.025);}}
.footer-panel{{padding:8px 18px;text-align:center;border-radius:10px;}}.footer-disclaimer{{font-family:'Inter',sans-serif;font-weight:400;font-size:9px;color:var(--muted);line-height:1.4;margin-bottom:3px;}}.footer-title{{font-family:'Barlow',sans-serif;font-weight:600;font-size:11px;color:var(--text);margin-bottom:2px;}}.footer-brand{{font-family:'JetBrains Mono',monospace;font-size:8.5px;color:var(--muted);}}
@media print{{@page{{size:9.375in 12.5in;margin:0;}}html,body{{background:#1A1F2E !important;-webkit-print-color-adjust:exact !important;print-color-adjust:exact !important;}}*{{-webkit-print-color-adjust:exact !important;print-color-adjust:exact !important;}}.stage{{position:static;display:block;overflow:visible;}}.poster-wrap{{transform:none !important;width:auto !important;height:auto !important;}}.poster{{box-shadow:none !important;width:900px !important;height:1200px !important;overflow:hidden !important;}}.glass{{backdrop-filter:none !important;-webkit-backdrop-filter:none !important;}}.tweaks{{display:none !important;}}}}
</style>
</head>
<body{body_attr}>
<div class="stage">
<div class="poster-wrap" id="posterWrap">
<div class="poster" id="poster">
  <span class="tack tl"></span><span class="tack tr"></span><span class="tack bl"></span><span class="tack br"></span>

  <div class="poster-header">
    <div class="header-row">
      <div class="header-left">
        <div class="eyebrow">{eyebrow}</div>
        <div class="headline">{d['headline']}</div>
        <div class="subhead">{d['subhead']}</div>
        <div class="tagline">{d['tagline']}</div>
      </div>
      <div class="logo-card">
        <div class="logo-mark"><span>PP</span></div>
        <div class="logo-word"><span class="a">Plating</span> <span class="b">Posters</span></div>
        <div class="logo-url">www.platingposters.com</div>
      </div>
    </div>
  </div>

  <div class="poster-body">
    {hazard_banner}
    {danger_zone}
    {protect_zone}
    {never_zone}
    {exposed_zone}
  </div>

  <div class="glass footer-panel poster-footer">
    <div class="footer-disclaimer">{footer_disclaimer}</div>
    <div class="footer-title">{footer_title}</div>
    <div class="footer-brand">{footer_brand}</div>
  </div>

</div>
</div>
</div>
<div class="tweaks" style="position:fixed;bottom:16px;right:16px;z-index:100;background:rgba(13,16,32,.92);border:1px solid rgba(255,255,255,.12);border-radius:10px;padding:12px 16px;display:flex;flex-direction:column;gap:8px;font-family:'Inter',sans-serif;font-size:12px;color:#F0EDE8;">
  <div style="display:flex;gap:8px;align-items:center;"><span style="color:rgba(240,237,232,.5);">Edition</span><button id="btnDark" onclick="setEdition('')" style="padding:3px 10px;border-radius:4px;border:1px solid #E05C5C;background:{'transparent' if is_light else '#E05C5C'};color:{'#F0EDE8' if is_light else '#1A1F2E'};cursor:pointer;font-size:11px;">Dark</button><button id="btnLight" onclick="setEdition('light')" style="padding:3px 10px;border-radius:4px;border:1px solid {'#E05C5C' if is_light else 'rgba(255,255,255,.2)'};background:{'#E05C5C' if is_light else 'transparent'};color:{'#1A1F2E' if is_light else '#F0EDE8'};cursor:pointer;font-size:11px;">Light</button></div>
  <button onclick="window.print()" style="padding:4px 12px;border-radius:4px;border:1px solid rgba(255,255,255,.2);background:transparent;color:#F0EDE8;cursor:pointer;font-size:11px;">Print / PDF</button>
</div>
<script>
const posterWrap=document.getElementById('posterWrap');const poster=document.getElementById('poster');function scalePoster(){{const s=Math.min((window.innerWidth-24)/900,(window.innerHeight-24)/1200);posterWrap.style.transform='scale('+s+')';posterWrap.style.transformOrigin='top center';posterWrap.style.width='900px';posterWrap.style.height=(1200*s)+'px';}}function setEdition(e){{if(e)document.body.dataset.edition=e;else delete document.body.dataset.edition;document.getElementById('btnDark').style.background=e?'transparent':'#E05C5C';document.getElementById('btnDark').style.color=e?'#F0EDE8':'#1A1F2E';document.getElementById('btnDark').style.borderColor=e?'rgba(255,255,255,.2)':'#E05C5C';document.getElementById('btnLight').style.background=e?'#E05C5C':'transparent';document.getElementById('btnLight').style.color=e?'#1A1F2E':'#F0EDE8';document.getElementById('btnLight').style.borderColor=e?'#E05C5C':'rgba(255,255,255,.2)';}}scalePoster();window.addEventListener('resize',scalePoster);
</script>
</body>
</html>"""


# ─── TOPIC NAME MAP (for filenames) ──────────────────────────────────────────
TOPIC_NAMES = {
    "01": "Cyanide Safety - Never Add Acid",
    "02": "Hexavalent Chromium - Protect Your Lungs",
    "03": "Acid Tank Burns - Skin and Eye Protection",
    "04": "Emergency Eyewash and Shower - Act in Seconds",
    "05": "Cyanide Waste - Segregation and Disposal",
    "06": "Cadmium Plating - Zero Tolerance Exposure",
    "07": "Nickel Dermatitis - Skin Protection",
    "08": "Alkaline Cleaner Burns",
    "09": "Nitric Acid and NOx - The Invisible Danger",
    "10": "Hydrogen Embrittlement Baking - Oven Safety",
    "11": "Anodize Line - Sulfuric Acid and Electrical Hazards",
    "12": "Electropolishing - Concentrated Acid Mixtures",
    "13": "Chemical Mixing - Order of Addition Matters",
    "14": "Confined Space - Tank Entry and Cleaning",
    "15": "Electrical Safety - Rectifiers and Bus Bars",
    "16": "Ventilation Failure - What to Do When the Air Stops",
    "17": "Spill Response - Know Your Chemical Know Your Kit",
    "18": "Compressed Gas - Nitrogen Air and Hydrogen Safety",
}


# ─── GENERATE ALL 72 FILES ───────────────────────────────────────────────────
if __name__ == "__main__":
    count = 0
    for topic in TOPICS:
        num = topic["num"]
        name = TOPIC_NAMES[num]
        for lang in ("en", "es"):
            for edition in ("dark", "light"):
                lang_label = "EN" if lang == "en" else "ES"
                ed_label = "Dark" if edition == "dark" else "Light"
                filename = f"Safety - {num} - SHOP FLOOR - {name} - {lang_label} - {ed_label}.html"
                filepath = os.path.join(OUT_DIR, filename)
                content = build_html(topic, lang, edition)
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content)
                count += 1
                print(f"  [{count:>2}/72] {filename}")

    print(f"\nDone! {count} safety posters generated in:\n  {OUT_DIR}")
