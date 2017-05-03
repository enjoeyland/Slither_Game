#-*- coding: utf-8 -*-

import pygame

from utils.observer import Observer
from utils.setting import *

class SnakeDisplayHandler(Observer):
	def __init__(self, snake):
		self.snake = snake
		self.snake.attach(self)
		self.snakeState = self.snake.getState()
		self.color = self.snakeState["color"]
		self.thick = self.snakeState["thick"]
		self.snakeList = self.snake.getSnakeList()
		self.length = self.snakeState["length"]

		self.snakeImg = self.snake.getSkin()
		self.headImg = self.snakeImg["head"]
		self.bodyImg = self.snakeImg["body"]
		self.tailImg = self.snakeImg["tail"]
		self.firstImg = self.snakeImg["first"]
		self.curveImg = self.snakeImg["curve"]

	def observeUpdate(self):
		self.snakeState = self.snake.getState()
		self.color = self.snakeState["color"]
		self.thick = self.snakeState["thick"]
		self.snakeList = self.snake.getSnakeList()
		self.length = self.snakeState["length"]


	def update(self):
		self.headClone = pygame.transform.rotate(self.headImg, 90 * self.snakeList[SNAKE_HEAD][DIRECTION])
		self.tailClone = pygame.transform.rotate(self.tailImg, 90 * self.snakeList[SNAKE_TAIL][DIRECTION])
		if self.firstImg != None:
			self.firstClone = pygame.transform.rotate(self.firstImg, 90 * self.snakeList[SNAKE_HEAD][DIRECTION])

	def getCurveImgDirection(self, lastDirection, currentDirection):
		if lastDirection is UP and currentDirection is LEFT \
			or lastDirection is RIGHT and currentDirection is DOWN:
			return 3

		elif lastDirection is RIGHT and currentDirection is UP \
			or lastDirection is DOWN and currentDirection is LEFT:
			return 2

		elif lastDirection is LEFT and currentDirection is UP \
			or lastDirection is DOWN and currentDirection is RIGHT:
			return 1

		elif lastDirection is LEFT and currentDirection is DOWN \
			or lastDirection is UP and currentDirection is RIGHT:
			return 4

		else:
			return 0


	def draw(self, surface):
		if self.length == 1 and self.firstImg != None:
			surface.blit(self.firstClone, (self.snakeList[SNAKE_HEAD][POS_X],self.snakeList[SNAKE_HEAD][POS_Y]))

		else:
			curveList = []

			if self.bodyImg is None and self.curveImg is None:
				for posX, posY, direction in self.snakeList[1:-1]:
					pygame.draw.rect(surface, self.color, [posX, posY, self.thick, self.thick])

			elif self.bodyImg is None and self.curveImg is not None:
				lastSegment = self.snakeList[SNAKE_TAIL]
				for posX, posY, direction in self.snakeList[1:-1]:
					if lastSegment[DIRECTION] == direction:
						pygame.draw.rect(surface, self.color, [posX, posY, self.thick, self.thick])
					else:
						curveList.append((direction, lastSegment))
					lastSegment = (posX, posY, direction)

			elif self.bodyImg is not None and self.curveImg is None:
				for posX, posY, direction in self.snakeList[1:-1]:
					self.bodyClone = pygame.transform.rotate(self.bodyImg, 90 * direction)
					surface.blit(self.bodyClone, (posX, posY))

			elif self.bodyImg is not None and self.curveImg is not None:
				lastSegment = self.snakeList[SNAKE_TAIL]

				for posX, posY, direction in self.snakeList[1:-1]:
					if lastSegment[DIRECTION] == direction:
						self.bodyClone = pygame.transform.rotate(self.bodyImg, 90 * direction)
						surface.blit(self.bodyClone, (posX, posY))
					else:
						curveList.append((direction, lastSegment))
					lastSegment = (posX, posY, direction)

			surface.blit(self.tailClone, (self.snakeList[SNAKE_TAIL][POS_X],self.snakeList[SNAKE_TAIL][POS_Y]))
			for direction, lastSegment in curveList:
				self.curveClone = pygame.transform.rotate(self.curveImg, 90 * self.getCurveImgDirection(lastSegment[DIRECTION], direction))
				surface.blit(self.curveClone, (lastSegment[POS_X], lastSegment[POS_Y]))
			surface.blit(self.headClone, (self.snakeList[SNAKE_HEAD][POS_X],self.snakeList[SNAKE_HEAD][POS_Y]))
