import pygame
import sys
import core.settings.screen as screenSettings

def setTitle(title):
    screenSettings.TITLE = title

def setWidth(width):
    screenSettings.WIDTH = width

def setHeight(height):
    screenSettings.HEIGHT = height

def setBackground(background):
    screenSettings.BACKGROUND_COLOR = background

def setFPS(fps):
    screenSettings.FPS = fps

def setScreenSize(size: tuple = None, fullscreen: bool = False):
    if size is not None:
        screenSettings.WIDTH, screenSettings.HEIGHT = size
    elif fullscreen:
        screenSettings.WIDTH, screenSettings.HEIGHT = (0, 0)
        screenSettings.FULLSCREEN = True
    else:
        sys.stderr.write("ERREUR : Aucune taille d'écran n'a été définie\n")
        sys.exit()

def setScreen():
    if screenSettings.BACKGROUND_COLOR is None:
        screenSettings.BACKGROUND_COLOR = (0, 0, 0)
    
    if screenSettings.FPS == 0:
        screenSettings.FPS = 60

    if screenSettings.FULLSCREEN:
        screenSettings.SCREEN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption(screenSettings.TITLE)
        setWidth(screenSettings.SCREEN.get_width())
        setHeight(screenSettings.SCREEN.get_height())
    else:
        if screenSettings.WIDTH == 0 or screenSettings.HEIGHT == 0:
            sys.stderr.write("ERREUR : La taille de l'écran n'a pas été définie\n")
            sys.exit()
        else:
            screenSettings.SCREEN = pygame.display.set_mode((screenSettings.WIDTH, screenSettings.HEIGHT))
            pygame.display.set_caption(screenSettings.TITLE)

def clean():
    screenSettings.SCREEN.fill(screenSettings.BACKGROUND_COLOR)