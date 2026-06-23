def move_logo():
    # 1. Spanish version
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Move watermark from right side to left side, set z-0 so it's behind text, and lower opacity to 5% so it doesn't affect readability
    old_watermark = '''    <!-- Large Logo Watermark on the Right (Pure White & z-20) -->
    <div class="absolute right-[6%] lg:right-[8%] top-[28%] w-[180px] lg:w-[240px] hidden md:block pointer-events-none z-20 select-none" style="opacity: 0.14;">
      <img src="assets/images/logo.png" alt="Sartori Logo Watermark" class="w-full h-auto" style="filter: brightness(0) invert(1);">
    </div>'''

    new_watermark = '''    <!-- Large Logo Watermark on the Left (Pure White Watermark behind text, z-0) -->
    <div class="absolute left-[6%] lg:left-[8%] top-[28%] w-[180px] lg:w-[240px] hidden md:block pointer-events-none z-0 select-none" style="opacity: 0.055;">
      <img src="assets/images/logo.png" alt="Sartori Logo Watermark" class="w-full h-auto" style="filter: brightness(0) invert(1);">
    </div>'''

    content = content.replace(old_watermark, new_watermark)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("ES watermark moved left!")

    # 2. English version
    with open('en/index.html', 'r', encoding='utf-8') as f:
        content_en = f.read()

    old_watermark_en = '''    <!-- Large Logo Watermark on the Right (Pure White & z-20) -->
    <div class="absolute right-[6%] lg:right-[8%] top-[28%] w-[180px] lg:w-[240px] hidden md:block pointer-events-none z-20 select-none" style="opacity: 0.14;">
      <img src="../assets/images/logo.png" alt="Sartori Logo Watermark" class="w-full h-auto" style="filter: brightness(0) invert(1);">
    </div>'''

    new_watermark_en = '''    <!-- Large Logo Watermark on the Left (Pure White Watermark behind text, z-0) -->
    <div class="absolute left-[6%] lg:left-[8%] top-[28%] w-[180px] lg:w-[240px] hidden md:block pointer-events-none z-0 select-none" style="opacity: 0.055;">
      <img src="../assets/images/logo.png" alt="Sartori Logo Watermark" class="w-full h-auto" style="filter: brightness(0) invert(1);">
    </div>'''

    content_en = content_en.replace(old_watermark_en, new_watermark_en)
    
    with open('en/index.html', 'w', encoding='utf-8') as f:
        f.write(content_en)
    print("EN watermark moved left!")

if __name__ == "__main__":
    move_logo()
