from langchain_community.llms import Ollama
from tools.flight_tool import flight_search
from tools.hotel_tool import hotel_recommendation
from tools.places_tool import places_discovery
from tools.weather_tool import weather_lookup
from tools.budget_tool import budget_estimator

def run_travel_agent(user_input):
    """
    Runs all travel planning tools and returns a combined itinerary.
    Expects user_input dict with keys:
    - source
    - destination
    - days
    - budget
    - interests
    """

    # 1️⃣ Flight search
    flight_result = flight_search.invoke({
        "source": user_input["source"],
        "destination": user_input["destination"]
    })

    # 2️⃣ Hotel recommendation
    hotel_result = hotel_recommendation.invoke({
        "city": user_input["destination"],
        "max_budget": user_input.get("budget", 10000)
    })

    # 3️⃣ Places discovery
    places_result = places_discovery.invoke({
        "city": user_input["destination"],
        "interests": user_input.get("interests", [])
    })

    # 4️⃣ Weather lookup
    weather_result = weather_lookup.invoke({
        "latitude": user_input.get("latitude", 15.5),   # default coords
        "longitude": user_input.get("longitude", 73.8)
    })

    # 5️⃣ Budget estimation
    budget_result = budget_estimator.invoke({
        "flight_price": flight_result.get("price", 0),
        "hotel_price": hotel_result.get("price_per_night", 0),
        "days": user_input.get("days", 3)
    })

    # Combine all results in structured output
    final_output = {
        "flight": flight_result,
        "hotel": hotel_result,
        "places": places_result,
        "weather": weather_result,
        "budget": budget_result
    }

    return final_output
