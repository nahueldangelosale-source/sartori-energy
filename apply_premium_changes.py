import re

def process_file(filepath, is_en=False):
    prefix = "../" if is_en else ""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Custom CSS animations for cinematic trailer reveal
    css_to_add = '''    @keyframes tracking-in-expand {
      0% { letter-spacing: -0.5em; opacity: 0; filter: blur(10px); }
      40% { opacity: 0.6; }
      100% { opacity: 1; filter: blur(0); }
    }
    .animate-tracking-expand {
      animation: tracking-in-expand 1.6s cubic-bezier(0.215, 0.610, 0.355, 1.000) both;
    }
    
    /* Radial glow for elements */
    .glow-hover {
      transition: all 0.3s ease;
    }
    .glow-hover:hover {
      box-shadow: 0 0 25px rgba(245, 158, 11, 0.35);
      border-color: rgba(245, 158, 11, 0.6);
      transform: scale(1.03);
    }'''

    content = content.replace(
      '    /* Grid overlay for ind',
      css_to_add + '\n\n    /* Grid overlay for ind'
    )

    # 2. H1 and Tagline optimization
    old_h1_block = '''        <h1 class="font-heading font-extrabold text-5xl sm:text-6xl lg:text-7xl text-white tracking-tight animate-fade-up">
          SARTORI <span class="text-sartori-amber">Energy</span>
        </h1>

        <!-- Tagline -->
        <p class="mt-3 font-heading font-normal text-sm text-sartori-teal-light tracking-[0.15em] uppercase animate-fade-up delay-100">
          Your energy project, our mission
        </p>'''

    new_h1_block = f'''        <!-- H1 -->
        <h1 class="font-heading font-black text-6xl sm:text-7xl lg:text-8xl text-white tracking-tighter animate-tracking-expand" style="text-shadow: 0 10px 30px rgba(0,7,45,0.75);">
          SARTORI <span class="text-sartori-amber filter drop-shadow-[0_0_20px_rgba(245,158,11,0.4)]">Energy</span>
        </h1>

        <!-- Tagline -->
        <p class="mt-5 font-heading font-extrabold text-base md:text-lg text-sartori-teal tracking-[0.25em] uppercase animate-fade-up delay-300" style="text-shadow: 0 2px 10px rgba(0,7,45,0.6);">
          Your energy project, <span class="text-sartori-amber">our mission</span>
        </p>'''

    content = content.replace(old_h1_block, new_h1_block)

    # 3. Transparent watermark logo in Hero
    # Remove old SVG logo watermark
    svg_watermark = '''    <!-- Decorative Logo Watermark -->
    <svg class="absolute right-0 top-1/2 -translate-y-1/2 w-[500px] h-[600px] opacity-[0.03] hidden lg:block" viewBox="0 0 100 120" fill="none">
      <polygon points="38,0 100,0 100,48 62,48" fill="white"/>
      <polygon points="38,0 62,48 38,48" fill="white"/>
      <polygon points="62,72 38,72 62,120" fill="white"/>
      <polygon points="0,72 62,72 38,120 0,120" fill="white"/>
    </svg>'''
    
    new_img_watermark = f'''    <!-- Large Logo Watermark on the side -->
    <div class="absolute right-[-80px] lg:right-[5%] top-1/2 -translate-y-1/2 w-[350px] lg:w-[450px] opacity-[0.035] hidden md:block pointer-events-none z-0 select-none animate-pulse" style="animation-duration: 6s;">
      <img src="{prefix}assets/images/logo.png" alt="Sartori Logo Watermark" class="w-full h-auto">
    </div>'''
    
    content = content.replace(svg_watermark, new_img_watermark)

    # 4. Hero video ID and playbackRate slow down
    content = content.replace(
        '<video autoplay loop muted playsinline class="w-full h-full object-cover opacity-25">',
        '<video id="hero-video" autoplay loop muted playsinline class="w-full h-full object-cover opacity-25">'
    )

    js_video_speed = '''    // ---- Hero Video Speed ----
    const heroVideo = document.getElementById('hero-video');
    if (heroVideo) {
      heroVideo.playbackRate = 0.5; // cinematic slow motion
    }'''

    # Insert inside the last script tag at the bottom before </script>
    content = content.replace(
        '// ---- Smooth Scroll for anchor links ----',
        js_video_speed + '\n\n    // ---- Smooth Scroll for anchor links ----'
    )

    # 5. Language flag fixes for Spanish version
    if not is_en:
        # replace the ES -> EN link emoji with fi-gb
        content = content.replace(
            '<a href="./en/index.html" class="text-white/50 hover:text-white font-body text-sm transition-colors duration-200">🇬🇧 EN</a>',
            '<a href="./en/index.html" class="text-white/50 hover:text-white font-body text-sm transition-colors duration-200"><span class="fi fi-gb rounded-sm mr-1 opacity-50"></span> EN</a>'
        )
        # Mobile ES/EN flag emoji replacement
        content = content.replace(
            '<a href="./en/index.html" class="text-white/50 hover:text-white font-body">🇬🇧 EN</a>',
            '<a href="./en/index.html" class="text-white/50 hover:text-white font-body"><span class="fi fi-gb rounded-sm mr-1 opacity-50"></span> EN</a>'
        )

    # 6. GIS / AIS Badges optimization
    gis_ais_old = '''        <div class="mt-8 flex flex-wrap gap-3 animate-fade-up delay-400">
          <span class="inline-flex items-center gap-2 px-5 py-2.5 border border-sartori-amber/40 bg-sartori-amber/10 text-sartori-amber font-heading font-semibold text-sm rounded-full backdrop-blur-sm">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z" stroke-linecap="round" stroke-linejoin="round"/></svg>
            Tecnología GIS
            <span class="text-xs text-sartori-amber/70 font-body font-normal">(Gas-Insulated Switchgear)</span>
          </span>
          <span class="inline-flex items-center gap-2 px-5 py-2.5 border border-sartori-teal/40 bg-sartori-teal/10 text-sartori-teal-light font-heading font-semibold text-sm rounded-full backdrop-blur-sm">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z" stroke-linecap="round" stroke-linejoin="round"/></svg>
            Tecnología AIS
            <span class="text-xs text-sartori-teal-light/70 font-body font-normal">(Air-Insulated Switchgear)</span>
          </span>
        </div>'''
        
    gis_ais_old_en = '''        <div class="mt-8 flex flex-wrap gap-3 animate-fade-up delay-400">
          <span class="inline-flex items-center gap-2 px-5 py-2.5 border border-sartori-amber/40 bg-sartori-amber/10 text-sartori-amber font-heading font-semibold text-sm rounded-full backdrop-blur-sm">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z" stroke-linecap="round" stroke-linejoin="round"/></svg>
            GIS Technology
            <span class="text-xs text-sartori-amber/70 font-body font-normal">(Gas-Insulated Switchgear)</span>
          </span>
          <span class="inline-flex items-center gap-2 px-5 py-2.5 border border-sartori-teal/40 bg-sartori-teal/10 text-sartori-teal-light font-heading font-semibold text-sm rounded-full backdrop-blur-sm">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z" stroke-linecap="round" stroke-linejoin="round"/></svg>
            AIS Technology
            <span class="text-xs text-sartori-teal-light/70 font-body font-normal">(Air-Insulated Switchgear)</span>
          </span>
        </div>'''

    gis_ais_new = f'''        <div class="mt-8 flex flex-wrap gap-3 animate-fade-up delay-400">
          <a href="#servicios" class="inline-flex items-center gap-2 px-5 py-2.5 border border-sartori-amber/30 bg-sartori-amber/5 text-sartori-amber font-heading font-semibold text-sm rounded-full backdrop-blur-sm hover:scale-105 hover:bg-sartori-amber/15 hover:border-sartori-amber/60 hover:shadow-[0_0_20px_rgba(245,158,11,0.25)] transition-all duration-300 group/badge">
            <svg class="w-4 h-4 text-sartori-amber group-hover/badge:rotate-12 transition-transform" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z" stroke-linecap="round" stroke-linejoin="round"/></svg>
            <span>{"GIS Technology" if is_en else "Tecnología GIS"}</span>
            <span class="text-xs text-sartori-amber/60 font-body font-normal group-hover/badge:text-sartori-amber/90 transition-colors">(Gas-Insulated Switchgear)</span>
          </a>
          <a href="#servicios" class="inline-flex items-center gap-2 px-5 py-2.5 border border-sartori-teal/30 bg-sartori-teal/5 text-sartori-teal-light font-heading font-semibold text-sm rounded-full backdrop-blur-sm hover:scale-105 hover:bg-sartori-teal/15 hover:border-sartori-teal/60 hover:shadow-[0_0_20px_rgba(42,123,136,0.25)] transition-all duration-300 group/badge2">
            <svg class="w-4 h-4 text-sartori-teal-light group-hover/badge2:rotate-12 transition-transform" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z" stroke-linecap="round" stroke-linejoin="round"/></svg>
            <span>{"AIS Technology" if is_en else "Tecnología AIS"}</span>
            <span class="text-xs text-sartori-teal-light/60 font-body font-normal group-hover/badge2:text-sartori-teal-light/90 transition-colors">(Air-Insulated Switchgear)</span>
          </a>
        </div>'''

    if is_en:
        content = content.replace(gis_ais_old_en, gis_ais_new)
    else:
        content = content.replace(gis_ais_old, gis_ais_new)

    # 7. Redesign Trust Bar
    # We will search for the entire <section class="relative bg-sartori-navy-deep border-t border-white/5"> block
    # and replace it with the new dashboard horizontal grid
    trust_bar_old_es = '''  <section class="relative bg-sartori-navy-deep border-t border-white/5">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
      <div class="grid grid-cols-2 lg:grid-cols-4 gap-6 lg:gap-8">
        <!-- Pilar 1: Seguridad -->
        <div data-animate class="flex items-center gap-4 group">
          <div class="w-12 h-12 flex items-center justify-center rounded-xl bg-sartori-teal/10 border border-sartori-teal/20 group-hover:bg-sartori-teal/20 transition-all">
            <svg class="w-6 h-6 text-sartori-teal" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" stroke-linecap="round" stroke-linejoin="round"/><path d="M9 12l2 2 4-4" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </div>
          <div>
            <p class="font-heading font-bold text-white text-sm tracking-wide">SEGURIDAD</p>
            <p class="font-body text-xs text-white/40 mt-0.5">en cada proyecto</p>
          </div>
        </div>
        <!-- Pilar 2: Precisión Técnica -->
        <div data-animate class="flex items-center gap-4 group delay-100">
          <div class="w-12 h-12 flex items-center justify-center rounded-xl bg-sartori-teal/10 border border-sartori-teal/20 group-hover:bg-sartori-teal/20 transition-all">
            <svg class="w-6 h-6 text-sartori-teal" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>
          </div>
          <div>
            <p class="font-heading font-bold text-white text-sm tracking-wide">PRECISIÓN TÉCNICA</p>
            <p class="font-body text-xs text-white/40 mt-0.5">en cada detalle</p>
          </div>
        </div>
        <!-- Pilar 3: Eficiencia -->
        <div data-animate class="flex items-center gap-4 group delay-200">
          <div class="w-12 h-12 flex items-center justify-center rounded-xl bg-sartori-teal/10 border border-sartori-teal/20 group-hover:bg-sartori-teal/20 transition-all">
            <svg class="w-6 h-6 text-sartori-teal" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </div>
          <div>
            <p class="font-heading font-bold text-white text-sm tracking-wide">EFICIENCIA</p>
            <p class="font-body text-xs text-white/40 mt-0.5">que genera valor</p>
          </div>
        </div>
        <!-- Pilar 4: Experiencia Global -->
        <div data-animate class="flex items-center gap-4 group delay-300">
          <div class="w-12 h-12 flex items-center justify-center rounded-xl bg-sartori-teal/10 border border-sartori-teal/20 group-hover:bg-sartori-teal/20 transition-all">
            <svg class="w-6 h-6 text-sartori-teal" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 014 10 15.3 15.3 0 01-4 10 15.3 15.3 0 01-4-10A15.3 15.3 0 0112 2z"/></svg>
          </div>
          <div>
            <p class="font-heading font-bold text-white text-sm tracking-wide">EXPERIENCIA GLOBAL</p>
            <p class="font-body text-xs text-white/40 mt-0.5">compromiso local</p>
          </div>
        </div>
      </div>
    </div>
  </section>'''

    trust_bar_old_en = '''  <section class="relative bg-sartori-navy-deep border-t border-white/5">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
      <div class="grid grid-cols-2 lg:grid-cols-4 gap-6 lg:gap-8">
        <!-- Pilar 1: Seguridad -->
        <div data-animate class="flex items-center gap-4 group">
          <div class="w-12 h-12 flex items-center justify-center rounded-xl bg-sartori-teal/10 border border-sartori-teal/20 group-hover:bg-sartori-teal/20 transition-all">
            <svg class="w-6 h-6 text-sartori-teal" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" stroke-linecap="round" stroke-linejoin="round"/><path d="M9 12l2 2 4-4" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </div>
          <div>
            <p class="font-heading font-bold text-white text-sm tracking-wide">SAFETY</p>
            <p class="font-body text-xs text-white/40 mt-0.5">in every project</p>
          </div>
        </div>
        <!-- Pilar 2: Precisión Técnica -->
        <div data-animate class="flex items-center gap-4 group delay-100">
          <div class="w-12 h-12 flex items-center justify-center rounded-xl bg-sartori-teal/10 border border-sartori-teal/20 group-hover:bg-sartori-teal/20 transition-all">
            <svg class="w-6 h-6 text-sartori-teal" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>
          </div>
          <div>
            <p class="font-heading font-bold text-white text-sm tracking-wide">TECHNICAL PRECISION</p>
            <p class="font-body text-xs text-white/40 mt-0.5">in every detail</p>
          </div>
        </div>
        <!-- Pilar 3: Eficiencia -->
        <div data-animate class="flex items-center gap-4 group delay-200">
          <div class="w-12 h-12 flex items-center justify-center rounded-xl bg-sartori-teal/10 border border-sartori-teal/20 group-hover:bg-sartori-teal/20 transition-all">
            <svg class="w-6 h-6 text-sartori-teal" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </div>
          <div>
            <p class="font-heading font-bold text-white text-sm tracking-wide">EFFICIENCY</p>
            <p class="font-body text-xs text-white/40 mt-0.5">that generates value</p>
          </div>
        </div>
        <!-- Pilar 4: Experiencia Global -->
        <div data-animate class="flex items-center gap-4 group delay-300">
          <div class="w-12 h-12 flex items-center justify-center rounded-xl bg-sartori-teal/10 border border-sartori-teal/20 group-hover:bg-sartori-teal/20 transition-all">
            <svg class="w-6 h-6 text-sartori-teal" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 014 10 15.3 15.3 0 01-4 10 15.3 15.3 0 01-4-10A15.3 15.3 0 0112 2z"/></svg>
          </div>
          <div>
            <p class="font-heading font-bold text-white text-sm tracking-wide">GLOBAL EXPERIENCE</p>
            <p class="font-body text-xs text-white/40 mt-0.5">local commitment</p>
          </div>
        </div>
      </div>
    </div>
  </section>'''

    new_trust_bar = f'''  <!-- ========================================
       TRUST BAR (4 PILARES)
       ======================================== -->
  <section class="relative bg-sartori-navy-deep border-y border-white/5 overflow-hidden">
    <!-- Subtle Top Glow Line -->
    <div class="absolute top-0 left-0 w-full h-[1px] bg-gradient-to-r from-transparent via-sartori-teal/20 to-transparent"></div>
    
    <div class="max-w-7xl mx-auto px-0">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 divide-y lg:divide-y-0 lg:divide-x divide-white/5">
        <!-- Pilar 1: Seguridad -->
        <div data-animate class="flex flex-col p-8 group hover:bg-white/[0.01] transition-all duration-300 relative overflow-hidden">
          <div class="absolute top-0 left-0 w-full h-[1.5px] bg-gradient-to-r from-transparent via-sartori-teal to-transparent scale-x-0 group-hover:scale-x-100 transition-transform duration-500 origin-center"></div>
          <div class="flex items-center gap-3 mb-3">
            <span class="text-xs font-heading font-bold text-sartori-teal tracking-widest font-mono opacity-60">01 //</span>
            <span class="text-sartori-teal group-hover:scale-110 group-hover:rotate-6 transition-transform duration-300">
              <svg class="w-5 h-5 stroke-[1.5]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" stroke-linecap="round" stroke-linejoin="round"/><path d="M9 12l2 2 4-4" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </span>
          </div>
          <h3 class="font-heading font-extrabold text-white text-sm tracking-[0.15em] uppercase">{"SAFETY" if is_en else "SEGURIDAD"}</h3>
          <p class="font-body text-xs text-white/50 mt-1">{"in every project" if is_en else "en cada proyecto"}</p>
        </div>
        <!-- Pilar 2: Precisión Técnica -->
        <div data-animate class="flex flex-col p-8 group hover:bg-white/[0.01] transition-all duration-300 relative overflow-hidden delay-100">
          <div class="absolute top-0 left-0 w-full h-[1.5px] bg-gradient-to-r from-transparent via-sartori-teal to-transparent scale-x-0 group-hover:scale-x-100 transition-transform duration-500 origin-center"></div>
          <div class="flex items-center gap-3 mb-3">
            <span class="text-xs font-heading font-bold text-sartori-teal tracking-widest font-mono opacity-60">02 //</span>
            <span class="text-sartori-teal group-hover:scale-110 group-hover:rotate-6 transition-transform duration-300">
              <svg class="w-5 h-5 stroke-[1.5]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>
            </span>
          </div>
          <h3 class="font-heading font-extrabold text-white text-sm tracking-[0.15em] uppercase">{"TECHNICAL PRECISION" if is_en else "PRECISIÓN TÉCNICA"}</h3>
          <p class="font-body text-xs text-white/50 mt-1">{"in every detail" if is_en else "en cada detalle"}</p>
        </div>
        <!-- Pilar 3: Eficiencia -->
        <div data-animate class="flex flex-col p-8 group hover:bg-white/[0.01] transition-all duration-300 relative overflow-hidden delay-200">
          <div class="absolute top-0 left-0 w-full h-[1.5px] bg-gradient-to-r from-transparent via-sartori-teal to-transparent scale-x-0 group-hover:scale-x-100 transition-transform duration-500 origin-center"></div>
          <div class="flex items-center gap-3 mb-3">
            <span class="text-xs font-heading font-bold text-sartori-teal tracking-widest font-mono opacity-60">03 //</span>
            <span class="text-sartori-teal group-hover:scale-110 group-hover:rotate-6 transition-transform duration-300">
              <svg class="w-5 h-5 stroke-[1.5]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </span>
          </div>
          <h3 class="font-heading font-extrabold text-white text-sm tracking-[0.15em] uppercase">{"EFFICIENCY" if is_en else "EFICIENCIA"}</h3>
          <p class="font-body text-xs text-white/50 mt-1">{"that generates value" if is_en else "que genera valor"}</p>
        </div>
        <!-- Pilar 4: Experiencia Global -->
        <div data-animate class="flex flex-col p-8 group hover:bg-white/[0.01] transition-all duration-300 relative overflow-hidden delay-300">
          <div class="absolute top-0 left-0 w-full h-[1.5px] bg-gradient-to-r from-transparent via-sartori-teal to-transparent scale-x-0 group-hover:scale-x-100 transition-transform duration-500 origin-center"></div>
          <div class="flex items-center gap-3 mb-3">
            <span class="text-xs font-heading font-bold text-sartori-teal tracking-widest font-mono opacity-60">04 //</span>
            <span class="text-sartori-teal group-hover:scale-110 group-hover:rotate-6 transition-transform duration-300">
              <svg class="w-5 h-5 stroke-[1.5]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 014 10 15.3 15.3 0 01-4 10 15.3 15.3 0 01-4-10A15.3 15.3 0 0112 2z"/></svg>
            </span>
          </div>
          <h3 class="font-heading font-extrabold text-white text-sm tracking-[0.15em] uppercase">{"GLOBAL EXPERIENCE" if is_en else "EXPERIENCIA GLOBAL"}</h3>
          <p class="font-body text-xs text-white/50 mt-1">{"local commitment" if is_en else "compromiso local"}</p>
        </div>
      </div>
    </div>
  </section>'''

    if is_en:
        content = content.replace(trust_bar_old_en, new_trust_bar)
    else:
        content = content.replace(trust_bar_old_es, new_trust_bar)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

process_file('index.html', is_en=False)
process_file('en/index.html', is_en=True)
print("Changes applied!")
