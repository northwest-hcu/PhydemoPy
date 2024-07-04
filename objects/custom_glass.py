from .position import Position
from .obj import Obj

class CustomGlass(Obj):
    def __init__(
            self,
            p1: Position=Position(0, 0),
            p2: Position=Position(0, 100),
            eqn1: str="0",
            eqn2: str="0.5\\cdot\\sqrt{1-x^2}",
            refIndex: float=1.5
        ) -> None:
        self.p1 = p1
        self.p2 = p2
        self.eqn1 = eqn1
        self.eqn2 = eqn2
        self.refIndex = refIndex
    
    def rotate(self, base_position: Position, degree: int):
        self.p1.rotate(base_position, degree)
        self.p2.rotate(base_position, degree)

    def move(self, dx: float, dy: float):
        self.p1.move(dx, dy)
        self.p2.move(dx, dy)

    @property
    def value(self) -> dict:
        return {
            "type": "CustomGlass",
            "p1": self.p1.value,
            "p2": self.p2.value,
            "eqn1": self.eqn1,
            "eqn2": self.eqn2,
            "refIndex": self.refIndex
        }