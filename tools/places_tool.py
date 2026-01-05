import json
from langchain.tools import tool
@tool
def places_discovery(places_input: str):
    """
    Recommends points of interest in a city based on user interests using places.json dataset.
    Input: {"city": "Goa", "interests": ["Nature", "Food"]}
    Output: List of attractions with type and rating.
    """
    places_input = json.loads(places_input)
    city = places_input["city"]
    interests = places_input.get("interests", [])

    with open("data/places.json") as f:
        places = json.load(f)

    matches = [p for p in places if p.get("city") == city and (not interests or p.get("type") in interests)]

    return sorted(matches, key=lambda x: -x.get("rating", 0))
