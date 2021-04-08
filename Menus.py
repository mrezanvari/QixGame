"""
Menu class: This class will provide functions and classes to deal with menu and handle user input.

This class is portable and costomizable so any addition to the menu options should work with little to no issues...
"""

import os
import pygame
from enum import Enum
import SoundFx

pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255,99,71) # not like red red, more like tomato red!

class menuType(Enum): # menu types; will be selected from main.py
    mainMenu = 0
    pauseMenu = 1

class Menu():

    def renderMenu(type):

        winW, winH = pygame.display.get_surface().get_size()
        window = pygame.display.get_surface()
        backgroundImg = BLACK # could be an image for now it's a black screen; not used for now
        hovericon = pygame.transform.scale(pygame.image.load(os.path.join("assets", "frog.png")) , (50,50)) # It is also possible to have dynamic hoverIcons... but for now...
        font = pygame.font.SysFont('Comic Sans MS', 40)
        offsetX = 20 # this is based on the size of the font 
        offsetY = 10 
        optionText = 'New Game' if type == menuType.mainMenu else 'Resume'
        options = {optionText : ( round(winW/2) - (round(len(optionText)/2) * offsetX), round(winH/7) * 3 ), 'Quit' : (round(winW/2) - (round(len('Quit')/2) * offsetX), round(winH/7) * 4)}

        run = True
        selectedIndex = 0
        window.fill(BLACK) 
        text = None  
        SoundFx.titleMenu.play()

        while run:

            pygame.time.Clock().tick(60)
            window.fill(BLACK)
            for index, option in enumerate(options): # draw texts and highlight the selected one
                text = font.render(option, False, RED if selectedIndex == index else WHITE)
                window.blit(text, options[option])
                if selectedIndex == index:
                    window.blit(hovericon, (options[option][0] - (offsetY * 5), options[option][1]))       

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP] or keys[pygame.K_w]:
                if (selectedIndex > 0 ):
                    selectedIndex -= 1 # reversed cuz index! so if 1 it should be the top one right? but the index of that will be zero

            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                if (selectedIndex < len(options) - 1 ):
                    selectedIndex += 1

            if keys[pygame.K_RETURN]:
                if selectedIndex == 0:
                    run = False # jump to main
                    SoundFx.titleMenu.stop()

                elif selectedIndex == 1: # exit the game
                    pygame.quit()

            pygame.display.update() 
            
            
        
