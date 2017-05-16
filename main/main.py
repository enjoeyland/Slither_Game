#-*- coding: utf-8 -*-
import pygame

from Main import game
from utils import utility
from utils.setting import SCREEN_WIDTH, SCREEN_HEIGHT, FULL_SCREEN, PLAYER1_HIGH_SCORE

# pygame init
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
pygame.mixer.init()


if FULL_SCREEN:
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
else:
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# screen = pygame.display.set_mode((640,480),SWSURFACE|FULLSCREEN)
pygame.display.set_caption("Slither")
pygame.display.set_icon(utility.loadImage("apple"))

gameObject = game.Game(screen)


whichGame = gameObject.display_intro()
if whichGame == PLAYER1_HIGH_SCORE:
	while gameObject.player1_highScore_gameLoop():
		pass

