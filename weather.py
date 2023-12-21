import requests
from api import OW_API_KEY, OW_BASE_URL

class WeatherForecast():
    def __init__(self) -> None:
        self.w_conditions:list
    
    def forecast_request(self, lat:float, lon:float) -> None:
        # TODO take in lat, lon from a call to geopy based on city, country input in ui
        params = {"lat":50, "lon":50, "appid":OW_API_KEY, "cnt":4}

        response = requests.get(OW_BASE_URL, params)
        response.raise_for_status()
        data = response.json()
        forecast_data = data["list"]
        print(forecast_data)
        # TODO extract forecast_data into a condition object from condition class
        # self.w_conditions = []