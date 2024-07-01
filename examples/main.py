import importlib
from objects.scene import Scene

if __name__ == "__main__":
    scene = Scene()
    scene.output(path="./test.json")