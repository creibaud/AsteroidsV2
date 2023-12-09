import pygame
import math
import components.Bullets as Bullets
import core.core as core

# Set up the spaceship
def setUp():
    # Initialize the main variables of the spaceship
    core.spaceShipSetUp.setLenght(20)
    core.spaceShipSetUp.setWidth(10)
    core.spaceShipSetUp.setRotationSpeed(5)
    core.spaceShipSetUp.setThrustPower(0.1)
    core.spaceShipSetUp.setMaxSpeed(5)
    core.spaceShipSetUp.setDeceleration(0.75)

    # Initialize the position, velocity, acceleration, axe, alpha and points of the spaceship

    # Initialize the horizontal position
    core.memory("SpaceShipX", core.screenSettings.WIDTH / 2)

    # Initialize the vertical position
    core.memory("SpaceShipY", core.screenSettings.HEIGHT / 2)

    # Initialize the velocity
    core.memory("SpaceShipVelocity", pygame.math.Vector2(0, 0))

    # Initialize the acceleration
    core.memory("SpaceShipAcceleration", pygame.math.Vector2(0, 0))

    # Get the position of the spaceship
    x = core.memory("SpaceShipX")
    y = core.memory("SpaceShipY")

    # Initialize the P point of the geometry of the spaceship
    core.memory("SpaceShipP", pygame.math.Vector2(x, y))

    # Initialize the alpha angle of the geometry of the spaceship
    core.memory("SpaceShipAlpha", math.radians(120))

    # Initialize the axe of the geometry of the spaceship
    core.memory("SpaceShipAxe", pygame.math.Vector2(1, 0))

    # Get P, axe and alpha
    P = core.memory("SpaceShipP")
    alpha = core.memory("SpaceShipAlpha")
    axe = core.memory("SpaceShipAxe")

    # Initialize the A, B and C point of the geometry of the spaceship
    core.memory("SpaceShipA", P + core.spaceShipSettings.LENGTH * axe)
    core.memory("SpaceShipB", P + core.spaceShipSettings.WIDTH * axe.rotate(-math.degrees(alpha)))
    core.memory("SpaceShipC", P + core.spaceShipSettings.WIDTH * axe.rotate(math.degrees(alpha)))

    # Initialize the bullets
    Bullets.setUp()

    # Initialize the canBeHit and framesHitAnimation
    core.memory("canBeHit", False)
    core.memory("framesHitAnimation", 0)

# Update the spaceship
def update():
    # Update the position, velocity, acceleration, axe, alpha and points of the spaceship
    velocity = core.memory("SpaceShipVelocity")
    accelerate = core.memory("SpaceShipAcceleration")
    velocity += accelerate
    core.memory("SpaceShipVelocity", velocity)

    velocity = core.memory("SpaceShipVelocity")

    # If the velocity is not 0, scale the velocity
    if velocity.length() != 0:
        velocity.scale_to_length(min(velocity.length(), core.spaceShipSettings.MAX_SPEED))
    
    P = core.memory("SpaceShipP")
    
    # If the spaceship is out of the screen
    if P.x < 0:
        P.x = core.screenSettings.WIDTH
    elif P.x > core.screenSettings.WIDTH:
        P.x = 0
    
    if P.y < 0:
        P.y = core.screenSettings.HEIGHT
    elif P.y > core.screenSettings.HEIGHT:
        P.y = 0

    # Update the Points
    P = core.memory("SpaceShipP")
    axe = core.memory("SpaceShipAxe")
    alpha = core.memory("SpaceShipAlpha")
    velocity = core.memory("SpaceShipVelocity")

    P += velocity
    core.memory("SpaceShipP", P)
    
    P = core.memory("SpaceShipP")
    core.memory("SpaceShipA", P + core.spaceShipSettings.LENGTH * axe)
    core.memory("SpaceShipB", P + core.spaceShipSettings.WIDTH * axe.rotate(-math.degrees(alpha)))
    core.memory("SpaceShipC", P + core.spaceShipSettings.WIDTH * axe.rotate(math.degrees(alpha)))

    bullets = core.memory("bullets")
    Bullets.update()
    bullets = [bullet for bullet in bullets if bullet[0].x <= core.screenSettings.WIDTH and bullet[0].x >= 0 and bullet[0].y <= core.screenSettings.HEIGHT and bullet[0].y >= 0]

# Acceleration with trus power
def accelerate():
    axe = core.memory("SpaceShipAxe")
    acceleration = core.memory("SpaceShipAcceleration")
    thrustVector = axe * core.spaceShipSettings.THRUST_POWER
    acceleration += thrustVector
    core.memory("SpaceShipAcceleration", acceleration)

# Deceleration
def decelerate():
    acceleration = core.memory("SpaceShipAcceleration")
    acceleration *= core.spaceShipSettings.DECELERATION
    core.memory("SpaceShipAcceleration", acceleration)

# Rotate the spaceship
def rotate(angle):
    axe = core.memory("SpaceShipAxe")
    axe.rotate_ip(math.degrees(angle))
    axe = core.memory("SpaceShipAxe")

# Hit the spaceship
def shoot():
    axe = core.memory("SpaceShipAxe")
    direction = axe.copy()
    A = core.memory("SpaceShipA")
    Bullets.add(A, direction)

# Animation for the hit
def animationHit():
    framesHitAnimation = core.memory("framesHitAnimation")

    if framesHitAnimation < 15:
        draw((0, 0, 0))
    else:
        draw((255, 165, 0))

    framesHitAnimation += 1
    core.memory("framesHitAnimation", framesHitAnimation)
    framesHitAnimation = core.memory("framesHitAnimation")
    
    if framesHitAnimation > 30:
        core.memory("framesHitAnimation", 0)

# Draw the spaceship
def draw(color):
    P = core.memory("SpaceShipP")
    B = core.memory("SpaceShipB")
    A = core.memory("SpaceShipA")
    C = core.memory("SpaceShipC")
    pygame.draw.polygon(core.screenSettings.SCREEN, color, [P, B, A, C], 3)