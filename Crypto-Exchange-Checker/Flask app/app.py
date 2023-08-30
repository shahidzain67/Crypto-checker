from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()
url = str(os.getenv('MAIN_URL'))
access_key = str(os.getenv('API_ACCESS_KEY'))

app = Flask(__name__)

# List API route
@app.route('/api/list', methods=['GET'])
def list_currencies():
    response = requests.get(url + "/list" + "?access_key=" + access_key)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Could not fetch data"}), response.status_code

# Live API route
@app.route('/api/live', methods=['GET'])
def live_currencies():
    response = requests.get(url + "/live" + "?access_key=" + access_key)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Could not fetch data"}), response.status_code

# Historical API route
@app.route('/api/historical/<string:date>', methods=['GET'])
def get_historical_data(date):
    response = requests.get(url + "/historical/" + date + "?access_key=" + access_key)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Could not fetch data"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
