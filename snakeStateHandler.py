from observer import Observer
from setting import *

class SnakeStateHandler(Observer):
	def __init__(self, Snake):
		self.snake = Snake
		self.snake.attach(self)
		self.snakeList = self.snake.getSnakeList()
		self.length = self.snake.getLength()

	def observeUpdate(self):
		self.snakeList = self.snake.getSnakeList()
		self.length = self.snake.getLength()

	def commit(self):
		self.snake.setSnakeList(self.snakeList)

	def move(self, newHeadPos, direction):
		self.snakeList.append((newHeadPos[POS_X],newHeadPos[POS_Y],direction))
		if len(self.snakeList) > self.length:
			del self.snakeList[0]
		self.commit()