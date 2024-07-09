from math import pi, sin, cos
import pygame

from renderer.Renderer3D import Renderer3D
from MazeGenerator import generateMaze
from Vector2 import Vector2

pygame.init()
clock = pygame.time.Clock()

SCALE = 50
MAZE_WIDTH = 11 # MUST BE ODD
MAZE_HEIGHT = 11 # MUST BE ODD

MOVE_SPEED = 2
ROTATE_SPEED = 2

maze: list[list[int]] = generateMaze(MAZE_WIDTH, MAZE_HEIGHT)

playerPosition = Vector2(1, 1)
playerDirection: float = 0

r3D = Renderer3D(maze, playerPosition, playerDirection)

def isInBounds(x, y) -> bool:
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
    r3D.setMaze(maze)

def movePlayer(dx: int, dy: int) -> Vector2:
    """Returns new position vector for player incremented by dx and dy values."""
    newX = playerPosition.x + dx
    cellX = round(newX)
    newY = playerPosition.y + dy
    cellY = round (newY)
    if isInBounds(newX, newY) and maze[cellY][cellX] != 1:
        if (maze[cellY][cellX] == 9):
            setupNewMaze()
            return Vector2(1, 1)
        return Vector2(newX, newY)
    return playerPosition

def handleKeyDown(e: pygame.event) -> None:
    """Handles key down events."""
    global playerDirection
    global playerPosition

    match e.key:
        case pygame.K_SPACE:
            setupNewMaze()
        case _:
            pass

def handleKeysPressed() -> None:
    """Gets keys pressed down and moves and rotates player accordingly."""
    global playerPosition
    global playerDirection

    deltaTime = clock.tick(60)/1000
    sinDirectionTimeScaled = MOVE_SPEED * round(sin(playerDirection)) * deltaTime 
    cosDirectionTimeScaled = MOVE_SPEED * round(cos(playerDirection)) * deltaTime
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        playerDirection += pi / 2 * deltaTime * ROTATE_SPEED
    if keys[pygame.K_d]:
        playerDirection -= pi / 2 * deltaTime * ROTATE_SPEED
    if keys[pygame.K_LEFT]:
        playerPosition = movePlayer(-sinDirectionTimeScaled, -cosDirectionTimeScaled)
    if keys[pygame.K_UP]:
        playerPosition = movePlayer(cosDirectionTimeScaled, -sinDirectionTimeScaled)
    if keys[pygame.K_RIGHT]:
        playerPosition = movePlayer(sinDirectionTimeScaled, cosDirectionTimeScaled)
    if keys[pygame.K_DOWN]:
        playerPosition = movePlayer(-cosDirectionTimeScaled, sinDirectionTimeScaled)

# Set up game loop
running = True
while running:
    handleKeysPressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            handleKeyDown(event)

    r3D.tick(playerPosition, playerDirection)
    r3D.render()

    pygame.display.flip()