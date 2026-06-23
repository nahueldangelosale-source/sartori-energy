def fix_files():
    # 1. Spanish translation of tagline in index.html
    # We will read index.html, replace the tagline with Spanish, reduce H1 size, and fix logo positioning
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace tagline with Spanish translation
    content = content.replace(
        '"Your energy project, <span class="text-sartori-amber font-semibold">our mission</span>"',
        '"Su proyecto de energía, <span class="text-sartori-amber font-semibold">nuestra misión</span>"'
    )
    
    # Reduce H1 font size to make it look sleeker and guarantee 1 line
    content = content.replace(
        'text-4xl sm:text-5xl md:text-6xl lg:text-6xl xl:text-7xl text-white tracking-tighter',
        'text-3xl sm:text-4xl md:text-5xl lg:text-5xl xl:text-6xl text-white tracking-tighter'
    )
    
    # Logo Watermark position fix (ensure z-10, right side, opacity 0.08, static, no brightness filter)
    old_watermark = '''    <!-- Large Logo Watermark on the Left (Sober & Static) -->
    <div class="absolute left-[3%] lg:left-[5%] top-[18%] w-[160px] lg:w-[200px] opacity-[0.06] hidden md:block pointer-events-none z-0 select-none">
      <img src="assets/images/logo.png" alt="Sartori Logo Watermark" class="w-full h-auto filter brightness-125 contrast-125">
    </div>'''
    
    new_watermark = '''    <!-- Large Logo Watermark on the Right (Sober & Static) -->
    <div class="absolute right-[8%] lg:right-[10%] top-[28%] w-[180px] lg:w-[240px] opacity-[0.09] hidden md:block pointer-events-none z-10 select-none">
      <img src="assets/images/logo.png" alt="Sartori Logo Watermark" class="w-full h-auto">
    </div>'''
    
    content = content.replace(old_watermark, new_watermark)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("ES file successfully fixed!")

    # 2. English version fixes
    with open('en/index.html', 'r', encoding='utf-8') as f:
        content_en = f.read()
        
    content_en = content_en.replace(
        'text-4xl sm:text-5xl md:text-6xl lg:text-6xl xl:text-7xl text-white tracking-tighter',
        'text-3xl sm:text-4xl md:text-5xl lg:text-5xl xl:text-6xl text-white tracking-tighter'
    )
    
    old_watermark_en = '''    <!-- Large Logo Watermark on the Left (Sober & Static) -->
    <div class="absolute left-[3%] lg:left-[5%] top-[18%] w-[160px] lg:w-[200px] opacity-[0.06] hidden md:block pointer-events-none z-0 select-none">
      <img src="../assets/images/logo.png" alt="Sartori Logo Watermark" class="w-full h-auto filter brightness-125 contrast-125">
    </div>'''
    
    new_watermark_en = '''    <!-- Large Logo Watermark on the Right (Sober & Static) -->
    <div class="absolute right-[8%] lg:right-[10%] top-[28%] w-[180px] lg:w-[240px] opacity-[0.09] hidden md:block pointer-events-none z-10 select-none">
      <img src="../assets/images/logo.png" alt="Sartori Logo Watermark" class="w-full h-auto">
    </div>'''
    
    content_en = content_en.replace(old_watermark_en, new_watermark_en)
    
    with open('en/index.html', 'w', encoding='utf-8') as f:
        f.write(content_en)
    print("EN file successfully fixed!")

if __name__ == "__main__":
    fix_files()
