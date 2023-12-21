import os
from dotenv import load_dotenv

load_dotenv("C:/Users/a3Eck/Projects/env_files/Python/.env")

# Weather API website - https://openweathermap.org/
OW_BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"
OW_API_KEY = os.getenv("OW_API_KEY")

# If you don't want to use dotenv:
# You can fun the following: pip uninstall python-dotenv
# and then just add your API KEY following the example below

# OW_API_KEY = "<your_api_key_here>"
