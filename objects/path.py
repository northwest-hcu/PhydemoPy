from .position import Position

class Path(Position):
    def __init__(self, x: float, y: float, arc: bool=True) -> None:
        super().__init__(self, x, y)
        self.arc = arc

    @property
    def value(self) -> dict:
        return {
            "x": self.x,
            "y": self.y,
            "arc": self.arc
        }