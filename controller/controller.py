# from model.weather_api import get_weather_data
#
# def map_icon_to_local(icon_code):
#     mapping = {
#         "01": "sun",            # czyste niebo
#         "02": "sun",            # małe zachmurzenie
#         "03": "cloud",          # zachmurzenie umiarkowane
#         "04": "cloud",          # duże zachmurzenie
#         "09": "drizzle",        # mżawka
#         "10": "rain",           # deszcz
#         "11": "thunderstorm",   # burza
#         "13": "ice",            # śnieg
#         "50": "fog",            # mgła
#     }
#     return mapping.get(icon_code[:2], "unknown")  # użyj np. '10d'[:2] = '10'
#
# class WeatherController:
#     def __init__(self, view):
#         self.view = view
#
#     def handle_city_request(self, city_name):
#         data = get_weather_data(city_name)
#         if data:
#             icon_name = map_icon_to_local(data["icon"])
#             self.view.update_weather_data(
#                 weather=data["weather"],
#                 temperature=data["temperature"],
#                 humidity=data["humidity"],
#                 icon_name=icon_name
#             )
#         else:
#             self.view.show_warning("Nie znaleziono miasta lub błąd API.")




from model.weather_api import get_weather_and_forecast_data

def map_icon_to_local(icon_code):
    mapping = {
        "01": "sun",            # czyste niebo
        "02": "sun",            # małe zachmurzenie
        "03": "cloud",          # zachmurzenie umiarkowane
        "04": "cloud",          # duże zachmurzenie
        "09": "drizzle",        # mżawka
        "10": "rain",           # deszcz
        "11": "thunderstorm",   # burza
        "13": "ice",            # śnieg
        "50": "fog",            # mgła
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

            # Przekazanie prognozy
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