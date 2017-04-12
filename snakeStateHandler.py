import pygame
from observer import Observer
from setting import *

class SnakeStateHandler(Observer):
	def __init__(self, snake, keyboardEventHandler):
		self.snake = snake
		self.snake.attach(self)
		self.snakeList = self.snake.getSnakeList()
		self.length = self.snake.getLength()
		self.setListener(keyboardEventHandler)

	def observeUpdate(self):
		self.snakeList = self.snake.getSnakeList()
		self.length = self.snake.getLength()

	def commit(self):
		self.snake.setSnakeList(self.snakeList)

	def move(self, newHeadPos, direction):
		self.snakeList.append((newHeadPos[POS_X],newHeadPos[POS_Y],direction))
		if len(self.snakeList) > self.length:
			del self.snakeList[0]
		self.commit()



	def eventOnKeyLeft(self):
		pass

	def eventOnKeyRight(self):
		pass

	def eventOnKeyUp(self):
		pass

	def eventOnKeyDown(self):
		pass

	def setListener(self, keyboardEventHandler):
		keyboardEventHandler.onKey(pygame.K_LEFT, self.eventOnKeyLeft)
		keyboardEventHandler.onKey(pygame.K_RIGHT, self.eventOnKeyRight)
		keyboardEventHandler.onKey(pygame.K_UP, self.eventOnKeyUp)
		keyboardEventHandler.onKey(pygame.K_DOWN, self.eventOnKeyDown)
		keyboardEventHandler.listen()