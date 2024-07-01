import sys, os
sys.path.insert(0, "..objects")
from objects.scene import Scene

def main():
    scene = Scene.load("./test.json")
    scene.output()
    scene.output(path="./test.json")

main()    