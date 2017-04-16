import pygame
import game
import event
import utility
import threading
from setting import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))#surface화면
# screen = pygame.display.set_mode((640,480),SWSURFACE|FULLSCREEN)
pygame.display.set_caption("Slither")
pygame.display.set_icon(utility.loadImage("apple"))

# event.IOEventHandler().start()
print("check -3")
eventThread = threading.Thread(target = event.eventHandler)
print("check -2")
eventThread.daemon = True
eventThread.start()
print("check -1")

import time
# while True:
	# time.sleep(1)

gameObject = game.Game(screen)
whichGame = gameObject.display_intro()
if whichGame == PLAYER1_HIGH_SCORE:
	print("check 0")
	gameObject.player1_highScore_gameLoop()

