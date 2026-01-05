import json
from langchain.tools import tool

@tool
def budget_estimator(budget_input: str):
    """
    Estimates total trip budget based on flight price, hotel price per night, and number of days.
    Input: {"flight_price": 3000, "hotel_price": 2500, "days": 5}
    Output: {"total_cost": 16250, "per_day": 3250}
    """
    budget_input = json.loads(budget_input)
    flight_price = budget_input["flight_price"]
    hotel_price = budget_input["hotel_price"]
    days = budget_input["days"]

    total_cost = flight_price + hotel_price * days
    per_day = total_cost / days

    return {"total_cost": total_cost, "per_day": per_day}
