from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import json

import weathermodule
import weathernow
import coronadata



app = Flask(__name__)
CORS(app)



@app.route('/weather',methods=['GET'])
def weather():
    with open('weather.json', 'r') as f:
        datasend = json.load(f)
        return jsonify(datasend)

@app.route('/weather_now',methods=['GET'])
def weather_now():
    with open('weather_now.json', 'r') as f:
        datasend = json.load(f)
        return jsonify(datasend)


@app.route('/coronadata',methods=['GET'])
def coronadata_update():
    with open('deagu_corona.json', 'r') as f:
        datasend = json.load(f)
        return jsonify(datasend)

@app.route('/air_condition',methods=['GET'])
def air_condition_update():
    with open('air_condition.json', 'r') as f:
        datasend = json.load(f)
        return jsonify(datasend)


if __name__ == "__main__":
    app.run(host = '0.0.0.0' ,port=5000)
