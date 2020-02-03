from flask import Flask, request, jsonify
from calculate import Calculate
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['POST'])
def index():
    value = request.json['percentage']
    cls = Calculate(value)
    out = cls.main()
    print(out)
    # result = {"output":out}
    #return jsonify(out)
    response=jsonify(out)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response




if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=8897, debug=True)
