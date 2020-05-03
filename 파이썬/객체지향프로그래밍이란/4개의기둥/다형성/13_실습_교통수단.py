from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


    def stop(self):
        self._speed = 0
        pass

    @property
    @abstractmethod    
    def speed(self):
        self._x = 0
    

print(Vehicle.mro())        
print(dir(Vehicle))