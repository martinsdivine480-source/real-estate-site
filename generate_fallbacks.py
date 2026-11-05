import os

img_dir = "real_estate_site/static/images"
os.makedirs(img_dir, exist_ok=True)

svg_fallback = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="800" height="600">
    <defs>
        <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#17252a;stop-opacity:1" />
            <stop offset="50%" style="stop-color:#2b7a78;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#3aafa9;stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect width="800" height="600" fill="url(#grad)" />
    <!-- House icon -->
    <path d="M400 150 L600 300 L550 300 L550 480 L250 480 L250 300 L200 300 Z" fill="none" stroke="#ffffff" stroke-width="12" stroke-linejoin="round" />
    <rect x="350" y="360" width="100" height="120" fill="#ffffff" rx="6" />
    <text x="50%" y="530" dominant-baseline="middle" text-anchor="middle" fill="#ffffff" font-family="'Segoe UI', Arial, sans-serif" font-size="28" font-weight="bold" letter-spacing="2">LUXEESTATE PROPERTY</text>
</svg>'''

for i in range(1, 11):
    path = os.path.join(img_dir, f"prop{i}.jpg")
    with open(path, 'w', encoding='utf-8') as f:
        f.write(svg_fallback)

hero_path = os.path.join(img_dir, "hero_bg.jpg")
with open(hero_path, 'w', encoding='utf-8') as f:
    f.write(svg_fallback)

print("All image placeholders generated successfully.")
