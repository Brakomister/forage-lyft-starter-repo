from car import Car
from engine.model.capulet_engine import *
from engine.model.willoughby_engine import *
from engine.model.sternman_engine import *
from battery.model.nubbin import *
from battery.model.spindler import *
from tires.model.carrigan import Carrigan
from tires.model.octoprime import Octoprime


class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tires):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = Carrigan(tires)
        return Car(engine, battery, tires)

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tires):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = Octoprime(tires)
        return Car(engine, battery, tires)

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_is_on, tires):
        engine = SternmanEngine(warning_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = Carrigan(tires)
        return Car(engine, battery, tires)

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tires):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = Octoprime(tires)
        return Car(engine, battery, tires)

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tires):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = Carrigan(tires)
        return Car(engine, battery, tires)
