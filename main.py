import sys, os
import pygame
from pygame import key
import random
import Characters
import SoundFx
from Menus import menuType, Menu

pygame.init()

WIDTH, HEIGHT = 900, 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Qix Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ARROW_KEYS = [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN]
FPS = 60

def draw_window():
        WIN.fill(BLACK)
        pygame.display.update()

def checkCollision(rect1, rect2):
    offsetX = rect2.x - rect1.x
    offsetY = rect2.y - rect1.y
    return rect1.mask.overlap(rect2.mask, (offsetX, offsetY)) != None

def main():

        speed = 5 # the speed of the main character; can and may change with the level
        offset = 40 # this is the image offset; used if the png has empty space. with this the player img will get closer to the bounderies
        memMovement = [] # used to draw line behind the player once they enter the grid
        dirChanges = [] # holds the coordinates of the grid which was covered by the player/ hols the coordinates in which the player changed direction
        clock = pygame.time.Clock()
        run = True
        draw_window()
        SoundFx.inGameInit()

        player = Characters.mainCharacter(round((WIDTH - offset) / 2), 455)
        canGoIngrid = False
        freedomCoor = (player.x, player.y) # the coordinate of which the player held down the rshift key to release themselves!

        enemies = [] 
        lastKey =  None   

        for i in range(5): # init enemies with random spawn location
                enemies.append(Characters.Enemy(random.randrange(WIDTH - offset), random.randrange(HEIGHT - offset)))

        for enemy in enemies:
                enemy.draw(WIN)

        while run: 
                clock.tick(FPS)
                if canGoIngrid: # this is for the tail line. If the player is holding down the shift key, start drawing
                        memMovement.append((player.x + offset / 2, player.y + offset))
                        pygame.draw.aalines(WIN, WHITE, False, memMovement)
                        # If the player was in the grid and now the moved to the edges, we should fill the area that they have covered:
                        if (player.y <= 0 or player.y >= HEIGHT - offset - 6) or (player.x <= 0 or player.x >= WIDTH - offset - 6): 
                                pygame.draw.aalines(WIN, WHITE, True, memMovement) # close the line
                                dirChanges.append((player.x, player.y)) # add the endpoint to the dirchange so we have all the coordinates that we need to fillout

                                """
                                Here we need to fillout the rectangle and maybe calculate the area
                                """

                                pygame.display.flip()
                                freedomCoor = (player.x, player.y) # player will let go of the shift once they made a rectangle so save that to continue from where they got to the edges
                                dirChanges.clear()
                                

                pygame.display.update() 

                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                run = False

                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_p: # press 'p' to print the main character's location
                                        print('X =', player.x, '     Y =', player.y) # debug

                                if event.key == pygame.K_RSHIFT: # save the coordinate
                                        freedomCoor = (player.x, player.y)
                                        memMovement.append((player.x + offset / 2, player.y + offset))
                                        dirChanges.clear()
                                        dirChanges.append((player.x, player.y))
                                
                                # check for any new direction input
                                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) or (event.key == pygame.K_RIGHT or event.key == pygame.K_d) or  (event.key == pygame.K_UP or event.key == pygame.K_w) or  (event.key == pygame.K_DOWN or event.key == pygame.K_d):
                                        dirChanges.append((player.x, player.y)) # this indicates a change in direction
                                        # print("Dir Change!" , dirChanges)
                        
                        if event.type == pygame.KEYUP:
                                if event.key == pygame.K_RSHIFT:
                                        canGoIngrid = False # if rshift released, dont go in the grid anymore and jump back to freedomCoor
                                        player.x = freedomCoor[0]
                                        player.y = freedomCoor[1]
                                        memMovement.clear()
                                        dirChanges.clear()

                keys = pygame.key.get_pressed()

                if (keys [pygame.K_RSHIFT]): 
                        canGoIngrid = True # jumps in the grid

                if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player.x - speed + 15 > 0:
                        if  canGoIngrid or (player.y <= 0 or player.y >= HEIGHT - offset - 6): # either be on the edges, or hold down the shift key to move
                                player.x -= speed


                elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player.x + speed + offset < WIDTH: # elif will prevent other angles; so only right angles are allowed...
                        if canGoIngrid or (player.y <= 0 or player.y >= HEIGHT - offset - 6):
                                player.x += speed

                elif (keys[pygame.K_UP] or keys[pygame.K_w]) and player.y + speed > 0:
                        if canGoIngrid or (player.x <= 0 or player.x >= WIDTH - offset - 6):
                                player.y -= speed

                elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and player.y + speed + offset < HEIGHT :
                        if canGoIngrid or (player.x <= 0 or player.x >= WIDTH - offset - 6):
                                player.y += speed
                
                elif (keys[pygame.K_ESCAPE]):
                        canGoIngrid = False
                        memMovement.clear()
                        SoundFx.inGamePause()
                        Menu.renderMenu(menuType.pauseMenu)
                        player.x, player.y = freedomCoor
                        SoundFx.inGameUnPause()
                                
                WIN.fill(BLACK)  
                player.draw(WIN)
                for enemy in enemies:
                        enemy.draw(WIN)

                for enemy in enemies: # enemy collisions
                        if checkCollision(player, enemy):
                                SoundFx.inGameStop()
                                print('u dead!')
                                player.health -= 10
                                SoundFx.gameOverSound.play(0)
                                pygame.time.wait(5000)
                                freedomCoor = (player.x, player.y)
                                Menu.renderMenu(menuType.mainMenu)
                                main()
                
        pygame.quit()

if __name__ == "__main__":
        Menu.renderMenu(menuType.mainMenu)
        main()
