import re

def process_file(filepath, is_en=False):
    prefix = "../" if is_en else ""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Google Fonts in <head> to load Lora serif font
    content = content.replace(
        'family=Montserrat:wght@400;600;700;800;900&family=Lato:wght@300;400;700&display=swap',
        'family=Montserrat:wght@400;600;700;800;900&family=Lato:wght@300;400;700&family=Lora:ital,wght@0,400;0,600;1,400&display=swap'
    )

    # 2. Update CSS in <style> block: add Lora custom transition and modal anims
    css_anims = '''    /* Delayed fade-in for tagline */
    @keyframes fadeInDelayed {
      0% { opacity: 0; transform: translateY(12px); filter: blur(4px); }
      100% { opacity: 1; transform: translateY(0); filter: blur(0); }
    }
    .animate-fade-in-delayed {
      animation: fadeInDelayed 1.2s cubic-bezier(0.25, 1, 0.5, 1) 1.2s both;
    }

    /* Modal Animation */
    .modal-active {
      opacity: 1 !important;
      pointer-events: auto !important;
    }
    .modal-active .modal-container {
      transform: scale(1) !important;
    }'''
    
    content = content.replace(
        '    .animate-tracking-expand {',
        css_anims + '\n\n    .animate-tracking-expand {'
    )

    # 3. Update Hero Watermark Logo (move to Left, make static, smaller and higher quality)
    old_watermark = f'''    <!-- Large Logo Watermark on the side -->
    <div class="absolute right-[-80px] lg:right-[5%] top-1/2 -translate-y-1/2 w-[350px] lg:w-[450px] opacity-[0.035] hidden md:block pointer-events-none z-0 select-none animate-pulse" style="animation-duration: 6s;">
      <img src="{prefix}assets/images/logo.png" alt="Sartori Logo Watermark" class="w-full h-auto">
    </div>'''
    
    new_watermark = f'''    <!-- Large Logo Watermark on the Left (Sober & Static) -->
    <div class="absolute left-[3%] lg:left-[5%] top-[18%] w-[160px] lg:w-[200px] opacity-[0.06] hidden md:block pointer-events-none z-0 select-none">
      <img src="{prefix}assets/images/logo.png" alt="Sartori Logo Watermark" class="w-full h-auto filter brightness-125 contrast-125">
    </div>'''
    
    content = content.replace(old_watermark, new_watermark)

    # 4. H1 size reduction to keep on 1 line and Tagline typography change (Lora, elegant mixed-case)
    old_h1_block = f'''        <!-- H1 -->
        <h1 class="font-heading font-black text-6xl sm:text-7xl lg:text-8xl text-white tracking-tighter animate-tracking-expand" style="text-shadow: 0 10px 30px rgba(0,7,45,0.75);">
          SARTORI <span class="text-sartori-amber filter drop-shadow-[0_0_20px_rgba(245,158,11,0.4)]">Energy</span>
        </h1>

        <!-- Tagline -->
        <p class="mt-5 font-heading font-extrabold text-base md:text-lg text-sartori-teal tracking-[0.25em] uppercase animate-fade-up delay-300" style="text-shadow: 0 2px 10px rgba(0,7,45,0.6);">
          Your energy project, <span class="text-sartori-amber">our mission</span>
        </p>'''

    new_h1_block = f'''        <!-- H1 -->
        <h1 class="font-heading font-black text-4xl sm:text-5xl md:text-6xl lg:text-6xl xl:text-7xl text-white tracking-tighter animate-tracking-expand whitespace-nowrap" style="text-shadow: 0 10px 30px rgba(0,7,45,0.85);">
          SARTORI <span class="text-sartori-amber filter drop-shadow-[0_0_20px_rgba(245,158,11,0.4)]">Energy</span>
        </h1>

        <!-- Tagline -->
        <p class="mt-5 font-serif italic text-lg md:text-xl lg:text-2xl text-sartori-teal-light tracking-wide animate-fade-in-delayed" style="text-shadow: 0 2px 10px rgba(0,7,45,0.6);">
          "Your energy project, <span class="text-sartori-amber font-semibold">our mission</span>"
        </p>'''

    content = content.replace(old_h1_block, new_h1_block)

    # 5. Quote section text: add data-animate for entrance movement
    old_quote_p = '<p class="font-heading font-bold text-2xl md:text-3xl lg:text-4xl text-white leading-tight italic">'
    new_quote_p = '<p data-animate class="font-heading font-bold text-2xl md:text-3xl lg:text-4xl text-white leading-tight italic delay-100">'
    content = content.replace(old_quote_p, new_quote_p)

    # 6. Service cards: add click cursor pointer classes and data-service-id
    # We will modify the service-card divs to contain data-service-id="X"
    for i in range(1, 7):
        content = content.replace(
            f'<!-- Card {i}: ',
            f'<!-- Card {i}: '
        )
    
    # We replace:
    # class="service-card bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl group transition-all duration-300 flex flex-col h-full"
    # with:
    # class="service-card cursor-pointer bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 hover:scale-[1.02] active:scale-[0.98] group transition-all duration-300 flex flex-col h-full"
    
    content = content.replace(
        'class="service-card bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl group transition-all duration-300 flex flex-col h-full"',
        'class="service-card cursor-pointer bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 hover:scale-[1.02] active:scale-[0.98] group transition-all duration-300 flex flex-col h-full"'
    )
    content = content.replace(
        'class="service-card bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl group transition-all duration-300 flex flex-col h-full delay-100"',
        'class="service-card cursor-pointer bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 hover:scale-[1.02] active:scale-[0.98] group transition-all duration-300 flex flex-col h-full delay-100"'
    )
    content = content.replace(
        'class="service-card bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl group transition-all duration-300 flex flex-col h-full delay-200"',
        'class="service-card cursor-pointer bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 hover:scale-[1.02] active:scale-[0.98] group transition-all duration-300 flex flex-col h-full delay-200"'
    )
    content = content.replace(
        'class="service-card bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl group transition-all duration-300 flex flex-col h-full delay-300"',
        'class="service-card cursor-pointer bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 hover:scale-[1.02] active:scale-[0.98] group transition-all duration-300 flex flex-col h-full delay-300"'
    )
    content = content.replace(
        'class="service-card bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl group transition-all duration-300 flex flex-col h-full delay-400"',
        'class="service-card cursor-pointer bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 hover:scale-[1.02] active:scale-[0.98] group transition-all duration-300 flex flex-col h-full delay-400"'
    )
    content = content.replace(
        'class="service-card bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl group transition-all duration-300 flex flex-col h-full delay-500"',
        'class="service-card cursor-pointer bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 hover:scale-[1.02] active:scale-[0.98] group transition-all duration-300 flex flex-col h-full delay-500"'
    )

    # Let's add data-service-id to the 6 card comments in HTML
    # We will do it by target matching the Card header comment and div.
    # Spanish:
    es_cards = [
        ('<!-- Card 1: Montaje e Instalación -->\n        <div data-animate class="service-card', '<!-- Card 1: Montaje e Instalación -->\n        <div data-animate data-service-id="1" class="service-card'),
        ('<!-- Card 2: Auditorías Técnicas -->\n        <div data-animate class="service-card', '<!-- Card 2: Auditorías Técnicas -->\n        <div data-animate data-service-id="2" class="service-card'),
        ('<!-- Card 3: Puesta en Servicio -->\n        <div data-animate class="service-card', '<!-- Card 3: Puesta en Servicio -->\n        <div data-animate data-service-id="3" class="service-card'),
        ('<!-- Card 4: Protección y Control -->\n        <div data-animate class="service-card', '<!-- Card 4: Protección y Control -->\n        <div data-animate data-service-id="4" class="service-card'),
        ('<!-- Card 5: Pruebas y Verificación -->\n        <div data-animate class="service-card', '<!-- Card 5: Pruebas y Verificación -->\n        <div data-animate data-service-id="5" class="service-card'),
        ('<!-- Card 6: Sincronización y Control -->\n        <div data-animate class="service-card', '<!-- Card 6: Sincronización y Control -->\n        <div data-animate data-service-id="6" class="service-card')
    ]
    
    # English:
    en_cards = [
        ('<!-- Card 1: Montaje e Instalación -->\n        <div data-animate class="service-card', '<!-- Card 1: Montaje e Instalación -->\n        <div data-animate data-service-id="1" class="service-card'),
        ('<!-- Card 2: Auditorías Técnicas -->\n        <div data-animate class="service-card', '<!-- Card 2: Auditorías Técnicas -->\n        <div data-animate data-service-id="2" class="service-card'),
        ('<!-- Card 3: Puesta en Servicio -->\n        <div data-animate class="service-card', '<!-- Card 3: Puesta en Servicio -->\n        <div data-animate data-service-id="3" class="service-card'),
        ('<!-- Card 4: Protección y Control -->\n        <div data-animate class="service-card', '<!-- Card 4: Protección y Control -->\n        <div data-animate data-service-id="4" class="service-card'),
        ('<!-- Card 5: Pruebas y Verificación -->\n        <div data-animate class="service-card', '<!-- Card 5: Pruebas y Verificación -->\n        <div data-animate data-service-id="5" class="service-card'),
        ('<!-- Card 6: Sincronización y Control -->\n        <div data-animate class="service-card', '<!-- Card 6: Sincronización y Control -->\n        <div data-animate data-service-id="6" class="service-card')
    ]

    cards_to_replace = en_cards if is_en else es_cards
    for old_tag, new_tag in cards_to_replace:
        content = content.replace(old_tag, new_tag)

    # 7. Append Modal HTML block right before </body>
    modal_html = f'''  <!-- Service Detail Modal (Zoom-in expand effect) -->
  <div id="service-modal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-sartori-navy-deep/85 backdrop-blur-md hidden opacity-0 transition-opacity duration-300 pointer-events-none">
    <!-- Modal Container -->
    <div class="modal-container relative bg-white rounded-2xl max-w-2xl w-full overflow-hidden shadow-2xl transform scale-95 transition-transform duration-300 flex flex-col max-h-[90vh]">
      <!-- Close Button -->
      <button id="modal-close-btn" class="absolute top-4 right-4 z-10 w-10 h-10 flex items-center justify-center rounded-full bg-sartori-navy-deep/60 hover:bg-sartori-navy-deep text-white transition-colors" aria-label="Cerrar modal">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M6 18L18 6M6 6l12 12" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </button>
      
      <!-- Modal Header Image -->
      <div class="relative h-60 sm:h-72 overflow-hidden flex-shrink-0">
        <img id="modal-img" src="" alt="Service Image" class="w-full h-full object-cover">
        <div class="absolute inset-0 bg-gradient-to-t from-sartori-navy-deep/80 via-transparent to-transparent"></div>
        <div class="absolute bottom-6 left-6 right-6">
          <span id="modal-badge" class="inline-block px-3 py-1 bg-sartori-amber text-sartori-navy-deep font-heading font-extrabold text-xs uppercase tracking-wider rounded-md mb-2">{"Sartori Capabilities" if is_en else "Sartori Especialidad"}</span>
          <h2 id="modal-title" class="font-heading font-black text-2xl sm:text-3xl text-white tracking-tight leading-tight"></h2>
        </div>
      </div>
      
      <!-- Modal Content Body -->
      <div id="modal-body" class="p-6 sm:p-8 overflow-y-auto font-body text-gray-600 text-base leading-relaxed space-y-4">
        <!-- filled dynamically by JS -->
      </div>
      
      <!-- Modal Footer -->
      <div class="p-6 bg-slate-50 border-t border-slate-100 flex justify-end flex-shrink-0">
        <button id="modal-action-btn" class="bg-sartori-navy-deep hover:bg-sartori-navy text-white font-heading font-bold text-sm px-6 py-2.5 rounded transition-all shadow-md">
          {"Close & Go Back" if is_en else "Volver a Servicios"}
        </button>
      </div>
    </div>
  </div>

</body>'''
    
    content = content.replace('</body>', modal_html)

    # 8. Append JavaScript controller for Modal at the bottom inside last <script> tag
    js_modal_controller = f'''    // ---- Service Modal Controller ----
    const servicesData = {{
      '1': {{
        title: '{"GIS and AIS Assembly and Installation" if is_en else "Montaje e Instalación de GIS y AIS"}',
        image: '{prefix}assets/images/01 - USAR - PARA SERVICIOS.jpg',
        desc: '{"We provide comprehensive services in power transmission and distribution networks as well as in various types of industries. Specialists trained by sector manufacturers in medium, high, and extra-high voltage technologies across various models." if is_en else "Proveemos servicios integrales en redes de transporte y distribución de energía como así también en distintos tipos de industrias. Especialistas con capacitaciones impartidas por fabricantes del sector en tecnologías de media, alta y extra alta tensión en distintos modelos."}',
        details: [
          '{"Assembly of GIS switchgear up to 500 kV" if is_en else "Montaje de celdas y bahías GIS hasta 500 kV"}',
          '{"Power and control cable routing and termination" if is_en else "Tendido y conexionado de cables de potencia y control"}',
          '{"SF6 gas handling, evacuation, and injection under strict environmental control" if is_en else "Tratamiento, recuperación e inyección de gas SF6 bajo estricto control ambiental"}',
          '{"Leak testing and gas quality verification (humidity, purity)" if is_en else "Ensayos de estanqueidad y calidad del gas (humedad, pureza)"}'
        ]
      }},
      '2': {{
        title: '{"Technical Audits and Asset Assessments" if is_en else "Auditorías Técnicas y Evaluación de Activos"}',
        image: '{prefix}assets/images/03 - USAR PARA SERVICIOS.jpg',
        desc: '{"Detailed diagnostics, risk analyses, performance comparisons, and strategic recommendations to improve reliability, safety, and operational efficiency of hydroelectric facilities and substations, in full compliance with IEC, IEEE, and ANSI standards." if is_en else "Diagnósticos detallados, análisis de riesgos, comparativas de rendimiento y recomendaciones estratégicas para mejorar la fiabilidad, la seguridad y la eficiencia operativa de instalaciones hidroeléctricas y subestaciones, en plena conformidad con las normas IEC, IEEE y ANSI."}',
        details: [
          '{"Predictive diagnostics via thermography and partial discharges" if is_en else "Diagnósticos predictivos mediante termografía y descargas parciales"}',
          '{"Regulatory compliance reviews (IEC, IEEE, ANSI)" if is_en else "Análisis de cumplimiento normativo (IEC, IEEE, ANSI)"}',
          '{"Operational risk and reliability assessments" if is_en else "Evaluaciones de riesgo operativo y confiabilidad"}',
          '{"Modernization plans and maintenance optimization (RCM)" if is_en else "Planes de modernización y optimización de mantenimiento (RCM)"}'
        ]
      }},
      '3': {{
        title: '{"Commissioning and Energization" if is_en else "Puesta en Servicio y Energización"}',
        image: '{prefix}assets/images/04 - USAR PARA SERVICIOS.jpg',
        desc: '{"Comprehensive commissioning, testing, and grid connection services for substations up to 500 kV, including AC and DC GIS systems for metro and railway applications." if is_en else "Servicios integrales de puesta en servicio, pruebas y conexión a red para subestaciones de hasta 500 kV, incluyendo sistemas GIS de corriente alterna (CA) y corriente continua (CC) destinados a aplicaciones de metro y ferrocarril."}',
        details: [
          '{"Functional testing of electrical and mechanical interlocking schemes" if is_en else "Pruebas funcionales de enclavamientos mecánicos y eléctricos"}',
          '{"Controlled and monitored energization of power transformers and reactors" if is_en else "Energización controlada y monitoreada de transformadores y reactores"}',
          '{"Primary and secondary current/voltage injection testing" if is_en else "Pruebas de inyección secundaria y primaria"}',
          '{"End-to-End (E2E) testing on transmission lines" if is_en else "Pruebas de extremo a extremo (End-to-End) en enlaces de transmisión"}'
        ]
      }},
      '4': {{
        title: '{"Protection and Control Systems" if is_en else "Sistemas de Protección y Control"}',
        image: '{prefix}assets/images/06 - USAR PARA SERVICIOS.jpg',
        desc: '{"Installation, configuration, testing, and parameterization of protection and control systems. We ensure optimal relay coordination, system selectivity, fault management, and grid reliability." if is_en else "Instalación, configuración, pruebas y parametrización de sistemas de protección y control. Garantizamos una coordinación óptima de los relés, selectividad del sistema, gestión de fallos y la fiabilidad de la red."}',
        details: [
          '{"Parameterization and testing of multifunction protection relays (SEL, ABB, Siemens, GE)" if is_en else "Configuración y parametrización de relés de protección (SEL, ABB, Siemens, GE)"}',
          '{"Teleprotection and Direct Transfer Trip (DTT) scheme testing" if is_en else "Pruebas de esquemas de teleprotección y disparo directo (DTT)"}',
          '{"Substation automation and protocol integration (IEC 61850, DNP3, Modbus)" if is_en else "Integración de protocolos de automatización (IEC 61850, DNP3, Modbus)"}',
          '{"Protection relay coordination studies" if is_en else "Estudios de coordinación de protecciones y selectividad"}'
        ]
      }},
      '5': {{
        title: '{"Testing and Verification" if is_en else "Pruebas y Verificación"}',
        image: '{prefix}assets/images/07 - USAR PARA SERVICIOS.jpg',
        desc: '{"Field testing to verify the dielectric and functional integrity of all primary and secondary electrical assets within the high-voltage substation." if is_en else "Servicios integrales de pruebas de campo para verificar la integridad dieléctrica y funcional de todos los equipos primarios y secundarios de la subestación."}',
        details: [
          '{"High voltage dielectric testing (AC Resonance test systems)" if is_en else "Pruebas dieléctricas en alta tensión (Resonancia de CA)"}',
          '{"Insulation resistance (Megger) and power factor/tan-delta (Doble) testing" if is_en else "Resistencia de aislamiento (Megger) y factor de potencia (Doble)"}',
          '{"CT and VT ratio, polarity, and excitation curve testing" if is_en else "Pruebas de relación, polaridad y curva de saturación en TCs/TTs"}',
          '{"Contact resistance (Ducter) and circuit breaker timing tests" if is_en else "Resistencia de contactos e intervalos de tiempo en interruptores"}'
        ]
      }},
      '6': {{
        title: '{"Synchronization and Control Systems" if is_en else "Sistemas de Sincronización y Control"}',
        image: '{prefix}assets/images/09 - USAR PARA SERVICIOS.jpg',
        desc: '{"Advanced platforms for automatic circuit breaker synchronization using proven methodologies to optimize system stability, maximize asset availability, and ensure safe infrastructure operation." if is_en else "Plataformas avanzadas de sincronización automática de interruptores mediante metodologías probadas para optimizar la estabilidad del sistema, maximizar la disponibilidad de los activos y garantizar una operación segura de la infraestructura."}',
        details: [
          '{"Advanced algorithms for adaptive synchronization control" if is_en else "Algoritmos avanzados de sincronización y control adaptativo"}',
          '{"Grid transient stability optimization during synchronization" if is_en else "Optimización de la estabilidad transitoria del sistema de potencia"}',
          '{"Sychrocheck relay calibration and dynamic testing" if is_en else "Calibración y pruebas de relés de sincronismo"}',
          '{"Stress reduction on generator and transformer windings" if is_en else "Reducción del estrés dinámico en bobinados de generadores y transformadores"}'
        ]
      }}
    }};

    const modal = document.getElementById('service-modal');
    const modalImg = document.getElementById('modal-img');
    const modalTitle = document.getElementById('modal-title');
    const modalBody = document.getElementById('modal-body');
    const modalCloseBtn = document.getElementById('modal-close-btn');
    const modalActionBtn = document.getElementById('modal-action-btn');

    document.querySelectorAll('.service-card').forEach(card => {{
      card.addEventListener('click', () => {{
        const serviceId = card.getAttribute('data-service-id');
        const data = servicesData[serviceId];
        if (!data) return;

        // Populate modal data
        modalImg.src = data.image;
        modalImg.alt = data.title;
        modalTitle.textContent = data.title;
        
        let bodyHtml = `<p class="text-gray-700 font-normal mb-6">${{data.desc}}</p>`;
        bodyHtml += `<h4 class="font-heading font-bold text-sartori-navy-deep text-sm tracking-wide mb-3 uppercase">{"Key Engineering Deliverables" if is_en else "Alcance de Ingeniería de Campo"}</h4>`;
        bodyHtml += `<ul class="space-y-2.5">`;
        data.details.forEach(item => {{
          bodyHtml += `
            <li class="flex items-start gap-2.5 text-sm text-gray-600">
              <span class="text-sartori-teal font-bold mt-0.5">•</span>
              <span>${{item}}</span>
            </li>`;
        }});
        bodyHtml += `</ul>`;
        modalBody.innerHTML = bodyHtml;

        // Show modal with animations
        modal.classList.remove('hidden');
        // trigger reflow
        modal.offsetWidth;
        modal.classList.add('modal-active');
        document.body.style.overflow = 'hidden';
      }});
    }});

    function closeModal() {{
      modal.classList.remove('modal-active');
      setTimeout(() => {{
        modal.classList.add('hidden');
        document.body.style.overflow = '';
      }}, 300);
    }}

    modalCloseBtn.addEventListener('click', closeModal);
    modalActionBtn.addEventListener('click', closeModal);
    modal.addEventListener('click', (e) => {{
      if (e.target === modal) closeModal();
    }});'''

    # Insert inside the last script tag at the bottom before </script>
    content = content.replace(
        '// ---- Smooth Scroll for anchor links ----',
        js_modal_controller + '\n\n    // ---- Smooth Scroll for anchor links ----'
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

process_file('index.html', is_en=False)
process_file('en/index.html', is_en=True)
print("SARTORI Energy single-line width, Lora fonts, delayed taglines, static watermarks and interactive detail modals integrated!")
