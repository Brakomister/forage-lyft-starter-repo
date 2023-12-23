from carfactory.car import Car
from engine.model.capulet_engine import *
from engine.model.willoughby_engine import *
from engine.model.sternman_engine import *
from battery.model.nubbin import *
from battery.model.splinder import *


class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SplinderBattery(current_date, last_service_date)
        return Car(engine, battery)

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SplinderBattery(current_date, last_service_date)
        return Car(engine, battery)

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_is_on):
        engine = SternmanEngine(warning_is_on)
        battery = SplinderBattery(current_date, last_service_date)
        return Car(engine, battery)

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        return Car(engine, battery)

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        return Car(engine, battery)
