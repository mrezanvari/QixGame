import sys, os
import pygame
from pygame import key
import random
import Characters
import SoundFx

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
        clock = pygame.time.Clock()
        run = True
        draw_window()

        player = Characters.mainCharacter(round((WIDTH - offset) / 2), 455)
        canGoIngrid = False
        freedomCoor = (0, 0) # the coordinate of which the player held down the rshift key to release themselves!

        enemies = [] 

        for i in range(5): # init enemies with random spawn location
                enemies.append(Characters.Enemy(random.randrange(WIDTH - offset), random.randrange(HEIGHT - offset)))

        for enemy in enemies:
                enemy.draw(WIN)

        while run: 
                clock.tick(FPS)
                pygame.display.update() 

                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                run = False

                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_p: # press 'p' to print the main character's location
                                        print('X =', player.x, '     Y =', player.y) # debug

                                if event.key == pygame.K_RSHIFT: # save the coordinate
                                        freedomCoor = (player.x, player.y)
                        
                        if event.type == pygame.KEYUP:
                                if event.key == pygame.K_RSHIFT:
                                        canGoIngrid = False # if rshift released, dont go in the grid anymore and jump back to freedomCoor
                                        player.x = freedomCoor[0]
                                        player.y = freedomCoor[1]

                keys = pygame.key.get_pressed()

                if (keys [pygame.K_RSHIFT]): 
                        canGoIngrid = True # jumps in the grid
                        
                
                if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player.x - speed + 15 > 0:
                        if  canGoIngrid or (player.y <= 0 or player.y >= HEIGHT - offset - 6):
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
                                
                WIN.fill(BLACK)  
                player.draw(WIN)
                for enemy in enemies:
                        enemy.draw(WIN)

                for enemy in enemies:
                        if checkCollision(player, enemy):
                                print('u dead!')
                                player.health -= 10
                                SoundFx.gameOverSound.play(0)
                                pygame.time.wait(5000)
                                freedomCoor = (player.x, player.y)
                                main() # reset the game
                
        pygame.quit()

if __name__ == "__main__":
        main()
