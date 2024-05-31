from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"}
}

# Root endpoint


@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Endpoint to return JSON data


@app.route('/data')
def get_data():
    usernames = list(users.keys())
    return jsonify(usernames)

# Endpoint to return status


@app.route('/status')
def status():
    return "OK"

# Endpoint to get user details by username


@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Endpoint to add a new user


@app.route('/add_user', methods=['POST'])
def add_user():
    if not request.json or 'username' not in request.json:
        return jsonify({"error": "Invalid data"}), 400

    username = request.json['username']
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    user_data = {
        "username": username,
        "name": request.json.get("name"),
        "age": request.json.get("age"),
        "city": request.json.get("city")
    }
    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201


# Run the development server
if __name__ == "__main__":
    app.run(debug=True, port=8000)
