import pygame
import math
import components.Bullets as Bullets
import core.core as core

def setUp():
    core.spaceShipSetUp.setLenght(20)
    core.spaceShipSetUp.setWidth(10)
    core.spaceShipSetUp.setRotationSpeed(5)
    core.spaceShipSetUp.setThrustPower(0.1)
    core.spaceShipSetUp.setMaxSpeed(5)
    core.spaceShipSetUp.setDeceleration(0.75)

    core.memory("SpaceShipX", core.screenSettings.WIDTH / 2)
    core.memory("SpaceShipY", core.screenSettings.HEIGHT / 2)
    core.memory("SpaceShipVelocity", pygame.math.Vector2(0, 0))
    core.memory("SpaceShipAcceleration", pygame.math.Vector2(0, 0))
    core.memory("SpaceShipThrusting", False)

    x = core.memory("SpaceShipX")
    y = core.memory("SpaceShipY")

    core.memory("SpaceShipP", pygame.math.Vector2(x, y))
    core.memory("SpaceShipAlpha", math.radians(120))
    core.memory("SpaceShipAxe", pygame.math.Vector2(1, 0))

    P = core.memory("SpaceShipP")
    alpha = core.memory("SpaceShipAlpha")
    axe = core.memory("SpaceShipAxe")

    core.memory("SpaceShipA", P + core.spaceShipSettings.LENGTH * axe)
    core.memory("SpaceShipB", P + core.spaceShipSettings.WIDTH * axe.rotate(-math.degrees(alpha)))
    core.memory("SpaceShipC", P + core.spaceShipSettings.WIDTH * axe.rotate(math.degrees(alpha)))

    Bullets.setUp()
    core.memory("canBeHit", False)
    core.memory("framesHitAnimation", 0)

def update():
    thrusting = core.memory("SpaceShipThrusting")

    if thrusting:
        accelerate()
    else:
        decelerate()
    
    velocity = core.memory("SpaceShipVelocity")
    accelerate = core.memory("SpaceShipAcceleration")
    velocity += accelerate
    core.memory("SpaceShipVelocity", velocity)

    velocity = core.memory("SpaceShipVelocity")

    if velocity.length() != 0:
        velocity.scale_to_length(min(velocity.length(), core.spaceShipSettings.MAX_SPEED))
    
    P = core.memory("SpaceShipP")

    if P.x < 0:
        P.x = core.screenSettings.WIDTH
    elif P.x > core.screenSettings.WIDTH:
        P.x = 0
    
    if P.y < 0:
        P.y = core.screenSettings.HEIGHT
    elif P.y > core.screenSettings.HEIGHT:
        P.y = 0
    
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

def accelerate():
    axe = core.memory("SpaceShipAxe")
    acceleration = core.memory("SpaceShipAcceleration")
    thrustVector= axe * core.spaceShipSettings.THRUST_POWER
    acceleration += thrustVector
    core.memory("SpaceShipAcceleration", acceleration)

def decelerate():
    acceleration = core.memory("SpaceShipAcceleration")
    acceleration *= core.spaceShipSettings.DECELERATION
    core.memory("SpaceShipAcceleration", acceleration)

def rotate(angle):
    axe = core.memory("SpaceShipAxe")
    axe.rotate_ip(math.degrees(angle))
    axe = core.memory("SpaceShipAxe")

def shoot():
    axe = core.memory("SpaceShipAxe")
    direction = axe.copy()
    A = core.memory("SpaceShipA")
    Bullets.add(A, direction)

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

def draw(color):
    P = core.memory("SpaceShipP")
    B = core.memory("SpaceShipB")
    A = core.memory("SpaceShipA")
    C = core.memory("SpaceShipC")
    pygame.draw.polygon(core.screenSettings.SCREEN, color, [P, B, A, C], 3)