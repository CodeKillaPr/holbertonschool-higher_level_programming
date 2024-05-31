#!/usr/bin/env python3
"""Develop a Simple API using Python with Flask"""
from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)

users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
         "john": {"name": "John", "age": 30, "city": "New York"},
         "james": {"name": "James", "age": 25, "city": "Chicago"}}


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/status')
def status():
    return "OK"


@app.route('/data')
def get_usernames():
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"})


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON data provided"})

    username = data.get('username')
    if not username:
        return jsonify({"error": "Username not provided"})

    if username in users:
        return jsonify({"error": "Username already exists"})

    users[username] = {
        "name": data.get('name', ''),
        "age": data.get('age', 0),
        "city": data.get('city', '')
    }

    return jsonify({"message": "User added successfully", "user": users[username]})


if __name__ == '__main__':
    app.run()
