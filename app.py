from flask import Flask, render_template, request
from datetime import datetime
from matplotlib import pyplot as plt
import requests

app = Flask(__name__)

@app.route('/')
def home():


    return render_template('home.html')


def get_weather(city):
    api_key = "95811ce11bed9885114029457eccb350"
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&unit=metric"
    print(url)
    response = requests.get(url)
    data = response.json()
    return render_template("home.html")

    # "description": data["weather"][0]["description"],




# forecast_list = response['list'[0]]
# for forecast in forecast_list:
#     timestap
# print(get_weather("adelaide"))


if __name__ == '__main__':
        app.run(debug=True)
