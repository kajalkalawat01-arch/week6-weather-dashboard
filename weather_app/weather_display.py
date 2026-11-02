def display_current_weather(weather):
    return (
        f"\nWeather in {weather['city']}, {weather['country']}\n"
        f"Temperature: {weather['temperature']}°C\n"
        f"Feels Like: {weather['feels_like']}°C\n"
        f"Condition: {weather['description']}\n"
        f"Humidity: {weather['humidity']}%\n"
        f"Wind Speed: {weather['wind_speed']} m/s\n"
    )


def display_forecast(forecast):
    result = "\n5-Day Weather Forecast\n"

    for day in forecast:
        result += (
            f"{day['date']}: "
            f"Min {day['min_temp']}°C, "
            f"Max {day['max_temp']}°C\n"
        )

    return result
