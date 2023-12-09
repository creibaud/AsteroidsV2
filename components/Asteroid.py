import pygame
import math
import random
import core.core as core

# Set up the asteroids
def setUp():

    # Initialize the main variables of the asteroids
    core.asteroidSetUp.setRadius(30)
    core.asteroidSetUp.setSize(["big", "medium", "small"])
    core.asteroidSetUp.setMaxSpeed(5)
    core.asteroidSetUp.setAnimationInterval(500)

    # Initialize the list of the asteroids
    core.memory("asteroids", [])

# Add an asteroid to the list of asteroids
def add(position, direction, size = None,):
    # Get the list of asteroids
    asteroids = core.memory("asteroids")

    # Set the size of the asteroid
    newSize = size

    # If the size is not specified, choose a random size
    if size is None:
        newSize = random.choice(core.asteroidSettings.SIZE)
    
    # If the Asteroids can give a life to the user (5% of chance) is he destroy it
    life = False
    if random.random() < 0.05:
        life = True

    # Set the speed of the asteroid (random)
    newSpeed = random.uniform(1, core.asteroidSettings.MAX_SPEED)

    # Add the asteroid to the list
    asteroids.append([position, direction, generateRandomPolygon(position, newSize), newSize, newSpeed, life])
    core.memory("asteroids", asteroids)

# Generate a random polygon
def generateRandomPolygon(position, size):
    # Get the number of vertices of the polygon
    numVertices = random.randint(5, 12)

    # Get the angle increment
    angleIncrement = 360 / numVertices

    # Get the radius of the polygon
    actualRadius = getRadius(size)

    # Generate the vertices
    vertices = []
    for i in range(numVertices):
        # Generate the angle (random)
        angle = math.radians(i * angleIncrement + random.uniform(-10, 10))

        # Generate the radius (random)
        radius = random.uniform(actualRadius / 2, actualRadius)

        # Generate the vertex
        x = position.x + radius * math.cos(angle)
        y = position.y + radius * math.sin(angle)

        # Add the vertex to the list
        vertices.append(pygame.math.Vector2(x, y))

    # Return the vertices (the polygon)
    return vertices

# Get the radius of the asteroid
def getRadius(size):
    if size == "small":
        return core.asteroidSettings.RADIUS // 3
    elif size == "medium":
        return core.asteroidSettings.RADIUS // 2
    else:
        return core.asteroidSettings.RADIUS

# Update the asteroids states
def update():
    # Get the list of asteroids
    asteroids = core.memory("asteroids")

    # Update the asteroids
    for i in range(0, len(asteroids)):
        position = asteroids[i][0]
        direction = asteroids[i][1]
        speed = asteroids[i][len(asteroids[i]) - 2]
        position += direction * speed

        # Check if the asteroid is out of the screen (x and y)
        if position.x <= 0:
            position.x = core.screenSettings.WIDTH
        elif position.x >= core.screenSettings.WIDTH:
            position.x = 0
        
        if position.y <= 0:
            position.y = core.screenSettings.HEIGHT
        elif position.y >= core.screenSettings.HEIGHT:
            position.y = 0
        
        # Generate a random Polygone (animation)
        asteroids[i][2] = generateRandomPolygon(position, asteroids[i][3])

    # Update the list of asteroids
    core.memory("asteroids", asteroids)

# If the asteroid is hit by a bullet then he split in two or disappear
def breakApart(asteroid, size):
    # It all random
    position = asteroid[0]
    if size == "big":
        add(position + pygame.math.Vector2(random.randint(0, 5), random.randint(0, 5)), pygame.Vector2(1, 0).rotate(random.uniform(0, 360)), "medium")
        add(position + pygame.math.Vector2(random.randint(0, 5), random.randint(0, 5)), pygame.Vector2(1, 0).rotate(random.uniform(0, 360)), "medium")
    elif size == "medium":
        add(position + pygame.math.Vector2(random.randint(0, 5), random.randint(0, 5)), pygame.Vector2(1, 0).rotate(random.uniform(0, 360)), "small")
        add(position + pygame.math.Vector2(random.randint(0, 5), random.randint(0, 5)), pygame.Vector2(1, 0).rotate(random.uniform(0, 360)), "small")
    else:
        pass

# Draw the asteroids and if he can give a life then he will be green
def draw():
    asteroids = core.memory("asteroids")
    for i in range(0, len(asteroids)):
        giveLife = asteroids[i][len(asteroids[i]) - 1]
        if giveLife:
            pygame.draw.polygon(core.screenSettings.SCREEN, (0, 255, 0), [vertex.xy for vertex in asteroids[i][2]], 1)
        else:
            pygame.draw.polygon(core.screenSettings.SCREEN, (255, 255, 255), [vertex.xy for vertex in asteroids[i][2]], 1)