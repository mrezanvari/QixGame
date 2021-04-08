import sys, os
from numpy.lib.financial import npv
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

def area(vertices):
    counter = 0
    total = 0
    for i in range(len(vertices)):
        counter += 1
        if i == len(vertices) - 1:
            j = 0
        else:
            j = i+1
        side1 = vertices[i][0] * vertices[j][1]
        side2 = vertices[i][1] * vertices[j][0]
        total += (side1-side2)
    return abs((total/2))


def main():

        speed = 5 # the speed of the main character; can and may change with the level
        offset = 40 # this is the image offset; used if the png has empty space. with this the player img will get closer to the bounderies
        memMovement = [] # used to draw line behind the player once they enter the grid
        dirChanges = [] # holds the coordinates of the grid which was covered by the player/ hols the coordinates in which the player changed direction
        clock = pygame.time.Clock()
        run = True
        draw_window()
        SoundFx.inGameInit() # start music
        traceLines = []
        isMoving = False # this indicates that the player is moving (This is not critical but it will help)

        player = Characters.mainCharacter(round((WIDTH - offset) / 2), 455)
        canGoInGrid = False
        freedomCoor = (player.x, player.y) # the coordinate of which the player held down the rshift key to release themselves!

        enemies = [] 
        movementKey_DOWN =  False

        lastKey = None

        for i in range(3): # init enemies with random spawn location
                enemies.append(Characters.Enemy(random.randrange(WIDTH - offset), random.randrange(HEIGHT - offset)))
        
        enemies.append(Characters.Enemy(0, 0, type=Characters.enemyType.sparx, dir='r', speed=2))
        enemies.append(Characters.Enemy(WIDTH - offset, HEIGHT - offset, type=Characters.enemyType.sparx, dir='l', speed=2))

        for enemy in enemies:
                enemy.draw(WIN)

        def gameOver(): # this is kinda temporary better to have it somewhere else...
                SoundFx.inGameStop()
                print('u dead!')
                player.health -= 10
                SoundFx.gameOverSound.play(0)
                pygame.time.wait(3000)
                freedomCoor = (player.x, player.y)
                memMovement.clear()
                dirChanges.clear()
                traceLines.clear()
                Menu.renderMenu(menuType.mainMenu) # jump to main menu
                main()

        while run: 
                clock.tick(FPS)
                if canGoInGrid: # this is for the tail line. If the player is holding down the shift key, start drawing
                        memMovement.append((player.x + offset / 2, player.y + offset))
                        traceLines.append(pygame.draw.aalines(WIN, WHITE, False, memMovement))
                        # If the player was in the grid and now the moved to the edges, we should fill the area that they have covered:
                        if (player.y <= 0 or player.y >= HEIGHT - offset - 6) or (player.x <= 0 or player.x >= WIDTH - offset - 6) and isMoving: # is moving can be removed but it prevents false valuse
                                traceLines.append(pygame.draw.aalines(WIN, WHITE, True, memMovement)) # close the line
                                dirChanges.append((player.x, player.y)) # add the endpoint to the dirchange so we have all the coordinates that we need to fillout

                                """
                                Here we need to fillout the rectangle and maybe calculate the area
                                """
                                print(dirChanges)

                                pygame.display.flip()
                                freedomCoor = (player.x, player.y) # player will let go of the shift once they made a rectangle so save that to continue from where they got to the edges
                                dirChanges.clear()
                                traceLines.clear()
                                canGoInGrid = False
                                movementKey_DOWN = False
                                # Menu.renderMenu(menuType.pauseMenu)

                pygame.display.update() 

                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                run = False

                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_p: # press 'p' to print the main character's location
                                        print('X =', player.x, '     Y =', player.y) # debug

                                if event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT: # save the coordinate
                                        freedomCoor = (player.x, player.y)
                                        memMovement.append((player.x + offset / 2, player.y + offset))
                                        dirChanges.clear()
                                        dirChanges.append((player.x, player.y))
                                
                                # check for any new direction input
                                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) or (event.key == pygame.K_RIGHT or event.key == pygame.K_d) or (event.key == pygame.K_UP or event.key == pygame.K_w) or  (event.key == pygame.K_DOWN or event.key == pygame.K_s) and canGoInGrid:
                                        if event.key != lastKey: # to prevent duplication if the user stopped and started again in the same direction
                                                # print('X =', player.x, '     Y =', player.y) # debug
                                                dirChanges.append((player.x, player.y)) # this indicates a change in direction
                                                lastKey = event.key
                                                isMoving = True
                                        movementKey_DOWN = True
                                        # print("Dir Change!" , dirChanges)
                        
                        if event.type == pygame.KEYUP:
                                if event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT:
                                        canGoInGrid = False # if rshift released, dont go in the grid anymore and jump back to freedomCoor
                                        player.x = freedomCoor[0]
                                        player.y = freedomCoor[1]
                                        memMovement.clear()
                                        dirChanges.clear()
                                        # it is not important to use isMoving but it will prevent false valuse. The false values can be handled with a simple try except block; if u decided to use try then remove isMoving...
                                        if (event.key == pygame.K_LEFT or event.key == pygame.K_a) or (event.key == pygame.K_RIGHT or event.key == pygame.K_d) or (event.key == pygame.K_UP or event.key == pygame.K_w) or  (event.key == pygame.K_DOWN or event.key == pygame.K_s) and canGoInGrid:
                                                isMoving = False

                                movementKey_DOWN = False

                enemies[-1].move(WIN)
                enemies[-2].move(WIN)

                keys = pygame.key.get_pressed()

                if (keys [pygame.K_RSHIFT] or keys [pygame.K_LSHIFT]): 
                        canGoInGrid = True # jumps in the grid

                if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player.x - speed + 15 > 0:
                        movementKey_DOWN = True
                        if  canGoInGrid or (player.y <= 0 or player.y >= HEIGHT - offset - 6): # either be on the edges, or hold down the shift key to move
                                player.x -= speed


                elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player.x + speed + offset < WIDTH: # elif will prevent other angles; so only right angles are allowed...
                        movementKey_DOWN = True
                        if canGoInGrid or (player.y <= 0 or player.y >= HEIGHT - offset - 6):
                                player.x += speed

                elif (keys[pygame.K_UP] or keys[pygame.K_w]) and player.y + speed > 0:
                        movementKey_DOWN = True
                        if canGoInGrid or (player.x <= 0 or player.x >= WIDTH - offset - 6):
                                player.y -= speed

                elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and player.y + speed + offset < HEIGHT :
                        movementKey_DOWN = True
                        if canGoInGrid or (player.x <= 0 or player.x >= WIDTH - offset - 6):
                                player.y += speed
                
                if (keys[pygame.K_ESCAPE]): # pause menu
                        canGoInGrid = False
                        memMovement.clear()
                        SoundFx.inGamePause()
                        Menu.renderMenu(menuType.pauseMenu)
                        player.x, player.y = freedomCoor # spawn back
                        SoundFx.inGameUnPause()
                                
                WIN.fill(BLACK)  
                player.draw(WIN)
                for enemy in enemies:
                        enemy.draw(WIN)

                for enemy in enemies: # enemy collisions
                        if checkCollision(player, enemy):
                               gameOver()

                        for move in memMovement:
                                if enemy.x == move[0] and enemy.y == move[1]:
                                        gameOver()

                if movementKey_DOWN:
                        for move in memMovement:
                                if player.x + offset / 2 == move[0] and player.y + offset == move[1]: # player coordinates shall not collide with any of the tracing lines
                                        gameOver()
                                        

        pygame.quit()

if __name__ == "__main__":
        Menu.renderMenu(menuType.mainMenu)
        main()
