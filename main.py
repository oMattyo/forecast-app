import requests
from ui import ForecastInterface
from api import OW_BASE_URL, OW_API_KEY

# Test API call with API Key and Base Url
params = {"lat":50, "lon":50, "appid":OW_API_KEY, "cnt":4}

response = requests.get(OW_BASE_URL, params)
response.raise_for_status()
data = response.json()
forecast_data = data["list"]

print(forecast_data)

ui = ForecastInterface()
