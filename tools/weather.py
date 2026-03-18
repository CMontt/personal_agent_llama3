import requests
from config.settings import API_WEATHER_URL

def weather(city: str) -> str:
    url = API_WEATHER_URL.format(city=city)

    try:
        data = requests.get(url).json()

        current = data["current_condition"][0]
        temp = current["temp_C"]
        feels_like = current["FeelsLikeC"]
        humidity = current["humidity"]
        chance_rain = current.get("precipMM", "0") 
        desc = current["weatherDesc"][0]["value"]

        return (
            f"Weather in {city}:\n"
            f"- Temperature: {temp}°C\n"
            f"- Feels like: {feels_like}°C\n"
            f"- Humidity: {humidity}%\n"
            f"- Precipitation (mm): {chance_rain}\n"
            f"- Condition: {desc}"
        )
    except Exception:
        return "Weather data unavailable"