import pygame
from observer import Observer
from setting import *

class SnakeDisplayHandler(Observer):
	def __init__(self, snake):
		self.snake = snake
		self.snake.attach(self)
		self.snakeState = self.snake.getState()
		self.color = self.snakeState["color"]
		self.thick = self.snakeState["thick"]
		self.snakeList = self.snakeState["snakeList"]

		self.snakeImg = self.snake.getSkin()
		self.headImg = self.snakeImg["head"]
		self.bodyImg = self.snakeImg["body"]
		self.tailImg = self.snakeImg["tail"]

	def observeUpdate(self):
		self.snakeState = self.snake.getState()
		self.color = self.snakeState["color"]
		self.thick = self.snakeState["thick"]
		self.snakeList = self.snakeState["snakeList"]
		# if SNAKE_AUTO_DRAW:
		# 	self.update()
		# 	# self.draw()

	def update(self):
		self.headClone = pygame.transform.rotate(self.headImg, 90 * self.snakeList[SNAKE_HEAD][DIRECTION])
		self.tailClone = pygame.transform.rotate(self.tailImg, 90 * self.snakeList[SNAKE_TAIL][DIRECTION])

	def draw(self, screen):
		screen.blit(self.headClone, (self.snakeList[SNAKE_HEAD][POS_X],self.snakeList[SNAKE_HEAD][POS_Y]))
		screen.blit(self.tailClone, (self.snakeList[SNAKE_TAIL][POS_X],self.snakeList[SNAKE_TAIL][POS_Y]))

		if self.bodyImg == None: 
			for posX, posY, direction in self.snakeList[1:-1]:
				pygame.draw.rect(screen, self.color, [posX, posY, self.thick, self.thick])
		else:
			for posX, posY, direction in self.snakeList[1:-1]:
				self.bodyClone = pygame.transform.rotate(self.bodyImg, 90 * direction)
				screen.blit(self.bodyClone, (posX, posY))