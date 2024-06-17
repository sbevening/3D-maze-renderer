import pygame
from math import pi

import RayCaster
from RayCastHit import RayCastHit
from renderer.Renderer import Renderer
from Vector2 import Vector2

SCALE = 50

class Renderer2D(Renderer):
    def __init__(self, maze: list[list[int]], playerPosition: Vector2, playerDirection: float) -> None:
        self.screen = pygame.display.set_mode([500, 500])
        self.screen.fill((255, 255, 255))
        self.maze = maze
        self.playerPosition = playerPosition
        self.playerDirection = playerDirection

    def render(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                if self.maze[i][j] == 1:
                    pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(SCALE * j, SCALE * i, SCALE, SCALE))
                else:
                    pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(SCALE * j, SCALE * i, SCALE, SCALE))

        hits: set[RayCastHit] = super().castRays()
        for hit in hits:
            pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(SCALE * hit.hitPos.x, SCALE * hit.hitPos.y, SCALE, SCALE))

        pygame.draw.rect(self.screen, (0, 0, 255), pygame.Rect(SCALE * self.playerPosition.x, SCALE * self.playerPosition.y, SCALE, SCALE))

        pygame.display.flip()