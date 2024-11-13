from flask import Flask, render_template, jsonify

app = Flask(__name__)
data = [
    {"id": 1, "name": "Tal"},
    {"id": 2, "name": "Bar"},
]

@app.route('/')
def home():
    return "Hello Tal!"

@app.route('/names')
def names():
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)