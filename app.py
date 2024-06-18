# Used to make HTTP requests
import requests
# Used to handle date and time operations.
from datetime import datetime
# From Flask framework for creating web applications, rendering templates, and handling HTTP requests.
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():

    api_key = '95811ce11bed9885114029457eccb350'
    city = 'Adelaide'
    url = f'https://api.openweathermap.org/data/2.5/forecast?q=' + city + '&APPID=' + api_key
    print(url)
    response = requests.get(url)
    data = response.json()
    city_name = data['city']['name']
    city_population = data['city']['population']
    print(city_name)
    print(city_population)

    #'description': data['weather'][0]['description'],

    forecast_list = data['list']
    index = 0
    forecast_data = []
    while index < len(forecast_list):
        forecast = forecast_list[index]
        # Print timestamp of forecast

        dt_txt = forecast_list[index]["dt_txt"]
        # Convert Unix timestamp to local time
        day_name = datetime.fromtimestamp(forecast['dt'])
        # Maximum temperature
        temp = forecast['main']['temp']
        # Description of weather
        description = forecast['weather'][0]['description']
        icon = response.json()
        # Rain
        if 'rain' in forecast_list[index]:
            rain = forecast_list[index]['rain']
        else:
            rain = "No Rain"
        print(rain)
        date_object = datetime.strptime(dt_txt, '%Y-%m-%d %H:%M:%S')
        print(date_object)
        day_name = date_object.strftime('%A')
        print(day_name)

        index += 8


        thisdict = {
            'dt_txt': dt_txt,
            'day_of_week': day_name,
            'temp': temp,
            'icon': 'http://openweathermap.org/img/w/' + '.png',
            'description': description,
            'rain': rain,
            'date_object': date_object,
            'day_name': day_name,
        }

        forecast_data.append(thisdict)

    return render_template('home.html', forecast_data=forecast_data)

if __name__ == '__main__':
    app.run(debug=True)
