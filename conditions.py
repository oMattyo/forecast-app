from datetime import datetime

class Conditions():
    def __init__(self, condition:str, cloud_coverage:int, date_time:str) -> None:
        self.condition = condition
        self.cloud_coverage = cloud_coverage
        self.format_date_time(date_time)
        self.date:str
        self.time:str

    def format_date_time(self, date_time:str) -> None:
        dt_string = datetime.fromtimestamp(date_time)
        self.date = dt_string.strftime("%d %B, %Y")
        self.time = dt_string.strftime("%I:%M:%S %p")