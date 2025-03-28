from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Lark Anonymous Bot is Running!"

@app.route("/message", methods=["POST"])
def receive_message():
    data = request.json
    user_message = data.get("text", "")

    # Hide sender and add an alias
    alias = data.get("alias", "Anonymous")
    anonymous_message = f"{alias}: {user_message}"

    # Send back the anonymous message
    return jsonify({"reply": anonymous_message})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
