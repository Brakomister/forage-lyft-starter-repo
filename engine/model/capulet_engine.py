from engine.engine import Engine

MILEAGE_PER_SERVICE = 30000


class CapuletEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        return (self.current_mileage - self.last_service_mileage) > MILEAGE_PER_SERVICE
