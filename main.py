from flask import Flask, request, jsonify
from calculate import Calculate
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def hello():
    return 'rest api'



@app.route('/price_pred', methods=['POST'])
def index():
    value = request.json['percentage']
    cls = Calculate(value)
    out = cls.main()
    print('result_sent')
    # result = {"output":out}
    #return jsonify(out)
    response=jsonify(out)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response




#if __name__ == '__main__':
 #   app.run(debug=True,port=80,host="0.0.0.0")
