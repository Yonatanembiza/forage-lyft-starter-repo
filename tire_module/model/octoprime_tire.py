
from tire_module.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, wear_sensor):
        self.wear_sensor = wear_sensor
    def needs_service(self):
        sum = 0
        for wear in self.wear_sensor:
            sum += wear
        return sum >= 3
