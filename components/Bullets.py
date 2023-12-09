import pygame
import core.core as core

# Set up the bullets
def setUp():
    # Initialize the main variables of the bullets
    core.bulletSetUp.setSpeed(10)
    core.bulletSetUp.setShootInterval(150)
    core.bulletSetUp.setRadius(3)

    # Initialize the list of bullets
    core.memory("bullets", [])

# Add a bullet to the list of bullets
def add(position, direction):
    # Get the list of bullets
    bullets = core.memory("bullets")

    # Add the bullet to the list
    bullets.append((position, direction))

    # Update the list of bullets
    core.memory("bullets", bullets)

# Update the bullets stats
def update():
    # Get the list of bullets
    bullets = core.memory("bullets")

    # Update the position
    for i in range(0, len(bullets)):
        position, direction = bullets[i]
        position += direction * core.bulletSettings.BULLET_SPEED
    
    # Update the list of bullets
    core.memory("bullets", bullets)

# Draw the bullets
def draw():
    bullets = core.memory("bullets")
    for i in range(0, len(bullets)):
        position = bullets[i][0]
        pygame.draw.circle(core.screenSettings.SCREEN, (255, 255, 255), (int(position.x), int(position.y)), core.bulletSettings.BULLET_RADIUS)