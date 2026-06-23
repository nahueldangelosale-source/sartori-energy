import os
import re
from PIL import Image

def optimize_images():
    images_dir = "assets/images"
    print("Optimizing images...")
    for filename in os.listdir(images_dir):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            filepath = os.path.join(images_dir, filename)
            
            # Skip the logos
            if "logo" in filename.lower():
                continue
                
            try:
                img = Image.open(filepath)
                orig_size = os.path.getsize(filepath)
                
                # Resize based on image name/type
                if "servicio" in filename.lower():
                    # Cards need 600px width max
                    img.thumbnail((600, 600))
                elif "fondo" in filename.lower() or "relleno" in filename.lower():
                    # Backgrounds can be 1600px width max
                    img.thumbnail((1600, 1600))
                elif "proyecto" in filename.lower():
                    # Projects 800px max
                    img.thumbnail((800, 800))
                else:
                    img.thumbnail((1000, 1000))
                    
                # Save optimized JPEG
                img.convert("RGB").save(filepath, "JPEG", quality=80, progressive=True)
                new_size = os.path.getsize(filepath)
                print(f"Compressed {filename}: {orig_size/1024/1024:.2f}MB -> {new_size/1024:.1f}KB")
            except Exception as e:
                print(f"Error compressing {filename}: {e}")

def fix_html_files():
    print("\nFixing HTML files...")
    
    def fix_file(filepath, is_en=False):
        prefix = "../" if is_en else ""
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 1. Fix SARTORI Energy H1 size to prevent wrapping and look sleeker
        # Reduce from text-6xl/7xl/8xl to text-3xl/4xl/5xl/6xl
        content = content.replace(
            f'class="font-heading font-black text-4xl sm:text-5xl md:text-6xl lg:text-6xl xl:text-7xl text-white tracking-tighter animate-tracking-expand whitespace-nowrap"',
            f'class="font-heading font-black text-3xl sm:text-4xl md:text-5xl lg:text-5xl xl:text-6xl text-white tracking-tighter animate-tracking-expand whitespace-nowrap"'
        )
        
        # 2. Update tagline content and translation
        if is_en:
            # English tagline
            content = content.replace(
                f'<p class="mt-5 font-serif italic text-lg md:text-xl lg:text-2xl text-sartori-teal-light tracking-wide animate-fade-in-delayed" style="text-shadow: 0 2px 10px rgba(0,7,45,0.6);">\n          "Your energy project, <span class="text-sartori-amber font-semibold">our mission</span>"\n        </p>',
                f'<p class="mt-5 font-serif italic text-lg md:text-xl lg:text-2xl text-sartori-teal-light tracking-wide animate-fade-in-delayed" style="text-shadow: 0 2px 10px rgba(0,7,45,0.6);">\n          "Your energy project, <span class="text-sartori-amber font-semibold">our mission</span>"\n        </p>'
            )
        else:
            # Spanish tagline (Translate!)
            content = content.replace(
                f'<p class="mt-5 font-serif italic text-lg md:text-xl lg:text-2xl text-sartori-teal-light tracking-wide animate-fade-in-delayed" style="text-shadow: 0 2px 10px rgba(0,7,45,0.6);">\n          "Your energy project, <span class="text-sartori-amber font-semibold">our mission</span>"\n        </p>',
                f'<p class="mt-5 font-serif italic text-lg md:text-xl lg:text-2xl text-sartori-teal-light tracking-wide animate-fade-in-delayed" style="text-shadow: 0 2px 10px rgba(0,7,45,0.6);">\n          "Su proyecto de energía, <span class="text-sartori-amber font-semibold">nuestra misión</span>"\n        </p>'
            )
            
        # 3. Logo Watermark re-positioning: Move to the Right, set z-10 for absolute visibility, and adjust opacity to 10%
        old_watermark_div = f'''    <!-- Large Logo Watermark on the Left (Sober & Static) -->
    <div class="absolute left-[3%] lg:left-[5%] top-[18%] w-[160px] lg:w-[200px] opacity-[0.06] hidden md:block pointer-events-none z-0 select-none">
      <img src="{prefix}assets/images/logo.png" alt="Sartori Logo Watermark" class="w-full h-auto filter brightness-125 contrast-125">
    </div>'''

        new_watermark_div = f'''    <!-- Large Logo Watermark on the Right (Sober & Static) -->
    <div class="absolute right-[6%] lg:right-[8%] top-[25%] w-[180px] lg:w-[240px] opacity-[0.1] hidden md:block pointer-events-none z-10 select-none">
      <img src="{prefix}assets/images/logo.png" alt="Sartori Logo Watermark" class="w-full h-auto">
    </div>'''
        
        content = content.replace(old_watermark_div, new_watermark_div)
        
        # 4. Remove backslash escapes in JS template literals (\\${{data.desc}} -> ${{data.desc}} and \\${{item}} -> ${{item}})
        content = content.replace('\\${data.desc}', '${data.desc}')
        content = content.replace('\\${item}', '${item}')
        
        # 5. Fix smooth scroll navigation issues if any, or verify.
        # Let's write the modifications back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {filepath}")

if __name__ == "__main__":
    optimize_images()
    fix_html_files()
