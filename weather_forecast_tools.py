import os
import dotenv
import requests

dotenv.load_dotenv()


def get_weather(lat: str, lon: str):
    url = os.getenv("WEATHER_API_CALL").format(latitude=lat, longitude=lon)
    weather_data = requests.get(url).json()
    return f"Latitude: {lat}; longitude: {lon}\n" \
           f"Temperature: {weather_data['main']['temp']}\n" \
           f"Feels like: {weather_data['main']['feels_like']}\n" \
           f"Weather: {weather_data['weather'][0]['main']}\n" \
           f"Description: {weather_data['weather'][0]['description'].capitalize()}"
