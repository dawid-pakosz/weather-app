# Weather App

A modern weather application written in Python with a graphical user interface (Tkinter).  
This project was developed as a final assignment for postgraduate studies in Python Development.

## Features

- Search for current weather by city name
- Displays temperature, humidity, and weather description
- Clean, modern GUI inspired by HTML/CSS web apps
- Error handling and user-friendly warnings
- "Clear" button to reset all fields and results

## Installation

1. **Clone the repository:**
git clone https://github.com/dawid-pakosz/weather-app.git
cd weather-app


2. **Install required libraries:**
pip install -r requirements.txt
*If you don't have `requirements.txt`, install manually:*
pip install pillow requests


3. **Run the application:**
python main.py

## Usage

- Enter a city name in the search field and click "SEND".
- Weather results will be displayed at the bottom of the window.
- Use the "Clear" button to reset the search and results.
- If an error occurs (e.g., invalid city name), a warning message will be shown and previous results will be cleared.

## Requirements

- Python 3.8+
- Libraries: `tkinter`, `Pillow`, `requests`

## Project Structure

weather_app/
├── controller/
│   ├── __init__.py
│   └── controller.py
├── model/
│   ├── __init__.py
│   └── weather_api.py
├── resources/
│   └── icons/
│       ├── cloud.png
│       ├── drizzle.png
│       ├── fog.png
│       ├── ice.png
│       ├── rain.png
│       ├── sun.png
│       ├── thunderstorm.png
│       └── unknown.png
├── tests/
│   ├── __init__.py
│   └── test_weather_api.py
├── view/
│   ├── __init__.py
│   └── main_view.py
├── .env
├── .env.example
├── .gitignore
├── main.py
├── README.md
└── requirements.txt



## Author

Dawid Pakosz  
Contact: dawid.pakosz@gmail.com
LinkedIn: [linkedin.com/in/dawid-pakosz](https://www.linkedin.com/in/dawid-pakosz)

## Featured on LinkedIn

This project has been showcased on my [LinkedIn profile](https://www.linkedin.com/in/dawid-pakosz).  
Feel free to connect or leave feedback!

## License

This project was created for educational purposes.  



