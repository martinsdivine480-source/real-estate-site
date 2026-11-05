import os

img_dir = "real_estate_site/static/images"
os.makedirs(img_dir, exist_ok=True)

# Generate valid JPEG files using Python's built-in header + colorful gradient patterns
# Since browsers render images when given correct Content-Type or SVG/PNG/JPG bytes, 
# let's write valid PNG files (which are 100% reliable in all browsers) and update app.py to reference .png extensions.

for i in range(1, 11):
    png_path = os.path.join(img_dir, f"prop{i}.png")
    # A tiny 1x1 valid red/blue/dark PNG with a clean data structure or we can write SVG files and update app.py to use .svg
    # Wait, in the screenshot earlier, the images were missing because app.py had image: "prop1.svg" but style.css or img tag didn't display svg properly, OR because it looked for .jpg/.png.
    # Let's check what app.py has:
