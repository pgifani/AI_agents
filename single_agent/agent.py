
from google.adk.agents.llm_agent import Agent
from datetime import datetime
import pytz

CITY_TIMEZONES = {
    # Americas
    "new york": "America/New_York",
    "los angeles": "America/Los_Angeles",
    "chicago": "America/Chicago",
    "toronto": "America/Toronto",
    "vancouver": "America/Vancouver",
    "mexico city": "America/Mexico_City",
    "sao paulo": "America/Sao_Paulo",
    "buenos aires": "America/Argentina/Buenos_Aires",

    # Europe
    "london": "Europe/London",
    "paris": "Europe/Paris",
    "berlin": "Europe/Berlin",
    "madrid": "Europe/Madrid",
    "rome": "Europe/Rome",
    "amsterdam": "Europe/Amsterdam",
    "brussels": "Europe/Brussels",
    "vienna": "Europe/Vienna",
    "zurich": "Europe/Zurich",
    "stockholm": "Europe/Stockholm",
    "oslo": "Europe/Oslo",
    "moscow": "Europe/Moscow",
    "istanbul": "Europe/Istanbul",

    # Middle East
    "dubai": "Asia/Dubai",
    "tehran": "Asia/Tehran",
    "riyadh": "Asia/Riyadh",
    "doha": "Asia/Qatar",
    "kuwait city": "Asia/Kuwait",
    "baghdad": "Asia/Baghdad",
    "beirut": "Asia/Beirut",
    "tel aviv": "Asia/Jerusalem",

    # Asia
    "tokyo": "Asia/Tokyo",
    "beijing": "Asia/Shanghai",
    "shanghai": "Asia/Shanghai",
    "hong kong": "Asia/Hong_Kong",
    "singapore": "Asia/Singapore",
    "seoul": "Asia/Seoul",
    "mumbai": "Asia/Kolkata",
    "delhi": "Asia/Kolkata",
    "karachi": "Asia/Karachi",
    "lahore": "Asia/Karachi",
    "dhaka": "Asia/Dhaka",
    "bangkok": "Asia/Bangkok",
    "jakarta": "Asia/Jakarta",
    "kuala lumpur": "Asia/Kuala_Lumpur",

    # Africa
    "cairo": "Africa/Cairo",
    "lagos": "Africa/Lagos",
    "nairobi": "Africa/Nairobi",
    "johannesburg": "Africa/Johannesburg",
    "casablanca": "Africa/Casablanca",

    # Oceania
    "sydney": "Australia/Sydney",
    "melbourne": "Australia/Melbourne",
    "auckland": "Pacific/Auckland",
}


def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city."""
    city_lower = city.lower().strip()
    timezone_str = CITY_TIMEZONES.get(city_lower)

    if not timezone_str:
        return {
            "status": "error",
            "city": city,
            "message": f"Timezone for '{city}' not found. Try cities like London, Tokyo, New York..."
        }

    tz = pytz.timezone(timezone_str)
    current_time = datetime.now(tz).strftime("%I:%M %p")

    return {
        "status": "success",
        "city": city,
        "time": current_time
    }


root_agent = Agent(
    model='groq/llama-3.3-70b-versatile',
    name='root_agent',
    description="Tells the current time in a specified city.",
    instruction="You are a helpful assistant that tells the current time in cities. Use the 'get_current_time' tool for this purpose.",
    tools=[get_current_time],
)
