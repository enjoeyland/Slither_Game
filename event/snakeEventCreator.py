import threading

from event.event import EventCreator
from utils.setting import *


class SnakeEventCreator(EventCreator):
	def __init__(self):
		self.wallListenerBuffer = {}
		self.wallListenDic = {}

	def crashWall(self, snake, func):
		thick = snake.getThick()
		snakeList = snake.getSnakeList()
		snakeHead = snakeList[SNAKE_HEAD]
		if  snakeHead[POS_X] > SCREEN_WIDTH - thick or snakeHead[POS_X] < 0 \
				or snakeHead[POS_Y] > SCREEN_HEIGHT - thick or snakeHead[POS_Y] < 0:
			self.createEvent(CRASH_WALL, snake = snake)
			func()

	def crashItem(self, snake, itemGroup):
		thick = snake.getThick()
		snakeList = snake.getSnakeList()
		snakeHead = snakeList[SNAKE_HEAD]
		for item in itemGroup.sprites():
			itemSize = item.getSize()
			itemLocation = item.getLocation()
			if snakeHead[POS_X] >= itemLocation[POS_X] and snakeHead[POS_X] <= itemLocation[POS_X] + itemSize[POS_X] \
					or snakeHead[POS_X] + thick >= itemLocation[POS_X] and snakeHead[POS_X] + thick <= itemLocation[POS_X] + itemSize[POS_X]:
				if snakeHead[POS_Y] >= itemLocation[POS_Y] and snakeHead[POS_Y] <= itemLocation[POS_Y] + itemSize[POS_Y] \
						or snakeHead[POS_Y] + thick >= itemLocation[POS_Y] and snakeHead[POS_Y] + thick <= itemLocation[POS_Y] + itemSize[POS_Y]:
					self.createEvent(CRASH_ITEM, snake = snake, item = item)


	def crashItself(self):
		pass
	def crashOtherSnake(self):
		pass