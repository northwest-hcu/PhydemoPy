from enum import Enum
import json

class Mode(Enum):
    rays = 'rays'
    extended = 'extended'
    images = 'images'
    observer = 'observer'

class Scene:
    def __init__(
            self, 
            objs: list[dict]=[], 
            modules: list[dict]=[],
            version: int=5, 
            width: int=1300, 
            height: int=1000,
            mode: Mode = Mode.rays,
            rayModeDensity: float=1.0,
            showGrid: bool=True,
            snapToGrid: bool=True,
            lockObjs: bool=True,
            girdSize: int=20,
            observer: dict={
                "c": {
                    "x": 0,
                    "y": 0
                },
                "r": 20
            },
            origin: dict={
                "x": 0,
                "y": 0
            },
            scale: float=1.0,
            simulateColors: bool=True
        ) -> None:
        self.objs = objs
        self.modules = modules
        self.version = version
        self.width = width
        self.height = height
        self.mode = mode
        self.rayModeDensity = rayModeDensity
        self.showGrid = showGrid
        self.snapToGrid = snapToGrid
        self.lockObjs = lockObjs
        self.gridSize = girdSize
        self.observer = observer
        self.origin = origin
        self.scale = scale
        self.simulateColors = simulateColors

    @classmethod
    def load(cls, path: str) -> 'Scene':
        with open(path, 'r') as fp:
            data = json.load(fp)
            return Scene(**data)

    def output(self, path: str | None=None) -> None | str:
        if path is None:
            return json.dumps(self)
        else:
            with open(path, 'w') as fp:
                json.dump(self, fp, indent=2)