from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test')
def predict():
    reponse = jsonify({'code' : 200, 'data' : 'hello world'})
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()