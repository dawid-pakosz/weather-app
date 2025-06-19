# Weather App – aplikacja pogodowa w Pythonie

Aplikacja desktopowa do wyświetlania bieżącej pogody oraz prognozy 5-dniowej dla wybranego miasta. 
Zbudowana w architekturze MVC z wykorzystaniem biblioteki `tkinter`, `Pillow`, `requests` oraz API OpenWeatherMap.

---

## Funkcje

- Wyszukiwanie pogody po nazwie miasta
- Wyświetlanie aktualnych danych:
  - pogoda (opis, temperatura, wilgotność)
  - ikona pogody
- Prognoza 5-dniowa:
  - dzień tygodnia
  - temperatura
  - ikonka
- Eksport danych do CSV / TXT
- Przycisk do czyszczenia danych
- Obsługa błędów i walidacja

---

## Jak uruchomić projekt

1. Sklonuj repozytorium:
git clone https://github.com/dawid-pakosz/weather-app.git
cd weather-app

2. Utwórz i aktywuj środowisko wirtualne (opcjonalnie):
python -m venv venv
venv\Scripts\activate

3. Zainstaluj zależności
pip install -r requirements.txt

4. Dodaj swój klucz API do pliku .env:
API_KEY=tu_wklej_swoj_klucz_api

5. Uruchom aplikacje
python main.py

6. Testy
pytest tests/
