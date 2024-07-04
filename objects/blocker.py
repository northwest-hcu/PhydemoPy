from .position import Position
from .obj import Obj

class Blocker(Obj):
    def __init__(
            self,
            p1: Position=Position(0, 0),
            p2: Position=Position(0, 100)
        ) -> None:
        self.p1 = p1
        self.p2 = p2
    
    def rotate(self, base_position: Position, degree: int):
        self.p1.rotate(base_position, degree)
        self.p2.rotate(base_position, degree)

    def move(self, dx: float, dy: float):
        self.p1.move(dx, dy)
        self.p2.move(dx, dy)

    @property
    def value(self) -> dict:
        return {
            "type": "Blocker",
            "p1": self.p1.value,
            "p2": self.p2.value
        }