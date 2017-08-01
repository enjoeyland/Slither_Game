from event.eventCreators.eventCreator import EventCreator
from utils.listener import Request
from utils.setting import SNAKE_HEAD, POS_X, SCREEN_WIDTH, SCREEN_HEIGHT, POS_Y, CRASH_WALL, CRASH_ITEM, CRASH_ITSELF, \
	FRAMES_PER_SECOND


class SnakeEventCreator(EventCreator):
	def __init__(self, snake, itemGroup):
		self.snake = snake
		self.snake.listen(Request("SnakeEventCreator",self.checkingProcess))

		self.snake_thick = self.snake.getThick()
		self.snake_speed = self.snake.getSpeed()
		self.snake_snakeList = self.snake.getSnakeList()
		self.snake_snakeHead = self.snake_snakeList[SNAKE_HEAD]

		self.itemGroup = itemGroup

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
		if  self.snake_snakeHead[POS_X] > SCREEN_WIDTH - self.snake_thick or self.snake_snakeHead[POS_X] < 0 \
				or self.snake_snakeHead[POS_Y] > SCREEN_HEIGHT - self.snake_thick or self.snake_snakeHead[POS_Y] < 0:
			print(self.snake_snakeHead)
			print("crash wall")
			self.createEvent(CRASH_WALL, snake = self.snake)

	def crashItem(self):
		for item in self.itemGroup.sprites():
			itemSize = item.getSize()
			itemLocation = item.getLocation()
			if self.snake_snakeHead[POS_X] >= itemLocation[POS_X] and self.snake_snakeHead[POS_X] <= itemLocation[POS_X] + itemSize[POS_X] \
					or self.snake_snakeHead[POS_X] + self.snake_thick >= itemLocation[POS_X] and self.snake_snakeHead[POS_X] + self.snake_thick <= itemLocation[POS_X] + itemSize[POS_X]:
				if self.snake_snakeHead[POS_Y] >= itemLocation[POS_Y] and self.snake_snakeHead[POS_Y] <= itemLocation[POS_Y] + itemSize[POS_Y] \
						or self.snake_snakeHead[POS_Y] + self.snake_thick >= itemLocation[POS_Y] and self.snake_snakeHead[POS_Y] + self.snake_thick <= itemLocation[POS_Y] + itemSize[POS_Y]:
					self.createEvent(CRASH_ITEM, snake = self.snake, item = item)


	def crashItself(self):
		for eachSegment in self.snake_snakeList[ : - int(3 * self.snake_thick / (self.snake_speed / FRAMES_PER_SECOND))]:
			if eachSegment[POS_X] <= self.snake_snakeHead[POS_X] and  eachSegment[POS_X] + self.snake_thick > self.snake_snakeHead[POS_X]\
					and eachSegment[POS_Y] <= self.snake_snakeHead[POS_Y] and eachSegment[POS_Y] + self.snake_thick > self.snake_snakeHead[POS_Y]:
				print("crash itself")
				self.createEvent(CRASH_ITSELF, snake = self.snake)


	def crashOtherSnake(self):
		pass