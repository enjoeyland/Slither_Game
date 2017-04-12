import pygame
import game

from setting import *
from utility import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))#surface화면
# screen = pygame.display.set_mode((640,480),SWSURFACE|FULLSCREEN)
pygame.display.set_caption("Slither")
pygame.display.set_icon(loadImage("apple"))

whichGame = game.Game.display_intro()
if whichGame == PLAYER1_HIGH_SCORE:
	game.Game.player1_highScore_gameLoop()

