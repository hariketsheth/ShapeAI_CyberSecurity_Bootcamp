import requests
from datetime import datetime

api_key ='b1b57d9af514a3484d3d527977c9b417'

location = input("Enter the  City name: ")
complete_api_link ="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key

api_link =requests.get(complete_api_link)
api_data= api_link.json()
temp_city=((api_data['main']['temp'])-273.15)
weather_desc =api_data['weather'][0]['description']
hmdt=api_data['main']['humidity']
wind_spd =api_data['wind']['speed']
date_time=datetime.now().strftime("%d %b %Y | %I:%M:%S%P")
print("-------------------------------")


print("weather states for - {} || {}".format(location.upper(), date_time))
print("-------------------------------")

print("Temperature is :{:2f} deg C".format(temp_city))
print("Weather Desc :",weather_desc)
print("Humidity :",hmdt, '%')
print("Wind speed:" ,wind_spd,'kmph')
