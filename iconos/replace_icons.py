import re

# Read SVG paths
icons = {
    "HTML": "html5",
    "CSS": "css3",
    "JavaScript": "javascript",
    "Figma": "figma",
    "PHP": "php",
    "Java": "java",
    "MySQL": "mysql",
    "Laravel": "laravel",
    "Symfony": "symfony",
    "Kotlin": "kotlin",
    "Swift": "swift",
    "Git & GitHub": "github",
    "Docker": "docker",
    "Android Studio": "androidstudio"
}

paths = {}
for name, file in icons.items():
    try:
        with open(f"/Users/dam1/Documents/portafolio-personal/{file}.txt", "r") as f:
            paths[name] = f.read().strip()
    except:
        paths[name] = None

# Read index.html
with open("/Users/dam1/Documents/portafolio-personal/index.html", "r") as f:
    html = f.read()

# For each icon name, find the block:
# <svg ...> ... </svg>\n\s*<span class="font-medium text-slate-700">NAME</span>
# We'll use regex to carefully replace just the SVG's inner content (or the whole SVG tag) with the new path
# But keep the class!

for name, path in paths.items():
    if not path:
        print(f"Skipping {name}, no path")
        continue

    # Find the SVG + Name
    pattern = r'(<svg[^>]*class="([^"]*)"[^>]*>).*?(</svg>\s*<span class="font-medium text-slate-700">{}</span>)'.format(re.escape(name))
    
    def replacer(match):
        svg_open = match.group(1)
        classes = match.group(2)
        svg_close_and_span = match.group(3)
        
        # Rewrite the svg open tag to ensure viewBox="0 0 24 24" and fill="currentColor"
        # Since simpleicons paths assume 0 0 24 24.
        new_svg_open = f'<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="currentColor" class="{classes}">'
        # We need to make sure we don't duplicate fill and we use fill instead of stroke for simpleicons
        new_path = f'<path d="{path}" />'
        
        return new_svg_open + new_path + svg_close_and_span

    html, count = re.subn(pattern, replacer, html, flags=re.DOTALL)
    if count > 0:
        print(f"Replaced {name}")
    else:
        print(f"Could not find {name} in html")

with open("/Users/dam1/Documents/portafolio-personal/index.html", "w") as f:
    f.write(html)
