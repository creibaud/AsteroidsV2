import pygame
import math
import random
import core.core as core

def setUp():
    core.memory("asteroids", [])

def add(position, direction, size = None,):
    asteroids = core.memory("asteroids")
    newSize = size

    if size is None:
        newSize = random.choice(core.asteroidSettings.SIZE)
    
    life = False

    if random.random() < 0.05:
        life = True

    newSpeed = random.uniform(1, core.asteroidSettings.MAX_SPEED)
    asteroids.append([position, direction, generateRandomPolygon(position, newSize), newSize, newSpeed, life])
    core.memory("asteroids", asteroids)

def generateRandomPolygon(position, size):
    numVertices = random.randint(5, 12)
    angleIncrement = 360 / numVertices

    actualRadius = getRadius(size)

    vertices = []
    for i in range(numVertices):
        angle = math.radians(i * angleIncrement + random.uniform(-10, 10))
        radius = random.uniform(actualRadius / 2, actualRadius)
        x = position.x + radius * math.cos(angle)
        y = position.y + radius * math.sin(angle)
        vertices.append(pygame.math.Vector2(x, y))
    return vertices

def getRadius(size):
    if size == "small":
        return core.asteroidSettings.RADIUS // 3
    elif size == "medium":
        return core.asteroidSettings.RADIUS // 2
    else:
        return core.asteroidSettings.RADIUS

def update():
    asteroids = core.memory("asteroids")
    for i in range(0, len(asteroids)):
        position = asteroids[i][0]
        direction = asteroids[i][1]
        speed = asteroids[i][len(asteroids[i]) - 2]
        position += direction * speed

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

def breakApart(asteroid, size):
    position = asteroid[0]
    if size == "big":
        add(position + pygame.math.Vector2(random.randint(0, 5), random.randint(0, 5)), pygame.Vector2(1, 0).rotate(random.uniform(0, 360)), "medium")
        add(position + pygame.math.Vector2(random.randint(0, 5), random.randint(0, 5)), pygame.Vector2(1, 0).rotate(random.uniform(0, 360)), "medium")
    elif size == "medium":
        add(position + pygame.math.Vector2(random.randint(0, 5), random.randint(0, 5)), pygame.Vector2(1, 0).rotate(random.uniform(0, 360)), "small")
        add(position + pygame.math.Vector2(random.randint(0, 5), random.randint(0, 5)), pygame.Vector2(1, 0).rotate(random.uniform(0, 360)), "small")
    else:
        pass

def draw():
    asteroids = core.memory("asteroids")
    for i in range(0, len(asteroids)):
        giveLife = asteroids[i][len(asteroids[i]) - 1]
        if giveLife:
            pygame.draw.polygon(core.screenSettings.SCREEN, (0, 255, 0), [vertex.xy for vertex in asteroids[i][2]], 1)
        else:
            pygame.draw.polygon(core.screenSettings.SCREEN, (255, 255, 255), [vertex.xy for vertex in asteroids[i][2]], 1)