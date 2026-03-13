import os

icons = {
    "HTML": "html5.txt",
    "CSS": "css3_full.svg",
    "JavaScript": "javascript.txt",
    "Figma": "figma.txt",
    "PHP": "php.txt",
    "Java": "java_full.svg",
    "MySQL": "mysql.txt",
    "Laravel": "laravel.txt",
    "Symfony": "symfony.txt",
    "Kotlin": "kotlin.txt",
    "Swift": "swift.txt",
    "Git & GitHub": "github.txt",
    "Docker": "docker.txt",
    "Android Studio": "androidstudio.txt"
}

paths = {}
for name, filename in icons.items():
    if os.path.exists(filename):
        with open(filename, "r") as f:
            paths[name] = f.read().strip()

with open("index.html", "r") as f:
    html = f.read()

for name, path_content in paths.items():
    if not path_content:
        continue
    
    # name is exactly what's in the span text
    span_str = f'<span class="font-medium text-slate-700">{name}</span>'
    
    idx_span = html.find(span_str)
    if idx_span == -1:
        # Some ampersands might be encoded or something. Let's try finding the name only
        print(f"Failed to find span for {name}")
        continue
        
    # Find the nearest <svg closing tag before the span
    idx_svg_close = html.rfind('</svg>', 0, idx_span)
    if idx_svg_close == -1:
        continue
        
    # Find the <svg opening tag for that closing tag
    idx_svg_open = html.rfind('<svg', 0, idx_svg_close)
    if idx_svg_open == -1:
        continue
        
    # The original SVG block is:
    orig_svg = html[idx_svg_open:idx_svg_close+6]
    
    # Extract the class from the orig_svg
    class_str = ""
    # find class="..."
    c_start = orig_svg.find('class="')
    if c_start != -1:
        c_end = orig_svg.find('"', c_start + 7)
        if c_end != -1:
            class_str = orig_svg[c_start:c_end+1]
            
    # For devicon full SVGs (like CSS and Java), we can inject the class into their <svg> root
    if filename.endswith(".svg"):
        # We replace the SVG tag attributes but keep its inner paths.
        # <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128">
        # Replace the opening <svg ...> with <svg width="18" height="18" class="..." viewBox="...">
        # or just add width/height/class and keep viewBox.
        vb_start = path_content.find('viewBox="')
        vb_end = path_content.find('"', vb_start + 9)
        vb = path_content[vb_start:vb_end+1] if vb_start != -1 else 'viewBox="0 0 128 128"'
        
        inner_content = path_content[path_content.find('>')+1:path_content.rfind('</svg>')]
        
        new_svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" {vb} {class_str}>{inner_content}</svg>'
    else:
        # for simpleicons, it's just a path. No need to fill since we use currentColor.
        new_svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="currentColor" {class_str}><path d="{path_content}"/></svg>'
        
    # Replace orig_svg in html
    html = html[:idx_svg_open] + new_svg + html[idx_svg_close+6:]
    print(f"Replaced {name}")
    
with open("index.html", "w") as f:
    f.write(html)
