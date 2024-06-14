from math import sin, cos

from RayCastHit import RayCastHit
from Vector2 import Vector2

STEPS = 50

def castRay(maze: list[list[int]], posX: int, posY: int, angle: float, depth: int) -> RayCastHit:
    """Casts a ray into a maze at a given angle in radians from a given x and y. Returns a RayCastHit object with information on the cast, or None
    if ray never makes contact with a wall."""
    depthX: float = cos(angle) * depth
    stepX: float = depthX / STEPS
    depthY: float = -sin(angle) * depth
    stepY: float = depthY / STEPS
    mazeHeight = len(maze)
    mazeWidth = len(maze[0])

    for stepNum in range(STEPS):
        pointX: int = round(posX + stepNum * stepX)
        pointY: int = round(posY + stepNum * stepY)
        isInBounds: bool = (0 <= pointX) and (pointX < mazeWidth) and (0 <= pointY) and (pointY < mazeHeight)
        isSamePosition: bool = (pointX == posX) and (pointY == posY)

        if isInBounds and (not isSamePosition) and maze[pointY][pointX] == 1:
            return RayCastHit(Vector2(pointX, pointY), Vector2(posX, posY))
    return None # no hits