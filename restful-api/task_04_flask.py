from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}
}


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route('/status')
def status():
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    if not request.json or 'username' not in request.json:
        return jsonify({"error": "Invalid data"}), 400

    username = request.json['username']
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    user_data = {
        "name": request.json.get("name"),
        "age": request.json.get("age"),
        "city": request.json.get("city")
    }
    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201


if __name__ == "__main__":
    app.run(debug=True)
