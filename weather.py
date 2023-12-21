import requests
from conditions import Conditions
from api import OW_API_KEY, OW_BASE_URL

class WeatherForecast():
    def __init__(self) -> None:
        self.w_conditions:list
    
    def forecast_request(self, lat:float, lon:float) -> None:
        params = {"lat":lat, "lon":lon, "appid":OW_API_KEY, "cnt":4}

        response = requests.get(OW_BASE_URL, params)
        response.raise_for_status()
        data = response.json()
        forecast_data = data["list"]

        self.w_conditions = [Conditions(condition=item["weather"][0]["description"], cloud_coverage=item["clouds"]["all"], 
                                 date_time=item["dt"]) for item in forecast_data]        