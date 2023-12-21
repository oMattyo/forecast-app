import tkinter
from constants import * 

class ForecastInterface():
    def __init__(self) -> None:
        # tkinter - main window
        self.window = tkinter.Tk()
        self.window.title("Forecast App")
        self.window.config(padx=20, pady=20, bg=THEME_BG_COLOR)

        # tkinter - location labels
        self.main_label = tkinter.Label(text="Forecast Conditions For:", 
                                        fg=TITLE_COLOR, 
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

        self.city_entry = tkinter.Entry(textvariable=city, font=ENTRY_FONT)
        self.city_entry.grid(row=1, column=1, sticky=tkinter.EW)
        self.city_entry.focus()

        self.country_entry = tkinter.Entry(textvariable=country, font=ENTRY_FONT)
        self.country_entry.grid(row=2, column=1, sticky=tkinter.EW, pady=(0, 10))



        self.window.mainloop()

