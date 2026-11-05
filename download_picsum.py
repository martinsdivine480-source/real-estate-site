import os
import urllib.request
import json

img_dir = "real_estate_site/static/images"
os.makedirs(img_dir, exist_ok=True)

# Search Unsplash Source or Picsum Photos (which provides guaranteed random high-res architectural house photos)
# Unsplash source URL pattern: https://images.unsplash.com/photo-... or https://picsum.photos/800/600?random=1

for i in range(1, 11):
    dest = os.path.join(img_dir, f"prop{i}.jpg")
    url = f"https://picsum.photos/seed/realestate{i}/800/600"
    try:
        urllib.request.urlretrieve(url, dest)
        print(f"Downloaded prop{i}.jpg via Picsum")
    except Exception as e:
        print(f"Error downloading prop{i}.jpg: {e}")

# Also download hero background image
hero_dest = os.path.join(img_dir, "hero_bg.jpg")
try:
    urllib.request.urlretrieve("https://picsum.photos/seed/luxuryherohouse/1920/1080", hero_dest)
    print("Downloaded hero_bg.jpg")
except Exception as e:
    print(f"Error hero: {e}")
