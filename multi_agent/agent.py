
import datetime
import requests
import pytz
from google.adk.agents import Agent

CITY_DATA = {
    # ── North America ──────────────────────────────────────────────────────
    "new york":         {"tz": "America/New_York",              "lat": 40.7128,  "lon": -74.0060},
    "los angeles":      {"tz": "America/Los_Angeles",           "lat": 34.0522,  "lon": -118.2437},
    "chicago":          {"tz": "America/Chicago",               "lat": 41.8781,  "lon": -87.6298},
    "houston":          {"tz": "America/Chicago",               "lat": 29.7604,  "lon": -95.3698},
    "miami":            {"tz": "America/New_York",              "lat": 25.7617,  "lon": -80.1918},
    "san francisco":    {"tz": "America/Los_Angeles",           "lat": 37.7749,  "lon": -122.4194},
    "seattle":          {"tz": "America/Los_Angeles",           "lat": 47.6062,  "lon": -122.3321},
    "toronto":          {"tz": "America/Toronto",               "lat": 43.6510,  "lon": -79.3470},
    "vancouver":        {"tz": "America/Vancouver",             "lat": 49.2827,  "lon": -123.1207},
    "montreal":         {"tz": "America/Toronto",               "lat": 45.5017,  "lon": -73.5673},
    "mexico city":      {"tz": "America/Mexico_City",           "lat": 19.4326,  "lon": -99.1332},

    # ── South America ──────────────────────────────────────────────────────
    "sao paulo":        {"tz": "America/Sao_Paulo",             "lat": -23.5505, "lon": -46.6333},
    "rio de janeiro":   {"tz": "America/Sao_Paulo",             "lat": -22.9068, "lon": -43.1729},
    "buenos aires":     {"tz": "America/Argentina/Buenos_Aires","lat": -34.6037, "lon": -58.3816},
    "bogota":           {"tz": "America/Bogota",                "lat": 4.7110,   "lon": -74.0721},
    "lima":             {"tz": "America/Lima",                  "lat": -12.0464, "lon": -77.0428},
    "santiago":         {"tz": "America/Santiago",              "lat": -33.4489, "lon": -70.6693},

    # ── Europe ────────────────────────────────────────────────────────────
    "london":           {"tz": "Europe/London",                 "lat": 51.5074,  "lon": -0.1278},
    "paris":            {"tz": "Europe/Paris",                  "lat": 48.8566,  "lon": 2.3522},
    "berlin":           {"tz": "Europe/Berlin",                 "lat": 52.5200,  "lon": 13.4050},
    "madrid":           {"tz": "Europe/Madrid",                 "lat": 40.4168,  "lon": -3.7038},
    "rome":             {"tz": "Europe/Rome",                   "lat": 41.9028,  "lon": 12.4964},
    "amsterdam":        {"tz": "Europe/Amsterdam",              "lat": 52.3676,  "lon": 4.9041},
    "brussels":         {"tz": "Europe/Brussels",               "lat": 50.8503,  "lon": 4.3517},
    "vienna":           {"tz": "Europe/Vienna",                 "lat": 48.2082,  "lon": 16.3738},
    "zurich":           {"tz": "Europe/Zurich",                 "lat": 47.3769,  "lon": 8.5417},
    "stockholm":        {"tz": "Europe/Stockholm",              "lat": 59.3293,  "lon": 18.0686},
    "oslo":             {"tz": "Europe/Oslo",                   "lat": 59.9139,  "lon": 10.7522},
    "copenhagen":       {"tz": "Europe/Copenhagen",             "lat": 55.6761,  "lon": 12.5683},
    "helsinki":         {"tz": "Europe/Helsinki",               "lat": 60.1699,  "lon": 24.9384},
    "warsaw":           {"tz": "Europe/Warsaw",                 "lat": 52.2297,  "lon": 21.0122},
    "prague":           {"tz": "Europe/Prague",                 "lat": 50.0755,  "lon": 14.4378},
    "budapest":         {"tz": "Europe/Budapest",               "lat": 47.4979,  "lon": 19.0402},
    "bucharest":        {"tz": "Europe/Bucharest",              "lat": 44.4268,  "lon": 26.1025},
    "athens":           {"tz": "Europe/Athens",                 "lat": 37.9838,  "lon": 23.7275},
    "lisbon":           {"tz": "Europe/Lisbon",                 "lat": 38.7223,  "lon": -9.1393},
    "dublin":           {"tz": "Europe/Dublin",                 "lat": 53.3498,  "lon": -6.2603},
    "istanbul":         {"tz": "Europe/Istanbul",               "lat": 41.0082,  "lon": 28.9784},
    "moscow":           {"tz": "Europe/Moscow",                 "lat": 55.7558,  "lon": 37.6173},
    "kyiv":             {"tz": "Europe/Kyiv",                   "lat": 50.4501,  "lon": 30.5234},

    # ── Middle East ───────────────────────────────────────────────────────
    "dubai":            {"tz": "Asia/Dubai",                    "lat": 25.2048,  "lon": 55.2708},
    "abu dhabi":        {"tz": "Asia/Dubai",                    "lat": 24.4539,  "lon": 54.3773},
    "tehran":           {"tz": "Asia/Tehran",                   "lat": 35.6892,  "lon": 51.3890},
    "riyadh":           {"tz": "Asia/Riyadh",                   "lat": 24.7136,  "lon": 46.6753},
    "jeddah":           {"tz": "Asia/Riyadh",                   "lat": 21.4858,  "lon": 39.1925},
    "baghdad":          {"tz": "Asia/Baghdad",                  "lat": 33.3152,  "lon": 44.3661},
    "kuwait city":      {"tz": "Asia/Kuwait",                   "lat": 29.3759,  "lon": 47.9774},
    "doha":             {"tz": "Asia/Qatar",                    "lat": 25.2854,  "lon": 51.5310},
    "muscat":           {"tz": "Asia/Muscat",                   "lat": 23.5880,  "lon": 58.3829},
    "beirut":           {"tz": "Asia/Beirut",                   "lat": 33.8938,  "lon": 35.5018},
    "tel aviv":         {"tz": "Asia/Jerusalem",                "lat": 32.0853,  "lon": 34.7818},
    "amman":            {"tz": "Asia/Amman",                    "lat": 31.9454,  "lon": 35.9284},

    # ── Asia ──────────────────────────────────────────────────────────────
    "delhi":            {"tz": "Asia/Kolkata",                  "lat": 28.6139,  "lon": 77.2090},
    "mumbai":           {"tz": "Asia/Kolkata",                  "lat": 19.0760,  "lon": 72.8777},
    "bangalore":        {"tz": "Asia/Kolkata",                  "lat": 12.9716,  "lon": 77.5946},
    "kolkata":          {"tz": "Asia/Kolkata",                  "lat": 22.5726,  "lon": 88.3639},
    "karachi":          {"tz": "Asia/Karachi",                  "lat": 24.8607,  "lon": 67.0011},
    "lahore":           {"tz": "Asia/Karachi",                  "lat": 31.5204,  "lon": 74.3587},
    "dhaka":            {"tz": "Asia/Dhaka",                    "lat": 23.8103,  "lon": 90.4125},
    "colombo":          {"tz": "Asia/Colombo",                  "lat": 6.9271,   "lon": 79.8612},
    "kathmandu":        {"tz": "Asia/Kathmandu",                "lat": 27.7172,  "lon": 85.3240},
    "kabul":            {"tz": "Asia/Kabul",                    "lat": 34.5553,  "lon": 69.2075},
    "tashkent":         {"tz": "Asia/Tashkent",                 "lat": 41.2995,  "lon": 69.2401},
    "almaty":           {"tz": "Asia/Almaty",                   "lat": 43.2220,  "lon": 76.8512},
    "bangkok":          {"tz": "Asia/Bangkok",                  "lat": 13.7563,  "lon": 100.5018},
    "ho chi minh":      {"tz": "Asia/Ho_Chi_Minh",              "lat": 10.8231,  "lon": 106.6297},
    "hanoi":            {"tz": "Asia/Bangkok",                  "lat": 21.0285,  "lon": 105.8542},
    "phnom penh":       {"tz": "Asia/Phnom_Penh",               "lat": 11.5564,  "lon": 104.9282},
    "yangon":           {"tz": "Asia/Yangon",                   "lat": 16.8661,  "lon": 96.1951},
    "kuala lumpur":     {"tz": "Asia/Kuala_Lumpur",             "lat": 3.1390,   "lon": 101.6869},
    "singapore":        {"tz": "Asia/Singapore",                "lat": 1.3521,   "lon": 103.8198},
    "jakarta":          {"tz": "Asia/Jakarta",                  "lat": -6.2088,  "lon": 106.8456},
    "manila":           {"tz": "Asia/Manila",                   "lat": 14.5995,  "lon": 120.9842},
    "tokyo":            {"tz": "Asia/Tokyo",                    "lat": 35.6762,  "lon": 139.6503},
    "osaka":            {"tz": "Asia/Tokyo",                    "lat": 34.6937,  "lon": 135.5023},
    "beijing":          {"tz": "Asia/Shanghai",                 "lat": 39.9042,  "lon": 116.4074},
    "shanghai":         {"tz": "Asia/Shanghai",                 "lat": 31.2304,  "lon": 121.4737},
    "hong kong":        {"tz": "Asia/Hong_Kong",                "lat": 22.3193,  "lon": 114.1694},
    "taipei":           {"tz": "Asia/Taipei",                   "lat": 25.0330,  "lon": 121.5654},
    "seoul":            {"tz": "Asia/Seoul",                    "lat": 37.5665,  "lon": 126.9780},
    "ulaanbaatar":      {"tz": "Asia/Ulaanbaatar",              "lat": 47.8864,  "lon": 106.9057},

    # ── Africa ────────────────────────────────────────────────────────────
    "cairo":            {"tz": "Africa/Cairo",                  "lat": 30.0444,  "lon": 31.2357},
    "lagos":            {"tz": "Africa/Lagos",                  "lat": 6.5244,   "lon": 3.3792},
    "nairobi":          {"tz": "Africa/Nairobi",                "lat": -1.2921,  "lon": 36.8219},
    "johannesburg":     {"tz": "Africa/Johannesburg",           "lat": -26.2041, "lon": 28.0473},
    "cape town":        {"tz": "Africa/Johannesburg",           "lat": -33.9249, "lon": 18.4241},
    "casablanca":       {"tz": "Africa/Casablanca",             "lat": 33.5731,  "lon": -7.5898},
    "accra":            {"tz": "Africa/Accra",                  "lat": 5.6037,   "lon": -0.1870},
    "addis ababa":      {"tz": "Africa/Addis_Ababa",            "lat": 9.0320,   "lon": 38.7469},
    "dar es salaam":    {"tz": "Africa/Dar_es_Salaam",          "lat": -6.7924,  "lon": 39.2083},
    "khartoum":         {"tz": "Africa/Khartoum",               "lat": 15.5007,  "lon": 32.5599},
    "tunis":            {"tz": "Africa/Tunis",                  "lat": 36.8190,  "lon": 10.1658},
    "algiers":          {"tz": "Africa/Algiers",                "lat": 36.7372,  "lon": 3.0865},

    # ── Oceania ───────────────────────────────────────────────────────────
    "sydney":           {"tz": "Australia/Sydney",              "lat": -33.8688, "lon": 151.2093},
    "melbourne":        {"tz": "Australia/Melbourne",           "lat": -37.8136, "lon": 144.9631},
    "brisbane":         {"tz": "Australia/Brisbane",            "lat": -27.4698, "lon": 153.0251},
    "perth":            {"tz": "Australia/Perth",               "lat": -31.9505, "lon": 115.8605},
    "auckland":         {"tz": "Pacific/Auckland",              "lat": -36.8485, "lon": 174.7633},
    "wellington":       {"tz": "Pacific/Auckland",              "lat": -41.2866, "lon": 174.7756},
}

WEATHER_CODES = {
    0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
    45: "Foggy", 48: "Icy fog",
    51: "Light drizzle", 53: "Moderate drizzle", 55: "Dense drizzle",
    61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
    71: "Slight snow", 73: "Moderate snow", 75: "Heavy snow",
    80: "Slight showers", 81: "Moderate showers", 82: "Violent showers",
    95: "Thunderstorm", 96: "Thunderstorm with hail", 99: "Thunderstorm with heavy hail",
}


def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city."""
    city_info = CITY_DATA.get(city.lower().strip())
    if not city_info:
        return {"status": "error", "error_message": f"No timezone info for '{city}'."}
    tz = pytz.timezone(city_info["tz"])
    now = datetime.datetime.now(tz)
    return {"status": "success", "report": f'Current time in {city.title()}: {now.strftime("%Y-%m-%d %H:%M:%S %Z")}'}


def get_weather(city: str) -> dict:
    """Retrieves the current weather for a specified city."""
    city_info = CITY_DATA.get(city.lower().strip())
    if not city_info:
        return {"status": "error", "error_message": f"No weather info for '{city}'."}
    try:
        url = (
            f"https://api.open-meteo.com/v1/forecast"
            f"?latitude={city_info['lat']}&longitude={city_info['lon']}"
            f"&current=temperature_2m,relative_humidity_2m,wind_speed_10m,weathercode"
        )
        data = requests.get(url, timeout=10).json()
        current = data["current"]
        temp_c = current["temperature_2m"]
        temp_f = round((temp_c * 9 / 5) + 32, 1)
        condition = WEATHER_CODES.get(current["weathercode"], "Unknown")
        return {
            "status": "success",
            "report": (
                f"Weather in {city.title()}: {condition}. "
                f"Temp: {temp_c}°C ({temp_f}°F). "
                f"Humidity: {current['relative_humidity_2m']}%. "
                f"Wind: {current['wind_speed_10m']} km/h."
            ),
        }
    except Exception as e:
        return {"status": "error", "error_message": str(e)}


# Single root agent — NO sub_agents (sub_agents not supported with Groq)
root_agent = Agent(
    name="weather_time_agent",
    model="groq/llama-3.3-70b-versatile",
    description="Agent that answers questions about weather and time in cities.",
    instruction=(
        "You are a helpful assistant that answers questions about the current time "
        "and weather in cities around the world. "
        "Use get_current_time for time questions and get_weather for weather questions. "
        "If asked about both, call both tools and combine the results."
    ),
    tools=[get_weather, get_current_time],
)
