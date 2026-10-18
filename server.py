import os
from flask import Flask, jsonify, request

app = Flask(__name__)
VALID_KEYS = ["Gooseofffiii67_stop23"]

@app.route("/check_key", methods=["GET"])
def check_key():
    user_key = request.args.get("key", "")
    if user_key in VALID_KEYS:
        return jsonify(ok=True)
    return jsonify(ok=False)

@app.route("/", methods=["GET"])
def root():
    return "Key Server OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
