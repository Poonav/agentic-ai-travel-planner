import json
from langchain.tools import tool
from typing import List

@tool
def places_discovery(city: str, interests: List[str] = []):
    """
    Recommends points of interest in a city based on user interests using places.json dataset.
    
    Input:
        city (str): Name of the city
        interests (List[str], optional): List of interests (e.g., ["Nature", "Food"])
    
    Output:
        List of attractions with type and rating.
    """

    # Load places dataset
    with open("data/places.json") as f:
        places = json.load(f)

    # Filter by city and interests
    matches = [
        p for p in places
        if p.get("city") == city and (not interests or p.get("type") in interests)
    ]

    # Sort by rating descending
    return sorted(matches, key=lambda x: -x.get("rating", 0))
