import sys
import os

os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app import app

if __name__ == '__main__':
    print("Starting Flask application...")
    app.run(debug=True, port=5000)
