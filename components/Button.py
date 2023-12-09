import pygame
import core.core as core

# Set up the button
def setUp():
    # Initialize the main variables of the button
    core.memory("rectButton", pygame.Rect(core.screenSettings.WIDTH // 2 - 100, 350, 200, 100))
    core.memory("textButton", "Start")
    core.memory("fontButton", pygame.font.Font(None, 60))
    core.memory("colorButton", (255, 255, 255))
    core.memory("StartButton", False)

# Draw the button
def draw():
    # Get the rectangle, the color, font and text of the button
    rect = core.memory("rectButton")
    color = core.memory("colorButton")
    font = core.memory("fontButton")
    text = core.memory("textButton")

    # Draw the rectangle of the button
    pygame.draw.rect(core.screenSettings.SCREEN, color, rect, border_radius=10)

    # Set the text surface and rectangle
    textSurface = font.render(text, True, (0, 0, 0))
    textRect = textSurface.get_rect(center=rect.center)

    # Draw the text
    core.screenSettings.SCREEN.blit(textSurface, textRect)