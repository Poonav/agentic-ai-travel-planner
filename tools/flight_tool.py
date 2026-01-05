import json
from langchain.tools import tool

@tool
def flight_search(flight_input: str):
    """
    Finds the cheapest flight between two cities.
    Input: {"source": "CityA", "destination": "CityB"}
    Output: A dictionary containing flight details (airline, price, departure, arrival)
    """
    flight_input = json.loads(flight_input)
    source = flight_input["source"]
    destination = flight_input["destination"]

    with open("data/flights.json") as f:
        flights = json.load(f)

    matches = [f for f in flights if f.get("source") == source and f.get("destination") == destination]

    if not matches:
        return "No flights found."

    return sorted(matches, key=lambda x: x["price"])[0]
