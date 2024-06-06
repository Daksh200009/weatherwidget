import requests
from datetime import datetime
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
    print('city_name')
    print('city_population')

    #'description': data['weather'][0]['description'],

    forecast_list = data['list']
    index = 0
    while index < len(forecast_list):

        while index < len(forecast_list):
            print(forecast_list[index]['dt_txt'])  # Print timestamp of forecast
            "day_of_week" : day_name
            print(forecast_list[index]['weather'][0]['description'])  # Description of weather
            print(forecast_list[index]['main']['temp'])  # Temperature
            print(forecast_list[index]['weather'][0]['main'])
            index += 1

            while index < len(forecast_list):
                forecast = forecast_list[index]
                print('server_time:', forecast['dt_txt'])  # Print timestamp of forecast
                dt_txt = forecast_list[index]["dt_txt"]
                print('local_time:', datetime.fromtimestamp(forecast['dt']))  # Convert Unix timestamp to local time
                print('Temperature (min):', forecast['main']['temp_min'])  # Minimum temperature
                print('Temperature (max):', forecast['main']['temp_max'])  # Maximum temperature
                print('Weather Description:', forecast['weather'][0]['description'])  # Description of weather
                print('Main Weather Condition:', forecast['weather'][0]['main'])  # Main weather condition
                index += 1

    date_object = datetime.strptime(dt_txt, '%Y-%m-%d %H %M %S')
    day_of_week = date_object.weekdays()
    print(day_of_week)
    day_name = date_object.strptime('%A')
    print(day_name)
    days.append(day_name)

    forecast_list = ""
    return render_template('home.html', forecast_list=forecast_list)

if __name__ == '__main__':
    app.run(debug=True)