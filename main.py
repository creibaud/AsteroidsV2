import pygame
import sys
import math
import core.core as core
import components.Game as Game

def setUpScreen():
    core.screenSetUp.setTitle("Asteroids")
    core.screenSetUp.setBackground((0, 0, 0))
    core.screenSetUp.setFPS(60)
    core.screenSetUp.setScreenSize((1000, 800))
    core.screenSetUp.setScreen()

def setUp():
    Game.setUp()

    core.memory("GameAngle", math.radians(0))
    core.memory("GameIsAcceleration", math.radians(0))
    core.memory("Shooting", False)
    core.memory("GameLastShootTime", pygame.time.get_ticks())
    core.memory("CanBeHitTime", pygame.time.get_ticks())
    core.memory("createAsteroidTime", pygame.time.get_ticks())
    core.memory("GameOver", False)

def main():
    pygame.init()

    clock = pygame.time.Clock()
    setUpScreen()
    setUp()

    core.memory("StartGame", False)

    run = True
    while run:
        angle = core.memory("GameAngle")
        isAcceleration = core.memory("GameIsAcceleration")
        shoot = core.memory("Shooting")
        lastShootTime = core.memory("GameLastShootTime")
        life = core.memory("life")
        canBeHitTime = core.memory("CanBeHitTime")
        createAsteroidTime = core.memory("createAsteroidTime")
        canBeHit = core.memory("canBeHit")
        GameOver = core.memory("GameOver")
        StartGame = core.memory("StartGame")

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
                
                if event.key == pygame.K_r:
                    setUp()

                if event.key == pygame.K_SPACE:
                    core.memory("StartGame", True)
            
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
        
        core.screenSetUp.clean()

        if GameOver:
            fontGameOver = pygame.font.Font(None, 70)
            fontRestart = pygame.font.Font(None, 50)

            gameOverText = fontGameOver.render("Game Over", True, (255, 0, 0))
            restartText = fontRestart.render("Press R to restart", True, (255, 255, 255))

            Game.update()
            Game.draw()

            core.screenSettings.SCREEN.blit(gameOverText, (core.screenSettings.WIDTH / 2 - gameOverText.get_width() / 2, core.screenSettings.HEIGHT / 2 - gameOverText.get_height() / 2))
            core.screenSettings.SCREEN.blit(restartText, (core.screenSettings.WIDTH / 2 - restartText.get_width() / 2, core.screenSettings.HEIGHT / 2 - restartText.get_height() / 2 - 150))
            
        else:
            if not StartGame:
                canBeHitTime = pygame.time.get_ticks()

                Game.update()
                Game.draw()

                fontStartGame = pygame.font.Font(None, 50)
                fontTitle = pygame.font.Font(None, 100)
                startGameText = fontStartGame.render("Press Space to start", True, (255, 255, 255))
                titleText = fontTitle.render("Asteroids", True, (255, 255, 255))
                core.screenSettings.SCREEN.blit(titleText, (core.screenSettings.WIDTH / 2 - titleText.get_width() / 2, 200))
                core.screenSettings.SCREEN.blit(startGameText, (core.screenSettings.WIDTH / 2 - startGameText.get_width() / 2, core.screenSettings.HEIGHT / 2 - startGameText.get_height() / 2))
            
            else:
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

                if pygame.time.get_ticks() - canBeHitTime > core.gameSettings.CAN_BE_HIT_INTERVAL and not canBeHit:
                    core.memory("canBeHit", True)

                if pygame.time.get_ticks() - createAsteroidTime > core.gameSettings.CREATE_ASTEROID_INTERVAL:
                    core.memory("createAsteroidTime", pygame.time.get_ticks())
                    Game.createRandomAsteroid()

                if life <= 0:
                    core.memory("GameOver", True)

                Game.update()
                Game.draw()

        pygame.display.update()
        clock.tick(core.screenSettings.FPS)

    pygame.quit()
    sys.exit()

main()