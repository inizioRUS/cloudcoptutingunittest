from flask import Flask, request, jsonify

li = {}
app = Flask(__name__)


@app.route('/give42', methods=['GET'])
def allgetaa():
    if request.method == "GET":
        return '42'
@app.route('/health', methods=['GET'])
def helth():
    if request.method == "GET":
        resp = jsonify(success=True)
        resp.status_code = 200
        return resp


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
