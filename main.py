import requests
from datetime import datetime
api_key = '589d27627ef632e239e16f50f645db55'
location = input("Enter City Name: ")
complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

city_temp = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
humid = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print("----------------------------------------------------------")
print("Weather stats for - {}  || {}".format(location.upper(), date_time))
print("-----------------------------------------------------------")

print(" Current temperature : {:.2f} deg C".format(city_temp))
print("Weather description: ", weather_desc)
print("Humidity: ", humid, '%')
print("Current Wind speed: ", wind_spd, 'kph')
with open('weatherReport.txt','wb') as f:
    f.write(api_link.content)

