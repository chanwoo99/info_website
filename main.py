from flask import Flask, request, jsonify
from flask_cors import CORS
import json

import weathermodule
import weathernow
import coronadata


app = Flask(__name__)
CORS(app)



@app.route('/weather',methods=['GET'])
def weather():
    weathermodule.run()
    with open('weather.json', 'r') as f:
        datasend = json.load(f)
        return jsonify(datasend)

@app.route('/weather_now',methods=['GET'])
def weather_now():
    weathernow.run()
    with open('weather_now.json', 'r') as f:
        datasend = json.load(f)
        return jsonify(datasend)


@app.route('/coronadata',methods=['GET'])
def coronadata_update():
    coronadata.run()
    with open('deagu_corona.json', 'r') as f:
        datasend = json.load(f)
        return jsonify(datasend)


if __name__ == "__main__":
    app.run(host = '0.0.0.0' ,port=8000)
