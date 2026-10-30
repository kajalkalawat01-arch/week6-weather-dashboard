import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

API_KEY = os.getenv("OPENWEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5"

DATA_DIR = BASE_DIR / "data"
CACHE_DIR = DATA_DIR / "cache"
FAVORITES_FILE = DATA_DIR / "favorites.json"

CACHE_DURATION = 600
