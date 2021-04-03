import sys, os
import pygame.mixer as mixer 

mixer.init()
gameOverSound = mixer.Sound(os.path.join("assets", 'uDead.wav'))