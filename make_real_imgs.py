import os

img_dir = "real_estate_site/static/images"
os.makedirs(img_dir, exist_ok=True)

# Generate simple valid JPEG-like or PNG files for 1-10 and hero
# Using a python script that writes a small valid BMP or PNG or colored SVG embedded in HTML if needed,
# but standard 1x1 or 300x200 PNG bytes:
png_bytes = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\xc8\x00\x00\x00d\x08\x02\x00\x00\x00\x16\xcc\xbf\xb7\x00\x00\x00\x0cIDATx\x9cc\xf8\xff\xff?\x03\x01\x01\x01\x00\x18\xdd\x8d\xb0\x00\x00\x00\x00IEND\xaeB`\x82'

for i in range(1, 11):
    with open(os.path.join(img_dir, f"prop{i}.jpg"), "wb") as f:
        f.write(png_bytes)
    with open(os.path.join(img_dir, f"prop{i}.png"), "wb") as f:
        f.write(png_bytes)

with open(os.path.join(img_dir, "hero.jpg"), "wb") as f:
    f.write(png_bytes)
with open(os.path.join(img_dir, "hero.png"), "wb") as f:
    f.write(png_bytes)

print("Images generated successfully.")
