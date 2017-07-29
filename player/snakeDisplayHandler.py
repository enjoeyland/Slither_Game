#-*- coding: utf-8 -*-

import pygame

from utils.listener import Request
from utils.observer import Observer
from utils.setting import *

class SnakeDisplayHandler:
	def __init__(self, snake):
		self.snake = snake
		self.snake.listen(Request("SnakeAction", self.updateSnakeAttribute))

		self.snake_snakeList = self.snake.getSnakeList()
		self.snake_color = self.snake.getColor()
		self.snake_thick = self.snake.getThick()
		self.snake_length = self.snake.getLength()

		self.snake_snakeImg = self.snake.getSkin()
		self.snake_headImg = self.snake_snakeImg["head"]
		self.snake_bodyImg = self.snake_snakeImg["body"]
		self.snake_tailImg = self.snake_snakeImg["tail"]
		self.snake_firstImg = self.snake_snakeImg["first"]
		self.snake_curveImg = self.snake_snakeImg["curve"]

	def updateSnakeAttribute(self):
		self.snake_snakeList = self.snake.getSnakeList()
		self.snake_color = self.snake.getColor()
		self.snake_thick = self.snake.getThick()
		self.snake_length = self.snake.getLength()


	def update(self):
		self.headClone = pygame.transform.rotate(self.snake_headImg, 90 * self.snake_snakeList[SNAKE_HEAD][DIRECTION])
		self.tailClone = pygame.transform.rotate(self.snake_tailImg, 90 * self.snake_snakeList[SNAKE_TAIL][DIRECTION])
		if self.snake_firstImg != None:
			self.firstClone = pygame.transform.rotate(self.snake_firstImg, 90 * self.snake_snakeList[SNAKE_HEAD][DIRECTION])

	#여기 있으면 않됨
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
		if self.snake_length == 1 and self.snake_firstImg != None:
			surface.blit(self.firstClone, (self.snake_snakeList[SNAKE_HEAD][POS_X],self.snake_snakeList[SNAKE_HEAD][POS_Y]))

		else:
			curveList = []

			if self.snake_bodyImg is None and self.snake_curveImg is None:
				for posX, posY, direction in self.snake_snakeList[1:-1]:
					pygame.draw.rect(surface, self.snake_color, [posX, posY, self.snake_thick, self.snake_thick])

			elif self.snake_bodyImg is None and self.snake_curveImg is not None:
				lastSegment = self.snake_snakeList[SNAKE_TAIL]
				for posX, posY, direction in self.snake_snakeList[1:-1]:
					if lastSegment[DIRECTION] == direction:
						pygame.draw.rect(surface, self.snake_color, [posX, posY, self.snake_thick, self.snake_thick])
					else:
						curveList.append((direction, lastSegment))
					lastSegment = (posX, posY, direction)

			elif self.snake_bodyImg is not None and self.snake_curveImg is None:
				for posX, posY, direction in self.snake_snakeList[1:-1]:
					self.bodyClone = pygame.transform.rotate(self.snake_bodyImg, 90 * direction)
					surface.blit(self.bodyClone, (posX, posY))

			elif self.snake_bodyImg is not None and self.snake_curveImg is not None:
				lastSegment = self.snake_snakeList[SNAKE_TAIL]

				for posX, posY, direction in self.snake_snakeList[1:-1]:
					if lastSegment[DIRECTION] == direction:
						self.bodyClone = pygame.transform.rotate(self.snake_bodyImg, 90 * direction)
						surface.blit(self.bodyClone, (posX, posY))
					else:
						curveList.append((direction, lastSegment))
					lastSegment = (posX, posY, direction)

			surface.blit(self.tailClone, (self.snake_snakeList[SNAKE_TAIL][POS_X],self.snake_snakeList[SNAKE_TAIL][POS_Y]))
			for direction, lastSegment in curveList:
				self.curveClone = pygame.transform.rotate(self.snake_curveImg, 90 * self.getCurveImgDirection(lastSegment[DIRECTION], direction))
				surface.blit(self.curveClone, (lastSegment[POS_X], lastSegment[POS_Y]))
			surface.blit(self.headClone, (self.snake_snakeList[SNAKE_HEAD][POS_X],self.snake_snakeList[SNAKE_HEAD][POS_Y]))
