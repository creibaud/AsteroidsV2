import pygame
import random
import math
import core.core as core
import components.SpaceShip as SpaceShip
import components.Asteroid as Asteroid

def setUp():
    SpaceShip.setUp()
    Asteroid.setUp()

    for i in range(0, 10):
        createRandomAsteroid()

    core.memory("life", 3)
    core.memory("score", 0)
    core.memory("scoreLimiteLevel", 1000)
    core.memory("level", 1)

def update():
    SpaceShip.update()
    Asteroid.update()
    bulletCollisionWithAsteroid()
    score = core.memory("score")
    scoreLimiteLevel = core.memory("scoreLimiteLevel")

    if score >= scoreLimiteLevel and score != 0:
        core.gameSettings.CREATE_ASTEROID_INTERVAL -= core.gameSettings.DECRESING_INTERVAL
        core.gameSettings.DECRESING_INTERVAL /= 2
        core.memory("scoreLimiteLevel", scoreLimiteLevel)

    core.memory("level", math.ceil(score / 1000))

def createRandomAsteroid():
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

def bulletCollisionWithAsteroid():
    bullets = core.memory("bullets")
    asteroids = core.memory("asteroids")

    for bullet in bullets:
        for asteroid in asteroids:
            bulletPosition = bullet[0]
            asteroidPosition = asteroid[0]
            asteroidSize = asteroid[3]
            score = core.memory("score")

            if bulletPosition.distance_to(asteroidPosition) < Asteroid.getRadius(asteroidSize) + core.bulletSettings.BULLET_RADIUS:
                if asteroidSize != "small":
                    Asteroid.breakApart(asteroid, asteroidSize)
                    if asteroidSize == "big":
                        core.memory("score", score + 100)
                    elif asteroidSize == "medium":
                        core.memory("score", score + 50)
                else:
                    core.memory("score", score + 25)
                
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

def displayLife():
    alpha = math.radians(120)
    axe = pygame.math.Vector2(0, -1)

    life = core.memory("life")

    for i in range(life):
        P = pygame.math.Vector2(109 + i * 30, 160)
        A = P + core.spaceShipSettings.LENGTH * axe
        B = P + core.spaceShipSettings.WIDTH * axe.rotate(-math.degrees(alpha))
        C = P + core.spaceShipSettings.WIDTH * axe.rotate(math.degrees(alpha))
        pygame.draw.polygon(core.screenSettings.SCREEN, (255, 0, 0), [P, B, A, C], 3)

def displayScore():
    score = core.memory("score")
    font = pygame.font.Font(None, 50)
    scoreText = font.render(str(score), True, (255, 255, 255))
    core.screenSettings.SCREEN.blit(scoreText, (100, 100))

def displayLevel():
    level = core.memory("level")
    font = pygame.font.Font(None, 50)
    levelText = font.render("Level : " + str(level), True, (255, 255, 255))
    core.screenSettings.SCREEN.blit(levelText, (core.screenSettings.WIDTH - 100 - levelText.get_width(), 100))

def draw():
    canBeHit = core.memory("canBeHit")
    GameOver = core.memory("GameOver")

    if not GameOver:
        if not canBeHit:
            SpaceShip.animationHit()
        else:
            SpaceShip.draw((255, 165, 0))
            core.memory("framesHitAnimation", 0)

        SpaceShip.Bullets.draw()
        
    Asteroid.draw()
    displayLife()
    displayScore()
    displayLevel()
