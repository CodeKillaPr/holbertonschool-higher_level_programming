from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, this is a simple API!'


@app.route('/data')
def data():
    data = {"name": "John", "age": 30, "city": "New York"}
    return jsonify(data)


@app.route('/status')
def status():
    return 'OK'


if __name__ == '__main__':
    app.run(port=8000)
