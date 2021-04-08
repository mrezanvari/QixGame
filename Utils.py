"""
Utilities Class: This class contains important functions and prevents code cluster...
"""

import os
import pygame

def checkCollision(rect1, rect2): # collision function for enemy-player only
    offsetX = rect2.x - rect1.x
    offsetY = rect2.y - rect1.y
    return rect1.mask.overlap(rect2.mask, (offsetX, offsetY)) != None

def checkCollision_Line(rect1, rect2): # collision function for enemy-player only
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

def loadImg(pathToFile):
    return pygame.image.load(pathToFile)

def scaleImg(inputImg, scaleW, scaleH):
    return pygame.transform.scale(inputImg, (scaleW,scaleH))

