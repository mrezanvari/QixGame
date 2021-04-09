"""
Character class containing both the main character and the enemies!
EnemyType will indicate the type of the enemy and their corresponding movement
"""

import os
import pygame
from enum import Enum
import main
import Utils

playerICON = Utils.loadImg(os.path.join("assets", "frog.png")) #just test lol 
playerICON = Utils.scaleImg(playerICON, 40, 43)

playerGameOverIcon = Utils.loadImg(os.path.join("assets", "frog_cry.png")) #just test lol 
playerGameOverIcon = Utils.scaleImg(playerGameOverIcon, 50, 50)

playerWorried = Utils.loadImg(os.path.join("assets", "frog_worried.png")) #just test lol 
playerWorried = Utils.scaleImg(playerWorried, 45, 45)

enemyICON = Utils.loadImg(os.path.join("assets", "bomb.png")) #just test lol
enemyICON = Utils.scaleImg(enemyICON, 40, 40)

offset = 40 

pygame.init()


class enemyType(Enum): # menu types; will be selected from main.py
    sparx = 0
    qix = 1

class mainCharacter(pygame.sprite.Sprite):
        def __init__(self, x, y, width=10, height=10, health=100):
                super().__init__()
                self.x = x
                self.y = y
                self.width = width
                self.height = height
                self.health = health
                self.max_health = health
                self.color = [255,100,40]
                self.image = playerICON
                self.rect = self.image.get_rect()
                self.rect.topleft = (self.x, self.y)
                self.mask = pygame.mask.from_surface(self.image)

        def draw(self, screen):
                screen.blit(self.image, (self.x, self.y))
        
        def update(self):
                self.rect.topleft = (self.x, self.y)

        def setImg(self, img):
                self.image = img

class Enemy(pygame.sprite.Sprite):
        def __init__(self, x, y, width=10, height=10, health=100, type=enemyType.sparx, dir='r', speed=2):
                super().__init__()
                self.x = x
                self.y = y
                self.width = width
                self.height = height
                self.health = health
                self.max_health = health
                self.color = [255,100,40]
                self.image = enemyICON
                self.rect = self.image.get_rect()
                self.rect.topleft = (self.x, self.y)
                self.mask = pygame.mask.from_surface(self.image)
                self.type=type
                self.dir=dir
                self.speed  = speed

        def draw(self, screen):
                screen.blit(self.image, (self.x, self.y))

        def update(self):
                self.rect.topleft = (self.x, self.y)

        def move(self, screen):
                
                if self.type == enemyType.sparx:
                        if self.dir == 'r' and self.x < main.WIDTH - offset:
                                self.x += self.speed
                        if self.dir == 'r' and self.x >= main.WIDTH - offset:
                                self.x = main.WIDTH - offset
                                self.dir = 'd'

                        if self.dir == 'd' and self.y < main.HEIGHT - offset:
                                self.y += self.speed
                        if self.dir == 'd' and self.y >= main.HEIGHT - offset:
                                self.y = main.HEIGHT - offset
                                self.dir = 'l'

                        if self.dir == 'l' and self.x > 0:
                                self.x -= self.speed
                        if self.dir == 'l' and self.x <= 0:
                                self.x = 0
                                self.dir = 'u'

                        if self.dir == 'u' and self.y > 0:
                                self.y -= self.speed
                        if self.dir == 'u' and self.y <= 0:
                                self.y = 0
                                self.dir = 'r'
                
                self.draw(screen)