import requests
from .config import API_KEY, BASE_URL


class WeatherAPI:
    def __init__(self, api_key=None):
        self.api_key = api_key or API_KEY
        self.session = requests.Session()

    def _get_data(self, endpoint, city):
        if not self.api_key:
            raise ValueError(
                "API key missing. Please add it to your .env file."
            )

        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }

        url = f"{BASE_URL}/{endpoint}"

        try:
            response = self.session.get(
                url, params=params, timeout=10
            )
            response.raise_for_status()
            return response.json()

        except requests.exceptions.HTTPError as error:
            if response.status_code == 404:
                raise ValueError("City not found.") from error
            if response.status_code == 401:
                raise ValueError("Invalid API key.") from error
            raise RuntimeError("Weather service error.") from error

        except requests.exceptions.RequestException as error:
            raise RuntimeError(
                "Network error. Please check your internet."
            ) from error

    def get_current_weather(self, city):
        return self._get_data("weather", city)

    def get_forecast(self, city):
        return self._get_data("forecast", city)
