from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

def create_app():
    return app


users = {"admin": "1234"}

items = {
    1: {"name": "Laptop", "price": 1000, "color": "black"},
    2: {"name": "Phone", "price": 500, "color": "white"}
}

@auth.verify_password
def verify(username, password):
    if username in users and users[username] == password:
        return username

@app.route("/items", methods=["GET", "POST"])
@auth.login_required
def all_items():
    if request.method == "GET":
        return jsonify(items)

    if request.method == "POST":
        data = request.json
        new_id = max(items.keys()) + 1
        items[new_id] = data
        return jsonify({"status": "item added", "id": new_id})

@app.route("/items/<int:item_id>", methods=["GET", "PUT", "DELETE"])
@auth.login_required
def one_item(item_id):
    if item_id not in items:
        return jsonify({"error": "item not found"})

    if request.method == "GET":
        return jsonify(items[item_id])

    if request.method == "PUT":
        items[item_id] = request.json
        return jsonify({"status": "item updated"})

    if request.method == "DELETE":
        del items[item_id]
        return jsonify({"status": "item deleted"})

if __name__ == "__main__":
    app.run(port=8001, debug=True)
