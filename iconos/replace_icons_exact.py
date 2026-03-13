import os

# We will literally just string.replace the EXACT known blocks from the original index.html
icons = {
    "HTML": {"filename": "html5.txt", "color": "text-orange-600"},
    "CSS": {"filename": "css3_full.svg", "color": "text-blue-600"},
    "JavaScript": {"filename": "javascript.txt", "color": "text-yellow-500"},
    "Figma": {"filename": "figma.txt", "color": "text-purple-500"},
    "PHP": {"filename": "php.txt", "color": "text-indigo-600"},
    "Java": {"filename": "java_full.svg", "color": "text-red-600"},
    "MySQL": {"filename": "mysql.txt", "color": "text-cyan-600"},
    "Laravel": {"filename": "laravel.txt", "color": "text-red-600"},
    "Symfony": {"filename": "symfony.txt", "color": "text-slate-800"},
    "Kotlin": {"filename": "kotlin.txt", "color": "text-purple-600"},
    "Swift": {"filename": "swift.txt", "color": "text-orange-500"},
    "Git & GitHub": {"filename": "github.txt", "color": "text-gray-600"},
    "Docker": {"filename": "docker.txt", "color": "text-blue-600"},
    "Android Studio": {"filename": "androidstudio.txt", "color": "text-green-600"}
}

with open("index.html", "r") as f:
    html = f.read()

for name, info in icons.items():
    if not os.path.exists(info["filename"]):
        continue
    
    with open(info["filename"], "r") as f:
        content = f.read().strip()
        
    span_str = f'<span class="font-medium text-slate-700">{name}</span>'
    idx_span = html.find(span_str)
    if idx_span == -1:
        print(f"Could not find span for {name}")
        continue
        
    idx_svg_end = html.rfind('</svg>', 0, idx_span)
    idx_svg_start = html.rfind('<svg', 0, idx_svg_end)
    
    if idx_svg_start == -1 or idx_svg_end == -1:
        print(f"Could not find SVG tags for {name}")
        continue
        
    orig_block = html[idx_svg_start:idx_svg_end+6]
    
    if info["filename"].endswith(".svg"):
        # it's a devicon with full svg
        inner = content[content.find('>')+1:content.rfind('</svg>')]
        # extract viewBox
        vb_start = content.find('viewBox="')
        vb_end = content.find('"', vb_start + 9)
        vb = content[vb_start:vb_end+1] if vb_start != -1 else 'viewBox="0 0 128 128"'
        new_svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" {vb} class="{info["color"]}">{inner}</svg>'
    else:
        # standard simpleicon path
        new_svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="currentColor" class="{info["color"]}"><path d="{content}"/></svg>'
        
    html = html[:idx_svg_start] + new_svg + html[idx_svg_end+6:]
    print(f"Replaced exactly for {name}")

with open("index.html", "w") as f:
    f.write(html)
