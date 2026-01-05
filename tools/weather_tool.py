import json
import requests
from langchain.tools import tool

@tool
def weather_lookup(weather_input: str):
    """
    Gets real-time weather forecast for a given latitude and longitude using Open-Meteo API.
    Input: {"latitude": 15.5, "longitude": 73.8}
    Output: Daily weather forecast (temperature, precipitation, etc.)
    """
    weather_input = json.loads(weather_input)
    latitude = weather_input["latitude"]
    longitude = weather_input["longitude"]

    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=auto"
    response = requests.get(url).json()

    return response.get("daily", {})
