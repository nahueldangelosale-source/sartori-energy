import os

def replace_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Head link (Add flag-icons css)
    content = content.replace(
        '<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800;900&family=Lato:wght@300;400;700&display=swap" rel="stylesheet">',
        '<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800;900&family=Lato:wght@300;400;700&display=swap" rel="stylesheet">\n  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/lipis/flag-icons@7.0.0/css/flag-icons.min.css"/>'
    )
    
    # 2. Logo image src & rounded
    content = content.replace(
        '<img src="assets/images/logo.jpg" alt="SARTORI Energy Logo" class="h-12 w-auto flex-shrink-0 rounded-sm">',
        '<img src="assets/images/logo.png" alt="SARTORI Energy Logo" class="h-12 w-auto flex-shrink-0">'
    ).replace(
        '<img src="../assets/images/logo.jpg" alt="SARTORI Energy Logo" class="h-12 w-auto flex-shrink-0 rounded-sm">',
        '<img src="../assets/images/logo.png" alt="SARTORI Energy Logo" class="h-12 w-auto flex-shrink-0">'
    )
    
    content = content.replace(
        '<img src="assets/images/logo.jpg" alt="SARTORI Energy Logo" class="h-10 w-auto flex-shrink-0 rounded-sm">',
        '<img src="assets/images/logo.png" alt="SARTORI Energy Logo" class="h-10 w-auto flex-shrink-0">'
    ).replace(
        '<img src="../assets/images/logo.jpg" alt="SARTORI Energy Logo" class="h-10 w-auto flex-shrink-0 rounded-sm">',
        '<img src="../assets/images/logo.png" alt="SARTORI Energy Logo" class="h-10 w-auto flex-shrink-0">'
    )

    # 3. Language switchers
    content = content.replace(
        '<span class="text-white font-body text-sm font-bold">🇪🇸 ES</span>',
        '<span class="text-white font-body text-sm font-bold"><span class="fi fi-es rounded-sm mr-1"></span> ES</span>'
    ).replace(
        '<span class="text-white font-body text-sm font-bold">🇬🇧 EN</span>',
        '<span class="text-white font-body text-sm font-bold"><span class="fi fi-gb rounded-sm mr-1"></span> EN</span>'
    )
    content = content.replace(
        '<a href="en/index.html" class="text-white/50 hover:text-white font-body text-sm transition-colors duration-200">🇬🇧 EN</a>',
        '<a href="en/index.html" class="text-white/50 hover:text-white font-body text-sm transition-colors duration-200"><span class="fi fi-gb rounded-sm mr-1 opacity-50"></span> EN</a>'
    ).replace(
        '<a href="../index.html" class="text-white/50 hover:text-white font-body text-sm transition-colors duration-200">🇪🇸 ES</a>',
        '<a href="../index.html" class="text-white/50 hover:text-white font-body text-sm transition-colors duration-200"><span class="fi fi-es rounded-sm mr-1 opacity-50"></span> ES</a>'
    )
    content = content.replace(
        '<span class="text-white font-body font-bold">🇪🇸 ES</span>',
        '<span class="text-white font-body font-bold"><span class="fi fi-es rounded-sm mr-1"></span> ES</span>'
    ).replace(
        '<span class="text-white font-body font-bold">🇬🇧 EN</span>',
        '<span class="text-white font-body font-bold"><span class="fi fi-gb rounded-sm mr-1"></span> EN</span>'
    ).replace(
        '<a href="en/index.html" class="text-white/50 hover:text-white font-body">🇬🇧 EN</a>',
        '<a href="en/index.html" class="text-white/50 hover:text-white font-body"><span class="fi fi-gb rounded-sm mr-1 opacity-50"></span> EN</a>'
    ).replace(
        '<a href="../index.html" class="text-white/50 hover:text-white font-body">🇪🇸 ES</a>',
        '<a href="../index.html" class="text-white/50 hover:text-white font-body"><span class="fi fi-es rounded-sm mr-1 opacity-50"></span> ES</a>'
    )
    content = content.replace(
        '<span class="font-body text-xs text-white/60 font-bold">🇪🇸 Español</span>',
        '<span class="font-body text-xs text-white/60 font-bold"><span class="fi fi-es rounded-sm mr-1"></span> Español</span>'
    ).replace(
        '<span class="font-body text-xs text-white/60 font-bold">🇬🇧 English</span>',
        '<span class="font-body text-xs text-white/60 font-bold"><span class="fi fi-gb rounded-sm mr-1"></span> English</span>'
    ).replace(
        '<a href="en/index.html" class="font-body text-xs text-white/30 hover:text-white transition-colors">🇬🇧 English</a>',
        '<a href="en/index.html" class="font-body text-xs text-white/30 hover:text-white transition-colors"><span class="fi fi-gb rounded-sm mr-1 opacity-50"></span> English</a>'
    ).replace(
        '<a href="../index.html" class="font-body text-xs text-white/30 hover:text-white transition-colors">🇪🇸 Español</a>',
        '<a href="../index.html" class="font-body text-xs text-white/30 hover:text-white transition-colors"><span class="fi fi-es rounded-sm mr-1 opacity-50"></span> Español</a>'
    )

    # 4. Project Filters
    content = content.replace('🇨🇱 Chile', '<span class="fi fi-cl rounded-sm mr-1 shadow-sm"></span> Chile')
    content = content.replace('🇨🇴 Colombia', '<span class="fi fi-co rounded-sm mr-1 shadow-sm"></span> Colombia')
    content = content.replace('🇦🇷 Argentina', '<span class="fi fi-ar rounded-sm mr-1 shadow-sm"></span> Argentina')
    
    # 5. Project Table Badges
    content = content.replace('<span class="badge-chile text-xs font-heading font-bold px-2 py-0.5 rounded mr-1.5">CL</span>', '<span class="fi fi-cl border border-gray-200 rounded-sm mr-1.5 text-base shadow-sm"></span>')
    content = content.replace('<span class="badge-colombia text-xs font-heading font-bold px-2 py-0.5 rounded mr-1.5">CO</span>', '<span class="fi fi-co border border-gray-200 rounded-sm mr-1.5 text-base shadow-sm"></span>')
    content = content.replace('<span class="badge-argentina text-xs font-heading font-bold px-2 py-0.5 rounded mr-1.5">AR</span>', '<span class="fi fi-ar border border-gray-200 rounded-sm mr-1.5 text-base shadow-sm"></span>')
    content = content.replace('<span class="badge-chile text-xs font-heading font-bold px-2 py-0.5 rounded">CL</span>', '<span class="fi fi-cl border border-gray-200 rounded-sm text-base shadow-sm"></span>')
    content = content.replace('<span class="badge-colombia text-xs font-heading font-bold px-2 py-0.5 rounded">CO</span>', '<span class="fi fi-co border border-gray-200 rounded-sm text-base shadow-sm"></span>')
    content = content.replace('<span class="badge-argentina text-xs font-heading font-bold px-2 py-0.5 rounded">AR</span>', '<span class="fi fi-ar border border-gray-200 rounded-sm text-base shadow-sm"></span>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

replace_in_file('index.html')
replace_in_file('en/index.html')
print("Changes applied!")
