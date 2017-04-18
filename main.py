#-*- coding: utf-8 -*-

import pygame
import game
import event
import utility
import threading
from setting import *
try:
	import pygame.fastevent as eventModule
except ImportError:
	import pygame.event as eventModule


pygame.init()
if hasattr(eventModule, 'init'):
	eventModule.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# screen = pygame.display.set_mode((640,480),SWSURFACE|FULLSCREEN)
pygame.display.set_caption("Slither")
pygame.display.set_icon(utility.loadImage("apple"))

gameObject = game.Game(screen)

whichGame = gameObject.display_intro()
if whichGame == PLAYER1_HIGH_SCORE:
	gameObject.player1_highScore_gameLoop()

