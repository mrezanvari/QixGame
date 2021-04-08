"""
Score board class: This class handles the events of the score board at the right side of the window
"""

import os
from sys import setdlopenflags
import pygame
from enum import Enum
import SoundFx
import main
import Characters
from Colors import *
import Utils

pygame.init()
pygame.font.init()

heartICON = Utils.loadImg(os.path.join("assets", "heart.png"))
heartICON = Utils.scaleImg(heartICON, 40, 40)

class panel:

    def __init__(self, entrySize, backgroundColor):
        self.size = entrySize
        self.color = backgroundColor
        self.score = 0
        self.health = 100
        self.level = 1
        self.precentage = 0
        self.font = pygame.font.SysFont('Comic Sans MS', 12)
        self.memHealth = 0 
        

    def renderAll(self, player):
        offsetX = main.WIDTH + self.size
        main.WIN.fill(WHITE, (main.WIDTH, 0, main.WIDTH + self.size, main.HEIGHT))
        main.WIN.blit(heartICON, (main.WIDTH + 10, 30))
        pygame.draw.rect(main.WIN, RED, (main.WIDTH + 60, 42, 90, 12))
        pygame.draw.rect(main.WIN, SHARPGREEN, (main.WIDTH + 60, 42, 90 * (player.health/player.max_health), 12))
        self.font.set_bold(True)
        text = self.font.render(str(player.health), True, TOMATORED if player.health < 40 else BLACK)
        main.WIN.blit(text, (main.WIDTH + 155, 39))


    def setScore(self, score):
        pass

    def setLevel(self, level):
        pass

    def setHealth(self, health):
        pass



