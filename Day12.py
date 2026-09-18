"""
Day 12

"""
import requests

city = input("Enter city name: ")

# Get city coordinates
geo = requests.get(
    "https://geocoding-api.open-meteo.com/v1/search",
    params={"name": city}
).json()

if "results" not in geo or not geo["results"]:
    print("City not found!")
    exit()

lat = geo["results"][0]["latitude"]
lon = geo["results"][0]["longitude"]
name = geo["results"][0]["name"]

# Get weather data
data = requests.get(
    "https://api.open-meteo.com/v1/forecast",
    params={
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,wind_speed_10m"
    }
).json()

# Extract current weather
temp = data["current"]["temperature_2m"]
wind = data["current"]["wind_speed_10m"]

print(f"\nCity: {name}")
print(f"Temp: {temp}°C")

print(f"Wind speed: {wind} km/h")
