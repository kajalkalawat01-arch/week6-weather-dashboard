from datetime import datetime


def parse_current_weather(data):
    return {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"].title(),
        "wind_speed": data["wind"]["speed"]
    }


def parse_forecast(data):
    daily = {}

    for item in data["list"]:
        date = datetime.fromtimestamp(item["dt"]).strftime("%Y-%m-%d")

        if date not in daily:
            daily[date] = []

        daily[date].append(item["main"]["temp"])

    forecast = []

    for date, temperatures in list(daily.items())[:5]:
        forecast.append({
            "date": date,
            "min_temp": min(temperatures),
            "max_temp": max(temperatures)
        })

    return forecast
