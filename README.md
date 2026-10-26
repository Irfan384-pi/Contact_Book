# Contact Book Website

A responsive Contact Book website with an HTML/CSS/JavaScript frontend connected to a Flask API. The Python backend uses the same dictionary-based add, search, update, delete, and alphabetical display logic from your original project.

## Run locally
1. Install Python 3.
2. Open a terminal in this folder.
3. Install Flask: `python -m pip install flask`
4. Start the server: `python app.py`
5. Open `http://127.0.0.1:5000` in your browser.

## Files
- `app.py` — Python backend and Flask routes
- `templates/index.html` — website structure
- `static/style.css` — design and responsive layout
- `static/app.js` — frontend behavior and API requests

## Important
This learning version stores contacts in memory in a Python dictionary. Contacts are lost when the server stops. A later improvement is to use SQLite or JSON for persistent storage. It is intended for local learning, not production deployment.

Project under process 
