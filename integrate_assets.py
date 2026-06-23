import sys

def process_file(filepath, is_en=False):
    prefix = "../" if is_en else ""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 1. HERO VIDEO BACKGROUND
    # Let's locate the Hero section starting tag and replace the background block.
    # Spanish:
    #   <section id="inicio" class="relative min-h-screen flex items-center overflow-hidden">
    #     <!-- Animated Gradient Background -->
    #     <div class="absolute inset-0 hero-bg"></div>
    #     <!-- Grid Overlay -->
    #     <div class="absolute inset-0 grid-overlay"></div>
    #     <!-- Gradient overlay for depth -->
    #     <div class="absolute inset-0 bg-gradient-to-b from-transparent via-transparent to-sartori-navy-deep/50"></div>
    
    old_hero_bg = '''  <section id="inicio" class="relative min-h-screen flex items-center overflow-hidden">
    <!-- Animated Gradient Background -->
    <div class="absolute inset-0 hero-bg"></div>
    <!-- Grid Overlay -->
    <div class="absolute inset-0 grid-overlay"></div>
    <!-- Gradient overlay for depth -->
    <div class="absolute inset-0 bg-gradient-to-b from-transparent via-transparent to-sartori-navy-deep/50"></div>'''

    new_hero_bg = f'''  <section id="inicio" class="relative min-h-screen flex items-center overflow-hidden">
    <!-- Video Background -->
    <div class="absolute inset-0 z-0 bg-sartori-navy-deep">
      <video autoplay loop muted playsinline class="w-full h-full object-cover opacity-25">
        <source src="{prefix}assets/videos/VIDEO FAST MOTION FRONT WEB.mp4" type="video/mp4">
      </video>
      <div class="absolute inset-0 bg-gradient-to-r from-sartori-navy-deep via-sartori-navy-deep/75 to-transparent"></div>
    </div>
    <!-- Grid Overlay -->
    <div class="absolute inset-0 grid-overlay opacity-25 z-0"></div>'''

    content = content.replace(old_hero_bg, new_hero_bg)

    # 2. CTA BACKGROUND TEXTURE
    # Spanish CTA starts with:
    # <section class="bg-gradient-to-r from-sartori-navy-deep via-sartori-navy to-sartori-navy-deep py-16 lg:py-20">
    # We want to add an absolute positioned background image container.
    old_cta = '<section class="bg-gradient-to-r from-sartori-navy-deep via-sartori-navy to-sartori-navy-deep py-16 lg:py-20">'
    new_cta = f'''<section class="relative bg-gradient-to-r from-sartori-navy-deep via-sartori-navy to-sartori-navy-deep py-16 lg:py-20 overflow-hidden">
    <!-- Background Texture -->
    <div class="absolute inset-0 z-0 opacity-15">
      <img src="{prefix}assets/images/16 - USAR PARA FONDO GENERICO.jpg" alt="Background Texture" class="w-full h-full object-cover">
      <div class="absolute inset-0 bg-sartori-navy-deep/40"></div>
    </div>'''
    content = content.replace(old_cta, new_cta)

    # In the CTA content, we also need to ensure relative z-10 is on the text container.
    # Original: <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
    content = content.replace(
        '<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">',
        '<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">'
    )

    # 3. TEAM BACKGROUND TEXTURE
    # <section id="equipo" class="py-20 lg:py-28 bg-sartori-navy-deep relative overflow-hidden">
    # Add subtle background image
    old_team = '<section id="equipo" class="py-20 lg:py-28 bg-sartori-navy-deep relative overflow-hidden">'
    new_team = f'''<section id="equipo" class="py-20 lg:py-28 bg-sartori-navy-deep relative overflow-hidden">
    <!-- Subtle team background -->
    <div class="absolute inset-0 z-0 opacity-[0.03] pointer-events-none">
      <img src="{prefix}assets/images/09 - USAR PARA EQUIPOS-PERSONAL.jpg" alt="Sartori Team Background" class="w-full h-full object-cover">
    </div>'''
    content = content.replace(old_team, new_team)

    # Also make sure team contents have relative z-10
    content = content.replace(
        '<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative">',
        '<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">'
    )

    # 4. SERVICES CARDS IMAGE INTEGRATION
    # We will replace each card chunk directly.
    
    # --- CARD 1 ---
    es_card_1_old = '''        <!-- Card 1: Montaje e Instalación -->
        <div data-animate class="service-card bg-white rounded-xl p-8 shadow-sm hover:shadow-xl group">
          <div class="service-icon w-14 h-14 flex items-center justify-center rounded-xl bg-sartori-teal/10 text-sartori-teal mb-6">
            <svg class="w-7 h-7" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>
          </div>
          <h3 class="font-heading font-bold text-xl text-sartori-navy-deep mb-4">Montaje e Instalación de GIS y AIS</h3>
          <p class="font-body text-gray-500 leading-relaxed text-[0.938rem]">
            Proveemos servicios integrales en redes de transporte y distribución de energía como así también en distintos tipos de industrias. Especialistas con capacitaciones impartidas por fabricantes del sector en tecnologías de media, alta y extra alta tensión en distintos modelos.
          </p>
        </div>'''
        
    en_card_1_old = '''        <!-- Card 1: Montaje e Instalación -->
        <div data-animate class="service-card bg-white rounded-xl p-8 shadow-sm hover:shadow-xl group">
          <div class="service-icon w-14 h-14 flex items-center justify-center rounded-xl bg-sartori-teal/10 text-sartori-teal mb-6">
            <svg class="w-7 h-7" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>
          </div>
          <h3 class="font-heading font-bold text-xl text-sartori-navy-deep mb-4">GIS and AIS Assembly and Installation</h3>
          <p class="font-body text-gray-500 leading-relaxed text-[0.938rem]">
            We provide comprehensive services in power transmission and distribution networks as well as in various types of industries. Specialists trained by sector manufacturers in medium, high, and extra-high voltage technologies across various models.
          </p>
        </div>'''

    card_1_new = f'''        <!-- Card 1: Montaje e Instalación -->
        <div data-animate class="service-card bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl group transition-all duration-300 flex flex-col h-full">
          <div class="relative h-48 overflow-hidden">
            <img src="{prefix}assets/images/01 - USAR - PARA SERVICIOS.jpg" alt="GIS and AIS Assembly and Installation" class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700">
            <div class="absolute inset-0 bg-sartori-navy-deep/20 group-hover:bg-sartori-navy-deep/10 transition-colors"></div>
            <div class="absolute top-4 left-4 w-12 h-12 flex items-center justify-center rounded-xl bg-white/95 text-sartori-teal shadow-md">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>
            </div>
          </div>
          <div class="p-6 lg:p-8 flex-grow flex flex-col">
            <h3 class="font-heading font-bold text-xl text-sartori-navy-deep mb-4">{"GIS and AIS Assembly and Installation" if is_en else "Montaje e Instalación de GIS y AIS"}</h3>
            <p class="font-body text-gray-500 leading-relaxed text-[0.938rem] flex-grow">
              {"We provide comprehensive services in power transmission and distribution networks as well as in various types of industries. Specialists trained by sector manufacturers in medium, high, and extra-high voltage technologies across various models." if is_en else "Proveemos servicios integrales en redes de transporte y distribución de energía como así también en distintos tipos de industrias. Especialistas con capacitaciones impartidas por fabricantes del sector en tecnologías de media, alta y extra alta tensión en distintos modelos."}
            </p>
          </div>
        </div>'''

    # --- CARD 2 ---
    es_card_2_old = '''        <!-- Card 2: Auditorías Técnicas -->
        <div data-animate class="service-card bg-white rounded-xl p-8 shadow-sm hover:shadow-xl group delay-100">
          <div class="service-icon w-14 h-14 flex items-center justify-center rounded-xl bg-sartori-teal/10 text-sartori-teal mb-6">
            <svg class="w-7 h-7" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round"><path d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2"/><rect x="9" y="3" width="6" height="4" rx="1"/><path d="M9 14l2 2 4-4"/></svg>
          </div>
          <h3 class="font-heading font-bold text-xl text-sartori-navy-deep mb-4">Auditorías Técnicas y Evaluación de Activos</h3>
          <p class="font-body text-gray-500 leading-relaxed text-[0.938rem]">
            Diagnósticos detallados, análisis de riesgos, comparativas de rendimiento y recomendaciones estratégicas para mejorar la fiabilidad, la seguridad y la eficiencia operativa de instalaciones hidroeléctricas y subestaciones, en plena conformidad con las normas IEC, IEEE y ANSI.
          </p>
        </div>'''
        
    en_card_2_old = '''        <!-- Card 2: Auditorías Técnicas -->
        <div data-animate class="service-card bg-white rounded-xl p-8 shadow-sm hover:shadow-xl group delay-100">
          <div class="service-icon w-14 h-14 flex items-center justify-center rounded-xl bg-sartori-teal/10 text-sartori-teal mb-6">
            <svg class="w-7 h-7" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round"><path d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2"/><rect x="9" y="3" width="6" height="4" rx="1"/><path d="M9 14l2 2 4-4"/></svg>
          </div>
          <h3 class="font-heading font-bold text-xl text-sartori-navy-deep mb-4">Technical Audits and Asset Assessments</h3>
          <p class="font-body text-gray-500 leading-relaxed text-[0.938rem]">
            Detailed diagnostics, risk analyses, performance comparisons, and strategic recommendations to improve reliability, safety, and operational efficiency of hydroelectric facilities and substations, in full compliance with IEC, IEEE, and ANSI standards.
          </p>
        </div>'''

    card_2_new = f'''        <!-- Card 2: Auditorías Técnicas -->
        <div data-animate class="service-card bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl group transition-all duration-300 flex flex-col h-full delay-100">
          <div class="relative h-48 overflow-hidden">
            <img src="{prefix}assets/images/03 - USAR PARA SERVICIOS.jpg" alt="Technical Audits and Asset Assessments" class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700">
            <div class="absolute inset-0 bg-sartori-navy-deep/20 group-hover:bg-sartori-navy-deep/10 transition-colors"></div>
            <div class="absolute top-4 left-4 w-12 h-12 flex items-center justify-center rounded-xl bg-white/95 text-sartori-teal shadow-md">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round"><path d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2"/><rect x="9" y="3" width="6" height="4" rx="1"/><path d="M9 14l2 2 4-4"/></svg>
            </div>
          </div>
          <div class="p-6 lg:p-8 flex-grow flex flex-col">
            <h3 class="font-heading font-bold text-xl text-sartori-navy-deep mb-4">{"Technical Audits and Asset Assessments" if is_en else "Auditorías Técnicas y Evaluación de Activos"}</h3>
            <p class="font-body text-gray-500 leading-relaxed text-[0.938rem] flex-grow">
              {"Detailed diagnostics, risk analyses, performance comparisons, and strategic recommendations to improve reliability, safety, and operational efficiency of hydroelectric facilities and substations, in full compliance with IEC, IEEE, and ANSI standards." if is_en else "Diagnósticos detallados, análisis de riesgos, comparativas de rendimiento y recomendaciones estratégicas para mejorar la fiabilidad, la seguridad y la eficiencia operativa de instalaciones hidroeléctricas y subestaciones, en plena conformidad con las normas IEC, IEEE y ANSI."}
            </p>
          </div>
        </div>'''

    # --- CARD 3 ---
    es_card_3_old = '''        <!-- Card 3: Puesta en Servicio -->
        <div data-animate class="service-card bg-white rounded-xl p-8 shadow-sm hover:shadow-xl group delay-200">
          <div class="service-icon w-14 h-14 flex items-center justify-center rounded-xl bg-sartori-teal/10 text-sartori-teal mb-6">
            <svg class="w-7 h-7" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
          </div>
          <h3 class="font-heading font-bold text-xl text-sartori-navy-deep mb-4">Puesta en Servicio y Energización</h3>
          <p class="font-body text-gray-500 leading-relaxed text-[0.938rem]">
            Servicios integrales de puesta en servicio, pruebas y conexión a red para subestaciones de hasta <strong class="text-sartori-navy-deep">500 kV</strong>, incluyendo sistemas GIS de corriente alterna (CA) y corriente continua (CC) destinados a aplicaciones de metro y ferrocarril.
          </p>
        </div>'''
        
    en_card_3_old = '''        <!-- Card 3: Puesta en Servicio -->
        <div data-animate class="service-card bg-white rounded-xl p-8 shadow-sm hover:shadow-xl group delay-200">
          <div class="service-icon w-14 h-14 flex items-center justify-center rounded-xl bg-sartori-teal/10 text-sartori-teal mb-6">
            <svg class="w-7 h-7" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
          </div>
          <h3 class="font-heading font-bold text-xl text-sartori-navy-deep mb-4">Commissioning and Energization</h3>
          <p class="font-body text-gray-500 leading-relaxed text-[0.938rem]">
            Comprehensive commissioning, testing, and grid connection services for substations up to 500 kV, including AC and DC GIS systems for metro and railway applications.
          </p>
        </div>'''

    card_3_new = f'''        <!-- Card 3: Puesta en Servicio -->
        <div data-animate class="service-card bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl group transition-all duration-300 flex flex-col h-full delay-200">
          <div class="relative h-48 overflow-hidden">
            <img src="{prefix}assets/images/04 - USAR PARA SERVICIOS.jpg" alt="Commissioning and Energization" class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700">
            <div class="absolute inset-0 bg-sartori-navy-deep/20 group-hover:bg-sartori-navy-deep/10 transition-colors"></div>
            <div class="absolute top-4 left-4 w-12 h-12 flex items-center justify-center rounded-xl bg-white/95 text-sartori-teal shadow-md">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
            </div>
          </div>
          <div class="p-6 lg:p-8 flex-grow flex flex-col">
            <h3 class="font-heading font-bold text-xl text-sartori-navy-deep mb-4">{"Commissioning and Energization" if is_en else "Puesta en Servicio y Energización"}</h3>
            <p class="font-body text-gray-500 leading-relaxed text-[0.938rem] flex-grow">
              {"Comprehensive commissioning, testing, and grid connection services for substations up to 500 kV, including AC and DC GIS systems for metro and railway applications." if is_en else "Servicios integrales de puesta en servicio, pruebas y conexión a red para subestaciones de hasta <strong class=\\\"text-sartori-navy-deep\\\">500 kV</strong>, incluyendo sistemas GIS de corriente alterna (CA) y corriente continua (CC) destinados a aplicaciones de metro y ferrocarril."}
            </p>
          </div>
        </div>'''

    # --- CARD 4 ---
    es_card_4_old = '''        <!-- Card 4: Protección y Control -->
        <div data-animate class="service-card bg-white rounded-xl p-8 shadow-sm hover:shadow-xl group delay-300">
          <div class="service-icon w-14 h-14 flex items-center justify-center rounded-xl bg-sartori-teal/10 text-sartori-teal mb-6">
            <svg class="w-7 h-7" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
          </div>
          <h3 class="font-heading font-bold text-xl text-sartori-navy-deep mb-4">Sistemas de Protección y Control</h3>
          <p class="font-body text-gray-500 leading-relaxed text-[0.938rem]">
            Instalación, configuración, pruebas y parametrización de sistemas de protección y control. Garantizamos una coordinación óptima de los relés, selectividad del sistema, gestión de fallos y la fiabilidad de la red.
          </p>
        </div>'''
        
    en_card_4_old = '''        <!-- Card 4: Protection and Control -->
        <div data-animate class="service-card bg-white rounded-xl p-8 shadow-sm hover:shadow-xl group delay-300">
          <div class="service-icon w-14 h-14 flex items-center justify-center rounded-xl bg-sartori-teal/10 text-sartori-teal mb-6">
            <svg class="w-7 h-7" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
          </div>
          <h3 class="font-heading font-bold text-xl text-sartori-navy-deep mb-4">Protection and Control Systems</h3>
          <p class="font-body text-gray-500 leading-relaxed text-[0.938rem]">
            Installation, configuration, testing, and parameterization of protection and control systems. We ensure optimal relay coordination, system selectivity, fault management, and grid reliability.
          </p>
        </div>'''

    card_4_new = f'''        <!-- Card 4: Protección y Control -->
        <div data-animate class="service-card bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl group transition-all duration-300 flex flex-col h-full delay-300">
          <div class="relative h-48 overflow-hidden">
            <img src="{prefix}assets/images/06 - USAR PARA SERVICIOS.jpg" alt="Protection and Control Systems" class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700">
            <div class="absolute inset-0 bg-sartori-navy-deep/20 group-hover:bg-sartori-navy-deep/10 transition-colors"></div>
            <div class="absolute top-4 left-4 w-12 h-12 flex items-center justify-center rounded-xl bg-white/95 text-sartori-teal shadow-md">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            </div>
          </div>
          <div class="p-6 lg:p-8 flex-grow flex flex-col">
            <h3 class="font-heading font-bold text-xl text-sartori-navy-deep mb-4">{"Protection and Control Systems" if is_en else "Sistemas de Protección y Control"}</h3>
            <p class="font-body text-gray-500 leading-relaxed text-[0.938rem] flex-grow">
              {"Installation, configuration, testing, and parameterization of protection and control systems. We ensure optimal relay coordination, system selectivity, fault management, and grid reliability." if is_en else "Instalación, configuración, pruebas y parametrización de sistemas de protección y control. Garantizamos una coordinación óptima de los relés, selectividad del sistema, gestión de fallos y la fiabilidad de la red."}
            </p>
          </div>
        </div>'''

    # --- CARD 5 ---
    es_card_5_old = '''        <!-- Card 5: Pruebas y Verificación -->
        <div data-animate class="service-card bg-white rounded-xl p-8 shadow-sm hover:shadow-xl group delay-400">
          <div class="service-icon w-14 h-14 flex items-center justify-center rounded-xl bg-sartori-teal/10 text-sartori-teal mb-6">
            <svg class="w-7 h-7" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>
          </div>
          <h3 class="font-heading font-bold text-xl text-sartori-navy-deep mb-4">Pruebas y Verificación</h3>
          <ul class="font-body text-gray-500 text-[0.938rem] space-y-2">
            <li class="flex items-start gap-2">
              <span class="text-sartori-teal mt-1 flex-shrink-0">▸</span>
              <span>Pruebas funcionales y dieléctricas de transformadores de medida (TC y TT)</span>
            </li>
            <li class="flex items-start gap-2">
              <span class="text-sartori-teal mt-1 flex-shrink-0">▸</span>
              <span>Instalación y puesta en servicio de interruptores de media y alta tensión</span>
            </li>
            <li class="flex items-start gap-2">
              <span class="text-sartori-teal mt-1 flex-shrink-0">▸</span>
              <span>Verificación de seccionadores e interruptores de puesta a tierra</span>
            </li>
            <li class="flex items-start gap-2">
              <span class="text-sartori-teal mt-1 flex-shrink-0">▸</span>
              <span>Mantenimiento preventivo y correctivo</span>
            </li>
          </ul>
        </div>'''
        
    en_card_5_old = '''        <!-- Card 5: Testing and Verification -->
        <div data-animate class="service-card bg-white rounded-xl p-8 shadow-sm hover:shadow-xl group delay-400">
          <div class="service-icon w-14 h-14 flex items-center justify-center rounded-xl bg-sartori-teal/10 text-sartori-teal mb-6">
            <svg class="w-7 h-7" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>
          </div>
          <h3 class="font-heading font-bold text-xl text-sartori-navy-deep mb-4">Testing and Verification</h3>
          <ul class="font-body text-gray-500 text-[0.938rem] space-y-2">
            <li class="flex items-start gap-2">
              <span class="text-sartori-teal mt-1 flex-shrink-0">▸</span>
              <span>Functional and dielectric testing of instrument transformers (CTs and VTs)</span>
            </li>
            <li class="flex items-start gap-2">
              <span class="text-sartori-teal mt-1 flex-shrink-0">▸</span>
              <span>Installation and commissioning of medium and high-voltage circuit breakers</span>
            </li>
            <li class="flex items-start gap-2">
              <span class="text-sartori-teal mt-1 flex-shrink-0">▸</span>
              <span>Verification of disconnect switches and grounding switches</span>
            </li>
            <li class="flex items-start gap-2">
              <span class="text-sartori-teal mt-1 flex-shrink-0">▸</span>
              <span>Preventive and corrective maintenance</span>
            </li>
          </ul>
        </div>'''

    card_5_new = f'''        <!-- Card 5: Pruebas y Verificación -->
        <div data-animate class="service-card bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl group transition-all duration-300 flex flex-col h-full delay-400">
          <div class="relative h-48 overflow-hidden">
            <img src="{prefix}assets/images/07 - USAR PARA SERVICIOS.jpg" alt="Testing and Verification" class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700">
            <div class="absolute inset-0 bg-sartori-navy-deep/20 group-hover:bg-sartori-navy-deep/10 transition-colors"></div>
            <div class="absolute top-4 left-4 w-12 h-12 flex items-center justify-center rounded-xl bg-white/95 text-sartori-teal shadow-md">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>
            </div>
          </div>
          <div class="p-6 lg:p-8 flex-grow flex flex-col">
            <h3 class="font-heading font-bold text-xl text-sartori-navy-deep mb-4">{"Testing and Verification" if is_en else "Pruebas y Verificación"}</h3>
            <ul class="font-body text-gray-500 text-[0.938rem] space-y-2 flex-grow">
              {"<li class=\\\"flex items-start gap-2\\\"><span class=\\\"text-sartori-teal mt-1 flex-shrink-0\\\">▸</span><span>Functional and dielectric testing of instrument transformers (CTs and VTs)</span></li><li class=\\\"flex items-start gap-2\\\"><span class=\\\"text-sartori-teal mt-1 flex-shrink-0\\\">▸</span><span>Installation and commissioning of medium and high-voltage circuit breakers</span></li><li class=\\\"flex items-start gap-2\\\"><span class=\\\"text-sartori-teal mt-1 flex-shrink-0\\\">▸</span><span>Verification of disconnect switches and grounding switches</span></li><li class=\\\"flex items-start gap-2\\\"><span class=\\\"text-sartori-teal mt-1 flex-shrink-0\\\">▸</span><span>Preventive and corrective maintenance</span></li>" if is_en else "<li class=\\\"flex items-start gap-2\\\"><span class=\\\"text-sartori-teal mt-1 flex-shrink-0\\\">▸</span><span>Pruebas funcionales y dieléctricas de transformadores de medida (TC y TT)</span></li><li class=\\\"flex items-start gap-2\\\"><span class=\\\"text-sartori-teal mt-1 flex-shrink-0\\\">▸</span><span>Instalación y puesta en servicio de interruptores de media y alta tensión</span></li><li class=\\\"flex items-start gap-2\\\"><span class=\\\"text-sartori-teal mt-1 flex-shrink-0\\\">▸</span><span>Verificación de seccionadores e interruptores de puesta a tierra</span></li><li class=\\\"flex items-start gap-2\\\"><span class=\\\"text-sartori-teal mt-1 flex-shrink-0\\\">▸</span><span>Mantenimiento preventivo y correctivo</span></li>"}
            </ul>
          </div>
        </div>'''

    # --- CARD 6 ---
    es_card_6_old = '''        <!-- Card 6: Sincronización y Control -->
        <div data-animate class="service-card bg-white rounded-xl p-8 shadow-sm hover:shadow-xl group delay-500">
          <div class="service-icon w-14 h-14 flex items-center justify-center rounded-xl bg-sartori-teal/10 text-sartori-teal mb-6">
            <svg class="w-7 h-7" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round"><path d="M23 4v6h-6M1 20v-6h6"/><path d="M3.51 9a9 9 0 0114.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0020.49 15"/></svg>
          </div>
          <h3 class="font-heading font-bold text-xl text-sartori-navy-deep mb-4">Sistemas de Sincronización y Control</h3>
          <p class="font-body text-gray-500 leading-relaxed text-[0.938rem]">
            Plataformas avanzadas de sincronización automática de interruptores mediante metodologías probadas para optimizar la estabilidad del sistema, maximizar la disponibilidad de los activos y garantizar una operación segura de la infraestructura.
          </p>
        </div>'''
        
    en_card_6_old = '''        <!-- Card 6: Synchronization and Control Systems -->
        <div data-animate class="service-card bg-white rounded-xl p-8 shadow-sm hover:shadow-xl group delay-500">
          <div class="service-icon w-14 h-14 flex items-center justify-center rounded-xl bg-sartori-teal/10 text-sartori-teal mb-6">
            <svg class="w-7 h-7" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round"><path d="M23 4v6h-6M1 20v-6h6"/><path d="M3.51 9a9 9 0 0114.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0020.49 15"/></svg>
          </div>
          <h3 class="font-heading font-bold text-xl text-sartori-navy-deep mb-4">Synchronization and Control Systems</h3>
          <p class="font-body text-gray-500 leading-relaxed text-[0.938rem]">
            Advanced platforms for automatic circuit breaker synchronization using proven methodologies to optimize system stability, maximize asset availability, and ensure safe infrastructure operation.
          </p>
        </div>'''

    card_6_new = f'''        <!-- Card 6: Sincronización y Control -->
        <div data-animate class="service-card bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl group transition-all duration-300 flex flex-col h-full delay-500">
          <div class="relative h-48 overflow-hidden">
            <img src="{prefix}assets/images/09 - USAR PARA SERVICIOS.jpg" alt="Synchronization and Control Systems" class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700">
            <div class="absolute inset-0 bg-sartori-navy-deep/20 group-hover:bg-sartori-navy-deep/10 transition-colors"></div>
            <div class="absolute top-4 left-4 w-12 h-12 flex items-center justify-center rounded-xl bg-white/95 text-sartori-teal shadow-md">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round"><path d="M23 4v6h-6M1 20v-6h6"/><path d="M3.51 9a9 9 0 0114.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0020.49 15"/></svg>
            </div>
          </div>
          <div class="p-6 lg:p-8 flex-grow flex flex-col">
            <h3 class="font-heading font-bold text-xl text-sartori-navy-deep mb-4">{"Synchronization and Control Systems" if is_en else "Sistemas de Sincronización y Control"}</h3>
            <p class="font-body text-gray-500 leading-relaxed text-[0.938rem] flex-grow">
              {"Advanced platforms for automatic circuit breaker synchronization using proven methodologies to optimize system stability, maximize asset availability, and ensure safe infrastructure operation." if is_en else "Plataformas avanzadas de sincronización automática de interruptores mediante metodologías probadas para optimizar la estabilidad del sistema, maximizar la disponibilidad de los activos y garantizar una operación segura de la infraestructura."}
            </p>
          </div>
        </div>'''

    if is_en:
        content = content.replace(en_card_1_old, card_1_new)
        content = content.replace(en_card_2_old, card_2_new)
        content = content.replace(en_card_3_old, card_3_new)
        content = content.replace(en_card_4_old, card_4_new)
        content = content.replace(en_card_5_old, card_5_new)
        content = content.replace(en_card_6_old, card_6_new)
    else:
        content = content.replace(es_card_1_old, card_1_new)
        content = content.replace(es_card_2_old, card_2_new)
        content = content.replace(es_card_3_old, card_3_new)
        content = content.replace(es_card_4_old, card_4_new)
        content = content.replace(es_card_5_old, card_5_new)
        content = content.replace(es_card_6_old, card_6_new)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

process_file('index.html', is_en=False)
process_file('en/index.html', is_en=True)
print("Hero, CTA, Team backgrounds and Service cards with images successfully integrated!")
