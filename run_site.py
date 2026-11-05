import subprocess
import os

print("Current working directory:", os.getcwd())
venv_python = os.path.abspath("../venv/Scripts/python.exe")
print("Venv python path:", venv_python)
print("Exists?", os.path.exists(venv_python))

if os.path.exists(venv_python):
    subprocess.run([venv_python, "app.py"])
else:
    print("Virtual environment not found at parent. Running with system python:")
    subprocess.run(["python", "app.py"])
