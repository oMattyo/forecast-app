from location import ForecastLocation
from weather import WeatherForecast
from ui import ForecastInterface

location = ForecastLocation()
weather = WeatherForecast()

ui = ForecastInterface(location, weather)
