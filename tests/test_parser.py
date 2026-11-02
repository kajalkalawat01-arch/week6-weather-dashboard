import unittest
from datetime import datetime

from weather_app.weather_parser import (
    parse_current_weather,
    parse_forecast
)


class TestWeatherParser(unittest.TestCase):

    def test_parse_current_weather(self):
        data = {
            "name": "Bhopal",
            "sys": {"country": "IN"},
            "main": {
                "temp": 30,
                "feels_like": 32,
                "humidity": 60
            },
            "weather": [{"description": "clear sky"}],
            "wind": {"speed": 5}
        }

        result = parse_current_weather(data)

        self.assertEqual(result["city"], "Bhopal")
        self.assertEqual(result["temperature"], 30)
        self.assertEqual(result["humidity"], 60)

    def test_parse_forecast(self):
        timestamp = int(datetime.now().timestamp())

        data = {
            "list": [
                {
                    "dt": timestamp,
                    "main": {"temp": 25}
                },
                {
                    "dt": timestamp + 3600,
                    "main": {"temp": 30}
                }
            ]
        }

        result = parse_forecast(data)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["min_temp"], 25)
        self.assertEqual(result[0]["max_temp"], 30)


if __name__ == "__main__":
    unittest.main()
