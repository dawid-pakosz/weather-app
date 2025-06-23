from view.main_view import MainView
from controller.controller import WeatherController

if __name__ == "__main__":
    app = MainView(controller=None)
    controller = WeatherController(view=app)
    app.controller = controller.handle_city_request
    app.mainloop()
