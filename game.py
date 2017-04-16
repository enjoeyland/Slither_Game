import pygame
import snake
import snakeDisplayHandler
import snakeStateHandler
import event
import skin
from setting import *

class Game():
	def __init__(self, screen):
		self.screen = screen

	def setGameRunningToFalse(self):
		self.gameIsRunning = False
	def display_intro(self):
		return 0
	def player1_highScore_gameLoop(self):
		defaultSpeed = 30
		defaultThick = 20

		self.gameIsRunning = True
		player = snake.Snake(1, defaultSpeed, defaultThick, skin.Skin())
		snakeStateHandler.SnakeStateHandler(player, event.KeyboardEventHandler())
		snakeDisplayHandler.SnakeDisplayHandler(player)
		while self.gameIsRunning:

			self.screen.fill((100,200,255))
			event.snakeEventHandler().crashWall(player, self.setGameRunningToFalse)
			snakeDisplayHandler.SnakeDisplayHandler(player).update()
			snakeDisplayHandler.SnakeDisplayHandler(player).draw(self.screen)

			pygame.display.update()
			pygame.time.Clock().tick(FRAMES_PER_SECOND)
	def player2_highScore_gameLoop(self):
		pass
	def player2_compete_gameLoop(self):
		pass