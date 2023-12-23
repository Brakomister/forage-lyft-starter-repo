from engine.engine import Engine


class SternmanEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage, warning_light_on):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.warning_light_on = warning_light_on

    def needs_service(self):
        return self.warning_light_on
