import json
from flask import Flask, request, jsonify, render_template
import os.path
import util

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return render_template("app.html")

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/get_area_type', methods=['GET'])
def get_area_type():
    response= jsonify({
        'area_type': util.get_area_type()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():

    tot = json.loads(request.form["dat"])
    total_sqft = tot['total_sqft']
    bhk = tot['bhk']
    bath = tot['bath']
    location = tot['location']
    area_type = tot['area']

    response = jsonify({
        'estimated_price': util.get_estimated_price(area_type,location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()
    print(get_location_names)
    print(response)


