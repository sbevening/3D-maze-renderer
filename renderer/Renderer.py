from abc import abstractmethod, ABC
from math import pi

import RayCaster
from RayCastHit import RayCastHit
from Vector2 import Vector2

FIELD_OF_VIEW = 5 * pi / 6

class Renderer(ABC):
    """Abstract class for a renderer for the game."""
    def __init__(self, maze: list[list[int]], playerPosition: Vector2, playerDirection: float, depth = 4) -> None:
        self.maze = maze
        self.playerPosition = playerPosition
        self.playerDirection = playerDirection
        self.depth = depth

    def castRays(self) -> list[RayCastHit]:
        """Cast rays within 120 degree field of view at a given depth of ray / length of sight line."""
        minAngle = self.playerDirection - FIELD_OF_VIEW / 2
        maxAngle = self.playerDirection + FIELD_OF_VIEW / 2
        hits: list[RayCastHit] = RayCaster.castRays(self.maze, self.playerPosition.x, self.playerPosition.y, minAngle, maxAngle, self.depth, 200)
        return hits[::-1]

    def tick(self, playerPosition: Vector2, playerDirection: float) -> None:
        """Updates fields representing player position and direction."""
        self.playerPosition = playerPosition
        self.playerDirection = playerDirection

    @abstractmethod
    def render(self):
        """Renders the player and the maze in some manner."""
        pass

    def setMaze(self, maze):
        self.maze = maze