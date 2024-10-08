from battery_module.model.nubbin_battery import NubbinBattery
from battery_module.model.spindler_battery import SpindlerBattery
from car_module.car import Car
from engine_module.model.capulet_engine import CapuletEngine
from engine_module.model.sternman_engine import SternmanEngine
from engine_module.model.willoughby_engine import WilloughbyEngine
from tire_module.model.carrigan_tire import CarriganTire
from tire_module.model.octoprime_tire import OctoprimeTire

class CarFactory:

    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, wear_sensor):
        engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        battery = SpindlerBattery(last_service_date=last_service_date, current_date=current_date)
        tire = CarriganTire(wear_sensor=wear_sensor)
        
        return Car(engine=engine, battery=battery, tire=tire)

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, wear_sensor):
        engine = WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        battery = SpindlerBattery(last_service_date=last_service_date, current_date=current_date)
        tire = OctoprimeTire(wear_sensor=wear_sensor)

        return Car(engine=engine, battery=battery, tire=tire)

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on, wear_sensor):
        engine = SternmanEngine(warning_light_on=warning_light_on)
        battery = SpindlerBattery(last_service_date=last_service_date, current_date=current_date)
        tire = CarriganTire(wear_sensor=wear_sensor)

        return Car(engine=engine, battery=battery, tire=tire)

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, wear_sensor):
        engine = WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        battery = NubbinBattery(last_service_date=last_service_date, current_date=current_date)
        tire = OctoprimeTire(wear_sensor=wear_sensor)

        return Car(engine=engine, battery=battery, tire=tire)

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, wear_sensor):
        engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        battery = NubbinBattery(last_service_date=last_service_date, current_date=current_date)
        tire = CarriganTire(wear_sensor=wear_sensor)

        return Car(engine=engine, battery=battery, tire=tire)   
