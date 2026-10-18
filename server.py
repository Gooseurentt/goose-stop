import os
from flask import Flask, jsonify, request

app = Flask(__name__)
ENABLED = True
ADMIN_KEY = os.environ.get("ADMIN_KEY", "CHANGE_ME")

@app.route("/check")
def check():
    return jsonify(ok=ENABLED)

@app.route("/set/<int:val>", methods=["GET", "POST"])
def set_enabled(val):
    key = request.args.get("key") or request.headers.get("X-Admin-Key")
    if key != ADMIN_KEY:
        return jsonify(error="forbidden"), 403
    global ENABLED
    ENABLED = bool(val)
    return jsonify(enabled=ENABLED)

@app.route("/status")
def status():
    return jsonify(enabled=ENABLED)

@app.route("/")
def root():
    return "Goose stop server OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
