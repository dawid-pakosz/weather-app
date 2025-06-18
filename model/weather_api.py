import requests

API_KEY = "23d5e4be716cffdf49784bf56fa6d380"  # <- uzupełnij własnym
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather_data(city_name):
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric",
        "lang": "pl"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=5)
        response.raise_for_status()  # Rzuca wyjątek dla błędów HTTP (np. 404)
        data = response.json()
        return {
            "weather": data["weather"][0]["description"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "icon": data["weather"][0]["icon"][:2]
        }
    except requests.exceptions.Timeout:
        print("Błąd: timeout – serwer nie odpowiada.")
    except requests.exceptions.RequestException as e:
        print(f"Błąd żądania: {e}")
    except Exception as e:
        print(f"Nieoczekiwany błąd: {e}")

    return None

# def get_weather_data(city_name):
#     params = {
#         "q": city_name,
#         "appid": API_KEY,
#         "units": "metric",
#         "lang": "pl"
#     }
#
#     try:
#         response = requests.get(BASE_URL, params=params)
#         if response.status_code == 200:
#             data = response.json()
#             return {
#                 "weather": data["weather"][0]["description"],
#                 "temperature": data["main"]["temp"],
#                 "humidity": data["main"]["humidity"],
#                 "icon": data["weather"][0]["icon"][:2]
#             }
#     except Exception as e:
#         print(f"Błąd podczas pobierania danych: {e}")
#     return None


