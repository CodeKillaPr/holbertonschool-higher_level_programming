from flask import Flask, jsonify, request

app = Flask(__name__)

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
    username = data["username"]
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


@app.route("/delete_user/<username>", methods=["DELETE"])
def test_get_user_not_found():
    response = app.test_client().get("/users/doesnotexist")
    assert response.status_code == 404
    assert response.get_json() == "User not found"


if __name__ == "__main__":
    app.run(debug=True)
