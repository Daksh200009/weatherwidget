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

        print(forecast_list[index]['dt_txt'])
        print(forecast_list[index]['main']['weather'])
        print(forecast_list[index]['weather'][0]['temp'])
        print(forecast_list[index]['weather'][0]['main'])
        index += 8

    #   print('server_time' + forecast['dt_txt'])
    #   print('local' + str(datetime.fromtimestamp(forecast['dt'])))
    #   print(forecast['main']['temp_min'])
    #   print(forecast['main']['temp_max'])
    #

    forecast_list = ""
    return render_template('home.html', forecast_list=forecast_list)

if __name__ == '__main__':
    app.run(debug=True)