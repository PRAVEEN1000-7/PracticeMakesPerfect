import requests

url = "https://api.open-meteo.com/v1/forecast"

params = {
    'latitude': 11.342423,
    'longitude': 77.728165,
    'current_weather': True
}

try :
    response = requests.get(url, params=params,timeout=5)
    response.raise_for_status()
    
    weatherdata = response.json()
    
    print("Temperature in Erode:", weatherdata["current_weather"]["temperature"],"°C")
    print("Wind speed : ", weatherdata["current_weather"]["windspeed"],"km/h")
    
except requests.exceptions.RequestException as e:
    print("Weather API request failed: ",e)