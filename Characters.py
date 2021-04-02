"""
Character class containing both the main character and the enemies! Note that both enemy and main character are the same; its just a difference in naming... Afterall, criminals 
too walk on their two feet!
"""

import os
import pygame

playerICON = pygame.image.load(os.path.join("assets", "frog.png")) #just test lol 
playerICON = pygame.transform.scale(playerICON, (50,50))

enemyICON = pygame.image.load(os.path.join("assets", "bomb.png")) #just test lol
enemyICON = pygame.transform.scale(enemyICON, (40,40))

class mainCharacter():
        def __init__(self, x, y, width=10, height=10, health=100):
                self.x = x
                self.y = y
                self.width = width
                self.height = height
                self.health = health
                self.max_health = health
                self.color = [255,100,40]
                self.img = playerICON
                self.rect = self.img.get_rect()
                self.mask = pygame.mask.from_surface(self.img)

        def draw(self, screen):
                screen.blit(self.img, (self.x, self.y))

class Enemy():
        def __init__(self, x, y, width=10, height=10, health=100):
                self.x = x
                self.y = y
                self.width = width
                self.height = height
                self.health = health
                self.max_health = health
                self.color = [255,100,40]
                self.img = enemyICON
                self.rect = self.img.get_rect()
                self.mask = pygame.mask.from_surface(self.img)

        def draw(self, screen):
                screen.blit(self.img, (self.x, self.y))