# main.py

# from view.main_view import MainView
#
#
# def mock_controller(city_name):
#     print(f"Pobrano dane dla miasta: {city_name}")
#     app.display_weather(f"Przykładowa pogoda dla {city_name}:\n🌡️ 21°C\n☁️ Częściowo pochmurno")
#
#
# if __name__ == "__main__":
#     app = MainView(mock_controller)
#     app.mainloop()




# po refaktoryzacji
from view.main_view import MainView


def mock_controller(city_name):
    print(f"Pobrano dane dla miasta: {city_name}")
    app.update_weather_data(
        weather="Częściowo pochmurno",
        temperature=21,
        humidity=65,
        icon_name="cloud"  # nazwa pliku PNG w folderze icons
    )


if __name__ == "__main__":
    app = MainView(controller=mock_controller)
    app.mainloop()
