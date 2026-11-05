import os
import urllib.request

img_dir = "real_estate_site/static/images"
os.makedirs(img_dir, exist_ok=True)

# Wikimedia Commons public domain / CC-licensed direct image links guaranteed to load without hotlink blocking
images = {
    "prop1.jpg": "https://upload.wikimedia.org/wikipedia/commons/e/e6/Home_construction.jpg",
    "prop2.jpg": "https://upload.wikimedia.org/wikipedia/commons/1/1a/Modern_building_facade.jpg",
    "prop3.jpg": "https://upload.wikimedia.org/wikipedia/commons/5/5f/House_in_Berkeley.jpg",
    "prop4.jpg": "https://upload.wikimedia.org/wikipedia/commons/8/88/Contemporary_house.jpg",
    "prop5.jpg": "https://upload.wikimedia.org/wikipedia/commons/c/c5/Modern_house_near_Seattle.jpg",
    "prop6.jpg": "https://upload.wikimedia.org/wikipedia/commons/7/74/A_modern_house_design.jpg",
    "prop7.jpg": "https://upload.wikimedia.org/wikipedia/commons/3/36/Typical_house.jpg",
    "prop8.jpg": "https://upload.wikimedia.org/wikipedia/commons/9/9e/Residential_house_in_Kista.jpg",
    "prop9.jpg": "https://upload.wikimedia.org/wikipedia/commons/d/d4/House-in-Nagoya.jpg",
    "prop10.jpg": "https://upload.wikimedia.org/wikipedia/commons/4/4c/Suburban_house_in_Solna.jpg",
    "hero_bg.jpg": "https://upload.wikimedia.org/wikipedia/commons/1/1a/Modern_building_facade.jpg"
}

headers = {'User-Agent': 'Mozilla/5.0'}
for filename, url in images.items():
    filepath = os.path.join(img_dir, filename)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response, open(filepath, 'wb') as out_file:
            out_file.write(response.read())
        print(f"Successfully downloaded {filename}")
    except Exception as e:
        print(f"Failed {filename}: {e}")
        # Create a simple SVG-based placeholder image if download fails
        svg_fallback = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="800" height="600">
            <defs>
                <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" style="stop-color:#2b7a78;stop-opacity:1" />
                    <stop offset="100%" style="stop-color:#3aafa9;stop-opacity:1" />
                </linearGradient>
            </defs>
            <rect width="800" height="600" fill="url(#grad)" />
            <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" fill="#ffffff" font-family="Arial, sans-serif" font-size="32" font-weight="bold">LuxeEstate Property</text>
        </svg>'''
        with open(filepath.replace('.jpg', '.svg'), 'w') as f:
            f.write(svg_fallback)
