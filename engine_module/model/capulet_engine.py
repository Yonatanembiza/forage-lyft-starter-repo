
from engine_module.engine import Engine

class CapuletEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        self.last_service_milage = last_service_mileage
        self.current_mileage = current_mileage
    
    def needs_service(self):
        return self.current_mileage - self.last_service_milage > 30000