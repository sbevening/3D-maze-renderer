from Vector2 import Vector2
from random import choice
from numpy import full


directions = (Vector2(1, 0), Vector2(-1, 0), Vector2(0, 1), Vector2(0, -1))

def isInBounds(maze: list[list[int]], position: Vector2) -> bool:
    """Determines if a given position is within bounds of a given maze."""
    mazeHeight = len(maze)
    mazeWidth = len(maze[0])
    yInBounds = (0 <= position.y) and (position.y < mazeHeight)
    xInBounds = (0 <= position.x) and (position.x < mazeWidth)
    return xInBounds and yInBounds

def generateMaze(width: int, height: int) -> list[list[int]]:
    """Using recursive backtracking, randomly generates a maze of given width and height."""
    maze: list[list[int]] = full((height, width), 0)

    for i in range(height):
        for j in range(width):
            if i % 2 == 0 or j % 2 == 0: #set up a grid of walls to carve through
                maze[i][j] = 1

    carveWall(1, 1, maze)
    removePlaceholders(width, height, maze)

    maze[height - 2][width - 2] = 9 # end square

    return maze

def removePlaceholders(width, height, maze) -> None:
    """Removes all temporary 2's that are used to represent visited cells when generating maze and replaces them with open cells."""
    for i in range(height):
        for j in range(width):
            cell = maze[i][j]
            if cell == 2:
                maze[i][j] = 0

def carveWall(currX: int, currY: int, maze: list[list[int]]) -> None:
    """From a given position, picks a non-visited, neighbouring, unvisited cell and removes the wall in between the given position and
    that cell."""
    maze[currY][currX] = 2 # temporary value to represent a visited tile
    potentialPositions = (Vector2(currX, currY - 2), Vector2(currX, currY + 2), Vector2(currX + 2, currY), Vector2(currX - 2, currY))
    validPotentialPositions = filter(lambda pos : isInBounds(maze, pos), potentialPositions)
    potentialCellValues = tuple(map(lambda v2 : maze[v2.y][v2.x], validPotentialPositions))
    if sum(potentialCellValues) == 2 * len(potentialCellValues): # are all 4 potential cells visited already?
        return
    
    directionIndices = list(range(4))
    while len(directionIndices) > 0:
        chosenIndex = choice(directionIndices)
        directionIndices.remove(chosenIndex)
        direction = directions[chosenIndex]

        midX = currX + direction.x
        nextX = midX + direction.x
        midY = currY + direction.y
        nextY = midY + direction.y

        if isInBounds(maze, Vector2(nextX, nextY)) and maze[nextY][nextX] != 2:
            maze[midY][midX] = 2
            carveWall(nextX, nextY, maze)