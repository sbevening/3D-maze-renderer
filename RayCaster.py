from math import atan2, sin, cos

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
        pointX: float = posX + stepNum * stepX
        pointY: float = posY + stepNum * stepY
        isInBounds: bool = (0 <= pointX) and (pointX < mazeWidth) and (0 <= pointY) and (pointY < mazeHeight)
        isSamePosition: bool = (pointX == posX) and (pointY == posY)

        if isInBounds and (not isSamePosition) and maze[round(pointY)][round(pointX)] != 0:
            return RayCastHit(Vector2(pointX, pointY), Vector2(posX, posY), angle, maze[round(pointY)][round(pointX)])
    return None # no hits

def castRays(maze: list[list[int]], posX: int, posY: int, minAngle: float, maxAngle: float, depth: int, rayCount: int) -> set[RayCastHit]:
    """Casts a given number of rays at equal intervals in a range of angles with a specific distance. Returns set of all unique hits."""
    angleStep: float = (maxAngle - minAngle) / rayCount
    theta: float = minAngle
    hits: list[RayCastHit] = list()

    while (theta <= maxAngle):
        hit: RayCastHit = castRay(maze, posX, posY, theta, depth)
        hits.append(hit)
        theta += angleStep
    return hits