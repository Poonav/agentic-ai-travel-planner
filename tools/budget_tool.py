from langchain.tools import tool

@tool
def budget_estimator(flight_price: float, hotel_price: float, days: int):
    """
    Estimates total trip budget based on flight price, hotel price per night, and number of days.

    Input:
        flight_price (float): Price of the flight
        hotel_price (float): Price per night of hotel
        days (int): Number of days of the trip

    Output:
        Dictionary with total_cost and per_day cost
    """

    total_cost = flight_price + hotel_price * days
    per_day = total_cost / days

    return {"total_cost": total_cost, "per_day": per_day}
