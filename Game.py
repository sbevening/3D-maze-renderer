from math import pi, sin, cos
import pygame

from renderer.Renderer2D import Renderer2D
from Vector2 import Vector2

pygame.init()

clock = pygame.time.Clock()

SCALE = 50

maze: list[list[int]] = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1]
]

playerPosition = Vector2(1, 1)
playerDirection: float = 0

def isInBounds(x, y):
    """Determines if a point with given x and y is within the maze."""
    mazeHeight = len(maze)
    mazeWidth = len(maze[0])
    return (0 <= x) and (x < mazeWidth) and (0 <= y) and (y < mazeHeight)

def movePlayer(dx: int, dy: int) -> Vector2:
    """Returns new position vector for player incremented by dx and dy values."""
    newX = playerPosition.x + dx
    newY = playerPosition.y + dy
    if isInBounds(newX, newY) and maze[newY][newX] != 1:
        return Vector2(newX, newY)
    return playerPosition

def handleKeyDown(e: pygame.event) -> None:
    """Handles key down events and moves or rotates player."""
    global playerDirection
    global playerPosition

    sinDirection = round(sin(playerDirection))
    cosDirection = round(cos(playerDirection))

    match e.key:
        case pygame.K_LEFT:
            playerPosition = movePlayer(-sinDirection, -cosDirection)
        case pygame.K_UP:
            playerPosition = movePlayer(cosDirection, -sinDirection)
        case pygame.K_RIGHT:
            playerPosition = movePlayer(sinDirection, cosDirection)
        case pygame.K_DOWN:
            playerPosition = movePlayer(-cosDirection, sinDirection)
        case pygame.K_a:
            playerDirection += pi / 2
        case pygame.K_d:
            playerDirection -= pi / 2
        case _:
            pass

# Set up game loop
r2D = Renderer2D(maze, playerPosition, playerDirection)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            handleKeyDown(event)

    r2D.tick(playerPosition, playerDirection)
    r2D.render()