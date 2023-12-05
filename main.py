import pygame
import sys
import math
import core.core as core
import components.Game as Game

def setUp():
    core.screenSetUp.setTitle("Asteroids")
    core.screenSetUp.setBackground((0, 0, 0))
    core.screenSetUp.setFPS(60)
    core.screenSetUp.setScreenSize((1000, 800))
    core.screenSetUp.setScreen()

    Game.setUp()

def main():
    pygame.init()

    clock = pygame.time.Clock()
    setUp()

    core.memory("GameAngle", math.radians(0))
    core.memory("GameIsAcceleration", math.radians(0))
    core.memory("Shooting", False)
    core.memory("GameLastShootTime", pygame.time.get_ticks())
    core.memory("CanBeHitTime", pygame.time.get_ticks())
    core.memory("GameOver", False)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    core.memory("GameAngle", math.radians(-core.spaceShipSettings.ROTATION_SPEED))
                
                if event.key == pygame.K_d:
                    core.memory("GameAngle", math.radians(core.spaceShipSettings.ROTATION_SPEED))
                
                if event.key == pygame.K_z:
                    core.memory("GameIsAcceleration", True)
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_q or event.key == pygame.K_d:
                    core.memory("GameAngle", math.radians(0))
                
                if event.key == pygame.K_z:
                    core.memory("GameIsAcceleration", False)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    core.memory("Shooting", True)
        
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    core.memory("Shooting", False)

        angle = core.memory("GameAngle")
        isAcceleration = core.memory("GameIsAcceleration")
        shoot = core.memory("Shooting")
        lastShootTime = core.memory("GameLastShootTime")
        life = core.memory("life")
        canBeHitTime = core.memory("CanBeHitTime")
        canBeHit = core.memory("canBeHit")
        GameOver = core.memory("GameOver")
        
        core.screenSetUp.clean()

        Game.rotateSpaceShip(angle)
        Game.spaceShipAccelerate(isAcceleration)

        if shoot and (pygame.time.get_ticks() - lastShootTime) > core.bulletSettings.SHOOT_INTERVAL:
            core.memory("GameLastShootTime", pygame.time.get_ticks())
            Game.shootSpaceShip()

        if Game.spaceShipCollisionWithAsteroid() and canBeHit:
            life -= 1
            core.memory("canBeHit", False)
            core.memory("CanBeHitTime", pygame.time.get_ticks())
            core.memory("life", life)

        if pygame.time.get_ticks() - canBeHitTime > 3000 and not canBeHit:
            core.memory("canBeHit", True)

        if life <= 0:
            core.memory("GameOver", True)
            print("GameOver")

        Game.update()
        Game.draw()

        print(canBeHit)

        pygame.display.update()
        clock.tick(core.screenSettings.FPS)

    pygame.quit()
    sys.exit()

main()