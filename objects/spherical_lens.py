from .position import Position
from .path import Path
from .obj import Obj
import math

class SphericalLens(Obj):
    def __init__(
            self,
            path: list[Path]
        ) -> None:
        self.p1 = 
    
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
    
    def createLens(self):
        thick = 10
        p1 = self.p1 | Position.midpoint(self.path[0], self.path[1])
        p2 = self.p2 | Position.midpoint(self.path[3], self.path[4])
        length = math.sqrt((p1.x - p2.x) ^ 2 + (p1.y - p2.y) ^ 2)
        dx = (p2.x - p1.x) / length
        dy = (p2.y - p1.y) / length
        dpx = dy
        dpy = -dx
        cx = (p1.x + p2.x) / 2
        cy = (p1.y + p2.y) / 2
        self.path = [
            Path(p1.x - dpx * thick, p1.y - dpy * thick, arc=False),
            Path(p1.x + dpx * thick, p1.y - dpy * thick, arc=False),
            Path(cx + dpx * thick * 2, cy + dpy * thick * 2, arc=True),
            Path(p2.x + dpx * thick, p2.y + dpy * thick, arc=False),
            Path(p2.x - dpx * thick, p2.y - dpy * thick, arc=False),
            Path(cx - dpx * thick * 2, cy - dpy * thick * 2, arc=True)
        ]
    
    def createLensDR1R2(self):
        p1 = self.p1 | Position.midpoint()