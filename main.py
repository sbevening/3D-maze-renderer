import RayCaster

mazeMap: list[list[int]] = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 1]
]

hit = RayCaster.castRay(mazeMap, 3, 3, 0.3, 6)
if hit == None:
    print("none")
else:
    print(f"x: {hit.hitPos.x}, y: {hit.hitPos.y}")