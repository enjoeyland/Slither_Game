import threading

from event.event import EventCreator
from utils.setting import SNAKE_HEAD, POS_X, SCREEN_WIDTH, SCREEN_HEIGHT, POS_Y, CRASH_WALL, CRASH_ITEM, CRASH_ITSELF, \
	FRAMES_PER_SECOND


class SnakeEventCreator(EventCreator):
	def __init__(self):
		pass
	def crashWall(self, snake, func):
		thick = snake.getThick()
		snakeList = snake.getSnakeList()
		snakeHead = snakeList[SNAKE_HEAD]
		if  snakeHead[POS_X] > SCREEN_WIDTH - thick or snakeHead[POS_X] < 0 \
				or snakeHead[POS_Y] > SCREEN_HEIGHT - thick or snakeHead[POS_Y] < 0:
			print("crash wall")
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


	def crashItself(self, snake, func):
		snakeList = snake.snakeList
		snakeThick = snake.thick
		snakeSpeed = snake.speed
		snakeHead = snakeList[SNAKE_HEAD]
		tick = snake.thick
		for eachSegment in snakeList[ : -1 - int(2 * snakeThick / (snakeSpeed / FRAMES_PER_SECOND))]:
			if eachSegment[POS_X] <= snakeHead[POS_X] and  eachSegment[POS_X] + tick > snakeHead[POS_X]\
					and eachSegment[POS_Y] <= snakeHead[POS_Y] and eachSegment[POS_Y] + tick > snakeHead[POS_Y]:
				print("crash itself")
				self.createEvent(CRASH_ITSELF, snake = snake)
				func()

	def crashOtherSnake(self):
		pass