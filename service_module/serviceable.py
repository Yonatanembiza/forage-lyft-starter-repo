from abc import ABC, abstractmethod

class Serviceable(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        """Returns True if engine needs service, otherwise False"""
        pass