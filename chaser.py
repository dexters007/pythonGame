# Chaser is a game where the user will have to try catch the star
# If the user catches the start they win
# if the user hits one of the walls they lose and the game is over
# If the user doesnt catch the star or hit the block the blocks will run off the screen and the user loses

import pygame
import random

# Get the game started 
pygame.init()

# Create the screen size

screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height))

# Create players and enemhy with Images

player = pygame.image.load("redcircle.png")
wall = pygame.image.load("greyblock.png")
wall2 = pygame.image.load("whiteblock.png")
wall3 = pygame.image.load("yellowblock.png")
star = pygame.image.load("star.png")

# Create width and height of images for boundary Detection

wall_height = wall.get_height()
wall_width = wall.get_width()
wall2_height = wall2.get_height()
wall2_width = wall2.get_width()
player_height = player.get_height()
player_width = player.get_width()
star_height = star.get_height()
star_width = star.get_width()

print("This is the height of the wall: " +str(wall_height))
print("This is the width of the wall: " +str(wall_width))

# Store Positions

playerXPosition = 100
playerYPosition = 100

wallXPosition = 800
wallYPosition = 680

wall2XPosition = 800
wall2YPosition = 0

wall3XPosition = 340
wall3YPosition = 0

starXPosition = 0
starYPosition = random.randint(0, screen_height- star_height)

# create conditions to check if buttons are pushed

keyUp= False
keyDown = False
keyLeft = False
keyRight = False

# Looping structure of the game
# Bring images to the screen

while 1:
    screen.fill(0)
    screen.blit(wall, (wallXPosition,wallYPosition)) 
    screen.blit(wall2, (wall2XPosition,wall2YPosition))
    screen.blit(player, (playerXPosition,playerYPosition))
    screen.blit(wall3, (wall3XPosition,wall3YPosition))
    screen.blit(star, (starXPosition,starYPosition))

    pygame.display.flip()# Update the screen

    # Loop through events of the game

    for event in pygame.event.get():

        # Check if the user quits the game

        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        
        # Check if user presses the keys down

        if event.type == pygame.KEYDOWN:
            
            # Test if right buttons are pushed

            if event.key == pygame.K_UP:
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
        
        # Check when button is released

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False

    # Check if buttons are pushed

    if keyUp == True:
        if playerYPosition > 0:
            playerYPosition -=1
    if keyDown == True:
        if playerYPosition < screen_height - player_height:
            playerYPosition +=1
    if keyLeft == True:
        if playerXPosition > 0:
            playerXPosition -=1
    if keyRight == True:
        if playerXPosition < screen_width - player_width:
            playerXPosition +=1

    # check for collision

    playerBox = pygame.Rect(player.get_rect())

    playerBox.top = playerYPosition
    playerBox.left = playerXPosition

    wallBox = pygame.Rect(wall.get_rect())
    wallBox.top = wallYPosition
    wallBox.left = wallXPosition

    wall2Box = pygame.Rect(wall2.get_rect())
    wall2Box.top = wall2YPosition
    wall2Box.left = wall2XPosition

    wall3Box = pygame.Rect(wall3.get_rect())
    wall3Box.top = wall3YPosition
    wall3Box.left = wall3XPosition
    
    starBox = pygame.Rect(star.get_rect())
    starBox.top = starYPosition
    starBox.left = starXPosition

    # Check for collision of player and walls

    if playerBox.colliderect(wallBox):

        print("Game Over, You Lose")

        pygame.quit()
        exit()

    if playerBox.colliderect(wall2Box):

        print("Game Over, You Lose")

        pygame.quit()
        exit()

    if playerBox.colliderect(wall3Box):

        print("Game Over, You lose")

        pygame.quit()
        exit()

    # Check if player gets the star
    if playerBox.colliderect(starBox):

        print("You Caught the star, You Win")
        pygame.quit()
        exit()
    
    # If the last wall goes off screen without player catching the star player loses

    if wall2XPosition < 0 - wall2_width:
        print("You Lose")
        pygame.quit()
        exit()


    wallYPosition -=0.15
    wall2XPosition -=0.15
    wall3YPosition +=0.15
    starXPosition +=0.65