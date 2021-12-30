from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test')
def predict():
    response = jsonify({'code' : 200, 'data' : 'hello world'})
    return response


if __name__ == '__main__':
    app.run()