from langchain.tools import tool


@tool
def tracking_tool(order_id: str) -> dict:
    """Track an order by its order ID and return delivery status."""
    return {
        "order_id": order_id,
        "status": "In transit",
        "eta_days": 2
    }


@tool
def refund(order_id: str) -> dict:
    """Process a refund request for a given order ID."""
    return {
        "order_id": order_id,
        "status": "approved",
        "message": "Refund processing"
    }


@tool
def complaint(issue: str) -> dict:
    """Log a customer complaint and return a ticket ID."""
    return {
        "issue": issue,
        "ticket_id": "TICKET-12345",
        "status": "received"
    }


@tool
def escalation(issue: str) -> dict:
    """Escalate a customer issue to a senior support agent."""
    return {
        "issue": issue,
        "status": "escalated",
        "message": "Senior agent will contact you"
    }


@tool
def hotel_search(location: str) -> dict:
    """Search for hotels in a given location and return a static list of results."""
    return {
        "location": location,
        "hotels": [
            {"name": "Marina View Hotel", "price": 120},
            {"name": "City Center Inn", "price": 95},
            {"name": "Desert Palm Resort", "price": 180},
        ]
    }


@tool
def flight_search(origin: str, destination: str) -> dict:
    """Search for flights between two cities and return static flight options."""
    return {
        "origin": origin,
        "destination": destination,
        "flights": [
            {"name": "Emirates EK202", "price": 450, "duration": "8h 10m"},
            {"name": "FlyDubai FZ145", "price": 320, "duration": "8h 45m"},
            {"name": "Qatar Airways QR101", "price": 500, "duration": "7h 55m"},
        ]
    }