from tools.flight_tool import flight_search
from tools.hotel_tool import hotel_recommendation
from tools.places_tool import places_discovery
from tools.weather_tool import weather_lookup
from tools.budget_tool import budget_estimator

def run_travel_agent(user_input):

    # 1️⃣ Flight search (FIXED)
    flight_result = flight_search.invoke({
        "flight_input": {
            "source": user_input["source"][0],
            "destination": user_input["destination"][0]
        }
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
        "latitude": user_input.get("latitude", 15.5),
        "longitude": user_input.get("longitude", 73.8)
    })

    # 5️⃣ Budget estimation
    budget_result = budget_estimator.invoke({
        "flight_price": flight_result["price"],
        "hotel_price": hotel_result["price_per_night"],
        "days": user_input.get("days", 3)
    })

    return {
        "flight": flight_result,
        "hotel": hotel_result,
        "places": places_result,
        "weather": weather_result,
        "budget": budget_result
    }
