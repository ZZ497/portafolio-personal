import re
import os

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
    "Git": "github",  # maps "Git & GitHub" to github icon
    "Docker": "docker",
    "Android": "androidstudio" # maps "Android Studio" to androidstudio icon
}

sources = {}
# simple icon paths
for name, icon_id in icons.items():
    if os.path.exists(f"{icon_id}.txt"):
        with open(f"{icon_id}.txt") as f:
            sources[name] = {"type": "path", "content": f.read().strip()}
    elif os.path.exists(f"{icon_id}_full.svg"):
        with open(f"{icon_id}_full.svg") as f:
            content = f.read().strip()
            # extract inner HTML of devicon SVG
            inner = content[content.find('>')+1:content.rfind('</svg>')]
            # extract viewBox
            vb_match = re.search(r'viewBox="([^"]+)"', content)
            vb = vb_match.group(1) if vb_match else "0 0 128 128"
            sources[name] = {"type": "full", "inner": inner, "vb": vb}

with open("index.html", "r") as f:
    html = f.read()

def replacer(match):
    full_str = match.group(0)
    svg_open = match.group(1)
    cls = match.group(2)
    svg_close_space = match.group(3)
    span_tag = match.group(4)
    name_text = match.group(5)
    
    key = None
    for k in icons.keys():
        if k in name_text:
            key = k
            break
            
    if not key or key not in sources:
        return full_str
        
    src = sources[key]
    
    if src["type"] == "path":
        # build simpleicon svg
        new_svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="currentColor" class="{cls}"><path d="{src["content"]}"/></svg>'
    else:
        # build devicon svg
        new_svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="{src["vb"]}" class="{cls}">{src["inner"]}</svg>'
        
    print(f"Replaced {key} (found as '{name_text}')")
    return new_svg + svg_close_space.replace("</svg>", "") + span_tag

# (?!</svg>) ensures we do not match across multiple SVG tags if the span is not immediately following
pattern = r'(<svg[^>]*?class="([^"]*?)"[^>]*?>)(?:(?!</svg>).)*?(</svg>\s*)(<span class="font-medium text-slate-700">([^<]+)</span>)'
new_html = re.sub(pattern, replacer, html, flags=re.DOTALL)

with open("index.html", "w") as f:
    f.write(new_html)
