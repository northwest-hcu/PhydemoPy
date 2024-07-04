import math

class Position:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
    
    def rotate(self, base_position: 'Position', degree: float) -> None:
        x_diff = self.x - base_position.x
        y_diff = self.y - base_position.y
        rad = (degree / 360) * 2 * math.pi
        self.x = math.cos(rad) * x_diff - math.sin(rad) * y_diff + base_position.x
        self.y = math.sin(rad) * x_diff + math.cos(rad) * y_diff + base_position.y

    def move(self, dx: float, dy: float) -> None:
        self.x = self.x + dx
        self.y = self.y + dy

    @staticmethod
    def midpoint(p1: 'Position', p2: 'Position') -> 'Position':
        return Position((p1.x + p2.x) / 2, (p1.y, p2.y) / 2)

    @property
    def value(self) -> dict:
        return {
            "x": self.x,
            "y": self.y
        }
