from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Backend logic adapted from your original Contact Book code.
# Contacts are stored in memory, so they reset when the server stops.
contacts = {}

def add_contact(name, phone_no):
    if name in contacts:
        return False, "Name is already present."
    contacts[name] = phone_no
    return True, "Contact added successfully."

def search_contact(name):
    if not contacts:
        return None, "Contact list is empty."
    if name in contacts:
        return {"name": name, "phone_no": contacts[name]}, None
    return None, f"{name} not found."

def update_contact_no(name, new_contact_no):
    if not contacts:
        return False, "Contact list is empty."
    if name not in contacts:
        return False, "Name not found."
    contacts[name] = new_contact_no
    return True, "Contact number updated successfully."

def delete_contact(name):
    if not contacts:
        return False, "Contact list is empty."
    if name not in contacts:
        return False, "Contact not found."
    del contacts[name]
    return True, "Contact deleted successfully."

def display_contacts():
    return [{"name": name, "phone_no": contacts[name]} for name in sorted(contacts)]

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/api/contacts")
def get_contacts():
    return jsonify(display_contacts())

@app.post("/api/contacts")
def create_contact():
    data = request.get_json(silent=True) or {}
    name = (data.get("name") or "").strip()
    phone_no = (data.get("phone_no") or "").strip()
    if not name or not phone_no:
        return jsonify(message="Please enter both a name and phone number."), 400
    ok, message = add_contact(name, phone_no)
    return jsonify(message=message), (201 if ok else 409)

@app.get("/api/contacts/<path:name>")
def get_contact(name):
    contact, error = search_contact(name)
    if error:
        return jsonify(message=error), (400 if not contacts else 404)
    return jsonify(contact)

@app.put("/api/contacts/<path:name>")
def update_contact(name):
    data = request.get_json(silent=True) or {}
    new_phone_no = (data.get("phone_no") or "").strip()
    if not new_phone_no:
        return jsonify(message="Please enter a new phone number."), 400
    ok, message = update_contact_no(name, new_phone_no)
    return jsonify(message=message), (200 if ok else 404)

@app.delete("/api/contacts/<path:name>")
def remove_contact(name):
    ok, message = delete_contact(name)
    return jsonify(message=message), (200 if ok else 404)

if __name__ == "__main__":
    app.run(debug=True)
