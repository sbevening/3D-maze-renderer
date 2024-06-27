import pygame

from RayCastHit import RayCastHit
from renderer.Renderer import Renderer
from Vector2 import Vector2

SCALE = 10

class Renderer2D(Renderer):
    def __init__(self, maze: list[list[int]], playerPosition: Vector2, playerDirection: float, depth = 4) -> None:
        mazeHeight = len(maze)
        mazeWidth = len(maze[0])
        self.screen = pygame.display.set_mode([mazeWidth * SCALE, mazeHeight * SCALE])
        self.screen.fill((255, 255, 255))
        self.maze = maze
        self.playerPosition = playerPosition
        self.playerDirection = playerDirection
        self.depth = depth

    def render(self) -> None:
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                if self.maze[i][j] == 1:
                    pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(SCALE * j, SCALE * i, SCALE, SCALE))
                else:
                    pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(SCALE * j, SCALE * i, SCALE, SCALE))

        hits: set[RayCastHit] = super().castRays()
        for hit in hits:
            if hit != None:
                roundedPos: Vector2 = Vector2(round(hit.hitPos.x), round(hit.hitPos.y))
                colourIntensityUnbounded = 255 / hit.distance() if hit.distance() != 0 else 255
                colourIntensity = colourIntensityUnbounded if colourIntensityUnbounded < 255 else 255
                pygame.draw.rect(self.screen, (colourIntensity, 0, 0), pygame.Rect(SCALE * roundedPos.x, SCALE * roundedPos.y, SCALE, SCALE))

        pygame.draw.rect(self.screen, (0, 0, 255), pygame.Rect(SCALE * self.playerPosition.x, SCALE * self.playerPosition.y, SCALE, SCALE))
