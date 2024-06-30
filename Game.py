from math import pi, sin, cos
import pygame

from renderer.Renderer2D import Renderer2D
from renderer.Renderer3D import Renderer3D
from MazeGenerator import generateMaze
from Vector2 import Vector2

pygame.init()

SCALE = 50
MAZE_WIDTH = 31
MAZE_HEIGHT = 31

maze: list[list[int]] = generateMaze(MAZE_WIDTH, MAZE_HEIGHT)

playerPosition = Vector2(1, 1)
playerDirection: float = 0

r2D = Renderer2D(maze, playerPosition, playerDirection)
r3D = Renderer3D(maze, playerPosition, playerDirection)

def isInBounds(x, y):
    """Determines if a point with given x and y is within the maze."""
    mazeHeight = len(maze)
    mazeWidth = len(maze[0])
    return (0 <= x) and (x < mazeWidth) and (0 <= y) and (y < mazeHeight)

def setupNewMaze():
    """Generates new maze, resets player position, sets renderers' target to new maze."""
    global playerDirection
    global playerPosition
    global maze

    maze = generateMaze(MAZE_WIDTH, MAZE_HEIGHT)
    playerDirection = 0
    playerPosition = Vector2(1, 1)
    r2D.setMaze(maze)
    r3D.setMaze(maze)

def movePlayer(dx: int, dy: int) -> Vector2:
    """Returns new position vector for player incremented by dx and dy values."""
    newX = playerPosition.x + dx
    newY = playerPosition.y + dy
    if isInBounds(newX, newY) and maze[newY][newX] != 1:
        if (maze[newY][newX] == 9):
            setupNewMaze()
            return Vector2(1, 1)
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
        case pygame.K_SPACE:
            setupNewMaze()
        case _:
            pass

# Set up game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            handleKeyDown(event)

    r3D.tick(playerPosition, playerDirection)
    r3D.render()
    r2D.tick(playerPosition, playerDirection)
    r2D.render()

    pygame.display.flip()