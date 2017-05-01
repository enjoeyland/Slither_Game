#-*- coding: utf-8 -*-

import pygame

from utils.observer import Observer
from utils.setting import POS_X, SNAKE_HEAD, DIRECTION, LEFT, RIGHT, UP, DOWN, FRAMES_PER_SECOND, POS_Y


class SnakeStateHandler(Observer):
	def __init__(self, snake, onKeyListenerHandler, onTickListenerHandler, IOEventHandler):
		self.snake = snake
		self.snake.attach(self)

		self.snakeList = self.snake.getSnakeList()

		self.length = self.snake.getLength()
		self.thick = self.snake.getThick()
		self.speed = self.snake.getSpeed()


		self.arrowKeyPressed = False
		self.IOEventHandler = IOEventHandler

		self.onKeyListenerHandler = onKeyListenerHandler
		self.onTickListenerHandler = onTickListenerHandler
		self.setListener()

	def observeUpdate(self):
		self.snakeList = self.snake.getSnakeList()
		self.length = self.snake.getLength()
		self.thick = self.snake.getThick()
		self.speed = self.snake.getSpeed()

	def commit(self):
		self.snake.setSnakeList(self.snakeList)

	def tickMove(self):
		direction = self.snakeList[SNAKE_HEAD][DIRECTION]
		if direction == LEFT:
			self.onKeyLeft()
		elif direction == RIGHT:
			self.onKeyRight()
		elif direction == UP:
			self.onKeyUp()
		elif direction == DOWN:
			self.onKeyDown()

	def move(self, newHeadPos, direction):
		self.snakeList.append((newHeadPos[POS_X],newHeadPos[POS_Y],direction))
		if len(self.snakeList) > self.length * self.thick / (self.speed / FRAMES_PER_SECOND):
			del self.snakeList[0]
		self.commit()


	def onKeyLeft(self):
		changeX = -(self.speed / FRAMES_PER_SECOND)
		changeY = 0
		direction = LEFT
		self.move((self.snakeList[SNAKE_HEAD][POS_X] + changeX,
			self.snakeList[SNAKE_HEAD][POS_Y] + changeY), direction)

	def onKeyRight(self):
		changeX = self.speed / FRAMES_PER_SECOND
		changeY = 0
		direction = RIGHT
		self.move((self.snakeList[SNAKE_HEAD][POS_X] + changeX,
			self.snakeList[SNAKE_HEAD][POS_Y] + changeY), direction)

	def onKeyUp(self):
		changeX = 0
		changeY = -(self.speed / FRAMES_PER_SECOND)
		direction = UP
		self.move((self.snakeList[SNAKE_HEAD][POS_X] + changeX,
			self.snakeList[SNAKE_HEAD][POS_Y] + changeY), direction)

	def onKeyDown(self):
		changeX = 0
		changeY = self.speed / FRAMES_PER_SECOND
		direction = DOWN
		self.move((self.snakeList[SNAKE_HEAD][POS_X] + changeX,
			self.snakeList[SNAKE_HEAD][POS_Y] + changeY), direction)

	def onTick(self):
		if not self.isArrowKeyPressed():
			self.tickMove()

	def onArrowKey(self):
		pass

	def isArrowKeyPressed(self):
		arrowKeyPressed = False
		pygameTickEventList = self.IOEventHandler.getPygameTickEvent()
		for pygameEvent in pygameTickEventList:
			if pygameEvent.type == pygame.KEYDOWN:
				if pygameEvent.key == pygame.K_LEFT or pygameEvent.key == pygame.K_RIGHT \
					or pygameEvent.key == pygame.K_UP or pygameEvent.key == pygame.K_DOWN:
					arrowKeyPressed = True
		return arrowKeyPressed


	def setListener(self):
		self.onKeyListenerHandler.listen(pygame.K_LEFT, self.onKeyLeft, group = "arrowKey", groupNotifyFunc = self.onArrowKey)
		self.onKeyListenerHandler.listen(pygame.K_RIGHT, self.onKeyRight, group = "arrowKey", groupNotifyFunc = self.onArrowKey)
		self.onKeyListenerHandler.listen(pygame.K_UP, self.onKeyUp, group = "arrowKey", groupNotifyFunc = self.onArrowKey)
		self.onKeyListenerHandler.listen(pygame.K_DOWN, self.onKeyDown, group = "arrowKey", groupNotifyFunc = self.onArrowKey)
		self.onTickListenerHandler.listen("snakeStateHandler", self.onTick)

	def endListen(self):
		self.onKeyListenerHandler.endListen(group = "arrowKey")
		self.onTickListenerHandler.endListen(listenerName = "snakeStateHandler")