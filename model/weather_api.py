import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
CURRENT_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

def get_weather_and_forecast_data(city_name):
    current_params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric",
        "lang": "en"
    }

    forecast_params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric",
        "lang": "en",
        "cnt": 40
    }

    try:
        current_response = requests.get(CURRENT_URL, params=current_params, timeout=5)
        current_response.raise_for_status()
        current_data = current_response.json()

        forecast_response = requests.get(FORECAST_URL, params=forecast_params, timeout=5)
        forecast_response.raise_for_status()
        forecast_data = forecast_response.json()

        current = {
            "weather": current_data["weather"][0]["description"],
            "temperature": int(current_data["main"]["temp"]),
            "humidity": current_data["main"]["humidity"],
            "icon": current_data["weather"][0]["icon"][:2]
        }

        forecast_list = forecast_data["list"]
        forecast_result = []
        today = datetime.today().date()
        day_map = {}

        for item in forecast_list:
            dt = datetime.strptime(item["dt_txt"], "%Y-%m-%d %H:%M:%S")
            forecast_day = dt.date()
            if forecast_day > today:
                if forecast_day not in day_map:
                    day_map[forecast_day] = item
                else:
                    current_best = day_map[forecast_day]
                    if abs(dt.hour - 12) < abs(datetime.strptime(current_best["dt_txt"], "%Y-%m-%d %H:%M:%S").hour - 12):
                        day_map[forecast_day] = item

        for i, (day, item) in enumerate(sorted(day_map.items())):
            if i >= 5:
                break
            forecast_result.append({
                "day": datetime.strptime(item["dt_txt"], "%Y-%m-%d %H:%M:%S").strftime("%A"),
                "temperature": int(item["main"]["temp"]),
                "icon": item["weather"][0]["icon"][:2]
            })
        return {"current": current, "forecast": forecast_result}

    except requests.exceptions.Timeout:
        print("Timeout – serwer nie odpowiada.")
    except requests.exceptions.RequestException as e:
        print(f"Błąd żądania: {e}")
    except Exception as e:
        print(f"Nieoczekiwany błąd: {e}")
    return None