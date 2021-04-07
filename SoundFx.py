import sys, os
import pygame.mixer as mixer 

mixer.init()
gameOverSound = mixer.Sound(os.path.join("assets", 'GameOver.wav'))
titleMenu = mixer.Sound(os.path.join("assets", 'titleMusic.wav'))
mixer.music.load(os.path.join("assets", 'inGameMusic.wav'))

def inGameInit():
    mixer.music.play(-1)

def inGamePause():
    mixer.music.pause()

def inGameUnPause():
    mixer.music.unpause()

def inGameStop():
    mixer.music.stop()

