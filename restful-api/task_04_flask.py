from flask import Flask, request, jsonify, requests, BASE_URL
app = Flask(__name__)

users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}


def test_add_user_no_username():
    user = {"name": "John Doe", "email": "john@example.com"}
    response = requests.post(f"{BASE_URL}/add_user", json=user)
    assert response.status_code == 400
    assert response.json()[
        "error"] == "Username is required and must be unique"


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/data')
def get_usernames():
    return jsonify(list(users.keys()))


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
    data = request.get_json()
    username = data.get("username")
    if not username or username in users:
        return jsonify({"error": "Username is required and must be unique"}), 400

    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
