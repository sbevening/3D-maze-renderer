import RayCaster
from math import pi

mazeMap: list[list[int]] = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 1]
]

hits = RayCaster.castRays(mazeMap, 3, 3, 0, 2 * pi, 10, 10)

# for hit in hits:
#     print(f"origin: ({hit.originPos.x}, {hit.originPos.y}). hit: ({hit.hitPos.x}, {hit.hitPos.y}).")