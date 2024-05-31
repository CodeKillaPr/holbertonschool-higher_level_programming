from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user data store
users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    return jsonify(list(users.values()))


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return "User not found", 404


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.json
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


@app.route("/delete_user/<username>", methods=["DELETE"])
def delete_user(username):
    if username in users:
        del users[username]
        return jsonify({"message": "User deleted"}), 200
    else:
        return "User not found", 404


if __name__ == "__main__":
    app.run(debug=True)
