import os
import sys

os.chdir("real_estate_site")
try:
    import app
    print("App imports successfully!")
except Exception as e:
    print(f"Import error: {e}")
    sys.exit(1)
