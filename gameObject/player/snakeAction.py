#-*- coding: utf-8 -*-

import pygame

from utils.listener import Request
from utils.observer import Observer
from utils.setting import POS_X, SNAKE_HEAD, DIRECTION, LEFT, RIGHT, UP, DOWN, FRAMES_PER_SECOND, POS_Y


class SnakeAction:
	def __init__(self, snake, KeyboardEventHandler):
		self.snake = snake
		self.KeyboardEventHandler = KeyboardEventHandler
		self.setListener()

		self.snake_snakeList = self.snake.getSnakeList()
		self.snake_length = self.snake.getLength()
		self.snake_thick = self.snake.getThick()
		self.snake_speed = self.snake.getSpeed()


	# listening func
	def updateSnakeAttribute(self):
		self.snake_snakeList = self.snake.getSnakeList()
		self.snake_length = self.snake.getLength()
		self.snake_thick = self.snake.getThick()
		self.snake_speed = self.snake.getSpeed()


	def commit(self):
		self.snake.setSnakeList(self.snake_snakeList)

	# snake move func
	def tickMove(self):
		direction = self.snake_snakeList[SNAKE_HEAD][DIRECTION]
		if direction == LEFT:
			self.moveLeft()
		elif direction == RIGHT:
			self.moveRight()
		elif direction == UP:
			self.moveUp()
		elif direction == DOWN:
			self.moveDown()

	def _move(self, newHeadPos, direction):
		self.snake_snakeList.append([newHeadPos[POS_X],newHeadPos[POS_Y],direction])
		if len(self.snake_snakeList) > self.snake_length * self.snake_thick / (self.snake_speed / FRAMES_PER_SECOND):
			del self.snake_snakeList[0]
		self.commit()


	def moveLeft(self):
		changeX = -(self.snake_speed / FRAMES_PER_SECOND)
		changeY = 0
		direction = LEFT
		self._move((self.snake_snakeList[SNAKE_HEAD][POS_X] + changeX,
			self.snake_snakeList[SNAKE_HEAD][POS_Y] + changeY), direction)

	def moveRight(self):
		changeX = self.snake_speed / FRAMES_PER_SECOND
		changeY = 0
		direction = RIGHT
		self._move((self.snake_snakeList[SNAKE_HEAD][POS_X] + changeX,
			self.snake_snakeList[SNAKE_HEAD][POS_Y] + changeY), direction)

	def moveUp(self):
		changeX = 0
		changeY = -(self.snake_speed / FRAMES_PER_SECOND)
		direction = UP
		self._move((self.snake_snakeList[SNAKE_HEAD][POS_X] + changeX,
			self.snake_snakeList[SNAKE_HEAD][POS_Y] + changeY), direction)

	def moveDown(self):
		changeX = 0
		changeY = self.snake_speed / FRAMES_PER_SECOND
		direction = DOWN
		self._move((self.snake_snakeList[SNAKE_HEAD][POS_X] + changeX,
			self.snake_snakeList[SNAKE_HEAD][POS_Y] + changeY), direction)

	# event notify func
	def onKeyLeft(self):
		self.snake_snakeList[SNAKE_HEAD][DIRECTION] = LEFT
		# print("[SnakeAction] : Left")
		self.commit()
	def onKeyRight(self):
		self.snake_snakeList[SNAKE_HEAD][DIRECTION] = RIGHT
		# print("[SnakeAction] : Right")
		self.commit()
	def onKeyUp(self):
		self.snake_snakeList[SNAKE_HEAD][DIRECTION] = UP
		# print("[SnakeAction] : Up")
		self.commit()
	def onKeyDown(self):
		self.snake_snakeList[SNAKE_HEAD][DIRECTION] = DOWN
		# print("[SnakeAction] : Down")
		self.commit()

	# listen to publisher
	def setListener(self):
		self.snake.listen(Request("SnakeAction", self.updateSnakeAttribute))

		self.KeyboardEventHandler.listen(Request("snakeStateHandler-K_LEFT", self.onKeyLeft, addtionalTarget= pygame.K_LEFT, groupName = "arrowKey"))
		self.KeyboardEventHandler.listen(Request("snakeStateHandler-K_RIGHT", self.onKeyRight, addtionalTarget= pygame.K_RIGHT, groupName = "arrowKey"))
		self.KeyboardEventHandler.listen(Request("snakeStateHandler-K_UP", self.onKeyUp, addtionalTarget= pygame.K_UP, groupName = "arrowKey"))
		self.KeyboardEventHandler.listen(Request("snakeStateHandler-K_DOWN", self.onKeyDown, addtionalTarget= pygame.K_DOWN, groupName = "arrowKey"))

	def endListen(self):
		self.KeyboardEventHandler.endGroupListen("arrowKey")
