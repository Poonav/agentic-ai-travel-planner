from langchain.tools import tool
import json

@tool
def hotel_recommendation(city: str, max_budget: int = 10000):
    """
    Finds the best hotel in a city based on budget using hotels.json dataset.
    
    Input:
        city (str): Name of the city
        max_budget (int, optional): Maximum price per night. Default is 10000.
    
    Output:
        A dictionary with hotel name, rating, price per night, and address.
    """

    # Load hotel dataset
    with open("data/hotels.json") as f:
        hotels = json.load(f)

    # Filter hotels by city and budget
    matches = [
        h for h in hotels
        if h.get("city") == city and h.get("price_per_night", 0) <= max_budget
    ]

    if not matches:
        return {"message": "No hotels found."}

    # Sort by rating descending, then price ascending
    best_hotel = sorted(
        matches,
        key=lambda x: (-x.get("rating", 0), x.get("price_per_night", 0))
    )[0]

    return best_hotel
