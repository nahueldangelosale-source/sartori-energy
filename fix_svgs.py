import re

def remove_svg(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    pattern = r'<div class="absolute bottom-4 right-4 w-12 h-12 flex items-center justify-center rounded-xl bg-white/95 text-sartori-teal shadow-md">\s*<svg.*?</svg>\s*</div>'
    
    new_content, count = re.subn(pattern, '', content, flags=re.DOTALL)
    print(f"Removed {count} SVGs from {filename}")
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)

remove_svg('index.html')
remove_svg('es/index.html')
