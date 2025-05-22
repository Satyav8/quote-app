from flask import Flask, request, jsonify, send_from_directory
import json, os

app = Flask(__name__, static_folder="../frontend", static_url_path="/")
DATA_FILE = "quotes.json"

def load_quotes():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_quotes(quotes):
    with open(DATA_FILE, "w") as f:
        json.dump(quotes, f, indent=2)

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/api/quotes", methods=["GET"])
def get_quotes():
    return jsonify(load_quotes())

@app.route("/api/quotes", methods=["POST"])
def add_quote():
    data = request.get_json()
    quotes = load_quotes()
    quotes.append(data)
    save_quotes(quotes)
    return jsonify({"status": "added"}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0")
