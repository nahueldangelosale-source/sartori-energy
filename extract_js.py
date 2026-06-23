with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
scripts = re.findall(r'<script>(.*?)</script>', content, re.DOTALL)
if scripts:
    with open('temp.js', 'w', encoding='utf-8') as tf:
        tf.write(scripts[-1])
    print("JS extracted to temp.js")
