from flask import Flask, jsonify, request

app = Flask(__name__)

# Almacenamiento de usuarios en memoria
users = {}

# Ruta principal


@app.route("/")
def home():
    return "Welcome to the Flask API!"

# Ruta para devolver los nombres de usuario


@app.route("/data")
def get_usernames():
    return jsonify(list(users.keys()))

# Ruta para verificar el estado


@app.route("/status")
def status():
    return "OK"

# Ruta para obtener detalles de un usuario


@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Ruta para agregar un nuevo usuario


@app.route("/add_user", methods=["POST"])
def add_user():
    new_user = request.json
    username = new_user.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username == users:
        return jsonify({"error": "User already exists"}), 400
    users[username] = new_user
    return jsonify({"message": "User added", "user": new_user}), 201


if __name__ == "__main__":
    app.run()
