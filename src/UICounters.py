import pygame
import pygame.freetype

pygame.font.init()
pygame.freetype.init()
font = pygame.freetype.SysFont("arial", 14)
clock = pygame.time.Clock()

def drawFpsCounter(screen: pygame.Surface) -> None:
    fps: int = 0
    deltaTime = clock.tick(60) / 1000
    if (deltaTime != 0):
        fps = 1 / deltaTime
    else:
        fps = 0
    font.render_to(screen, (7, 7), f"fps: {round(fps)}", (255, 255, 255))

def drawLevelCounter(screen: pygame.Surface, level: int) -> None:
    font.render_to(screen, 7, 28), f"level: {level}, {255, 255, 255}"