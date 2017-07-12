from flask import Flask, jsonify, request
from index import index

app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
def indexf():
    return index()


@app.route('/post', methods=["POST"])
def post():
    return request.url

@app.route('/show/<string:id>')
def show(id):
    return 'you requested: '+id

if __name__ == '__main__':
    app.run(debug=True)