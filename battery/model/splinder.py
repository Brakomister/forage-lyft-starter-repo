from battery.battery import Battery
from datetime import datetime as dt


class SplinderBattery(Battery):
    def __init__(self, last_service_date, current_service_date):
        self.last_service_date = last_service_date
        self.current_service_date = current_service_date
        self.service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)

    def needs_service(self):
        return dt.today() > self.service_threshold_date
