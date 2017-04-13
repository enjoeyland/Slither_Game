import pygame
from observer import Observer
from setting import *

class SnakeStateHandler(Observer):
	def __init__(self, snake, keyboardEventHandler):
		self.snake = snake
		self.snake.attach(self)
		self.snakeList = self.snake.getSnakeList()
		self.length = self.snake.getLength()
		self.thick = self.snake.getThick()
		self.setListener(keyboardEventHandler)

	def observeUpdate(self):
		self.snakeList = self.snake.getSnakeList()
		self.length = self.snake.getLength()
		self.thick = self.snake.getThick()

	def commit(self):
		self.snake.setSnakeList(self.snakeList)

	def move(self, newHeadPos, direction):
		self.snakeList.append((newHeadPos[POS_X],newHeadPos[POS_Y],direction))
		if len(self.snakeList) > self.length:
			del self.snakeList[0]
		self.commit()



	def eventOnKeyLeft(self):
		lead_x_change = - self.thick
		lead_y_change = 0
		direction = LEFT
		self.move((self.snakeList[SNAKE_TAIL][POS_X] + lead_x_change,
			self.snakeList[SNAKE_TAIL][POS_Y] + lead_y_change), direction)

	def eventOnKeyRight(self):
		lead_x_change = self.thick
		lead_y_change = 0
		direction = RIGHT
		self.move((self.snakeList[SNAKE_TAIL][POS_X] + lead_x_change,
			self.snakeList[SNAKE_TAIL][POS_Y] + lead_y_change), direction)

	def eventOnKeyUp(self):
		lead_x_change = 0
		lead_y_change = - self.thick
		direction = UP
		self.move((self.snakeList[SNAKE_TAIL][POS_X] + lead_x_change,
			self.snakeList[SNAKE_TAIL][POS_Y] + lead_y_change), direction)

	def eventOnKeyDown(self):
		lead_x_change = 0
		lead_y_change = self.thick
		direction = DOWN
		self.move((self.snakeList[SNAKE_TAIL][POS_X] + lead_x_change,
			self.snakeList[SNAKE_TAIL][POS_Y] + lead_y_change), direction)

	def setListener(self, keyboardEventHandler):
		keyboardEventHandler.onKey(pygame.K_LEFT, self.eventOnKeyLeft)
		keyboardEventHandler.onKey(pygame.K_RIGHT, self.eventOnKeyRight)
		keyboardEventHandler.onKey(pygame.K_UP, self.eventOnKeyUp)
		keyboardEventHandler.onKey(pygame.K_DOWN, self.eventOnKeyDown)
		keyboardEventHandler.listen()