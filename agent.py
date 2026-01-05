from langchain_community.llms import Ollama
from tools.flight_tool import flight_search
from tools.hotel_tool import hotel_recommendation
from tools.places_tool import places_discovery
from tools.weather_tool import weather_lookup
from tools.budget_tool import budget_estimator

def run_travel_agent(user_input):
    # Call flight_search tool correctly for LangChain
    flight_result = flight_search.invoke({
    "source": user_input["source"],
    "destination": user_input["destination"]
})

    # Similarly, call other tools
    hotel_result = hotel_recommendation.invoke({
    "city": user_input["destination"],
    "max_budget": user_input.get("budget", 10000)

    })

    places_result = places_discovery.invoke({
    "city": user_input["destination"],
    "interests": user_input.get("interests", [])
})


    weather_result = weather_lookup.invoke({
    "latitude": user_input.get("latitude", 15.5),   # replace with real coords
    "longitude": user_input.get("longitude", 73.8)
})

    budget_result = budget_estimator.invoke({
    "flight_price": flight_result["price"],
    "hotel_price": hotel_result["price_per_night"],
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

