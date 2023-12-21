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
                                        font=LABLE_FONT)
        self.city_label.grid(row=1, column=0, sticky=tkinter.W)

        self.city_label = tkinter.Label(text="Country:", 
                                        fg=LABEL_COLOR, 
                                        bg=THEME_BG_COLOR, 
                                        font=LABLE_FONT)
        self.city_label.grid(row=3, column=0, sticky=tkinter.W, pady=(0, 10))


        self.window.mainloop()

