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

    core.memory("life", 3)

def update():
    SpaceShip.update()
    Asteroid.update()
    bulletCollisionWithAsteroid()

def bulletCollisionWithAsteroid():
    bullets = core.memory("bullets")
    asteroids = core.memory("asteroids")

    for bullet in bullets:
        for asteroid in asteroids:
            bulletPosition = bullet[0]
            asteroidPosition = asteroid[0]
            asteroidSize = asteroid[3]

            if bulletPosition.distance_to(asteroidPosition) < Asteroid.getRadius(asteroidSize) + core.bulletSettings.BULLET_RADIUS:
                if asteroidSize != "small":
                    Asteroid.breakApart(asteroid, asteroidSize)
                
                bullets.remove(bullet)
                asteroids.remove(asteroid)
                break
    core.memory("bullets", bullets)
    core.memory("asteroids", asteroids)

def spaceShipCollisionWithAsteroid():
    asteroids = core.memory("asteroids")
    P = core.memory("SpaceShipP")
    B = core.memory("SpaceShipB")
    A = core.memory("SpaceShipA")
    C = core.memory("SpaceShipC")

    for asteroid in asteroids:
        positionAsteroid = asteroid[0]
        asteroidSize = asteroid[3]
        
        shipPoints = [P, B, A, C]
        for shipPoint in shipPoints:
            if positionAsteroid.distance_to(shipPoint) < Asteroid.getRadius(asteroidSize):
                return True
    return False

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
    canBeHit = core.memory("canBeHit")

    if not canBeHit:
        SpaceShip.animationHit()
    else:
        SpaceShip.draw((255, 165, 0))
        core.memory("framesHitAnimation", 0)
    SpaceShip.Bullets.draw()
    Asteroid.draw()
