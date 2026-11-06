import sys
import subprocess
import os

# Install requirements into the environment
os.chdir("real_estate_site")
subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
print("Dependencies installed successfully!")
