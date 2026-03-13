import urllib.request
import re

icons = [
    "html5", "css3", "javascript", "figma", "php", "java", "mysql", 
    "laravel", "symfony", "kotlin", "swift", "github", "git", "docker", "androidstudio"
]

for icon in icons:
    try:
        url = f"https://cdn.simpleicons.org/{icon}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        svg_content = response.read().decode('utf-8')
        match = re.search(r'<path[^>]*d="([^"]+)"', svg_content)
        if match:
            with open(f"/Users/dam1/Documents/portafolio-personal/{icon}.txt", "w") as f:
                f.write(match.group(1))
            print(f"Got {icon}")
        else:
            print(f"No path found for {icon}")
    except Exception as e:
        print(f"Error fetching {icon}: {e}")
