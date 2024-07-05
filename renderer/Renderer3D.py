from numpy import clip
from math import sqrt, cos
import pygame

from RayCastHit import RayCastHit
from renderer.Renderer import Renderer
from Vector2 import Vector2

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLOUR_MAP = {
    1: pygame.Color(255, 255, 255),
    9: pygame.Color(0, 255, 0)
}

class Renderer3D(Renderer):
    def __init__(self, maze: list[list[int]], playerPosition: Vector2, playerDirection: float, depth = 10) -> None:
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        self.screen.fill((255, 255, 255))
        self.maze = maze
        self.playerPosition = playerPosition
        self.playerDirection = playerDirection
        self.depth = depth
    
    def applyBrightnessToColour(self, col: pygame.Color, brightness: int):
        """Returns a given colour with its components scaled to a brightness between 0 and 255"""
        proportionalBrightness = brightness / 255
        appliedR = int(col.r * proportionalBrightness)
        appliedG = int(col.g * proportionalBrightness)
        appliedB = int(col.b * proportionalBrightness)
        return pygame.Color(appliedR, appliedG, appliedB)

    def render(self):
        self.screen.fill((0, 0, 0))
        hits: set[RayCastHit] = super().castRays()
        step = round(SCREEN_WIDTH / len(hits))

        for i, hit in enumerate(hits):
            if hit != None:
                colourIntensityUnbounded = 255 / sqrt(hit.distance()) if hit.distance() != 0 else 255
                colourIntensity = clip(colourIntensityUnbounded, 128, 255)

                undimmedColour = COLOUR_MAP.get(hit.cellType)
                colour = self.applyBrightnessToColour(undimmedColour, colourIntensity)
                rectHeight = SCREEN_HEIGHT * (hit.distance() / self.depth)
                pygame.draw.rect(self.screen, colour, pygame.Rect(i * step, rectHeight, step, SCREEN_HEIGHT - 2 * rectHeight))