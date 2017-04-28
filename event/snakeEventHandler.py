import threading

from event.event import Event
from utils.setting import *


class SnakeEventHandler(Event, threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.wallListenerBuffer = {}
		self.wallListenDic = {}
		self.__suspend = False
		self.__exit = False
		# pygame.event.Event(pygame.USEREVNT,  )

	def crashWall(self, snake, func):
		thick = snake.getThick()
		snakeList = snake.getSnakeList()
		snakeHead = snakeList[SNAKE_HEAD]
		if  snakeHead[POS_X] > SCREEN_WIDTH - thick or snakeHead[POS_X] < 0 \
				or snakeHead[POS_Y] > SCREEN_HEIGHT - thick or snakeHead[POS_Y] < 0:
			func()

	def crashItem(self, snake, item, func):
		thick = snake.getThick()
		snakeList = snake.getSnakeList()
		snakeHead = snakeList[SNAKE_HEAD]
		itemSize = item.size()
		itemPos = item.positon()
		if snakeHead[POS_X] > itemPos[POS_X] and snakeHead[POS_X] < itemPos[POS_X] + itemSize \
				or snakeHead[POS_X] + thick > itemPos[POS_X] and snakeHead[POS_X] + thick < itemPos[POS_X] + itemSize:
			if snakeHead[POS_Y] > itemPos[POS_Y] and snakeHead[POS_Y] < itemPos[POS_Y] + itemSize \
					or snakeHead[POS_Y] + thick > itemPos[POS_Y] and snakeHead[POS_Y] + thick < itemPos[POS_Y] + itemSize:
				item.effect()
				func()

	def crashItself(self):
		pass
	def crashOtherSnake(self):
		pass