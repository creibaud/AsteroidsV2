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

    core.printMemory()

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

        angle = core.memory("GameAngle")
        isAcceleration = core.memory("GameIsAcceleration")
        
        core.screenSetUp.clean()

        Game.rotateSpaceShip(angle)
        Game.spaceShipAccelerate(isAcceleration)

        Game.update()
        Game.draw()

        pygame.display.update()
        clock.tick(core.screenSettings.FPS)

    pygame.quit()
    sys.exit()

main()