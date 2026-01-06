import json
from langchain.tools import tool

@tool
def flight_search(source: str, destination: str):
    """
    Finds the cheapest flight between two cities using flights.json dataset.
    
    Input:
        source (str): Departure city
        destination (str): Arrival city
    
    Output:
        Dictionary containing flight details (flight_id, airline, source, destination,
        departure_time, arrival_time, price). If no flight is found, returns a default dict
        with price 0.
    """

    # Load flights dataset
    try:
        with open("data/flights.json") as f:
            flights = json.load(f)
    except FileNotFoundError:
        return {
            "flight_id": None,
            "airline": None,
            "source": source,
            "destination": destination,
            "departure_time": None,
            "arrival_time": None,
            "price": 0
        }

    # Filter flights matching source and destination
    matches = [f for f in flights if f.get("source") == source and f.get("destination") == destination]

    if not matches:
        # Return a safe default if no flights found
        return {
            "flight_id": None,
            "airline": None,
            "source": source,
            "destination": destination,
            "departure_time": None,
            "arrival_time": None,
            "price": 0
        }

    # Return the cheapest flight
    cheapest = sorted(matches, key=lambda x: x.get("price", 0))[0]

    # Ensure price key exists
    if "price" not in cheapest:
        cheapest["price"] = 0

    return cheapest
