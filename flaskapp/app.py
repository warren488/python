from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
def index():
    return jsonify({"name":"warren"})


@app.route('/post', methods=["POST"])
def post():
    return jsonify(request.json)

@app.route('/show/<string:id>')
def show(id):
    return 'you requested: '+id

if __name__ == '__main__':
    app.run(debug=True)