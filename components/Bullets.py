import pygame
import core.core as core

def setUp():
    core.bulletSetUp.setSpeed(10)
    core.bulletSetUp.setShootInterval(150)
    core.bulletSetUp.setRadius(3)
    core.memory("bullets", [])

def add(position, direction):
    bullets = core.memory("bullets")
    bullets.append((position, direction))
    core.memory("bullets", bullets)

def update():
    bullets = core.memory("bullets")
    for i in range(0, len(bullets)):
        position, direction = bullets[i]
        position += direction * core.bulletSettings.BULLET_SPEED
    core.memory("bullets", bullets)

def draw():
    bullets = core.memory("bullets")
    for i in range(0, len(bullets)):
        position = bullets[i][0]
        pygame.draw.circle(core.screenSettings.SCREEN, (255, 255, 255), (int(position.x), int(position.y)), core.bulletSettings.BULLET_RADIUS)