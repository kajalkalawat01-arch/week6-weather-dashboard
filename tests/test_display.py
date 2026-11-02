import unittest

from weather_app.weather_display import (
    display_current_weather,
    display_forecast
)


class TestWeatherDisplay(unittest.TestCase):

    def test_display_current_weather(self):
        weather = {
            "city": "Bhopal",
            "country": "IN",
            "temperature": 30,
            "feels_like": 32,
            "description": "Clear Sky",
            "humidity": 60,
            "wind_speed": 5
        }

        result = display_current_weather(weather)

        self.assertIn("Bhopal", result)
        self.assertIn("30", result)
        self.assertIn("60%", result)

    def test_display_forecast(self):
        forecast = [
            {
                "date": "2026-11-02",
                "min_temp": 20,
                "max_temp": 30
            }
        ]

        result = display_forecast(forecast)

        self.assertIn("5-Day Weather Forecast", result)
        self.assertIn("20°C", result)
        self.assertIn("30°C", result)


if __name__ == "__main__":
    unittest.main()
