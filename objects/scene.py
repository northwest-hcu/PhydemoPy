from typing import TypeAlias, Literal
import json
from .position import Position

Mode: TypeAlias = Literal[
    'rays',
    'extended',
    'images',
    'observer'
]

class Scene:
    def __init__(
            self, 
            objs: list[dict]=[], 
            modules: list[dict]=[],
            version: int=5, 
            width: int=1300, 
            height: int=1000,
            mode: Mode = 'rays',
            rayModeDensity: float=1.0,
            showGrid: bool=True,
            snapToGrid: bool=True,
            lockObjs: bool=True,
            gridSize: int=20,
            observer: dict={
                "c": Position(0, 0),
                "r": 20
            },
            origin: Position=Position(0, 0),
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
        self.gridSize = gridSize
        self.observer = observer
        self.origin = origin
        self.scale = scale
        self.simulateColors = simulateColors

    @property
    def data(self) -> dict:
        return {
            'objs': [obj.value for obj in self.objs],
            'modules': self.modules,
            'version': self.version,
            'width': self.width,
            'height': self.height,
            'mode': self.mode,
            'rayModeDensity': self.rayModeDensity,
            'showGrid': self.showGrid,
            'snapToGrid': self.snapToGrid,
            'lockObjs': self.lockObjs,
            'gridSize': self.gridSize,
            'observer': {"c": self.observer["c"].value, "r": self.observer["r"]},
            'origin': self.origin.value,
            'scale': self.scale,
            'simulateColors': self.simulateColors
        }

    @property
    def mode(self) -> Mode:
        return self.__mode
    
    @mode.setter
    def mode(self, value: Mode) -> None:
        if value in ['rays','extended','images','observer']:
            self.__mode = value
        else:
            self.__mode = 'rays'

    @classmethod
    def load(cls, path: str) -> 'Scene':
        with open(path, 'r') as fp:
            data = json.load(fp)
            return Scene(**data)

    def output(self, path: str | None=None) -> None | str:
        if path is None:
            return json.dumps(self.data)
        else:
            with open(path, 'w') as fp:
                json.dump(self.data, fp, indent=2)