# from view.main_view import MainView
#
#
# def mock_controller(city_name):
#     print(f"Pobrano dane dla miasta: {city_name}")
#     app.update_weather_data(
#         weather="Częściowo pochmurno",
#         temperature=21,
#         humidity=65,
#         icon_name="cloud"  # nazwa pliku PNG w folderze icons
#     )
#
#
# if __name__ == "__main__":
#     app = MainView(controller=mock_controller)
#     app.mainloop()



from view.main_view import MainView
from controller.controller import WeatherController


if __name__ == "__main__":
    app = MainView(controller=None)  # najpierw bez kontrolera
    controller = WeatherController(view=app)
    app.controller = controller.handle_city_request
    app.mainloop()
