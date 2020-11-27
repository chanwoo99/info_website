from flask import Flask, request, jsonify
from flask_cors import CORS
import json

import weathermodule


app = Flask(__name__)
CORS(app)

@app.route('/test',methods=['GET'])
def test():
    aa= "test"
    return aa

@app.route('/weather',methods=['GET'])
def weather():
    weathermodule.run()
    with open('weather.json', 'r') as f:
        datasend = json.load(f)
        return jsonify(datasend)



if __name__ == "__main__":
    app.run(host = '0.0.0.0')
