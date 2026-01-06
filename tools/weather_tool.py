import requests
from langchain.tools import tool

@tool
def weather_lookup(latitude: float, longitude: float):
    """
    Gets real-time weather forecast for a given latitude and longitude using Open-Meteo API.
    
    Input:
        latitude (float): Latitude of the location
        longitude (float): Longitude of the location
    
    Output:
        Daily weather forecast (temperature, precipitation, etc.)
    """

    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=auto"
    
    response = requests.get(url).json()
    
    return response.get("daily", {})
