#!/usr/bin/python3

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}


@app.route("/")
def home():
    return "Welcome to the Flask API!."


@app.route("/data")
def data():
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def user_dict(username):
    if username in users:
        user = users[username]
        user['username'] = username
        return jsonify(users[username])
    else:
        return "404 Not Found", 404


@app.route("/add_user", methods=['POST'])
def add_user():
    user_data = request.get_json()
    username = user_data['username']
    users[username] = {
        'name': user_data['name'],
        'age': user_data['age'],
        'city': user_data['city']
    }
    user = users[username]
    user['username'] = username
    return jsonify({"message": "User added", "user": user})


if __name__ == "__main__":
    app.run()
