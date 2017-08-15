from itertools import count

class Player(object):
    _ids = count(1)

    def __init__(self):
        self._id = next(self._ids)
        self.snake = None
        self.snakeAction = None
        self.snakeDisplayHandler = None
        self.snakeEventCreator = None
        self.levelHandler = None
        self.score = None

    def setSnake(self, snake):
        self.snake = snake
    def getSnake(self):
        return self.snake

    def setSnakeAction(self, snakeAction):
        self.snakeAction = snakeAction
    def getSnakeAction(self):
        return self.snakeAction

    def setSnakeDisplayHandler(self, snakeDisplayHandler):
        self.snakeDisplayHandler = snakeDisplayHandler
    def getSnakeDisplayHandler(self):
        return self.snakeDisplayHandler

    def setSnakeEventCreator(self, snakeEventCreator):
        self.snakeEventCreator = snakeEventCreator
    def getSnakeEventCreator(self):
        return self.snakeEventCreator

    def setLevelHandler(self, levelHandler):
        self.levelHandler = levelHandler
    def getLevelHandler(self):
        return self.levelHandler

    def setScore(self, score):
        self.score = score
    def getScore(self):
        return self.score
