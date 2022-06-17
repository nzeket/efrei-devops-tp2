
import requests
import json
import os

from flask import Flask, render_template, request


app = Flask(__name__)

# create a function that returns the weather for a specific location using env lat and lon
def get_weather(lat, lon, api_key):
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
    response = requests.get(url)
    data = json.loads(response.text)
    return data

@app.route('/')
def index():
    args = request.args
    
    lat = args['lat']
    lon = args['lon']
    api_key = os.environ['API_KEY']
    
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}').text
    
    return f"{res}\n"

if __name__ == "__main__":
    #print(get_weather(lat, lon, api_key))
    app.run(host="0.0.0.0", port=8081, debug=True)