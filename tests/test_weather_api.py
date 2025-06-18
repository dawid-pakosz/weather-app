from model.weather_api import get_weather_data

def test_valid_city():
    result = get_weather_data("Warszawa")
    assert result is not None, "Nie udało się pobrać danych dla poprawnego miasta"
    assert "temperature" in result
    assert "humidity" in result
    assert "weather" in result

def test_invalid_city():
    result = get_weather_data("Zzzzzz")
    assert result is None, "Powinno zwrócić None dla niepoprawnego miasta"

def test_empty_city():
    result = get_weather_data("")
    assert result is None, "Powinno zwrócić None dla pustego ciągu"

def test_get_weather_data_none():
    result = get_weather_data(None)
    assert result is None

def test_get_weather_data_special_chars():
    result = get_weather_data("!@#$%^&*()")
    assert result is None