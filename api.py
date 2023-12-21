import os
from dotenv import load_dotenv

load_dotenv("C:/Users/a3Eck/Projects/env_files/Python/.env")

# Weather API website - https://openweathermap.org/
OW_BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"
OW_API_KEY = os.getenv("OW_API_KEY")
