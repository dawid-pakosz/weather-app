# controller.py – szkielet pliku

from model.weather_api import get_weather_data

class WeatherController:
    def __init__(self, view):
        self.view = view

    def handle_city_request(self, city_name):
        data = get_weather_data(city_name)
        if data:
            self.view.update_weather_data(
                weather=data["weather"],
                temperature=data["temperature"],
                humidity=data["humidity"],
                icon_name=data["icon"]
            )
        else:
            self.view.show_warning("Nie znaleziono miasta lub błąd API.")
