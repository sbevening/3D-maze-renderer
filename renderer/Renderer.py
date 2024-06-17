from abc import abstractmethod, ABC
from math import pi

import RayCaster
from RayCastHit import RayCastHit
from Vector2 import Vector2

class Renderer(ABC):
    """Abstract class for a renderer for the game."""
    def __init__(self, maze: list[list[int]], playerPosition: Vector2, playerDirection: float) -> None:
        self.maze = maze
        self.playerPosition = playerPosition
        self.playerDirection = playerDirection

    def castRays(self, depth = 3) -> set[RayCastHit]:
        """Cast rays within 120 degree field of view at a given depth of ray / length of sight line."""
        minAngle = self.playerDirection - pi / 3
        maxAngle = self.playerDirection + pi / 3
        hits: set[RayCastHit] = RayCaster.castRays(self.maze, self.playerPosition.x, self.playerPosition.y, minAngle, maxAngle, depth, 19)
        return hits

    def tick(self, playerPosition: Vector2, playerDirection: float) -> None:
        """Updates fields representing player position and direction."""
        self.playerPosition = playerPosition
        self.playerDirection = playerDirection

    @abstractmethod
    def render(self):
        """Renders the player and the maze in some manner."""
        pass