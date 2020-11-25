import datetime
from datetime import datetime
import requests as req
from geopy.geocoders import Nominatim

api_key = 'a013fd02b8d6ebae248924f08741e6ec'


def get_city_coordinates(city_name):
    default = 51, 21
    geolocator = Nominatim(user_agent="Piotr Bobel")
    location = geolocator.geocode(city_name)
    if location is None:
        return default
    else:
        return location.latitude, location.longitude


def get_json_data(coordinates, include):
    type_list = ['minutely', 'hourly', 'daily', 'alerts']
    type_list.remove(include)
    excludes = ','.join(type_list)
    url = 'https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&exclude=%s&appid=%s&units=metric' %\
          (coordinates[0], coordinates[1], excludes, api_key)
    json_data = req.get(url).json()
    return json_data


def get_weather_conditions_for_n_days(how_many_days, json_data):
    weather_conditions = []

    weather_conditions.append(
        {"temp": json_data['current']['temp'],
         'feels_like': json_data['current']['feels_like'],
         'desc': json_data['current']['weather'][0]['description'],
         'icon': json_data['current']['weather'][0]['icon'],
         'humidity': json_data['current']['humidity']
         }
    )
    for i in range(1, how_many_days):
        weather_conditions.append(
            {"temp_min": json_data['daily'][i]['temp']['min'],
             'temp_max': json_data['daily'][i]['temp']['max'],
             'desc': json_data['daily'][i]['weather'][0]['description'],
             'icon': json_data['daily'][i]['weather'][0]['icon'],
             'humidity': json_data['daily'][i]['humidity']
             }
        )

    return weather_conditions


def get_hourly_forecast(date, json_data):
    hourly_forecast = []

    for i in range(48):
        if date == date.fromtimestamp(json_data['hourly'][i]['dt']):
            hourly_forecast.append(
                {'temp': json_data['hourly'][i]['temp'],
                 'date': str(datetime.fromtimestamp(json_data['hourly'][i]['dt']))
                 }
            )

    return hourly_forecast


def main():
    pass


if __name__ == '__main__':
    main()