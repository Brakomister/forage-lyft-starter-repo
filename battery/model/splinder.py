from battery.battery import Battery


class SplinderBattery(Battery):
    def __init__(self,  current_date, last_service_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        self.service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)

    def needs_service(self):
        return self.current_date > self.service_threshold_date
