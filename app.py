from flask import Flask, jsonify
from model import predict

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test')
def test():
    response = jsonify({'code' : 200, 'data' : 'hello world'})
    return response

@app.route('/predict')
def makePrediction():
    res = predict()
    response = jsonify({'code' : 200, 'data' : str(res)})
    return response

if __name__ == '__main__':
    app.run()