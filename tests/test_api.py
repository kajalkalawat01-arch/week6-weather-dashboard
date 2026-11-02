import unittest
from unittest.mock import Mock

from weather_app.weather_api import WeatherAPI


class TestWeatherAPI(unittest.TestCase):

    def setUp(self):
        self.api = WeatherAPI(api_key="test_key")
        self.api.session.get = Mock()

    def test_get_current_weather(self):
        mock_response = Mock()
        mock_response.json.return_value = {"name": "Bhopal"}
        self.api.session.get.return_value = mock_response

        result = self.api.get_current_weather("Bhopal")

        self.assertEqual(result["name"], "Bhopal")

    def test_get_forecast(self):
        mock_response = Mock()
        mock_response.json.return_value = {"list": []}
        self.api.session.get.return_value = mock_response

        result = self.api.get_forecast("Bhopal")

        self.assertEqual(result["list"], [])


if __name__ == "__main__":
    unittest.main()
