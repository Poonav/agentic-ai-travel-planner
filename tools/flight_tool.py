from langchain.tools import tool
import json

@tool
def flight_search(source: str, destination: str):
    """
    Finds the cheapest flight between two cities.
    Input: source (str), destination (str)
    Output: A dictionary containing flight details (airline, price, departure, arrival)
    """

    # Load your JSON dataset
    with open("data/flights.json") as f:
        flights = json.load(f)

    # Filter flights matching source and destination
    matches = [f for f in flights if f.get("source") == source and f.get("destination") == destination]

    # No flights found
    if not matches:
        return {"message": "No flights found."}

    # Return cheapest flight
    return sorted(matches, key=lambda x: x["price"])[0]
