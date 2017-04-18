#-*- coding: utf-8 -*-

import pygame
from observer import Observer
from setting import *

class SnakeStateHandler(Observer, object):
	def __init__(self, snake, onKeyListenerHandler, onTickListenerHandler, IOEventHandler):
		self.snake = snake
		self.snake.attach(self)
		self.snakeList = self.snake.getSnakeList()
		self.length = self.snake.getLength()
		self.thick = self.snake.getThick()

		self.arrowKeyPressed = False
		self.IOEventHandler = IOEventHandler
		self.setListener(onKeyListenerHandler, onTickListenerHandler)

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

	def smallMove(self):
		pass # 속도 * (나중 - 처음) / thick
		#if 처음 == 원래 나중:
		#
		#thickMove()

	def onKeyLeft(self):
		lead_x_change = - self.thick
		lead_y_change = 0
		direction = LEFT
		self.move((self.snakeList[SNAKE_HEAD][POS_X] + lead_x_change,
			self.snakeList[SNAKE_HEAD][POS_Y] + lead_y_change), direction)

	def onKeyRight(self):
		lead_x_change = self.thick
		lead_y_change = 0
		direction = RIGHT
		self.move((self.snakeList[SNAKE_HEAD][POS_X] + lead_x_change,
			self.snakeList[SNAKE_HEAD][POS_Y] + lead_y_change), direction)

	def onKeyUp(self):
		lead_x_change = 0
		lead_y_change = - self.thick
		direction = UP
		self.move((self.snakeList[SNAKE_HEAD][POS_X] + lead_x_change,
			self.snakeList[SNAKE_HEAD][POS_Y] + lead_y_change), direction)

	def onKeyDown(self):
		lead_x_change = 0
		lead_y_change = self.thick
		direction = DOWN
		self.move((self.snakeList[SNAKE_HEAD][POS_X] + lead_x_change,
			self.snakeList[SNAKE_HEAD][POS_Y] + lead_y_change), direction)

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
				if pygameEvent.key==pygame.K_LEFT or pygameEvent.key==pygame.K_RIGHT \
					or pygameEvent.key ==pygame.K_UP or pygameEvent.key==pygame.K_DOWN:
					arrowKeyPressed = True
		return arrowKeyPressed


	def setListener(self, onKeyListenerHandler, onTickListenerHandler):
		onKeyListenerHandler.listen(pygame.K_LEFT, self.onKeyLeft, group = "arrowKey", groupNotifyFunc = self.onArrowKey)
		onKeyListenerHandler.listen(pygame.K_RIGHT, self.onKeyRight, group = "arrowKey", groupNotifyFunc = self.onArrowKey)
		onKeyListenerHandler.listen(pygame.K_UP, self.onKeyUp, group = "arrowKey", groupNotifyFunc = self.onArrowKey)
		onKeyListenerHandler.listen(pygame.K_DOWN, self.onKeyDown, group = "arrowKey", groupNotifyFunc = self.onArrowKey)
		onTickListenerHandler.listen("snakeStateHandler", self.onTick)