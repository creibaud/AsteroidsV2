import pygame
import core.core as core

def setUp():
    core.memory("rectButton", pygame.Rect(core.screenSettings.WIDTH // 2 - 100, 350, 200, 100))
    core.memory("textButton", "Start")
    core.memory("fontButton", pygame.font.Font(None, 60))
    core.memory("colorButton", (255, 255, 255))
    core.memory("StartButton", False)

def draw():
    rect = core.memory("rectButton")
    color = core.memory("colorButton")
    font = core.memory("fontButton")
    text = core.memory("textButton")
    pygame.draw.rect(core.screenSettings.SCREEN, color, rect, border_radius=10)
    textSurface = font.render(text, True, (0, 0, 0))
    textRect = textSurface.get_rect(center=rect.center)
    core.screenSettings.SCREEN.blit(textSurface, textRect)