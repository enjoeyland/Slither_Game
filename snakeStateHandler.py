class SnakeStateHandler(Observer):
	def __init__(self, snake):
		snake.attach(self)
		self.snakeState = snake.getState()
	def observeUpdate(self):
		self.snakeState = snake.getState()
	def commit(self):
		snake.setState(self.snakeState)
	def move(self, newHeadPos, direction):
		self.snakeState["snakeList"].append((newHeadPos[POS_X],newHeadPos[POS_Y],direction))
		if len(self.snakeState["snakeList"]) > self.snakeState["length"]:
			del self.snakeState["snakeList"][0]
		self.commit()