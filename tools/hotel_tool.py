import json
from langchain.tools import tool

@tool 
def hotel_recommendation(hotel_input: str):  # string, not dict
    """
    Finds the best hotel in a city based on budget using hotels.json dataset.
    Input: {"city": "Goa", "max_budget": 10000}
    Output: A dictionary with hotel name, rating, price per night, and address.
    """
    hotel_input = json.loads(hotel_input)  # convert string to dict
    city = hotel_input["city"]
    max_budget = hotel_input.get("max_budget", 10000)

    with open("data/hotels.json") as f:
        hotels = json.load(f)

    matches = [h for h in hotels if h.get("city") == city and h.get("price_per_night", 0) <= max_budget]

    if not matches:
        return "No hotels found."

    return sorted(matches, key=lambda x: (-x.get("rating", 0), x.get("price_per_night", 0)))[0]
