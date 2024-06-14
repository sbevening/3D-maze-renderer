import pygame

from Renderer2D import Renderer2D
from Vector2 import Vector2

pygame.init()

clock = pygame.time.Clock()

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
playerDirection: float = 0

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

def handleKeyDown(e: pygame.event) -> None:
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
        case _:
            pass

def handleKeyPresses() -> None:
    global playerDirection
    global playerPosition
    dt: int = clock.tick() / 1000
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        playerDirection += dt
    elif keys[pygame.K_d]:
        playerDirection -= dt

r2D = Renderer2D(maze, playerPosition, playerDirection)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            handleKeyDown(event)
    handleKeyPresses()

    r2D.tick(playerPosition, playerDirection)
    r2D.render()