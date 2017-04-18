import pygame

import listener
import snake
import snakeDisplayHandler
import snakeStateHandler
import event
import skin
from setting import *

class Game(object):
	def __init__(self, screen):
		self.screen = screen

	def setGameRunningToFalse(self):
		self.gameIsRunning = False
	# def setGameOverTrue(self):
	# 	self.gameOver = True
	def display_intro(self):
		return 0
	def player1_highScore_gameLoop(self):
		defaultSpeed = 30
		defaultThick = 20

		self.gameIsRunning = True
		
		# setting
		myOnKeyListenerHandler = listener.OnKeyListenerHandler()
		myOnTickListenerHandler = listener.OnTickListenerHandler()

		myKeyboardEventHandler = event.KeyboardEventHandler(myOnKeyListenerHandler)
		myIOEventHandler = event.IOEventHandler(myKeyboardEventHandler, myOnTickListenerHandler)
		mysnakeEventHandler = event.SnakeEventHandler()
		myEvent = event.Event(myOnTickListenerHandler)

		player = snake.Snake(1, defaultSpeed, defaultThick, skin.Skin())
		mySnakeStateHandler = snakeStateHandler.SnakeStateHandler(player, myOnKeyListenerHandler, myOnTickListenerHandler, myIOEventHandler)
		mySnakeDisplayHandler = snakeDisplayHandler.SnakeDisplayHandler(player)

		while self.gameIsRunning:
			myEvent.onTick()

			self.screen.fill((100,200,255))
			mysnakeEventHandler.crashWall(player, self.setGameRunningToFalse)
			snakeDisplayHandler.SnakeDisplayHandler(player).update()
			snakeDisplayHandler.SnakeDisplayHandler(player).draw(self.screen)

			pygame.display.update()
			pygame.time.Clock().tick(FRAMES_PER_SECOND)

	def player2_highScore_gameLoop(self):
		pass
	def player2_compete_gameLoop(self):
		pass