from abc import ABCMeta, abstractmethod
from .position import Position

class Obj(ABCMeta):
    @abstractmethod
    def rotate(self, base_position: Position, degree: int):
        pass
    
    @abstractmethod
    def move(self, dx: float, dy: float):
        pass

    @property
    @abstractmethod
    def value(self):
        pass