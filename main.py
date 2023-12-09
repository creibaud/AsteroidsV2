import pygame
import sys
import math
import core.core as core
import components.Game as Game

# Function for setting up the screen
def setUpScreen():
    core.screenSetUp.setTitle("Asteroids")
    core.screenSetUp.setBackground((0, 0, 0))
    core.screenSetUp.setFPS(60)
    core.screenSetUp.setScreenSize((1000, 800))
    core.screenSetUp.setScreen()

# Function for setting up the main variables and the game (spaceship, asteroids, bullets, etc...)
def setUp():
    Game.setUp()
    
    # Initialize the game variables and store them in the MEMORY_STORAGE variable

    # Actual angle of the spaceship
    core.memory("GameAngle", math.radians(0))

    # If the spacehip is accelerating
    core.memory("GameIsAcceleration", math.radians(0))

     # If the spacehip is shooting
    core.memory("Shooting", False)

    # Last time the spaceship shoot
    core.memory("GameLastShootTime", pygame.time.get_ticks())

    # If the spacehip is out of the interval where he can't be hit
    core.memory("CanBeHitTime", pygame.time.get_ticks())

    # Create asteroids depending on the time and interval
    core.memory("createAsteroidTime", pygame.time.get_ticks())

    # GameOver state
    core.memory("GameOver", False)

    # StartGame state
    core.memory("StartGame", False)

# Function for setting up the main music
def musicSetUp():
    # Set up the path of the music
    path = "assets/music.mp3"

    # Initialize the mixer
    pygame.mixer.init()

    # Load the music
    pygame.mixer.music.load(path)
    
    # Play the music in loop
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play(-1)

# Function to read
def readFile(filename):
    file = open(filename, "r")
    content = file.read()
    file.close()
    return content

# Function to write
def writeFile(filename, content):
    file = open(filename, "w")
    file.write(content)
    file.close()

# Main function
def main():
    # Initialize pygame
    pygame.init()

    # Set up the Clock
    clock = pygame.time.Clock()

    # Call the setup functions
    setUpScreen()
    setUp()
    musicSetUp()

    # Read File
    path = "data/BestScore.txt"
    core.memory("BestScore", readFile(path))

    # Loop main variable
    run = True

    # Main loop
    while run:
        # Get the main variables from the MEMORY_STORAGE variable
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

        # Main events (user interactions)
        for event in pygame.event.get():
            # If the user click on the red cross of the screen to quit the game
            if event.type == pygame.QUIT:
                run = False

            # If the music is finished so we can do the loop again of the music
            if event.type == pygame.constants.USEREVENT:
                pygame.mixer.music.play()
            
            # If the user press a key
            if event.type == pygame.KEYDOWN:
                # If the user press the q key then we rotate the spaceship to the left
                if event.key == pygame.K_q:
                    core.memory("GameAngle", math.radians(-core.spaceShipSettings.ROTATION_SPEED))
                
                # If the user press the d key then we rotate the spaceship to the right
                if event.key == pygame.K_d:
                    core.memory("GameAngle", math.radians(core.spaceShipSettings.ROTATION_SPEED))

                # If the user press the z key then we accelerate the spaceship  
                if event.key == pygame.K_z:
                    core.memory("GameIsAcceleration", True)
                
                """
                if event.key == pygame.K_s:
                    velocity = core.memory("SpaceShipVelocity")
                    velocity *= 0.5
                    core.memory("SpaceShipVelocity", velocity)
                """
                
                # If the user press the r key then we restart the game
                if event.key == pygame.K_r:
                    setUp()
            
            # If the user release a key
            if event.type == pygame.KEYUP:
                # If the user release the q or d key then we stop the rotation of the spaceship
                if event.key == pygame.K_q or event.key == pygame.K_d:
                    core.memory("GameAngle", math.radians(0))
                
                # If the user release the z key then we stop the acceleration of the spaceship
                if event.key == pygame.K_z:
                    core.memory("GameIsAcceleration", False)
            
            # If the user click on the mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user click on the left mouse button
                if event.button == 1:
                    # Get the position of the mouse
                    mousePosition = pygame.mouse.get_pos()

                    # Get the hitbox of the button
                    rect = core.memory("rectButton")
                    
                    # If the user click on the button and the game is not started then we start the game
                    if rect.collidepoint(mousePosition) and not StartGame:
                        core.memory("StartGame", True)
                    
                    # If the user click on the button and the game is started then we shoot
                    if StartGame:
                        core.memory("Shooting", True)
            
            # If the user release the mouse button
            if event.type == pygame.MOUSEBUTTONUP:
                # If the user release the left mouse button then we stop the shooting
                if event.button == 1:
                    core.memory("Shooting", False)
        
        # We refresh the screen
        core.screenSetUp.clean()
        
        # If the game is over then we display the game over screen
        if GameOver:
            # Set up the font
            fontGameOver = pygame.font.Font(None, 70)
            fontRestart = pygame.font.Font(None, 50)
            
            # Set up the text
            gameOverText = fontGameOver.render("Game Over", True, (255, 0, 0))
            restartText = fontRestart.render("Press R to restart", True, (255, 255, 255))

            # We continue the animation of the game but the user can't move the ship
            Game.update()
            Game.draw()

            # Write the Score if is over the Old Best Score
            score = int(core.memory("score"))
            BestScore = int(core.memory("BestScore"))

            if score > BestScore:
                writeFile(path, str(score))
                core.memory("BestScore", score)
            
            # We display the text
            core.screenSettings.SCREEN.blit(gameOverText, (core.screenSettings.WIDTH / 2 - gameOverText.get_width() / 2, core.screenSettings.HEIGHT / 2 - gameOverText.get_height() / 2))
            core.screenSettings.SCREEN.blit(restartText, (core.screenSettings.WIDTH / 2 - restartText.get_width() / 2, core.screenSettings.HEIGHT / 2 - restartText.get_height() / 2 - 150))
        
        # if the game is not over then we display the game
        else:
            # If the game is not started then we display the start screen
            if not StartGame:
                # update canBeHitTime variable
                canBeHitTime = pygame.time.get_ticks()

                # We continue the animation of the game but the user can't move the ship
                Game.update()
                Game.draw()
                
                # Set up the font
                fontTitle = pygame.font.Font(None, 100)
                fontBestScore = pygame.font.Font(None, 50)

                ActualBestScore = core.memory("BestScore")
                
                # Set up the text
                titleText = fontTitle.render("Asteroids", True, (255, 255, 255))
                bestScoreText = fontBestScore.render("Best Score : " + str(ActualBestScore), True, (255, 255, 255))

                # We display the text
                core.screenSettings.SCREEN.blit(titleText, (core.screenSettings.WIDTH / 2 - titleText.get_width() / 2, 200))
                core.screenSettings.SCREEN.blit(bestScoreText, (core.screenSettings.WIDTH / 2 - bestScoreText.get_width() / 2, 290))
            
            # If the game is started then we display the game
            else:
                # update rotation and acceleration of the spaceship 
                Game.rotateSpaceShip(angle)
                Game.spaceShipAccelerate(isAcceleration)

                # If the user is shooting then we shoot, we regulate the firing rate
                if shoot and (pygame.time.get_ticks() - lastShootTime) > core.bulletSettings.SHOOT_INTERVAL:
                    # reset the time to the previous shoot
                    core.memory("GameLastShootTime", pygame.time.get_ticks())

                    # shoot
                    Game.shootSpaceShip()

                # If the spaceship collide with an asteroid then we remove a life and we can't be hit for a certain time
                if Game.spaceShipCollisionWithAsteroid() and canBeHit:
                    life -= 1

                    # reset the time where we can't be hit
                    core.memory("CanBeHitTime", pygame.time.get_ticks())

                    # update the variables
                    core.memory("canBeHit", False)
                    core.memory("life", life)

                # If the spaceship is out of the interval where he can't be hit then we can be hit again
                if pygame.time.get_ticks() - canBeHitTime > core.gameSettings.CAN_BE_HIT_INTERVAL and not canBeHit:
                    # update the variables
                    core.memory("canBeHit", True)

                # If the time is out of the interval where we can create an asteroid then we create an asteroid
                if pygame.time.get_ticks() - createAsteroidTime > core.gameSettings.CREATE_ASTEROID_INTERVAL:
                    # reset the time of creation of the asteroid
                    core.memory("createAsteroidTime", pygame.time.get_ticks())

                    # create an asteroid
                    Game.createRandomAsteroid()

                # If the user has no more life
                if life <= 0:
                    # Then game is over
                    core.memory("GameOver", True)

                # We update the game state
                Game.update()

                # We draw the elements
                Game.draw()

        # We update the screen
        pygame.display.update()

        # We regulate the frames
        clock.tick(core.screenSettings.FPS)
    
    # If the user quit the game then we end the mixer, pygame and the program
    pygame.mixer.quit()
    pygame.quit()
    sys.exit()

# Start the game
main()