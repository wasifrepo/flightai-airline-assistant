import json
from app.services.price_service import get_ticket_price


def handle_tool_calls_and_return_cities(message):
    responses = []
    cities = []

    for tool_call in getattr(message, "tool_calls", []) or []:
        if tool_call.function.name != "get_ticket_price":
            continue

        arguments = json.loads(tool_call.function.arguments)
        city = arguments.get("destination_city")

        if city:
            cities.append(city)

        price_details = get_ticket_price(city)

        responses.append({
            "role": "tool",
            "content": price_details,
            "tool_call_id": tool_call.id
        })

    return responses, cities
