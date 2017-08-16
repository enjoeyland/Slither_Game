import os

import sys

from event.eventCreators.eventCreator import EventCreator
from utils.listener import Request
from utils.setting import SNAKE_HEAD, POS_X, SCREEN_WIDTH, SCREEN_HEIGHT, POS_Y, CRASH_WALL, CRASH_ITEM, CRASH_ITSELF, \
	FRAMES_PER_SECOND, SPRITE_OFFSET, END, BEGIN, CRASH_OTHER_SNAKE, PLAYER2_COMPETE


class SnakeEventCreator(EventCreator):
	def __init__(self, snake, itemGroup, gameState):
		self.snake = snake
		self.snake.listen(Request("SnakeEventCreator",self.checkingProcess))

		self.gameState = gameState

		self.snake_thick = self.snake.getThick()
		self.snake_speed = self.snake.getSpeed()
		self.snake_snakeList = self.snake.getSnakeList()
		self.snake_snakeHead = self.snake_snakeList[SNAKE_HEAD]

		self.itemGroup = itemGroup

	def setOtherSnake(self, allSnakes):
		self.otherSnakes = allSnakes
		self.otherSnakes.remove(self.snake)


	def checkingProcess(self):
		self.updateSnakeAttribute()
		self.crashWall()
		self.crashItem()
		self.crashItself()
		self.crashOtherSnake()

	def updateSnakeAttribute(self):
		self.snake_thick = self.snake.getThick()
		self.snake_speed = self.snake.getSpeed()
		self.snake_snakeList = self.snake.getSnakeList()
		self.snake_snakeHead = self.snake_snakeList[SNAKE_HEAD]


	def crashWall(self):
		if  self.snake_snakeHead[POS_X] > SPRITE_OFFSET[POS_X][END] - self.snake_thick[POS_X] or self.snake_snakeHead[POS_X] < SPRITE_OFFSET[POS_X][BEGIN] \
				or self.snake_snakeHead[POS_Y] > SPRITE_OFFSET[POS_Y][END] - self.snake_thick[POS_Y] or self.snake_snakeHead[POS_Y] < SPRITE_OFFSET[POS_Y][BEGIN]:
			if os.path.split(os.path.abspath(sys.argv[0]))[1] != "training.py":
				print("crash wall")
			self.createEvent(CRASH_WALL, snake = self.snake)


	def crashItem(self):
		for item in self.itemGroup.sprites():
			itemSize = item.getSize()
			itemLocation = item.getLocation()
			if self.snake_snakeHead[POS_X] >= itemLocation[POS_X] and self.snake_snakeHead[POS_X] <= itemLocation[POS_X] + itemSize[POS_X] \
					or self.snake_snakeHead[POS_X] + self.snake_thick[POS_X] >= itemLocation[POS_X] and self.snake_snakeHead[POS_X] + self.snake_thick[POS_X] <= itemLocation[POS_X] + itemSize[POS_X]:
				if self.snake_snakeHead[POS_Y] >= itemLocation[POS_Y] and self.snake_snakeHead[POS_Y] <= itemLocation[POS_Y] + itemSize[POS_Y] \
						or self.snake_snakeHead[POS_Y] + self.snake_thick[POS_Y] >= itemLocation[POS_Y] and self.snake_snakeHead[POS_Y] + self.snake_thick[POS_Y] <= itemLocation[POS_Y] + itemSize[POS_Y]:
					self.createEvent(CRASH_ITEM, snake = self.snake, item = item)


	def crashItself(self):
		for eachSegment in self.snake_snakeList[ : - int(3 * self.snake_thick[POS_X] / (self.snake_speed / FRAMES_PER_SECOND))]:
			if eachSegment[POS_X] <= self.snake_snakeHead[POS_X] and  eachSegment[POS_X] + self.snake_thick[POS_X] > self.snake_snakeHead[POS_X]\
					and eachSegment[POS_Y] <= self.snake_snakeHead[POS_Y] and eachSegment[POS_Y] + self.snake_thick[POS_Y] > self.snake_snakeHead[POS_Y]:
				if os.path.split(os.path.abspath(sys.argv[0]))[1] == "training.py" or self.gameState == PLAYER2_COMPETE:
					pass
				else:
					print("crash itself")
				self.createEvent(CRASH_ITSELF, snake = self.snake)
				break


	def crashOtherSnake(self):
		for otherSnake in self.otherSnakes:
			for eachSegment in otherSnake.snakeList:
				if self.snake_snakeHead[POS_X] >= eachSegment[POS_X] and self.snake_snakeHead[POS_X] <= eachSegment[POS_X] + otherSnake.thick[POS_X] \
					or self.snake_snakeHead[POS_X] + self.snake_thick[POS_X] >= eachSegment[POS_X] and self.snake_snakeHead[POS_X] + self.snake_thick[POS_X] <= eachSegment[POS_X] + otherSnake.thick[POS_X]:
					if self.snake_snakeHead[POS_Y] >= eachSegment[POS_Y] and self.snake_snakeHead[POS_Y] <= eachSegment[POS_Y] + otherSnake.thick[POS_Y] \
							or self.snake_snakeHead[POS_Y] + self.snake_thick[POS_Y] >= eachSegment[POS_Y] and self.snake_snakeHead[POS_Y] + self.snake_thick[POS_Y] <= eachSegment[POS_Y] + otherSnake.thick[POS_Y]:
						if os.path.split(os.path.abspath(sys.argv[0]))[1] != "training.py":
							print("crash other snake")
						self.createEvent(CRASH_OTHER_SNAKE, snake = self.snake, otherSnake = otherSnake)
						break