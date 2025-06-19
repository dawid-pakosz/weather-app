# import requests
#
# API_KEY = "23d5e4be716cffdf49784bf56fa6d380"
# BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
#
# def get_weather_data(city_name):
#     params = {
#         "q": city_name,
#         "appid": API_KEY,
#         "units": "metric",
#         "lang": "pl"
#     }
#
#     try:
#         response = requests.get(BASE_URL, params=params, timeout=5)
#         response.raise_for_status()  # Rzuca wyjątek dla błędów HTTP (np. 404)
#         data = response.json()
#         return {
#             "weather": data["weather"][0]["description"],
#             "temperature": int(data["main"]["temp"]),
#             "humidity": data["main"]["humidity"],
#             "icon": data["weather"][0]["icon"][:2]
#         }
#     except requests.exceptions.Timeout:
#         print("Błąd: timeout – serwer nie odpowiada.")
#     except requests.exceptions.RequestException as e:
#         print(f"Błąd żądania: {e}")
#     except Exception as e:
#         print(f"Nieoczekiwany błąd: {e}")
#     return None



import requests
from datetime import datetime, timedelta

API_KEY = "23d5e4be716cffdf49784bf56fa6d380"
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
        "cnt": 40  # 5 dni x 8 pomiarów co 3h = 40
    }

    try:
        current_response = requests.get(CURRENT_URL, params=current_params, timeout=5)
        current_response.raise_for_status()
        current_data = current_response.json()

        forecast_response = requests.get(FORECAST_URL, params=forecast_params, timeout=5)
        forecast_response.raise_for_status()
        forecast_data = forecast_response.json()

        # aktualna pogoda
        current = {
            "weather": current_data["weather"][0]["description"],
            "temperature": int(current_data["main"]["temp"]),
            "humidity": current_data["main"]["humidity"],
            "icon": current_data["weather"][0]["icon"][:2]
        }

        # prognoza na najbliższe 5 dni
        forecast_list = forecast_data["list"]
        forecast_result = []
        today = datetime.today().date()
        day_map = {}

        for item in forecast_list:
            dt = datetime.strptime(item["dt_txt"], "%Y-%m-%d %H:%M:%S")
            forecast_day = dt.date()
            if forecast_day > today:
                # Pierwszy wpis w danym dniu — zapisz jako najlepszy kandydat
                if forecast_day not in day_map:
                    day_map[forecast_day] = item
                else:
                    # Nadpisz, jeśli godzina jest bliżej 12:00
                    current_best = day_map[forecast_day]
                    if abs(dt.hour - 12) < abs(datetime.strptime(current_best["dt_txt"], "%Y-%m-%d %H:%M:%S").hour - 12):
                        day_map[forecast_day] = item

        # Zamień day_map na forecast_result i zatrzymaj się po 5 dniach
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
        print("❌ Timeout – serwer nie odpowiada.")
    except requests.exceptions.RequestException as e:
        print(f"❌ Błąd żądania: {e}")
    except Exception as e:
        print(f"❌ Nieoczekiwany błąd: {e}")

    return None


