from model.weather_api import get_weather_and_forecast_data

def map_icon_to_local(icon_code):
    mapping = {
        "01": "sun",
        "02": "sun",
        "03": "cloud",
        "04": "cloud",
        "09": "drizzle",
        "10": "rain",
        "11": "thunderstorm",
        "13": "ice",
        "50": "fog",
    }
    return mapping.get(icon_code[:2], "unknown")


class WeatherController:
    def __init__(self, view):
        self.view = view

    def handle_city_request(self, city_name):
        data = get_weather_and_forecast_data(city_name)
        if data:
            current = data["current"]
            forecast = data["forecast"]

            icon_name = map_icon_to_local(current["icon"])
            self.view.update_weather_data(
                weather=current["weather"],
                temperature=current["temperature"],
                humidity=current["humidity"],
                icon_name=icon_name
            )

            forecast_ui_data = []
            for item in forecast:
                forecast_ui_data.append({
                    "day": item["day"],
                    "temperature": item["temperature"],
                    "icon_name": map_icon_to_local(item["icon"])
                })

            self.view.update_forecast(forecast_ui_data)

        else:
            self.view.show_warning("Nie znaleziono miasta lub błąd API.")