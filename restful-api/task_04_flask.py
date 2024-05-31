
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return "OK"


@app.route('/info')
def get_info():
    return jsonify({
        "version": "1.0",
        "description": "A simple API built with Flask"
    })


@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    user = request.get_json()

    if 'username' not in user:
        return jsonify({'error': 'No username provided'}), 400

    if user['username'] in users:
        return jsonify({'error': 'Username already exists'}), 400

    users[user['username']] = user

    return jsonify({'message': 'User added', 'user': user}), 201


@app.route("/<path:path>")
def undefined_endpoint(path):
    return jsonify({"error": "Endpoint not found"}), 404


if __name__ == "__main__":
    app.run()
