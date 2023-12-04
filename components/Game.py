import pygame
import random
import core.core as core
import components.SpaceShip as SpaceShip
import components.Asteroid as Asteroid

def setUp():
    SpaceShip.setUp()
    Asteroid.setUp()

    for i in range(0, 10):
        side = random.choice(["top", "bottom", "left", "right"])
        position = pygame.math.Vector2(0, 0)

        if side == "top":
            position = pygame.math.Vector2(random.randint(0, core.screenSettings.WIDTH), 0)
        elif side == "bottom":
            position = pygame.math.Vector2(random.randint(0, core.screenSettings.WIDTH), core.screenSettings.HEIGHT)
        elif side == "left":
            position = pygame.math.Vector2(0, random.randint(0, core.screenSettings.HEIGHT))
        elif side == "right":
            position = pygame.math.Vector2(core.screenSettings.WIDTH, random.randint(0, core.screenSettings.HEIGHT))

        direction = pygame.math.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        Asteroid.add(position, direction)

def update():
    SpaceShip.update()
    Asteroid.update()

def rotateSpaceShip(angle):
    SpaceShip.rotate(angle)

def spaceShipAccelerate(isAcceleration):
    if isAcceleration:
        SpaceShip.accelerate()
    else:
        SpaceShip.decelerate()

def shootSpaceShip():
    SpaceShip.shoot()

def draw():
    SpaceShip.draw((255, 165, 0))
    SpaceShip.Bullets.draw()
    Asteroid.draw()
