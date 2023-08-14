import requests

CITY_NAME = "Kathmandu"  # Replace with your desired city name
URL = f"https://wttr.in/{CITY_NAME}?format=%t+%C"

response = requests.get(URL)

if response.status_code == 200:
    weather_info = response.text.strip().split(' ')

else:
        print("Failed to retrieve weather data.")

def provide_temperature():
    temperature = weather_info[0]
    print(f"The current temperature in {CITY_NAME} is {temperature}")
    
def provide_weather():
     weather_description = ' '.join(weather_info[1:])
     print(f"According to the web, current weather in {CITY_NAME}: {weather_description}")
