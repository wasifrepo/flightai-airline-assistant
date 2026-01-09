import sqlite3
from app.config import DB_PATH


def get_ticket_price(city: str) -> str:
    if not city:
        return "No price data available for this city"

    print(f"DATABASE TOOL CALLED: Getting price for {city}", flush=True)

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT price FROM prices WHERE city = ?", (city.lower(),))
        result = cursor.fetchone()

    if result:
        return f"Ticket price to {city} is ${result[0]}"
    return "No price data available for this city"
