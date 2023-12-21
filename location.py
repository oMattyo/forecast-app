import geopy

class ForecastLocation():
    def __init__(self) -> None:
        self.lat:float
        self.lon:float
    
    def location_request(self, city:str, country:str) -> None:
        # For U.S. users, country = state
        geolocator = geopy.Nominatim(user_agent="Forecast App")
        location = geolocator.geocode(f"{city},{country}")
        self.lat = location.latitude
        self.lon = location.longitude