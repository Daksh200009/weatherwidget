# Used to make HTTP requests
import requests
# Used to handle date and time operations.
from datetime import datetime
# From Flask framework for creating web applications, rendering templates, and handling HTTP requests.
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():

    # API key for OpenWeatherMap API
    api_key = '95811ce11bed9885114029457eccb350'
    # City for which weather forecast is requested
    city = 'Adelaide'
    # URL to fetch weather forecast data for the city using OpenWeatherMap API
    url = f'https://api.openweathermap.org/data/2.5/forecast?q=' + city + '&APPID=' + api_key
    print(url)
    # Sending HTTP GET request to the API endpoint
    response = requests.get(url)
    data = response.json()
    # Extracting city name from the response data
    city_name = data['city']['name']
    # Extracting city population from the response data
    city_population = data['city']['population']
    # Printing the variables listed above
    print(city_name)
    print(city_population)

    #'description': data['weather'][0]['description'],

    # List of forecast data for the next 5 days (3-hour intervals)
    forecast_list = data['list']
    index = 0
    forecast_data = []
    while index < len(forecast_list):
        forecast = forecast_list[index]
        # Print timestamp of forecast
        dt_txt = forecast_list[index]["dt_txt"]
        # Convert Unix timestamp to local time
        day_name = datetime.fromtimestamp(forecast['dt'])
        # Main temperature
        # Ensure temperature is fetched correctly and is in Kelvin
        temp_kelvin = forecast['main']['temp']
        # Convert Kelvin to Celsius and round to 2 decimal places
        temp_celsius = round(temp_kelvin - 273.15, 0)
        # Description of weather
        description = forecast['weather'][0]['description']
        icon = response.json()
        icon_code = forecast['weather'][0]['icon']
        icon_url = f"http://openweathermap.org/img/w/{icon_code}.png"
        # Checking if it will rain during the forecast period
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

        # Dictionary containing forecast details for one period
        thisdict = {
            'dt_txt': dt_txt,
            'day_of_week': day_name,
            'temp': temp_celsius,
            'icon': icon_url,
            'description': description,
            'rain': rain,
            'date_object': date_object,
            'day_name': day_name,

        }

        forecast_data.append(thisdict)

    return render_template('home.html', forecast_data=forecast_data)

if __name__ == '__main__':
    app.run(debug=True)
