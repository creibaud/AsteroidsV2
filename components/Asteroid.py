import pygame
import math
import random
import core.core as core

def setUp():
    core.memory("asteroids", [])

def add(position, direction):
    asteroids = core.memory("asteroids")
    size = random.choice(core.asteroidSettings.SIZE)
    print(size)
    asteroids.append([position, direction, generateRandomPolygon(position, size), size])
    core.memory("asteroids", asteroids)

def generateRandomPolygon(position, size):
    numVertices = random.randint(5, 12)
    angleIncrement = 360 / numVertices

    actualRadius = 0

    if size == "small":
        actualRadius = core.asteroidSettings.RADIUS // 3
    elif size == "medium":
        actualRadius = core.asteroidSettings.RADIUS // 2
    else:
        actualRadius = core.asteroidSettings.RADIUS

    vertices = []
    for i in range(numVertices):
        angle = math.radians(i * angleIncrement + random.uniform(-10, 10))
        radius = random.uniform(actualRadius / 2, actualRadius)
        x = position.x + radius * math.cos(angle)
        y = position.y + radius * math.sin(angle)
        vertices.append(pygame.math.Vector2(x, y))
    return vertices

def update():
    asteroids = core.memory("asteroids")
    for i in range(0, len(asteroids)):
        position = asteroids[i][0]
        direction = asteroids[i][1]
        position += direction * core.asteroidSettings.MAX_SPEED

        if position.x <= 0:
            position.x = core.screenSettings.WIDTH
        elif position.x >= core.screenSettings.WIDTH:
            position.x = 0
        
        if position.y <= 0:
            position.y = core.screenSettings.HEIGHT
        elif position.y >= core.screenSettings.HEIGHT:
            position.y = 0
        
        asteroids[i][2] = generateRandomPolygon(position, asteroids[i][3])

    core.memory("asteroids", asteroids)

def draw():
    asteroids = core.memory("asteroids")
    for i in range(0, len(asteroids)):
        pygame.draw.polygon(core.screenSettings.SCREEN, (255, 255, 255), [vertex.xy for vertex in asteroids[i][2]], 1)