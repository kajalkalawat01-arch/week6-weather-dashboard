# Weather Dashboard

A Python-based Weather Dashboard that displays current weather and a 5-day forecast.

## Features
- Search weather by city name
- Display temperature and feels-like temperature
- Show humidity and wind speed
- Display 5-day weather forecast
- Save favorite cities
- Cache weather data
- Refresh weather information
- Handle API and network errors

## Technologies Used
- Python
- OpenWeatherMap API
- Requests
- JSON
- Python-dotenv

## Installation

Install the required packages:

pip install -r requirements.txt

## API Configuration

1. Get an API key from OpenWeatherMap.
2. Create a `.env` file in the project folder.
3. Add this line:

OPENWEATHER_API_KEY=your_api_key_here

Replace it with your actual API key.

## Run the Project

python -m weather_app.main

## Run Tests

python -m unittest discover -s tests

## Author

Python Developer Intern
