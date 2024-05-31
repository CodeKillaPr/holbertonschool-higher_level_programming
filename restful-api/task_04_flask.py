#!/usr/bin/python3
"""A simple api with Flask"""
from flask import Flask, jsonify, request


app = Flask(__name__)

# In-memory storage for users
users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}
}

# Root endpoint


@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Endpoint to return status


@app.route('/status')
def status():
    return "OK"

# Endpoint to return all usernames


@app.route('/data')
def get_usernames():
    usernames = list(users.keys())
    return jsonify(usernames)

# Endpoint to return user data for a specific username


@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return "User not found", 404

# Endpoint to add a new user


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    if 'username' in data:
        username = data['username']
        users[username] = data
        return jsonify({"message": "User added", "user": data})
    else:
        return "Missing username in request", 400


if __name__ == "__main__":
    app.run()
