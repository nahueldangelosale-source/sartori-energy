def fix_files():
    # 1. ES version fixes
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Add custom animations to <style> block
    custom_styles = '''    /* Animated line for hero paragraphs */
    @keyframes lineExpand {
      0% { transform: scaleY(0); }
      100% { transform: scaleY(1); }
    }
    .animate-line-expand {
      animation: lineExpand 1.2s cubic-bezier(0.25, 1, 0.5, 1) 0.8s both;
    }
    
    @keyframes fadeInLeft {
      0% { opacity: 0; transform: translateX(-15px); filter: blur(2px); }
      100% { opacity: 1; transform: translateX(0); filter: blur(0); }
    }
    .animate-fade-in-left {
      animation: fadeInLeft 1.2s cubic-bezier(0.25, 1, 0.5, 1) both;
    }'''

    content = content.replace(
        '    .animate-tracking-expand {',
        custom_styles + '\n\n    .animate-tracking-expand {'
    )

    # Replace logo watermark div with z-10, right side, opacity 0.15, and brightness/invert filter to make it pure white
    old_watermark = '''    <!-- Large Logo Watermark on the Right (Sober & Static) -->
    <div class="absolute right-[8%] lg:right-[10%] top-[28%] w-[180px] lg:w-[240px] opacity-[0.09] hidden md:block pointer-events-none z-10 select-none">
      <img src="assets/images/logo.png" alt="Sartori Logo Watermark" class="w-full h-auto">
    </div>'''

    new_watermark = '''    <!-- Large Logo Watermark on the Right (Pure White & z-20) -->
    <div class="absolute right-[6%] lg:right-[8%] top-[28%] w-[180px] lg:w-[240px] hidden md:block pointer-events-none z-20 select-none" style="opacity: 0.14;">
      <img src="assets/images/logo.png" alt="Sartori Logo Watermark" class="w-full h-auto" style="filter: brightness(0) invert(1);">
    </div>'''

    content = content.replace(old_watermark, new_watermark)

    # Wrap the paragraphs in a side-border block with animation
    old_paragraphs_es = '''        <!-- Subtitle -->
        <p class="mt-8 font-body text-lg md:text-xl text-white/85 leading-relaxed max-w-2xl animate-fade-up delay-200">
          Soluciones especializadas de ingeniería eléctrica para todo el espectro en infraestructura de estaciones transformadoras de <strong class="text-sartori-navy-deep">alta y extra alta tensión</strong>.
        </p>
        <p class="mt-4 font-body text-sm md:text-base text-white/60 leading-relaxed max-w-2xl animate-fade-up delay-300">
          Ejecución técnica rigurosa y compromiso con los más altos estándares internacionales para proyectos complejos de transmisión de energía y subestaciones.
        </p>'''

    new_paragraphs_es = '''        <!-- Staggered Paragraphs Block with Left line -->
        <div class="mt-8 border-l border-sartori-teal/20 pl-6 space-y-4 relative">
          <!-- Animated left border line -->
          <div class="absolute left-0 top-0 w-[1.5px] h-full bg-sartori-amber scale-y-0 origin-top animate-line-expand"></div>
          
          <p class="font-body text-lg md:text-xl text-white/85 leading-relaxed max-w-2xl animate-fade-in-left" style="animation-delay: 1.2s;">
            Soluciones especializadas de ingeniería eléctrica para todo el espectro en infraestructura de estaciones transformadoras de <strong class="text-sartori-amber font-bold">alta y extra alta tensión</strong>.
          </p>
          <p class="font-body text-sm md:text-base text-white/60 leading-relaxed max-w-2xl animate-fade-in-left" style="animation-delay: 1.4s;">
            Ejecución técnica rigurosa y compromiso con los más altos estándares internacionales para proyectos complejos de transmisión de energía y subestaciones.
          </p>
        </div>'''

    content = content.replace(old_paragraphs_es, new_paragraphs_es)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("ES file successfully updated!")

    # 2. EN version fixes
    with open('en/index.html', 'r', encoding='utf-8') as f:
        content_en = f.read()

    content_en = content_en.replace(
        '    .animate-tracking-expand {',
        custom_styles + '\n\n    .animate-tracking-expand {'
    )

    old_watermark_en = '''    <!-- Large Logo Watermark on the Right (Sober & Static) -->
    <div class="absolute right-[8%] lg:right-[10%] top-[28%] w-[180px] lg:w-[240px] opacity-[0.09] hidden md:block pointer-events-none z-10 select-none">
      <img src="../assets/images/logo.png" alt="Sartori Logo Watermark" class="w-full h-auto">
    </div>'''

    new_watermark_en = '''    <!-- Large Logo Watermark on the Right (Pure White & z-20) -->
    <div class="absolute right-[6%] lg:right-[8%] top-[28%] w-[180px] lg:w-[240px] hidden md:block pointer-events-none z-20 select-none" style="opacity: 0.14;">
      <img src="../assets/images/logo.png" alt="Sartori Logo Watermark" class="w-full h-auto" style="filter: brightness(0) invert(1);">
    </div>'''

    content_en = content_en.replace(old_watermark_en, new_watermark_en)

    old_paragraphs_en = '''        <!-- Subtitle -->
        <p class="mt-8 font-body text-lg md:text-xl text-white/85 leading-relaxed max-w-2xl animate-fade-up delay-200">
          Specialized electrical engineering solutions across the entire spectrum of high- and extra-high-voltage substation infrastructure.
        </p>
        <p class="mt-4 font-body text-sm md:text-base text-white/60 leading-relaxed max-w-2xl animate-fade-up delay-300">
          Rigorous technical execution and commitment to the highest international standards for complex power transmission and substation projects.
        </p>'''

    new_paragraphs_en = '''        <!-- Staggered Paragraphs Block with Left line -->
        <div class="mt-8 border-l border-sartori-teal/20 pl-6 space-y-4 relative">
          <!-- Animated left border line -->
          <div class="absolute left-0 top-0 w-[1.5px] h-full bg-sartori-amber scale-y-0 origin-top animate-line-expand"></div>
          
          <p class="font-body text-lg md:text-xl text-white/85 leading-relaxed max-w-2xl animate-fade-in-left" style="animation-delay: 1.2s;">
            Specialized electrical engineering solutions across the entire spectrum of high- and extra-high-voltage substation infrastructure.
          </p>
          <p class="font-body text-sm md:text-base text-white/60 leading-relaxed max-w-2xl animate-fade-in-left" style="animation-delay: 1.4s;">
            Rigorous technical execution and commitment to the highest international standards for complex power transmission and substation projects.
          </p>
        </div>'''

    content_en = content_en.replace(old_paragraphs_en, new_paragraphs_en)

    with open('en/index.html', 'w', encoding='utf-8') as f:
        f.write(content_en)
    print("EN file successfully updated!")

if __name__ == "__main__":
    fix_files()
