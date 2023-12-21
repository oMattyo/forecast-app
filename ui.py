import tkinter
from location import ForecastLocation
from weather import WeatherForecast
from constants import * 

class ForecastInterface():
    def __init__(self, location:ForecastLocation, weather:WeatherForecast) -> None:
        self.weather = weather
        self.location = location

        # tkinter - main window
        self.window = tkinter.Tk()
        self.window.title("Forecast App")
        self.window.config(padx=20, pady=20, bg=THEME_BG_COLOR)

        # tkinter - location labels
        self.main_label = tkinter.Label(text="Forecast Conditions For:", 
                                        fg=LABEL_COLOR, 
                                        bg=THEME_BG_COLOR, 
                                        font=TITLE_FONT)
        self.main_label.grid(row=0, column=0, columnspan=3, pady=10)

        self.city_label = tkinter.Label(text="City:", 
                                        fg=LABEL_COLOR, 
                                        bg=THEME_BG_COLOR, 
                                        font=LABEL_FONT)
        self.city_label.grid(row=1, column=0, sticky=tkinter.E)

        self.city_label = tkinter.Label(text="Country:", 
                                        fg=LABEL_COLOR, 
                                        bg=THEME_BG_COLOR,
                                        font=LABEL_FONT)
        self.city_label.grid(row=2, column=0, sticky=tkinter.E, pady=(0, 10))

        # tkinter - location entries
        city = tkinter.StringVar()
        country = tkinter.StringVar()

        # TODO - consider adding input validation to prevent numericals from being entered.
        self.city_entry = tkinter.Entry(textvariable=city, font=ENTRY_FONT, bg=ENTRY_BG_COLOR)
        self.city_entry.grid(row=1, column=1, sticky=tkinter.EW)
        self.city_entry.focus()

        # TODO - consider adding input validation to prevent numericals from being entered.
        self.country_entry = tkinter.Entry(textvariable=country, font=ENTRY_FONT, bg=ENTRY_BG_COLOR)
        self.country_entry.grid(row=2, column=1, sticky=tkinter.EW, pady=(0, 10))

        # tkinter - button
        self.get_forecast_btn = tkinter.Button(text="Get Forecast", 
                                               highlightthickness=0, 
                                               command=lambda: self.fill_forecast_info(city.get(), country.get()),
                                               font=BTN_FONT)
        self.get_forecast_btn.grid(row=3,column=0, columnspan=3, sticky=tkinter.EW, padx=(20, 20), pady=(0, 20))

        # tkinter - Forecast canvas'
            # tkinter Forecast One - canvas
        self.forecast_one_canvas = tkinter.Canvas(width=320, height=140, bg=LIGHT_BG_COLOR)

        self.fcast_one_condition = self.forecast_one_canvas.create_text(160, 30, width=300,
                                                                           text="Condition: ----",
                                                                           fill=VALUE_COLOR,
                                                                           font=VALUE_FONT)
        self.fcast_one_clouds = self.forecast_one_canvas.create_text(160, 70, width=300,
                                                                           text="Cloud Coverage: ----",
                                                                           fill=VALUE_COLOR,
                                                                           font=VALUE_FONT)
        self.fcast_one_dt = self.forecast_one_canvas.create_text(160, 110, width=300,
                                                                           text="Date : Time",
                                                                           fill=VALUE_COLOR,
                                                                           font=DT_FONT)
        self.forecast_one_canvas.grid(row=4, column=0, columnspan=3)
            # tkinter Forecast Two - canvas
        self.forecast_two_canvas = tkinter.Canvas(width=320, height=140, bg="white")

        self.fcast_two_condition = self.forecast_two_canvas.create_text(160, 30, width=300,
                                                                           text="Condition: ----",
                                                                           fill=VALUE_COLOR,
                                                                           font=VALUE_FONT)
        self.fcast_two_clouds = self.forecast_two_canvas.create_text(160, 70, width=300,
                                                                           text="Cloud Coverage: ----",
                                                                           fill=VALUE_COLOR,
                                                                           font=VALUE_FONT)
        self.fcast_two_dt = self.forecast_two_canvas.create_text(160, 110, width=300,
                                                                           text="Date : Time",
                                                                           fill=VALUE_COLOR,
                                                                           font=DT_FONT)
        self.forecast_two_canvas.grid(row=5, column=0, columnspan=3)
            # tkinter Forecast Three - canvas
        self.forecast_three_canvas = tkinter.Canvas(width=320, height=140, bg="white")

        self.fcast_three_condition = self.forecast_three_canvas.create_text(160, 30, width=300,
                                                                           text="Condition: ----",
                                                                           fill=VALUE_COLOR,
                                                                           font=VALUE_FONT)
        self.fcast_three_clouds = self.forecast_three_canvas.create_text(160, 70, width=300,
                                                                           text="Cloud Coverage: ----",
                                                                           fill=VALUE_COLOR,
                                                                           font=VALUE_FONT)
        self.fcast_three_dt = self.forecast_three_canvas.create_text(160, 110, width=300,
                                                                           text="Date : Time",
                                                                           fill=VALUE_COLOR,
                                                                           font=DT_FONT)
        self.forecast_three_canvas.grid(row=6, column=0, columnspan=3)
            # tkinter Forecast Four - canvas
        self.forecast_four_canvas = tkinter.Canvas(width=320, height=140, bg="white")

        self.fcast_four_condition = self.forecast_four_canvas.create_text(160, 30, width=300,
                                                                           text="Condition: ----",
                                                                           fill=VALUE_COLOR,
                                                                           font=VALUE_FONT)
        self.fcast_four_clouds = self.forecast_four_canvas.create_text(160, 70, width=300,
                                                                           text="Cloud Coverage: ----",
                                                                           fill=VALUE_COLOR,
                                                                           font=VALUE_FONT)
        self.fcast_four_dt = self.forecast_four_canvas.create_text(160, 110, width=300,
                                                                           text="Date : Time",
                                                                           fill=VALUE_COLOR,
                                                                           font=DT_FONT)
        self.forecast_four_canvas.grid(row=7, column=0, columnspan=3)

        # tkinter mainloop
        self.window.mainloop()

    def fill_forecast_info(self, city:str, country:str) -> None:
        self.location.location_request(city, country)
        self.weather.forecast_request(self.location.lat, self.location.lon)

        # TODO - Consider a refactor where you loop through canvas widgets to fill with data
        # config forecast one canvas with data
        self.forecast_one_canvas.itemconfig(self.fcast_one_condition, text=f"Condition: {self.weather.w_conditions[0].condition.capitalize()}")
        self.forecast_one_canvas.itemconfig(self.fcast_one_clouds, text=f"Cloud Coverage: {self.weather.w_conditions[0].cloud_coverage}%")
        self.forecast_one_canvas.itemconfig(self.fcast_one_dt, text=f"{self.weather.w_conditions[0].date} | {self.weather.w_conditions[0].time}")
        # config forecast two canvas with data
        self.forecast_two_canvas.itemconfig(self.fcast_two_condition, text=f"Condition: {self.weather.w_conditions[1].condition.capitalize()}")
        self.forecast_two_canvas.itemconfig(self.fcast_two_clouds, text=f"Cloud Coverage: {self.weather.w_conditions[1].cloud_coverage}%")
        self.forecast_two_canvas.itemconfig(self.fcast_two_dt, text=f"{self.weather.w_conditions[1].date} | {self.weather.w_conditions[1].time}")
        # config forecast three canvas with data
        self.forecast_three_canvas.itemconfig(self.fcast_three_condition, text=f"Condition: {self.weather.w_conditions[2].condition.capitalize()}")
        self.forecast_three_canvas.itemconfig(self.fcast_three_clouds, text=f"Cloud Coverage: {self.weather.w_conditions[2].cloud_coverage}%")
        self.forecast_three_canvas.itemconfig(self.fcast_three_dt, text=f"{self.weather.w_conditions[2].date} | {self.weather.w_conditions[2].time}")
        # config forecast four canvas with data
        self.forecast_four_canvas.itemconfig(self.fcast_four_condition, text=f"Condition: {self.weather.w_conditions[3].condition.capitalize()}")
        self.forecast_four_canvas.itemconfig(self.fcast_four_clouds, text=f"Cloud Coverage: {self.weather.w_conditions[3].cloud_coverage}%")
        self.forecast_four_canvas.itemconfig(self.fcast_four_dt, text=f"{self.weather.w_conditions[3].date} | {self.weather.w_conditions[3].time}")


