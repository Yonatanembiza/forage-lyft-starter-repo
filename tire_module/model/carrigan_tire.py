
from tire_module.tire import Tire


class CarriganTire(Tire):
    def __init__(self, wear_sensor):
        self.wear_sensor = wear_sensor
    def needs_service(self):
        for wear in self.wear_sensor:
            if wear >= 0.9:
                return True
        return False
    
