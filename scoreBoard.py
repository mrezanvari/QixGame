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
import glob

pygame.init()
pygame.font.init()

heartICON = Utils.loadImg(os.path.join("assets", "heart.png"))
heartICON = Utils.scaleImg(heartICON, 40, 40)

f1 = 0 # frame number for smart guy meme
f2 = 0 # frame number for vibe cat meme
flipFlop = False # flip-flop variable for changing the memes
meme1 = []
meme2 = []
fileList = []

for file in glob.glob(os.path.join("assets", "man") + "/*.gif"):
    fileList.append(file)

for file in sorted(fileList):
    meme1.append(Utils.scaleImg(Utils.loadImg(file), 180, 100))


for file in glob.glob(os.path.join("assets", "cat") + "/*.gif"):
    fileList.append(file)

for file in sorted(fileList):
    meme2.append(Utils.scaleImg(Utils.loadImg(file), 180, 100))

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
        self.currFrame = 0
        

    def renderAll(self, player):
        global flipFlop, f1,f2
        offsetX = main.WIDTH + self.size
        main.WIN.fill(WHITE, (main.WIDTH, 0, main.WIDTH + self.size, main.HEIGHT))
        main.WIN.blit(heartICON, (main.WIDTH + 10, 30))
        pygame.draw.rect(main.WIN, RED, (main.WIDTH + 60, 42, 90, 12))
        pygame.draw.rect(main.WIN, SHARPGREEN, (main.WIDTH + 60, 42, 90 * (player.health/player.max_health), 12))
        self.font.set_bold(True)
        text = self.font.render(str(player.health), True, TOMATORED if player.health < 40 else BLACK)
        main.WIN.blit(text, (main.WIDTH + 155, 39))
        if self.currFrame % 5 == 0 and flipFlop == False:
            f1 += 1
            if f1 > len(meme1) - 1: f1 = 0

        elif self.currFrame % 4 == 0 and flipFlop == True:
            f2 += 1
            if f2 > len(meme2) - 1: f2 = 0

        self.currFrame += 1
        main.WIN.blit(meme1[f1], (main.WIDTH + 10, 200)) if flipFlop == False else main.WIN.blit(meme2[f2], (main.WIDTH + 10, 200)) 
        if self.currFrame % 300 == 0 : flipFlop = not flipFlop

    def setScore(self, score):
        pass

    def setLevel(self, level):
        pass

    def setHealth(self, health):
        pass



