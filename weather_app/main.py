import json
from pathlib import Path

from .config import CACHE_DIR, FAVORITES_FILE
from .weather_api import WeatherAPI
from .weather_parser import parse_current_weather, parse_forecast
from .weather_display import display_current_weather, display_forecast


api = WeatherAPI()


def load_cache(city):
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    file_path = CACHE_DIR / f"{city.lower()}.json"

    if file_path.exists():
        with open(file_path, "r") as file:
            return json.load(file)

    return None


def save_cache(city, current, forecast):
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    file_path = CACHE_DIR / f"{city.lower()}.json"

    with open(file_path, "w") as file:
        json.dump({
            "current": current,
            "forecast": forecast
        }, file, indent=4)


def load_favorites():
    if FAVORITES_FILE.exists():
        with open(FAVORITES_FILE, "r") as file:
            return json.load(file)

    return []


def add_favorite(city):
    favorites = load_favorites()

    if city not in favorites:
        favorites.append(city)

        FAVORITES_FILE.parent.mkdir(parents=True, exist_ok=True)

        with open(FAVORITES_FILE, "w") as file:
            json.dump(favorites, file, indent=4)

        print("City added to favorites!")
    else:
        print("City is already in favorites.")


def show_weather(city, refresh=False):
    try:
        cached_data = None if refresh else load_cache(city)

        if cached_data:
            print("\nShowing cached weather data...")
            current = cached_data["current"]
            forecast = cached_data["forecast"]
        else:
            print("\nFetching weather data...")
            current_data = api.get_current_weather(city)
            forecast_data = api.get_forecast(city)

            current = parse_current_weather(current_data)
            forecast = parse_forecast(forecast_data)

            save_cache(city, current, forecast)

        print(display_current_weather(current))
        print(display_forecast(forecast))

    except (ValueError, RuntimeError) as error:
        print("Error:", error)


def main():
    print("===== WEATHER DASHBOARD =====")

    while True:
        print("\n1. Search City Weather")
        print("2. Refresh Weather")
        print("3. View Favorites")
        print("4. Add Favorite City")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            city = input("Enter city name: ").strip()
            if city:
                show_weather(city)

        elif choice == "2":
            city = input("Enter city name: ").strip()
            if city:
                show_weather(city, refresh=True)

        elif choice == "3":
            favorites = load_favorites()
            print("\nFavorite Cities:", favorites)

        elif choice == "4":
            city = input("Enter city name: ").strip()
            if city:
                add_favorite(city)

        elif choice == "5":
            print("Thank you for using Weather Dashboard!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
