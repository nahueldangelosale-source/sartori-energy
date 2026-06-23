import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('en/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('id="servicios"')
end = content.find('</section>', start)
print(content[start:end+10])
