
from PIL import Image, ImageDraw, ImageFont
import os

img_dir = "real_estate_site/static/images"
os.makedirs(img_dir, exist_ok=True)

images = ["hero.jpg"] + [f"prop{i}.jpg" for i in range(1, 11)]

colors = [
    (30, 41, 59), (15, 23, 42), (51, 65, 85), (30, 58, 138), 
    (19, 78, 74), (120, 53, 15), (88, 28, 135), (157, 23, 77),
    (67, 56, 202), (4, 120, 87), (180, 83, 9)
]

for idx, img_name in enumerate(images):
    img = Image.new('RGB', (800, 600), color=colors[idx % len(colors)])
    d = ImageDraw.Draw(img)
    # Draw a stylized house graphic
    d.rectangle([300, 350, 500, 550], fill=(241, 245, 249))
    d.polygon([(270, 350), (400, 200), (530, 350)], fill=(225, 29, 72))
    d.rectangle([370, 450, 430, 550], fill=(15, 23, 42))
    d.rectangle([320, 380, 370, 430], fill=(56, 189, 248))
    d.rectangle([430, 380, 480, 430], fill=(56, 189, 248))
    
    # Add text banner
    d.rectangle([150, 80, 650, 150], fill=(15, 23, 42))
    d.text((170, 100), f"LuxeEstate Luxury Property #{idx}" if idx > 0 else "LuxeEstate Exclusive Hero", fill=(255, 255, 255))
    
    img.save(os.path.join(img_dir, img_name), "JPEG")

print("Generated all property images successfully.")
