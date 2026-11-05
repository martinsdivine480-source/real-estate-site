import os
import urllib.request
import zipfile
import subprocess
import sys
import webbrowser
import threading
import time
import app as flask_app

print("Downloading cloudflared for instant free public sharing...")

cf_path = "cloudflared.exe"
if not os.path.exists(cf_path):
    url = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe"
    try:
        print("Downloading Cloudflare Tunnel (cloudflared)...")
        urllib.request.urlretrieve(url, cf_path)
        print("Download complete!")
    except Exception as e:
        print(f"Download failed: {e}")

def run_flask():
    flask_app.app.run(port=5000, debug=False, use_reloader=False)

t = threading.Thread(target=run_flask, daemon=True)
t.start()
time.sleep(2)

print("\n" + "="*60)
print(" GENERATING YOUR PUBLIC SHAREABLE LINK...")
print("="*60 + "\n")

if os.path.exists(cf_path):
    try:
        # Run cloudflared tunnel
        subprocess.run([cf_path, "tunnel", "--url", "http://localhost:5000"])
    except Exception as e:
        print(f"Tunnel error: {e}")
else:
    print("Please run python app.py")

try:
    input("\nPress Enter to exit...\n")
except KeyboardInterrupt:
    pass
