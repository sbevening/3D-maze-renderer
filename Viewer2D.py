import pygame
from math import pi

from Vector2 import Vector2
import RayCaster

pygame.init()
screen = pygame.display.set_mode([500, 500])
screen.fill((255, 255, 255))

SCALE = 50

maze: list[list[int]] = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 1]
]

playerPosition = Vector2(1, 1)
playerDirection: int = 0

def isInBounds(x, y):
    mazeHeight = len(maze)
    mazeWidth = len(maze[0])
    return (0 <= x) and (x < mazeWidth) and (0 <= y) and (y < mazeHeight)

def movePlayer(dx: int, dy: int) -> Vector2:
    newX = playerPosition.x + dx
    newY = playerPosition.y + dy
    if isInBounds(newX, newY) and maze[newY][newX] != 1:
        return Vector2(newX, newY)
    return playerPosition

def handleKey(e: pygame.event) -> None:
    global playerDirection
    global playerPosition
    match e.key:
        case pygame.K_LEFT:
            playerPosition = movePlayer(-1, 0)
        case pygame.K_UP:
            playerPosition = movePlayer(0, -1)
        case pygame.K_RIGHT:
            playerPosition = movePlayer(1, 0)
        case pygame.K_DOWN:
            playerPosition = movePlayer(0, 1)
        case pygame.K_a:
            playerDirection += 0.1
        case pygame.K_d:
            playerDirection -= 0.1
        case _:
            pass
    # print(f"{playerPosition.x}, {playerPosition.y}")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            handleKey(event)
    
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(SCALE * j, SCALE * i, SCALE, SCALE))
            else:
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(SCALE * j, SCALE * i, SCALE, SCALE))

    for hit in RayCaster.castRays(maze, playerPosition.x, playerPosition.y, playerDirection - pi / 2, playerDirection + pi / 2, 10, 10):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(SCALE * hit.hitPos.x, SCALE * hit.hitPos.y, SCALE, SCALE))

    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(SCALE * playerPosition.x, SCALE * playerPosition.y, SCALE, SCALE))

    pygame.display.flip()