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
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            return {
                "weather": data["weather"][0]["description"],
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "icon": data["weather"][0]["icon"][:2]
            }
    except Exception as e:
        print(f"Błąd podczas pobierania danych: {e}")
    return None

#Test
if __name__ == "__main__":
    result = get_weather_data("Warszawa")
    print(result)
