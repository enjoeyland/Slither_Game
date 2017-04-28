#-*- coding: utf-8 -*-

import pygame

from utils.observer import Observer
from utils.setting import *


class SnakeDisplayHandler(Observer, object):
	def __init__(self, snake):
		self.snake = snake
		self.snake.attach(self)
		self.snakeState = self.snake.getState()
		self.color = self.snakeState["color"]
		self.thick = self.snakeState["thick"]
		self.snakeList = self.snakeState["snakeList"]
		self.length = self.snakeState["length"]

		self.snakeImg = self.snake.getSkin()
		self.headImg = self.snakeImg["head"]
		self.bodyImg = self.snakeImg["body"]
		self.tailImg = self.snakeImg["tail"]
		self.firstImg = self.snakeImg["first"]

	def observeUpdate(self):
		self.snakeState = self.snake.getState()
		self.color = self.snakeState["color"]
		self.thick = self.snakeState["thick"]
		self.snakeList = self.snakeState["snakeList"]
		self.length = self.snakeState["length"]

		# if SNAKE_AUTO_DRAW:
		# 	self.update()
		# 	# self.draw()

	def update(self):
		self.headClone = pygame.transform.rotate(self.headImg, 90 * self.snakeList[SNAKE_HEAD][DIRECTION])
		self.tailClone = pygame.transform.rotate(self.tailImg, 90 * self.snakeList[SNAKE_TAIL][DIRECTION])
		if self.firstImg != None:
			self.firstClone = pygame.transform.rotate(self.firstImg, 90 * self.snakeList[SNAKE_HEAD][DIRECTION])

	def draw(self, surface):
		if self.length == 1 and self.firstImg != None:
			surface.blit(self.firstClone, (self.snakeList[SNAKE_HEAD][POS_X],self.snakeList[SNAKE_HEAD][POS_Y]))

		else:
			surface.blit(self.headClone, (self.snakeList[SNAKE_HEAD][POS_X],self.snakeList[SNAKE_HEAD][POS_Y]))
			surface.blit(self.tailClone, (self.snakeList[SNAKE_TAIL][POS_X],self.snakeList[SNAKE_TAIL][POS_Y]))

			if self.bodyImg == None:
				for posX, posY, direction in self.snakeList[1:-1]:
					pygame.draw.rect(surface, self.color, [posX, posY, self.thick, self.thick])
			else:
				for posX, posY, direction in self.snakeList[1:-1]:
					self.bodyClone = pygame.transform.rotate(self.bodyImg, 90 * direction)
					surface.blit(self.bodyClone, (posX, posY))
