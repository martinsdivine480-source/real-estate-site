import os

img_dir = "real_estate_site/static/images"
os.makedirs(img_dir, exist_ok=True)

# Generate distinct realistic photo-like SVG illustrations with rich colors for all 10 properties
styles = [
    ("#1a365d", "#2b6cb0", "#2f855a", "Modern Glass Villa", "$2,450,000"),
    ("#2c3e50", "#4ca1af", "#27ae60", "Contemporary Urban Penthouse", "$1,850,000"),
    ("#7f8c8d", "#bdc3c7", "#27ae60", "Serene Suburban Family Home", "$920,000"),
    ("#0f2027", "#203a43", "#134e5e", "Minimalist Architectural Haven", "$3,100,000"),
    ("#3e5151", "#decba4", "#2c5e1a", "Lakeside Luxury Estate", "$2,750,000"),
    ("#232526", "#414345", "#1e5128", "Classic Luxury Mansion", "$3,890,000"),
    ("#870000", "#190a05", "#d4af37", "Sunset Horizon Villa", "$1,650,000"),
    ("#373b44", "#4286f4", "#2b580c", "Coastal Cliffside Retreat", "$4,200,000"),
    ("#2c3e50", "#3498db", "#bdc3c7", "Alpine Ski Chalet", "$3,400,000"),
    ("#4b6cb7", "#182848", "#2c3e50", "Historic Brownstone Elegance", "$2,100,000")
]

for i, (c1, c2, c3, title, price) in enumerate(styles, start=1):
    svg_code = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="100%" height="100%">
  <defs>
    <linearGradient id="bg{i}" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{c1}"/>
      <stop offset="100%" stop-color="{c2}"/>
    </linearGradient>
    <linearGradient id="roof{i}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#111111"/>
      <stop offset="100%" stop-color="#333333"/>
    </linearGradient>
  </defs>
  <!-- Sky background -->
  <rect width="800" height="600" fill="url(#bg{i})"/>
  <!-- Decorative sun/glow -->
  <circle cx="680" cy="120" r="50" fill="#fff" opacity="0.15"/>
  <!-- Ground -->
  <rect y="440" width="800" height="160" fill="{c3}"/>
  
  <!-- Modern architectural house body -->
  <rect x="180" y="200" width="440" height="260" fill="#f8f9fa" rx="12"/>
  <polygon points="140,200 400,80 660,200" fill="url(#roof{i})"/>
  
  <!-- Large glass windows / panels -->
  <rect x="220" y="240" width="100" height="140" fill="#00d2ff" opacity="0.7" rx="6"/>
  <rect x="480" y="240" width="100" height="140" fill="#00d2ff" opacity="0.7" rx="6"/>
  
  <!-- Door -->
  <rect x="360" y="320" width="80" height="140" fill="#5c4033" rx="4"/>
  <circle cx="420" cy="390" r="6" fill="#ffd700"/>
  
  <!-- Property Title & Price Overlay -->
  <rect x="40" y="40" width="720" height="70" fill="#000000" opacity="0.65" rx="12"/>
  <text x="65" y="85" fill="#ffffff" font-family="'Segoe UI', Arial, sans-serif" font-size="28" font-weight="bold">{title}</text>
  <text x="650" y="85" fill="#ffd700" font-family="'Segoe UI', Arial, sans-serif" font-size="24" font-weight="bold" text-anchor="end">{price}</text>
</svg>'''
    
    # Save as SVG
    svg_path = os.path.join(img_dir, f"prop{i}.svg")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_code)

print("All 10 property SVGs regenerated successfully!")
